# A3 FORENSIC NOTES: RAYMONDREL (Raymond Realty Limited), CONCALL, Q2 FY27

Agent: A3 forensics | model: claude-opus-5-5 | run date: 2026-10-28
Inputs read: extracted/raymondrel-concall-q2fy27-structured.md (R001-R320), extracted/raymondrel-concall-q2fy27-fulltext.md (lines 19-618), work/ledger_concall_raymondrel_q2fy27.md, work/monitoring_checklist_raymondrel.md, work/notion_page_raymondrel_2026-10-28.md lines 876-969 (Q1 FY27 review, operator notes, promise tracking only).
Not opened: source transcript, anything under inputs/.

Evidence caveat. This is an ASR machine transcript (faster-whisper small.en). Speakers are unlabelled and turns are inferred. Every number below is management tier and unverified (fulltext L19). Q1 FY27 comparatives come from the operator's Notion notes, not from filed evidence. "Derived" marks arithmetic done here from stated figures; it never fills a missing number.

## 0. LEDGER RECONCILIATION

- Ledger rows: 320 (R001-R320). Rows read at their fulltext line: 320. Reconciled: 100%.
- A2 anchor drift confirmed and corrected at the true line: R054 (true L142, "average debt was about 300, 400 crores"), R073 (L243), R086 (L331), R095 (L351), R110 (L396-397), R123 (L458), R130 (L492, "guided 20% growth"). R052 (L130), R064 (L196), R067 (L198), R139 (L536) sit at the cited line or within one line. No row is missing from the structured file.
- A2 conflicts, resolution:
  1. ICICI Rs 140 Cr (R129, analyst, L480) vs Rs 210 Cr (R055 L146, R066 L198). Management states 210 three times as the cap on ICICI's 60% share ("up to 210 crores of rupees", L198). Management did not answer the 140 question; it answered only the debt classification (L486). Candidate reconciliation (derived, unconfirmed): 210 / 0.60 x 0.40 = Rs 140 Cr, which is RR's own 40% share of the project equity. Carried to A4 as FND-14.
  2. Promoter equity ~400 Cr (R056, L149, "committed ... is infusing ... first branch of that ... is going to be received shortly") vs ~410 Cr (R069, L208, "has infused"). Same commitment, rounded. The conflict that matters is tense: received vs committed. Carried as FND-11.
  3. "No revenue guidance" (R185, L230) vs "similar range" (R186/R228, L246) vs "not very different from a twenty percent growth" (R144/R260, L545-547). Resolution, conservative: the formal revenue guide is withdrawn; a verbal near-20% soft guide replaces it with no number (L547). Carried as FND-03.
  4. Thane current sales 1,500-2,000 (R121, L438) vs stabilise at 1,500-1,600 (R122, L439): the stable state is the low end of the current band. Carried as FND-19.
  5. R036/R037 net 912 vs gross "1200 odd" label order: read correctly at L98-99 (net 912, gross 1,200 odd). No conflict.

## 1. FINDINGS TABLE

| id | check | ledger rows | line | short verbatim quote | classification | forward implication |
| --- | --- | --- | --- | --- | --- | --- |
| FND-01 | F6 | R004, R005, R007, R062, R206, R207, R223 | L50-54; L176 | "They are expected to normalize progressively ... as this year progresses and moves into next year also" / "firmly on track to meet our ... FY27 Beta Margin Guidance of 17 to 19%" | FORWARD-SIGNAL | H1 margin sits near 14% (Q1 13% per Notion; Q2 15%, L48). Derived: if H2 income equals H1 (Rs 1,293 Cr), H2 needs ~20% margin to reach 17% and ~24% to reach 19%. Management's own normalisation extends "into next year", which softens the FY27 claim. Back-ended guide; ask for the quarterly path. |
| FND-02 | F17 | R003, R004, R005 | L47-48 | "our EBITDA also rose from 14% and 15 crores with margins now at 15%" | AMBIGUOUS | Checklist #1 / stop-loss "two consecutive Q <15%": Q1 13%, Q2 "15%" sits on the boundary. The rupee EBITDA is garbled. One consistent reading is "rose 14% to 115 crores" (115/757 = 15.2%; PY 115/1.14 over 757/1.07 = 14.3%, matches "14%"). That is a candidate reading only. A 14.5-14.9% actual rounded to 15% would fire the <15% stop. Operator ruling on which stop binds (14 / 15 / 18%) is still pending. Score only on the Reg 33 figure. |
| FND-03 | F16 | R070, R073, R074, R143, R144, R184, R185, R186, R205, R228, R260 | L227-230; L242-244; L543-547 | "This year we have not given a guidance on revenue growth" / "August 19 presentation, slide 9, where you called out a revenue guidance also" / "you've got the same calculator as me my friend" / "I don't have an exact number to guide you with" | FORWARD-SIGNAL | Revenue guidance dropped between decks. Q1 notes record "Revenue growth minimum 20% YoY, HIGH" (Notion L902). Now a verbal "in that range" with no number. Management did not dispute the analyst's back-calculation of low double digit or high single digit revenue growth (L541-543). Stated reason: "we follow percentage completion there are many moving parts" (L233-234); confirm the Ind AS 115 recognition method. Treat FY27 revenue growth below 20% as the conservative case. |
| FND-04 | F6 | R063, R224 | L176-178 | "the pet margin will be 9 to 10 percent. This has been a earlier guidance we are maintaining" | AMBIGUOUS | Q1 notes record PAT guidance REFUSED ("not a policy of giving that out", Notion L905). Now a 9-10% PAT margin is called "earlier guidance". Either the Q1 record is wrong or management has started guiding PAT (Notion I-6 turn-confirming). "pet" is an ASR reading. Confirm on the filing / deck and resolve against the Q1 record. |
| FND-05 | F6 | R094-R106, R189-R193, R237, R238 | L351-365 | "it is around 10,000 crore kind of pre-tax cash flow" / "10,000 crore net operating cash flow we can assume over next 4-5 years" / "It would be pretty tight." | AMBIGUOUS | First portfolio-level OCF figure (I-6 partial). The basis is unclear: pre-tax, before interest?, assumes the full 52,000 Cr GDV is executed (L351), and the GDV base moves to "50,000 crore" in the next line (L359). Project cash flow "14300" (L348) vs "14000 375" (L352) is ASR-suspect. "Pretty tight" is unattributed. Rs 10,000 Cr over 4-5 years is about Rs 2,000-2,500 Cr a year against a negative CFO today. Ask for basis, timing curve and the first year it turns positive. |
| FND-06 | F6 | R043, R044, R045, R075, R076, R229 | L104-105; L260-267 | "total interest cost for Q2FI27 is 44 crores ... bank borrowings of 27 crores and 17, 17 crores of interest to government authorities" / "it will be following the same run rate" | AMBIGUOUS | The analyst cites Rs 91 Cr H1 interest (ASR-suspect) and a prior Rs 100-120 Cr full-year guide (L262-263). Management neither reaffirmed nor withdrew that guide; it said only "same run rate" as H1. Derived: H2 = H1 gives about Rs 180 Cr all-in FY27. Bank-only at Rs 27 Cr a quarter is ~Rs 108 Cr a year, inside 100-120. So the old guide may have been bank-only. If H1 is 91 and Q2 is 44, Q1 was 47, so interest fell QoQ while debt rose. Check capitalisation. Q1 QM-7 (publish exact FY27 interest) is still unanswered. |
| FND-07 | F11 | R036, R037, R038, R039, R174, R175 | L98-100 | "net debt of 912 crores and a gross debt of 1200 odd crores with a healthy debt to equity ratio of 0.8 X ... net debt to equity ratio which it will be closer to 0.5" | AMBIGUOUS | Implied net worth does not tie. Derived: 1,200 / 0.8 = ~Rs 1,500 Cr; 912 / 0.5 = ~Rs 1,824 Cr. The gap is ~22%, above the 5% line. At Rs 1,500 Cr equity, net D/E is ~0.61, not "closer to 0.5". Candidate reconciling items: promoter warrant money (counted on receipt or on commitment), ICICI OCPRS at the 10X subsidiary (NCI), the Rs 410 Cr promoter infusion, rounding of "1200 odd". This is the second quarter in a row that D/E fails to tie (Q1 FND-08). Ask for exact net worth, net debt and net D/E. |
| FND-08 | F11 | R042, R045, R176, R177, R280-R282 | L102; L105-109 | "stable cost of debt at 9.6 percent" / "the government charges a nominal interest without any documentation" | AMBIGUOUS | Rs 17 Cr in the quarter of interest on deferred approval dues to authorities (DMC/TMC/"MARA") sits outside the 9.6% headline. It probably sits outside the Rs 1,200 Cr gross debt too. Derived run rate is ~Rs 68 Cr a year against ~Rs 45 Cr for FY26 (Q1 notes, FND-17), so the leg is rising. It is a debt-like liability with no debt-style disclosure on the call. Ask for the principal outstanding and the blended cost. Q1 QM-12 is repeated and unanswered. |
| FND-09 | F17 | R036, R038 | L98-99 | "net debt of 912 crores ... debt to equity ratio of 0.8 X" | CONFIRMATORY-NEGATIVE | Both first signals of risk matrix #2 are now lit: "Q1 FY27 net debt >Rs.900 Cr" (912; one quarter late) and "D/E >0.75x" (0.8x gross). Net debt is up ~Rs 88 Cr QoQ (824 in Q1 per Notion). It is below the Rs 1,000 Cr Q2 red line, so checklist #3 is AMBER and has not fired. Q3 net debt will benefit from ICICI and promoter inflows (FND-11, FND-14). Read Q3 net debt before and after those inflows (pending operator ruling). |
| FND-10 | F6 | R053, R127, R213, R214, R252, R254 | L140; L211-214; L471-472 | "market is showing concern on debt levels and interest cost and also we don't want the debt to go out of control. So naturally the other option is to raise equity." / "we are at 1200, it will not come down at least for the next one or two years for sure" | FORWARD-SIGNAL | The 1:1 ceiling binds in practice. Equity is raised to cap debt, and gross debt holds at Rs 1,200-1,400 Cr into FY28-FY29. This matches I-3 red-leaning and the FTTCP cash conversion DECLINING grade. Rate hardening (FND-21) applies to a base that is not shrinking. |
| FND-11 | F10 | R056, R069, R113, R128, R180, R215, R246, R253, R286 | L149-151; L205-208; L408-410; L473-476 | "committed about 400 crores of equity that he is infusing and the first branch of that ... is going to be received shortly" / "a promoter has infused equity of approximately 410 crores" / "May be in the range of 5-600 crores of equity going forward we may need. Apart from what we have already raised" / "our requirement as per the LRP is in the range of maybe 4 to 600 crores" | FORWARD-SIGNAL | Three dilution layers: (a) ~Rs 410 Cr promoter preferential issue, EGM-approved (L151). The call says both "infused" and "first tranche to be received shortly". Tracker title: Rs 102 Cr upfront, Rs 307 Cr by ~Apr-2028. (b) A new Rs 400-600 Cr equity need under the 5-year LRP, called not "significant" (L408) and to be decided by "the board and the shareholders" (L410). (c) The analyst recalls a no-fundraise stance "two or three concall" ago (L205-207). Management did not contest it. A4 to check the basic/diluted spread against the warrants. Promise-vs-delivery: capital stance reversed. |
| FND-12 | F15 | R055, R057, R064-R068, R181, R183, R216, R231, R283, R284 | L145-146; L193-202; L219-221; L378-380 | "Raymond Realty's subsidiary company has raised 210 crores from AIF which is promoted by ICICI" / "they are contributing 60% of the capital ... we are contributing 40% ... the balance profit ... distributed in that 60-40 ratio ... 40% plus 5% or top line" / "my margin profile also improves because I am charging a fee" | FORWARD-SIGNAL | Relationship change in a consolidated entity. The 10X subsidiary (10X Realty, L378; Q1 "10X Mahalakshmi" SPV) moves from wholly owned to holding an outside AIF investor with 60% of the capital. Expect a non-controlling interest line: consolidated pre-sales and EBITDA carry 100% of the Mahim project, and attributable PAT carries ~40% plus the fee. A 5% fee from parent to subsidiary eliminates on consolidation. The "margin profile improves" claim holds only at RR's economic share, not at consolidated EBITDA. Ask how the fee and the NCI will show. |
| FND-13 | F7 | R182, R196, R197, R198, R285 | L486-490; L584-587 | "No, it will not reflect as debt." / "the coupon is virtually zero ... So, there will be no dividend payout, it is effectively zero" | AMBIGUOUS | Equity treatment is management's assertion. Under Ind AS 32 the OCPRS terms (conversion ratio, any redemption or put, any coupon) decide the classification. "Virtually" and "effectively" zero is not "nil". Ties to the pending operator ruling on counting the Rs 210 Cr AIF money before or after the net-debt lines. Ask for the term sheet: conversion date, ratio, any put or redemption, and the coupon. |
| FND-14 | F6 | R055, R108, R109, R129, R159, R160, R240, R241 | L146; L152; L376-377; L480 | "has raised 210 crores" / "our subsidiary will get 210 crores" / "The first part of that money is expected in the next 30 days ... by March, we would have received the entire sum." / "our 140 crore have you already infused" | AMBIGUOUS | At the call date the ICICI money had not arrived; "raised" means committed. A tranche lands in Q3 and the rest by Mar-2027, which lowers Q3/Q4 net debt for financing reasons. The 140 question went unanswered. Candidate: RR's 40% matching share (derived). Ask for the tranche amounts and dates, and whether RR's Rs 140 Cr share is already deployed. |
| FND-15 | F6 | R058, R059, R107, R154, R157, R158, R203, R218, R239, R242, R256, R287 | L166-167; L366-368; L380-382; L503 | "H2 will see two launches from us both of these launches are going to be in Mahil" / "we are launching currently in Q3 one project and in Q4 one project" / "We haven't taken that call yet" | FORWARD-SIGNAL | Unchanged from Q1 (Mahim-1 Q3, Mahim-2 Q4). Q3 is the current quarter, yet the call gives no RERA date and no inventory release. Combined GDV is "about 4100" (L167) vs "close to 4000" (L366). Product mix: one Invictus, one Address (L503). Mahim is the ICICI-funded project (L380), so the launch timing also depends on the ICICI tranche (FND-14). Checklist #4 holds GREEN only if a Q3 RERA registration shows. Risk #3: >2 Q slippage = downgrade. |
| FND-16 | F6 | R138, R165, R257, R258, R304 | L516-524 | "the aviation approval which is pending which is expected shortly it should happen in the next few weeks" / "I have to get rarer registration of those once I have the approval" | FORWARD-SIGNAL | New dated commitment. BKC Invictus upper floors cannot be sold until (1) aviation height approval and then (2) RERA registration. H2 pre-sales depend on this in part. Track the approval date in Q3. |
| FND-17 | F6 | R017, R018, R019, R114, R219, R247 | L72-74; L168-169; L412-413 | "we have added in H1 of approximately 8,500" / "there are more GDEs which are in the pipeline which we will be signing going forward" / "if we add about 8 to 10,000 crores worth of GDP every year" | FORWARD-SIGNAL | H1 additions of Rs 8,500 Cr match the Q1 Parel signing (Notion L946), so Q2 added no apparent new JDA. The FY27 Rs 8,000 Cr target is met (checklist #5 GREEN). The LRP plans Rs 8,000-10,000 Cr of new GDV every year for five years. That is the I-5 red case: signings keep pace with deliveries, the early-stage cash burn restarts each year, and the inflection drifts (Notion L58: "FY29 quietly becomes FY31"). |
| FND-18 | F6 | R015, R031, R032, R047, R048, R050, R179, R210, R211, R212, R274 | L64-66; L88-89; L117-119; L124-126; L136-137 | "receiving the occupation certificate for address by GS1 Tower B in Thane" / "sales value of 3432 crores and a collection of 857 crores" / "remains cash flow negative for the first two years" / "my estimate is that within the period of two years we will reach that steady state" | CONFIRMATORY-NEGATIVE | I-1 red: the only OC this quarter is at Thane. The four launched JDAs have collected 25% of their bookings (857 / 3,432, derived). Most new projects launched "towards the end of Q4" FY26 (L136), so they are cash-negative into FY28 at least. Steady state "within two years" is labelled the MD's "estimate". This matches I-7 red (negative CFO through FY28). |
| FND-19 | F6 | R009, R020-R026, R034, R120, R121, R122, R249 | L57-58; L438-440 | "we are currently doing between 1500 to 2000 range every year" / "let us say Tana will stabilize at 1500-1600 crores per annum, I do not see any significant growth coming beyond this number from Tana" | CONFIRMATORY-NEGATIVE | Management concedes that Thane, the cash engine, has stopped growing; the stable level is the bottom of the current band. Risk #5 (<Rs 1,000 Cr sustained) has not fired. Derived: Thane in Q2 = 43% of ~Rs 900 Cr = ~Rs 390 Cr. All growth and all execution risk now sit in the JDAs. "Started out with a sale of 4500 crores in a year" (L438) is ASR-suspect against 9,770 Cr sold over the whole life (L81). |
| FND-20 | F7 | R200, R201, R202, R261, R262, R263, R301 | L590-592; L602-608 | "The projects which will get launched in future will definitely have that impact" / "part of it will get passed on to the customer and part of it we will absorb in our contingencies" / "all this is subject to this not being prolonged into years and years of inflationary pressures" | FORWARD-SIGNAL | Fixed-price EPC contracts protect only the ongoing projects. The H2 Mahim launches and the whole LRP pipeline carry labour and material inflation, absorbed partly from contingency. This is a hedge on the margin path for FY28 and later, and on the 17-19% steady state. |
| FND-21 | F7 | R077, R078, R079, R187, R230 | L276-278; L287; L290-291 | "I am only referring to our portfolio I am not talking about market in general" / "they have to harden interest rates a little bit" | FORWARD-SIGNAL | Management itself expects rates to rise, while gross debt holds at Rs 1,200-1,400 Cr for 1-2 years (FND-10). Checklist #8 (green 9.5-9.75%, red >10.5%) will be tested. The demand view is scoped to its own Rs 1.5 Cr+ ticket portfolio. "2550 basis point" (L276) is ASR-garbled. |
| FND-22 | F17 | (checklist) | see Section 4 | (silence; no quote by definition) | CONFIRMATORY-NEGATIVE | Four Notion monitors drew silence for a second quarter in a row: #6 related-party sub-loans, #7 promoter governance, #9 Thane commercial optionality, #10 quarterly CFO (sent to deck slide 23, L110-112). Seven of the thirteen Q1 management questions went unaddressed (Section 4). |
| FND-23 | F6 | R006, R013, R014, R110, R130-R137, R204, R221, R227, R243, R255 | L43-45; L385-387; L492-500 | "nearly doubling our quarterly pre-sales without any new launches" / "it will be better than age one because the festive season" / "out of your 900 crore 700 crore you know came from your ... address" | FORWARD-SIGNAL | The pre-sales guide of at least 20% is reaffirmed. The analyst's arithmetic needs ~Rs 1,900-2,000 Cr in H2 against Rs 1,602 Cr in H1 (L493-495), with management saying existing stock alone gives "much more" than Rs 1,000 Cr (L497-498). The analyst put ~78% of Q2 bookings (700 of 900) in one product line, Address by GS, and management did not contest it. H2 depends on Mahim timing (FND-15) and the BKC approval (FND-16). The "nearly doubling" claim is consistent with H1 +111% (L63; derived Q2 ~Rs 900 Cr vs ~Rs 453 Cr). |

## 2. CHECKLIST SCORECARD

| check | status | basis |
| --- | --- | --- |
| F1 Zero-value standing line items | N.A. | Concall; no financial-statement template. Ledger ZERO_STANDING: none. |
| F2 Standalone vs consolidated | N.A. | No S/C tables on a concall. The S/C effect of the 10X NCI is logged under F15 (FND-12) for the Reg 33 run. |
| F3 Shell-entity detection | N.A. | No entity cost lines on a concall. |
| F4 Unaudited contribution ratio | N.A. | No auditor Other Matters on a concall. |
| F5 Going concern / EoM scope | N.A. | No auditor report on a concall. No prior-quarter fulltext in the repo either. |
| F6 Forward-commitment mining | FINDING | 59 FORWARD rows read. 13 findings (FND-01, 03-06, 10, 14-19, 23); commitment register in Section 3. |
| F7 Hedge phrase mining | FINDING | FND-13 ("virtually zero"), FND-20 ("subject to this not being prolonged"), FND-21 (portfolio-scoped demand view, rate hardening). |
| F8 Tax forensics | N.A. | No tax line, ETR or deferred tax on the call. Only a PAT margin guide (FND-04). |
| F9 OCI forensics | N.A. | No OCI disclosed on a concall. |
| F10 Share count and dilution | FINDING | FND-11: Rs ~410 Cr promoter preferential issue plus Rs 400-600 Cr more equity under the LRP. Spread cross-check vs warrants goes to A4. |
| F11 Net worth tie-out | FINDING | FND-07: implied net worth Rs ~1,500 Cr vs Rs ~1,824 Cr (~22% gap). FND-08: government-dues liability outside debt and outside the cost of debt. |
| F12 Segment forensics | N.A. | No segment assets or liabilities on a concall. The Thane vs JDA booking mix is covered under FND-19. |
| F13 Board outcome beyond results | N.A. | No board outcome document. The EGM approval (L151) and the future capital decision (L410) are logged under F10, not counted twice. |
| F14 Note drafting inconsistencies | N.A. | No notes or auditor letter. Entity-name variants ("Raymond Reit", two CFOs named at L31-32, "Ipro") are ASR artefacts, not company drafting. |
| F15 Entity list diffs | FINDING | FND-12: the 10X subsidiary changes from wholly owned to having an AIF (ICICI Pru) OCPRS holder with 60% of the capital. |
| F16 Dropped / reframed disclosures | FINDING | FND-03: the call shows the revenue guide was dropped from the deck (analyst cites the Aug-19 deck, slide 9, L242-244). Logged here because the transcript carries the evidence directly. |
| F17 Silence audit | FINDING | FND-02 (checklist #1 at the boundary), FND-09 (risk #2 first signals lit), FND-22 (silence table, Section 4). |

Totals: 7 FINDING / 0 PASS / 10 N.A. / 0 blank. GATE A3: pass.

## 3. COMMITMENT REGISTER (F6)

| # | commitment | implied date | ref (line / row) | status word |
| --- | --- | --- | --- | --- |
| C-01 | FY27 EBITDA margin 17-19% | FY27 (Mar-2027) | L53-54, L176 / R207, R223 | underway (reaffirmed; H1 ~14%) |
| C-02 | Margin normalisation as projects reach mid-stage | through FY27 "into next year" (FY28) | L50-52 / R206 | underway (window widened) |
| C-03 | Pre-sales growth of at least 20% | FY27 | L174-175, L237-238 / R221, R227 | underway (reaffirmed) |
| C-04 | EBITDA growth 20% | FY27 | L237, L536-537 / R226, R139 | initiated (new verbal form) |
| C-05 | ROCE 20% | FY27 | L175 / R222 | underway (reaffirmed) |
| C-06 | PAT margin 9-10% | FY27 | L176-178 / R224 | initiated (vs Q1 refusal; see FND-04) |
| C-07 | Revenue growth "in that range", no number | FY27 | L246, L545-547 / R228, R260 | softened (formal guide withdrawn) |
| C-08 | Interest cost H2 at the H1 run rate | H2 FY27 | L266-267 / R229 | initiated (100-120 Cr guide not restated) |
| C-09 | Gross debt stabilises at Rs 1,200-1,400 Cr; within 1:1 | FY27-FY28 | L139-140, L476-478 / R213, R214, R254 | underway |
| C-10 | Debt does not fall for 1-2 years | to ~FY28-FY29 | L471-472 / R252 | initiated |
| C-11 | Promoter equity ~Rs 400-410 Cr; first tranche "shortly", balance per schedule | first tranche Q3 FY27; balance by ~Apr-2028 (tracker) | L149-151, L208 / R215 | underway (EGM-approved; receipt unconfirmed) |
| C-12 | ICICI AIF Rs 210 Cr: first tranche within 30 days, full sum by March | ~Nov-2026; Mar-2027 | L376-377 / R240, R241 | initiated (not received at call date) |
| C-13 | Further equity Rs 400-600 Cr under the new LRP, board and shareholders to decide | LRP window (FY28-FY32) | L409-410, L475 / R246, R253 | initiated |
| C-14 | Two Mahim launches: one in Q3, one in Q4; GDV ~Rs 4,100 Cr | Q3 FY27 (Oct-Dec 2026); Q4 FY27 | L166-167, L368 / R218, R239 | underway (unchanged from Q1) |
| C-15 | Mahim launch inventory decided closer to launch | at launch | L382 / R242 | initiated |
| C-16 | BKC aviation approval, then RERA registration of upper floors | "next few weeks" (~Nov-Dec 2026) | L517-518, L522 / R257, R258 | underway (pending) |
| C-17 | More JDAs to sign; Rs 8,000-10,000 Cr GDV added every year | annual, 5 years | L169, L413 / R219, R247 | underway (H1 Rs 8,500 Cr) |
| C-18 | 5-year LRP: ~20% pre-sales CAGR | FY28-FY32 | L404-407 / R245 | completed (LRP finalised) / initiated (delivery) |
| C-19 | Steady state of 8-10 projects outside Thane; quarterly stability | ~FY29 ("within two years", MD estimate) | L121-126 / R211, R212 | initiated |
| C-20 | JDA project turns cash positive from year 3 or mid year 3 | per project | L117-119 / R210 | standing claim |
| C-21 | Rs ~10,000 Cr pre-tax operating cash flow from the current portfolio | next 4-5 years | L357-362 / R237, R238 | initiated (first disclosure) |
| C-22 | Thane sales stabilise at Rs 1,500-1,600 Cr a year | ongoing | L439-440 / R249 | standing claim |
| C-23 | Research coverage from 1 firm to at least 4 | by end of "this year" | L316-317 / R232, R233 | underway |
| C-24 | Project-wise launch break-up to be sent to the analyst separately | unspecified | L346 / R236 | initiated |
| C-25 | Future launches: cost impact partly passed on, partly absorbed; margins maintained | FY27 H2 launches onward | L603-605 / R262, R263 | hedged |
| C-26 | Continue PE-partner / ICICI-type deals for the right projects | ongoing | L217-218, L389-391 / R225, R244 | standing claim |
| C-27 | Thane OC for Address by GS Tower B received ahead of the RERA timeline | Q2 FY27 | L64-67 / R015 | completed |

## 4. WHAT WAS NOT DISCUSSED (F17 silence table)

| item | source | addressed on Q2 call? | consecutive quarters silent | note |
| --- | --- | --- | --- | --- |
| #6 Related-party loans to subs (stable Rs 1,000-1,200 Cr / red >Rs 1,500 Cr) | Notion checklist | No | 2 (Q1, Q2) | The new 10X NCI structure (FND-12) makes this more relevant. |
| #7 Raymond Ltd promoter governance event | Notion checklist | No (only the promoter equity infusion was discussed) | 2 | Silence is GREEN by the checklist definition; no event was raised. |
| #9 Thane commercial optionality | Notion checklist | No | 2 | 12-month silence = expires; window advancing. |
| #10 Quarterly CFO figure | Notion checklist; Q1 QM-13 | No figure; sent to deck slide 23 (L110-112) | 2 | Only qualitative "Tana is already net cash positive" (L123). |
| Thane Jekegram launch (RERA) vs warrant objects Rs 247 Cr | Downstream tracker | No | 1 (Q1 status not recorded) | Warrant objects not linked to any spoken use of the money. |
| Q1 QM-2 Parel route to market (~18 months) | Q1 questions | No | 1 | Parel not named on the call. |
| Q1 QM-3 Which JDAs reach 6 of 8 launched by FY27-end; Kandivali | Q1 questions | Partly (4 launched + 2 Mahim = 6 implied, L86-87, L166) | 1 (Kandivali) | Kandivali not named. |
| Q1 QM-6 ROCE step-down from >25% to 20% | Q1 questions | No; 20% reaffirmed (L175) | 1 | |
| Q1 QM-7 Exact FY27 interest cost | Q1 questions | No; "same run rate" only (L266-267) | 1 | FND-06. |
| Q1 QM-8 D/E reconciliation | Q1 questions | Addressed; does not tie | n/a | FND-07. |
| Q1 QM-9 Runway 6-7 vs 7-8 years | Q1 questions | No | 1 | |
| Q1 QM-11 CFO presence on finance questions | Q1 questions | Indeterminate (speakers unlabelled) | n/a | Two people introduced as CFO (L31-32); answers read as the MD's ("Amit who is on the call with me", L319). Operator to confirm. |
| Q1 QM-12 Blended cost including the government-dues leg | Q1 questions | No; leg disclosed again at Rs 17 Cr | 1 | FND-08. |
| Watch item: margin basis with or without other income | Orchestrator watch list; R168 FOOTNOTE_UNRESOLVED | No; only the analyst's "16 and a half percent including your other income" (L539) | 1 | The 17-19% guide basis is still unstated. |
| Watch item: Ind AS 115 revenue timing | Orchestrator watch list | Partly ("we follow percentage completion", L233-234) | n/a | Confirm the policy and thresholds against the AR. |

## 5. CHECKLIST ITEMS ADDRESSED (scored for A4; management tier)

| # | monitor | Q2 reading | status |
| --- | --- | --- | --- |
| 1 | EBITDA margin | 15% (L48); boundary, EBITDA rupee figure garbled | AMBER, unscorable until Reg 33 (FND-02) |
| 2 | Booking value | H1 Rs 1,602 Cr +111% (L63); Q2 ~Rs 900 Cr (analyst, L499) | GREEN |
| 3 | Net debt | Rs 912 Cr (L98), up from 824 | AMBER (below Rs 1,000 Cr red; FND-09) |
| 4 | Mahim 1 & 2 | Q3 and Q4 (L368), no date | GREEN pending Q3 RERA (FND-15) |
| 5 | New JDA signings | Rs 8,500 Cr H1 (L73) | GREEN (target met; I-5 caution, FND-17) |
| 8 | Cost of debt | 9.6% (L102); government leg excluded | GREEN headline; effective higher (FND-08) |

## 6. A4 HAND-OFF

- FORWARD-SIGNAL (convert to management questions): FND-01, FND-03, FND-10, FND-11, FND-12, FND-15, FND-16, FND-17, FND-20, FND-21, FND-23.
- AMBIGUOUS (convert to management questions): FND-02, FND-04, FND-05, FND-06, FND-07, FND-08, FND-13, FND-14.
- CONFIRMATORY-NEGATIVE (carry to verdict; questions optional): FND-09, FND-18, FND-19, FND-22.
- Operator rulings still pending that bind these findings: which margin stop applies to Q2 (FND-02); whether the AIF money counts before or after the net-debt lines (FND-09, FND-13, FND-14).

```yaml
stage: A3-forensics
company: "RAYMONDREL"
quarter: "q2fy27"
doctype: "concall"
model: "claude-opus-5-5"
status: complete
forensics_path: "runs/raymondrel-q2fy27/work/forensics_concall_raymondrel_q2fy27.md"
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
  F10: FINDING
  F11: FINDING
  F12: N.A.
  F13: N.A.
  F14: N.A.
  F15: FINDING
  F16: FINDING
  F17: FINDING
findings:
  - {id: "FND-01", check: "F6", line: "L50-54; L176", classification: "FORWARD-SIGNAL", implication: "17-19% FY27 margin guide back-ended; H1 ~14%, H2 needs ~20-24% if H2 income = H1; normalisation window widened into FY28"}
  - {id: "FND-02", check: "F17", line: "L47-48", classification: "AMBIGUOUS", implication: "Q2 margin 15% sits on the <15% two-quarter stop boundary; EBITDA rupee figure garbled; score only on Reg 33; margin-stop ruling pending"}
  - {id: "FND-03", check: "F16", line: "L227-230; L242-244; L543-547", classification: "FORWARD-SIGNAL", implication: "Revenue guide (min 20% in Q1 notes, Aug-19 deck slide 9) withdrawn; verbal 'that range', no number; sub-20% revenue is the conservative case"}
  - {id: "FND-04", check: "F6", line: "L176-178", classification: "AMBIGUOUS", implication: "PAT margin 9-10% called 'earlier guidance' though Q1 notes record a PAT refusal; I-6 may be turning; confirm against deck/filing"}
  - {id: "FND-05", check: "F6", line: "L351-365", classification: "AMBIGUOUS", implication: "First portfolio OCF figure, Rs ~10,000 Cr pre-tax over 4-5 yrs; basis (pre-tax, interest, GDV 52k vs 50k) unclear; 'pretty tight'"}
  - {id: "FND-06", check: "F6", line: "L104-105; L260-267", classification: "AMBIGUOUS", implication: "Interest H2 = H1 run rate implies ~Rs 180 Cr all-in FY27 vs prior Rs 100-120 Cr guide, which was not restated; possibly bank-only"}
  - {id: "FND-07", check: "F11", line: "L98-100", classification: "AMBIGUOUS", implication: "Implied net worth ~Rs 1,500 Cr (gross 0.8x) vs ~Rs 1,824 Cr (net ~0.5x), ~22% gap; second quarter D/E fails to tie"}
  - {id: "FND-08", check: "F11", line: "L102; L105-109", classification: "AMBIGUOUS", implication: "Government-dues interest Rs 17 Cr/qtr (~Rs 68 Cr/yr vs ~45 FY26) outside the 9.6% cost of debt and likely outside gross debt"}
  - {id: "FND-09", check: "F17", line: "L98-99", classification: "CONFIRMATORY-NEGATIVE", implication: "Risk #2 first signals both lit (net debt 912 >900; gross D/E 0.8x >0.75x); +88 Cr QoQ; Rs 1,000 Cr red line not fired"}
  - {id: "FND-10", check: "F6", line: "L140; L211-214; L471-472", classification: "FORWARD-SIGNAL", implication: "Equity raised because debt cannot rise further; gross debt holds Rs 1,200-1,400 Cr for 1-2 yrs; I-3 red-leaning"}
  - {id: "FND-11", check: "F10", line: "L149-151; L205-208; L408-410; L473-476", classification: "FORWARD-SIGNAL", implication: "Dilution: ~Rs 410 Cr promoter issue (received vs committed unclear) plus new Rs 400-600 Cr LRP equity; prior no-fundraise stance reversed"}
  - {id: "FND-12", check: "F15", line: "L145-146; L193-202; L219-221", classification: "FORWARD-SIGNAL", implication: "10X subsidiary gains AIF OCPRS holder at 60% capital; NCI line coming; 5% fee eliminates on consolidation; margin-uplift claim is economic, not consolidated"}
  - {id: "FND-13", check: "F7", line: "L486-490; L584-587", classification: "AMBIGUOUS", implication: "OCPRS equity treatment is management's assertion; 'virtually zero' coupon; Ind AS 32 terms decide; ties to the pending AIF-money ruling"}
  - {id: "FND-14", check: "F6", line: "L146; L152; L376-377; L480", classification: "AMBIGUOUS", implication: "ICICI money not received at call date ('raised' = committed); tranche Q3, rest by Mar-2027 lowers net debt via financing; 140 likely RR's 40% share (derived)"}
  - {id: "FND-15", check: "F6", line: "L166-167; L366-368; L380-382", classification: "FORWARD-SIGNAL", implication: "Mahim Q3 + Q4 launches unchanged; Q3 is current quarter with no RERA date or inventory call; launch tied to ICICI tranche"}
  - {id: "FND-16", check: "F6", line: "L516-524", classification: "FORWARD-SIGNAL", implication: "BKC upper floors need aviation approval ('next few weeks') then RERA; H2 Invictus pre-sales contingent"}
  - {id: "FND-17", check: "F6", line: "L72-74; L168-169; L412-413", classification: "FORWARD-SIGNAL", implication: "No apparent new JDA in Q2; LRP adds Rs 8-10k Cr GDV every year, which is the I-5 red case that resets the cash clock"}
  - {id: "FND-18", check: "F6", line: "L64-66; L88-89; L117-119; L124-126", classification: "CONFIRMATORY-NEGATIVE", implication: "Only Thane delivering (I-1 red); JDAs collected 25% of bookings; most JDAs cash-negative into FY28 (I-7 red)"}
  - {id: "FND-19", check: "F6", line: "L438-440", classification: "CONFIRMATORY-NEGATIVE", implication: "Thane ex-growth at Rs 1,500-1,600 Cr/yr (bottom of current band); all growth and risk shift to JDAs"}
  - {id: "FND-20", check: "F7", line: "L590-592; L602-608", classification: "FORWARD-SIGNAL", implication: "Fixed-price contracts cover ongoing projects only; H2 Mahim and LRP launches carry cost inflation; margin hedge"}
  - {id: "FND-21", check: "F7", line: "L276-278; L287; L290-291", classification: "FORWARD-SIGNAL", implication: "Management expects rate hardening on a debt base that will not fall; checklist #8 (>10.5% red) at risk; demand view scoped to own portfolio"}
  - {id: "FND-22", check: "F17", line: "L110-112 (CFO to slide 23); silence table Section 4", classification: "CONFIRMATORY-NEGATIVE", implication: "Monitors #6, #7, #9, #10 silent 2 consecutive quarters; 7 of 13 Q1 questions unaddressed"}
  - {id: "FND-23", check: "F6", line: "L43-45; L385-387; L492-500", classification: "FORWARD-SIGNAL", implication: "20% pre-sales needs ~Rs 1,900-2,000 Cr H2 vs Rs 1,602 Cr H1; ~78% of Q2 from one product line (analyst-stated); H2 depends on Mahim and BKC"}
forward_signals: ["FND-01", "FND-03", "FND-10", "FND-11", "FND-12", "FND-15", "FND-16", "FND-17", "FND-20", "FND-21", "FND-23"]
ambiguous: ["FND-02", "FND-04", "FND-05", "FND-06", "FND-07", "FND-08", "FND-13", "FND-14"]
commitments:
  - {commitment: "FY27 EBITDA margin 17-19%", implied_date: "FY27", ref: "L53-54, L176 / R207, R223", status_word: "underway"}
  - {commitment: "Margin normalisation as projects reach mid-stage", implied_date: "FY27 into FY28", ref: "L50-52 / R206", status_word: "underway"}
  - {commitment: "Pre-sales growth >=20%", implied_date: "FY27", ref: "L174-175, L237-238 / R221, R227", status_word: "underway"}
  - {commitment: "EBITDA growth 20%", implied_date: "FY27", ref: "L237, L536-537 / R226", status_word: "initiated"}
  - {commitment: "ROCE 20%", implied_date: "FY27", ref: "L175 / R222", status_word: "underway"}
  - {commitment: "PAT margin 9-10%", implied_date: "FY27", ref: "L176-178 / R224", status_word: "initiated"}
  - {commitment: "Revenue growth near 20%, no number", implied_date: "FY27", ref: "L246, L545-547 / R228, R260", status_word: "softened"}
  - {commitment: "Interest H2 at H1 run rate", implied_date: "H2 FY27", ref: "L266-267 / R229", status_word: "initiated"}
  - {commitment: "Gross debt stabilises Rs 1,200-1,400 Cr within 1:1", implied_date: "FY27-FY28", ref: "L139-140, L476-478 / R213, R214, R254", status_word: "underway"}
  - {commitment: "Debt does not fall for 1-2 years", implied_date: "to ~FY28-FY29", ref: "L471-472 / R252", status_word: "initiated"}
  - {commitment: "Promoter equity ~Rs 400-410 Cr, first tranche shortly", implied_date: "Q3 FY27; balance ~Apr-2028", ref: "L149-151, L208 / R215", status_word: "underway"}
  - {commitment: "ICICI AIF Rs 210 Cr, first tranche 30 days, full by March", implied_date: "~Nov-2026; Mar-2027", ref: "L376-377 / R240, R241", status_word: "initiated"}
  - {commitment: "Further equity Rs 400-600 Cr under LRP", implied_date: "FY28-FY32", ref: "L409-410, L475 / R246, R253", status_word: "initiated"}
  - {commitment: "Mahim launches Q3 and Q4, GDV ~Rs 4,100 Cr", implied_date: "Q3 FY27; Q4 FY27", ref: "L166-167, L368 / R218, R239", status_word: "underway"}
  - {commitment: "Mahim launch inventory decided near launch", implied_date: "at launch", ref: "L382 / R242", status_word: "initiated"}
  - {commitment: "BKC aviation approval then RERA for upper floors", implied_date: "next few weeks (~Nov-Dec 2026)", ref: "L517-518, L522 / R257, R258", status_word: "underway"}
  - {commitment: "Add Rs 8,000-10,000 Cr GDV every year; more JDAs to sign", implied_date: "annual, 5 years", ref: "L169, L413 / R219, R247", status_word: "underway"}
  - {commitment: "5-year LRP ~20% pre-sales CAGR", implied_date: "FY28-FY32", ref: "L404-407 / R245", status_word: "initiated"}
  - {commitment: "Steady state 8-10 projects outside Thane", implied_date: "~FY29 (MD estimate)", ref: "L121-126 / R211, R212", status_word: "initiated"}
  - {commitment: "Rs ~10,000 Cr pre-tax operating cash flow from current portfolio", implied_date: "next 4-5 years", ref: "L357-362 / R237, R238", status_word: "initiated"}
  - {commitment: "Thane sales stabilise Rs 1,500-1,600 Cr/yr", implied_date: "ongoing", ref: "L439-440 / R249", status_word: "initiated"}
  - {commitment: "Research coverage 1 -> at least 4 firms", implied_date: "end of this year", ref: "L316-317 / R233", status_word: "underway"}
  - {commitment: "Project-wise launch break-up to analyst", implied_date: "unspecified", ref: "L346 / R236", status_word: "initiated"}
  - {commitment: "Future-launch cost impact part passed on, part absorbed; margins maintained", implied_date: "H2 FY27 onward", ref: "L603-605 / R262, R263", status_word: "initiated"}
  - {commitment: "Thane OC Address by GS Tower B ahead of RERA timeline", implied_date: "Q2 FY27", ref: "L64-67 / R015", status_word: "completed"}
gate_a3: pass
blank_checks: []
analyst_note: "Lean-bear read of an ASR transcript; every number is management tier. Three threads matter for A4. (1) Capital: debt will not fall for 1-2 years (L471-472). Equity is raised because the market worries about debt (L211-214). The new LRP adds Rs 400-600 Cr more equity (L409, L475) on top of ~Rs 410 Cr promoter money and Rs 210 Cr ICICI money. The 1:1 ceiling binds in practice, and Q3 net debt will fall for financing reasons, not operating ones. (2) Guidance: the revenue guide was dropped from the deck (L227-229, L242-244) and replaced by 'that range' with no number. The 17-19% margin guide needs an H2 near 20-24% from an H1 near 14%. PAT 9-10% is called 'earlier guidance' though Q1 notes record a refusal. (3) The Q2 margin of 15% sits on the <15% stop boundary and the EBITDA rupee figure is garbled (L47). The stop cannot be scored until Reg 33 lands and the margin-stop ruling is made. The 140 vs 210 ICICI conflict likely resolves as RR's 40% share (arithmetic, unconfirmed). The 10X NCI means consolidated EBITDA will overstate RR's economic share of Mahim."
```
