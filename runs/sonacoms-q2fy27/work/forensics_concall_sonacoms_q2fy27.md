# FORENSICS (A3) — concall — SONACOMS (Sona BLW Precision Forgings Ltd) — Q2 FY27

Doctype: concall (26-Oct-2026, Nomura-hosted Webex). Source class: MACHINE ASR transcript (faster-whisper small.en), management-tier, unverified, speakers not identified (53 inferred turns). Filed documents win on any conflict. Anchors: fulltext L### and [hh:mm:ss].
Inputs read: A1 structured (R001-R336), A1 fulltext (L001-L921, all lines), A2 ledger (336 R rows + M01-M09), Notion COMPANIES MASTER page saved 28-Oct-2026 (operator memory, not corpus; used only for the F17 checklist and prior-quarter commitment register). Prior-quarter fulltext: not available (no prior SONACOMS concall extraction in repo). Source PDF and inputs/ not opened.
Model: claude-opus-5-5. Date: 2026-10-28.

## 0. Ledger reconciliation (100%)

- Rows in ledger: 336 structured IDs (R001-R336) + 9 MISSING_FROM_STRUCTURED (M01-M09) = 345. Rows read at cited line: 345. ledger_reconciled_pct = 100.
- Every R row was read in the structured file and its quote located in the fulltext. Every M row was read at its own line (M01 L092, M02 L101, M03 L144, M04 L149, M05 L243, M06 L558, M07 L577, M08 L136, M09 L217); all nine verified verbatim.
- Anchor discrepancies found (none changes a claim; recorded for A1/A2 hygiene):
  - R187 "aerospace" cites L647; the word is at L658 ("so like aerospace is a segment where everybody's looking at").
  - R206 (INFERRED TURN BOUNDARY, CEO opening) cites L050; the CEO starts speaking at L029 ("Hi, I'm Gopal and welcome everyone."). T03 span in the ledger (L29-L280) is right; the boundary row anchor is 21 lines late.
  - R038 cites L249; "37% increase" is at L250. R114 cites L774; "1% of our revenue even in 2019" is at L775.
  - One-to-two-line offsets on multi-line spans (acceptable): R152-R154, R162, R170, R171, R177, R233, R243, R249, R293, R331, R335.
- Spoken-number internal arithmetic (my arithmetic on ASR figures, not filed): Q2 EBITDA 356 / revenue 1,546 = 23.0% (ties R051); H1 EBITDA 659 / 2,857 = 23.1% (ties R064); H1 PAT 404 / 2,857 = 14.1% (ties R068); CFO 594 / 659 = 90% (ties R071); 594 - 148 = 446 FCF (ties R074); Q1 implied revenue 2,857 - 1,546 = 1,311 (ties R045 1,310); Q1 implied EBITDA 659 - 356 = 303. The spoken set coheres except R054 and R060 (below).

### ASR number reconciliation (A2 section 9 items)

| Item | Lines | Spoken | Internal check (my arithmetic, ASR figures) | Disposition |
|---|---|---|---|---|
| R054 Q2 PAT | L320-321 | "Profit after tax grew by 29% to 23 crores." / "Pat margin was 14.4%" | 14.4% x 1,546 = about 223 | ASR dropped a digit. Not finding-driving. Filed number governs (Notion memory logs owners' PAT 223.4 Cr from the filing; A4 confirms against filed doc). |
| R052 margin delta | L314 | "Evita margin was 23% which was lower by 2.3%" | 23.0 + 2.3 = 25.3% prior-year Q2; H1 "lower by about one and a half percent" (L332) is coherent with Q1 down about 0.7 pt (Notion memory) | Reads as 2.3 percentage points, not an ASR merge. Drives A3-F17-01; basis (rev-ops vs incl. forex) still a question. |
| R021 vs R060 vs R023/R061 | L163-166, L328-329, L276 | "revenues have crossed the 10 billion mark ... now it's 48% for the first half"; "Our BV revenue grew by 119%, 2,042 crores, and constituted 48% of our automotive product sales" | 2,042 / 2,857 = 71% of total H1 revenue; auto is about 70% of revenue (L276), so 2,042 cannot be 48% of automotive product sales. 10 bn (about 1,000 Cr) / about 2,000 Cr auto = about 50%, coherent with 48%. | UNRESOLVED. Drives A3-F14-01. Management/filed-deck question; do not pick a number from the transcript. |
| R031/R032/R108 order units | L215, L219-220, L745 | "36 billion", "251 billion", "4% of a $250 billion order book" | Same book stated in two currencies | Unit/currency slip. Drives A3-F14-03. |

## 1. FINDINGS TABLE

| id | check | ledger row ref | line/turn | short verbatim quote | classification | forward implication |
|---|---|---|---|---|---|---|
| A3-F6-01 | F6 | R321 (context R051, R052); Notion C1 | L053-L057 (T03) | "Last quarter, I'd spoken about margins improving on cost pass through ... However, this quarter, the continued margin pressure has been there, but it's mainly driven by change in product mix." | CONFIRMATORY-NEGATIVE | Management itself scores Q1 promise C1 (recovery from Q2) as not delivered and moves the cause from input cost to mix. Mix cause is structural while traction motors outgrow (L060 "almost 50% quarter on quarter"); a mix-driven margin does not recover by pass-through. C1 = MISS, conceded on the call. |
| A3-F6-02 | F6 | R232, R234, R237, R092, R093, R333 | L610-L611, L618, L630-L634 (T29-T30) | "23 to 25 is fair" / "if the world is operating in a normal fashion, I think we should probably, around 23%. I don't hold us to like every 10 or 20 bips, but I think that's probably ballpark" | FORWARD-SIGNAL | Range kept, but the CFO's working number is the floor, with a stated 10-20 bps tolerance below it. That tolerance band (22.8-23.0%) sits on the Notion bear line (<23.0%). Treat 23% as the ceiling of the near-term base, not the floor. Five-year margin exercise exists (L616-L617) but is undisclosed. |
| A3-F6-03 | F6 | R223, R224, R225, R226, R289, R290, R291, R162, R163 | L435-L445, L449-L453 (T10-T13) | "JV1 part of it, which is carving out of the business by end of December ... it may spill over to January" / "JV-2 ... it's not yet formed up, but we are targeting to close ... first half of calendar year, 27" | FORWARD-SIGNAL | First dated DENSO close guidance: JV1 end-Dec 2026 or Jan 2027 (Q3/Q4 FY27); JV2 H1 CY2027. JV1 close is when eDrive stops being wholly owned: like-for-like margin/ROCE breaks, NCI or equity-method treatment begins, and a gain lands. Pre-emptive slip cover already given (advisors' holidays, L450-L453). |
| A3-F6-04 | F6 | R105, R243, R239, R097-R100 (analyst), R330 | L660-L664, L697-L700 (T34) | "we will pay tax on ... JV2 also has some, you know, amount that we will block for the CapEx" / "cash to a better ratio, as long as it doesn't go above 1.5, we don't have to rush into any decision" | FORWARD-SIGNAL | Management states its own capital-deployment trigger: cash/EBITDA 1.5x. Gross cash 1,966 Cr (L361) over annualised H1 EBITDA (659 x 2 = 1,318) is about 1.49x already (my arithmetic, ASR figures, gross basis); H2 FCF plus DENSO proceeds push it above 1.5x by FY27 end. An M&A or capital-return decision is therefore likely inside the 12-month window. Basis (gross or net cash; trailing or forward EBITDA) not stated. |
| A3-F6-05 | F6 | R229, R230, R231; M06 | L554-L562, L565-L566 (T22-T24) | "we are launching another product in this current quarter" / "I think that was pretty small so far" | FORWARD-SIGNAL | Dated motor-business launch in Q3 FY27 (product unnamed). 3W traction is small today; the "share should kick in" claim is undated. Scorable at the Q3 call. |
| A3-F6-06 | F6 | R109, R246, R247, R248, R249, R297, R245 | L748-L754, L761-L767 (T37) | "when we give our ranges for EBITDA, et cetera, those are considering all these facts" / "62 crore of capex is for this area that should cover it" / "Bharat expo I think in February" | FORWARD-SIGNAL | Robotics R&D is inside the margin range and "will continue" (L761); it is a named drag on % margin (L751-L752 "one of the reasons also that the margins are not"). Next robotics milestone offered is a February 2027 demonstration, not an SOP or revenue date. |
| A3-F7-01 | F7 | R211, R212, R213 | L069-L072 (T03) | "Both these factors are largely beyond our control, which makes near-term predictability a little difficult, however, it is mostly good news because absolute margins continue to improve" | FORWARD-SIGNAL | Pre-emptive cover for Q3 % margin, and a pivot of the yardstick from % margin to absolute EBITDA. The gate variable is % margin; management now steers to a metric that rises with revenue alone. |
| A3-F7-02 | F7 | R263, R264, R265, R334, R120-R122 | L858-L868, L875-L878 (T47-T48) | "Yes, we do, but how so." / "there is a possible mechanism with the customers" / "even when the full pass-through happens ... arithmetically, the percentage margin tends to come down" | FORWARD-SIGNAL | Pass-through restores rupees, not %. % recovery is now conditional on material prices falling (L878). C1 as framed in Q1 cannot deliver % recovery in a flat or rising commodity tape. |
| A3-F7-03 | F7 | R220, R221, R222, R332, R160, R331, R037 | L401, L417-L418, L427-L430 (T08) | "It is very hard to predict the trajectory." / "The order book so far is limited to that one customer" / "I can't give you anything definite" | AMBIGUOUS | Fastest-growing product (suspension motors, "already reached 7%", L241) rests on one customer and one vehicle model (China, L084). Upside is real but single-point; a model cycle at that OEM moves about 7% of revenue. |
| A3-F7-04 | F7 | R250, R251, R336; Notion C2, C9 | L772, L776-L778 (T39) | "I don't know is the real answer." / "this is a recorded call and you know you can always hold me to it ... which is why we don't want to stick our neck out on this one" | FORWARD-SIGNAL | Date retreat. Q1 gave dated robotics SOPs (Notion C2: one this quarter, one next, one within 15 months); Q2 refuses any timing and gives the reason as accountability. Robotics drew five separate asks (Q05, Q12, Q13, Q14, Q18) and none got a date. |
| A3-F7-05 | F7 | R006 (ASR "Prey trades"), R189, R190 | L064-L067 (T03) | "Prey trades have also risen sharply. They've nearly doubled from previous quarters level." | AMBIGUOUS | Freight (ASR reading) doubled QoQ. The pass-through answer (L860-L882) covers material only. Whether freight is passed through is unstated; an unrecovered freight line is a separate % headwind. |
| A3-F8-01 | F8 | R239, R099 (analyst), R186 | L649, L660-L661 (T33-T34) | "by year end, 900 crore from Denso" (analyst) / "what we get from Denso will pay tax on" | FORWARD-SIGNAL | First management statement on DENSO tax: proceeds are taxable. Management did not contest the analyst's 900 Cr by year end, nor confirm it. Expect a one-off tax charge (and a gain, likely exceptional) in the JV1 close quarter; ETR in that quarter will not be comparable. ETR itself not spoken. |
| A3-F10-01 | F10 | R078, R198 | L358 (T05) | "There was an inflow on account of ESOPs exercised by employees, about 108 crores" | NEUTRAL-FACT | H1 dilution source spoken. Basic vs diluted spread not on the call. A4 cross-checks against the Notion share-base log (allotments 28-Aug to 03-Oct; MD PSP 1,70,747 shares). |
| A3-F14-01 | F14 | R021, R060, R061, R023, R042, R324 | L163-L166, L328-L329, L276 | "revenues have crossed the 10 billion mark" vs "Our BV revenue grew by 119%, 2,042 crores, and constituted 48% of our automotive product sales" | AMBIGUOUS | Spoken H1 BEV/EV revenue figures cannot all be true (2,042 Cr = 71% of total H1 revenue against a 70:30 auto split). Possible ASR error or a different basis. Do not carry any H1 BEV rupee figure from this transcript; take it from the filed deck. |
| A3-F14-02 | F14 | R115, R114, R015, R048, R324 | L131-L132, L311-L312, L775 | "BEVs contribute more than 50% of our automotive revenue" / "51% of our automotive product sales" / "It was 1% of our revenue even in 2019. And now it's 51%." | AMBIGUOUS | Basis drift in management's own framing: the same 51% is cited as share of automotive product sales (CFO), automotive revenue (CEO) and total revenue (CEO anecdote). On a 70:30 split, BEV is nearer 36% of total revenue (my arithmetic). The drift overstates EV dependence of the whole company, a bull framing on tripwire 9. |
| A3-F14-03 | F14 | R032, R108, R033, R031, R313 | L219-L222, L745 | "net order book of 251 billion" / "4% of a $250 billion order book" | AMBIGUOUS | Same order book stated in rupee and dollar terms; dollar is a speech or ASR slip. Robotics share is 4% (Q1 3%, Notion memory), so about Rs 10 bn (my arithmetic, rupee basis). Ask for robotics order book in Rs Cr and its revenue-conversion schedule. |
| A3-F14-04 | F14 | R160, R331, R306, R307 | L011-L014, L402-L403 | "Please refrain from naming any customer" / "this is public information so I can share it with Neo" | NEUTRAL-FACT | CEO names an end customer (ASR "Neo") after the call rule bars naming. Individually immaterial; it also confirms the single-customer, China-linked base of suspension motors (A3-F7-03). |
| A3-F17-01 | F17 | R051, R052, R065, R321 | L313-L315, L331-L333 | "Evita margin was 23% which was lower by 2.3% compared to the same quarter last year" / H1 "lower by about one and a half percent" | CONFIRMATORY-NEGATIVE | Checklist margin leg addressed. YoY compression widened from about 0.7 pt in Q1 (Notion memory) to about 2.3 pt in Q2 (ASR figure, basis unstated). Bull line (>=24.5%) clearly missed; bear line (<23.0%) depends on basis, which the call never states. |
| A3-F17-02 | F17 | R003, R139, R153, R140, R245; Notion C2 | L098-L105, L744-L747 (T03, T37) | "we commercialized three new products ... helical limited slip differential, air springs for railways and rear radar sensors" / "We have orders. It's still small" | AMBIGUOUS | Promise C2 (first robotics SOP in Q2) is never scored by management despite five robotics questions. None of the three Q2 launches is robotics. Lean bear: C2 not delivered until shown. 1 quarter of silence. |
| A3-F17-03 | F17 | R032, R216 | L219-L220 (T03) | "we have closed Q2 with a net order book of 251 billion as we continue to win new business in EVs" | AMBIGUOUS | EV share of the order book (61%, third straight easing per Notion memory of the filed deck) is not stated on the call; the only EV framing is positive. 1 quarter of silence on a deteriorating metric; a repeat at Q3 makes it CONFIRMATORY-NEGATIVE. |
| A3-F17-04 | F17 | R072, R077, R070, R071, R315, R096 | L350-L353, L357, L644 | "supported mainly by release of 44 crores from working capital" / "cash inflows on account of additional borrowings of 224 crores" / "That's gross" | AMBIGUOUS | CFO/PAT leg is computable from spoken figures (594 / 404 = 1.47x, my arithmetic) and passes. The call frames working capital as a net 44 Cr release; it is silent on the payables build that carried it (Notion memory: +278.8 Cr payables, filed). It adds 224 Cr of borrowing while holding about 1,966 Cr gross cash, with no reason given. Payables unwind risk for 9M CFO/PAT. |
| A3-F17-05 | F17 | R214, R219, R320 | L152-L153, L367-L368 | "Our return ratios have also improved and we expect them to continue improving" | AMBIGUOUS | ROCE number and the path to >18% again not spoken (2 consecutive calls). Direction claimed up; the number and the un-normalised basis are withheld. |
| A3-F17-06 | F17 | R185, R192 | L652-L653, L757 | "since IPO we have only seen novelic as a MNA" (analyst) / "the novella teams time" | AMBIGUOUS | Novelic named twice, impairment and carrying value never addressed (2 consecutive calls). Tripwire 3 stays silent; the KAM indicator from the FY26 AR is unanswered. |
| A3-F17-07 | F17 | R049-R052 | L313-L314 | "Our EBITDA for the quarter grew by 23% to 356 crores. Evita margin was 23%" | CONFIRMATORY-NEGATIVE | Forex gain inside revenue and the margin basis (incl. or ex forex) not stated, 2 consecutive calls. The Q2 gate sits between bull and bear only on the forex-inclusive basis (operator ruling pending); sustained silence on the variable that decides a deteriorating metric. |
| A3-F17-08 | F17 | R223-R226, R239, R162, R163 | L435-L445, L660-L661 | "we shared the announcement of JV is now we have to finalize and close those" | AMBIGUOUS | DENSO financial terms (EV Rs 1,750 Cr, 49% stake, slump-sale of the EV motors business, post-close accounting, gain quantum and line) still not stated, 2 consecutive calls. Close dates now given (A3-F6-03); terms are not. |
| A3-F17-09 | F17 | R310, R253-R258 | L809-L811, L824-L825 (T41) | "We don't share business-wise growth outlook or we don't get growth guidance." / "It's more dependent on whether we are successful to launch these products on time" | AMBIGUOUS | Head of Railway spoke this time (Q1: 0 turns) but gave no revenue or PAT and declined guidance. Railway quantum silent 2 consecutive calls; growth is conditional on on-time launches. |
| A3-F17-10 | F17 | R009, R135, R136 | L113-L118 (T03) | "our drive line division has won the 2026 Deming Prize for Total Quality Management" | AMBIGUOUS | Quality is celebrated; the H1 warranty provision rise (12.5 Cr vs 2.2 Cr) and slow-moving inventory provision (8.0 Cr vs 1.2 Cr) logged from the filing in Notion memory are not mentioned. Together about 70 bps of H1 margin per that log. One-off or recurring is the question. 1 quarter of silence. |
| A3-F17-11 | F17 | R032, R035, M01 | L219-L220, L230-L233 | "we have closed Q2 with a net order book of 251 billion" / "they contribute almost two thirds of our total revenue" | CONFIRMATORY-NEGATIVE | Order-book consumption and the gross-to-net bridge not addressed, 2 consecutive calls, while the filed deck bridge shows consumption up to about 1.6x revenue from about 1.15x (Notion memory). India-specific revenue % also not given (eastern markets only). Sustained silence on a worsening book-quality ratio. |

Classification counts (28 findings): FORWARD-SIGNAL 9; AMBIGUOUS 13; CONFIRMATORY-NEGATIVE 4; NEUTRAL-FACT 2. All 22 FORWARD-SIGNAL and AMBIGUOUS findings are flagged for A4 (YAML lists).

## 2. CHECKLIST SCORECARD

| Check | Status | Basis |
|---|---|---|
| F1 Zero-value standing items | N.A. | Concall; A2 zero_standing = 0; no line-item template in a transcript. |
| F2 Standalone vs consolidated | N.A. | Call speaks consolidated figures only; no standalone numbers spoken. |
| F3 Shell-entity detection | N.A. | No cost-line tables on a call. |
| F4 Unaudited contribution ratio | N.A. | No auditor Other Matters on a call. |
| F5 Going concern / EoM scope | N.A. | No EoM paragraph on a call; no prior-quarter extract to diff. |
| F6 Forward-commitment mining | FINDING | 6 findings; 22-row commitment register below; first dated DENSO close guidance; C1 conceded missed. |
| F7 Hedge mining | FINDING | 5 findings; about 19 hedge instances (inventory below) against about 9 logged for Q1 (Notion memory; counting hands differ, indicative only). |
| F8 Tax forensics | FINDING | ETR not spoken; one forward tax statement: DENSO proceeds taxable (A3-F8-01). |
| F9 OCI forensics | N.A. | No OCI content on the call. |
| F10 Share count and dilution | FINDING | ESOP inflow about 108 Cr spoken (A3-F10-01, NEUTRAL-FACT); EPS spread not on the call. |
| F11 Reserves / net worth tie-out | N.A. | No net worth or reserves spoken; cash 1,966 Cr gross is a treasury figure, not net worth. |
| F12 Segment forensics | N.A. | Product-mix shares spoken (suspension 7%, 2W/3W 14%, 70:30 auto/non-auto, DA+DG +37%); no segment assets or liabilities on a call. |
| F13 Board outcome | N.A. | No board outcome on the call. |
| F14 Drafting / internal inconsistencies | FINDING | Applied to spoken metric bases and call-rule consistency (by analogy; ASR artefacts are not counted as governance points): 4 findings. |
| F15 Entity list diffs | N.A. | No consolidation list on a call; no prior extract. The coming eDrive relationship change (WOS to JV) is carried as a commitment in A3-F6-03. |
| F16 Presentation-specific | N.A. | Doctype is concall; deck not in this document set. Guidance softening (A3-F6-02) and metric-basis drift (A3-F14-02) are carried under F6/F14. |
| F17 Silence audit | FINDING | 11 findings; "What Was NOT Discussed" table below with consecutive-quarter counts. |

## 3. COMMITMENT REGISTER (F6)

Status words: initiated / underway / completed, plus reaffirmed, missed, unscored, withdrawn where the register needs them. Q1 C-codes are from Notion memory (Q1 FY27 baseline register); no prior fulltext was available to verbatim-diff.

| # | Commitment | Implied date | Turn / line ref | Status word |
|---|---|---|---|---|
| K01 | DENSO JV1: carve-out of the business closed | end-Dec 2026; may slip to Jan 2027 (Q3/Q4 FY27) | T10 L439-L440 | underway |
| K02 | DENSO JV2: formed and closed ("not yet formed up") | H1 CY2027 (Q4 FY27-Q1 FY28) | T11 L443-L445 | initiated |
| K03 | Sona to block capital for JV2 capex | FY27-FY28 | T34 L662-L663 | initiated |
| K04 | DENSO proceeds taxable; "substantial cash balance at the end of the year" | FY27 year end | T34 L660-L664 | underway |
| K05 | M&A only on four filters; no rush while cash/EBITDA <= 1.5 | trigger-based | T34 L670-L700 | initiated (policy) |
| K06 | EBITDA margin range 23-25% held; "around 23%" ballpark, 10-20 bps tolerance; holds "unless oil goes to 150" | FY27 / medium term | T29-T30 L610-L611, L618, L624-L638 | reaffirmed |
| K07 | Motor business: launch another product | Q3 FY27 (current quarter) | T22/T24 L555, L561-L562 | underway |
| K08 | 3W traction share to "kick in" as won programs ramp | undated | T24 L565-L566 | initiated |
| K09 | Suspension motors book to span more customers; orders reported when won | undated | T08 L417-L421 | initiated |
| K10 | Robotics: Bharat Expo demonstration | Feb 2027 | T37 L764-L767 | initiated |
| K11 | Robotics capex 62 Cr (declared Q1) covers the area | FY27 | T37 L762-L763 | underway |
| K12 | Robotics R&D spend continues, inside margin range | ongoing | T37 L748-L761 | underway |
| K13 | AMRs deployed on own factory floors for real-world training | now | T39 L792-L797 | underway |
| K14 | Robotics inflection timing | none given ("I don't know") | T39 L772-L781 | withdrawn (vs Q1 C9) |
| K15 | Return ratios to keep improving | undated | T03 L152-L153; T05 L367-L368 | underway |
| K16 | 10x in 10 years; 25% CAGR held in the medium term | about FY36 | T03 L045-L049; T43 L830-L838 | reaffirmed (Q1 C8) |
| K17 | Railway: air springs ramp; HVAC up in coming quarters; electric panels ramp; NPI main driver over 3 years; pipeline for 5 years | 3-5 years | T41 L812-L822 | underway |
| K18 | Europe: more business as OEMs seek a China alternative | undated | T17 L498-L501 | underway (claim) |
| K19 | Humanoid robots on own production lines | evaluating | T50 L886-L898 | initiated (evaluating) |
| K20 | Q1 C1: cost pass-through recovery visible from Q2 | Q2 FY27 | T03 L053-L057 | missed (conceded) |
| K21 | Q1 C2: first robotics SOP this quarter (Q2), next in Q3 | Q2/Q3 FY27 | not addressed | unscored (silent) |
| K22 | Q1 C3: radar commercialisation | due Q1; delivered Q2 | T03 L098-L105, L186-L192; T04 L297-L301 | completed (2W rear radar, one quarter late; whether this is the Q1 "ADAS short-range radar" is not stated) |

## 4. WHAT WAS NOT DISCUSSED (F17 silence audit)

Count = consecutive tracked concalls of silence. Q1 FY27 (23-Jul) was the first tracked call, so the maximum is 2. Notion live items and the Q1 C-register were checked against all 921 lines.

| Checklist item / commitment | Q2 call | Consecutive quarters silent | Note |
|---|---|---|---|
| Op EBITDA margin (bull >=24.5 / bear <23.0) | ADDRESSED (23%, range held, ballpark 23%) | 0 | A3-F17-01, A3-F6-02 |
| Margin basis incl./ex forex; forex gain in revenue | SILENT | 2 | A3-F17-07 |
| CFO/PAT >=1.0x | ADDRESSED (CFO 594 Cr, 90% of EBITDA) | 0 | ratio computable, 1.47x |
| Payables build behind CFO | SILENT (framed as net 44 Cr WC release) | 1 | A3-F17-04 |
| Short-term borrowings | PARTIAL (224 Cr added; reason and tenor silent) | 1 | A3-F17-04 |
| C1 margin recovery from Q2 | ADDRESSED (conceded missed) | 0 | A3-F6-01 |
| C2 first robotics SOP | SILENT on the SOP | 1 | A3-F17-02 |
| C3 ADAS radar | PARTIAL (2W rear radar commercialised) | 0 | K22 |
| DENSO close / eDrive deconsolidation timing | ADDRESSED (JV1 Dec/Jan; JV2 H1 CY27) | 0 | A3-F6-03 |
| DENSO financial terms (EV, 49%, slump-sale, gain line, post-close accounting) | SILENT (tax point only) | 2 | A3-F17-08, A3-F8-01 |
| eDrive named; post-JV1 consolidation vs NCI | SILENT | 1 | A3-F6-03 |
| Auditor signing time before board start | SILENT | 2 | not a usual call topic; carry to AR / A4 |
| EV share of order book (61%, third easing) | SILENT | 1 | A3-F17-03 |
| Order book gross-to-net, consumption bridge | SILENT | 2 | A3-F17-11 |
| Novelic carrying value / impairment (tripwire 3) | SILENT (name only) | 2 | A3-F17-06 |
| ROCE number and path to >18% (tripwire 1) | SILENT on number | 2 | A3-F17-05 |
| Railway revenue / PAT (tripwire 8) | SILENT on quantum (Head of Railway spoke, no numbers) | 2 | A3-F17-09 |
| Customer concentration % | PARTIAL (diversification claim L137-L140; suspension motors one customer L417) | 2 | A3-F7-03 |
| Debtor days / WC days (tripwire 7) | PARTIAL (release claimed, days silent) | 2 | |
| Corporate guarantees (tripwire 5) | SILENT | 2 | |
| India revenue % (tripwire 10) | PARTIAL (eastern markets "almost two thirds", L233) | 2 | A3-F17-11 |
| Warranty and slow-moving inventory provisions | SILENT | 1 | A3-F17-10 |
| Capex envelope FY27-FY28 | PARTIAL (H1 148 Cr; robotics 62 Cr) | 2 | |
| JV2 revenue-recognition quarter (Q1 N2) | SILENT (close date given, revenue date not; not asked directly) | 2 | |
| Q1 C6 JV2 global phase 2 | SILENT | 1 | |
| Q1 C7 2W/3W India traction share 25% to >50% | PARTIAL (wallet share up, L549; no %) | 1 | |
| Q1 C9 robotics ramp faster than EV | SOFTENED ("I don't know") | 0 | A3-F7-04 |

## 5. HEDGE INVENTORY (F7)

About 19 instances: L069 "remains uncertain"; L070-L071 "largely beyond our control ... predictability a little difficult"; L401 "very hard to predict the trajectory"; L427-L430 "can't give you anything definite ... how bright we don't know"; L440 "possibility it may spill over"; L450-L453 advisors' holidays; L561 "may not be the numbers"; L624-L628 "if they are flattish ... The only scenario where it deteriorates"; L632-L634 "probably, around 23% ... I don't hold us to"; L637-L638 "unless oil goes to 150"; L772 "I don't know is the real answer"; L776-L778 "don't want to stick our neck out"; L798 "we don't know is the real short answer"; L809-L810 "We don't share business-wise growth outlook"; L824-L825 "dependent on whether we are successful to launch these products on time"; L846 "fairly hypothetical question"; L854 "we don't see any signs that those restrictions will be eased"; L860 "possible mechanism"; L886-L898 "we are evaluating" (four times). Hedges cluster on margin, robotics timing and the DENSO close.

## 6. Notes for A4 (question seeds, one per FORWARD-SIGNAL / AMBIGUOUS finding)

- A3-F6-02: Is about 23% the FY27 base, and what does the five-year margin exercise show for FY28?
- A3-F6-03 / A3-F17-08: After JV1 closes, is eDrive consolidated at 51% with 49% NCI, or equity-accounted? What share of Q2 traction-motor revenue and order additions sits in eDrive? Gain quantum and P&L line?
- A3-F6-04: Is the 1.5x threshold gross or net cash, trailing or forward EBITDA? At FY27 end, what happens if it is crossed?
- A3-F6-05: Which motor product launches in Q3?
- A3-F6-06 / A3-F7-04 / A3-F17-02: Did any robotics SOP happen in Q2? Status of the Q1 dated SOPs?
- A3-F7-01 / A3-F7-02: With full pass-through, what commodity path returns % margin to 24%+?
- A3-F7-03: Suspension motors: share of Q2 revenue from one customer and one model; timing of a second customer.
- A3-F7-05: Is freight passed through?
- A3-F8-01: Expected tax on DENSO proceeds and net cash received.
- A3-F14-01 / F14-02: H1 BEV revenue in Rs Cr and its share of total revenue.
- A3-F14-03: Robotics order book in Rs Cr and conversion schedule.
- A3-F17-03 to F17-06, F17-09, F17-10: EV share of the book; payables and borrowing reason; un-normalised ROCE; Novelic carrying value; railway revenue and PAT; warranty and inventory provisions, one-off or recurring.

## 7. YAML

```yaml
stage: A3-forensics
company: "SONACOMS"
quarter: "q2fy27"
doctype: "concall"
model: "claude-opus-5-5"
status: complete
forensics_path: "C:/Users/SUMIT SHARMA/repos/inflection-pipeline/.claude/worktrees/qr-sonacoms-q2fy27-c7173c/runs/sonacoms-q2fy27/work/forensics_concall_sonacoms_q2fy27.md"
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
  F10: FINDING
  F11: N.A.
  F12: N.A.
  F13: N.A.
  F14: FINDING
  F15: N.A.
  F16: N.A.
  F17: FINDING
findings:
  - {id: "A3-F6-01", check: "F6", line: "L053-L057", classification: "CONFIRMATORY-NEGATIVE", implication: "Mgmt concedes Q1 promise C1 (margin recovery from Q2) missed; cause moved from input cost to product mix, which pass-through does not fix"}
  - {id: "A3-F6-02", check: "F6", line: "L610-L611, L618, L630-L634", classification: "FORWARD-SIGNAL", implication: "23-25% range kept but CFO ballpark is about 23% with 10-20 bps tolerance, which sits on the <23.0% bear line; five-year margin exercise undisclosed"}
  - {id: "A3-F6-03", check: "F6", line: "L435-L445, L449-L453", classification: "FORWARD-SIGNAL", implication: "DENSO JV1 close end-Dec 2026 (may slip to Jan); JV2 H1 CY27; like-for-like breaks, NCI or equity accounting and a gain arrive at JV1 close"}
  - {id: "A3-F6-04", check: "F6", line: "L660-L664, L697-L700", classification: "FORWARD-SIGNAL", implication: "Own capital-deployment trigger cash/EBITDA 1.5x; gross cash already about 1.49x annualised H1 EBITDA (ASR figures, my arithmetic); DENSO cash pushes it over; M&A or return decision likely within 12 months; JV2 capex to be funded"}
  - {id: "A3-F6-05", check: "F6", line: "L554-L562, L565-L566", classification: "FORWARD-SIGNAL", implication: "Dated new motor-product launch in Q3 FY27; 3W traction pretty small so far, ramp undated"}
  - {id: "A3-F6-06", check: "F6", line: "L748-L754, L761-L767", classification: "FORWARD-SIGNAL", implication: "Robotics R&D continues inside the margin range and is a named margin drag; next milestone is a Feb 2027 expo demo, not an SOP or revenue date"}
  - {id: "A3-F7-01", check: "F7", line: "L069-L072", classification: "FORWARD-SIGNAL", implication: "Pre-emptive cover on near-term % margin and pivot of yardstick to absolute EBITDA"}
  - {id: "A3-F7-02", check: "F7", line: "L858-L868, L875-L878", classification: "FORWARD-SIGNAL", implication: "Full pass-through still dilutes % margin; % recovery now needs falling material prices"}
  - {id: "A3-F7-03", check: "F7", line: "L401, L417-L418, L427-L430", classification: "AMBIGUOUS", implication: "Suspension motors (about 7% of revenue) rest on one customer and one model; trajectory not predictable per mgmt"}
  - {id: "A3-F7-04", check: "F7", line: "L772, L776-L778", classification: "FORWARD-SIGNAL", implication: "Robotics date retreat versus Q1 dated SOPs; five robotics asks, no date given, accountability cited as the reason"}
  - {id: "A3-F7-05", check: "F7", line: "L064-L067", classification: "AMBIGUOUS", implication: "Freight (ASR reading) nearly doubled QoQ; pass-through answer covers material only"}
  - {id: "A3-F8-01", check: "F8", line: "L649, L660-L661", classification: "FORWARD-SIGNAL", implication: "DENSO proceeds taxable; one-off tax and gain in JV1 close quarter; analyst 900 Cr by year end neither confirmed nor contested"}
  - {id: "A3-F10-01", check: "F10", line: "L358", classification: "NEUTRAL-FACT", implication: "ESOP exercise inflow about 108 Cr in H1; A4 cross-checks share base"}
  - {id: "A3-F14-01", check: "F14", line: "L163-L166, L328-L329, L276", classification: "AMBIGUOUS", implication: "Spoken H1 BEV figures irreconcilable (2,042 Cr would be 71% of total revenue vs 48% of auto sales); take BEV rupees from filed deck only"}
  - {id: "A3-F14-02", check: "F14", line: "L131-L132, L311-L312, L775", classification: "AMBIGUOUS", implication: "Same 51% cited as share of auto product sales, auto revenue and total revenue; overstates whole-company EV share (about 36% of total on 70:30)"}
  - {id: "A3-F14-03", check: "F14", line: "L219-L222, L745", classification: "AMBIGUOUS", implication: "Order book stated as 251 billion and $250 billion; robotics 4% (Q1 3%) about Rs 10 bn on rupee basis; conversion schedule absent"}
  - {id: "A3-F14-04", check: "F14", line: "L011-L014, L402-L403", classification: "NEUTRAL-FACT", implication: "CEO names an end customer against the call rule; confirms single-customer China base of suspension motors"}
  - {id: "A3-F17-01", check: "F17", line: "L313-L315, L331-L333", classification: "CONFIRMATORY-NEGATIVE", implication: "YoY margin compression widened to about 2.3 pt in Q2 from about 0.7 pt in Q1; bull gate missed, bear depends on unstated basis"}
  - {id: "A3-F17-02", check: "F17", line: "L098-L105, L744-L747", classification: "AMBIGUOUS", implication: "Promise C2 first robotics SOP never scored despite five robotics asks; lean bear, not delivered until shown"}
  - {id: "A3-F17-03", check: "F17", line: "L219-L220", classification: "AMBIGUOUS", implication: "EV share of order book (third easing) unstated; only positive EV framing; repeat at Q3 makes it confirmatory-negative"}
  - {id: "A3-F17-04", check: "F17", line: "L350-L353, L357, L644", classification: "AMBIGUOUS", implication: "CFO/PAT passes on spoken figures but payables build behind it is unmentioned and 224 Cr new borrowing unexplained; 9M unwind risk"}
  - {id: "A3-F17-05", check: "F17", line: "L152-L153, L367-L368", classification: "AMBIGUOUS", implication: "ROCE number and path to >18% unstated for a second call"}
  - {id: "A3-F17-06", check: "F17", line: "L652-L653, L757", classification: "AMBIGUOUS", implication: "Novelic named, impairment and carrying value unaddressed for a second call (tripwire 3)"}
  - {id: "A3-F17-07", check: "F17", line: "L313-L314", classification: "CONFIRMATORY-NEGATIVE", implication: "Forex gain and margin basis unstated for a second call while the gate outcome turns on it"}
  - {id: "A3-F17-08", check: "F17", line: "L435-L445, L660-L661", classification: "AMBIGUOUS", implication: "DENSO financial terms and post-close accounting unstated for a second call; only close dates and taxability given"}
  - {id: "A3-F17-09", check: "F17", line: "L809-L811, L824-L825", classification: "AMBIGUOUS", implication: "Railway revenue and PAT unstated for a second call; growth conditional on on-time launches"}
  - {id: "A3-F17-10", check: "F17", line: "L113-L118", classification: "AMBIGUOUS", implication: "Deming Prize celebrated; rising warranty and slow-moving inventory provisions (about 70 bps of H1 margin per Notion log) unmentioned"}
  - {id: "A3-F17-11", check: "F17", line: "L219-L220, L230-L233", classification: "CONFIRMATORY-NEGATIVE", implication: "Order-book consumption and gross-to-net bridge unaddressed for a second call while consumption ratio worsened; India revenue % also unstated"}
forward_signals: ["A3-F6-02", "A3-F6-03", "A3-F6-04", "A3-F6-05", "A3-F6-06", "A3-F7-01", "A3-F7-02", "A3-F7-04", "A3-F8-01"]
ambiguous: ["A3-F7-03", "A3-F7-05", "A3-F14-01", "A3-F14-02", "A3-F14-03", "A3-F17-02", "A3-F17-03", "A3-F17-04", "A3-F17-05", "A3-F17-06", "A3-F17-08", "A3-F17-09", "A3-F17-10"]
commitments:
  - {commitment: "DENSO JV1 carve-out close", implied_date: "end-Dec 2026, may slip to Jan 2027", ref: "T10 L439-L440", status_word: "underway"}
  - {commitment: "DENSO JV2 formed and closed", implied_date: "H1 CY2027", ref: "T11 L443-L445", status_word: "initiated"}
  - {commitment: "Sona blocks capital for JV2 capex", implied_date: "FY27-FY28", ref: "T34 L662-L663", status_word: "initiated"}
  - {commitment: "DENSO proceeds taxable; substantial year-end cash", implied_date: "FY27 year end", ref: "T34 L660-L664", status_word: "underway"}
  - {commitment: "M&A on four filters; no rush while cash/EBITDA <= 1.5", implied_date: "trigger-based", ref: "T34 L670-L700", status_word: "initiated"}
  - {commitment: "EBITDA margin range 23-25% held; ballpark about 23%", implied_date: "FY27 / medium term", ref: "T29-T30 L610-L638", status_word: "reaffirmed"}
  - {commitment: "Launch another motor product", implied_date: "Q3 FY27", ref: "T22-T24 L555, L561-L562", status_word: "underway"}
  - {commitment: "3W traction share kicks in as programs ramp", implied_date: "undated", ref: "T24 L565-L566", status_word: "initiated"}
  - {commitment: "Suspension motor book spans more customers", implied_date: "undated", ref: "T08 L417-L421", status_word: "initiated"}
  - {commitment: "Robotics demo at Bharat Expo", implied_date: "Feb 2027", ref: "T37 L764-L767", status_word: "initiated"}
  - {commitment: "Robotics capex 62 Cr covers the area", implied_date: "FY27", ref: "T37 L762-L763", status_word: "underway"}
  - {commitment: "Robotics R&D continues inside margin range", implied_date: "ongoing", ref: "T37 L748-L761", status_word: "underway"}
  - {commitment: "AMRs deployed on own factory floors", implied_date: "now", ref: "T39 L792-L797", status_word: "underway"}
  - {commitment: "Robotics inflection timing", implied_date: "none given", ref: "T39 L772-L781", status_word: "withdrawn"}
  - {commitment: "Return ratios keep improving", implied_date: "undated", ref: "T03 L152-L153; T05 L367-L368", status_word: "underway"}
  - {commitment: "10x in 10 years; 25% CAGR medium term", implied_date: "about FY36", ref: "T03 L045-L049; T43 L830-L838", status_word: "reaffirmed"}
  - {commitment: "Railway NPI ramp (air springs, HVAC, electric panels); 5-year pipeline", implied_date: "3-5 years", ref: "T41 L812-L822", status_word: "underway"}
  - {commitment: "Europe: more business as OEMs seek China alternative", implied_date: "undated", ref: "T17 L498-L501", status_word: "underway"}
  - {commitment: "Humanoids on own production lines", implied_date: "evaluating", ref: "T50 L886-L898", status_word: "initiated"}
  - {commitment: "Q1 C1 margin recovery from Q2", implied_date: "Q2 FY27", ref: "T03 L053-L057", status_word: "missed"}
  - {commitment: "Q1 C2 first robotics SOP", implied_date: "Q2 FY27", ref: "not addressed", status_word: "unscored"}
  - {commitment: "Q1 C3 radar commercialisation", implied_date: "Q1 FY27, delivered Q2", ref: "T03 L098-L105, L186-L192; T04 L297-L301", status_word: "completed"}
gate_a3: pass
blank_checks: []
analyst_note: "ASR transcript: every number is management-tier and may be misheard. The spoken set ties internally except R054 (PAT 23 Cr, a dropped digit; about 223 Cr by the 14.4% margin) and R060 (2,042 Cr BEV H1 cannot be 48% of auto sales); neither is resolved here, filed documents govern. The call's centre of gravity: management conceded C1 and moved the margin cause to mix, the CFO anchored the working margin at the 23% floor with a 10-20 bps tolerance that sits on the bear line, and pass-through was redefined as rupee-restoring, not percent-restoring. So the bull gate cannot fire on pass-through alone. DENSO now has dates (JV1 Dec/Jan, JV2 H1 CY27); terms, gain line and post-close accounting are still withheld, so expect a non-comparable Q3 or Q4. Management's own cash/EBITDA 1.5x trigger is about to be crossed once DENSO cash lands, which makes a capital deployment decision a 12-month item. Robotics: five asks, no SOP status, explicit date retreat. Silence counts reach 2 on forex basis, ROCE number, Novelic, railway quantum, DENSO terms and order-book bridge. Prior-quarter comparisons rely on Notion memory, not a prior extract."
```
