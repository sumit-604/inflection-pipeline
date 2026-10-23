# SESSION COST — PITTIENG Q2 FY27 (/run-quarterly), 2026-10-23

## Document review summary (shared baseline)
ticker | date | doctype | pages | a1_extracted_text_tok | total_run_tok | loop_iterations
---|---|---|---|---|---|---
PITTIENG | 2026-10-23 | results + presentation (no concall) | 15 + 32 = 47 | NOT FOUND (no tokenizer run; fulltext size 46,625 + 67,628 = 114,253 chars) | 1,726,644 (subagents only; orchestrator NOT FOUND) | 2

## Per-agent ledger (subagent totals from task notifications)
agent | doc | model | total_tok | wall | run#
---|---|---|---|---|---
A1 extractor | results | claude-sonnet-5-5 | 120,404 | 512 s | 1
A2 enumerator | results | claude-sonnet-5-5 | 75,208 | 208 s | 1
A3 forensics | results | claude-opus-5-5 | 187,395 | 718 s | 1
A1 extractor | presentation | claude-sonnet-5-5 | 113,854 | 345 s | 1
A2 enumerator | presentation | claude-sonnet-5-5 | 52,242 | 146 s | 1
A3 forensics | presentation | claude-opus-5-5 | 217,440 | 710 s | 1
A4 analyst | merged | claude-opus-5-5 | 340,914 | 1,017 s | 1
A5 adversary | merged | claude-opus-5-5 | 332,862 | 970 s | 1
**Base run subtotal** | | | **1,440,319** | | 

## Correction loop (own rows)
agent | iteration | model | total_tok | wall | note
---|---|---|---|---|---
A4 analyst (resumed) | 1 | claude-opus-5-5 | 69,921 | 421 s | 7 A5 fixes (5 FACTUAL, 2 MISSING)
A5 adversary (resumed, re-audit) | 1 | claude-opus-5-5 | 89,982 | 358 s | verdict still INCOMPLETE: 1 new CONTRADICTION (A5-C1, wording)
**Loop 1 subtotal** | | | **159,903** | | loop cap reached; stopped for operator

## Correction loop 2 (operator approval 2026-10-24: "complete them fully", relayed by parent session)
agent | iteration | model | total_tok | wall | note
---|---|---|---|---|---
A4 analyst (resumed) | 2 | claude-opus-5-5 | 67,480 | 942 s | A5-C1 wording fix (two other-income readings) + STYLE S3, S4
A5 adversary (resumed, re-audit) | 2 | claude-opus-5-5 | 58,942 | 234 s | verdict COMPLETE with style notes (S1, S5, S6 open)
**Loop 2 subtotal** | | | **126,422** | | final; no third iteration

Loop token figures are the resumed agents' cumulative totals less their first-run totals.

## Cost checks
- A2 below A1: results 75,208 < 120,404 PASS; presentation 52,242 < 113,854 PASS.
- No A2-A5 agent reported reading inputs/.

## Cache figures (CLAUDE.md close-out)
- Fresh tokens: NOT FOUND (not exposed to the orchestrator)
- Re-read tokens: NOT FOUND
- Re-read multiple: NOT FOUND
