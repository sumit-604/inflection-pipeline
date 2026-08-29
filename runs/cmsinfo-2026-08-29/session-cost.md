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
| 9 | tam-sam-som (web) | claude-sonnet-5 | default | - | - | 125559 | 11m16s | 1 |
| 12a | verifier-a-numerical | claude-haiku-4-5 | default | - | - | 95128 | 2m29s | 1 |
| 12b | verifier-b-redflags | claude-opus-4-8 | default | - | - | 163223 | 5m10s | 1 |
| 12c | verifier-c-framework (phase-1 scope) | claude-opus-4-8 | default | - | - | 80019 | 4m51s | 1 |
| 12d | verifier-d-peers | claude-sonnet-5 | default | - | - | 127988 | 6m14s | 1 |
| 13 | synthesis-lite (phase-1, 3 files) | claude-opus-4-8 | default | - | - | 109455 | 6m34s | 1 |
| 09b | halt1-dossier | claude-sonnet-5 | default | - | - | 176200 | 8m33s | 1 |

---
## SESSION CLOSE-OUT (phase 1)

Run total (subagent tokens, all rows): ~2,369,220 tokens across 17 subagent runs
(stage 2 = 3 runs). Orchestrator stage-0 validation ran inline (no subagent).

### (a) TOP FIVE BY TOKENS
| rank | stage | total_tok | share of run |
|------|-------|-----------|--------------|
| 1 | stage 2 notes-triple-pass (3 runs summed) | 327,788 | 13.8% |
| 2 | stage 3 AR deep dive | 263,567 | 11.1% |
| 3 | stage 6 peer-concall verification | 225,250 | 9.5% |
| 4 | stage 09b halt-1 dossier | 176,200 | 7.4% |
| 5 | verifier B redflags (opus) | 163,223 | 6.9% |

### (b) DOWNSHIFT FAILURES
none. The mechanical stages that DISPATCH routes to haiku ran on haiku: verifier A
on claude-haiku-4-5. Stage 0 validation and stage 10 assembly are the other
mechanical stages; stage 0 ran orchestrator-inline (no subagent, no model spend),
stage 10 is phase-3, not run here. No mechanical stage ran on Opus.

### (c) COST SPIKES
none. This is the first CMSINFO run; no prior runs/cmsinfo-*/session-cost.md ledger
exists to compare against the 1.5x threshold.

### (d) OPERATOR SNAPSHOT
Operator: run /cost and /usage now and paste the cache hit ratio and the loop
totals below. The orchestrator cannot read those interactive commands.

#### Operator snapshot
(cache hit ratio + loop totals — operator fills)
