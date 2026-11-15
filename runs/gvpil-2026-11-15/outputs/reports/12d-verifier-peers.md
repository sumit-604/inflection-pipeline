# B12d Verifier D: Peer coverage audit, GVPIL, run 2026-11-15

Method: opened B06 report, B05 peer_questions, and the 12 peer .txt files. Spot-checked quotes by keyword search with line numbers, and matched line numbers to "[page N]" markers. Not every cited sentence was re-read; the sample is stated per row.

## Coverage audit table per peer

| Peer / call | B06 usage | Citation located in transcript? | Result |
|---|---|---|---|
| BHEL Jul 2021 | CITED-ONLY | "revamp of business model for spares & services business" at line 93 (p.3 region) | Confirmed. Nothing larger left unused in keyword search |
| BHEL May 2022 | CITED-ONLY | 1,67,000 MW identified, ~1,10,000 MW finalised (lines 162-164); PVC "index based" with cap (line 320). Material-cost passage lines 302-313 exists, not cited | Confirmed. Material-cost passage is dated and of the same kind as the BHEL 2023 cite: MINOR at most |
| BHEL May 2023 | SUBSTANTIVE | "high margin spares and services business... over INR 3, 800 crores" (line 100-101); spares +25% (line 142-143); R&M of GSECL Ukai (line 137) | Confirmed (page given as "p.4, p.7 region" for Ukai is loose: MINOR) |
| BHEL May 2024 | SUBSTANTIVE | "Spares and services business of around" (line 71); Ukai also at line 121 | Confirmed |
| ISGEC Feb 2026 | SUBSTANTIVE | FGD "almost completed... 99%" line 445 (p.11); commodity/lock-in lines 585-595, 663-678 | Confirmed |
| ISGEC Jun 2026 | SUBSTANTIVE | Input costs "steel forgings, castings, chemicals" line 168, 201 | Confirmed. Retention Rs 165 Cr not re-read (FGD key not in sampled pattern) |
| ISGEC Aug 2026 | SUBSTANTIVE | "retrofit and modernization, services, spares" line 200-201; "slightly higher margin" line 673; "double the existing O&M base" line 674 | Confirmed |
| ISGEC Nov 2026 | SUBSTANTIVE | "steel, copper, aluminium, and nickel, skewed up to 10% fluctuation" line 169 | Confirmed |
| POWERMECH Nov 2025 | SUBSTANTIVE | CEA "another 45000mw" line 700 (p.12); Udupi line 1001 (p.16); escalation "pass through" line 911 (p.15) | Confirmed, pages match markers |
| POWERMECH Feb 2026 | SUBSTANTIVE | "nonmoving FGD... 4,260" line 424 | Confirmed |
| POWERMECH May 2026 | SUBSTANTIVE | "15% to 16%" lines 600-612, 1034-1037; "12.3%" lines 146, 1039 | Confirmed |
| POWERMECH Aug 2026 | SUBSTANTIVE | "10% to 11%" line 655; "around what we are having 18" line 691; Udupi "almost completed" line 748 | Confirmed |

12 of 12 handled correctly. 9 SUBSTANTIVE... correction: 10 SUBSTANTIVE, 2 CITED-ONLY (BHEL 2021, 2022). All 10 SUBSTANTIVE peers have at least one real, findable citation.

## Unused or CITED-ONLY spot-read (rule 3)

- BHEL Jul 2021 and May 2022: keyword search for spares, services, R&M, retrofit, FGD, index, material cost. Only items already cited or dated industry context found. No directly claim-relevant statement left unused.
- Unused extra anchor (MINOR): POWERMECH Nov 2025 also states O&M margin "15% to 16%" (lines 747, 819, p.13-14). B06 Q1 cites May 2026 and Aug 2026 only. It adds a third dated reading to the same peer, not a second peer, so the verdict does not change.

## Verdict discipline per claim (rules 4, 5)

| Q | B06 verdict | Independent anchors | Discipline |
|---|---|---|---|
| 1 margin | PARTIALLY VERIFIED | Power Mech only (1 peer) | Correct. Not upgraded |
| 2 third-party share | UNVERIFIABLE | none | Correct. Adjacent evidence labelled adjacent |
| 3 R&M ordering | UNVERIFIABLE | none | Correct. Silence read as informative, not as a verdict upgrade |
| 4 FGD restart | PARTIALLY VERIFIED | Power Mech, ISGEC (2 current) corroborate run-off, not the policy claim | Correct, and explicitly limited |
| 5 market size | UNVERIFIABLE | none | Correct |
| 6 demand | PARTIALLY VERIFIED | direction only; numeric claims uncorroborated | Correct |
| 7 input cost | PARTIALLY VERIFIED | Power Mech, ISGEC; magnitude not matched | Correct |
| 8 Gulf/Saudi | UNVERIFIABLE | none | Correct |

No VERIFIED verdict exists (0 of 8), so no one-peer VERIFIED (MAJOR) and no upgrade from silence (CRITICAL). All 8 peer_questions in B05 received a verdict. B06 flags the keyword-only reading of eight files, stated honestly; a miss outside the search terms remains possible and is not a finding.

## Findings
1. MINOR: Power Mech Nov 2025 O&M margin 15-16% not used as a further anchor for Q1.
2. MINOR: BHEL May 2023 R&M Ukai page cited loosely ("p.4, p.7 region").

```yaml
stage: B12d
company: "GVPIL"
run_date: "2026-11-15"
model: claude-sonnet-5-5
status: complete
peers_audited: 12
substantive_confirmed: 10
substantive_unsupported: []
unused_but_relevant: []
claims_all_addressed: true
verdict_discipline_fails: []
findings:
  - {severity: MINOR, item: "POWERMECH Nov 2025 O&M margin 15-16% (lines 747, 819) not used as extra Q1 anchor; same peer, verdict unchanged"}
  - {severity: MINOR, item: "BHEL May 2023 Ukai R&M cited as 'p.4, p.7 region'; page imprecise"}
critical_count: 0
major_count: 0
minor_count: 2
acceptance_rate: 100
```
