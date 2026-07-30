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

## Addendum (2026-07-29): two more documents supplied
- inputs/pressrel_mtar_q1fy27.pdf: 4 pages, Reg 30(6) Investors Press Release for Q ended 30.06.2026.
  CLASS: narrative investor communication -> processed via presentation/narrative ruleset
  (doctype token "pressrel"; enumerate all financials + segment/vertical figures + MD quotes +
  forward/hedge phrases; reconcile numbers vs results filing).
- inputs/presentation_mtar_q1fy27.pdf: 32 pages, 960x540 16:9 slides, image-heavy (slides 1/6/10
  etc under 100 chars -> OCR fallback). CLASS: presentation.
- Protocol: each new doc gets A1->A2->A3; then A4 RE-RUNS ONCE merging all three docs
  (results + pressrel + presentation); then A5; then Notion updated with additional-details section.
