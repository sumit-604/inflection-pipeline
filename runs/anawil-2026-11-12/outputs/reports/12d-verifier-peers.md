# Verifier D: Peer Coverage Audit, ANAWIL (run 2026-11-12)

Method: located each B06 citation in the page-marked .txt by phrase search, then mapped file line to the nearest [page N] marker above it. Sampling: every SUBSTANTIVE peer got at least one quote and page check (all 12 peers, 25+ anchors). Unused-material scan: searched all 12 transcripts for tower, tubular, Envision, Sany, steel, retention.

## Coverage audit per peer

| Peer / call | B06 status | Citation found | Page check | Result |
|---|---|---|---|---|
| KP Green H1 FY25 | SUBSTANTIVE | steel "passed on" (file l.344, page 9); H2 skew; EBITDA 15-16% | p9 ok | Confirmed |
| KP Green H2 FY25 | SUBSTANTIVE | receivable days 142 (l.247, l.424); wind tubular tower "planned" (l.302); Sanvion (l.133) | present | Confirmed |
| KP Green H1 FY26 | SUBSTANTIVE | EBITDA "15% to 18%" (l.862); royalty 2%; ramp lag | present | Confirmed |
| KP Green H2 FY26 | SUBSTANTIVE | onshore tubular tower (l.150 p4; l.397 p10); 30% to 34% (l.815 p21); piled up (l.896 p23); TReDS (l.674) | all ok | Confirmed |
| Inox Q2 FY26 | SUBSTANTIVE | "70% of the annual" (l.86 p3); tower facility (l.110) | tower plant is page 4, not 3 | Confirmed, minor page error |
| Inox Q3 FY26 | SUBSTANTIVE | "always H2 heavy" (l.659 p17); "setting up towers" (l.391 p10); WC 200-210 (l.268) | ok | Confirmed |
| Inox Q4 FY26 | SUBSTANTIVE | "8 to 10 GW" (l.117 p3); steel "passed on", LC (l.573-574 p14); Rs 400 Cr (l.451) | ok | Confirmed |
| Inox Q1 FY27 | SUBSTANTIVE | "70% to 75%" (l.334 p8); "almost 25%" (l.659 p15); "24 to 36" (l.146 p4); tower ready (l.152 p4) | ok | Confirmed |
| Suzlon Q3 FY26 | SUBSTANTIVE | "record 6.34" (l.102 p3); receivables 5,700 (l.206) | ok | Confirmed |
| Suzlon Q4 FY26 | SUBSTANTIVE | "8 gigawatt in" (l.297 p8); pass-through (l.478-481 p12); ASP 5.9 | ok | Confirmed |
| Suzlon Q1 FY27 | SUBSTANTIVE | "about 35, 40" (l.188 p5); 10% to 20% deferred (l.104 p3); ASP Rs 6.3 Cr | ASP is page 4, not 3 | Confirmed, minor page error |
| Suzlon Q2 FY27 | SUBSTANTIVE | "crossed 59", "over 40 gigawatts" (p3); 1.5x (p7); tower in ALMM list (l.441 p12); 5% to 10% (l.618 p16); 3,900/1,300 MW (l.608 p16); 18 months (p4) | ok | Confirmed |

Rule 2 result: 12 of 12 SUBSTANTIVE confirmed. No unsupported peer.

## Rule 3: UNUSED / CITED-ONLY peers
B06 marks none UNUSED or CITED-ONLY. Spot-read for missed claim-relevant material anyway. Searched tower, tubular, Envision, Sany across all 12 files. Envision and Sany appear nowhere (B06 Q12 correct). Suzlon tower mentions: only the ALMM component list (used). KP tower mentions: wind lattice towers, Sanvion, tubular entry (all used). KP H1 FY26 l.359 "windmill towers... approved by a lot of DISCOMs" and H2 FY25 l.186 "wind tower" outlook are lattice-product statements, not relevant to tubular claims. No directly claim-relevant statement left unused. unused_but_relevant: none.

## Rule 4: Verdict discipline per claim

| Q | B06 verdict | Independent peer anchors | Discipline |
|---|---|---|---|
| Q1 | VERIFIED | Inox, Suzlon, KP (7 anchors) | Pass. Note: Anawil 80% top exceeds peer max 75%; disclosed in B06 net read. |
| Q2 | VERIFIED | Inox, Suzlon (8 anchors); "28 GW" flagged as understated vs Suzlon 40+ GW | Pass (2 independent). Magnitude caveat disclosed. |
| Q3 | UNVERIFIABLE | none | Pass, no upgrade from silence. |
| Q4 | UNVERIFIABLE | none | Pass. |
| Q5 | UNVERIFIABLE | none | Pass. |
| Q6 | PARTIALLY VERIFIED | Suzlon, Inox on platform size only | Pass. |
| Q7 | VERIFIED | KP, Suzlon, Inox on pass-through | Pass on count. Minor: plate-buyer half is unverifiable, so PARTIALLY would fit better. |
| Q8 | VERIFIED | Suzlon, Inox, KP | Pass. |
| Q9 | PARTIALLY VERIFIED | Inox, one peer | Pass; correctly not upgraded. |
| Q10 | PARTIALLY VERIFIED | KP margin; others non-comparable | Pass. |
| Q11 | VERIFIED | Inox, Suzlon, KP | Pass. Tower lag is labelled [INFERENCE]. |
| Q12 | UNVERIFIABLE | none; text search confirms no Envision/Sany | Pass. |

No VERIFIED rests on a single peer. No verdict is upgraded from silence. critical 0, major 0.

## Rule 5: B05 peer_questions
B05 lists 12 questions. B06 Part 1 answers Q1 to Q12 in order, each with a verdict. All addressed.

## Findings (all MINOR)
1. Inox Q2 FY26 tower plant cited [page 3]; actual [page 4] (used in Q3, 2D, flags, risks).
2. Suzlon Q1 FY27 ASP Rs 6.3 Cr cited [page 3]; actual [page 4].
3. Q7 headline VERIFIED covers only the pass-through half.
4. Q1 headline VERIFIED sits beside an 80% top that no peer reaches (disclosed).

```yaml
stage: B12d
company: "ANAWIL"
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
  - {severity: MINOR, item: "Page anchor error: Inox Q2 FY26 South India blade and tower plant is on [page 4] (file line 110, page 4 starts line 97), cited as [page 3] in Q3, 2D, flags and risks. Quote and fact confirmed."}
  - {severity: MINOR, item: "Page anchor error: Suzlon Q1 FY27 ASP Rs 6.3 Cr is on [page 4] (file lines 118-119), cited as [page 3] in Q4 and 2B/coverage map. Fact confirmed."}
  - {severity: MINOR, item: "Q7 headlined VERIFIED although the claim's first half (who buys the plate) is UNVERIFIABLE; PARTIALLY VERIFIED would match the evidence. Pass-through itself has 3 independent peers, so no downgrade to the discipline rule."}
  - {severity: MINOR, item: "Q1 VERIFIED while the 80% top of Anawil's 70-80% sits above every peer figure (peer max 75%). B06 states this in the net read and FLAG-H2-RANGE-TOP, so disclosed; the headline verdict does not carry it."}
critical_count: 0
major_count: 0
minor_count: 4
acceptance_rate: 100
```
