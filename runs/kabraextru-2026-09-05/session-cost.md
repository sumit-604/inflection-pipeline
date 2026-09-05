# Session cost ledger — KABRAEXTRU 2026-09-05 (Phase 1)

Per-stage token ledger. One row per subagent run. Stage 0 is orchestrator-inline
(no subagent metadata). Model/effort/tokens from each subagent's result metadata.

| # | stage | model | effort | in_tok | out_tok | total_tok | wall | run# |
|---|-------|-------|--------|--------|---------|-----------|------|------|
| 0 | input validation | orchestrator-inline (fable) | n/a | n/a | n/a | n/a | n/a | 1 |
| 8 | promoter check | claude-sonnet-5 | default | n/a | n/a | 178598 | 830s | 1 |
| 2 | notes triple-pass (pass 1) | claude-sonnet-5 | default | n/a | n/a | 229345 | 791s | 1 |
| 1 | gate 0 scorecard | claude-sonnet-5 | default | n/a | n/a | 171467 | 1031s | 1 |
| 2 | notes triple-pass (pass 2) | claude-sonnet-5 | default | n/a | n/a | 180031 | 823s | 2 |
| 7 | emerging moat scan | claude-sonnet-5 | default | n/a | n/a | 243831 | 973s | 1 |
| 2 | notes triple-pass (pass 3 + consolidation) | claude-sonnet-5 | default | n/a | n/a | 116854 | 457s | 3 |
| 3 | AR deep dive (8 phases) | claude-sonnet-5 | default | n/a | n/a | 305649 | 730s | 1 |
| 5 | concall (NO-CONCALL: AR guidance vs delivery) | claude-sonnet-5 | default | n/a | n/a | 185340 | 792s | 1 |
| 4 | business model decoder | claude-sonnet-5 | default | n/a | n/a | 172321 | 955s | 1 |
| 6 | peer concall verification (FAILED: API 429 session rate limit, aborted mid-read, no report written) | claude-sonnet-5 | default | n/a | n/a | n/a | n/a | 1 |
| 6 | peer concall verification | claude-sonnet-5 | default | n/a | n/a | 168103 | 553s | 2 |
| 12c | verifier C framework (phase-1 scope) | claude-opus-4-8 | default | n/a | n/a | 130352 | 562s | 1 |
| 12d | verifier D peer coverage | claude-sonnet-5 | default | n/a | n/a | 185059 | 475s | 1 |
| 9 | TAM/SAM/SOM sizing | claude-sonnet-5 | default | n/a | n/a | 193951 | 1197s | 1 |
| 12b | verifier B red-flags (NO-CONCALL: AR sources) | claude-opus-4-8 | default | n/a | n/a | 362059 | 944s | 1 |
| 12a | verifier A numerical | claude-haiku-4-5 | default | n/a | n/a | 120887 | 263s | 1 |
| 13 | synthesis-lite (phase 1) | claude-opus-4-8 | default | n/a | n/a | 192948 | 855s | 1 |
| 09b | Halt 1 dossier | claude-sonnet-5 | default | n/a | n/a | 303087 | 1074s | 1 |

## PHASE 1 CLOSE-OUT

Total subagent tokens across all rows: ~3,439,882 (stage 0 orchestrator-inline, no metadata; stage 6 run 1 aborted on a 429 rate limit with no usage returned).

### (a) TOP FIVE BY TOKENS (stage totals, loop/retry summed)
1. Stage 2 notes triple-pass (3 runs: 229,345 + 180,031 + 116,854) = 526,230 — 15.3%
2. Stage 12b verifier B red-flags = 362,059 — 10.5%
3. Stage 3 AR deep dive = 305,649 — 8.9%
4. Stage 09b Halt 1 dossier = 303,087 — 8.8%
5. Stage 7 emerging moat scan = 243,831 — 7.1%

### (b) DOWNSHIFT FAILURES
none. Verifier A (mechanical) ran on haiku as dispatched. Stage 0 validation is
orchestrator-inline by design per run-pipeline "do this yourself", not a
dispatched subagent. Stage 10 assembly does not run in phase 1.

### (c) COST SPIKES
none. No prior runs/kabraextru-*/ ledger exists (first KABRAEXTRU run); nothing
to compare against 1.5x.

### (d) OPERATOR SNAPSHOT
Operator: run /cost and /usage now and paste the cache hit ratio and loop totals
under an "Operator snapshot" heading below. The orchestrator cannot read those
interactive commands.

### Run notes
- Stage 6 run 1 aborted on an API 429 session rate limit (reset 17:30 UTC); run 2
  completed clean after the reset. Aborted draft kept as
  outputs/reports/06-peers-run1-aborted.md for the record.
- Stages 8 and 9 status partial: WebSearch worked, WebFetch to sebi.gov.in,
  crisil.com, bseindia.com and research-report hosts was egress-blocked.
