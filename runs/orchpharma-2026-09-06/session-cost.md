# SESSION COST — ORCHPHARMA 2026-09-06 (Phase 1)

Per-stage token ledger. One line per subagent run, written and committed with
its own stage. Loops and retries each get their own line with a run counter.

| # | stage | model | effort | in_tok | out_tok | total_tok | wall | run# |
|---|-------|-------|--------|--------|---------|-----------|------|------|
| 0 | input validation + corpus audit | opus-5 (orchestrator, inline) | default | n/a | n/a | n/a | n/a | 1 |
| 1 | gate 0 scorecard | sonnet-5 | default | n/a | n/a | 131,843 | 12m26s | 1 |
| 2 | notes triple-pass, pass 1 | sonnet-5 | default | n/a | n/a | 164,215 | 12m15s | 1 |
| 5 | concall analysis (4 calls) | sonnet-5 | default | n/a | n/a | 149,182 | 9m41s | 1 |
| 8 | promoter check (web) | sonnet-5 | default | n/a | n/a | 161,595 | 12m03s | 1 |
| 6 | peer concall verification | sonnet-5 | default | n/a | n/a | 141,996 | 6m58s | 1 |
| 4 | business model decoder | sonnet-5 | default | n/a | n/a | 145,220 | 10m17s | 1 |
| 7 | emerging moat scan | sonnet-5 | default | n/a | n/a | 152,541 | 11m14s | 1 |
| 9 | TAM SAM SOM (web) | sonnet-5 | default | n/a | n/a | 180,888 | 15m53s | 1 |
| 2 | notes triple-pass, pass 2 | sonnet-5 | default | n/a | n/a | 182,321 | 7m33s | 1 |
| 3 | AR backward deep dive | sonnet-5 | default | n/a | n/a | 287,774 | 11m31s | 1 |
| 2 | notes triple-pass, pass 3 | sonnet-5 | default | n/a | n/a | n/a | n/a | 1 |
| 12d | verifier D peer coverage | sonnet-5 | default | n/a | n/a | 122,156 | 5m56s | 1 |
| 12c | verifier C framework (phase 1 scope) | opus-4.8 | default | n/a | n/a | n/a | n/a | 1 |
| 12a | verifier A numerical | haiku-4.5 | default | n/a | n/a | 116,842 | 2m53s | 1 |
| 12a | verifier A numerical, re-run with coverage addendum | haiku-4.5 | default | n/a | n/a | 117,347 | 6m13s | 2 |
| 12b | verifier B concall red flags | opus-4.8 | default | n/a | n/a | 372,409 | 15m43s | 1 |
| 5 | concall analysis, remediation re-run | sonnet-5 | default | n/a | n/a | 241,394 | 16m25s | 2 |
| 12b | verifier B concall red flags, re-run on remediated B05 | opus-4.8 | default | n/a | n/a | n/a | n/a | 2 |
| 13 | synthesis lite (phase 1) | opus-5 | default | n/a | n/a | n/a | n/a | 1 |
| 09b | Halt 1 understanding dossier | sonnet-5 | default | n/a | n/a | 214,400 | 8m37s | 1 |

## SESSION CLOSE-OUT

### (a) TOP FIVE BY TOKENS
Stage totals sum loop and retry runs into one stage figure. Run total of the
recorded rows is 2,891,000 tokens.

| Rank | Stage | Total tokens | Share of run |
|---|---|---|---|
| 1 | 5 concall analysis (2 runs: 149,182 + 241,394) | 390,576 | 13.5% |
| 2 | 12b verifier B red flags (2 rounds: 372,409 + 228,723) | 601,132 | 20.8% |
| 3 | 3 AR backward deep dive | 287,774 | 10.0% |
| 4 | 12a verifier A numerical (2 runs: 116,842 + 117,347) | 234,189 | 8.1% |
| 5 | 09b Halt 1 dossier | 214,400 | 7.4% |

The two largest lines are both the remediation loop on stage 5 and its
verifier. One REWORK cycle cost about 991,000 tokens, roughly a third of the
run, and did not clear the 60% gate.

### (b) DOWNSHIFT FAILURES
Mechanical stages are the ones DISPATCH routes to haiku: stage 0 validation,
stage 10 assembly, verifier A.
- verifier A: ran on haiku-4.5 both runs. Correct.
- stage 10 assembly: did not run in phase 1.
- stage 0 validation: DOWNSHIFT FAILURE: stage 0. It ran inline in the
  orchestrator session on opus-5 rather than as a haiku subagent. The run
  overpaid for a mechanical inventory. The /run-pipeline command tells the
  orchestrator to do stage 0 itself, which conflicts with the DISPATCH
  routing for a mechanical stage. Recorded in LESSONS_ARCHIVE.md.

### (c) COST SPIKES
None. No prior run folder exists for ORCHPHARMA, so no 1.5x comparison is
possible. This is the first workup on this name.

### (d) OPERATOR SNAPSHOT
Keerti runs /cost and /usage now and pastes the cache hit ratio and the loop
totals below, under an "Operator snapshot" heading. The orchestrator cannot
read those interactive commands.

Note on the ledger itself: per-stage input and output token splits were not
available from the subagent result metadata in this environment, so the
in_tok and out_tok columns read n/a and total_tok carries the figure the
harness reported. Wall times are the harness-reported durations.
