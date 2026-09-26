# RUN LOG — AVIENCE 2026-09-26

- step1 intake: identity resolved (NSE SME AVIENCE, screener consolidated). Peers QLINE, MOLBIO, TARSONS; Hemant Surgical rejected (no transcripts).
- worktree: run branch run/avience-2026-09-26 built in a separate worktree (C:\Users\SUMIT SHARMA\repos\inflection-avience) off origin/main, because the main checkout carries the operator's uncommitted and staged framework edits (v3.11) and other same-day /step1 sessions share it.
- collector (dry-run): screener "Annual Report 2026" x2 were 3-page Reg 30 intimations, not the AR; announcements/ empty (no BSE code). Repaired by hand from NSE (AR, RHP, three FY26 results filings, 11 Reg 30 filings, SHP XBRL). Two byte-identical intimation duplicates removed in the phase 1 commit.
- tooling: pdftotext exit 127; pymupdf extraction to page-marked .txt; image-only pages (RHP pdf 279-362 restated statements, 23 deck slides, 17-Jul results) rendered to PNG under inputs/_render/ (local, git-excluded).
- stage 0: run inline by the orchestrator. Corpus commit 9ae79ec7.
