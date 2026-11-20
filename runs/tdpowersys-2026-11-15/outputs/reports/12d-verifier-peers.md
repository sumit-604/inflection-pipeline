# Verifier D: peer coverage audit of B06, TDPOWERSYS, run 2026-11-15

Method: read B06 (06-peers.md and its block), the 12 peer_questions in B05, and searched the 12 page-marked peer .txt files. Spot-checked quotes were located at the stated source. Page numbers were not re-counted file by file; quote text and speaker were matched.

## Coverage audit per peer (all 12 marked SUBSTANTIVE)

| Peer / quarter | Citation located in transcript | Result |
|---|---|---|
| CGPOWER Q2 FY26 | Power PBIT 310 bps "better price realization" (txt l.105-106); rail commodity pass-through lag (l.92-94) | Confirmed |
| CGPOWER Q3 FY26 | 378 bps price realization (l.99); "kind of slowed down" on duty (l.459) | Confirmed |
| CGPOWER Q4 FY26 | 287 bps (l.130); 90 to 100 days (l.319); 17.5% price increase (l.473); tap changers 9-12 months (l.496); FAS Mumbai (l.217) | Confirmed |
| CGPOWER Q1 FY27 | backlog Rs 17,333 cr, +45% (l.64, 71); further price rise after 17.5% (l.163) | Confirmed |
| TRITURBINE Q2 FY26 | finalised US orders kept out of book (l.283-285); "56 -odd percent" tariff (l.964) | Confirmed |
| TRITURBINE Q3 FY26 | gas turbine makers "booked out for five" years (l.631); "double-digit growth in top line" (l.705) | Confirmed |
| TRITURBINE Q4 FY26 | 84 days vs 49 (l.215); "not a correct number right now" (l.670) | Confirmed |
| TRITURBINE Q1 FY27 | orders lower 35.4% (l.177); GT delivery 3 to 4 to 5 years (l.477); "what we get is what our competitors get" (l.812-813) | Confirmed |
| AZAD Q2 FY26 | "Azad is going to bear the 5%" (l.387) | Confirmed |
| AZAD Q3 FY26 | "pricing decisions are not being done" (l.492); 150 to 200 people per month (l.563) | Confirmed |
| AZAD Q4 FY26 | 8-year contract (l.127); "fully booked for next 10 years" is analyst text (l.306); "not dependent on any single customer" (l.197) | Confirmed |
| AZAD Q1 FY27 | debtors "170, 180 days" (l.454) | Confirmed |

Zero hits for "generator", "alternator", "TD Power" across all 12 files (grep count), matching B06's peer-set limit.

UNUSED / CITED-ONLY peers: none in B06. Spot-read for missed claim-relevant material: searched for capacity doubling/tripling, slot reservation, machine-tool lead times. No peer statement on any of these exists, so nothing directly claim-relevant was left unused. Q2 and Q6 verdicts (PARTIALLY VERIFIED on OEM sold-out status; UNVERIFIABLE) are consistent with the search.

## Verdict-discipline audit per claim

| Q | B06 verdict | Independent peer anchors | Check |
|---|---|---|---|
| 1 | PARTIALLY VERIFIED | Triveni, CG | OK |
| 2 | PARTIALLY VERIFIED | Azad, Triveni; capacity figures have no anchor, stated | OK |
| 3 | PARTIALLY VERIFIED | Azad, Triveni | OK |
| 4 | PARTIALLY VERIFIED | CG, Azad, Triveni | OK |
| 5 | UNVERIFIABLE | none about TD; not upgraded | OK |
| 6 | UNVERIFIABLE | none; not upgraded | OK |
| 7 | VERIFIED | CG, Azad, Triveni (see finding 1) | OK with MINOR |
| 8 | PARTIALLY VERIFIED | Azad (match), CG, Triveni (different mechanism) | OK |
| 9 | CONTRADICTED | Triveni, CG against; Azad for; weighting by product type argued | OK |
| 10 | PARTIALLY VERIFIED | CG, Triveni, Azad | OK |
| 11 | PARTIALLY VERIFIED | Triveni, CG | OK |
| 12 | PARTIALLY VERIFIED (adjacent only) | CG, Triveni, Azad; no peer covers generators | OK; UNVERIFIABLE would also be defensible |

No verdict is upgraded from silence. Only Q7 is VERIFIED, and it has at least two peers on each tier.

## Claim completeness
All 12 peer_questions in B05 appear in B06 Part 1 (Q1-Q12) with text matching the B05 list and a verdict. claims_all_addressed: true.

## Findings
1. MINOR. Q7 VERIFIED: "OEMs raise prices" rests on CG alone (Azad's premise was an analyst's; Triveni declines to push price). B06 flags direction only. PARTIALLY VERIFIED is the stricter label.
2. MINOR. B06 pools CG margin gains of 280-380 bps as price-led (Part 4, 2B, cross-peer hypothesis). CG Q4 FY26 gives operating leverage and execution for the 287 bps, not price. The hypothesis holds on Q2 and Q3 (310, 378 bps) but the range overstates price.

Counts: critical 0, major 0, minor 2. Acceptance 12 of 12 = 100%.

```yaml
stage: B12d
company: "TDPOWERSYS"
run_date: "2026-11-15"
model: claude-sonnet-5-5
status: complete
peers_audited: 12
substantive_confirmed: 12
substantive_unsupported: []
unused_but_relevant: []
claims_all_addressed: true
verdict_discipline_fails: []
findings:
  - {severity: MINOR, item: "Q7 VERIFIED: first half rests on CG alone; PARTIALLY VERIFIED stricter", anchor: "AZAD Q3 FY26 txt l.492; CGPOWER Q2 FY26 txt l.105-106"}
  - {severity: MINOR, item: "B06 pools CG 280-380 bps as price-led; Q4 FY26 287 bps attributed to operating leverage", anchor: "CGPOWER Q4 FY26 txt l.128-131"}
critical_count: 0
major_count: 0
minor_count: 2
acceptance_rate: 100
```
