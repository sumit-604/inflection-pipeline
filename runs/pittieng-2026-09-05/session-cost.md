# Session cost ledger — pittieng-2026-09-05 (phase 1)

Per-stage token ledger. One line per subagent run. Token counts are taken
from the Agent tool result metadata where the harness reports them; "n/a"
where it does not.

| # | stage | model | effort | in_tok | out_tok | total_tok | wall | run# |
|---|-------|-------|--------|--------|---------|-----------|------|------|
| 0 | input validation + corpus audit | orchestrator (claude-fable-5-1) | n/a | n/a | n/a | n/a | ~12m | 1 |
| 2 | notes triple-pass (pass 1) | claude-sonnet | default | n/a | n/a | 283170 | 8m31s | 1 |
| 2 | notes triple-pass (pass 2) | claude-sonnet | default | n/a | n/a | 148436 | 8m57s | 2 |
| 1 | gate 0 scorecard | claude-sonnet | default | n/a | n/a | 180950 | 18m33s | 1 |
| 2 | notes triple-pass (pass 3, consolidation + B02) | claude-sonnet | default | n/a | n/a | 80693 | 5m22s | 3 |
| 3 | AR deep dive | claude-sonnet | default | n/a | n/a | 369769 | 13m07s | 1 |
| 4 | business model decoder | claude-sonnet | default | n/a | n/a | 170183 | 11m11s | 1 |
| 8 | promoter check (web, partial: 2 fetches proxy-blocked) | claude-sonnet | default | n/a | n/a | 245445 | 11m46s | 1 |
| 5 | concall analysis | claude-sonnet | default | n/a | n/a | 163199 | 14m26s | 1 |
| 6 | peer concall verification | claude-sonnet | default | n/a | n/a | 361695 | 9m41s | 1 |
| 7 | emerging moat scan (report + B07 block complete on disk; agent cut by API 429 while returning, so token metadata lost) | claude-sonnet | default | n/a | n/a | n/a | n/a | 1 |
| 12b | verifier B red flags (FAILED: API 429 session limit after independent read) | claude-opus | default | n/a | n/a | n/a | n/a | 1 |
| 12d | verifier D peer coverage (FAILED: API 429 session limit at launch) | claude-sonnet | default | n/a | n/a | n/a | n/a | 1 |
| 12d | verifier D peer coverage (retry) | claude-sonnet | default | n/a | n/a | 326482 | 6m04s | 2 |
| 12c | verifier C framework (phase-1 scope: Gate 0 + EM only) | claude-opus | default | n/a | n/a | 131382 | 10m37s | 1 |
| 12b | verifier B red flags (retry) | claude-opus | default | n/a | n/a | 386274 | 17m12s | 2 |
| 9 | TAM SAM SOM (web) | claude-sonnet | default | n/a | n/a | 182856 | 14m17s | 1 |
| 12a | verifier A numerical (pass 1: Gate 0 figures, 29 numbers) | claude-haiku | default | n/a | n/a | 96035 | 3m07s | 1 |
| 12a | verifier A numerical (pass 2: coverage extension to 02/03/05/07, cumulative 52 numbers) | claude-haiku | default | n/a | n/a | 121991 | 3m53s | 2 |
| 13 | synthesis-lite (phase 1: 3 files) | claude-opus | default | n/a | n/a | 148149 | 9m11s | 1 |
| 9b | Halt 1 understanding dossier + Section 6 annex | claude-sonnet | default | n/a | n/a | 299624 | 17m12s | 1 |

## Summary block (close-out)

Run total (sum of every ledger row with a token figure): 3,696,333 tokens. Rows without token metadata (stage 0 inline; stage 7, whose agent was cut by an API 429 after writing its report) are excluded from the sum and the ranking.

### (a) TOP FIVE BY TOKENS (loop/retry runs summed per stage)

| rank | stage | model | total_tok | share |
|---|---|---|---|---|
| 1 | 2 notes triple-pass | claude-sonnet | 512,299 | 13.9% |
| 2 | 12b verifier B red flags | claude-opus | 386,274 | 10.5% |
| 3 | 3 AR deep dive | claude-sonnet | 369,769 | 10.0% |
| 4 | 6 peer concall verification | claude-sonnet | 361,695 | 9.8% |
| 5 | 12d verifier D peer coverage | claude-sonnet | 326,482 | 8.8% |

### (b) DOWNSHIFT FAILURES

none. Verifier A (12a) ran on claude-haiku (both passes). Stage 10 does not run in phase 1. Stage 0 validation ran inline in the orchestrator session (claude-fable-5-1) per the run-pipeline command's "do this yourself" instruction; no haiku subagent exists for it, so it is not a downshift failure, but it is not a haiku run either.

### (c) COST SPIKES

none. No prior runs/pittieng-*/session-cost.md exists (first run for this ticker).

### (d) OPERATOR SNAPSHOT

Operator: run /cost and /usage now and paste the cache hit ratio and the loop totals under the heading below.

## Operator snapshot

(to be filled by the operator)
