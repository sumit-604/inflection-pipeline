# token-meter (Claude Code mod)

A live band above the prompt: session tokens, cache-hit rate, subagents finished,
and the last three subagent runs with their tokens.

- `/cost-bar` shows or hides the band.
- `/stage-cost runs/<ticker>-<date> [--all]` appends one line per finished pipeline
  stage (agent types `stage-*`, `verifier-*`, `quarterly-*`; `--all` adds every
  subagent) to that run's `session-cost.md`, in the ledger's row shape:
  `| # | stage | model | effort | in_tok | out_tok | total_tok | wall | run# |`.
  in_tok is uncached + cache-read + cache-write input tokens. Effort comes from the
  agent file's frontmatter. Each stage is logged once.
- The append is the only write. Everything else is read-only.

Load it for one session: `claude --plugin-dir tools/mods/token-meter`.
Check it: `claude plugin validate tools/mods/token-meter` and
`claude plugin test tools/mods/token-meter`.
