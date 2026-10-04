# Verifier D: Peer coverage audit, MMP (run 2026-10-05)

Inputs read: B06 report and block, B05 peer_questions (8), eight peer transcripts (page-marked .txt). Method: grep each B06 quote and page anchor against the transcript text. Page rule: printed page = file marker minus 1 (confirmed on APARINDS Jun-26 "past performance", file [page 17] = printed p.16).

## Coverage audit per peer

| Peer / call | B06 usage | Citations checked and found | Result |
|---|---|---|---|
| APARINDS Nov-25 (Q2 FY26) | SUBSTANTIVE | "waiting game" (line 236), "order inflow has not been cancelled, but it's on hold" (477), "completely hedged book" (485), "absolute change in the price" (834-836) | Confirmed |
| APARINDS Feb-26 (Q3 FY26) | SUBSTANTIVE | "shift from ACSR to AL-59 ... higher EBITDA per metric ton" (105); AL-59 plus ACSR "98% of the market" (157); "not part of premium ... getting very competitive" (157) | Confirmed. Minor attribution: "conventional" label is Kushal's "Correct" reply to the analyst, not Chaitanya's words |
| APARINDS Jun-26 (Q4 FY26) | SUBSTANTIVE | "no shipments ... March. Nothing went in the month of April" (577-578); ECB mark-to-market (159); PGCIL past-performance rule (744-745) | Confirmed |
| APARINDS Jul-26 (Q1 FY27) | SUBSTANTIVE | volume "down 6.7%" and "withheld manufacturing clearance" (163-165); "AL-59 or other conventional types" (296); "exhausted that ... manufacturing clearances" (619); Hamriyah closure (207, 810-811) | Confirmed |
| MAANALU Nov-25 (Q2 FY26) | SUBSTANTIVE | "95%-98% hedged", back-to-back MCX or LME (368-374); margin add 15-18% on value-add (397-398) | Confirmed |
| MAANALU Feb-26 (Q3 FY26) | SUBSTANTIVE | "total metal is hedged" (389); 450 t lost on US cancellation to local suppliers (392, 453-459) | Confirmed |
| MAANALU Jun-26 (Q4 FY26) | SUBSTANTIVE | Gulf "standstill ... not restarted" (291); exports from India down 50%, own 30-40% (548-549) | Confirmed |
| MAANALU Aug-26 (Q1 FY27) | SUBSTANTIVE | freight "five times to 10 times" (271); under 5% unhedged (300-304) | Confirmed |
| ARFIN | UNUSED | No transcripts in the corpus | Correct handling; input gap named, nothing filled from memory |

Rule 2: no SUBSTANTIVE peer unsupported. substantive_unsupported is empty.

Rule 3 (UNUSED or CITED-ONLY): only ARFIN, with no transcript. Nothing to spot-read. I also searched all eight files for RDSS, discom, payment delay, receivable, powder (metal), foil, lidding, ABC, wire rod, insulator, FRP. Only hit was powder coating (MAANALU, a paint finish, not aluminium powder). B06's silence statements hold for Q2 and Q4 and for powder and foil.

Missed or misstated material (all MINOR, none changes a verdict):
1. B06 Q6 says "MAANALU lists no Europe growth". MAANALU Nov-25 says it is adding customers and growing in UK, Israel, Europe, Australia (lines 199-200). Qualitative only. Wrong sentence.
2. MAANALU Jun-26 p.13: Europe and US states require declaration of aluminium origin; export customers want Indian smelting origin (lines 533-545). Context for the Europe export leg.
3. APARINDS Jun-26 p.16: a private rival with carbon-score conductor is near PGCIL approval; management answers with the past-performance barrier (lines 739-745). Context for MMP's PGCIL registration.

## Verdict discipline per claim

| Q | B06 verdict | Anchors independent? | Audit |
|---|---|---|---|
| Q1 conductor offtake and pass-through | PARTIALLY VERIFIED | APARINDS (4 calls) plus MAANALU | Sound. Direction only; B06 says magnitude fails |
| Q2 payment delays | UNVERIFIABLE | none | Sound. Silence not upgraded; RDSS and discom absent in all files |
| Q3 AL59 premium | PARTIALLY VERIFIED | one peer | Sound. One peer caps at PARTIAL |
| Q4 EBITDA per tonne with and without rod | UNVERIFIABLE | none | Sound |
| Q5 approvals timing | PARTIALLY VERIFIED | two peers, direction only | Acceptable; no duration anchor, B06 states so |
| Q6 exports and price resistance | CONTRADICTED (scoped) | three anchors across two peers | Quotes real. Label stronger than adjacent evidence; B06 scopes it. MINOR |
| Q7 inventory gains | PARTIALLY VERIFIED | two peers on hedging; oil effect from one | Evidence is contrast, not verification. MINOR |
| Q8 utilisation, working capital, funding | PARTIALLY VERIFIED | two peers | Sound |

VERIFIED count is 0, so no VERIFIED rests on one peer. No verdict was upgraded from silence (CRITICAL test passes).

Rule 5: all 8 peer_questions in B05 received a verdict in B06 Part 1 (Q1 to Q8 map one to one). claims_all_addressed is true.

## Counts
Critical 0, Major 0, Minor 4 (three missed or misstated items above plus verdict calibration on Q6 and Q7, Q5 noted as acceptable). Acceptance rate 100% (3 of 3 peers handled correctly at the MAJOR bar).

```yaml
stage: B12d
company: "MMP"
run_date: "2026-10-05"
model: claude-sonnet-5-5
status: complete
peers_audited: 3
substantive_confirmed: 2
substantive_unsupported: []
unused_but_relevant:
  - {peer: "MAANALU", missed_item: "Nov-25 call says it is adding customers and growing in UK, Israel, Europe, Australia; B06 Q6 states 'MAANALU lists no Europe growth' (misstatement, qualitative)", anchor: "MAANALU-Concall_Nov_2025_Transcript.txt lines 199-200"}
  - {peer: "MAANALU", missed_item: "Europe and US states require declaration of aluminium origin; Indian smelting origin preferred", anchor: "MAANALU-Concall_Jun_2026_Transcript.txt lines 533-545, printed p.13 of 14"}
  - {peer: "APARINDS", missed_item: "Private rival with carbon-score conductor close to PGCIL approval; past-performance barrier answer", anchor: "APARINDS-Concall_Jun_2026_Transcript.txt lines 739-745, file p.17"}
claims_all_addressed: true
verdict_discipline_fails: []
findings:
  - {severity: MINOR, finding: "B06 Q6 says MAANALU lists no Europe growth; MAANALU Nov-25 says it is adding customers and growing in Europe. Verdict unchanged.", anchor: "MAANALU Nov-25 lines 199-200"}
  - {severity: MINOR, finding: "Q6 CONTRADICTED rests on non-powder peers; scoped by B06, quotes real, label stronger than adjacent evidence.", anchor: "B06 Part 1 Q6"}
  - {severity: MINOR, finding: "Q7 PARTIALLY VERIFIED is a contrast (peers hedged), not verification of MMP's 2-2.5 Cr gain.", anchor: "B06 Part 1 Q7"}
  - {severity: MINOR, finding: "Q5 PARTIALLY VERIFIED is direction only; stated by B06; acceptable.", anchor: "B06 Part 1 Q5"}
critical_count: 0
major_count: 0
minor_count: 4
acceptance_rate: 100
```
