# Session cost — KUSUMGAR 2026-11-12 (Phase 1, /step1)

Per-stage token ledger. One row per subagent run, from the subagent result
metadata. n/a where the harness does not expose the figure; never an estimate.

| # | stage | model | effort | in_tok | cache_read | cache_write | out_tok | total_tok | wall | run# |
|---|---|---|---|---|---|---|---|---|---|---|
| 0 | stage-00-intake-check | claude-haiku-5-5 | medium | n/a | n/a | n/a | n/a | 84778 | 152s | 1 |
| 1 | stage-01-gate0 | claude-sonnet-5-5 | medium | n/a | n/a | n/a | n/a | 112016 | 286s | 1 |
| 2 | stage-02-notes-pass (pass 1) | claude-sonnet-5-5 | default | n/a | n/a | n/a | n/a | 232562 | 556s | 1 |
| 2 | stage-02-notes-pass (pass 2) | claude-sonnet-5-5 | default | n/a | n/a | n/a | n/a | 148383 | 362s | 1 |
| 2 | stage-02-notes-pass (pass 3) | claude-sonnet-5-5 | default | n/a | n/a | n/a | n/a | 87001 | 173s | 1 |
| 3 | stage-03-ardeep | claude-sonnet-5-5 | default | n/a | n/a | n/a | n/a | 407088 | 943s | 1 |
| 5 | stage-05-concall (no-concall mode + 1 transcript) | claude-sonnet-5-5 | default | n/a | n/a | n/a | n/a | 129853 | 229s | 1 |
| 4 | stage-04-bizmodel | claude-sonnet-5-5 | medium | n/a | n/a | n/a | n/a | 224870 | 407s | 1 |
| 8 | stage-08-promoter | claude-sonnet-5-5 | default | n/a | n/a | n/a | n/a | 237511 | 479s | 1 |
| 6 | stage-06-peers | claude-sonnet-5-5 | medium | n/a | n/a | n/a | n/a | 159000 | 236s | 1 |
| 7 | stage-07-emoat | claude-sonnet-5-5 | default | n/a | n/a | n/a | n/a | 198808 | 401s | 1 |
| 9 | stage-09-tam | claude-sonnet-5-5 | default | n/a | n/a | n/a | n/a | 172204 | 433s | 1 |
| 12a | verifier-a-numerical | claude-sonnet-5-5 | high | n/a | n/a | n/a | n/a | 442844 | 763s | 1 |
| 12a-shadow | verifier-a-shadow | claude-haiku-5-5 | high | n/a | n/a | n/a | n/a | 259439 | 642s | 1 |
| 12c | verifier-c-framework (Gate 0 + EM scope) | claude-opus-5-5 | xhigh | n/a | n/a | n/a | n/a | 161273 | 744s | 1 |
| 12d | verifier-d-peers | claude-sonnet-5-5 | medium | n/a | n/a | n/a | n/a | 41110 | 58s | 1 |
