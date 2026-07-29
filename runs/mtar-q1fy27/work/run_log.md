# Quarterly Run Log — MTAR Q1 FY27

## Setup (orchestrator)
- Invocation: /run-quarterly MTAR --docs <uploaded pdf>
- Date: 2026-07-29
- Branch: claude/mtar-annual-reports-qo0c39

## Prechecks
- Protocol files: all 3 PRESENT (Results v1.2, Concall v1.1, Master v3.3)
- Toolchain: pdftotext/pdfinfo/pdftoppm/tesseract installed OK (poppler-utils, tesseract-ocr)
- Company memory: companies/MTAR.md ABSENT (first quarterly run for this ticker in repo)

## Document class detection
- inputs/results_mtar_q1fy27.pdf: 9 pages, text layer healthy (700-3666 chars/page)
  - Page 1: Reg 33 Board Outcome letter, "Un-audited Financial Results (Standalone and
    Consolidated) for the quarter ended 30.06.2026", Limited Review Reports attached.
  - CLASS: results
  - Quarter: Q1 FY27 (quarter ended 30.06.2026 = Q1 of FY2026-27)
  - Board Outcome: 7 agenda items; item 5 = Annual Report/AGM notice/BRSR/MD&A for FY25-26.
    Items beyond item 1 to be enumerated & assessed by A2/A3.

## Pipeline completion (2026-07-29)
- A1 extractor: GATE A1 pass (100% coverage, 9/9 pages, unit Millions x0.1)
- A2 enumerator: GATE A2 pass (11 notes / 68 line items / 8 zero-standing / 7 agenda / 26 auditor paras / 3 entities)
- A3 forensics: GATE A3 pass (100% reconcile; findings F6/F8/F13/F14)
- A4 analyst: PROCEED WITH CAVEATS (cash conversion INDETERMINATE); Decision Status held WATCHLIST/AVOID
- A5 adversary: VERDICT COMPLETE (coverage/arithmetic/adversarial all PASS)
- Notion save: full review appended to MTAR page; Key Notes audit trail prepended (prior entry preserved); Decision Status unchanged (no trigger fired)
- Count reconciliation: 11 notes reviewed / 0 turns (no concall) / 0 slides (no deck) — all reviewed
