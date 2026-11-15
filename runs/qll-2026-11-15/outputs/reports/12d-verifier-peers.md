# Verifier D: Peer coverage audit, QLL, run 2026-11-15

Scope: B06 (outputs/reports/06-peers.md), 12 transcripts, 6 peer_questions in B05. Method: grep spot-checks of quoted phrases and figures against the .txt files; full re-read not done (stated honestly).

## Coverage audit per peer
| Peer | Calls | B06 label | Citations spot-checked in transcript | Result |
|---|---|---|---|---|
| VIMTALABS | 4 | SUBSTANTIVE x4 | "at least 60%" occupancy (Jul file); "almost double that rate" 8-11% (Jul); "stretch number, but definitely doable" (May); US ~60% of exports (Feb); no receivable/goodwill text (0 hits, confirms "silent") | Confirmed |
| KRSNAA | 4 | SUBSTANTIVE x4 | "timing issue and not [structural]" (Feb); DSO 155 to 139 (May); "virtually 0 bad debt" (May); "temporarily suspend the operations" (Feb) | Confirmed |
| LALPATHLAB | 4 | SUBSTANTIVE x4 | Shahbazkers up to Rs 20 crore (May); DSO 17 days, net cash Rs 1,746 Cr (Nov); S N GeneLab acquisition and 30% remainder (Nov) | Confirmed |

Unused/cited-only peers: none. All 12 calls are marked SUBSTANTIVE. Rule 3 not triggered. Eurofins mention in Vimta Jul call (competitor/acquisition model) is industry context and B06 cites it in 2D; no miss.

## Verdict-discipline audit
| Claim | B06 verdict | Independent peer anchors | Finding |
|---|---|---|---|
| 1 margin | PARTIALLY VERIFIED | 3 peers, level; path 1 peer | Properly capped |
| 2 growth base | PARTIALLY VERIFIED | 3 peers | Properly capped |
| 3 CFO/PBT, DSO | PARTIALLY VERIFIED | Krsnaa only (Lal different payer; Vimta silent) | Properly capped; CFO/PBT NOT FOUND stated |
| 4 ramp/capex | VERIFIED | Vimta, Krsnaa, Lal (3) | Meets the 2-anchor bar. Note: Lal gives no ramp period, so effective anchors are 2 (Vimta, Krsnaa); still compliant |
| 5 bolt-on multiples | PARTIALLY VERIFIED | Lal only | Properly capped |
| 6 overseas | PARTIALLY VERIFIED | Vimta, Lal (opposite) | Properly capped |

No verdict upgraded from silence. Silent peers (Vimta on Claim 3, Krsnaa on Claim 6) were named, not counted.

## peer_questions coverage
6 of 6 questions have a verdict (Claims 1-6 map one-to-one to B05 peer_questions). Claims all addressed: true.

## Findings
- MINOR: Claim 4 header says "two peers" but Part 1 cites three; Lal supplies capex per centre only, no ramp. Wording only; verdict stands.
- MINOR: Caveats note file-name vs call-date mismatches (Lal, Krsnaa, Vimta); Part 3 labels follow cover pages. No effect on anchors, but file-page citations use "Q_ FY__ call" labels, so a reader must map to the file by hand.

Critical 0, major 0, minor 2. Acceptance: 3 of 3 peers correctly handled = 100%.

```yaml
stage: B12d
company: "QLL"
run_date: "2026-11-15"
model: claude-sonnet-5-5
status: complete
peers_audited: 3
substantive_confirmed: 3
substantive_unsupported: []
unused_but_relevant: []
claims_all_addressed: true
verdict_discipline_fails: []
findings:
  - {severity: MINOR, item: "Claim 4 labelled two peers but cites three; Lal gives no ramp period", anchor: "06-peers.md Claim 4"}
  - {severity: MINOR, item: "Call labels differ from file names; mapping needs the Caveats note", anchor: "06-peers.md Caveats"}
critical_count: 0
major_count: 0
minor_count: 2
acceptance_rate: 100
```
