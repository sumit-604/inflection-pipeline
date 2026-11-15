# Session cost: keltech-2026-11-15 (Phase 1)

Per-stage token ledger. The harness exposes only each subagent's total tokens and wall time. Input,
cache-read, cache-write and output splits are not exposed and are written n/a, never estimated.

| # | stage | model | effort | in_tok | cache_read | cache_write | out_tok | total_tok | wall | run# |
|---|---|---|---|---|---|---|---|---|---|---|
| S1-BCD | step1 brief, peers, cap row | claude-opus-5-5 | default | n/a | n/a | n/a | n/a | 129211 | 6m11s | 1 |
| S1-F | step1 corpus collection | claude-sonnet-5-5 | default | n/a | n/a | n/a | n/a | 157297 | 20m23s | 1 |
| 0 | stage-00-intake-check | claude-haiku-5-5 | medium | n/a | n/a | n/a | n/a | 91806 | 3m10s | 1 |
| 1 | stage-01-gate0 | claude-sonnet-5-5 | medium | n/a | n/a | n/a | n/a | 104114 | 4m48s | 1 |
| 2 | stage-02-notes-pass (pass 1) | claude-sonnet-5-5 | default | n/a | n/a | n/a | n/a | 158208 | 6m34s | 1 |
| 2 | stage-02-notes-pass (pass 2) | claude-sonnet-5-5 | default | n/a | n/a | n/a | n/a | 179403 | 6m22s | 2 |
| 2 | stage-02-notes-pass (pass 3) | claude-sonnet-5-5 | default | n/a | n/a | n/a | n/a | 93551 | 2m57s | 3 |
| 3 | stage-03-ardeep | claude-sonnet-5-5 | default | n/a | n/a | n/a | n/a | 337017 | 12m14s | 1 |
| 4 | stage-04-bizmodel | claude-sonnet-5-5 | medium | n/a | n/a | n/a | n/a | 132499 | 5m32s | 1 |
| 5 | stage-05-concall (no-concall mode) | claude-sonnet-5-5 | default | n/a | n/a | n/a | n/a | 174554 | 6m33s | 1 |
| 8 | stage-08-promoter | claude-sonnet-5-5 | default | n/a | n/a | n/a | n/a | 191749 | 8m31s | 1 |
| 9 | stage-09-tam | claude-sonnet-5-5 | default | n/a | n/a | n/a | n/a | 127303 | 5m56s | 1 |
| 7 | stage-07-emoat | claude-sonnet-5-5 | default | n/a | n/a | n/a | n/a | 123869 | 4m58s | 1 |
| 6 | stage-06-peers | claude-sonnet-5-5 | medium | n/a | n/a | n/a | n/a | 202805 | 6m36s | 1 |
| 12d | verifier-d-peers | claude-sonnet-5-5 | medium | n/a | n/a | n/a | n/a | 81575 | 2m19s | 1 |
| 12a | verifier-a-numerical (stalled, no output) | claude-sonnet-5-5 | high | n/a | n/a | n/a | n/a | n/a | stalled >10m | 1 |
| 12a | verifier-a-numerical | claude-sonnet-5-5 | high | n/a | n/a | n/a | n/a | 329096 | 8m29s | 2 |
| 12c | verifier-c-framework (stalled, no output) | claude-opus-5-5 | xhigh | n/a | n/a | n/a | n/a | n/a | stalled >10m | 1 |
| 12c | verifier-c-framework (phase-1 scope) | claude-opus-5-5 | xhigh | n/a | n/a | n/a | n/a | 158958 | 13m33s | 2 |
| 12b | verifier-b-redflags (stalled, no output) | claude-opus-5-5 | xhigh | n/a | n/a | n/a | n/a | n/a | stalled >10m | 1 |
| 12b | verifier-b-redflags | claude-opus-5-5 | xhigh | n/a | n/a | n/a | n/a | 320666 | 18m38s | 2 |
