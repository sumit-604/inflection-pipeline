# Verifier D: peer coverage audit. PVRINOX, run date 2026-11-12

Inputs read: B06 report, B05 peer_questions (9), and the page-marked .txt of the peer transcripts. I spot-checked every SUBSTANTIVE call row by locating the cited quote in the transcript.

## Coverage audit per peer

| Peer / call | B06 usage | Citation found in transcript | Result |
|---|---|---|---|
| UFO Q3 FY26 (Feb file) | SUBSTANTIVE | Govt ad vertical 100 crores to 30 crores (lines 264); Mirage 230 screens (554); 63.83% share (579); 70-75% flow-through region (304) | Confirmed |
| UFO Q4 FY26 (May file) | SUBSTANTIVE | 33% to 59.5% ad share (237, 277); 38% footfalls (417); DSO 110-160 days (243); analyst "what PVR runs" (401) | Confirmed |
| UFO Q1 FY27 (Aug file) | SUBSTANTIVE | "33% year-on-year growth in our advertisement revenues" (121, PDF p.3); 399 vs 456 (125-126); Rs 1,118 vs 1,090 Mn (131); Dubai Rs 7 crore (229-234); 30-40% annual (265); "complete outlier" (276) | Confirmed |
| UFO Q2 FY27 (Nov file) | SUBSTANTIVE | 386 vs 462 (131-132); Rs 1,299 vs 1,113 Mn (136); Toxic 6 crores (362-366); product sales 254 to 422 Mn (268); ad share +2%, VPF +16% (259-261); "no uncertainty" (232) | Confirmed |
| WONDERLA Q3 FY26 (Feb file) | CITED-ONLY | Hyderabad ticket price (530-540, PDF p.15); Rs 8 crore labour code (112) | Confirmed. Spot-read found unused material (below) |
| WONDERLA Q4 FY26 (May file) | SUBSTANTIVE | "discretionary spend could be under pressure if the war" (167, p.5); 50 to 60 licences, "structural thing" (462-467, p.12); non-ticket 30% (540, p.14) | Confirmed. One unused item (below) |
| WONDERLA Q1 FY27 (Aug file) | SUBSTANTIVE | ATP Rs 1,310 +2%, non-ticket Rs 591 +20% (125-126); "experiment", "category-creating" (237-238); payback 4 to 5 years (338) | Confirmed |
| WONDERLA Q2 FY27 (Nov file) | SUBSTANTIVE | ATP -3% to Rs 983, non-ticket +11% to Rs 510, ARPU Rs 1,491 (111-114, p.3); "dip in ARPU to drive more volume" (335); Bhubaneswar "completely weather-led" (211); 2 to 3 locations, no final call (469) | Confirmed |
| CINELINE | NOT PROVIDED | No transcripts exist | Correct handling, not an unused file |

Rule 2: 7 of 7 SUBSTANTIVE call rows have real, findable citations. No MAJOR.

## Unused but relevant (rule 3)

1. WONDERLA Q3 FY26 (CITED-ONLY row). Footfall was flat (Q3 9.17 lakh; 9M 23.4 vs 23.7 lakh, lines 108-109). Management states growth comes from "new parks and ARPU" (124) and FY ARPU rose over 8% (67). So Wonderla leaned on price in FY26 before leaning on volume in FY27. This qualifies B06's Q5 line "Wonderla chose volume". It is on the claim but the FY27 quarters still show the opposite of PVR, so it is MINOR.
2. WONDERLA Q4 FY26 (PDF p.11, lines 385-393). "We had a plan of doing smaller parks, but then we recalibrated... we will focus on Tier 1 more than the Tier 2 cities." B06 Part 2C offers Bhubaneswar as the small-format analogue and gives land and licences as the reason for slow expansion. The peer's own move away from small format is unused. MINOR, as B06 already calls the analogue weak.

## Verdict discipline per claim

| Q | B06 verdict | Anchors | Audit |
|---|---|---|---|
| 1 | PARTIALLY VERIFIED | UFO only | Acceptable. Direction quotes are real (Q1 p.3, Q2 p.3). Magnitudes correctly left open |
| 2 | CONTRADICTED | UFO only | MINOR. Label stronger than the evidence. UFO credits the +33% to Dhurandhar spillover "to a significant extent" (Q1 PDF p.5), UFO Q2 ad growth is NOT FOUND, and B06's own net read says "half-supported" |
| 3 | PARTIALLY VERIFIED | UFO only | MINOR. Net read says UFO "neither backs nor refutes"; UNVERIFIABLE fits better. Not an upgrade from silence, since UFO does speak on content selectivity |
| 4 | UNVERIFIABLE | none | Correct |
| 5 | CONTRADICTED | Wonderla only | MINOR. The -3% ATP is consolidated and includes Chennai at Rs 948, which an analyst puts 20% below the 3-quarter average (Q2 PDF p.4). Mix effect not stated. Direction still holds, since Q1 +2% and existing-park ARPU +2% are also weak against +14% |
| 6 | PARTIALLY VERIFIED | Wonderla + UFO | Acceptable, two peers |
| 7 | PARTIALLY VERIFIED | Wonderla only | Acceptable. Not VERIFIED, and attach rate left open |
| 8 | UNVERIFIABLE | none | Correct. No Hollywood share or premium-format data in UFO calls (searched IMAX, 4DX, premium, Hollywood) |
| 9 | UNVERIFIABLE | none | Correct. No Karnataka or CCI mention in UFO or Wonderla |

Rule 4: 0 VERIFIED in B06, so the two-anchor rule is not triggered. No verdict upgraded from silence. No CRITICAL.
Rule 5: all 9 peer_questions have a verdict. claims_all_addressed is true.

## Counts

Peers audited 2 (8 transcripts). CRITICAL 0, MAJOR 0, MINOR 4. Acceptance 100%.

```yaml
stage: B12d
company: "PVRINOX"
run_date: "2026-11-12"
model: claude-sonnet-5-5
status: complete
peers_audited: 2
substantive_confirmed: 7
substantive_unsupported: []
unused_but_relevant:
  - {peer: "WONDERLA", missed_item: "Q3 FY26 call: footfall flat, growth from new parks and ARPU, FY ARPU +8%; qualifies 'Wonderla chose volume' (Q5)", anchor: "WONDERLA-Concall_Feb_2026 .txt lines 65-66, 108-109, 124 (PDF pp.2-3)"}
  - {peer: "WONDERLA", missed_item: "Q4 FY26 call: recalibrated from smaller parks to Tier 1 cities; bears on the small-format analogue (Q4/2C)", anchor: "WONDERLA-Concall_May_2026 .txt lines 385-393 (PDF p.11)"}
claims_all_addressed: true
verdict_discipline_fails:
  - {claim: "Q3 content mix vs share loss", issue: "PARTIALLY VERIFIED but net read says neither backs nor refutes; should be UNVERIFIABLE"}
  - {claim: "Q2 ad weakness", issue: "CONTRADICTED rests on one peer of a different business, UFO credits +33% to Dhurandhar spillover, Q2 ad growth NOT FOUND; label stronger than evidence"}
findings:
  - {severity: MINOR, claim: "Q2", detail: "CONTRADICTED label overstated; citations real"}
  - {severity: MINOR, claim: "Q3", detail: "PARTIALLY VERIFIED vs net read 'neither backs nor refutes'"}
  - {severity: MINOR, claim: "Q5", detail: "Wonderla ATP -3% is consolidated incl. Chennai Rs 948 deliberate low price (Q2 PDF p.4); Q3 FY26 ARPU-led quarter unused"}
  - {severity: MINOR, claim: "Q4 / 2C", detail: "Wonderla Q4 PDF p.11 shift from small parks to Tier 1 unused"}
critical_count: 0
major_count: 0
minor_count: 4
acceptance_rate: 100
```
