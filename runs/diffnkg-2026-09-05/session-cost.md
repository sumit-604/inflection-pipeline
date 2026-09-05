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
| 4 | business-model | sonnet | default | n/a | n/a | 103833 | 254s | 1 |
| 5 | concall-analysis | sonnet | default | n/a | n/a | 130916 | 420s | 1 |
| 8 | promoter-check | sonnet | default | n/a | n/a | 101121 | 315s | 1 |
| 9 | tam-sam-som | sonnet | default | n/a | n/a | 83282 | 357s | 1 |
| 6 | peer-verification | sonnet | default | n/a | n/a | 77665 | 196s | 1 |
| 12d | verifier-d-peers | sonnet | default | n/a | n/a | 68720 | 162s | 1 |
| 12a | verifier-a-numerical | haiku | default | n/a | n/a | 97723 | 225s | 1 |
| 12c | verifier-c-framework | opus | default | n/a | n/a | 81902 | 241s | 1 |
| 12b | verifier-b-redflags | opus | default | n/a | n/a | 149248 | 294s | 1 |
| 12a | verifier-a-numerical | haiku | default | n/a | n/a | 88243 | 181s | 2 |
| 13 | synthesis-lite | opus | default | n/a | n/a | 84752 | 263s | 1 |
