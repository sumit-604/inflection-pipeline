# Run Log — Route Mobile Q1 FY27 Quarterly Review

Run date: 2026-07-24
Ticker: ROUTE (Route Mobile Limited, BSE 543228 / NSE ROUTE)
Quarter: Q1 FY27 (quarter ended June 30, 2026)
Branch: claude/route-mobile-quarterly-pkqpxv

## Prechecks
- Protocol files: PRESENT (Results v1.2, Concall v1.1, Master v3.3)
- Toolchain: pdftotext/pdfinfo/pdftoppm/tesseract installed (poppler-utils + tesseract-ocr via apt)
- Company memory companies/ROUTE.md: ABSENT (Notion fetched live instead)

## Document classification (by content, per orchestrator Step d)
| Input file | Pages | Ref No | Class | doctype passed | filename stem |
|---|---|---|---|---|---|
| results_board_outcome_reg33.pdf | 12 | RML/2026-27/691 | Reg 33 Board Outcome + Unaudited Financial Results + Limited Review Reports | results | results |
| investor_presentation.pdf | 18 | RML/2026-27/693 | Investor Presentation | presentation | presentation |
| press_release.pdf | 3 | RML/2026-27/692 | Press Release (Q1 FY27 results announcement, mgmt narrative) | presentation-template | pressrelease |

## Orchestrator decisions
- No concall transcript supplied. Role 4 (results) runs fully; Role 5 has no transcript. Deck + press release feed Role 4.
- Press release: no native slide/note/turn structure. Enumerated with the INVESTOR PRESENTATION template (claims/numbers/footnotes as units), distinct `pressrelease` filenames to avoid collision with the investor deck.

## Pipeline completion (2026-07-24)
- A1 gates: results 12pp / presentation 18pp / pressrelease 3pp — all 100% coverage.
- A2 gates: results (22 notes / 94 line-items / 16 zero-standing / 33 entities) / presentation (18 slides / 381 nums) / pressrelease (3 / 9 mgmt nums) — count tests reconciled.
- A3 gates: all three docs, 17 checks marked, 100% ledger-reconciled, no blanks.
- A4: PROCEED WITH FLAGS; cash conversion INDETERMINATE (capped); Decision Status held HELD 4% (flagged).
- A5: verdict COMPLETE (0 orphan rows, 0 arithmetic mismatches, 0 surviving bear counters).
- Notion save: full review appended to page body; Key Notes prepended (4 entries, 3 prior preserved); Decision Status UNCHANGED. Saved value recorded in work/_keynotes_new.txt.
- No thesis-broken trigger formally fired. Cap-5% gate FAILED on GM. Deferred RDE trim re-put to operator.

## Concall addendum (2026-07-24, transcript supplied after initial run)
- Concall transcript added as 4th document; run through A1-A5.
- A1 concall: 204 lines verbatim, 100% coverage (text input, no OCR).
- A2 concall: 9 participants (MD Gupta ABSENT), 91 turns, 37 questions, 34 mgmt numbers, 35 fwd-commitments, 20 hedges; count test reconciled.
- A3 concall: F6/F7/F17 apply; 20 findings; F17 silence audit + commitment register; GATE A3 pass.
- A4 v2: Role 5 now FULL. Credibility Grade C (Mixed, 41.7%); archetype EVASIVE (provisional). Prior-12 answer status: 0 answered / 5 partial / 3 dodged / 4 not addressed. Verdict UNCHANGED PROCEED WITH FLAGS; Decision Status UNCHANGED HELD 4%.
- A5 v2: verdict COMPLETE (0 orphan / 0 arithmetic / 0 surviving bear counters).
- Notion: concall addendum appended to page body; Key Notes prepended with concall entry (5 entries total, 4 prior preserved); Decision Status UNCHANGED. Written value recorded in work/_keynotes_new_v2.txt.
- Key concall signals: GM band recalibrated down to 21.5-23% (below 25% thesis destination); FY27 numeric guidance withheld; GM bridge refused; Heltar consideration undisclosed; CLO go-live slipped; MD absent; CFO spoken -14.1% QoQ adj-PAT conflicts with filing -40% (filing wins).
