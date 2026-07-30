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

## 3-document merge completion (2026-07-30)
- Press release: A1 pass (4pp, Crores x1) / A2 pass (54 rows) / A3 pass (all PR numbers tie to consolidated)
- Presentation: A1 pass (32 slides, 1 OCR page) / A2 pass (535 numbers) / A3 pass (monitorables resolved)
- A4 merged: PROCEED WITH CAVEATS, Decision Status held WATCHLIST/AVOID; 24 A3 findings incorporated
- A5 merged: INCOMPLETE (loop 1) on 3 numbers + 1 graft -> A4 corrected -> A5 re-audit COMPLETE
- Notion: additional-detail section appended (segment split, order book, guidance, promoter stake,
  13 management questions, completeness proof); Key Notes audit trail prepended (both prior entries preserved)
- Count reconciliation: results 11 notes / pressrel 26 numbers / presentation 32 slides - all reviewed

## Valuation refresh + final Notion save (2026-07-30)
- Role 1 valuation refresh (stage 11) run on operator question (raise entry with raised guidance?).
  Result: entry zone Rs 1,542-1,789 (~+3% vs prior), decision AVOID-on-valuation, HR 1.22/1.53 STOP
  at CMP ~5,200. Destination PE held 40x; evidenced ROCE 17.2% -> 16.1x independent (pressures down).
- Notion: full 3-doc merged review + valuation refresh saved (segment split, order book, guidance,
  promoter stake, monitorable resolution, questions, Section 1B re-derivation, FY31 projections,
  delta table, hurdle, direct answer). Key Notes audit trail carries 4 entries (refresh + 3-doc +
  results + original May thesis), all prior preserved. Decision Status UNCHANGED WATCHLIST/AVOID.
- All work files committed to branch claude/mtar-annual-reports-qo0c39.

## Addendum 2 (2026-07-30): concall transcript supplied
- inputs/concall_mtar_q1fy27.txt: Q1 FY27 earnings call, supplied as TEXT (auto-STT, heavily
  garbled: company "NT/MTA/ENA Technologies" = MTAR; names garbled). Doctype: concall -> Role 5
  now ACTIVE (was N.A. in prior runs). Chain A1->A2->A3 (F6/F7/F17 silence audit + reconcile
  spoken numbers vs filing/deck), then A4 RE-RUNS ONCE merging all FOUR docs, A5, Notion.
- High-value items to reconcile: spoken gross margin 45.61% vs 47.65% YoY (deck showed 45.5 vs
  54.2 = -8.7pp; concall implies only -2pp -> DEFINITION/reconciliation flag); Jun-26 debt
  Rs 423.6 Cr + investments Rs 379 Cr -> net ~20-30 Cr (resolves net-debt-basis question);
  Q1 CFO Rs 247.69 Cr spoken (resolves INDETERMINATE? but advance-driven caveat); +Rs 800 Cr
  order today -> book ~5,943 Cr; guidance reaffirmed 80% + 24% margin, "will do better".
  Silences: promoter stake (not asked), Bloom concentration deflected as "unwanted noise".
