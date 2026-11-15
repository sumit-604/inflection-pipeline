# Session cost ledger: kpl-2026-11-15 (Phase 1)

Token columns: the harness exposes one total per subagent run (subagent_tokens), tool uses and wall time. The in / cache_read / cache_write / out split is not exposed, so those cells are n/a, never an estimate.

| # | stage | model | effort | in_tok | cache_read | cache_write | out_tok | total_tok | wall | run# |
|---|-------|-------|--------|--------|------------|-------------|---------|-----------|------|------|
| pre | step1 B/C/D brief (general-purpose) | claude-opus-5-5 | default | n/a | n/a | n/a | n/a | 134250 | 473s | 1 |
| pre | step1 F corpus (general-purpose) | claude-sonnet-5-5 | default | n/a | n/a | n/a | n/a | 147234 | 576s | 1 |
| 0 | stage-00-intake-check | claude-haiku-5-5 | medium | n/a | n/a | n/a | n/a | 87149 | 178s | 1 |
| 1 | stage-01-gate0 | claude-sonnet-5-5 | medium | n/a | n/a | n/a | n/a | 75888 | 203s | 1 |
| 2 | stage-02-notes-pass (pass 1) | claude-sonnet-5-5 | high | n/a | n/a | n/a | n/a | 184862 | 410s | 1 |
| 2 | stage-02-notes-pass (pass 2) | claude-sonnet-5-5 | high | n/a | n/a | n/a | n/a | 183402 | 526s | 2 |
| 2 | stage-02-notes-pass (pass 3) | claude-sonnet-5-5 | high | n/a | n/a | n/a | n/a | 79260 | 115s | 3 |
| 3 | stage-03-ardeep | claude-sonnet-5-5 | high | n/a | n/a | n/a | n/a | 355490 | 965s | 1 |
| 4 | stage-04-bizmodel | claude-sonnet-5-5 | medium | n/a | n/a | n/a | n/a | 129960 | 317s | 1 |
| 8 | stage-08-promoter | claude-sonnet-5-5 | high | n/a | n/a | n/a | n/a | 191139 | 449s | 1 |
| 5 | stage-05-concall | claude-sonnet-5-5 | high | n/a | n/a | n/a | n/a | 234920 | 599s | 1 |
| 6 | stage-06-peers | claude-sonnet-5-5 | medium | n/a | n/a | n/a | n/a | 278880 | 328s | 1 |
| 7 | stage-07-emoat | claude-sonnet-5-5 | high | n/a | n/a | n/a | n/a | 174445 | 354s | 1 |
| 9 | stage-09-tam | claude-sonnet-5-5 | high | n/a | n/a | n/a | n/a | 140721 | 402s | 1 |
| 12a | verifier-a-numerical | claude-sonnet-5-5 | high | n/a | n/a | n/a | n/a | 357620 | 610s | 1 |
| 12c | verifier-c-framework (phase-1 scope) | claude-opus-5-5 | xhigh | n/a | n/a | n/a | n/a | 160090 | 799s | 1 |
| 12d | verifier-d-peers | claude-sonnet-5-5 | medium | n/a | n/a | n/a | n/a | 59753 | 68s | 1 |
| 12b | verifier-b-redflags | claude-opus-5-5 | xhigh | n/a | n/a | n/a | n/a | 400662 | 873s | 1 |
| 13 | stage-13-synthesis (phase 1 lite) | claude-opus-5-5 | high | n/a | n/a | n/a | n/a | 205744 | 762s | 1 |
| 9b | stage-09b-dossier | claude-sonnet-5-5 | medium | n/a | n/a | n/a | n/a | 242146 | 676s | 1 |

## Close-out summary (Phase 1)

Run total over 20 ledger rows (subagents only): 3,823,615 tokens. Phase 1 stages and verifiers only (excluding the two step1 pre rows): 3,542,131.

### (a) Top five by tokens
- stage-02-notes-pass: 447,524 (11.7%)
- verifier-b-redflags: 400,662 (10.5%)
- verifier-a-numerical: 357,620 (9.4%)
- stage-03-ardeep: 355,490 (9.3%)
- stage-06-peers: 278,880 (7.3%)

### (b) Downshift failures
none. stage-00-intake-check ran on claude-haiku-5-5; verifier A ran on claude-sonnet-5-5; verifier-a-shadow did not run in this session (the single shadow run belongs to the TD Power session).

### (c) Cost spikes
none. No prior run exists for KPL.

### (d) Operator snapshot
SESSION TOTAL (/cost)


### (e) Fresh vs re-read
The harness exposed one total per subagent run. The in / cache_read / cache_write / out split is n/a on every row, so all 20 rows are left out of the sums below.
Fresh tokens (cache write + output + uncached input): n/a
Re-read tokens (cache read): n/a
Re-read multiple (re-read / cache write): n/a
