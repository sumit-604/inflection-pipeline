---
description: PHASE 3 (finalize) of the Inflection Alpha pipeline. Usage: /finalize runs/<ticker>-<date>
---
You are the pipeline orchestrator, running PHASE 3 (finalize). The user
has given you a run folder:
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

PHASE 3 turns the phase-1 evidence and the phase-2 deliberation into the
final investment decision: valuation, thesis, devil's advocate, valuation
verification, final synthesis, and the Notion save payload.

## GATE: DELIBERATION MUST EXIST

Before anything else, check that outputs/final/fttcp-deliberation.md
exists in the run folder. If it does NOT, REFUSE to start and tell the
operator:

  "Cannot finalize: outputs/final/fttcp-deliberation.md is missing. Run
  /fttcp runs/<folder> first (PHASE 2 deliberation), then re-run
  /finalize."

Do not run any stage until that file is present. Once it is present,
proceed AUTONOMOUSLY through every step below in one run, no stops.

Read prompts/00-orchestrator.md now (PHASES section and the rule that
FTTCP deliberation conclusions supersede pipeline determinations in
phase 3), then:

1. STAGE 10 — INPUT ASSEMBLY. Invoke stage-10-assembly with the B01..B09
   blocks and the results PDFs AS BEFORE, and ADDITIONALLY the
   deliberation record outputs/final/fttcp-deliberation.md. The
   deliberation record is AUTHORITATIVE and supersedes the pipeline's own
   earlier determinations wherever they conflict. In the task message,
   direct the stage that these deliberation outputs are authoritative
   inputs:
     - the FTTCP ROCE forward verdict (the sole authority for Pillar 1
       ROCE selection),
     - the cash-conversion structural / growth-induced determination as
       the operator confirmed or overrode it,
     - every recorded operator override.
   Where any of these conflict with a value the pipeline assembled
   earlier, the deliberation value wins and the assembly must anchor it to
   the deliberation record. Collect B10 into outputs/blocks/.

2. STAGE 11 — VALUATION. Invoke stage-11-valuation exactly per the
   existing wrapper: pass the three framework file paths from frameworks/
   as its stable prefix plus B10. If frameworks/ is missing any of the
   three files, STOP and tell the user which to add. The FTTCP ROCE
   forward verdict and structural/growth determination it consumes are
   the deliberation-confirmed ones carried on B10. Collect B11.

3. STAGE 14 — ROLE 2 INVESTMENT THESIS. Invoke stage-14-thesis (model
   opus, thin wrapper reading its Role 2 section from
   frameworks/Master_Project_Prompt_v3.3.md, pipeline mode, source
   anchors). Pass B01..B11, the Role 1 valuation report, and the
   deliberation record. Its output ends with the B14-thesis YAML block
   (verdict, entry range, position size with any documented override,
   thesis-broken conditions, monitoring checklist). Collect B14.

4. STAGE 15 — ROLE 3 DEVIL'S ADVOCATE. Invoke stage-15-devil (model opus,
   thin wrapper reading its Role 3 section from
   frameworks/Master_Project_Prompt_v3.3.md, pipeline mode, source
   anchors). Pass Role 2's output (B14 report) PLUS all blocks. Its output
   ends with the B15-devil YAML block (per-dimension survives / weakened /
   destroyed, overall, top counters). Collect B15.

5. VERIFIER C — VALUATION ADHERENCE (phase 3 half). Invoke
   verifier-c-framework with the framework docs and B10, B11 for its
   deferred valuation-adherence audit, EXTENDED to also check Role 2's
   (B14) decision rules and position-sizing logic against the Master
   prompt. Give it only the artifact paths its section names, never other
   verifiers' output, never your commentary. Merge its valuation findings
   into B12c (its Gate 0 + EM findings were recorded in phase 1) and
   recompute the framework-adherence confidence component, then update
   outputs/blocks/confidence.yaml to the full four-component delta.

6. FINAL SYNTHESIS. Invoke stage-13-synthesis with everything (all blocks
   B01..B15, both halves of B12c, the full confidence delta, the
   deliberation record, and the stage reports), instructing it in the
   task message to run in PHASE 3 FINALIZE mode and produce all four
   deliverables, each written to outputs/final/ at its FILE dividers:
     - business-narrative.md: the final narrative, now including the
       valuation conclusion (both destination PE tracks, entry zone,
       decision) and the thesis/devil's-advocate outcome.
     - fttcp-recommendation.md: the full investment recommendation per the
       synthesis prompt's Deliverable 2 rules — the five-verdict gate line,
       the valuation decision (BUY / WATCHLIST / AVOID, entry range, MoS
       price, both destination PE tracks, Hurdle verdict), all active flag
       blocks, the full confidence delta, monitorables, and the
       falsification line.
     - verifier-summary.md: all verifier findings including the phase-3
       valuation-adherence audit, sorted by severity with location anchors.
     - fttcp-handoff.md: the ARCHIVE DOSSIER. The machine-anchored record
       carrying every block reference, the deliberation-confirmed inputs
       and overrides, the Role 1 / Role 2 / Role 3 outputs, and the full
       source anchors. Block references (B04 etc.) are permitted and
       expected here; this is the audit trail, not a reading document.

7. NOTION PAYLOAD. Write outputs/final/notion-payload.md containing the
   full save content structured per Notion_Save_Instructions conventions:
   page title, run summary, verdict, entry zones, thesis-broken triggers,
   monitoring checklist, and links (Drive folder, run folder). Mark the
   file explicitly at the top:

   "Execute via the claude.ai project; never overwrite Decision Status."

   This file is a payload, not an action. Do not write to Notion from this
   session; the operator executes the save in the project.

8. COMMIT all outputs with message "phase 3 (finalize): <ticker> <date>"
   and report to the user: the recommendation verdict line, the valuation
   decision, entry range, flags active, the full confidence delta overall,
   the devil's-advocate overall verdict, and the paths to the four final
   deliverables plus outputs/final/notion-payload.md.

   PRINT FINALS IN CHAT: after writing the final files and committing,
   always print the primary human-readable documents in full in the chat,
   in this order: the thesis verdict card (from B14), then the devil's
   advocate final table (from B15). End with exactly:

   "Files committed. Ask me anything about this analysis — I have the sources."

Rules for you, the orchestrator session:
- You coordinate; you do not analyse. Every judgment comes from a subagent.
- Deliberation conclusions supersede earlier pipeline determinations
  wherever they conflict; this is the phase-3 authority rule.
- Never let any exit PE enter from outside Section 1B v3.3.
- Never paste full PDFs into subagent task messages; pass file PATHS.
- Verifier independence is absolute.
- Nothing halts on company quality; only mechanical failures halt.
