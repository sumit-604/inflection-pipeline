# Session cost ledger — MODISONLTD 2026-09-03 (Phase 1 evidence)

Per-stage token ledger. One line per subagent run, written and committed with
its own stage. Loop/retry runs get their own line with a run counter.

| # | stage | model | effort | in_tok | out_tok | total_tok | wall | run# |
|---|-------|-------|--------|--------|---------|-----------|------|------|
| 0 | input-validation | orchestrator-opus-4-8 (inline) | - | - | - | - | - | 1 |
| 2 | notes-pass1 | claude-sonnet | - | - | - | 139801 | 7m40s | 1 |
| 1 | gate0 | claude-sonnet | - | - | - | 111941 | 11m32s | 1 |
| 2 | notes-pass2 | claude-sonnet | - | - | - | 100796 | 6m12s | 2 |
| 2 | notes-pass3 | claude-sonnet | - | - | - | 65166 | 3m15s | 3 |
| 3 | ar-deep-dive | claude-sonnet | - | - | - | 222338 | 12m18s | 1 |
| 4 | bizmodel | claude-sonnet | - | - | - | 114320 | 7m29s | 1 |
| 5 | concall-agm | claude-sonnet | - | - | - | 119204 | 7m40s | 1 |
| 8 | promoter | claude-sonnet | - | - | - | 142517 | 10m35s | 1 |
| 6 | peers | claude-sonnet | - | - | - | 216616 | 4m01s | 1 |
| 7 | emerging-moat | claude-sonnet | - | - | - | 168715 | 10m07s | 1 |
| 9 | tam-sam-som | claude-sonnet | - | - | - | 117127 | 11m33s | 1 |
| 12a | verifier-numerical | claude-haiku | - | - | - | 110862 | 3m34s | 1 |
