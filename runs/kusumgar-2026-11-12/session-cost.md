# Session cost — KUSUMGAR 2026-11-12 (Phase 1, /step1)

Per-stage token ledger. One row per subagent run, from the subagent result
metadata. n/a where the harness does not expose the figure; never an estimate.

| # | stage | model | effort | in_tok | cache_read | cache_write | out_tok | total_tok | wall | run# |
|---|---|---|---|---|---|---|---|---|---|---|
| 0 | stage-00-intake-check | claude-haiku-5-5 | medium | n/a | n/a | n/a | n/a | 84778 | 152s | 1 |
| 1 | stage-01-gate0 | claude-sonnet-5-5 | medium | n/a | n/a | n/a | n/a | 112016 | 286s | 1 |
| 2 | stage-02-notes-pass (pass 1) | claude-sonnet-5-5 | default | n/a | n/a | n/a | n/a | 232562 | 556s | 1 |
| 2 | stage-02-notes-pass (pass 2) | claude-sonnet-5-5 | default | n/a | n/a | n/a | n/a | 148383 | 362s | 1 |
| 2 | stage-02-notes-pass (pass 3) | claude-sonnet-5-5 | default | n/a | n/a | n/a | n/a | 87001 | 173s | 1 |
| 3 | stage-03-ardeep | claude-sonnet-5-5 | default | n/a | n/a | n/a | n/a | 407088 | 943s | 1 |
| 5 | stage-05-concall (no-concall mode + 1 transcript) | claude-sonnet-5-5 | default | n/a | n/a | n/a | n/a | 129853 | 229s | 1 |
