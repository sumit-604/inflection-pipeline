# VERIFIER D: PEER COVERAGE AUDIT — Millworks Technologies Limited (MILLWORKS)
Run date: 2026-08-22 | Model: claude-sonnet-5 | Audits: B06-peers.md against the 7 peer transcripts and the B05 peer_questions list

Scope note: 7 peer transcripts were provided (Unimech x4, Airfloa x2, Apsis x1), not the 12 named in the
stage-12 template header. B06 itself documents this as the full peer set for this run (NO-CONCALL mode,
peers verify B05 claims rather than a main-company concall). This audit covers all 7 transcripts actually
supplied and read; "peers_provided" below is set to 7 to match the run's actual scope, not the template's
generic count.

---

## PART 1: COVERAGE MAP AUDIT — is every SUBSTANTIVE label backed by a real, findable citation?

All 7 peer-transcript entries in B06's Part 3 coverage map are marked SUBSTANTIVE. For each, I located the
underlying transcript text independently (full read or targeted grep across the source file) and checked
it against B06's citations in Parts 1–2.

| Peer / call | B06 claim used for | Verified in transcript? | Anchor precision |
|---|---|---|---|
| UNIMECH Feb 2026 (Q3 FY26) | Nuclear/Shanti Bill tailwind; utilization ~60%; WC guidance 150-160 days; "not present" in domestic defence; competitor names declined | YES — all four quotes located verbatim | "p.6" (utilization/WC) is EXACT (internal doc page 6 of 19). "p.4-5" (Shanti Bill) is imprecise, quote is solely on internal p.4. "p.11" (no domestic defence presence) is off by one, actual is internal p.10; the adjacent "p.10-11" (competitor-naming decline) correctly captures the same block starting at p.10. |
| UNIMECH May 2026 (Apr 28 Acquisition/Hobel call) | Hobel two-OEM 93% revenue concentration; 50-60% utilization at acquisition | YES — "two key OEMs or the OEM groups who contribute close to around 93% of their revenue" located verbatim | "p.9-10" is accurate (internal doc page 9). |
| UNIMECH Jun 2026 (May 29, Q4/FY26) | WC days ~120-125; utilization ~50%; order book Rs314cr | YES — all three figures located verbatim | Utilization "~50%" at "p.7" is EXACT. WC days "~120-125" cited at "p.7" is off by one page — actual internal page is 6 (same paragraph as the utilization figure, one page earlier in the transcript). |
| UNIMECH Aug 2026 (Q1 FY27) | WC trending to 160+; utilization 58%; 100% tariff-threat Q&A; FACC agreement | YES — all located verbatim, including the FACC Austria USD7.5mn agreement (not separately anchored by B06 but confirmed real) | "p.6" (WC/utilization) and "p.16" (tariff Q&A) are both EXACT matches to internal doc pagination. |
| AIRFLOA Nov 2025 (H1 FY26) | Utilization 85%; Rs65cr defence order book; Big Bang Boom drone/anti-drone JV | YES — all located verbatim | "p.9-10" (utilization 85%) is accurate. The specific "autonomous drones and anti-drone laser systems" characterization (used in the Q4 answer, cited "Nov 2025, p.4-5") is more precisely located on internal p.8, where drone/anti-drone/radar/laser systems are named explicitly; p.4-5 only carries the general JV announcement and the Rs65cr defence order figure, not the drone/laser detail. |
| AIRFLOA Jun 2026 (H2/FY26) | Receivable days improved 24 days; raw-material inflation "because of the war"; 66%/114% growth; 90% utilization; Rs120cr debt at 8.25%; China machinery delay | Receivable-days quote, growth and utilization figures YES, verbatim and correctly anchored. Raw-material/war quote: content is real ("increase of more than 80% of price for aluminium... 60% to 65%... stainless steel... because of the war that has been happening") but is NOT on the cited page. | "p.4-5" (receivable days) is EXACT. "p.12-13" (aluminium/stainless/war quote) is WRONG — the actual location is internal doc page 9; pages 12-13 of this transcript instead cover the defence order-book breakdown and R&D spend Q&A, an unrelated exchange. This is a genuine mis-citation, not a rounding difference: a reader following the cited page would not find the quoted material. "p.20" (China machinery delay) is off by one, actual is internal p.19. "p.11" (8.25% debt rate, within "p.7-8, p.11") is off by one, actual is internal p.10; the Rs120cr commitment itself is correctly located around p.8. |
| APSISAERO Jun 2026 (H2/FY26) | Collection period ~45 days stable, receivables 18.38%→13.14%; customer concentration 52%→35%/top5 94%→87%; Unit 1 100% utilized ahead of Unit 2 Rs60cr capex; defence 65%/Rs20cr of Rs30.65cr; "hardly one or two competitors" | YES — all located verbatim | "p.13" ("hardly one or two competitors") is EXACT. "p.3-4" (defence 65%/Rs20cr/Rs30.65cr) is reasonably accurate, the figures recur on internal p.2 and p.4. "p.4" (collection period/receivables%) is off by one, actual is internal p.5. "p.5" (Atmanirbhar Bharat FY27-priority quote) is off by two, actual is internal p.3. "p.4" (customer-concentration reduction, cited in Part 2E) is off by one, actual is internal p.5. "p.7-8" (Unit 1 100% utilized) correctly captures the "completely utilised" Q&A on internal p.8, but the Rs60cr Unit 2 capex figure it is paired with actually first appears on internal p.2, not p.7. |

**Finding on Part 1.** No fabricated quotes and no invented figures were found anywhere across the 7
transcripts. Every substantive claim I checked exists in the source text, in the sense the report describes
it. However, page-citation precision is inconsistent: roughly half the anchors I checked land on the exact
internal transcript page, and the other half are off by one to two pages (locatable with minor effort). One
citation (Airfloa Jun 2026 "p.12-13" for the aluminium/steel/war quote) is a real miss — the cited page
contains unrelated Q&A content, and the actual quote is four pages earlier (p.9). This is a source-fidelity
gap in the anchor, not in the substance: the claim itself is accurately quoted and correctly used to support
the Q2 contradiction and the 2B cross-read finding, just pointed at the wrong page number.

All 7 SUBSTANTIVE labels in B06's Part 3 coverage map are CONFIRMED as genuinely substantive: each
transcript contributes multiple distinct, real pieces of evidence that materially inform at least one of the
six injected claims or the cross-read sections. None reads as cited-only or decorative.

---

## PART 2: UNUSED-OR-CITED-ONLY CHECK

B06 marks zero peers as UNUSED or CITED-ONLY, so Rule 3's comparison table has no rows to audit directly.
I instead spot-read each transcript against the claim list for material the pipeline could have used but
did not.

- No fabricated or overstated peer contribution found.
- One tangential item not picked up: Airfloa Jun 2026 management flags that the "timeline towards Rs.1000
  Crores revenue milestone may [slip]" (internal p.3-4 area) — a guidance-walkback signal about Airfloa's
  own growth trajectory. This does not map to any of the six injected Millworks claims and is Airfloa's own
  promise-delivery matter, not peer evidence about Millworks; omitting it from B06 is reasonable and not a
  coverage gap. Flagged here only as INDUSTRY-CONTEXT MINOR, not MAJOR, per Rule 3's own distinction.
- No other claim-relevant peer statement was found left unused in my read-through of the four Unimech
  calls, two Airfloa calls, or the Apsis call.

---

## PART 3: VERDICT-DISCIPLINE AUDIT

Rule 4 (>=2 independent peer anchors for any VERIFIED claim; single-peer VERIFIED is MAJOR; any verdict
upgraded from silence is CRITICAL):

- B06's Part 4 triangulation summary records **0 of 6 claims VERIFIED**. There is therefore no VERIFIED
  verdict to test against the two-independent-anchor rule — the rule does not trigger.
- PARTIALLY VERIFIED and UNVERIFIABLE verdicts do not carry the same two-anchor requirement under Rule 4
  (which applies only to VERIFIED). Spot-checking anyway: Q1 (defence tailwind) rests on three peers
  (Unimech, Apsis, Airfloa), Q5 (capex-vs-utilization) rests on three peers, Q6 (Railways growth) rests on
  one peer (Airfloa) but Airfloa was the only rail-sector peer named in B05's check_peers list for that
  question — single-peer support is the ceiling the injected question allows, not a shortfall.
- CONTRADICTED (Q2): rests on two independent peers (Apsis, Airfloa) both showing stable-to-improving
  receivable metrics, with a third peer (Unimech) providing a business-mix explanation for its own WC-day
  rise rather than a war/geopolitical one. This is adequately multi-sourced for a CONTRADICTED verdict; not
  a single-peer call.
- No verdict I could find was upgraded from peer silence to a stronger claim than the evidence supports;
  Q4's UNVERIFIABLE verdict explicitly self-flags its "silence is informative" reasoning as an inference, not
  confirmed evidence — correct discipline, not an overreach to CONTRADICTED or VERIFIED.
- **No verdict-discipline failures found.**

Rule 5 (every claim in the injected peer_questions list gets a verdict): B05-concall.yaml's peer_questions
list has exactly 6 entries (Q1–Q6). B06 Part 1 addresses all 6 in order, each with a verdict. **All claims
addressed.** check_peers assignments in B05 are also honoured: Q3 and Q6 correctly restrict peer scope to
the named subset (Unimech only; Airfloa only) and B06 does not claim verification from peers outside that
scope, while transparently noting when an out-of-scope peer (e.g., Airfloa for Q4) offers relevant
corroborating context — additive, not a violation.

---

## PART 4: OVERALL ASSESSMENT

The substance of B06 is sound: every peer classification, every quoted figure, and every characterization
of peer management commentary I checked is a real, accurate representation of what is in the transcripts.
I found zero fabricated citations, zero invented numbers, and zero misclassified verdicts. The
CONTRADICTED call on Q2 and the UNVERIFIABLE calls on Q3/Q4 are all well-supported by the actual transcript
text, and the report's own hedging (flagging Q4 as an inference from absence) shows appropriate discipline.

The one systemic weakness is anchor precision: a material share of page citations across all three peer
companies are off by one to two pages from the internal transcript pagination, and one citation (Airfloa
Jun 2026 "p.12-13" for the war/raw-material quote) points to the wrong page entirely — a reader following
that specific citation would land on unrelated Q&A content. This does not change any verdict or any
finding's substance, since the underlying quote is genuine and correctly used, but it is a real
verifiability gap that should be tightened before this report is treated as a citation-checkable source of
record.

---

```yaml
stage: B12d
company: "MILLWORKS"
run_date: "2026-08-22"
model: claude-sonnet-5
status: complete
peers_audited: 7
substantive_confirmed: 7
substantive_unsupported: []
unused_but_relevant:
  - {peer: "AIRFLOA (544516) Jun 2026", missed_item: "Rs.1000 Crores revenue-milestone timeline slippage flagged by management (own guidance walkback, not mapped to any injected Millworks claim)", anchor: "Airfloa 544516 Jun 2026 Transcript, internal p.3-4 area"}
claims_all_addressed: true
verdict_discipline_fails: []
findings:
  - {severity: "MAJOR", location: "B06-peers.md Part 2B / Part 1 Q2, citation 'Airfloa Jun 2026, p.12-13'", description: "The aluminium (+80%) / stainless steel (+60-65%) / 'because of the war that has been happening' quote is genuine but does not appear on the cited pages. Pages 12-13 of the Airfloa Jun 2026 transcript cover the defence order-book breakdown and R&D-spend Q&A, an unrelated exchange. The actual quote is on internal doc page 9 (peer: AIRFLOA 544516, transcript: 544516-Concall_Jun_2026_Transcript.txt, page 9 internal / extraction page 10)."}
  - {severity: "MINOR", location: "B06-peers.md Part 1 Q3/Q4 and Part 2D, citation 'Feb 2026, p.11' and 'p.10-11'", description: "Unimech's 'we are not present, but continuing to explore' domestic-defence statement and the MTAR/competitor-naming exchange are both on internal doc page 10, not page 11 as cited in one instance (peer: UNIMECH, transcript: UNIMECH-Concall_Feb_2026_Transcript.txt)."}
  - {severity: "MINOR", location: "B06-peers.md Part 1 Q3, citation 'Jun 2026, p.7' for working-capital days ~120-125", description: "The '120 to 125 days at the year-end' figure is on internal doc page 6, one page earlier than cited; the adjacent utilization figure (~50%) on the same citation is correctly on page 7 (peer: UNIMECH, transcript: UNIMECH-Concall_Jun_2026_Transcript.txt)."}
  - {severity: "MINOR", location: "B06-peers.md Part 1 Q2 and Part 2E, citations 'Apsis Jun 2026 p.4' (collection period/receivables%) and 'p.4' (customer concentration)", description: "The 45-day collection-period/18.38%->13.14% receivables quote and the 52%->35% top-customer / 94%->87% top-5 concentration figures are both on internal doc page 5, not page 4 as cited (peer: APSISAERO, transcript: APSISAERO-Concall_Jun_2026_Transcript.txt)."}
  - {severity: "MINOR", location: "B06-peers.md Part 1 Q1, citation 'Apsis Jun 2026, p.5' for the Atmanirbhar Bharat FY27-priority quote", description: "'Deepening partnerships with global OEMs and expanding our footprint in defence manufacturing under the Atmanirbhar Bharat programme' is on internal doc page 3, two pages earlier than cited (peer: APSISAERO, transcript: APSISAERO-Concall_Jun_2026_Transcript.txt)."}
  - {severity: "MINOR", location: "B06-peers.md Part 2E, citations 'Airfloa Jun 2026, p.20' (China machinery delay) and 'p.11' (within 'p.7-8, p.11', 8.25% debt rate)", description: "The China end-user-certificate machinery-delay discussion is on internal doc page 19, not 20; the 8.25% interest-rate statement is on internal doc page 10, not 11. The paired Rs120cr debt-commitment figure in the same citation is correctly anchored to page 8 (peer: AIRFLOA 544516, transcript: 544516-Concall_Jun_2026_Transcript.txt)."}
  - {severity: "MINOR", location: "B06-peers.md Part 1 Q4, citation 'Airfloa Nov 2025, p.4-5' for 'autonomous drones and anti-drone laser systems'", description: "The general Big Bang Boom JV disclosure and the Rs65cr defence order figure are correctly on internal doc pages 3-4, but the specific drone/anti-drone/radar/laser-systems characterization used in the same sentence is more precisely located on internal doc page 8 (peer: AIRFLOA 544516, transcript: 544516-Concall_Nov_2025_Transcript.txt)."}
critical_count: 0
major_count: 1
minor_count: 6
acceptance_rate: 100    # 7 of 7 peers correctly classified SUBSTANTIVE with genuine, verifiable underlying evidence; no fabrication, no misclassification, no verdict-discipline failure found
```
