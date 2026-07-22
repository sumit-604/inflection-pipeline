# Run Log — E2E Networks Q1 FY27 Quarterly Review

Run date: 2026-07-21
Operator: Keerti Kaushik (via orchestrator)

## Document classification (orchestrator, from content)
- `e2e_results_q1fy27.pdf` (7pp, orig 3362a276) -> **results** (Reg 33 Board Outcome + unaudited financial results, E2E Networks, Scrip 544783, dated 2026-07-21)
- `e2e_pressrelease_q1fy27.pdf` (2pp, orig 7d976e9d) -> **presentation** (Press Release "E2E Networks Reports Q1 FY'27 Results", E2E Networks, Scrip 544783, dated 2026-07-21)
- `e047399e...` (9pp) -> REJECTED. Belongs to ARIS/Arisinfra Solutions (Scrip 544419), Scheme of Amalgamation. No E2E content. Dropped per operator ruling 2026-07-21.

## Setup decisions
- Company memory companies/E2E.md: ABSENT (new company, first quarterly run).
- No concall transcript supplied -> Role 5 (Concall Analysis Protocol v1.1) marked N/A for this run.
- Toolchain: poppler-utils + tesseract-ocr installed at session start (were missing).
- Protocol files: all three present.

## Gate log
(to be appended as pipeline runs)

## Gate log (all passed)
- GATE A1 (page coverage 100%): results 7/7 pages; press release 2/2 pages. PASS.
- GATE A2 (count reconciliation): results 18 notes / 60 line items / 4 ZERO_STANDING / 10 auditor paras / 1 entity; press release 29 line items / 2 slides. grep == manual sweep. PASS (first pass, both docs).
- GATE A3 (17 checks, no blanks): results 7 findings (5 FORWARD-SIGNAL, 1 AMBIGUOUS, 1 NEUTRAL); press release 7 findings (3 FORWARD-SIGNAL, 2 AMBIGUOUS, 2 NEUTRAL). Ledger 100% reconciled. PASS.
- A4: single merged review; Role 4 full, Role 5 N/A (no transcript). Verdict PROCEED WITH FLAGS; cash conversion INDETERMINATE. 12 mgmt questions, 9 monitorables, 9 flags.
- GATE A5 (verdict COMPLETE): coverage clean (0 orphan rows), arithmetic within rounding (1x 0.01 Cr slip, decision-irrelevant), no surviving bear counter. PASS first pass, no loop-backs.

## Notion save (page 345bb2b9-d3ab-80ab-87ce-e5296355301b)
- Full review appended at page end (headline tables, forensic synthesis, Questions-for-Management, monitorables, verdict, A5 COMPLETE note).
- Key Notes property: Jul-21-2026 entry PREPENDED, Jun-30 entry preserved.
- Decision Status UNCHANGED (WATCHLIST / BUY ON DIPS) — no pre-committed trigger fired.

## Count-reconciliation line
2 documents reviewed: results filing (18 notes / 60 line items / 10 auditor paras / 1 entity / 1 agenda item) + press release (29 line items / 2 slides). 0 concall turns (no transcript). 100% reviewed.

LESSONS.md note: this run is a quarterly review (Role 4/5); LESSONS.md append is a /run-pipeline, /fttcp, /finalize convention. Quarterly runs log to this run folder.

## ADDENDUM 2026-07-21: investor presentation added
- `e2e_presentation_deck_q1fy27.pdf` (22pp, orig 176ef221) -> doctype **presentation** (slide deck). E2E Networks, Scrip 544783, Q1 FY27, dated 2026-07-21. Confirmed genuine E2E.
- Distinct from the earlier press release (also class presentation); artifacts suffixed "_deck" to avoid collision.
- Image-only slides p2 (39 ch), p15 (26 ch) -> OCR required (A1 handles <100 ch pages).
- Re-running A1->A2->A3 on deck, then A4 re-merge (results + press release + deck), A5, Notion update.

## Deck run gate log (2026-07-22) — all passed
- GATE A1 (deck): 22/22 pages, OCR on slides 2 & 15, Millions x0.1. PASS.
- GATE A2 (deck): 42 line items / 22 slides / 1 ZERO_STANDING (zero named customers) / 46 third-party entity refs; grep == manual sweep. PASS. Flags DISCLOSED_IN_DECK, NUMERIC_INCONSISTENCY.
- GATE A3 (deck): 17 checks, no blanks, ledger 100%. 10 findings (5 FORWARD-SIGNAL, 2 AMBIGUOUS, incl FND-01 zero named customers, FND-09 exit MRR/capex/BS, FND-08 SovCloud funding vehicle). PASS.
- A4 v2: merged review across THREE docs (results + press release + deck). Verdict UNCHANGED PROCEED WITH FLAGS; cash conversion INDETERMINATE. Deck re-rates checklist #1 (Exit MRR Rs71.8 Cr) and #2 (CWIP->PPE) to GREEN; #4 (L&T board link) to AMBER partial; #3 hardened (zero named customers). 14 mgmt questions (2 new).
- GATE A5 v2 (verdict COMPLETE): coverage clean (0 orphan rows across 3 ledgers), arithmetic within rounding (deck figures recompute: Exit MRR Rs71.8 Cr, Mar-26 net cash ~Rs239 Cr, capex/PPE series, dry powder Rs132.68 Cr), no surviving bear counter. PASS first pass. 4 non-blocking tightening notes (N1 PPE causal wording; N2 roster A3-F2/F11; N3 BS row display; N4 4608 vs 4609 bps), none verdict-affecting.

## Notion update (deck)
- Deck addendum appended at page end (deck tables, updated checklist, 14-question status table, verdict, A5 COMPLETE note).
- Key Notes: Jul-22 deck entry PREPENDED; Jul-21 and Jun-30 entries preserved.
- Decision Status UNCHANGED (WATCHLIST / BUY ON DIPS) — no pre-committed trigger fired.

## Count-reconciliation line (3 docs)
Results filing (18 notes / 60 line items / 10 auditor paras / 1 entity / 1 agenda) + press release (29 line items / 2 slides) + investor deck (42 line items / 22 slides / 46 entity refs). 0 concall turns. 100% reviewed.
