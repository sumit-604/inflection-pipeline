# RUN LOG — /run-quarterly ARIS Q1 FY27 (SPRA quarterly pipeline)
Orchestrator session. Run date 2026-08-06.

## 0. SETUP & PRECHECKS
- **Ticker:** ARIS (Arisinfra Solutions Ltd), Scrip 544419, NSE/BSE.
- **Quarter:** Q1 FY27 (quarter ended 30-Jun-2026).
- **Toolchain precheck:** pdftotext, pdfinfo, pdftoppm, tesseract — MISSING at
  start; installed poppler-utils + tesseract-ocr via apt. All four now present.
- **Protocol-file check:** all present —
  frameworks/Quarterly_Results_Review_Protocol_v1_2.md,
  frameworks/Quarterly_Concall_Analysis_Protocol_v1_1.md,
  frameworks/Master_Project_Prompt_v3.3.md.
- **Company memory:** companies/ARIS.md does NOT exist. Prior runs: none.
- **Notion:** live page found ("ArisInfra Solutions Ltd"). Decision Status =
  HELD 4% at Rs 106. Fetched and digested to work/notion_thesis_aris_q1fy27.md.
  This Q1 FY27 result is the pre-committed MASTER MONITORABLE test (debtor days).

## DOCUMENT-CLASS DETECTION (from content, per orchestrator step d)
| input file | pages | detected class | evidence |
|---|---|---|---|
| aris-q1fy27-results-filing.pdf | 10 | **results** | Reg 30/33 Board Outcome; "Unaudited Financial Results"; Limited Review Report |
| aris-q1fy27-investor-presentation.pdf | 42 | **presentation** | slide structure; "Investor Presentation" cover |
| aris-q1fy27-press-release.pdf | 4 | press release (Reg 30) | "Announcement under Regulation 30 - Press Release" |
| aris-q1fy27-esop-intimation.pdf | 3 | ESOP grant intimation (Reg 30) | NRC approved grant of 1,633 options under ESOP-2024 |

## SCOPING DECISION (documented per orchestrator rule 11 + non-negotiables)
The pipeline doctype taxonomy is {results | concall | presentation}. Two of the
four documents map cleanly and go through the full A1->A2->A3 chain:
  - results filing  -> A1/A2/A3 (doctype results)
  - investor presentation -> A1/A2/A3 (doctype presentation)
No concall was supplied (earnings call is scheduled 06-Aug-2026, today; no
transcript exists yet) -> Role 5 / concall chain N.A. this run.
The press release and the ESOP intimation are short same-day Reg 30 ancillary
disclosures whose content does not map to the enumerable disclosure units the
A2/A3 checklists are built around (notes / turns / slides). They are extracted
mechanically to line-numbered text (work/extract_pressrelease_*.txt,
work/extract_esop_*.txt) and passed to A4 as supplementary evidence so nothing
is dropped: A4 cross-checks the press release's headline claims (37% revenue,
~4x PAT, 10.49% EBITDA margin) against the filing numbers (anti-miss), and logs
the ESOP grant (1,633 options) against monitoring item #7 (dilution) and F10.

## SEQUENCE STATUS
- [x] A1 results (610 lines, 10pp), A1 presentation (1251 lines, 42pp, OCR 6 slides) — GATE A1 pass
- [x] A2 results (16 notes/77 items/8 entities/13 auditor paras), A2 presentation (42 slides/211 numbers) — GATE A2 pass
- [x] A3 results (11 findings), A3 presentation (9 findings) — GATE A3 pass
- [x] A4 merged review — PROCEED WITH CAVEATS; cash INDETERMINATE; HELD (no add)
- [x] A5 audit — loop 1 INCOMPLETE (segment arithmetic + EPS caveat) -> A4 fixed;
      loop 2 INCOMPLETE (slide-36 period-mapping: 3,437=Q4FY26 not Q1FY27) -> A4 fixed;
      loop 3 (final) COMPLETE. Two loops used (max two); verdict COMPLETE.
- [ ] Notion save — PENDING operator go-ahead (outward-facing append to live thesis page)
- [x] commit (incremental, each stage) + push

## OPERATIONAL NOTES (for the record)
- Toolchain (poppler-utils, tesseract) was missing at session start; installed via apt.
- The A1 results extractor ran a broad `rm -f page-*.jpg page-*.txt` in the SHARED work/
  directory and deleted the concurrently-running presentation extractor's temp OCR files.
  No damage resulted (presentation A1 completed with its extract intact), but concurrent A1
  invocations share work/ — temp OCR files should be namespaced per doctype, not globbed.
- A5 final audit noted ONE non-propagating raw discrepancy: consolidated Other Expenses
  Q1FY26 comparative on OCR-suspect line l.486 (5.94 vs 7.94 Cr in the A2 ledger). It does
  not feed any derived Q1FY27 metric (Total Expenses l.487 is independently anchored);
  verify at source in the H1/AR. Not a blocker; verdict COMPLETE.
- Verdict summary: PROCEED WITH CAVEATS. Master monitorable (debtor days) UNCOMPUTABLE this
  quarter (P&L-only filing, no Q1 balance sheet). No thesis-broken trigger fired. HELD, no add.

## Role 5 Concall Analysis — 06-Aug-2026 (appended post-call)
- Concall held 06-Aug (~1 day after 05-Aug filing; canned window). Transcript operator-pasted.
- First concall under Role 5 protocol → Promise-vs-Delivery tracker initialised (no prior to score); credibility ratio N/A this quarter.
- Promoter (CMD Ronak Morpia) present = GREEN. Audience retail/small-broker heavy, no institutional buy-side, softball-dominated = orchestration yellow flag.
- Net thesis impact: MAINTAINED. Verdict unchanged: PROCEED WITH CAVEATS, cash INDETERMINATE, HELD, HOLD/NO ADD.
- Resolved/updated: seasonality explained (H1 40%/H2 60%, Q1-Q2 lean) softens QoQ-deceleration concern; CM utilization now point 65-70% (#3 AMBER->GREEN-ish); Wadhwa 650cr confirmed = GDV not revenue.
- Still open: debtor days + >6-mo aging NOT disclosed (NWC days 56 given instead); zero-ECL-this-Q vs 4.46cr Q4 not reconciled (lifetime 0.5% offered).
- NEW flags: (a) NWC days internal contradiction 66 (opening) vs 97 (Q&A) for Mar-26; (b) ~80cr swing from net cash (~65cr Mar) to net debt (14.5cr Jun) in one quarter, unexplained by hard numbers, no CFS; (c) part of margin gain from SCF early-payment discounts, not pure mix; (d) dash GDV take-rate REFUSED ("take offline").
- Artifacts: work/extract_concall_aris_q1fy27.txt, work/review_concall_aris_q1fy27.md.
