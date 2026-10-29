# PAUSED: ROUTE q2fy27 (/run-quarterly), 29-Oct-2026

Paused on a coordinator STOP: the operator closed the batch without Route.
Nothing is committed. Every file stays in place on branch
`claude/qr-route-q2fy27-fb3514` (worktree `.claude/worktrees/qr-route-q2fy27-fb3514`).
The whole run folder `runs/route-q2fy27/` is untracked.

## What finished

| Step | State | Evidence |
|---|---|---|
| Setup, guard, sources | done | work/run-log.md; inputs/SOURCES.md; guard PASS 29-Oct |
| Notion read (read only) | done | work/notion_snapshot_2026-10-29.md, work/notion_thesis_context.md, work/monitoring_checklist.md. Decision Status HELD, 4% at Rs 509 |
| A1 results / presentation / pressrelease | GATE A1 pass (18/18, 23/23, 3/3 pages) | extracted/*; blocks/a1-*.yaml |
| A2 results / presentation / pressrelease | GATE A2 pass (1129, 368, 74 IDs; zero orphans) | work/ledger_*; blocks/a2-*.yaml |
| A3 results / presentation / pressrelease | GATE A3 pass (F1-F17 statused in each) | work/forensics_*; blocks/a3-*.yaml |
| Transcript check before A4 | ABSENT; filed documents only | run-log |
| A4 merged review | done: PROCEED WITH FLAGS; cash INDETERMINATE-WITH-DIRECTION; branch 8A | work/review_route_q2fy27.loop0.md (pre-loop) |
| A5 audit, loop 0 | INCOMPLETE: M-1 (A2), F-1 to F-7, M-2 to M-4, C-1 (A4); 8 STYLE | work/audit_route_q2fy27.loop0.md and audit_route_q2fy27.md (same text); blocks/a5.yaml |
| Correction loop 1, A2 fix | done: 12 signature blocks; M01-M11 MISSING_FROM_STRUCTURED rows | work/ledger_results_route_q2fy27.md (pre-loop copy *.loop0.md); blocks/a2-results.yaml |
| Correction loop 1, A4 fix | done: all 11 items plus 8 STYLE patched; change log in review section "CORRECTION LOOP 1 CHANGE LOG"; verdict and cash class unchanged; questions 23 | work/review_route_q2fy27.md (853 lines, 08:11); blocks/a4.yaml (08:12) |

## What did NOT run

1. A5 re-audit of the loop-1 review (the last step of the one permitted loop).
2. Close-out: session-cost.md, operator-brief.md, notion-payload.md.
3. Commit.

## Exact next step on RESUME

1. Re-check `C:/ConcallPipeline/Daily Concall Intelligence/Q2 FY27 Results/35 Route Mobile/concall_audio/` for `RouteMobile_Q2FY27_Concall_Transcript_ASR.txt`. If it has appeared, the review needs A1-A3 on it as `concall` and an A4 Role 5 pass before A5; that is a scope change for the operator.
2. Otherwise run A5 (quarterly-a5-adversary) as the loop-1 re-audit, with the same inputs as loop 0: review `work/review_route_q2fy27.md`, the three A1 fulltexts and structured files, the three A2 ledgers; output `work/audit_route_q2fy27.md` (keep `audit_route_q2fy27.loop0.md`), block `work/blocks/a5.yaml`. Tell it this is the re-audit of correction loop 1 and point it at the change log section and the loop-0 audit for the items to check. This is the one loop; if still INCOMPLETE, stop and ask the operator.
3. Then write `session-cost.md`, then `operator-brief.md` (format of the 21-22 Oct briefs; CMP Rs 435 from `_CMP_snapshot_2026-10-28.md`), then `notion-payload.md` (no Notion write), delete PAUSED.md, and `git add runs/route-q2fy27 && git commit -q -m "quarterly review: ROUTE q2fy27"`.

## Token ledger so far (harness subagent_tokens; resumed agents report cumulative counts)

| Agent | Doc / step | Cumulative tok | Note |
|---|---|---|---|
| A1 | results (runs 1-2) | 138,587 | run 1 126,206; resume read 3 cells by render |
| A1 | presentation (runs 1-3) | 114,607 | run 1 68,396; re-extraction of 8 scrambled slides; 4 anchors |
| A1 | pressrelease (runs 1-2) | 56,670 | run 1 41,180; 21 anchors fixed |
| A2 | results (base + loop 1) | 106,842 | base 97,522; loop 9,320 |
| A2 | presentation | 52,158 | |
| A2 | pressrelease | 37,380 | |
| A3 | results | 206,972 | |
| A3 | presentation | 148,223 | |
| A3 | pressrelease | 76,297 | |
| A4 | review + loop 1 | NOT RECORDED | the orchestrator process exited before both completion notices |
| A5 | audit loop 0 | 298,246 | 1,204 s |

Recorded so far: 1,235,982 tokens (A4 excluded). Loop iterations: 1 (in progress; A5 re-audit pending).

## Key result for the operator (from the loop-1 review; not yet re-audited)

- Verdict PROCEED WITH FLAGS. Thesis-broken condition 1 depends on the basis: Adjusted EBITDA margin 10.04% (NOT FIRED, Rs 0.45 Cr headroom, rests on a Rs 6.90 Cr Masivian add-back); reported 9.75% after 9.16% (FIRED, pre-committed exit 50%). Operator ruling needed.
- CMP Rs 435 is below the Rs 450 hard floor; the 52-week low Rs 407 is below the Rs 420 floor (date ND).
- H1 CFO/PAT 0.22x; Rs 116.83 Cr supplier prepayment; Strategic Premium expiry condition met on filed evidence (no Proximus KPI).
