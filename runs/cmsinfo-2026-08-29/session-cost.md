# Session Cost Ledger — CMSINFO 2026-08-29 (Phase 1)

Per-stage token ledger. One line per subagent run (loops/retries get their own line).

| # | stage | model | effort | in_tok | out_tok | total_tok | wall | run# |
|---|-------|-------|--------|--------|---------|-----------|------|------|
| 0 | input-validation (orchestrator inline) | - | - | - | - | - | - | 1 |
| 1 | gate-0-scorecard | claude-sonnet-5 | default | - | - | 118039 | 9m35s | 1 |
| 2 | notes-triple-pass (pass1 full extraction) | claude-sonnet-5 | default | - | - | 148582 | 8m10s | 1 |
| 2 | notes-triple-pass (pass2 what-missed) | claude-sonnet-5 | default | - | - | 117075 | 6m33s | 2 |
| 2 | notes-triple-pass (pass3 consolidate B02) | claude-sonnet-5 | default | - | - | 62131 | 3m22s | 3 |
| 3 | ar-deep-dive (8 phases) | claude-sonnet-5 | default | - | - | 263567 | 14m25s | 1 |
| 4 | business-model-decoder | claude-sonnet-5 | default | - | - | 143169 | 8m59s | 1 |
| 5 | concall-analysis (4 transcripts) | claude-sonnet-5 | default | - | - | 152721 | 7m08s | 1 |
| 8 | promoter-check (web) | claude-sonnet-5 | default | - | - | 102618 | 5m31s | 1 |
| 6 | peer-concall-verification | claude-sonnet-5 | default | - | - | 225250 | 7m26s | 1 |
| 7 | emerging-moat-scan | claude-sonnet-5 | default | - | - | 158496 | 8m43s | 1 |
