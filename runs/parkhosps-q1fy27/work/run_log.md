# RUN LOG — quarterly review: PARKHOSPS (Park Medi World Limited) Q1 FY27

Orchestrator: /run-quarterly. Operator: Keerti Kaushik. Run date: 2026-08-03.
Company: Park Medi World Limited | NSE: PARKHOSPS | BSE: 544645 | Sector: Hospitals.
Quarter under review: Q1 FY27 (quarter ended June 30, 2026).

## TOOLCHAIN PRECHECK
- pdftotext 24.02.0, pdfinfo, pdftoppm, tesseract: ALL PRESENT (installed poppler-utils + tesseract-ocr this session via apt).
- Read-tool PDF rendering NOT used as evidence spine (poppler unavailable at session start; installed before A1).

## PROTOCOL-FILE CHECK
- frameworks/Quarterly_Results_Review_Protocol_v1_2.md  PRESENT
- frameworks/Quarterly_Concall_Analysis_Protocol_v1_1.md PRESENT (no concall in docs; not exercised)
- frameworks/Master_Project_Prompt_v3.3.md              PRESENT

## INPUT DOCUMENTS (5 supplied, 4 unique)
| file in inputs/ | source upload | pdfinfo pages | md5(extract) | doctype decision | basis |
|---|---|---|---|---|---|
| results.pdf | 83b9baf5 | 15 | 7ccd30de... | results | Reg 30/33 Board Outcome + Unaudited Financial Results (std+consol) + Limited Review Report |
| (duplicate) | 40ccf173 | 15 | 7ccd30de... | — DROPPED — | byte-identical to results.pdf (same md5); not reprocessed |
| presentation.pdf | b92bb247 | 26 | — | presentation | Reg 30 Investor/Earnings Presentation Q1 FY27, slide structure |
| earnings_release.pdf | 68a74900 | 4 | — | release (enumerate as presentation/narrative) | Reg 30 Media Release / Earnings Release, page-based narrative + KPI table |
| monitoring_agency.pdf | 7b6f706d | 13 | — | monitoring (enumerate as results/regulatory) | Reg 32(6) CRISIL Monitoring Agency Report on IPO proceeds utilization |

Doctype tokens `release` and `monitoring` are descriptive labels to avoid extract-filename collision; A1/A2 run the closest canonical enumeration path (presentation for release, results for monitoring). Orchestrator wins on extraction discipline per prompts/quarterly-00-orchestrator.md L7-9.

## COMPANY MEMORY / NOTION
- companies/PARKHOSPS.md: ABSENT (fresh coverage; no prior operator rulings/tripwires).
- runs/ prior folders for parkhosps: NONE.
- Notion live fetch: SUCCESS. Page "Park Medi World Ltd" (COMPANIES MASTER). Decision Status WATCHLIST, entry ₹101-126, MoS ₹101, Position None, Promoter Verdict MONITOR. Full monitoring checklist + 4 thesis-broken triggers + FY26 baseline captured in work/notion_thesis_brief.md and passed inline to A3/A4.

## GATES LOG
- 2026-08-03: Setup complete. A1 x4 launched in parallel (results, presentation, release, monitoring).
- GATE A1 release: PASS. 4pp/4ff, 100% coverage, unit=Millions (x0.1 to Cr), no OCR needed.
- GATE A1 monitoring: PASS. 13pp/13ff, 100% coverage, unit=Millions. A1 already flags IPO medical-equipment object deviation (~Rs 229.59mn planned vs 36.08mn actual) for A3.
- GATE A1 presentation: PASS. 26pp/26ff, 100% coverage, unit=Millions, OCR pages [7,16,20,23] all section-divider photos (no hidden data), 10 charts flagged inline. CAVEAT: this agent deleted shared work/ocr_tmp belonging to the concurrent results A1 — verify results gate carefully; re-run results A1 if any gap.
(to be appended as each gate clears)
