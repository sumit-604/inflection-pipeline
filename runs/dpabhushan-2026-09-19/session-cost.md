# SESSION COST LEDGER — DPABHUSHAN 2026-09-19 (step1 intake + phase 1)

Token counts come from subagent result metadata (total only; the harness does
not split input/output, so in_tok/out_tok read n/a).

| # | stage | model | effort | in_tok | out_tok | total_tok | wall | run# |
|---|---|---|---|---|---|---|---|---|
| 0 | step1 intake + corpus repair + input validation | orchestrator (opus, inline) | n/a | n/a | n/a | n/a | ~70m | 1 |
| 1 | gate 0 scorecard (layout text, superseded) | claude-sonnet-5 | default | n/a | n/a | 151657 | 11m39s | 1 |
| 2 | notes triple-pass, pass 1 | claude-sonnet-5 | default | n/a | n/a | 192948 | 11m30s | 1 |
| 1 | gate 0 scorecard (table text, governs) | claude-sonnet-5 | default | n/a | n/a | 137514 | 10m07s | 2 |
| 2 | notes triple-pass, pass 2 | claude-sonnet-5 | default | n/a | n/a | 181911 | 6m58s | 2 |
| 2 | notes triple-pass, pass 3 (consolidated) | claude-sonnet-5 | default | n/a | n/a | 101923 | 4m00s | 3 |
