# SESSION COST — PITTIENG Q2 FY27 (/run-quarterly), 2026-10-23

## Document review summary (shared baseline)
ticker | date | doctype | pages | a1_extracted_text_tok | total_run_tok | loop_iterations
---|---|---|---|---|---|---
PITTIENG | 2026-10-23 | results + presentation + concall (ASR) | 15 + 32 + 11 five-minute blocks | NOT FOUND (no tokenizer run) | 2,819,959 (subagents only; orchestrator NOT FOUND) | 3 (2 base-pass loops + 1 concall-pass loop)

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

## Concall pass (2026-10-23/24; operator request via parent session; ASR of YouTube XoAOF3cf9J4)
agent | doc | model | total_tok | wall | run#
---|---|---|---|---|---
ASR faster-whisper small int8 (local CPU) | concall | n/a | 0 | ~40 min | 2 (first run died at chunk 1 in the app restart; mechanical re-run)
A1 extractor | concall | claude-sonnet-5-5 | 113,105 | 416 s | 1
A2 enumerator | concall | claude-sonnet-5-5 | 58,189 | 220 s | 1
A3 forensics | concall | claude-opus-5-5 | 213,969 | 688 s | 1
A4 analyst (resumed, merge + Role 5) | merged | claude-opus-5-5 | 208,899 | 983 s | merge
A5 adversary (resumed, merge audit) | merged | claude-opus-5-5 | 242,882 | 811 s | merge
**Concall pass subtotal** | | | **837,044** | |

## Concall-pass correction loop (standing approval 2026-10-24)
agent | iteration | model | total_tok | wall | note
---|---|---|---|---|---
A4 analyst (resumed) | 1 | claude-opus-5-5 | 128,580 | 788 s | CM-M1..M5 + CM-S1..S6
A5 adversary (resumed, re-audit) | 1 | claude-opus-5-5 | 127,691 | 420 s | verdict COMPLETE with style notes (CM2-S1..S3; A5-S1, S5, S6)
**Concall loop subtotal** | | | **256,271** | |

Loop token figures are the resumed agents' cumulative totals less their first-run totals.

## Cost checks
- A2 below A1: results 75,208 < 120,404 PASS; presentation 52,242 < 113,854 PASS; concall 58,189 < 113,105 PASS.
- No A2-A5 agent reported reading inputs/.

## Cache figures (CLAUDE.md close-out)
- Fresh tokens: NOT FOUND (not exposed to the orchestrator)
- Re-read tokens: NOT FOUND
- Re-read multiple: NOT FOUND
