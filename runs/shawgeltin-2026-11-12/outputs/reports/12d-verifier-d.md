# Verifier D (B12d): peer coverage audit, SHAWGELTIN, 2026-11-12

## Coverage audit per peer
| Peer | B06 label | Check | Result |
|---|---|---|---|
| NATCAPSUQ Q4 FY25 | SUBSTANTIVE | "softening of gelatin price" (p.4, txt line 145); "consistent rate of 6% to 7%" (line 419, p.11) | Found, confirmed |
| NATCAPSUQ Q2 FY26 | SUBSTANTIVE | HPMC 5% volume / 10% revenue (line 390, p.10); gelatin down ~4% FY25, 4-5% current six months, consolidation, imports Brazil/Argentina/Thailand (lines 397-403, p.11); HPMC 2.8-3x price (line 741) | Found, confirmed. Omitted: "last six quarters" (MINOR) |
| NATCAPSUQ Q4 FY26 | SUBSTANTIVE | 36-day backlog (line 165, p.6); >93% utilisation (line 670, p.18); HPMC <50% (line 658, p.17, errata correct); cold shelf (line 834, p.21) | Found, confirmed. Tariff text is p.20 not p.21 (MINOR) |
| NITTAGELA | UNUSED | No transcript in corpus; screening table only | Correct handling |
| IGCL 531253 | UNUSED | No transcript; B06 errata discloses the file changed after the stage read it | Correct handling |

Spot-read for unused material: grep of all three transcripts for bone, ossein, DCP, gelatin supply/capacity, vegan/plant. No bone, ossein or DCP content exists. No gelatine capacity statement beyond the unnamed consolidation. Only the "six quarters" duration was left out. No MAJOR miss.

## Verdict-discipline audit
| Claim | B06 verdict | Anchors | Result |
|---|---|---|---|
| Q1 pricing | PARTIALLY VERIFIED | One buyer, FY25 to H1 FY26; H2 FY26 and FY27 H1 stated unverified | Pass |
| Q2 demand/imports | PARTIALLY VERIFIED | Growth 6-7%, 4-6%; import 18-20%; no domestic volume data | Pass |
| Q3 bone/raw material | UNVERIFIABLE (clause); PARTIALLY (import clause) | Silence kept as unverifiable, not upgraded | Pass |
| Q4 HPMC substitution | PARTIALLY VERIFIED | Share 5% volume/10% revenue; "primary barrier" not supported, share-of-market NOT FOUND | Pass |
| Q5 capacity | UNVERIFIABLE | No peer data | Pass |

No VERIFIED verdicts, so no single-peer VERIFIED. No upgrade from silence. All 5 peer_questions in B05 received a verdict.

## Findings
0 CRITICAL, 0 MAJOR, 3 MINOR (see block). Acceptance 100% (3 of 3 peers handled correctly).

```yaml
stage: B12d
company: "SHAWGELTIN"
run_date: "2026-11-12"
model: claude-sonnet-5-5
status: complete
peers_audited: 3
substantive_confirmed: 1
substantive_unsupported: []
unused_but_relevant:
  - {peer: NATCAPSUQ, missed_item: "gelatin prices softening 'for the last six quarters'", anchor: "NATCAPSUQ-concall-Q2FY26-2025-11 p.11"}
claims_all_addressed: true
verdict_discipline_fails: []
findings: [3 MINOR, see block file]
critical_count: 0
major_count: 0
minor_count: 3
acceptance_rate: 100
```
