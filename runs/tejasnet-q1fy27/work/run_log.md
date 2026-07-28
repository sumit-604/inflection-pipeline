# Run Log — TEJASNET Q1 FY27 Quarterly Review
Run date: 2026-07-27

## Document class detection
- results_tejasnet_q1fy27.pdf (8p): Board Outcome + Unaudited Financial Results (Standalone & Consolidated) + Limited Review Report -> RESULTS
- pressrelease_tejasnet_q1fy27.pdf (3p): "Tejas announces Q1FY27 results" narrative + headline P&L + mgmt quotes + order book/net debt -> PRESENTATION (company narrative preprocessing class)
- reg30_smp_tejasnet_q1fy27.pdf (2p): Reg 30 disclosure, COO Preetham Uthaiah designated Senior Management Personnel -> GOVERNANCE DISCLOSURE (A1 extract only; fed to A4 as F13 management-change evidence; A2/A3 forensic machinery is financial-statement oriented and N.A. for a 4-row SMP annexure)

## Toolchain
poppler-utils + tesseract installed this session (apt fetch initially 404'd on stale index; apt-get update fixed).

## Quarter: Q1 FY27 (quarter ended June 30, 2026)

## Pipeline gates (all pass)
- A1: results 8p/100% (pages 2-8 OCR'd, scanned filing); press release 3p/100%; reg30 SMP 2p/100%.
- A2: results ledger — 14 notes, 76 line items, 5 ZERO_STANDING, 4 entities, 11 auditor paras, gate pass (one internal re-sweep for OCR'd note-5 digit). Press-release ledger — 14 categories reconciled, gate pass.
- A3: results — 6 FINDINGs (F2,F3,F8,F9,F13,F14), all 17 marked, 100% reconciled, gate pass. Press release — 2 FINDINGs (F6,F16), gate pass.
- A4: PROCEED WITH FLAGS; cash conversion INDETERMINATE; Decision Status verified WATCHLIST; branch 8A; 9 mgmt questions; 14 monitorables. Role 5 N.A. (no concall).
- A5: COMPLETE — 0 orphan rows, 0 arithmetic mismatches, 0 surviving bear counters. No loop-back.

## Notion save (after A5 COMPLETE)
- Full review appended to Tejas Networks page (2 inserts: financials/tripwire tables + Questions/forensics/audit).
- Key Notes property: dated Q1FY27 line PREPENDED, prior FY26-AR and AGM-26 entries preserved.
- Decision Status UNCHANGED (WATCHLIST) — no pre-committed trigger fired.

## Operational notes (for LESSONS.md at next /finalize; /run-quarterly does not itself append LESSONS.md)
1. Toolchain: poppler-utils/tesseract absent at session start; apt index stale (poppler .deb 404) — `apt-get update` then install fixed. Consider baking the toolchain into the environment setup script.
2. Concurrent A1 collision risk: prompts/quarterly-a1-extractor.md step 3 OCR fallback uses a generic `page` prefix (pdftoppm/tesseract) with no ticker/doctype disambiguation. When multiple A1 agents share one work/ dir, temp images can collide. No output text was corrupted this run (agents used unique intermediates after noticing), but the prompt should mandate a `<ticker>_<doctype>_` temp prefix.
3. Both the results filing AND the press release are scanned PDFs with embedded-OCR text-layer artifacts (Ql/FV27/l00G, teiasnetworks). Financial digits read clean and cross-reconciled; label artifacts only. A5 arithmetic audit found 0 mismatches.

## Role 5 concall addendum (2026-07-28)
- Concall transcript (ICICI Securities Q1 FY27 call, ASR text) added and run through the full pipeline.
- A1 concall: 223 lines verbatim, byte-identical, gate pass.
- A2 concall: 14 participants, 109 turns, 37 questions, 40 mgmt numbers, 27 phrases, gate pass (flags MGMT_ABSENCE, REPEAT_QUESTION, ARITHMETIC_CHECK, ASR_GARBLE, DECLINED_DISCLOSURE).
- A3 concall: F6/F7/F14/F17 findings (21), all 17 marked, silence audit (6 silences), gate pass.
- A4 merged Role4+Role5 review -> review_merged_tejasnet_q1fy27.md. Combined verdict PROCEED WITH FLAGS; Decision Status WATCHLIST unchanged.
- A5 merged audit: COMPLETE (0 orphans, 0 arithmetic mismatches, 0 surviving bear counters). Three non-blocking maker notes logged (A2 question-count off-by-one; A4 finance-cost basis label; DTA figure 365 vs 434 carried-memory not anchored).
- Notion: concall Role 5 section appended to Tejas page (debt decomposition, promise-vs-delivery, silence audit, critical exchanges, arithmetic reconciliation, residual questions, combined verdict); Key Notes concall line prepended, all prior entries preserved. Decision Status unchanged (no trigger fired).
- Key call takeaway: CFO decomposed the +Rs 746 Cr net-debt jump (net receivables +~325 + supplier payouts + capex); receivables absorbed ~81% of revenue and non-BSNL collections conceded sticky -> structural-WC risk better evidenced. Profitability target softened (Q4 FY27 -> 12-18 months). BSNL add-on now 26,000 sites, 6th qtr of imminence. Six silences incl QIP amid RED net debt.

## Operational note (Role 5)
- The DTA figure appears as both Rs 365 Cr (FY26 KAM, Notion) and ~Rs 434 Cr (FY26 DTA + Q1 deferred-tax benefit ~68.57): the ~434 is carried-memory arithmetic, NOT anchored (no Q1 balance sheet). Flagged for the analyst; resolve at Q2 half-year balance sheet.
