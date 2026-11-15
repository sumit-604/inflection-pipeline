
## Step F corpus collection (2026-11-15)

Collector ran clean in dry-run (scratch wrapper for REPO_ROOT, headless sitecustomize); no 429s hit. No edits under tools/. Nothing committed.

**inputs/ contents (all PDFs open in pypdf; pre-extracted .txt exists for every PDF)**
- annual-report/: Annual_Report_2026.pdf (FY2025-26, 191pp, BSE 3 Sep 2026), Annual_Report_2025.pdf (FY2024-25, 183pp).
- results/: 20261113-190e3152 (H1 FY27, half-year ended 30 Sep 2026, filed 13 Nov 2026); 20260520-dc0311a3 (FY26 audited, incl. H2 FY26); 20251112-d1d63f49 (H1 FY26). All from BSE.
- prospectus/: Qualitek_Final_Prospectus_Jan2024.pdf (final SME prospectus, 389pp, bseindia.com, lead manager Oneview).
- presentation/: Investor_Presentation_May2026_H2FY26.pdf (20 May 2026, 42pp); Investor_Presentation_May2025_H2FY25.pdf (38pp).
- announcements/: 58 BSE Reg 30 filings, 12 months (16 Nov 2025 to 14 Nov 2026), via 90-day windows. Includes Nov 2026 EGM notice (c4dee558), board outcome (05e9700a), preferential-issue filings (Sep 2026), earnings-call intimation (ffae6832), newspaper ads.
- shareholding/: screener-shareholding-pattern-extract-2026-11-15.txt (Sep 2026: promoters 56.46%, FII 1.54%, DII 0.15%, public 41.85%; 1,014 holders). Secondary extract, not the BSE filing.
- peer-concalls/: 12 PDFs, 4 each: VIMTALABS (Feb, May, Jul, Nov 2026), KRSNAA (Feb, May, Aug, Nov 2026), LALPATHLAB (Feb, May, Jul, Nov 2026). First pages verified as the right issuer.
- screening/: 4 Data_Sheet CSVs (screener = QLL, plus 3 peers).
- concalls/, rating/, research/: empty.

**Gaps (what was tried)**
- concalls/: none. Screener lists May 2026 and May 2025 calls with "Transcript" chips that carry no link (only PPT links); BSE has no transcript filing in 2023-12 to 2026-11; qualiteklab.com has no transcript page; web search found none. Chrome fallback not used: no screener document link exists to download. H1 FY27 call intimated 14 Nov 2026, not yet held.
- rating/: no rating report found (web search across all agencies, BSE filings text scan). Company may be unrated.
- shareholding BSE PDF: BSE returns 403 (bot wall) to scripted and headless access; screener extract used. Chrome fallback not tried for this file.
- H1 FY27 investor presentation: not yet filed.

**Chrome browser:** no file came through it.

**Collector warnings:** announcements originally 16 files only (collector's window); repaired to 58. Collector reported empty xlsx sheets (formulas without cached values) for all four companies' P&L, Quarters, BS, CF, Customization.

**EMPTY screening sheets:** screener-Data_Sheet.csv (QLL) Quarters block has labels, 0 figures (EMPTY). Its P&L/BS/CF have FY21, FY22, FY25, FY26 only; FY23 and FY24 columns absent. Peers' Data_Sheet quarters have figures. File names "screener-Data_Sheet.csv" is the QLL file.

**OCR:** none needed. check_extraction flagged two newspaper-ad announcements (20261114-080a5e86, 20261114-16192e74) as GARBLED: 20% non-ASCII, which is the Hindi advert text; cover letters extract clean. Not OCR'd.

**Misfiles:** none moved between folders. Removed the duplicate H1 FY27 results copy from announcements/ (kept in results/). Renamed presentation file to Investor_Presentation_May2026_H2FY26.pdf.

**Manifest:** company Qualitek Labs Ltd, ticker QLL, cmp 552.0, market_cap_cr 643.0 (collector values; confirmed on the screener page, not 0), run_date 2026-11-15, run_type full, sector_cap_row "Consulting / Engineering services", listed_date 2024-01-29, concalls_available false, warnings kept and extended. Parses with yaml.

## Phase 1 orchestration (2026-11-15)
- Checkout guard: PASS against origin/main (b4ec38ce). Run branch run/qll-2026-11-15 cut from origin/main. Corpus commit eef45981.
- Identity: Qualitek Labs Ltd, BSE SME 544091, symbol QLL. Screener resolves only by BSE code: https://www.screener.in/company/544091/consolidated/ (check_url OK 200). Run ticker QLL.
- Steps B, C, D ran on an Opus 5.5 subagent with live web; Step F on a Sonnet 5.5 subagent (operator batch instruction).
- Brief vs corpus: the brief said concalls_available true (screener Transcript chips). Step F found no transcript link on screener, BSE or the company site. Manifest set to concalls_available false; Phase 1 runs in NO-CONCALL MODE. The company does hold calls; H1 FY27 call is on 2026-11-24.
- Chrome download fallback: not used. No file came through the browser. The missing documents (main transcripts, rating) have no link on the screener Documents section; the BSE shareholding PDF (403) is not hosted there.
- LESSONS pre-read done. No tagged lessons for sector "Consulting / Engineering services"; no archetype declared yet. Open actions read (C2: record stage 5 no-call cost, target under 100k).
- Tooling gate: every inputs/ PDF has a page-marked .txt; stages and verifiers get the .txt path, PDF as fallback.
- SPEAR GATE: PASS (OVERRIDE line in companies/QLL.md).
- EMPTY-FOLDER CONFIRMATION: suppressed per /step1 autonomy contract; proceed with the gaps (rating, concalls, research).
- Verifier A shadow: NOT RUN here. Nine /step1 sessions run in parallel today; the single shadow run belongs to the TD Power session. .claude/shadow.yaml left untouched by this run.
- Execution: this harness dispatches subagents asynchronously with a completion notification. The orchestrator waits for each notification and runs the completion check (report file, block file, block parses) before any dependent stage.
- Stage 0: B00-intake (Haiku 5.5) 83 rows, 0 misfiles, 0 unreadable. Freshness pairs OK (pair 1 skipped, no-concall).
