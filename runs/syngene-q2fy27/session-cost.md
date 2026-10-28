# Session cost — SYNGENE q2fy27 (/run-quarterly, batch 2026-10-28, batch 2)

## DOCUMENT REVIEW summary row (shared baseline)

`ticker | date | doctype | pages | a1_extracted_text_tok | total_run_tok | loop_iterations`

`SYNGENE | 2026-10-28 | results+presentation+pressrelease+disclosure (no concall) | 56 (11+32+9+4) | ~32,780 (8,138 + 15,897 + 6,990 + 1,755; fulltext chars / 4) | 1,736,667 | 1`

- Base run (12 agent runs): 1,587,744 tokens.
- Correction loop 1 (A4 fix + A5 re-audit): 148,923 tokens. Logged as its own rows below.
- Orchestrator session tokens: NOT MEASURED in-session (not included in total_run_tok).

## Per-agent ledger

Token figures are the harness `subagent_tokens` per agent run. The two loop rows resumed the same agent, whose counter is cumulative; the loop row is the counter after the loop minus the base run.

| Agent | Document / step | Model | total_tok | Wall | Run # | Gate / result |
|---|---|---|---|---|---|---|
| A1 | results | claude-sonnet-5-5 | 83,703 | 190s | 1 | GATE A1 pass, 11/11 pages, R001-R828; pages 2-11 via pdftotext -raw after render check |
| A1 | presentation | claude-sonnet-5-5 | 101,332 | 251s | 1 | GATE A1 pass, 32/32 pages, R001-R350; p6/p27/p28 render-verified blocks |
| A1 | pressrelease | claude-sonnet-5-5 | 76,949 | 323s | 1 | GATE A1 pass, 9/9 pages, R001-R879; pages 6-9 via -raw |
| A1 | disclosure (change in management) | claude-sonnet-5-5 | 47,548 | 85s | 1 | GATE A1 pass, 4/4 pages, R001-R071; A1 only by coordinator instruction |
| A2 | results | claude-sonnet-5-5 | 81,965 | 161s | 1 | GATE A2 pass, 828/828 IDs, zero orphans; below A1 |
| A2 | presentation | claude-sonnet-5-5 | 70,422 | 166s | 1 | GATE A2 pass, 350/350 IDs; fulltext sweep found M01-M09 (non-financial) carried as ledger rows; below A1 |
| A2 | pressrelease | claude-sonnet-5-5 | 73,073 | 191s | 1 | GATE A2 pass, 879/879 IDs; 2 postal codes MISSING_FROM_STRUCTURED; below A1 |
| A3 | results | claude-opus-5-5 | 169,025 | 467s | 1 | GATE A3 pass, F1-F17 statused, 16 findings |
| A3 | presentation | claude-opus-5-5 | 113,759 | 327s | 1 | GATE A3 pass, 17 findings |
| A3 | pressrelease | claude-opus-5-5 | 168,355 | 582s | 1 | GATE A3 pass, 26 findings |
| A4 | merged review | claude-opus-5-5 | 322,478 | 836s | 1 | PROCEED WITH FLAGS; T3 FIRED, T4 FIRED (conservative, contested) |
| A5 | audit | claude-opus-5-5 | 279,135 | 959s | 1 | INCOMPLETE: 3 FACTUAL, 4 MISSING, 2 CONTRADICTION, 8 STYLE -> loop to A4 |
| A4 | correction loop 1 | claude-opus-5-5 | 64,618 | 378s | loop 1 | 9 items fixed; diff 56 lines, all at the patch sites |
| A5 | re-audit | claude-opus-5-5 | 84,305 | 308s | loop 1 | COMPLETE (style notes only; no drift) |

Concurrency: at most two subagents at once (6 GB machine, three sibling sessions).

## Notes for the coordinator
- Cost check: every A2 came in below its A1 (results 81,965 < 83,703 is the narrowest margin).
- Results and press-release statement pages carry a scrambled `-layout` text layer (values on the wrong labels). A1 switched those pages to `pdftotext -raw` after a render check. Same family of defect as the earlier batch.
- Resuming the A4 and A5 agents for the loop (instead of fresh runs) kept the loop at 148,923 tokens, about 9% of the base run.
- Fresh tokens / re-read tokens / re-read multiple: NOT MEASURED in-session (harness reports one total per subagent).
