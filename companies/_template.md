# COMPANY MEMORY TEMPLATE

One file per ticker at companies/<TICKER>.md. Written or updated at
/finalize close. Read as COMPANY MEMORY by /run-pipeline stage 0 and by
/fttcp whenever the file exists. This is the durable per-company layer that
outlives any single run folder. It is memory to weigh, not a source: every
number a stage reports still comes from that run's own inputs, verified
against the source PDFs.

Keep it short. It is a memory, not an archive. Carry the existing content
forward at each /finalize and update it; never delete an operator ruling or
a run-folder link.

## THESIS (one line)
The current one-line thesis from the latest run.

## DECISION STATUS AND ENTRY ZONE
Decision Status and entry zone as of the latest run, with the run date.

## SPEAR
The spear pass result, set by Claude web before any pipeline run on this name.
One line, above the Mental Model block, in one of these two forms:
- Spear: HIT YYYY-MM-DD - entry <= Rs X - load-bearing facts: [2-4 items]
- Spear: OVERRIDE YYYY-MM-DD (operator)
The load-bearing facts are the run's first verification priority. Absent this
line, /run-pipeline and /fttcp STOP.

## HALT 1 GATE
The Understanding Gate rulings, each with its date. Set at Halt 1, before
any deliberation or valuation runs.
- Mental Model signed: YYYY-MM-DD (or NOT SIGNED). Signed-model block:
  - FROM rung -> TO rung: [R_ label -> R_ label, per line where lines differ]
  - Engine: [the one or two things that physically change, one line]
  - Proof gate: [exact metric + threshold FTTCP tests, quarter by quarter]
  - Ugliness verdict: [ARTIFACT-OF-CLIMB | STRUCTURAL-FEATURE] — [one line]
  - Transition falsifier: [evidence that kills the transition thesis]
  - Business falsifier: [evidence that kills the FROM business itself]
- Halt 1 decision (KILL/SHALLOW/PROCEED): YYYY-MM-DD [decision] — [reasoning]

## OPERATOR RULINGS
Every operator ruling with its date, appended and never deleted.
- YYYY-MM-DD: [ruling] — [operator's reasoning]

## ACTIVE TRIPWIRES
The thesis-broken triggers and falsification metrics currently live.
- [metric and threshold]

## OPTIONALITY REGISTER (summary)
The optionality register items being watched (from B07.optionality_register),
one line each.
- [optionality] → converts on [evidence], first appears [where], window [when]

## RUN FOLDERS
Links to every run folder for this ticker, newest first.
- runs/<ticker>-<YYYY-MM-DD>/
