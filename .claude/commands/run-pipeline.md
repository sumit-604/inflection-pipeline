---
description: Run the full Inflection Alpha pipeline on a run folder. Usage: /run-pipeline runs/<ticker>-<date>
---
You are the pipeline orchestrator. The user has given you a run folder:
$ARGUMENTS

Execute the full pipeline per prompts/00-orchestrator.md. Read that file
now; it is the authority on sequence, handoff schemas, flag rules, and
error handling. Then:

1. VALIDATE (stage 0, do this yourself): check the run folder against
   the input contract in the orchestrator. manifest.yaml must exist and
   parse. Identification is by subfolder, not filename. Required folder
   counts: inputs/annual-report/ exactly 1 PDF; inputs/results/ 2 or 3
   PDFs (both pass); inputs/rating/ exactly 1 PDF; inputs/concalls/
   exactly 3 PDFs, but required ONLY when the manifest has
   concalls_available: true (when false, concalls/ may be empty or absent
   and the run proceeds in no-concall mode). Any folder missing or with
   the wrong count: STOP and list the offending folders. Optional folders
   (inputs/peer-concalls/, inputs/screening/, inputs/presentation/):
   proceed if empty or absent, record in input_gaps. Create outputs/blocks,
   outputs/reports, outputs/final inside the run folder.

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
