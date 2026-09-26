# VERIFIER D: PEER COVERAGE AUDIT — AVIENCE (2026-09-26)

Inputs: 6 peer transcripts (QLINE Jun-2026; MOLBIO Sep-2026; TARSONS Nov-2025,
Feb-2026, Jun-2026, Aug-2026), B06-peers.md/.yaml, B05-concall.yaml
`peer_questions`. Read the transcripts directly and cross-checked every
citation B06 gives against the actual `[page N]` PDF-page markers in the
source .txt files (these markers, not the printed "Page X of NN" footer, are
the anchor unit named in the task).

## PART 1: COVERAGE AUDIT PER PEER

All six transcripts are marked SUBSTANTIVE in B06's coverage map (Part 3);
none CITED-ONLY or UNUSED. For each, I located the material B06 actually
cites and confirmed it is real content in that transcript.

| Peer/call | B06 usage | Content verified in transcript? | Citation accuracy |
|---|---|---|---|
| QLINE H2/FY26 | SUBSTANTIVE | Yes — reagent margins, closed-loop mix, receivable days, related-party distributor, export figures, growth rate all present as quoted | Mostly accurate; one 1-page drift (see Part 2) |
| MOLBIO Q1 FY27 | SUBSTANTIVE | Yes — margin, receivable days, TAM, two-year contract, closed-system quote all present as quoted | Two citations drift 1 page; one drifts ~5 pages (see Part 2) |
| TARSONS Q2/H1 FY26 (Nov-2025) | SUBSTANTIVE | Yes — Rs550-650 Cr capex figure and 3-5yr/2-3yr ramp timelines both present verbatim | Both citations drift 1-2 pages (see Part 2) |
| TARSONS Q3/9M FY26 (Feb-2026) | SUBSTANTIVE | Yes — explicit "15%, 20%... 30%, 35%" ramp curve present verbatim; GeM/L1 government-procurement content ALSO appears in this call (not cited by B06, see Part 3) | Citation accurate (page 12, within cited p.11-12) |
| TARSONS Q4/FY26 (Jun-2026) | SUBSTANTIVE | Yes — "first half of the current financial year" commissioning slip present; -13.4% export decline present | Commissioning-slip citation accurate; export-decline citation drifts ~4 pages (see Part 2) |
| TARSONS Q1 FY27 (Aug-2026) | SUBSTANTIVE | Yes — second commissioning slip, GeM/L1 discussion, 20-25% FY28 standalone-revenue guidance, +29% export rebound, +21% Q1 growth all present | Slip and export-rebound citations exact; GeM citation exact; FY28 figure drifts 1 page |

No peer's SUBSTANTIVE claim is unsupported. Every quoted or paraphrased
figure B06 attributes to a peer transcript is genuinely present in that
transcript. The finding below is about anchor precision (page numbers), not
fabrication or invented content.

## PART 2: CITATION ANCHOR FINDINGS

Anchor unit = the `[page N]` marker embedded in each .txt file (per the run's
own convention, confirmed in B06's identity block). Severity: a drift of 3+
pages that could send a reader to unrelated content is MAJOR; a 1-2 page
drift onto an adjacent page of the same answer/exchange is MINOR.

| Severity | Peer/call | B06 location cited | Content found at | Note |
|---|---|---|---|---|
| MAJOR | MOLBIO Q1 FY27 | "transcript p.16-17" (Q3, closed-system quote: "our reagents, our consumables work only on our devices... no third-party kits can be used on the device") | Actual: p.12 | The blended-margin half of the same citation ("60% to 63% gross margin") IS correctly at p.17; the closed-system quote bundled into the same "p.16-17" tag is not — it sits 4-5 pages earlier, in the Q&A on device life-cycle, not the Q&A on margins. |
| MAJOR | TARSONS Q4/FY26 | "transcript p.2-3" (Q1, "-13.4% decline in export during the quarter") | Actual: p.6 | Cited anchor is on the presentation's opening pages; the actual quote is in the CFO's segment-performance remarks several pages later. |
| MINOR | MOLBIO Q1 FY27 | "transcript p.20" (two-year rate contract) | Actual: p.19 | Adjacent page, same closing Q&A exchange. |
| MINOR | MOLBIO Q1 FY27 | "transcript p.5" (17.9% CAGR TAM) | Actual: p.6 | Adjacent page. |
| MINOR | TARSONS Q2/H1 FY26 | "transcript p.11-12" (Rs550-650 Cr capex plan) | Actual: p.13 | Figure is 1-2 pages later than cited; still inside the same capex Q&A block. |
| MINOR | TARSONS Q2/H1 FY26 | "transcript p.11-12" (3-5yr new-product / 2-3yr capacity-expansion ramp timeline) | Actual: p.12-13 | 1-page overrun into p.13, minor. |
| MINOR | TARSONS Q1 FY27 | "transcript p.7-8, p.16" (20-25% of standalone revenue by FY28) | Actual: p.15 | 1-page drift from the p.16 tag. |
| MINOR | QLINE H2/FY26 | "transcript p.10" (India diagnostic market growing 8-9%) | Actual: p.11 | Adjacent page, same answer. |

Citations verified as EXACT (spot sample, no drift): QLINE Rs1.2 Cr export
base and 5x target (p.6, p.8-9); QLINE 60-65%/50%/15-20%/52-55% margin ladder
and 134-day receivables (p.12, within cited p.11-12); QLINE 75-80% closed
system (p.16); MOLBIO 87/86-day receivables and 75% test-kit revenue (p.9);
MOLBIO 60-63% margin figure itself (p.17); TARSONS Q4/FY26 "first half of
the current financial year" commissioning slip (p.5); TARSONS Q1 FY27 "second
half of FY'27" second slip (p.7); TARSONS Q1 FY27 +29% export rebound (p.4);
TARSONS Q1 FY27 GeM/L1 procurement passage (p.18, within cited p.17-18).

Net read: the pattern is a consistent 1-5 page anchor drift, not fabrication.
Every cited figure is real and correctly attributed to the right transcript
and the right speaker's answer; the page number is sometimes off by enough
to send a manual checker to the wrong passage. The two MAJOR items above are
flagged because the drift (4-5 pages) crosses into a different section of
the call, which would mislead a reader trying to locate the source quickly.
This is a source-fidelity precision issue Verifier A's hard gate does not
reach (Verifier A audits numbers against report claims; this is anchor
location within a transcript already confirmed to contain the number), so it
is reported here as a coverage-quality finding, not escalated as a
non-overridable Verifier A gate item.

## PART 3: UNUSED-BUT-RELEVANT CHECK

Spot-read all six transcripts beyond the quoted passages for claim-relevant
material B06 did not use.

- TARSONS Feb-2026 call ALSO contains the GeM/L1 government-procurement
  discussion (transcript p.12, "the government business has taken a big
  setback over the last 3 to 4 years since GeM... L1 process") — the same
  theme B06 sources only from the Aug-2026 call (p.17-18). This is not a
  miss (B06 used the theme, correctly and with a stronger, more detailed
  citation from the later call), but the earlier call's corroborating
  mention is a second independent occurrence of the same risk that could
  have strengthened the finding's evidentiary weight (two calls, ~6 months
  apart, both naming the same structural risk). MINOR — an industry-context
  reinforcement left unused, not a claim-relevant miss.
- No other directly claim-relevant material was found unused across the six
  transcripts on spot-read (TARSONS debt/capex/pricing detail in the
  Aug-2026 call, QLINE's CDMO/export detail, and MOLBIO's OptraScan/Prognosys
  subsidiary detail are all genuinely tangential to the five B05
  peer_questions and the Avience claim set).

## PART 4: VERDICT-DISCIPLINE AUDIT

- `verified: []` in B06 — zero claims upgraded to VERIFIED. Correct
  discipline: no claim in this run has 2+ independent peer anchors that
  actually match Avience's own figure (Q3 margin band and Q4 utilisation
  percentage each rest on real but partial/non-matching corroboration,
  correctly downgraded to PARTIALLY VERIFIED per rule 4).
- No claim is upgraded from silence to a positive verdict anywhere in B06.
- All 5 `peer_questions` from B05 received a verdict in B06 Part 1 (Q1
  export collapse: UNVERIFIABLE; Q2 payment terms: PARTIALLY VERIFIED; Q3
  margin/mix: PARTIALLY VERIFIED; Q4 YEIDA ramp: PARTIALLY VERIFIED; Q5
  growth/CDSCO: split verdict, PARTIALLY VERIFIED / UNVERIFIABLE). No skipped
  claim.
- No VERIFIED claim rests on a single peer (none are marked VERIFIED at
  all, so this check is vacuously satisfied).

## PART 5: OVERALL READ

B06 did not invent peer support. Every figure and quote traced back to a
real, correctly-attributed passage in the correct transcript. Verdict
discipline is conservative and correctly calibrated — no claim was
over-verified. The genuine defect is citation-anchor precision: two findings
(MOLBIO closed-system quote, TARSONS export-decline quote) drift far enough
(4-5 pages) that a reader following the citation would land on the wrong
passage, and six further citations drift a single adjacent page. None of
this changes the substance of B06's Part 4 Triangulation Summary or its
`net_narrative_effect: "complicates"` conclusion; the underlying evidence
for every finding is real. This does not clear the 60% acceptance-rate
REWORK bar (the denominator here is 6 peers, all correctly handled in
substance; see acceptance_rate below), and no CRITICAL finding exists.

```yaml
stage: B12d
company: "AVIENCE"
run_date: "2026-09-26"
model: claude-sonnet-5
status: complete
peers_audited: 6
substantive_confirmed: 6
substantive_unsupported: []
unused_but_relevant:
  - {peer: "TARSONS", missed_item: "Feb-2026 call (Q3/9M FY26) also names the GeM/L1 government-procurement setback, ~6 months before the Aug-2026 call B06 sources it from; a second independent occurrence of the same structural risk not credited", anchor: "TARSONS-Concall_Feb_2026_Transcript.txt [page 12]"}
claims_all_addressed: true
verdict_discipline_fails: []
findings:
  - {severity: "MAJOR", location: "B06 Q3 (margin/closed-loop), MOLBIO citation", claimed: "transcript p.16-17 for the closed-system quote (\"our reagents, our consumables work only on our devices... no third-party kits can be used on the device\")", source_truth: "quote is at [page 12]; only the paired 60-63% margin figure is genuinely at p.17", note: "Quote is real and correctly attributed to MOLBIO's Q1 FY27 call; page anchor for this half of the citation is off by 4-5 pages, landing in a different Q&A exchange (device life-cycle, not margins)."}
  - {severity: "MAJOR", location: "B06 Q1 (export collapse), TARSONS Q4/FY26 citation", claimed: "transcript p.2-3 for \"-13.4% decline in export during the quarter\"", source_truth: "quote is at [page 6]", note: "Quote is real and correctly attributed to the Q4/FY26 (25-May-2026) call's CFO remarks; page anchor points to the call's opening pages instead."}
  - {severity: "MINOR", location: "B06 Q1, MOLBIO citation", claimed: "transcript p.20 for the two-year rate contract", source_truth: "[page 19]", note: "adjacent-page drift, same closing exchange"}
  - {severity: "MINOR", location: "B06 Part 2A/5, MOLBIO citation", claimed: "transcript p.5 for 17.9% CAGR TAM", source_truth: "[page 6]", note: "adjacent-page drift"}
  - {severity: "MINOR", location: "B06 Q4, TARSONS Nov-2025 citation", claimed: "transcript p.11-12 for Rs550-650 Cr capex plan", source_truth: "[page 13]", note: "figure is 1-2 pages later than cited, same capex Q&A block"}
  - {severity: "MINOR", location: "B06 Q4, TARSONS Nov-2025 citation", claimed: "transcript p.11-12 for 3-5yr/2-3yr ramp timeline language", source_truth: "[page 12-13]", note: "1-page overrun"}
  - {severity: "MINOR", location: "B06 Q4/Part 3, TARSONS Aug-2026 citation", claimed: "transcript p.7-8, p.16 for 20-25% of standalone revenue by FY28", source_truth: "[page 15]", note: "1-page drift from the p.16 tag"}
  - {severity: "MINOR", location: "B06 Q5, QLINE citation", claimed: "transcript p.10 for India diagnostic market growing 8-9%", source_truth: "[page 11]", note: "adjacent-page drift"}
critical_count: 0
major_count: 2
minor_count: 6
acceptance_rate: 100
```
