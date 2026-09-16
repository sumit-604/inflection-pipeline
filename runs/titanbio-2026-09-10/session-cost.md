# SESSION COST LEDGER — TITANBIO phase 1 (evidence)

Run: runs/titanbio-2026-09-10 | Phase 1 executed 2026-09-16

| # | stage | model | effort | in_tok | out_tok | total_tok | wall | run# |
|---|---|---|---|---|---|---|---|---|
| 0 | input validation | orchestrator | - | - | - | - | - | 1 |
| 1 | Gate 0 scorecard | sonnet | - | n/r | n/r | 188016 | 17m54s | 1 |
| 2 | Notes triple-pass, pass 1 | sonnet | - | n/r | n/r | 206658 | 8m47s | 1 |
| 2 | Notes triple-pass, pass 2 | sonnet | - | n/r | n/r | 109917 | 6m51s | 2 |
| 2 | Notes triple-pass, pass 3 | sonnet | - | n/r | n/r | 81134 | 4m39s | 3 |
| 3 | AR deep dive, 8 phases | sonnet | - | n/r | n/r | 281584 | 11m25s | 1 |
| 4 | Business model decoder | sonnet | - | n/r | n/r | 125461 | 9m05s | 1 |
| 5 | Concall analysis (NO-CONCALL MODE) | sonnet | - | n/r | n/r | 176832 | 9m03s | 1 |
| 8 | Promoter check (web) | sonnet | - | n/r | n/r | 156610 | 9m53s | 1 |
| 6 | Peer concall verification | sonnet | - | n/r | n/r | 303652 | 5m53s | 1 |
| 7 | Emerging moat scan | sonnet | - | n/r | n/r | 127498 | 7m43s | 1 |
| 9 | TAM SAM SOM (web) | sonnet | - | n/r | n/r | 119510 | 11m30s | 1 |
| 12a | Verifier A numerical | haiku | - | n/r | n/r | 118822 | 2m04s | 1 |
| 12b | Verifier B red flags | opus | - | n/r | n/r | 230239 | 11m04s | 1 |
| 12c | Verifier C framework (phase-1 scope) | opus | - | n/r | n/r | 131426 | 10m09s | 1 |
| 12d | Verifier D peer coverage | sonnet | - | n/r | n/r | 319829 | 7m07s | 1 |
| 1 | Gate 0 scorecard, CORRECTION run | sonnet | - | n/r | n/r | 87446 | 6m35s | 2 |
| 7 | Emerging moat scan, CORRECTION run | sonnet | - | n/r | n/r | 129645 | 11m33s | 2 |
| 12a | Verifier A numerical, RE-RUN with addendum | haiku | - | n/r | n/r | 138111 | 4m35s | 2 |
| 13 | Synthesis-lite (3 files) | opus | - | n/r | n/r | 130981 | 6m51s | 1 |
| 09b | Halt 1 understanding dossier | sonnet | - | n/r | n/r | 199336 | 10m57s | 1 |

## SESSION CLOSE-OUT

Run total across every subagent invocation: 3,362,707 tokens, 20 subagent runs
(15 stages plus 5 correction or re-runs).

### (a) TOP FIVE BY TOKENS

| Rank | Stage | Total tokens | Share of run |
|---|---|---|---|
| 1 | Stage 2 notes triple-pass (3 passes) | 397,709 | 11.8% |
| 2 | Verifier D peer coverage | 319,829 | 9.5% |
| 3 | Stage 6 peer concall verification | 303,652 | 9.0% |
| 4 | Stage 3 AR deep dive | 281,584 | 8.4% |
| 5 | Stage 1 Gate 0 scorecard (2 runs) | 275,462 | 8.2% |

The peer transcripts are the expensive half of this run. Stage 6 and Verifier D
together read the same eleven transcripts and cost 623,481 tokens, 18.5% of the run,
on a company that holds no calls of its own. That is the price of NO-CONCALL MODE:
the only current management voice in the corpus belongs to the peers, so it gets read
twice, once to use and once to audit.

### (b) DOWNSHIFT FAILURES

none. Verifier A ran on haiku on both passes. Stage 0 ran in the orchestrator, not as
a subagent. Stage 10 assembly does not run in phase 1.

### (c) COST SPIKES

none. No prior run folder exists for TITANBIO, so there is no ledger to compare
against. This run becomes the baseline.

Two stages ran twice and the second run is not a spike but a correction:
- Stage 1, run 2, 87,446 tokens, correcting a CRITICAL payable-days unit error.
- Stage 7, run 2, 129,645 tokens, correcting the dependent emerging-moat fields.
- Verifier A, run 2, 138,111 tokens, re-invoked with the severity and coverage
  addendum after the orchestrator found a false MAJOR in its first pass.
Correction cost for the run: 355,202 tokens, 10.6%.

### (d) OPERATOR SNAPSHOT

Keerti runs /cost and /usage now and pastes the cache hit ratio and the loop totals
below, under this heading. The orchestrator cannot read those interactive commands.

#### Operator snapshot

_(to be filled by the operator)_
