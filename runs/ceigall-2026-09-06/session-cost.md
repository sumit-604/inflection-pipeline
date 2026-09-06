# SESSION COST — CEIGALL 2026-09-06 (phase 1, evidence)

Per-stage token ledger. One line per subagent run, written and committed
with its own stage. A stage that loops or retries gets one line per run.

| # | stage | model | effort | in_tok | out_tok | total_tok | wall | run# |
|---|-------|-------|--------|--------|---------|-----------|------|------|
| 0 | input validation | orchestrator (opus) | — | — | — | — | ~25m | 1 |
| 1 | gate 0 scorecard | claude-sonnet-5 | default | — | — | 54,376 | 5m06s | 1 |
| 2 | notes triple-pass (pass 1) | claude-sonnet-5 | default | — | — | 138,673 | 8m55s | 1 |
| 2 | notes triple-pass (pass 2) | claude-sonnet-5 | default | — | — | 140,165 | 11m03s | 2 |
| 2 | notes triple-pass (pass 3, final) | claude-sonnet-5 | default | — | — | 133,457 | 5m09s | 3 |
| 3 | AR deep dive (8 phases) | claude-sonnet-5 | default | — | — | 233,649 | 13m19s | 1 |
| 4 | business model decoder | claude-sonnet-5 | default | — | — | 131,038 | 7m02s | 1 |
| 5 | concall analysis (3 transcripts) | claude-sonnet-5 | default | — | — | 126,037 | 7m11s | 1 |
| 8 | promoter check (web) | claude-sonnet-5 | default | — | — | 143,350 | 10m33s | 1 |
| 6 | peer concall verification | claude-sonnet-5 | default | — | — | 166,182 | 10m43s | 1 |
| 7 | emerging moat 22-cat scan | claude-sonnet-5 | default | — | — | 239,049 | 9m46s | 1 |
| 9 | TAM/SAM/SOM (web) | claude-sonnet-5 | default | — | — | 142,716 | 10m41s | 1 |
| 12a | verifier A numerical | claude-haiku-4-5 | default | — | — | 101,771 | 3m11s | 1 |
| 12c | verifier C framework (phase 1) | claude-opus-4-8 | default | — | — | 101,498 | 7m31s | 1 |

Stage 0 ran in the orchestrator session, not as a subagent, so it has no
subagent metadata. Its wall time is dominated by a rejected OCR attempt on
the scanned annual report (see outputs/reports/00-input-validation.md 4.1).
