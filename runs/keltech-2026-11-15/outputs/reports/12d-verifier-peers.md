# VERIFIER D: PEER COVERAGE, KELTECH, 2026-11-15

Model claude-sonnet-5-5. Inputs: 12 peer transcript .txt twins, 06-peers.md (B06 report), peer_questions[] of B05. Page numbers are the [page N] markers. Method: all 12 coverage-map rows traced to at least one findable citation; about 25 quotes and figures grep-checked against the .txt twins; one claim-relevant unused passage hunt on APOLLO Q4FY26.

## Coverage audit per peer

| Peer / call | B06 usage | Citation check | Result |
|---|---|---|---|
| APOLLO Q3FY26 | SUBSTANTIVE | "six months' time we definitely going to start producing" found p.6 (line 219). IDL order book "INR500-odd crores" found p.12 (line 497); B06 text said p.13, orchestrator errata already corrects to 12. | Confirmed |
| APOLLO Q4FY26 | SUBSTANTIVE | "little less than INR380 crores" p.10; TNT 500 tons / HMX 50 tons, licences = industrial requirement, DPRs "getting ready" p.11; "huge depletion of stocks" p.12; TNT/RDX licence p.5 (line 185). | Confirmed |
| APOLLO Q1FY27 | SUBSTANTIVE | "shrinking margin business ... bulk explosives" line 264; Q4 EBITDA positive, Q1 PAT positive; Premier 41.33% for about Rs 1,550 Cr; order book Rs 480 Cr (line 175). | Confirmed |
| APOLLO Q2FY27 | SUBSTANTIVE | 9,000 metric ton storage (line 89, p.3); working capital 353 vs 359 days (line 103); "off-season lean quarter" (line 161); "couple of quarters more" (line 155). | Confirmed |
| PREMEXPLN Q2FY26 | SUBSTANTIVE | "By the end of financial year, we will be starting production" (lines 310, 319). | Confirmed |
| PREMEXPLN Q3FY26 | SUBSTANTIVE | "first quarter of next financial year" (line 194); Coal India "at least breaks even ... not supplying any bulk" (line 515). | Confirmed |
| PREMEXPLN Q4FY26 | SUBSTANTIVE | "It may go up to Q3 ... qualification" p.7 (line 245); "at least ... 5 years minimum" new entrants (line 522). | Confirmed |
| PREMEXPLN Q1FY27 | SUBSTANTIVE | Water trials September (line 287); "more than 40" players (line 388, p.10); Coal India withdrawn, margins "very, very thin. Many places, it is negative" (lines 408-411, p.11); Rs 80 Cr (line 404, p.11). The 94%/6% defence/industrial order split is at line 325, before p.10; B06 cites pp.4, 10-11 for it. | Confirmed, one page drift |
| SOLARINDS Q2FY26 | SUBSTANTIVE | "L1 basis rather than on overall value proposition" (line 573). | Confirmed |
| SOLARINDS Q3FY26 | SUBSTANTIVE | "practically no growth in this financial year" (line 361). | Confirmed |
| SOLARINDS Q4FY26 | SUBSTANTIVE | "totally flat growth market" (line 283); "only, say, 60% of the total increase" (line 353); Kalyani Group entry question (line 291). | Confirmed |
| SOLARINDS Q2FY27 | SUBSTANTIVE | EBITDA 29.02% p.3; domestic 27% from 29%, international 43% from 46% p.4 (lines 162-169); industry growth 6% to 7% (line 457). Defence order book Rs 17,568 Cr is at line 393, p.10; B06 cites p.9. | Confirmed, one page drift |

Peers audited: 12 call rows (3 peers). Substantive confirmed: 12. No SUBSTANTIVE row lacks a real citation. No UNUSED or CITED-ONLY row exists.

Spot-read for unused material (rule 3), APOLLO Q4FY26 pp.11-12 and 18. Apollo's TNT answer at p.18 (lines 724-740) says IDL has "presently negative EBITDA" in May 2026, margin guidance from Q3 FY27, Apollo already buys defence explosive fill from outsourcers and "would continue to do with our captive systems", and "the size of the industry players ... supplying for it is pretty small". B06 uses the "no margin guidance" point (Q9) but not the captive-buyer and small-supplier-base statements. Impact is small because the remarks are about defence explosives broadly, not TNT price or offtake, so the "no peer states a TNT price" finding stands. MINOR.

## Verdict-discipline audit per claim

| Claim | B06 verdict | Independent peers | Result |
|---|---|---|---|
| Q1 | PARTIALLY VERIFIED | Solar only on volume | Correct |
| Q2 | PARTIALLY VERIFIED | Solar only | Correct |
| Q3 | VERIFIED | Premier, Solar, Apollo, all quoted | Passes. Per-unit price NOT FOUND is stated in the cell. |
| Q4 | PARTIALLY VERIFIED | Direction from three, TNT specifics from none | Correct |
| Q5 | VERIFIED | Solar, Apollo, Premier | Passes |
| Q6 | PARTIALLY VERIFIED | Solar mainly | Correct |
| Q7 | CONTRADICTED (base rate) | Premier four calls, Solar, Apollo | Passes. B06 limits it to a base-rate reading; no upgrade from silence. |
| Q8 | PARTIALLY VERIFIED | Solar | Correct |
| Q9 | VERIFIED | Apollo for all IDL specifics (loss, seasonality, licences). Premier supports only the Coal India margin sub-point and says nothing on IDL. | MAJOR. Four Apollo calls are one source. The question names APOLLO alone in check_peers, so two independent anchors cannot exist. Should read PARTIALLY VERIFIED, or VERIFIED (single-source, Apollo, with Premier on the Coal India sub-point). |

No verdict upgraded from silence: CRITICAL count 0. Q4 "tightness" correctly stays PARTIAL and the NOT FOUND items stay NOT FOUND.

## Rule 5: peer_questions coverage

B05 lists nine questions. B06 answers Q1 to Q9 in order, each with a verdict. All addressed: true.

## Findings

1. MAJOR. Q9 VERIFIED rests on one peer (Apollo) for the IDL-specific claim. Anchor: 06-peers.md Q9 verdict and `verified` block, anchor_count 8. Fix: relabel PARTIALLY VERIFIED (single peer) or note single-source in the verified entry.
2. MINOR. Page drift: SOLARINDS Q2FY27 defence order book Rs 17,568 Cr is p.10 not p.9 (line 393); PREMEXPLN Q1FY27 94%/6% order split precedes p.10 (line 325). The orchestrator errata does not cover these two.
3. MINOR. Unused: APOLLO Q4FY26 p.18, IDL "presently negative EBITDA" at May 2026, captive defence-explosive buying and small supplier base (lines 724-740). Relevant to Q4 "who buys" and the Q9 profit path.

Counts: critical 0, major 1, minor 2. Acceptance rate: 11 of 12 peer rows handled without a MAJOR (APOLLO rows carry the Q9 verdict issue), 92%.

```yaml
stage: B12d
company: "KELTECH"
run_date: "2026-11-15"
model: claude-sonnet-5-5
status: complete
peers_audited: 12
substantive_confirmed: 12
substantive_unsupported: []
unused_but_relevant:
  - {peer: "APOLLO Q4FY26", missed_item: "IDL presently negative EBITDA (May 2026); Apollo buys defence explosive fill from outsourcers and will keep captive demand; defence explosive supplier base 'pretty small'", anchor: "APOLLO-Q4FY26 transcript p.18, lines 724-740"}
claims_all_addressed: true
verdict_discipline_fails:
  - {claim: "Q9 IDL demand and margins", issue: "VERIFIED rests on APOLLO alone for IDL specifics; PREMEXPLN corroborates only the Coal India margin sub-point; should be PARTIALLY VERIFIED (single peer)", severity: MAJOR}
findings:
  - {id: 1, severity: MAJOR, item: "Q9 VERIFIED on one peer", anchor: "06-peers.md Q9; B06 verified[] entry Q9"}
  - {id: 2, severity: MINOR, item: "Page drift: SOLARINDS Q2FY27 Rs 17,568 Cr defence order book is p.10 not p.9; PREMEXPLN Q1FY27 94/6 order split precedes p.10", anchor: "SOLARINDS-Q2FY27 line 393; PREMEXPLN-Q1FY27 line 325"}
  - {id: 3, severity: MINOR, item: "Unused APOLLO Q4FY26 p.18 statements (negative EBITDA, captive buying, small supplier base)", anchor: "APOLLO-Q4FY26 lines 724-740"}
critical_count: 0
major_count: 1
minor_count: 2
acceptance_rate: 92
```
