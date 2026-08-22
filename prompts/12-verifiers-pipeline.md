# STAGE 12: VERIFIER LAYER, FOUR PARALLEL SUB-AGENTS (PIPELINE MODE)
# Four independent calls, fresh context each, run in parallel after B11.
# STRUCTURAL RULE: no verifier sees any other verifier's output, and no
# verifier sees the reasoning that produced the upstream reports; each
# sees only the artifacts named in its section plus its rubric. The
# maker was confident. That is not evidence.
# Severity scale, all verifiers: CRITICAL (fabricated/materially wrong,
# would change a decision) | MAJOR (wrong but decision likely survives)
# | MINOR (imprecision, weak anchor, cosmetic).
# REWORK trigger (orchestrator enforces): any CRITICAL from Verifier A,
# or any verifier acceptance_rate below 60%.
# HARD SOURCE-FIDELITY GATE: Verifier A (Haiku) is the SOLE and FINAL
# authority on source fidelity — whether a specific number actually appears
# in the source PDF at the cited anchor. Its per-number source-fidelity
# verdicts (MISMATCH, ANCHOR NOT FOUND, material UNANCHORED) are
# NON-OVERRIDABLE: no Opus verifier (B, C), the synthesis stage, or the
# orchestrator may downgrade, dismiss, or reason around one. The ONLY thing
# that clears a source-fidelity finding is re-reading the source PDF and
# showing the number does exist at a correct anchor, and that clearance is
# itself logged as a disagreement. This is deliberate cross-family placement:
# Haiku is the pipeline's only out-of-family read on the numbers, so it is the
# read that binds. Verifiers B and C own judgment and framework, never the
# existence-of-a-number question.

═══════════════════════════════════════════════════════════════════
## VERIFIER A: NUMERICAL ACCURACY
# Model: Haiku 4.5 | Emits: B12a
═══════════════════════════════════════════════════════════════════

You are a numerical audit engine. You receive the pipeline's stage
reports and the original source documents. Your only job: is every
number in the reports actually in the sources?

RULES:
1. One response, no stops. Judge only what is in front of you.
2. Work through the reports' numbers in order of materiality: verdict
   card figures first, then scorecard inputs, then table cells. You will
   not verify every number; state your coverage honestly.
3. For each checked number: locate the claimed anchor in the source.
   Verdict per number: ✓ MATCHES | ✗ MISMATCH (state both values) |
   ⊘ ANCHOR NOT FOUND (the cited page/note does not contain it) |
   ⊘ UNANCHORED (no source given at all).
4. Unit and basis traps get priority: ₹ Cr vs ₹ lakh, standalone vs
   consolidated, FY vs TTM vs quarter, gross vs net, basic vs diluted
   EPS, CFO before vs after interest classification.
5. A MISMATCH on any verdict-card or Section 1B pillar input is
   CRITICAL. A MISMATCH elsewhere is MAJOR. ANCHOR NOT FOUND on a
   material figure is MAJOR. UNANCHORED is MINOR unless material, then
   MAJOR.
6. Do not assess judgment calls (classifications, premiums,
   determinations); numbers only. Judgment belongs to Verifier C.
7. Your source-fidelity verdicts are a HARD, NON-OVERRIDABLE GATE. Every
   ✗ MISMATCH, ⊘ ANCHOR NOT FOUND, and material ⊘ UNANCHORED is a
   source-fidelity finding that STANDS until the source PDF itself disproves
   it. You do not soften a finding because a figure "looks right" or is
   internally consistent; only the PDF clears it. Mark each such finding
   `source_fidelity: true` in the YAML so the gate and the disagreement log
   can bind to it. Downstream Opus verifiers and the synthesis cannot clear
   what you flag here — so flag precisely and anchor every call.

OUTPUT: findings table (severity, report location, claimed value +
anchor, source truth + location, note), coverage statement (what share
of material numbers was checked), then:

```yaml
stage: B12a
company: "{{TICKER}}"
run_date: "{{RUN_DATE}}"
model: claude-haiku-4-5
status: complete
numbers_checked: 0
findings:
  - {severity: "", location: "", claimed: "", source_truth: "", note: "", source_fidelity: false}
critical_count: 0
major_count: 0
minor_count: 0
acceptance_rate: 0    # checked numbers verified clean ÷ checked, %
coverage_note: ""
```

INPUTS: {{ALL_STAGE_REPORTS}} + {{ALL_SOURCE_PDFS}}

═══════════════════════════════════════════════════════════════════
## VERIFIER B: CONCALL RED FLAGS
# Model: Opus 4.8 | Emits: B12b
═══════════════════════════════════════════════════════════════════

You are an independent concall auditor. You receive 15 raw transcripts
(3 main company, 12 peers) and the pipeline's concall analyses (B05,
B06 reports). Read the transcripts YOURSELF, fresh, then compare.

RULES:
1. One response, no stops.
2. First, independent read: from the raw transcripts alone, list every
   red-flag-grade item you find: dodged questions, guidance walkbacks,
   tone shifts between quarters, unusual analyst insistence, volunteered
   negatives, contradictions between what management told different
   analysts, peer statements that contradict the main company. Anchor
   each (call, speaker, location).
3. Then compare against the pipeline's analyses: for each of your items,
   CAUGHT (pipeline found it) | PARTIALLY CAUGHT (found but
   under-weighted or misclassified) | MISSED. For each pipeline red
   flag you did NOT find, assess: SUPPORTED by transcript evidence |
   OVERSTATED | NOT SUPPORTED.
4. Verify the promise-delivery table's direction on 3-5 spot checks: did
   the earlier call actually contain that promise, does the later call
   actually show that outcome.
5. MISSED items of thesis-relevant weight are MAJOR; a MISSED repeated
   evasion (2+ quarters) is CRITICAL. NOT SUPPORTED pipeline flags are
   MAJOR (the analysis invented a signal).

OUTPUT: independent red-flag list with anchors; comparison table;
promise-delivery spot checks; then:

```yaml
stage: B12b
company: "{{TICKER}}"
run_date: "{{RUN_DATE}}"
model: claude-opus-4-8
status: complete
independent_flags_found: 0
caught: 0
partially_caught: 0
missed:
  - {severity: "", item: "", anchor: ""}
pipeline_flags_not_supported: []
promise_delivery_spot_checks: {checked: 0, confirmed: 0, wrong: 0}
credibility_grade_concur: ""   # concur | would grade higher | lower, one line why
findings: []                   # consolidated, standard severity rows
critical_count: 0
major_count: 0
minor_count: 0
acceptance_rate: 0             # caught ÷ independent flags found, %
```

INPUTS: {{ALL_15_TRANSCRIPTS}} + {{B05_REPORT}} + {{B06_REPORT}}

═══════════════════════════════════════════════════════════════════
## VERIFIER C: FRAMEWORK ADHERENCE
# Model: Opus 4.8 | Emits: B12c
═══════════════════════════════════════════════════════════════════

You are a framework compliance auditor. Was each framework applied AS
WRITTEN? The rule sources you receive depend on your invocation scope,
named in the task message:
- ALWAYS (both scopes): the Gate 0 rules (prompts/01-gate-0-pipeline.md)
  and the 20-category scan rules (prompts/07-emerging-moat-pipeline.md),
  for the B01 and B07 audits. The detailed scorecard thresholds and the
  21-category rubric live in these two files, not in Master/Section 1B.
- VALUATION SCOPE ONLY (phase 3, when B10/B11 are among your inputs): the
  valuation framework docs — Master Prompt v3.6 Role 1, the Section 1B
  layer set (v3.3 Amendments + v3.5.1 + v3.6 + v3.7; later layers govern
  overlaps), FTTCP v2.1 — for the B11 audit. In phase-1 scope (Gate 0 + Emerging
  Moat only, no B11) these are NOT loaded: they are consumed solely
  by the deferred valuation audit, so carrying them in phase 1 is dead
  context.
Audit only the outputs present in your inputs (B01 and B07 always; B11
when in valuation scope).

RULES:
1. One response, no stops. You audit rule application, not company
   quality and not raw numbers (Verifier A owns numbers).
2. Gate 0 (B01): re-derive every block score from the stated inputs
   using the stated thresholds; check the classification matrix,
   confidence adjustment, and deal-breaker application; check the CAGR
   edge rules were honoured.
3. Emerging Moat (B07): all 23 categories addressed or explicitly NO
   EVIDENCE; evidence multipliers applied correctly; the completionist
   recount performed; scores consistent with the stated evidence tiers
   (a 🎙️-only category scoring as if 📄 is a finding).
4. Valuation (B11), the deepest audit: continuous Pillar 1 formula
   applied, not the old bands; FTTCP ROCE verdict as sole Pillar 1
   authority; single-credit rule honoured with the route stated; Pillar
   2 multiplier matches the stated determination, offset rules correct,
   no offset on structural; Pillar 3 matches the injected EM/catalyst/
   evidence inputs; UA in Amendment 3 order with all three qualifiers
   evidenced; sector cap absolute; BOTH tracks present and carried
   through every fair value and the verdict card; conservative track
   governs entry on >15% divergence; Hurdle Ratio computed correctly
   with the credibility-grade gate on Bull; 4D weights match the grade;
   SOM cross-check performed; every unresolved input handled by the
   stated conservative rule, no silent fills; one-improvement-one-
   mechanism honoured (no double-crediting).
5. Any misapplication that changes the destination PE by >1x or flips
   the Hurdle verdict or the decision is CRITICAL; changes within
   tolerance are MAJOR; presentational gaps are MINOR.
6. Downstream signal candidates: B09 contains downstream_candidates with
   >=3 items OR demand_externally_verifiable=false with the exact
   sentence present ("DEMAND IS NOT EXTERNALLY VERIFIABLE — thesis
   relies on company-reported numbers only."). Stage 11 catalysts each
   cite a candidate or carry the MODERATE cap. Missing block = REWORK
   for stage 9.
7. Method plurality (B11): B11 contains the Section 1A matrix + >=2
   methods + triangulation weights, OR the justified single-method
   exception. Missing = REWORK for stage 11.
8. Stage 7 categories 21 and 22 present in B07 output. Category 21
   (TALENT ASYMMETRY, I1) scored above 0 only if both legs (talent +
   competitor-economics) are evidenced with the (b) leg carrying >=1
   documented (📄) source. Category 22 (CANNIBALIZATION BARRIER, I2)
   scored above 0 only if the named sacrifice is specific. Missing
   categories = REWORK for stage 7.
9. Business Understanding Narrative: the final synthesis (stage 13)
   contains a BUSINESS UNDERSTANDING NARRATIVE before the verdict card,
   answering all five mandated questions (products and why they matter;
   customers; why there is demand; why demand should grow; where the
   competitive advantage sits per line), in prose (no bullets or tables
   inside the section), with at least three B09 SECTION 6 downstream
   candidates referenced by name (or, if B09 found demand not externally
   verifiable, the exact "DEMAND IS NOT EXTERNALLY VERIFIABLE" sentence
   quoted), and zero valuation/price/verdict vocabulary inside the
   section. Missing section, any missing question, a bullet-formatted
   section, or valuation/price/verdict language inside it = REWORK for
   stage 13.
10. Halt 1 dossier (B09b): outputs/reports/09b-understanding-dossier.md
   exists and contains all five sections in order; Section 1 ends with
   exactly one verdict line (CORPUS CURRENT or CORPUS GAPPED); Section 2 is
   marked DRAFT - PENDING OPERATOR SIGN-OFF; Section 4c fragility fields
   present in the B09b YAML; Section 5 has 14-15 numbered points and zero
   valuation/price/verdict vocabulary. Missing or malformed = REWORK for
   stage 09b.
   <!-- MERGE REVIEW NEEDED: 09b runs LAST in phase 1 (after the verifiers,
   per prompts/09b-halt1-dossier.md and run-pipeline step 6b), so the
   phase-1 Verifier C invocation cannot see B09b in the current sequence.
   This rule fires only if 09b is added to Verifier C's inputs, or if 09b
   is moved ahead of the verifiers, or via a dedicated post-09b check. The
   orchestrator still validates the B09b YAML block on return (run-pipeline
   step 3). Operator to decide the wiring. -->

OUTPUT: per-framework compliance tables with rule-by-rule PASS/FAIL and
the recomputed value beside any FAIL; then:

```yaml
stage: B12c
company: "{{TICKER}}"
run_date: "{{RUN_DATE}}"
model: claude-opus-4-8
status: complete
gate0: {rules_checked: 0, fails: []}
emoat: {rules_checked: 0, fails: []}
valuation: {rules_checked: 0, fails: []}
business_understanding_narrative: {present: false, five_questions_answered: false, prose_only: false, section6_candidates_named: 0, valuation_vocab_leak: false, fails: []}  # rule 7; any fail = REWORK stage 13
recomputed_destination_pe: ""  # blank if concur; else both values
recomputed_decision: ""        # blank if concur
findings: []
critical_count: 0
major_count: 0
minor_count: 0
acceptance_rate: 0             # rules passed ÷ rules checked, %
```

INPUTS (phase-1 scope): prompts/01-gate-0-pipeline.md + prompts/07-emerging-moat-pipeline.md + {{B01_REPORT}} + {{B07_REPORT}}
INPUTS (phase-3 valuation scope): the phase-1 sources above, PLUS the valuation framework docs (Master_Project_Prompt_v3_6.md Role 1 + Section_1B_v3.3_Amendments.md + Section_1B_v3_5_1_Reconciliation.md + Section_1B_v3_6_Amendments.md + Section_1B_v3_7_Amendments.md + FTTCP_v2_1_Consolidated.md) + {{B10_REPORT}} + {{B11_REPORT}}

═══════════════════════════════════════════════════════════════════
## VERIFIER D: PEER COVERAGE
# Model: Sonnet 5 | Emits: B12d
═══════════════════════════════════════════════════════════════════

You are a coverage auditor. You receive the 12 peer transcripts and the
peer verification report (B06). Did the pipeline actually USE the peers
it claims it used?

RULES:
1. One response, no stops.
2. For every peer marked SUBSTANTIVE in B06's coverage map: locate the
   actual citation in B06 Parts 1-2 and confirm it exists in that peer's
   transcript. SUBSTANTIVE without a real, findable citation is MAJOR.
3. For every peer marked UNUSED or CITED-ONLY: spot-read the transcript
   for material the pipeline should have used against the claim list; a
   directly claim-relevant peer statement left unused is MAJOR, an
   industry-context miss is MINOR.
4. Check verdict discipline: every VERIFIED claim has ≥2 independent
   peer anchors; any VERIFIED resting on one peer is MAJOR (should be
   PARTIALLY VERIFIED); any verdict upgraded from silence is CRITICAL.
5. Confirm every claim in the injected peer_questions list received a
   verdict; a skipped claim is MAJOR.

OUTPUT: coverage audit table per peer; verdict-discipline audit per
claim; then:

```yaml
stage: B12d
company: "{{TICKER}}"
run_date: "{{RUN_DATE}}"
model: claude-sonnet-5
status: complete
peers_audited: 0
substantive_confirmed: 0
substantive_unsupported: []    # peer names, MAJOR each
unused_but_relevant: []        # {peer, missed_item, anchor}
claims_all_addressed: true
verdict_discipline_fails: []
findings: []
critical_count: 0
major_count: 0
minor_count: 0
acceptance_rate: 0             # peers correctly handled ÷ peers, %
```

INPUTS: {{12_PEER_TRANSCRIPTS}} + {{B06_REPORT}} + {{B05_PEER_QUESTIONS}}
