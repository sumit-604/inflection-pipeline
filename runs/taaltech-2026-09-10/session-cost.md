# SESSION COST LEDGER — TAALTECH 2026-09-10 (Phase 1, /step1 intake)

Per-stage token ledger. One line per subagent run, written and committed with
its own stage. Loops and retries each get their own line with a run counter.

| # | stage | model | effort | in_tok | out_tok | total_tok | wall | run# |
|---|-------|-------|--------|--------|---------|-----------|------|------|
| pre | corpus: transcribe scanned results filings | sonnet | default | - | - | 150,132 | 182s | 1 |
| 0 | input validation (orchestrator inline) | opus (orchestrator) | default | - | - | - | - | 1 |
