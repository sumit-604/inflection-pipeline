# FORENSICS AYE Q2 FY27 (doctype: results) - A3

Source index: runs/aye-q2fy27/extracted/aye-results-q2fy27-structured.md (R001-R755)
Fulltext: runs/aye-q2fy27/extracted/aye-results-q2fy27-fulltext.md (line numbers below = this file)
Ledger: runs/aye-q2fy27/work/ledger_results_aye_q2fy27.md
Prior quarter: runs/aye-q2fy27/work/prior_q1fy27_results_fulltext.md (cited "prior L###", the embedded 5-digit line number; Q1 FY27 filing 22-Jul-2026, auditor S S Kothari Mehta)
Monitoring checklist: runs/aye-q2fy27/work/monitoring_checklist_AYE.md
Model: claude-opus-5-5. Source PDF and inputs/ not opened.

Lender variants applied (NBFC-ML, Note 1 line 479):
- F4: the share of PAT that rests on unreviewed components, plus the assurance level of each report.
- F5: verbatim diff of the limited review report (LRR) and the security cover / covenant report against Q1.
- F12: Note 6 (line 588) states one segment. The lender variant therefore runs on asset quality, provisioning, direct assignment (DA), co-lending, liquidity and NCD security cover.

## 1. LEDGER RECONCILIATION

| Item | Count | Result |
|---|---|---|
| Structured rows in ledger (R001-R755) | 755 | 755 read at cited fulltext line (100%) |
| MISSING_FROM_STRUCTURED rows (M01-M05) | 5 | read at lines 69, 183, 267, 465, 746 |
| Signature timestamps A2 did not list | 2 | line 980 (auditor, security cover report, 11:09:12); line 1438 (CS, Reg 52(7) letter, 11:39:14) |
| Orphan IDs | 0 | none |

Cell resolutions by cross-foot (no estimate; arithmetic on printed totals only):
- R089 (Q1 FY27 derecognition gain, blank): nil. 452.67 + 19.56 + 5.14 = 477.37 = R097. Prior Note 5(a) (prior L220) confirms no Q1 assignment.
- R248 (OCR "0-64)", line 371): (9.64). The H1 FY27 adjustments foot to R274 637.51 only at (9.64).
- R311 / R313 (H1 FY26 financing blanks): nil. The other H1 FY26 rows foot to R327 427.62.

Pipeline error for the orchestrator: ledger line 28 says "No signature timestamp precedes the results approval (11:21)". That is wrong. At fulltext line 980 the auditor signs the security cover report at 11:09:12. That is before the board met at 11:15 (line 43). See A3-18.

Signature timeline (all 21-Oct-2026, IST): auditor security cover report 11:09:12 (line 980). Board start 11:15 (line 43). Results approved 11:21 (line 45). MD balance sheet 11:21:52 (line 267). MD cash flow 11:22:37 (line 465). Auditor LRR 11:24:32 (lines 183-184). CS outcome letter 11:36:53 (line 69). CS security cover letter 11:38:21 (line 746). CS Reg 52(7) letter 11:39:14 (line 1438).

## 2. FINDINGS TABLE

| id | check | ledger row ref | line | short verbatim quote | classification | forward implication |
|---|---|---|---|---|---|---|
| A3-01 | F1 | R120, R121, R123, R200, R202, R203, R206, R208, R209, R246 | 303, 328, 370 | line 303: "-            -                   18.66               -"; line 328: "Cash flow hedge reserve" | AMBIGUOUS | "Net loss on fair value changes" is a dash for Q2, Q1 and H1 FY27. It was 66.77 in FY26 (R125). The cash flow hedge reserve line is nil for all of FY26 and opens in FY27 (Q1 (3.93), Q2 4.68). The cross currency swap fair value line was (31.41) in H1 FY26 and is a dash in H1 FY27. Reading: hedge accounting was designated from FY27, so derivative mark-to-market now goes to OCI, not PAT. This weakens PAT comparability with FY26. Ask for the designation date and the hedged items. |
| A3-02 | F1 | R254, R255 | 373-374 | "Provision on investment" (dash both periods) | AMBIGUOUS | The template has an impairment line for investments, and it is nil. The company holds Arcil security receipts in four trusts (lines 560-567), and investments rose from 158.14 to 222.96 (line 220). This line activates if SR recoveries miss. Ask for the SR carrying value and the provision held against SRs. |
| A3-03 | F5 | R739, R740, R411, R749, R617 | 932-934, 950-951, 1276-1286; prior L575-576, L910-920 | "in breach of the required financial covenant of (PAR 90 + Write off)/Gross Loan Portfolio"; "except for paragraph 12" | FORWARD-SIGNAL | This is the second quarter in a row with the same ISIN (INE501X07588), clause 10.3(a) and reason text. Q1 auditor: "except for as reported in Annexure 2" (prior L576). The new auditor moves the breach into a body Observation (para 12) and qualifies its conclusion. The cause text still reads "Increase in write-offs in this financial year due to higher delinquencies" (lines 1276-1280). The ISIN matures 17-NOV-26 (line 1282), Rs 55.22 cr (R528 + R532), so the breach falls away at redemption. Other deeds use the same clause-10.3 family (line 1305 onward). Thresholds and headroom on those deeds are not disclosed. |
| A3-04 | F5 | R696, R697, R698, R699, R577 | 155-167, 169-175; prior L83-115 | "which has not been reviewed by its auditor" | NEUTRAL-FACT | The new auditor adds two Other Matter paragraphs. The Q1 LRR (prior L83-115) had none. The Trust adds 0.12 cr of Q2 PAT (0.14% of 86.72) and 0.47 cr of H1 PAT (0.29% of 161.22). This is immaterial, but the Trust links to A3-10. |
| A3-05 | F5 | R738 | prior L521-525 vs 881-928 | prior L521: "The loan assets are not assigned to a specific borrowing in the company's loan management system." | AMBIGUOUS | The Q1 auditor said charge allocation sits in Excel and compared assets with borrowings only in aggregate. The Q2 procedures (lines 886-928) drop this language. Either the control was fixed or the new auditor does not report it. Read this with A3-06 (Rs 455 cr of borrowings without security) and ask which applies. |
| A3-06 | F6 | R616, R744, R468 | 1105; prior L882 | "Rs. 455 crores for which corresponding security is not maintained due to time limit granted by the lenders" | FORWARD-SIGNAL | Q1: Rs 510 cr (prior L882). Q2: Rs 455 cr. This is the second consecutive quarter, and no creation date is given. Unencumbered loans in Column H are 1,009.48 (line 1050), so capacity exists. If security is not created when the lender time limits expire, the bank lines are at risk. Ask for the expiry dates and the lender count. |
| A3-07 | F6 | R563, R564, R752, R753 | 1471-1473 | "220   150" | FORWARD-SIGNAL | Of the 29-Jul-2026 NCD (INE501X07745), Rs 70 cr was not deployed at 30-Sep. The filing reports "Any deviation: No" (line 1491). Deployment is implied in Q3 FY27. Cash plus bank balances are already 1,341.66 (A3-14). |
| A3-08 | F6 | R613, R694 | 46 | "thereafter the Meeting is continuing for consideration of other agenda items" | AMBIGUOUS | The agenda outcome is not disclosed. Q1 used the same wording (prior L27-28). Check for a later Reg 30 outcome (KMP appointment, borrowing or NCD enabling resolutions). |
| A3-09 | F9 | R186, R187, R189, R191, R211, R215 | 318-323 | line 321: "(5.36)                                (0.44)      (0.56)" | AMBIGUOUS | Actuarial re-measurement loss: Q1 (3.45), Q2 (1.91), H1 (5.36). Each quarter is larger than the full FY26 loss of (0.56); H1 is 9.6 times it. Total OCI in Q1 (5.52) exceeds the full FY26 total of (0.42). This points to an assumption change (discount rate, attrition, salary escalation). Verify the assumptions in the FY27 Annual Report. |
| A3-10 | F10 | R064, R222, R225, R228, R231, R392, R393 | 250, 336-338 | line 250: "49.02                    48.90"; line 336: "3.51         3.02                       1.80         6.53" | AMBIGUOUS | Paid-up capital 49.02 / Rs 2 = 24.51 cr shares. The weighted basic share count implied by H1 EPS is 161.22 / 6.53 = 24.69 cr; Q2 gives 86.72 / 3.51 = 24.71 cr. The gap is 0.16 to 0.20 cr shares even at rounding limits, and the weighted count should not exceed shares outstanding. One possible link is treasury shares held by the Trust (5,04,152 transferred in H1, line 623). The capital increase of +0.12 cr matches the Trust transfer plus 3,913 allotted shares. The basic vs diluted spread is Q2 0.85% and Q1 0.66%, which is inside rounding noise. Ask for the EPS denominator and the treasury share count. |
| A3-11 | F12 | R402, R404, R250, R256, R126, R127 | 663, 673, 372, 375-376; prior L322, L334 | line 673: "62.42%"; line 372: "Impairment of financial instruments                                                    (0.55)" | AMBIGUOUS | GNPA fell from 4.49% to 4.20%, and PCR fell from 63.80% to 62.42% (-138 bps). The ECL stock fell 0.55 cr over H1 while loans grew 9.3% (6,266.44 to 6,849.85, line 218). H1 write-offs were 155.56 (R256), against 146.20 in H1 FY26. The covenant reason (line 1279) still says delinquencies are higher this financial year. Reading 1: the stage mix really improved. Reading 2: write-offs drove the GNPA fall and coverage is thinning. Gross slippage separates the two readings, and this filing does not disclose it (add-gate item i: NOT FOUND). |
| A3-12 | F12 | R363-R371 | 574-586 | line 584: "(ii) Non-Performing Loans                                                                                                                                               10.61" | FORWARD-SIGNAL | First disclosure of the co-lending book (Q1 Note 5 had no section (d)). NPL is 10.61 of 53.31 = 19.9%, against company GNPA of 4.20%. There are 39,096 cases, an average of about Rs 13,600 per case, at a 31.27% rate. Fees paid and charged are nil (lines 579-580). The ticket size and the covenant text naming "MFI Loans" (line 1284) raise a product question. Ask what the product is, whose share 53.31 represents, the ECL held, and why there are no fees. |
| A3-13 | F12 | R084, R089, R355-R359 | 290, 534-542; prior L220 | line 534: "Amount of loan accounts transferred (Rs. in crores)  39.95"; line 542: "Coverage of tangible security  0%" | FORWARD-SIGNAL | DA restarted in Q2 after a nil Q1. The gain of 10.12 on 39.95 sold is 25.3% of principal. It is 1.92% of Q2 total income (checklist trigger is 4%: not hit), 8.7% of Q2 PBT, and 54% of the QoQ PBT rise (115.80 - 97.15 = 18.65). The pool is unsecured and unrated. Q2 earnings momentum partly rests on a lumpy upfront gain. Watch whether it recurs in Q3. |
| A3-14 | F12 | R014-R017, R046-R049, R072, R073, R114, R115, R406 | 214-215, 235-236, 288, 303, 679; prior L340 | line 679: "(v) Liquidity coverage ratio (LCR)                                                                                                                   404.31%" | AMBIGUOUS | Cash plus other bank balances rose from 1,011.07 to 1,341.66 (+32.7%). Borrowings rose from 5,017.63 to 5,858.32 (+16.8%), and loans +9.3%. Finance cost rose 10.8% QoQ against interest income +5.9%. LCR went from 269.61% to 404.31%. Reading 1: pre-funding for H2 disbursement. Reading 2: negative carry that compresses NIM. The Q3 loan growth rate separates them. |
| A3-15 | F12 | R424, R437, R443, R460, R466, R521 | 1065-1066, 1097; prior L672, L757 | line 1097: "Security          1.1" | AMBIGUOUS | Catalyst exclusive cover is 1,376.64 / 1,261.45 = 1.091x, printed "1.1". Q1 was 1,167.68 / 1,061.48 = 1.100x. Note 8 (line 597) states a 100% minimum, so the cover complies on that basis. If any deed needs 1.10x, rounding hides a shortfall. Ask for the cover each deed requires. |
| A3-16 | F13 | R572, R573 | 62-72, 738-749, 1429-1441, 1107; prior L42-52, L897-899, L1051-1062 | line 72: "Company Secretary & Compliance Officer"; line 1107: "For Aye Finance-limited" | FORWARD-SIGNAL | In Q1, CFO Gaurav Seth signed the outcome letter, the security cover letter, the annexures and the Reg 52(7) letter. In Q2 the CS signs every letter, the annexures carry no named signatory, and no CFO appears anywhere in the filing. The checklist already flags KMP churn AMBER (3 CFOs in 5 months). Ask who the current CFO is and the effective date. |
| A3-17 | F13 | R003, R004, R622 | 43-46; prior L25-27 | "commenced at 11:15 A.M. (1ST) and the Unaudited Financial Results ... approved by the Board of Directors at 11:21 A.M." | AMBIGUOUS | 6 minutes from board start to approval, against 29 minutes in Q1 (10:51 to 11:20). The Audit Committee met the same day (line 483). This came in the first quarter under a new auditor and with a covenant observation in the report. Reading 1: pre-read discipline. Reading 2: thin board scrutiny. |
| A3-18 | F14 | R738, R740, R643, R003 | 979-980, 789, 890, 43, 183-184 | line 980: "11:09:12+05'30’"; line 890: "Obtained the Board approved unaudited financial results" | AMBIGUOUS | The auditor digitally signed the security cover report 6 minutes before the board met and 12 minutes before it approved the results. Yet the report says it used "Board approved" results (lines 789, 890). It also cites an LRR conclusion (line 854) that was signed at 11:24:32. Signing workflow may explain this, but the document is internally inconsistent on its face. Ask the auditor or the company. |
| A3-19 | F14 | R618, R391, R384 | 620; prior L269 | "Company has unutilised Rs. 22.63 crores till period ended September 30, 2026" vs prior L269 "Rs. 28.55 crores has been incurred and for remaining amount provison has been created" | AMBIGUOUS | Q1 implies 37.76 - 28.55 = 9.21 remaining. Q2 states 22.63 unutilised. The basis changed from "incurred" to "unutilised". H1 share issue expenses paid were 6.56 (R312). Ask whether the offer expense estimate will be revised, and whether any surplus returns to net proceeds. |
| A3-20 | F14 | R714 | 496-497 | "August 06, 2020 (resolution framework - 2.0)" | NEUTRAL-FACT | The Aug-2020 circular is resolution framework 1.0. Both circulars are labelled 2.0. A1 normalised this to "1.0/2.0" in R714. |
| A3-21 | F14 | R577, R588 | 155, 621-623 | "Aye Employee Welfare Trust" vs "Aye Finance Employees Welfare Trust" | NEUTRAL-FACT | The same entity has two names within one filing. The Q1 note used the second form (prior L272). |
| A3-22 | F14 | R751 | 1289-1294, 1363-1364 | "6. INE501X07653" then "8. 1NE501X07661"; "15. INE501X07737" / "15. INE501X07745" | NEUTRAL-FACT | S.No 7 is missing and 15 is duplicated, a leftover from removing INE501X07620 (A3-25). |
| A3-23 | F14 | R357, R358 | 538, 540 | "Weighted average maturity (residual maturity)  90.46" | NEUTRAL-FACT | Units are not stated for the residual maturity or the holding period (10.33). The DA economics in A3-13 cannot be fully read without them. |
| A3-24 | F15 | R574, R578, R580 | 92, 486-488 | "S S Kothari Mehta & Co. LLP, Chartered Accountants, the previous statutory auditors" | AMBIGUOUS | The auditor changed from SSKM (Q1 LRR dated 22-Jul-2026) to MSKA. The filing gives no reason and no appointment date. The checklist lists the 1-Sep AGM scrutinizer report as open. Ask whether this was rotation or a resignation. |
| A3-25 | F15 | R595-R610, R523-R539 | 1116-1131; prior L738-757, L935 | prior L748: "11  INE501X07620 28-08-2024" | NEUTRAL-FACT | INE501X07620 (maturity 28-AUG-26, Rs 9.38 cr in Q1) has dropped out. INE501X07745 (29-07-2026, 220.12) is added. Listed NCDs rose from 1,061.48 to 1,261.45. A new trustee agreement is dated July 28, 2026 (line 798). |
| A3-26 | F15 | R586, R722 | 589-594; prior L241-243 | "unable to earn any variable return/ economic benefits from the voting rights" | NEUTRAL-FACT | The FAME non-consolidation reason is rewritten. Q1 cited the company's "objective". Q2 cites the Section 8 bar on distribution. The relationship is unchanged and FAME is still not consolidated. |
| A3-27 | F15 | R583, R375 | 566-567; prior L234-235 | line 567: "RR1" vs prior "Unrated" | NEUTRAL-FACT | Arcil Trust-2026-031 moved from unrated to RR1 (India Ratings). The co-lending section (d) appears for the first time (see A3-12). |

## 3. CHECKLIST SCORECARD

| Check | Status | One-line basis |
|---|---|---|
| F1 | FINDING | 30 ZERO_STANDING rows read. A3-01 (hedge accounting shift) and A3-02 (no SR provision). The OTR dashes (R343-R352) show the run-off book at 0.02. IPO unutilised 0.00 (R387, R390). |
| F2 | N.A. | Single-entity statement (Company plus Trust per LRR para 5, line 155). No consolidated results. FAME not consolidated (Note 7, line 594). |
| F3 | N.A. | No consolidated cost lines to compare. No Going Concern language in the LRR (lines 107-175). |
| F4 | PASS | Unreviewed Trust PAT 0.12 cr = 0.14% of Q2 PAT and 0.47 cr = 0.29% of H1 PAT (lines 157-158), below 10%. No prior comparator: the Q1 LRR had no such paragraph (logged as A3-04). |
| F5 | FINDING | A3-03 (same covenant breach, escalated to a body Observation with a qualified conclusion), A3-04 (new Other Matter paragraphs), A3-05 (Q1 Excel charge-allocation language dropped). |
| F6 | FINDING | A3-06, A3-07, A3-08. Register below. |
| F7 | PASS | No lexicon hedge in the notes ("may sometimes", "no assurance", "evaluating", "exploring", "in discussions", "endeavour": none). The Note 3 RBI phrase (lines 493-494) is carried verbatim from Q1 (prior L212-213). The auditor's "does not enable us to obtain assurance" (lines 130-131) is standard SRE 2410 text. |
| F8 | PASS | ETR Q2 25.11%, Q1 23.31%, H1 24.29%, FY26 21.70%, against statutory 25.17%. Deferred tax sign is mixed (Q1 credit 4.55, Q2 charge 2.15), so there is no persistent credit. No earlier-years tax line. ETR is already close to statutory. |
| F9 | FINDING | A3-09 (actuarial loss far above the prior year). The CFHR swing is covered in A3-01. |
| F10 | FINDING | A3-10 (implied EPS denominator exceeds shares implied by paid-up capital). The capital change of +0.12 cr traces to the Trust transfer plus 3,913 ESOP shares (Note 11). The diluted spread is inside rounding. |
| F11 | PASS | 49.02 + 2,645.59 = 2,694.61 (lines 250-252). Reg 52(4) net worth 2,621.80 (line 653) is 2.7% lower, explained by DTA 55.01, intangibles 2.88, IAUD 2.99 and implied prepaid 11.93. D/E 2.25 and debt/assets 67.30% recompute. |
| F12 | FINDING | Lender variant: A3-11 (PCR and ECL vs GNPA), A3-12 (co-lending NPL 19.9%), A3-13 (DA restart), A3-14 (liquidity build and negative carry), A3-15 (NCD cover 1.091x printed 1.1). |
| F13 | FINDING | No AR, AGM, dividend, director or fund-raise item disclosed (lines 36-48). A3-16 (CFO absent, CS signs all) and A3-17 (6-minute approval). |
| F14 | FINDING | A3-18 (auditor signed before the board met), A3-19 (offer expense basis change), A3-20, A3-21, A3-22, A3-23. |
| F15 | FINDING | A3-24 (auditor change), A3-25 (NCD ISIN list), A3-26 (FAME rationale), A3-27 (SR rating, new co-lending section). |
| F16 | N.A. | Results filing, not a presentation. |
| F17 | N.A. | Results filing, not a concall. The checklist cross-walk below is given for A4. |

## 4. COMMITMENT REGISTER (F6)

| Commitment | Implied date | Note / line ref | Status word |
|---|---|---|---|
| File H1 FY27 RPT disclosure (Reg 23(9)) with the XBRL | with the XBRL filing; date NOT FOUND | lines 84-86 (R614) | initiated |
| Trading window closed until 48 hours after announcement | 23-Oct-2026 | lines 47-48 (R612) | underway |
| Board meeting continuing on other agenda items; outcome not disclosed | 21-Oct-2026 | line 46 (R613) | underway |
| Create security for Rs 455 cr bank/NBFC borrowings within lender time limits | NOT FOUND | line 1105 (R616, R744); prior L882 Rs 510 cr | underway (510 to 455) |
| INE501X07588 covenant 10.3(a) waiver | received | line 1286 (R617) | completed |
| INE501X07588 redemption (Rs 55.22 cr; the breached ISIN) | 17-Nov-2026 | line 1282 (R664) | initiated |
| Deploy the balance Rs 70 cr of INE501X07745 (raised 220, utilised 150) | Q3 FY27 | line 1473 (R563, R564) | underway |
| IPO net proceeds Rs 672.24 cr utilised | by 30-Jun-2026 (prior L265) | lines 613-618 (R385-R390) | completed |
| Offer expenses: Rs 22.63 cr unutilised | NOT FOUND | line 620 (R618); prior L269 | underway |
| ESOP transfers by the Trust (5,04,152) and allotment (3,913) | H1 FY27 | lines 621-624 (R392, R393) | completed |
| Implement RBI directions "as and when they are issued/applicable" | standing | lines 493-494 (R615) | underway |

## 5. CHECKLIST CROSS-WALK FOR A4 (informational, F17 is N.A.)

| Checklist item | This filing | Line |
|---|---|---|
| 1 GNPA trend | 4.20% (Q1 4.49%). The thesis-broken trigger needs an upward reversal, so it has not fired. | 663 |
| 2 DA % of income | 1.92% in Q2 (10.12 / 527.12), 0% in Q1. Below the 4% trigger, but 54% of the QoQ PBT rise (A3-13). | 290, 300 |
| 3 AUM growth YoY | NOT FOUND (no Sep-25 balance sheet). Loans +9.3% over H1. Interest income +29.0% YoY. | 218, 288 |
| 4 FY27 PAT >= Rs 270 cr | H1 161.22, run-rate 322. | 318 |
| 5 Credit cost band | Impairment Q2 81.90, Q1 81.41. Band metric NOT FOUND in this filing. | 305 |
| 6 PCR >= 60% | 62.42%, falling (A3-11). | 673 |
| 7 Unwaived covenant instances (4) | This filing covers listed NCDs only: one breach, waived (A3-03). Bank-lender count NOT FOUND. | 1286 |
| 8 Over-lending metrics | NOT FOUND. | none |
| Add-gate (i) gross slippage | NOT FOUND (the bear reading of the add-gate applies if it is not disclosed elsewhere). | none |
| KMP churn | CFO absent from the filing (A3-16). | 62-72 |

```yaml
stage: A3-forensics
company: "AYE"
quarter: "Q2 FY27"
doctype: "results"
model: "claude-opus-5-5"
status: complete
forensics_path: "runs/aye-q2fy27/work/forensics_results_aye_q2fy27.md"
ledger_reconciled_pct: 100
checklist:
  F1: FINDING
  F2: N.A.
  F3: N.A.
  F4: PASS
  F5: FINDING
  F6: FINDING
  F7: PASS
  F8: PASS
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
  - {id: "A3-01", check: "F1", line: "303, 328, 370", classification: "AMBIGUOUS", implication: "FV-loss line nil and CFHR opens in FY27; hedge accounting likely designated, derivative MTM moved from PAT to OCI; FY26 PAT comparability"}
  - {id: "A3-02", check: "F1", line: "373-374", classification: "AMBIGUOUS", implication: "Provision on investment nil while Arcil SRs held and investments rose 158.14 to 222.96; SR impairment line can activate"}
  - {id: "A3-03", check: "F5", line: "932-934, 950-951, 1276-1286; prior L575-576", classification: "FORWARD-SIGNAL", implication: "INE501X07588 (PAR90+WO)/GLP breach second quarter running, waived; auditor escalated to body Observation; cites higher delinquencies this FY; ISIN matures 17-Nov-26; same clause family in other deeds"}
  - {id: "A3-04", check: "F5", line: "155-167, 169-175", classification: "NEUTRAL-FACT", implication: "New Other Matter paras under new auditor; Trust 0.14% of Q2 PAT"}
  - {id: "A3-05", check: "F5", line: "prior L521-525 vs 881-928", classification: "AMBIGUOUS", implication: "Q1 auditor disclosed Excel-based charge allocation; Q2 report drops it; fixed or unreported"}
  - {id: "A3-06", check: "F6", line: "1105; prior L882", classification: "FORWARD-SIGNAL", implication: "Rs 455 cr borrowings without security (Q1 510); no creation date; lender time limits"}
  - {id: "A3-07", check: "F6", line: "1471-1473", classification: "FORWARD-SIGNAL", implication: "Rs 70 cr of 29-Jul-26 NCD undeployed at 30-Sep; Q3 deployment"}
  - {id: "A3-08", check: "F6", line: "46", classification: "AMBIGUOUS", implication: "Board continued on undisclosed agenda items; check later Reg 30 outcome"}
  - {id: "A3-09", check: "F9", line: "318-323", classification: "AMBIGUOUS", implication: "Actuarial loss H1 (5.36) vs FY26 (0.56); assumption change; verify at FY27 AR"}
  - {id: "A3-10", check: "F10", line: "250, 336-338", classification: "AMBIGUOUS", implication: "Implied basic EPS shares 24.69 cr exceed 24.51 cr from paid-up capital; treasury share treatment via Trust"}
  - {id: "A3-11", check: "F12", line: "663, 673, 372, 375-376", classification: "AMBIGUOUS", implication: "GNPA down but PCR -138 bps, ECL stock -0.55 cr on +9.3% loans, write-offs 155.56; gross slippage not disclosed"}
  - {id: "A3-12", check: "F12", line: "574-586", classification: "FORWARD-SIGNAL", implication: "Co-lending book first disclosed: 19.9% NPL, ~Rs 13.6k per case, 31.27% rate, nil fees"}
  - {id: "A3-13", check: "F12", line: "290, 534-542", classification: "FORWARD-SIGNAL", implication: "DA restarted: 10.12 gain on 39.95 sold, 54% of QoQ PBT rise; unsecured, unrated pool"}
  - {id: "A3-14", check: "F12", line: "214-215, 235-236, 288, 303, 679", classification: "AMBIGUOUS", implication: "Liquidity +32.7%, borrowings +16.8% vs loans +9.3%; finance cost +10.8% QoQ vs interest income +5.9%; NIM pressure or pre-funding"}
  - {id: "A3-15", check: "F12", line: "1065-1066, 1097", classification: "AMBIGUOUS", implication: "Catalyst exclusive cover 1.091x printed 1.1 (Q1 1.100x); shortfall if any deed needs 1.10x"}
  - {id: "A3-16", check: "F13", line: "62-72, 738-749, 1429-1441, 1107; prior L42-52", classification: "FORWARD-SIGNAL", implication: "CFO absent from all Q2 documents; CS signs; KMP churn"}
  - {id: "A3-17", check: "F13", line: "43-46; prior L25-27", classification: "AMBIGUOUS", implication: "6-minute approval vs 29 minutes in Q1"}
  - {id: "A3-18", check: "F14", line: "979-980, 789, 890, 43", classification: "AMBIGUOUS", implication: "Auditor signed security cover report 11:09:12, before 11:15 board start, citing Board approved results; A2 ledger line 28 wrong"}
  - {id: "A3-19", check: "F14", line: "620; prior L269", classification: "AMBIGUOUS", implication: "Offer expenses: Q1 implied 9.21 remaining, Q2 22.63 unutilised; basis changed"}
  - {id: "A3-20", check: "F14", line: "496-497", classification: "NEUTRAL-FACT", implication: "Aug-2020 circular mislabelled resolution framework 2.0"}
  - {id: "A3-21", check: "F14", line: "155, 621-623", classification: "NEUTRAL-FACT", implication: "Trust named two ways in one filing"}
  - {id: "A3-22", check: "F14", line: "1289-1294, 1363-1364", classification: "NEUTRAL-FACT", implication: "Annexure 3 S.No 7 missing, 15 duplicated"}
  - {id: "A3-23", check: "F14", line: "538, 540", classification: "NEUTRAL-FACT", implication: "DA maturity and holding period units missing"}
  - {id: "A3-24", check: "F15", line: "92, 486-488", classification: "AMBIGUOUS", implication: "Auditor change SSKM to MSKA; reason and date not in filing"}
  - {id: "A3-25", check: "F15", line: "1116-1131; prior L748, L935", classification: "NEUTRAL-FACT", implication: "INE501X07620 matured out, INE501X07745 added; NCDs 1,061.48 to 1,261.45"}
  - {id: "A3-26", check: "F15", line: "589-594; prior L241-243", classification: "NEUTRAL-FACT", implication: "FAME non-consolidation rationale rewritten; relationship unchanged"}
  - {id: "A3-27", check: "F15", line: "566-567; prior L234-235", classification: "NEUTRAL-FACT", implication: "Arcil Trust-2026-031 now RR1; co-lending section new"}
forward_signals: ["A3-03", "A3-06", "A3-07", "A3-12", "A3-13", "A3-16"]
ambiguous: ["A3-01", "A3-02", "A3-05", "A3-08", "A3-09", "A3-10", "A3-11", "A3-14", "A3-15", "A3-17", "A3-18", "A3-19", "A3-24"]
commitments:
  - {commitment: "File H1 FY27 RPT disclosure with XBRL", implied_date: "with XBRL; NOT FOUND", ref: "lines 84-86 (R614)", status_word: "initiated"}
  - {commitment: "Trading window closed", implied_date: "2026-10-23", ref: "lines 47-48 (R612)", status_word: "underway"}
  - {commitment: "Board meeting continuing on other agenda items", implied_date: "2026-10-21", ref: "line 46 (R613)", status_word: "underway"}
  - {commitment: "Create security for Rs 455 cr bank/NBFC borrowings within lender time limit", implied_date: "NOT FOUND", ref: "line 1105 (R616, R744); prior L882 Rs 510 cr", status_word: "underway"}
  - {commitment: "INE501X07588 covenant 10.3(a) waiver", implied_date: "received", ref: "line 1286 (R617)", status_word: "completed"}
  - {commitment: "INE501X07588 redemption Rs 55.22 cr", implied_date: "2026-11-17", ref: "line 1282 (R664)", status_word: "initiated"}
  - {commitment: "Deploy Rs 70 cr balance of INE501X07745", implied_date: "Q3 FY27", ref: "line 1473 (R563, R564)", status_word: "underway"}
  - {commitment: "IPO net proceeds Rs 672.24 cr utilised", implied_date: "by 2026-06-30", ref: "lines 613-618 (R385-R390)", status_word: "completed"}
  - {commitment: "Offer expenses Rs 22.63 cr unutilised", implied_date: "NOT FOUND", ref: "line 620 (R618); prior L269", status_word: "underway"}
  - {commitment: "ESOP Trust transfers 5,04,152 and allotment 3,913", implied_date: "H1 FY27", ref: "lines 621-624 (R392, R393)", status_word: "completed"}
  - {commitment: "Implement RBI directions as and when issued", implied_date: "standing", ref: "lines 493-494 (R615)", status_word: "underway"}
gate_a3: pass
blank_checks: []
analyst_note: "Lender variants: F4 = unreviewed share of PAT; F5 = LRR and covenant report diff vs Q1; F12 = asset quality, ECL, DA, co-lending, liquidity, NCD cover (Note 6: one segment). Central tension: GNPA fell 4.49% to 4.20%, but the covenant reason (line 1279) still cites higher delinquencies this financial year. The ECL stock fell Rs 0.55 cr over H1 while loans grew 9.3%. PCR fell 138 bps and H1 write-offs were Rs 155.56 cr. Two readings: real stage-mix gain, or write-off-led GNPA with thinning cover. Gross slippage separates them, and this filing does not disclose it (add-gate i: NOT FOUND). Q2 PBT includes a Rs 10.12 cr DA gain (Q1 nil), 54% of the QoQ PBT rise. The first co-lending disclosure shows 19.9% NPL. No CFO signs any Q2 document. Pipeline error: A2 ledger line 28 says no timestamp precedes approval. Fulltext line 980 shows the auditor signed the security cover report at 11:09:12, before the 11:15 board start. The bank-lender unwaived covenant count (checklist item 7) is not in this filing: NOT FOUND."
```
