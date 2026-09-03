# Session cost ledger — MODISONLTD 2026-09-03 (Phase 1 evidence)

Per-stage token ledger. One line per subagent run, written and committed with
its own stage. Loop/retry runs get their own line with a run counter.

| # | stage | model | effort | in_tok | out_tok | total_tok | wall | run# |
|---|-------|-------|--------|--------|---------|-----------|------|------|
| 0 | input-validation | orchestrator-opus-4-8 (inline) | - | - | - | - | - | 1 |
| 2 | notes-pass1 | claude-sonnet | - | - | - | 139801 | 7m40s | 1 |
| 1 | gate0 | claude-sonnet | - | - | - | 111941 | 11m32s | 1 |
