# Session Cost Ledger — DIFFNKG 2026-09-05 (Phase 1)

Per-stage token ledger. One row per subagent run. Summary block appended at close-out.

| # | stage | model | effort | in_tok | out_tok | total_tok | wall | run# |
|---|-------|-------|--------|--------|---------|-----------|------|------|
| 0 | input-validation | inline-orch | n/a | n/a | n/a | n/a | n/a | 1 |
| 1 | gate0-scorecard | sonnet | default | n/a | n/a | 61075 | 317s | 1 |
| 2 | notes-triple-pass (pass1) | sonnet | default | n/a | n/a | 167372 | 291s | 1 |
| 2 | notes-triple-pass (pass2) | sonnet | default | n/a | n/a | 157280 | 150s | 2 |
| 2 | notes-triple-pass (pass3-close) | sonnet | default | n/a | n/a | 53049 | 129s | 3 |
| 7 | emerging-moat-scan | sonnet | default | n/a | n/a | 95447 | 323s | 1 |
| 3 | ar-deep-dive | sonnet | default | n/a | n/a | 179604 | 649s | 1 |
