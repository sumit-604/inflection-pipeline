# SESSION COST LEDGER — SYNGENE 2026-09-15 (phase 1, via /step1)

| # | stage | model | effort | in_tok | out_tok | total_tok | wall | run# |
|---|---|---|---|---|---|---|---|---|
| 0 | step1 intake (identity, brief, peers, corpus repair) + input validation | orchestrator (opus, inline) | n/a | n/a | n/a | n/a | ~75m | 1 |
| 1 | gate 0 scorecard | claude-sonnet-5 | default | n/a | n/a | 134317 | 10m07s | 1 |
| 2 | notes triple-pass, pass 1 | claude-sonnet-5 | default | n/a | n/a | 193887 | 8m35s | 1 |
| 2 | notes triple-pass, pass 2 | claude-sonnet-5 | default | n/a | n/a | 103205 | 5m49s | 2 |
| 2 | notes triple-pass, pass 3 (VOID: shared working copy switched to branch prompt-audit-fixes by another session at 07:00:18 IST; inputs absent during the pass; output discarded) | claude-sonnet-5 | default | n/a | n/a | 104402 | 7m44s | 3 |
| 2 | notes triple-pass, pass 3 (consolidated, re-run in worktree) | claude-sonnet-5 | default | n/a | n/a | 81907 | 3m58s | 4 |
| 3 | AR backward deep dive (8 phases) | claude-sonnet-5 | default | n/a | n/a | 268914 | 13m36s | 1 |
| 4 | business model decoder | claude-sonnet-5 | default | n/a | n/a | 159864 | 6m15s | 1 |
| 5 | concall analysis (4 transcripts) | claude-sonnet-5 | default | n/a | n/a | 155072 | 8m17s | 1 |
| 8 | promoter background check (web) | claude-sonnet-5 | default | n/a | n/a | 235906 | 9m02s | 1 |
| 6 | peer concall verification (6 transcripts) | claude-sonnet-5 | default | n/a | n/a | 184349 | 5m36s | 1 |
| 7 | emerging moat scan (22 categories) | claude-sonnet-5 | default | n/a | n/a | 148077 | 9m57s | 1 |
| 9 | TAM SAM SOM market sizing (web) | claude-sonnet-5 | default | n/a | n/a | 169656 | 14m38s | 1 |
| 12a | verifier A numerical | claude-haiku-4-5 | default | n/a | n/a | 80190 | 3m53s | 1 |
| 12b | verifier B red flags | claude-opus (frontmatter) | default | n/a | n/a | 315616 | 12m33s | 1 |
| 12d | verifier D peer coverage | claude-sonnet-5 | default | n/a | n/a | 137859 | 7m29s | 1 |
| 12c | verifier C framework (phase-1 scope) | claude-opus (frontmatter) | default | n/a | n/a | 125408 | 8m53s | 1 |
| 1 | gate 0 scorecard (verifier corrections) | claude-sonnet-5 | default | n/a | n/a | 104662 | 6m33s | 2 |
| 5 | concall analysis (verifier corrections) | claude-sonnet-5 | default | n/a | n/a | 185460 | 10m16s | 2 |
| 6 | peer concall verification (verifier corrections) | claude-sonnet-5 | default | n/a | n/a | 261848 | 12m12s | 2 |
| 7 | emerging moat scan (verifier corrections) | claude-sonnet-5 | default | n/a | n/a | 245708 | 18m17s | 2 |
| 12a | verifier A numerical (run 2, severity addendum) | claude-haiku-4-5 | default | n/a | n/a | 100853 | 4m17s | 2 |
| 12c | verifier C framework (phase-1 scope, run 2) | claude-opus (frontmatter) | default | n/a | n/a | 143828 | 8m29s | 2 |
| 12b | verifier B red flags (run 2) | claude-opus (frontmatter) | default | n/a | n/a | 346691 | 14m04s | 2 |
| 12d | verifier D peer coverage (run 2) | claude-sonnet-5 | default | n/a | n/a | 209704 | 4m19s | 2 |
| 13 | synthesis-lite (phase 1, three files) | claude-opus (frontmatter) | default | n/a | n/a | 205997 | 11m24s | 1 |
| 9b | Halt 1 understanding dossier | claude-sonnet-5 | default | n/a | n/a | 176696 | 9m46s | 1 |

## SESSION CLOSE-OUT — SYNGENE 2026-09-15, phase 1 (via /step1)

Run total across every subagent invocation: **4,580,076 tokens** over 28 subagent
runs. Stage 0 and the Step-1 intake ran inline on the orchestrator and are not counted.

### (a) TOP FIVE BY TOKENS

| # | Stage | Total tokens | Share of run | Runs |
|---|---|---|---|---|
| 1 | Verifier B, concall red flags | 662,307 | 14.5% | 2 |
| 2 | Stage 2, notes triple-pass | 483,401 | 10.6% | 4 (incl. 1 void) |
| 3 | Stage 6, peer concall verification | 446,197 | 9.7% | 2 |
| 4 | Stage 7, emerging moat scan | 393,785 | 8.6% | 2 |
| 5 | Verifier D, peer coverage | 347,563 | 7.6% | 2 |

The top five are 51.0% of the run. One correction cycle (stages 1, 5, 6, 7 and all
four verifiers re-run) accounts for most of the second-run tokens. Stage 2 pass 3
run 3 (104,402 tokens) was voided: another session switched the shared working copy
to branch prompt-audit-fixes at 07:00:18 IST while it ran. The run then moved to its
own worktree (.claude/worktrees/syngene) and pass 3 re-ran there.

### (b) DOWNSHIFT FAILURES

none. Verifier A ran on claude-haiku-4-5 in both runs. Stage 10 does not run in
phase 1. Stage 0 ran inline in the orchestrator session, as run-pipeline.md step 1
directs (same treatment as TOTEM 2026-09-09).

### (c) COST SPIKES

none. No prior runs/syngene-* ledger exists.

### (d) OPERATOR SNAPSHOT

Operator: run /cost and /usage now and paste the cache hit ratio and the loop totals
below under "Operator snapshot". The orchestrator cannot read those commands.

### Operator snapshot

(pending)
