# VERIFIER D: Peer coverage audit, SOUTHWEST (2026-11-09)

## Coverage audit (12 transcripts)
All 12 coverage-map rows checked. Spot-read of citations in the transcript files (text search, lines noted):
- DEEPINDS Q1 FY27 "fleet utilization is 100%" (Jul 2026 file line 164), outsourced 120-125 rigs (line 442): found.
- DEEPINDS Q2 FY27 "fleet is fully utilized" (Nov 2026 file lines 355, 396); "300 bps to 400 bps" (lines 736, 771): found. No "monsoon" or "diesel" hit in this file: confirmed.
- DEEPINDS Q4 FY26 "assets are 100% utilized" (May 2026 line 485), rig capex Rs 100-120 Cr (line 588): found.
- JINDRILL Q1 FY27 "$62,000 ... pushed down to $47,800" (Aug 2026 lines 361-367), largest offshore jack-up (line 93): found.
- JINDRILL Q3 FY26 "rates in India were affected due to competition in the last tender" (Feb 2026 line 169): found.
- JINDRILL Q2 FY26 Explorer at $35,606 (Nov 2025 line 162): found.
- ASIANENE Q2 FY26 monsoon "washout ... 20, 25 days" (Nov 2025 lines 350-351), "45 to 75 days" (line 203): found.
- No hit for "South West", "Pinnacle", "Alpha Geo" in any file: confirmed (B06 2D).

| Peer file | B06 usage | Result |
|---|---|---|
| ASIANENE Q4 FY25 | SUBSTANTIVE | confirmed (Rs 120 Cr seismic prior year, line 441) |
| ASIANENE Sep 2025 | CITED-ONLY | handled correctly, used in Q4 |
| ASIANENE Q2 FY26 | SUBSTANTIVE | confirmed |
| ASIANENE Q4 FY26 | SUBSTANTIVE | consistent with B06; not exhaustively re-read |
| DEEPINDS x4 | SUBSTANTIVE | confirmed |
| JINDRILL Q1 FY26 | CITED-ONLY | handled correctly |
| JINDRILL x3 later | SUBSTANTIVE | confirmed |

Unused but relevant material (Rule 3): search of DEEPINDS and JINDRILL files for CBM, seismic, hydraulic, rate-rise language found only the DEEPINDS CBM rounds line (used in Q4). No claim-relevant miss. One counter-quote omitted (MINOR, below).

## Verdict discipline
- Q9 VERIFIED: three peers anchored. Pass.
- Q10 VERIFIED: one peer only. MAJOR under Rule 4 (four calls of one company are not independent peers). The claim is a single-entity fact, so the substance is sound, but the label breaks the rule.
- Q1, Q3, Q6, Q7 PARTIALLY VERIFIED: pass. Q2, Q4, Q5, Q8 UNVERIFIABLE: silence not upgraded to a verdict. No CRITICAL.
- Contradicted items carry quote anchors that exist.

## Rule 5
All ten peer_questions in B05 received a verdict (Q1 to Q10). claims_all_addressed true.

## Findings
- MAJOR: Q10 VERIFIED on one peer.
- MINOR: Q1 omits JINDRILL's stated expectation that day rates will improve (Aug 2026 lines 361-367). It sits beside the same quote B06 used and does not change the verdict.

```yaml
stage: B12d
company: "SOUTHWEST"
run_date: "2026-11-09"
model: claude-sonnet-5-5
status: complete
peers_audited: 12
substantive_confirmed: 10
substantive_unsupported: []
unused_but_relevant: []
claims_all_addressed: true
verdict_discipline_fails:
  - {claim: "Q10 JINDRILL offshore only", issue: "VERIFIED rests on one peer (JINDRILL, four calls of the same company); Rule 4 asks for 2 independent peer anchors", severity: MAJOR}
findings:
  - {severity: MAJOR, item: "Q10 VERIFIED on a single peer", anchor: "B06 Q10; JINDRILL Aug 2026 line 93"}
  - {severity: MINOR, item: "Q1 omits JINDRILL expectation that day rates will improve", anchor: "JINDRILL-Concall_Aug_2026 lines 361-367"}
critical_count: 0
major_count: 1
minor_count: 1
acceptance_rate: 100
```
