# STAGE 12, VERIFIER B: CONCALL RED FLAGS, TD Power Systems Ltd (TDPOWERSYS), run 2026-11-15

Model: claude-opus-5-5. Fresh context. Inputs: 3 TDPS transcripts, 12 peer transcripts, B05 and B06 reports. No other verifier output was read.

## 0. Scope and read route

**Anchor key.** Q3C = `inputs/concalls/1_2026-02-04_Q3FY26_Transcript` (call held 30 Jan 2026). Q4C = `2_2026-05-19_Q4FY26_Transcript` (call held 15 May 2026). Q1C = `3_2026-08-18_Q1FY27_Transcript` (call held 12 Aug 2026). File names carry the filing date, not the call date. "p.N" = the `[page N]` marker in the .txt, which is the PDF page. NK = Nikhil Kumar (MD). MV = M N Varalakshmi (CFO). VH = Vinay Hegde (sales head).

**Coverage, stated honestly.**
- TDPS: all 3 transcripts read in full, fresh, before B05 and B06 were opened.
- Peers: 3 of 12 read in full (AZAD Q1 FY27, CGPOWER Q1 FY27, TRITURBINE Q1 FY27). Read in part: TRITURBINE Q4 FY26 p.3-5 and p.15, AZAD Q3 FY26 p.12-13. The other 9 were searched by topic: domestic market, orders and enquiries (Triveni, all 4); copper, price hikes and data centres (CG, Q2 to Q4 FY26); data centres, gas turbines, slots, backlog and lead time (Azad, all 4); tariffs (all 12); "generator" (all 12, zero hits). A peer item outside those topics could be missed.
- Not read: the Q2 FY26 TDPS transcript in `inputs/other/` (outside the named inputs). The Q2 FY27 transcript is absent from the corpus (B05 records this).
- Numbers. Verifier A owns whether a number exists at its anchor. This report judges reading, weighting and direction only. Where I do arithmetic, I say "my arithmetic".

---

## 1. Independent red-flag list (from the raw transcripts alone, then graded)

Severity scale: CRITICAL / MAJOR / MINOR, same as all verifiers. Grade = weight of the item itself, not of the pipeline's treatment.

| # | Item | Anchors (call, speaker, location) | Severity |
|---|---|---|---|
| I-1 | **Large-generator plan: repeated deferral across two quarters, past a date management set itself.** Q4: "in about 2 or 3 months from now, I will be happy to answer all these questions in full detail"; "all these questions will be answered in the next quarter"; "All questions are questions after 3 months, please." Q1: "close to signing agreements ... probably in the month of August"; TAM: "I can't give you any further information right now"; revenue timing: "I have no comments. I can't answer any of these questions." Timeline also moved: Q3 "ramp-up in this business in '27, calendar '27, and we still stick to that schedule" (20-100 MW); Q4 "big ramp-up ... only in calendar '28" (above 100 MW). Four analysts asked in Q4, three in Q1. | Q4C p.5-6, p.9, p.12 NK; Q1C p.4, p.5, p.12 NK; Q3C p.12 NK | CRITICAL (repeated evasion, 2+ quarters) |
| I-2 | **Data-centre share of orders refused on all three calls; gas-turbine vs gas-engine split refused.** Q3: "No, we're not going to give that information, Ganesh." Q4: "Generally, we don't give a split." Q1: "No, we don't give that split-up of applications." Export share of Q1 inflow is 93%. CG Power has the same policy ("they're not breaking it down", CG Q1 FY27 p.14), so this is a disclosure policy, not a dodge of one fact. It still blocks sizing the core demand concentration. | Q3C p.12; Q4C p.12; Q1C p.3, p.9 NK | MAJOR |
| I-3 | **Margin narrative softened over three calls; levers never decomposed.** Q3: copper "absolutely no problem in getting the price increases"; gross margin 35% "Yes"; FX upside "very positive ... from Q4 itself, definitely to a major extent in Q1". Q4: "hovering between 33% and 34% ... let's say 34%"; "our hedges are now running out ... some of the prices are not kicking in"; FX now the offset that makes margins "neutral"; "let's see how it plays out"; "if the commodity prices again go up ... another 20%, 30%, then we have to see". Q1: "plus/minus 1%"; "I can't give you the exact breakup"; "I cannot commit"; "I answered this question a number of times". Three analysts asked the same question on Q1. Peer: CG said three days before the Q3 call that its price rise "could not completely cover the increase in the commodity prices" (CG Q3 FY26 p.4) and "Is that sufficient? No" (CG Q1 FY27 p.4-5). | Q3C p.6, p.8, p.9, p.13; Q4C p.6, p.8, p.16; Q1C p.7, p.15 NK | MAJOR |
| I-4 | **Share of wallet with OEMs refused across two quarters, and the answer changed.** Q4: "I'm not going to answer that question" (to Karan, after he asked twice). Q1: "we don't have that number". | Q4C p.10; Q1C p.9 NK | MAJOR |
| I-5 | **Equity raise not signalled on the Q3 or Q4 calls; refused on Q1.** Q4: "all our retained earnings are basically going into working capital." Q1: QIP timing "not in a position to be able to answer"; on debt vs equity: "I'm not going to be able to talk about any fundraise issues" before the Friday board. Each call says "we continue to maintain a strong cash position". | Q4C p.12 NK; Q1C p.15, p.17 NK; Q3C p.4, Q4C p.4, Q1C p.3 | MAJOR |
| I-6 | **Working capital and a bargaining-power asymmetry.** Analyst: EBITDA to CFO 21% for FY26; MV first said she did not understand the question. Q1: payment terms "cannot be altered significantly because otherwise, we will lose business ... practically, it is not possible"; TD's own advances come from "certain customers", quantum "Sorry, we can't do that". Same call: OEM customers "have taken significant amounts of non-refundable advances". So OEMs hold buyer cash while TD finances the cycle. Peer: suppliers do not get the OEM price rises (Azad Q3 FY26 p.13, "pricing decisions are not being done"). | Q4C p.11-12 MV, NK; Q1C p.13, p.14, p.17 NK | MAJOR |
| I-7 | **Domestic steam turbine: "steady 10-12%, no surprises" repeated on all three calls against falling domestic orders.** Q3: analyst already asks about "sequential movement of domestic orders downwards"; VH answers 10-12%. Q4 and Q1: "no surprises both on the upside or the downside". TD domestic share of inflow: 21% (Q3, Q4) to 7% (Q1). Same Q1 call: "very buoyant market for TDPS in all segments" (p.3) and "In India, the demand is fairly subdued" (p.14). Peer, one day earlier: Triveni domestic order booking "lower by 35.4%" and "The Indian market has seen a decline, and that is broad-based across all industries". Triveni's FY26 "35%" growth figure was withdrawn on its own call ("this is not a correct number"). Steam turbines are about 25% of TD revenue (VH, Q4C p.12). | Q3C p.4-5 VH; Q4C p.4 NK; Q1C p.3-4, p.14 NK; TRITURBINE Q1 FY27 p.3, p.6; TRITURBINE Q4 FY26 p.15 | MAJOR |
| I-8 | **Big new US customer promised, never confirmed.** Q3: "very close to acquiring a big new customer in the U.S. market", engineering order to become a machine order "by the next couple of weeks". Not mentioned in Q4. Q1: "We don't have any major client additions at the moment"; "we don't see a big opportunity to increase client addition which can dramatically change the business outlook." | Q3C p.7 NK; Q1C p.10 NK | MAJOR |
| I-9 | **Data-centre downstream delays: tone shift from denial to concession.** Q4: "it's just the opposite ... 180 degrees reverse", not "a single machine sitting in our shop". Q1: first "I don't know how shipping delays will cause disruptions", then "They may not be commissioned immediately. It could be execution delays", then "Let's move on to the next question"; minutes later: "as Alisha pointed out a little bit earlier, there are execution delays on the data centre side." Prepared remarks add "Despite differing views on the sustainability of this buoyancy in the media". Peer: Triveni says site activities "may not have kept pace" and customers "pushed out some of their dispatches". | Q4C p.7 NK; Q1C p.4, p.8, p.9 NK; TRITURBINE Q1 FY27 p.7 | MAJOR |
| I-10 | Employee cost: "We have largely employed everyone ... no major increases" (Q4) then +20% QoQ (analyst, Q1); count of additions refused ("we don't share that kind of information"). | Q4C p.9 NK; Q1C p.13 MV | MINOR |
| I-11 | Rail reversal: "steady state situation for the next few years", 4 markets including Russia (Q3); "nothing new to report" (Q4); "not taking any fresh orders ... review the sustainability" (Q1). | Q3C p.5, p.11; Q4C p.5; Q1C p.4 NK | MINOR |
| I-12 | Motors: about Rs 150 cr FY26 target and "not having the same priority" (Q3); "remains a key focus area", "expect the Motor segment to stabilize" (Q4); "key area" (Q1). No number ever confirmed. | Q3C p.5, p.10; Q4C p.4-5; Q1C p.4 NK | MINOR |
| I-13 | Turkey: liquidated-damages penalty, "the customer also was exceptionally brutal", amount never given; "most of our contracts ... are ex works" yet shipping was in scope; plant now an "insurance facility" with a cost "to keep it alive", "We don't see a big pipeline for business for next year". | Q4C p.4, p.6; Q1C p.10-12 NK | MINOR |
| I-14 | Capacity and capex numbers drift between and inside calls: Rs 2,600-2,800 cr peak (Q3) to Rs 3,000-3,200 cr with Rs 50 + 50 cr (Q4) to Rs 3,200 cr; Q1 prepared remarks "INR22 billion" and "INR500 million" vs Q&A "INR32 billion", "INR50 crores", analyst's Rs 100 cr accepted ("Yes"), then "now I'm saying we need INR50 crores for FY28". Bulk-capacity decision "around this time next year" (Q3) became "next earnings call" (Q1). | Q3C p.10, p.12-13; Q4C p.7; Q1C p.4-6, p.12 NK | MINOR |
| I-15 | Guidance upside language shrank: "extremely high probability to increase our guidance further" (Q3, Q4) to "a small chance that we may even cross this number" (Q1). Q2 later beat it (per B05, filed data). | Q3C p.5; Q4C p.5; Q1C p.4 NK | MINOR |
| I-16 | Dismissive answers to AI-demand questions: "Absolutely not. Absolutely not. I don't know how else to answer this question" (Q3); "I have absolutely no idea" (Q1). Repetition irritation: "again and again and again" (Q1 twice), "I don't want to answer it once again". | Q3C p.9; Q1C p.12, p.15, p.16 NK | MINOR |
| I-17 | Hydro language softened: "the highest in the history of the company" (Q3) to "one of the highest" (Q4, Q1). Inside Q1: refurbishment "in India and abroad" (p.4) vs "At the moment, we're not looking at taking it global" (p.10). | Q3C p.5; Q4C p.4; Q1C p.4, p.10 NK | MINOR |
| I-18 | DFPS subsidiary: 100% of the investment provided (Rs 30 mn) in FY26, volunteered in prepared remarks. | Q4C p.3 NK | MINOR |
| I-19 | FX left largely unhedged by choice: "Very small volume. 10% of our business"; "We took a conscious decision to stop hedging". Export book 75-93%. A firming rupee reverses the tailwind. | Q3C p.12 MV, NK | MINOR |
| I-20 | Q1 export share of order book "57%" against 76% (Q4) with 93% export inflow; "87% on a Q-on-Q basis" is year on year. | Q1C p.3 NK; Q4C p.3 | MINOR |
| I-21 | China question not answered: "Something I cannot understand"; "I don't see why this suddenly becomes an issue"; then "I didn't answer it correctly". | Q3C p.6, p.13-14 NK | MINOR |
| I-22 | New CEO surfaced only when an analyst asked; "Deepak is not on the call. Right. So maybe he logged out." | Q4C p.15 NK | MINOR |
| I-23 | Aftermarket undercut by management: "almost 0 service potential in the first 10 years"; service 5-6% of sales. | Q1C p.11 NK | MINOR |
| I-24 | CFO answer quality: asked about receivables, MV said "the outstanding creditors have been completely covered", then "Yes" to the analyst's "INR700 crores ... completely covered"; asked about EBITDA to CFO, "I don't understand it". | Q4C p.11 MV | MINOR |
| I-25 | Volunteered utilisation risk: "the factory is running very full", a breakdown means "production delays", "this is a new normal". | Q4C p.14-15 NK | MINOR |

Counts: 25 items. CRITICAL 1, MAJOR 8, MINOR 16. Material (CRITICAL + MAJOR) = 9.

---

## 2. Comparison against the pipeline (B05, B06)

| # | Status | Where the pipeline has it | Note |
|---|---|---|---|
| I-1 | CAUGHT | B05 2E row 4; 1C; "Timelines that keep slipping"; 2A rows 13, 18, 23; 4D #10 | B05 handles the 20-100 MW vs above-100 MW ambiguity fairly. |
| I-2 | CAUGHT | B05 2D; 2E row 1; 4D #3 (High) | |
| I-3 | CAUGHT | B05 1C pricing row; 2A rows 5, 6; 2B; 2E row 2; 3A; B06 Q4, 2B | |
| I-4 | CAUGHT | B05 2E row 3; 3C; B06 Q5 | |
| I-5 | CAUGHT | B05 0A item 4; 2D; 3C; 4D #2 (High) | Precision point in F9. |
| I-6 | CAUGHT | B05 2E row 7; 3C; 2A row 19; 4D #1; B06 Q7, Q10, cross-peer hypothesis | Facts and refusals are in B05; the asymmetry is drawn in B06. |
| I-7 | PARTIALLY CAUGHT | B05 3B ("a habit, not a measurement"), 3D, 4D #4; B06 Q1 net read | B06 labels the claim PARTIALLY VERIFIED though its net read says the latest quarter reverses it. B05 never lists the management claim itself as contradicted by TD's own inflow. See F3. |
| I-8 | CAUGHT | B05 2A row 9; dropped triggers; slippages | Outcome over-classified as missed. See F4. |
| I-9 | PARTIALLY CAUGHT | B05 3B: "execution delays sit at data-centre sites, not at TD"; 1C "Q1C adds a defensive line"; B06 2E freight | B05 takes the management framing as reassurance. The Q4-to-Q1 shift and the intra-call reversal are not flagged. See F2. |
| I-10 | CAUGHT | B05 2A row 17; 2E row 6 | Headcount label questioned in F5. |
| I-11 | CAUGHT | B05 2A row 10; 1C; dropped triggers | |
| I-12 | CAUGHT | B05 2A row 12; 1C; dropped triggers | |
| I-13 | CAUGHT | B05 2B; 2A row 16; 2D; dropped triggers | |
| I-14 | CAUGHT | B05 1B conflict rows; 1C; 4D #6 | |
| I-15 | PARTIALLY CAUGHT | B05 1B and 0A quote "small chance"; not weighed as a tone shift | F10. |
| I-16 | CAUGHT | B05 2C defensiveness; 3C; 4D #11 | |
| I-17 | PARTIALLY CAUGHT | B05 1A, 1C record "not going global" and "one of the highest"; contradiction and softening not flagged | F10. |
| I-18 | MISSED | not in B05 or B06 | F7. |
| I-19 | PARTIALLY CAUGHT | B05 1B and 3B record the hedge fact; not flagged as a reversal risk | F10. |
| I-20 | CAUGHT | B05 3D export-share conflict and mislabel; 4D #12 | |
| I-21 | CAUGHT | B05 2B; 3A | |
| I-22 | CAUGHT | B05 2D | |
| I-23 | CAUGHT | B05 3B | |
| I-24 | PARTIALLY CAUGHT | B05 2A row 21 records the answer but credits the analyst's words to MV | F6, F10. |
| I-25 | CAUGHT | B05 2D (risk answer names only equipment breakdown) | |

Totals: CAUGHT 18, PARTIALLY CAUGHT 6, MISSED 1. Material: 7 CAUGHT, 2 PARTIALLY CAUGHT (I-7, I-9), 0 MISSED.

### 2A. Pipeline red flags not on my list, assessed against the transcripts

| Pipeline flag | Assessment | Basis |
|---|---|---|
| B05 4D #1 cash conversion via advances | SUPPORTED | Transcript evidence agrees: EBITDA to CFO 21% (Q4C p.11), "retained earnings ... into working capital" (Q4C p.12), terms cannot change (Q1C p.17), Q1 current-liability rise is "customer advances and also the provision for taxation" (Q1C p.16 MV). Filed numbers are Verifier A's. |
| B05 4D #4 order-book roll-forward gap about Rs 320 cr | SUPPORTED IN PART | Revenue basis is unstated on the calls and moves the gap. See F8. |
| B05 4D #7 customer concentration never addressed | SUPPORTED | No call gives a customer share. "Not being dependent on a single market and a single segment" (Q3C p.4) is a segment claim. |
| B05 4D #8 labour dispute and management exits absent from calls | SUPPORTED (as an absence) | Asked for major risks, NK names only factory utilisation and breakdowns (Q4C p.14-15). |
| B05 4D #9 guidance is a floor | SUPPORTED | "Conservative" (Q3C p.5, p.7); raised at Q4C p.5 and Q1C p.4. |
| B05 4D #10 large-generator claim unvalued; 18-20 months vs Aug 2027 delivery | SUPPORTED (as an open question) | "it takes within 18 to 20 months to make a large generator" (Q1C p.7). Whether the Rs 192 cr order is a large unit is NOT FOUND in the transcripts. |
| B05 4D #12 mis-statements | SUPPORTED | Q1C p.3 "87% on a Q-on-Q basis"; Q4C p.12 "at least INR33 billion". |
| B06 Q9 CONTRADICTED ("no order disruption" from US tariff) | OVERSTATED | Wrong premise on TD's customer type. TD's own Q3 FY26 inflow was a record. See F1. |
| B06 FLAG-DATA-CENTRE-NOT-YET-ORDERS | SUPPORTED, limited reach | Triveni: "we are hoping it could translate in this year" (TRITURBINE Q1 FY27 p.11). The flag is about steam-side demand. TD's gas-generator data-centre orders are booked. TD itself puts combined cycle "years from now" (Q1C p.9). |
| B06 FLAG-MARGIN-CAPTURE-BY-CONTRACT-TYPE | SUPPORTED, with a TD-side fact B06 did not cite | TD says "We have price variation clauses for raw material variations" (Q4C p.10) and "wherever we have price variation clauses, those have been implemented" (Q1C p.7). The share of the book covered stays NOT FOUND. |
| B06 FLAG-PEER-SET-ADJACENT | SUPPORTED | My search for "generator" across all 12 peer files returned zero hits. |
| B06 FLAG-GUIDANCE-COUNTEREXAMPLE | SUPPORTED | Triveni FY26 growth "9%" (TRITURBINE Q4 FY26 p.4). The Q3 FY26 p.14 guide quote was not re-read. |

NOT SUPPORTED pipeline flags: none.

---

## 3. Promise-delivery spot checks (B05 2A)

| B05 row | Did the earlier call contain the promise? | Does the later call show the outcome? | Result |
|---|---|---|---|
| 1. FY26 revenue "cross INR 1,800 crores" | Yes: "we will cross INR 1,800 crores this financial year" (Q3C p.5 NK) | Yes, on consolidated only: standalone total income Rs 17.37 bn (Q4C p.3), consolidated Rs 18.78 bn (Q4C p.4). B05 states the basis split. | CONFIRMED |
| 2. Q4 FY26 Rs 550-575 cr | Yes: "In Q4, we'll ramp up to INR 550 crores to INR 575 crores" (Q3C p.4 NK) | Yes. Transcript arithmetic (my arithmetic): consolidated total income 18.78 - 12.8 = Rs 598 cr; standalone 17.37 - 11.94 = Rs 543 cr (Q4C p.3-4; Q3C p.3-4). Matches B05's in-band consolidated, below-band standalone. | CONFIRMED (speaker slip, F6) |
| 5. Gross margin about 35% | Yes: analyst "sustain here at around 35%?", NK "Yes." (Q3C p.13) | Yes: "we are about 3% down from that in this last quarter" (Q4C p.6 NK) | CONFIRMED |
| 9. Big new US customer | Yes: "very close to acquiring a big new customer in the U.S. market"; machine order "by the next couple of weeks" (Q3C p.7 NK) | No. Neither Q4C nor Q1C reports on conversion. "We don't have any major client additions at the moment" (Q1C p.10) is present-tense and does not say the Q3 customer was lost. B05 itself cites a "second major global OEM" (presentation p.27). | WRONG (silence, not a miss; F4) |
| 17. "No major increases" in employee cost | Yes: "There could be incremental increases, but no major increases taking place from this point onwards" (Q4C p.9 NK) | Yes: analyst cites "20% Q-o-Q employee expense increase"; MV: "The number of employees have increased" (Q1C p.13) | CONFIRMED (headcount label, F5) |

Checked 5, confirmed 4, wrong 1.

---

## 4. Findings (standard severity rows)

| ID | Severity | Finding | Anchor | Fix |
|---|---|---|---|---|
| F1 | MAJOR | B06 Q9 verdict CONTRADICTED is OVERSTATED. B06 weights Triveni and CG over Azad because they "sell capital equipment to the end buyer, as TD does". That premise is wrong. TD sells generators to prime-mover OEMs, which is Azad's position, and B06 says Azad saw no disruption. TD's own Q3 FY26 inflow was a record Rs 6.56 bn, +61% YoY, 84% export. B06 calls this its "most consequential contradiction" and a priority for synthesis. | B06 Q9 net read and Part 4; AR FY26 p.82 (BRSR: "customer base of manufacturers of prime movers"); Q4C p.8 NK ("x number of engines, then you need x number of generators"); Q3C p.3 NK | For TD, reclassify to PARTIALLY VERIFIED: customer-pays is corroborated, disruption is not shown at TD. Keep the peer deferral as context. Add the TD-side signal B06 did not use: an analyst says TD used the Turkey plant for FY26 exports "because of the tariff uncertainties" (Q1C p.11). That is an operational adjustment, not lost orders. |
| F2 | MAJOR | I-9 is material and only partly caught. Management moved from "180 degrees reverse" (Q4) to "there are execution delays on the data centre side" (Q1). It first denied the point on the same call and cut the analyst off. B05 records only that delays "sit at data-centre sites, not at TD", which repeats management's framing as reassurance. Downstream commissioning lag can build OEM inventory before it cuts TD orders. Triveni independently reports dispatches pushed out for the same reason. | Q4C p.7; Q1C p.8, p.9 NK; TRITURBINE Q1 FY27 p.7; B05 3B | Record it as a tone shift and a leading indicator. Add a tracker kill signal beside "inflow / revenue below 1.0": OEM or customer reports of deferred dispatch or commissioning. |
| F3 | MINOR | I-7 is under-labelled. B06 Q1 grades "domestic market growing 10-12%" PARTIALLY VERIFIED. Its own net read says the latest quarter reverses it. Management said "no surprises both on the upside or the downside" while TD's domestic share of inflow fell from 21% to 7%. Triveni domestic orders fell 35.4%, a "broad-based" decline. Triveni's 35% FY26 figure was withdrawn on its call. The Q1 call itself says "very buoyant ... all segments" (p.3) and "India ... fairly subdued" (p.14). | Q3C p.4-5; Q4C p.4; Q1C p.3-4, p.14; TRITURBINE Q1 FY27 p.3, p.6; TRITURBINE Q4 FY26 p.15 | Label the claim CONTRADICTED for the latest quarter, magnitude unanchored. B05 should list the "steady 10-12%" claim as contradicted by TD's own inflow on a segment of about 25% of revenue (Q4C p.12 VH). |
| F4 | MINOR | B05 2A row 9 classes the big US customer as missed (❌). Neither later call shows non-conversion. It is silence. | Q3C p.7; Q1C p.10; B05 2A row 9 | Reclassify UNVERIFIED (silence). Counts become 11 delivered, 5 partial, 3 missed. Grade B is unchanged. |
| F5 | MINOR | B05 reads MV's "we are scaling up from 1,750 to 2,600" as headcount and carries it as fact (1B, 2B, 2E row 6, 3C, 4B item 8). B06 Q8 then PARTIALLY VERIFIES it. The phrase is ambiguous. 2,600 equals the FY27 revenue guide on the same call (Rs 2,600 cr, Q1C p.4), and FY26 standalone total income was Rs 17.37 bn (Q4C p.3). The AR shows 1,550 total staff at 31 Mar 2026 (730 employees plus 820 workers, my arithmetic), which also fits headcount. In the next answer MV refused the number of employees added. | Q1C p.13 MV; Q1C p.4; Q4C p.3; AR FY26 p.82 (BRSR item 20) | State both readings. Do not carry "headcount 1,750 to 2,600" as a fact. Flag B06 Q8 as resting on it. |
| F6 | MINOR | Speaker attribution. B05 row 2 credits "ramped up production to about INR590 crores" to NK. The words are analyst Ganeshram's, and NK did not dispute them. Row 21 credits "INR700 crores which was due was completely covered" to MV. That is analyst Garvit Goyal's restatement. MV said "the outstanding creditors have been completely covered", then "Yes". | Q4C p.9; Q4C p.11 | Correct the speakers. Note that the CFO said "creditors" when asked about receivables. |
| F7 | MINOR | I-18 MISSED: in prepared remarks, management volunteered that 100% of the DFPS investment (Rs 30 mn) was provided in FY26. | Q4C p.3 NK | Add to B05 2D or the subsidiary notes. It is small, but it is a second subsidiary write-down in the same year as the Turkey penalty. |
| F8 | MINOR | B05 3D roll-forward compares the order book and inflow with consolidated revenue. The calls do not state the basis of either. On B05's own standalone Q4 FY26 revenue (Rs 534.3 cr), the Q3-to-Q4 gap is about -Rs 4 cr, not +Rs 51 cr (1,845 + 666 - 534.3 = 1,976.7 vs 1,973; my arithmetic). The Q4-to-Q1 gap stays positive. It is at most Rs 131 cr on standalone total income of Rs 630 cr (Q1C p.3; my arithmetic). | Q3C p.3; Q4C p.3; Q1C p.3; B05 3D | Name the revenue basis as a candidate driver. The flag stands in part. |
| F9 | MINOR | B05 2A row 24 says the equity raise was "never pre-signalled". The board meeting was notified to the exchange before the Q1 call, and an analyst asked about the QIP on that call. The Q3 and Q4 calls carried no signal, as B05 says. | Q1C p.15, p.17 NK | Reword: "not signalled on the Q3 or Q4 calls; pre-notified by board notice before the Q1 call". |
| F10 | MINOR | Four minor items recorded but not weighed: the shrinking guidance upside language (I-15); hydro softening and the "abroad" contradiction (I-17); FX about 90% unhedged by choice on a 75-93% export book (I-19); CFO answer quality (I-24). | Q3C p.5, p.12; Q4C p.4-5, p.11; Q1C p.4, p.10 | Carry them as tone notes. Put FX into the margin-bridge sensitivity. |

No CRITICAL finding: the one CRITICAL item (I-1) is CAUGHT.

---

## 5. Credibility grade

B05 grade: B (Good). I concur. Every headline revenue and inflow promise in the window was met or beaten, and the guide was raised at each step. Against that: the large-generator disclosure was deferred across two quarters, capacity and capex numbers drift, margin levers are never decomposed, and the equity raise had no call signal. Moving row 9 from missed to unverified (F4) slightly strengthens B. It does not move the grade.

## 6. Second-order notes for synthesis (inference, labelled)

- [INFERENCE] I-6 and I-9 link. OEMs collect non-refundable buyer advances, while TD cannot change terms "otherwise, we will lose business". If downstream sites slip (I-9), the OEM holds the cash and TD holds the receivable and the inventory. The first sign would show in TD's receivable days and the advance line before it shows in inflow.
- [INFERENCE] I-2, I-7 and I-8 together mean that TD's growth is concentrated in export gas-generator demand from a few OEMs. Domestic demand is shrinking and no major customer has been added. The mix that supports the Section 1B destination multiple cannot be sized from the calls.
- Observation that separates the two readings of I-9 (benign site delay vs OEM inventory build): TD's Q3 FY27 inflow against revenue, together with any OEM statement on deferred generator call-offs.

```yaml
stage: B12b
company: "TDPOWERSYS"
run_date: "2026-11-15"
model: "claude-opus-5-5"
status: complete
independent_flags_found: 25
caught: 18
partially_caught: 6
missed:
  - {severity: "MINOR", item: "DFPS subsidiary: 100% of the investment (Rs 30 mn) provided in FY26, volunteered in Q4 prepared remarks; absent from B05 and B06", anchor: "Q4C p.3, NK"}
pipeline_flags_not_supported: []
promise_delivery_spot_checks: {checked: 5, confirmed: 4, wrong: 1}
credibility_grade_concur: "concur: B fits; every headline revenue and inflow promise beaten, against two-quarter large-generator deferral, drifting capacity numbers and no call signal of the equity raise; reclassifying the US-customer row from missed to unverified does not move the grade"
findings:
  - {id: F1, severity: MAJOR, finding: "B06 Q9 CONTRADICTED (no order disruption from US tariff) is OVERSTATED: its weighting premise that TD sells capital equipment to the end buyer is wrong; TD sells to prime-mover OEMs (the Azad position, no disruption), and TD Q3 FY26 inflow was a record Rs 6.56 bn, +61% YoY, 84% export", anchor: "B06 Q9; AR FY26 p.82 BRSR; Q4C p.8 NK; Q3C p.3 NK", fix: "Reclassify for TD to PARTIALLY VERIFIED (customer-pays corroborated, disruption not shown at TD); keep peer deferral as context; add Q1C p.11 analyst note that FY26 exports were routed via Turkey because of tariff uncertainty"}
  - {id: F2, severity: MAJOR, finding: "Material item partially caught: management moved from '180 degrees reverse' (Q4) to 'there are execution delays on the data centre side' (Q1), after first denying it on the same call; B05 3B records it as delays 'not at TD'. Triveni reports dispatches pushed out for the same reason", anchor: "Q4C p.7; Q1C p.8, p.9 NK; TRITURBINE Q1 FY27 p.7; B05 3B", fix: "Record as tone shift and leading indicator; add tracker kill signal: OEM or customer reports of deferred dispatch or commissioning"}
  - {id: F3, severity: MINOR, finding: "B06 Q1 labels domestic 10-12% growth PARTIALLY VERIFIED though its net read says the latest quarter reverses it; TD domestic inflow share 21% to 7%; Triveni domestic orders -35.4%, decline broad-based; Q1C says 'all segments' buoyant (p.3) and India 'fairly subdued' (p.14)", anchor: "Q3C p.4-5; Q4C p.4; Q1C p.3-4, p.14; TRITURBINE Q1 FY27 p.3, p.6; TRITURBINE Q4 FY26 p.15", fix: "Label CONTRADICTED for the latest quarter, magnitude unanchored; B05 to list the management claim as contradicted by TD's own inflow (segment about 25% of revenue, Q4C p.12)"}
  - {id: F4, severity: MINOR, finding: "B05 2A row 9 (big new US customer) classed missed; neither later call shows non-conversion; Q1C p.10 'no major client additions at the moment' is present-tense", anchor: "Q3C p.7; Q1C p.10; B05 2A row 9", fix: "Reclassify UNVERIFIED (silence); counts 11 delivered, 5 partial, 3 missed; grade unchanged"}
  - {id: F5, severity: MINOR, finding: "B05 carries MV's 'scaling up from 1,750 to 2,600' as headcount fact (1B, 2B, 2E, 3C, 4B item 8) and B06 Q8 partially verifies it; the phrase is ambiguous: 2,600 equals the FY27 revenue guide on the same call; AR shows 1,550 total staff at 31 Mar 2026 (730 employees + 820 workers), which also fits", anchor: "Q1C p.13 MV; Q1C p.4; Q4C p.3; AR FY26 p.82 BRSR item 20", fix: "State both readings; drop headcount 2,600 as a fact; flag B06 Q8 as resting on it"}
  - {id: F6, severity: MINOR, finding: "Speaker attribution: B05 row 2 credits 'about INR590 crores' to NK (analyst Ganeshram's words); row 21 credits 'INR700 crores ... completely covered' to MV (analyst Garvit Goyal's restatement; MV said 'outstanding creditors have been completely covered', then 'Yes')", anchor: "Q4C p.9; Q4C p.11", fix: "Correct speakers; note CFO used 'creditors' for receivables"}
  - {id: F7, severity: MINOR, finding: "Missed volunteered negative: 100% of DFPS subsidiary investment (Rs 30 mn) provided in FY26", anchor: "Q4C p.3 NK", fix: "Add to B05 2D or subsidiary notes beside the Turkey penalty"}
  - {id: F8, severity: MINOR, finding: "B05 3D roll-forward uses consolidated revenue against an order book and inflow of unstated basis; on B05's standalone Q4 FY26 revenue Rs 534.3 cr the Q3-to-Q4 gap is about -Rs 4 cr not +Rs 51 cr (my arithmetic); Q4-to-Q1 gap stays positive, at most Rs 131 cr on standalone total income Rs 630 cr", anchor: "Q3C p.3; Q4C p.3; Q1C p.3; B05 3D", fix: "Name revenue basis as a candidate driver; flag stands in part"}
  - {id: F9, severity: MINOR, finding: "B05 row 24 says the equity raise was never pre-signalled; the board meeting was notified to the exchange before the Q1 call and an analyst asked about the QIP on it", anchor: "Q1C p.15, p.17 NK", fix: "Reword: not signalled on the Q3 or Q4 calls; pre-notified by board notice before the Q1 call"}
  - {id: F10, severity: MINOR, finding: "Recorded but not weighed: guidance upside language shrank to 'small chance' (I-15); hydro softening and 'abroad' vs 'not global' (I-17); FX about 90% unhedged by choice (I-19); CFO answer quality (I-24)", anchor: "Q3C p.5, p.12; Q4C p.4-5, p.11; Q1C p.4, p.10", fix: "Carry as tone notes; FX into margin-bridge sensitivity"}
critical_count: 0
major_count: 2
minor_count: 8
material_found: 9
material_caught: 7
acceptance_rate: 78
coverage_basis: "9 material (1 CRITICAL, 8 MAJOR) of 25 listed; 7 caught, 2 partially caught, 0 missed; 78% counts CAUGHT only (100% if PARTIALLY CAUGHT counts). TDPS 3 of 3 transcripts read in full; peers 3 of 12 in full, 9 by topic search"
```
