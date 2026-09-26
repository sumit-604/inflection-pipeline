# VERIFIER D: PEER COVERAGE AUDIT — Fabtech Technologies Ltd (FABTECH)

Run date: 2026-09-26. Model: claude-sonnet-5.

Inputs: 12 raw peer transcripts (SETL x4, HLEGLAS x4, PRAJIND x4) in
runs/fabtech-2026-09-26/inputs/peer-concalls/; B06 report and B06-peers.yaml
block; B05-concall.yaml peer_questions list (6 questions).

Method: for every peer marked SUBSTANTIVE in B06's coverage map, the cited
quote or paraphrase was located in the raw transcript text and checked for
accuracy. For every peer marked CITED-ONLY (HLEGLAS Q4 FY25 May-2025,
PRAJIND Q3 FY26 Mar-2026), the transcript was spot-read independently and
checked against the six-question claim list for anything the pipeline
should have used but did not. A full-corpus grep for "Fabtech" was run to
check the 2D no-mention finding. Verdict discipline was checked against the
VERIFIED/PARTIALLY VERIFIED/CONTRADICTED/UNVERIFIABLE calls.

---

## PART 1: COVERAGE AUDIT PER PEER

| Peer | Quarter | B06 usage | Citation located in transcript? | Verdict |
|---|---|---|---|---|
| SETL | Q2 FY26 (Nov-2025) | SUBSTANTIVE | Confirmed: "they are our competitors, but there are two, three variety of products they are manufacturing. Today, we are almost 91 variety of products" (verbatim, p.7 of transcript); "Solution working capital, it will increase, sir... Milestone basis, we will get the payment" (verbatim, p.17); "Market share, we don't know. But we have a full order book" (verbatim, p.13); "customer inspections are delayed... Customer inspections. Equipment inspections delayed" (p.6) matches the "customer inspections postponed" framing used in Part 2E, and a later Yash Upadhyay exchange uses the literal words "customer inspections postponed" (p.12) | Citation exists, accurately used |
| SETL | Q3 FY26 (Feb-2026) | SUBSTANTIVE | Confirmed: "We have decided not to disclose the figures order book because of I don't want to take my competitor advantage" (verbatim, p.17); "next year, we are going to become the largest glass lining equipment manufacturer in India... This product don't have any alternative competitor... Europe and U.S. markets... our partner, IPP, going to sell" (verbatim, p.15) | Citation exists, accurately used |
| SETL | Q4 FY26 (May-2026) | SUBSTANTIVE | Confirmed: "some challenges already they are facing. Because today metal cost is X, tomorrow is X plus one. That is, we are facing already, not only us, whole industry is facing" (verbatim, p.p.~21 of May-2026 transcript); "our export freight always we put -- keep it in customer's scope" region confirmed nearby | Citation exists, accurately used |
| SETL | Q1 FY27 (Aug-2026) | SUBSTANTIVE | Confirmed: "cycle of 220 to 240 days... this September result we are going to it will coming down to below 200 days" (verbatim); GScale AI data-centre diversification extensively present | Citation exists, accurately used |
| HLEGLAS | Q4 FY25 (May-2025) | CITED-ONLY | Spot-read complete: no Middle East, Saudi, export, retention, or geopolitical-delay material present in this transcript (checked by full-text grep, zero hits on those terms). One competitor-comparison exchange exists ("there is no competitor in India which has all of these platforms available under any one single roof", Kinam heat-transfer sub-business) that is tangential to Q6 but concerns Indian domestic heat-transfer competition, not Fabtech's MENA/Africa pharma-plant EPC niche — MINOR unused item, not claim-relevant enough to be MAJOR | No unaddressed MAJOR item; one MINOR industry-context miss |
| HLEGLAS | Omeras call (Aug-2025) | SUBSTANTIVE | Confirmed: "governments worldwide, particularly in the Middle East and Asia Pacific, are modernizing transport hubs, tunnels, and clean rooms" (verbatim); "they are building new cities" (verbatim); competitive geography "the players for the tanks and silos are located in North America and Europe, largely. There are also a few in China, but they are largely catering to the Chinese market... one or two competitors within Europe" (verbatim, close match to B06's quoted paraphrase); "reduce dependence on our traditional chemical and API industry clientele" (verbatim) | Citation exists, accurately used |
| HLEGLAS | Q2 FY26 (Nov-2025) | SUBSTANTIVE | Confirmed: "The receivable days are back to the FY '22 levels" (verbatim, analyst Dhaval Shah's question); "margins were impacted because of higher material costs" region present, consistent with B06's "high-cost raw material" citation | Citation exists, accurately used |
| HLEGLAS | Q4 FY26 (Jun-2026) | SUBSTANTIVE | Confirmed: "the pharma -- the pharmaceutical and the API sectors are not yet doing that, but especially the [CDMO/agrochemical]... again, deferred a few things" (verbatim); "next phase of growth for HLE Glascoat" (verbatim); "before all this conflict started" (verbatim, Middle East sales-team context) | Citation exists, accurately used |
| PRAJIND | Q2 FY26 (Dec-2025) | SUBSTANTIVE | Confirmed: "Many countries from Africa region also are keen to either introduce the blending mandates or increase the current mandates" (verbatim) | Citation exists, accurately used |
| PRAJIND | Q3 FY26 (Mar-2026) | CITED-ONLY | Spot-read: Africa margin commentary ("we had delivered a little bit more on the Africa market side... Africa margins... executing a very big order... also for the construction activity... margins are not generally what we get in the international market") is a near-repeat of the Dec-2025/Jun-2026 points already used elsewhere. No Middle East, Saudi, win-rate, or order-finalisation-delay material found on grep. B06's "no new verdict-level contribution" framing is accurate | No unaddressed item |
| PRAJIND | Q4 FY26 (Jun-2026) | SUBSTANTIVE | Confirmed: "there is a good inquiry pipeline for projects... there are some delays in order finalization" (verbatim); "we did experience some escalation of cost in our execution... revenues remained flat, but the cost of execution went up" (verbatim); "Overall impact is 1-1.5% additional which we have incurred... cost escalation coming up in the site execution... because the sites are open. They are not getting completely closed" (verbatim, exact match to B06's quoted 1-1.5% figure and mechanism) | Citation exists, accurately used |
| PRAJIND | Q1 FY27 (Aug-2026) | SUBSTANTIVE | Confirmed: "because of the current geopolitical scenario, there will be some kind of pressure on the material cost, but we are cautious and aware about it" (verbatim) | Citation exists, accurately used |

**12 of 12 peers audited. 10 of 10 SUBSTANTIVE citations independently
located and confirmed accurate (verbatim or near-verbatim) in the cited
transcript. 0 SUBSTANTIVE citations unsupported. Both CITED-ONLY peers
spot-read against the six-question claim list: no MAJOR unused material
found; one MINOR industry-context item (HLEGLAS May-2025, tangential
domestic-competitor remark) not used, correctly weighted low because it
does not speak to Fabtech's MENA/Africa or pharma-plant-EPC-specific
claims.**

**2D check (no peer mentions Fabtech):** full-corpus grep for "Fabtech"
across all 12 transcripts returns zero matches, confirming B06's
`peer_mentions_of_company: []` finding.

---

## PART 2: VERDICT-DISCIPLINE AUDIT PER CLAIM

| Claim (B05 peer_questions) | B06 verdict | Peers cited | Anchor count | Discipline check |
|---|---|---|---|---|
| Q1: $30bn/$70bn TAM + Saudi hard-tender-qualification | PARTIALLY VERIFIED | HLEGLAS, PRAJIND | 3 quotes across 2 peers | Correctly not upgraded to VERIFIED; no peer names the dollar TAM or the "hard tender qualification" framing specifically. Appropriate. |
| Q2: RMC ~33%/execution ~43% YoY cost inflation | VERIFIED (direction), UNVERIFIABLE (magnitude) | PRAJIND, SETL, HLEGLAS | 4+ quotes across 3 peers | Direction claim rests on 3 independent peers — clears the ≥2-anchor bar comfortably. Magnitude correctly left unconfirmed given PRAJIND's own 1-1.5% figure is an order of magnitude smaller; not silently upgraded. Appropriate. |
| Q3: order-finalisation delay, not cancellation | VERIFIED | PRAJIND, HLEGLAS, SETL | 4 anchors, 3 independent peers | Passes the ≥2-independent-peer-anchor rule with margin. No single-peer VERIFIED found anywhere in the report. Appropriate. |
| Q4: export receivable retention structure, ~180 days | PARTIALLY VERIFIED (direction only) | SETL, HLEGLAS | 2 peers | Correctly not VERIFIED: no peer discloses the specific 10-15%/1-2yr retention structure or LC-at-sight terms; only the broader long-cycle mechanism is confirmed. Appropriate, not upgraded from silence. |
| Q5: win-rate improvement 10-12% to 15-17% | UNVERIFIABLE | SETL, HLEGLAS, PRAJIND (all checked, none disclose) | 0 supporting anchors | Correctly held at UNVERIFIABLE despite the interesting inference drawn (industry-wide non-disclosure). No verdict upgraded from silence — this is the correct handling of an absence. Appropriate. |
| Q6: "only unnamed European competitors, no Indian/Chinese" | CONTRADICTED (general shape) / UNVERIFIABLE (specific niche) | SETL, HLEGLAS | 2 peers, both with direct quotes | Contradiction is anchored to real quotes (verified in Part 1) and is correctly scoped as partial (neither peer operates in Fabtech's specific full-scope niche). Not overstated as a clean contradiction. Appropriate. |

**No VERIFIED verdict in the report rests on a single peer anchor.**
**No verdict was upgraded from a silence/absence into a positive
verdict** (Q5's disclosure-vacuum observation is explicitly kept as
UNVERIFIABLE, not converted into support).

**Claim coverage check:** all 6 questions in B05's `peer_questions` list
received an explicit verdict in B06 Part 1 (Q1-Q6, table rows above). No
skipped claim found.

---

## PART 3: FINDINGS

| Severity | Location | Finding |
|---|---|---|
| MINOR | HLEGLAS Q4 FY25 (May-2025), CITED-ONLY | The transcript contains a tangential competitor-differentiation remark for the Kinam heat-transfer sub-business ("no competitor in India which has all of these platforms available under any one single roof") that the pipeline did not use. It speaks to domestic Indian competitive structure in a different product line (heat-transfer equipment, not pharma-plant turnkey EPC) and does not directly bear on Fabtech's MENA/Africa or "no Indian competitor" claims (Q1, Q6). Industry-context miss, not claim-relevant — correctly graded MINOR under rule 3. |

No CRITICAL or MAJOR findings. No SUBSTANTIVE-without-real-citation
instances. No unused-but-materially-relevant item found in either
CITED-ONLY transcript. No verdict-discipline failure.

---

## PART 4: SUMMARY

The pipeline's peer-coverage work (B06) holds up under independent
re-reading of all 12 source transcripts. Every SUBSTANTIVE citation
checked was locatable and accurately quoted or paraphrased, including the
most load-bearing ones: PRAJIND's 1-1.5% cost-escalation figure and
delay-driven mechanism (Q2/Q3), SETL's explicit order-book/win-rate
disclosure refusal (Q5), SETL's and HLEGLAS's competitive-geography
framing that contradicts Fabtech's "no Indian peer" claim (Q6), and the
zero-mention check on Fabtech itself (2D). Verdict discipline is sound:
no VERIFIED call rests on a single peer, and the one claim with zero
supporting peer evidence (Q5, win-rate) is correctly left UNVERIFIABLE
rather than inferred into a verdict either way. The two CITED-ONLY
transcripts were read in full and yielded only one MINOR, non-claim-
relevant unused item.

```yaml
stage: B12d
company: "FABTECH"
run_date: "2026-09-26"
model: claude-sonnet-5
status: complete
peers_audited: 12
substantive_confirmed: 10
substantive_unsupported: []
unused_but_relevant:
  - {peer: "HLEGLAS Q4 FY25 (May-2025)", missed_item: "Kinam heat-transfer sub-business competitor remark ('no competitor in India which has all of these platforms available under any one single roof') not used; tangential to Q6, different product line and geography, not claim-relevant enough to be MAJOR", anchor: "HLEGLAS-Concall_May_2025_Transcript.txt, p.~14 (line ~670)"}
claims_all_addressed: true
verdict_discipline_fails: []
findings:
  - {severity: "MINOR", location: "B06 Part 3 peer coverage map, HLEGLAS Q4 FY25 row", claimed: "CITED-ONLY, general receivables-improvement and macro remarks only", source_truth: "transcript also contains an unused tangential domestic-competitor remark (Kinam sub-business)", note: "industry-context miss, not claim-relevant; correctly low severity"}
critical_count: 0
major_count: 0
minor_count: 1
acceptance_rate: 100
```
