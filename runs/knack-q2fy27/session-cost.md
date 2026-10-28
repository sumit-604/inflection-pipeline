# Session cost: KNACK Q2 FY27 quarterly review (/run-quarterly, 28-29 Oct 2026)

## Document review summary row (shared baseline)

`ticker | date | doctype | pages | a1_extracted_text_tok | total_run_tok | loop_iterations`

`KNACK | 2026-10-28 | results+presentation(deck)+concall(ASR) | 21+36 pages, 557 call lines (16 turns) | ~46,300 | 3,093,413 | 1`

- a1_extracted_text_tok: the three A1 fulltexts measured at about 4 characters per token: results ~15,400 (61,541 chars); deck ~17,600 (70,214 chars); concall ~13,400 (53,474 chars).
- total_run_tok: base run 2,094,085 plus correction loop 999,328. Agent tokens as reported by the harness per subagent. Orchestrator session tokens are not in this figure.
- The press release (3 pages) got no chain. It is text-identical to results pp. 17-19 (Annexure B); `diff -w -B` showed only the annexure header and the signature timestamp. Saved about 0.2M tokens.
- The run was paused by the coordinator after A5 loop 0 (28-Oct, about one hour) and resumed on 29-Oct. Resumed agents (SendMessage) carried their context, so the loop rows include re-read context.

## Per-agent ledger (base run)

| Agent | Document | Model | total_tok | Wall | Run # |
|---|---|---|---|---|---|
| A1 extractor | results | claude-sonnet-5-5 | 157,101 | 490 s | 1 |
| A1 extractor | deck | claude-sonnet-5-5 | 155,681 | 392 s | 1 |
| A1 extractor | deck (p5, p13, p14 image-slide OCR; orchestrator gate miss, mechanical) | claude-sonnet-5-5 | 171,614 | 58 s | 2 (resume) |
| A1 extractor | concall (ASR) | claude-sonnet-5-5 | 79,784 | 206 s | 1 |
| A2 enumerator | results | claude-sonnet-5-5 | 116,462 | 445 s | 1 |
| A2 enumerator | deck | claude-sonnet-5-5 | 78,575 | 256 s | 1 |
| A2 enumerator | concall | claude-sonnet-5-5 | 68,763 | 136 s | 1 |
| A3 forensics | results | claude-opus-5-5 | 184,187 | 509 s | 1 |
| A3 forensics | deck | claude-opus-5-5 | 177,186 | 472 s | 1 |
| A3 forensics | concall | claude-opus-5-5 | 156,501 | 408 s | 1 |
| A4 analyst | merged | claude-opus-5-5 | 370,692 | 1,106 s | 1 |
| A5 adversary | audit (loop 0) | claude-opus-5-5 | 377,539 | 1,276 s | 1 |
| **Base subtotal** | | | **2,094,085** | **5,754 s** | |

A2 cost check: every A2 came in below its A1 (results 116,462 < 157,101; deck 78,575 < 155,681; concall 68,763 < 79,784). The deck comparison uses A1 run 1 only.

## Correction loop (own rows; loop_iterations = 1)

| Agent | Scope | Model | total_tok | Wall | Iteration |
|---|---|---|---|---|---|
| A2 enumerator | concall question ledger: A5-07, A5-08 | claude-sonnet-5-5 | 74,094 | 40 s | loop 1 (resume) |
| A4 analyst | A5-01 to A5-06, A2 alignment, 3 rounding errata | claude-opus-5-5 | 447,021 | 497 s | loop 1 (resume) |
| A5 adversary | re-audit with drift check | claude-opus-5-5 | 478,213 | 249 s | loop 1 (resume) |
| **Loop subtotal** | | | **999,328** | **786 s** | |

Loop 0 findings: FACTUAL 2, MISSING 5, CONTRADICTION 1, STYLE 4. Loop 1 result: COMPLETE, all eight closed, no drift, STYLE 7 logged (not looped). No verdict-card number, verdict or forward figure moved in the loop.

## Notes for the next run

- Resumed A4 and A5 cost 0.45-0.48M each, more than their first runs, because the resume re-reads the whole context. Loop cost was 48% of base. A fresh A4 given only the eight gap lines might be cheaper; untested.
- A1 marked image slides "title only" without rendering them. Three of the five held data (plant units and start dates, warehouse size). The A1 gate should treat a title-only slide with a large image as a render candidate, not only zero-character pages.
- A2 deck missed nothing material; the fulltext sweep as second method worked.
