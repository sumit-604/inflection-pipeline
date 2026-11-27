## Corpus collection (Step F)

Date: 2026-11-15. Company: Premier Explosives Ltd (PREMEXPLN, BSE 526247). Peers: SOLARINDS, BDL, ASTRAMICRO.

### What the collector got (collect_to_repo.py --dry-run, via wrapper)
- Manifest: cmp 578.0, market_cap_cr 3108.0, concalls_available true. Not edited.
- collector_warnings (4): shareholding empty; screener export sheets EMPTY except Data_Sheet (P&L, Quarters, Balance Sheet, Cash Flow, Customization have formulas with no cached values); no results PDFs; no rating PDF.
- annual-report: AR FY2025-26 (46th AR, filed 3 Sep 2026, 218 pp) and AR FY2024-25 (45th AR, filed 6 Sep 2025, 216 pp). Year confirmed from the covering letter on page 1.
- concalls: four transcripts (Aug 2026, Jun 2026, Feb 2026, Nov 2025). Presentation: Q2 FY27 deck (12 Nov 2026, 25 pp). Announcements: 16 BSE files. Screening: Data_Sheet CSV only.
- Peers: collector pulled only annual reports and presentations for peers, then deleted _download. No peer transcripts came through.
- BSE API (api.bseindia.com) returned 403 Access Denied to scripts today, so the 12-month announcement list was not available from BSE.

### Repairs and sources
- Announcements: NSE corporate-announcements API (nseindia.com, cookie session) for 16 Nov 2025 to 15 Nov 2026 gave 73 items; 64 PDFs downloaded from nsearchives.nseindia.in (9 are .zip open-offer attachments, not downloaded: idx 4, 7, 8, 27, 30, 31 zips, and 3 items with no attachment). Six more items from 2025 (outside the window, relevant): 4 Jan 2025 Peddakandukur fire intimation, 30 Apr 2025 Katepally fire and explosion intimation, 3 Jun 2025 TGPCB revocation order, 16 Sep 2025 Revocation of Closure Orders, 16 Sep 2025 credit rating, 11 Nov 2025 order win. Filenames use the `prior-window` tag.
- Present in announcements/: 9 Jul 2026 Apollo Micro Systems SPA board outcomes and press release (20260709-33/34/35), 10 Jul 2026 open-offer public announcement notes, 22 Apr 2026 export order cancellation, order wins (5 May, 22 Apr, 21 Jan 2026, 24 Nov 2025), 31 Jul 2026 KMP/director resignations, 1 Nov 2026 director change, 6 Nov 2026 post-offer advertisement, 21 May 2026 credit rating letter.
- No fire, accident or licence-suspension intimation exists in the 16 Nov 2025 to 13 Nov 2026 NSE feed. The accident disclosures found are dated Jan and Apr 2025. The FY26 results note an accident loss (about Rs 609.80 lakhs in Q1 FY27 filing, Rs 709.80 lakhs of machinery and buildings in Q4 FY26 filing) and the AR Directors' Report names an Accident at Katepally. PENDING LIVE VERIFICATION: a TGPCB closure order of a C-11 building (Times of India) is not dated in my capture; no filing found.
- Results (3): Q2 FY27 (12 Nov 2026), Q1 FY27 (13 Aug 2026), Q4/FY26 audited (29 May 2026). Source NSE. Face unit: "Rs in lakhs". AR unit: "Rs. in lakhs".
- Concalls (3 kept): Q1 FY27 (call 14 Aug 2026, transcript filed 20 Aug), Q4 FY26 (filed 2 Jun 2026), Q3 FY26 (call 20 Feb 2026). Nov 2025 transcript (Q2 FY26) moved to other/.
- Q2 FY27 transcript: NOT yet published. The call was held 13 Nov 2026; NSE shows only the recording link (13 Nov). Screener's "Nov 2026" row has the audio and PPT; its transcript link points to the August transcript (dated 20 Aug 2026). FRESHNESS GAP: record it.
- Presentation: Q2 FY27 deck already in presentation/ (identical bytes to the 12 Nov 2026 BSE filing).
- Rating: Indian rating agencies publish web releases, no PDF. Saved the full text from the India Ratings public API (pressrelease/84558): 21 Jul 2026, IND A-/IND A2+ placed on Rating Watch with Developing Implications after the Apollo SPA; and the 20 May 2026 release (83114), which holds the full rationale: IND A-/Stable affirmed, additional limits. ICRA (older) shows "Ratings withdrawn"; not saved. Both files are secondary text captures, not PDFs.
- Shareholding: NSE SHP XBRL for Sep 2026 (filed 9 Oct 2026) saved as .xml: promoters 41.33%. Plus a screener text capture (secondary) of both shareholding tables. Government holding appears at 2.94% in Sep 2026; check at Halt 1.
- Peer concalls: SOLARINDS (Q2 FY27 call 4 Nov 2026, Q4 FY26, Q3 FY26, Q2 FY26) and ASTRAMICRO (Q1 FY27, Q4 FY26, Q3 FY26, Q2 FY26), downloaded by BSE AnnPdfOpen links from each peer's screener page. SOLARINDS Sep 2026 transcript is the Omnia Holdings acquisition call, not an earnings call: moved to other/. BDL: no transcripts exist on screener (PPT only) or in the NSE feed since Jan 2024. GAP.
- Screening: Data_Sheet populated (63 rows). Number of shares row is blank. The other screener sheets (Profit & Loss, Quarters, Balance Sheet, Cash Flow, Customization) produced no CSV: EMPTY. The Data_Sheet carries the same history, so it is a note rather than a block.

### Chrome browser fallback
No document came through the Chrome download path. I used a new tab in the operator's Chrome only to read the document links on the screener documents section and to see the India Ratings network calls. A script call that read the BSE API from inside the page was blocked by the permission classifier, so I did not use it. The tab is closed.

### Verification and OCR
- Every PDF opens with pypdf (page count above 0). First pages confirm issuer, type and period for all main-company files.
- extract_pdfs.py then check_extraction.py: core documents OK. 12 announcement files were BLANK or GARBLED (scanned): Reg 29 and 31(4) takeover disclosures, newspaper publications, 21 Aug 2026 open offer update, and four BSE open-offer files. All re-OCR'd with tesseract through ocr_repair.py (200 dpi): all exit 0. The check tool still prints "no [page N] markers" for the OCR output (the OCR files use a different header); text is readable.
- A 218-page duplicate of the FY26 AR in announcements/ was removed (same hash as annual-report/).

### Remaining gaps
- Q2 FY27 concall transcript not yet filed (freshness).
- BDL transcripts: none exist.
- BSE API blocked (403); announcement list taken from NSE.
- Zip attachments for open-offer items not opened (untrusted); the open-offer PDFs for 5 Oct, 8 Oct and 20 Jul 2026 are in zips only.
- No rating PDF (agency publishes web text).
- Screening: five screener sheets empty.

## Orchestrator notes (Phase 1)
- Identity (Step A): PREMEXPLN, https://www.screener.in/company/PREMEXPLN/consolidated/ (check_url OK after one 429 retry).
- Steps B, C, D ran on an Opus 5.5 subagent with live web (operator batch instruction). Step F ran on a Sonnet 5.5 subagent.
- Verifier A shadow: NOT run here. Nine /step1 sessions run in parallel on 2026-11-15 and the single shadow run belongs to the TD Power session (operator batch instruction). .claude/shadow.yaml is not touched by this run; manifest carries verifier_a_shadow: skipped.
- EMPTY-FOLDER CONFIRMATION suppressed under /step1 (standing answer: proceed with the gaps).
- Text route: every inputs/ PDF has a page-marked .txt beside it; stages and verifiers read the .txt and open the PDF page where text is garbled.
- FLAG-DISAGREEMENT settled (B02 rank 3 vs B03): over-one-year receivables FY26 = 1,186.73 L (AR Note 11); B02's 888.35 L was the over-two-year sum. Erratum appended to 02-notes.md, 02-notes-pass2.md and B02-notes.yaml (orchestrator_corrections).
- Stage 1 report erratum appended (garbled other-income line; stage agent reported it).
- SEBI freshness pair re-checked after stage 3: the only SEBI order in the AR is Exemption Order WTM/KCV/CFD/18/2025-26 (8 Jan 2026); its text is in inputs/announcements/20260220-61-General-Updates. Pair stays PASS.
- Stages 6 and 7 first invocations stalled (stream watchdog, no progress for 600s; API-side). Mechanical re-invoke, run# 2 each.
- Stage 6: the stalled run had already written a complete report (closed YAML block) and a parsing block file; accepted from disk per 7A. Its token usage was not reported (n/a). Stage 7 re-invoked.
- Verifiers A, B, C (phase 1 scope), D each ran once (manifest verifier_runs 1 each). Completion check passed for all four. Verifier A identity check: no CRITICAL rows, nothing struck. No REWORK trigger. No remediation cycle run (remediation_cycles stays 0).
- Verifier B and C block `model` fields read claude-opus-5-5, matching the agent frontmatter.
- Verifier C reported a prompt defect: prompts/12-verifiers-pipeline.md line 379 holds patch text instead of the YAML key. Not edited here (framework files travel on their own branch); recorded in LESSONS_ARCHIVE.md.
- Confidence delta: overall 73 set by redflag_coverage; peer_utilisation not applicable (denominator 3).
