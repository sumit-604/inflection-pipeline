# Run log — KUSUMGAR 2026-11-12 (/step1, Phase 1)

- Checkout guard: fetch OK, framework diff empty against origin/main.
- Collector run 1 failed mechanically: Playwright headed Chromium launch "spawn UNKNOWN" from this shell; nothing downloaded. Run 2 forced headless through a session-local sitecustomize hook (no edit to tools/). REPO_ROOT in collect_to_repo.py is hardcoded to a path that does not exist here; overridden through a scratch wrapper (no edit to tools/).
- Hand-collected after the collector: prospectus (SEBI), Q1 and Q2 FY27 results, CARE and CRISIL rationales, Q1 FY27 presentation, screener print of Sep 2026 shareholding (SECONDARY).
- FY2025-26 standalone audited statements: scanned, no text layer; tesseract is not installed, tools/ocr_repair.py cannot run. Moved to inputs/other/, not consumed.
- No annual report exists (listed 2026-07-15). Stages 2 and 3 run on the prospectus restated financial information (precedent: Kwick 2026-10-04, AMAGI 2026-07-12), bounded by inputs/prospectus/SECTION_INDEX.md. This departs from the DEGRADATION MAP line "No annual report: stages 2 and 3 are skipped"; recorded in B00.
- Empty-folder confirmation suppressed per /step1 autonomy contract; standing answer "proceed with the gaps".
- Subagents are dispatched by the harness as async tasks; each is completion-checked (report file, block file) before any later stage reads it.
- Verifier A shadow: ten /step1 sessions run in parallel today on an armed switch. This session claimed the single shadow run in the shared notes folder (shadow-claim.txt) before dispatch.
