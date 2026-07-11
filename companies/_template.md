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
