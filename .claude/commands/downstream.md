---
description: Downstream Signal Identification (Role 5.5) for one company, autonomous. Usage: /downstream runs/<folder> | <ticker> | <name fragment>
model: sonnet
---
You are running Role 5.5, Downstream Signal Identification, for the operator,
Keerti Kaushik, as a standalone stage. Your job is to identify the external,
leading, primary-source signals on which the company's forward thesis depends,
verify each one, and write the workup output into the run folder. No questions
to the operator; make every call and print a finished result.

The run folder argument is:
$ARGUMENTS

## NAME RESOLUTION (do this first, silently)

The argument may be a full path, a bare ticker (any case), or a company-name
fragment. If it is not an existing path, resolve it to the runs/ folder whose
name starts with the lowercased argument, or whose manifest company field
contains the fragment, picking the LATEST date. State the resolved folder in
one line before you start. If nothing matches, list the available runs under
runs/ and stop. If more than one matches at the same latest date, list the
matches and pick the latest; if still tied, ask.

## WHAT TO READ

- `manifest.yaml` (company, ticker, run_date, run_type).
- The prior blocks, if they exist, from `outputs/blocks/`: `B03-ardeep.yaml`,
  `B04-bizmodel.yaml`, `B05-concall.yaml`, `B06-peers.yaml`, and the matching
  reports under `outputs/reports/`. These are the ONLY basis for discovering
  dependencies.
- The run folder `inputs/` (annual report, presentations, results, rating,
  and `inputs/announcements/` if present) as supporting documents.

If the prior blocks are ABSENT (the evidence pipeline has not been run for this
company), do NOT invent them. Run in DEGRADED MODE: discover dependencies from
the raw `inputs/` documents (annual report, results, investor presentation),
state prominently that B03-B06 were unavailable, list them in `input_gaps`,
lower confidence, and set `status: partial`. Never fabricate a concall or a
business-model finding that does not exist in the folder.

## HOW TO RUN

Follow `prompts/05b-downstream-signal-pipeline.md` exactly: everything above
its "INJECTED INPUTS" section is your operating rules. Execute all five steps
in one pass. Use web search ONLY to locate and verify each signal's primary
source; discover dependencies from the documents, never from the web. The
target company's own MD&A, presentation, or concall is never its own
downstream signal. Record searches performed and skipped.

## OUTPUT AND SAVE

- Write the full five-step report to `outputs/reports/05b-downstream.md` in the
  resolved run folder (create `outputs/reports/` if missing).
- Write the fenced YAML block to `outputs/blocks/B05b-downstream.yaml` (create
  `outputs/blocks/` if missing).
- Print a short plain-language summary to the operator: the count of verified
  signals, the Signal Gate effect on FTTCP, and whether the thesis is
  externally verifiable (the INSUFFICIENT CONVICTION candidacy).
- Commit quietly: `git add` the two output files and
  `git commit -q -m "Role 5.5 downstream signals: <TICKER>"`. Do not push
  unless the operator asks.

Pipeline discipline applies: nothing halts on company quality; flags
propagate; only a mechanical failure halts (missing run folder, missing
manifest). Fewer than three verifiable signals is a finding, not a failure:
record it and flag INSUFFICIENT CONVICTION candidacy for Role 2.
