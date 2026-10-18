# A3 FORENSIC NOTES: Cyient DLM (CYIENTDLM) Q2 FY27, doctype CONCALL (call 15 October 2026)

Agent: A3 forensic notes, model claude-opus-5-5. Run date 2026-10-18.
Inputs read: A1 structured extraction `extracted/cyientdlm-concall-q2fy27-structured.md` (R001-R303, T001-T097); A1 fulltext `extracted/cyientdlm-concall-q2fy27-fulltext.md` (488 lines); A2 ledger `work/ledger_concall_cyientdlm_q2fy27.md`; review `work/review_cyientdlm_q2fy27.md` lines 527-571 (Step 8.5 table only). Prior-quarter transcript: NOT AVAILABLE. Source PDF and `inputs/`: not opened.

SOURCE CAVEAT (binds every row below). The text is a faster-whisper MACHINE transcript (fulltext L20). Speakers are INFERRED by A1. Numbers and names may be misheard. Where a spoken figure conflicts with the filing, the filing wins, and doubts about misheard numbers are classed AMBIGUOUS, not management error. Filing figures quoted here come only from the injected Notion checklist and the review's Step 8.5 table. A3 did not read the filing.

[INFERENCE] marks arithmetic A3 ran on figures spoken on the call. No missing number is estimated; NOT FOUND is used where the call is silent.

---

## 0. LEDGER RECONCILIATION

- Rows in ledger: 303 (R001-R303), plus 97 turns (T001-T097). Rows read at the cited fulltext line: 303 of 303. ledger_reconciled_pct = 100.
- Verbatim match at the cited line: 301 of 303 rows. The two exceptions are anchor defects. Neither changes a value.
  - R294 ("we don't publish the numbers of what is for each year"). Ledger and A1 cite line 450 / T086 (a moderator line: "You are in Audible sir."). The quote is at **line 454**, turn **T088** (CFO inferred).
  - R177 context says "BLM Electronics Inc" is at line 413. It is at **line 437** (R196). Line 413 is the micro VCS question.
- A1 turn table, `cue` column: the cue line numbers ("line 8", "line 39 hands to Rajendra", "line 163 opens Q&A") are SOURCE-file line numbers, not fulltext lines. The turn line RANGES are correct. Hygiene only.
- Spoken internal variances, verbatim, recorded and not resolved: one-time reversal Rs 182 Mn (L133, L142, L163) vs Rs 183 Mn (L173); Box Build growth 86% (L111, CEO) vs 85% (L153, CFO); "EBITDA for the first year" (L169) is machine text for first half (the figure Rs 733 Mn ties to H1).
- Call arithmetic that ties [INFERENCE]: EBITDA 342/3,931 = 8.70% (L129); Q2 FY26 EBITDA 342/1.095 = Rs 312.3 Mn on Rs 3,106 Mn = 10.06%, so the decline is 135 bps (L130 ties). H1 EBITDA 733/7,669 = 9.56% (L170). Q1 FY27 by subtraction: EBITDA Rs 391 Mn on revenue Rs 3,738 Mn = 10.46%. Normalized PAT 158 = reported 340 minus 182 (L161-L164). Order book 28.1 minus 26.0 = 2.1 bn (L127, L148).

---

## 1. FINDINGS TABLE

| id | check | ledger row ref | line / turn | short verbatim quote | classification | forward implication |
|---|---|---|---|---|---|---|
| CF01 | F6 | R211, R102, R218, R106, R221, R112 | L103 (T003), L230 (T015), L244 (T021), L266 (T031) | "maybe close to around 9% EBITDA margin" (L230); "9% to 10% range. So, that is what we have currently in the guidance" (L244) | FORWARD-SIGNAL | H1 ran at 9.56% (Rs 733 Mn on Rs 7,669 Mn, L168-L170). A FY27 print of 9.0% needs an H2 EBITDA margin of about 8.4-8.6% [INFERENCE: H2 revenue between 1.0x and 1.3x H1]. That is BELOW Q2's 8.7%. The 10% top end needs H2 at about 10.3-10.4%. The point guidance ("close to around 9%") implies no H2 recovery. It conflicts with "intensity of investments will get kind of lower from Q3 or Q4" (L295) and the no-new-S&M pledge (L288). The band is 2 points wide in H2 terms. Q: which end, and what holds H2 below Q2? |
| CF02 | F6 | R204, R206, R013, R203, R011, R225, R160, R248 | L82, L86 (T003); L266 (T031); L476 (T096) | "from FY27 through FY29, we plan to apply this proven stat to new sectors" (L82); "the margin framework for this phase is approximately 11 to 13%" (L86); "into FY28, that itself will take our margins into 10 plus percent" (L476) | FORWARD-SIGNAL | The EXPAND phase starts in FY27 with an 11-13% framework. FY27 guidance is 9-10% and FY28 is "double digits" / "10 plus". On management's own dates the band cannot be entered before FY29, the last year of the phase. The "margin framework" metric is never named as EBITDA (L78, L86, L96). This answers review Q5 only in part. Role 5 anchor: FY28 >=10% EBITDA. |
| CF03 | F17 (Notion test 2) | R300, R299, R114 | L158 (T004, CFO); L282-L284 (T039, chairman INFERRED) | "First, we saw an impact from the revenue mix and certain product development related costs" (L158) vs "So, it's not the revenue mix" (L284); "even this quarter if you compare it to the same quarter last year, our contribution margin is still higher" (L283) | AMBIGUOUS (bear lean) | The Notion checklist has Q2 gross margin at 37.41%, down 381 bps YoY (filing). The chairman says gross and contribution margin are "significantly higher in FA27 by a year to date" (L282) and higher even in Q2 YoY. The filing wins on gross margin. "Contribution margin" is undefined and could be a non-GAAP measure on another basis. Two management speakers give opposite causes in the same call. Review Q4 records that the filed opex ratio FELL 245 bps YoY. The call's YoY story (gross margin up, opex up) is the reverse of the filing (gross margin down 381, opex ratio down 245). No component-cost explanation is given. Q: define contribution margin and reconcile it with the 381 bps gross margin fall. |
| CF04 | F6 | R101, R114, R116, R141 | L199 (T007), L231 (T015), L287, L290, L291 (T039) | "This is in the range of 100 to 150 basis points" (L199); "the drop in margins by about 100 bps or so" (L287); "which is almost a 150-200 basis point" (L290); "some of these one-offs" (L231) vs "it's not a one-off thing" (L291) | AMBIGUOUS | Three sizes for the same investment drag: 100-150, ~100 and 150-200 bps. The product development cost is a "one-off" at L231 and "not a one-off thing" at L291. The actual YoY fall is 135 bps (L130). If S&M absorption alone costs 150-200 bps, the residual business would have expanded margin. That contradicts the filed 381 bps gross margin fall (CF03). The drag that is meant to reverse in FY28 has no fixed size, so the FY28 recovery claim cannot be tested. |
| CF05 | F6 | R226, R228, R115 | L288 (T039), L297 (T040) | "we won't add any more sales and marketing costs till we hit at least double our revenue on a quarterly basis" (L288); "There will not be any future investment in that area" (L297) | FORWARD-SIGNAL | This is a hard and testable pledge. Q2 quarterly revenue is Rs 3,931 Mn (L126), so the S&M freeze holds until about Rs 7,862 Mn a quarter [INFERENCE: 2x]. Tripwire for Role 5: any QoQ rise in S&M employee cost or selling expense before that level breaks the pledge. Speaker is INFERRED (chairman, T039); attribution of the pledge carries that caveat. |
| CF06 | F6 | R117, R227, R265 | L293-L294 (T039/T040); audio gap [00:40:00]-[00:40:30] | "The margin expansion will happen of around 200 basis points." (L294) | AMBIGUOUS | This statement follows a 30-second audio gap (L293 at 40:00, L294 at 40:30; A2 MISSING_FROM_STRUCTURED note). Base, metric and year are lost. If it means 200 bps on FY27's ~9%, it implies ~11% (inside the EXPAND band). If it means the absorption of 150-200 bps (L290), it restates the FY28 "10 plus" claim. Q: 200 bps on what base, by which year? |
| CF07 | F17 (Notion test 4) | R140, R230, R233, R239, R241, R145, R147, R148, R175 | L376 (T061, analyst); L382-L394 (T062); L308, L317 (T042/T046); L411 (T064); L428-L429 (T071); L91 (T003) | "we had mentioned that B2S sales contribution should be in double digit in F527" (L376, analyst); reply: "Built Respect Division is where we are now renamed as a Product Division" (L382); "So FY29 probably it may start. So FY30 onwards is where you will be seeing the full production" (L428-L429) | FORWARD-SIGNAL (bear) | The analyst put the prior FY27 double-digit B2S share target to management. The reply (L382-L394) covers lifecycle and expensing and gives no share. The target is neither confirmed nor withdrawn. A3 cannot verify the prior guidance (no prior transcript). In the same call, B2S revenue moves from "by FY30" (L308) to "from FY 29" (L411) to "FY29 probably it may start" (L428). B2S was renamed "Electronic Products" (L91). On management's own timeline, the share leg of the proof gate (double-digit B2S share for two quarters) cannot fire before FY29-FY30 [INFERENCE]. Q: Q2 B2S share (review Q16), and is the FY27 double-digit target withdrawn? |
| CF08 | F6 | R120, R121, R146, R289, R291, R292, R240, R290, R149 | L307, L309, L313 (T042/T044); L409-L410 (T064); L427 (T071); L327 (T051); L431 (T073) | "we already have some of the contracts signed" (L307); "the contracts have been signed, but it is not there in our order book" (L409) vs "few other things are contract signed and few will be contract signed once it comes to a stage" (L427) | AMBIGUOUS | The "close to $1 billion" across four programmes (L309) is outside the order book. Only "a part" of it is in the pipeline (L327). By L427 it is only partly signed, and it books only after design and prototype testing (L410). It spans "7 to 9 years" (L431), so at full run-rate it is about $111-143 Mn a year [INFERENCE: straight-line $1 bn / 9 to 7 yrs]. Its first revenue is FY29-FY30. Q: signed value vs unsigned value of the $1 bn. |
| CF09 | F6 | R002, R126, R127, R131, R132, R287, R109, R128 | L33 (T002); L331-L333 (T051); L338-L339 (T053); L262 (T029) | "we were close here on 1.4 billion dollars. Now it is in the range what we said more than a billion dollars" (L331) vs "1.5 billion dollars roughly which is the unweighted pipeline ... So, 1.5 which has increased" (L338-L339) | AMBIGUOUS (machine transcript) | The CEO's wording implies the pipeline FELL from $1.4 bn to just over $1 bn. The chairman says it ROSE to $1.5 bn. The 40% win ratio (L262) on $1.5 bn gives $600 Mn [INFERENCE], against a stated $400-500 Mn order impact (L332-L333). The direction of the pipeline (the feeder the chairman tells investors to watch, L348) is unresolved. Q: pipeline at 30-Jun and 30-Sep, on one basis. |
| CF10 | F17 (Notion test 3) | R004, R015, R107, R108, R223 | L36 (T002); L106 (T003); L255-L256 (T025) | "our book-to-bill ratio remained at over 1.6 times" (L36); "close to 600 crores plus, that's where probably you will be expecting it for the next two quarters too" (L256) | AMBIGUOUS | Review Q15: the book walk gives Q2 intake of Rs 6,079 Mn, which is 1.55x on Rs 3,931 Mn revenue, not "over 1.6x". The spoken "600 crores plus" intake fits the Rs 6,079 Mn walk. The ratio claim does not. The filing-based walk wins, so Notion test 3 should read 1.55x on the book walk. The 600 Cr per quarter run-rate for Q3-Q4 FY27 goes into the commitment register. |
| CF11 | F6 | R222, R103, R153, R047, R166, R213, R236 | L39 (T002); L248-L251 (T023); L356 (T055); L148 (T004); L481 (T096) | "due to all the challenges in getting the materials ... that's why the 18 to 24 months" (L248-L251); "it is all depending upon the availability of the material" (L356); "Inventory days remain stable at 162 days" (L148) | FORWARD-SIGNAL | The order book grows faster than revenue because of component supply ("memory market", L39). The H2 >30% growth pledge (L361) and the 600 Cr intake both run through the same constraint. Inventory stays at 162 days. The chairman's "we're over all the challenges that we had last year" (L481) conflicts with the CEO's L248 and L356. No NWC target or date is given, so Notion test 1 (NWC <=120 days by Q4 FY27) has no management anchor. Q3 test: does growth recover to >30% while inventory days fall? |
| CF12 | F17 (Notion test 6) | R032, R041, R077, R092, R280-R284, R158, R159, R301, R086, R087, R090, R091 | L133, L163, L173 (T004); L462-L465 (T091/T092) | "the one-time reversal of the earned provisions of Rs. 182 million" (L133); analyst: "we should understand that in during Q2 there will be other income or this is one of?" (L463); CFO: "There are forex variations ... some export incentives is also part of it. So every quarter it keeps varying." (L464-L465) | FORWARD-SIGNAL (bear) | The CFO put the Rs 182 Mn reversal in other income (L163). Asked directly whether the 23 Cr Q2 other income recurs, he named forex and export incentives and did not mention the reversal. On the call's own figures the reversal is about 79% of the analyst's 23 Cr [INFERENCE: 18.2/23]. H1 arithmetic: reported H1 PAT Rs 503 Mn up 27% gives H1 FY26 about Rs 396 Mn. Normalized Rs 321 Mn up 60.4% gives about Rs 200 Mn. So H1 FY26 carried about Rs 196 Mn of normalization [INFERENCE from L171-L172], similar in size to this year's "one-time" Rs 182 Mn. This supports review Q1 ("recurs each Q2"). "One-time" is the label on what looks like a second annual write-back. The variance 182 vs 183 (L173) is a misspeak or mishearing; the filing figure of 181.95 Mn (review Q1) wins. |
| CF13 | F17 (Notion test 6) | R176, R177, R196, R242 | L114 (T003); L437-L439 (T077) | "we completed the integration of Altec Electronics and renamed the business" (L114); "that business is currently doing as per our plans" (L438) | FORWARD-SIGNAL (bear) | An earnout write-back means the expected payout fell, which means the acquired unit is tracking below the earnout targets. The Notion checklist puts US arm EBITDA at 1.17% and loss-making ex-earnout. "As per our plans" conflicts with both. The filing wins. The call gives no subsidiary revenue or EBITDA (review Q3 unanswered). Forward: the FY27 impairment test of goodwill Rs 730.94 Mn plus intangibles Rs 447.97 Mn (review Q11) runs on forecasts that management describes as on-plan while the earnout says otherwise. |
| CF14 | F17 | R073, R074, R097 | L160 (T004); L179 (T004) | "finance costs declined by 10.4% year-on-year to Rs. 61 million, supported by lower working capital borrowings" (L160) | FORWARD-SIGNAL | The YoY claim may hold. The call is silent on the H1 FY27 build: consolidated borrowings rose to Rs 1,319.60 Mn from Rs 1,061.25 Mn, and standalone took Rs 287.91 Mn of new short-term debt (review Q7, Q10). Finance cost is likely to rise QoQ from Q3 [INFERENCE, as review Q10]. Q3 test: finance cost above Rs 61 Mn. |
| CF15 | F17 (Notion test 1) | R050, R051, R052 | L149 (T004) | "Customer advances stood at 13 days compared to 15 days in the previous quarter." (L149) | FORWARD-SIGNAL | Only the sequential comparison is given. Review Q8: advance days fell from 33 to 13 YoY. Falling customer advances on a rising book means each new rupee of revenue needs more working capital, which works against the Notion cash falsifier. Silence on the YoY figure: 1 quarter counted (prior transcript NOT AVAILABLE). |
| CF16 | F17 (Notion test 1) | R052 | L149 (T004) | "helped us generate an operating free cash flow of Rs 172 million during the quarter" (L149) | AMBIGUOUS | The cash figure is Q2-only and undefined. Review Q12: H1 consolidated CFO minus capex is Rs 4.11 Mn, which puts Q1 near Rs (168) Mn on that basis. The call gives no H1 cash figure and no definition (review Q12, Q13 unanswered). |
| CF17 | F17 | R171, R053-R060, R167-R170 | L76 (T003); L41 (T002); L151-L152 (T004) | "automotive focused in electric vehicles" listed as a core industry (L76); "We are seeing positive growth across all key segments." (L41) | FORWARD-SIGNAL (bear) | The CFO's Q2 industry mix (L151-L152) is aerospace 47%, industrial 31%, defence 7%, Med Tech 14%, which sums to 99%. Automotive is not named. Back-solving the stated shares and growth rates gives the residual (Auto & Others) as about 1% of Q2 revenue against about 9-10% in Q2 FY26 [INFERENCE; integer-% rounding gives a wide band; review Q30 has the aggregate]. One of the four named core industries appears to have shrunk, and the call never mentions it. The "all key segments" growth claim (L41) does not hold for it. Review Q30: silent. |
| CF18 | F7 | R215, R245, R246, R010, R205, R220, R244 | L215-L217 (T009); L460-L461 (T090); L69, L83 (T003); L238 (T017) | "on the other two areas ... we just started exploring it right now. And it may take some time for us to get to a number there." (L215-L216) | FORWARD-SIGNAL | Hedge hit "exploring", twice (L215, L460). The prepared remarks size AI and data centre at "$58 billion" (L69) and put robotics and AI DC into the FY27-29 EXPAND phase (L82-L83). In Q&A both are at the "just started exploring" stage, with no revenue, pipeline or date before the end of FY27 (L217, L461). Semicap has revenue "in the last two quarters" (L238), unquantified. Two of the three new-industry legs of the EXPAND phase are narrative only today. Due date: Q4 FY27 call. |
| CF19 | F7 | R137, R145, R147, R201 | L354 (T055); L411, L428 (T064/T071) | "now probably yes, you will be getting that much of the growth" (L354); "probably you'll be seeing the revenues coming in for us from FY 29" (L411) | NEUTRAL-FACT | Hedging words ("probably", "may start") sit on the FY27 growth figure and the B2S start year. The lexicon gave no hits for "no assurance", "in discussions" or "endeavour". The only "subject to" is the boilerplate safe-harbour (L30). The hit at L164 ("Exploring this") is machine text for "Excluding". Logged for the promise tracker; spoken hedges are weaker evidence than note hedges. |
| CF20 | F6 | R285, R286, R297, R298, R295, R296 | L389-L391 (T062); L473 (T096); L205, L208 (T007) | "what we have the option is to calculate some of the costs, which we have chosen not to do it because from a pure conservatism principle" (L389-L390) | AMBIGUOUS | Expensing all product development is conservative today. But the option to capitalise is kept and the spend is not disclosed (L205, L208). A later switch to capitalising would lift reported EBITDA. It could supply the >=100 bps uplift in the proof gate through accounting alone. Tripwire: any change in capitalisation policy or new intangibles under development before FY28. |
| CF21 | F6 | R191, R192, R193, R302 | L404-L407 (T064); L420 (T066) | "some modifications, engineering changes were happening. That's where it has took some time to just bring it back into the serial production." (L406-L407) | AMBIGUOUS | The Honeywell programme is build-to-print (L404, L420), not B2S, so the analyst's high-margin framing (L400-L403) is wrong. Serial production has slipped because of engineering changes, and no date is given. The "800 airbuses" figure is the analyst's, not management's (L402). Q: serial production date. |
| CF22 | F15 | R176, R177, R196 | L114 (T003); L437 (T077) | "renamed the business as Sign DLM Electronics Inc." (L114, machine text); "we just renamed that as BLM Electronics Inc." (L437) | NEUTRAL-FACT | Entity rename: Altec Electronics to Cyient DLM Electronics Inc. (machine text varies). The call gives no date and no earnout terms. Review Q28 is already open. No prior-quarter entity list was available for a full diff. |
| CF23 | F6 | R235, R236, R137, R139, R016 | L354, L361 (T055); L108 (T003) | "if you look at for the H2, we will definitely be going above 30% growth" (L361) | NEUTRAL-FACT | FY27 revenue growth of 30-35% (the analyst offered the figure and management accepted it, L353-L354), with H2 above 30%. Q2 grew 26.5% (L108). This answers review Q19. Q3 test: YoY growth >=30%. A second print below 30% would be the first miss on a dated pledge (CF11 names the constraint). |
| CF24 | F6 | R219, R261 | L231 (T015) | "I think from the Q1 onwards, we will be having a double-digit EBITDA margin." (L231) | AMBIGUOUS | Q1 FY27 already printed 10.46% [INFERENCE: (733-342)/(7,669-3,931)]. So this is either a Q1 FY28 pledge or a mishearing. If it is Q1 FY28, it is the earliest dated double-digit quarter, and the first quarter of the proof-gate margin leg. Q: confirm the quarter. |
| CF25 | F17 (Notion test 1) | R045, R046, R048, R049 | L148 (T004) | "networking capital improved sequentially to 153 days from 161 days in Q1" (L148) | AMBIGUOUS | The call states the deck basis (153 days) with no formula. The Notion basis is pending: filing 189.0 days, deck 153, Notion 169. The test result flips with the basis. On the deck basis Q2 153 <= 161 (no confirm). On the filing basis 189 > 161 (confirms STRUCTURAL). The call does not resolve it (review Q6 unanswered). The basis ruling stays with the operator. |

---

## 2. CHECKLIST SCORECARD

| check | status | basis |
|---|---|---|
| F1 Zero-value standing items | N.A. | Concall. The ledger has no ZERO_STANDING rows. |
| F2 Standalone vs consolidated | N.A. | The call gives no standalone figures. The US-arm divergence goes to F17 (CF12, CF13). |
| F3 Shell-entity detection | N.A. | The call has no cost lines by entity. |
| F4 Unaudited contribution | N.A. | The call has no auditor Other Matters. |
| F5 Going concern / EoM scope | N.A. | The call has no EoM paragraph. Prior transcript is not available anyway. |
| F6 Forward-commitment mining | FINDING | 24 commitments registered (Section 3). Findings CF01, CF02, CF04, CF05, CF06, CF08, CF09, CF11, CF20, CF21, CF23, CF24. Status words: "completed" (Altec integration, L114); "underway" (B2S design/testing L315-L316, semicap L238); "initiated" (AI DC / robotics exploring L215). |
| F7 Hedge-phrase mining | FINDING | Lexicon hits: "exploring" x2 (L215, L460; L164 is a false positive), "subject to" x1 (boilerplate L30). The "probably" / "may" hedges sit on dated pledges. CF18, CF19. |
| F8 Tax forensics | PASS | Reported PBT Rs 393 Mn and PAT Rs 340 Mn (L161) give an ETR of 13.5%. Ex-reversal PBT is Rs 211 Mn, tax Rs 53 Mn, so the ETR is 25.1% against statutory 25.17% [INFERENCE]. The Rs 182 Mn reversal is untaxed (normalized PAT = PAT minus 182 exactly, L164). The call mentions no prior-year tax and no DTA. |
| F9 OCI forensics | N.A. | The call has no OCI data. |
| F10 Share count / dilution | N.A. | The call has no EPS or paid-up capital. The 15-Oct ESOP grant (review Q25) is not mentioned; it is logged under F17. |
| F11 Net worth tie-out | N.A. | The call has no balance-sheet equity. |
| F12 Segment forensics | N.A. | The call gives industry and product revenue shares only, with no segment assets or liabilities. The mix gap is in CF17 (F17). |
| F13 Board outcome | N.A. | The call reports no board outcomes. |
| F14 Note drafting inconsistencies | N.A. | The call has no notes and no auditor letter. Spoken variances (182/183, 85%/86%) are machine-transcript or misspeak items logged in Section 0, not drafting signals. |
| F15 Entity list diffs | FINDING | Altec Electronics renamed Cyient DLM Electronics Inc. (L114, L437). CF22. No prior list for a full diff. |
| F16 Presentation dropped / reframed | N.A. | Presentation-specific. The B2S to "Electronic Products" rename (L91, L382) is logged in CF07. |
| F17 Silence audit | FINDING | 6 Notion tests: 1 addressed, 3 partly or in conflict, 2 silent. 30 review questions: 1 answered, 7 partial, 2 declined, 20 silent. One FY27 target from a prior quarter, put by an analyst, got no answer (CF07). Findings CF03, CF07, CF10, CF12-CF17, CF25. Tables in Section 4. |

GATE A3: every check marked. No blanks.

---

## 3. COMMITMENT REGISTER (from F6)

Status words: initiated / underway / completed, where the call uses process language. "stated" marks a guidance figure with no process stage.

| # | commitment | implied date | turn / line ref | status word |
|---|---|---|---|---|
| 1 | FY27 EBITDA margin "close to around 9%" / "9% to 10% range" / "higher end of the single-digit range" | FY27 (Q4 FY27 print) | T003 L103; T015 L230; T021 L244; T031 L266 | stated |
| 2 | FY28 EBITDA margin "double digits"; "10 plus percent" from backlog execution alone | FY28 | T031 L266; T096 L476-L477 | stated |
| 3 | "from the Q1 onwards ... double-digit EBITDA margin" (period unclear, see CF24) | Q1 FY28 (inferred) | T015 L231 | stated |
| 4 | EXPAND phase: 4 to 7 industries (robotics, AI DC; semicap focus); margin framework ~11-13% | FY27-FY29 | T003 L82-L86 | initiated |
| 5 | TRANSFORM phase: product and platform moat; margin framework ~13-18% | FY30 onward | T003 L88, L96 | stated |
| 6 | No net new S&M cost until quarterly revenue at least doubles; "no future investment in that area" | open-ended (until ~Rs 7,862 Mn a quarter) | T039 L288; T040 L297 | stated |
| 7 | Investment intensity lower | Q3 or Q4 FY27 | T040 L295 | stated |
| 8 | Margin expansion of ~200 bps (base lost in the audio gap) | undated | T040 L294 | stated |
| 9 | FY27 revenue growth 30-35%; H2 "definitely" above 30% | FY27 / H2 FY27 | T055 L354, L361 | stated |
| 10 | Order inflow "600 crores plus" a quarter | Q3 and Q4 FY27 | T025 L256 | stated |
| 11 | Order book executes over 18-24 months on average; year split not published | rolling | T017 L236-L237; T088 L452-L455 | stated |
| 12 | Pipeline win ratio ~40%; $400-500 Mn order impact from the existing pipeline | undated | T029 L262-L264; T051 L332-L333 | stated |
| 13 | Four B2S programmes, ~$1 bn, enter the order book after design and prototype testing | undated | T042 L309-L310; T064 L409-L410 | underway (design and testing, L315-L316) |
| 14 | B2S production and revenue start FY29 ("probably"); full production and ramp FY30 (earlier in the call: FY30) | FY29 / FY30 | T042 L308; T046 L317; T064 L411; T071 L428-L429 | underway |
| 15 | Update on AI DC and robotics: where we stand, opportunities, pipeline | end FY27 (Q4 FY27 call) | T009 L217; T090 L460-L461 | initiated ("just started exploring") |
| 16 | Semicap growth "every quarter" | from Q3 FY27 | T017 L238-L239; T090 L458-L459 | underway |
| 17 | Altec integration done; renamed Cyient DLM Electronics Inc. | done (date NOT FOUND) | T003 L114; T077 L437 | completed |
| 18 | More revenue traction in the US division | undated | T077 L438-L439 | stated |
| 19 | Working-capital focus: inventory optimisation and collections (no target) | undated | T004 L150, L182 | stated |
| 20 | "ready to convert some large orders from the new sales team" | undated | T096 L478-L479 | stated |
| 21 | Honeywell build-to-print programme back into serial production after engineering changes | undated | T064 L405-L407 | underway |
| 22 | Product development expensed, not capitalised ("no surprises in the future") | policy, ongoing | T007 L199; T062 L389-L391; T096 L473 | stated |
| 23 | Exports continue; "a little growth in that India market" | undated | T081 L444-L445 | stated |
| 24 | Growth sustains "through the rest of the year and into next year" | FY27-FY28 | T002 L56 | stated |

---

## 4. SILENCE AUDIT: WHAT WAS NOT DISCUSSED (F17)

Consecutive-quarter count: prior-quarter transcripts are NOT AVAILABLE to A3, so every count is "1 (this call; earlier quarters unverified)". No row can yet be called SUSTAINED silence (Role 5 confirmatory-negative threshold).

### 4a. Notion monitoring checklist (six Q2 tests)

| test | call coverage | line cite | status | quarters silent |
|---|---|---|---|---|
| 1 Cash falsifier (NWC <=120 days by Q4 FY27 with positive CFO; >161 confirms) | Deck-basis NWC 153 days stated; no formula, no target, no CFO figure; Q2-only "operating FCF" | L148, L149 | PARTIAL (basis unresolved, CF25; CFO silent, CF16) | 1 (formula and CFO) |
| 2 Gross margin (compression without a component-cost explanation) | No gross-margin figure. Causes conflict: "revenue mix" (CFO) vs "it's not the revenue mix" (chairman). Chairman claims gross and contribution margin higher YoY, against the filed -381 bps. Memory market named only as a supply shortage. | L158, L282-L284, L39 | CONFLICT (CF03); component cost SILENT | 1 |
| 3 Order book (Rs 2,813.7 Cr; 1.6x) | Rs 2,813 Cr / Rs 28.1 bn; "over 1.6 times"; 600 Cr+ intake | L33, L36, L127, L148, L256 | ADDRESSED (ratio vs book walk 1.55x, CF10) | 0 |
| 4 Proof gate (B2S share double digits x2 quarters + >=100 bps EBITDA uplift) | No B2S share; analyst's FY27 double-digit question unanswered; B2S revenue FY29-FY30; FY27 9-10%, FY28 10+ | L376, L382-L394, L411, L428-L429, L244, L476 | PARTIAL / EVADED on share (CF07) | 1 (share) |
| 5 Related-party flow to parent Cyient Ltd | Parent never mentioned | none | SILENT | 1 |
| 6 Standalone vs consolidated (US arm 1.17% EBITDA; earnout write-back 53.5% of PAT) | Reversal called "one-time"; US arm "doing as per our plans"; no subsidiary figures; recurrence question answered without the reversal | L133, L163, L438, L462-L465 | CONFLICT (CF12, CF13) | 1 (subsidiary P&L) |

### 4b. Review Step 8.5 questions (30), call coverage

Caveat: these questions were drafted after the call and were never put to management. Silence on an unasked question is weak evidence. Questions an analyst DID ask and management did not answer are marked (ASKED).

| Q# | topic | call coverage | line cite | status |
|---|---|---|---|---|
| 1 | Remaining earnout liability | Reversal amount only; no residual | L133, L163, L173 | SILENT |
| 2 | Size of the earnout-metric miss | none | none | SILENT |
| 3 | US subsidiary Q2 EBITDA | Qualitative only: "doing as per our plans" | L438 | PARTIAL (qualitative; conflicts with filing, CF13) |
| 4 | Gross margin split: component cost vs Box Build mix | Causes named but contradictory; no bps split | L158, L284 | PARTIAL / CONFLICT (CF03) |
| 5 | 11-13% band: metric and entry year | Band stated for FY27-29 as "margin framework"; metric unnamed; FY28 "10 plus" | L82, L86, L266, L476 | PARTIAL (CF02) |
| 6 | NWC formula | 153 days stated, no formula | L148 | SILENT |
| 7 | Peak standalone short-term borrowings | none | none | SILENT |
| 8 | Share of order book with customer advances | Advance days 13 vs 15 QoQ only | L149 | SILENT (CF15) |
| 9 | US term debt current / refinancing | none | none | SILENT |
| 10 | Borrowings at 30-Sep-2025; funding of the H1 WC build | "lower working capital borrowings" repeated; no balances | L160, L179 | PARTIAL (CF14) |
| 11 | FY27 impairment test of the US CGU | none | none | SILENT |
| 12 | Definition of "operating free cash flow" | Figure only | L149 | SILENT (CF16) |
| 13 | Q2 consolidated CFO | none | none | SILENT |
| 14 | Share of order book executable within 12 months | (ASKED, L451) "we don't publish the numbers of what is for each year"; average 18-24 months | L452-L455 | DECLINED |
| 15 | Intake reconciliation (1.55x vs 1.6x; cancellations, FX) | "600 crores plus"; "over 1.6"; no cancellations or FX | L36, L256 | PARTIAL (CF10) |
| 16 | Q2 B2S revenue share | (ASKED, L376) not answered | L382-L394 | SILENT / EVADED (CF07) |
| 17 | Order book from semicap, robotics, AI DC | Semicap revenue "last two quarters", unquantified; AI and robotics "just started exploring" | L238, L215, L460 | PARTIAL (CF18) |
| 18 | Product development purchases in material cost | (ASKED, L195) "do not want to be putting a number" | L205, L208 | DECLINED |
| 19 | Numeric FY27 revenue growth guidance | 30-35% FY27; H2 above 30% | L354, L361 | ANSWERED (CF23) |
| 20 | FX hedge ratio | Forex named as an other-income item only | L464 | SILENT |
| 21 | US unused tax losses and expiry | none | none | SILENT |
| 22 | Standalone ECL write-back | none | none | SILENT |
| 23 | Contract assets unbilled >90 days | none | none | SILENT |
| 24 | IP-communications investee re-valuation | none | none | SILENT |
| 25 | ESOP grants of 15-Oct-2026 to KMP | none (grant date = call date) | none | SILENT |
| 26 | Q2 FY26 employee-cost misprint | none | none | SILENT |
| 27 | H1 FY26 inflow under acquisition line | none | none | SILENT |
| 28 | Altek rename date and earnout terms | Rename confirmed; no date or terms | L114, L437 | PARTIAL (CF22) |
| 29 | Q3 FY26 Rs 34 Mn one-off | none | none | SILENT |
| 30 | Auto & Others Q2 revenue and YoY | Industry mix omits Auto; "positive growth across all key segments" | L41, L151-L152 | SILENT (CF17) |

Tally: ANSWERED 1 (Q19); PARTIAL 7 (Q3, Q4, Q5, Q10, Q15, Q17, Q28); DECLINED 2 (Q14, Q18); SILENT 20 (including Q16, which an analyst asked). Total 30.

### 4c. Commitments from a prior quarter raised on this call

| commitment (per analyst recall) | line | addressed? | quarters silent |
|---|---|---|---|
| B2S sales contribution double digit in FY27 (stated in FY26 Q3/Q4 calls, per analyst; not verifiable here) | L375-L376 | NOT ANSWERED: reply at L382-L394 covers lifecycle and expensing only | 1 (prior unverified) |

---

## 5. FLAGS FOR A4 (management-question conversion)

FORWARD-SIGNAL: CF01, CF02, CF05, CF07, CF11, CF12, CF13, CF14, CF15, CF17, CF18.
AMBIGUOUS: CF03, CF04, CF06, CF08, CF09, CF10, CF16, CF20, CF21, CF24, CF25.
NEUTRAL-FACT (no question needed): CF19, CF22, CF23.

Suggested question themes, new beyond review Q1-Q30:
- CF01: which end of the 9-10% FY27 band applies, and why H2 at about 8.5% (below Q2) if investment intensity falls from Q3.
- CF03: definition of "contribution margin", and its Q2 FY27 vs Q2 FY26 value against the filed -381 bps gross margin.
- CF06 / CF24: the base and year of the "200 bps" expansion, and whether the "Q1 onwards double-digit" pledge means Q1 FY28.
- CF07: is the FY27 double-digit B2S share target withdrawn?
- CF08: signed vs unsigned value inside the "close to $1 billion".
- CF09: pipeline at 30-Jun and 30-Sep on one unweighted basis.
- CF12: does the Q2 other income of about 23 Cr in both years include an earnout write-back in each year?
- CF20: will product development stay fully expensed through FY28?
- CF21: Honeywell serial-production date.

---

```yaml
stage: A3-forensics
company: "CYIENTDLM"
quarter: "q2fy27"
doctype: "concall"
model: "claude-opus-5-5"
status: complete
forensics_path: "runs/cyientdlm-q2fy27/work/forensics_concall_cyientdlm_q2fy27.md"
ledger_reconciled_pct: 100
checklist:
  F1: N.A.
  F2: N.A.
  F3: N.A.
  F4: N.A.
  F5: N.A.
  F6: FINDING
  F7: FINDING
  F8: PASS
  F9: N.A.
  F10: N.A.
  F11: N.A.
  F12: N.A.
  F13: N.A.
  F14: N.A.
  F15: FINDING
  F16: N.A.
  F17: FINDING
findings:
  - {id: "CF01", check: "F6", line: "L103, L230, L244, L266", classification: "FORWARD-SIGNAL", implication: "FY27 ~9% guidance on H1 9.56% implies H2 EBITDA margin ~8.4-8.6%, below Q2 8.7% [INFERENCE]; contradicts lower investment intensity from Q3/Q4 (L295)"}
  - {id: "CF02", check: "F6", line: "L82, L86, L266, L476", classification: "FORWARD-SIGNAL", implication: "EXPAND phase FY27-29 framework 11-13% vs FY27 9-10% and FY28 10+; band entry not before FY29 on mgmt's own dates; metric unnamed"}
  - {id: "CF03", check: "F17", line: "L158, L282-L284", classification: "AMBIGUOUS", implication: "Chairman says gross/contribution margin higher YoY and 'not the revenue mix'; CFO says revenue mix; filing GM -381 bps YoY wins; Notion test 2 still lacks a component-cost cause"}
  - {id: "CF04", check: "F6", line: "L199, L231, L287, L290, L291", classification: "AMBIGUOUS", implication: "Investment drag sized 100-150, ~100 and 150-200 bps; PD cost 'one-off' and 'not a one-off'; FY28 recovery has no fixed size to test"}
  - {id: "CF05", check: "F6", line: "L288, L297", classification: "FORWARD-SIGNAL", implication: "No net new S&M cost until quarterly revenue doubles (~Rs 7,862 Mn); any QoQ S&M rise before that breaks the pledge (speaker inferred chairman)"}
  - {id: "CF06", check: "F6", line: "L293-L294", classification: "AMBIGUOUS", implication: "'around 200 basis points' expansion follows a 30-second audio gap; base and year lost"}
  - {id: "CF07", check: "F17", line: "L376, L382-L394, L308, L411, L428-L429, L91", classification: "FORWARD-SIGNAL", implication: "Analyst-put FY27 double-digit B2S share target unanswered; B2S revenue now FY29-FY30; proof-gate share leg cannot fire before FY29-FY30 on mgmt timeline [INFERENCE]"}
  - {id: "CF08", check: "F6", line: "L307, L309, L313, L409-L410, L427, L431", classification: "AMBIGUOUS", implication: "$1 bn B2S is outside the order book and only partly signed (L427 vs L409); spans 7-9 yrs, ~$111-143 Mn/yr at full run-rate [INFERENCE]"}
  - {id: "CF09", check: "F6", line: "L33, L331, L338-L339", classification: "AMBIGUOUS", implication: "CEO wording implies pipeline fell from $1.4 bn to >$1 bn; chairman says it rose to $1.5 bn; direction of the feeder metric unresolved (machine transcript)"}
  - {id: "CF10", check: "F17", line: "L36, L106, L255-L256", classification: "AMBIGUOUS", implication: "'over 1.6 times' vs book-walk 1.55x (review Q15); filing wins; 600 Cr+ intake fits the walk; Notion test 3 should record 1.55x"}
  - {id: "CF11", check: "F6", line: "L39, L148, L248-L251, L356, L481", classification: "FORWARD-SIGNAL", implication: "Book-to-revenue conversion is material-constrained; H2 >30% pledge and 162 inventory days run through the same constraint; no NWC target for Notion test 1"}
  - {id: "CF12", check: "F17", line: "L133, L163, L173, L462-L465", classification: "FORWARD-SIGNAL", implication: "Rs 182 Mn earnout reversal called one-time; CFO's answer on Q2 other-income recurrence omits it; H1 math implies ~Rs 196 Mn normalization in H1 FY26 too [INFERENCE]; recurring Q2 write-back pattern"}
  - {id: "CF13", check: "F17", line: "L114, L437-L439", classification: "FORWARD-SIGNAL", implication: "US unit 'doing as per our plans' conflicts with the earnout write-back and 1.17% US EBITDA (filing wins); FY27 goodwill/intangible impairment test at risk"}
  - {id: "CF14", check: "F17", line: "L160, L179", classification: "FORWARD-SIGNAL", implication: "'lower working capital borrowings' is a YoY claim; silent on the H1 FY27 borrowing rise to Rs 1,319.60 Mn (review Q10); finance cost likely up QoQ from Q3 [INFERENCE]"}
  - {id: "CF15", check: "F17", line: "L149", classification: "FORWARD-SIGNAL", implication: "Customer advances given QoQ only (15 to 13 days); YoY fall from 33 days (review Q8) not mentioned; more WC per rupee of revenue"}
  - {id: "CF16", check: "F17", line: "L149", classification: "AMBIGUOUS", implication: "Rs 172 Mn 'operating free cash flow' is Q2-only and undefined; H1 CFO minus capex Rs 4.11 Mn (review Q12) not mentioned"}
  - {id: "CF17", check: "F17", line: "L41, L76, L151-L152", classification: "FORWARD-SIGNAL", implication: "Industry mix sums to 99% without Auto; back-solve puts Auto & Others ~1% vs ~9-10% a year ago [INFERENCE]; core EV/auto industry shrinking unmentioned; 'all key segments' claim fails"}
  - {id: "CF18", check: "F7", line: "L215-L217, L460-L461, L69, L83, L238", classification: "FORWARD-SIGNAL", implication: "AI DC and robotics 'just started exploring' vs $58 bn sizing and FY27 EXPAND phase; no revenue, pipeline or date before the Q4 FY27 call; semicap unquantified"}
  - {id: "CF19", check: "F7", line: "L354, L411, L428", classification: "NEUTRAL-FACT", implication: "'probably'/'may start' hedges on FY27 growth and the B2S start year; no hits for 'no assurance', 'in discussions' or 'endeavour'; L164 'Exploring' is machine text"}
  - {id: "CF20", check: "F6", line: "L389-L391, L473, L205, L208", classification: "AMBIGUOUS", implication: "Option to capitalise PD retained, spend undisclosed; a policy switch could supply the >=100 bps proof-gate uplift through accounting (tripwire)"}
  - {id: "CF21", check: "F6", line: "L404-L407, L420", classification: "AMBIGUOUS", implication: "Honeywell programme is build-to-print; serial production slipped on engineering changes; no date"}
  - {id: "CF22", check: "F15", line: "L114, L437", classification: "NEUTRAL-FACT", implication: "Altec renamed Cyient DLM Electronics Inc.; rename date and earnout terms not given (review Q28 open)"}
  - {id: "CF23", check: "F6", line: "L354, L361, L108", classification: "NEUTRAL-FACT", implication: "FY27 growth 30-35% and H2 >30% against Q2 26.5%; Q3 YoY <30% is the first miss on a dated pledge; answers review Q19"}
  - {id: "CF24", check: "F6", line: "L231", classification: "AMBIGUOUS", implication: "'from the Q1 onwards ... double-digit EBITDA margin'; Q1 FY27 already 10.46% [INFERENCE], so this means Q1 FY28 or is a mishearing"}
  - {id: "CF25", check: "F17", line: "L148", classification: "AMBIGUOUS", implication: "NWC 153 days on deck basis, no formula; Notion test 1 flips with the basis (deck 153 <=161; filing 189 >161); basis ruling still pending"}
forward_signals: ["CF01", "CF02", "CF05", "CF07", "CF11", "CF12", "CF13", "CF14", "CF15", "CF17", "CF18"]
ambiguous: ["CF03", "CF04", "CF06", "CF08", "CF09", "CF10", "CF16", "CF20", "CF21", "CF24", "CF25"]
commitments:
  - {commitment: "FY27 EBITDA margin close to 9% / 9-10% range", implied_date: "FY27", ref: "T003 L103; T015 L230; T021 L244; T031 L266", status_word: "stated"}
  - {commitment: "FY28 EBITDA margin double digits / 10 plus from backlog alone", implied_date: "FY28", ref: "T031 L266; T096 L476", status_word: "stated"}
  - {commitment: "Double-digit EBITDA margin from Q1 onwards (period unclear)", implied_date: "Q1 FY28 (inferred)", ref: "T015 L231", status_word: "stated"}
  - {commitment: "EXPAND phase 4 to 7 industries, margin framework ~11-13%", implied_date: "FY27-FY29", ref: "T003 L82-L86", status_word: "initiated"}
  - {commitment: "TRANSFORM phase, margin framework ~13-18%", implied_date: "FY30 onward", ref: "T003 L88, L96", status_word: "stated"}
  - {commitment: "No net new S&M cost until quarterly revenue at least doubles", implied_date: "open-ended", ref: "T039 L288; T040 L297", status_word: "stated"}
  - {commitment: "Investment intensity lower", implied_date: "Q3 or Q4 FY27", ref: "T040 L295", status_word: "stated"}
  - {commitment: "Margin expansion ~200 bps (base lost in audio gap)", implied_date: "undated", ref: "T040 L294", status_word: "stated"}
  - {commitment: "FY27 revenue growth 30-35%; H2 above 30%", implied_date: "FY27", ref: "T055 L354, L361", status_word: "stated"}
  - {commitment: "Order inflow 600 Cr plus per quarter", implied_date: "Q3-Q4 FY27", ref: "T025 L256", status_word: "stated"}
  - {commitment: "Order book average execution 18-24 months", implied_date: "rolling", ref: "T017 L236; T088 L452-L455", status_word: "stated"}
  - {commitment: "Pipeline win ratio ~40%; $400-500 Mn order impact", implied_date: "undated", ref: "T029 L262-L264; T051 L332-L333", status_word: "stated"}
  - {commitment: "Four B2S programmes ~$1 bn enter order book after design/prototype", implied_date: "undated", ref: "T042 L309-L310; T064 L409-L410", status_word: "underway"}
  - {commitment: "B2S production start FY29, full ramp FY30", implied_date: "FY29/FY30", ref: "T042 L308; T064 L411; T071 L428-L429", status_word: "underway"}
  - {commitment: "Update on AI DC and robotics position and pipeline", implied_date: "end FY27", ref: "T009 L217; T090 L460-L461", status_word: "initiated"}
  - {commitment: "Semicap growth every quarter", implied_date: "from Q3 FY27", ref: "T017 L238; T090 L459", status_word: "underway"}
  - {commitment: "Altec integration done, renamed Cyient DLM Electronics Inc.", implied_date: "done (date NOT FOUND)", ref: "T003 L114; T077 L437", status_word: "completed"}
  - {commitment: "More revenue traction in US division", implied_date: "undated", ref: "T077 L439", status_word: "stated"}
  - {commitment: "Inventory optimisation and collections focus (no target)", implied_date: "undated", ref: "T004 L150, L182", status_word: "stated"}
  - {commitment: "Convert large orders from new sales team", implied_date: "undated", ref: "T096 L478-L479", status_word: "stated"}
  - {commitment: "Honeywell programme back to serial production", implied_date: "undated", ref: "T064 L405-L407", status_word: "underway"}
  - {commitment: "Product development expensed, not capitalised", implied_date: "policy, ongoing", ref: "T007 L199; T062 L389-L391; T096 L473", status_word: "stated"}
  - {commitment: "Exports continue; a little India growth", implied_date: "undated", ref: "T081 L444-L445", status_word: "stated"}
  - {commitment: "Growth sustains through rest of FY27 and into FY28", implied_date: "FY27-FY28", ref: "T002 L56", status_word: "stated"}
gate_a3: pass
blank_checks: []
analyst_note: "The call's margin story runs opposite to the filing. Management says gross and contribution margin rose YoY and opex investment drove the 135 bps fall. The filing shows gross margin down 381 bps and the opex ratio down 245 bps. The 9% FY27 point guidance implies an H2 margin below Q2, which no speaker explains. Read together, CF01 to CF04 say the margin leg of the proof gate has no fixed baseline. The B2S share leg slips to FY29 or FY30 (CF07). On management's own words, the proof gate cannot fire inside FY27. Second thread: the Rs 182 Mn earnout reversal is called one-time. H1 arithmetic points to a similar item a year earlier. The CFO left it out when asked if Q2 other income recurs. With the US unit called on-plan (CF13), this points to the FY27 impairment test. Speaker tags for the S&M pledge and the contribution-margin claim are inferred (T039). Two A1/A2 anchor defects (R294 at L454, R177 cross-ref) change no values."
```
