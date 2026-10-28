# A3 FORENSIC NOTES: WeWork India Management Ltd (WEWORK) Q2 FY27, doctype: results

Inputs read: A1 structured extraction runs/wework-q2fy27/extracted/wework-results-q2fy27-structured.md (R001-R1112, all rows read); A1 fulltext runs/wework-q2fy27/extracted/wework-results-q2fy27-fulltext.md (lines 1-721, all read); A2 ledger runs/wework-q2fy27/work/ledger_results_wework_q2fy27.md. Source PDF and inputs/ not opened.
Prior-quarter fulltext: none (first quarterly review of this name). Every quarter-over-quarter diff (F5 language, F6 status transitions, F15 entity list, F4 trend in the Other Matters paragraph) is untestable and is recorded below as a BASELINE, not as a pass on change.
Monitoring checklist: no Notion page and no companies/WEWORK.md. PRE-THESIS READ. Operator batch watch list used in its place (occupancy, desks, rent-to-revenue, net debt, Ind AS 116 lease liabilities, Ind AS vs "IGAAP-equivalent" headline gap). Coverage table in section 6.
Units: Rs Million unless stated. The only exception in the filing is "34.25 crore" (board letter, line 65) = Rs 342.5 Mn.

## 0. LEDGER RECONCILIATION
- Structured IDs: 1,112. Ledger IDs referenced: 1,112. Rows read at their cited fulltext line: 1,112 of 1,112 = 100%.
- Count test re-verified: 25 ZERO_STANDING line items, 52 nil cells (SA P&L 28, SA BS 1, SA CF 7, CA P&L 8, CA BS 1, CA CF 7). Agenda items 2 (lines 52, 60). Auditor paragraphs 10 (lines 101/107/115/126; 387/394/402/415/433/442). Entities in consolidation list 4 (lines 419-424). Forward rows 9.
- Ledger flags confirmed at line: CA Note 5 has no printed number in the text layer (line 676 starts "On November 21, 2025"; P&L line 502 cites "(Refer Note 5)"). UDINs illegible (lines 142, 473). CA partner name partial (line 469 "ra Shah"). Membership 222345 at lines 140 and 471.
- Ledger defects found: none. A2 tie-outs (66, 0 FAIL) not re-run in full; A3 re-derived the equity roll-forward (section 5, F11) and the S-vs-C gaps independently and both tie.

## 1. FINDINGS TABLE

| id | check | ledger row ref | line | short verbatim quote | classification | forward implication |
|---|---|---|---|---|---|---|
| F1-a | F1 | G067/R244-R245, G072/R254-R255, G066/R242-R243, G071/R252-R253, G069/R248, G068/R246, G002/R016-R021 | 159, 260, 261, 262, 264, 265 | "Profit on sale of investments in mutual funds (net) \|\| (46.96) \| -"; "Gain on termination/modification of lease (net) \|\| (52.37) \| -"; "Other income \|\| 110.95 \| 73.58 \| 5.23 \| 184.53 \| 11.14" | FORWARD-SIGNAL | Four gain lines nil in H1FY26 are live in H1FY27. Six non-operating gain adjustments sum to 184.39 vs H1 standalone PBT 148.54 and other income 184.53 (composition of other income NOT DISCLOSED; match is an A3 inference). H1 PBT ex other income = (35.99) vs (83.35) H1FY26. Q2 ex other income = 83.41 (Q1: (119.40)). Reported profitability turn rests on treasury and lease gains in H1; Q2 is positive without them. Next-quarter PBT is sensitive to MF marks. |
| F1-b | F1 | G072/R254-R255, G069/R248-R249, G086/R282 | 262, 265, 281 | "(Profit)/Loss on sale of property plant and equipment (net) \|\| (28.32) \| 1.24"; "Gain on termination/modification of lease (net) \|\| (52.37) \| -" | AMBIGUOUS | Lease termination/modification gain plus a PPE disposal gain on proceeds of 31.90 point to centre exits or lease re-cuts in H1. Desks and centres exited are NOT FOUND in the filing. Ties to watch list (occupancy, desks). |
| F1-c | F1 | G103/R316-R317, G104/R318-R319, G089/R288-R289, G092/R294-R295, G093/R296 | 284, 288, 289, 301, 302 | "- in current accounts \|\| - \| 75.52"; "- in escrow accounts \|\| 40.60 \| 3.00"; "(1,173.71) \| -" | AMBIGUOUS | Standalone holds zero cash in current accounts; all 40.60 is in escrow (purpose NOT DISCLOSED). In the same half it bought 1,173.71 of current investments while net borrowing rose 560.80 (1,893.16 in, 1,332.36 out). Inference: cash interest on borrowings ~10.0% annualised (180.32 x2 on average 3,608) vs MF gains ~6.3% annualised (99.47 x2 on average 3,149): a negative carry of about 3.7 points. |
| F1-d | F1 | G005/R034-R039, G110/R387-R392 | 163 | "Sub-contracting cost \|\| 27.57 \| - \| - \| 27.57 \| 36.02 \| 219.28" | AMBIGUOUS | Line is nil in Q1FY27 and Q2FY26, reappears at 27.57 in Q2FY27. FY26 carried 219.28, of which 183.26 fell in H2FY26 (derived). The line anticipates project-type work (likely fit-out / design-build "allied services"); the matching revenue is not separately disclosed. A lumpy services stream sits inside a single-segment revenue line. |
| F2-a | F2 | G018/R112-R117, G126/R483-R488, G119/R441-R446 | 177, 500, 508 | "SI No. 4 Share of profit/(loss) in associate \|\| 8.69 \| 0.94 \| (2.74)" | AMBIGUOUS | C-minus-S PAT gap as % of standalone PAT: Q2FY26 -13.3%, Q1FY27 +11.4%, Q2FY27 +5.1% (YoY swing 18.4 pp; QoQ 6.3 pp); H1FY26 -7.2% to H1FY27 +10.2% (17.4 pp). Q2 decomposition: associate 8.69 + subsidiaries 3.35 (line 447) + eliminations (2.05) = 9.99. YoY swing of 19.80: associate +11.43, subsidiaries and eliminations +8.37. Group PAT now carries a lumpy associate line. |
| F4-a | F4 | R351-R352, R357-R358, R1026-R1030 | 447, 451 | "of Rs. 3.35 million and Rs. 9.02 million"; "Group's share of net profit of Rs. 8.69" | NEUTRAL-FACT | PAT resting on other-auditor review (not S.R. Batliboi): Q2 12.04 = 5.9% of consolidated PAT 204.35; H1 18.65 = 11.4% of 163.74 (above the 10% bar). Thin group PAT (2.7% of Q2 revenue) magnifies small entities. On revenue and assets the share is about 0.4% (31.51 of 7,678.38; 293.78 of 73,698.18). |
| F4-b | F4 | G119/R441-R443, R357 | 451, 500 | "8.69 \| 0.94 \| (2.74)" | AMBIGUOUS | Associate (MyHQ Anarock) share moved (2.74) Q2FY26 to 0.94 Q1FY27 to 8.69 Q2FY27: a 9x QoQ jump, reviewed only by the associate's own auditor. Prior Other Matters text is not available, so the subsidiary half of the YoY test is untestable. |
| F6-a | F6 | R864, R867, R1007, R1092, G013/R082-R087, G121/R453-R458 | 171, 331-333, 680-681 | "impact of these will be evaluated and accounted for" | FORWARD-SIGNAL | Dateable on notification of the final Labour Code rules (date NOT FOUND). The exceptional-item line (nil in 5 of 6 columns, line 171) exists for this charge and is primed for a second Labour Code charge. FY26 first round: 42.94 SA / 43.26 CA. |
| F6-b | F6 | R865-R866, R868-R869, R342-R343, R1015, R1100 | 355-358, 700-702 | "During the year, the Company has filed a scheme"; "the Company shall adjust the accumulated losses" | AMBIGUOUS | NCLT capital reduction to set off 20,501.60 of accumulated losses against Securities Premium. Filing date, hearing status and expected sanction date NOT FOUND. "During the year" in a Q2FY27 note does not say which year. Book-neutral, but sanction is the gate to dividend capacity (accumulated losses block distributable profit). |
| F7-a | F7 | R1008, R1093, R324, R755 | 328-330, 679 | "published draft Central Rules and FAQs"; "which has resulted in estimated" | AMBIGUOUS | The FY26 provision is an estimate on DRAFT rules. Final rules can move it either way. Open-ended hedge with no range given. Size so far: 42.94 = 2.2% of FY26 standalone employee cost 1,937.67. |
| F8-a | F8 | G015/R094-R099, G016/R100-R105, G017/R106-R111, G033/R176-R177 | 174-176, 207 | "Current tax charge \|\| - \| - \| - \| - \| - \| -"; "(g) Deferred tax assets (net) \|\| 3,077.49 \| 3,077.49" | FORWARD-SIGNAL | Standalone ETR 0% in Q2, Q1, Q2FY26, H1FY27, H1FY26 vs statutory 25.17%; FY26 ETR -44.3% (DTA credit 221.71 on PBT 500.44 = 30.7% of FY26 PAT 722.15). DTA unchanged across H1 despite PBT 148.54: no interim deferred-tax accounting. Shield: Q2 48.92 (2,517 bps of PBT); H1 37.39. Consolidated ETR Q2 0.08%, H1 0.81%. Expect a Q4FY27 DTA event in either direction and an eventual ETR step-up. No "earlier years" tax line exists. |
| F8-b | F8 | G034/R178-R179, G083/R276-R277 | 208, 277 | "(h) Income tax assets (net) \|\| 1,047.64 \| 657.66"; "Income taxes refunded/(paid) (net) \|\| (389.97) \| (205.81)" | AMBIGUOUS | Cash tax paid 389.97 with zero tax charge; the tax asset rose by exactly 389.98. Refundable tax (likely TDS by members) now 1,047.64 = 30% of standalone net worth. Cash is tied up until refunds arrive. |
| F9-a | F9 | G019/R118-R123, G020/R124-R129 | 180, 181 | "Re-measurement (loss)/gain on defined benefit plans \|\| 2.96 \| (6.69) \| 0.89 \| (3.73) \| (3.42) \| (5.81)" | NEUTRAL-FACT | Q1FY27 actuarial loss (6.69) exceeds the full FY26 loss (5.81): an assumption change by the rule. Q2 reversed +2.96. Amounts are trivial (under 0.1% of revenue). Also: Q2FY26 tax effect (1.08) with H1FY26 nil, so a Q1FY26 +1.08 offset (derived). Verify discount-rate assumption in the FY27 Annual Report. |
| F10-a | F10 | R335-R340, R333-R334, G094/R298-R299, G023/R142-R147, G024-G025/R150-R161 | 186-187, 290, 342, 345-347 | "allotment of 279,961 and 3,492,205 equity shares respectively on"; "Proceeds from exercise of employee stock options \|\| 171.75 \| -" | FORWARD-SIGNAL | ESOP exercise added 3.49 Mn shares in H1 = 2.58% of the 31-Mar-2026 base (Q1 3.21 Mn, Q2 0.28 Mn). Paid-up capital +3.6% YoY (1,340.23 to 1,388.70). Average exercise price about Rs 49 per share (171.75 / 3.49 Mn; inference) vs IPO price Rs 648. New grants 468,896 in H1. Basic-diluted spread narrowed (FY26 SA 5.39/5.23 = 3.0%; Q2 1.40/1.39 = 0.7%) as options converted. A4: cross-check remaining EIP 2018 pool. |
| F11-a | F11 | G033/R176-R177, G046/R202-R203, G048/R206-R207, G054/R218-R219, G044-G045/R198-R201 | 207, 222-224, 228, 236 | "(g) Deferred tax assets (net) \|\| 3,077.49 \| 3,077.49"; "Total equity \|\| 3,465.28 \| 3,052.33" | AMBIGUOUS | Tie-out holds (1,388.70 + 2,076.58 = 3,465.28; roll-forward ties to 0.01). But DTA = 88.8% of standalone net worth at 30-Sep-2026 and 100.8% at 31-Mar-2026 (net worth ex DTA: (25.16) in March, 387.79 now). Lease liabilities 52,331.24 = 15.1x net worth. Any DTA reversal erases most book equity. No third-party net-worth number in this filing to reconcile against. |
| F12-a | F12 | G049/R208-R209, G051/R212-R213, G058/R226-R227, G057/R224-R225, G080/R270-R271, G081/R272-R273 | 229, 231, 241, 274, 275 | "(iii) Other financial liabilities (non-current) \|\| 2,626.08 \| 1,623.12"; "(c) Other non-current liabilities \|\| 750.89 \| 270.69" | AMBIGUOUS | Single segment (Note 9, line 349), so check run at entity level. Other financial liabilities NC +1,002.96 (+61.8%) and other NC liabilities +480.20 (+177%) in six months. Working-capital inflow from "other liabilities" 707.62 (= 480.20 + 227.42 exactly) plus "other financial liabilities" 757.74 = 1,465.36, 14.3% of H1 OCF 10,247.80. Two readings: member deposits and advance billing from longer enterprise contracts (quality), or landlord or capex-related items (no quality). Nature NOT DISCLOSED. |
| F13-a | F13 | R003-R004, R861-R863, R873, R941-R942 | 60-65 | "the Board has accorded its final approval for the proposed project at an estimated project cost of"; "34.25 crore." | FORWARD-SIGNAL | 10 MWp captive solar, Karnataka, Rs 342.5 Mn (9.4% of H1 PPE capex 3,639.79). In-principle 3-Sep-2026, final 26-Oct-2026. No commissioning date, funding source or expected power-cost saving given. Only non-results agenda item; no AR, AGM, dividend, director, auditor or enabling-resolution item. |
| F14-a | F14 | R008, R812, R362, R845, R952, R1031 | 138, 140, 142, 469, 471, 473 | "per Nikunj Jay"; "Membership No. : 222345"; "ra Shah"; "Membership No.: 222345" | AMBIGUOUS | One ICAI membership number appears under two different printed partner names (standalone vs consolidated review reports). Both UDINs are illegible in the text layer. Likely OCR (line 469 is partial), but unverifiable from A1 text. Verify both UDINs on the ICAI portal and the partner name from A1's page images. |
| F14-b | F14 | R004, R955, R821, R853, R1015, R294, R725, R1092, R945 | 65, 101, 155, 288, 343, 355, 638, 676, 690 | "34.25 crore." vs "(Rs. in Million)"; "Equity Incentive Plan 2018" vs "the Equity Plan 2018"; "Proceeds from borrowings" vs "Proceeds from long-term borrowings" | NEUTRAL-FACT | Cumulative drafting slips: crore in the letter vs Million in statements, no "Rs." on 34.25; ESOP plan named two ways; SA cash-flow borrowing lines lack the "long-term" tag the CA lines carry (while SA current borrowings rose 969.20 to 1,154.23); CA Note 5 unnumbered in the text layer; "During the year" undated in Note 10; "We Work" (line 101). Individually immaterial; a governance data point in aggregate. |

## 2. CHECKLIST SCORECARD

| check | status | basis (one line) |
|---|---|---|
| F1 | FINDING | 25 ZERO_STANDING items read; four with forward content (F1-a to F1-d). Exceptional line anticipates a Labour Code charge (see F6-a). Other nil lines (OCI tax effect, intangibles under development 11.29 new, CA non-current investment purchase nil vs 21.72) are routine. |
| F2 | FINDING | PAT gap swings 18.4 pp YoY and 6.3 pp QoQ on standalone PAT; revenue gap stable at 0.3-0.5%; EBITDA proxy gap 2.84 (0.06%). See F2-a and section 3. |
| F3 | PASS | No shells. Cost of materials consumed exists only in consolidated (8.44 Q2, line 492); employee cost differs (543.16 SA vs 557.90 CA); subsidiaries carry revenue 31.51 and assets 293.78 (lines 445-446). No going concern or EoM language in either report. |
| F4 | FINDING | Other-auditor PAT share H1 11.4% (>10%); associate component jumped (2.74) to 8.69 YoY. Prior Other Matters text unavailable for full trend. |
| F5 | PASS | No EoM, no going concern, no qualification in either review report (lines 126-132, 433-440, 462-463 "not modified"). Prior-quarter verbatim diff untestable (no prior fulltext). This quarter's text is the baseline. |
| F6 | FINDING | Lexicon hits at lines 64, 67 (meeting time, not a commitment), 332, 336, 356, 680-681, 684, 701. Four register rows (section 4). Status transitions vs prior quarter untestable; one in-document transition (solar in-principle to final). |
| F7 | FINDING | Hits: "estimated" (329, 679), "evaluated" (332, 681), "subjected to" (319, 669, review status, not a hedge), auditor "assurance" boilerplate (119, 123, 405, 409). One substantive hedge: F7-a. Whether newly added is untestable. |
| F8 | FINDING | Zero standalone tax all periods, flat DTA, FY26 year-end DTA credit (F8-a); tax refund asset build (F8-b). No earlier-years adjustment line. |
| F9 | FINDING | Q1FY27 actuarial loss exceeds full FY26 (F9-a); immaterial in size. |
| F10 | FINDING | Paid-up capital changes trace to ESOP allotments (Note 8 ties exactly: 279,961 and 3,492,205 shares). Dilution 2.58% in H1 (F10-a). EPS spread narrowing, not widening. |
| F11 | FINDING | Net worth ties (SA and CA, roll-forward within 0.01 and 0.04). DTA concentration in net worth flagged (F11-a). No third-party number in context. |
| F12 | FINDING | Single segment; entity-level liability build funding OCF (F12-a). |
| F13 | FINDING | Two agenda items only; solar capex final approval (F13-a). No AR, AGM, record date, director term or fund-raise item. |
| F14 | FINDING | Membership number vs partner name mismatch, illegible UDINs (F14-a); cumulative drafting slips (F14-b). Note 3 vs review letters consistent ("limited review" both sides). |
| F15 | PASS | List: holding, WW Tech Solutions India Pvt Ltd, Zoapi Innovations Pvt Ltd (subsidiaries), MyHQ Anarock Pvt Ltd (associate), lines 419-424. Prior list unavailable, so recorded as BASELINE. Internal evidence of no H1 addition: SA non-current investments flat 318.88/318.88 (line 205), goodwill flat 22.21/22.21 (line 543), CA purchase of non-current investments nil in H1FY27 (line 634). |
| F16 | N.A. | Results filing, not a presentation. Dropped-disclosure test belongs to the deck run. |
| F17 | N.A. | Results filing, not a concall. Silence audit belongs to the concall run; watch-list coverage of this filing recorded in section 6 for A4. |

## 3. F2 DECOMPOSITION DETAIL (Rs Mn; CA PAT is total incl. NCI)

| period | SA PAT | CA PAT | gap | gap % of abs SA PAT | associate share | subsidiaries + eliminations (derived) |
|---|---|---|---|---|---|---|
| Q2FY27 | 194.36 | 204.35 | 9.99 | +5.1% | 8.69 | 1.30 (subs PAT 3.35, elims (2.05)) |
| Q1FY27 | (45.82) | (40.61) | 5.21 | +11.4% | 0.94 | 4.27 |
| Q2FY26 | 73.87 | 64.06 | (9.81) | -13.3% | (2.74) | (7.07) |
| H1FY27 | 148.54 | 163.74 | 15.20 | +10.2% | 9.63 | 5.57 (subs PAT 9.02, elims (3.45)) |
| H1FY26 | (72.21) | (77.41) | (5.20) | -7.2% | (6.19) | 0.99 |
| FY26 | 722.15 | 749.18 | 27.03 | +3.7% | 21.38 | 5.65 |

Revenue gap (CA minus SA): Q2 25.34 vs subsidiary revenue 31.51, so 6.17 intra-group eliminated; H1 61.64 vs 73.38, so 11.74 eliminated. Consolidated operating expenses run BELOW standalone (Q2 (3.99), Q1 (4.43), FY26 (11.86)) and consolidated PPE sits 6.19 below standalone PPE (lines 199, 540): the parent buys services and capital goods from its subsidiaries, and intra-group margin is eliminated. NEUTRAL-FACT; related-party flow worth one line in the AR read.

## 4. COMMITMENT REGISTER (F6)

| commitment | implied date | note / line ref | status word |
|---|---|---|---|
| Evaluate and account for Labour Code rule impact when rules are notified | on notification of rules; date NOT FOUND | SA Note 5 lines 331-333; CA note (unnumbered, Note 5) lines 680-681 | pending (government "in the process of") |
| NCLT capital reduction: set off accumulated losses 20,501.60 against Securities Premium | on NCLT sanction; filing date and sanction date NOT FOUND | SA Note 10 lines 355-358; CA Note 10 lines 700-702 | initiated (scheme filed) |
| 10 MWp captive solar power plant, Karnataka, est. cost 34.25 crore (Rs 342.5 Mn) | commissioning date NOT FOUND | Board letter item 2, lines 60-65 | initiated (in-principle 3-Sep-2026, final approval 26-Oct-2026) |
| IPO offer for sale, 46,296,296 shares, Rs 29,996.43 Mn; listed NSE/BSE 10-Oct-2025 | done (10-Oct-2025) | SA Note 6 lines 335-340; CA Note 6 lines 683-687 | completed (pure OFS; no primary proceeds to the company) |

## 5. WORKINGS FOR A4 (derived by A3 from filed lines; not company-reported figures)
- Revenue (SA): Q2 7,653.04, +33.6% YoY, +12.5% QoQ (line 158).
- PBT ex other income (SA): Q2 83.41; Q1 (119.40); Q2FY26 68.64; H1FY27 (35.99); H1FY26 (83.35). Other income = 57.1% of Q2 PBT.
- Operating expenses / revenue (SA): Q2 25.5%, Q1 24.1%, Q2FY26 22.3% (line 167). D&A Q2 +11.1% QoQ (3,140.38 vs 2,825.43, line 166).
- Cash lease outflow (principal 2,758.58 + interest 3,121.53, lines 293-294) = 5,880.11 = 40.7% of H1 revenue vs 4,957.95 = 44.8% in H1FY26.
- Ind AS 116 lease liabilities (SA = CA): 52,331.24 at 30-Sep-2026 vs 52,175.31 at 31-Mar-2026 (lines 228, 236). ROU assets 45,030.93 vs 45,939.04.
- Net debt ex leases: SA 66.66 (borrowings 3,894.09 less cash 40.60 and current investments 3,786.83) vs 194.40 in March. CA net cash 2.04 (incl. other bank balances 57.72) vs net debt 142.98 in March. Including leases, SA net debt 52,397.90.
- Ind AS EBITDA proxy (PBT + finance costs + D&A minus other income and finance income), SA H1: 9,271.26; less cash lease outflow: 3,391.15 = 23.5% of revenue vs 19.8% in H1FY26. This includes ESOP cost (96.40) and uses cash rent, not straight-lined rent. The company's "IGAAP-equivalent" headline: NOT FOUND in this filing.
- Post-rent, post-capex cash (SA H1): OCF 10,247.80 less lease cash 5,880.11 less PPE capex 3,639.79 less ROU additions 783.68 = (55.78), vs (741.50) in H1FY26.
- Equity roll-forward (SA): 3,052.33 + TCI 144.81 + ESOP proceeds 171.75 + SBP 96.40 = 3,465.29 vs reported 3,465.28.

## 6. WATCH-LIST COVERAGE IN THIS FILING (pre-thesis; replaces Notion checklist)

| watch item | in this filing? | where / note |
|---|---|---|
| Occupancy | NOT FOUND | Not in results filing; expect deck. F1-b lease terminations are the only indirect signal. |
| Desks | NOT FOUND | Not in results filing; expect deck. |
| Rent-to-revenue | Derivable (cash basis) | 40.7% H1FY27 vs 44.8% H1FY26 (section 5). Company definition NOT FOUND. |
| Net debt | Derivable | SA 66.66 ex leases; CA net cash 2.04 (section 5). |
| Lease liabilities (Ind AS 116) | Yes | 52,331.24 (lines 228, 236, 575, 583). |
| Ind AS vs IGAAP-equivalent gap | NOT FOUND | No IGAAP-equivalent figure in the filing; reconcile against the press release and deck. |

## 7. RUN NOTES
- Stuck rule not triggered. No source access required or attempted.
- Untestable this run for lack of a prior quarter: F5 language diff, F6 status transitions, F15 list diff, F4 Other Matters trend for subsidiaries, F7 "newly added" test. All recorded as baseline for Q3FY27.

```yaml
stage: A3-forensics
company: "WEWORK"
quarter: "q2fy27"
doctype: "results"
model: "claude-opus-5-5"
status: complete
forensics_path: "runs/wework-q2fy27/work/forensics_results_wework_q2fy27.md"
ledger_reconciled_pct: 100
checklist:
  F1: FINDING
  F2: FINDING
  F3: PASS
  F4: FINDING
  F5: PASS
  F6: FINDING
  F7: FINDING
  F8: FINDING
  F9: FINDING
  F10: FINDING
  F11: FINDING
  F12: FINDING
  F13: FINDING
  F14: FINDING
  F15: PASS
  F16: N.A.
  F17: N.A.
findings:
  - {id: "F1-a", check: "F1", line: "159, 260-265", classification: "FORWARD-SIGNAL", implication: "Six gain lines (nil in H1FY26) sum 184.39 vs H1 SA PBT 148.54 and other income 184.53; H1 PBT ex other income (35.99); Q2 ex other income 83.41. Profit turn leans on treasury and lease gains."}
  - {id: "F1-b", check: "F1", line: "262, 265, 281", classification: "AMBIGUOUS", implication: "Lease termination gain 52.37 and PPE disposal gain 28.32 imply centre exits or lease re-cuts; desks and centres exited NOT FOUND."}
  - {id: "F1-c", check: "F1", line: "284, 288-289, 301-302", classification: "AMBIGUOUS", implication: "SA cash all in escrow (40.60), zero in current accounts; MF purchases 1,173.71 funded alongside net borrowing +560.80; inferred negative carry ~3.7 points."}
  - {id: "F1-d", check: "F1", line: "163", classification: "AMBIGUOUS", implication: "Sub-contracting cost lumpy (nil Q1, 27.57 Q2, 183.26 in H2FY26); project-type services stream hidden in single-segment revenue."}
  - {id: "F2-a", check: "F2", line: "177, 500, 508", classification: "AMBIGUOUS", implication: "C-S PAT gap swung -13.3% to +5.1% of SA PAT YoY (18.4 pp); associate +11.43 of the 19.80 swing; group PAT carries a lumpy associate line."}
  - {id: "F4-a", check: "F4", line: "447, 451", classification: "NEUTRAL-FACT", implication: "Other-auditor PAT share H1 18.65 = 11.4% of consolidated PAT (Q2 5.9%); thin PAT magnifies; ~0.4% of revenue and assets."}
  - {id: "F4-b", check: "F4", line: "451, 500", classification: "AMBIGUOUS", implication: "MyHQ Anarock share (2.74) Q2FY26 -> 0.94 Q1 -> 8.69 Q2; 9x QoQ, reviewed only by its own auditor."}
  - {id: "F6-a", check: "F6", line: "171, 331-333, 680-681", classification: "FORWARD-SIGNAL", implication: "Second Labour Code charge likely when final rules are notified; exceptional line primed; date NOT FOUND."}
  - {id: "F6-b", check: "F6", line: "355-358, 700-702", classification: "AMBIGUOUS", implication: "NCLT set-off of 20,501.60 accumulated losses pending; filing and sanction dates NOT FOUND; sanction gates dividend capacity."}
  - {id: "F7-a", check: "F7", line: "328-330, 679", classification: "AMBIGUOUS", implication: "Labour Code provision is an estimate on draft rules; final rules can move it either way; no range given."}
  - {id: "F8-a", check: "F8", line: "174-176, 207", classification: "FORWARD-SIGNAL", implication: "SA ETR 0% all interim periods; DTA flat 3,077.49; FY26 PAT 30.7% from year-end DTA credit 221.71; Q2 shield 48.92 (2,517 bps); Q4 DTA event and eventual ETR step-up."}
  - {id: "F8-b", check: "F8", line: "208, 277", classification: "AMBIGUOUS", implication: "Tax paid 389.97 with zero charge; refundable tax asset 1,047.64 (30% of SA net worth); cash tied to refund timing."}
  - {id: "F9-a", check: "F9", line: "180-181", classification: "NEUTRAL-FACT", implication: "Q1FY27 actuarial loss 6.69 exceeds FY26 full-year 5.81; immaterial; verify discount rate at FY27 AR."}
  - {id: "F10-a", check: "F10", line: "186-187, 290, 342, 345-347", classification: "FORWARD-SIGNAL", implication: "ESOP exercise diluted 2.58% in H1 (3.49 Mn shares at ~Rs 49 avg vs IPO Rs 648); paid-up +3.6% YoY; A4 to check remaining pool."}
  - {id: "F11-a", check: "F11", line: "207, 222-224, 228, 236", classification: "AMBIGUOUS", implication: "Net worth ties, but DTA = 88.8% of SA net worth (100.8% in March); lease liabilities 15.1x net worth; DTA reversal erases most book equity."}
  - {id: "F12-a", check: "F12", line: "229, 231, 241, 274-275", classification: "AMBIGUOUS", implication: "Single segment; other NC financial liabilities +61.8% and other NC liabilities +177% in H1; 1,465.36 = 14.3% of H1 OCF; nature NOT DISCLOSED."}
  - {id: "F13-a", check: "F13", line: "60-65", classification: "FORWARD-SIGNAL", implication: "Final approval of 10 MWp captive solar, Rs 342.5 Mn; no commissioning date, funding or saving stated; only non-results agenda item."}
  - {id: "F14-a", check: "F14", line: "138, 140, 142, 469, 471, 473", classification: "AMBIGUOUS", implication: "Membership 222345 under two partner names; both UDINs illegible; likely OCR; verify on ICAI UDIN portal and A1 page images."}
  - {id: "F14-b", check: "F14", line: "65, 101, 155, 288, 343, 355, 638, 676, 690", classification: "NEUTRAL-FACT", implication: "Crore vs Million units, ESOP plan named two ways, borrowing label variance, unnumbered CA Note 5, undated 'During the year'; cumulative governance data point."}
forward_signals: ["F1-a", "F6-a", "F8-a", "F10-a", "F13-a"]
ambiguous: ["F1-b", "F1-c", "F1-d", "F2-a", "F4-b", "F6-b", "F7-a", "F8-b", "F11-a", "F12-a", "F14-a"]
commitments:
  - {commitment: "Evaluate and account for Labour Code rule impact when rules are notified", implied_date: "on notification; NOT FOUND", ref: "SA Note 5 L331-333; CA Note 5 L680-681", status_word: "pending"}
  - {commitment: "NCLT capital reduction: set off accumulated losses 20,501.60 Mn against Securities Premium", implied_date: "on NCLT sanction; NOT FOUND", ref: "SA Note 10 L355-358; CA Note 10 L700-702", status_word: "initiated"}
  - {commitment: "10 MWp captive solar plant, Karnataka, est. 34.25 crore (Rs 342.5 Mn)", implied_date: "NOT FOUND", ref: "Board letter item 2 L60-65", status_word: "initiated (in-principle 2026-09-03 -> final approval 2026-10-26)"}
  - {commitment: "IPO offer for sale 46,296,296 shares, Rs 29,996.43 Mn; listed 2025-10-10", implied_date: "2025-10-10", ref: "SA Note 6 L335-340; CA Note 6 L683-687", status_word: "completed"}
gate_a3: pass
blank_checks: []
analyst_note: "Pre-thesis baseline. No prior quarter, so F5, F15, status transitions and the F4 trend are baselines, not passes on change. Three points matter. First, earnings quality: H1 standalone PBT 148.54 sits below other income 184.53. Six cash-flow gain lines that were nil a year ago sum to 184.39, so H1 operating PBT is about (36) derived; Q2 alone is positive ex other income (83.41). Second, thin equity: DTA 3,077.49 is 88.8% of standalone net worth against 52,331 of lease liabilities. No tax is booked in interim periods, and FY26 PAT took a 221.71 DTA credit at year-end, so a Q4 DTA event is likely either way. Third, OCF growth is partly funded by other liabilities (+1,465 in H1, nature undisclosed). Supporting the climb: cash rent fell to 40.7% of revenue from 44.8%, and post-rent, post-capex cash is near breakeven (-56) vs (-742) a year ago. The IGAAP-equivalent headline is not in this filing; A4 must reconcile it from the deck. The partner-name mismatch on membership 222345 is likely OCR but needs UDIN verification."
```
