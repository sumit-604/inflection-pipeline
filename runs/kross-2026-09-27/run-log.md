# RUN LOG — KROSS 2026-09-27

- intake (/step1): identity KROSS, standalone screener page (consolidated page carries no figures). CMP Rs 268, mcap Rs 1,728 Cr.
- intake: collector dry-run staged main + AUTOAXLES + JAMNAAUTO + HAPPYFORGE. Repairs: results (3), rating rationale, prospectus, SHP XBRL, 16 announcements fetched by hand; duplicates removed; JAMNAAUTO swapped for RKFORGE (no Jamna call in 12 months); sector_cap_row Pharma / CDMO -> Recycling / Manufacturing.
- tooling: all 49 PDFs pre-extracted with PyMuPDF to page-marked .txt; image pages of the Q4 FY26 monitoring agency report and the 16-Sep-2026 scrutinizer report OCR'd with RapidOCR.
- corpus commit 022306e4 on run/kross-2026-09-27 (worktree C:\Users\SUMIT SHARMA\repos\inflection-pipeline-kross, branched from origin/main 4779c889).
- stage 0: run inline by the orchestrator; B00 parses. Empty-folder pause suppressed (/step1 autonomy contract); only research/ empty.
- stage 1: Core 68/100, moat 11/60, grand 79, GOOD (deal-breaker 2, Block B 1/20). Orchestrator omitted the peer Data_Sheets from the task; resumed the same agent with them: M2 0->1, M5 0->1 (weak pass, 5-name set), M9 stays 0; moat 13/60, grand 81/160, GOOD unchanged. Ledger run#2 tokens = 154009 cumulative - 111540 = 42469.
- stage 2 pass 1 / pass 2: complete. Red-flag tier: Note 52 ROE computed on share capital (171%); Bull Auto Parts RPT (Kunal Rai proprietorship). Stage anchors use PRINTED AR folios.
- tooling: ARs are two-page landscape spreads; AR .txt re-extracted with left/right halves carrying printed folios; page map recorded in B00.
- stage 2 pass 3: B02-notes complete, accounting_quality 6/10, one red flag (Note 52 ROE formula), FLAG-CASH (receivables ageing). Anchors converted to 'AR PDF p.N (printed p.X)'.
