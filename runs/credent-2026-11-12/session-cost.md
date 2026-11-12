# SESSION COST: credent-2026-11-12 (Phase 1)

Per-stage token ledger. Token figures come from subagent result metadata. This harness exposes only each subagent's total tokens and wall time. The input, cache-read, cache-write and output split reads n/a, never an estimate.

| # | stage | model | effort | in_tok | cache_read | cache_write | out_tok | total_tok | wall | run# |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | stage-01-gate0 | claude-sonnet-5-5 | medium | n/a | n/a | n/a | n/a | 68063 | 2m18s | 1 |
| 0 | stage-00-intake-check | claude-haiku-5-5 | medium | n/a | n/a | n/a | n/a | 175796 | 2m41s | 1 |
| 2 | stage-02-notes-pass (pass 1) | claude-sonnet-5-5 | high (default) | n/a | n/a | n/a | n/a | 203800 | 7m54s | 1 |
