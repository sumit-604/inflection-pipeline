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

## REWORK COVERAGE RERUN (ordered 2026-09-09)

Run-1 reports and blocks preserved under *-run1.md, outputs/final/run1/ and
outputs/blocks/run1/. Rows below carry run# 2 (or 3 for stage 6, whose run 1
aborted). Same ledger row shape.

| # | stage | model | effort | in_tok | out_tok | total_tok | wall | run# |
|---|-------|-------|--------|--------|---------|-----------|------|------|
| 7 | emerging moat scan (rework addendum, Class D) | claude-sonnet-5 | default | n/a | n/a | 104880 | 457s | 2 |
| 6 | peer concall verification (rerun: Class C + item 5) | claude-sonnet-5 | default | n/a | n/a | 208810 | 641s | 3 |
| 5 | concall NO-CONCALL (rerun: Class B, C item 10, Class A read) | claude-sonnet-5 | default | n/a | n/a | 236342 | 815s | 2 |
| 3 | AR deep dive (rework addendum, Class A) | claude-sonnet-5 | default | n/a | n/a | 193641 | 1000s | 2 |
| 12c | verifier C framework (phase-1 scope, rerun) | claude-opus-4-8 | default | n/a | n/a | 137943 | 577s | 2 |
| 12d | verifier D peer coverage (rerun) | claude-sonnet-5 | default | n/a | n/a | 204717 | 494s | 2 |
| 2 | notes triple-pass (rework addendum, Class A + traceability) | claude-sonnet-5 | default | n/a | n/a | 229390 | 1370s | 4 |
| 6 | peer concall verification (verdict-discipline correction) | claude-sonnet-5 | default | n/a | n/a | 133610 | 700s | 4 |
| 12b | verifier B red-flags (rerun, NO-CONCALL: AR sources) | claude-opus-4-8 | default | n/a | n/a | 421040 | 1342s | 2 |
| 12a | verifier A numerical (targeted rerun) | claude-haiku-4-5 | default | n/a | n/a | 122664 | 258s | 2 |
| 13 | synthesis-lite (phase 1, rerun) | claude-opus-4-8 | default | n/a | n/a | 247423 | 1108s | 2 |

### RERUN CLOSE-OUT (2026-09-09)

Rerun subagent tokens across the rows above: ~2,240,460. Run-1 phase-1 total was ~3,439,882; cumulative for the run folder ~5,680,342.

(a) TOP FIVE BY TOKENS, rerun rows only (loop/retry summed)
1. Stage 12b verifier B red-flags = 421,040 — 18.8%
2. Stage 6 peer concall verification (2 runs: 208,810 + 133,610) = 342,420 — 15.3%
3. Stage 13 synthesis-lite = 247,423 — 11.0%
4. Stage 5 concall NO-CONCALL = 236,342 — 10.5%
5. Stage 2 notes triple-pass = 229,390 — 10.2%

(b) DOWNSHIFT FAILURES: none. Verifier A (mechanical) ran on haiku as dispatched; stage 0 and stage 10 did not run in the rerun.

(c) COST SPIKES: no prior runs/kabraextru-*/ ledger exists, so the 1.5x rule has no prior-run comparator and nothing is written to LESSONS.md. For the record, within this run folder the rerun rows exceeded 1.5x the same stage's run-1 total for: Stage 6 peer concall verification (342,420 vs run-1 168,103, 2.0x). Stage 6's excess is the verdict-discipline correction pass on top of the rerun; verifier B's second fresh read enlarged its flag universe from 30 to 52 items.

(d) OPERATOR SNAPSHOT: operator runs /cost and /usage now and pastes the cache hit ratio and loop totals under an "Operator snapshot" heading below.

Rerun notes: all five wave-1 agents completed without a rate-limit abort; stage 6 received a second small pass to relabel a single-peer VERIFIED as PARTIALLY VERIFIED after verifier D's audit; the 09b dossier was not re-issued (rework cycle still open).
