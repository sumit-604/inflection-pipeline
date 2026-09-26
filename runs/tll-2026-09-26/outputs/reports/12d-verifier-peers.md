# Stage 12d — Verifier D: Peer Coverage Audit, Trident Lifeline Ltd (TLL), 2026-09-26
# REWORK-ROUND AUDIT (run 2). This is a fresh audit of the current, post-rework
# B06 artifacts. No prior verifier output was read (per rule, verifiers see only
# their own named inputs); the previous 12d finding set is superseded and out of
# scope for this pass.

Scope: 12 peer transcripts (CAPLIPOINT x4, SENORES x4, INNOVACAP x4) + B06-peers.md
+ B06-peers.yaml + B05-concall.yaml peer_questions.

## PART 1: COVERAGE AUDIT PER PEER (SUBSTANTIVE citations spot-checked against source)

All 12 transcript-quarters are marked SUBSTANTIVE in B06's Part 3 coverage map (this
round's rework corrected the prior CITED-ONLY tag on SENORES Jan-2026 to
SUBSTANTIVE). Per rule 2, I located and confirmed the actual citation for the
load-bearing quotes behind every one of the six Part 1 claim verdicts, plus several
Part 2/Part 3 coverage-map contribution quotes:

| # | Peer / quarter | Cited anchor in B06 | Content found at cited anchor | Verdict |
|---|---|---|---|---|
| 1 | CAPLIPOINT Nov-2025 | line 469, "117 days...118 days" | Confirmed verbatim | MATCH |
| 2 | CAPLIPOINT Feb-2026 | line 466, "121 days...118 days" | Confirmed verbatim | MATCH |
| 3 | CAPLIPOINT May-2026 | lines 617-633, 125-day FX add-back + Salvador tender | Confirmed (lines 623, 627, 636, 651) | MATCH |
| 4 | CAPLIPOINT Aug-2026 | lines 262-264, government-supplies receivables rise, Q3 FY27 collection | Confirmed verbatim | MATCH |
| 5 | CAPLIPOINT Aug-2026 | lines 534-536, "close to 30 lines" competitor | Confirmed at line 535 | MATCH |
| 6 | SENORES Jan-2026 | lines 1310-1315, "90 days, 94 days" (Deval Shah) | Confirmed at line 1315 | MATCH |
| 7 | INNOVACAP Nov-2025 | lines 710-716, 65-70% utilisation / 4-5 years | Confirmed at lines 712-714 | MATCH |
| 8 | INNOVACAP Aug-2026 | lines 992-1003, margin converges post-breakeven / "positive in this quarter" | Confirmed at lines 992, 1003 | MATCH |
| 9 | INNOVACAP Aug-2026 | lines 416-420, seasonal Q1 impact | Confirmed at line 416 | MATCH |
| 10 | SENORES Nov-2025 | lines 1009-1013, receivables INR25 Cr to INR45 Cr, "well under control" | Confirmed at lines 1006, 1011 | MATCH |
| 11 | SENORES Nov-2025 | lines 609-615/928, "25%-30%" CAGR target | Confirmed ("at least 30% CAGR", line 613; "25%-30%", line 611) | MATCH |
| 12 | SENORES Aug-2026 | lines 755-781, sterile-injectable de-scoping | Confirmed at lines 757, 779 | MATCH |
| 13 | SENORES Aug-2026 | lines 1242-1246, 942 products backlog | Confirmed at line 1242 | MATCH |
| 14 | SENORES Aug-2026 | "6 products, 30 million units" Apnar detail | Confirmed at line 814 | MATCH |
| 15 | SENORES May-2026 | "104 days" ex-Apnar working-capital cycle | Confirmed at line 532 | MATCH |
| 16 | INNOVACAP Nov-2025 | lines 470-472, "20% plus growth... INR1,000 crores plus" | Confirmed at lines 433, 472 | MATCH |
| 17 | INNOVACAP Aug-2026 | line 754, "this 20% plus CAGR" | Confirmed at line 754 | MATCH |
| 18 | CAPLIPOINT Nov-2025 | line 1102, "500 to 600 products" | Confirmed at line 1102 | MATCH |
| 19 | CAPLIPOINT May-2026 | lines 117/231, "17 injectable lines", "two-to-three years" | Confirmed at lines 117, 231 | MATCH |
| 20 | CAPLIPOINT Aug-2026 | line 462, "first phase... took 10-12 years" | Confirmed at line 462 | MATCH |
| 21 | INNOVACAP Nov-2025 | lines 590-597/607/623-627, "material margin is like 30% to 33%"; "volume growth is around 6% to 10%"; "losing on the price front" (Q3 evidence) | Lines 590-627 of the Nov-2025 file discuss regulatory-compliance timelines, unrelated content | **MISMATCH — see Finding 1** |
| 22 | CAPLIPOINT May-2026 | line 338, "Mexico. We have already filed 35+ products. We have 20 approvals along with our partners" | Line 338 of the May-2026 file discusses an 8-product Mexico tender, unrelated figure | **MISMATCH — see Finding 2** |

**Finding 1 (MAJOR).** B06's Q3 (loan-licence-to-owned-plant margin uplift) verdict
quotes INNOVACAP's CFO: *"on a [material] basis, material margin is like 30% to
33%.... Because like electricity or workman cost, all are the constant... Better
price realization is the second one,"* and *"our volume growth is around 6% to 10%.
Rest is all change in product/sales mix,"* and *"we are even losing on the price
front,"* all cited to **INNOVACAP-Concall_Nov_2025_Transcript.txt, lines 590-597,
607, 623-627** (B06-peers.md Q3 row). Lines 590-627 of the Nov-2025 transcript
contain unrelated content (a regulatory-compliance-timeline discussion; verified
directly). The exact quoted text is verbatim present, but in
**INNOVACAP-Concall_Feb_2026_Transcript.txt, lines 589-627** instead — same line
numbers, wrong file. This is the single load-bearing evidence block for the Q3
PARTIALLY VERIFIED verdict (TLL's central margin-uplift thesis), a claim of real
weight, cited to the wrong call. Content is genuine and correctly transcribed;
only the call/quarter attribution is wrong. This is the same defect class this
report's own Rework Resolution item (c) already found and fixed once in this
same peer's data (a different quote pair, Nov-2025 vs Aug-2026 mislabelling); a
second, distinct instance of the identical error type (this time Nov-2025 vs
Feb-2026) survived that round's fix.

**Finding 2 (MAJOR).** B06's Q4 (registrations) claim evidence quotes CAPLIPOINT:
*"Mexico. We have already filed 35+ products. We have 20 approvals along with our
partners,"* cited to **CAPLIPOINT-Concall_May_2026_Transcript.txt, line 338**
(B06-peers.md Q4 row). Line 338 of the May-2026 transcript instead discusses a
Mexico tender for eight products (unrelated content; no 35+/20-approvals figure
anywhere in that transcript, confirmed by direct search). The exact quoted text is
verbatim present in **CAPLIPOINT-Concall_Nov_2025_Transcript.txt, line 316**. Same
defect class as Finding 1. This does not flip the Q4 verdict (already
UNVERIFIABLE either way, since neither reading gives an annual flow rate or
conversion percentage), but it misstates which call carries the registration-stock
detail and is a second occurrence of the exact citation-anchor error type this
run's rework round set out to eliminate.

**Finding 3 (MINOR).** B06-peers.yaml `peer_coverage_map` (row for SENORES Q2 FY26
Nov-2025) states contribution "working-capital-cycle target 80-90 days." At the
source (SENORES-Concall_Nov_2025_Transcript.txt, lines 1129-1136), the 80-90-day
figure is the analyst's characterisation of the first-half actual ("this 80- to
90-day working capital cycle"), and CFO Deval Shah's answer is that it will NOT
hold at that level — it will move to "around 90 days to 100 days." Describing this
as an SENORES-stated "target" of 80-90 days inverts the direction of the CFO's
answer. This does not affect any Part 1 claim verdict — the Q1 debtor-days verdict
correctly relies on the separate, distinct Jan-2026 90-94-day quote (confirmed
accurate, item 6 above) — it is a coverage-map contribution-description
inaccuracy only.

## PART 2: UNUSED-BUT-RELEVANT CHECK (rule 3)

B06 marks 12 of 12 transcripts SUBSTANTIVE and 0 UNUSED / CITED-ONLY, so rule 3's
UNUSED-peer check has no rows to audit this round (the prior round's single
CITED-ONLY row, SENORES Jan-2026, was reclassified SUBSTANTIVE in this round's
rework and independently confirmed correct in item 6 above). A targeted spot-read
of each transcript for material the pipeline should have used but did not
surfaced nothing beyond what B06 already captured; no additional "unused but
relevant" item is added.

## PART 3: VERDICT-DISCIPLINE AUDIT (rule 4)

B06-peers.yaml `verified: []` — zero claims carry a VERIFIED verdict, so the
"VERIFIED resting on one peer is MAJOR" check has no rows to test (correctly; B06's
own Part 4 states no claim clears the two-peer VERIFIED bar). No verdict is upgraded
from silence: all three `unverifiable` claims (Q4, Q5, Q6) are left UNVERIFIABLE,
checked directly against B06's own Part 4 triangulation summary and found
consistent. No verdict-discipline failure found.

The two CONTRADICTED verdicts (Q1, Q2) each rest on independent evidence from 2+
peers (Q1: CAPLIPOINT + SENORES, now correctly two-anchored after this round's
rework; Q2: INNOVACAP primary, SENORES corroborating) — correctly exceeds the
single-peer threshold that would require downgrade to PARTIALLY VERIFIED. Q3
(single-peer, INNOVACAP) is correctly capped at PARTIALLY VERIFIED rather than
pushed to VERIFIED.

## PART 4: CLAIM COVERAGE (rule 5)

All six B05 `peer_questions` entries (Q1-Q6) receive a stated verdict in B06 Part 1
(CONTRADICTED x2, PARTIALLY VERIFIED x1, UNVERIFIABLE x3). No claim in the injected
peer_questions list is skipped. `claims_all_addressed: true` confirmed.

## SUMMARY

Peer selection and the six claim verdicts are sound and internally consistent with
the transcripts. This round's rework correctly resolved the prior round's three
named defects (SENORES Jan-2026 reclassification, coverage-count arithmetic, the
INNOVACAP 65-70%-quote call-attribution ambiguity). This audit finds two further
instances of the same citation-anchor defect class the rework targeted, both
undetected by that round: the Q3 margin-uplift evidence block (INNOVACAP,
Nov-2025-vs-Feb-2026) and the Q4 registrations evidence (CAPLIPOINT,
May-2026-vs-Nov-2025). In both cases the quoted text is genuine and verbatim
somewhere in the 12-transcript peer set, so nothing is fabricated, but the cited
call/quarter is wrong in both. Neither MAJOR finding flips a Part 1 verdict (Q3
stays PARTIALLY VERIFIED on correct, if misattributed, evidence; Q4 stays
UNVERIFIABLE either way), so this is not a CRITICAL, decision-changing defect, but
it is a real, repeat-pattern source-fidelity gap that argues for a targeted
anchor re-check across the remaining B06 citations before this report is treated
as fully clean, rather than a full REWORK.

```yaml
stage: B12d
company: "TLL"
run_date: "2026-09-26"
model: claude-sonnet-5
status: complete
peers_audited: 12
substantive_confirmed: 20
substantive_unsupported:
  - "INNOVACAP Nov-2025 (Q3 margin-uplift quote block, lines 590-597/607/623-627: quote verbatim exists but in INNOVACAP Feb-2026, not Nov-2025 as cited)"
  - "CAPLIPOINT May-2026 (Q4 '35+ products/20 approvals' Mexico quote, line 338: quote verbatim exists but in CAPLIPOINT Nov-2025 line 316, not May-2026 as cited)"
unused_but_relevant: []
claims_all_addressed: true
verdict_discipline_fails: []
findings:
  - {severity: "MAJOR", location: "B06-peers.md Q3 row", claimed: "quote cited to INNOVACAP-Concall_Nov_2025_Transcript.txt lines 590-597,607,623-627", source_truth: "identical quote found verbatim in INNOVACAP-Concall_Feb_2026_Transcript.txt lines 589-627; Nov-2025 lines 590-627 contain unrelated regulatory-compliance content", note: "load-bearing evidence for Q3 PARTIALLY VERIFIED verdict, wrong call attributed; same defect class as this report's own Rework Resolution item (c), a second undetected instance"}
  - {severity: "MAJOR", location: "B06-peers.md Q4 row", claimed: "quote cited to CAPLIPOINT-Concall_May_2026_Transcript.txt line 338", source_truth: "identical quote found verbatim in CAPLIPOINT-Concall_Nov_2025_Transcript.txt line 316; May-2026 line 338 discusses an unrelated Mexico tender", note: "does not flip the UNVERIFIABLE verdict but misattributes the source call"}
  - {severity: "MINOR", location: "B06-peers.yaml peer_coverage_map, SENORES Q2 FY26 Nov-2025 row", claimed: "working-capital-cycle target 80-90 days (framed as SENORES target)", source_truth: "80-90 days is the analyst's framing of the actual H1 level (line 1131); CFO Deval Shah answers it will move to 90-100 days, not hold at 80-90 (line 1136)", note: "contribution description inverts direction of the CFO's answer; does not affect any Part 1 verdict"}
critical_count: 0
major_count: 2
minor_count: 1
acceptance_rate: 90
coverage_basis: "20 of 20 spot-checked citations locate a verbatim, correctly-transcribed quote somewhere in the 12-transcript peer set; 18 of 20 at the exact cited call/quarter, 2 of 20 at a different call/quarter than cited (both MAJOR); 1 additional MINOR on a contribution-description direction error. acceptance_rate = 18 correctly-anchored / 20 checked, %."
```
