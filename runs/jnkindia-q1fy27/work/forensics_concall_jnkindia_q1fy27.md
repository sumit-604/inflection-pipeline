# A3 FORENSIC NOTES — JNK India Limited (JNKINDIA), Q1 FY27, CONCALL

Source extract: `/home/user/inflection-pipeline/runs/jnkindia-q1fy27/work/extract_concall_jnkindia_q1fy27.txt`
Ledger: `/home/user/inflection-pipeline/runs/jnkindia-q1fy27/work/ledger_concall_jnkindia_q1fy27.md`
Prior-quarter extract: none in scope (no prior concall transcript) — QoQ verbatim diffs (F5/F15) not runnable.
Doctype live checks: **F6 (forward-commitment), F7 (hedge), F17 (silence)** primary. Balance-sheet checks
N.A. except spoken numbers contradicting the filing, routed to F14/F17 per doctype rule.

Line citations use the Read-tool line number of the extract file (transcript body lines 16-160);
turn = the transcript's embedded 1-145 numbering, per A2 ledger Methodology Note 1.

## RECONCILIATION STATEMENT
Every A2 ledger row was read verbatim at its cited extract line before judging:
Participants (16), Turns (145, incl. 2 BLANK_TURN + 1 NOT_A_TURN), Questions (44),
Mgmt Numbers (56), Forward-Commitment phrases (17), Hedge phrases (11). **Rows read / rows in ledger = 100%.**
No ledger row is un-reconciled. The A2 internal flags carried forward and adjudicated below:
`NUMBER_INCONSISTENT` (rows 14/33), `DISCLOSURE_ERROR`/`CORRECTION_MIDCALL` (turns 101-106),
`SPEAKER_AMBIGUOUS` (turn 47 TAM), `SINGLE_FOLLOWUP` (licensor), `HEDGED_FIGURE` (March unbilled).

---

## FINDINGS TABLE

| id | check | ledger row ref | line / turn | verbatim quote (short) | classification | forward implication |
|---|---|---|---|---|---|---|
| A3-F6-01 | F6 | Commit #2/#17; Num #6,#54; Q38 | line 134, turn 119 | "for our understanding what we have announced was 12 to 14%. But if for some reason we are missing something...these numbers we will recheck it" | FORWARD-SIGNAL | EBITDA guidance is 12-14% vs prior-thesis 14-15%; mgmt denies any change ("nothing has changed...remains the same", line 134) while the number itself is ~100-200bps lower. A de facto margin cut framed as continuity. Track FY27 realised margin vs 14% standalone print. |
| A3-F6-02 | F6 | Commit #1; Num #5,#20; Q1 | line 19, turn 4 | "Our revenue growth guidance of around 20 to 25% remains intact" | FORWARD-SIGNAL | Prior thesis recorded 25-30%. "Remains intact" describes a downward reset (top-end cut 500bps). Watch H2 backend (H2 = 60-70% of FY revenue, line 19) for whether even 20-25% holds. |
| A3-F6-03 | F6/F7 | Commit #16; Q44 | line 154, turn 139 | "debt raising...absolutely that's a fair conclusion but...we might need a bank guarantee limit enhancement...non-fund based limits we might need" | AMBIGUOUS | "No fund-raise 4-6 quarters" is paired with an admitted need for BG/non-fund-based limit enhancement to execute new contracts. Non-fund funding need is a real balance-sheet dependency masked by the "no debt" headline. Growth is contingent on banker BG appetite. |
| A3-F6-04 | F6 | Commit #4,#11,#14; Num #47,#50,#51; Q24,#28,#34 | line 86/124, turns 71/109 | "our expectation is by year end we should be able to get it into the green" / "revenues anywhere about 10 to 15% of JNK India's revenue...gross margins...around 20%" | FORWARD-SIGNAL | Chemdist (Rs 3.6 Cr Q1 operating loss, 8.8% of group rev) promised break-even by Mar-2027 at ~20% GM and 10-15% of revenue. Dated promise to hold mgmt to next quarter; loss is the swing factor dragging consol margin from 14% to 11.8%. |
| A3-F6-05 | F6 | Commit #12; Num #49; Q32 | line 115, turn 100 | "both refinery and fertilizer the order finalization should should happen in Q2 Q3...that's correct" | FORWARD-SIGNAL | Nigeria/Africa refinery+fertilizer export orders dated to Q2/Q3 FY27. These are the JNK-Global-routed export bids exposed to the parent litigation (A3-F7-01). Promise-vs-delivery checkpoint next quarter. |
| A3-F6-06 | F6 | Commit #7,#9; Num #8,#25,#43; Q4,#15 | line 35/64, turns 20/49 | "we expect that all these pipeline should get finalized in this financial year" / "heat ratio should be anything around 10 to 12%...not more than that" | FORWARD-SIGNAL | ~Rs 6,000 Cr pipeline (50/50 export/domestic) claimed to finalise within FY27, but new-segment hit ratio guided down to 10-12% (vs 20-25% heating). Implied FY27 order intake far below headline pipeline; conversion, not pipeline size, is the constraint. |
| A3-F6-07 | F6 | Commit #3,#15; Num #7,#52; Q35 | line 19/124, turns 4/109 | "execution would happen this year and next year both the years uniformly and...Overall EBITDA would be in line with whatever we have guided" | FORWARD-SIGNAL | BPCL Bina booked FY27+FY28. Mgmt declines to confirm the analyst's 200-300bps gross-margin uplift thesis, only "EBITDA in line" — a downgrade of the bull margin case to a neutral. |
| A3-F6-08 | F6 | Commit #5,#6; Num #21,#22,#23; Q1 | line 24, turn 9 | "another four to five years time we should be able to get a healthy mix of around 40%" | FORWARD-SIGNAL | Non-heating 40% target pushed to a 4-5 year horizon (~FY31-FY32); diversification is long-dated, not a near-term earnings driver. |
| A3-F6-09 | F6 | Commit #13; Q36 | line 129, turn 114 | "going forward yes we will be more diligent and checking for this kind of approval...any such orders we'll be testing through these parameters before we accept" | FORWARD-SIGNAL | New SOP to pre-vet licensor approval before accepting export orders. Implies future order acceptance may slow / some bids declined = order-intake friction as a control response to the cancellation. |
| A3-F7-01 | F7 | Hedge #6; Q31 | line 114, turn 99 | "though it is you know the matter is subdued we would not like to comment on that as on now" | FORWARD-SIGNAL | Activist "MJ partner" litigation at JNK Global parent (board-legitimacy challenge, in court). JNK Global supplies the BGs for Nigeria/Africa export bids and ALL export fired-heater/reformer/cracking orders route back-to-back through it (turn 53). Single-point dependency; mgmt downplays ("not comprehending any issues"). Structural risk to the entire export channel. |
| A3-F7-02 | F7 | Hedge #4,#5; Q25,#26 | line 92/94, turns 77/79 | "not officially yet renewed, but...Our understanding is it is already in force or...will automatically be continued" | AMBIGUOUS | DRHP 3-year cooperation agreement with JNK Global not formally renewed; mgmt cannot confirm status on the call ("we'll check it"). This related-party agreement governs the export back-to-back channel. Unconfirmed renewal of the instrument the export model depends on = governance gap. |
| A3-F7-03 | F7 | Hedge #7,#8; Q38,#39 | line 134/136, turns 119/121 | "if for some reason we are missing something...recheck it" / "I can share these numbers with you eventually" | AMBIGUOUS | When pressed on whether 12-14% includes other income, and on the other-income constituents (interest income, prior ESOP-cost reversal), mgmt deflects to "share eventually." The quality of the 12-14% margin (organic vs other-income supported) is unresolved. |
| A3-F7-04 | F7 | Hedge #11; Num #11,#53; Q36,#37 | line 132, turn 117 | "We cannot disclose the name of the licenser but the one which you said is not correct" | FORWARD-SIGNAL | Cancelled June-8-2026 export order: end-user's licensor (third party, NOT JNK Global) withheld technical approval; JNK later qualified but "too late." Analyst's guessed licensor name denied. Confirms export revenue carries an uncontrollable third-party-licensor gating risk; the entry barrier cuts both ways. |
| A3-F7-05 | F7 | Hedge #1; Q3 | line 26, turn 11 | "we do not have anything which we can disclose publicly...till we get...some official commitment from the client" | AMBIGUOUS | Dangote Phase 2 "still under discussion," repeat-order chance claimed but no commitment. A named catalyst with no dated progress; do not credit to pipeline until confirmed. |
| A3-F7-06 | F7 | Hedge #8,#9,#10 | line 137/141/149, turns 122/126/134 | "I can share these numbers with you eventually" / "March was also around...I'll have to check the exact number" | CONFIRMATORY-NEGATIVE | Serial deferral of hard figures — other-income breakup, contract-asset/liability composition, March unbilled comparator — all pushed to "eventually / annual report." Pattern of not having granular numbers to hand on a results call = disclosure opacity around the very lines (unbilled/contract assets) that drive earnings quality. |
| A3-F13-01 | F13 | Q12; Num (Iraq) | line 57, turn 42 | "we have kind of taken a board approval yesterday to register a branch office" (Iraq) | FORWARD-SIGNAL | Board-approved corporate action beyond the results: overseas branch registration in Iraq (currently "registered paper office," may add engineering/execution later). Foreshadows Middle-East market entry and future capex/opex; a dateable governance/expansion signal. |
| A3-F14-01 | F14 | Turns 101-106 (DISCLOSURE_ERROR); Q33 | line 120, turn 105 | "mainly profit after tax margin those numbers are more of arithmetic on the bottom few rows...that is being corrected...you will find the revised filing" | CONFIRMATORY-NEGATIVE | Published investor presentation carried a PAT-margin arithmetic error; corrected mid-call, re-filing same day. Disclosure-controls data point (immaterial in isolation, relevant cumulatively) — the reported margins were mis-stated in the primary deck this quarter. |
| A3-F14-02 | F14 | Num #12,#14,#16,#17,#33,#34,#35 (NUMBER_INCONSISTENT 14/33) | line 19/47, turns 4/32 | "the JV has contributed 8.8% to the group revenue" / standalone rev "about 170 crores...EVITA of 14%...chemist...loss of about 3.6 crores so...IITA has come down to about 11.8%" | AMBIGUOUS | Chemdist is described as a "JV" yet its revenue (8.8% of group) and Rs 3.6 Cr operating loss are line-consolidated into group P&L and used to bridge standalone 14% -> consolidated 11.8%. Line-consolidation is inconsistent with an equity-method JV label. Consol basis (subsidiary vs JV vs proportionate) needs confirmation against the Role 4 filing; it materially changes how the 8.8%/3.6 Cr flow. (Consol Rs 186 Cr = standalone Rs 170 Cr + ~Rs 16 Cr ≈ 8.8% of 186 — arithmetically ties, but only under full-line consolidation, not equity method.) |
| A3-F14-03 | F14 | Q41; Num #55,#56; turns 127-135 | line 143/147, turns 128/132 | "now we are going on the...input method. So whatever the expenses we build...revenue recognition based on that" | AMBIGUOUS | Revenue-recognition method changed from output to input method; unbilled revenue / contract assets ~Rs 200-210 Cr at Q1-end (mgmt says similar at March). Input method pulls revenue forward relative to output. Mgmt asserts "doesn't change the working capital cycle," but a rev-rec change coincident with an 80.6% YoY revenue print is an earnings-quality flag warranting the AR schedules. |
| A3-F17-01 | F17 | checklist item 1 (silence) | (absent — whole transcript) | (no operating cash-flow / CFO figure spoken anywhere in 145 turns) | CONFIRMATORY-NEGATIVE | Operating cash flow was neither disclosed nor asked, despite a rev-rec change, ~Rs 200 Cr unbilled build, and BG-limit-enhancement admission. On a WC-intensive EPC name growing 80% YoY, silence on cash conversion is the negative. |
| A3-F17-02 | F17 | checklist item 2 (silence) | (absent) | (debtor days / <180-day target never mentioned) | CONFIRMATORY-NEGATIVE | Debtor-days monitoring metric not addressed; only qualitative "friendly payment terms (Reliance, BPCL Bina)" offered (line 76). No receivables quantification given the WC intensity flagged by two analysts (Q20, Q43). |
| A3-F17-03 | F17 | checklist item 3 (silence) | (absent) | (no reference to CFO / interim CFO / permanent appointment by any speaker) | CONFIRMATORY-NEGATIVE | Permanent CFO appointment (role still interim per Notion) not mentioned by management and not asked by any of 11 analysts. Consecutive-quarter silence count = 1 on this call (prior concall out of scope). Governance open item unaddressed. |
| A3-F17-04 | F17 | checklist item 4 (partial silence); Hedge #7 | line 136, turn 121 | "can you bifocate...natural other income or operating other income...if you can highlight that" -> mgmt: "share these numbers with you eventually" | AMBIGUOUS | Whether the 12-14% margin guidance is stated on an ex-other-income basis was directly asked (Kamesh) and left unanswered. Other-income composition (interest on FDs + prior ESOP-cost reversal) not broken out. Margin-quality question survives the call unresolved. |

---

## CHECKLIST SCORECARD (all 17)

| Check | Status | Basis (one line) |
|---|---|---|
| F1 Zero-value standing items | N.A. | Concall, no balance-sheet template line items present to interrogate. |
| F2 Standalone vs Consolidated decomposition | N.A. | Balance-sheet check; spoken S-vs-C gap (Rs 186 consol vs Rs 170 standalone; 11.8% vs 14%) routed to F14-02 per doctype rule (Chemdist consolidation-label inconsistency). |
| F3 Shell-entity detection | N.A. | No standalone-vs-consolidated cost-line tables in a transcript. |
| F4 Unaudited contribution ratio | N.A. | No auditor Other-Matters paragraph in a concall. |
| F5 Going concern / EoM scope | N.A. | No EoM language spoken; no prior-quarter concall in scope for verbatim diff. |
| **F6 Forward-commitment mining** | **FINDING** | 17 dated commitments mined; 9 elevated to findings incl. margin/revenue guidance resets (A3-F6-01/02) — see Commitment Register. |
| **F7 Hedge mining** | **FINDING** | 11 hedges; litigation non-comment, cooperation-agreement non-renewal, margin recheck, licensor non-disclosure, serial figure deferrals (A3-F7-01..06). |
| F8 Tax forensics | N.A. | No ETR / deferred-tax / prior-year tax-adjustment figures spoken. |
| F9 OCI forensics | N.A. | No OCI / actuarial figures in transcript. |
| F10 Share count & dilution | N.A. | No paid-up capital / EPS figures spoken. ESOP-cost reversal mention (turn 121) captured under other-income (A3-F17-04); no share-count data to analyse. |
| F11 Reserves & net-worth tie-out | N.A. | No equity / net-worth figures spoken. |
| F12 Segment forensics | N.A. | No segment asset/liability tables in a transcript (heating/non-heating discussed qualitatively only). |
| **F13 Board outcome beyond results** | **FINDING** | Board approval "yesterday" to register Iraq branch office (A3-F13-01); no AGM/AR/dividend resolution mentioned. |
| **F14 Note drafting inconsistencies** | **FINDING** | Mid-call PAT-margin arithmetic error + re-filing (A3-F14-01); Chemdist "JV" label vs line-consolidation (A3-F14-02); output->input rev-rec change (A3-F14-03). |
| F15 Entity list diffs | N.A. | No prior-quarter concall in scope; no consolidation list in transcript to diff. |
| F16 Presentation dropped/reframed disclosures | N.A. | Doctype is concall, not the deck; guidance softening (14-15->12-14, 25-30->20-25) captured under F6/F17, not F16. |
| **F17 Silence audit** | **FINDING** | Operating CFO (A3-F17-01), debtor days (A3-F17-02), permanent CFO appointment (A3-F17-03) all unaddressed; margin/other-income treatment deflected (A3-F17-04). See "What Was NOT Discussed". |

No check left blank. **GATE A3 = PASS.**

---

## WHAT WAS NOT DISCUSSED (F17 silence audit vs Notion checklist + F6 commitments)

| # | Monitoring item | Discussed? | Evidence / silence | Consecutive Qtrs silent | Note |
|---|---|---|---|---|---|
| 1 | Operating cash flow this quarter | NO | No CFO figure in any of 145 turns | 1 (prior concall out of scope) | CONFIRMATORY-NEGATIVE — A3-F17-01. Never volunteered, never asked. |
| 2 | Debtor days <180 | NO | Only qualitative "friendly payment terms" (line 76) | 1 | CONFIRMATORY-NEGATIVE — A3-F17-02. |
| 3 | Permanent CFO appointment (interim) | NO | Zero references to CFO role/appointment | 1 | CONFIRMATORY-NEGATIVE — A3-F17-03. No analyst asked. |
| 4 | EBITDA margin floor / 12-14 vs 14-15; other-income inclusion | PARTIAL | Guidance stated 12-14% (line 19); change challenged (line 133), other-income treatment deflected (line 136) | n/a | FINDING A3-F6-01 + A3-F17-04. Change denied; quality unresolved. |
| 5 | Revenue guidance (25-30 prior vs 20-25 now) | YES | "20 to 25%...remains intact" (line 19, 22) | n/a | FINDING A3-F6-02 — downward reset framed as continuity. |
| 6 | Dangote Phase 2 | YES | "still under discussion...good chance...cannot disclose" (line 26) | n/a | Hedge A3-F7-05. No dated progress. |
| 7 | Order cancellation / licensor | YES | Raised unprompted (line 19); licensor withheld approval; name undisclosed, guess denied (line 132) | n/a | FINDING A3-F7-04 — licensor-dependency signal. |
| 8 | BPCL Bina execution FY27+FY28 | YES | "recognized during FY27 and also on FY28" / "uniformly" (line 19, 124) | n/a | Confirmed. A3-F6-07. Margin uplift NOT confirmed. |
| 9 | JNK Global structural role | YES | Export routed back-to-back through JNK Global; incinerators/flares direct; 4 projects (line 66, 68) | n/a | Structural dependency documented; feeds A3-F7-01. |
| 10 | Activist "MJ partner" litigation at JNK Global | YES | "matter is subdued we would not like to comment" (line 114) | n/a | FINDING A3-F7-01 — downplayed; BG channel risk. |
| 11 | Chemdist loss/break-even/margin | YES | 3.6 Cr loss, 8.8% rev, green by year-end, 10-15% rev, ~20% GM (line 47, 86, 124) | n/a | FINDING A3-F6-04. |
| 12 | Working capital / BG / no-raise / unbilled ~200 Cr | YES | Friendly terms; JNK Global BGs; no raise 4-6 qtrs but BG-limit enhancement needed; unbilled ~200-210 Cr (line 76, 147, 154) | n/a | FINDING A3-F6-03 (BG dependency) + A3-F14-03 (rev-rec). Operating cash NOT quantified (item 1). |
| 13 | New-business hit ratio 10-12% | YES | "heat ratio...10 to 12%...not more than that" (line 64) | n/a | A3-F6-06 — conversion is the constraint. |
| 14 | Cooperation agreement renewal | YES | "not yet renewed...automatically be continued" (line 92, 94) | n/a | FINDING A3-F7-02 — governance gap. |

---

## COMMITMENT REGISTER (F6 — seeds next-quarter promise-vs-delivery tracker)

| # | Commitment | Implied date | Note / turn ref | Status word |
|---|---|---|---|---|
| 1 | Revenue growth ~20-25% | FY27 (full year) | Commit #1, turn 4 / line 19 | reaffirmed ("remains intact") — but reset down from prior 25-30 |
| 2 | EBITDA margin ~12-14% | FY27 (full year) | Commit #2/#17, turns 4/119 / line 19,134 | reaffirmed — but 100-200bps below prior 14-15 (A3-F6-01) |
| 3 | BPCL Bina revenue recognition | FY27 and FY28 | Commit #3/#15, turns 4/109 / line 19,124 | underway ("execution is underway") |
| 4 | Chemdist operating leverage to improve | H2 FY27 onward | Commit #4, turn 4 / line 19 | anticipated |
| 5 | Non-heating -> ~40% of revenue | 3-5 yrs (~FY30-FY32) | Commit #5, turn 9 / line 24 | target / in progress |
| 6 | Non-heating 40% healthy mix | "another 4-5 years" (~FY31-32) | Commit #6, turn 9 / line 24 | anticipated |
| 7 | ~Rs 6,000 Cr pipeline finalisation | within FY27 (3-6 / 6-8 mo) | Commit #7, turn 20 / line 35 | expected |
| 8 | Maintain 12-14% margin on new business | ongoing | Commit #8, turn 46 / line 61 | intends |
| 9 | New-segment hit ratio ~10-12% | "next couple of years" (FY27-28) | Commit #9, turn 49 / line 64 | expected |
| 10 | Iraq sales-office build-out | going forward (post board approval) | Commit #10, turn 56 / line 71 | board approved (registration) — A3-F13-01 |
| 11 | Chemdist "into the green" (break-even) | by year-end (Mar 2027) | Commit #11, turn 71 / line 86 | expected |
| 12 | Refinery & fertilizer order finalisation | Q2/Q3 FY27 | Commit #12, turn 100 / line 115 | expected |
| 13 | SOP to pre-vet licensor approvals | going forward | Commit #13, turn 114 / line 129 | being incorporated |
| 14 | Chemdist ~10-15% of JNK revenue | FY27 / next couple years | Commit #14, turn 109 / line 124 | expected |
| 15 | BPCL Bina uniform execution, EBITDA in line | FY27 + FY28 | Commit #15, turn 109 / line 124 | underway |
| 16 | No significant debt/equity raise | next 4-6 quarters (~to FY28) | Commit #16, turn 139 / line 154 | guided/agreed — caveated by BG-limit enhancement need (A3-F6-03) |
| 17 | Margin projection unchanged | FY27 | Commit #17, turn 119 / line 134 | reaffirmed — contradicts 14-15 prior (A3-F6-01) |

---

## A4 HAND-OFF — QUESTIONS TO CONVERT (FORWARD-SIGNAL + AMBIGUOUS)
Forward-signal: A3-F6-01, A3-F6-02, A3-F6-04, A3-F6-05, A3-F6-06, A3-F6-07, A3-F6-08, A3-F6-09, A3-F7-01, A3-F7-04, A3-F13-01.
Ambiguous (lean-bear, generate question): A3-F6-03, A3-F7-02, A3-F7-03, A3-F7-05, A3-F14-02, A3-F14-03, A3-F17-04.
Priority pairing for management questions: (i) margin guidance 14-15 -> 12-14 with other-income basis [F6-01+F17-04];
(ii) JNK Global litigation + unrenewed cooperation agreement vs 100% export back-to-back dependency [F7-01+F7-02];
(iii) input-method rev-rec change + ~200 Cr unbilled vs unquantified operating cash flow [F14-03+F17-01].

```yaml
stage: A3-forensics
company: "JNKINDIA"
quarter: "Q1 FY27"
doctype: "concall"
model: claude-opus-4-8
status: complete
forensics_path: "/home/user/inflection-pipeline/runs/jnkindia-q1fy27/work/forensics_concall_jnkindia_q1fy27.md"
ledger_reconciled_pct: 100
checklist:
  F1: N.A.
  F2: N.A.
  F3: N.A.
  F4: N.A.
  F5: N.A.
  F6: FINDING
  F7: FINDING
  F8: N.A.
  F9: N.A.
  F10: N.A.
  F11: N.A.
  F12: N.A.
  F13: FINDING
  F14: FINDING
  F15: N.A.
  F16: N.A.
  F17: FINDING
findings:
  - {id: "A3-F6-01", check: "F6", line: "134/turn119", classification: "FORWARD-SIGNAL", implication: "EBITDA guidance 12-14% vs prior 14-15%; change denied while number is lower"}
  - {id: "A3-F6-02", check: "F6", line: "19/turn4", classification: "FORWARD-SIGNAL", implication: "Revenue 20-25% 'intact' is a downward reset from 25-30%"}
  - {id: "A3-F6-03", check: "F6", line: "154/turn139", classification: "AMBIGUOUS", implication: "'No raise' paired with admitted BG/non-fund-limit enhancement need"}
  - {id: "A3-F6-04", check: "F6", line: "86/turn71", classification: "FORWARD-SIGNAL", implication: "Chemdist break-even by Mar-2027, 10-15% rev, 20% GM — dated promise"}
  - {id: "A3-F6-05", check: "F6", line: "115/turn100", classification: "FORWARD-SIGNAL", implication: "Refinery+fertilizer export orders dated Q2/Q3 FY27, JNK-Global exposed"}
  - {id: "A3-F6-06", check: "F6", line: "64/turn49", classification: "FORWARD-SIGNAL", implication: "New-segment hit ratio 10-12% vs 20-25% — conversion is the constraint"}
  - {id: "A3-F6-07", check: "F6", line: "124/turn109", classification: "FORWARD-SIGNAL", implication: "BPCL Bina 'EBITDA in line'; 200-300bps GM uplift not confirmed"}
  - {id: "A3-F6-08", check: "F6", line: "24/turn9", classification: "FORWARD-SIGNAL", implication: "Non-heating 40% pushed to 4-5yr horizon; not near-term"}
  - {id: "A3-F6-09", check: "F6", line: "129/turn114", classification: "FORWARD-SIGNAL", implication: "New licensor-approval SOP may slow future order acceptance"}
  - {id: "A3-F7-01", check: "F7", line: "114/turn99", classification: "FORWARD-SIGNAL", implication: "JNK Global activist litigation vs 100% export back-to-back BG dependency; downplayed"}
  - {id: "A3-F7-02", check: "F7", line: "92/turn77", classification: "AMBIGUOUS", implication: "DRHP cooperation agreement not formally renewed; status unconfirmed on call"}
  - {id: "A3-F7-03", check: "F7", line: "134/turn119", classification: "AMBIGUOUS", implication: "Margin 'recheck' hedge; other-income inclusion unresolved"}
  - {id: "A3-F7-04", check: "F7", line: "132/turn117", classification: "FORWARD-SIGNAL", implication: "Export orders gated by uncontrollable third-party licensor approval"}
  - {id: "A3-F7-05", check: "F7", line: "26/turn11", classification: "AMBIGUOUS", implication: "Dangote Phase 2 no dated progress; do not credit to pipeline"}
  - {id: "A3-F7-06", check: "F7", line: "137/turn122", classification: "CONFIRMATORY-NEGATIVE", implication: "Serial deferral of other-income/contract-asset/March-unbilled figures = opacity"}
  - {id: "A3-F13-01", check: "F13", line: "57/turn42", classification: "FORWARD-SIGNAL", implication: "Board-approved Iraq branch registration — overseas expansion signal"}
  - {id: "A3-F14-01", check: "F14", line: "120/turn105", classification: "CONFIRMATORY-NEGATIVE", implication: "PAT-margin arithmetic error in published deck, re-filed same day"}
  - {id: "A3-F14-02", check: "F14", line: "47/turn32", classification: "AMBIGUOUS", implication: "Chemdist 'JV' label vs line-consolidation of its rev/loss; consol basis unclear"}
  - {id: "A3-F14-03", check: "F14", line: "143/turn128", classification: "AMBIGUOUS", implication: "Output->input rev-rec change + ~200 Cr unbilled; earnings-quality flag"}
  - {id: "A3-F17-01", check: "F17", line: "absent", classification: "CONFIRMATORY-NEGATIVE", implication: "Operating cash flow never disclosed or asked despite WC intensity"}
  - {id: "A3-F17-02", check: "F17", line: "absent", classification: "CONFIRMATORY-NEGATIVE", implication: "Debtor days (<180 target) not addressed"}
  - {id: "A3-F17-03", check: "F17", line: "absent", classification: "CONFIRMATORY-NEGATIVE", implication: "Permanent CFO appointment unmentioned; no analyst asked"}
  - {id: "A3-F17-04", check: "F17", line: "136/turn121", classification: "AMBIGUOUS", implication: "Whether 12-14% margin is ex-other-income deflected"}
forward_signals: ["A3-F6-01","A3-F6-02","A3-F6-04","A3-F6-05","A3-F6-06","A3-F6-07","A3-F6-08","A3-F6-09","A3-F7-01","A3-F7-04","A3-F13-01"]
ambiguous: ["A3-F6-03","A3-F7-02","A3-F7-03","A3-F7-05","A3-F14-02","A3-F14-03","A3-F17-04"]
commitments:
  - {commitment: "Revenue growth ~20-25%", implied_date: "FY27", ref: "turn4/line19", status_word: "reaffirmed"}
  - {commitment: "EBITDA margin ~12-14%", implied_date: "FY27", ref: "turn4/119/line19", status_word: "reaffirmed"}
  - {commitment: "BPCL Bina revenue recognition", implied_date: "FY27-FY28", ref: "turn4/line19", status_word: "underway"}
  - {commitment: "Chemdist operating leverage to improve", implied_date: "H2 FY27+", ref: "turn4/line19", status_word: "anticipated"}
  - {commitment: "Non-heating to ~40% of revenue", implied_date: "3-5yrs (~FY30-32)", ref: "turn9/line24", status_word: "in-progress"}
  - {commitment: "Non-heating 40% healthy mix", implied_date: "~4-5yrs", ref: "turn9/line24", status_word: "anticipated"}
  - {commitment: "Rs 6,000 Cr pipeline finalisation", implied_date: "FY27", ref: "turn20/line35", status_word: "expected"}
  - {commitment: "Maintain 12-14% margin new business", implied_date: "ongoing", ref: "turn46/line61", status_word: "intends"}
  - {commitment: "New-segment hit ratio ~10-12%", implied_date: "FY27-28", ref: "turn49/line64", status_word: "expected"}
  - {commitment: "Iraq sales-office build-out", implied_date: "going-forward", ref: "turn56/line71", status_word: "board-approved"}
  - {commitment: "Chemdist break-even into the green", implied_date: "Mar-2027", ref: "turn71/line86", status_word: "expected"}
  - {commitment: "Refinery & fertilizer order finalisation", implied_date: "Q2/Q3 FY27", ref: "turn100/line115", status_word: "expected"}
  - {commitment: "SOP to pre-vet licensor approvals", implied_date: "going-forward", ref: "turn114/line129", status_word: "being-incorporated"}
  - {commitment: "Chemdist ~10-15% of JNK revenue", implied_date: "FY27/next-couple-yrs", ref: "turn109/line124", status_word: "expected"}
  - {commitment: "BPCL Bina uniform execution, EBITDA in line", implied_date: "FY27-FY28", ref: "turn109/line124", status_word: "underway"}
  - {commitment: "No significant debt/equity raise", implied_date: "next 4-6 quarters", ref: "turn139/line154", status_word: "guided"}
  - {commitment: "Margin projection unchanged", implied_date: "FY27", ref: "turn119/line134", status_word: "reaffirmed"}
gate_a3: pass
blank_checks: []
```
