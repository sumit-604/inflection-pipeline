# CLEANMAX 2026-09-01 — Phase 1 session cost ledger

Per-stage token ledger. One row per subagent run.

| # | stage | model | effort | in_tok | out_tok | total_tok | wall | run# |
|---|-------|-------|--------|--------|---------|-----------|------|------|
| 1 | stage-01-gate0 | sonnet | n/a | n/a | n/a | 147214 | 9m51s | 1 |
| 2 | stage-02-notes (pass 1) | sonnet | n/a | n/a | n/a | 237015 | 9m40s | 1 |
| 3 | stage-02-notes (pass 2) | sonnet | n/a | n/a | n/a | 143529 | 8m40s | 2 |
| 4 | stage-02-notes (pass 3) | sonnet | n/a | n/a | n/a | 77227 | 4m24s | 3 |
| 5 | stage-03-ardeep | sonnet | n/a | n/a | n/a | 215917 | 14m41s | 1 |
| 6 | stage-04-bizmodel | sonnet | n/a | n/a | n/a | 129577 | 7m47s | 1 |
| 7 | stage-05-concall | sonnet | n/a | n/a | n/a | 153617 | 8m28s | 1 |
| 8 | stage-08-promoter | sonnet | n/a | n/a | n/a | 161347 | 9m50s | 1 |
| 9 | stage-06-peers | sonnet | n/a | n/a | n/a | 161767 | 7m18s | 1 |
| 10 | stage-07-emoat | sonnet | n/a | n/a | n/a | 206729 | 8m01s | 1 |
| 11 | stage-09-tam | sonnet | n/a | n/a | n/a | 95863 | 9m04s | 1 |
| 12 | verifier-a-numerical | haiku | n/a | n/a | n/a | 85956 | 2m35s | 1 |
| 13 | verifier-c-framework | opus | n/a | n/a | n/a | 82639 | 4m20s | 1 |
| 14 | verifier-d-peers | sonnet | n/a | n/a | n/a | 99766 | 5m11s | 1 |
| 15 | verifier-b-redflags | opus | n/a | n/a | n/a | 159673 | 6m08s | 1 |
| 16 | stage-13-synthesis (lite) | opus | n/a | n/a | n/a | 100486 | 5m41s | 1 |
| 17 | stage-09b-dossier | sonnet | n/a | n/a | n/a | 161159 | 9m50s | 1 |

## SESSION CLOSE-OUT (phase 1)

Run total (sum of all 17 ledger rows): 2,419,481 subagent tokens. Stage 0
validation and the confidence-delta computation were done by the orchestrator
itself (not billed as subagents). Only aggregate subagent_tokens are exposed
per run; in/out split is not available, so those columns read n/a.

**(a) TOP FIVE BY TOKENS** (stage-02 loop summed into one stage):
1. stage-02-notes (3 passes)   457,771   18.9%
2. stage-03-ardeep             215,917    8.9%
3. stage-07-emoat              206,729    8.5%
4. stage-06-peers              161,767    6.7%
5. stage-08-promoter           161,347    6.7%
(stage-09b-dossier 161,159 and verifier-b 159,673 are the next two.)

**(b) DOWNSHIFT FAILURES:** none. The only MECHANICAL stage that runs as a
subagent in phase 1 is verifier-a-numerical; it ran on haiku as routed. Stage 0
validation was performed by the orchestrator directly; stage 10 assembly is a
phase-3 stage and did not run here.

**(c) COST SPIKES:** none. No prior runs/cleanmax-* session-cost.md ledger
exists (first run for this ticker), so there is no 1.5x baseline to cross.

**(d) OPERATOR SNAPSHOT:** the orchestrator cannot read the interactive /cost
and /usage commands. Operator: run /cost and /usage now and paste the cache-hit
ratio and the loop totals below under this heading.

### Operator snapshot
(to be filled by the operator from /cost and /usage)

(Only aggregate subagent_tokens are exposed per run; in/out split shown n/a.)
