# STAGE 12d: VERIFIER D — PEER COVERAGE — QUALITEK
Run date: 2026-09-26 | Model: claude-sonnet-5

Scope: did the pipeline actually USE the 12 peer transcripts it claims, and does its
verdict discipline hold? Inputs read in full: all 12 peer transcripts (VIMTALABS x4,
METROPOLIS x4, KRSNAA x4), B06 report (outputs/reports/06-peers.md), and the six
peer_questions[] items in B05 (outputs/blocks/B05-concall.yaml).

## PART 1: COVERAGE AUDIT PER PEER

| Peer | Transcript | B06 marks | Real citation found? | Verdict |
|---|---|---|---|---|
| VIMTALABS | Q2 FY26 (Nov-2025) | SUBSTANTIVE | Yes. "50% to 60%" Phase 2 utilisation (line 392-394 of transcript); "7.5% to around 9%" sector CAGR (Samir Palod exchange). | CONFIRMED |
| VIMTALABS | Q3 FY26 (Jan-2026, filed as "Feb_2026") | SUBSTANTIVE | Yes. "Now are we going to come to the run rate of INR125 crores... maybe not, we may not touch that number" — verbatim match. Attrition quote ("attrition is quite high across the industry... that's going to be the norm") also verbatim. | CONFIRMED |
| VIMTALABS | Q4 FY26 (May-2026) | SUBSTANTIVE | Yes. Amita Modi's exact question and Harita Vasireddi's answer on the INR500 Cr target match verbatim. USD9.7bn/USD300mn TAM figures verbatim. | CONFIRMED |
| VIMTALABS | Q1 FY27 (Jul-2026) | SUBSTANTIVE | Yes. "cost of some input materials, consumables has gone up slightly... a slightly longer lead time" verbatim; 60% of 200,000 sq ft utilisation verbatim; 90%+ retention verbatim. | CONFIRMED |
| METROPOLIS | Q3 FY26 (Feb-2026) | SUBSTANTIVE | Yes. Core Diagnostics margin-trajectory language, GST 12/18%-to-5% detail, delayed January price revision — all verbatim or close paraphrase. | CONFIRMED |
| METROPOLIS | Q4 FY26 (May-2026) | SUBSTANTIVE | Yes. "we would move from a negative 2% EBITDA to a high-single-digit EBITDA in Q4. We have completed this mission" verbatim. | CONFIRMED |
| METROPOLIS | Q1 FY27 (Aug-2026) | SUBSTANTIVE | Yes. 14-15% guide vs 17% delivered, CGHS "about a percentage or so" immateriality — verbatim. **But** the "<2x revenue... effective acquisition multiple would be approximately 10x EBITDA" quote, which B06 Part 1 Q2 correctly anchors to this Aug-2026 Q1 FY27 call, is ALSO listed in B06's Part 3 coverage-map row for the separate "Investor Meet (Aug-27-2026)" transcript as that transcript's "key contribution." That quote does not appear in the investor-meet transcript (confirmed by full-text grep: zero matches for "2x revenue", "10x EBITDA", "effective acquisition multiple"). See Finding 3. | CONFIRMED (with a coverage-map misattribution, Finding 3) |
| METROPOLIS | Investor Meet (Aug-27-2026, filed "Sep_2026") | SUBSTANTIVE | Partially. The $11bn→$28.5bn/11% CAGR figure, the "less than 6% of Indians have ever been diagnosed" line, and the Core Diagnostics "1 year after acquisition, this is high single-digit EBITDA... maybe year 3 we will be close to the company levels of EBITDA" line are all verbatim in THIS transcript. The "<2x revenue/10x EBITDA" line claimed as this transcript's contribution in Part 3 is not present here (see above). | CONFIRMED for the TAM/moat content; the acquisition-multiple line is misattributed |
| KRSNAA | Q2 FY26 (Nov-2025) | SUBSTANTIVE | Yes. "receivable currently stands around 150 days" and the RBI-link-account/central-government-payment-guideline explanation are verbatim in THIS transcript. | CONFIRMED |
| KRSNAA | Q3 FY26 (Feb-2026) | SUBSTANTIVE | Partially. "Rs 130 Cr recovered in-quarter" and "Rs 100 Cr more collected than Q3 FY25" are verbatim in this transcript. Himachal/Karnataka receivable discussion is verbatim. But the specific restated figure B06 attributes to this call — "our receivable currently stands around 150 days" (repeated) — is NOT found anywhere in this transcript (grepped; only "days of outstanding moving down" appears, no number given). See Finding 2. | CONFIRMED for recovery figures; the repeated "150 days" quote is not findable here |
| KRSNAA | Q4 FY26 (May-2026) | SUBSTANTIVE | Yes. "139 days... against 155 days in the previous quarter" verbatim; "sub 120 days" FY27 guide verbatim; Mayur's exact 25%→16%/15-16%→1% guidance-miss question and Yash Mutha's response verbatim. | CONFIRMED |
| KRSNAA | Q1 FY27 (Aug-2026) | SUBSTANTIVE | Yes. "in the first year, the EBITDA was negative, I think marginally" verbatim; "confident of becoming EBITDA positive by Q2" verbatim; "Rs 26 Cr" Rajasthan first-quarter revenue verbatim; "carry their full fixed cost base from the very first day... while still operating below mature utilization levels" verbatim; Apulki "30-plus years" exclusive-rights language verbatim. | CONFIRMED |

**substantive_confirmed: 12 of 12.** Every peer transcript marked SUBSTANTIVE does contain
genuine, locatable material the pipeline used. No peer is SUBSTANTIVE-in-name-only. Two
findings below are citation-placement errors (a quote real in one transcript but claimed
for another), not fabrication — the underlying number/quote exists somewhere in the peer
corpus and was read, but B06's own cross-reference to WHICH call is wrong in each case.

**substantive_unsupported: []** — no peer's SUBSTANTIVE tag lacks any real citation.

**unused_but_relevant: []** — no peer or quarter was left unused where a directly
claim-relevant statement existed; all 12 of 12 were read and drawn on (matches B06's own
"All 12 of 12 peer transcripts were SUBSTANTIVE; none CITED-ONLY or UNUSED" claim, and I
independently confirm this from a full read, not merely accepting B06's self-report).

## PART 2: VERDICT-DISCIPLINE AUDIT PER CLAIM

| Claim (peer_questions #) | B06 verdict | Independent peer-anchor count | Discipline check |
|---|---|---|---|
| Q1 debtor days | VERIFIED | 1 peer (KRSNAA only, across 4 quarters). Metropolis explicitly stated silent/immaterial (no comparable DSO metric in any of its 4 transcripts — confirmed, I found none). Vimta never discussed. | **FAIL.** Rule 4: "any VERIFIED resting on one peer is MAJOR (should be PARTIALLY VERIFIED)." Four quotes from one company, however consistent, is one independent anchor, not two. This is a MAJOR finding (Finding 1). |
| Q2 related-party disclosure norm | CONTRADICTED | 1 peer with direct content (METROPOLIS); Vimta and Krsnaa's "silence" is itself argued as evidence, correctly flagged by B06 itself as "an inference from the absence of a matching precedent rather than a direct peer statement." Rule 4 applies only to VERIFIED verdicts; CONTRADICTED is not bound by the two-anchor rule. No fail. | PASS (rule scope; B06 itself flags the inferential nature honestly) |
| Q3 new-lab margin trajectory | VERIFIED | 3 peers (METROPOLIS Core Diagnostics, KRSNAA RPL/Rajasthan, VIMTALABS new-capacity ramp) | PASS — clears the ≥2-anchor bar with margin to spare |
| Q4 industry growth rate | VERIFIED | 2 peers with explicit CAGR figures (VIMTALABS 7-11%, METROPOLIS 11%); Krsnaa gives implied headroom only, correctly not counted as a CAGR anchor by B06 | PASS |
| Q5 guidance walk-down acknowledgment | CONTRADICTED | 2 peers (VIMTALABS, KRSNAA), both with named analyst confrontation and management acknowledgment | PASS (and not bound by the VERIFIED-only rule regardless) |
| Q6 input-cost trend | PARTIALLY VERIFIED | 3 peers | PASS |

**claims_all_addressed: true.** All six peer_questions items received a verdict (Q1-Q6);
none skipped.

**verdict_discipline_fails: 1** (Q1, detailed above).

**No verdict was upgraded from silence to a positive verdict** — the one CRITICAL-tier
check in rule 4 (upgrade from silence) does not apply anywhere in B06; every verdict traces
to a stated peer utterance or an explicitly-argued absence, never a silent invention.

## FINDINGS TABLE

| # | Severity | Location | Finding |
|---|---|---|---|
| 1 | MAJOR | B06 Part 1, Q1 verdict ("VERIFIED") | The debtor-days claim is VERIFIED on the strength of KRSNAA alone (four quotes, one company, one mechanism — RBI link account/SNA-SPARSH). METROPOLIS is explicitly silent on DSO in all four of its transcripts (confirmed by direct read: no DSO/receivable-days figure appears anywhere in the four Metropolis transcripts). VIMTALABS is never discussed for this claim. Per the Verifier D rubric, a VERIFIED verdict resting on one peer must be downgraded to PARTIALLY VERIFIED. The underlying analysis (Krsnaa's own 124-155-day band, tied to a named government-payment-system mechanism) is sound and well-anchored; only the VERIFIED label is too strong for a single-peer, single-mechanism match. |
| 2 | MAJOR | B06 Part 1, Q1 narrative row ("Peer evidence") | B06 attributes the restated quote "our receivable currently stands around 150 days" (repeated) to the Q3 FY26 (Feb-2026) call. That exact figure/quote is not present anywhere in the Feb-2026 transcript (confirmed by full-text search: no instance of "150 days" or any specific DSO number in that transcript; the only DSO-adjacent language is "has shown an impact in overall days of outstanding moving down," unquantified). The 150-day figure and its RBI-link-account explanation are real, but they belong to the Q2 FY26 (Nov-2025) call, which B06 also cites separately and correctly for the same figure. The Feb-2026 call's genuine, verifiable contribution is the Rs 130 Cr in-quarter recovery and the Rs 100 Cr YoY collection improvement, both of which are correctly quoted. The "150 days (repeated)" attribution to Feb-2026 should be struck or re-anchored to Nov-2025. |
| 3 | MAJOR | B06 Part 3, coverage-map row "METROPOLIS \| Investor Meet (Aug-27-2026)" | The row's "Key contribution" cell states: "Detailed Core Diagnostics acquisition valuation disclosure (<2x revenue, 3-4yr to 25% margin, effective 10x EBITDA on FY27 basis)." This content — the "less than 2x revenue" acquisition price and the "approximately 10x EBITDA" effective-multiple recomputation — is verbatim in the Aug-05-2026 Q1 FY27 earnings-call transcript, NOT in the Aug-27-2026 investor-meet transcript (confirmed: zero matches for "2x revenue," "10x EBITDA," or "effective acquisition multiple" anywhere in the investor-meet transcript). B06's own Part 1 Q2 narrative correctly cites this same quote to "Metropolis Aug-2026 Q1 FY27 call" — so the underlying fact is sound and correctly anchored elsewhere in the same report; only this one Part 3 coverage-map cell misattributes it to the wrong transcript. The investor meet's own genuine, verified contribution is the $11bn→$28.5bn/11% CAGR TAM figure, the "less than 6% of Indians have ever been diagnosed" line, and the "1 year after acquisition... high single-digit EBITDA... maybe year 3 we will be close to company levels" Core Diagnostics update — all confirmed present in that transcript. |
| 4 | MINOR | B06 Part 1, Q4 narrative ("7% to 9%") | B06 paraphrases Vimta's Nov-2025 sector-growth figure as "7% to 9%." The transcript's exact wording is "7.5% to around 9%." A half-point rounding on a range that is itself explicitly approximate ("anywhere between") — cosmetic, not material, and does not change any downstream reading. |
| 5 | MINOR | B06 Part 1, Q6 narrative (peer-evidence attribution) | B06 attributes the quote "the cost of some input materials, consumables has gone up slightly... a slightly longer lead time" to "(May-2026, Jul-2026 calls)." That exact language is found only in the Jul-2026 (Q1 FY27) transcript; the May-2026 (Q4 FY26) transcript does not contain it (the May-2026 transcript's manpower/cost language is a different quote — "manpower is something that continuously keeps on increasing" — which IS correctly present there). The finding itself (ongoing but manageable input-cost pressure) is well-supported across both calls with different quotes; only the specific quoted sentence is over-attributed to one call it does not appear in. |

**false_positives_struck: 0.** No candidate finding was struck; all five above pass the
identity check (claimed location and source-truth location are genuinely different) and
are not clerical restatements.

## SUMMARY

Twelve of twelve peer transcripts were read in full and independently checked against B06's
claimed usage. Every peer transcript marked SUBSTANTIVE genuinely is: the pipeline actually
read and drew on all twelve, and B06's own "12 of 12 SUBSTANTIVE, none unused" self-report
holds up under an independent re-read rather than being taken on faith. All six
peer_questions items received a verdict; none were skipped or silently dropped.

The material weakness is not fabrication but attribution precision under time pressure: one
verdict (Q1, debtor days) is graded VERIFIED when the evidence — real and well-anchored —
comes from a single peer and should read PARTIALLY VERIFIED; and two quotes (one Krsnaa DSO
figure, one Metropolis acquisition-multiple figure) are genuine and exist in the corpus but
are cross-referenced to the wrong specific call within an otherwise-correct multi-call
citation cluster. None of the three MAJOR findings would change B05/B06's substantive
conclusions if corrected — Krsnaa's receivables story and Metropolis's Core Diagnostics
valuation story both stand once the citations are pointed at the right transcript — but the
Q1 verdict label itself should change from VERIFIED to PARTIALLY VERIFIED, which the
operator should note before this feeds any downstream credibility-grade weighting.

```yaml
stage: B12d
company: "QUALITEK"
run_date: "2026-09-26"
model: claude-sonnet-5
status: complete
peers_audited: 12
substantive_confirmed: 12
substantive_unsupported: []
unused_but_relevant: []
claims_all_addressed: true
verdict_discipline_fails:
  - {claim: "Q1 debtor days (peer_questions #1)", issue: "Verdict VERIFIED rests on a single peer (KRSNAA only, across 4 quarters/one mechanism); METROPOLIS confirmed silent on DSO in all 4 transcripts, VIMTALABS never discussed. Per rule 4 should be PARTIALLY VERIFIED.", severity: "MAJOR"}
findings:
  - {severity: "MAJOR", location: "B06 Part 1, Q1 verdict", claim: "Debtor-days claim VERIFIED", issue: "Single-peer verdict overgraded; should be PARTIALLY VERIFIED per rule 4"}
  - {severity: "MAJOR", location: "B06 Part 1, Q1 peer-evidence narrative", claim: "'our receivable currently stands around 150 days (repeated)' attributed to Feb-2026 (Q3 FY26) call", issue: "Quote not found in Feb-2026 transcript (verified by full-text search); belongs to Nov-2025 (Q2 FY26) call, which is separately and correctly cited for the same figure"}
  - {severity: "MAJOR", location: "B06 Part 3 coverage map, row 'METROPOLIS | Investor Meet (Aug-27-2026)'", claim: "'<2x revenue, ... effective 10x EBITDA' listed as this transcript's key contribution", issue: "Quote not found in the investor-meet transcript (verified by full-text search); belongs to the Aug-05-2026 Q1 FY27 earnings call, which B06 Part 1 Q2 correctly cites separately"}
  - {severity: "MINOR", location: "B06 Part 1, Q4 narrative", claim: "Vimta sector CAGR paraphrased as '7% to 9%'", issue: "Transcript says '7.5% to around 9%'; cosmetic rounding, not material"}
  - {severity: "MINOR", location: "B06 Part 1, Q6 narrative", claim: "Input-cost quote attributed to '(May-2026, Jul-2026 calls)'", issue: "The specific quoted sentence is found only in Jul-2026; May-2026 has a different, also-supportive quote on manpower cost, not this one"}
critical_count: 0
major_count: 3
minor_count: 2
acceptance_rate: 100
