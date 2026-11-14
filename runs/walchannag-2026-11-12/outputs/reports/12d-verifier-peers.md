# Verifier D: Peer Coverage Audit. WALCHANNAG, 2026-11-12

Method: read B06 Parts 1-4, then grep-checked B06 citations against the page-marked .txt files in inputs/peer-concalls/. About 45 distinct figures/quotes checked. All located.

## Coverage audit per peer (all 12 marked SUBSTANTIVE)
| Peer-quarter | Spot-checked citation | Found |
|---|---|---|
| MTAR Q3 FY26 | book 2,394; inflow 1,370; NWC 260; End Shield/Calandria 350-400 Cr | Yes (Feb txt l.129-130, 233, 741) |
| MTAR Q4 FY26 | book 2,580 vs guide; "already qualified for Calandrias and End shield"; ASHVINI tenders this year; NWC 172 vs 278 | Yes (May txt l.116, 179, 743-744) |
| MTAR Q1 FY27 | book 5,143 plus 800; 1-year process, orders next FY; receivables 140 to 82, inventory 208 to 145; NWC 59 | Yes (Aug txt l.219, 270, 355, 563-565) |
| MTAR Q2 FY27 | EBITDA 24.4% on 406.8; H1 inflow 4,102 (inaudible); 700-1,000 Cr share of 4 reactors; 50 NWC days; quotations to private players | Yes (Nov txt l.106, 245, 142, 448, 554) |
| ISGEC Q3 FY26 | book 7,649; Shanti Bill question | Yes (Feb txt l.141, 538) |
| ISGEC Q4 FY26 | 550 Cr cancelled; 165 Cr FGD left; forex 103 Cr | Yes (Jun txt l.163, 380, 292) |
| ISGEC Q1 FY27 | 130 Cr on hold; 502 Cr programme; 4 years becoming 6 | Yes (Aug txt l.272, 312, 506) |
| ISGEC Q2 FY27 | 4,844 vs "4,400-plus"; book 8,757; EBIT 13.7% and 5.7%; 502/199 Cr | Yes (Nov txt l.126-127, 154-155, 161-163, 283). Internal conflict correctly flagged by B06 |
| ELECON Q3 FY26 | 40% organised share; metal "almost stagnant"; McNally/TRF | Yes (Jan txt l.323, 602, 430) |
| ELECON Q4 FY26 | nuclear "No, we don't"; 56-60% utilisation; 720 Cr receivables; 70 Cr impact; goodwill 102 Cr | Yes (Apr txt l.540, 339, 480, 474, 192) |
| ELECON Q1 FY27 | fabricated gear case +6-7%; "abnormal" price rise; 70 Cr not converted | Yes (Jul txt l.444, 572, 716) |
| ELECON Q2 FY27 | EBITDA 23.1%; gear EBIT 22.1%; books 1,056 and 579; WC 89 vs 98 days; TRF closed; P-17 Bravo order Q1 FY29, single bidder | Yes (Oct txt l.189, 205, 215, 228, 239, 593, 349-363). B06 calls it "P-17 Bravo follow-on"; speaker says follow-on of P17 Alpha for the Bravo order. Reading is fair |

substantive_confirmed 12 of 12. No MAJOR under rule 2.

## Rule 3: unused or cited-only
None marked UNUSED or CITED-ONLY. Spot-read for missed claim-relevant items (nuclear tenders, margin, receivables, retention in the MTAR Q1/Q2 and ISGEC Q2 files): none found left unused.

## Rule 4: verdict discipline
| Claim | B06 verdict | Peers anchoring | Finding |
|---|---|---|---|
| Q1 | VERIFIED (benchmark); order-book reconciliation UNVERIFIABLE | 3 | OK. Split verdict is honest |
| Q2 | PARTIALLY VERIFIED | MTAR only (ISGEC vague, ELECON "No") | OK. Correctly not VERIFIED |
| Q3 | PARTIALLY VERIFIED | 2 | OK |
| Q4 | VERIFIED | 3 | OK |
| Q5 | PARTIALLY VERIFIED | 2 | OK |
| Q6 | VERIFIED capex direction/late delivery; customer-funded UNVERIFIABLE | 3 | OK; MINOR wording (peer slips, not WIL evidence) |
| Q7 | PARTIALLY VERIFIED | 3 | OK |
| Q8 | PARTIALLY VERIFIED | ISGEC (ELECON adjacent) | OK; MINOR: Part 4 "unverifiable whole: 0" vs YAML listing state-utility as unverifiable |

No VERIFIED rests on one peer. No upgrade from silence; silences are recorded (Peers silent rows, unverifiable list).

## Rule 5: peer_questions coverage
B05 lists 8 questions; B06 Q1-Q8 map one to one in order. claims_all_addressed: true.

## Findings
- MINOR: Q8 labelling inconsistency (above).
- MINOR: MTAR "60 to 70% share" line follows an inaudible marker (Aug txt l.679) and reads as a loose tag. B06 flags the marker; FLAG-INCUMBENT still leans on it.
- MINOR: Q6 wording.

Counts: CRITICAL 0, MAJOR 0, MINOR 3. Acceptance 100%.

```yaml
stage: B12d
company: "WALCHANNAG"
run_date: "2026-11-12"
model: claude-sonnet-5-5
status: complete
peers_audited: 12
substantive_confirmed: 12
substantive_unsupported: []
unused_but_relevant: []
claims_all_addressed: true
verdict_discipline_fails: []
findings:
  - {severity: MINOR, item: "B06 Part 4 says 'Unverifiable as whole: 0' but YAML lists Q8 state-utility overruns as unverifiable while Part 1 gives Q8 PARTIALLY VERIFIED on central-PSU retention; labelling inconsistent, not an upgrade from silence"}
  - {severity: MINOR, item: "MTAR 60-70% nuclear share line (MTAR Aug 2026 txt l.679) sits after an inaudible marker and reads as a rhetorical tag; B06 attributes it to Srinivas Reddy and flags the marker, but flag FLAG-INCUMBENT leans on it"}
  - {severity: MINOR, item: "Q6 VERIFIED 'late delivery' rests on peer date slips (benchmark), not WIL evidence; wording could say benchmark verified"}
critical_count: 0
major_count: 0
minor_count: 3
acceptance_rate: 100
```
