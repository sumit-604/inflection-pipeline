# session-cost — UNIMECH Q2 FY27 (/run-quarterly, 2026-10-28 to 2026-10-29)

DOCUMENT REVIEW summary row (shared baseline):

`ticker | date | doctype | pages | a1_extracted_text_tok | total_run_tok | loop_iterations`

`UNIMECH | 2026-10-28 | results+presentation+pressrelease+concall(ASR) + supporting monitoring+deviation+lta | 17+26+3 pages + 828 transcript lines; supporting 13+4+1 pages | ~62,200 (fulltext chars / 4: results 15,450; deck 15,800; PR 2,070; call 14,020; monitoring 12,160; deviation 1,950; LTA 750) | 2,909,985 | 1`

Token figures are the harness `subagent_tokens` per agent run. Loop rows are fresh agents with a narrow scope (no resumed context). The orchestrator session's own tokens are not in this ledger (NOT FOUND: the harness gives no per-session figure in-session). The run paused about one hour on the coordinator's order after the loop-0 A5 returned (28-Oct), and resumed on 29-Oct with one subagent at a time.

## Per-agent ledger, base run

| Agent | Doc | Model | total_tok | Wall | Run # | Gate / note |
|---|---|---|---|---|---|---|
| A1 | presentation | claude-sonnet-5-5 | 113,220 | 344.5 s | 1 | PASS 26/26 pages, R001-R670; 6 slides render-verified |
| A1 | results | claude-sonnet-5-5 | 135,475 | 372.3 s | 1 | PASS 17/17 pages, R001-R953; 10 statement pages transcribed from renders (HiddenHorzOCR layer scrambled) |
| A2 | presentation | claude-sonnet-5-5 | 71,782 | 137.3 s | 1 | PASS 670/670, 0 orphans, M1-M2 unrowed labels; fulltext sweep; below A1 |
| A2 | results | claude-sonnet-5-5 | 101,829 | 263.3 s | 1 | PASS 953/953, 0 orphans; tie-outs 244/245 (1 filing-level RECON_GAP, consol opening cash); below A1 |
| A3 | presentation | claude-opus-5-5 | 194,694 | 643.7 s | 1 | PASS 17/17 (10 FINDING, 7 N.A.), 27 findings D-A3-01..27; M3 unrowed item logged |
| A3 | results | claude-opus-5-5 | 230,237 | 557.6 s | 1 | PASS 17/17 (11 FINDING, 4 PASS, 2 N.A.), 25 findings R-A3-01..25 |
| A1 | pressrelease | claude-sonnet-5-5 | 49,825 | 88.7 s | 1 | PASS 3/3 pages, R001-R123; page 2 table render-verified |
| A2 | pressrelease | claude-sonnet-5-5 | 42,438 | 52.9 s | 1 | PASS 123/123, 0 orphans, M01-M05 trivial; below A1 |
| A1 | concall (ASR .txt) | claude-sonnet-5-5 | 78,573 | 171.0 s | 1 | PASS 828/828 lines, 65 turns, R001-R257; numbers ASR-UNVERIFIED |
| A2 | concall | claude-sonnet-5-5 | 58,013 | 119.4 s | 1 | PASS 257/257, 0 orphans, 65 turns, 24 questions; below A1 |
| A3 | pressrelease | claude-opus-5-5 | 110,266 | 236.6 s | 1 | PASS 17/17 (4 FINDING, 2 PASS, 11 N.A.), 10 findings P-A3-01..10 |
| A1 | monitoring (supporting) | claude-sonnet-5-5 | 85,006 | 262.3 s | 1 | PASS 13/13 pages, R001-R261; pp4-11 render-verified; A1 only |
| A1 | deviation (supporting) | claude-sonnet-5-5 | 49,230 | 99.0 s | 1 | PASS 4/4 pages, R001-R068; pp2-3 render-verified; A1 only |
| A1 | lta (supporting) | claude-sonnet-5-5 | 36,576 | 44.8 s | 1 | PASS 1/1 page, R001-R031; A1 only |
| A3 | concall | claude-opus-5-5 | 208,604 | 590.4 s | 1 | PASS 17/17 (6 FINDING, 11 N.A.), 25 findings C-A3-01..25; ASR mishearings resolved against filed docs |
| A4 | merged (4 docs + 3 supporting) | claude-opus-5-5 | 491,459 | 1,453.7 s | 1 | PROCEED WITH FLAGS; no trigger fired; 38 questions |
| A5 | audit | claude-opus-5-5 | 351,685 | 1,114.2 s | 1 | INCOMPLETE (M1-M5, C1; 9 STYLE) |
| **Base subtotal** | | | **2,408,912** | | | |

Cost checks: every A2 came in below its A1 (deck 71,782 < 113,220; results 101,829 < 135,475; PR 42,438 < 49,825; call 58,013 < 78,573). No A2-A5 agent reported reading inputs/.

## Correction loop 1 (one iteration, its own rows)

Trigger: loop-0 A5 INCOMPLETE on 5 MISSING (M1 A2; M2, M3, M4, M5 A4) and 1 CONTRADICTION (C1). A4 wrote a JSON patch file (34 exact-anchor replacements); the orchestrator applied it with a script that refuses any anchor not found exactly once. A5 re-audited with the mechanical diff (work/review_loop1_diff.txt) for a drift check.

| Agent | Doc | Model | total_tok | Wall | Run # | Gate / note |
|---|---|---|---|---|---|---|
| A2 | concall (loop 1) | claude-sonnet-5-5 | 31,111 | 28.7 s | loop 1 | PASS; M1 fixed, questions 24 -> 25 (T57 Gaurav) |
| A3 | addendum deck R222 + call R244/R065 (loop 1) | claude-opus-5-5 | 97,034 | 342.3 s | loop 1 | PASS; D-A3-28 (C1), C-A3-26 (M2) |
| A4 | patch file (loop 1) | claude-opus-5-5 | 188,560 | 562.4 s | loop 1 | 34 replace patches, closes C1 M1-M5; applied by orchestrator script, all anchors unique; no verdict change |
| A5 | re-audit (loop 1) | claude-opus-5-5 | 184,368 | 543.5 s | loop 1 | COMPLETE; C1 M1-M5 CLOSED; drift PASS; 5 STYLE |
| **Loop subtotal** | | | **501,073** | | | |

## Totals

| Item | Tokens |
|---|---|
| Base run (17 agent runs) | 2,408,912 |
| Correction loop 1 (4 agent runs) | 501,073 |
| **total_run_tok** | **2,909,985** |
| loop_iterations | 1 |

## Cache accounting
- Fresh tokens: NOT FOUND (no per-session split available in-session).
- Re-read tokens: NOT FOUND.
- Re-read multiple: NOT FOUND. Every agent ran in a fresh context. The orchestrator context sat idle across the one-hour pause, so its cache expired once.

## Notes for the next run
- The loop-1 patch-file method cost 188,560 for A4, below a whole-review rewrite (A4 base 491,459), and A5 found no drift.
- Supporting A1-only documents cost 170,812 in all (monitoring 85,006; deviation 49,230; LTA 36,576).
