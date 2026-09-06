# SESSION COST — CEIGALL 2026-09-06 (phase 1, evidence)

Per-stage token ledger. One line per subagent run, written and committed
with its own stage. A stage that loops or retries gets one line per run.

| # | stage | model | effort | in_tok | out_tok | total_tok | wall | run# |
|---|-------|-------|--------|--------|---------|-----------|------|------|
| 0 | input validation | orchestrator (opus) | — | — | — | — | ~25m | 1 |

Stage 0 ran in the orchestrator session, not as a subagent, so it has no
subagent metadata. Its wall time is dominated by a rejected OCR attempt on
the scanned annual report (see outputs/reports/00-input-validation.md 4.1).
