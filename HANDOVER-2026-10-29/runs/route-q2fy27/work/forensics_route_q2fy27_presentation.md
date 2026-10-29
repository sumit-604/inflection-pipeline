# A3 FORENSIC NOTES: Route Mobile Limited (ROUTE), Q2 FY27, doctype: PRESENTATION

Inputs read: A1 structured `runs/route-q2fy27/extracted/route-presentation-q2fy27-structured.md` (R001-R368); A1 fulltext `runs/route-q2fy27/extracted/route-presentation-q2fy27-fulltext.md` (909 lines; re-extraction lines 495-909 used for slides 12, 13, 17-22); A2 ledger `runs/route-q2fy27/work/ledger_presentation_route_q2fy27.md`; prior deck `runs/route-q2fy27/work/prior/extract_presentation_route_q1fy27.txt` (cited "prior line N"); Notion checklist `runs/route-q2fy27/work/monitoring_checklist.md`. No source PDF and nothing under `inputs/` was opened.

Units: the slides state "(in mn)" (lines 296, 393, 430, 462). Only slide 9 (Heltar) uses crore (lines 190, 197). All numbers below are Rs mn unless marked cr.

## LEDGER RECONCILIATION
- Ledger contract: 368 IDs (R001-R368), orphan_ids none. Rows read at cited line: 368 of 368 = 100%.
- Value text matched the fulltext at the cited line for all 368 rows. On slides 12, 13 and 17-22, NUMBER rows were read in the re-extraction mapping blocks.
- Line-cite drift. Seven rows cite a line 1 to 9 lines off from where the text sits on the same slide: R010 (46-47), R013 (cites 55, text 57), R095 (182; text 181/183), R101 (205; CareCenter at 214), R129 (228; segments from 229), R301 (398; text 399), R322 (431 blank; text 430-432). The values are not affected, so these are not findings.
- Arithmetic tie-outs pass. Revenue Q1+Q2 = 23,312. GP Q1+Q2 = 5,044. Every % growth label on slides 16-18 recomputes. Adj. EBITDA bridges on slide 19 add up in all 5 columns. The slide 20 CFO bridge adds up: 1,924.0 + 445.3 - 456.9 - 1,613.3 + 496.8 - 462.5 = 333.4. Headcount sums to 786 on both charts, and 783 + 63 - 60 = 786.

## FINDINGS TABLE

| id | check | ledger row ref | line / slide | short verbatim quote | classification | forward implication |
|---|---|---|---|---|---|---|
| A3-01 | F1 | R290-R292, R249, R255 | 740, 761-765 / s19 | "(+) Employee stock option expense (non cash) - - 5.8 - 11.5" | AMBIGUOUS | The ESOP add-back is a dash in every FY27 column but kept in the template, so no ESOP charge exists in FY27. Leavers were 60 in Q2 (line 908) and 60 in Q1 (prior line 533). Ask whether any live retention instrument exists or a new scheme is planned. A new scheme's cost would be added back and would never reach Adj. EBITDA. |
| A3-02 | F1 | R357, R260, R271, R312, R318 | 743, 846, 834 / s19-20 | "(+) Loss allowance - Capital advance (one time impact) - 49.0 - 49.0 -" | FORWARD-SIGNAL | The "one time" slot stays in the template after the Q1 write-down of 49.0. Meanwhile 1,168.3 of new vendor advances sit on the balance sheet (24x the Q1 write-down). An impairment of that pool would go into this add-back slot and stay out of Adj. EBITDA. Ask: counterparty, security held, and whether the Q1 49.0 was the same vendor. |
| A3-03 | F1 | R353-R356, R362-R367, R253, R259, R272 | 739, 741, 751 / s19 | "EBITDA 1,150.2 1,054.8 1,359.6 2,205.0 2,476.1" | NEUTRAL-FACT | H1 FY26 EBITDA 2,476.1 exceeds Q1 FY26 938.9 (prior line 472) + Q2 FY26 1,359.6 by 177.6. That equals the Q2 FY26 forex gain (line 660). Forex sits in expenses or in other income depending on the period's net sign, so reported EBITDA does not add across periods. Use Adjusted EBITDA for sums: 1,153.9 + 1,332.5 = 2,486.4 vs 2,486.8. The forex add-back is one-way: losses are added back, and gains sit outside EBITDA by definition (line 735). The exceptional and tax-impact slots stay in the template after the FY26 exceptional of 1,358.7. |
| A3-04 | F6 | R318, R312, R313 | 834 / s20 | "Advance paid to vendor for services which will be availed in the subsequent period" | FORWARD-SIGNAL | Dateable commitment: the 1,168.3 advance should be used up in H2 FY27. It would then unwind through COGS with no cash outflow and lift H2 CFO. If the balance holds or grows at Q3/Q4, the cause is a supplier-term change (prepayment demanded), not timing. |
| A3-05 | F6 | R059, R060, R078-R088 | 133, 190-199 / s7, s9 | "Deferred, payable 18 months after closing" | NEUTRAL-FACT | Heltar "completed in July 2026" (closed 29 Jul 2026). Consideration 33.7 cr = 23.9 cr upfront + 9.8 cr deferred. The deferred 9.8 cr is a cash outflow due about 29 Jan 2028 (Q4 FY28). "Core team to be expanded with the right hires" (line 193) has no date. FY27 M&A tally from the deck: 33.7 cr. |
| A3-06 | F8 | R303, R284, R308 | 837, 799, 842 / s19-20 | "Profit before tax (Ind AS) 1924.0" | AMBIGUOUS | H1 effective tax rate = (1,924.0 - 1,511.0) / 1,924.0 = 21.5%, against a statutory 25.17%. The 370 bp gap is a tax shield of about 71 for the half. Direct taxes paid of 462.5 exceed the implied P&L tax of 413.0. The deck has no deferred-tax split; verify in the results filing. At statutory rate, H1 PAT would be about 4.7% lower. |
| A3-07 | F10 | R024 | 91 / s4 | "22.57 Earning Per Share (EPS) in H1 26-27" | AMBIGUOUS | Implied H1 share base = 1,511.0 / 22.57 = 66.95 mn. Implied Q1 base = 685.5 / 9.94 = 68.96 mn (prior lines 115, 489). Implied Q2 EPS 12.63 is +27.1% QoQ, while reported PAT is +20.4%. Three possible causes: the minority-interest share fell, the share count fell, or the EPS basis changed. The deck has no basic vs diluted split. Cross-check against the results filing. |
| A3-08 | F13 | R025, R032 | 92 / s4 | "Board recommended  4 per share interim dividend" | AMBIGUOUS | Same wording as Q1: "Board recommended ₹ 4 per share interim dividend" (prior line 120). The deck does not show whether this is a second interim (H1 total Rs 8) or the Q1 line carried over. No record date. Interims are declared, not "recommended". Capital-return watch item. |
| A3-09 | F13 | R061, R062 | 137-138 / s7 | "appointment of Marko Erkic as CEO of Masiv" | AMBIGUOUS | New CEO at the subsidiary whose breach-remediation fees rose from 13.6 to 69.0 this quarter (line 744). The deck gives no date and no reason for the predecessor's exit. Ask whether the change is linked to the incident. |
| A3-10 | F14 | R217, R186-R187, R194-R198 | 627 (orig. 333) / s17 | "Adjusted PAT trend is in-line with EBITDA" | AMBIGUOUS | The numbers do not support this claim. QoQ: PAT +20.4% vs EBITDA +8.7%. YoY: PAT -17.8% vs EBITDA -11.1%. Ex-forex Adj. PAT: 826.0 (1,003.6 - 177.6) to 815.3 (825.5 - 10.2), -1.3%, while reported EBITDA fell 209.4 (-15.4%). So lines below EBITDA improved about 199 YoY. Q1 printed the same sentence (prior line 445). Ask for the bridge: treasury income on cash, amortisation roll-off, tax. |
| A3-11 | F14 | R242, R243 | 707 (orig. 384) / s18 | "8.6% Y-o-Y 5.0% Y-o-Y" | NEUTRAL-FACT | Both are declines (Adj. EBITDA 2,487 to 2,274; Adj. PAT 1,591 to 1,511). They are printed unsigned, in the same format as the growth labels "7.4% Y-o-Y 6.8% Y-o-Y" (line 706). Slide 17 says "decreased" in words. Presentation governance data point. |
| A3-12 | F14 | R062, R296, R079, R081-R082 | 138, 744, 190, 197 / s7, s9, s19 | "CEO of Masiv" / "Masivian data breach remediation" / "33.7 crore" | NEUTRAL-FACT | The same deck uses two names for the subsidiary, and the deck does not reconcile them. Units switch to crore on slide 9 only: 33.7 cr = 337 mn. |
| A3-13 | F14 | R305, R329, R330 | 839, 868-869 / s20-21 | "(Increase) in trade receivables, mn, H1 FY27" (456.9) | AMBIGUOUS | The receivables balance moved +375 (9,094 to 9,469), but the cash-flow line shows +456.9. About 82 left the balance without cash collection. Candidates: write-off, credit-loss provision, FX translation, reclassification. An acquisition would push the gap the other way. Ask. |
| A3-14 | F15 | R059, R089, R090, R348, R349 | 133, 194, 486 / s7, s9, s22 | "Acquired on slump sale basis through Route Connect, a wholly owned subsidiary" | NEUTRAL-FACT | Heltar was a business transfer into an existing subsidiary. The deck names no new consolidated legal entity, and the seller (Heltar Technologies) stays outside the group. Call2Connect is excluded from headcount in both decks (prior line 537), and its status is not explained. Konera and Truecaller are named in Q1 and absent in Q2. |
| A3-15 | F16 | R019, R033 | 87 / s4 | "5,101 mn EBITDA for LTM ended 30 September 2026" | AMBIGUOUS | The headline LTM EBITDA changed basis between decks under the same label. Q2: 5,101 = FY26 reported 5,372.5 (prior line 472) - H1 FY26 2,476.1 (line 760) + H1 FY27 2,205.0 (line 759) = 5,101.4, a REPORTED basis. Q1: 5,195 (prior line 99) = FY26 adjusted 5,259.1 - 1,153.9 + 1,089.3 = 5,194.5, an ADJUSTED basis. Like-for-like changes: adjusted 5,195 to 5,046 (-2.9%); reported about 5,488 to 5,101 (-7.1%, approximate because of A3-03). The mixed basis prints -1.8%. |
| A3-16 | F16 | R021, R034 | 89 / s4 | "13,556 mn Cash as on 30 September 2026" | AMBIGUOUS | Q1 read "₹ 13,452 mn Net Cash as on 30 June 2026" (prior line 109), so "Net" was dropped. Cash still rose 104 in a quarter with H1 CFO of only 333.4, a Heltar upfront payment of 239 and an interim dividend. Ask for Q2 net cash and gross debt. Watch item #10 depends on net, not gross. |
| A3-17 | F16 | R262, R263, R274, R296 | 744 / s19 | "(+) Professional fees related to Masivian data breach remediation - 69.0 13.6" | FORWARD-SIGNAL | The label moved from "Masivian security incident remediation" (prior line 480) to "data breach". Fees are 5.1x QoQ, 82.6 for H1. A data breach suggests exposed data, which can bring regulatory and customer-claim costs later. Q1 said the incident "marginally impacted gross profit" (prior line 413); Q2 does not update that. Slide 17 also lists "higher expenditure on legal and professional fees" (lines 623-624) as a YoY cost driver beyond this add-back. |
| A3-18 | F16 | R266, R268, R250, R262, R171 | 745-746 / s19 | "EBITDA margin % on a Non-GAAP basis 10.0% 9.5%" | AMBIGUOUS | Computed margin: 1,184.2 / 11,797 = 10.04%. The 10% line is 1,179.7, so headroom is 4.5. The Masivian add-back of 69.0 is 15x that headroom. Excluding it: 1,115.2, a 9.45% margin. Reported EBITDA margin: 9.75%. Q1 on the same bases: adjusted 9.46%, reported 9.16%. Whether the thesis-broken condition fires depends on the basis and on treating the add-back as non-recurring for a second quarter. A3 does not rule. |
| A3-19 | F16 | R309, R311-R315, R320-R321, R326, R328 | 827-833, 865, 867 / s20-21 | "Reported CFO/EBITDA 15%" ... "Adjusted CFO/EBITDA 66%" | FORWARD-SIGNAL | This is the first deck with a cash-flow slide, and it introduces a new non-GAAP "Adjusted CFO". H1 CFO/PAT is 0.22x reported and 0.99x adjusted. Days payable fell from 64 to 50 at the same time, so suppliers were paid faster and also prepaid. Two readings: timing (the advance unwinds in H2) or tighter supplier terms. The observation that separates them is the vendor-advance balance and DPO at FY27 year end. |
| A3-20 | F16 | R105-R120, R131-R150, R154 | 510, 588, 556-559 / s12-13 | "Revenue contribution from select industries in H1 26-27"; "(1) 6M FY26-27 Annualized" | FORWARD-SIGNAL | The mix and cohort slides moved from a Q1-only basis ("in Q1 26-27", prior line 294; "3M FY26-27 Annualized", prior line 370) to H1. That blends Q1 into Q2. Backing Q1 out of H1: Europe-HQ customer revenue was about 2,303 in Q1 and about 1,893 in Q2. At rounding extremes Q2 is still down 178 to 642. Asia-HQ rose 333 to 797. Proximus is Europe-HQ, but the deck does not say whether Proximus-linked revenue sits in the drop. |
| A3-21 | F16 | R067 (ledger T8 dropped slide) | 149 / s7 | "Proximus Global won the Carrier Community Global Award 2026 for Best Application Service Provider" | AMBIGUOUS | The same CCGA 2026 award was credited in Q1 to "the Konera solution, Route Mobile's Network APIs" (prior lines 188-193). Credit has moved to the parent. Ask who owns the Konera IP and books its revenue. Also dropped from the Q1 deck: the "Technological Advancements" RCS slide (prior lines 204-222) and footnote 3 defining non-core items (prior line 464). |
| A3-22 | F16 | R027, R098, R100, R341, R343 | 94, 217, 900-901 / s4, s10, s22 | "2,400+ active billable clients" | AMBIGUOUS | Q1 read "2,100+" (prior line 105). Clients rose by 300 (+14%) and new-products revenue by 339 (945 to 1,284) in the quarter Heltar closed. The deck gives no organic vs acquired split. Tech & Tech Support fell 346 to 340 and Sales & Marketing 229 to 224, despite the acquired Heltar "core team" (line 192). Ask for Heltar revenue, clients and headcount added. |
| A3-23 | F16 | R182, R183 | 311 / s16 | "Enhanced routing strategy delivering higher gross profit margins" | AMBIGUOUS | New driver language. Margin earned from route choice can reverse if mobile operators or OTT channel owners reprice. The Q1 drivers ("customer-specific items", Masivian impact; prior lines 411-413) are not updated. GP per billable transaction: Rs 0.0555 in Q2, vs 0.0525 in Q1 (+5.7%) and 0.0547 in Q2 FY26 (+1.5%). |
| A3-24 | F17 | none (absence) | deck-wide grep nil; prior lines 186-194 | Q1: "strategic partnership with Truecaller" (prior line 188) | FORWARD-SIGNAL | Truecaller does not appear anywhere in the Q2 deck. Watch #13 is now silent for 2 of 3 quarters (deck basis; no Q2 transcript exists). One more silent quarter (Q3 FY27) meets the red condition. |
| A3-25 | F17 | R134, R136, R138, R147 | 598, 600, 614 / s13 | "19 \| clients with account size >$5mn, H1 FY27 (6M annualized)" | AMBIGUOUS | Clients above $5mn went 21 (FY26), 21 (Q1 run-rate, prior line 355), 19 (H1). Clients above $10mn went 8, 10, 9. Top-5 share went 33%, 31%, 30%. Q1's "transitory traffic reduction at a large account ... recovery expected" (prior lines 411-412) is not updated: 1 quarter of silence. NRR is 105% (line 277), so the weakness sits at the top of the book. Ask whether that account recovered. |
| A3-26 | F17 | R063, R091, R094 | 171, 190 / s8-9 | "Sales Route Mobile and Proximus Global sales teams" | AMBIGUOUS | The deck has no number for any of these: Proximus-linked revenue or synergies, channel mix (SMS vs OTT vs voice), Heltar revenue, promoter holding / delisting / open offer, ROCE. Each is silent for 2 quarters on a deck basis. Proximus appears only as a distribution channel. |

## CHECKLIST SCORECARD

| check | status | basis |
|---|---|---|
| F1 | FINDING | All 18 ZERO_STANDING rows (R290-R292, R353-R367) read at lines 761-809; A3-01, A3-02, A3-03. |
| F2 | N.A. | The deck carries consolidated figures only; no standalone columns to decompose. |
| F3 | N.A. | No standalone cost lines in the deck. |
| F4 | N.A. | No auditor report or Other Matters paragraph in a presentation. |
| F5 | N.A. | No Going Concern or Emphasis of Matter text in either deck. |
| F6 | FINDING | Lexicon hits at lines 31 (meeting logistics), 451/834 (vendor advance), 133/193/199 (Heltar); register below; A3-04, A3-05. |
| F7 | PASS | No hedge-lexicon hits. "evaluate" (line 423) is non-GAAP boilerplate, the same as prior line 497. Safe harbor lines 67-79 match prior lines 71-83 word for word. No new hedge. |
| F8 | FINDING | The deck carries H1 PBT and PAT, so ETR is computable: 21.5% vs 25.17%; A3-06. No deferred-tax or prior-year tax line. |
| F9 | N.A. | No OCI in the deck. |
| F10 | FINDING | EPS only (no share count, no basic vs diluted). Implied denominators move by 2.0 mn; A3-07. |
| F11 | N.A. | No net worth or other-equity figure in the deck. The cash relabel is handled under F16 (A3-16). |
| F12 | N.A. | No segment assets or liabilities. Industry, geography and HQ revenue mix handled under F16 (A3-20). |
| F13 | FINDING | Interim dividend wording repeated, no record date (A3-08); Masiv CEO appointment (A3-09). No AGM, enabling resolution or director-term content. |
| F14 | FINDING | Claim vs arithmetic (A3-10), unsigned declines (A3-11), name and unit inconsistency (A3-12), receivables tie-out gap (A3-13). |
| F15 | FINDING | Heltar business absorbed via Route Connect; Call2Connect exclusion unchanged; Konera and Truecaller dropped; A3-14. |
| F16 | FINDING | LTM EBITDA basis switch, Net Cash relabel, breach relabel, threshold headroom, new Adjusted CFO, period-basis change, dropped slides and credits, unseparated acquired contribution, reframed GM driver; A3-15 to A3-23. |
| F17 | FINDING | No Q2 concall transcript exists, so the silence audit ran against the deck and the Notion checklist; A3-24 to A3-26 and the table below. |

## COMMITMENT REGISTER (F6)

| commitment | implied date | ref | status word |
|---|---|---|---|
| Heltar AI customer-engagement business acquisition | completed 29 Jul 2026 (BTA 13 Jul 2026) | lines 133, 190, 192 / s7, s9 | completed |
| Heltar deferred consideration 9.8 cr | about 29 Jan 2028 (18 months after closing) | line 199 / s9 | initiated |
| Heltar core team "to be expanded with the right hires" | undated | line 193 / s9 | initiated |
| Heltar roadmap: Voice AI, analytics, customer data layer | undated | line 169 / s8 | initiated |
| Vendor advance 1,168.3 for services "which will be availed in the subsequent period" | H2 FY27 (next reporting period) | line 834 (orig. 451) / s20 | initiated |
| Interim dividend Rs 4/share "Board recommended" | record/payment date not stated | line 92 / s4 (same as prior line 120) | initiated (ambiguous: new or carried) |
| Salesforce AgentExchange messaging app | launched Aug 2026 | lines 145-146 / s7 | completed |
| Masiv CEO appointment (Marko Erkic) | undated, within Q2 | line 137 / s7 | completed |
| Q1 carry: large-account traffic "recovery expected" pending new solution deployment | not dated in Q1 | prior lines 411-412; no Q2 update | initiated (no Q2 status) |
| Q1 carry: capital advance loss allowance "one time impact" | Q1 FY27 | line 743; Q2 column dash | completed (held one quarter) |

## F17 SILENCE AUDIT: WHAT WAS NOT DISCUSSED (deck basis; no Q2 transcript)

| item | Q2 deck status | consecutive quarters silent |
|---|---|---|
| #1 Gross margin | 22.4% (line 307) | 0 |
| #2 Adj. EBITDA margin | 10.0% printed, 10.04% computed (line 746; A3-18) | 0 |
| #3 CFO/PAT | first disclosure: H1 0.22x reported (lines 827, 799); trailing 4 quarters not computable | 0 (partial) |
| #4 DSO | 72 days (line 866); checklist method on LTM revenue gives about 75.6 days | 0 |
| #5 New products YoY | 36.7% (line 214); acquired share not separated (A3-22) | 0 |
| #6 Top 10 concentration | 42% H1 (line 610); about 41% implied for Q2 alone | 0 |
| #7 Loss of large clients | cohort thinning; Q1 large account not updated (A3-25) | 1 |
| #8 Proximus cross-sell revenue | no figure; distribution role only (A3-26) | 2 |
| #9 Rs 113 cr arbitration | closed 19 Feb 2026; not in deck | n/a (closed) |
| #10 Cash position | 13,556 "Cash", relabelled from "Net Cash" (A3-16) | 0 (basis changed) |
| #11 Promoter (Proximus) holding | absent (shareholding filing is the venue) | 2 |
| #12 CEO continuity | Route CEO not named; Masiv CEO changed (A3-09) | 2 (concall is the venue) |
| #13 Truecaller BM revenue KPI | absent (A3-24) | 2 of 3 |
| #14 Heltar integration | terms disclosed; revenue KPI absent | 2 (revenue KPI) |
| #15 FY27 M&A pace | 33.7 cr disclosed (line 190) | 0 |
| Trigger 4 ROCE | absent | 2 |
| Context: channel mix SMS vs OTT vs voice | absent in both decks | 2 |
| Context: delisting / open offer | absent in both decks | 2 |
| Q1 carry: Masivian gross-profit impact | not updated | 1 |

## DERIVED METRICS FOR A4 (computed from the deck; not findings)
- Revenue per billable transaction, Rs: Q2 FY27 0.2478; Q1 0.2514; Q2 FY26 0.2477. H1 FY27 0.2496 vs H1 FY26 0.2571 (-2.9%).
- Billable transactions: +3.9% QoQ, +5.3% YoY. H1 +10.7% (93.4 vs 84.4), while H1 revenue rose 7.4%.
- New products share of revenue: Q2 10.9% (1,284 / 11,797); Q1 8.2%.
- Net working-capital days (DSO - DPO): FY25 12; FY26 12; H1 FY27 22.
- Vendor advance = about 11.7 days of H1 COGS (1,168.3 / 18,268 x 182.5).
- Ex-forex Adj. PAT, YoY: 826.0 to 815.3.

## PIPELINE NOTES (not findings)
1. The A1 header unit_convention says "Crores". The slides state mn; only slide 9 uses crore. A4 must not apply a crore factor to mn figures.
2. Seven minor line-cite drifts in A1 rows (listed under reconciliation). Values unaffected.

```yaml
stage: A3-forensics
company: "ROUTE"
quarter: "q2fy27"
doctype: "presentation"
model: "claude-opus-5-5"
status: complete
forensics_path: "runs/route-q2fy27/work/forensics_route_q2fy27_presentation.md"
ledger_reconciled_pct: 100
checklist:
  F1: FINDING
  F2: N.A.
  F3: N.A.
  F4: N.A.
  F5: N.A.
  F6: FINDING
  F7: PASS
  F8: FINDING
  F9: N.A.
  F10: FINDING
  F11: N.A.
  F12: N.A.
  F13: FINDING
  F14: FINDING
  F15: FINDING
  F16: FINDING
  F17: FINDING
findings:
  - {id: "A3-01", check: "F1", line: "740, 761-765 (s19)", classification: "AMBIGUOUS", implication: "ESOP add-back nil in all FY27 periods; no visible retention instrument while 60 leave per quarter"}
  - {id: "A3-02", check: "F1", line: "743, 834, 846 (s19-20)", classification: "FORWARD-SIGNAL", implication: "one-time capital-advance allowance slot kept while 1,168.3 mn vendor advance outstanding; any impairment would be added back"}
  - {id: "A3-03", check: "F1", line: "739, 741, 751, 660 (s17, s19)", classification: "NEUTRAL-FACT", implication: "reported EBITDA not additive across periods (H1 FY26 gap 177.6 = Q2 FY26 forex gain); use Adjusted for sums"}
  - {id: "A3-04", check: "F6", line: "834 (s20)", classification: "FORWARD-SIGNAL", implication: "vendor advance should unwind in H2 FY27; balance not unwinding = supplier-term change"}
  - {id: "A3-05", check: "F6", line: "133, 190-199 (s7, s9)", classification: "NEUTRAL-FACT", implication: "Heltar 33.7 cr completed; 9.8 cr deferred due about 29 Jan 2028"}
  - {id: "A3-06", check: "F8", line: "837, 799, 842 (s19-20)", classification: "AMBIGUOUS", implication: "H1 ETR 21.5% vs 25.17%, about 71 mn shield; verify on results filing"}
  - {id: "A3-07", check: "F10", line: "91 (s4); prior 115, 489", classification: "AMBIGUOUS", implication: "EPS-implied share base 68.96 mn Q1 vs 66.95 mn H1; Q2 EPS +27.1% vs PAT +20.4%"}
  - {id: "A3-08", check: "F13", line: "92 (s4); prior 120", classification: "AMBIGUOUS", implication: "Rs 4 interim dividend line identical to Q1; second interim or carry-over unclear; no record date"}
  - {id: "A3-09", check: "F13", line: "137-138 (s7)", classification: "AMBIGUOUS", implication: "new Masiv CEO in the quarter breach fees rose 5x; no reason given"}
  - {id: "A3-10", check: "F14", line: "627 (s17); prior 445", classification: "AMBIGUOUS", implication: "'PAT in-line with EBITDA' false; below-EBITDA lines improved about 199 mn YoY, bridge needed"}
  - {id: "A3-11", check: "F14", line: "706-707 (s18)", classification: "NEUTRAL-FACT", implication: "H1 EBITDA and PAT declines printed unsigned beside growth labels"}
  - {id: "A3-12", check: "F14", line: "138, 744, 190, 197", classification: "NEUTRAL-FACT", implication: "Masiv vs Masivian naming; crore on slide 9, mn elsewhere"}
  - {id: "A3-13", check: "F14", line: "839, 868-869 (s20-21)", classification: "AMBIGUOUS", implication: "receivables balance +375 vs cash-flow +456.9; about 82 mn non-cash reduction (write-off or provision?)"}
  - {id: "A3-14", check: "F15", line: "133, 194, 486 (s7, s9, s22)", classification: "NEUTRAL-FACT", implication: "Heltar via slump sale into Route Connect; no new entity; Call2Connect exclusion unexplained"}
  - {id: "A3-15", check: "F16", line: "87 (s4); prior 99, 472, 481", classification: "AMBIGUOUS", implication: "LTM EBITDA moved from adjusted (Q1) to reported (Q2) basis; like-for-like adjusted -2.9% vs printed -1.8%"}
  - {id: "A3-16", check: "F16", line: "89 (s4); prior 109", classification: "AMBIGUOUS", implication: "'Net Cash' relabelled 'Cash'; net cash and debt needed for watch #10"}
  - {id: "A3-17", check: "F16", line: "744 (s19); prior 480, 413", classification: "FORWARD-SIGNAL", implication: "'security incident' became 'data breach'; fees 13.6 to 69.0; regulatory and claim costs may follow"}
  - {id: "A3-18", check: "F16", line: "744-746 (s19)", classification: "AMBIGUOUS", implication: "Adj EBITDA margin 10.04%, headroom 4.5 mn vs 69.0 add-back; ex-add-back 9.45%, reported 9.75%"}
  - {id: "A3-19", check: "F16", line: "827-833, 865, 867 (s20-21)", classification: "FORWARD-SIGNAL", implication: "reported CFO/EBITDA 15%, CFO/PAT 0.22x; new Adjusted CFO; DPO 64 to 50"}
  - {id: "A3-20", check: "F16", line: "510, 556-559, 588 (s12-13); prior 294, 370", classification: "FORWARD-SIGNAL", implication: "mix moved to H1 basis; Q2 Europe-HQ revenue down 178-642 mn QoQ even at rounding extremes"}
  - {id: "A3-21", check: "F16", line: "149 (s7); prior 188-193, 204-222, 464", classification: "AMBIGUOUS", implication: "CCGA award re-credited from Route's Konera to Proximus Global; RCS slide and non-core footnote dropped"}
  - {id: "A3-22", check: "F16", line: "94, 217, 900-901; prior 105", classification: "AMBIGUOUS", implication: "+300 clients and +339 mn new-products revenue in Heltar quarter; no organic split; tech headcount fell"}
  - {id: "A3-23", check: "F16", line: "311 (s16); prior 411-413", classification: "AMBIGUOUS", implication: "GP margin credited to routing; could reverse; Q1 drivers not updated"}
  - {id: "A3-24", check: "F17", line: "deck-wide absence; prior 188", classification: "FORWARD-SIGNAL", implication: "Truecaller silent 2 of 3 quarters; Q3 silence meets red condition"}
  - {id: "A3-25", check: "F17", line: "598, 600, 614 (s13); prior 349, 355, 411-412", classification: "AMBIGUOUS", implication: ">$5mn cohort 21 to 19, top-5 share 33 to 30%; Q1 large-account recovery not updated"}
  - {id: "A3-26", check: "F17", line: "171, 190 (s8-9)", classification: "AMBIGUOUS", implication: "no number for Proximus revenue, channel mix, Heltar revenue, promoter, delisting, ROCE: 2 quarters silent"}
forward_signals: ["A3-02", "A3-04", "A3-17", "A3-19", "A3-20", "A3-24"]
ambiguous: ["A3-01", "A3-06", "A3-07", "A3-08", "A3-09", "A3-10", "A3-13", "A3-15", "A3-16", "A3-18", "A3-21", "A3-22", "A3-23", "A3-25", "A3-26"]
commitments:
  - {commitment: "Heltar business acquisition", implied_date: "2026-07-29", ref: "lines 133, 190, 192 (s7, s9)", status_word: "completed"}
  - {commitment: "Heltar deferred consideration 9.8 cr", implied_date: "about 2028-01-29", ref: "line 199 (s9)", status_word: "initiated"}
  - {commitment: "Heltar core team to be expanded", implied_date: "undated", ref: "line 193 (s9)", status_word: "initiated"}
  - {commitment: "Heltar roadmap Voice AI, analytics, customer data layer", implied_date: "undated", ref: "line 169 (s8)", status_word: "initiated"}
  - {commitment: "Vendor advance 1,168.3 mn services availed in subsequent period", implied_date: "H2 FY27", ref: "line 834 (s20)", status_word: "initiated"}
  - {commitment: "Interim dividend Rs 4/share", implied_date: "not stated", ref: "line 92 (s4); prior 120", status_word: "initiated"}
  - {commitment: "Salesforce AgentExchange app launch", implied_date: "2026-08", ref: "lines 145-146 (s7)", status_word: "completed"}
  - {commitment: "Masiv CEO appointment", implied_date: "Q2 FY27", ref: "line 137 (s7)", status_word: "completed"}
  - {commitment: "Q1 carry: large-account traffic recovery expected", implied_date: "not dated", ref: "prior 411-412; no Q2 update", status_word: "initiated"}
gate_a3: pass
blank_checks: []
analyst_note: "Three items carry the quarter. (1) The thesis-broken margin test. Adjusted EBITDA margin computes to 10.04%, 4.5 mn above 10%. The Masivian add-back (69.0 mn, 5x Q1, relabelled 'data breach') is 15x that headroom. Reported margin is 9.75%. Like-for-like with the Q1 reading (9.5% adjusted), the test reads not fired. On a reported basis, both quarters sit below 10%. A3 does not rule; A4/A5 must state which basis the pre-committed condition uses. (2) Cash. The first cash-flow slide shows reported CFO/EBITDA 15% and CFO/PAT 0.22x. Management adds an 'Adjusted CFO' that adds back a 1,168.3 mn vendor prepayment, while days payable fell 64 to 50 and Q1 already wrote down a capital advance. The separating observation is whether that advance unwinds in H2. (3) Headline framing drift. Slide 4 LTM EBITDA moved from adjusted to reported basis (arithmetic exact), and 'Net Cash' became 'Cash'. The mix slides moved to an H1 basis, which hides a Q2 drop in Europe-HQ revenue that holds at rounding extremes; Proximus is Europe-HQ. Pipeline note: the A1 header says Crores, but the slides are in mn."
```
