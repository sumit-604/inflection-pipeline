# token-meter (Claude Code mod)

A live band above the prompt: session tokens, cache-hit rate, subagents finished,
and the last three subagent runs with their tokens.

- `/cost-bar` shows or hides the band.
- `/stage-cost runs/<ticker>-<date> [--all]` appends one line per finished pipeline
  stage to that run's `session-cost.md`, in the ledger's row shape:
  `| # | stage | model | effort | in_tok | cache_read | cache_write | out_tok | total_tok | wall | run# |`.
  in_tok is uncached + cache-read + cache-write input tokens; cache_read and
  cache_write show the split. Effort comes from the agent file's frontmatter. Each
  stage is logged once. A ledger that holds only the older 9-column header gets the
  current header as a new table below its old rows.
- The append is the only write. Everything else is read-only.

## What it records

Per subagent run: input tokens, cache-read tokens, cache-write tokens, output
tokens, total tokens and wall time. `/stage-cost` writes the runs of agent types
`stage-*`, `verifier-*` and `quarterly-*`; with `--all` it writes every subagent.

## What it does not record

- Orchestrator usage: the main session's own turns feed the band's session total
  but never reach the ledger. Get the session total from `/cost` in the terminal.
- Inline stage 0 work, which runs on the orchestrator session.
- Anything in a session where the mod is not loaded. It loads only through
  `claude --plugin-dir tools/mods/token-meter`.
- Anything after the session ends. Run `/stage-cost` before closing.

Load it for one session: `claude --plugin-dir tools/mods/token-meter`.
Check it: `claude plugin validate tools/mods/token-meter` and
`claude plugin test tools/mods/token-meter`.
