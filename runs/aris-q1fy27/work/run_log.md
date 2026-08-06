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
- [ ] A1 results, A1 presentation (parallel)
- [ ] A2 results, A2 presentation
- [ ] A3 results, A3 presentation
- [ ] A4 merged
- [ ] A5 audit -> COMPLETE
- [ ] Notion save
- [ ] commit
