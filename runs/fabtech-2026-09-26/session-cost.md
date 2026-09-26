# SESSION COST LEDGER — FABTECH 2026-09-26 (step1 intake + phase 1)

Token counts come from subagent result metadata (total only; the harness does
not split input/output, so in_tok/out_tok read n/a).

| # | stage | model | effort | in_tok | out_tok | total_tok | wall | run# |
|---|---|---|---|---|---|---|---|---|
| 0 | step1 intake + corpus repair + input validation (incl. AR OCR) | orchestrator (opus, inline) | n/a | n/a | n/a | n/a | ~90m | 1 |
| 2 | notes triple-pass, pass 1 | claude-sonnet-5 | default | n/a | n/a | 216527 | 5m47s | 1 |
| 2 | notes triple-pass, pass 2 | claude-sonnet-5 | default | n/a | n/a | 83532 | 2m39s | 2 |
| 2 | notes triple-pass, pass 3 (consolidated) | claude-sonnet-5 | default | n/a | n/a | 87339 | 3m44s | 3 |
