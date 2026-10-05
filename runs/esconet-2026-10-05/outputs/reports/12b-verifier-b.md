# STAGE 12, VERIFIER B: CONCALL RED FLAGS. ESCONET (Esconet Technologies Ltd), run 2026-10-05

Model: claude-opus-5-5. Fresh context. Rubric: prompts/12-verifiers-pipeline.md, VERIFIER B section.

## 0. Method, inputs, anchor keys

Order of work. I read both company transcripts in full first, then the filed sources and the 12 peer transcripts (targeted reads on margin, price, inventory, allocation and order book). I opened B05 and B06 only after my independent list was graded.

Anchor keys.
- JUN25 = inputs/concalls/Concall_Jun_2025_Transcript.txt (call 19 Jun 2025, FY25). AUG26 = inputs/concalls/Concall_Aug_2026_Transcript.txt (call 13 Aug 2026, Q1 FY27). "p.N" is the "[page N]" marker in the .txt; "l.N" is the .txt line.
- DECK26 = inputs/presentation/Investor_Presentation_Jun_2026.txt (FY26 meet, 22 Jun 2026, deck only). DECK25 = inputs/presentation/Investor_Presentation_Sep_2025.txt (same content as the NSE-filed copy in inputs/other/2025-09-22).
- Q1BM = inputs/results/2026-08-12 Outcome (Q1 FY27 results, limited review reports, utilisation certificate, press release). FY26PR = announcements/2026-05-28 Press Release. H1PR = announcements/2025-11-17 PR. AR26 = inputs/annual-report/Annual_Report_2026.txt.
- Peers: (PEER, call, p.N, l.N).

Units. Esconet filings in INR Lakhs; calls speak INR Cr (1 Cr = 100 Lakhs). "Derived" marks my arithmetic on two anchored figures.

Self-check note. AOC-1 (AR26 p.69) reports Esconet Singapore in SGD. I first read its turnover as INR and corrected it before use. Tie-out: Singapore PAT SGD 35,163.02 equals INR 25.57 Lakhs in the AR26 consolidation share table (AR26 l.10085), which implies 72.72 INR per SGD. All Singapore FY26 rupee figures below use that implied rate and are marked derived.

## 1. INDEPENDENT RED-FLAG LIST (graded before comparison)

Severity scale: CRITICAL (repeated evasion over 2+ calls, or would change a decision) | MAJOR (thesis-relevant, decision likely survives) | MINOR.

No item met the CRITICAL test. I looked for a repeated evasion across both calls. The 3-to-5-year sizing refusal repeats (m14), but two peers also decline forward guidance (ORIENTTECH Aug 2026 p.7 l.261-262; NETWEB Aug 2026 p.12 l.476), so I grade it MINOR.

### MAJOR items (11)

| ID | Item | Anchors |
|---|---|---|
| M1 | Fluidech guidance missed by about two thirds, then recast as "planned". Jun 2025: FY26 revenue "easily" 15 to 20 Cr and 25 to 30% operating margin. The Fluidech head promised state-government contracts in "10 to 14 months" and "a very steep growth curve". Filed FY26: turnover 538.96 Lakhs, PBT (68.02) Lakhs, which is 27% to 36% of the range (derived). The Jun 2026 deck calls it "a planned ~Rs 0.67 Cr loss". The Aug 2026 call gave no Fluidech figure, and the Fluidech head was not on it. | JUN25 p.6 l.332-335; p.9 l.510-511, l.525; p.10 l.582-589 (Gaurav Gupta); AR26 p.69 AOC-1; DECK26 p.13; AUG26 p.2 l.74-80 (attendees) |
| M2 | ZeaCloud: guidance walkback, a filed-PR contradiction and a self-contradiction inside one call. Jun 2025: +50 to 60%, 8 to 8.5 Cr, and 30 to 40% "bare minimum" for 3 to 4 years. Filed FY26: turnover 534.43 Lakhs, PAT (10.04) Lakhs. The FY26 PR says "healthy operational growth with encouraging EBITDA performance"; the deck says "Healthy operations. Encouraging EBITDA". On the Aug 2026 call the MD says "flat revenue growth... could not onboard any much new customers". Minutes later he challenges the analyst: "how do you have that information that we are not able to onboard enterprise customers?... Come down to my office". He refused utilisation and guided FY27 flat. | JUN25 p.6 l.319; p.9 l.525-527; AR26 p.69; FY26PR p.7 l.332-333; DECK26 p.12; AUG26 p.18 l.981-999, l.1004-1015 |
| M3 | FY26 margin promise missed, explained three different ways. Jun 2025: "in the current year, margins will definitely improve". FY26 consolidated EBITDA margin was 3.46% vs 5.67% and PAT fell 23.04%. The H1 PR blamed ONGC cost and revenue timing with "reversal expected in H2". The FY26 PR blamed opex, employee cost and investment. The deck blamed component inflation (about Rs 7 Cr of gross profit). The bottom-line promise moved from FY26 to FY27. In Aug 2026 the MD said "we had missed the bus on the bottom lines". | JUN25 p.7 l.400-402; p.6 l.307-312; FY26PR p.1 l.73-81, p.2 l.107-109; H1PR p.2 l.54-58; DECK26 p.8; AUG26 p.14 l.747-751 |
| M4 | The Q1 FY27 margin step-up is partly price and inventory driven, unquantified, and still called "sustainable". MD: "hardware price volatility has played some role... I may not be able to quantify... I would not deny that fact"; inventory "contributed to some extent to our margins"; the trend runs through FY27 and maybe FY28 "per industry analyst experts". Standalone gross margin was 29.2% in Q1 vs 13.7% in FY26 (derived). Same-day peer contrast: Orient reports "greater stability in pricing" and cost pass-through, and RPTECH says the price-rise "speed should be half" in Q2. | AUG26 p.10 l.544-559; p.12 l.665-668; Q1BM p.4 (standalone); AR26 p.103; ORIENTTECH Aug 2026 p.4 l.144-150; RPTECH Aug 2026 p.11 l.95 |
| M5 | Cash conversion dodged, and filed claims contradict it. CFO: "In numbers, it cannot tell here only, but it is on positive side", then "5% of revenue". MD: cash goes into inventories that "keep rising". No Q1 balance sheet was filed. FY26 consolidated CFO was (882.50) Lakhs and consolidated inventory went from 1,894.21 to 5,149.87 Lakhs (+171.9%, derived). Both the FY26 PR and the Q1 PR carry identical text: "Controlled working capital management... Strengthening operational cash flows". The deck says inventory "supports signed orders", but the MD guesses the order book at "20-25 crores, not more than that", against 51.50 Cr of consolidated stock at 31 Mar 2026. | AUG26 p.12 l.642-668; p.15 l.821-829; AR26 p.132 (BS), p.134 (CFS); FY26PR p.4 l.204-208; Q1BM p.16 l.686-688; DECK26 p.9 |
| M6 | Singapore trading made 46% of Q1 consolidated revenue at about zero margin and was not explained on the call. CFO: "Revenue from Singapore is approximately 53 crores". MD: "that is what he has guessed... correct figure". No customer, product or margin detail was given. The limited review report gives Singapore Q1 revenue 5,332.02 Lakhs (45.8% of 11,632.69, derived), net profit 29.67 Lakhs (0.56%) and total assets 67.09 Lakhs. FY26 Singapore turnover was SGD 67,46,372, about 4,906 Lakhs (derived), or 13.8% of FY26 consolidated revenue. Subsidiaries supplied 41.4% of FY26 consolidated revenue growth (derived). Jun 2025: "not exporting any product from India... 90-95% of our business is still happening in India". | AUG26 p.15 l.834-841; Q1BM p.10 l.407-415; AR26 p.69; AR26 l.10085; JUN25 p.6 l.360-361; p.3 l.159-163; DECK26 p.14 |
| M7 | Segment disclosure was withdrawn as performance weakened. Jun 2025 gave HexaData at "approximately around 35 percent", segment gross margins (SI 7 to 8%, HexaData 10 to 15%) and ZeaCloud and Fluidech revenue. Aug 2026 refused the HexaData vs non-HexaData split ("we don't have those numbers"), the AI/GPU order mix and ZeaCloud utilisation. Yet the MD credits margin expansion "mostly" to HexaData. | JUN25 p.9 l.520-525; p.12 l.727-728; AUG26 p.14 l.790-793; p.15 l.802-808; p.18 l.1004-1005, l.1026-1029 |
| M8 | Walkback from filed targets. The NSE-filed Sep 2025 deck states "Current order book in pipeline Rs 100 Cr+" and "A Vision to build a Rs 500 Cr+ company". Aug 2026: "whether it 500 crores happens or not, I should not be commenting"; the 100 Cr "may not be anytime soon. It may be probably sometime in the previous year"; order book "20-25 crores". FY27 revenue "may not be very different from what we did previous year", against the Jun 2026 deck's "we see good growth across all four verticals this year". | DECK25 p.19; AUG26 p.14 l.747-752; p.15 l.828-829; p.16 l.858-859, l.885-891; DECK26 p.17 |
| M9 | The NVIDIA "privileged allocation" moat claim is unsupported. Deck: Elite gives "privileged allocation of scarce GPUs... A structural moat: privileged access to constrained supply when others cannot procure". The company's own NSE intimation describes Elite as "the highest tier... within the Solution Provider category". It lists benefits as "technical enablement, priority support, and expanded go-to-market collaboration". It expects no "immediate material financial impact". It makes no allocation claim. MD on Aug 2026: "We buy NVIDIA hardware from the NVIDIA channel". Netweb says its NVIDIA OEM tier is held by "less than 10" firms worldwide and that it is "the only company" in the region with it. RPTECH, a distributor, reports "good allocation". [INFERENCE] Allocation sits with OEM partners and distributors; Esconet buys downstream of them. | DECK26 p.11, p.15; announcements/2026-04-29 NVIDIA l.36-50; AUG26 p.16 l.863-869; NETWEB Nov 2025 p.8 l.332-340; RPTECH Aug 2026 p.9 l.87 |
| M10 | The governance overhang went unmentioned on a call framed around governance. The independent director said governance is "of the highest levels" and answered a strategy question for management. AR26 records Rs 12.00 Lakhs of consultancy fees to Manoj Chugh Advisory LLP, where he is a partner. He also cites a "long association with this firm". Not raised by management or asked: (a) the s.131(1A) income tax summons on the IPO, pre-IPO placements, share transactions and use of IPO proceeds; (b) the NSE-directed correction of FY26 EPS in XBRL, 3 weeks before the call; (c) the lapse of 2,13,600 warrants. | AUG26 p.3 l.129, l.145-151; p.13 l.688-735; AR26 l.9828-9832; announcements/2026-02-28 NSE_Intimation_ITD Annexure A item 4; announcements/2026-07-27 Revised_Clari l.18-41; announcements/2026-04-29 Forfiture |
| M11 | Q1 other income matches the warrant forfeiture closely, and the CFO called total income core. Standalone Q1 other income was 190.04 Lakhs, against 289.30 Lakhs for all of FY26. The 184.23 Lakhs upfront warrant money was forfeited on 25 Apr 2026, inside Q1, and sat in shareholders' funds at 31 Mar 2026. CFO: total income "was substantially driven by core operating activity". The Q1 notes describe other income as interest, PPE gain and miscellaneous. Where the forfeiture was booked is NOT FOUND. [INFERENCE, unverified] If it went through P&L, it is 19.7% of Q1 standalone PBT of 935.67 Lakhs, and it sits inside the 15.39% headline EBITDA margin. | Q1BM p.4 l.146; p.8 l.336-337; AR26 p.102 l.6748; announcements/2026-04-29 Forfiture l.41-49; AUG26 p.6 l.334-337; Q1BM p.14 l.565, l.600-601 |

### MINOR items (14)

| ID | Item | Anchors |
|---|---|---|
| m1 | The CS blocked the YoY growth question on 116 Cr ("we cannot actually compare"). Standalone Q1 revenue is 18.0% below the FY26 quarterly average (derived). | AUG26 p.11 l.575-586; Q1BM p.4; AR26 p.103 |
| m2 | "We raised... 32.69 crores" included 552.69 Lakhs of warrant money that never arrived; the issue was revised to 2,716.53 Lakhs. | JUN25 p.3 l.111, l.163-164; Q1BM p.12-13 l.482-491 |
| m3 | Volunteered: government revenue "has been lower" this year, from 40 to 45% last year. | AUG26 p.17 l.924-930 |
| m4 | MeitY timeline drifting: "still a little far away" (Jun 2025), then FY27 (deck), then ISO by September, apply, wait 3 to 4 months (Aug 2026). | JUN25 p.4 l.231; DECK26 p.12; AUG26 p.14 l.771-777 |
| m5 | Silent drops: Cato "significant numbers in this current year"; South India "significant inroads within this year"; the Scality product line. | JUN25 p.3 l.157-159; p.4 l.196-198 |
| m6 | Fluidech acquisition date is inconsistent. Aug 2026: "acquired at the start of financial year 24-25". AOC-1: 16 Apr 2025. Jun 2025: "last year". | AUG26 p.9 l.510-511; AR26 p.69; JUN25 p.2 l.99 |
| m7 | Defensive tone in 2026 vs an open tone in 2025: "Come down to my office"; "you have a misunderstanding"; "atom bomb"; call cut short for "another meeting". | AUG26 p.18 l.1013-1014; p.19 l.1037, l.1062-1063; p.15 l.846-848 |
| m8 | MD unsure whether his own HPC platform v1 has shipped. | AUG26 p.17 l.952-956; JUN25 p.4 l.216-218 |
| m9 | R&D accounting signal. CFO: on the Ind AS move "after 2-3 years... we might probably then have to be capitalized". The AGM 2025 speech said "Investing significantly in research and development"; the call says under 2% of revenue. | AUG26 p.11 l.609-614; p.12 l.631-640; announcements/2025-09-12 AGM l.306 |
| m10 | Leadership change unexplained. The Sep 2025 deck names "SIVAMANI, Chief Executive Officer". AR26 lists only the CFO and CS as KMP, and no cessation filing is in the corpus (NOT FOUND). A CRO was appointed 29 Jul 2026: Amit Gupta, earlier "Director in Subsidiary". | DECK25 p.5; AR26 l.3056-3060, l.9826; announcements/2026-07-29 CRO |
| m11 | Volunteered: Fluidech ran business "under a different entity also which has been wound up". | JUN25 p.6 l.332-334 |
| m12 | Volunteered: would take a 100 Cr deal at 1% gross margin; "similar kind of deals" in the FY26 pipeline. | JUN25 p.7 l.409-423 |
| m13 | Peer contradiction on order books. Esconet: "we do not have an order book model". Orient (SI, same day) discloses 375.43 Cr; Netweb discloses an order book despite an 8-to-20 week cycle. | AUG26 p.15 l.821-827; ORIENTTECH Aug 2026 p.5 l.171-174; NETWEB Aug 2026 p.11 l.461-466 |
| m14 | 3-to-5-year sizing refused on both calls ("not done that math"; "would not want to comment"). Peers also decline forward guidance. | JUN25 p.8 l.455-456; AUG26 p.15 l.811-816, l.846-848 |

Totals: 25 listed; 11 MAJOR, 14 MINOR, 0 CRITICAL.

## 2. COMPARISON AGAINST THE PIPELINE (B05, B06)

| ID | Sev | Verdict | Where the pipeline has it / what is missing |
|---|---|---|---|
| M1 | MAJOR | CAUGHT | B05 promise rows 3-4 MISSED; excuse table "Deflection; silence on the call"; dropped triggers. Fluidech head's absence not noted (cosmetic). |
| M2 | MAJOR | CAUGHT | B05 promise row 2; Consistency rated 2 ("healthy growth" in PR vs "no expansion" on call); 3C Ashish exchange; defensiveness. |
| M3 | MAJOR | CAUGHT | B05 promise row 1 and row 13; excuse pattern external-blame-heavy. The three-way shift in explanation is listed but not called inconsistent (no finding). |
| M4 | MAJOR | CAUGHT | B05 HIGH flag and FLAG-MARGIN-BASIS; B06 FLAG-PEER-SPLIT-MARGIN-MECHANISM and cross-peer hypothesis. |
| M5 | MAJOR | PARTIALLY CAUGHT | B05 FLAG-CASH at MEDIUM. Not flagged: the identical "strengthening operational cash flows" text in both PRs against a negative FY26 consolidated CFO; the deck's "supports signed orders" against a 20 to 25 Cr order book. B06 then calls the inventory build "small" (see Section 3). |
| M6 | MAJOR | PARTIALLY CAUGHT (misclassified) | B05 lists Singapore as trigger #8 "committed" and "Strengthening", and leaves the 53 Cr period NOT FOUND. The Q1 limited review report (Q1BM p.10) gives Q1 Singapore revenue 5,332.02 Lakhs. B05 analyst_note derives a 0.7% margin on the rest of the group, so the economics were seen but not raised as a revenue-quality flag. |
| M7 | MAJOR | CAUGHT | B05 MEDIUM flag; repeated-question tracker "answer changed between quarters". |
| M8 | MAJOR | PARTIALLY CAUGHT | B05 FLAG-GUIDANCE-INCONSISTENCY covers FY27 vs Q1 run-rate. B05 2D item 8 calls "500 crores" garbled and unresolved. The filed source (DECK25 p.19: Rs 500 Cr+ vision, Rs 100 Cr+ pipeline) is missed. |
| M9 | MAJOR | MISSED | B05 trigger #2 rests on "NVIDIA Elite allocation" at conviction M. B05 1C notes "scarce supply moat... Unchanged claim". B06 Q7 is VERIFIED. No stage set the deck claim against the company's own Reg 30 text or the MD's "we buy... from the NVIDIA channel". |
| M10 | MAJOR | CAUGHT | B05 HIGH flag (summons, warrants), MEDIUM flag (ID's LLP fee), LOW flag (XBRL). |
| M11 | MAJOR | PARTIALLY CAUGHT | B05 input gap (stage3: forfeiture accounting NOT FOUND) and analyst-note reading B (other income). Not raised as a flag. The CFO's "core operating activity" framing is not challenged. |
| m1 | MINOR | PARTIALLY CAUGHT | Substance in FLAG-GUIDANCE-INCONSISTENCY (standalone 18% below FY26 run-rate); the CS deflection itself not noted. |
| m2 | MINOR | CAUGHT | B05 side check (a). |
| m3 | MINOR | CAUGHT | B05 1C, 3D. |
| m4 | MINOR | CAUGHT | B05 timeline_slippages. |
| m5 | MINOR | CAUGHT | B05 dropped_triggers. |
| m6 | MINOR | MISSED | Not in B05 or B06. |
| m7 | MINOR | CAUGHT | B05 2C defensiveness 3. |
| m8 | MINOR | CAUGHT | B05 promise row 9. |
| m9 | MINOR | MISSED | B05 records R&D under 2% and expensed; the capitalisation signal and the AGM contrast are absent. |
| m10 | MINOR | MISSED | Not in B05 or B06 (may sit in B08, not in my inputs). |
| m11 | MINOR | PARTIALLY CAUGHT | B05 2D item 4 cites "former-director seller history (B03)"; the wound-up parallel entity is not named. |
| m12 | MINOR | CAUGHT | B05 3D pricing; 2B. |
| m13 | MINOR | CAUGHT | B06 FLAG-ESCONET-DISCLOSURE-GAP-VS-PEERS. |
| m14 | MINOR | CAUGHT | B05 repeated_evasions row 3. |

Counts: CAUGHT 15, PARTIALLY CAUGHT 6, MISSED 4 (1 MAJOR, 3 MINOR).
Material: 11 found; 6 caught fully, 4 partially, 1 missed.

## 3. PIPELINE FLAGS I DID NOT FIND INDEPENDENTLY, AND PIPELINE CLAIMS TESTED

| Pipeline item | Assessment | Basis |
|---|---|---|
| B05 FLAG-STATEMENT-CONFLICT: "no stake sale" in ZeaCloud vs the 9 Feb 2026 Reg 30 | SUPPORTED (as an omission) | The Reg 30 describes fresh-equity dilution talks via Merino Consulting, not a sale (announcements/2026-02-09 l.30-41). The MD said he "could not get" the question and "we do not intend to sell any stake" (AUG26 p.14 l.777-780). That is narrowly true but gives no update on a disclosed matter. "Conflict" overstates the wording; the signal is real. |
| B05 MEDIUM: independent director's LLP fee 12.00 Lakhs | SUPPORTED | AR26 l.9828-9832: "Manoj Chugh Advisory LLP... Consultancy Fees 12.00". |
| B05 repeated_evasions: margin quantum "deflected every time" | OVERSTATED (Jun 2025 leg) | Jun 2025 gave a direction and benchmark (JUN25 p.7 l.400-402) and segment margins (p.9 l.504-511; p.12 l.727-728). Only Aug 2026 refused to quantify. |
| B05 repeated_evasions: ZeaCloud capital intensity "deflected every time" | OVERSTATED (Jun 2025 leg) | Jun 2025 gave a range: 10 Cr may earn 2 or 5 Cr a year depending on asset life (JUN25 p.11 l.628-633). Aug 2026 refused utilisation (p.18 l.1004-1005). |
| B06 analyst_note and FLAG-PEER-SPLIT net read: "Esconet's own inventory build is small (518.50 Lakhs), which weakens the stock-gain reading" | OVERSTATED (not supported on the filed record) | 518.50 is the Q1 standalone change only. FY26 consolidated inventory rose 3,255.66 Lakhs to 5,149.87 (AR26 p.134 CFS; p.132 BS); standalone rose 826.72 in FY26 (AR26 p.103). The MD says stock "keep rising" across halves and "contributed to some extent to our margins" (AUG26 p.12 l.665-668). Reading B (stock gain) deserves equal standing with reading C (repricing reset). Both readings are non-structural, so the decision likely survives. |
| B06 verified Q7: "partner-status vendors keep GPU and component allocation" | OVERSTATED as support for Esconet | B06 itself says this "does not prove Esconet's tier of access". The YAML entry drops that caveat, and B05 trigger #2 leans on it. Contra: Esconet's Reg 30 (no allocation benefit, Solution Provider category) and AUG26 p.16 l.867 (buys through the NVIDIA channel). Folded into finding F1. |
| B06 quotes used for the margin-mechanism verdict | VERIFIED | NETWEB Aug 2026 l.311-312 ("There is no question of some memory pricing... we have the pricing power"); NETWEB Nov 2025 l.280, l.752-755 ("150 to 200 basis points lower at PBT level"). |

No pipeline flag is NOT SUPPORTED outright. The analysis did not invent a signal. Two B06 items and two B05 tracker rows overstate.

## 4. PROMISE-DELIVERY SPOT CHECKS (B05 Section 2A)

| B05 row | Promise in the earlier call? | Outcome in later call or filing? | Verdict |
|---|---|---|---|
| 1. FY26 margins "definitely improve" | Yes: JUN25 p.7 l.400-402 | FY26 consolidated EBITDA 3.46% vs 5.67% (FY26PR p.1 l.76); gross 13.19% vs 15.23% (derived from AR26 p.133, matches B05) | CONFIRMED (MISSED) |
| 2. ZeaCloud +50 to 60% | Yes: JUN25 p.6 l.319; p.9 l.525 | AOC-1 534.43 Lakhs, PAT (10.04) (AR26 p.69); MD admits flat (AUG26 p.18 l.985) | CONFIRMED (MISSED) |
| 3. Fluidech 15 to 20 Cr | Yes: JUN25 p.6 l.334-335 | AOC-1 538.96 Lakhs (AR26 p.69); no Fluidech number on AUG26 | CONFIRMED (MISSED) |
| 5. Employee cost +30% | Yes: JUN25 p.9 l.537-538 | Missed on both bases. B05's +67.5% compares FY26 consolidated (including Fluidech, acquired 16 Apr 2025) with FY25 consolidated without it. Standalone 795.39 vs 557.04 Lakhs = +42.8% (AR26 p.103, derived) | CONFIRMED direction; basis note (F8) |
| 8. FY26 same growth; bottom line from FY27 | Ambiguous: JUN25 p.6 l.307-312 says "next two years instead of top lines... bottom lines", and also "this year we'll continue to do the same". The MD's own 2026 retelling matches B05's reading (AUG26 p.14 l.747-751) | Total income +53.41%, PAT -23.04% (FY26PR p.1) | CONFIRMED with ambiguity note |
| 12. FY27 margin to exceed FY24 "by far" | Yes: JUN25 p.7 l.401-402 | B05 cites standalone 29.2% gross. The 2025 discussion was consolidated (FY25 15%, FY24 about 20%, JUN25 p.7 l.405-406). Q1 FY27 consolidated gross is 16.6% (derived from Q1BM p.7): progress on FY25, not yet above FY24 | CONFIRMED (PARTIAL holds); basis note (F9) |

Checked 6, confirmed 6, wrong 0. Two rows carry a basis caveat. One row carries a wording ambiguity.

## 5. CREDIBILITY GRADE

B05 grade: C (lower edge). I would grade lower, at the C/D boundary. Quantified forecasts hit 0 of 4. At least five PR or deck claims are contradicted by filings or by the MD's own words on the call:
1. ZeaCloud "healthy operational growth" (FY26PR p.7).
2. Fluidech "planned" loss (DECK26 p.13).
3. "Strengthening operational cash flows" (FY26PR p.4; Q1BM p.16).
4. "Privileged allocation of scarce GPUs" (DECK26 p.11).
5. Inventory "supports signed orders" (DECK26 p.9).

Candour under questioning on the call is real. But the filed channel overstates more than B05 counted.

## 6. HANDOFF NOTES (not scored; numerical domain belongs to Verifier A and the forensic stages)

1. FY26 consolidated P&L change in inventories is (826.72) Lakhs, identical to standalone (AR26 p.133 vs p.103). Yet consolidated balance-sheet inventory rose 3,255.66 Lakhs (AR26 p.134). The non-parent stock at 31 Mar 2026 is 2,428.94 Lakhs (5,149.87 less 2,720.93, derived). [INFERENCE] That matches Singapore's AOC-1 total assets of SGD 33,89,867, about 2,465 Lakhs (derived). Singapore total assets were 67.09 Lakhs by 30 Jun 2026 (Q1BM p.10). Q1 consolidated change in inventories again equals standalone, at (518.50). About Rs 24 Cr of subsidiary stock moved over two periods without a P&L inventory line.
2. Singapore total assets carry three filed values: SGD 33,89,867 (AOC-1), 553.64 Lakhs (auditor, per B05 input gap) and 67.09 Lakhs (Q1 limited review report).
3. Location of the 184.23 Lakhs forfeiture booking (capital reserve or other income): NOT FOUND in the Q1 filing. See M11.

## 7. CONSOLIDATED FINDINGS

| # | Sev | Location | Issue | Evidence | Action |
|---|---|---|---|---|---|
| F1 | MAJOR | B05 trigger #2, 1C; B06 verified Q7 | NVIDIA allocation-moat premise accepted; MISSED red flag | Reg 30 29 Apr 2026 l.36-50 (Solution Provider tier, no allocation claim, no material impact); AUG26 p.16 l.867; NETWEB Nov 2025 p.8 l.332-340 | Drop the allocation premise from trigger #2; treat Elite as a reseller-tier credential until a filed allocation benefit appears |
| F2 | MAJOR | B05 trigger #8, 1C, FLAG-GUIDANCE-INCONSISTENCY | Singapore classed as a growth trigger; period left NOT FOUND though filed | Q1BM p.10 l.407-415 (5,332.02 Lakhs Q1, 0.56% net, 67.09 Lakhs assets); AR26 p.69 (SGD 67,46,372, about 4,906 Lakhs derived) | Reclassify as a revenue-quality flag; show standalone and ex-Singapore growth beside consolidated |
| F3 | MAJOR | B06 analyst_note, FLAG-PEER-SPLIT net read | Inventory build called "small" from the Q1 standalone figure alone | AR26 p.132, p.134 (+3,255.66 Lakhs consolidated FY26); AUG26 p.12 l.665-668 | Restore reading B to equal standing with C |
| F4 | MINOR | B05 FLAG-CASH | Filed cash and inventory claims contradicted, not flagged | FY26PR p.4 l.204-208; Q1BM p.16 l.686-688; AR26 p.134 CFO (882.50); DECK26 p.9 vs AUG26 p.15 l.828-829 | Add to FLAG-CASH; cash conversion stays INDETERMINATE |
| F5 | MINOR | B05 2D item 8; 1B order-book row | Rs 500 Cr+ vision and Rs 100 Cr+ pipeline source missed | DECK25 p.19; AUG26 p.14 l.747-752; p.16 l.858-859 | Record as a walkback against filed targets |
| F6 | MINOR | B05 FLAG-MARGIN-BASIS; stage3 gap | Other income 190.04 vs forfeiture 184.23 in the same quarter not raised as a flag | Q1BM p.4; Forfeiture filing l.41-49; AUG26 p.6 l.334-337 | Name the flag; separating observation: H1 FY27 notes or FY27 AR showing capital reserve vs other income |
| F7 | MINOR | B05 repeated_evasions rows 1 and 4 | "Deflected every time" overstated for Jun 2025 | JUN25 p.7 l.400-402; p.9 l.504-511; p.11 l.628-633 | Reclassify as "answered 2025, withdrawn 2026" |
| F8 | MINOR | B05 promise row 5 | Employee-cost miss on a mixed basis | AR26 p.103 (795.39 vs 557.04, +42.8% standalone) | Show standalone basis |
| F9 | MINOR | B05 promise row 12 | Standalone gross margin used against a consolidated promise | Q1BM p.7 (consolidated gross 16.6% derived); JUN25 p.7 l.405-406 | State consolidated basis |
| F10 | MINOR | B05/B06 (missed m6) | Fluidech acquisition date misstated on the call | AUG26 p.9 l.510-511 vs AR26 p.69 (16 Apr 2025) | Note in management-accuracy record |
| F11 | MINOR | B05/B06 (missed m9) | Future R&D capitalisation signalled | AUG26 p.12 l.631-640 | Add a tripwire: capitalised development cost after any Ind AS move |
| F12 | MINOR | B05/B06 (missed m10) | CEO named in Sep 2025 deck absent from AR26 KMP; no cessation filing in corpus | DECK25 p.5; AR26 l.3056-3060; CRO filing 29 Jul 2026 | Ask in the Halt 1 extraction annex; NOT FOUND until then |

Counts: CRITICAL 0, MAJOR 3, MINOR 9.

## 8. COVERAGE STATEMENT

- Company transcripts: 2 of 2 read in full (no third exists).
- Peer transcripts: 12 of 12 present. Full reads: ORIENTTECH Aug 2026 and RPTECH Aug 2026. Targeted reads: NETWEB Aug 2026 p.10-13, NETWEB Nov 2025 p.8-9, RPTECH Feb 2026 p.5-7, p.10-11, p.16. The other 7 peer files were checked by text search only, for the price, inventory, allocation, Elite, order-book and Esconet terms.
- Filed cross-checks: Q1 FY27 board outcome, FY26 PR, H1 FY26 PR, FY26 and Sep 2025 decks, AR26 (AOC-1, AOC-2, standalone and consolidated statements, KMP, RPT note), and 8 Reg 30 filings (ITD x2, NVIDIA, forfeiture, XBRL clarification, ZeaCloud, CRO, AGM x2).
- Material count: 11 MAJOR of 25 listed. 6 fully caught, 4 partially caught, 1 missed. The acceptance rate counts a partial catch as "had" (found, under-weighted). On full catches only, the rate would be 54.5% (6 of 11). Both are stated so the orchestrator can apply its rule.

```yaml
stage: B12b
company: "ESCONET"
run_date: "2026-10-05"
model: "claude-opus-5-5"
status: complete
independent_flags_found: 25
caught: 15
partially_caught: 6
missed:
  - {severity: "MAJOR", item: "NVIDIA 'privileged allocation of scarce GPUs / structural moat' (deck) unsupported by the company's own Reg 30 (Solution Provider Elite tier; benefits are enablement, support, GTM; no material financial impact) and contradicted by the MD buying 'from the NVIDIA channel'; Netweb claims the regional OEM tier", anchor: "DECK26 p.11, p.15; Reg 30 29 Apr 2026 l.36-50; AUG26 p.16 l.867 (MD); NETWEB Nov 2025 p.8 l.332-340"}
  - {severity: "MINOR", item: "Fluidech acquisition date stated as start of FY24-25 on the call vs AOC-1 16 Apr 2025", anchor: "AUG26 p.9 l.510-511 (MD); AR26 p.69"}
  - {severity: "MINOR", item: "CFO signals future capitalisation of R&D on Ind AS move; AGM 2025 'investing significantly in R&D' vs under 2% now", anchor: "AUG26 p.12 l.631-640 (CFO, MD); p.11 l.612; AGM 12 Sep 2025 l.306"}
  - {severity: "MINOR", item: "CEO named in Sep 2025 deck absent from AR26 KMP list; no cessation filing in corpus (NOT FOUND); CRO appointed Jul 2026", anchor: "DECK25 p.5; AR26 l.3056-3060; Reg 30 29 Jul 2026"}
pipeline_flags_not_supported:
  - "OVERSTATED: B06 analyst_note / FLAG-PEER-SPLIT net read 'Esconet's own inventory build is small (518.50 Lakhs)'; FY26 consolidated inventory rose 3,255.66 Lakhs to 5,149.87 (AR26 p.132, p.134); MD says stock kept rising and helped margins (AUG26 p.12 l.665-668)"
  - "OVERSTATED: B06 verified Q7 used as support for Esconet GPU allocation; own Reg 30 makes no allocation claim and MD buys through the NVIDIA channel (AUG26 p.16 l.867)"
  - "OVERSTATED: B05 repeated_evasions rows 1 and 4 'deflected every time'; Jun 2025 answered with direction, segment margins and a capital-to-revenue range (JUN25 p.7 l.400-402; p.9 l.504-511; p.11 l.628-633); only Aug 2026 refused"
promise_delivery_spot_checks: {checked: 6, confirmed: 6, wrong: 0}
credibility_grade_concur: "lower (C/D boundary): 0 of 4 quantified forecasts hit and at least five PR or deck claims contradicted by filings or the MD's own call words (ZeaCloud healthy growth, Fluidech planned loss, strengthening cash flows, privileged GPU allocation, inventory backed by signed orders)"
findings:
  - {severity: "MAJOR", location: "B05 trigger #2 and 1C; B06 verified Q7", issue: "NVIDIA allocation-moat premise accepted; red flag missed", evidence: "Reg 30 29 Apr 2026 l.36-50; AUG26 p.16 l.867; NETWEB Nov 2025 p.8 l.332-340", action: "drop allocation premise from trigger #2 until a filed allocation benefit appears"}
  - {severity: "MAJOR", location: "B05 trigger #8, 1C, FLAG-GUIDANCE-INCONSISTENCY", issue: "Singapore classed as a committed growth trigger; 53 Cr period left NOT FOUND though filed", evidence: "Q1BM p.10 l.407-415: Q1 revenue 5,332.02 Lakhs (45.8% of consolidated, derived), net profit 29.67 (0.56%), total assets 67.09; AR26 p.69 FY26 turnover SGD 67,46,372 (about 4,906 Lakhs derived at 72.72)", action: "reclassify as revenue-quality flag; show standalone and ex-Singapore growth"}
  - {severity: "MAJOR", location: "B06 analyst_note and FLAG-PEER-SPLIT-MARGIN-MECHANISM net read", issue: "inventory build called small from the Q1 standalone change alone; weakens stock-gain reading on a wrong input", evidence: "AR26 p.132, p.134 (consolidated inventory 1,894.21 to 5,149.87 Lakhs, +3,255.66); AUG26 p.12 l.665-668", action: "restore reading B to equal standing with reading C"}
  - {severity: "MINOR", location: "B05 FLAG-CASH", issue: "identical 'strengthening operational cash flows' PR text and deck 'inventory supports signed orders' contradicted by filings, not flagged", evidence: "FY26PR p.4 l.204-208; Q1BM p.16 l.686-688; AR26 p.134 consolidated CFO (882.50) Lakhs; DECK26 p.9 vs AUG26 p.15 l.828-829", action: "add to FLAG-CASH; cash conversion stays INDETERMINATE"}
  - {severity: "MINOR", location: "B05 2D item 8; 1B order-book row", issue: "Rs 500 Cr+ vision and Rs 100 Cr+ pipeline source missed; walkback not recorded", evidence: "DECK25 p.19; AUG26 p.14 l.747-752; p.16 l.858-859", action: "record as walkback against filed targets"}
  - {severity: "MINOR", location: "B05 FLAG-MARGIN-BASIS; stage3 input gap", issue: "Q1 other income 190.04 Lakhs vs 184.23 Lakhs forfeiture in same quarter not raised as a flag; CFO framed income as core", evidence: "Q1BM p.4 l.146; Reg 30 29 Apr 2026 forfeiture l.41-49; AUG26 p.6 l.334-337", action: "name the flag; verify booking in H1 FY27 notes or FY27 AR"}
  - {severity: "MINOR", location: "B05 repeated_evasions rows 1 and 4", issue: "'deflected every time' overstated for Jun 2025 leg", evidence: "JUN25 p.7 l.400-402; p.9 l.504-511; p.11 l.628-633", action: "reclassify as answered 2025, withdrawn 2026"}
  - {severity: "MINOR", location: "B05 promise row 5", issue: "employee-cost miss computed on mixed basis (FY26 consolidated includes Fluidech, FY25 does not)", evidence: "AR26 p.103 standalone 795.39 vs 557.04 Lakhs, +42.8% derived", action: "show standalone basis; direction MISSED stands"}
  - {severity: "MINOR", location: "B05 promise row 12", issue: "standalone 29.2% gross used against a consolidated margin promise", evidence: "Q1BM p.7 consolidated gross 16.6% derived; JUN25 p.7 l.405-406 (FY24 about 20%)", action: "state consolidated basis; PARTIAL stands"}
  - {severity: "MINOR", location: "B05/B06, not covered", issue: "Fluidech acquisition date misstated on the call", evidence: "AUG26 p.9 l.510-511 vs AR26 p.69 (16 Apr 2025)", action: "note in management-accuracy record"}
  - {severity: "MINOR", location: "B05/B06, not covered", issue: "future R&D capitalisation signalled by CFO", evidence: "AUG26 p.12 l.631-640", action: "add tripwire on capitalised development cost after Ind AS move"}
  - {severity: "MINOR", location: "B05/B06, not covered", issue: "CEO in Sep 2025 deck absent from AR26 KMP; no cessation filing in corpus", evidence: "DECK25 p.5; AR26 l.3056-3060; Reg 30 29 Jul 2026 CRO", action: "ask in Halt 1 extraction annex; NOT FOUND until answered"}
critical_count: 0
major_count: 3
minor_count: 9
material_found: 11
material_caught: 10
acceptance_rate: 90.9
coverage_basis: "11 material (0 CRITICAL, 11 MAJOR) of 25 listed; pipeline had 10 (6 fully caught, 4 partially caught, counted as had); 1 missed (NVIDIA allocation claim). Full-catch-only rate would be 54.5% (6 of 11). 2 of 2 company transcripts read in full; 12 of 12 peer files present, 5 read in full or in targeted sections, 7 by text search."
```
