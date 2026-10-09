# Stage 12, Verifier B: Concall Red Flags. Supreme Power Equipment Ltd (SUPREMEPWR). Run date 2026-10-06

Model: claude-opus-5-5. Scope: VERIFIER B section of prompts/12-verifiers-pipeline.md. Phase 1.

## Inputs

| Input | Path |
|---|---|
| Company transcript, Q3 FY26, call 11-Feb-2026 (code FEB) | runs/supremepwr-2026-10-06/inputs/concalls/Concall_Feb_2026_Transcript.txt |
| Company transcript, H2 FY26, call 02-Jun-2026 (code JUN) | runs/supremepwr-2026-10-06/inputs/concalls/Concall_Jun_2026_Transcript.txt |
| Company transcript, Q1 FY27, call 17-Aug-2026 (code AUG) | runs/supremepwr-2026-10-06/inputs/concalls/Concall_Aug_2026_Transcript.txt |
| Shilchar 531201: Q4 FY25 22-Apr-2025 (SHIL-APR25), Q2 FY26 18-Oct-2025 (SHIL-OCT25), Q4 FY26 05-May-2026 (SHIL-MAY26), Q1 FY27 14-Aug-2026 (SHIL-AUG26) | runs/supremepwr-2026-10-06/inputs/peer-concalls/531201-Concall_*.txt |
| Danish Power: H1 FY26 08-Nov-2025 (DAN-NOV25), H2 FY26 11-May-2026 (DAN-MAY26) | runs/supremepwr-2026-10-06/inputs/peer-concalls/DANISH-Concall_*.txt |
| B05 report | runs/supremepwr-2026-10-06/outputs/reports/05-concall.md |
| B06 report | runs/supremepwr-2026-10-06/outputs/reports/06-peers.md |

Method. I read all nine transcripts first. I drafted the independent list in Part 1 from the transcripts alone. I opened B05 and B06 only after that list was fixed. I read no other stage report and no other verifier output. No live web was used.

Anchor convention. "p.N" is the file "[page N]" marker, the convention B05 and B06 state. On the company calls the printed page is N-1. Speakers: CMD = Mr Vee Rajmohan, the only management speaker on all three company calls. Analysts are named. DERIVED marks my own arithmetic from transcript figures. Verifier A owns whether a number exists in a filed source; nothing here overrides that gate.

---

## PART 1: INDEPENDENT RED-FLAG LIST (from the transcripts alone)

Severity is graded as if the pipeline had missed the item entirely: CRITICAL (a missed repeated evasion, or would change a decision), MAJOR (thesis-relevant), MINOR (tone, detail, or already contained).

### 1A. Material items (CRITICAL and MAJOR)

| ID | Sev | Type | Item and anchors |
|---|---|---|---|
| B-01 | CRITICAL | Guidance walkback across three calls, with a denial | FY27 revenue. FEB: "we are expecting more than INR300 crores next year" (CMD to Garvit Goyal, p.6); "FY '27 most likely will cross INR300 crores... Correct. Correct." (CMD to Paras Chheda, p.11); "Next year, yes." (CMD to Gaurav Shukla, p.14). JUN: "Fixed target to achieve between INR275 crores to INR300 crores" (CMD to Paras Chheda, p.5). AUG: "INR250 crores to INR300 crores" (p.6, p.14). Garvit Goyal: "earlier you mentioned INR300 crores"; CMD: "No. I said it's between INR250 crores to INR300 crores." (AUG p.6). Achuth cites "60% growth... INR275 crores... a minimum"; CMD reframes: "if I commit something less... the investor will be safeguarded" (AUG p.16). |
| B-02 | MAJOR | Guidance walkback | FY28 revenue. FEB: "Possibility to go up to INR400 crores to INR500 crores" (CMD to Paras Chheda, p.11). Paras then ties "INR450 crores to INR500 crores... by FY '28" to the working capital and equity needed "to reach this full optimal capacity"; the CMD answers on dilution and does not dispute the number (FEB p.12). JUN: "Another INR100 crores will be added" (p.5), about 375-400 Cr on 275-300 (DERIVED). AUG: "You can take us 30% as our guideline" (p.9); "30% -- 20% to 30% will be the increase" (p.17), about 300-390 Cr on 250-300 (DERIVED). |
| B-03 | MAJOR | Guidance walkback, volunteered later | FY26 revenue. FEB: Garvit Goyal "earlier we were targeting INR200 crores plus"; CMD "INR180 crores to INR200 crores" (p.5; also p.14). JUN: FY26 total income INR182.1 crores (CMD opening, p.4). AUG: CMD volunteers "Initially, I committed INR225 crores... I have started committing INR200 crores, but INR190 crores only" (CMD to Achuth, p.17). |
| B-04 | MAJOR | Contradiction between analysts, same call | JUN: 275-300 "fixed target" to Paras Chheda (p.5); "around INR250 crores to INR300 crores" to Jayesh Lad (p.7); "INR250 crores to INR300 crores" to Nikunj Bhanushali (p.9); "INR270 crores to INR300 crores" to Ranga Rushwith (p.10). AUG: 250-300 to Garvit Goyal and Pankaj (p.6) vs "Almost INR350 crores, we are going to do this year" to Paras Chheda (p.15). |
| B-05 | MAJOR | Analyst insistence; excuse does not cover the gap | JUN: "this year, we have to execute INR412 crores. Out of that, definitely, we will execute INR275 crores to INR300 crores" (CMD to Jayesh Lad, p.7); "depends upon the... payment from customer and the raw material production cycle" (p.13). AUG: "INR377 crores should be completed before March" vs 250-300 (CMD to Pankaj, p.7); Pankaj presses twice; reason: "for 10%, 20% customers... they are extending their delivery period" (p.7). 377 Cr less 10-20% is 302-339 Cr (DERIVED), still above the top of the guide. The rest of the gap points to execution capacity, not to customer deferral. |
| B-06 | MAJOR | Capacity claim walked down | FEB: "Full operation means monthly INR60 crores to INR70 crores" (CMD to Paras Chheda, p.10), about 720-840 Cr a year (DERIVED); new plant "INR600 crores to INR650 crores" plus existing "INR100 crores to INR110 crores... maximum INR700 crores" (CMD to Ramaiy Kapoor, p.15). JUN: new facility "estimated revenue potential of INR500 crores to INR550 crores at optimal utilization" (CMD opening, p.4). AUG: both plants "INR600 crores to INR650 crores" (p.8), then "INR550 crores to INR600 crores in FY29" (p.9) (CMD to Paras Chheda). |
| B-07 | MAJOR | Internal contradiction (capacity vs revenue) | Existing plant "up to INR100 crores to INR110 crores" (FEB p.15) vs FY25 revenue "INR148 crores" (CMD to Dhanraj Tolani, FEB p.7) and Q4 FY25 "around INR60 crores" (CMD to Majid Ahamed, FEB p.8), both from the old plant alone. Analyst premise "INR45 crores on a quarterly basis" for the old plant left uncorrected (Garvit Goyal, FEB p.5). Old plant "70% to 78%" (CMD to Ranga Rushwith, JUN p.10) vs "Unit 1, it was utilized fully" (CMD to Manish, AUG p.11), while "20% to 25% skilled workers from the Unit 1" moved to Kannur (CMD to Jitesh K, AUG p.14). |
| B-08 | MAJOR | Repeated over-promise; explanation shifts | Kannur. FEB: new plant to contribute "INR30 crores to INR40 crores" in Q4; "only the manpower we have to increase" (CMD to Garvit Goyal and Majid Ahamed, p.17). JUN: FY26 contribution "INR20 crores to INR25 crores" (CMD to Nikunj Bhanushali, p.8; "Last year, INR20 crores", p.10); no explanation of the Q4 gap; "it will take 3 to 4 months to ramp up" (p.8-9). AUG: utilisation "20% to 25%" (CMD to Pankaj, p.6); "As of now, it is a little less. But definitely, it will be improved in Q2" (p.14). Feb names manpower scarcity ("Getting the manpower. That is a challenge", p.16); Aug discloses a choice to hire freshers instead of experienced workers (p.14). Jitesh K says the ramp lags peers (AUG p.14). |
| B-09 | MAJOR | Stance shift, only under insistence | FEB: "we have not planned anything on dilution" (CMD to Paras Chheda, p.12). AUG, after three pushes: "Next year, '27, '28 may require" (CMD to Paras Chheda, p.10). |
| B-10 | MAJOR | Margin guide walkback; basis switch | PAT: "10% to 12%" (FEB p.5), "10% to 12%, 10% to 13%" (FEB p.12); 10-12% (JUN p.5); AUG "10% to 12%" (p.5), then "9% to 12%" (p.14), "not able to increase above this 9% to 12%", "Maybe 1%, this or that" (p.15). Operating margin: Jayesh Lad's "15% to 16%" accepted (JUN p.7); EBITDA "18% to 20%" (Garvit Goyal, AUG p.5). No basis stated. |
| B-11 | MAJOR | Prepared remarks contradicted in Q&A (two calls) | JUN opening: input inflation "mitigated... through an improved high-voltage product mix" (p.4) vs Q&A "there was a dip in margin of 1% or 1.5%" (p.6) and "there is a drop of PAT margin of 1.5%" (p.11). Kannur gave 20-25 Cr in FY26 (p.8), too small to move the mix. AUG opening: "delivering greater operating leverage" (p.3), "improved operating leverage" (p.4) vs Q&A "this margin will be absorbed by the overheads... It will maintain the same" (p.8) and "not able to increase above this 9% to 12%" (p.15). The "absorbed by the overheads" line also appears in FEB p.15 and JUN p.5. |
| B-12 | MAJOR | Pass-through story widens each quarter | FEB: "Only that copper portion we will be able to pass on... Only the copper raise will be shared" (CMD to Garvit Goyal, p.6); same rule for "all" orders (CMD to Ramaiy Kapoor, p.15). JUN: "partially... delivery beyond 3, 4 months... price variation clause will be applied... below 3, 4 months... we will not able to pass" (CMD to Paras Chheda, p.6); PVC for orders "supplied after 5, 6 months" (CMD to Aditya, p.9). AUG: "Almost 80%, 85% order... covered with price variation clause" (CMD to Paras Chheda, p.10); "Generally, we don't take secure order without price variation" (CMD to Harinder Singh, p.11). Distribution transformers are 17.84% of the book (AUG p.4) and build in about 4 weeks (JUN p.13). |
| B-13 | MAJOR | Dodged question tied to a volunteered fact | AUG: Garvit Goyal: gross margin 23.80% to 28.82%, "is it a sort of any inventory gain lying there?"; CMD: "I could not get your question?", then a PVC answer; the inventory question is never answered (p.5). JUN: "luckily, we booked a large quantity of transformer oil in advance. Copper... strategically we have procured" and "For the Q1 already, we have booked most of the raw material in the month of March itself" (CMD to Saurabh Gupta, p.11). PVC passes "either variation on the positive side or the negative side" (JUN p.9). Peers: oil "almost double than what we used to buy in month of February" (SHIL-MAY26, Alay Shah, p.8); "transformer oil there is an 100% plus rise" (DAN-MAY26, Shivam Talwar, p.15). Pre-bought inputs sold at PVC-indexed prices would lift Q1 gross margin once. |
| B-14 | MAJOR | Volunteered, never explained | FEB opening: "an order of INR1.5 crores executed through Danya Electric Company" (p.4). AUG: "In this Danya Electric Company, we are using backward integration there. that company is supporting for that, which is for distribution transformers" (CMD to Paras Chheda, p.16). No analyst asked. Relationship, trade terms and guarantees never stated on any call. |
| B-15 | MAJOR | Book described larger than filed orders suggest | JUN: "we are fully booked with power transformers ranging from 25 MVA to 60-70 MVA" (CMD to Nikunj Bhanushali, p.9); "the capacity is built only for a larger power transformer... above 50 MVA" (CMD to Aditya, p.9). FEB opening: Karnataka EPC orders of INR24.63 crores "for supply of 20 MVA power transformer", 8-9 months (p.4), still in the June book. AUG: Kannur at 20-25% (p.6). |
| B-16 | MAJOR | Peer contradicts company (220 kV) | SPEL: "For 220 kV transformers, number of players are less" (CMD to Manish, AUG p.11); larger power transformers carry "1% or 2%" more margin (FEB p.7; AUG p.8, p.15). Shilchar: new plant "up to 160 MVA 220 kV class" from Apr-2027 (SHIL-MAY26, Alay Shah, p.9); "Initially, being new in the market, our margins will be lower mainly to create references" (SHIL-AUG26, Alay Shah, p.7). Danish: "up to 100 MVA and 245 KV... type testing processes have already commenced" (DAN-MAY26, Shivam Talwar, p.3); a new 220 kV entrant must "compromise on some other part in order to get that entry" (DAN-NOV25, Shivam Talwar, p.16-17); "product type... does not determine the margin" (DAN-MAY26, p.13). |
| B-17 | MAJOR | Peer contradicts company (PVC) | SPEL 80-85% PVC (AUG p.10) vs Danish "around 30% of the orders should be on price variation" (DAN-MAY26, Shivam Talwar, p.9); Shilchar "some orders... based on the PV clause", fixed-price orders reopened as "force majeure" (SHIL-MAY26, Alay Shah, p.16); "about 50-60% of the price rise" passed on older orders (SHIL-AUG26, Alay Shah, p.5). |

### 1B. Minor items

| ID | Sev | Type | Item and anchors |
|---|---|---|---|
| B-18 | MINOR | Silent miss | Q1 FY27 "INR50 crores to INR60 crores" (CMD to Saurabh Gupta, JUN p.11) vs total income INR48.31 crores (AUG opening, p.3). Not mentioned in August. |
| B-19 | MINOR | Shifting excuse | Q3 FY26 shortfall. Payment hold, "INR4 crores, INR5 crores" (FEB p.5); "the environmental clearance was delayed" (FEB p.5); "it is generally like that... sector culture", then "No, no. This year... awaiting for the payment", "INR10 crores" (CMD to Majid Ahamed, FEB p.8); "INR5 crores to INR10 crores" (FEB p.8, p.13); "the revenue has dipped by INR4 crores" (CMD to Gaurav Shukla, FEB p.13). Three causes, four sizes. |
| B-20 | MINOR | Internal contradiction (receivables) | Same answer: repeat buyers get "60 days and sometimes they take 75 days", receivables "80 to 90 days", yet "we have stopped giving credits to all customers" (CMD to Paras Chheda, FEB p.12) and "as a policy, we don't want to give any credit" (FEB p.13). Baseline "from 210 to 80 days" (FEB p.12) vs "was 110" (CMD to Ramaiy Kapoor, FEB p.15). Then 94 days (JUN p.4) and "80 to 100 days" (CMD to Pankaj, AUG p.7). |
| B-21 | MINOR | Unclosed regulatory item | First invoice "on Friday" (FEB p.7) vs "on 30th for the auspicious day" (FEB p.10). "Only thing this PCB claims, environmental claims we have to get... just a matter of a week" (FEB p.10). Garvit Goyal's clearance question went unanswered when his line dropped (FEB p.17). Never reported in JUN or AUG. |
| B-22 | MINOR | Deck vs call | Aditya: the June deck had "a mention about the DC orders" (JUN p.10). AUG: "as of now, we have not received any order"; "FY27 we'll not get" (p.11); "we have not secured any order from data centers" (p.12). |
| B-23 | MINOR | Inconsistent order facts | "160 MVA and 220 kV class and 112 MVA with 333 kV class" (JUN p.9); "112 MVA, 330 kV class" (JUN p.10) vs "capacity to manufacture up to 200 MVA to 220 kV class" and 300-330 kV only "in Phase 2, by addition of a few testing equipment" (JUN p.12). AUG: "2 numbers of 165 MVA from KPTCL" (p.11). 330 kV is not a standard Indian transmission class; the figure needs a filed check. |
| B-24 | MINOR | Same-call timing conflict | Tank factory "will complete in this financial year" (JUN p.6) vs "come into operation next financial year" (JUN p.11); "before March" (AUG p.10). |
| B-25 | MINOR | Tone shift between quarters | JUN: "truly exceptional year" (p.3); "flawless execution", "impressive 9,000 MVA" (p.4). AUG: "margins witnessed some moderation" (p.3); "measured manner" (p.4); "cautiously, we are telling" (p.7); "if I commit something less" (p.16). |
| B-26 | MINOR | Deflection | Main board: "very much focused" (JUN p.13); "In an appropriate time" (AUG p.7); "Let us see" (AUG p.15). |
| B-27 | MINOR | Repeated no-progress | Exports: "not able to give any guideline" (FEB p.9); "we have not yet exported significantly" (FEB p.14); "direct export is not there" (AUG p.9); "last 1.5 years, we are trying" (AUG p.16). |
| B-28 | MINOR | Wrong analyst figures left standing | 9M "INR118.45 crores" (Gaurav Shukla, FEB p.14) vs INR111.38 crores in the opening (FEB p.3). H2 "14.6% of EBITDA margin" (Saurabh Gupta, JUN p.11) vs 19.01 on 106.75 = 17.8% (JUN p.4, DERIVED). Employee cost "around 4x" (Sanjiv Mittal, AUG p.7). The CMD corrects none. |
| B-29 | MINOR | Over-promotion | "FY '26 was definitely defined by flawless execution" (JUN p.4) against a one-quarter plant slip (FEB p.5) and the Kannur Q4 miss (B-08). |
| B-30 | MINOR | Peer context vs company claim | SPEL: "there is no symptom about that" on competitive margin pressure (CMD to Garvit Goyal, FEB p.6). Peers: "huge capacity coming in the market in the next two to three years" (SHIL-APR25, Alay Shah, p.9); "everyone is expanding right now" (SHIL-MAY26, Alay Shah, p.12); analyst "a lot of supply coming" (DAN-NOV25, p.3). Counter: "there is no pressure of lower margins... domestic market is normal" (SHIL-AUG26, Alay Shah, p.10). Today the claim holds; the risk is forward. |

Two transcript items I checked and dropped as not red flags. (1) The June order book of 588.17 Cr vs 585.14 Cr: the call dates them 27-May and 2-Jun, and six days of execution explains the gap (see Part 3). (2) Peers also cut guidance (Shilchar 900 to 800 Cr, SHIL-MAY26 p.9-10; Danish about 600 to 500-550 Cr, DAN-NOV25 p.15). That is context for B-01, not a flag against SPEL.

One symmetric item, recorded so the bar stays even. Order intake beat the February conversion range. FEB: pipeline "INR700 crores to INR800 crores", conversion "10% to 20%" (CMD to Garvit Goyal, p.16), so about 70-160 Cr. Order book went from about 311 Cr (FEB p.9, p.11) to 588.17 Cr on 27-May (JUN p.4), a net 277 Cr addition before any execution is added back (DERIVED). This is a delivery the B05 promise table does not record (finding F15).

---

## PART 2: COMPARISON AGAINST B05 AND B06

| ID | Sev | Status | Where the pipeline has it | Note |
|---|---|---|---|---|
| B-01 | CRITICAL | CAUGHT | B05 FLAG-GUIDANCE-DRIFT; red_flags HIGH; repeated_evasions row 1; 2E quotes the Aug denial | Fully weighted. |
| B-02 | MAJOR | PARTIALLY CAUGHT | B05 1B lists Feb 400-500 as "order intake... ambiguous: revenue or orders"; dropped_triggers files it as "FY28 order booking" | Misclassified. FEB p.12 ties 450-500 Cr to working capital and equity "by FY '28": it is revenue. The FY28 chain loses its high-water mark. Finding F2. |
| B-03 | MAJOR | CAUGHT | B05 Section 0 row 1i; red_flags HIGH; guidance row | B05 correctly notes 225 and 190 are retrospective only. |
| B-04 | MAJOR | CAUGHT | B05 Section 0 rows 1a and 2b; guidance row "275-300 ('fixed target'); also 250-300 and 270-300 on same call" | B05 reads "350" as a schedule step, not as a revenue contradiction; both readings exist (see F3). |
| B-05 | MAJOR | CAUGHT | B05 3C Pankaj row; Section 4A cross-check | Fully weighted. |
| B-06 | MAJOR | CAUGHT | B05 1B peak revenue row; red_flags HIGH 2 | B05 omits the "INR60-70 crores monthly" line (FEB p.10); no effect. |
| B-07 | MAJOR | CAUGHT | B05 FLAG-CAPACITY-INCONSISTENT; Section 0 row 3d | Caught. The derived 225-275 Cr range inside the flag is one-sided (finding F4). |
| B-08 | MAJOR | CAUGHT | B05 2A rows (Q4 30-40 MISSED; 3-4 months PARTIAL); repeated_evasions row 2; 2B | B05 records the cause as "a mix of external and internal". |
| B-09 | MAJOR | CAUGHT | B05 Section 0 row 1h; 2A; repeated_evasions row 3; 2D warrant balance | Fully weighted. |
| B-10 | MAJOR | CAUGHT | B05 Section 0 rows 1d, 1e; FLAG-MARGIN-BASIS; red_flags MEDIUM | Fully weighted. |
| B-11 | MAJOR | PARTIALLY CAUGHT | B05 trigger 5 ("absorbed by overheads", conviction L); 2B notes the H2 dip as an "honest admission" | The Q&A facts are in. The scripted claims that the Q&A contradicts (JUN p.4; AUG p.3-4) are not flagged. Finding F5. |
| B-12 | MAJOR | CAUGHT | B05 repeated_evasions row 5 ("scope widened"); B06 FLAG-PVC-OUTLIER | Fully weighted. |
| B-13 | MAJOR | PARTIALLY CAUGHT | B05 3C last row cites "I could not get your question" but frames the question as about opex; B05 3C H2 row notes the March pre-buy and "Reopens Q2"; B05 trigger 4 confirm_signal takes the Q1 gross margin as the level to hold; B06 2B reads the oil spike as a cost risk only | The inventory-gain question and its link to the pre-buy are missed. Finding F1. |
| B-14 | MAJOR | CAUGHT | B05 FLAG-DANYA; red_flags MEDIUM; 2D; 3D | Weight fits the thin transcript evidence; the filed facts sit with other stages. |
| B-15 | MAJOR | PARTIALLY CAUGHT | B05 FLAG-QUALIFICATION-GAP and red_flags MEDIUM show the thin large-MVA mix from filings | The CMD's own "25 MVA to 60-70 MVA" description is not flagged as an overstatement. Finding F6. |
| B-16 | MAJOR | CAUGHT | B06 Q5, Q6, FLAG-220KV-ENTRANT-CLUSTER, cross_peer_hypothesis | Fully weighted. |
| B-17 | MAJOR | CAUGHT | B06 Q3a CONTRADICTED; FLAG-PVC-OUTLIER | Fully weighted. |
| B-18 | MINOR | CAUGHT | B05 2A row MISSED; silence | |
| B-19 | MINOR | CAUGHT | B05 red_flags MEDIUM ("two causes", "sized at 4, 5, 5-10 and 10") | B05 counts two causes; the seasonality answer (FEB p.8) is a third. No effect. |
| B-20 | MINOR | PARTIALLY CAUGHT | B05 2A receivables row (94 days; 210 vs AR) | The in-call "no credit" policy vs 60-75 day credit, and 210 vs 110 days in one call, are not noted. Finding F7. |
| B-21 | MINOR | CAUGHT | B05 red_flags MEDIUM; 2D PCB row; 3C row 2 | |
| B-22 | MINOR | CAUGHT | B05 Section 0 row 4a; repeated_evasions row 6 | The deck-vs-call nuance is not noted; no effect. |
| B-23 | MINOR | PARTIALLY CAUGHT | B05 Section 0 row 4b (160 vs 165, one vs two, KPTCL vs Hyderabad) | The 330 kV order vs the 220 kV plant rating is not noted. Finding F8. |
| B-24 | MINOR | CAUGHT | B05 timeline_slippages row 3 | |
| B-25 | MINOR | PARTIALLY CAUGHT | B05 2B ("reframed as prudence"); 2C over-promotion 4 | The cross-quarter tone shift itself is not called out. Finding F9. |
| B-26 | MINOR | CAUGHT | B05 repeated_evasions row 7 | |
| B-27 | MINOR | CAUGHT | B05 repeated_evasions row 4 | |
| B-28 | MINOR | PARTIALLY CAUGHT | B05 Section 0 (the "4x" instance only) | The pattern across three calls is not noted. Finding F10. |
| B-29 | MINOR | CAUGHT | B05 2B, 2C | |
| B-30 | MINOR | CAUGHT | B06 2C capex cycle; B05 3A | B05's reason for its Low rating is a non sequitur (finding F14). |

Totals. Caught 22, partially caught 8, missed 0. Material (17): caught 13, partially caught 4, missed 0. Minor (13): caught 9, partially caught 4, missed 0.

---

## PART 3: PIPELINE FLAGS ASSESSED AGAINST THE TRANSCRIPTS

### 3A. B05 red_flags and flags

| Pipeline item | Verdict | Basis |
|---|---|---|
| red_flags HIGH: guidance cascade | SUPPORTED | B-01, B-03, B-08, B-18. |
| red_flags HIGH: Kannur and Unit 1 utilisation, capacity potential conflict | SUPPORTED | B-06, B-07. The AR 45-50% vs 19.4% point is outside my inputs. |
| red_flags MEDIUM: Danya never explained | SUPPORTED (transcript part) | FEB p.4; AUG p.16. The Rs 88.13 Cr Danya book is from the deck, outside my inputs. |
| red_flags MEDIUM: Q3 FY26 two causes, deferral sized four ways, PCB never closed | SUPPORTED | B-19, B-21. |
| red_flags MEDIUM: larger-MVA mix thin | SUPPORTED (consistent) | Filings are outside my inputs; FEB p.4 shows 20 MVA orders; the CMD's description overstates (B-15). |
| red_flags MEDIUM: PAT floor to 9% while EBITDA guide rises | SUPPORTED | AUG p.5, p.14, p.15. |
| red_flags LOW: 13-Jul order and 160 vs 165 MVA | SUPPORTED where testable | JUN p.9; AUG p.11. |
| FLAG-GUIDANCE-DRIFT | SUPPORTED | As B-01. |
| FLAG-CAPACITY-INCONSISTENT | SUPPORTED as an inconsistency; derived range OVERSTATED | See F4 below. |
| FLAG-SCHEDULE-DRIFT (and repeated_evasions row 8) | OVERSTATED | See F3 below. |
| FLAG-DANYA | SUPPORTED | As B-14. |
| FLAG-QUALIFICATION-GAP | SUPPORTED | AUG p.11-13; JUN p.12. |
| FLAG-MARGIN-BASIS | SUPPORTED | JUN p.7; AUG p.5. |
| repeated_evasions rows 1-7 | SUPPORTED | Each row checked against the cited pages. |
| Section 3D: "Gap of 3.03 Cr is unexplained" | NOT SUPPORTED | See F11. |
| Section 2C: "repeats 'I could not get your question' four times in Q1" | NOT SUPPORTED | See F12. |
| Section 3A: "no symptom" rated Low credibility | OVERSTATED | See F14. |

**F3. FLAG-SCHEDULE-DRIFT is OVERSTATED (MAJOR).** B05 reads 412 Cr (JUN p.7) to 377 Cr (AUG p.7) as a schedule slip. The two figures sit on different start dates. 412 Cr is the part of the 27-May book due by March. 377 Cr is the part of the 13-Aug book due by March. Between those dates are 78 days. At the Q1 FY27 run-rate (48.31 Cr over 91 days, AUG p.3) about 41 Cr was executed (DERIVED). That closes all but about 6 Cr of the 35 Cr step, and new orders due before March can fill the rest. The sub-claim "order book is flat at 590.06 vs 588.17 despite Rs 195.64 Cr of Q1 wins" double counts. The April and May wins already sit inside the 588.17 Cr of 27-May. About 43 Cr of inflow between 27-May and 13-Aug (DERIVED) fits a flat book. Two parts of the flag stand: the step from 377 Cr to "almost INR350 crores" in one call (AUG p.15), and the gap between 377 Cr due and a 250-300 Cr revenue guide (B-05). The correct reading: order coverage held while the revenue guide fell. That points the cut at execution capacity, not at order flow. This matters to stage 11's choice of revenue basis.

**F4. The derived range inside FLAG-CAPACITY-INCONSISTENT is one-sided (MAJOR).** B05 derives FY27 revenue of 225-275 Cr from Unit 1 at 100-110 Cr (FEB p.15) plus Kannur at 25-30% of 500-550 Cr. Its analyst_note then says "stage 11 should not take the top of the range as evidenced". The same flag shows the Unit 1 figure is contradicted by the record: non-Kannur revenue was about 157-162 Cr in FY26, and FY25 revenue of about 148 Cr came from the old plant alone (FEB p.7). On demonstrated non-Kannur output plus the same Kannur assumption, the range is about 282-327 Cr (DERIVED). Two readings exist. Reading 1: stated plant potential binds, so 225-275 Cr. Reading 2: demonstrated output binds, so 282-327 Cr. Part of the non-Kannur revenue may run through Danya, which moves margin quality, not the revenue count. The separating observation is Q2 FY27 revenue against the 55-65 Cr path B05 names, plus any revenue split by unit. Stage 11 needs both readings in front of it, per the house rule on stating both readings.

### 3B. B06 flags and verdicts

| Pipeline item | Verdict | Basis |
|---|---|---|
| FLAG-PVC-OUTLIER | SUPPORTED | B-17. |
| FLAG-PEER-SEGMENT-MISMATCH | SUPPORTED | Shilchar solar and wind "about 80% of domestic revenue" (SHIL-OCT25, Aashay Shah, p.12); Danish IDT "about 70%" (DAN-NOV25, Shivam Talwar, p.12). |
| FLAG-220KV-ENTRANT-CLUSTER and cross_peer_hypothesis | SUPPORTED | B-16; the falsifier is stated. |
| Q3a CONTRADICTED | SUPPORTED | B-17. |
| Q6 CONTRADICTED (gross gain) | SUPPORTED | DAN-MAY26 p.13; DAN-NOV25 p.16-17, p.19; SHIL-AUG26 p.7. B06 also records the one supporting peer line (SHIL-OCT25). |
| Q1b CONTRADICTED, listed as a priority item for synthesis | OVERSTATED | See F13. |
| Q1a, Q2, Q3b, Q4, Q5, Q7-Q11 | SUPPORTED as graded | Spot-read against the cited peer pages. |

**F13. B06 Q1b is OVERSTATED (MINOR).** SPEL never claimed 12-24 month lead times on a call. Its own figures are about 4 weeks for distribution transformers, 6-8 weeks at 25 MVA and 3-4 months at 50-100 MVA (CMD to Saurabh Gupta, JUN p.13-14). Those agree with the peers. The 2-year figure on the calls is analyst Harinder Singh's remark about 300-500 MVA units at Siemens, Bharat Bijlee and T&R (AUG p.12). The contradiction lands on the wording of B05's peer question, not on management. Synthesis should not count it against SPEL's credibility.

**F11. B05 3D "gap of 3.03 Cr is unexplained" is NOT SUPPORTED (MINOR).** The June call dates the two figures. 588.17 Cr is "As of May 27, 2026" (JUN p.4). 585.14 Cr is "As of date", 2-Jun (JUN p.10). Six days at about 0.53 Cr a day is about 3.2 Cr (DERIVED). The government and non-government split of 196.79 + 388.35 (JUN p.7) sums to the as-of-date figure. This observation feeds no flag. Rule 5's MAJOR grade binds pipeline red flags, so I grade it MINOR.

**F12. B05 2C "four times in Q1" is NOT SUPPORTED (MINOR).** "I could not get your question" appears once in the August call (p.5). Across all three calls there are five replies of this kind (FEB p.8, p.15, p.16; JUN p.14; AUG p.5). It feeds only the Defensiveness score of 2, which still holds.

**F14. B05 3A rates "no symptom" of competitive pressure Low credibility on a non sequitur (MINOR).** The reason given is the H2 input-cost dip. An input-cost dip is not evidence of price competition. Shilchar says domestic prices show no pressure (SHIL-AUG26, Alay Shah, p.10). The better basis for caution is the forward capacity race (B06 2C; B-30).

---

## PART 4: PROMISE-DELIVERY SPOT CHECKS (5)

| # | B05 row | Earlier call contains the promise? | Later call shows the outcome? | Result |
|---|---|---|---|---|
| 1 | Q4 FY26 revenue 70-80 Cr: DELIVERED at floor | Yes. Garvit Goyal "this quarter, we'll be touching INR70 crores to INR80 crores"; CMD "Yes, yes, yes" (FEB p.5); "INR70-odd crores?"; "anyway, we will do it" (FEB p.14). | Yes. H2 total income 106.75 Cr (JUN p.4) less Q3 36.03 Cr (FEB p.3) = 70.72 Cr (DERIVED). | CONFIRMED |
| 2 | New plant 30-40 Cr in Q4 FY26: MISSED | Yes. "new plant will be contributing something around INR40 crores... INR30 crores to INR40 crores" (FEB p.17). | Yes. "INR20 crores to INR25 crores from the new facility" for FY26 (JUN p.8); "Last year, INR20 crores" (JUN p.10). | CONFIRMED |
| 3 | Q1 FY27 50-60 Cr: MISSED | Yes. "up to INR50 crores to INR60 crores in this first quarter" (JUN p.11). | Yes. Total income 48.31 Cr (AUG p.3). B05's 48.23 is revenue from results, outside my inputs; both are below 50. | CONFIRMED |
| 4 | Kannur output in 3-4 months: PARTIAL | Yes. "it will take 3 to 4 months to ramp up and get required or expected output" (JUN p.8); "2 to 3 months, 4 months" (JUN p.9). | Yes. Utilisation "20% to 25%" (AUG p.6); "As of now, it is a little less" (AUG p.14). | CONFIRMED, with a caveat: the window ran to early Sep to early Oct 2026; the August call came about 2.5 months after June. NOT YET DUE is the cleaner label. |
| 5 | Government exposure below 50%: DELIVERED | Yes. "we want to restrict below 50%... as of now... 30% to 35%" (FEB p.9). | Yes. 30.10% (AUG p.4). | CONFIRMED, with a caveat: the target was already met when stated, so the row tests nothing and pads the delivered count. |

Checked 5, confirmed 5, wrong 0. The two caveats and two more table issues are finding F15. (a) "Identify land within about a quarter: MISSED" rests on "Yes, yes. But okay, we will try." (FEB p.11), a hedged intent, not a promise. (b) The table omits the order-intake beat recorded in Part 1. Net effect on the tally: delivered 3, partial 3, missed 3, plus one positive delivery not tabled. The grade does not move.

---

## PART 5: CREDIBILITY GRADE

B05 grade: C (Mixed). Verdict: **concur**.

The case for a lower grade: every revenue guide landed at or below its floor (FY26 182.1 Cr on 180-200; Q4 70.72 Cr on 70-80; Q1 FY27 48.31 Cr on 50-60); FY27 was cut twice and the cut was denied on the call (B-01); FY28 walked down from 400-500 Cr (B-02, missed by B05); scripted remarks claim mix and leverage gains that the Q&A denies (B-11); one direct inventory question went unanswered (B-13).

The case for a higher grade: the PAT band of 10-12% held in Q4 FY26 and Q1 FY27; order intake beat the February conversion range by a wide margin; the CMD volunteered hard facts unasked (labour as the top constraint, FEB p.16; "Last two years, it was bad" on receivables, FEB p.12; the 1-1.5 point margin dip, JUN p.6; the FY26 guidance history, AUG p.17).

The two cases offset. C holds. B05's upgrade test (Q2 FY27 revenue inside 55-65 Cr and Kannur utilisation of at least 30% stated with its basis) is the right observation. I add one: Q2 FY27 gross margin against Q1's 28.82%, which separates a PVC run-rate from a one-time pre-buy gain (B-13).

---

## PART 6: CONSOLIDATED FINDINGS

| # | Sev | Type | Finding | Anchor |
|---|---|---|---|---|
| F1 | MAJOR | PARTIALLY CAUGHT (B-13) | The Q1 FY27 gross margin jump (23.80% to 28.82%) carries an unanswered inventory-gain question and a disclosed March pre-buy of oil and copper. B05 trigger 4 takes the Q1 gross margin as the level to hold. B06 reads the oil spike one way only. Two readings: a PVC run-rate, or a one-time gain from pre-bought inputs sold at PVC-indexed prices, which also reverses when prices fall. Separating observation: Q2 FY27 gross margin. Stage 11 should not anchor the margin bridge on Q1 until Q2 prints. | AUG p.5; JUN p.9, p.11; SHIL-MAY26 p.8; DAN-MAY26 p.15 |
| F2 | MAJOR | PARTIALLY CAUGHT (B-02) | The FY28 high-water mark of 400-500 Cr revenue is filed as "order booking, ambiguous" and a dropped trigger. The FEB p.12 follow-up makes it revenue. The FY28 chain reads 400-500 (Feb), about 375-400 (Jun), about 300-390 (Aug, DERIVED). | FEB p.11-12; JUN p.5; AUG p.9, p.17 |
| F3 | MAJOR | OVERSTATED pipeline flag | B05 FLAG-SCHEDULE-DRIFT compares 412 Cr and 377 Cr on different start dates; about 41 Cr of execution in 78 days explains the step. "Flat book despite Q1 wins" double counts April-May wins. The 377 to 350 step and the 377 vs 250-300 guide gap stand. | JUN p.4, p.7; AUG p.3, p.7, p.15 |
| F4 | MAJOR | OVERSTATED pipeline derivation | B05's FY27 cross-check of 225-275 Cr uses the contradicted Unit 1 potential and steers stage 11 away from the top of the guide. The demonstrated-output reading is about 282-327 Cr (DERIVED). Both readings belong in front of stage 11; Q2 FY27 revenue separates them. | FEB p.7, p.15; JUN p.4, p.8; AUG p.11 |
| F5 | MINOR | PARTIALLY CAUGHT (B-11) | Scripted claims of a mix-driven margin offset (JUN) and operating leverage (AUG) are contradicted in the Q&A of the same calls and are not flagged. B05's own margin read (trigger 5, conviction L) is right, so no value moves. Do not quote the opening remarks as margin evidence. | JUN p.4, p.6, p.11; AUG p.3, p.4, p.8, p.15 |
| F6 | MINOR | PARTIALLY CAUGHT (B-15) | The CMD's "25 MVA to 60-70 MVA" description of the book is not flagged as an overstatement. B05 reaches the right substance from filings. | JUN p.9; FEB p.4; AUG p.6 |
| F7 | MINOR | PARTIALLY CAUGHT (B-20) | "No credit" policy vs 60-75 day credit in one answer; 210 vs 110 day baseline in one call. Not noted. | FEB p.12, p.13, p.15 |
| F8 | MINOR | PARTIALLY CAUGHT (B-23) | A 112 MVA "330 kV" order sits above the 220 kV plant rating; 330 kV is not a standard Indian class. Needs a filed check. | JUN p.9, p.10, p.12 |
| F9 | MINOR | PARTIALLY CAUGHT (B-25) | The June-to-August tone shift is not called out as a shift. | JUN p.3-4; AUG p.3, p.4, p.7, p.16 |
| F10 | MINOR | PARTIALLY CAUGHT (B-28) | Wrong analyst figures left standing in all three calls; B05 notes one instance. | FEB p.14; JUN p.11; AUG p.7 |
| F11 | MINOR | NOT SUPPORTED pipeline observation | B05 3D "3.03 Cr gap unexplained": the two figures carry different as-of dates. | JUN p.4, p.7, p.10 |
| F12 | MINOR | NOT SUPPORTED pipeline evidence | B05 2C "four times in Q1": one instance. | AUG p.5 |
| F13 | MINOR | OVERSTATED pipeline verdict | B06 Q1b contradicts a lead-time claim SPEL never made; SPEL's own lead times match the peers. | JUN p.13-14; AUG p.12 |
| F14 | MINOR | OVERSTATED pipeline rating | B05 3A rates "no symptom" Low on an input-cost dip; the right basis is the forward capacity race. | FEB p.6; SHIL-AUG26 p.10 |
| F15 | MINOR | Promise table | One padded row (government below 50%), one premature row (Kannur 3-4 months), one hedged intent tabled as a promise (land), one positive delivery omitted (order intake). The grade does not move. | FEB p.9, p.11, p.16; JUN p.4, p.8; AUG p.4, p.6 |
| F16 | MINOR | Anchor drift (note for Verifiers A and D) | Some anchors use the printed page, not the stated file marker. B05: 500-550 Cr at "H2 p.3" is p.4; "players are less" at "Q1 p.12" is p.11; 160 MVA 220 kV at "H2 p.8" is p.9. B06: Danish 30% PVC at "p.8" is DAN-MAY26 p.9; Shilchar PV clause at "p.15" is SHIL-MAY26 p.16; Shilchar entry margin at "p.6" is SHIL-AUG26 p.7; Danish "product type" at "p.12" is DAN-MAY26 p.13. All quotes exist; only the page is off by one. | as listed |

Counts: CRITICAL 0, MAJOR 4, MINOR 12.

---

## PART 7: SCORING

Material items on my list: 17 (1 CRITICAL, 16 MAJOR) of 30 listed. Caught 13, partially caught 4, missed 0. The rate counts CAUGHT only: 13 of 17 = 76%. With partials at half credit it is 88%; at full credit 100%. The denominator is 4 or more, so the rate is reported, not null. It is above 60% on every counting rule.

```yaml
stage: B12b
company: "SUPREMEPWR"
run_date: "2026-10-06"
model: "claude-opus-5-5"  # must equal .claude/agents frontmatter; the orchestrator compares it
status: complete
independent_flags_found: 30
caught: 22
partially_caught: 8
missed: []
pipeline_flags_not_supported:
  - {status: "OVERSTATED", severity: MAJOR, flag: "B05 FLAG-SCHEDULE-DRIFT (and repeated_evasions row 8)", reason: "412 Cr (27-May book, Jun call p.7) and 377 Cr (13-Aug book, Aug call p.7) sit on different start dates; about 41 Cr executed in the 78 days between (DERIVED from Q1 FY27 total income 48.31 Cr over 91 days, Aug p.3) closes most of the step. 'Flat book despite 195.64 Cr of Q1 wins' double counts April-May wins already inside 588.17 Cr. The 377 to 'almost 350' step (Aug p.15) and the 377 vs 250-300 guide gap stand."}
  - {status: "OVERSTATED", severity: MAJOR, flag: "B05 FLAG-CAPACITY-INCONSISTENT derived FY27 range 225-275 Cr and analyst_note 'stage 11 should not take the top of the range as evidenced'", reason: "Uses the Unit 1 potential of 100-110 Cr (Feb p.15) that the same flag shows is contradicted (FY26 non-Kannur revenue about 157-162 Cr; FY25 about 148 Cr from the old plant alone, Feb p.7). Demonstrated-output reading is about 282-327 Cr (DERIVED). Both readings belong in front of stage 11; Q2 FY27 revenue separates them."}
  - {status: "NOT SUPPORTED", severity: MINOR, flag: "B05 Section 3D: 'Gap of 3.03 Cr is unexplained' (588.17 vs 585.14)", reason: "Jun call dates them 'As of May 27' (p.4) and 'As of date', 2-Jun (p.10); six days at about 0.53 Cr a day is about 3.2 Cr (DERIVED); the 196.79 + 388.35 split (p.7) sums to the as-of-date figure. Feeds no flag, so graded MINOR."}
  - {status: "NOT SUPPORTED", severity: MINOR, flag: "B05 Section 2C: 'repeats I could not get your question four times in Q1'", reason: "One instance in the Aug call (p.5); five such replies across all three calls. Feeds only the Defensiveness score, which holds."}
  - {status: "OVERSTATED", severity: MINOR, flag: "B06 Q1b CONTRADICTED, listed as a priority item for synthesis", reason: "SPEL never claimed 12-24 month lead times; its own figures (about 4 weeks DT, 6-8 weeks at 25 MVA, 3-4 months at 50-100 MVA, Jun p.13-14) match the peers. The 2-year figure is an analyst remark on 300-500 MVA units at other makers (Aug p.12)."}
  - {status: "OVERSTATED", severity: MINOR, flag: "B05 Section 3A: 'no symptom' of competitive pressure rated Low credibility because of the H2 input-cost dip", reason: "An input-cost dip is not price competition; Shilchar says domestic prices show no pressure (SHIL-AUG26 p.10). The forward capacity race is the better basis."}
promise_delivery_spot_checks: {checked: 5, confirmed: 5, wrong: 0}
credibility_grade_concur: "concur (C): every revenue guide landed at or below its floor and FY27 was cut twice with a denial, offset by a held PAT band and order intake that beat the Feb conversion range; after removing one padded and one premature row the tally is 3/3/3, still C"
findings:
  - {severity: MAJOR, type: "PARTIALLY CAUGHT (B-13)", item: "Q1 FY27 gross margin 23.80% to 28.82%: inventory-gain question unanswered; March pre-buy of oil and copper disclosed in June; PVC passes rises and falls. B05 trigger 4 takes Q1 gross margin as the level to hold; B06 reads the oil spike one way.", anchor: "AUG p.5 (Garvit Goyal, CMD); JUN p.9, p.11 (CMD); SHIL-MAY26 p.8 (Alay Shah); DAN-MAY26 p.15 (Shivam Talwar)", note: "Two readings: PVC run-rate vs one-time pre-buy gain. Separating observation: Q2 FY27 gross margin. Stage 11 should not anchor the margin bridge on Q1 until Q2 prints."}
  - {severity: MAJOR, type: "PARTIALLY CAUGHT (B-02)", item: "FY28 revenue guide walked down 400-500 Cr (Feb) to about 375-400 (Jun) to about 300-390 (Aug, DERIVED); B05 files the Feb figure as 'order booking, ambiguous' and a dropped trigger", anchor: "FEB p.11-12 (Paras Chheda, CMD); JUN p.5; AUG p.9, p.17", note: "Feb p.12 follow-up ties 450-500 Cr by FY28 to working capital and equity: it is revenue."}
  - {severity: MAJOR, type: "OVERSTATED pipeline flag", item: "B05 FLAG-SCHEDULE-DRIFT: 412 vs 377 Cr is a time-basis comparison; 'flat book despite Q1 wins' double counts", anchor: "JUN p.4, p.7; AUG p.3, p.7, p.15", note: "Order coverage held while the revenue guide fell; the cut points at execution capacity, not order flow."}
  - {severity: MAJOR, type: "OVERSTATED pipeline derivation", item: "B05 FY27 cross-check 225-275 Cr uses the contradicted Unit 1 potential and steers stage 11 off the top of the guide; demonstrated-output reading about 282-327 Cr (DERIVED)", anchor: "FEB p.7, p.15; JUN p.4, p.8; AUG p.11", note: "State both readings; Q2 FY27 revenue and any split by unit separate them."}
  - {severity: MINOR, type: "PARTIALLY CAUGHT (B-11)", item: "Scripted margin claims (Jun: offset by high-voltage mix; Aug: greater operating leverage) contradicted in the same calls' Q&A; not flagged", anchor: "JUN p.4, p.6, p.11; AUG p.3, p.4, p.8, p.15", note: "B05 trigger 5 (conviction L) already holds the right margin read; do not quote the opening remarks as margin evidence."}
  - {severity: MINOR, type: "PARTIALLY CAUGHT (B-15)", item: "CMD describes the book as '25 MVA to 60-70 MVA' while 20 MVA orders sit in it; not flagged as a management overstatement", anchor: "JUN p.9; FEB p.4; AUG p.6", note: "B05 reaches the substance from filings."}
  - {severity: MINOR, type: "PARTIALLY CAUGHT (B-20)", item: "'No credit' policy vs 60-75 day credit in one answer; 210 vs 110 day baseline in one call", anchor: "FEB p.12, p.13, p.15", note: ""}
  - {severity: MINOR, type: "PARTIALLY CAUGHT (B-23)", item: "112 MVA '330 kV' order above the 220 kV plant rating; 330 kV not a standard Indian class", anchor: "JUN p.9, p.10, p.12", note: "Needs a filed check."}
  - {severity: MINOR, type: "PARTIALLY CAUGHT (B-25)", item: "June-to-August tone shift (exceptional, flawless, impressive to moderation, measured, cautiously, commit less) not called out", anchor: "JUN p.3-4; AUG p.3, p.4, p.7, p.16", note: ""}
  - {severity: MINOR, type: "PARTIALLY CAUGHT (B-28)", item: "Wrong analyst figures left standing in all three calls (9M 118.45 vs 111.38; H2 EBITDA 14.6% vs 17.8% DERIVED; employee cost 4x)", anchor: "FEB p.3, p.14; JUN p.4, p.11; AUG p.7", note: "B05 notes only the 4x instance."}
  - {severity: MINOR, type: "NOT SUPPORTED pipeline observation", item: "B05 3D '3.03 Cr gap unexplained'", anchor: "JUN p.4, p.7, p.10", note: "Different as-of dates explain it."}
  - {severity: MINOR, type: "NOT SUPPORTED pipeline evidence", item: "B05 2C 'four times in Q1'", anchor: "AUG p.5", note: "One instance."}
  - {severity: MINOR, type: "OVERSTATED pipeline verdict", item: "B06 Q1b contradicts a lead-time claim SPEL never made", anchor: "JUN p.13-14; AUG p.12", note: "Synthesis should not count it against SPEL."}
  - {severity: MINOR, type: "OVERSTATED pipeline rating", item: "B05 3A rates 'no symptom' Low on an input-cost dip", anchor: "FEB p.6; SHIL-AUG26 p.10", note: "Use the forward capacity race as the basis."}
  - {severity: MINOR, type: "Promise table", item: "Padded row (government below 50%), premature row (Kannur 3-4 months), hedged intent tabled as a promise (land), positive delivery omitted (order book 311 to 588.17 Cr vs 70-160 Cr implied conversion, DERIVED)", anchor: "FEB p.9, p.11, p.16; JUN p.4, p.8; AUG p.4, p.6", note: "Tally becomes 3/3/3 plus one untabled positive; grade unchanged."}
  - {severity: MINOR, type: "Anchor drift (note for Verifiers A and D)", item: "Some B05 and B06 anchors use the printed page instead of the stated file marker; all quotes exist, page off by one", anchor: "B05: 500-550 at H2 p.3 is p.4; players-less at Q1 p.12 is p.11; 160 MVA at H2 p.8 is p.9. B06: DAN-MAY26 PVC p.8 is p.9; SHIL-MAY26 PV clause p.15 is p.16; SHIL-AUG26 entry margin p.6 is p.7; DAN-MAY26 product type p.12 is p.13", note: ""}
critical_count: 0
major_count: 4
minor_count: 12
material_found: 17
material_caught: 13
acceptance_rate: 76
coverage_basis: "17 material (1 CRITICAL, 16 MAJOR) of 30 listed; 13 caught, 4 partially caught, 0 missed. Rate counts CAUGHT only (13/17 = 76%); partials at half credit give 88%, at full credit 100%. 13 MINOR: 9 caught, 4 partially caught. Counts in critical/major/minor_count are the 16 consolidated findings."
```
