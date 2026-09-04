# Session cost ledger — vilas-2026-09-03 (phase 1)

Per-stage token ledger. One line per subagent run.

| # | stage | model | effort | in_tok | out_tok | total_tok | wall | run# |
|---|-------|-------|--------|--------|---------|-----------|------|------|
| 0 | input validation | orchestrator (opus-4-8) | n/a | n/a | n/a | n/a | n/a | 1 |
| 2 | notes triple-pass (pass 1) | claude-sonnet | default | n/a | n/a | 282810 | 7m40s | 1 |
| 1 | gate 0 (data-gap fail, results PDFs unreadable) | claude-sonnet | default | n/a | n/a | 87982 | 10m53s | 1 |
| 2 | notes triple-pass (pass 2) | claude-sonnet | default | n/a | n/a | 294324 | 6m11s | 2 |
| 1 | gate 0 (re-run, corrected inputs) | claude-sonnet | default | n/a | n/a | 75449 | 5m52s | 2 |
| 2 | notes triple-pass (pass 3, consolidation + B02) | claude-sonnet | default | n/a | n/a | 79768 | 5m15s | 3 |
| 7 | emerging moat scan | claude-sonnet | default | n/a | n/a | 528157 | 9m41s | 1 |
| 3 | AR deep dive | claude-sonnet | default | n/a | n/a | 499439 | 11m37s | 1 |
| 4 | business model decoder | claude-sonnet | default | n/a | n/a | 523998 | 7m21s | 1 |
| 5 | concall analysis | claude-sonnet | default | n/a | n/a | 238078 | 8m30s | 1 |
| 8 | promoter check (web, partial) | claude-sonnet | default | n/a | n/a | 319465 | 12m40s | 1 |
| 6 | peer concall verification | claude-sonnet | default | n/a | n/a | 681740 | 9m43s | 1 |
