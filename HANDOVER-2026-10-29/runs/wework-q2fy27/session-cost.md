# Session cost: WEWORK Q2 FY27 quarterly review (/run-quarterly, 28-Oct-2026)

## Document review summary row (shared baseline)

`ticker | date | doctype | pages | a1_extracted_text_tok | total_run_tok | loop_iterations`

`WEWORK | 2026-10-28 | results+presentation(deck, letter, press)+concall(ASR) | 12+40+31+5 pages, 7 call blocks | ~92,300 | 3,148,233 | 1`

- a1_extracted_text_tok: the five A1 fulltexts measured at about 4 characters per token: results ~12,100; deck ~23,400; letter ~37,400; press ~3,800; concall ~15,600.
- total_run_tok: base run 2,634,763 plus correction loop 513,470. Agent tokens as reported by the harness per subagent. Orchestrator session tokens are not in this figure.

## Per-agent ledger (base run)

| Agent | Document | Model | total_tok | Wall | Run # |
|---|---|---|---|---|---|
| A1 extractor | concall (ASR) | claude-sonnet-5-5 | 96,391 | 250 s | 1 |
| A1 extractor | results | claude-sonnet-5-5 | 162,933 | 554 s | 1 |
| A1 extractor | deck | claude-sonnet-5-5 | 147,533 | 469 s | 1 |
| A1 extractor | letter | claude-sonnet-5-5 | 182,722 | 514 s | 1 |
| A1 extractor | press | claude-sonnet-5-5 | 61,721 | 123 s | 1 |
| A2 enumerator | results | claude-sonnet-5-5 | 83,468 | 199 s | 1 |
| A2 enumerator | concall | claude-sonnet-5-5 | 48,786 | 88 s | 1 |
| A2 enumerator | deck | claude-sonnet-5-5 | 79,036 | 188 s | 1 |
| A2 enumerator | letter | claude-sonnet-5-5 | 82,070 | 236 s | 1 |
| A2 enumerator | press | claude-sonnet-5-5 | 62,661 | 142 s | 1 |
| A3 forensics | results | claude-opus-5-5 | 194,246 | 455 s | 1 |
| A3 forensics | concall | claude-opus-5-5 | 144,366 | 443 s | 1 |
| A3 forensics | letter | claude-opus-5-5 | 250,922 | 585 s | 1 |
| A3 forensics | deck | claude-opus-5-5 | 221,695 | 666 s | 1 |
| A3 forensics | press | claude-opus-5-5 | 84,218 | 296 s | 1 (see note 2) |
| A4 analyst | merged | claude-opus-5-5 | 379,242 | 1,036 s | 1 |
| A5 adversary | audit (loop 0) | claude-opus-5-5 | 352,753 | 1,131 s | 1 |
| **Base subtotal** | | | **2,634,763** | | |

## Correction loop (own rows; loop_iterations = 1)

| Agent | Scope | Model | total_tok | Wall | Iteration |
|---|---|---|---|---|---|
| A4 analyst | fix F1, C1, C2, M1-M3 (+ style S1-S10) | claude-opus-5-5 | 234,538 | 815 s | loop 1 |
| A5 adversary | re-audit with drift check | claude-opus-5-5 | 278,932 | 651 s | loop 1 |
| **Loop subtotal** | | | **513,470** | | |

**Total run: 3,148,233 tokens. Loop share: 16.3%.**

## Notes

1. Cost check A2 < A1 held for results, concall, deck and letter. Press A2 (62,661) exceeded press A1 (61,721) by 940 tokens (1.5%). Diagnosed as fixed prompt overhead on a 5-page release plus the mandated fulltext sweep; no source path was in its task message. Its transcript file was empty, so no tool-call audit was possible. Logged in work/run-log.md; run figure not marked compromised.
2. Press A3 was first launched while two other A3 agents ran, over the two-agent cap. It was stopped at launch and restarted later. The harness reported no tokens for the stopped attempt; its cost is not in the total.
3. Heaviest stages: A4 (379k), A5 loop 0 (353k), letter A3 (251k). The 31-page shareholders' letter duplicates the filed statements; its A3 was told to cross-check them only, yet it remains the costliest A3.
4. Change that would make the next run cheaper: treat the press release as optional when the deck and letter carry the same headline numbers. Its A1-A3 chain cost about 209k tokens and added 11 findings, mostly restating deck findings.

## Token economics (CLAUDE.md session-cost close)

- Fresh tokens: NOT FOUND. The harness reports one total per subagent, not a fresh versus cache-read split.
- Re-read tokens: NOT FOUND (same reason).
- Re-read multiple: NOT FOUND (same reason).
