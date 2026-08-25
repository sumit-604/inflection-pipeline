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
     - inputs/prospectus/     0-2 PDF (DRHP/RHP; MANDATORY-to-attempt and a
                              HIGH gap if the company listed within ~3 years
                              of run_date, per manifest.listed_date or IPO
                              evidence — it carries promoter/group history and
                              the restated pre-IPO financials nothing else has)
     - inputs/annual-report/  0-1 PDF
     - inputs/results/        0-3 PDFs (use the 3 most recent if more)
     - inputs/rating/         0-1 PDF (most recent if more)
     - inputs/concalls/       0-3 PDFs, honoring concalls_available; when
                              concalls_available is false the run proceeds
                              in NO-CONCALL MODE
     - inputs/peer-concalls/  0-12 PDFs
     - inputs/announcements/  0-N PDFs (exchange / Reg 30 filings, last ~12m;
                              the documented-ACTION record)
     - inputs/shareholding/   0-N (latest quarterly shareholding pattern;
                              closes FII+DII UA qualifier and pledge trend)
     - inputs/research/       0-N (broker notes; NON-ANCHORED, leads only)
     - inputs/screening/      0-N (csv / txt / pdf / xlsx)
     - inputs/presentation/   0-N
     - inputs/other/          0-N (preserved, never consumed)
   HALT ONLY IF: manifest.yaml is missing or unparseable, OR the entire
   inputs/ tree is empty. In every other case proceed, writing B00 with
   input_gaps naming each absent document type; degraded stages run per
   the orchestrator's DEGRADATION MAP. There is no count-based halting.

   EMPTY-FOLDER CONFIRMATION: after the inventory above, if ANY input
   folder is empty or absent (prospectus, annual-report, results, rating,
   concalls, peer-concalls, announcements, shareholding, research,
   screening, presentation), PAUSE before executing any stage and ask the
   operator exactly once, listing all empty folders together in one
   message, and calling out an empty prospectus/ as HIGH priority when the
   company listed within ~3 years: "These input folders are empty: [list].
   Proceed with these gaps, or push the documents (py
   collect_to_repo.py --push-again) and tell me to continue?" Proceed
   only on the operator's explicit answer, then never ask again for the
   rest of the run. If the manifest has concalls_available: false, do
   not list concalls or peer-concalls as gaps: their absence is
   declared, not accidental. This is the single permitted question in
   the pipeline.

   COMPANY MEMORY: if companies/<TICKER>.md exists (the durable per-company
   memory written by prior /finalize runs), read it at stage 0 and carry it
   into every stage task message as COMPANY MEMORY, alongside any refresh-run
   PRIOR RUN CONTEXT. It is memory, not a source: stages weigh it but never
   treat its figures as anchored evidence; every number a stage reports
   still comes from this run's own inputs, verified against the source PDFs.

   Create outputs/blocks, outputs/reports, outputs/final inside the run
   folder. Also plant inputs/research/.gitkeep alongside the other input
   directories if it is absent: git does not track empty directories, so a
   fresh checkout can drop inputs/research/ and the claude.ai
   web-handover-dossier.md then lands nowhere. The .gitkeep keeps the folder
   present for the handover input gate downstream.

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
       (B07) compliance checks only, and pass it ONLY the two rule
       sources those checks need — prompts/01-gate-0-pipeline.md and
       prompts/07-emerging-moat-pipeline.md — alongside B01 and B07. Do
       NOT pass the valuation framework docs (Master Prompt v3.6, Section
       1B layers, FTTCP v2.1): they are consumed only by the B11 valuation
       audit, which is deferred to PHASE 3, so in phase 1 they are dead
       context. Its valuation-adherence audit (B11, B10) must NOT run
       here; it emits the gate0 and emoat sections of B12c with valuation
       left blank/pending.
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

6b. HALT 1 DOSSIER (stage 09b). RUNS LAST, after the verifiers and the
   synthesis-lite, before the halt. Invoke stage-09b-dossier per
   prompts/09b-halt1-dossier.md. Pass it ONLY the committed blocks (B00
   through B09 plus the verifier blocks B12a, B12b, B12c-partial, B12d) and
   the stage reports for quote retrieval, and the output path
   outputs/reports/09b-understanding-dossier.md. It assembles from
   committed evidence only: no new research, no web claims, no valuation
   numbers. It writes the five-section understanding dossier (corpus audit,
   mental model declaration draft, business narrative, downstream dossier
   with fragility read, 14-15 point plain-language summary) and emits the
   B09b YAML block. Collect B09b into outputs/blocks/. Nothing in this
   stage or here may mark the Mental Model Declaration signed.

   MECHANICAL DOSSIER CHECK (before the HALT 1 message prints): grep
   outputs/reports/09b-understanding-dossier.md for the five section
   headers (SECTION 1 through SECTION 5, in order), exactly one corpus
   verdict line (CORPUS CURRENT or CORPUS GAPPED), and the
   "DRAFT - PENDING OPERATOR SIGN-OFF" marker in Section 2. On any miss,
   re-run stage 09b once. If it is still malformed after the re-run, STOP
   and report which check failed. The HALT 1 message never prints over a
   malformed dossier.

7. COMMIT all outputs with message "phase 1 (evidence): <ticker> <date>"
   and report to the user: the corpus verdict and fragility verdict from
   the dossier, the gate recommendation verdict line, flags active,
   phase-1 confidence delta overall, and the final file paths including
   outputs/reports/09b-understanding-dossier.md.

   PRINT FINALS IN CHAT: after writing the final files and committing,
   always print the primary human-readable documents in full in the chat,
   in this order: 09b-understanding-dossier.md, then business-narrative.md,
   then gate-recommendation.md. Then tell the operator exactly:

   "HALT 1 — UNDERSTANDING GATE. The dossier is at
   outputs/reports/09b-understanding-dossier.md. Operator decisions
   required before anything further runs: (1) resolve corpus gaps or
   accept CORPUS CURRENT; (2) take the Mental Model Declaration to
   claude.ai for live stress-testing and sign-off; (3) decide KILL /
   SHALLOW WATCH / PROCEED. On PROCEED: live verification + Role 5.5
   tracker writes happen in claude.ai; /fttcp runs only after the tracker
   gate is satisfied and the model is signed. Record the decision in
   companies/<TICKER>.md."

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
