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

## One thing to watch later (not fixed here)

`LESSONS.md` grows forever. Even for the heavy commands, ~18k tokens will keep
climbing. When it gets uncomfortable, the clean move is: keep the full file as
the permanent archive, but split a short "active lessons" head (the
PROMOTED-TO-LAW rules plus the last ~10 entries) that the commands read, and let
`/compost` work the full archive. Left as a future step to avoid bundling it in.
