# STAGE 12 VERIFIER B: CONCALL RED FLAGS, RAPPID (Rappid Valves (India) Ltd)

Run date: 2026-09-19. Model: claude-opus-5. Mode: NO-CONCALL MODE (manifest
concalls_available: false). The audit runs on the only company call
(01-Jun-2026, FY26 results) plus the written communication record: Reg 30
business updates, results PDFs, the FY26 AR (Chairman's Message, MD&A), the
IPO variation filings and the order disclosures.

## Inputs and coverage

- Company transcript: Concall_Jun_2026_Transcript.txt. Read in full (pages 1 to 31).
- Written communication, read in full: 01Feb2025 QIA business update; 03Jul2025, 16Oct2025 business updates;
  09Jul2026 and 10Jul2026 (revised) Q1 FY27 updates; 09Mar2026 business-update deck; 21Mar2026 board outcome
  (IPO object variation); 16Jan2026 and 19Jan2026 clarification letters; the four work-order filings (29May, 08Jun,
  15Jun, 13Aug 2026).
- Read in targeted sections: 27May2026 FY26 results (p.8 to p.10 notes, balance sheet lines); 13Nov2025 H1 FY26 results
  (p.3 statement); 24Mar2026 postal ballot notice (p.18 reasons); 30Mar2026 corrigendum; 30Apr2026 scrutinizer report;
  Annual_Report_2026.txt (Chairman's Message p.6 to p.7, capacity page p.15, MD&A p.23 to p.25); CS filings 01Mar2025,
  28Feb2026, 07Mar2026.
- Peer transcripts (8 of the 12 the rubric expects; the pipeline input set holds 8). Read by targeted search plus
  context reads, not cover to cover: KSB Mar-2026 (p.9 to p.10), KSB Aug-2026 (p.20 to p.26), with keyword sweeps over all
  four KSB calls, the three ATAM calls and the QUESTFLOW (Meson Valves) call. Coverage of the peer set is therefore
  partial. Peer items below are limited to what those reads surfaced.
- Pipeline artifacts audited: outputs/reports/05-concall.md and outputs/reports/06-peers.md (B06 YAML embedded).

Basis notes. Revenue figures are standalone, Rs Lakh, from the results PDFs. Rs Cr = Rs Lakh / 100.
FY26 EBITDA is Rs 10.31 Cr (AR 2026, Chairman's Message p.6). FY26 PAT is Rs 647.8 L (27May2026 results p.8).
On revenue of Rs 5,323.3 L, the EBITDA margin is 19.4% and the PAT margin is 12.17%.

---

## PART 1: INDEPENDENT RED-FLAG LIST (graded before comparison)

Anchors use: CC = Concall_Jun_2026_Transcript.txt, page; GD = Gaurav Dalal (CMD).

| # | Item | Anchor | Severity |
|---|---|---|---|
| F1 | The Feb-2025 guidance of 50% volume CAGR for FY26 and FY27 missed. FY26 revenue grew 2.1% (Rs 5,212.5 L to Rs 5,323.3 L). GD claims "we were on track". H1 FY26 revenue grew 46.9% (Rs 1,961.6 L to Rs 2,882.2 L), so that claim holds for H1 only. H2 FY26 fell 24.9% (Rs 3,250.9 L to Rs 2,441.1 L). | 01Feb2025 GBU p.2 "Volume CAGR Target: 50% CAGR in FY 2026 and FY 2027"; CC p.5 GD; 27May2026 results p.8; 13Nov2025 results p.3 | MAJOR |
| F2 | GD restates FY27 growth as "closing to 50% or more" (CC p.10). He then retreats under analyst extrapolation: "If I overcommit and underperform, that's a problem" (CC p.14). Deepanshu Bhatia later says "you are right now not very clearly telling us the next 2 or 3 years" (CC p.26). The FY26 AR does not repeat the figure. | CC p.10, p.14, p.26; AR 2026 (no "50%" hit) | MAJOR |
| F3 | IPO object variation. The full unutilised Rs 764.51 L is moved to working capital: Rs 364.51 L of unspent plant-and-machinery capex plus Rs 400 L for acquisitions. The Feb-2025 "advanced talks to acquire a Pune-based foundry" is abandoned. The notice gives a reason for the acquisition balance only. It gives none for the unspent capex balance. | 01Feb2025 GBU p.1; 21Mar2026 board outcome Annexure I p.2; 24Mar2026 notice p.18; CC p.22 to p.23 | MAJOR |
| F4 | Capex figure and funding contradict the filings. Asked for FY26 capex, GD says "around 3.65 crores", then "No, no, no, no, one second" and moves the answer to email (CC p.12). Rs 3.65 Cr matches the unspent IPO capex balance (Rs 364.51 L), not capex spent. Audited FY26 capex is Rs 179.4 L (27May2026 results p.10). GD says current capex is funded by "a working capital loan from our bankers" (CC p.22). The IPO capex money was at the same time moved to working capital. This is a live misstatement of a use-of-proceeds number, plus a circular funding swap. | CC p.12, p.22; 27May2026 results p.10; 21Mar2026 Annexure I | MAJOR |
| F5 | The written working-capital explanation conflicts with the call. The FY26 results note says the rise "reflects business expansion and execution of higher order volumes". Revenue grew 2.1%. GD says Rs 10 Cr of finished material sat undispatched in March, pending a price revision (CC p.6). Inventory rose Rs 1,050.5 L. CFO was an outflow of Rs 1,082.6 L. The same note says the IPO completed "during the financial year" (it completed in FY25). | 27May2026 results p.9 to p.10; CC p.5 to p.6 | MAJOR |
| F6 | Working-capital stress stated plainly. GD says "Currently, no working capital is enough" (CC p.21). The company pays 50% advances to all suppliers (CC p.16). It will seek funding "down the line 4 or 5 months" (CC p.20, p.25). GD calls it an "extremely capital-intensive manufacturing business" (CC p.25). The bank limit is Rs 23 Cr (CC p.21). ST borrowings rose from Rs 841.4 L to Rs 1,784.3 L (27May2026 results p.8). | CC p.16, p.20 to p.21, p.25 to p.26; results p.8 | MAJOR |
| F7 | US data-centre customer. The Oct-2025 filing says the valves "underwent extensive testing at the customer's laboratory", received UL approval and "will be exclusively manufactured and exported". In Jun-2026, GD says the company still waits for lab results on 10 valves, "prices to revisit", with no bulk contract. He says the process is "barely from last one year". | 16Oct2025 GBU p.2; CC p.9, p.20, p.27 | MAJOR |
| F8 | Capacity arithmetic stays unreconciled: 85% utilisation, "well equipped up to 120 crores", FY26 revenue Rs 53.23 Cr (CC p.5, p.11). The unit-capacity figure also moves: 29,625 units (09Mar2026 deck p.3) to 33,500 units at 85% (AR 2026 p.15). | CC p.11; 09Mar2026 deck p.3; AR p.15 | MAJOR |
| F9 | The order-book definition shifts between statements. 1-Jun: "42 crores = 33 PO + 8.5 LOI". Also on 1-Jun: "carry-forward 20, 22 + fresh 18 to 20", and "80% of the order booking has been concluded" (CC p.5, p.7). BHEL's Rs 18.05 Cr came on 15-Jun. The 9-Jul update reports "executable ~Rs 40 Cr" plus "~Rs 11 Cr confirmations". The disclosures do not reconcile the 42 + 18.05 inflow less June execution to that 40 + 11. | CC p.5 to p.7, p.17; 15Jun2026 work order; 09/10Jul2026 GBU | MAJOR |
| F10 | The tender pipeline disappears without an outcome. The Oct-2025 update cites "total bid worth INR 119 Crores on GEM Portal where result is awaited". The Mar-2026 deck shows "Tender Quoted ₹90 Crores". On the call, PSU bids are "around 40-50 crores", with "8-10 crores" awarded (CC p.26). No filing reports what happened to the Rs 119 Cr. | 16Oct2025 GBU p.1; 09Mar2026 deck p.3; CC p.26 | MAJOR |
| F11 | Single-customer concentration. Praj alone gives "13 to 14 crores" a year (CC p.12, p.18), which is 24% to 26% of FY26 revenue. Its ARC was still under price renegotiation on 1-Jun. The Feb-2025 update said the ARC would "ensure continuous flow of orders". The AR's largest vertical is ethanol, breweries and wastewater at 30.81%, above shipbuilding and repair at 24.51%. | CC p.12, p.18, p.22; 01Feb2025 GBU p.1; AR p.23 | MAJOR |
| F12 | Volunteered negative. The Rs 20 to 22 Cr carried-forward book goes out at low margin, because PSU orders carry no escalation (CC p.15). GD: "a 10 crore order can flip to a 3-4 crore loss" (CC p.16). | CC p.15 to p.16 | MAJOR |
| F13 | Rs 10 to 12 Cr of finished goods held back from a private shipyard to force a price revision (CC p.5 to p.6). This carries customer-dispute risk. The AR repeats the figure. | CC p.5 to p.6; AR p.23 | MINOR |
| F14 | Within-call inconsistency on escalation clauses. On p.6: "no PSU units ... any price variation" and the private-shipyard order still needs a revision. On p.16: "we have put a price escalation clause" for later private shipsets. The analyst flags the conflict (p.16). | CC p.6, p.16 to p.17 | MINOR |
| F15 | Narrative drift on exports and data centres. GD: "I am not trying to focus on export market as of now" (CC p.10). The company earlier commissioned a 6,000 sq ft export-dedicated unit (16Oct2025 GBU p.4). GD had "not scouted for any, in India, for data centers" (CC p.28). Three months later the AR says "We also intend to pursue emerging opportunities in data-centre cooling" (AR p.24). | CC p.10, p.28; 16Oct2025 GBU p.4; AR p.24 | MINOR |
| F16 | The same small capex keeps slipping and changing count. Mar-2026: a VMC plus 4 test benches, "installed ... 10th March 2026 and ... 25th March 2026". Jun-2026: 2 VMCs plus 5 benches "within the next 25 days", also given as "7 new machines", Rs 1.25 Cr. Jul-2026: 2 VMCs plus 6 benches, "POs placed and advances released". Aug-2026 AR: "planned deployment of four automated test benches and a new VMC". | 09Mar2026 deck p.3; CC p.4, p.8, p.13; 09Jul2026 GBU p.2; AR p.15 | MINOR |
| F17 | Unverifiable promotional claims. "supplying all the valves through both the shipyards for FSS" (CC p.15); filed FSS orders come via BHEL, Shree, Muller-BBM and L&T. "90% capacities [of foundries] are dedicated to Rappid" (CC p.21). "India's building more than 20 warships" and "next 20 years" (CC p.21). | CC p.15, p.21; work orders | MINOR |
| F18 | Cluster of filing corrections: a PIT disclosure value error (16Jan2026); an NSE query on a segment discrepancy in the H1 results (19Jan2026); a corrigendum to the postal ballot notice (30Mar2026); a Q1 FY27 "Revenue from Operations" to "Sales" relabel (10Jul2026). The FY26 results note calls the variation approval an "EGM held on April 17, 2026", but the vote was a postal ballot, with results on 30Apr2026. The CS changed in Feb-2025, Feb-2026 and Mar-2026. | named filings | MINOR |
| F19 | Margin guidance deferred: "when we connect again ... after 6 months, you'll have a better, clear picture" (CC p.13). | CC p.13 | MINOR |
| F20 | Receivables deflection: "I would not use the word delay" (CC p.27). Receivables over 6 months stand at Rs 207.1 L, and unbilled at Rs 161.3 L (27May2026 results p.9). | CC p.23, p.27; results p.9 | MINOR |
| F21 | Volunteered negative: new entrants took orders last year ("whatever orders we have lost", CC p.28). | CC p.28 | MINOR |
| F22 | No raw-material hedge. Hedging "requires huge working capital ... 15-20 crores, that's not something I'm looking at" (CC p.26). The FY26 excuse therefore can repeat. | CC p.26 | MINOR |
| F23 | Silence ahead of the miss. The order book fell from Rs 24.64 Cr (Jun-2025) to Rs 20.19 Cr (Sep-2025). The Oct-2025 update led with certifications and did not flag the decline. | 03Jul2025 GBU p.2; 16Oct2025 GBU p.1 | MAJOR |
| P1 | Peer timing tension on the central FY26 excuse. On 17-Mar-2026, KSB treats the commodity spike as prospective: "there is a chances of the spike in commodity prices ... we are watching very carefully" (KSB-Concall_Mar_2026 p.9). By Aug-2026, KSB describes foundry increases of 12% to 15% over "last 6 months or maybe last 3 months" (KSB-Concall_Aug_2026 p.24). Rappid dates its shock to H2 FY26 (Oct-2025 to Mar-2026), and its order book was already falling by Sep-2025 (F23). [INFERENCE] Order intake weakened before the peer-dated commodity shock, so the excuse explains at most part of the H2 miss. Caveat: KSB is mainly ferrous, and Rappid's shock is non-ferrous (NAB, copper). | KSB Mar-2026 p.9; KSB Aug-2026 p.24; CC p.4 to p.5 | MAJOR |
| P2 | Peer corroboration: KSB says its domestic project business runs "without PVC" (price-variation clause) with long deliveries (KSB Mar-2026 p.9 to p.10). This supports Rappid's no-escalation PSU claim. | KSB Mar-2026 p.9 to p.10 | MINOR |
| P3 | Peer ballpark on content share. KSB puts pumps at "3% to 5% ... of the total value of the project", including marine and data centres (KSB Aug-2026 p.25). This is comparable to Rappid's 2% to 3% valve share of a vessel (CC p.25). | KSB Aug-2026 p.25 to p.26 | MINOR |
| P4 | Peer corroboration of the niche. Meson: fewer than 5% of Indian valve makers are non-ferrous, and "nonferrous, they have better margins". It ran near 100% utilisation on domestic defence demand (QUESTFLOW-Concall_Jun_2024 transcript around lines 247 to 249, 316 to 318, 1076 to 1080). | QUESTFLOW Jun-2024 | MINOR |

Independent list: 27 items. Material (CRITICAL + MAJOR): 14. CRITICAL: 0. No repeated evasion across 2 or more
quarters can be tested, because only one company call exists.

---

## PART 2: COMPARISON AGAINST THE PIPELINE (B05, B06)

| # | Status | Where the pipeline has it / what is missing |
|---|---|---|
| F1 | CAUGHT | B05 2A row 1, 4D row 1, 3C row 3. B05 does not credit the 46.9% H1 FY26 growth that partly backs "we were on track" |
| F2 | CAUGHT | B05 1B, 2C Consistency, 1C "quiet drop", 4D |
| F3 | CAUGHT | B05 1C (foundry, capex), 2A rows 2-3, 4D row 2 |
| F4 | MISSED | B05 does not mention the Rs 3.65 Cr misstatement and retraction, the audited Rs 179.4 L capex, or the bank-loan-for-capex against the IPO-capex-to-WC swap |
| F5 | MISSED | B05 2D notes negative CFO only as an AR risk-table silence. It does not test the results note's "higher order volumes" explanation against +2.1% revenue and the held inventory |
| F6 | PARTIALLY CAUGHT | B05 1B (funding "in 4 or 5 months"), 4B Q6 (advances as a peer question). Absent from the 4D red-flag table. "No working capital is enough" not quoted |
| F7 | CAUGHT | B05 1C, 4A row 3, 4D (Medium). The Oct-2025 "testing done, exclusive" versus Jun-2026 "awaiting lab results" contradiction is implicit, not stated |
| F8 | CAUGHT | B05 3C row 1, 4D. The unit-capacity drift (29,625 to 33,500) is not noted |
| F9 | PARTIALLY CAUGHT | B05 3D lists each figure but does not flag that the definitions change and do not reconcile |
| F10 | MISSED | The Rs 119 Cr GeM pipeline (Oct-2025) and its outcome appear nowhere in B05 |
| F11 | PARTIALLY CAUGHT | B05 3D and 4A row 4 treat Praj as a repricing trigger, not as ~25% single-customer concentration under renegotiation |
| F12 | CAUGHT | B05 4A row 5 |
| F13 | CAUGHT | B05 4A row 1 "Kills" column |
| F14 | PARTIALLY CAUGHT | B05 3B reports the reconciled version (PSU no, private yes) and does not name the within-call reversal |
| F15 | MISSED | B05 1C lists domestic data centres as a dropped trigger. The AR (p.24), which B05 says it read, names data-centre cooling as intended. The export-focus contradiction is absent |
| F16 | PARTIALLY CAUGHT | B05 2A row 2 and 1C mention repeated VMC/bench announcements. The Mar-2026 install dates and count drift are missing |
| F17 | PARTIALLY CAUGHT | B05 3B flags "20 warships" as unverified. The FSS "all the valves" and foundry-dedication claims are not flagged |
| F18 | PARTIALLY CAUGHT | B05 4C has the GBU relabel and CS churn. The PIT correction, NSE segment query, corrigendum and "EGM" mislabel are missing. B05 itself repeats "17-Apr-2026 EGM" |
| F19 | CAUGHT | B05 4A row 5, 4B Q2 |
| F20 | PARTIALLY CAUGHT | B05 4B Q1 hands this to peers. The deflection and the >6-month bucket are not flagged |
| F21 | CAUGHT | B05 3A |
| F22 | MISSED | Absent |
| F23 | CAUGHT | B05 2B, 2D, 3D, 4D |
| P1 | MISSED | B06 2B says KSB "matches the direction" of Rappid's narrative. It does not test timing |
| P2 | MISSED | B06 Claim 1 says no peer discusses a price-escalation clause. KSB Mar-2026 does, for domestic project business |
| P3 | MISSED | B06 Claim 4 says no peer gives a per-vessel/per-project content share. KSB Aug-2026 gives 3-5% for pumps |
| P4 | PARTIALLY CAUGHT | B06 uses Meson's utilisation and margins. The non-ferrous scarcity point that backs Rappid's niche claim is not used |

Tally: caught 10, partially caught 9, missed 8 (27 total).
Material subset (14): caught 7 (F1, F2, F3, F7, F8, F12, F23); partially caught 3 (F6, F9, F11); missed 4 (F4, F5, F10, P1).

### Pipeline flags not on my list: support test

| Pipeline flag | Verdict | Reason |
|---|---|---|
| B06 FLAG-MARGIN-CONTRADICTION ("Quest Flow 23-25% EBITDA ... roughly double Rappid's ~12%"; CMD framed 12% as "structural", "where everybody in this niche ends up") | NOT SUPPORTED as framed | (1) Basis mismatch. Rappid's 12.17% is PAT margin. Its FY26 EBITDA margin is 19.4% (AR p.6: EBITDA Rs 10.31 Cr on Rs 53.23 Cr). On a like basis the gap is 23.6-25.0% vs 19.4% EBITDA and 14.3-14.85% vs 12.17% PAT. That is about 2.5 to 5.5 points, not "double". (2) The transcript has no "structural" or "floor" framing. GD says "nobody likes to be at the 12% margin point ... We are trying to improvise our margins" (CC p.13), which is the opposite. A residual reading survives: Meson earns a few points more in the same niche. |
| B05 4D "Jul-2025 'further acceleration' claim followed by 24.9% H2 decline" (High), 2A "MISSED" | OVERSTATED | Q2 FY26 revenue was ~Rs 17.19 Cr (H1 Rs 2,882.2 L less Q1 "sales" Rs 11.63 Cr), up from Rs 11.63 Cr in Q1. The quarter right after the claim did accelerate. H2 then fell. The correct grade is MIXED, and the tally becomes delivered 1, partial 2, missed 2. Caveat: the Q1 FY26 figure is labelled "sales" |
| B05 2C Over-promotion evidence: "framing a 2.1% growth year as a positive surprise" | NOT SUPPORTED (quote misread) | The full sentence reads "not something that our stakeholders and shareholders would have expected, but there's a reasonable reason" (CC p.4). That is an admission of disappointment |
| B05 2E "two analysts independently pressed the same capacity inconsistency" | OVERSTATED (minor) | Chintan Parikh asked whether 85% utilisation caused low growth (CC p.8). Only Nishita Shanklesha pressed the arithmetic (CC p.11) |
| B05 all other 4D rows (foundry abandonment, US stall, capacity, Sep-2025 order-book decline, GBU relabel, CS churn, AR omission of FY27 figure) | SUPPORTED | Verified against the anchors above |
| B06 Claims 1, 3 partially verified; Claims 5, 6 unverifiable | SUPPORTED | Anchors check. Minor: ATAM's capacity is stated both "per month" (Apr-2024 line 133) and "per day" (line 370 to 374). B06 uses per month without noting the conflict |
| B06 Claim 4 "Peers silent: no per-vessel cost percentage" | PARTIALLY WRONG | KSB Aug-2026 p.25 gives 3-5% of project value for pumps (P3) |

---

## PART 3: PROMISE-DELIVERY SPOT CHECKS (B05 2A)

| # | Promise (source) | Pipeline outcome | Check | Result |
|---|---|---|---|---|
| 1 | 50% volume CAGR FY26 (01Feb2025 GBU p.2) | MISSED | The promise is in the source. Revenue +2.1% (27May2026 results p.8). Volume data is NOT FOUND, so revenue stands in as the proxy | CONFIRMED |
| 2 | Pune foundry acquisition (01Feb2025 GBU p.1) | MISSED / ABANDONED | Rs 400 L moved to WC (21Mar2026 Annexure I). Reason: "unable to tap the right opportunity" (24Mar2026 notice p.18) | CONFIRMED |
| 3 | Capex completion by June 2025 (01Feb2025 GBU p.1) | PARTIAL | Rs 364.51 L unspent and moved to WC. Equipment still being ordered in Mar, Jun and Jul 2026. PARTIAL is lenient but defensible, given the Jul-2025 facility commissioning | CONFIRMED |
| 4 | "Anticipates further growth acceleration in the forthcoming quarters" (03Jul2025 GBU p.1) | MISSED | Q2 FY26 ~Rs 17.19 Cr vs Q1 Rs 11.63 Cr: acceleration delivered. H2 FY26 -24.9% YoY. Outcome is MIXED, not MISSED | WRONG (overgraded) |
| 5 | Quarterly business updates (CC p.30) | DELIVERED | 09Jul2026 GBU issued, revised 10Jul2026 | CONFIRMED |

Checked 5, confirmed 4, wrong 1.

---

## PART 4: CREDIBILITY GRADE

B05 grade: C. Verifier view: concur at C. Two effects offset. The missed items push lower: the live capex misstatement (F4), the written WC explanation that contradicts the call (F5), and the pipeline figure that vanished (F10). The overgraded Jul-2025 item pushes higher, as do the H1 FY26 +46.9% print and the four filed FSS orders in Q1 FY27. Net, C holds.

Operator action items (flag only, decision stays human):
1. Put the capex-funding swap (F4) and the Rs 119 Cr pipeline outcome (F10) into the Halt 1 extraction annex. Ask the company directly.
2. Withdraw or restate the B06 margin-contradiction flag on a like-for-like basis before it reaches FTTCP or Role 3.
3. Correct the B05 promise tally to delivered 1, partial 2, missed 2.

---

```yaml
stage: B12b
company: "RAPPID"
run_date: "2026-09-19"
model: "claude-opus-5"
status: complete
independent_flags_found: 27
caught: 10
partially_caught: 9
missed:
  - {severity: "MAJOR", item: "CMD misstated FY26 capex as ~Rs 3.65 Cr then retracted; audited capex Rs 179.4 L; 3.65 Cr equals unspent IPO capex balance (Rs 364.51 L); current capex funded by bank WC loan while IPO capex money moved to WC", anchor: "Concall_Jun_2026 p.12, p.22; 27May2026 results p.10; 21Mar2026 board outcome Annexure I"}
  - {severity: "MAJOR", item: "FY26 results note attributes WC build to 'execution of higher order volumes' while revenue +2.1% and CMD says Rs 10 Cr material held undispatched; CFO -Rs 1,082.6 L", anchor: "27May2026 results p.9-10; Concall_Jun_2026 p.5-6"}
  - {severity: "MAJOR", item: "Rs 119 Cr GeM bid pipeline (Oct-2025) never reported on; deck shows Rs 90 Cr quoted (Mar-2026); call gives PSU bids Rs 40-50 Cr with Rs 8-10 Cr won", anchor: "16Oct2025 GBU p.1; 09Mar2026 deck p.3; Concall_Jun_2026 p.26"}
  - {severity: "MAJOR", item: "Peer timing tension: KSB treats commodity spike as prospective in Mar-2026; Rappid dates its shock to H2 FY26 while its order book already fell by Sep-2025 [INFERENCE; ferrous-peer caveat]", anchor: "KSB-Concall_Mar_2026 p.9; KSB-Concall_Aug_2026 p.24; 16Oct2025 GBU p.1"}
  - {severity: "MINOR", item: "Export/data-centre narrative drift: CMD 'not trying to focus on export' and 'not scouted' Indian data centres vs export-dedicated unit and AR intent to pursue data-centre cooling; B05 lists data centres as dropped", anchor: "Concall_Jun_2026 p.10, p.28; 16Oct2025 GBU p.4; AR 2026 p.24"}
  - {severity: "MINOR", item: "No raw-material hedge; hedging needs Rs 15-20 Cr WC, so the FY26 excuse can repeat", anchor: "Concall_Jun_2026 p.26"}
  - {severity: "MINOR", item: "KSB confirms domestic project business runs without PVC clause (corroborates Rappid PSU claim); B06 says peers silent", anchor: "KSB-Concall_Mar_2026 p.9-10"}
  - {severity: "MINOR", item: "KSB gives 3-5% content share of project value for pumps incl. marine; B06 says no peer gives a share", anchor: "KSB-Concall_Aug_2026 p.25-26"}
pipeline_flags_not_supported:
  - "B06 FLAG-MARGIN-CONTRADICTION: compares Quest Flow EBITDA 23-25% with Rappid PAT 12.17% (Rappid EBITDA is 19.4%, AR 2026 p.6); CMD never framed 12% as structural (Concall p.13). Like-for-like gap is ~2.5-5.5 pts, not 'double'"
  - "B05 2C over-promotion evidence misreads Concall p.4: 'not something ... would have expected, but there's a reasonable reason' is an admission, not a positive-surprise framing"
  - "B05 4D/2A Jul-2025 'further acceleration' graded MISSED/High: OVERSTATED, since Q2 FY26 ~Rs 17.19 Cr vs Q1 Rs 11.63 Cr accelerated before H2 fell; correct grade MIXED"
promise_delivery_spot_checks: {checked: 5, confirmed: 4, wrong: 1}
credibility_grade_concur: "concur at C: missed capex, WC and pipeline items lean lower; the overgraded Jul-2025 item and the H1 FY26 +46.9% print lean higher; net C holds"
findings:
  - {severity: "MAJOR", location: "B05 (absent)", claimed: "no capex-funding flag", source_truth: "CMD Rs 3.65 Cr vs audited Rs 179.4 L; capex on bank WC loan while IPO capex moved to WC", note: "MISSED; Concall p.12, p.22; results p.10"}
  - {severity: "MAJOR", location: "B05 2D", claimed: "negative CFO noted only as AR risk silence", source_truth: "results note says WC build from 'higher order volumes' vs +2.1% revenue and held inventory", note: "MISSED; results p.9-10"}
  - {severity: "MAJOR", location: "B05 3D", claimed: "pipeline not tracked", source_truth: "Rs 119 Cr GeM bids (Oct-2025) with no outcome disclosed", note: "MISSED; 16Oct2025 GBU p.1"}
  - {severity: "MAJOR", location: "B06 2B", claimed: "KSB matches direction of Rappid commodity narrative", source_truth: "KSB treats the spike as prospective in Mar-2026; timing does not back an Oct-2025 start", note: "MISSED; inference with ferrous caveat"}
  - {severity: "MAJOR", location: "B06 flags / Part 4", claimed: "Quest Flow margin roughly double Rappid ~12%; CMD framed 12% as structural", source_truth: "Rappid EBITDA 19.4%, PAT 12.17%; CMD said he wants to improve from 12%", note: "NOT SUPPORTED as framed; basis mismatch"}
  - {severity: "MAJOR", location: "B05 4D", claimed: "WC stress not in red-flag table", source_truth: "'no working capital is enough', 50% supplier advances, funding need in 4-5 months, ST debt Rs 841.4 L to Rs 1,784.3 L", note: "PARTIALLY CAUGHT"}
  - {severity: "MAJOR", location: "B05 3D", claimed: "order-book figures listed", source_truth: "definitions shift (PO/LOI/carry-forward/executable/confirmations) and do not reconcile after the BHEL Rs 18.05 Cr win", note: "PARTIALLY CAUGHT"}
  - {severity: "MAJOR", location: "B05 3D, 4A", claimed: "Praj as repricing trigger", source_truth: "Praj Rs 13-14 Cr/yr, ~24-26% of FY26 revenue, ARC under renegotiation", note: "PARTIALLY CAUGHT; concentration unflagged"}
  - {severity: "MINOR", location: "B05 2A row 4, 4D", claimed: "Jul-2025 acceleration MISSED (High)", source_truth: "Q2 FY26 ~Rs 17.19 Cr vs Q1 Rs 11.63 Cr; H2 -24.9%", note: "OVERSTATED; tally becomes 1/2/2"}
  - {severity: "MINOR", location: "B05 2C", claimed: "positive-surprise framing of 2.1% growth", source_truth: "Concall p.4 admits shortfall", note: "quote misread"}
  - {severity: "MINOR", location: "B05 2E", claimed: "two analysts pressed capacity math", source_truth: "only Nishita Shanklesha pressed the arithmetic (p.11)", note: "overstated"}
  - {severity: "MINOR", location: "B05 1C, 2A", claimed: "17-Apr-2026 EGM", source_truth: "approval by postal ballot, results 30-Apr-2026", note: "company filing error transcribed"}
  - {severity: "MINOR", location: "B05 1C", claimed: "domestic data-centre dropped", source_truth: "AR 2026 p.24 names data-centre cooling as intended", note: "MISSED narrative drift, with export-focus contradiction"}
  - {severity: "MINOR", location: "B05 (absent)", claimed: "", source_truth: "no hedging; Rs 15-20 Cr WC needed to hedge", note: "MISSED; Concall p.26"}
  - {severity: "MINOR", location: "B05 3B", claimed: "PSU no clause, private clause", source_truth: "within-call reversal p.6 vs p.16", note: "PARTIALLY CAUGHT"}
  - {severity: "MINOR", location: "B05 1C", claimed: "repeat VMC/bench announcements", source_truth: "Mar-2026 install dates missed; counts drift 4 to 5 to 6 benches, 1 to 2 VMCs", note: "PARTIALLY CAUGHT"}
  - {severity: "MINOR", location: "B05 3B", claimed: "20 warships unverified", source_truth: "FSS 'all the valves' and 90% foundry-dedication claims also unverifiable", note: "PARTIALLY CAUGHT"}
  - {severity: "MINOR", location: "B05 4C", claimed: "GBU relabel, CS churn", source_truth: "also PIT correction, NSE segment query, ballot corrigendum, results-note mislabels", note: "PARTIALLY CAUGHT"}
  - {severity: "MINOR", location: "B05 4B Q1", claimed: "PSU receivables handed to peers", source_truth: "'I would not use the word delay'; Rs 207.1 L over 6 months", note: "PARTIALLY CAUGHT"}
  - {severity: "MINOR", location: "B06 Claim 1", claimed: "no peer discusses escalation clause", source_truth: "KSB Mar-2026 p.9-10 domestic project business without PVC", note: "MISSED corroboration"}
  - {severity: "MINOR", location: "B06 Claim 4", claimed: "no peer gives content share", source_truth: "KSB Aug-2026 p.25 pumps 3-5% of project value", note: "MISSED"}
  - {severity: "MINOR", location: "B06 Claim 2", claimed: "Meson margins used", source_truth: "Meson: <5% of Indian valve makers non-ferrous, non-ferrous better margins", note: "PARTIALLY CAUGHT; niche corroboration unused"}
critical_count: 0
major_count: 8
minor_count: 14
material_found: 14
material_caught: 10
acceptance_rate: 71
coverage_basis: "14 material of 27 listed; 7 caught fully + 3 partially caught = 10 counted as caught (pipeline had them, under-weighted); strict full-catch rate 7/14 = 50%. Company call read in full; peer set 8 transcripts read by targeted search, not cover to cover"
```
