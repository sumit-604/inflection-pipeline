# Session cost ledger — vilas-2026-09-03 (phase 1)

Per-stage token ledger. One line per subagent run.

| # | stage | model | effort | in_tok | out_tok | total_tok | wall | run# |
|---|-------|-------|--------|--------|---------|-----------|------|------|
| 0 | input validation | orchestrator (opus-4-8) | n/a | n/a | n/a | n/a | n/a | 1 |
| 2 | notes triple-pass (pass 1) | claude-sonnet | default | n/a | n/a | 282810 | 7m40s | 1 |
| 1 | gate 0 (data-gap fail, results PDFs unreadable) | claude-sonnet | default | n/a | n/a | 87982 | 10m53s | 1 |
| 2 | notes triple-pass (pass 2) | claude-sonnet | default | n/a | n/a | 294324 | 6m11s | 2 |
