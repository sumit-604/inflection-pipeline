---
description: Run the full Inflection Alpha pipeline on a run folder. Usage: /run-pipeline runs/<ticker>-<date>
---
You are the pipeline orchestrator. The user has given you a run folder:
$ARGUMENTS

Execute the full pipeline per prompts/00-orchestrator.md. Read that file
now; it is the authority on sequence, handoff schemas, flag rules, and
error handling. Then:

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
   Create outputs/blocks, outputs/reports, outputs/final inside the run
   folder.

2. EXECUTE the stages by invoking the matching subagent for each, in
   dependency order (1 and 2 can interleave; 4, 5, 8, 9 after 3; 6 after
   5; 7 after 1; 10 after all of 1-9; 11 after 10; verifiers after 11,
   all four; 13 last). For each invocation, pass in the task message:
   the exact input file paths the stage needs, the injected content the
   prompt's {{...}} markers expect (prior YAML blocks inline, since
   blocks are small), and the output path outputs/reports/<stage>.md.
   Stage 2 is THREE sequential invocations of stage-02-notes-pass (pass
   1, then pass 2 with pass 1's report path, then pass 3 with both).
   Stage 11: pass the three framework file paths from frameworks/ so the
   subagent reads them as its stable prefix. If frameworks/ is missing
   any of the three files, STOP before stage 11 and tell the user which
   to add.

3. COLLECT each stage's YAML block into outputs/blocks/<stage>.yaml.
   Malformed or missing block: re-invoke once with the retry addendum
   from the orchestrator; second failure halts the run with the stage
   named.

4. COMPUTE the confidence delta from the four verifier blocks per the
   orchestrator's Section 5, write it to outputs/blocks/confidence.yaml.

5. INVOKE stage-13-synthesis with everything. Split its output into the
   three files in outputs/final/ at its FILE dividers.

6. COMMIT all outputs with message "pipeline run: <ticker> <date>" and
   report to the user: verdict line, decision, entry range, flags
   active, confidence delta overall, and the three final file paths.

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
