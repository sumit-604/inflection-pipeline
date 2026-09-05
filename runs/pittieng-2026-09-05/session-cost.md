# Session cost ledger — pittieng-2026-09-05 (phase 1)

Per-stage token ledger. One line per subagent run. Token counts are taken
from the Agent tool result metadata where the harness reports them; "n/a"
where it does not.

| # | stage | model | effort | in_tok | out_tok | total_tok | wall | run# |
|---|-------|-------|--------|--------|---------|-----------|------|------|
| 0 | input validation + corpus audit | orchestrator (claude-fable-5-1) | n/a | n/a | n/a | n/a | ~12m | 1 |
| 2 | notes triple-pass (pass 1) | claude-sonnet | default | n/a | n/a | 283170 | 8m31s | 1 |
| 2 | notes triple-pass (pass 2) | claude-sonnet | default | n/a | n/a | 148436 | 8m57s | 2 |
| 1 | gate 0 scorecard | claude-sonnet | default | n/a | n/a | 180950 | 18m33s | 1 |
| 2 | notes triple-pass (pass 3, consolidation + B02) | claude-sonnet | default | n/a | n/a | 80693 | 5m22s | 3 |
| 3 | AR deep dive | claude-sonnet | default | n/a | n/a | 369769 | 13m07s | 1 |
| 4 | business model decoder | claude-sonnet | default | n/a | n/a | 170183 | 11m11s | 1 |
| 8 | promoter check (web, partial: 2 fetches proxy-blocked) | claude-sonnet | default | n/a | n/a | 245445 | 11m46s | 1 |
