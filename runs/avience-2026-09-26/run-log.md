# RUN LOG — AVIENCE 2026-09-26

- step1 intake: identity resolved (NSE SME AVIENCE, screener consolidated). Peers QLINE, MOLBIO, TARSONS; Hemant Surgical rejected (no transcripts).
- worktree: run branch run/avience-2026-09-26 built in a separate worktree (C:\Users\SUMIT SHARMA\repos\inflection-avience) off origin/main, because the main checkout carries the operator's uncommitted and staged framework edits (v3.11) and other same-day /step1 sessions share it.
- collector (dry-run): screener "Annual Report 2026" x2 were 3-page Reg 30 intimations, not the AR; announcements/ empty (no BSE code). Repaired by hand from NSE (AR, RHP, three FY26 results filings, 11 Reg 30 filings, SHP XBRL). Two byte-identical intimation duplicates removed in the phase 1 commit.
- tooling: pdftotext exit 127; pymupdf extraction to page-marked .txt; image-only pages (RHP pdf 279-362 restated statements, 23 deck slides, 17-Jul results) rendered to PNG under inputs/_render/ (local, git-excluded).
- stage 0: run inline by the orchestrator. Corpus commit 9ae79ec7.
- stage 1: block file wrapped in markdown code fences; orchestrator removed the fence lines (content unchanged), now parses.
- stages 1-9: every stage ran once in the foreground; no re-invoke. Block files for B01, B02 (all passes), B03-B09 and verifier blocks arrived wrapped in markdown code fences in some cases; the orchestrator removed the fence lines (content unchanged) before parsing.
- stage 2 pass 3 settled the AR Note 40 label swap (listed parent earns ~76% of FY26 group profit, not 24%).
- verifiers: 0 CRITICAL. Confidence overall 71 (set by redflag_coverage, partial catches counted as had; strict 28.6% recorded). Verifier C F-E1: B07 capex_embedded_growth_pct should read 190, not 90 (left in B07 as the stage wrote it; correction carried in confidence.yaml notes; fix before phase 3).
- synthesis-lite: PROCEED WITH FLAGS (FLAG-CASH INDETERMINATE, capped to CAVEATS, band 60-74 moves one level). It also wrote B13-synthesis.yaml to blocks/.
- 09b: mechanical dossier check passed first time.
