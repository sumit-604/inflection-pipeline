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
| 09b | halt1-dossier | sonnet | default | n/a | n/a | 104032 | 253s | 1 |

## SESSION CLOSE-OUT (Phase 1)

Run total (sum of every ledger row with a token count): ~1,885,264 tokens across 15 subagent runs (stage 0 is orchestrator-inline, no token metadata).

### (a) TOP FIVE BY TOKENS
Loop/retry runs summed into one stage total for the ranking.

| rank | stage | total_tok | share of run |
|------|-------|-----------|--------------|
| 1 | 2 notes triple-pass (pass1+2+3) | 377,701 | 20.0% |
| 2 | 12a verifier A (run1+run2) | 185,966 | 9.9% |
| 3 | 3 AR deep dive | 179,604 | 9.5% |
| 4 | 12b verifier B | 149,248 | 7.9% |
| 5 | 5 concall analysis | 130,916 | 6.9% |

### (b) DOWNSHIFT FAILURES
none. Verifier A ran on haiku (claude-haiku-4-5) on both runs. Stage-0
validation is orchestrator-inline by design (the run-pipeline command says
"stage 0, do this yourself"), not a dispatched haiku subagent, so DISPATCH's
haiku routing does not apply to it. Stage 10 assembly is a Phase 3 stage and
did not run here.

### (c) COST SPIKES
none. No prior run folder exists for DIFFNKG, so there is no previous ledger
to compare against the 1.5x threshold.

### (d) OPERATOR SNAPSHOT
Operator: run /cost and /usage now and paste the cache hit ratio and the loop
totals below under "Operator snapshot". The orchestrator cannot read those
interactive commands.

#### Operator snapshot
(to be filled by operator)
