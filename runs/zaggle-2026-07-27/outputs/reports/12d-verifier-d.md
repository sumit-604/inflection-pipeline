# Verifier D: Peer Coverage Audit — ZAGGLE (run 2026-07-27)

Model: claude-sonnet-5 | Fresh context | Inputs: 7 peer transcripts (Capillary
Feb-2026, Capillary May-2026, RateGain Nov-2025, RateGain Feb-2026, Tanla
Jul-2025, Tanla Oct-2025, Tanla Jan-2026), B06 (06-peers.md), and B05's
peer_questions[] list.

Scope per rubric: did the pipeline actually USE the peers it claims to have
used? Every transcript was read in full and cross-checked against B06's
Part 1-3 citations.

## PART 1: COVERAGE AUDIT TABLE (all 7 transcripts marked SUBSTANTIVE in B06)

| Peer / Call | B06 label | Citations checked | Verdict |
|---|---|---|---|
| Capillary Q3 FY26 (Feb-2026) | SUBSTANTIVE | Q6 AI/migration cross-read; NRR 111%/organic 115%; new order book INR66cr vs INR53cr; 0.5-1.5x revenue / 4-5yr payback M&A math | All located verbatim in transcript. CONFIRMED |
| Capillary Q4 FY26 (May-2026) | SUBSTANTIVE | SessionM $35mn/closed May 1; two-to-four-week UAT vs 24-36mo legacy migration; inorganic NRR 94%; Kognitiv churn-indemnity clause (Anant Choubey) | All located verbatim. CONFIRMED |
| RateGain Q2 FY26 (Nov-2025) | SUBSTANTIVE | GRR/local churn "consistent at 10%"; lost MHS customer; INR1,090cr utilized on Sojern; VIVA/15-20% OTA take-rate pricing model | All located verbatim (see Part 3 note on call-date for the VIVA quote). CONFIRMED with one minor date mislabel |
| RateGain Q3 FY26 (Feb-2026) | SUBSTANTIVE | $12mn annualized cost synergies in 100 days; "large section of what we code now is AI generated...white code projects"; performance-linked pricing | All located verbatim. CONFIRMED |
| Tanla Q1 FY26 (Jul-2025) | SUBSTANTIVE | INR175cr buyback / ~INR1,000cr 5-yr shareholder return; zero-debt balance sheet; no M&A executed | All located verbatim. CONFIRMED |
| Tanla Q2 FY26 (Oct-2025) | SUBSTANTIVE | Dream11/gaming regulation "overnight...entire business has gone" (Deepak Goyal); Meta/WhatsApp incentive volatility | All located verbatim. CONFIRMED |
| Tanla Q3 FY26 (Jan-2026) | SUBSTANTIVE | UPI "going through the roof" (Deepak Goyal); CPaaS TAM "8% to 12%" (Anubhav Batra); NIC tender dispute; pricing pressure "that remains" — **plus a fabricated AI/vibe-coding citation, see Finding 1** | Genuine citations CONFIRMED; one citation in this row is **NOT FOUND / MISATTRIBUTED** |

**substantive_confirmed: 6 of 7 transcripts have no issues at all.** The
seventh (Tanla Q3 FY26, Jan-2026) earns its SUBSTANTIVE label honestly on
three genuine citations (UPI, CPaaS TAM, NIC tender) but also carries one
fabricated citation described below.

## PART 2: THE CRITICAL FINDING — a RateGain quote misattributed to Tanla

B06 Part 1, Q6 ("comparable AI-driven productivity gains") states:

> "Tanla: 'half of the code that we write is AI generated... vibe coding'
> used for faster prototyping — 'what used to take us several months to
> build and prototype now can be done in weeks' (TANLA Q3 FY26 call,
> Jan-2026, Bhanu... [Uday Kumar Reddy])."

I read all three Tanla transcripts in full (Jul-2025, Oct-2025, Jan-2026).
**This quote does not appear anywhere in any Tanla transcript.** Tanla never
discusses AI-generated code, "vibe coding," or engineering/prototyping cycle
compression in any of the three calls provided. The report's own citation
betrays the error — it names "Bhanu" (no Tanla speaker is named Bhanu; Bhanu
Chopra is RateGain's founder) and then self-corrects mid-citation to "[Uday
Kumar Reddy]," but Uday Kumar Reddy never said this either.

The actual source: RateGain Q3 FY26 call (Feb-2026), Bhanu Chopra, in
response to a question from Aditya Jhawar about AI priorities:

> "...even from our perspective, whatever products we are building now half
> of the code that we write is AI generated... pretty much across all our
> teams we have introduced by vibe coding and build AI tools to get these
> productivity gains... Similarly, we are using it in faster prototyping in
> new ideas. What used to take us several months to build and prototype now
> can be done in weeks..."

This is a **second, distinct RateGain quote** from the same Feb-2026 call
already cited once elsewhere in the same B06 paragraph ("a large section of
what we code now is AI generated... white code projects," also Bhanu Chopra,
Feb-2026). B06 has effectively used one RateGain call twice and dressed one
of the two citations up as an independent Tanla data point.

**Consequence:** B06's Q6 verdict is "PARTIALLY VERIFIED (direction
corroborated by three peers)" and the triangulation summary states this
claim is "independently described by all three peers." In fact only **two**
peers (Capillary and RateGain) address AI-driven productivity/dev-cycle
compression at all; Tanla is silent on it across all three of its
transcripts. Per the rubric, converting a peer's silence into affirmative
corroborating evidence is a **CRITICAL** finding — it inflates the strength
of the pipeline's single "confirmed" (partially) claim by fabricating a
third independent source where none exists. This also propagates into Part
3's coverage map, which lists "AI/vibe-coding commentary for Q6" as a
genuine Tanla Jan-2026 contribution.

This does not, on its own, invalidate the underlying direction of the
claim — Capillary and RateGain genuinely do describe AI compressing
engineering/migration timelines — but the pipeline's own stated evidentiary
weight ("three structurally different peers independently...") is
overstated by 50% (three claimed, two real, one of the two double-counted).

## PART 3: SECONDARY (MINOR) CITATION-DATE ISSUES

**Finding 2 — Part 3 coverage-map internal inconsistency (MINOR).** The
coverage map's Tanla Q1 FY26 (Jul-2025) row lists "CPaaS TAM commentary
informing Q1" as a contribution. The actual quantified figure used in Part 1
Q1 ("8% to 12% range year-on-year") is correctly cited there as coming from
the Jan-2026 (Q3 FY26) call, Anubhav Batra — not the Jul-2025 call. Part 1's
own citation is accurate; only the Part 3 summary table misattributes which
quarter's call supplied the number. Presentational, not an evidence
fabrication.

**Finding 3 — RateGain VIVA-pricing call-date bundling (MINOR).** Part 2B
bundles two RateGain statements under one citation ("RATEGAIN Q3 FY26 call,
Feb-2026, Bhanu Chopra"): the "performance-linked pricing" quote (genuinely
Feb-2026) and the claim that RateGain "prices its new VIVA voice-booking
product below the 15-20% OTA take-rate it displaces." The 15-20% OTA
take-rate quote is actually from the **Nov-2025 (Q2 FY26) call**, in the
same answer where Bhanu Chopra first discusses VIVA. The substance is
genuinely anchored; the quarter attribution for that specific clause is
off by one call.

## PART 4: UNUSED-BUT-RELEVANT SPOT-READ (industry-context misses, MINOR)

Reading each peer transcript independently against Zaggle's claim list, two
industry-context items were available but not folded into B06's cross-reads
(neither is claim-relevant enough to rise above MINOR per the rubric):

- **RateGain (Nov-2025 call):** the Skift Travel Health Index commentary
  ("Global Health Index stood at 101, reflecting the sector's ability to
  sustain momentum despite ongoing geopolitical challenges") is a
  ready-made macro-demand data point that could have sharpened Part 2A's
  demand-environment cross-read; left unused.
- **Tanla (Jan-2026 call):** an analyst (Dharwi Sharma) raises a structural
  OTP-to-passkey migration risk to Tanla's core SMS business, which
  Anubhav Batra rebuts confidently ("we have not seen any drop... in the
  volumes"). This is a genuine risk-disclosure exchange in the same spirit
  as B06's Part 2E disclosure-candor theme, but it concerns Tanla's own
  terminal-value risk rather than anything transferable to Zaggle; left
  unused, reasonably.

No directly claim-relevant peer statement was found unused in any
transcript; both misses above are industry-context only.

## PART 5: VERDICT-DISCIPLINE AUDIT

- **Claims fully VERIFIED:** 0 of 7. No rule-4 "single-peer VERIFIED"
  violation is possible since none were marked VERIFIED.
- **Claims PARTIALLY VERIFIED:** 1 of 7 (Q6). As detailed in Part 2 above,
  this verdict's stated evidentiary base ("three peers") is fabricated by
  one-third; genuine corroboration is 2 peers, with one peer's call quoted
  twice. **FAIL — CRITICAL** (verdict strength upgraded from partial silence
  via a misattributed citation).
- **Claims UNVERIFIABLE:** 6 of 7 (Q1-Q5, Q7). Spot-checked each against the
  transcripts; all six "peers silent" / "structurally non-comparable"
  characterizations are fair and accurately reflect what is (and is not) in
  the seven transcripts. No peer statement was found that would upgrade any
  of these six to VERIFIED, PARTIALLY VERIFIED, or CONTRADICTED. PASS.
- **All B05 peer_questions[] entries (Q1-Q7) received a verdict in B06 Part
  1.** No skipped claim. PASS — claims_all_addressed: true.
- **Part 2D "no peer mentions Zaggle"** — independently confirmed; no
  mention of Zaggle by name or unmistakable description in any of the 7
  transcripts. PASS.

## PART 6: TRIANGULATION-SUMMARY SPOT CHECK

The other Part 4 (B06) summary claims were spot-checked and hold up:
Capillary's organic growth, RateGain's churn/GRR disclosure, Tanla's
Dream11 concentration-loss disclosure, and the disclosure-candor contrast
in Part 2E (the single most consequential cross-read finding) are all
accurately anchored and characterized. The one place the triangulation
summary overstates itself is precisely Q6, covered in Part 2 above.

## SUMMARY

Of 7 peer transcripts, 6 are cleanly and honestly used with every citation
verified in the source. The seventh (Tanla Q3 FY26 / Jan-2026) has three
genuine, correctly cited contributions but also carries one fabricated
citation — a RateGain quote relabeled as Tanla's — that inflates the
pipeline's only non-zero corroboration verdict (Q6) from two genuine peers
to a claimed three. This is a CRITICAL finding under the verdict-upgraded-
from-silence rule. Two further MINOR call-date misattributions and two
MINOR unused industry-context items round out the audit. No peer was
under-used, over-cited without support, or skipped; the fleet-management
(Q7) and cashback-ratio (Q2) UNVERIFIABLE calls are correctly reasoned as
structural non-overlap rather than evidentiary contradiction.

peers_audited: 7 (transcript-level) | substantive_confirmed: 6 fully clean,
1 with an embedded fabrication | acceptance_rate: 6/7 = 86%

```yaml
stage: B12d
company: "ZAGGLE"
run_date: "2026-07-27"
model: claude-sonnet-5
status: complete
peers_audited: 7
substantive_confirmed: 6
substantive_unsupported:
  - "Tanla Q3 FY26 (Jan-2026 call): the Q6 AI/vibe-coding productivity citation attributed to Tanla ('half of the code that we write is AI generated... vibe coding... what used to take us several months to build and prototype now can be done in weeks') does not appear in any Tanla transcript. It is a RateGain quote (Bhanu Chopra, RATEGAIN Q3 FY26 call, Feb-2026) misattributed. Tanla's other citations in this row (UPI, CPaaS TAM, NIC tender) are genuine and confirmed."
unused_but_relevant:
  - {peer: "RateGain (Q2 FY26, Nov-2025 call)", missed_item: "Skift Travel Health Index macro-demand commentary (Global Health Index at 101, sector resilience despite geopolitical headwinds) not folded into the Part 2A demand-environment cross-read", anchor: "RATEGAIN Q2 FY26 call, Nov-2025, Bhanu Chopra opening remarks"}
  - {peer: "Tanla (Q3 FY26, Jan-2026 call)", missed_item: "OTP-to-passkey structural migration risk raised by an analyst and rebutted by management (no OTP volume decline seen) — an industry risk-disclosure exchange left unused, though not directly Zaggle-relevant", anchor: "TANLA Q3 FY26 call, Jan-2026, Dharwi Sharma/Anubhav Batra exchange"}
claims_all_addressed: true
verdict_discipline_fails:
  - {claim: "Q6 — comparable AI-driven productivity gains", issue: "PARTIALLY VERIFIED verdict and triangulation summary claim 'three peers' independently corroborate; genuine corroboration is two peers (Capillary, RateGain), with RateGain's Feb-2026 call quoted twice and one instance relabeled as Tanla. Tanla is silent on AI/dev-cycle compression across all three of its transcripts.", severity: "CRITICAL"}
findings:
  - {severity: "CRITICAL", location: "B06 Part 1 Q6 / Part 3 coverage map, Tanla Q3 FY26 (Jan-2026) row", claimed: "Quote 'half of the code that we write is AI generated...vibe coding...what used to take us several months to build and prototype now can be done in weeks' cited to TANLA Q3 FY26 call, Jan-2026, Bhanu.../Uday Kumar Reddy", source_truth: "Quote is from RATEGAIN Q3 FY26 call, Feb-2026, Bhanu Chopra (Aditya Jhawar exchange) — a second RateGain quote from a call already cited once elsewhere in the same B06 paragraph. Not present in any Tanla transcript.", note: "Converts Tanla's actual silence on this topic into fabricated corroborating evidence; inflates Q6 triangulation from 2 genuine peers to a claimed 3.", source_fidelity: true}
  - {severity: "MINOR", location: "B06 Part 3 coverage map, Tanla Q1 FY26 (Jul-2025) row", claimed: "Row lists 'CPaaS TAM commentary informing Q1' as a Jul-2025-call contribution", source_truth: "The quantified 8-12% CPaaS TAM growth figure used in Part 1 Q1 is correctly cited there as coming from the Jan-2026 (Q3 FY26) call, Anubhav Batra, not Jul-2025.", note: "Internal inconsistency between Part 1's own correct citation and Part 3's summary table; presentational only."}
  - {severity: "MINOR", location: "B06 Part 2B pricing cross-read", claimed: "RateGain VIVA-below-OTA-take-rate (15-20%) statement bundled under 'RATEGAIN Q3 FY26 call, Feb-2026, Bhanu Chopra'", source_truth: "The 15-20% OTA take-rate/VIVA quote is from the Nov-2025 (Q2 FY26) call, in the same answer that first discusses VIVA.", note: "Substance is genuinely anchored; quarter attribution for this one clause is off by one call."}
critical_count: 1
major_count: 0
minor_count: 4
acceptance_rate: 86
```
