# Verifier D: Peer Coverage Audit — FABTECH (2026-08-04)
Fresh-context audit of Stage 6 (B06-peers). Model: claude-sonnet-5.

Scope per rubric: did Stage 6 actually USE the 12 provided arm's-length peer
transcripts (Anup Engineering, HLE Glascoat, Ion Exchange, Praj Industries —
3 calls each), and are its SUBSTANTIVE / CITED-ONLY / UNUSED classifications
and its six claim verdicts (VERIFIED / PARTIALLY VERIFIED / UNVERIFIABLE /
CONTRADICTED) supported when checked against the raw transcripts read fresh
by this verifier? All 12 PDFs were read directly (not taken on B06's word).
The excluded fifth file set (BSE 544332, Fabtech Technologies Cleanrooms
Ltd) was correctly treated by B06 as a related-party entity, not an
arm's-length peer, and is not counted against peer_utilisation — this
exclusion is itself correct and is not re-litigated here.

Note on method: an initial read of the three ANUP transcripts returned no
visible page content to this verifier (a tool artifact). Rather than rely on
inference from B06's own claims, all three ANUP files were re-read in full
before any finding was written, specifically to avoid confirming B06's
citations against nothing. This is flagged so the orchestrator can weight
this report's ANUP-related findings as directly transcript-verified, not
second-hand.

## PART 1: Coverage-map audit (per peer-call entry, all 12 read fresh)

| Peer | Call | B06 tier | Verified? |
|---|---|---|---|
| ANUP | May 2026 (Q4 FY26) | SUBSTANTIVE | CONFIRMED — Strait of Hormuz closure/freight cost language present verbatim ("a little bit of shipping challenges currently because of the closure of Strait of Hormuz," p.8); ADNOC skid order "close to about INR30 crores single order" present (p.11); the "let go of the order... close to about INR200 crores" quote (Aashna Q&A, p.9) is genuinely IN THIS call, not misattributed — checked carefully given this is exactly the kind of cross-quarter mixup this audit looks for. |
| ANUP | Feb 2026 (Q3 FY26) | SUBSTANTIVE | CONFIRMED — "roughly about 120 days kind of working capital" (Sonal Minhas Q&A, p.13) and export advances "average 40%," domestic "average 25%" (p.14) both present verbatim. Also contains "our projects are 100% fixed term contracts. There are no variable contracts" (Ganeshram Q&A, p.15) — material for the Part 5 finding below. |
| ANUP | Nov 2025 (Q2 FY26) | SUBSTANTIVE | CONFIRMED — "working capital block was a touch high at an average 3x, that's 120 days" (p.3) and "official presence in Dubai with our sales and marketing head EME region" (p.4) both present verbatim. |
| HLEGLAS | Jun 2026 (Q4 FY26) | SUBSTANTIVE | CONFIRMED — Iran-conflict gas price pass-through and Middle East growth framing both present in substance (paraphrase in B06 is a fair characterization, not a verbatim misquote). |
| HLEGLAS | Nov 2025 (Q2 FY26) | CITED-ONLY | CONFIRMED, and re-checked directly (pp.1-22 read in full by this verifier, not taken on faith) — content is domestic glass-line/Omeras/Kinam margin discussion; no MENA/West Asia material found that B06 should have flagged as missed. B06's claimed page count ("20 of 22 pages") matches this verifier's independently-confirmed total of 22 pages — no discrepancy. |
| HLEGLAS | Aug 2025 (special, Omeras) | SUBSTANTIVE | CONFIRMED — "global investments in water and wastewater infrastructure are projected to exceed US $100 billion annually by 2030" and "delivered 350 tanks in Saudi Arabia alone in the past decade" both present verbatim. |
| IONEXCHANG | Jun 2026 (Q4 FY26) | SUBSTANTIVE | CONFIRMED — "West Asia crisis," ~Rs 60cr shipment deferral, Dammam Saudi plant, Oman DBOOT JV (51%, OMR 73.46mn) all present verbatim/near-verbatim. |
| IONEXCHANG | Feb 2026 (Q3 FY26) | CITED-ONLY | CONFIRMED — general margin/RM commentary, no West Asia crisis language of the sharpness seen in the Jun 2026 call; classification reasonable. |
| IONEXCHANG | Nov 2025 (Q2 FY26) | SUBSTANTIVE | CONFIRMED — "this is a standard norm which is followed across all EPC companies" present verbatim (percentage-of-completion/milestone billing discussion). The ~Rs 9,011 crore bid pipeline figure is also genuinely in THIS call — see Part 2 finding below on a citation-location error in the prose report. |
| PRAJIND | Jun 2026 (Q4 FY26) | SUBSTANTIVE | CONFIRMED — RM "3% raw material prices going up" (consolidated), "almost Rs. 300 plus crores inquiries which we didn't finalize," "we are not looking for building up any facility per se" all present verbatim. |
| PRAJIND | Feb 2026 (Q3 FY26) | SUBSTANTIVE | CONFIRMED — "Rs.10,000 crores Biopharma Shakti Program" and "incremental Rs.3,344 million impact" (labor code) both present verbatim; Kandla "milestone payments happening in between" also present. |
| PRAJIND | Nov 2025 (Q2 FY26) | SUBSTANTIVE | CONFIRMED — "Africa margin, margins are better than India margin, but not as good as European or American margins" present verbatim; US tariff discussion and GenX pivot strategy both present. |

peers_audited: 12 (peer-call entries) — 10 SUBSTANTIVE, 2 CITED-ONLY, all
citations located and confirmed genuine in the actual transcripts.

## PART 2: Findings

**Finding 1 — MAJOR — Part 5 "Cross-Peer Hypothesis" misstates Anup Engineering's contract terms, directly contradicted by the transcripts B06 itself read and correctly quoted elsewhere.**
Location: `06-peers.md`, Part 5 (Cross-Peer Hypothesis section).
B06 states: "Anup Engineering and Praj Industries, facing the same disruption, are instead managing it through contract-term flexibility (**Anup's shift away from 100% fixed-price terms**, selective project acceptance)."
This is false on the transcripts. Anup's MD explicitly and repeatedly states the opposite in both calls B06 itself cites elsewhere in the same report:
- Feb 2026 (Q3 FY26) call, Ganeshram Q&A: *"No, Ganesh, in our case, our projects are 100% fixed term contracts. There are no variable contracts."*
- May 2026 (Q4 FY26) call, Aashna Q&A: *"No price variability clause in our contracts. Historically, it has never been."*
There is no shift; Anup states its pricing model has never varied. The "selective project acceptance" half of the same sentence (letting go of the ~Rs 200cr order) is accurate and independently confirmed. Only the "shift away from 100% fixed-price terms" clause is fabricated — it appears to be an inference the analysis reached for to complete a tidy "capital-light / contract-flexible" contrast with the "capital-committed" camp (Ion Exchange, HLE Glascoat), but it is not supported and is directly contradicted by the source. This does not change any of the six formal claim verdicts (Q1-Q6), which are otherwise well-anchored, but it weakens the reliability of Part 5's synthesis conclusion and should not be carried into Stage 13 without correction.

**Finding 2 — MINOR — Ion Exchange Rs 9,011cr bid-pipeline figure is correctly sourced in the B06 YAML block but mislabeled by quarter in the prose report.**
Location: `06-peers.md`, Part 2 (2A Demand environment): *"Ion Exchange describes strong, supply-constrained demand in its chemicals segment and a large (~Rs 9,011 crore) engineering bid pipeline (IONEXCHANG, Feb 2026/Q3 FY26 call)."*
The actual quote — *"Our current bid pipeline stands at approximately Rs. 9,011 crores"* (Saket Kapoor Q&A) — is in the **Nov 2025/Q2 FY26** call, not the Feb 2026/Q3 FY26 call. `B06-peers.yaml`'s own `peer_coverage_map` correctly attributes this figure to "Ion Exchange, Q2 FY26 (Nov 2025 call)" — so the underlying research is right, but the human-readable report text cites the wrong call. Anyone checking this specific citation against the Feb 2026 transcript (as labeled in the prose) would not find it. Low materiality since the figure itself is genuine and correctly anchored in the machine-readable block.

## PART 3: Verdict-discipline audit (Rule 4)

No claim in B06 is marked full VERIFIED (all six are PARTIALLY VERIFIED or
UNVERIFIABLE), so the "VERIFIED resting on one peer" trap does not arise.
Checked all four PARTIALLY VERIFIED claims for genuine multi-peer support:
- Q2 (RMC/execution cost, 4 peers cited): all four peers' West-Asia-linked
  cost/logistics quotes independently confirmed genuine.
- Q4 (ticket sizes, 3 peers cited): Ion Exchange Oman DBOOT (OMR 73.46mn),
  Anup ~Rs 200cr order + ADNOC skid, Praj GenX "Rs. 50 crores to as high as
  Rs. 150 crores" — all three confirmed genuine and correctly attributed.
- Q5 (revenue recognition/WC, 3 peers cited): Anup 120-day WC (both Feb and
  Nov 2025 calls), Ion Exchange "standard norm" quote, Praj Kandla milestone
  billing quote — all confirmed genuine.
- Q6 (GCC local-content, 2 peers cited): Ion Exchange Dammam plant + Oman
  JV, HLE Glascoat "350 tanks" — both confirmed genuine; B06 correctly
  notes neither independently confirms the "hard qualification mandate"
  framing itself, which is honest scoping, not an upgrade from silence.
No verdict-upgrade-from-silence found. No skipped peer_questions: all six
B05 peer_questions (Q1-Q6) received a verdict in B06 Part 1.

## PART 4: Unused-but-relevant check (Rule 3, cited-only peers)

Both CITED-ONLY calls (HLEGLAS Nov 2025, IONEXCHANG Feb 2026) were spot-read
independently by this verifier. Neither contains MENA/West-Asia-crisis
material of the kind found in the corresponding SUBSTANTIVE calls for the
same companies; B06's "no materially distinguishable content" judgment on
both holds up. unused_but_relevant: none identified.

## Summary

12 of 12 peer-call entries correctly classified (SUBSTANTIVE/CITED-ONLY)
with genuine, locatable citations. All six claim verdicts are well-anchored
by real multi-peer evidence. One MAJOR finding: a fabricated detail in
Part 5's speculative cross-peer hypothesis (Anup contract-terms claim)
directly contradicted by the same transcripts B06 read and cited correctly
elsewhere. One MINOR finding: a quarter-mislabeled citation in prose (Part
2) inconsistent with the correctly-sourced YAML block. No related-entity
(544332) miscounting, no skipped peer_questions, no verdict-discipline
failures.
