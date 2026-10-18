# FORENSICS concall TATACOMM q2fy27 (A3 forensic notes, doctype: concall)

Company: Tata Communications Ltd (TATACOMM). Quarter: Q2 FY27 (quarter ended 30-Sep-2026; call 15-Oct-2026).
Inputs read: A1 structured (R001-R199, T001-T058, Q01-Q19), A1 fulltext (512 lines), A2 ledger, Role 4 review Step 8.5 only (lines 601-655). Prior-quarter fulltext: not available. No source PDF and nothing under inputs/ was opened.

SOURCE CAVEAT. The fulltext is a faster-whisper MACHINE transcript (L4, L24). A1 inferred every speaker. Where a spoken number conflicts with the filing, the conflict is recorded and the filing wins. Misheard-number doubts are AMBIGUOUS, not management error.

## 0. LEDGER RECONCILIATION

- R rows: 199 of 199 read at the cited fulltext line. Every verbatim value was found at its line.
- Turns: 58 of 58 line ranges read (T001 L27 to T058 L506-512). Questions: 19 of 19 read.
- ledger_reconciled_pct: 100.
- Reconciliation notes (no finding, data hygiene for A4):
  - R093 context says "referenced in voice question". L429 "WhatsApp" sits in the CEO's action-layer answer. The voice-question mention is L303.
  - R094 context says "region of cancelled media events". L439 "Middle East" is where the CEO held Commotion customer talks. The cancelled media events are L332 (R194).
  - A1 TURN TABLE cue lines (for example "cue L15") use SOURCE line numbers. The fulltext range column uses FULLTEXT lines. A4 should cite the range column.
  - R034 / R189 "2.17F" is garbled machine text (unit unclear). See C07.
  - Internal restatements reconcile within rounding: EBITDA 1400 (L55, CEO "crossed") vs 1422 (L154). H1 EBITDA growth 15% (L199) vs 14.8% (L155). Digital growth 18% (L202, L454) vs 18.6% (L149). EBITDA margin 21.3% (L156) vs filing 21.26%. Net debt 11,197 (L169) vs filing 11,197.04.

## 1. FINDINGS TABLE

| id | check | ledger row ref | line/turn | short verbatim quote | classification | forward implication |
|---|---|---|---|---|---|---|
| C01 | F6 | R134, R135, R196, R045, R046 (T029-T030; T030 speaker INFERRED CFO) | L364-366 | "we don't know one-offs or there's no such events that are impacting our Q2 performance" | AMBIGUOUS | The call says the ~45% implied core connectivity margin is "achievable" in coming quarters with no one-offs. The filing says half the YoY margin gain came from staff and other cost cuts (employee cost -60.98, other expenses -63.07 QoQ, review Q1). If those cuts include releases or credits, the 21.26% margin is not a run-rate. Lean bear. Review Q1 stays open. |
| C02 | F7 | R017, R019, R021, R044, R182, R183, R192 (T003, T012) | L148, L152, L154, L232 | "Normalizing for the same, data revenue saw a growth of about 6%"; "in constant currency terms, our EBITDA has been around 10%" | FORWARD-SIGNAL | Currency supplies about half of reported data revenue growth (12.2% vs ~6%) and of reported EBITDA growth (21.2% vs ~10%). A rupee reversal removes it. The period of "around 10%" (Q2 or H1) is not stated (also AMBIGUOUS). The "highest YoY EBITDA growth" claim (L56) is on the FX-aided basis. |
| C03 | F6 | R114, R152, R173, R025, R053 (T006, T050) | L211, L456, L155 | "making sure that we deliver double digit EBITDA growth this year" | FORWARD-SIGNAL | The only quantified FY27 commitment. H1 growth is already 14.8% (L155), so H2 can grow far below H1 and still meet it. A low bar. With cc EBITDA ~10% (L232), a currency reversal is the main way the promise misses. |
| C04 | F17 | Q01, R113, R115, R116, R118 (T005-T006) | L189, L213-214 | "You used to talk about certain revenue growth numbers and EBITDA margin targets"; "We will come back to you in the investor call in February" | AMBIGUOUS | The analyst asked directly whether earlier quantified targets stand. The CEO neither reaffirmed nor withdrew them. He deferred to a February 2027 investor call. Review Q28 remains unanswered. |
| C05 | F6 | R102, R110, R112, R144, R145, R148, R153, R006, R007 (T002, T003, T040, T050) | L60, L158, L415 | "we are very close to a EBITDA breakeven"; "So you will hopefully see that in the coming quarters" | FORWARD-SIGNAL | No quarter is named, and the timing carries "hopefully". The CFO calls the metric "EBITDA margin" (L158). This partly answers review Q3 (definition), not the date. Q3 FY27 test: margin must move a further ~360 bps from -3.6%. The deck's Q2 loss of -107 Cr (review Q2 context) is what "very close" means. |
| C06 | F8 | R030, R079, R080, R111, R164, R186, R187, R188 (T003) | L161-163 | "in-principle agreement with the Canada Revenue Agency"; "contingent liability as on 31st of March 2026 stood at Rs. 1658 crores"; "terms of settlement are currently under finalisation" | FORWARD-SIGNAL | A prior-year tax matter is turning from contingent to actual. The settlement amount is not disclosed, and it is likely to hit H2 FY27 P&L (tax for earlier years) and/or cash. The CFO quotes a 31-Mar-2026 figure, not 30-Sep-2026. Any cash outflow adds to net debt. A4: test whether the Q2 filing carries a provision or note. |
| C07 | F14 | R033, R034, R189, R190 (T003) | L169-171 | "Net debt to EBITDA stood at 2.17F."; "The net debt to EBITDA has held steady despite dividend payments this quarter." | AMBIGUOUS | Spoken net debt matches the filing (11,197.04). Spoken leverage of 2.17 (garbled unit) differs from the filing-derived 2.11x. "Held steady" contradicts the filing: leverage rose from 1.99x to 2.11x and net debt rose 1,606.60 Cr in H1 (review Q5). The filing wins. Ask for the company's ratio definition and the H1 rise. |
| C08 | F17 | R079, R080 (T003; no VAT row exists) | L161 | "settling a long-standing tax matter in our Canada subsidiary" | AMBIGUOUS | The CFO volunteered a favourable tax item. The call said nothing on the National Court VAT and penalty judgment (365.80 Cr) due 13-Oct-2026, two days before the call. That is selective disclosure on a dated binary event. It is one quarter, so not yet confirmatory. Email IR at once (review 8.5D, Q4). Lean bear. |
| C09 | F17 | R026, R029, R110 (T003, T050) | L157, L454-455 | "The improvement in profitability is driven by significant reduction in losses across the digital portfolio." | AMBIGUOUS | The call names only digital loss reduction, mix (NR/GR) and operating leverage. The filing says about 90% (185.39 of 206.80) of the QoQ parent PAT rise came from non-parent sources, and that half the YoY margin gain came from staff and other cuts. Digital explains about half at most (review Q1). The other half of the profit step has no named cause. |
| C10 | F7 | R197, R072, R073, R074, R075 (T034, T002) | L379-380, L118 | "Let me not disclose the number of customers yet ... keep it a little under the wraps for some more time to come"; "You might say that Tata Consumer is our sister company" | AMBIGUOUS | AI-platform revenue and customer count were withheld when asked (review Q30). The AI story rests on two named cases. One (Tata Consumer) is a group company, so the headline AI win is a related-party sale. The undated "for some more time" means it may stay undisclosed until the investor day. |
| C11 | F6 | R071, R020, R022, R052, R184 (T002, T003) | L87, L149, L153 | "Through our commotion acquisition"; "Digital portfolio revenue is up by 18.6% on a YOY basis"; "growth at constant currency was healthy double digits" | AMBIGUOUS | Commotion (wef 01-Dec-2025, review Q27) is in Q2 FY27 but not in Q2 FY26. The call gives no organic/inorganic split and no cc number. The 18.6% may be partly perimeter. Commotion and SaaS run "as one entity under one leader as one PNO" (L397-398), so Commotion's own numbers are not visible. |
| C12 | F6 | R119-R124, R009, R041, R042, R043, R169, R193 (T011-T015) | L226-227, L234 | "I think this is two and a half years of double digit order book growth"; "let's wait one more quarter, you will definitely see" | FORWARD-SIGNAL | A dated test: Q3 FY27 cc data growth should step up from ~6%. The analyst's premise is that 2.5 years of double-digit order growth has not produced double-digit cc data revenue. No order book value was given ("best quarter in Q2", L230). If Q3 cc data growth stays near 6%, the order-to-revenue claim fails. |
| C13 | F6 | R139, R141, R101 (T036, T002) | L408-409 | "we will be undertaking a massive transformation of our own company using this AI product" | FORWARD-SIGNAL | The CEO plans an internal AI-led "reimagination" of service, sales, delivery and assurance. That signals more workforce restructuring. The filing shows a "one-time" staff optimisation charge recurring in Q2 FY26, Q1 FY27 and Q2 FY27 (98.26, 44.78, 36.54; review Q6). Expect more charges. Cost cuts may be the margin engine more than mix. |
| C14 | F6 | R128, R129, R130, R170, R087, R194 (T025) | L329-332 | "media has a big Olympics coming up next year"; "support for the LA Olympics" | AMBIGUOUS | [INFERENCE, external date, PENDING LIVE VERIFICATION] The LA Olympics are scheduled for July 2028 (FY29), not "next year" from October 2026. The words may be misheard or loose. The media catalyst then sits about 7 quarters out. The Middle East cancellations (L332) are a current drag. Media cost initiatives (L342-343) are the nearer driver. |
| C15 | F6 | R107, R142, R031 (T002, T003, T038) | L166, L412, L164 | "Cash CapEx trended up this quarter"; "we are focused on the GPU utilization which we have bought and we have invested" | FORWARD-SIGNAL | Capex stays high (undersea cable, DC-to-DC, "definitely investing in the cloud business"). Q2 FCF was 212 Cr after a negative Q1, and the filing shows net debt +1,607 Cr in H1. The build stays debt-funded. The GPU "utilization" focus suggests use is below plan (ambiguous). No capex guidance and no leverage ceiling were given (review Q5, Q31). |
| C16 | F7 | R126, R127 (T023) | L305, L315 | "But it's too early to say whether it's a material or not." | NEUTRAL-FACT | The voice revival claim is hedged and carries no forecast value. No question needed. |
| C17 | F7 | R181 (T002) | L56 | "This is highest year on year EBITDA growth ever achieved since the recent M&As." | NEUTRAL-FACT | The qualifier limits the comparison base to the post-M&A period, on the FX-aided reported basis (see C02). |
| C18 | F6 | R011, R012, R076, R193 (T002, T013) | L132, L235 | "multi-million dollar engagement with the leading global Neo cloud provider"; "there are no large wins which are part of this order book" | NEUTRAL-FACT | The headline AI-infrastructure win is unquantified and small against Rs 6,688 Cr quarterly revenue (L147). Order growth is broad-based. "CPU clusters" (L132) is likely a misheard "GPU" (machine text). |
| C19 | F17 | Q01-Q19, T004-T058 | L177-512; L507 | "Last call and first question and then we'll close." | AMBIGUOUS | Silence audit against the 31 Role 4 questions: 0 fully answered, 7 partial, 1 declined, 1 deflected, 22 silent (Section 4). No analyst raised any balance-sheet, contingency, entity or tax item, and management volunteered none except the CRA settlement. This is the first quarter of silence (prior transcripts NOT FOUND), so it is not yet confirmatory. Every silent row goes to the IR email. |

## 2. CHECKLIST SCORECARD

| check | status | basis |
|---|---|---|
| F1 | N.A. | Concall. A2 ZERO_STANDING section is empty. No zero-value standing line items in a transcript. |
| F2 | N.A. | Concall gives no standalone vs consolidated figures. The subsidiary-driven QoQ profit gap is covered under F17 (C09). |
| F3 | N.A. | No cost-line tables in a transcript. |
| F4 | N.A. | No auditor Other Matters in a transcript. |
| F5 | N.A. | No EoM paragraph in a transcript, and no prior-quarter fulltext. |
| F6 | FINDING | C01, C03, C05, C11, C12, C13, C14, C15, C18. 18 commitments registered (Section 3). |
| F7 | FINDING | C02, C10, C16, C17. Hedge cluster on timing: "hopefully" (L412, L415), "That is our hope" (L286), "We're hoping" (L230), "I'm hoping" (L234). Settlement hedges "in-principle" / "under finalisation" (L161, L163). |
| F8 | FINDING | C06. The call discloses a pending prior-year tax settlement (CRA, contingent 1,658 Cr at 31-Mar-2026). ETR not discussable from a transcript. |
| F9 | N.A. | No OCI data in a transcript. |
| F10 | N.A. | No share count or EPS spoken. |
| F11 | N.A. | No net worth figure spoken. Net debt 11,197 ties to the filing (11,197.04). |
| F12 | N.A. | No segment assets or liabilities spoken. The analyst-derived core margin (R045/R046) is covered under C01. |
| F13 | N.A. | No board outcome in a transcript. The CTO appointment (L45, a management role) and the February investor call (L213) are in the commitment register. |
| F14 | FINDING | Applied as spoken-vs-filing tie-out: C07 (leverage 2.17 / "held steady" vs filing 1.99x to 2.11x and +1,606.60 Cr H1). Internal spoken restatements reconcile within rounding (Section 0). |
| F15 | N.A. | No consolidation list in a transcript. |
| F16 | N.A. | Presentation-specific. The deck is a separate document. Target reframing on the call is covered under F17 (C04). |
| F17 | FINDING | C04, C08, C09, C19. Of 31 questions: 22 silent, 7 partial, 1 declined, 1 deflected, 0 fully answered. |

## 3. COMMITMENT REGISTER (from F6)

| # | commitment | implied date | turn / line ref | status word |
|---|---|---|---|---|
| 1 | Digital portfolio to EBITDA breakeven / positive ("very close", "coming quarters", "at the soonest") | no date; "coming quarters" (earliest Q3 FY27) | T002 L60; T003 L159, L173; T040 L415, L418; T050 L456 (R102, R110, R112, R144, R145, R148, R153) | underway (-6.9% Q1 to -3.6% Q2) |
| 2 | Double-digit EBITDA growth in FY27; "deliver what we have promised" | FY27 (31-Mar-2027) | T006 L211; T050 L456 (R114, R152, R173) | underway (H1 14.8%, L155) |
| 3 | Constant-currency data growth to show order book conversion "one more quarter" | Q3 FY27 results (about Jan-2027) | T012 L234 (R121) | initiated |
| 4 | Order book converts to revenue | "coming years" (undated) | T012 L234; T014-T015 L237-238 (R122, R124) | underway |
| 5 | Investor call / investor day: longer-term growth, business framing (platform / infra / services mix), internal AI transformation detail | February 2027 | T006 L213-214, L217; T036 L409; T040 L416-417 (R115, R116, R118, R140, R146, R147) | initiated (scheduled) |
| 6 | CRA Canada tax settlement: "necessary disclosures in due course" | undated (likely H2 FY27) | T003 L161-163 (R111, R186, R188) | initiated (in-principle agreement; terms under finalisation) |
| 7 | Core connectivity margin ~45% "achievable" in coming quarters | coming quarters | T030 L364-365 (R134, R135; speaker INFERRED) | completed for Q2 (analyst-derived); sustainability open |
| 8 | Media cost initiatives to "start playing out in the coming quarters" | coming quarters | T026 L342-343, L348 (R132, R133) | underway ("already started playing out") |
| 9 | LA Olympics media support | "next year" as spoken; Games scheduled Jul-2028 [external, verify] | T025 L329-331 (R128, R129, R170) | initiated ("getting ready") |
| 10 | More languages for SDFC Ergo voice AI | "soon" | T002 L124 (R106) | initiated |
| 11 | Internal AI-led transformation of the company | "already happening"; detail at investor day | T036 L408-409 (R139, R141) | underway |
| 12 | CIS business to become AI-led platform business, improve profitability | undated | T036 L407 (R137, R138) | initiated |
| 13 | Invest in the cloud business; sell own AI / sovereign cloud; GPU utilisation | "in the future" | T038 L411-413 (R142, R143) | underway |
| 14 | Scale capacity in line with demand; anchor-customer-led expansion | ongoing | T002 L137 (R107) | underway |
| 15 | Narotan Sharma (chief transformation officer) leads the enterprise transformation agenda | joined since last investor call | T002 L45-46 (R067, R101) | completed (appointment) |
| 16 | More unified-stack solutions ("That is our hope") | undated | T019 L285-286 (R125) | initiated |
| 17 | Network: infra leader, platform innovator; expand while keeping profitability | undated | T054 L486-487 (R154, R155) | underway |
| 18 | Net debt / capital discipline ("remain disciplined in our capital allocation") | undated | T003 L168 | underway (no ceiling stated) |

## 4. WHAT WAS NOT DISCUSSED (F17 silence audit, 31 Role 4 questions, review lines 609-644)

Consecutive quarters of silence = 1 for every row (first look; prior-quarter transcripts NOT FOUND).

| Q# | topic | call status | nearest line cite | quarters silent |
|---|---|---|---|---|
| 1 | Rupee amount of non-recurring Q2 cost (employee -60.98, other -63.07 QoQ) | PARTIAL: "no one-offs" asserted (inferred CFO), no rupee figure; staff/other cuts not named; "razor sharp focus on cost" | L365-366; L455 | 1 |
| 2 | Digital rupee loss Q1 FY27, Q2 FY26, FY26 | PARTIAL: margins only (-3.6 vs -6.9), "less than half" of Q1 losses; no rupee series | L58-59 | 1 |
| 3 | Digital breakeven quarter and metric definition | PARTIAL: called "EBITDA margin"; no quarter, "hopefully ... coming quarters" | L158; L415 | 1 |
| 4 | National Court VAT judgment 13-Oct-2026 (365.80 Cr) | SILENT (material, dated; see C08) | none; CFO tax segment L161-163 covers Canada only | 1 |
| 5 | FY27 capex guidance; net debt / EBITDA ceiling | PARTIAL: "Cash CapEx trended up"; "held steady"; no guidance, no ceiling | L166; L171 | 1 |
| 6 | Total cost and end date of staff optimisation programme | SILENT; internal "massive transformation" signals more (C13) | L409 | 1 |
| 7 | FY27 ETR; DTA remaining | SILENT | none | 1 |
| 8 | Campaign Registry result swing; Canada exit; renewals | SILENT | none | 1 |
| 9 | Entity raising 2,628.15 Cr H1 LT borrowings; parent guarantee | SILENT | none | 1 |
| 10 | Parent write-off 116.73 Cr; bad-debt ratio | SILENT | none | 1 |
| 11 | 50.00 Cr contractual-obligation provision | SILENT | none | 1 |
| 12 | Associate investment 356.10 Cr; return; commitments | SILENT | none | 1 |
| 13 | Two management-furnished unreviewed subsidiaries | SILENT | none | 1 |
| 14 | DoT demand aggregate and new notices | SILENT. Pipeline note: task brief gives DoT contingent Rs 7,513.71 Cr; review Q14 gives 7,844.57; A4 to reconcile from the filing | none | 1 |
| 15 | Kaleyra, Inc. standalone carrying value vs FMV USD 92.625m | SILENT | none | 1 |
| 16 | Kaleyra transfer to TCNL completion date; TCNL financing | SILENT | none | 1 |
| 17 | Kaleyra Africa exit 04-Sep-2026 mode and P&L | SILENT | none | 1 |
| 18 | TComm Turkey purpose and capital | SILENT | none | 1 |
| 19 | Q1 fire provision 30.10 Cr insurance claim | SILENT | none | 1 |
| 20 | H1 tax refund; refundable balance | SILENT | none | 1 |
| 21 | Standalone Q1 OCI loss 9.37 Cr driver | SILENT | none | 1 |
| 22 | SBP forfeiture reversal; FY27 grants | SILENT | none | 1 |
| 23 | Transformation Services revenue -33.70% YoY | SILENT | none | 1 |
| 24 | Zubin Adil Patel exit / Ridhi Sood from 01-Nov-2026 | SILENT | none | 1 |
| 25 | Press-release vs filed Data revenue reconciliation; Digital definition | PARTIAL: digital drivers named (interaction, next-gen connectivity, IoT); no reconciliation | L150; L250 (analyst) | 1 |
| 26 | 7.40 Cr asset held for sale | SILENT | none | 1 |
| 27 | Digital perimeter restatement; Commotion contribution | SILENT on split; Commotion named only as capability (C11) | L87; L397-398 | 1 |
| 28 | Earlier targets still stand | DEFLECTED to February investor call (C04) | L189; L213-214 | 1 |
| 29 | Tower structure date; new heads in last 12 months | PARTIAL: "full team is in place"; one new head named (Narotan Sharma); "individual towers" | L44-46; L389-390 | 1 |
| 30 | AI-platform revenue and paying customers | DECLINED (C10) | L379-380 | 1 |
| 31 | India GPU cost, use, depreciation in Digital margin | PARTIAL: "focused on the GPU utilization"; no rupee, %, or treatment | L412 | 1 |

Key filing facts from the task brief, tested against the call:
- Op EBITDA margin 21.26%, half the YoY gain from staff and other cuts: the call attributes the gain to digital and operating leverage only (L157, L454-455), and says there are no one-offs (L365-366). C01, C09.
- About 90% of the QoQ profit rise from subsidiaries: SILENT. C09.
- Net debt +Rs 1,607 Cr in H1: the CFO says "held steady" (L171). C07.
- DoT contingent: SILENT (Q14 row).
- VAT judgment due 13-Oct-2026: SILENT. C08.
- Recurring "one-time" staff charge: SILENT; signal of more (C13).
- Digital margin -3.6%, no breakeven date: confirmed, no date (L60, L415). C05.

## 5. FLAGS FOR A4

FORWARD-SIGNAL (to management questions / tracker): C02, C03, C05, C06, C12, C13, C15.
AMBIGUOUS (to management questions): C01, C04, C07, C08, C09, C10, C11, C14, C19.

```yaml
stage: A3-forensics
company: "TATACOMM"
quarter: "q2fy27"
doctype: "concall"
model: "claude-opus-5-5"
status: complete
forensics_path: "C:\\Users\\SUMIT SHARMA\\repos\\inflection-pipeline\\.claude\\worktrees\\q2fy27\\runs\\tatacomm-q2fy27\\work\\forensics_concall_tatacomm_q2fy27.md"
ledger_reconciled_pct: 100
checklist:
  F1: N.A.
  F2: N.A.
  F3: N.A.
  F4: N.A.
  F5: N.A.
  F6: FINDING
  F7: FINDING
  F8: FINDING
  F9: N.A.
  F10: N.A.
  F11: N.A.
  F12: N.A.
  F13: N.A.
  F14: FINDING
  F15: N.A.
  F16: N.A.
  F17: FINDING
findings:
  - {id: "C01", check: "F6", line: "L364-366", classification: "AMBIGUOUS", implication: "Inferred-CFO says no one-offs and ~45% core margin achievable; filing says half YoY margin gain is staff/other cuts; 21.26% may not be run-rate"}
  - {id: "C02", check: "F7", line: "L152; L232", classification: "FORWARD-SIGNAL", implication: "Currency supplies about half of reported data growth (12.2% vs ~6% cc) and EBITDA growth (21.2% vs ~10% cc); rupee reversal removes it"}
  - {id: "C03", check: "F6", line: "L456; L155", classification: "FORWARD-SIGNAL", implication: "Only quantified FY27 promise is double-digit EBITDA growth, already exceeded in H1 (14.8%); low bar, FX is the main miss route"}
  - {id: "C04", check: "F17", line: "L189; L213-214", classification: "AMBIGUOUS", implication: "Earlier revenue and margin targets neither reaffirmed nor withdrawn; deferred to Feb-2027 investor call"}
  - {id: "C05", check: "F6", line: "L60; L415", classification: "FORWARD-SIGNAL", implication: "Digital breakeven undated and hedged 'hopefully'; metric is EBITDA (L158); Q3 needs ~360 bps more"}
  - {id: "C06", check: "F8", line: "L161-163", classification: "FORWARD-SIGNAL", implication: "CRA prior-year tax settlement in-principle; contingent 1,658 Cr at 31-Mar-2026; undisclosed amount likely hits H2 P&L and cash"}
  - {id: "C07", check: "F14", line: "L169-171", classification: "AMBIGUOUS", implication: "Spoken leverage 2.17 and 'held steady' vs filing 1.99x to 2.11x and net debt +1,606.60 Cr H1; filing wins"}
  - {id: "C08", check: "F17", line: "L161", classification: "AMBIGUOUS", implication: "Favourable Canada tax item volunteered; VAT judgment (365.80 Cr) due 13-Oct-2026 unmentioned; selective disclosure, email IR at once"}
  - {id: "C09", check: "F17", line: "L157; L454-455", classification: "AMBIGUOUS", implication: "Call credits digital and operating leverage only; ~90% of QoQ parent PAT rise from non-parent sources has no named cause"}
  - {id: "C10", check: "F7", line: "L379-380; L118", classification: "AMBIGUOUS", implication: "AI customer count and revenue withheld; one of two showcase wins is a group (related-party) company"}
  - {id: "C11", check: "F6", line: "L87; L149; L153", classification: "AMBIGUOUS", implication: "Digital +18.6% includes Commotion perimeter (wef 01-Dec-2025); no organic split, cc growth unquantified"}
  - {id: "C12", check: "F6", line: "L226-227; L234", classification: "FORWARD-SIGNAL", implication: "Dated test: Q3 FY27 cc data growth must step up from ~6% after 2.5 years of double-digit order growth"}
  - {id: "C13", check: "F6", line: "L408-409", classification: "FORWARD-SIGNAL", implication: "Internal AI-led transformation signals more restructuring; recurring 'one-time' staff charges likely continue"}
  - {id: "C14", check: "F6", line: "L329-332", classification: "AMBIGUOUS", implication: "LA Olympics 'next year' vs Games scheduled Jul-2028 [external, verify]; media catalyst ~7 quarters out"}
  - {id: "C15", check: "F6", line: "L164; L166; L412", classification: "FORWARD-SIGNAL", implication: "Capex rising (cable, DC-DC, cloud, GPUs) with thin FCF; debt-funded build continues; no capex guidance or leverage ceiling"}
  - {id: "C16", check: "F7", line: "L305; L315", classification: "NEUTRAL-FACT", implication: "Voice revival hedged 'too early to say'; no forecast value"}
  - {id: "C17", check: "F7", line: "L56", classification: "NEUTRAL-FACT", implication: "'Highest since the recent M&As' limits the base and sits on the FX-aided reported basis"}
  - {id: "C18", check: "F6", line: "L132; L235", classification: "NEUTRAL-FACT", implication: "Neo cloud win unquantified, small vs 6,688 Cr quarterly revenue; order growth broad, no large wins"}
  - {id: "C19", check: "F17", line: "L177-512; L507", classification: "AMBIGUOUS", implication: "Of 31 Role 4 questions: 22 silent, 7 partial, 1 declined, 1 deflected, 0 answered; first quarter of silence; all to IR email"}
forward_signals: ["C02", "C03", "C05", "C06", "C12", "C13", "C15"]
ambiguous: ["C01", "C04", "C07", "C08", "C09", "C10", "C11", "C14", "C19"]
commitments:
  - {commitment: "Digital portfolio EBITDA breakeven/positive", implied_date: "coming quarters, no date (earliest Q3 FY27)", ref: "T002 L60; T040 L415; T050 L456", status_word: "underway"}
  - {commitment: "Double-digit EBITDA growth FY27", implied_date: "FY27", ref: "T006 L211; T050 L456", status_word: "underway"}
  - {commitment: "Constant-currency data growth visible after one more quarter", implied_date: "Q3 FY27 results (about Jan-2027)", ref: "T012 L234", status_word: "initiated"}
  - {commitment: "Order book converts to revenue", implied_date: "coming years", ref: "T012 L234; T015 L238", status_word: "underway"}
  - {commitment: "Investor call/day: long-term growth, revenue mix, internal AI transformation", implied_date: "Feb-2027", ref: "T006 L213-214; T036 L409; T040 L416", status_word: "initiated"}
  - {commitment: "CRA settlement disclosures in due course", implied_date: "undated (likely H2 FY27)", ref: "T003 L161-163", status_word: "initiated"}
  - {commitment: "Core connectivity ~45% margin achievable", implied_date: "coming quarters", ref: "T030 L364-365", status_word: "completed"}
  - {commitment: "Media cost initiatives play out", implied_date: "coming quarters", ref: "T026 L342-343", status_word: "underway"}
  - {commitment: "LA Olympics media support", implied_date: "'next year' as spoken; Games Jul-2028 [verify]", ref: "T025 L329-331", status_word: "initiated"}
  - {commitment: "More languages for SDFC Ergo voice AI", implied_date: "soon", ref: "T002 L124", status_word: "initiated"}
  - {commitment: "Internal AI-led company transformation", implied_date: "already happening; detail at investor day", ref: "T036 L408-409", status_word: "underway"}
  - {commitment: "CIS business to AI-led platform, better profitability", implied_date: "undated", ref: "T036 L407", status_word: "initiated"}
  - {commitment: "Invest in own cloud; GPU utilisation", implied_date: "in the future", ref: "T038 L411-413", status_word: "underway"}
  - {commitment: "Scale capacity in line with demand, anchor-customer-led", implied_date: "ongoing", ref: "T002 L137", status_word: "underway"}
  - {commitment: "Chief transformation officer leads transformation agenda", implied_date: "joined since last investor call", ref: "T002 L45-46", status_word: "completed"}
  - {commitment: "More unified-stack solutions", implied_date: "undated ('That is our hope')", ref: "T019 L285-286", status_word: "initiated"}
  - {commitment: "Infra leader, platform innovator; expand with profitability", implied_date: "undated", ref: "T054 L486-487", status_word: "underway"}
  - {commitment: "Disciplined capital allocation", implied_date: "undated, no ceiling", ref: "T003 L168", status_word: "underway"}
gate_a3: pass
blank_checks: []
analyst_note: "The call tells a profit-quality story on a reported basis. Two spoken numbers carry the weight: cc data growth about 6% (L152) vs 12.2% reported, and cc EBITDA about 10% (L232) vs 21.2% reported. Currency supplies roughly half the growth the CEO calls the highest since the M&As. The filing adds that half the YoY margin gain is staff and other cuts, and that non-parent sources gave about 90% of the QoQ profit rise. The call names neither, and an inferred-CFO turn says there are no one-offs (L365). The only quantified FY27 promise (double-digit EBITDA, L456) is already met by H1's 14.8%, and earlier targets were deferred to February. The CFO volunteered a favourable Canada tax settlement (L161) but said nothing on the VAT judgment due 13-Oct. That is selective disclosure, but it is one quarter, so AMBIGUOUS, not confirmatory. Pipeline note: the task brief gives DoT contingent Rs 7,513.71 Cr and review Q14 gives 7,844.57. A4 must reconcile from the filing. 'LA Olympics next year' (L330) conflicts with the 2028 Games date [external, verify]."
```
