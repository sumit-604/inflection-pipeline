# RUN LOG — AMAGI Q1 FY27 quarterly review

## Setup (orchestrator)
- Date: 2026-08-13
- Ticker: AMAGI (Amagi Media Labs Ltd), Scrip 544679 / NSE AMAGI
- Docs supplied: 1 PDF
- Toolchain: pdftotext/pdfinfo/pdftoppm/tesseract installed via apt (poppler 24.02.0, tesseract 5.3.4)

## Document class detection
- inputs/amagi_results_q1fy27.pdf — 13 pages, Producer "Adobe Acrobat Paper Capture Plug-in"
  - Page 1: BSE/NSE cover letter, "Outcome of the Board Meeting", Reg 33, "Unaudited Standalone and Consolidated Financial Results" for quarter ended June 30, 2026.
  - CLASS = results. Quarter = Q1 FY27 (three months ended 30 Jun 2026).
  - Text-layer health: all 13 pages > 700 chars, no zero-text pages. A1 to confirm per-page and OCR-fallback any image-heavy page.

## Gates
- (pending A1/A2/A3/A5)

## Notion (live fetch attempt — orchestrator, Step 0F)
- Searched workspace 5x (name, scrip 544679, thesis keywords). AMAGI has NO directly-discoverable standalone Notion page; it is referenced by other companies' pages (AURUM) but not indexed as its own page. Likely never saved to Notion (only prior run 2026-07-12; no /finalize Notion save on record).
- FALLBACK: companies/AMAGI.md is the authoritative thesis/monitoring context passed inline to A3 and A4. Notion-fetch failure is NOT a mechanical halt condition per orchestrator NON-NEGOTIABLE list.
- Notion save (Step 4) will re-search and, if still absent, create the page under EQUITY RESEARCH.

## GATE A1 — PASS
- 13/13 pages, 13 formfeeds, 804 lines, unit=Millions (x0.1 -> Cr), no OCR needed, coverage 100%.

## GATE A2 — PASS
- 16 notes, 52 line items, 7 zero_standing, 4 Board agenda items, 13 auditor paras, 11 entities. Count test reconciled. Flags: ZERO_STANDING, ENTITY_COVERAGE_GAP, TEXT_ANOMALY.

## GATE A3 — PASS
- All 17 checks statused, no blanks, 100% ledger reconciliation. 10 findings.
- Forward-signals: A3-F1-01 (standalone zero tax/finite shield), A3-F6-01 (MOA enables equity raise), A3-F8-01 (consol ETR ~16% latent shield), A3-F13-01 (Board capital-raising + MD reappt agenda).
- Ambiguous: A3-F2-01 (sub PAT -25% QoQ), A3-F4-02 (entity coverage gap), A3-F7-01 (going-concern-ish tax hedge), A3-F9-01 (actuarial OCI loss 29.86 > full FY26 7.21).

## A4 — complete
- Verdict PROCEED WITH CAVEATS; cash conversion INDETERMINATE (capped correctly). Decision Status verified WATCHLIST/AVOID (not held), UNCHANGED (no tripwire fired). 9 mgmt questions, 8 monitorables, 8 flags. Plain-language brief included.

## GATE A5 — PASS (verdict COMPLETE, first pass, no loops)
- Coverage PASS (fresh grep = ledger: 16/52/7/4/13/11, no orphans). Arithmetic PASS (only <=0.1pp rounding variances). Adversarial: 3 strongest bear counters all already in A4. No surviving counters.

## COUNT RECONCILIATION LINE
- 16 notes / 52 line items / 7 zero-standing / 4 Board agenda items / 13 auditor paras / 11 entities — all reviewed. (0 concall turns, 0 slides — none supplied.)
