# VERIFIER D: PEER COVERAGE — eMudhra Ltd (EMUDHRA), run 2026-09-19

Model: Sonnet 5. Inputs: 12 raw peer transcripts (NEWGEN x4, PROTEAN x4, QUICKHEAL
x4), outputs/reports/06-peers.md + outputs/blocks/B06-peers.yaml, and the
peer_questions list from outputs/blocks/B05-concall.yaml (9 questions).

Method: every peer transcript was read in full, independently, against the .txt
page markers embedded beside each PDF (`[page N]`). Every SUBSTANTIVE citation in
B06 Parts 1-2 that carries a quoted phrase and a call+page anchor was located by
searching the transcript text and cross-checking the page marker the quote falls
under, not merely trusting the surrounding prose.

## COVERAGE AUDIT TABLE — PER PEER (12 peer-quarter transcripts)

| Peer | Quarter | B06 usage | Verdict on citation fidelity |
|---|---|---|---|
| NEWGEN | Q2FY26 (Nov-2025) | SUBSTANTIVE | Confirmed. Growth figures (11% Y-o-Y, EMEA 3%, India 7%) and deal-size disclosures locate correctly. |
| NEWGEN | Q3FY26 (Jan-2026) | SUBSTANTIVE | Confirmed for the cited "AI-led uncertainty" quote (p.11, verified — content between file's [page 11] and [page 12] markers). **Not flagged in B06's coverage-map contribution line: this transcript also contains the H-1B quote B06 attributes to the May-2026 call (see finding #1 below).** |
| NEWGEN | Q4FY26 (May-2026) | SUBSTANTIVE | **Anchor mismatch.** B06 cites this call, p.10, for the H-1B quote ("We don't do any H-1Bs anyway..."). That quote does not exist anywhere in this transcript. The FY26 6% growth benchmark and Middle East "serious impact last quarter" quote (p.8) are correctly anchored here. |
| NEWGEN | Q1FY27 (Jul-2026) | SUBSTANTIVE | Confirmed. Q1FY27 growth 11%/EMEA 10%, CEO transition (Tarun Nandwani effective 1-Aug-2026), deal-size disclosures, DSO/EMEA delay language all verified at stated locations. |
| PROTEAN | Dec-2025 (NSDL stake business-update call) | CITED-ONLY | Confirmed correct classification: transcript header confirms "Business Update Conference Call," not an earnings call. No claim-relevant content missed. |
| PROTEAN | Q3FY26 (Feb-2026) | SUBSTANTIVE | Confirmed. CRA/pension AUM-linked repricing discussion, Suresh Sethi departure context, Aadhaar Seva Kendra (34 centres) all verified. |
| PROTEAN | Q4FY26 (May-2026) | SUBSTANTIVE | **Anchor mismatch.** This call, p.13, actually contains the "decision-making in some of these countries is slow because of the war and supply chain situation going on" quote (Sandeep Mantri, in response to Sham Chandani). B06 credits this quote to the Aug-2026 (Q1FY27) call instead. The "remain cautious with the ongoing war situation" quote B06 correctly cites to this call (p.7 per markers) is fine. |
| PROTEAN | Q1FY27 (Aug-2026) | SUBSTANTIVE | **Anchor mismatch (two issues).** (a) The "decision-making...war and supply chain" quote cited here at p.11 does not appear in this transcript at all (it is the May-2026 call's quote — see above). (b) The EBITDA-margin-crater comparison "18.7% -> 10%" is cited at p.4; the 10% figure alone appears on p.4 (Ajay Rajan's opening remarks), but the 18.7% prior-year comparator that makes this a "crater" claim appears only in Sandeep Mantri's CFO detail on p.11. The procurement-cost-inflation quote (p.4-5) and the "EBITDA margin profile used to be at 23%...deteriorated to about 11%" investor quote (p.13) are both correctly anchored. |
| QUICKHEAL | Q3FY25 (Feb-2025) | SUBSTANTIVE | Confirmed. "Government orders are pushed forward in timelines" (p.3) and DPDP deal-size range 75L-3cr (p.12) both verified. |
| QUICKHEAL | Q1FY26 (Aug-2025) | SUBSTANTIVE | Confirmed. CEO search context (succession planning underway) verified. |
| QUICKHEAL | Q2FY26 (Oct-2025) | SUBSTANTIVE | Confirmed. "This quarter, we have seen an uptick in revenue in our Government business especially" verified at p.5. |
| QUICKHEAL | Q4FY26 (May-2026) | SUBSTANTIVE | Confirmed. Enterprise mix 20%->50%+ (p.2), IT hardware "up to 400%" inflation (p.4), Rs 64cr order and Operation Sindoor context (p.3-4) all verified. Negative EBITDA/PAT figures verified at p.5. |

11 of 12 transcripts are marked SUBSTANTIVE, 1 CITED-ONLY (correctly). Of the 11
SUBSTANTIVE entries, 9 have every checked citation locating cleanly; 2 (NEWGEN
Q4FY26/May-2026, PROTEAN Q1FY27/Aug-2026) each carry at least one load-bearing
quote whose stated call+page does not contain it — the quote is genuine and
accurately transcribed, but sits in a different peer-quarter transcript than
claimed. QUICKHEAL's full set of 4 transcripts checked out clean on every
sampled citation.

## FINDINGS

| # | Severity | Location in B06 | Claimed anchor | Actual location | Note |
|---|---|---|---|---|---|
| 1 | MAJOR | Q8 verdict table, Part 4 "single most consequential contradiction," YAML `contradicted.quote_anchor` | "NEWGEN Q4FY26 call (May-2026), p.10" | NEWGEN Q3FY26 call (Jan-2026), p.16 | The quote ("We don't do any H-1Bs anyway... we sell products and products don't need [people movement]") is genuine and accurately transcribed, but does not appear anywhere in the May-2026 transcript. It is spoken by Virender Jeet in the Jan-2026 call in response to Vinay Nadkarni. This is the report's single highest-stakes finding (Q8 CONTRADICTED, carried forward as the "priority item for synthesis"), so a wrong call+page anchor here is material: a reader following the citation to verify the CRITICAL-adjacent claim would not find it. |
| 2 | MAJOR | Q6 verdict, Part 2A cross-read | "PROTEAN Q1FY27 (Aug-2026 call)... p.11" for "decision-making in some of these countries is slow because of the war and supply chain situation going on" | PROTEAN Q4FY26 call (May-2026), p.13 | This quote (Sandeep Mantri) is genuine but sits in the May-2026 transcript, not Aug-2026. It directly feeds the report's self-described "strongest piece of independent triangulation in this stage" (Middle East war corroboration) — the same quarter-attribution error recurs in a second load-bearing citation. |
| 3 | MAJOR | Q5 verdict, "PROTEAN's Q1FY27 EBITDA margin cratered to 10% from 18.7% a year earlier... (PROTEAN Q1FY27, Aug-2026 call, p.4)" | p.4 | p.11 (within the same Aug-2026 transcript) for the 18.7%-vs-10% comparison; p.4 contains only the standalone "10%" figure in Ajay Rajan's opening remarks | Same-call, wrong-page. Lower stakes than #1/#2 since the call itself is correct and both figures are genuinely in this transcript, but the specific comparison as quoted is not on the cited page. |

No fabricated peer evidence was found anywhere in the report: every quote traced
back to a real, correctly-transcribed statement by the named peer. The defect in
all three findings is anchor precision (wrong quarter and/or wrong page), not
invented content.

## VERDICT-DISCIPLINE AUDIT PER CLAIM (rule 4)

B06 marks 0 of 9 claims VERIFIED (Part 4 states this explicitly and correctly —
the peer set is a partial-mapping comp group, so the ≥2-independent-peer bar for
VERIFIED was never claimed to be met). With no VERIFIED verdicts issued, the
"VERIFIED resting on one peer" failure mode does not apply. No verdict is
upgraded from silence — UNVERIFIABLE, PARTIALLY VERIFIED and CONTRADICTED are
each used in a way consistent with the underlying evidence described in Part 1.
**No verdict-discipline failures found.**

## CLAIM ADDRESS CHECK (rule 5)

All 9 items in B05's `peer_questions` list receive an explicit verdict in B06
Part 1 (Q1 through Q9, each with a Verdict field). No skipped claims.

## UNUSED-BUT-RELEVANT CHECK (rule 3)

The only CITED-ONLY transcript (PROTEAN Dec-2025) is a business-update call
about the NSDL Payments Bank stake with no content bearing on any of the 9
eMudhra claims; CITED-ONLY is the correct classification and nothing
claim-relevant was left on the table there.

Within the 11 SUBSTANTIVE transcripts, no directly claim-relevant peer statement
was found unused. Minor industry-context items exist that B06 did not pull in
(e.g., NEWGEN's RPO-disclosure discussion, Protean's DPI-in-a-box strategy
narrative) but none bears on eMudhra's 9 scoped claims or on a material
red-flag-grade item — these are MINOR at most and not written up as findings.

## SUMMARY

- Peers/quarters audited: 12 (11 SUBSTANTIVE + 1 CITED-ONLY, both counts correct
  as classified).
- Citation fidelity: 9 of 11 SUBSTANTIVE transcripts have every checked citation
  locating cleanly at the stated call+page. 2 transcripts (NEWGEN Q4FY26/May-2026,
  PROTEAN Q1FY27/Aug-2026) each anchor at least one load-bearing quote to the
  wrong call or page — in both cases the true source is a different quarter's
  transcript from the same peer.
- All three anchor defects affect genuine, correctly-transcribed peer statements;
  none is fabricated or reverses the meaning of what the peer actually said. The
  underlying analytical conclusions in B06 (Q8 contradiction stands on the real
  Jan-2026 NEWGEN quote; the Middle East corroboration stands on the real
  May-2026 PROTEAN quote) survive once the correct anchor is substituted — but as
  filed, a reader checking the citation against the named source would fail to
  find it, which is the exact failure mode this verifier is scoped to catch.
- No verdict-discipline failures, no skipped claims, no fabricated peer evidence,
  no unused-but-relevant peer material of note.

```yaml
stage: B12d
company: "EMUDHRA"
run_date: "2026-09-19"
model: claude-sonnet-5
status: complete
peers_audited: 12
substantive_confirmed: 9
substantive_unsupported:
  - "NEWGEN (Q4FY26/May-2026 entry — H-1B quote cited at p.10 does not exist in this transcript; true source is Q3FY26/Jan-2026, p.16)"
  - "PROTEAN (Q1FY27/Aug-2026 entry — 'decision-making...war and supply chain' quote cited at p.11 does not exist in this transcript; true source is Q4FY26/May-2026, p.13)"
unused_but_relevant: []
claims_all_addressed: true
verdict_discipline_fails: []
findings:
  - {severity: "MAJOR", location: "B06 Q8 verdict / Part 4 / YAML contradicted.quote_anchor", claimed_anchor: "NEWGEN Q4FY26 call (May-2026), p.10", actual_location: "NEWGEN Q3FY26 call (Jan-2026), p.16", note: "Quote genuine and accurately transcribed, wrong call and page cited; feeds the report's single highest-stakes finding"}
  - {severity: "MAJOR", location: "B06 Q6 verdict / Part 2A", claimed_anchor: "PROTEAN Q1FY27 (Aug-2026 call), p.11", actual_location: "PROTEAN Q4FY26 call (May-2026), p.13", note: "Quote genuine, wrong call and page; feeds the report's self-described strongest independent triangulation"}
  - {severity: "MAJOR", location: "B06 Q5 verdict", claimed_anchor: "PROTEAN Q1FY27, Aug-2026 call, p.4", actual_location: "PROTEAN Q1FY27, Aug-2026 call, p.11", note: "Same call, wrong page; the 18.7%-vs-10% comparison sits in the CFO's detailed remarks (p.11), not the opening remarks (p.4) where only the standalone 10% figure appears"}
critical_count: 0
major_count: 3
minor_count: 0
acceptance_rate: 83
```
