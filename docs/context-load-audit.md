# Context load audit (18 July 2026)

Question: what gets loaded into every session whether the task needs it or not,
and can we load less?

## The good news: the pipeline is already just-in-time

The heavy rule-book files are NOT loaded every session. Each pipeline stage only
loads the files it needs, injected at run time:

- The big framework files (Master ~12.7k tokens, FTTCP ~12.8k, Section 1B
  ~4.9k + ~1.7k) load only into the valuation and thesis stages that use them.
- A stage that reads annual reports loads AR inputs, not FTTCP. A stage that
  writes an X post would not pull valuation scaffolding.

So the worry from the review ("when writing an X post it still loads full FTTCP")
does not apply here. That is already handled by the stage design.

## The one real always-on cost: LESSONS.md

`LESSONS.md` is ~71 KB (~18k tokens) and was being read at the start of *every*
session. It keeps growing (entries are never deleted). Most light sessions (a
quick question, a small edit) do not need 18k tokens of run history.

**Fix applied:** only the sessions that actually use it — `/run-pipeline`,
`/fttcp`, `/finalize`, `/compost` — read it at start now. Lighter sessions skip
it. Changed in CLAUDE.md (MEMORY section).

`CLAUDE.md` itself is small (~850 tokens) and stays always-on. That is correct.

## Done: LESSONS.md split (token-optimization Phase 2)

`LESSONS.md` grew forever (~18k tokens, never deleted) and was read at the
start of every heavy command. Fixed by splitting: the active `LESSONS.md` is
now a lean head (named failure catalogue, recurring patterns, promoted-to-law
fixes, open actions) under a hard 1,500-token budget (~1.1k actual), and the
full dated run history moved to `LESSONS_ARCHIVE.md` (never deleted). The
orchestrator commands read the lean active file; new dated entries append to
the archive; `/compost` mines the archive and reviews one active lesson for
archiving on each promotion. Every pattern-match preserved (the
INDETERMINATE-cash guard stays law in `prompts/00-orchestrator.md`).

## Done: session and cache discipline (Phase 3)

Added a SESSION DISCIPLINE section to `CLAUDE.md` (model/effort fixed per
session, quiet-by-default command flags) and a SESSION HYGIENE section to
`prompts/00-orchestrator.md` (`/clear` between companies; @-mention the
orchestrator's own stable project reads, per-company sources still travel to
subagents as paths).
