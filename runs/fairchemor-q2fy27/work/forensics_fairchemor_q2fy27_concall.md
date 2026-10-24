# A3 FORENSIC NOTES: Fairchem Organics (FAIRCHEMOR) Q2 FY27, doctype CONCALL (call 23-Oct-2026, ASR transcript)

Agent: A3 forensic notes | model claude-opus-5-5 | run date 2026-10-23
Inputs read: A1 structured (R001-R182, T001-T101), A1 fulltext (lines 1-356), A2 ledger. Source audio, source text and inputs/ not opened.
Same-quarter cross-reference (read-only): work/forensics_fairchemor_q2fy27_results.md and work/forensics_fairchemor_q2fy27_presentation.md. Filed figures below come from those reports (Rs Lakhs or Rs Mn as printed there, converted to Rs Cr).
Prior-quarter extract: NONE (no prior concall on record). No quarter-on-quarter diff was possible.
Monitoring checklist: NONE. No Notion COMPANIES MASTER page, no companies/FAIRCHEMOR.md, no spear. PRE-THESIS READ. F17 runs against the same-quarter F6 registers instead.
Evidence tier: every spoken number is ASR-tier. Possible mishearings are flagged, not resolved. Derived numbers are marked [DERIVED]; inferences are marked [INFERENCE].

## 0. LEDGER RECONCILIATION

- Structured rows: 182 (45 NUMBER, 48 ENTITY, 30 FORWARD, 18 DATE, 41 QUALIFIER) plus 101 speaker turns. Ledger accounts for 182 of 182 IDs and T001-T101 (orphan_ids empty). A3 read every row at its ID and at its cited fulltext line. Reconciled: 100%.
- ARITH_CHECK R008 and R015: both tie [DERIVED]. Q2 revenue 166.92 Cr / Q2 FY26 111.52 Cr = +49.7%. H1 343.07 Cr / H1 FY26 242.59 Cr = +41.4%.
- Spoken figures that tie to the filing: revenue 167 Cr (L58), net profit 10.2 Cr (L61; filed 10.17 Cr), H1 revenue 343 Cr (L65), H1 EBITDA 35.4 Cr and 10.3% (L67-68), "Abidya margin of 10.5%" (L60; filed Q2 EBITDA 17.54 Cr / 166.92 Cr = 10.51%, so the label is EBITDA margin), receivables "around 100 odd crores" (L211; filed 100.18 Cr), land "12 crore rupees" (L201; filed Rs 12.01 Cr).
- A1 anchor offsets (values correct, pipeline note only): R028 "5%" sits on L163, not L162. R113 "approval cycle is over" sits on L270-271, not L267. R115 "15-18%" sits on L284, not L283. R097 "could help us enhance" sits on L92 (page 2), not L89. R135 "last six months" sits on L124.
- A1 gap threshold note: A1 logs gaps of 20 s or more. A 13 s gap at L266-267 (00:26:19 to 00:26:32) falls below it, but the first item of the H2 priority list is missing there (A3C-18).
- T046 (L191-198) is "mixed with MGMT, unclear". The capacity sentence at L194-196 may be the analyst's restatement. A3 does not treat it as a management statement.

## 1. FINDINGS TABLE

| id | check | ledger row ref | line / turn | short verbatim quote | classification | forward implication |
|---|---|---|---|---|---|---|
| A3C-01 | F6 | R106 R107 R109 R136 R137 (TIMING_CONFLICT) R071 | L166-168 (T032-T033); L170-174 (T035); L186-187 (T043) | L166 "in the second quarter there was some new product that we were planning to launch"; L168 "Sir, only in third quarter."; L173 "plant and everything is done, but based on some R&D suggestion, we are observing and modifying that plant"; L187 "It is going to take its own time." | FORWARD-SIGNAL | Launch slipped one quarter, from Q2 to Q3 FY27. The plant is built but being modified on R&D advice, so the process is not yet proven. The product is unnamed. The answer on its size (L184-185 "how large they can be") falls in a 36 s and a 32 s gap (R169, R170). Q3 is now a dated test. Ask: product name, what is being modified, the new launch date, capacity and revenue potential. |
| A3C-02 | F6 | R028 R141 R105 R013 R020 R012 R019 | L162-164 (T030-T031); L63; L70 | L162-163 "every quarter you are planning to increase the production by 5% and also increasing the exports. So are we online to achieve that?"; L164 "Yes, yes, we are online." | AMBIGUOUS | Management's own volumes contradict the "online" answer. Sold tonnage: H1 25,800 t less Q2 12,300 t = Q1 13,500 t, so Q2 volume fell 8.9% QoQ [DERIVED, ASR-tier inputs]. Filed Q2 revenue fell 5.2% QoQ (176.15 Cr to 166.92 Cr). Q2 processed tonnage is garbled ("1,200 tons", L62). Every reading below 12,300 t also implies lower Q2 processing than Q1. Lean bear: production fell in the quarter management called "online". Ask: Q1 and Q2 processed and sold tonnage, and why volume fell. |
| A3C-03 | F6 | R026 R158 R013 R020 | L138 (T021) | L138 "After 2, the realisation was 135 rupees." | NEUTRAL-FACT | The garbled realisation ties to the filing. Filed Q2 revenue 166.92 Cr / 12,300 t = Rs 135.7 per kg [DERIVED]. Q1 is Rs 130.5 per kg (176.15 Cr / 13,500 t); H1 is Rs 133.0. This supports the 12,300 t and 25,800 t sold figures. Realisation rose about 4% QoQ while volume fell about 9%: Q2 was price-led, not volume-led (ties presentation A3P-11). Basis includes all operating revenue, so per-kg is an approximation. |
| A3C-04 | F14 | R009 R150 R018 R153 R012 R152 | L59; L62; L69 (T003) | L59 "Krita for the quarter was 7%."; L69 "And the next for the half-year was 21.2 crores."; L62 "We have processed 1,200 tons of raw material" | NEUTRAL-FACT | Three CFO figures do not map to the filing. (1) L69 sits where the H1 net profit sentence belongs. Filed H1 PAT is 20.18 Cr (2,018.14 L), not 21.2 Cr. A mishearing of "20.2" or a misspoken figure; not resolvable from ASR. (2) "7%" (L59) maps to no filed Q2 ratio (PAT margin 6.1%, PBT margin 8.2% [DERIVED]). The parallel H1 sentence (L67) suggests "EBITDA for the quarter was 17.5 crores" (filed 17.54 Cr); candidate only. (3) "1,200 tons" processed against 12,300 t sold is not possible without a large stock draw. A4 uses filed figures. A company-filed transcript, if one appears, should replace these rows. |
| A3C-05 | F14 | R025 R157 R156 R044 R045 R163 R043 R103 R104 | L126-130 (T014-T017); L322-328 (T087-T090) | L128 "We cannot say that."; L130 "365% which is expected to improve with better availability of warm-up."; L328 "Low storage, 85%, 90%." | AMBIGUOUS | Management first refuses to give utilisation, then gives a figure 18 seconds later. Two utilisation figures on one call conflict: "365%" (impossible; "65%" is one candidate) and "85%, 90%" with a garbled label. The deck states no capacity or utilisation figure (presentation A3P-02, A3P-04), and the deck says throughput expansion is "completed". So no baseline exists for the FY27 "enhance our capacity utilisation" commitment (L92). Lean bear: if 65% is right, the plant is supply-starved and the duty-cut story carries the volume case. Ask: installed raw-material capacity (MT per year) before and after the expansion, Q2 utilisation, and the basis of the 85-90% figure. |
| A3C-06 | F6 | R115 R116 R037 R038 R039 (RESTATED) R102 R135 R155 R036 R162 | L280-284 (T070-T071); L291-293 (T075-T076); L296-298 (T078-T079); L121-124 (T012-T013) | L284 "I would love to see 15-18%."; L292 "Yeah, we should be able to maintain this margin."; L296 "16 to 18 percent"; L298 "Yes, yes."; L123-124 "maintain if the situation remains like what it says in last six months" | FORWARD-SIGNAL | An undated margin aspiration of 15-18% against a filed Q2 EBITDA margin of 10.51%: a gap of 449 to 749 bps [DERIVED]. No year in the deck record reaches it (FY24 10.78%, FY25 7.96%, FY26 4.70%, H1 FY27 10.32%). The only firm statement is "maintain this margin"; lean bear, "this" means the current ~10.5%. That statement is itself conditional on the last six months repeating (L123-124). No bridge (spread, mix, utilisation) was given. Ask: what moves margin from 10.5% to 15%, on what timeline, and what margin holds if import parity normalises. |
| A3C-07 | F7 | R056 R065 R066 R166 R167 | L79-80 (T004); L139-145 (T022-T025) | L79-80 "lower imports of dimer acid helping improve the realization and supporting the company's operating margins"; L141 "Dumping has gone down. Dumping has gone down."; L145 "Not from China to India." | AMBIGUOUS | Management names lower imports as the margin driver, but gives no cause for the fall in Chinese dumping. It rejects the analyst's freight theory for the China-India route (L145). The incentive question (L142) has no transcribed answer, and two gaps (R166 25 s, R167 21 s) sit in this exchange. The durability of the driver is unknown. Two readings: (1) a structural change in Chinese export policy or supply; (2) a cyclical lull that reverses. The observation that separates them: dimer acid import volume and landed price into India, quarter by quarter. Ask both. Ties presentation A3P-11, A3P-15. |
| A3C-08 | F14 | R094 (T004 opening) vs deck p15 | L77-78 (T004); deck line 402-403 (presentation A3P-11) | Call L77-78 "improved price realization, primarily reflecting lower raw material cost and higher prices of finished products"; deck "higher price realization primarily due to higher raw material cost and higher import finished product cost" | AMBIGUOUS | The call and the same-day deck give opposite raw-material directions for the same quarter. ASR may have swapped "higher" for "lower"; the deck is the filed text. The direction matters: on the deck reading, realisation rose because input costs rose (pass-through); on the call reading, spread widened from both ends. Lean bear: take the deck reading until management clarifies. Ask: H1 FY27 raw-material cost per tonne vs H1 FY26, and the spread per tonne. |
| A3C-09 | F6 | R100 R101 R099 | L108 (T007); L117-120 (T010-T011) | L108 "there will be some reduction in the prices also"; L118-120 "we do carry some inventory of raw material, but then future already, I mean it has started softening, market prices have started softening a little bit." | FORWARD-SIGNAL | Raw-material prices are softening while the company carries raw-material stock bought at higher prices. If finished-goods prices follow inputs down at import parity, Q3 FY27 carries an inventory-cost squeeze. Filed inventory already fell from 92.2 Cr to 69.9 Cr in H1 (presentation A3P-10), so the stock is smaller, but its cost basis is unknown. Ask: raw-material days on hand at 30-Sep-2026, and the Q3 margin effect of softer input prices. |
| A3C-10 | F7 | R023 R154 R099 R024 | L101-103 (T006); L104-109 (T007); L110-116 (T008-T009) | L102 "on some of the earlier calls, we had spoken of a potential 8% margin hit"; L110 "how can we actually quantify this"; L113 "we suffered badly because of the 27% duty on the food oils" | AMBIGUOUS | The analyst recalls an earlier management warning of an 8% margin hit tied to the duty change. Management did not confirm, deny or size it. It answered on availability (L104-109), then on the past 27% duty (L113). No prior transcript is on record to verify the 8% claim. Lean bear: an earlier warned margin hit is now unaddressed. Ask: what the 8% referred to, whether it still applies after the cut to 11%, and the net effect of more supply against lower import parity. |
| A3C-11 | F7 | R118 R119 R041 R042 R089 R090 R179 | L301-304 (T082); L305-308 (T083); L318-319 (T085) | L304 "there's a high risk that it kind of moves back again"; L305 "Inflation is very high. ... We believe that not take any risk to increase."; L318-319 "we don't expect the government to increase the import duty in near future." | AMBIGUOUS | The volume case (A3C-05) and the input-cost case (A3C-09) both rest on a policy variable the company does not control. Management's comfort is a view on inflation, not a fact. It also states duty sat at "around 5-7%" for 8-10 years (L308), which frames today's 11% as high and conflicts with the 16.5% and 27% levels it cites (L87, L113); ASR-tier, not resolved. Ask: utilisation and margin at a 16.5% duty, and how much supply the duty cut has added so far (MT). |
| A3C-12 | F13 | R029 R075 R138 R120 R121; results A3-07 A3-08 | L201-205 (T048-T049); L325-331 (T088-T092) | L205 "it's already been getting used in our operations as well as our worker colony. So, it's already been used with us and we thought of buying it."; L330 "Since we do not have any immediate expansion plans"; L331 "we need CAPEX. We need to go for CAPEX." | AMBIGUOUS | The call changes the reading of the same-day Rs 12.01 Cr land purchase from the CMD and relatives. The results and deck forensics read the plot as a precursor to expansion (A3-08, A3P-08). Management says the company already uses it, for operations and a worker colony. No management turn contests the analyst's "no immediate expansion plans" (L330); capex waits on new-product success (L325-326). [INFERENCE] The company has been using promoter land; the filing does not show on what terms. Lean bear: a purchase of land already in use, at a self-asserted arm's-length price with no valuer, is a governance point, not a growth signal. Ask: was rent or a licence fee paid to the promoter before, how much, and is the new H1 lease (results A3-01) on this land; the valuer and per-sq-m basis; why buy now. |
| A3C-13 | F6 | R030 R031 R032 R123 R159 | L210-215 (T051-T052) | L213 "we will be having a working capital cycle between 90 to 100 days for domestic sales."; L214 "For export sales it will elevate further."; L215 "So as of now, we should be seeing around 100 days" | FORWARD-SIGNAL | Management's "around 100 days" is close to an A3 rebuild from filed balances: receivables 53.4 + inventory 48.4 - payables 7.8 = about 94 days on H1 FY27 flows [DERIVED]. The deck charts 128 days for H1 FY27 by an unknown method (presentation A3P-10). Two forward points. (1) The deck target of 25% then 50% export share, with export cycles "elevated further", lengthens the cycle as exports grow. (2) Suppliers give almost no credit (payables about 8 days), so the extra days land on cash-credit borrowings. Management did not explain why receivables rose 47% while Q2 revenue fell 5.2% QoQ. Ask: the CCC method behind the deck's 128, export receivable days, and the borrowing limit headroom. |
| A3C-14 | F6 | R095 R105 R111 R113 R122 R076-R078 R081-R083 R093 | L84-86 (T004); L164-165 (T031); L226-231 (T054); L267-271 (T067); L334-343 (T094-T095) | L84-86 "could provide a more favorable trade environment for us to export our products"; L165 "Things are not moving as expected."; L228-229 "cosmetic business will get affected in near term"; L341 "the marketing has not reached its full potential." | FORWARD-SIGNAL | The prepared remarks are upbeat on exports; the Q&A is not. US exports are stalled on freight cost (L164-165). European cosmetic demand for isostearic acid is down (L226-228, L340). The analyst says it has been "a long time" since launch (L334-335). Approvals are "over or ... at advanced stage" (L270-271), so the gate is demand, not approval. The deck targets 25% then 50% of sales from exports (presentation A3P-03); the filing says almost all revenue is domestic. Lean bear: no export lift in H2 FY27. Ask: export share of H1 revenue, isostearic acid volume and revenue, and the year for the 25% step. |
| A3C-15 | F7 | R156 R161 R164 R071 | L128 (T015); L287 (T073); L349 (T097); L115 (T009) | L128 "We cannot say that."; L287 "it would be good if we don't share our raw material combination."; L349 "Manufacturing costs have remained stable, even though we have this inflation."; L115 "We have not lost market share." | AMBIGUOUS | A pattern of withheld numbers on the variables that matter for a converter: utilisation target, raw-material mix, cost-saving size (the deck's energy-audit claim, presentation C8), market share (claimed, not sized) and the new product's name. The deck also carries no volume, capacity or utilisation figure. Taken together, an outsider cannot split Q2 margin into spread and volume. Ask for disclosure at the next call: tonnage processed and sold, installed capacity, and the share of contracted vs spot raw material. |
| A3C-16 | F17 | R072 R085 | L176-177 (T036-T037); L182-183 (T040-T041) | L176 "is it the same product, fat, bypass, sperm, palm oil?"; L177 "No, no, it's a different product."; L182 "this FAD bypass, so this product has commercialised?" | AMBIGUOUS | The deck lists bypass fat from PFAD as a new product (presentation C7). The call confirms the Q3 launch product is a different one (L177). The analyst's direct question on whether bypass fat is commercial gets no answer: the moderator moves to the next caller at L183. The status of a deck-listed product is therefore unknown. Ask: bypass fat commercial status, volume and revenue. |
| A3C-17 | F17 | (cross-document; see section 4) | whole transcript L31-356 | No hit for "held for sale", "lease", "tax", "finance cost", "borrowing" or "buyback" in L31-356. | AMBIGUOUS | Twelve material items from the same-quarter filing and deck went unaddressed (section 4). The ones that bear on cash and governance: the held-for-sale disposal group, the new lease, the Rs 73.46 L tax-asset provision, the 87.5% H1 finance-cost rise, how the Rs 34 Cr buyback was funded, and the land valuation basis. Silence count is 1 quarter (first quarter on record). One quarter is not yet a confirmatory negative under Role 5. A4 should put these to management directly. |
| A3C-18 | F17 | R165-R182 (TIMESTAMP_GAP) R143 R144 | L184-198 (T042-T046); L266-267 (T066-T067) | L184-185 "With regards to how large they can be and the implications"; L272 "That is second thing." | NEUTRAL-FACT | Evidence limit, not a company finding. 18 logged gaps total about 494 s, or 22% of the 2,217 s recording [DERIVED]. 164 s of gaps fall inside the 223 s window from 00:15:32 to 00:19:15, the exchange on new-product size, China and utilisation (R169-R173). The H2 priority answer lists a "second" and "third" thing but the first is not transcribed (13 s gap at L266-267, below A1's 20 s threshold). The VAD setting (R143) may drop quiet speech. Pipeline action: replace with the company-filed transcript when it appears and re-run A1-A3 on these turns. |
| A3C-19 | F14 | R051-R055 (NAME_VARIANT, ASR_DOUBT) R088 | L36; L51; L55; L71; L73; L355 | L51 "Mr. Naush Zarivala, Managing Director and Chairman and Mr. Bhavishta, Chief Financial Officer"; L73 "Thank you Gaurish." | NEUTRAL-FACT | ASR name variants: MD as "Naush Zarivala" and "Naushariwala" (results filing: Nahoosh Jariwala); CFO as "Bhavishta" and "Gaurish" (two different names for one speaker); IR firm as "Valeram" vs header "Valorem"; company as "FAICAM" (L355). No governance meaning. A4 and later stages must take names from the filing, never from this transcript. |

FORWARD-SIGNAL (A4 questions): A3C-01, A3C-06, A3C-09, A3C-13, A3C-14.
AMBIGUOUS (A4 questions): A3C-02, A3C-05, A3C-07, A3C-08, A3C-10, A3C-11, A3C-12, A3C-15, A3C-16, A3C-17.
NEUTRAL-FACT (no question needed): A3C-03, A3C-04, A3C-18, A3C-19.
CONFIRMATORY-NEGATIVE: none (no prior quarter, so no sustained silence can be counted).

## 2. CHECKLIST SCORECARD

| check | status | one-line basis |
|---|---|---|
| F1 Zero-value standing lines | N.A. | Concall. Ledger zero_standing count 0; A1 confirms none present. |
| F2 S-vs-C decomposition | N.A. | Concall; no statements. Filing is standalone only (results Note 4). |
| F3 Shell-entity detection | N.A. | Concall; no cost lines. No subsidiaries (results Note 4). |
| F4 Unaudited contribution ratio | N.A. | Concall; no auditor Other Matters. |
| F5 Going concern / EoM scope | N.A. | Concall; no EoM paragraph. No prior transcript. |
| F6 Forward-commitment phrases | FINDING | 19 commitments registered (section 3). Status changes: new product slipped Q2 to Q3 (A3C-01); production "online" vs derived volume fall (A3C-02); margin aspiration (A3C-06); input-price softening on carried stock (A3C-09); WC days (A3C-13); exports stalled (A3C-14). Realisation tie-out (A3C-03). |
| F7 Hedge phrases | FINDING | Hedges: "cautiously optimistic" L82, "could provide" L85, "could help" L92, "if the situation remains" L123, "hopefully" L197, "would love to see" L284, "try to" L293 and L300, "We are hopeful" L342, "subject to risk" L43 (safe harbour, not counted). Findings: A3C-07, A3C-10, A3C-11, A3C-15. |
| F8 Tax forensics | N.A. | No tax figure spoken on the call. Tax findings sit in results A3-03; their silence is logged in section 4. |
| F9 OCI forensics | N.A. | No OCI or actuarial content on the call. |
| F10 Share count and dilution | N.A. | No share-count, ESOP or warrant content on the call; buyback not mentioned. |
| F11 Reserves and net worth tie-out | N.A. | No net worth figure spoken. |
| F12 Segment forensics | N.A. | Single segment; no segment assets or liabilities discussed. |
| F13 Board outcome beyond results | FINDING | The call adds evidence on board item 2 (land RPT): the land is already in use for operations and a worker colony, which weakens the expansion reading (A3C-12). No AGM, director or capital-raising content. |
| F14 Drafting inconsistencies (concall analogue: spoken vs filed, internal conflicts) | FINDING | Spoken H1 figure 21.2 Cr vs filed PAT 20.18 Cr and other unmapped figures (A3C-04); two conflicting utilisation figures (A3C-05); raw-material cost direction opposite to the deck (A3C-08); ASR name variants (A3C-19). |
| F15 Entity list diffs | N.A. | Concall; no consolidation list. |
| F16 Presentation dropped / reframed | N.A. | Concall, not a deck. Call-vs-deck conflicts are logged under F14 (A3C-08) and F6 (A3C-13, A3C-14). |
| F17 Concall silence audit | FINDING | No Notion checklist (pre-thesis). Audit run against same-quarter results and deck F6 registers and forensics: 12 items not addressed, 3 partly addressed (section 4); A3C-16, A3C-17. Evidence limit from transcript gaps: A3C-18. |

Blank checks: none. GATE A3: pass.

## 3. COMMITMENT REGISTER (F6)

| # | commitment | implied date | turn / line ref | status word |
|---|---|---|---|---|
| C1 | Crude soybean oil duty cut 16.5% to 11% "is expected to improve the raw material availability" | FY27 (course of the year) | T004 L87-88; T007 L104-106 | expected |
| C2 | Raw-material prices to fall as availability improves; "market prices have started softening" | near term (Q3 FY27) | T007 L108; T011 L118-120 | underway (started) |
| C3 | Raise capacity utilisation further (no baseline; target refused L128) | over FY27 | T004 L92; T013 L125; T017 L130 | expected |
| C4 | "maintain" if conditions stay as in the last six months; into the next year ("2020 year", garbled, likely FY28) | rest of FY27 and FY28 | T012-T013 L121-124 | conditional |
| C5 | Raise production 5% every quarter and raise exports ("we are online") | every quarter | T030-T031 L162-164 | claimed underway; derived Q2 volume fell 8.9% QoQ (A3C-02) |
| C6 | US exports: groundwork done; freight cost stalls them | undated | T031 L164-165 | stalled |
| C7 | New product launch, plant built, under modification on R&D advice | Q3 FY27 (slipped from Q2 FY27) | T032-T035 L166-174 | slipped; modification underway |
| C8 | New product: "first company making it"; import substitution plus export potential; "take its own time" | undated | T039 L181; T043-T045 L186-190 | claim |
| C9 | Isostearic acid export approvals "over or ... at advanced stage" (H2 FY27 second priority) | H2 FY27 | T067 L267-272 | near-completed |
| C10 | Isostearic acid cosmetic demand "affected in near term", "going to happen" long term; will scale "once things stabilize" | undated | T054 L228-231; T095 L342-343 | stalled |
| C11 | Value-added linoleic acid products: realisation premium "more than 5% and anywhere between 5 to 10%" over import price | undated | T057 L238-239 | expected |
| C12 | H2 FY27 priorities: first item NOT TRANSCRIBED; second exports approvals; third new product launch | H2 FY27 | T067 L267-274 | stated (incomplete) |
| C13 | Margin: "should be able to maintain this margin", "try to improve"; aspiration 15-18% (analyst 16-18%, "Yes, yes") | undated | T071 L283-284; T076 L292-293; T078-T079 L296-298 | aspiration |
| C14 | "Try to achieve 5-10% growth every quarter" (answer to "immediately from Q3?") | from Q3 FY27 (implied) | T080-T081 L299-300 | target |
| C15 | Working capital cycle 90-100 days domestic; export cycle higher; about 100 days now | standing | T052 L213-215 | stated |
| C16 | No import duty increase expected "in near future" | near future | T085 L318-319 | view |
| C17 | Capacity capex only once the new product proves out ("we'll go for it"; "We need to go for CAPEX") | conditional on C7 | T088 L323-326; T092 L330-331 | conditional |
| C18 | Land purchase (Rs 12 Cr) put "through in the current period"; land already in use | current period (agreement "being entered" per filing) | T048-T049 L201-205 | initiated |
| C19 | Monitor global trade, raw material and import competition over the coming two quarters | Q3-Q4 FY27 | T004 L92-94 | stated |

## 4. WHAT WAS NOT DISCUSSED (F17 silence audit)

Source list: no Notion checklist exists. Items come from the same-quarter results and deck F6 registers and A3 findings. Consecutive quarters of silence = 1 for every row (first quarter on record; no prior transcript).

| item | source | addressed on call? | quarters silent |
|---|---|---|---|
| Held-for-sale disposal group (assets 3.96 Cr, liabilities 1.01 Cr), no note | results A3-10, deck A3P-09 | No | 1 |
| New lease in H1 FY27 (ROU 1.94 Cr), lessor unnamed | results A3-01 | No | 1 |
| Land RPT valuation basis, valuer, independent-director vote | results A3-07 | Partly (use stated L205; price basis not) | 1 |
| Rs 73.46 L provision against non-current tax assets; earlier-year tax | results A3-03 | No | 1 |
| H1 finance cost +87.5% YoY while borrowings fell | deck A3P-20 | No | 1 |
| Funding of the Rs 34 Cr buyback; FY26 debt rise | results A3-05, deck A3P-12 | No | 1 |
| Receivables +47% since March while Q2 revenue fell 5.2% QoQ | deck A3P-10 | Partly (WC days L213-215; divergence not explained) | 1 |
| Q2 revenue decline of 5.2% QoQ | deck A3P-13 | No (callers congratulated, L279, L333) | 1 |
| Throughput expansion "completed with minimal capex"; installed capacity (MT) | deck C1, A3P-02 | No (capacity never stated; utilisation figures conflict, A3C-05) | 1 |
| Capitalised project of about Rs 10 Cr in H1 FY27 | results A3-06 | No | 1 |
| Export target 25% then 50% of sales | deck C4, A3P-03 | Partly (qualitative only, A3C-14) | 1 |
| Bypass fat from PFAD commercial status | deck C7 | Asked L182, not answered (A3C-16) | 1 |
| Domestic catalyst substitution | deck C9 | No | 1 |
| Scrubber for air emissions | deck C10 | No | 1 |
| Energy audit / cost optimisation size | deck C8 | Asked L346-348; no figure (A3C-15) | 1 |
| Actuarial swing / Labour Code cost run-rate | results A3-04 | No (low money value) | 1 |

## 5. LIMITATIONS

- ASR-tier source. Every spoken number may be misheard; none was corrected. Speaker turns are inferred (R144).
- About 22% of the recording time sits in logged gaps (A3C-18); the new-product and utilisation exchange is the worst hit.
- Pre-thesis read: no thesis or checklist, so no finding is weighed against a thesis claim.
- No prior transcript: the analyst's references to "earlier calls" (L102, L157, L162) cannot be verified.
- Not disclosed on the call (NOT FOUND): installed capacity, Q2 processed tonnage, raw-material mix, export share, new-product name, isostearic acid revenue, land valuation basis.

```yaml
stage: A3-forensics
company: "FAIRCHEMOR"
quarter: "q2fy27"
doctype: "concall"
model: "claude-opus-5-5"
status: complete
forensics_path: "runs/fairchemor-q2fy27/work/forensics_fairchemor_q2fy27_concall.md"
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
  - {id: "A3C-01", check: "F6", line: "L166-168 'Sir, only in third quarter.'; L173 'we are observing and modifying that plant'; L187", classification: "FORWARD-SIGNAL", implication: "New product slipped Q2 to Q3 FY27; plant built but under modification; unnamed; size answer lost in gaps; Q3 is a dated test"}
  - {id: "A3C-02", check: "F6", line: "L162-164 'Yes, yes, we are online.'; L63; L70", classification: "AMBIGUOUS", implication: "5%-per-quarter production claim vs derived sold volume 13,500 t to 12,300 t (-8.9% QoQ) and filed revenue -5.2% QoQ; ask Q1/Q2 processed and sold tonnage"}
  - {id: "A3C-03", check: "F6", line: "L138 'the realisation was 135 rupees'", classification: "NEUTRAL-FACT", implication: "Ties to filed revenue / 12,300 t = Rs 135.7/kg; Q1 Rs 130.5/kg; Q2 price-led (+4% realisation, -9% volume)"}
  - {id: "A3C-04", check: "F14", line: "L59 'Krita for the quarter was 7%'; L62 '1,200 tons'; L69 '21.2 crores'", classification: "NEUTRAL-FACT", implication: "Spoken H1 figure 21.2 Cr vs filed H1 PAT 20.18 Cr; 7% and 1,200 t unmappable; A4 uses filed figures; replace with company transcript if filed"}
  - {id: "A3C-05", check: "F14", line: "L128 'We cannot say that.'; L130 '365%'; L328 'Low storage, 85%, 90%.'", classification: "AMBIGUOUS", implication: "Refusal then two conflicting utilisation figures; no capacity baseline anywhere; FY27 utilisation commitment untestable; ask installed MT and Q2 utilisation"}
  - {id: "A3C-06", check: "F6", line: "L284 'I would love to see 15-18%.'; L292 'maintain this margin'; L296-298; L123-124", classification: "FORWARD-SIGNAL", implication: "Undated 15-18% aspiration vs filed Q2 EBITDA margin 10.51% (+449 to +749 bps); firm statement is only 'maintain', conditional on last six months repeating; no bridge"}
  - {id: "A3C-07", check: "F7", line: "L79-80 'lower imports of dimer acid'; L141 'Dumping has gone down.'; L145 'Not from China to India.'", classification: "AMBIGUOUS", implication: "Margin driver is lower Chinese imports with no stated cause; structural vs cyclical; separator = dimer acid import volume and landed price by quarter"}
  - {id: "A3C-08", check: "F14", line: "L77-78 'lower raw material cost'; deck line 402-403 'higher raw material cost'", classification: "AMBIGUOUS", implication: "Call and same-day deck give opposite input-cost direction; possible ASR swap; take deck reading; ask RM cost and spread per tonne"}
  - {id: "A3C-09", check: "F6", line: "L118-120 'we do carry some inventory of raw material ... market prices have started softening'", classification: "FORWARD-SIGNAL", implication: "Softening inputs against stock bought higher; Q3 FY27 inventory-cost squeeze risk if finished prices follow import parity down"}
  - {id: "A3C-10", check: "F7", line: "L102 'potential 8% margin hit'; L104-116", classification: "AMBIGUOUS", implication: "Earlier-warned 8% margin hit from duty change neither confirmed nor sized; answer pivoted to availability; ask net effect"}
  - {id: "A3C-11", check: "F7", line: "L304 'high risk that it kind of moves back'; L305; L308; L318-319", classification: "AMBIGUOUS", implication: "Volume and input-cost case rest on import duty staying low; management view only; duty history figures conflict (5-7%, 16.5%, 27%); ask utilisation and margin at 16.5%"}
  - {id: "A3C-12", check: "F13", line: "L205 'it's already been getting used in our operations as well as our worker colony'; L330-331", classification: "AMBIGUOUS", implication: "Rs 12.01 Cr promoter land is already in use, weakening the expansion reading (results A3-08); ask prior rent to promoter, link to new H1 lease, valuer, why buy now"}
  - {id: "A3C-13", check: "F6", line: "L213-215 '90 to 100 days for domestic sales ... For export sales it will elevate further'", classification: "FORWARD-SIGNAL", implication: "Mgmt ~100 days matches A3 rebuild ~94 days; deck 128 unreproduced; export push lengthens cycle onto cash-credit (payables ~8 days)"}
  - {id: "A3C-14", check: "F6", line: "L84-86; L165 'Things are not moving as expected.'; L228-229; L341 'has not reached its full potential'", classification: "FORWARD-SIGNAL", implication: "Opening export optimism vs Q&A: US stalled on freight, EU cosmetic isostearic demand down, approvals done so gate is demand; no H2 export lift vs deck 25%/50% target"}
  - {id: "A3C-15", check: "F7", line: "L128; L287 'we don't share our raw material combination'; L349; L115", classification: "AMBIGUOUS", implication: "Withheld utilisation target, RM mix, cost-saving size, market share and product name; with no deck volumes, margin cannot be split into spread and volume"}
  - {id: "A3C-16", check: "F17", line: "L177 'No, no, it's a different product.'; L182 'this FAD bypass, so this product has commercialised?'; L183", classification: "AMBIGUOUS", implication: "Deck-listed bypass fat status asked and not answered; Q3 product is a different one; ask commercial status"}
  - {id: "A3C-17", check: "F17", line: "whole transcript L31-356 (no hit for held for sale, lease, tax, finance cost, borrowing, buyback)", classification: "AMBIGUOUS", implication: "12 filed or deck items unaddressed and 3 partly addressed, 1 quarter of silence; held-for-sale, lease, tax provision, finance cost, buyback funding, land valuation go to A4"}
  - {id: "A3C-18", check: "F17", line: "L184-198 (gaps R169-R173); L266-272 'That is second thing.'", classification: "NEUTRAL-FACT", implication: "18 gaps about 494 s = 22% of recording; 164 s in the new-product/utilisation window; first H2 priority not transcribed; re-run on company transcript"}
  - {id: "A3C-19", check: "F14", line: "L51 'Mr. Naush Zarivala ... Mr. Bhavishta'; L73 'Thank you Gaurish.'", classification: "NEUTRAL-FACT", implication: "ASR name variants for MD, CFO, IR firm and company; take names from the filing only"}
forward_signals: ["A3C-01", "A3C-06", "A3C-09", "A3C-13", "A3C-14"]
ambiguous: ["A3C-02", "A3C-05", "A3C-07", "A3C-08", "A3C-10", "A3C-11", "A3C-12", "A3C-15", "A3C-16", "A3C-17"]
commitments:
  - {commitment: "Duty cut 16.5% to 11% expected to improve raw material availability", implied_date: "FY27", ref: "T004 L87-88; T007 L104-106", status_word: "expected"}
  - {commitment: "Raw material prices to fall; already softening", implied_date: "Q3 FY27", ref: "T007 L108; T011 L118-120", status_word: "underway"}
  - {commitment: "Raise capacity utilisation further (no baseline, target refused)", implied_date: "FY27", ref: "T004 L92; T013 L125; T017 L130", status_word: "expected"}
  - {commitment: "Maintain if conditions stay as last six months, into next year", implied_date: "rest of FY27 and FY28", ref: "T012-T013 L121-124", status_word: "conditional"}
  - {commitment: "Raise production 5% every quarter and raise exports ('we are online')", implied_date: "every quarter", ref: "T030-T031 L162-164", status_word: "claimed underway (derived Q2 volume -8.9% QoQ)"}
  - {commitment: "US exports groundwork done, stalled on freight", implied_date: "undated", ref: "T031 L164-165", status_word: "stalled"}
  - {commitment: "New product launch; plant built, under modification", implied_date: "Q3 FY27 (slipped from Q2)", ref: "T032-T035 L166-174", status_word: "slipped"}
  - {commitment: "New product first-in-company-class, import substitution plus export, ramp takes own time", implied_date: "undated", ref: "T039 L181; T043-T045 L186-190", status_word: "claim"}
  - {commitment: "Isostearic acid export approvals over or at advanced stage", implied_date: "H2 FY27", ref: "T067 L267-272", status_word: "near-completed"}
  - {commitment: "Isostearic acid cosmetic demand to recover long term; scale once stable", implied_date: "undated", ref: "T054 L228-231; T095 L342-343", status_word: "stalled"}
  - {commitment: "Linoleic value-added products premium 5-10% over import price", implied_date: "undated", ref: "T057 L238-239", status_word: "expected"}
  - {commitment: "H2 FY27 priorities: first not transcribed, exports second, new product third", implied_date: "H2 FY27", ref: "T067 L267-274", status_word: "stated (incomplete)"}
  - {commitment: "Maintain current margin, try to improve; aspiration 15-18%", implied_date: "undated", ref: "T071 L283-284; T076 L292-293; T079 L298", status_word: "aspiration"}
  - {commitment: "Try to achieve 5-10% growth every quarter", implied_date: "from Q3 FY27 (implied)", ref: "T080-T081 L299-300", status_word: "target"}
  - {commitment: "Working capital 90-100 days domestic, higher for exports, ~100 days now", implied_date: "standing", ref: "T052 L213-215", status_word: "stated"}
  - {commitment: "No import duty increase expected", implied_date: "near future", ref: "T085 L318-319", status_word: "view"}
  - {commitment: "Capacity capex only after new product proves out", implied_date: "conditional on new product", ref: "T088 L323-326; T092 L330-331", status_word: "conditional"}
  - {commitment: "Land purchase (Rs 12 Cr) of land already in use", implied_date: "current period", ref: "T048-T049 L201-205", status_word: "initiated"}
  - {commitment: "Monitor trade, raw material and import competition", implied_date: "Q3-Q4 FY27", ref: "T004 L92-94", status_word: "stated"}
gate_a3: pass
blank_checks: []
analyst_note: "ASR-tier call; spoken headline figures tie to the filing except the H1 '21.2 crores' (filed PAT 20.18 Cr). The call's main value is three cross-document corrections. First, Q2 was price-led: management's own tonnage gives sold volume down 8.9% QoQ while realisation rose about 4%, and that contradicts the 'we are online' claim of 5% production growth per quarter. Second, the Rs 12.01 Cr promoter land is already in use for operations and a worker colony. That weakens the expansion reading in the results and deck forensics and points to a governance question: prior rent to the promoter and the price basis. Third, the export story stalls in Q&A (US freight, EU cosmetic demand) despite the opening optimism and the deck's 25%/50% target. Margin durability rests on two outside variables: low Chinese dimer acid imports, with no stated cause, and a low crude-oil duty. The 15-18% figure is an aspiration; the only firm statement is 'maintain', and it is conditional. 22% of recording time sits in gaps, concentrated on the new-product and utilisation exchange. Re-run on a company transcript if one is filed."
```
