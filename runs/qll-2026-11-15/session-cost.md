# Session cost ledger: QLL 2026-11-15 (/step1 intake + Phase 1)

Token figures come from subagent result metadata. This harness exposes only total tokens and wall time per subagent; the split columns are n/a, never estimated.

| # | stage | model | effort | in_tok | cache_read | cache_write | out_tok | total_tok | wall | run# |
|---|---|---|---|---|---|---|---|---|---|---|
| S1 | step1-BCD brief/peers/cap | claude-opus-5-5 | default | n/a | n/a | n/a | n/a | 115644 | 5m06s | 1 |
| S1 | step1-F corpus collection | claude-sonnet-5-5 | default | n/a | n/a | n/a | n/a | 197414 | 23m53s | 1 |
| 0 | stage-00-intake-check | claude-haiku-5-5 | medium | n/a | n/a | n/a | n/a | 154227 | 5m06s | 1 |
| 1 | stage-01-gate0 | claude-sonnet-5-5 | medium | n/a | n/a | n/a | n/a | 153162 | 6m42s | 1 |
| 2 | stage-02-notes-pass (pass 1) | claude-sonnet-5-5 | default | n/a | n/a | n/a | n/a | 232236 | 6m41s | 1 |
| 2 | stage-02-notes-pass (pass 2) | claude-sonnet-5-5 | default | n/a | n/a | n/a | n/a | 189034 | 6m14s | 2 |
| 2 | stage-02-notes-pass (pass 3) | claude-sonnet-5-5 | default | n/a | n/a | n/a | n/a | 99426 | 2m21s | 3 |
| 3 | stage-03-ardeep | claude-sonnet-5-5 | default | n/a | n/a | n/a | n/a | 463796 | 18m16s | 1 |
| 5 | stage-05-concall (no-concall mode) | claude-sonnet-5-5 | default | n/a | n/a | n/a | n/a | 63841 | 2m46s | 1 |
| 4 | stage-04-bizmodel | claude-sonnet-5-5 | medium | n/a | n/a | n/a | n/a | 131875 | 4m24s | 1 |
| 8 | stage-08-promoter | claude-sonnet-5-5 | default | n/a | n/a | n/a | n/a | 200225 | 6m32s | 1 |
| 6 | stage-06-peers | claude-sonnet-5-5 | medium | n/a | n/a | n/a | n/a | 293869 | 4m51s | 1 |
| 7 | stage-07-emoat | claude-sonnet-5-5 | default | n/a | n/a | n/a | n/a | 216316 | 8m11s | 1 |
| 9 | stage-09-tam (stalled 600s, no output; mechanical re-invoke) | claude-sonnet-5-5 | default | n/a | n/a | n/a | n/a | n/a | n/a | 1 |
| 9 | stage-09-tam | claude-sonnet-5-5 | default | n/a | n/a | n/a | n/a | 81174 | 4m00s | 2 |
| 12a | verifier-a-numerical | claude-sonnet-5-5 | high | n/a | n/a | n/a | n/a | 329966 | 6m48s | 1 |
| 12b | verifier-b-redflags | claude-opus-5-5 | xhigh | n/a | n/a | n/a | n/a | 422667 | 25m49s | 1 |
| 12c | verifier-c-framework (phase-1 scope) | claude-opus-5-5 | xhigh | n/a | n/a | n/a | n/a | 185539 | 15m56s | 1 |
| 12d | verifier-d-peers | claude-sonnet-5-5 | medium | n/a | n/a | n/a | n/a | 40533 | 0m42s | 1 |
| 13 | stage-13-synthesis (phase 1 lite) | claude-opus-5-5 | high | n/a | n/a | n/a | n/a | 207066 | 9m58s | 1 |
| 9b | stage-09b-dossier | claude-sonnet-5-5 | medium | n/a | n/a | n/a | n/a | 227522 | 9m23s | 1 |

## Close-out summary (Phase 1, 2026-11-15)

Run total over ledger rows with a token figure: 4,005,532 tokens (19 rows; the stalled stage 9 run 1 has no figure and is left out). Intake rows S1 (313,058) are included; Phase 1 stages and verifiers alone total 3,692,474.

(a) TOP FIVE BY TOKENS
1. stage 2 notes triple-pass (3 runs): 520,696 (13.0%)
2. stage 3 AR deep dive: 463,796 (11.6%)
3. verifier B red flags (Opus 5.5 xhigh): 422,667 (10.6%)
4. verifier A numerical: 329,966 (8.2%)
5. stage 6 peers: 293,869 (7.3%)

(b) DOWNSHIFT FAILURES: none. stage-00-intake-check ran on claude-haiku-5-5; verifier A ran on claude-sonnet-5-5. verifier-a-shadow did not run in this session (the single shadow run belongs to the TD Power session of this batch).

(c) COST SPIKES: none (no prior run for QLL).

Open action C2 measurement (LESSONS.md, 2026-10-04): stage 5 in no-call mode cost 63,841 tokens, under the 100k target (Kwick 254k).

(d) SESSION TOTAL (/cost)


(e) FRESH VS RE-READ
This harness reports one total per subagent and no input, cache-read, cache-write or output split. All 20 ledger rows carry n/a in those columns and are left out of the sums.
Fresh tokens (cache write + output + uncached input): n/a (20 rows left out)
Re-read tokens (cache read): n/a (20 rows left out)
Re-read multiple (re-read / cache write): n/a (20 rows left out)
