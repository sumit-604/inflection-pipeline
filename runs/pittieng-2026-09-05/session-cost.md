# Session cost ledger — pittieng-2026-09-05 (phase 1)

Per-stage token ledger. One line per subagent run. Token counts are taken
from the Agent tool result metadata where the harness reports them; "n/a"
where it does not.

| # | stage | model | effort | in_tok | out_tok | total_tok | wall | run# |
|---|-------|-------|--------|--------|---------|-----------|------|------|
| 0 | input validation + corpus audit | orchestrator (claude-fable-5-1) | n/a | n/a | n/a | n/a | ~12m | 1 |
| 2 | notes triple-pass (pass 1) | claude-sonnet | default | n/a | n/a | 283170 | 8m31s | 1 |
| 2 | notes triple-pass (pass 2) | claude-sonnet | default | n/a | n/a | 148436 | 8m57s | 2 |
