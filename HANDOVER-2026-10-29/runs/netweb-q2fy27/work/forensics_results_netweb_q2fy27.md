# A3 FORENSIC NOTES: NETWEB Q2 FY27, doctype RESULTS (Reg 33 standalone filing, board 24-Oct-2026)

Inputs read: A1 structured (R001-R429), A1 fulltext (383 lines), A2 ledger with ORCHESTRATOR ADDENDUM, Notion checklist 2026-10-26 (memory, not evidence). Source PDF and inputs/ not opened. Units INR million unless stated (x0.1 = Rs Cr). Line numbers = A1 fulltext lines.

## 0. LEDGER RECONCILIATION
- Ledger IDs accounted: 429 of 429 (R001-R428 plus R429 = MISSING-1, per addendum). Each structured row was read at its cited fulltext line. Reconciled 100%.
- Addendum applied: R428 conclusion time 2:40 PM (L63), R351 signatory Lohit Chhabra (L72), R429 Annexure II item 3 (L356).
- A1 line-cite drift (value correct, line off): R330, R331, R332 cite L312; the text sits at L313 ("issue price of INR 4,790 per share, comprising a share premium of INR 4,788 per share, aggregating to INR 12,000.00 million"). R345 cites L350; "100%" sits at L374. No value error. Downstream cites in this report use the true lines.
- Mechanical tie-outs run (all pass unless listed in findings): balance sheet casts both dates; P&L quarter columns cast; cash flow A+B+C = (321.94) and closes to BS cash 3,333.28; borrowings change +496.39 = CF 497.00 - 0.61; other bank balances change +5,672.83 = net FD flow 4,737.13 + monitoring line 935.70; DTA change +27.06 = P&L deferred credit 28.08 - OCI tax 1.03 (0.01 rounding); EPS recomputed on day-weighted shares (Q2 58.056m shares, 23.54; H1 57.501m, 38.60; Q1 56.94m, 14.98); other equity roll-forward ties to 0.00 (see F11). One failure: H1 other income and other expenses do not add from the quarters (A3-13).

## 1. FINDINGS TABLE
| id | check | ledger row ref | line | short verbatim quote | classification | forward implication |
|---|---|---|---|---|---|---|
| A3-01 | F1 | R162-R163 | L205 | "(i) Investments \| - \| -" | FORWARD-SIGNAL | Non-current investments are nil at both dates. The Taiwan WOS share subscription "will be in cash" (L367) and populates this line first. The first non-zero print marks the capital outflow and the start of consolidated reporting. |
| A3-02 | F1 | R067-R072 | L172 | "IV Exceptional items (net) \| - \| - \| - \| - \| - \| -" | NEUTRAL-FACT | Template line, nil in all six periods. It is the slot a future inventory write-down or a QIP-related one-off would use. Watch it while inventory sits at 19,306.91. |
| A3-03 | F8 | R085-R090 | L176 | "Adjustment of tax relating to earlier period \| - \| - \| - \| - \| - \| (0.68)" | NEUTRAL-FACT | Non-zero only in audited FY26: a 0.68 credit, 2 bps of FY26 PBT 2,765.20. Nil in Q1, Q2 and H1 FY27. No ETR distortion. |
| A3-05 | F9 | R109-R114 | L182 | "Re-measurement gains / (losses) on defined benefit plans \| 2.96 \| 1.15 \| 1.78 \| 4.11 \| 2.94 \| 0.52" | NEUTRAL-FACT | The Q2 gain of 2.96 exceeds the full-year FY26 figure of 0.52 (H2 FY26 implied loss 2.42). Pattern is H1 gains and a year-end reversal. Immaterial (0.2% of Q2 PAT). Verify discount-rate assumptions at the FY27 AR. |
| A3-06 | F10 | R134, R137, R138 | L186 | "Paid up equity share capital ... \| 118.89 \| 113.88 \| 113.31 \| 118.89 \| 113.31 \| 113.88" | AMBIGUOUS | Share capital rose 0.57 (about 2.85 lakh shares at INR 2) between 30-Sep-2025 and 31-Mar-2026. No note in this filing traces it. Notion memory dates an ESOP allotment of 2.87 lakh shares to May-26, but the 30-Jun-2026 column still reads 113.88. A4 to reconcile the allotment date. The QIP step (+5.01 = 25,05,219 x INR 2) traces to Note 3. Basic = diluted in all six periods: spread zero. |
| A3-07 | F12 | R172-R173, R025, R260 | L211, L165, L271 | "(a) Inventories \| 19,306.91 \| 8,048.44"; "(6,100.89)" | FORWARD-SIGNAL | Inventory rose 139.9% in six months (+11,258.47, equal to CF L271). Q2 alone built 6,100.89 of FG/WIP, 46.1% of Q2 revenue. H2 revenue depends on delivering this stock. A slip moves the cost into carrying cost and write-down risk (A3-02 slot). Question: which orders and delivery dates the FG/WIP maps to. |
| A3-08 | F12 | R037-R039, R204-R205, R210-R211 | L167, L234, L238 | "Finance costs \| 238.00 \| 115.24 \| 9.30"; "(i) Borrowings \| 3,204.77 \| 2,707.71" | FORWARD-SIGNAL | Finance cost rose 106.5% QoQ. Period-end total borrowings rose only 18.3% (2,716.71 to 3,213.10). Q2 annualised finance cost 952.00 is 29.6% of closing debt. So the funding that carries the cost is not visible at the balance-sheet date: intra-quarter peak borrowing, LC/bill discounting, or interest-bearing supplier credit inside non-MSME payables (+4,584.68 to 12,181.37) [INFERENCE]. The run-rate persists while the inventory build persists. Question: the instruments behind finance cost and the peak intra-quarter debt. |
| A3-09 | F12 | R214-R215, R262 | L240, L272 | "(b) Other current liabilities \| 2,747.62 \| 4,405.44"; "(1,664.46)" | AMBIGUOUS | Other current liabilities fell 37.6% (1,657.82). The reading splits two ways: customer advances consumed as orders deliver (WC unwinding), or advances not replaced by new orders. Single segment, so entity BS = segment BS. Question: contract-liability balance and new advances received in H1. |
| A3-10 | F12 | R242-R245, R174-R175 | L261, L262, L213 | "Provision for doubtful debts \| 38.26 \| 1.86"; "Bad debts written Off \| 15.05 \| 1.71" | AMBIGUOUS | Credit charges 53.31 in H1 FY27 vs 3.57 in H1 FY26 (14.9x). Receivables grew only 17.1% (6,699.55 to 7,843.73). Lean bear: a named-customer credit event, or an ECL model step-up. DTA growth 8.28 to 35.34 (L207) is consistent with disallowed provisions [INFERENCE]. Question: which customers, and whether the write-off is one account. |
| A3-12 | F13 | R368, R369, R374, R429 | L54-55, L371, L356 | "The proposal to incorporate a wholly owned subsidiary in Taiwan. The incorporation process has not yet been initiated"; "To be determined" | FORWARD-SIGNAL | The only non-results agenda item is an overseas capital commitment with no stated size, date or purpose beyond "Same industry in which we operate" (L356). No AR, AGM, dividend, director or auditor item. Question: purpose (supply-chain or partner proximity is a guess, not evidence), capital to be subscribed, timeline. |
| A3-13 | F14 | R007-R010, R049-R052, R013-R016, R055-R058 | L161, L169 | "Other income \| 128.62 \| 84.72 \| 9.24 \| 161.13"; "Other expenses \| 352.78 \| 282.47 \| 187.08 \| 583.04" | AMBIGUOUS | Q1 + Q2 other income = 213.34, but H1 shows 161.13. Q1 + Q2 other expenses = 635.25, but H1 shows 583.04. Both gaps are 52.21; H1 PBT still adds (2,967.87). The likely cause is a net forex item shown gross in a quarter and netted in the half (CF L259 unrealised forex (56.38)) [INFERENCE]. Effect: one quarter's other income or other expenses carries 52.21 that the half-year nets away, so quarterly operating margin reads are uncertain by up to 0.39% of Q2 revenue. Question: nature of the 52.21 and the quarter it sits in. |
| A3-14 | F14 | R298-R301, R334-R335 | L292, L293, L314-315 | "Proceeds in monitoring account \| (935.70)"; "Dividends paid \| (170.82)" | AMBIGUOUS | The financing outflow of 935.70 into the monitoring account exceeds the disclosed QIP balances (monitoring 587.88 + escrow 177.00 = 764.88) by 170.82. That residual equals dividends paid to the paisa. It may be coincidence, or a dividend earmarked account routed through the same line. If routed, the dividend flow may be counted twice with an offset elsewhere. The label "Proceeds" sits on an outflow. Question: line breakdown and opening earmarked balances. |
| A3-15 | F6 | R423, R333-R335, R304, R274 | L314-315, L295, L278 | "...Escrow account balance amounting to INR 177.00 million relating to QIP proceeds."; "11,755.76" | AMBIGUOUS | Note 3 locates 4,264.88 of QIP money (FD 3,500.00, monitoring 587.88, escrow 177.00). Net proceeds were 11,755.76 (gross 12,000.00; issue expenses 244.24, 2.04%). 7,490.88 (63.7%) is not located in the filing. H1 CFO of (6,391.48) implies working-capital use [INFERENCE]. The 7-page filing carries no objects-of-issue text and no Reg 32 deviation statement (usually filed with results; it may have been filed separately) [INFERENCE, verify]. Notion memory states Rs 767 Cr spent on WC; the filing gives Rs 749.1 Cr off net proceeds or Rs 773.5 Cr off gross. Neither matches. Question: objects, deployment to date, monitoring agency report date. |
| A3-16 | F15 | R367, R350, R376, R345 | L350, L352-354, L374 | "Country of Incorporation: Taiwan"; "will be incorporated as a wholly owned subsidiary"; "100%" | FORWARD-SIGNAL | First proposed subsidiary. Today the filing is standalone only, with no consolidation list. From the quarter of incorporation the company must file consolidated results [INFERENCE: Reg 33]. F2, F3 and F4 become live then. No prior entity list exists to diff (no prior NETWEB run). |
| A3-17 | F14 | R428, R316, R383, R395 | L63, L146, L332 | "commenced at 11:45 A.M and concluded at 2:40 PM [handwritten, read from image]" | NEUTRAL-FACT | The conclusion time was filled by hand on a pre-typed letter. The meeting ran 2h55m on a Saturday. Auditor report (L146) and MD sign-off (L332) are both dated 24-Oct-2026 with no time stamp, so within-day sign order cannot be tested. Date sequence is consistent. |

(ID A3-04 and A3-11 not used: the deferred-tax swing was folded into the F8 basis and the payables evidence into A3-08.)

## 2. CHECKLIST SCORECARD
| check | status | basis |
|---|---|---|
| F1 | FINDING | 18 ZERO_STANDING cells over 8 lines. Investments nil at both dates (A3-01, Taiwan WOS fills it). Exceptional items nil in all six periods (A3-02). Partial-dash CF lines (loss on discard L264, profit on sale L265, sale proceeds L281, IPO expense recovery L294, share issue L295) are ordinary one-half events: the IPO recovery ends, the QIP lands. |
| F2 | N.A. | Standalone filing only. No consolidated columns, no subsidiaries (investments nil, L205). Live from the Taiwan WOS incorporation quarter (A3-16). |
| F3 | N.A. | No consolidated cost lines to compare. No going concern EoM. |
| F4 | PASS | Review scope covers the whole Company Statement (L96-98). No Other Matter, no component or management-certified numbers. Unreviewed contribution = 0.00, 0% of PAT. |
| F5 | PASS | Unmodified SRE 2410 conclusion (L118-124). No EoM, Other Matter or going concern text. The verbatim diff against Q1 FY27 did not run: there is no prior-quarter extract, and the Notion file does not carry the Q1 auditor paragraph. The PASS covers this quarter only; the prior-quarter text is NOT FOUND. |
| F6 | FINDING | Lexicon hits: "will be" (L352, L367), "initiated" (L55, "not yet been initiated"), "commenc" (L63, meeting time only, boilerplate), "approved" (L47, L312). Off-lexicon dateable: "will vest" (L316), "To be incorporated" (L349), "To be determined" (L371). Commitment register below. QIP deployment gap A3-15. |
| F7 | PASS | Zero hits in notes for the hedge lexicon ("subject to", "evaluating", "exploring", "in discussions", "endeavour", "no assurance", "may sometimes", "could have an effect"). The Reg 30 qualifiers on the Taiwan WOS ("not available as on date" L56, "to the extent applicable and available" L59, "if required" L364) are disclosure scope language, carried under A3-12. No new hedge on revenue lumpiness or concentration. |
| F8 | FINDING | ETR: Q2 FY27 25.18%, Q1 FY27 25.25%, Q2 FY26 25.21%, H1 FY27 25.21%, H1 FY26 25.97%, FY26 25.57%, all at or near the 25.17% statutory rate. Deferred tax: Q1 credit (35.94) = 315 bps shield, Q2 charge 7.86 = 43 bps reversal, H1 net credit (28.08) = 95 bps. Not a persistent credit pattern; it reads as timing differences (current tax 28.39% in Q1, 24.75% in Q2). DTA 8.28 to 35.34 ties to the P&L and OCI. Earlier-year tax adjustment non-zero in FY26 only (A3-03). |
| F9 | FINDING | A single-quarter OCI gain (Q2 2.96) exceeds the full prior year (0.52). Immaterial (A3-05). Verify assumptions at the FY27 AR. |
| F10 | FINDING | QIP step +5.01 traces to Note 3. The FY26 step +0.57 has no trace in this filing and conflicts with the Notion memory date (A3-06). Basic-diluted spread 0.00 in every period; 4,935 unvested ESOPs (L316) are 0.008% of 59.445m shares. |
| F11 | PASS | 118.89 + 20,922.52 = 21,041.41 (L221-223); 113.88 + 7,119.10 = 7,232.98. Roll-forward: 7,119.10 + TCI 2,222.87 + QIP premium net of expenses 11,750.75 (11,755.76 - 5.01) + ESOP 0.62 - dividend 170.82 = 20,922.52, difference 0.00. No third-party net worth number in context. R139 single column is the Reg 33 format. |
| F12 | FINDING | One segment, "Computer servers" (L308), so entity BS = segment BS. Total assets +80.3% (22,549.28 to 40,667.66), equity-funded by QIP and supplier credit. Findings: inventory build (A3-07), finance cost vs debt (A3-08), other current liabilities down 37.6% (A3-09), credit charges up 14.9x (A3-10). |
| F13 | FINDING | Two agenda items only (L49, L54). No AR, Board's Report, AGM, record date, dividend, enabling resolution, director or auditor item. Taiwan WOS approval with size and date TBD (A3-12). No director term dates to map. |
| F14 | FINDING | H1 non-additivity of 52.21 in other income and other expenses (A3-13). Monitoring-account residual equals dividends paid (A3-14). Handwritten conclusion time (A3-17). Clean items: Note 1 "limited review" (L307) matches the auditor's SRE 2410 review (L110-116); Saturday 24-Oct-2026 is correct; the entity name is the same across all pages. The ICAI registration "000756N/N50044 1" (L130) is an OCR spacing artifact, not a drafting error. |
| F15 | FINDING | No consolidation list (standalone). One proposed addition: Taiwan WOS (A3-16). No prior list to diff. |
| F16 | N.A. | Presentation-only check; doctype is results. |
| F17 | N.A. | Concall-only check; doctype is results. The Notion checklist was read; items #2, #3, #6 and #9 (CCC, Blackwell execution, concentration, new orders) are not addressed by a Reg 33 filing by design. They pass to the concall run. |

## 3. COMMITMENT REGISTER (F6)
| commitment | implied date | note / line ref | status word |
|---|---|---|---|
| Incorporate a wholly owned subsidiary in Taiwan | Undated ("Date: To be incorporated") | Board outcome item 2, L54-55; Annexure II L349 | not yet initiated (pre-initiation) |
| Subscribe Taiwan WOS share capital in cash; cost to be determined; 100% holding | Undated | Annexure II L367, L371, L374 | not yet initiated |
| Obtain competent-authority approval for incorporation, if required | Undated | Annexure II L363-364 | not yet initiated |
| Vest 4,935 ESOPs granted 18-Jan-2025 over 1-2 years | Window 18-Jan-2026 to 18-Jan-2027 [my arithmetic] | Note 4, L316-317 | underway |
| QIP of INR 12,000.00m: approve (Board 1-Jul, postal ballot 1-Aug), open (17-Aug), allot (20-Aug-2026) | 20-Aug-2026 | Note 3, L309-313 | completed |
| Deploy QIP proceeds; 4,264.88 parked at 30-Sep-2026, use of the rest not stated | Undated | Note 3, L314-315 | underway [INFERENCE from parking balances] |

## 4. ITEMS FOR A4 (FORWARD-SIGNAL and AMBIGUOUS, convert to management questions)
- A3-01, A3-12, A3-16: Taiwan WOS purpose, capital, timeline, first consolidated quarter.
- A3-07: FG/WIP 6,100.89 built in Q2. Map it to named orders and delivery quarters.
- A3-08: Finance cost 238.00 on 3,213.10 closing debt. Name the instruments and the peak intra-quarter debt.
- A3-09: Other current liabilities down 1,657.82. Customer advances consumed or not replaced?
- A3-10: Credit charges 53.31. Which customers, and is it one account?
- A3-13: The 52.21 H1 netting in other income and other expenses.
- A3-14: The 935.70 monitoring-account line breakdown vs the 170.82 dividend.
- A3-15: QIP objects, deployment to date, Reg 32 statement and monitoring agency report.
- A3-06: The FY26 share-capital step +0.57 vs the Notion "May-26 ESOP allotment" date.

```yaml
stage: A3-forensics
company: "NETWEB"
quarter: "q2fy27"
doctype: "results"
model: "claude-opus-5-5"
status: complete
forensics_path: "C:/Users/SUMIT SHARMA/repos/inflection-pipeline/.claude/worktrees/qr-netweb-q2fy27-a60c5c/runs/netweb-q2fy27/work/forensics_results_netweb_q2fy27.md"
ledger_reconciled_pct: 100
checklist:
  F1: FINDING
  F2: N.A.
  F3: N.A.
  F4: PASS
  F5: PASS
  F6: FINDING
  F7: PASS
  F8: FINDING
  F9: FINDING
  F10: FINDING
  F11: PASS
  F12: FINDING
  F13: FINDING
  F14: FINDING
  F15: FINDING
  F16: N.A.
  F17: N.A.
findings:
  - {id: "A3-01", check: "F1", line: "L205", classification: "FORWARD-SIGNAL", implication: "Non-current investments nil at both dates; Taiwan WOS cash subscription populates it first and marks the consolidation start"}
  - {id: "A3-02", check: "F1", line: "L172", classification: "NEUTRAL-FACT", implication: "Exceptional items nil in all six periods; the slot a future inventory write-down would use"}
  - {id: "A3-03", check: "F8", line: "L176", classification: "NEUTRAL-FACT", implication: "Earlier-year tax adjustment (0.68) in FY26 only, 2 bps of FY26 PBT; nil in FY27 periods"}
  - {id: "A3-05", check: "F9", line: "L182", classification: "NEUTRAL-FACT", implication: "Q2 actuarial gain 2.96 exceeds FY26 full year 0.52; immaterial; verify assumptions at FY27 AR"}
  - {id: "A3-06", check: "F10", line: "L186", classification: "AMBIGUOUS", implication: "Share capital +0.57 between Sep-25 and Mar-26 untraced in this filing; conflicts with Notion May-26 ESOP allotment date; basic-diluted spread zero"}
  - {id: "A3-07", check: "F12", line: "L211, L165, L271", classification: "FORWARD-SIGNAL", implication: "Inventory +139.9% to 19,306.91; Q2 FG/WIP build 6,100.89 = 46.1% of Q2 revenue; H2 revenue rests on delivering it"}
  - {id: "A3-08", check: "F12", line: "L167, L234, L238", classification: "FORWARD-SIGNAL", implication: "Finance cost +106.5% QoQ to 238.00 vs closing debt +18.3%; annualised 29.6% of closing debt implies funding not visible at period end"}
  - {id: "A3-09", check: "F12", line: "L240, L272", classification: "AMBIGUOUS", implication: "Other current liabilities -37.6% (1,657.82); advances consumed vs not replaced"}
  - {id: "A3-10", check: "F12", line: "L261, L262", classification: "AMBIGUOUS", implication: "Doubtful-debt provision plus write-off 53.31 vs 3.57 (14.9x) on receivables +17.1%; lean bear, name the customers"}
  - {id: "A3-12", check: "F13", line: "L54-55, L371, L356", classification: "FORWARD-SIGNAL", implication: "Taiwan WOS approved with cost, date and purpose undetermined; overseas capital commitment"}
  - {id: "A3-13", check: "F14", line: "L161, L169", classification: "AMBIGUOUS", implication: "Q1+Q2 other income and other expenses each exceed H1 by 52.21; PBT adds; quarterly margin read uncertain"}
  - {id: "A3-14", check: "F14", line: "L292, L293, L314-315", classification: "AMBIGUOUS", implication: "Monitoring-account outflow 935.70 minus disclosed QIP balances 764.88 = 170.82 = dividends paid exactly; possible routing or double count"}
  - {id: "A3-15", check: "F6", line: "L314-315, L295, L278", classification: "AMBIGUOUS", implication: "Only 4,264.88 of 11,755.76 net QIP proceeds located; 7,490.88 (63.7%) use not stated; no objects or Reg 32 statement in the filing"}
  - {id: "A3-16", check: "F15", line: "L350, L352-354, L374", classification: "FORWARD-SIGNAL", implication: "First subsidiary proposed; consolidated reporting from incorporation quarter; F2-F4 go live"}
  - {id: "A3-17", check: "F14", line: "L63, L146, L332", classification: "NEUTRAL-FACT", implication: "Handwritten conclusion time 2:40 PM; same-day sign-offs without time stamps; intra-day order untestable"}
forward_signals: ["A3-01", "A3-07", "A3-08", "A3-12", "A3-16"]
ambiguous: ["A3-06", "A3-09", "A3-10", "A3-13", "A3-14", "A3-15"]
commitments:
  - {commitment: "Incorporate wholly owned subsidiary in Taiwan", implied_date: "undated (To be incorporated)", ref: "Board outcome item 2 L54-55; Annexure II L349", status_word: "not yet initiated"}
  - {commitment: "Subscribe Taiwan WOS capital in cash, cost TBD, 100% holding", implied_date: "undated", ref: "Annexure II L367, L371, L374", status_word: "not yet initiated"}
  - {commitment: "Competent-authority approval for Taiwan incorporation, if required", implied_date: "undated", ref: "Annexure II L363-364", status_word: "not yet initiated"}
  - {commitment: "Vest 4,935 ESOPs granted 18-Jan-2025 over 1-2 years", implied_date: "18-Jan-2026 to 18-Jan-2027", ref: "Note 4 L316-317", status_word: "underway"}
  - {commitment: "QIP INR 12,000.00m raised and allotted", implied_date: "2026-08-20", ref: "Note 3 L309-313", status_word: "completed"}
  - {commitment: "Deploy QIP proceeds; 4,264.88 parked at 30-Sep-2026", implied_date: "undated", ref: "Note 3 L314-315", status_word: "underway"}
gate_a3: pass
blank_checks: []
analyst_note: "The statements tie internally. The BS casts, the CF closes to BS cash, borrowings and other bank balances, and other equity rolls forward to 0.00 (7,119.10 + TCI 2,222.87 + net premium 11,750.75 + ESOP 0.62 - dividend 170.82 = 20,922.52). The forward risk is in working capital, not accounting. QIP cash, supplier credit (non-MSME payables +4,584.68) and costlier funding paid for an 11,258.47 inventory build; H1 CFO was (6,391.48). Finance cost doubled QoQ while closing debt rose 18%. Some funding is not visible at the balance-sheet date, and that cost persists until the stock ships. Two presentation items need management answers: the 52.21 H1 netting in other income and other expenses, and the 935.70 monitoring-account outflow whose residual over disclosed QIP balances equals dividends paid to the paisa (this may be coincidence). The Taiwan WOS makes NETWEB a consolidated filer from incorporation, and F2-F4 go live then. The prior-quarter auditor verbatim diff did not run (no prior extract). A1 line cites drift for R330-R332 (true L313) and R345 (true L374); the values are correct."
```
