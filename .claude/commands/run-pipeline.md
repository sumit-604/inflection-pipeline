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

LESSONS PRE-READ: after the run folder resolves and before any stage runs,
read the ACTIVE LESSONS.md (not LESSONS_ARCHIVE.md) and print, before
proceeding: (a) every entry under OPEN ACTIONS, plus every line marked OPEN,
IN PROGRESS or PENDING anywhere in the file, one line each; (b) every lesson
tagged [sector: X] where X equals manifest.yaml sector_cap_row, or
[archetype: Y] where Y equals the archetype declared in companies/<TICKER>.md
(Mental Model block) or, when that is absent, in the B04 business-model block.
If no archetype is declared yet, say so and match on sector only. If nothing
is tagged for this sector or archetype, print "no tagged lessons for this
sector/archetype". The list is memory to weigh, never an instruction that
overrides a prompt or framework, and it is never passed to a stage or
verifier subagent.

TOOLING GATE (before stage 0, not after the first failure). The
session-start hook runs a PDF tooling preflight and reports its result in
session context. Read that line first. Then confirm it yourself: test-read
one inputs/ PDF end to end. Tooling that the hook could not install is
installed here (apt-get install -y -qq poppler-utils; pip install -q pypdf;
pip install -q --force-reinstall cffi when pypdf imports but fails on a real
file).

If a real Read still fails, do not start the stages on broken tooling. Switch
the whole run to pre-extracted text FIRST: extract every inputs/ PDF to a
page-marked .txt beside it (one "[page N]" marker per page), and pass the
.txt path to every stage and every verifier in place of the PDF. Pre-extracted
text is the reliable default on any large corpus in any case, because it also
avoids the ~20-32MB image-render wall. Record the switch in B00.

Verifiers must never skip source verification because rendering is
unavailable; if a PDF is genuinely unreadable by both routes, name it in the
run log and in the confidence delta note.

OPERATOR CONTEXT MID-RUN (provenance, hard rule). The operator sometimes
supplies a fact, a correction or a document in chat while the run is going:
a figure from a filing not in the corpus, a ruling, a company detail. It is
useful and it must not vanish into conversation, where the next stage cannot
see it and the verifiers cannot audit it.

On every such input, before using it:
- Write it to runs/<ticker>-<date>/inputs/operator-notes.md, appending one
  dated entry: what was said, verbatim, and the date and time.
- Classify it. A DOCUMENT the operator pushes is ordinary anchored evidence
  once it is in an inputs/ folder. A FIGURE or claim typed in chat is
  OPERATOR CONTEXT: it is memory to weigh, the same tier as COMPANY MEMORY,
  and it is never anchored evidence. A RULING is an operator ruling, recorded
  with its date, and it binds.
- Cite it as (operator, YYYY-MM-DD) wherever it is used, so Verifier A reads
  it as unanchored rather than as a number with a missing source.
- Pass it into every later stage's task message as OPERATOR CONTEXT, and name
  it in B00.input_gaps if it fills a gap the corpus should have filled.

Never let an operator figure enter a table with a document anchor it does not
have. The rule is provenance, not distrust: an unattributed number cannot be
verified by anyone later, including the operator.

EXECUTION DISCIPLINE: invoke every stage as a foreground subagent call
that blocks until the subagent returns. Never use background task
launching with passive waiting. Achieve parallelism only by invoking
multiple foreground subagents in a single message where the dependency
table allows.

PROVE COMPLETION, DO NOT ASSUME IT. Stages have repeatedly been dispatched
to the background despite the rule above, and the run carried on against
reports that did not exist yet, because "the call returned" was treated as
"the stage finished". The two are different events. Before you treat any
stage as done, and before any later stage reads its output:

- Confirm the report file exists at the output path you gave it and is not
  empty. A missing or empty file means the stage did not run to completion,
  whatever the reply said.
- Confirm the block file exists at the block path you gave it and parses.
  The stage writes that file before it replies, so a missing block file with
  a block sitting in the reply means the reply arrived without the work
  behind it.
- Confirm the YAML block you have came from that invocation, not from a
  template or an earlier stage.
- If either check fails, the stage was backgrounded or it died. Re-invoke it
  in the foreground. Do not proceed on a partial result, and do not wait
  passively for a background task to land.
- A stage that cannot be made to run in the foreground after one re-invoke
  halts the run with the stage named. Note it in the run log and in
  LESSONS_ARCHIVE.md at close.

After each stage returns AND passes the completion check, validate its YAML
block and commit before proceeding. At that same moment, before moving to
the next stage, append one line to the per-stage token ledger in
runs/<ticker>-<date>/session-cost.md, taken from the subagent result
metadata: stage number, stage name, model, effort, input tokens, output
tokens, total tokens, and wall time. Create the ledger with its header row
when the first stage writes to it. Write one line per subagent run: if a
stage runs as a loop or is retried, each run gets its own line with a run
counter (run# 1, 2, ...) so the loop or retry total stays visible. Never
defer these lines to the end of the run; each is written and committed with
its own stage. The ledger row shape:

    | # | stage | model | effort | in_tok | out_tok | total_tok | wall | run# |

A stage exceeding 45 minutes is noted in the run log, not killed.

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

   SECTOR CAP ROW: the manifest ships sector_cap_row empty and a
   sector_cap_row_guess beside it. Resolve the real row now, per the
   orchestrator's SECTOR CAP ROW RESOLUTION section: read the cap table
   (section-1b chunk 05), pick the row the business sits in, write it into
   manifest.yaml and B00 with its evidence and the chunk cite. The guess is a
   hint to check. "NOT FOUND" is a valid answer and a HIGH gap; it blocks
   stage 11 in phase 3, not the evidence stages here.

   DOCUMENT IDENTITY: run the orchestrator's DOCUMENT IDENTITY CHECK over
   every PDF in inputs/ and write B00.corpus_manifest[]. Read the first page
   of each document and take its issuer, type and period from the page, never
   from the filename. Move a misfiled document and record both paths. A
   broker note is research/ whatever it is called.

   UNITS: read the reporting unit off the face of the latest results filing
   and the AR and write B00.reporting_units. Name the unit in every stage
   task message (step 2).

   COLLECTOR DEFECT GATE: the collector records what it already knows it got
   wrong. Read manifest.collector_warnings and carry every entry into
   B00.input_gaps verbatim. Then run the three checks the collector cannot
   make for itself, per the orchestrator's COLLECTOR DEFECT GATE section:
     - A screening CSV is checked for CONTENT, never for existence. Open each
       one. A file whose row labels are present with no figures beside them is
       an EMPTY export, and counts as an absent document, not a present one.
     - An empty inputs/announcements/ or inputs/shareholding/ is a COLLECTOR
       gap, never evidence that the company files nothing. Record it as a gap
       and say which one it is.
     - manifest.cmp of 0, or a market_cap_cr of 0, means the wrong screener URL
       variant was collected (a /consolidated/ page on a company that files no
       consolidated statements). HALT and tell the operator to re-collect from
       the standalone /company/<TICKER>/ page. Every valuation stage downstream
       reads cmp; a zero there is a mechanical failure, not a gap.

   FRESHNESS PAIR CHECK: after the inventory, run the four-pair freshness
   check per the orchestrator's FRESHNESS PAIR CHECK section and write
   freshness_pairs[] and freshness_verdict into B00. The pairs: newest
   results filing to same-quarter concall (skipped when concalls_available
   is false); rating bulletin to full rationale; any referenced SEBI order
   to its order text; AR not older than the latest audited annual results.
   On any FAIL, B00.freshness_verdict is CORPUS GAPPED-FRESHNESS. This does
   not halt: it caps the phase-1 gate recommendation at PROCEED WITH CAVEATS
   (step 6) and names the missing mate as the first line of
   gate-recommendation.md. Carry the failed pair into the empty-folder
   confirmation message below so the operator can push the missing document.

   EMPTY-FOLDER CONFIRMATION: after the inventory above, if ANY input
   folder is empty or absent (prospectus, annual-report, results, rating,
   concalls, peer-concalls, announcements, shareholding, research,
   screening, presentation), PAUSE before executing any stage and ask the
   operator exactly once, listing all empty folders together in one
   message, and calling out an empty prospectus/ as HIGH priority when the
   company listed within ~3 years: "These input folders are empty: [list].
   Proceed with these gaps, or push the documents (py
   collect_to_repo.py --push-again) and tell me to continue?"

   Ask ONCE and do not block on the answer. The question is delivered through
   AskUserQuestion, whose stream sometimes closes in a remote session; the run
   used to stop there waiting for a reply that could never arrive. If the
   question delivers, proceed on the operator's answer. If it does not deliver,
   or it returns no answer, proceed on the documented evidence-maximizing
   default for each empty folder (run degraded per the DEGRADATION MAP, never
   substitute a guess for a document), record in B00 both the defaults taken
   and the fact that the question was undeliverable, and repeat the full list
   of empty folders in the Halt 1 dossier so the operator sees it there. Either
   way the question is asked once and never again for the rest of the run.
   If the manifest has concalls_available: false, do
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
   blocks are small), the output path outputs/reports/<stage>.md, the BLOCK
   path outputs/blocks/<stage>.yaml, and the units line: "All figures in
   ₹ Cr unless the source says otherwise; the source unit is on the face of
   the document, not in the filename."
   Every stage writes its own block file to the block path before replying;
   the reply is a copy, not the only copy.
   Stage 2 is THREE sequential invocations of stage-02-notes-pass (pass
   1, then pass 2 with pass 1's report path, then pass 3 with both).
   Stages 10 and 11 do NOT run in this phase.

3. COLLECT each stage's block by READING outputs/blocks/<stage>.yaml, the
   file the stage wrote. Compare it with the block in the stage's reply; if
   they differ, the file governs and the difference is noted in the run log.
   If the file is absent, write it from the reply before doing anything else,
   so the block is never carried only in conversation.
   Malformed block, or absent from both file and reply: re-invoke once with
   the retry addendum from the orchestrator; second failure halts the run
   with the stage named.

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
       1B layers, FTTCP v2.3): they are consumed only by the B11 valuation
       audit, which is deferred to PHASE 3, so in phase 1 they are dead
       context. Its valuation-adherence audit (B11, B10) must NOT run
       here; it emits the gate0 and emoat sections of B12c with valuation
       left blank/pending.
   The verifiers run as parallel FOREGROUND calls in one message. Apply the
   completion check in EXECUTION DISCIPLINE to each one separately before
   reading any of them: four verifiers in one message is the place a
   background dispatch hides best, because three good results make the
   fourth look present. A verifier whose report file is missing or empty did
   not run; re-invoke that one alone, in the foreground.
   Collect B12a, B12b, B12c (partial), B12d into outputs/blocks/.

5. COMPUTE the phase-1 confidence delta from the available verifier blocks
   per the orchestrator's Section 5 (numerical_acceptance, redflag_
   coverage, peer_utilisation, and the Gate 0 + EM portion of framework_
   adherence), write it to outputs/blocks/confidence.yaml. The valuation
   framework-adherence component is marked pending phase 3.
   Apply the denominator floor: any component computed on fewer than 4 items
   is NOT APPLICABLE, is dropped from overall, and is listed in
   not_applicable with its counts. Record overall_set_by. Where B12b returns
   acceptance_rate: null, redflag_coverage is not applicable; do not
   substitute a number for it.
   Before computing numerical_acceptance, run the Verifier A identity check:
   for every CRITICAL row in B12a, confirm `claimed` and `source_truth` hold
   genuinely different values. A row where they hold the same value is a
   clerical error in the finding and is struck, with the strike recorded in
   the run log. This is the ONLY permitted reason to strike a Verifier A
   finding: the source-fidelity gate is otherwise absolute, and a CRITICAL
   that survives the identity check triggers REWORK exactly as written.

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
       FRESHNESS CAP: if B00.freshness_verdict is CORPUS GAPPED-FRESHNESS,
       the verdict caps at PROCEED WITH CAVEATS regardless of flag count
       (no better; a more severe REWORK / INSUFFICIENT EVIDENCE still
       stands), and the missing mate document is the FIRST line of the
       file, before any flag block, naming it and its expected source.
       EXCLUDE every valuation-dependent element: no BUY/WATCHLIST/AVOID,
       no entry range, no MoS price, no destination PE tracks, no Hurdle
       verdict. This is the gate decision on evidence alone; the
       investment decision is formed in phase 3.
     - verifier-summary.md: the phase-1 verifier findings tables (A, B, D,
       and the Gate 0 + EM portion of C), sorted by severity, each finding
       with a location anchor, headed by the phase-1 confidence delta.

6b. HALT 1 DOSSIER (stage 09b). RUNS LAST, after the verifiers and the
   synthesis-lite, before the halt. Invoke stage-09b-dossier per
   prompts/09b-halt1-dossier.md. Pass it the committed blocks (B00
   through B09 plus the verifier blocks B12a, B12b, B12c-partial, B12d) and
   the stage reports for quote retrieval, the output path
   outputs/reports/09b-understanding-dossier.md, AND two inputs the Section 6
   Standing Extraction Annex needs: (a) the corpus commit hash, from
   `git rev-parse HEAD` run in the run folder before the invocation, passed
   at the prompt's {{CORPUS_COMMIT_HASH}} marker; (b) the inputs/ PDF paths
   (annual-report/, results/, concalls/, announcements/, shareholding/,
   prospectus/), passed at {{CORPUS_PDF_PATHS}} so the annex can retrieve an
   anchored quote where a stage report does not already carry it. Sections
   1-5 assemble from committed evidence only: no new research, no web claims,
   no valuation numbers. Section 6 is the ANNEX EXCEPTION: it answers the ten
   standing-extraction questions from corpus in quote-then-comment form, and
   may open the named PDFs for anchored quotes. It writes the six-section
   dossier (corpus audit, mental model declaration draft, business narrative,
   downstream dossier with fragility read, 14-15 point plain-language summary,
   then the Section 6 Standing Extraction Annex) and emits the B09b YAML
   block. Collect B09b into outputs/blocks/. Nothing in this stage or here may
   mark the Mental Model Declaration signed.

   MECHANICAL DOSSIER CHECK (before the HALT 1 message prints): grep
   outputs/reports/09b-understanding-dossier.md for the six section
   headers (SECTION 1 through SECTION 6, in order), exactly one corpus
   verdict line (CORPUS CURRENT, CORPUS GAPPED, or CORPUS GAPPED-FRESHNESS),
   and the "DRAFT - PENDING OPERATOR SIGN-OFF" marker in Section 2. ANNEX
   CHECK (team workflow v2, Hand-off 1): confirm Section 6 answers all ten
   numbered questions (1 through 10, in order) and ends with the corpus
   commit hash line; a Section 6 that is absent, short of ten questions, or
   missing the hash makes Halt 1 INCOMPLETE. When the verdict is CORPUS
   GAPPED-FRESHNESS, also confirm the missing mate is the first line of
   outputs/final/gate-recommendation.md. On any miss, re-run stage 09b once.
   If it is still malformed after the re-run, STOP and report which check
   failed. The HALT 1 message never prints over a malformed or annex-
   incomplete dossier.

6c. SESSION CLOSE-OUT (summary block). RUNS AFTER THE LAST STAGE, before
   the run outputs are committed and their PR opens. By now
   runs/<ticker>-<date>/session-cost.md already holds the per-stage token
   ledger built during the run (EXECUTION DISCIPLINE). Append a summary
   block to the same file with four parts:
   (a) TOP FIVE BY TOKENS. The stages ranked by total tokens, the top five,
       each with its share of the run total (its total_tok over the sum of
       every ledger row). Sum a stage's loop or retry runs into one stage
       total for the ranking.
   (b) DOWNSHIFT FAILURES. Any MECHANICAL stage that ran on Opus, flagged
       "DOWNSHIFT FAILURE: <stage>". The mechanical stages are the ones
       DISPATCH routes to haiku (stage 0 validation, stage 10 assembly,
       verifier A); a mechanical stage on Opus means the downshift did not
       take and the run overpaid. Write "none" if every mechanical stage
       ran on haiku.
   (c) COST SPIKES. Any stage whose total tokens exceed 1.5x the same
       stage in the previous run for this ticker (the most recent prior
       runs/<ticker>-<date>/session-cost.md ledger), flagged
       "COST SPIKE: <stage> (<this_total> vs <prior_total>)". Write "none"
       if no prior run exists or nothing crossed 1.5x.
   (d) OPERATOR SNAPSHOT. A reminder line: the operator runs /cost and
       /usage now and pastes the cache hit ratio and the loop totals into
       this file under an "Operator snapshot" heading. The orchestrator
       cannot read those interactive commands, so the operator fills the
       snapshot.
   If any DOWNSHIFT FAILURE or COST SPIKE is found, append one line naming the
   stage to this run's dated entry in LESSONS_ARCHIVE.md (the MEMORY rule's
   home for run history). Add a line under OPEN ACTIONS in LESSONS.md only
   when the item is still open at close, in the form "- OPEN (<YYYY-MM-DD>,
   <TICKER>, <stage>): <what> [session-cost.md]; see LESSONS_ARCHIVE.md
   <YYYY-MM-DD> <TICKER>." The active file is budget-capped (CLAUDE.md
   MEMORY). session-cost.md is a run output: it travels
   with the run outputs on the run branch and its PR, never on a framework
   branch.

7. COMMIT all outputs (including session-cost.md) with message "phase 1 (evidence): <ticker> <date>"
   and report to the user: the corpus verdict and fragility verdict from
   the dossier, the gate recommendation verdict line, flags active,
   phase-1 confidence delta overall, and the final file paths including
   outputs/reports/09b-understanding-dossier.md and session-cost.md.

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
