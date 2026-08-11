# RUN LOG — EXICOM Q1 FY27 Quarterly Analysis Pipeline

Run date: 2026-08-11
Ticker: EXICOM (Exicom Tele-Systems Limited)
Quarter: Q1 FY27 (quarter ended June 30, 2026)
Operator: Keerti Kaushik / Inflection Alpha

## TOOLCHAIN PRECHECK
- pdftotext, pdfinfo, pdftoppm, tesseract: ABSENT at session start.
- Installed poppler-utils + tesseract-ocr via apt-get (2nd attempt after apt-get update). VERIFIED present. PASS.
- (Recurrent LESSONS.md pattern: PDF tooling absent at session start.)

## PROTOCOL-FILE CHECK (all present)
- frameworks/Quarterly_Results_Review_Protocol_v1_2.md  ✓
- frameworks/Quarterly_Concall_Analysis_Protocol_v1_1.md ✓
- frameworks/Master_Project_Prompt_v3.3.md              ✓

## DOCUMENT CLASS DETECTION (by content, not filename — filenames were misleading)
| # | Original filename | Pages | Detected class | Decision basis | Run action |
|---|---|---|---|---|---|
| D1 | eaa100a3-…8df53935ca4448e.pdf | 10 | results | Reg 30 "Outcome of Board Meeting" + Reg 33 Unaudited Financial Results + both auditor limited-review reports + segment tables + Board agenda items (RPT, AGM notice). Most complete. | results = inputs/results_board_outcome.pdf |
| D2 | 67a18825-…87edffc.pdf | 38 | presentation | "Investors' Presentation" slide deck, chart-heavy | presentation = inputs/presentation_investor_deck.pdf |
| D3 | fea9c6f5-Pace_DigitekRHP.pdf | 4 | presentation (press release) | Despite filename, content is Exicom "Press Release on Unaudited Financial Results Q1 FY27". Unique quantified claims (AC +35% YoY, GM 31.7% vs 39.4%, capacity doubling Q3). | pressrelease = inputs/press_release.pdf |
| D4 | (operator chat paste) | n/a | concall | Speaker-turn earnings-call structure, Monarch Networth-hosted, Aug 10 2026 | concall = inputs/concall_transcript.txt |
| — | 472698a6-…009b8b02.pdf | 9 | results (DUPLICATE) | Strict subset of D1: identical financial results statement + auditor reports; lacks the Board agenda items. Confirmed same "Profit/(Loss) for period" figures. NOT re-run to avoid redundant chain; noted here. | inputs/results_financials_duplicate.pdf (reference only) |

Note: filenames as uploaded do NOT correspond to their content (the file named
"Pace_DigitekRHP.pdf" is Exicom's press release). All four PDFs are Exicom Q1 FY27 filings.

## COMPANY MEMORY
- companies/EXICOM.md: ABSENT (no durable per-company memory file yet).
- Notion page "Exicom Tele-Systems" (id 345bb2b9-d3ab-80a9-8b02-efef533e1865): FETCHED LIVE. See prior_context.md.

## PIPELINE PLAN
A1→A2→A3 per document on D1 (results), D2 (presentation deck), D3 (press release), D4 (concall).
Then A4 merged review (Role 4 first, Role 5 second), then A5 adversary, then Notion save + commit.

## RUN CLOSE — 2026-08-11
- Chain complete: A1 (4 docs extracted) → A2 (4 ledgers, count-tests reconciled) → A3 (4 forensics, 17-check) → A4 (merged Role 4/5 review) → A5 (adversary).
- A5 VERDICT: COMPLETE. No loop-back required. One advisory (immaterial Rs0.10 Cr consol expense-line OCR gap) logged for next run's A2.
- A4 verdict: PROCEED WITH FLAGS. Cash-conversion axis INDETERMINATE (no CFS in Reg 33 half-yearly filing) → capped at PROCEED WITH CAVEATS; PROCEED WITH FLAGS is strictly more conservative, cap honoured.
- Pre-committed print: BEAR (consol quarterly EBITDA −Rs21.9 Cr < −Rs20 Cr threshold). Q4FY26 breakeven reversed.
- Management archetype: OVERPROMISER-WATCH; credibility held provisional Grade B with formal watch (Q2 miss → C).
- Decision Status: WATCHLIST hold (flag, not decide). Master gate pushed to Q2 FY27. Human decides.
- Notion save: page 345bb2b9-d3ab-80a9-8b02-efef533e1865 — Role 4, Role 5, A3 scorecard, silence audit all verified present.
- LESSONS.md: absent in this clone; no append target. Recurrent PDF-tooling-absent pattern noted in TOOLCHAIN PRECHECK above.
