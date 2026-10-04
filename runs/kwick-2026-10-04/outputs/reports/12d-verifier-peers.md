# VERIFIER D: PEER COVERAGE AUDIT. KWICK, run 2026-10-04

Scope: B06 (06-peers.md, B06-peers.yaml) against the peer transcripts and B05 peer_questions. The task named 11 transcripts (4 ZENTEC, 4 ADSL, 3 DSSL), not 12. All 11 were audited. Page convention: the [page N] marker precedes the text of page N. Hits were found by full-text search and reading of the surrounding lines.

## Coverage audit table (per peer call)

| Peer call | B06 usage | Citation found in transcript | Result |
|---|---|---|---|
| ZENTEC Oct-2025 (Q2 FY26) | SUBSTANTIVE | EP orders "before March of 2026" (line 617, p17); H1 Rs 235.71 Cr vs 495.64 Cr (line 94, p4); government "extreme" delay (line 69) | CONFIRMED |
| ZENTEC Feb-2026 (Q3 FY26) | SUBSTANTIVE | "Foxconn ... Apple" (p8); anti-drone margins lower than simulators (p12); "pace" remark (p13); Rs 931 Cr in four months (p4) | CONFIRMED |
| ZENTEC May-2026 (Q4 FY26) | SUBSTANTIVE | DSO 119 vs 161 (p9); Q4 Rs 178.1 Cr vs Rs 325 Cr, FY Rs 687.7 Cr vs 973.6 Cr (p8); warranty Rs 3.1 Cr (p8); outsourced build (p16); WC 196 (p9) | CONFIRMED |
| ZENTEC Jul-2026 (Q1 FY27) | SUBSTANTIVE | 72.9% gross, Rs 7.65 Cr release, Rs 2.88 Cr warranty, Rs 177.5 Cr MoD order, WC 257, debtor days 122, cash Rs 1,217 Cr, order book Rs 1,239 Cr (all p4); no simulator tenders (line 563, p15 not p16) | CONFIRMED, page drift |
| ADSL Nov-2025 (Q2 FY26) | SUBSTANTIVE | "2 weeks, 3 weeks, 4 weeks" (p11); Mumbai Rs 2,100 Cr with partner (p11); hardware commodity (p14); US 65% (p15); diversified banking (p8); subcontract (p9-10) | CONFIRMED |
| ADSL Feb-2026 (Q3 FY26) | SUBSTANTIVE | DSO 75 analyst figure (p13); "uneasiness" (p14); debtors over 3 years, audit points (p16); hardware-only single digit, 20% full cycle (p14 area); EBITDA not translating with solution mix (p23); 10% announcement threshold (line 940, p23 not p24) | CONFIRMED, page drift |
| ADSL May-2026 (Q4 FY26) | SUBSTANTIVE | Rs 36 Cr ECL (p13); Western Railway Rs 165 Cr + 85 Cr rebid, cost up 25% to 30% (line 516, p13 not p14); Mumbai announce in 2 to 3 weeks (p12); government -6% vs +31% (p5) | CONFIRMED, page drift |
| ADSL Aug-2026 (Q1 FY27) | SUBSTANTIVE | Rs 180 to 200 Cr railway exits, "silence" on large orders (p11); finance cost (p7); audit report unmodified (lines 154, 262); 25% to 30% price rise (line 428) | CONFIRMED |
| DSSL Feb-2026 (Q3 FY26) | SUBSTANTIVE | Back-to-back with Redington and Rashi (p12); no seasonality (p14); top-10 about 60% (p14-15); longer implementation cycle (p13) | CONFIRMED. Net debt Rs 68 Cr cited here is not in this call (F4). Milestone vs upfront billing is in Q4 call, not Q3 (F5) |
| DSSL Jun-2026 (Q4 FY26) | SUBSTANTIVE | Revenue Rs 402 Cr and Rs 1,424 Cr, EBITDA 10.2%, net debt Rs 68 Cr (p5); milestone vs upfront, 134 payable days, Rs 301 to 602 Cr (p10); NWC 14 to 17 days, margin 18% to 14% (p11); Rs 602 Cr (p13) | CONFIRMED |
| DSSL Aug-2026 (Q1 FY27) | SUBSTANTIVE | Revenue Rs 313 Cr vs 328 Cr, orders RBI 750, NPCI 267, CBI 125 (p4); component price rise 30% to 50% (p8); direct OEM margin "significantly lower", declarable threshold (p17) | CONFIRMED |

Result: 11 of 11 SUBSTANTIVE rows have real, findable citations. No peer is UNUSED or CITED-ONLY, so Rule 3 spot-read has no target. I still searched all 11 files for the topics B06 calls silent (BNSS, forensic, FSL, NFIES, NFSU, GeM, bank guarantee, performance bond, liquidated damages, dealer, vehicle builder, police, crime). Result matches B06: no hit on any except "police" once (Zen Jul-2026 line 482) and "guarantee" twice, both unrelated to Kwick's tender guarantees. No directly claim-relevant statement was left unused. `unused_but_relevant` is empty.

## Verdict-discipline audit per claim

| # | Claim | B06 verdict | Independent peer anchors | Audit |
|---|---|---|---|---|
| Q1 | Receivable days, buyer payment | PARTIALLY VERIFIED | Zen, ADSL, DSSL | OK. No upgrade. State police or FSL payment correctly left unanswerable |
| Q2 | Dealer and integrator channel | UNVERIFIABLE | none (adjacent only) | OK. Silence not read as support |
| Q3 | Resale vs own-IP margin, mix compression | VERIFIED | Margin band: 3. Mix compression: ADSL only | MAJOR. See F1 |
| Q4 | Tender conversion, Q4 loading | PARTIALLY VERIFIED | Zen, ADSL, DSSL | OK. DERIVED shares recomputed and correct: Zen 325/973.6 = 33.4%, 178.1/687.7 = 25.9%; DSSL 402/1,424 = 28.2%; ADSL (968 - 700)/968 = 27.7%. Note: three of four shares sit within 3 points of a flat 25%, so "direction holds" is carried by qualitative remarks (ADSL March milestones, Zen EP deadline), not by the numbers |
| Q5 | BNSS, grants | UNVERIFIABLE | none | OK. Not upgraded. Operator note overreaches (F7) |
| Q6 | Concentration, stop after big year | PARTIALLY VERIFIED | DSSL on concentration; Zen and ADSL on pause effects | OK |
| Q7 | BG, LD, bonds | UNVERIFIABLE | none | OK. Confirmed by full-text search |
| Q8 | Reg 30 disclosure | VERIFIED | Zen, DSSL, ADSL on practice | MINOR. Practice half has 3 anchors. "How soon after award" and GeM wording rest on one peer or silence (F2) |

Rule 4 (upgrade from silence): none found. No CRITICAL.
Rule 5 (peer_questions coverage): B05 lists 8 questions. B06 Part 1 gives all 8 a verdict, in the same order and wording. `claims_all_addressed: true`.
Block integrity: B06 yaml counts (2 verified, 3 partial, 3 unverifiable, 0 contradicted) match Part 1 and Part 4. Small yaml/prose mismatch: Q4 shares "26% to 34%" in prose, "26% to 33%" in yaml flag. Trivial.

## Findings

- F1 MAJOR. Q3 VERIFIED should read PARTIALLY VERIFIED. The net read claims three peers confirm that heavier hardware mix compresses margin. DSSL management says the 18% to 14% fall came from component cost, not mix (Jun-2026 p11). Zen is own IP and gives only the ceiling (72.9%). Only ADSL speaks to mix, and the dilution point comes from an analyst question that N. Shah accepts with "That is right" (Feb-2026 p23). The margin-band leg stands on three peers. B06 itself warns the compression can recur from input cost alone, which is a different mechanism from the Kwick mix story in B05.
- F2 MINOR. Q8 timing and GeM wording not covered by the VERIFIED label.
- F3 MINOR. Six page anchors off by one (list in YAML). All quotes real.
- F4 MINOR. DSSL net debt Rs 68 Cr cited to the wrong call.
- F5 MINOR. Coverage map credits DSSL Q3 with a Q4 point.
- F6 MINOR. Zen WC and cash link is B06 inference stated as a transcript fact in the cross-peer hypothesis.
- F7 MINOR. "ADSL and Zen sell to police" is not stated in the transcripts.

Acceptance: all 11 peers correctly handled at the coverage level (100%). One claim verdict needs a downgrade.

```yaml
stage: B12d
company: "KWICK"
run_date: "2026-10-04"
model: claude-sonnet-5-5
status: complete
peers_audited: 11
substantive_confirmed: 11
substantive_unsupported: []
unused_but_relevant: []
claims_all_addressed: true
verdict_discipline_fails:
  - {claim: "Q3 gross margin on resale vs own IP and mix compression", b06_verdict: "VERIFIED", should_be: "PARTIALLY VERIFIED", reason: "Margin-band leg has three peer anchors. The mix-compression leg rests on ADSL alone (Q3 FY26 p.23, analyst-led, N. Shah 'That is right'). DSSL management attributes its 18% to 14% fall to component cost, not mix (Q4 FY26 p.11). Zen is own IP and only sets the ceiling.", severity: MAJOR}
findings:
  - {id: F1, severity: MAJOR, item: "Q3 verdict VERIFIED overstates; compression leg rests on ADSL alone and DSSL denies mix as cause", anchor: "B06 Part 1 Q3; DSSL Jun-2026 p.11; ADSL Feb-2026 p.23"}
  - {id: F2, severity: MINOR, item: "Q8 VERIFIED covers practice only; timing and GeM wording unsupported by two peers", anchor: "B06 Part 1 Q8; ADSL May-2026 p.12"}
  - {id: F3, severity: MINOR, item: "Six page anchors off by one; quotes real", anchor: "ADSL Feb-2026 lines 867, 940; ADSL May-2026 line 516; ZENTEC Jul-2026 lines 482, 563; DSSL Jun-2026 line 57"}
  - {id: F4, severity: MINOR, item: "DSSL net debt Rs 68 Cr cited to Q3 call, only in Q4 call", anchor: "DSSL Feb-2026 p.6; DSSL Jun-2026 p.5"}
  - {id: F5, severity: MINOR, item: "Coverage map credits DSSL Q3 with milestone vs upfront point that is in Q4", anchor: "DSSL Feb-2026 p.13; DSSL Jun-2026 p.10"}
  - {id: F6, severity: MINOR, item: "Zen WC 257 days 'only because' of cash is B06 inference, transcript says supplier advances and inventory", anchor: "ZENTEC Jul-2026 p.4"}
  - {id: F7, severity: MINOR, item: "'ADSL and Zen sell to police' not stated in transcripts; Q5 UNVERIFIABLE verdict itself correct", anchor: "ZENTEC Jul-2026 line 482; full-text search"}
critical_count: 0
major_count: 1
minor_count: 6
acceptance_rate: 100
```
