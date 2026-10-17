# A3 FORENSIC NOTES: results | Eimco Elecon (India) Ltd (EIMCOELECO) | q2fy27

Inputs read: A1 structured (R001-R470), A1 fulltext (lines 1-523, all), A2 ledger (LI001-LI099, Z1-Z11, AG1-AG2d, P1-P4, S1-S4, M001). Prior-quarter fulltext: ND. Notion checklist: ND (pre-thesis read, no spear on record). Source PDF and inputs/ not opened.
Units: Rs lakhs unless stated (x0.01 = Rs crore). Quotes are verbatim from the fulltext with runs of whitespace collapsed. Ratios marked [derived] are arithmetic on filed numbers, not filed numbers.

## LEDGER RECONCILIATION
- Structured IDs in ledger: 470 of 470, plus M001 (fulltext line 322). Every row read at its fulltext line. Reconciled: 100%.
- Arithmetic tie-outs run (all tie unless noted): P&L totals Q/H1/FY; BS NCA, CA, NCL, CL, total (both dates); CF operating, investing, financing and net change (all three columns); taxes paid vs current tax plus current tax liability movement (779.00 + 5.32 = 784.32); investments movement vs CF (102.75 purchase + 721.17 FV gain = 823.92 = change in total investments); DTL movement vs P&L deferred tax (770.36 - 676.36 = 94.00).
- A2 Z5 confirmed: R150 Other non-current assets 4,824.68 belongs to 31.03.26. Line 211 places it in the right-hand column, and NCA sums tie only that way (31,717.32 with it; 33,502.99 without it at 30.09.26).
- A2 layout flag confirmed (H1 FY26 investing column, lines 303-308): the column sums to the printed (364.39), but 241.20 and 10.15 equal the H1 FY26 interest and dividend add-backs (lines 280-281) one row higher. The comparative labels are misaligned. See FN20.
- Text-layer glitches resolved by tie: R014 = 8,528.25; R153 = 11,547.54; R242 = (308.64); R267 FY26 PPE sale proceeds = 121.03 [derived from investing total; verbatim value NOT FOUND].
- ASSIGNMENT_BY_LAYOUT (R307-R310) confirmed: current liabilities tie at both dates with 791.17 + 1,803.87 (Sep-26) and 770.37 + 992.58 (Mar-26).

## FINDINGS TABLE

| id | check | ledger row ref | line | short verbatim quote | classification | forward implication |
|---|---|---|---|---|---|---|
| FN01 | F1 | Z5 / R150, R151, R152 | 211, 212 | "(f) Other non-current assets 4,824.68" (right-hand, 31.03.26 column) | NEUTRAL-FACT | Data correction for A1/A4: the Mar-26 cell is 4,824.68 and the Sep-26 cell is blank. The line did not stand at zero. It emptied in H1. Substance carried to FN09. |
| FN02 | F1 | Z8 / R287, R288; LI054 R187, R188 | 315, 243 | "Borrowing 286.58 270.39" ; "(i) Borrowing 574.91 278.93" | AMBIGUOUS | Borrowing line is blank for H1 FY26, so borrowing started in H2 FY26. It then doubled to 574.91 by Sep-26 while the company held 21,277.57 of investments (lines 209, 216). Question: nature of the facility, and why borrow instead of drawing the treasury book. |
| FN03 | F1 | Z6, Z7 / R179, R180 | 236, 237 | "(Ii) Other Financial Liabilities 28.37" ; "(b) Other non-current liabilities 8.89" | NEUTRAL-FACT | Two NC liability classes nil at Mar-26 now carry balances (37.26 total, 0.07% of total equity and liabilities). Template lines for deposits or deferred income. Track size in Q3. |
| FN04 | F6 | R355, R412 | 408 | "Margins are in line with our targeted range of 18-20%." | FORWARD-SIGNAL | Undated margin target. Computed EBITDA margin [derived]: Q2 18.9%, Q1 18.4%, H1 18.6%, FY26 18.6%. Feeds Role 5 promise tracker. The Q2 figure depends on FN11. |
| FN05 | F6 | R356, R415, R336, R341, R435, R436 | 374, 377, 381, 386, 413-414 | "Order Book as on September 30th, 2026 (₹ crore)" ; "133" ; "44" ; "Sep-25 Sep-26" | FORWARD-SIGNAL | Rs 133 cr at Sep-26 against a Sep-25 bar of 44 [chart mapping unresolved, CHART_UNMAPPED], about 3x. Order book = 0.50x TTM revenue of Rs 264.26 cr [derived: 23,074.65 - 10,080.63 + 13,432.03]. No inflow figure or basis (GST, executed vs pending) given. |
| FN06 | F8 | Z1 / R091 | 171 | "Adjustment of tax relating to earlier periods ... (10.54)" | NEUTRAL-FACT | Non-zero in FY26 only (a credit of 10.54, 0.2% of FY26 PBT). Blank in all Q/H1 columns. Rule-triggered finding, low weight. Check the FY26 AR tax note at the Role 6 deep dive. |
| FN07 | F8 | R092-R097, R098-R103, R183, R184 | 172, 173, 239 | "Deferred Tax (0.41) (93.59) 7.30 (94.00) 62.15 22.35" ; "(d) Deferred tax liabilities (net) 676.36 770.36" | AMBIGUOUS | ETR [derived]: Q2 25.0%, Q1 21.6%, Q2 FY26 22.4%, H1 22.8%, H1 FY26 21.6%, FY26 23.1%, against 25.17% statutory. The H1 gap below statutory (238 bps) comes from the Q1 deferred credit of 93.59. Ex-deferred, H1 ETR is 25.9%. The DTL fell 94.00 in a half with 721.17 of fair-value gains (line 278) and about Rs 47 cr capitalised (FN09), and both would normally raise a DTL. Question: what reversed. If it does not recur, ETR steps up about 300 bps. |
| FN08 | F11 | R173, R174, R116, R295, R297, R278, R280 | 230, 180, 319, 308 | "Dividend Paid (232.11) (288.21) (286.34)" ; "Bank balance not considered as cash and cash equivalent (Net) 1.37 (0.21) (2.08)" | AMBIGUOUS | Reserve roll [derived]: 46,173.87 + 2,321.09 - 48,264.22 = 230.74 charged to equity = Rs 4.00 x 57.684 lakh shares. The H1 FY26 payout ties to 286.34 + 2.08 = 288.42 = Rs 5.00 per share. Implied FY26 dividend is Rs 4.00 per share, against Rs 5.00 for FY25 (-20%). No dividend note is in this filing. Question: confirm the DPS and the reason (capex funding vs caution). |
| FN09 | F12 | R138, R139, R140, R141, R150, R263, R264, R055, R056; R412-R416 | 204, 205, 211, 303, 164, 405 | "(a) Property, plant and equipment 11,154.88 6,410.76" ; "Depreciation, Impairment and amortisation expense 206.96 210.75" ; "better capacity utilisation" | FORWARD-SIGNAL | PPE +4,744.12 (+74%). Other NCA (capital advance pattern) -4,824.68, CWIP -111.66, but H1 cash capex only 211.48. FY26 cash capex was 6,054.91, so about Rs 47-48 cr was advanced in FY26 and capitalised in H1 FY27, with no note. Q2 D&A fell QoQ (206.96 vs 210.75). So the asset is non-depreciable (land), or it was capitalised late in the half. If late, a Q3 D&A step-up follows. Adding Rs 47 cr of block also sits awkwardly with "better capacity utilisation". Questions: what asset, what capacity, commissioning date. |
| FN10 | F12 | R157, R158, R153, R154, R233, R236, R260, R262, R261, R107 | 217, 214, 288, 289, 300 | "(ii) Trade receivables 9,118.35 7,248.77" ; "NET CASH GENERATED FROM OPERATING ACTIVITIES (A) 183.78 2,210.89 604.44" | AMBIGUOUS | H1 OCF/PAT [derived] = 7.9% (H1 FY26 30.5%; FY26 57.1%). OCF/EBITDA = 7.4%. Receivables +1,869.58 (+25.8%) and equal 68% of H1 billing. DSO on annualised H1 revenue is about 124 days, against about 115 at Mar-26. Last year H1 released 3,039.33 from receivables. This year H1 absorbed 1,870.64. Lean bear: the collection stretch is unexplained. Question: customer mix and overdue ageing. Per CLAUDE.md, cash conversion stays INDETERMINATE until H2. |
| FN11 | F12 | R061-R066, R067-R072, R001-R006 | 165, 166 | "(h) Compensation to Distributors 316.53 870.66 393.91" ; "(i) Other Expenses 1,265.91 1,139.11 658.44" | AMBIGUOUS | Distributor compensation as % of revenue [derived]: Q2 5.6%, Q1 11.2%, Q2 FY26 11.9%, H1 FY26 11.6%, FY26 11.5%. At the Q1 rate, Q2 EBITDA would be 753 (13.3%), not 1,074 (18.9%). Other Expenses rose to 22.3% of revenue (FY26 14.0%). The two lines combined moved less: 27.9% vs 25.5% FY26. So a reclassification is possible (Note 4, line 193, "regrouped /rearranged"), or the channel mix changed (direct vs distributor-routed). The press release credits operating leverage and cost discipline (lines 404-405) and does not name this line. The 18-20% target (FN04) is not creditable until this is answered. |
| FN12 | F12 | R019-R036, R001-R006, R462 | 158-160, 154, 369 | "Changes in inventories of finished goods and work-in-progress (1,149.94) 1,113.13 (1,372.14)" ; "Product Spares" | FORWARD-SIGNAL | Q2 materials consumed 3,187.99 (+47.7% QoQ) and FG/WIP build of 1,149.94, while revenue fell 26.7% QoQ. That points to H2 dispatch loading (a Q3 revenue signal) or to slow-moving stock. Inventory is 11,547.54, about 361 days of H1 COGS annualised [derived]. Gross margin [derived]: Q2 59.9%, Q1 54.1%, Q2 FY26 71.8%, H1 56.6%, H1 FY26 62.7%, FY26 57.1%. Q2 FY26 is the outlier base. The chart stacks (33 = 16 + 17; 57 = 20 + 37; 101 = 30 + 71) hint at mix, but the series are unmapped. Question: the product vs spares revenue split by quarter. |
| FN13 | F12 | R007-R012, R212-R214, R218, R221, R146, R147, R155, R156 | 155, 278, 209, 216 | "Other Income 189.06 775.94 427 .22 965.00" ; "Gain on sale/ fair valuation of Investment (Net) (721.17)" | NEUTRAL-FACT | Investments total 21,277.57 (38.0% of total assets) [derived]. H1 fair-value and sale gains of 721.17 are 74.7% of H1 other income and 24.0% of H1 PBT. The QoQ other-income swing (-586.88) explains 64% of the Q1-to-Q2 PBT fall (-917.61). PBT ex-OI [derived]: Q2 855.18 vs Q2 FY26 262.00 (+226%); H1 2,041.09 vs 1,294.14 (+57.7%). Reported PAT growth (+46.5% Q2) understates core growth because of the treasury line. |
| FN14 | F12 | R191, R192, R193, R194, R195, R196, R251 | 260, 261, 262, 294 | "(iv) Other financial liabilities 1,110.30 527.46" ; "(b) Other current liabilities 1,169.14 1,421 .33" | AMBIGUOUS | Current other financial liabilities +582.84 (+110%). The CF line shows +713.83, and the BS movement explains only 611.21 including FN03, leaving a gap of about 103. Other current liabilities (customer advances usually sit here) fell 252.19 (-17.7%) while the order book rose (FN05). Provisions +174.59 (+29%). Per F12, a falling liability is either a WC unwind or a mix change. Question: what the 1,110.30 holds (capital creditors, deposits, employee dues), and the customer-advance trend. |
| FN15 | F12 | R001-R005 | 154, 393 | "Revenue from Operations 5,679.72 7,752.31 3,323 .64 13,432.03 10,080.63" ; "reflects the sustained momentum in our business" | NEUTRAL-FACT | Q2 revenue -26.7% QoQ. The same pattern ran in FY26: Q1 FY26 6,756.99 [derived] to Q2 FY26 3,323.64 (-50.8%). H2 FY26 was 12,994.02 (56.3% of FY26). Seasonal and lumpy. The press release shows YoY only. Q1 FY27 vs Q1 FY26 [derived] = +14.7%, and Q2 = +70.9%. |
| FN16 | F13 | AG2, R381, R404-R408, R423, R440 | 41-44, 46-50, 474-475 | "has noted the resignation of Mr. Vishal C. Begwani as Chief Financial Officer (CFO) and Key Managerial Personnel (KMP)" | FORWARD-SIGNAL | CFO, materiality KMP and Risk Committee member exits at close of business on 30 Oct 2026. No successor or interim CFO is named (NOT FOUND). The Q3 FY27 close and limited review will be the first without him. His letter names "audit closures" in the handover (line 509). Statutory deadlines for filling the vacancy (Companies Act s.203(4), six months; any LODR timeline) are for A4 to verify. They are not stated here. |
| FN17 | F13 | AG2 TIMING_GAP, R441, R419, R402 | 486, 18, 489 | "Date: September 5, 2026" ; "To: The Executive Director" | AMBIGUOUS | The letter is dated 5 Sep 2026. The exchange disclosure is dated 13 Oct 2026, 38 days later. This filing states no receipt date and references no earlier intimation. The letter is addressed to the Executive Director, not the Board or Chair. Question: when it was received, whether an earlier Reg 30 intimation exists, and why the board noted it only at the results meeting. |
| FN18 | F14 | R353, R354, R340, R343, R345, R346 | 406-407, 380-384 | "PAT stood at ₹8 crore, registering a 46.5% year-on-year increase. Margins improved year-on- year" ; "16.1% 13.8%" | AMBIGUOUS | The deck's own PAT margin chart shows 16.1% to 13.8% (Q2) and 19.7% to 17.3% (H1); the filed numbers confirm 16.1% and 13.8% [derived]. "Margins improved" holds for EBITDA only. The sentence sits next to PAT. Low materiality, but it is a framing tell. |
| FN19 | F14 | R356, R415, R463 | 374, 413-414 | "Order Book as on September 30th, 2026" ; "healthy open order pipeline of ₹133 crore" | AMBIGUOUS | One number, two terms. A "pipeline" can include unconfirmed or bid-stage orders. A "book" means firm orders. Question: are the Rs 133 cr firm executable orders, and what is the GST, spares and executed treatment. Do not use it as a book-to-bill input until answered. |
| FN20 | F14 | R350-R352, R464, R329, R330, R333; LI082-LI087 | 403-404, 363-366, 303-307 | "EBITDA for the quarter increased by 108.8% year-on-year to ₹11 crore, with the EBITDA margin improving to 18.8%" ; "Payments for purchase of property plant and equipment and CWIP (211.48) (6,054.91) 0.40" | AMBIGUOUS | The press-release EBITDA does not reproduce from the statement. Computed ex-OI [derived]: Q2 1,074.35 (18.9%) vs stated 18.8%; Q2 FY26 522.04 (15.7%) vs chart 15.4%; YoY +105.8% vs stated +108.8%; H1 18.6% vs chart 18.5%. The definition is not stated (R464). Separately, the filed H1 FY26 investing comparatives are row-misaligned (the column total ties, the labels do not). Two drafting defects in one filing. Question: the EBITDA definition. |

## F1 ZERO_STANDING EXPLANATION (all 11 rows)
| Z | row | line | why the line exists / transaction class anticipated | outcome |
|---|---|---|---|---|
| Z1 | R091 | 171 | Assessment true-ups for prior years | Non-zero FY26 only; FN06 |
| Z2-Z4 | R110-R112 | 177-179 | Actuarial remeasurement of the gratuity plan | Booked annually only (FY26 gross (35.22)). Interim columns blank, so all of FY27's remeasurement lands in Q4 FY27 |
| Z5 | R150 | 211 | Capital advances / prepaid non-current | Not a standing zero; 4,824.68 emptied in H1; FN01, FN09 |
| Z6-Z7 | R179, R180 | 236-237 | NC deposits, deferred income | Newly populated; FN03 |
| Z8 | R287 | 315 | Borrowing drawdown | Borrowing began H2 FY26; FN02 |
| Z9 | R393 | 192 | Group structure | No subsidiary, associate or JV at 30 Sep 2026 |
| Z10-Z11 | R468, R469 | 476-477 | Reg 30 appointment template | Not applicable (a cessation, not an appointment). It confirms no successor was appointed in this filing |
| Absent lines | - | - | No exceptional-items or discontinued-operations line is in the template at all | Nothing to anticipate from the template |

## CHECKLIST SCORECARD
| check | status | basis |
|---|---|---|
| F1 | FINDING | All 11 ZERO_STANDING rows explained. R150 is a mislabel and an emptied line (FN01). Borrowing started H2 FY26 (FN02). New NC liability lines (FN03). |
| F2 | N.A. | Standalone-only filer. Note 3 (line 192): "The Company has no Subsidiary, Associate or Joint Venture Company(ies) as on September 30, 2026." No consolidated statement exists to decompose. |
| F3 | N.A. | No subsidiaries (line 192), so no shell entities to detect. No Going Concern EoM to reconcile. |
| F4 | PASS | Auditor paras 1-4 (lines 94-123) cover the Company only, with no Other Matter and no component auditors. 0 Rs and 0% of PAT rest on unreviewed numbers. |
| F5 | PASS | No EoM, Going Concern or Other Matter paragraph in the current review report (lines 94-123). Prior-quarter fulltext is ND, so a verbatim diff was not possible. A removal of an earlier EoM cannot be ruled out from this file. |
| F6 | FINDING | Lexicon hits: "shall ... cease" (46, 49), "will relinquish" (470), "I will work closely" (510). Commitments are registered below. Margin target FN04, order book FN05, CFO exit FN16. No "expected to be", "underway" or "completed" status language in the notes. |
| F7 | PASS | Hedge lexicon swept across the notes and full document. The only hit is "future endeavours" (line 516), the valediction of the resignation letter, which is not a hedge. No "subject to", "evaluating", "exploring" or "no assurance" anywhere. |
| F8 | FINDING | ETR 21.6-25.0% across periods vs 25.17%. FY26 earlier-period adjustment is non-zero (FN06). The H1 deferred credit drives the ETR gap, against the expected DTL direction (FN07). |
| F9 | PASS | No OCI in any Q/H1 column (lines 177-179). FY26 net OCI was (26.36), 0.7% of FY26 PBT. There is no interim swing to test. The annual-only booking is noted in F1. Verify the actuarial assumptions at the FY27 AR. |
| F10 | PASS | Paid-up capital 576.84 in all six columns (line 181) and at both BS dates (line 229). Basic = diluted in every period (lines 185-186). Spread is zero, so no dilutive instruments are visible. |
| F11 | FINDING | Net worth ties: 576.84 + 48,264.22 = 48,841.06; 576.84 + 46,173.87 = 46,750.71. The P&L Other Equity of 46,173.87 (line 182) equals the BS. No third-party number is in context. The reserve roll ties to within 1.37, and that 1.37 equals the earmarked-bank release (line 308). The roll exposes the implied DPS cut (FN08). |
| F12 | FINDING | Single segment (line 191), so the whole BS is the segment. Findings: capitalisation (FN09), WC and cash conversion (FN10), cost-line mix (FN11), inventory build and gross margin (FN12), treasury weight (FN13), liability moves (FN14), revenue seasonality (FN15). |
| F13 | FINDING | Board items: results, plus the CFO resignation noted. No AR, AGM, record date, dividend, fund raise or director appointment items. CFO exit with no successor (FN16). 38-day letter-to-disclosure gap (FN17). |
| F14 | FINDING | Note 1 (line 189) "reviewed by Statutory Auditors ... Unmodified conclusion" is consistent with the limited-review letter (lines 86, 117), so there is no audit/review mismatch. Press-release framing and definition defects: FN18, FN19, FN20. Minor: the circular cited at line 56 carries a "SEBI/" prefix that line 462 drops. The board letter (line 43) and Annexure B (line 469) say "outside the Organization", but the resignation letter (line 501) does not. |
| F15 | PASS | The consolidation list is nil at 30 Sep 2026 (line 192). No entity exists to add, delete or rename. Prior-quarter list is ND, so the check is current-period only. |
| F16 | N.A. | Results doctype (instruction rule). The embedded press release has no prior deck to diff against. Its in-document framing issues are carried under F14. |
| F17 | N.A. | Results doctype, no transcript. The Notion checklist is ND (pre-thesis). |

## COMMITMENT REGISTER (F6)
| commitment | implied date | ref | status word |
|---|---|---|---|
| Vishal C. Begwani ceases as CFO and KMP | close of business 30 Oct 2026 | lines 41-43, 474-475 (R404, R407, R408, R423, R440) | initiated |
| Ceases as materiality KMP (Reg 30) and Risk Committee member | 30 Oct 2026 | lines 46-50 (R405, R406) | initiated |
| "seamless, structured handover of all financial operations, statutory reporting, audit closures" | by 30 Oct 2026 | lines 508-511 (R410, R411) | initiated |
| Successor CFO appointment | NOT STATED. Statutory window is for A4 to verify | implied by lines 41-44, 476 | not started (NOT FOUND) |
| EBITDA margin "targeted range of 18-20%" | undated, ongoing | line 408 (R355, R412) | in line (Q2 18.8% stated) |
| Execute Rs 133 cr "open order pipeline" / order book | undated, as at 30 Sep 2026 | lines 374, 413-414 (R356, R415) | underway |
| "continuing to invest in capabilities" | undated | line 409 (R416) | underway (see FN09 capitalisation) |

## QUESTIONS SEEDED FOR A4 (from FORWARD-SIGNAL and AMBIGUOUS findings)
FN02 borrowing nature; FN04/FN11 distributor-compensation drop vs Other Expenses rise (reclass or channel mix?); FN05/FN19 order book definition and inflow; FN07 DTL reversal source; FN08 FY26 DPS; FN09 asset capitalised, capacity, commissioning, Q3 D&A; FN10 receivable ageing and collection; FN12 inventory build purpose and product/spares split; FN14 content of other financial liabilities, customer advances; FN16/FN17 CFO successor and disclosure timing; FN18/FN20 EBITDA definition.

```yaml
stage: A3-forensics
company: "EIMCOELECO"
quarter: "q2fy27"
doctype: "results"
model: "claude-opus-5-5"
status: complete
forensics_path: "runs/eimcoeleco-q2fy27/work/forensics_results_eimcoeleco_q2fy27.md"
ledger_reconciled_pct: 100        # 470/470 structured IDs + M001
checklist:
  F1: FINDING
  F2: N.A.
  F3: N.A.
  F4: PASS
  F5: PASS
  F6: FINDING
  F7: PASS
  F8: FINDING
  F9: PASS
  F10: PASS
  F11: FINDING
  F12: FINDING
  F13: FINDING
  F14: FINDING
  F15: PASS
  F16: N.A.
  F17: N.A.
findings:
  - {id: "FN01", check: "F1", line: "211", classification: "NEUTRAL-FACT", implication: "Other NCA 4,824.68 belongs to 31.03.26; Sep-26 blank; line emptied in H1 (see FN09)"}
  - {id: "FN02", check: "F1", line: "315, 243", classification: "AMBIGUOUS", implication: "Borrowing began H2 FY26, doubled to 574.91 while holding 21,277.57 investments; ask facility nature"}
  - {id: "FN03", check: "F1", line: "236, 237", classification: "NEUTRAL-FACT", implication: "New NC liability classes 28.37 and 8.89; track size"}
  - {id: "FN04", check: "F6", line: "408", classification: "FORWARD-SIGNAL", implication: "18-20% margin target, undated; Q2 18.9% computed depends on FN11"}
  - {id: "FN05", check: "F6", line: "374, 377, 381, 386, 413-414", classification: "FORWARD-SIGNAL", implication: "Order book Rs 133 cr vs 44 Sep-25 (chart unmapped), 0.50x TTM revenue; basis and inflow not given"}
  - {id: "FN06", check: "F8", line: "171", classification: "NEUTRAL-FACT", implication: "FY26 prior-period tax credit (10.54); rule-triggered, low weight"}
  - {id: "FN07", check: "F8", line: "172, 173, 239", classification: "AMBIGUOUS", implication: "H1 ETR 22.8% vs 25.17% from Q1 deferred credit 93.59; DTL fell despite FV gains and capitalisation; ~300 bps step-up risk"}
  - {id: "FN08", check: "F11", line: "230, 319, 308", classification: "AMBIGUOUS", implication: "Reserve roll implies FY26 DPS Rs 4.00 vs Rs 5.00 FY25 (derived); confirm and ask why"}
  - {id: "FN09", check: "F12", line: "204, 205, 211, 303, 164, 405", classification: "FORWARD-SIGNAL", implication: "~Rs 47 cr advance capitalised into PPE in H1, no note, no D&A step-up; land or late capitalisation; Q3 D&A is the tell"}
  - {id: "FN10", check: "F12", line: "217, 214, 288, 289, 300", classification: "AMBIGUOUS", implication: "H1 OCF/PAT 7.9%; receivables +25.8%, DSO ~124d; cash conversion INDETERMINATE until H2"}
  - {id: "FN11", check: "F12", line: "165, 166", classification: "AMBIGUOUS", implication: "Distributor comp 5.6% of revenue vs 11.2-11.9%; at Q1 rate Q2 EBITDA margin is 13.3%; Other Expenses rose to 22.3%; possible reclass"}
  - {id: "FN12", check: "F12", line: "158-160, 154, 369", classification: "FORWARD-SIGNAL", implication: "Q2 FG/WIP build 1,149.94 with revenue -26.7% QoQ; H2 dispatch loading or slow stock; product/spares split unmapped"}
  - {id: "FN13", check: "F12", line: "155, 278, 209, 216", classification: "NEUTRAL-FACT", implication: "FV gains 74.7% of H1 OI; OI swing explains 64% of QoQ PBT fall; core PBT ex-OI +226% YoY Q2"}
  - {id: "FN14", check: "F12", line: "260, 261, 262, 294", classification: "AMBIGUOUS", implication: "Other financial liabilities +110%, other current liabilities -17.7% while order book rose; ask contents and customer advances"}
  - {id: "FN15", check: "F12", line: "154, 393", classification: "NEUTRAL-FACT", implication: "Q2 -26.7% QoQ mirrors FY26 seasonality (-50.8%); H2-heavy year; press release shows YoY only"}
  - {id: "FN16", check: "F13", line: "41-44, 46-50, 474-475", classification: "FORWARD-SIGNAL", implication: "CFO exits 30 Oct 2026, no successor named; Q3 close is the first without him"}
  - {id: "FN17", check: "F13", line: "486, 18, 489", classification: "AMBIGUOUS", implication: "Letter 5 Sep 2026, disclosed 13 Oct 2026 (38 days); addressed to ED; ask receipt date and earlier intimation"}
  - {id: "FN18", check: "F14", line: "406-407, 380-384", classification: "AMBIGUOUS", implication: "Margins improved claim next to PAT while PAT margin fell 16.1% to 13.8%"}
  - {id: "FN19", check: "F14", line: "374, 413-414", classification: "AMBIGUOUS", implication: "Rs 133 cr called both order book and open order pipeline; firm vs pipeline unresolved"}
  - {id: "FN20", check: "F14", line: "403-404, 363-366, 303-307", classification: "AMBIGUOUS", implication: "Press-release EBITDA not reproducible (18.9% vs 18.8%, +105.8% vs +108.8%); H1 FY26 investing comparatives row-misaligned"}
forward_signals: ["FN04", "FN05", "FN09", "FN12", "FN16"]
ambiguous: ["FN02", "FN07", "FN08", "FN10", "FN11", "FN14", "FN17", "FN18", "FN19", "FN20"]
commitments:
  - {commitment: "Begwani ceases as CFO and KMP", implied_date: "2026-10-30", ref: "lines 41-43, 474-475", status_word: "initiated"}
  - {commitment: "Ceases as materiality KMP and Risk Committee member", implied_date: "2026-10-30", ref: "lines 46-50", status_word: "initiated"}
  - {commitment: "Structured handover incl. statutory reporting and audit closures", implied_date: "2026-10-30", ref: "lines 508-511", status_word: "initiated"}
  - {commitment: "Successor CFO appointment (not stated)", implied_date: "NOT FOUND; statutory window for A4 to verify", ref: "lines 41-44, 476", status_word: "not started"}
  - {commitment: "EBITDA margin targeted range 18-20%", implied_date: "undated", ref: "line 408", status_word: "in line"}
  - {commitment: "Execute Rs 133 cr open order pipeline / order book", implied_date: "undated, as at 2026-09-30", ref: "lines 374, 413-414", status_word: "underway"}
  - {commitment: "Continue to invest in capabilities", implied_date: "undated", ref: "line 409", status_word: "underway"}
gate_a3: pass
blank_checks: []
analyst_note: "Pre-thesis read, standalone-only filer, no EoM. Three things matter for A4. (1) The Q2 EBITDA margin of 18.9% (computed) rests on Compensation to Distributors falling to 5.6% of revenue from 11.2-11.9%. Other Expenses rose to 22.3% from 14.0% (FY26). Combined, the two lines moved little (27.9% vs 25.5%), so a Note 4 reclassification is possible. Do not credit the 18-20% target until this is answered. (2) Cash conversion is weak. H1 OCF is 183.78 lakhs against PAT of 2,321.09 (7.9%). Receivables hold 68% of H1 billing. Q2 built 1,149.94 of FG/WIP while revenue fell 26.7% QoQ. Either H2 dispatch loading or slow collection explains it; Q3 separates the two. (3) About Rs 47 cr moved from Other NCA (a Mar-26 capital advance) into PPE in H1, with no note and no D&A step-up. The asset is land or was capitalised late; Q3 D&A is the observation. The CFO exits 30 Oct 2026 with no successor, after a 38-day letter-to-disclosure gap. Derived, not filed: FY26 DPS Rs 4.00 vs Rs 5.00. Fair-value gains make up 74.7% of other income; core PBT ex-OI rose 226% YoY."
```
