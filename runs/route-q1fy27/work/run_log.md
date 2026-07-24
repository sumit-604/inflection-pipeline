# Run Log — Route Mobile Q1 FY27 Quarterly Review

Run date: 2026-07-24
Ticker: ROUTE (Route Mobile Limited, BSE 543228 / NSE ROUTE)
Quarter: Q1 FY27 (quarter ended June 30, 2026)
Branch: claude/route-mobile-quarterly-pkqpxv

## Prechecks
- Protocol files: PRESENT (Results v1.2, Concall v1.1, Master v3.3)
- Toolchain: pdftotext/pdfinfo/pdftoppm/tesseract installed (poppler-utils + tesseract-ocr via apt)
- Company memory companies/ROUTE.md: ABSENT (Notion fetched live instead)

## Document classification (by content, per orchestrator Step d)
| Input file | Pages | Ref No | Class | doctype passed | filename stem |
|---|---|---|---|---|---|
| results_board_outcome_reg33.pdf | 12 | RML/2026-27/691 | Reg 33 Board Outcome + Unaudited Financial Results + Limited Review Reports | results | results |
| investor_presentation.pdf | 18 | RML/2026-27/693 | Investor Presentation | presentation | presentation |
| press_release.pdf | 3 | RML/2026-27/692 | Press Release (Q1 FY27 results announcement, mgmt narrative) | presentation-template | pressrelease |

## Orchestrator decisions
- No concall transcript supplied. Role 4 (results) runs fully; Role 5 has no transcript. Deck + press release feed Role 4.
- Press release: no native slide/note/turn structure. Enumerated with the INVESTOR PRESENTATION template (claims/numbers/footnotes as units), distinct `pressrelease` filenames to avoid collision with the investor deck.
