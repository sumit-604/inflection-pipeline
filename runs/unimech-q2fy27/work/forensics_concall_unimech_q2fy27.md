# A3 FORENSIC NOTES: UNIMECH q2fy27 (doctype: concall, ASR machine transcript of the 28-Oct-2026 call)

Agent: A3 forensic notes | model: claude-opus-5-5 | run date: 2026-10-28
Evidence tier: management tier, UNVERIFIED (ASR). Every call number is ASR-UNVERIFIED. Where a filed figure exists, the filed figure wins.
Inputs read:
- A1 structured: runs/unimech-q2fy27/extracted/unimech-concall-q2fy27-structured.md (R001-R257)
- A1 fulltext: runs/unimech-q2fy27/extracted/unimech-concall-q2fy27-fulltext.md (lines 1-847, all read)
- A2 ledger: runs/unimech-q2fy27/work/ledger_concall_unimech_q2fy27.md
- Filed cross-checks (structured only): unimech-presentation-q2fy27-structured.md ("deck Rnnn"), unimech-results-q2fy27-structured.md ("results Rnnn"). Results values are in Rs lakhs; deck financial values in Rs Mn.
- Prior baseline: work/monitoring_checklist_unimech.md (Notion snapshot, memory to weigh, not a verbatim prior transcript). No prior-quarter fulltext exists.
- Source PDF and inputs/: NOT opened.

Speaker attribution: Q&A answers T08-T62 are UNIDENTIFIED management. Prepared remarks: T03 CMD, T04 WTD (Rajni), T05 WTD and CFO (Ram).

## 0. LEDGER RECONCILIATION

Rows in ledger: 257 (R001-R257). Rows read at cited fulltext line: 257. ledger_reconciled_pct = 100.
Turns T01-T65 all read. Questions Q01-Q24 all read.

Anchor drifts found (quote sits one line from the cited line; content matches, not material):
- R007 cited 62, text at 61 ("rests on three core pillars").
- R008 cited 82, text at 81 ("our two-year development efforts").
- R017 cited 166, text at 165 ("extendable by an additional two years").
- R031 cited 275, text at 274 ("250-plus qualified base").
- R071 cited 450, text at 451 ("This is a five-year contract").
- R085 / R184 cited 574, number at 575 ("roughly a 200 to 250 crore of outlay").

Paraphrase discrepancy (A1 wording vs verbatim; verbatim governs):
- R204 A1 reads "Next year is a qualification year". Line 800 verbatim: "The other thing would happen next year, this is a qualification year." The verbatim reading puts FY27 as the qualification year and FY28 as the scale year (consistent with R203, line 799). A4 should use the verbatim.

### 0A. MISHEARING_CANDIDATE resolution (19 A2 rows plus 1 unflagged)

| Row | Line | ASR text | Filed check | Resolution |
|---|---|---|---|---|
| R006 | 58-59 | "an increase of over seven at first" | deck R048-R050: confirmed PO book Rs 105 Cr (Sep-25) to Rs 266 Cr (Sep-26), +153%; deck R041 total ~Rs 855 Cr | 855/105 = +714% (my arithmetic). The ASR "seven" and "715%" are probably accurate. A2's "likely 71%" is contradicted. See C-A3-01. |
| R035 | 282 | "715% by over" | same as R006 | Same. |
| R008 | 81 | "two-year" | deck R006 "20-month" | Filed: 20 months. |
| R019 | 177 | "20-month" | deck R006 | Confirmed 20 months. |
| R010 | 88 | "300 40-year plus part" | deck R068 FAI pipeline 346 | 340-plus; filed 346. |
| R011 | 97 | "USD $4 billion" | deck R012 "~USD 4mn"; results R346/R348 ODI 01-Oct-2026, 51% | USD 4 million. |
| R012 | 155 | "USP 7.5 million" | deck R045 "USD 7.5 million" | USD 7.5 million. |
| R018 | 169 | "over 320 parts" | deck R062 aerospace FAI pipeline 322 | Consistent. |
| R041 | 310 | "96%" | deck R074 H1 Rs 2,306.2 Mn; deck R268 FY26 Rs 2,404.9 Mn | 95.9%. Confirmed. |
| R044 | 315 | "COBEL contributed 30%" | Results are single segment (results note line 9); no filed Hobel revenue | Entity = Hobel. The 30% is NOT FILED and stays unverified. See C-A3-04. |
| R049 | 325 | "10% to 2%" | deck R184 materials 32.8% H1 | Unresolvable. Line is garbled. |
| R051 | 326 | "H1 margin at 8%" | deck R030 H1 EBITDA margin 38% | 38%. |
| R052 | 329 | "15% working percent" | deck R189 employee 15.4% H1 | 15% employee cost confirmed; the "operational expenses" figure is lost. |
| R065 | 353 | "50% to 20%" | none | Unresolvable. |
| R067 | 412 | "primarily 3%" | none filed | Consistent with 33% PCA less 30% Hobel = 3% non-Hobel PCA. See C-A3-04. |
| R068 | 441 | "589 corrode" | deck R043 "~Rs. 589 Cr" | Rs 589 Cr. |
| R084 | 565 | "2.5 times of the available hospitals" | none | Unresolvable. |
| R088 | 605 | "2x add a term" | none (analyst) | Consistent with the Q1 call's "gross block ~2x by FY27-end" (Notion baseline). |
| R096 | 818 | "2000 CR" | management answer line 824 "1000 CR" | Rs 1,000 Cr. |
| R061 (not flagged by A2) | 340 | "ROC ... approximately 20%" | deck R349 ROCE H1 FY27 14.9%; deck R353 ROE 14.9% | Filed ROCE 14.9% wins. ROE 15% matches. See C-A3-05. |

Other call numbers checked against filed and found consistent: R036 Rs 123 Cr (deck R069 Rs 1,230.0 Mn); R037 14% QoQ (deck R073); R038 98% (deck R071); R039 Rs 231 Cr (deck R074); R047 67% / R048 69% gross margin (1 minus deck R184 32.8% = 67.2%; 1 minus deck R181 30.6% = 69.4%); R050 40% (deck R028); R053 1,332 employees (deck R241); R054 Rs 32 Cr (deck R032 Rs 317.7 Mn); R055 24% (deck R038); R057 103% (deck R033); R058 Rs 60 Cr (deck R035 Rs 596.4 Mn); R059 71% (deck R036); R045 Rs 7 Cr / R046 Rs 14 Cr other income (deck R117 Rs 69.8 Mn; R122 Rs 143.1 Mn); R064 65% utilisation (deck R253); R022 USD 4 million (deck R012); R023 27% (results R345 27.24%).

## 1. FINDINGS TABLE

Arithmetic marked "(my arithmetic)" is A3's, not filed. Notion figures are memory to weigh.

| id | check | ledger row ref | line / turn | short verbatim quote | classification | forward implication |
|---|---|---|---|---|---|---|
| C-A3-01 | F16 | R005, R006, R034, R035, R237, R240 | l.57-59, l.281-282 (T03, T04) | "855 Crores representing an increase of over seven" / "715% by over" | AMBIGUOUS | The YoY claim compares the total book incl. LTA/award letters (Rs 855 Cr, deck R041) with last year's confirmed-PO book (Rs 105 Cr, deck R048). 855/105 = +714% (my arithmetic). Like-for-like firm growth is +153% (deck R050). The headline growth rate mixes two definitions. A4: ask management to state the like-for-like basis. |
| C-A3-02 | F7 | R068, R069, R075, R077, R078, R240, R247 | l.283-287 (T04); l.468-475 (T13) | "completely addresses historical concerns regarding short cycle order dependency" vs "this customer has provided the indication of 43 million" | FORWARD-SIGNAL | Rs 589 Cr of Rs 855 Cr (68.9%, my arithmetic) is LTA/award/forecast schedules spanning "5 to 10 years" (l.475), not firm POs (deck R042 firm Rs 266 Cr). The French award is an "indication" (l.468). Honeywell is a framework under which Honeywell "may issue" POs (Notion 26-Oct filing note). The "completely addresses" claim overstates firm visibility. Score revenue visibility on Rs 266 Cr firm. |
| C-A3-03 | F16 | R005, R034, R100, R237 | l.57-58 (T03); l.839 (T64) | "our consolidated order book stands at 855 Crores" | FORWARD-SIGNAL | The firm book fell for a second quarter. Rs 314 Cr at Q4 FY26 (Notion 29-May) to Rs 280.3 Cr at 30-Jun-26 (Notion Q1; CARE cites Rs 280 Cr) to Rs 266 Cr at 30-Sep-26 (deck R042). QoQ -5.1% (my arithmetic) while Q2 revenue rose 14%. The call never states the firm figure and leads with Rs 855 Cr. Caveat: Jun-26 basis included Hobel Rs 100.1 Cr; deck R056 now shows Industrials (Hobel) at 7% of the PCA mix. Comparability NOT confirmed. A4: ask for firm book QoQ on one definition and the Hobel book. |
| C-A3-04 | F12 | R042, R043, R044, R066, R067, R241 | l.312-318 (T05); l.411-412 (T08) | "COBEL contributed 30% of total H1 consulate revenue" / "of which primarily 3% has been coming from PCA" | FORWARD-SIGNAL | If Hobel = 30% of H1 (Rs ~69 Cr) and Q1 Hobel was ~Rs 22 Cr (Notion), Q2 Hobel ~Rs 47 Cr. Then Q2 organic ex-Hobel ~Rs 76 Cr vs Q1 ~Rs 86 Cr, about -11% QoQ (my arithmetic, ASR-unverified 30%). Non-Hobel PCA is ~3% of H1 (~Rs 7 Cr) while PCA is 91% of the order book (deck R051). This tests Notion prove-it condition (1), organic core still growing. A4: ask Hobel Q2 revenue and organic QoQ growth. |
| C-A3-05 | F14 | R061, R062, R243 | l.339-340 (T05) | "both our ROC and ROE for H-1s today are approximately 20% and 15% each" | AMBIGUOUS | Filed deck R349 shows H1 FY27 ROCE 14.9%, not 20%. The filed figure wins. The Q1 call promised ROCE ~14.3% to 20-21% "as utilisation lifts" (Notion baseline). On the filed basis, ROCE moved +0.6 pp, not to 20%. Lean bear: the promise is not yet delivered. A4: ask which ROCE basis gives 20% (ex-goodwill? pre-tax?). |
| C-A3-06 | F6 | R172, R191, R192, R205, R206, R207, R208, R251, R254, R257 | l.330 (T05); l.689-697 (T43); l.532 (T24); l.825-829 (T62) | "we are confident that the margins will sustain what we have delivered in the first half" / "one percentage or two percentage of margin compression" | FORWARD-SIGNAL | The FY27 guide moves up from 34-35% (floor 30-32%, Q1 call) to "H2 same as H1", about 38% (deck R030). No number is stated. Beyond FY27, management signals a step down: PCA margins "equal to the tooling business or less" (l.532), mix to "around 50 50" (l.825), plus 1-2% for R&D (l.828-829). Gross margin is already 67.2% H1 vs 75.5% FY26 and 79.0% FY24 (deck R322-R325, my arithmetic). FY27 reads as a margin peak. Trigger (b) is far away. |
| C-A3-07 | F16 | R086, R188, R192, R252, R254, R096, R097 | l.599-601 (T33); l.697 (T43); l.824 (T62) | "While we are not giving any forward-looking guidances over the next two years" | AMBIGUOUS | New guidance stance: two-year no-guidance plus "one year at a time" on margins, while a Rs 1,000 Cr "aspiration" is given with no year ("over a couple of years", l.824). That is ~2.2x H1 annualised revenue (my arithmetic). No numeric FY27 revenue guide for a second call. A4: ask the target year for Rs 1,000 Cr and the organic share (Hobel ~20%, l.765). |
| C-A3-08 | F17 | none (absence); nearest R245, R123 | absent l.22-847 (T01-T65); nearest hook l.360-371 (T05) | (no mention of CRISIL or any rating; nearest: "while maintaining a disciplined balance sheet", l.364) | CONFIRMATORY-NEGATIVE | CRISIL "Issuer Not Cooperating" unaddressed on a 6th consecutive call (Notion: 5th at Q1). The deck carries "CARE A; Stable" (deck R013). Neither management nor 7 analysts raised CRISIL. The persistence leg of trigger (d) stays CONFIRMED. |
| C-A3-09 | F7 | R249, R250, R251 | l.527-533 (T24) | "as an internal policy, what we'll do is we'll strictly report on a consolidated basis, not on a vertical or a customer basis" | FORWARD-SIGNAL | The segment-margin refusal is now a standing "internal policy". The Q1 refusals were case by case. Trigger (c), Hobel EBITDA below 40%, is untestable for a 3rd consecutive call and will stay untestable on calls. A4: route trigger (c) to another source (Hobel statutory accounts, AR subsidiary note). |
| C-A3-10 | F17 | none (absence); nearest R105-R109 | absent l.22-847; Preetam (WTD) on panel l.36 (T02) | "Mr. Preetam Esri, Old-Time Director" (panel intro only) | AMBIGUOUS | The 29-Sep pledge by WTD Preetham S V (1,87,500 sh, 0.37%, to 360 One "for loans"; revised Reg 31(1) on 17-Oct) is not addressed. He was on the panel. First call since the pledge. A4: ask purpose, loan size, and whether more pledges will follow. |
| C-A3-11 | F17 | R063, R173, R245 | l.341-344, l.360-364 (T05) | "working capital for the quarter today approximately haven't been this, remaining well within our historical operating range" / "maintaining a disciplined balance sheet" | AMBIGUOUS | The call gives no CFO, debt or net-cash figure, and the WC-days number is lost to ASR. Filed: consolidated H1 CFO Rs 53.46 Cr (results R693) vs PAT Rs 59.64 Cr (deck R178) = 0.896x (my arithmetic). That is just below the 0.90x Pillar 2 upgrade line (Notion). Consolidated borrowings went from Rs 112.09 Cr to Rs 160.98 Cr (+43.6%; results R415+R423 vs R416+R424, my arithmetic), incl. Rs 38.85 Cr net WC borrowings (results R721). Standalone CFO is negative, Rs -22.99 Cr (results R285). |
| C-A3-12 | F6 | R011, R022, R085, R143, R160, R161, R184, R221 | l.97-98 (T03); l.227-229 (T04); l.574-575 (T31) | "initial equity investment of approximately USD $4 billion deployed at least this month fully capitalizes this space" / "roughly a 200 to 250 crore of outlay" | FORWARD-SIGNAL | Promise vs delivery: Q1 promised "USD 10M infusion in Aug-2026". Delivered USD 4M (Unimech's 51% of SAR 30M, deck R012) on 01-Oct (results R346). That is late and smaller. "Fully capitalizes" conflicts with the pending second SAR 30M tranche (Notion 01-Oct). The Rs 200-250 Cr outlay is above the total planned equity of SAR 60M (~Rs 154 Cr at the filed SAR rate, my arithmetic). The Rs 46-96 Cr gap has no stated funding source. A4: ask the second-tranche date, JV debt, and Unimech's share. |
| C-A3-13 | F6 | R023, R024, R120, R121, R222 | l.235 (T04); l.238-241 (T04) | "UNMEC holds an approximate 27% equity stake" / "validated in 26 September when Avana Capital invested in DHEA at an approximate 200 crore valuation" | AMBIGUOUS | Filed: stake fell from 35.07% (Notion 08-Sep, after a Rs 2.998 Cr secondary, results R344) to 27.24% after the external raise (results R345, R907). That is -7.8 pp. The only H1 associate outflow is that secondary (results R301), so no participation in the primary round shows. The Q1 promise was "UNIMECH participation, modest dilution". The secondary implies ~Rs 59 Cr for 100% vs Avana's ~Rs 200 Cr weeks later (my arithmetic). Associate loss rose to Rs 75.35 lakh in Q2 from Rs 13.80 lakh in Q1 (results R547, R548). The call presents the dilution as validation and is silent on the loss. Dheya is a related party (Notion). |
| C-A3-14 | F6 | R025, R163, R193, R231, R233 | l.243-246 (T04) vs l.721-723 (T47-T48) | "serial production and manufacturing initiated" vs "it's mostly you know testing out of the engine in the platform" | AMBIGUOUS | Prepared remarks say Dheya serial production has started. Q&A says revenue is "at least F28 or maybe F29" and the engine is still in platform testing. A4: ask which applies, and what Unimech earns as "exclusive manufacturing partner" (l.266) before FY28. |
| C-A3-15 | F6 | R158, R219, R220 | l.222-223 (T04) | "AS9100 quality certification for the WYZAC facilities underway with completion targeted by Ceph27" | AMBIGUOUS | The Q1 baseline said Hobel AS9100 "by Q4 FY27" (Mar-2027). "Ceph27" most likely reads as Sep-2027, a ~6-month slip. ASR garble, unverified. A4: confirm the target date. |
| C-A3-16 | F6 | R045, R046, R242 | l.319-321 (T05) | "stood at approximately seven crores and 14 crores respectively, maintaining a steady run rate" | AMBIGUOUS | The Q1 promise was other income "to ~half again" (~Rs 3.7 Cr). Q2 was Rs 6.98 Cr vs Q1 Rs 7.33 Cr (deck R117, R120). Not delivered, and reframed as "steady". Other income is ~21% of Q2 pre-associate PBT (Rs 32.53 Cr, results R541; my arithmetic). The group holds treasury income while adding Rs 48.9 Cr of borrowings (C-A3-11). A4: ask why the group borrows while it holds treasury assets. |
| C-A3-17 | F7 | R154, R159, R174, R175, R176, R185, R186, R187, R197, R198, R199, R200, R201, R245 | l.358-359, l.365-371 (T05); l.580-592 (T31); l.769-790 (T56) | "expect to consider an equity fund raise in early calendar year to be consistent subject to final requirement and market conditions" / "we don't need random money or internal accrual support enough" | FORWARD-SIGNAL | An equity raise is guided for early CY2027 for capacity beyond Rs 1,000 Cr "and potentially inorganic expansion" (l.790) and MPS (l.371). The Rs 1,000 Cr plan is said to need no outside money. The call does not state the size; the Rs 750 Cr QIP enabling and the Rs 2,000 Cr Sec 186 envelope stand (Notion). Capacity messages conflict: "initiating capacity expansion ... if needed" (l.358), "next two years ... sufficient capacity" (l.580), "might have to do early investment" (l.592). Dilution comes before the earnings it funds. Use of funds includes unnamed M&A. |
| C-A3-18 | F7 | R009, R031, R095, R202, R203, R204, R238, R256 | l.792-800 (T57-T58) | "not the entire 250 ... everything will not get into serial production" | FORWARD-SIGNAL | The analyst asked how many of the 250 parts are in serial production and their quarterly run rate. No count and no run rate were given. Only "60-70% would be moving". The deck calls them "250 FAIs completed" (deck R010), not qualified-in-production. "This is a qualification year" (l.800) places revenue scale in FY28. The Rs 590 parts metric is a pipeline count, not a revenue count. |
| C-A3-19 | F17 | R089, R090, R142, R194, R195 | l.726-733 (T49-T50) | "any more clarity on when the nuclear orders may flow in?" / "we'll wait for the time session to complete" | AMBIGUOUS | No update on the existing ~Rs 87 Cr nuclear order. The Q1 baseline was "~50% executed H2". Only new reactor bids via VGS are discussed, with no date. History: FY26 nuclear was Rs 400 Cr guided vs Rs 68 Cr delivered (Notion). Nuclear is 11% of the PCA order mix (deck R054). A4: ask H1 nuclear execution in Rs Cr. |
| C-A3-20 | F17 | R125 (T10); none for board items | l.430-433 (T09-T10); absent elsewhere | "we've been doing a great job hiring senior leadership" | AMBIGUOUS | Three items were not addressed on the call. (1) The 27-Oct board approved Unimech buying 60,80,000 Hobel shares from Innomech, "pursuant to an internal group restructuring" (results R002, R883). (2) Senior manager Prathap B. Naidu moves to Innomech's Toolings Division (results R769, R827). (3) The 07-Sep SMP exits (5, disclosed late) got only a generic hiring answer, and a 23-s ASR gap sits inside it (l.430-431). Innomech carries the group debt (Notion), so the restructuring moves Hobel's cash flows relative to that debt. |
| C-A3-21 | F17 | R080, R081, R082 | l.116 (T03); l.510-511 (T21) | "illuminate customer concentration risks" / "Semiconductor we have one established customer two in the pipeline aerospace we have three" | AMBIGUOUS | Concentration is claimed as reduced, with no number (FY26 top-1 44.5%, Notion). Semiconductor revenue depends on one customer. The order book is 90% export (deck R058). US tariffs are not mentioned. Honeywell is a US counterparty booked in Innomech, the subsidiary the tariff hit in FY26 (Notion). The only duty answer covers UK/EU (l.806-809). |
| C-A3-22 | F7 | R016, R017, R073, R074, R117, R246, R249 | l.462-465 (T13); l.521-522 (T24) | "this is what's been summed up under the 589 code also" / "From my NDA perspective, we are not allowed to specifically talk" | AMBIGUOUS | The Honeywell value now sits inside Rs 589 Cr but is not disclosed on its own. FACC (USD 7.5M) and French (USD 43M) are sized. The Honeywell residual cannot be computed: FX is not stated, and it is unclear whether FACC's "can double" is included. Notion's separating observation (a number by the Q3 FY27 call) is partly met. |
| C-A3-23 | F14 | R052 (T05); T09-T10, T11-T12 turn table | l.373-374 (ts 00:23:39 to 00:23:54); l.430-431 (00:26:37 to 00:27:00); l.440-441 (00:27:32 to 00:27:49) | "Now I would like to talk about / EFI" | AMBIGUOUS | ASR lost about 15 s where the CFO opens what reads as an outlook passage, 23 s inside the organisation answer, and 17 s at the 589 question. Silence scored on outlook and organisation may be a transcription loss. A4: get the official transcript before scoring those two topics as silent. |
| C-A3-24 | F6 | R063, R173, R228 | l.348-350 (T05) | "gradually move towards the 150 to 160 days range by end of 5-27" | NEUTRAL-FACT | The WC target moves from "160+ days" (Q1 baseline) to 150-160 days by Mar-2027, a slight improvement. The current-quarter WC days are not audible (l.343). Filed: receivables Rs 122.6 Cr H1 vs Rs 64.8 Cr FY26 (deck R481, R480); inventory Rs 38.2 Cr vs Rs 25.1 Cr (deck R473, R472). Both include Hobel. |
| C-A3-25 | F6 | R037, R064, R087, R189, R013, R016, R071 | l.43, l.301 (T03, T05); l.352; l.602-606; l.155-157; l.164-166 | "As indicated during our previous call, Q2 has turned out to be a very strong quarter" | NEUTRAL-FACT | Q1 promises shown delivered: Q2 stronger (Rs 123 Cr, +14% QoQ, deck R073); utilisation 58% to 65% (deck R253); gross block ~2x to ~Rs 500 Cr by FY27-end reaffirmed; FACC "moving into initial execution" (l.157); engine Tier-1 LTA signed (Honeywell). |

## 2. CHECKLIST SCORECARD

| Check | Status | Basis |
|---|---|---|
| F1 Zero-value standing items | N.A. | A transcript has no line items. A2 found ZERO_STANDING none. |
| F2 Standalone vs consolidated | N.A. | The call gives consolidated figures only. The S-vs-C check belongs to the results A3. |
| F3 Shell-entity detection | N.A. | No cost lines on the call. |
| F4 Unaudited contribution | N.A. | No auditor matter on a call. |
| F5 Going concern / EoM | N.A. | No EoM paragraph on a call. |
| F6 Forward-commitment mining | FINDING | 27 dated or dateable commitments (register below). Q1 promises are slipped or reframed: Saudi size and timing, Dheya participation, other income, ROCE, AS9100 date. C-A3-06, 12-16, 24, 25. |
| F7 Hedge mining | FINDING | 21 hedge hits: "subject to final requirement and market conditions", "evaluating", "in initial discussions", "contemplating", "indication", NDA, "internal policy". The consolidated-only margin policy is new. C-A3-02, 09, 17, 18, 22. |
| F8 Tax forensics | N.A. | The call states no tax figures. |
| F9 OCI forensics | N.A. | No OCI on the call. |
| F10 Share count / dilution | N.A. | No share count or EPS on the call. The fund-raise dilution sits in F6/F7 (C-A3-17). |
| F11 Net worth tie-out | N.A. | No net worth figure on the call. The ROCE conflict with the deck is under F14. |
| F12 Segment forensics | FINDING | The call is the only source of the vertical split (the filing has one segment). Hobel 30% plus non-Hobel PCA 3% implies an organic QoQ decline. C-A3-04. |
| F13 Board outcome | N.A. | A call is not a board outcome. The call's silence on the 27-Oct board items is under F17 (C-A3-20). |
| F14 Drafting inconsistencies | FINDING | Call vs filed: ROCE 20% vs 14.9% (C-A3-05). ASR coverage gaps sit at the outlook and organisation passages (C-A3-23). |
| F15 Entity list diffs | N.A. | The consolidation-list diff is a results-filing check. The call's entity references (Dheya 27%, Saudi JV, Hobel) are covered in F6/F17. |
| F16 Dropped / reframed disclosures | FINDING | Applied call vs Q1 call baseline. The order-book definition widened from firm Rs 280.3 Cr to a Rs 855 Cr total with +715% on mixed bases. The firm book is not stated. The numeric FY27 margin guide was replaced. A two-year no-guidance stance is new. C-A3-01, 03, 07. |
| F17 Silence audit | FINDING | 16 checklist and commitment items unaddressed or only partly addressed (table below). CRISIL is silent for a 6th consecutive call. C-A3-08, 10, 11, 19, 20, 21. |

Counts: PASS 0 | FINDING 7 | N.A. 10 | blank 0.

## 3. COMMITMENT REGISTER (F6)

| # | commitment | implied date | turn / line | status word |
|---|---|---|---|---|
| 1 | Special process cells: trials this month; submission completed by December | Oct-2026 trials; Dec-2026 | T03 l.105-107; T31 l.573 | underway |
| 2 | NADCAP ("NACAF") certification | Mar-2027 (deck R591: FY27-end) | T03 l.107 | initiated |
| 3 | Semiconductor revenue step-up | H2 FY27 | T03 l.81-83; T08 l.413-415 | expected |
| 4 | Qualify over 320 aerospace parts | FY27 | T04 l.168-169 | underway |
| 5 | Another 20 semiconductor parts / assemblies | Dec-2026 (calendar year end) | T04 l.186-187 | targeted |
| 6 | More than 590 qualified parts (deck R044: 596) | Mar-2027 | T04 l.273-277; T64 l.840 | targeted |
| 7 | Second global semiconductor OEM: discussions | undated | T04 l.188-189 | underway |
| 8 | Dutch semiconductor OEM tooling account | undated | T04 l.140-147 | initiated ("initial discussions") |
| 9 | FACC USD 7.5M / 5-yr LTA into execution; tenure "can potentially double" | live; doubling undated | T04 l.155-160; T13 l.451-455 | underway |
| 10 | French Tier-1 USD 43M / 10-yr award: qualification | undated | T04 l.162-164; T13 l.466-475 | underway |
| 11 | Honeywell 10-yr LTA (+2 yr extendable) | effective 1-Apr-2026 (filed) | T04 l.164-166; T13 l.457-461 | completed (signed) |
| 12 | Hobel: absorb extra capacity requests with existing infrastructure | FY27 | T04 l.213-214 | underway |
| 13 | Hobel new clients (turbine switchgear, locomotive exhaust, engine bellows) | undated (Q1 baseline: two by FY27-end) | T04 l.216-217 | underway |
| 14 | Hobel Vizag AS9100 | "Ceph27" (likely Sep-2027; Q1 baseline Q4 FY27) | T04 l.222-223 | underway |
| 15 | Saudi JV commercial manufacturing readiness | Mar/Apr-2027 | T04 l.227-229 | underway ("progressing on schedule") |
| 16 | Saudi JV capex outlay Rs 200-250 Cr | undated | T31 l.574-575 | initiated |
| 17 | Dheya: critical design review | before Dec-2026 | T04 l.262-263 | underway |
| 18 | Dheya: final design approval | "FEP-27" (likely Feb-2027) | T04 l.265 | targeted |
| 19 | Dheya: four thrust variants available | Mar-2027 | T04 l.248-250 | underway |
| 20 | Dheya revenue | FY28 or FY29 | T47-T48 l.721-723 | expected |
| 21 | Recurring PCA revenue / compounding | FY28 | T04 l.279-280; T58 l.798-800 | expected |
| 22 | FY27 margins: H2 at H1 level (~38%) | FY27 | T05 l.330; T43 l.689-691; T62 l.821-822 | committed |
| 23 | Working capital days 150-160 | Mar-2027 | T05 l.348-350 | expected |
| 24 | Equity fund raise (incl. MPS) | early CY2027 | T05 l.365-371; T56 l.773-790 | evaluating |
| 25 | Gross block ~Rs 500 Cr incl. JV (~2x) | Mar-2027 | T33 l.602-606 | underway |
| 26 | Capacity for Rs 1,000 Cr "mostly" complete | FY27 | T56 l.769-772 | "already completed" / underway |
| 27 | Rs 1,000 Cr revenue aspiration (Hobel ~20%); mix ~50:50; 1-2% R&D margin drag | undated ("over a couple of years") | T33 l.600-601; T54 l.765; T62 l.824-829 | aspiration |
| 28 | Nuclear: bid 4 new reactors via VGS | undated | T50 l.727-733 | initiated |

Status transitions vs Q1 baseline: FACC moved from signed to "initial execution". The engine Tier-1 LTA moved from "advanced stage" to signed (Honeywell). The Saudi JV moved from "USD 10M in Aug" to USD 4M deployed in Oct, with construction "on schedule". Hobel AS9100 moved from "by Q4 FY27" to "Ceph27" (possible slip).

## 4. WHAT WAS NOT DISCUSSED (F17 silence audit)

| item | source of the ask | addressed on call? | consecutive calls of silence | direction of metric |
|---|---|---|---|---|
| CRISIL "Issuer Not Cooperating" | Notion master variable; 23-Oct save | No (0 hits l.22-847) | 6 | persists (deteriorating governance read) |
| Hobel segment / EBITDA margin (trigger c) | Notion trigger (c); 23-Oct save | Refused as standing policy (l.527-529) | 3 | untestable |
| Promoter pledge (WTD Preetham S V, 0.37%) | 18-Oct and 23-Oct saves | No | 1 | new (first pledge) |
| Honeywell LTA value | 26-Oct save | Partly: inside Rs 589 Cr, no standalone value (l.462-465) | 1 | n/a |
| H1 CFO / CFO-to-PAT (Pillar 2 upgrade test) | AR review; 23-Oct save | No | 1 | filed 0.896x vs 0.957x FY26 (down) |
| Borrowings / net debt (post-Hobel leverage) | Q1 monitorables | No ("disciplined balance sheet" only, l.364) | 1 | filed +43.6% in H1 (up) |
| Firm (confirmed PO) order book | implicit in every prior call | No; only Rs 855 Cr total stated | 1 | filed Rs 280.3 to 266 Cr (down) |
| Organic ex-Hobel growth % | Q1 follow-up | Partly: Hobel 30% of H1 given, no organic % | 2 | implied QoQ decline (C-A3-04) |
| QIP size / structure / dilution % | Q1 follow-up | Partly: "equity fund raise early calendar year" only | 2 (size) | n/a |
| Hobel consideration Rs 450 vs Rs 148 Cr; ICDR cure; commingling controls | Q1 follow-ups | No | 2 | n/a |
| Standalone parent explanation | Q1 follow-up | No | 2 | n/a |
| Numeric FY27 revenue guidance | Q1 follow-up | No (two-year no-guidance stance, l.599) | 2 | n/a |
| Nuclear ~Rs 87 Cr order execution (~50% in H2) | Q1 promise baseline | No; only new bids (l.727-733) | 1 | unknown |
| Saudi JV second tranche date and funding source | 23-Oct save; tracker row | No; "fully capitalizes" (l.98) | 1 | n/a |
| Dheya dilution 35.07% to 27.24%; Unimech participation; associate loss | Q1 promise baseline | No; framed as "validated" (l.239) | 1 | loss up 5.5x QoQ (filed) |
| Top-customer share / concentration % | Notion risk #3 | No number ("illuminate customer concentration risks", l.116) | NOT FOUND (prior count) | n/a |
| Export share / US tariff exposure | Notion risk #6; 26-Oct save | No (UK/EU duty answer only, l.806-809) | NOT FOUND (prior count) | n/a |
| 27-Oct board: Hobel internal restructuring; Naidu transfer | results R002, R883, R769 | No | 1 | n/a |
| 07-Sep late SMP exits | Notion 07-Sep | Partly: generic hiring answer (l.431-433), ASR gap | 1 | n/a |
| Uniflux renewable-energy subsidiary plan | AR review follow-up | No | NOT FOUND (prior count) | n/a |
| CARE vs CRISIL (why a second agency) | 16-Sep save | No | 1 | n/a |
| AMCA / Force MTU / Hobel-MTU watch items | Notion watch list | No | NOT FOUND (prior count) | n/a |

Addressed on the call (removed from silence): Cummins / data-centre pull on Hobel (l.211-212); utilisation (l.352); other income (l.319-321); FACC execution (l.157); gross block (l.602-603); semiconductor customer count (l.510).

Role 5 rule: sustained silence on a deteriorating metric is a confirmatory negative. CRISIL qualifies (6 calls). The firm book, CFO/PAT and borrowings deteriorated but this is the first silent call for each, so they are flagged AMBIGUOUS, not confirmatory.

## 5. FLAGS FOR A4 (management questions)

FORWARD-SIGNAL: C-A3-02, C-A3-03, C-A3-04, C-A3-06, C-A3-09, C-A3-12, C-A3-17, C-A3-18.
AMBIGUOUS: C-A3-01, C-A3-05, C-A3-07, C-A3-10, C-A3-11, C-A3-13, C-A3-14, C-A3-15, C-A3-16, C-A3-19, C-A3-20, C-A3-21, C-A3-22, C-A3-23.
CONFIRMATORY-NEGATIVE: C-A3-08.
NEUTRAL-FACT: C-A3-24, C-A3-25.

Thesis-trigger touchpoints (A4 runs the test; A3 only maps): (a) FY27 revenue < Rs 400 Cr: H1 Rs 230.6 Cr filed, so not near. (b) EBITDA < 22%: H1 38% filed, so not near. (c) Hobel EBITDA < 40%: untestable by policy (C-A3-09). (d) CRISIL persistence plus a new governance event: the persistence leg holds (C-A3-08). The candidate new-event legs are still the pending cumulative-count ruling, the pledge (C-A3-10) and the Dheya related-party dilution (C-A3-13). A3 does not fire triggers.

```yaml
stage: A3-forensics
company: "UNIMECH"
quarter: "q2fy27"
doctype: "concall"
model: "claude-opus-5-5"
status: complete
forensics_path: "runs/unimech-q2fy27/work/forensics_concall_unimech_q2fy27.md"
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
  F12: FINDING
  F13: N.A.
  F14: FINDING
  F15: N.A.
  F16: FINDING
  F17: FINDING
findings:
  - {id: "C-A3-01", check: "F16", line: "57-59; 281-282", classification: "AMBIGUOUS", implication: "+715% YoY compares total book incl LTA (855) with prior-year firm-only book (105, deck R048); like-for-like firm growth +153% (deck R050)"}
  - {id: "C-A3-02", check: "F7", line: "283-287; 468-475", classification: "FORWARD-SIGNAL", implication: "Rs 589 Cr (68.9%) of Rs 855 Cr is LTA/award/indication over 5-10 yrs; firm book Rs 266 Cr; 'completely addresses' short-cycle claim overstated"}
  - {id: "C-A3-03", check: "F16", line: "57-58; 839", classification: "FORWARD-SIGNAL", implication: "firm book down two quarters: 314 -> 280.3 -> 266 Cr (deck R042); call never states it; definition comparability unconfirmed"}
  - {id: "C-A3-04", check: "F12", line: "312-318; 411-412", classification: "FORWARD-SIGNAL", implication: "Hobel 30% of H1, non-Hobel PCA ~3%; implied Q2 organic ex-Hobel ~-11% QoQ (ASR, my arithmetic); tests prove-it condition 1"}
  - {id: "C-A3-05", check: "F14", line: "339-340", classification: "AMBIGUOUS", implication: "call ROCE ~20% vs filed H1 FY27 14.9% (deck R349); Q1 promise of 20-21% not delivered on filed basis"}
  - {id: "C-A3-06", check: "F6", line: "330; 532; 689-697; 825-829", classification: "FORWARD-SIGNAL", implication: "FY27 margin guide implicitly raised to ~38% from 34-35%; FY28+ steps down on PCA mix 50:50 plus 1-2% R&D; gross margin 67.2% vs 75.5% FY26"}
  - {id: "C-A3-07", check: "F16", line: "599-601; 697; 824", classification: "AMBIGUOUS", implication: "new two-year no-guidance stance; undated Rs 1,000 Cr aspiration (~2.2x H1 annualised); no numeric FY27 revenue guide, 2nd call"}
  - {id: "C-A3-08", check: "F17", line: "absent 22-847; hook 360-371", classification: "CONFIRMATORY-NEGATIVE", implication: "CRISIL unaddressed 6th consecutive call; trigger (d) persistence leg stays confirmed"}
  - {id: "C-A3-09", check: "F7", line: "527-533", classification: "FORWARD-SIGNAL", implication: "consolidated-only margin reporting now an 'internal policy'; trigger (c) Hobel EBITDA untestable on calls, 3rd consecutive"}
  - {id: "C-A3-10", check: "F17", line: "absent 22-847; panel 36", classification: "AMBIGUOUS", implication: "WTD Preetham S V 29-Sep pledge (0.37%) not addressed though he was on the panel"}
  - {id: "C-A3-11", check: "F17", line: "341-344; 360-364", classification: "AMBIGUOUS", implication: "no CFO/debt on call; filed H1 CFO/PAT 0.896x (below 0.90x upgrade line); borrowings 112.09 -> 160.98 Cr (+43.6%) vs 'disciplined balance sheet'"}
  - {id: "C-A3-12", check: "F6", line: "97-98; 227-229; 574-575", classification: "FORWARD-SIGNAL", implication: "Saudi USD 10M Aug promise delivered as USD 4M on 01-Oct; 'fully capitalizes' vs pending tranche 2; Rs 200-250 Cr outlay exceeds ~Rs 154 Cr planned equity, funding unstated"}
  - {id: "C-A3-13", check: "F6", line: "235; 238-241", classification: "AMBIGUOUS", implication: "Dheya diluted 35.07% -> 27.24% with no evident participation (promise was participation, modest dilution); loss share 5.5x QoQ; related party; framed as validation"}
  - {id: "C-A3-14", check: "F6", line: "243-246; 721-723", classification: "AMBIGUOUS", implication: "Dheya 'serial production initiated' vs revenue FY28/FY29 and 'mostly testing'"}
  - {id: "C-A3-15", check: "F6", line: "222-223", classification: "AMBIGUOUS", implication: "Hobel AS9100 'Ceph27' likely Sep-2027 vs Q1 baseline Q4 FY27: possible ~6-month slip (ASR garble)"}
  - {id: "C-A3-16", check: "F6", line: "319-321", classification: "AMBIGUOUS", implication: "other income promised to halve; stayed Rs 6.98 Cr (~21% of pre-associate PBT), reframed 'steady'; borrowing while holding treasury"}
  - {id: "C-A3-17", check: "F7", line: "358-371; 580-592; 769-790", classification: "FORWARD-SIGNAL", implication: "equity raise early CY2027 for capacity beyond Rs 1,000 Cr plus unnamed inorganic and MPS; size unstated; capacity messages conflict"}
  - {id: "C-A3-18", check: "F7", line: "792-800", classification: "FORWARD-SIGNAL", implication: "serial-production count and run-rate for the 250 parts not given; deck calls them FAIs; FY27 'qualification year', scale FY28"}
  - {id: "C-A3-19", check: "F17", line: "726-733", classification: "AMBIGUOUS", implication: "no execution update on ~Rs 87 Cr nuclear order (~50% H2 promised); only undated new bids"}
  - {id: "C-A3-20", check: "F17", line: "430-433; absent elsewhere", classification: "AMBIGUOUS", implication: "27-Oct Hobel restructuring (results R002/R883), Naidu transfer (R769), 07-Sep SMP exits not addressed"}
  - {id: "C-A3-21", check: "F17", line: "116; 510-511; 806-809", classification: "AMBIGUOUS", implication: "concentration claimed reduced with no number; one semi customer; 90% export book; US tariff silent with Honeywell US in Innomech"}
  - {id: "C-A3-22", check: "F7", line: "462-465; 521-522", classification: "AMBIGUOUS", implication: "Honeywell value inside Rs 589 Cr but not stated; NDA; residual not computable (FX, FACC doubling basis)"}
  - {id: "C-A3-23", check: "F14", line: "373-374; 430-431; 440-441", classification: "AMBIGUOUS", implication: "ASR gaps (15s, 23s, 17s) at outlook, organisation and 589 passages; get official transcript before scoring those silences"}
  - {id: "C-A3-24", check: "F6", line: "348-350", classification: "NEUTRAL-FACT", implication: "WC target 160+ -> 150-160 days by Mar-2027; current WC days inaudible"}
  - {id: "C-A3-25", check: "F6", line: "43; 155-166; 301; 352; 602-606", classification: "NEUTRAL-FACT", implication: "Q1 promises delivered: Q2 stronger, utilisation 65%, gross block ~2x, FACC in execution, engine LTA signed"}
forward_signals: ["C-A3-02", "C-A3-03", "C-A3-04", "C-A3-06", "C-A3-09", "C-A3-12", "C-A3-17", "C-A3-18"]
ambiguous: ["C-A3-01", "C-A3-05", "C-A3-07", "C-A3-10", "C-A3-11", "C-A3-13", "C-A3-14", "C-A3-15", "C-A3-16", "C-A3-19", "C-A3-20", "C-A3-21", "C-A3-22", "C-A3-23"]
commitments:
  - {commitment: "special process cells submission complete", implied_date: "Dec-2026", ref: "T03 l.105-107", status_word: "underway"}
  - {commitment: "NADCAP certification", implied_date: "Mar-2027", ref: "T03 l.107", status_word: "initiated"}
  - {commitment: "semiconductor revenue step-up", implied_date: "H2 FY27", ref: "T03 l.81-83", status_word: "expected"}
  - {commitment: "qualify 320+ aerospace parts", implied_date: "FY27", ref: "T04 l.168-169", status_word: "underway"}
  - {commitment: "20 more semiconductor parts", implied_date: "Dec-2026", ref: "T04 l.186-187", status_word: "targeted"}
  - {commitment: "590+ qualified parts", implied_date: "Mar-2027", ref: "T04 l.273-277", status_word: "targeted"}
  - {commitment: "FACC LTA execution; tenure may double", implied_date: "live; doubling undated", ref: "T04 l.155-160", status_word: "underway"}
  - {commitment: "French Tier-1 USD 43M award qualification", implied_date: "undated", ref: "T04 l.162-164", status_word: "underway"}
  - {commitment: "Honeywell 10-yr LTA", implied_date: "effective 1-Apr-2026", ref: "T04 l.164-166", status_word: "completed"}
  - {commitment: "Hobel new clients", implied_date: "undated", ref: "T04 l.216-217", status_word: "underway"}
  - {commitment: "Hobel AS9100", implied_date: "Ceph27 (likely Sep-2027)", ref: "T04 l.222-223", status_word: "underway"}
  - {commitment: "Saudi JV manufacturing readiness", implied_date: "Mar/Apr-2027", ref: "T04 l.227-229", status_word: "underway"}
  - {commitment: "Saudi JV capex Rs 200-250 Cr", implied_date: "undated", ref: "T31 l.574-575", status_word: "initiated"}
  - {commitment: "Dheya critical design review", implied_date: "Dec-2026", ref: "T04 l.262-263", status_word: "underway"}
  - {commitment: "Dheya final design approval", implied_date: "FEP-27 (likely Feb-2027)", ref: "T04 l.265", status_word: "targeted"}
  - {commitment: "Dheya four variants available", implied_date: "Mar-2027", ref: "T04 l.248-250", status_word: "underway"}
  - {commitment: "Dheya revenue", implied_date: "FY28 or FY29", ref: "T47-T48 l.721-723", status_word: "expected"}
  - {commitment: "recurring PCA revenue compounding", implied_date: "FY28", ref: "T58 l.798-800", status_word: "expected"}
  - {commitment: "H2 FY27 margins at H1 level (~38%)", implied_date: "FY27", ref: "T43 l.689-691", status_word: "committed"}
  - {commitment: "WC days 150-160", implied_date: "Mar-2027", ref: "T05 l.348-350", status_word: "expected"}
  - {commitment: "equity fund raise incl MPS", implied_date: "early CY2027", ref: "T05 l.365-371", status_word: "evaluating"}
  - {commitment: "gross block ~Rs 500 Cr incl JV", implied_date: "Mar-2027", ref: "T33 l.602-606", status_word: "underway"}
  - {commitment: "capacity for Rs 1,000 Cr mostly complete", implied_date: "FY27", ref: "T56 l.769-772", status_word: "underway"}
  - {commitment: "Rs 1,000 Cr revenue aspiration, Hobel ~20%", implied_date: "undated", ref: "T33 l.600-601; T54 l.765", status_word: "aspiration"}
  - {commitment: "nuclear bids on 4 reactors via VGS", implied_date: "undated", ref: "T50 l.727-733", status_word: "initiated"}
gate_a3: pass
blank_checks: []
analyst_note: "The headline Rs 855 Cr order book is the call's main frame, and it is the weakest number. Firm POs are Rs 266 Cr, down from Rs 280.3 Cr in June and Rs 314 Cr in March. The +715% growth claim compares the total book with last year's firm-only book; A2's 71% mishearing guess is wrong. A second weak point: if Hobel is 30% of H1 (ASR), organic ex-Hobel revenue fell about 11% QoQ. That is the Notion prove-it condition (1). Third: the call's 20% ROCE conflicts with the deck's 14.9%. Filed H1 CFO/PAT is 0.896x, just under the 0.90x upgrade line, and the call says nothing on cash or the 44% rise in borrowings. The margin read is bullish for FY27 (~38%) but signals a FY28+ step down. CRISIL is silent for a 6th call, and segment margins are now refused as policy. Get the official transcript before scoring outlook silence: ASR lost 15 s at the CFO outlook passage."
```
