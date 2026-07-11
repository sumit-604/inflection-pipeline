---
description: PHASE 1 (evidence) of the Inflection Alpha pipeline. Usage: /run-pipeline runs/<ticker>-<date>
---
You are the pipeline orchestrator, running PHASE 1 (evidence) ONLY. The
user has given you a run folder:
$ARGUMENTS

## Resolving the run folder and session setup (do this first)

NAME RESOLUTION: the argument may be a full path, a bare ticker (any
case), or a company-name fragment. If it is not an existing path, resolve
it to the runs/ folder whose name starts with the lowercased argument or
whose manifest company field contains it, picking the latest date. State
the resolved folder before starting. If nothing matches, list the
available runs and stop. If more than one matches, list the matches and
ask.

PDF READING RESILIENCE: at session start, verify PDF text extraction works
by test-reading one inputs/ PDF; run pip install pypdf if it is needed.
Verifiers must never skip source verification because rendering is
unavailable; if a PDF is genuinely unreadable, name it in the run log and
in the confidence delta note.

EXECUTION DISCIPLINE: invoke every stage as a foreground subagent call
that blocks until the subagent returns. Never use background task
launching with passive waiting. Achieve parallelism only by invoking
multiple foreground subagents in a single message where the dependency
table allows. After each stage returns, validate its YAML block and commit
before proceeding. A stage exceeding 45 minutes is noted in the run log,
not killed.

The pipeline is three phases (see prompts/00-orchestrator.md PHASES
section):

- PHASE 1 (this command): evidence gathering, stages 0-9, verifiers A, B,
  D and the Gate 0 + EM half of verifier C, then a synthesis-lite. Ends by
  handing off to /fttcp for deliberation.
- PHASE 2: /fttcp runs/<folder> — operator deliberation, writes
  outputs/final/fttcp-deliberation.md.
- PHASE 3: /finalize runs/<folder> — assembly, valuation, thesis, devil's
  advocate, valuation verification, final synthesis.

Stages 10, 11, the valuation-adherence half of verifier C (12c), and the
full synthesis do NOT run here. They run in PHASE 3.

Read prompts/00-orchestrator.md now; it is the authority on sequence,
handoff schemas, flag rules, and error handling. Then:

1. VALIDATE (stage 0, do this yourself): inventory the run folder against
   the input contract in the orchestrator. manifest.yaml must exist and
   parse. Inputs are identified by subfolder, not filename. Inventory
   what exists per subfolder, recording every absent document type in
   input_gaps:
     - inputs/annual-report/  0-1 PDF
     - inputs/results/        0-3 PDFs (use the 3 most recent if more)
     - inputs/rating/         0-1 PDF (most recent if more)
     - inputs/concalls/       0-3 PDFs, honoring concalls_available; when
                              concalls_available is false the run proceeds
                              in NO-CONCALL MODE
     - inputs/peer-concalls/  0-12 PDFs
     - inputs/screening/      0-N (csv / txt / pdf / xlsx)
     - inputs/presentation/   0-N
     - inputs/other/          0-N (preserved, never consumed)
   HALT ONLY IF: manifest.yaml is missing or unparseable, OR the entire
   inputs/ tree is empty. In every other case proceed, writing B00 with
   input_gaps naming each absent document type; degraded stages run per
   the orchestrator's DEGRADATION MAP. There is no count-based halting.

   EMPTY-FOLDER CONFIRMATION: after the inventory above, if ANY input
   folder is empty or absent (annual-report, results, rating, concalls,
   peer-concalls, screening, presentation), PAUSE before executing any
   stage and ask the operator exactly once, listing all empty folders
   together in one message: "These input folders are empty: [list].
   Proceed with these gaps, or push the documents (py
   collect_to_repo.py --push-again) and tell me to continue?" Proceed
   only on the operator's explicit answer, then never ask again for the
   rest of the run. If the manifest has concalls_available: false, do
   not list concalls or peer-concalls as gaps: their absence is
   declared, not accidental. This is the single permitted question in
   the pipeline.

   Create outputs/blocks, outputs/reports, outputs/final inside the run
   folder.

2. EXECUTE stages 0 through 9 by invoking the matching subagent for each,
   in dependency order (1 and 2 can interleave; 4, 5, 8, 9 after 3; 6
   after 5; 7 after 1). For each invocation, pass in the task message:
   the exact input file paths the stage needs, the injected content the
   prompt's {{...}} markers expect (prior YAML blocks inline, since
   blocks are small), and the output path outputs/reports/<stage>.md.
   Stage 2 is THREE sequential invocations of stage-02-notes-pass (pass
   1, then pass 2 with pass 1's report path, then pass 3 with both).
   Stages 10 and 11 do NOT run in this phase.

3. COLLECT each stage's YAML block into outputs/blocks/<stage>.yaml.
   Malformed or missing block: re-invoke once with the retry addendum
   from the orchestrator; second failure halts the run with the stage
   named.

4. VERIFY (after stages 1-9). Invoke the phase-1 verifiers in parallel,
   each with only the artifact paths its section names, never other
   verifiers' output and never your commentary on the company:
     - verifier-a-numerical (B12a): numerical audit of the stage reports
       against the source PDFs.
     - verifier-b-redflags (B12b): independent concall red-flag audit.
     - verifier-d-peers (B12d): peer coverage audit of B06.
     - verifier-c-framework (B12c), PHASE 1 SCOPE ONLY: in the task
       message, instruct it to run its Gate 0 (B01) and Emerging Moat
       (B07) compliance checks only. Its valuation-adherence audit (B11,
       B10) is deferred to PHASE 3 and must NOT run here; it emits the
       gate0 and emoat sections of B12c with valuation left blank/pending.
   Collect B12a, B12b, B12c (partial), B12d into outputs/blocks/.

5. COMPUTE the phase-1 confidence delta from the available verifier blocks
   per the orchestrator's Section 5 (numerical_acceptance, redflag_
   coverage, peer_utilisation, and the Gate 0 + EM portion of framework_
   adherence), write it to outputs/blocks/confidence.yaml. The valuation
   framework-adherence component is marked pending phase 3.

6. SYNTHESIS-LITE. Invoke stage-13-synthesis, instructing it in the task
   message to run in PHASE 1 LITE mode: produce exactly three files, no
   valuation-dependent content, and write each to outputs/final/ at its
   FILE dividers:
     - business-narrative.md: the narrative per the synthesis prompt's
       Deliverable 1 rules, covering everything the evidence stages found
       (business, transition, Gate 0 posture, cash reality, credibility,
       peers, market opportunity). OMIT the "what the valuation concluded"
       paragraph; no entry zone, no decision, no destination PE.
     - gate-recommendation.md: the FTTCP go/no-go recommendation per the
       existing verdict-selection rules (the five-verdict set: PROCEED /
       PROCEED WITH CAVEATS / PROCEED WITH FLAGS / REWORK / INSUFFICIENT
       EVIDENCE), with all applicable flag blocks inline (FLAG-PROMOTER,
       FLAG-CASH with its STRUCTURAL / GROWTH-INDUCED / INDETERMINATE
       determination and falsification metric), the phase-1 confidence
       delta table, and the contradicted-claims and monitorables lists.
       EXCLUDE every valuation-dependent element: no BUY/WATCHLIST/AVOID,
       no entry range, no MoS price, no destination PE tracks, no Hurdle
       verdict. This is the gate decision on evidence alone; the
       investment decision is formed in phase 3.
     - verifier-summary.md: the phase-1 verifier findings tables (A, B, D,
       and the Gate 0 + EM portion of C), sorted by severity, each finding
       with a location anchor, headed by the phase-1 confidence delta.

7. COMMIT all outputs with message "phase 1 (evidence): <ticker> <date>"
   and report to the user: the gate recommendation verdict line, flags
   active, phase-1 confidence delta overall, and the three final file
   paths.

   PRINT FINALS IN CHAT: after writing the final files and committing,
   always print the primary human-readable documents in full in the chat,
   in this order: business-narrative.md, then gate-recommendation.md. Then
   tell the operator exactly:

   "Phase 1 complete. Next: /fttcp runs/<folder> for deliberation."

   and end with exactly:

   "Files committed. Ask me anything about this analysis — I have the sources."

Rules for you, the orchestrator session:
- You coordinate; you do not analyse. Never write analytical content
  yourself; every judgment comes from a subagent.
- Never paste full PDFs into subagent task messages; pass file PATHS and
  let the subagent read them (fresh context is the point).
- Verifier independence is absolute: verifier task messages contain only
  the artifact paths their section names, never other verifiers' output
  and never your commentary on the company.
- Respect the flag rules: nothing halts on company quality. Only
  mechanical failures halt.
