# Verifier D: Peer Coverage Audit, DEEDEV, run 2026-11-15

Scope: B06 (06-peers.md) against 12 peer transcripts (.txt twins) and the 7 B05 peer_questions. Spot-read by text search with line context.

## Coverage audit per peer
| Peer / quarter | B06 usage | Citation found in transcript | Result |
|---|---|---|---|
| ANUP Q2 FY26 | CITED-ONLY | "average 3x, that's 120 days" (Nov 2025 .txt l.89) | OK |
| ANUP Q3 FY26 | SUBSTANTIVE | Adani/L&T/Torrent (l.350), 120 days (l.523), 40% vs 25% advances (p.14) | Confirmed. But missed the 190-200 day analyst figure at p.14 (see finding 1) |
| ANUP Q4 FY26 | SUBSTANTIVE | "over 14 gigawatts" (May 2026 l.150) | Confirmed |
| ANUP Q1 FY27 | SUBSTANTIVE | "only two mills... AM/NS and Jindal" (Aug 2026 l.340) | Confirmed |
| ISGEC Q3 FY26 | SUBSTANTIVE | BHEL exchange, MD declines to speak on BHEL (l.392-397); FGD "not really BHEL" (l.443) | Confirmed; BHEL link on FGD overreach (finding 2) |
| ISGEC Q4 FY26 | SUBSTANTIVE | Two orders about Rs 550 cr cancelled (Jun 2026 l.162) | Confirmed |
| ISGEC Q1 FY27 | SUBSTANTIVE | Rs 502 cr board-approved, piping shops at Rattangarh (Aug 2026 l.190, l.312) | Confirmed |
| ISGEC Q2 FY27 | SUBSTANTIVE | Rs 502 cr, back-to-back offers (Nov 2026 l.161, l.219, l.534) | Confirmed |
| RATNAMANI Q4 FY25 | SUBSTANTIVE | Pierced boiler tubes allowed, 80,000 MW (May 2025 l.249-254); analyst 163 days (l.483) | Confirmed |
| RATNAMANI Q2 FY26 | CITED-ONLY | Not spot-read in full; nothing found contrary in B06 pairing | No finding |
| RATNAMANI Q4 FY26 | SUBSTANTIVE | "substantial capacities have been added" (May 2026 l.458), back-to-back (l.693) | Confirmed |
| RATNAMANI Q2 FY27 | SUBSTANTIVE | "five to six months" (Nov 2026 l.457) | Confirmed |

Substantive confirmed: 10 of 10. Page numbers inside B06 were not each re-checked; line-level text existence was. Both CITED-ONLY peers: only ANUP Q2 FY26 searched for unused material; none found beyond what B06 holds. Ratnamani Q2 FY26 not exhaustively read.

## Verdict-discipline audit
| Q | B06 verdict | Check |
|---|---|---|
| 1 Thermal pace | PARTIALLY VERIFIED | Two independent peers (Ratnamani, ANUP). No upgrade from silence. OK |
| 2 Mill credit | UNVERIFIABLE | No peer states terms. OK |
| 3 WC cycle | PARTIALLY VERIFIED | Level claim weakened by finding 1. Verdict itself holds |
| 4 Material-supplied | UNVERIFIABLE | OK |
| 5 P91/P92 | UNVERIFIABLE | OK |
| 6 HRSG | UNVERIFIABLE | OK |
| 7 Nuclear | PARTIALLY VERIFIED | Three peers on opportunity; partner point stated as uncorroborated. OK |

No VERIFIED verdicts, so rule 4 has nothing to fail. No upgrade from silence. All 7 of 7 peer_questions received a verdict.

## Findings
1. MAJOR (rule 3). ANUP Q3 FY26 p.14: an analyst asks when ANUP's cash conversion cycle falls to 120 days "from where it is right now around 190 to 200-odd days"; management answers on the timeline and does not dispute. B06 Q3 and Part 4 say 190-200 days is above every peer figure and use only 2.2 turns (about 166 days). The question text itself used the 190-200 figure. Fix: state one peer shows 190-200 days in a stressed FY26 with a 120-day target, an analyst figure. B06 treated an analyst-quoted 163 days at Ratnamani as usable, so the standard was uneven. Verdict PARTIALLY VERIFIED stands.
2. MINOR (rule 3). ISGEC Q3 FY26: the stuck FGD retention is "not really BHEL" (NTPC). B06 flag 3 ties it to a BHEL-weighted book. The PSU milestone and retention point holds; the BHEL tie does not.

Acceptance rate: 11 of 12 peers correctly handled = 92%.

```yaml
stage: B12d
company: "DEEDEV"
run_date: "2026-11-15"
model: claude-sonnet-5-5
status: complete
peers_audited: 12
substantive_confirmed: 10
substantive_unsupported: []
unused_but_relevant:
  - {peer: "ANUP", missed_item: "Analyst on ANUP Q3 FY26 call puts ANUP's own cash conversion cycle at 'around 190 to 200-odd days' (target 120); management answers on the path to 3 turns and does not dispute. B06 Q3 says 190-200 is above every peer figure and uses only 2.2 turns (~166 days)", anchor: "ANUP-Concall_Feb_2026_Transcript, page 14 (lines 545-550 of .txt)"}
claims_all_addressed: true
verdict_discipline_fails: []
findings:
  - {severity: MAJOR, rule: 3, item: "B06 Q3 net read and Part 4 'most consequential gap' state no peer supports 190-200 days. ANUP Q3 FY26 p.14 carries an analyst figure of 190-200 days for ANUP itself, undisputed. B06 accepted an analyst-quoted 163 days for Ratnamani (Q4 FY25) but skipped this one, so the standard is uneven. Verdict PARTIALLY VERIFIED stands; the 'above every peer figure' sentence and the flag in B06 need softening to: one peer shows 190-200 days in the stressed FY26 period, with management targeting 120", anchor: "ANUP Q3 FY26 p.14"}
  - {severity: MINOR, rule: 3, item: "B06 flag 3 and Part 2E tie FGD retention to a BHEL-weighted book. ISGEC CFO says the stuck FGD retention is 'not really BHEL' (NTPC). The PSU-terms point holds; the BHEL link does not", anchor: "ISGEC Q3 FY26 (Feb 2026 transcript, .txt line 443)"}
critical_count: 0
major_count: 1
minor_count: 1
acceptance_rate: 92
```
