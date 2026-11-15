# Run log: keltech-2026-11-15

## Step F corpus collection (2026-11-15)

Collector: tools/collector via a scratch wrapper, `--dry-run`, headless Chromium (headed launch failed). Exit 0. Screener login worked for PREMEXPLN and APOLLO. For KELTECH and SOLARINDS the Excel export timed out in that pass. Screener listed no annual report, concall or presentation for KELTECH. The collector pulled 8 peer transcripts (APOLLO 4, PREMEXPLN 4), 6 BSE announcements, 2 screening CSVs. It found no AR, results, rating, shareholding.

Repairs, with source route:
- manifest.yaml: sector_cap_row set to "Cables / Industrial products". sector_cap_row_guess and collector_warnings left as collected. cmp 16564 and market_cap_cr 1656 match the screener page. ticker, run_date, run_type, concalls_available already correct.
- annual-report: AR FY2025-26 (149 pages) by direct HTTP from BSE AttachHis. AR FY2024-25 (151 pages) by direct HTTP, moved to other/.
- results: Q2 FY27 (filed 2026-11-14), Q1 FY27 (2026-07-31), Q4 FY26 audited (2026-05-27), all direct HTTP (BSE AttachLive/AttachHis, Referer set). The second Q2 filing (5f136ec7) is byte-identical to the first (95abefc3), so it sits in other/. The Q1 FY27 PDF has a sound text layer on page 1 only. Pages 2 to 4 were re-OCR'd with tools/ocr_repair.py (tesseract); the text sits beside the PDF as .ocr.txt. Q3 FY26 results (4 pages, same scan issue, not OCR'd) sit in other/.
- rating: CRISIL 2026-02-13 full rationale by direct HTTP, saved as .html, printed to .pdf with Playwright, plus a .txt extraction.
- announcements: found with the BSE announcements API (12-month window; browser UA, Origin and Referer headers). 10 files fetched by direct HTTP. Exact duplicates were dropped: several 2026-05-27 filings, the 2026-07-31 board outcome and the 2026-07-13 AGM notice are the same PDFs as the Q4 results and the AR. Boilerplate (trading window, Reg 74(5), newspaper ads) skipped. The 2026-04-24 stock exchange clarification query has no attachment on BSE.
- screening: KELTECH and SOLARINDS Excel exports re-run with the collector's own screener login function, headless, second attempt worked. Converted with the collector's xlsx_to_csvs. Four Data_Sheet CSVs, all populated.
- peer-concalls: SOLARINDS had no transcripts from the collector. Fetched from the BSE links on its screener Documents page by direct HTTP. The Aug 2026 "Transcript" link is an investor presentation, and the Sep 2026 call covers the Omnia acquisition only; both sit in other/.
- shareholding: BSE pattern page is blocked (Akamai Access Denied for curl and Playwright). Saved the screener shareholding table (quarterly and yearly) as csv. No pledge data in it.
- Empty folders (concalls, presentation, prospectus, research) hold .gitkeep. _download and _unclassified no longer exist.

Browser route: no file came through the Chrome browser fallback.

Gaps:
- Formal BSE shareholding pattern (promoter pledge, FII/DII breakdown for Sep 2026): not retrieved.
- Premier Explosives Q2 FY27 transcript: not published on screener yet at run time.
- SOLARINDS Q1 FY27 transcript: none exists on screener, only a presentation.

## Phase 1 orchestration (2026-11-15)
- Checkout guard: passed against origin/main b4ec38ce.
- Spear gate: passed on the OVERRIDE line in companies/KELTECH.md.
- LESSONS pre-read done. No lesson tagged for sector "Cables / Industrial products". No archetype declared yet.
- Tooling gate: the whole run reads pre-extracted page-marked .txt (tools/extract_pdfs.py). The rating .txt was re-extracted from the PDF; the HTML extraction is kept as *_html-extract.txt. The Q1 FY27 results .txt is the tesseract OCR text with [page N] markers.
- No file came through the Chrome browser fallback. The one remaining document gap (BSE shareholding pattern, Sep 2026) is not in the screener Documents section, so the fallback did not apply.
- Stage 0: the intake check proposed four moves out of inputs/other/. All four were confirmed at the page and deliberately not moved (contract caps). See B00-inputs.yaml.
- Empty-folder confirmation suppressed per /step1. Standing answer: proceed with the gaps.
- Verifier A shadow NOT run here. The single shadow run belongs to the TD Power session of this batch. .claude/shadow.yaml is untouched by this run.
- Subagent calls dispatch in the background in this harness. Completion is proven per stage by report and block files on disk before any later stage reads them.
