# Session cost ledger — INDOBORAX 2026-08-30 (phase 1)

| # | stage | model | effort | in_tok | out_tok | total_tok | wall | run# |
|---|-------|-------|--------|--------|---------|-----------|------|------|
| 1 | gate-0 | claude-sonnet-5 | - | - | - | 152081 | 544s | 1 (AR-unreadable, superseded) |
| 2 | notes-pass1 | claude-sonnet-5 | - | - | - | 34993 | 123s | 1 (blocked: pdftoppm missing) |
| 2 | notes-pass1 | claude-sonnet-5 | - | - | - | 188567 | 442s | 2 (rerun after poppler install) |
| 2 | notes-pass2 | claude-sonnet-5 | - | - | - | 173158 | 618s | 1 |
| 1 | gate-0 | claude-sonnet-5 | - | - | - | 179149 | 921s | 2 (rerun with AR readable) |
| 2 | notes-pass3 | claude-sonnet-5 | - | - | - | 66731 | 203s | 1 |
| 3 | ar-deep-dive | claude-sonnet-5 | - | - | - | 220451 | 1110s | 1 |
| 4 | business-model | claude-sonnet-5 | - | - | - | 199692 | 441s | 1 |
| 5 | concall | claude-sonnet-5 | - | - | - | 102398 | 495s | 1 |
| 8 | promoter | claude-sonnet-5 | - | - | - | 196527 | 504s | 1 |
| 6 | peers | claude-sonnet-5 | - | - | - | 202522 | 534s | 1 |
| 7 | emerging-moat | claude-sonnet-5 | - | - | - | 196789 | 953s | 1 |
| 9 | tam-sam-som | claude-sonnet-5 | - | - | - | 143260 | 581s | 1 |
| 12a | verifier-a-numerical | claude-haiku-4-5 | - | - | - | 111959 | 141s | 1 |
| 12b | verifier-b-redflags | claude-opus-4-8 | - | - | - | 86204 | 300s | 1 |
| 12c | verifier-c-framework | claude-opus-4-8 | - | - | - | 90029 | 283s | 1 |
| 12d | verifier-d-peers | claude-sonnet-5 | - | - | - | 183794 | 366s | 1 |
| 13 | synthesis-lite | claude-opus-4-8 | - | - | - | 102303 | 273s | 1 |
| 09b | halt1-dossier | claude-sonnet-5 | - | - | - | 255050 | 772s | 1 |

## SESSION CLOSE-OUT

Run total (sum of all ledger rows): ~2,885,657 tokens across 18 subagent runs.

### (a) TOP FIVE BY TOKENS (stage totals, loops/retries summed)
| rank | stage | total_tok | share |
|------|-------|-----------|-------|
| 1 | stage 2 notes triple-pass (pass1 run1+run2, pass2, pass3) | 463,449 | 16.1% |
| 2 | stage 1 gate-0 (run1 superseded + run2) | 331,230 | 11.5% |
| 3 | stage 09b halt-1 dossier | 255,050 | 8.8% |
| 4 | stage 3 ar-deep-dive | 220,451 | 7.6% |
| 5 | stage 6 peers | 202,522 | 7.0% |

### (b) DOWNSHIFT FAILURES
none. The one mechanical stage that ran in phase 1 (verifier A) ran on claude-haiku-4-5 as routed; stage 0 validation was done by the orchestrator, not a subagent.

### (c) COST SPIKES
none. No prior INDOBORAX run exists, so there is no baseline to compare against.

### (d) WASTED-WORK NOTE (not a downshift/spike, but a real cost)
poppler-utils (pdftoppm) was absent at session start, so stage 1 run#1 (152,081 tok) and stage 2 pass1 run#1 (34,993 tok) failed to read the AR and had to be re-run after the orchestrator installed poppler. ~187,074 tokens of avoidable rework. See LESSONS_ARCHIVE.md.

### (e) OPERATOR SNAPSHOT
Operator: run /cost and /usage now and paste the cache hit ratio and the loop totals below.
Operator snapshot:
  cache_hit_ratio:
  loop_totals:
