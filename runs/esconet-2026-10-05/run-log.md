# Run log: ESCONET 2026-10-05 (Phase 1)

- 2026-10-05 stage 0: B00 first wrote ARs as INR Crores; stage 1 found INR Lakhs on the face; B00 corrected in the stage 1 commit.
- 2026-10-05 stage 1 commit (bfb148e6) swept in a partial 02-notes-pass1.md while pass 1 was still writing; the pass 1 commit replaced it.
- 2026-10-05 dispatch order: stage 9's prompt needs B04_YAML and B07_CAPEX_FIGURE, so stage 9 runs after stages 4 and 7, not in parallel with 4, 5, 8.
- 2026-10-05 B05 block file line 39 lacked the closing brace of a flow mapping (reply copy had it); clerical repair by the orchestrator, no content change.
- 2026-10-05 stage 8 status partial: web sources failed (MCA, zaubacorp, NSE 2025 filing, SEBI/SAT portals); searches_skipped populated.
- 2026-10-05 several stage agents reported the Edit tool unavailable and left small report blemishes (anchor typos) unfixed; each named in its hand-back.
