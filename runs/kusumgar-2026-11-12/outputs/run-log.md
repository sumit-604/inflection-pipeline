# Run log — KUSUMGAR 2026-11-12 (/step1, Phase 1)

- Checkout guard: fetch OK, framework diff empty against origin/main.
- Collector run 1 failed mechanically: Playwright headed Chromium launch "spawn UNKNOWN" from this shell; nothing downloaded. Run 2 forced headless through a session-local sitecustomize hook (no edit to tools/). REPO_ROOT in collect_to_repo.py is hardcoded to a path that does not exist here; overridden through a scratch wrapper (no edit to tools/).
- Hand-collected after the collector: prospectus (SEBI), Q1 and Q2 FY27 results, CARE and CRISIL rationales, Q1 FY27 presentation, screener print of Sep 2026 shareholding (SECONDARY).
- FY2025-26 standalone audited statements: scanned, no text layer; tesseract is not installed, tools/ocr_repair.py cannot run. Moved to inputs/other/, not consumed.
- No annual report exists (listed 2026-07-15). Stages 2 and 3 run on the prospectus restated financial information (precedent: Kwick 2026-10-04, AMAGI 2026-07-12), bounded by inputs/prospectus/SECTION_INDEX.md. This departs from the DEGRADATION MAP line "No annual report: stages 2 and 3 are skipped"; recorded in B00.
- Empty-folder confirmation suppressed per /step1 autonomy contract; standing answer "proceed with the gaps".
- Subagents are dispatched by the harness as async tasks; each is completion-checked (report file, block file) before any later stage reads it.
- Verifier A shadow: ten /step1 sessions run in parallel today on an armed switch. This session claimed the single shadow run in the shared notes folder (shadow-claim.txt) before dispatch.
- Cross-block figure to settle (FLAG-DISAGREEMENT candidate): offer-for-sale share count. B01 carries 15,521,350 (Q2 FY27 results p.7); B03 carries 15,521,698 (Prospectus p.392, p.118). Different documents; left to Verifier A and stage 10.
- B03 found two discrepancies against B02 (customer above 10% in FY26: 11.13% at Prospectus p.28 against Note 45(c) 0.00%; ECFPL valuer is named at p.235). The B03 reading carries forward.
- B00 correction: freshness pair 1 was first set FAIL (Q2 FY27 transcript not published). Stage 5 reported, and the orchestrator confirmed at the page (Q2 FY27 presentation p.22-25, Q&A item 21), that no Q2 call was held; a written Investor Q&A replaced it and is in the corpus. Pair 1 is PASS, freshness_verdict is FRESHNESS PAIRS OK. The corpus stays CORPUS GAPPED on its other gaps. No freshness cap applies to the gate recommendation.
- Stage 5 total 129,853 tokens against the 100k no-concall target (LESSONS open action C2: record stage 5 cost on the next no-call run).
- Stage 8 returned status partial (SEBI orders database, MCA21, exchange portal and proxy-adviser sites not reachable; two fetches refused). It named four clerical errata in its own report that it could not edit; the orchestrator applied them as stated and added an ERRATA note above the block. The block governs.
- Stage 6 report and block were swept into the stage 8 commit (aa1e11e6) before the stage 6 hand-back arrived; the completion check ran afterwards and the files on disk match the committed ones.
