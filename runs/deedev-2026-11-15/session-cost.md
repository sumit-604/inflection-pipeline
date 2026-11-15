# SESSION COST: deedev 2026-11-15 (Phase 1, /step1)

Per-stage token ledger. Subagents run async in this app; the result metadata gives a total token figure and wall time only, so the split columns are n/a. Never an estimate.

| # | stage | model | effort | in_tok | cache_read | cache_write | out_tok | total_tok | wall | run# |
|---|---|---|---|---|---|---|---|---|---|---|
| 0 | stage-00-intake-check | claude-haiku-5-5 | medium | n/a | n/a | n/a | n/a | 127408 | 254s | 1 |
| 1 | gate0 | claude-sonnet-5-5 | medium | n/a | n/a | n/a | n/a | 97582 | 246s | 1 |
| 2 | notes-pass (pass 1) | claude-sonnet-5-5 | default (high) | n/a | n/a | n/a | n/a | 214092 | 410s | 1 |
| 2 | notes-pass (pass 2) | claude-sonnet-5-5 | default (high) | n/a | n/a | n/a | n/a | 174123 | 383s | 2 |
| 2 | notes-pass (pass 3) | claude-sonnet-5-5 | default (high) | n/a | n/a | n/a | n/a | 82097 | 146s | 3 |
| 3 | ardeep | claude-sonnet-5-5 | default (high) | n/a | n/a | n/a | n/a | 289405 | 676s | 1 |
| 4 | bizmodel | claude-sonnet-5-5 | medium | n/a | n/a | n/a | n/a | 165562 | 358s | 1 |
