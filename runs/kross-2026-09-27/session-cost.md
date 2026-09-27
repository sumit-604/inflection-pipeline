# SESSION COST LEDGER — KROSS 2026-09-27 (step1 intake + phase 1)

Token counts come from subagent result metadata (total only; the harness does
not split input/output, so in_tok/out_tok read n/a).

| # | stage | model | effort | in_tok | out_tok | total_tok | wall | run# |
|---|---|---|---|---|---|---|---|---|
| 0 | step1 intake + corpus repair + input validation | orchestrator (opus, inline) | n/a | n/a | n/a | n/a | ~40m | 1 |
| 1 | gate 0 scorecard | claude-sonnet-5 | default | n/a | n/a | 111540 | 7m22s | 1 |
| 2 | notes triple-pass, pass 1 | claude-sonnet-5 | default | n/a | n/a | 133955 | 5m57s | 1 |
| 1 | gate 0 scorecard (peer rescore, resumed) | claude-sonnet-5 | default | n/a | n/a | 42469 | 4m02s | 2 |
| 2 | notes triple-pass, pass 2 | claude-sonnet-5 | default | n/a | n/a | 161252 | 4m18s | 2 |
| 2 | notes triple-pass, pass 3 (consolidation) | claude-sonnet-5 | default | n/a | n/a | 69933 | 4m01s | 3 |
