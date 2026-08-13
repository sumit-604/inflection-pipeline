# RUN LOG — quarterly review: FINKURVE (Arvog) Q1 FY27

Orchestrator: /run-quarterly
Run date: 2026-08-13
Company: Finkurve Financial Services Ltd (brand Arvog) | NSE FINKURVE | BSE 508954
Business class: NBFC — gold-loan lender (use 1L/5L lending variants per protocol v1.2)
Quarter detected: Q1 FY27 (quarter ended 30 June 2026)
Filing units: Rs in Lakhs (results) -> convert /100 to Rs Crores at extraction

## TOOLCHAIN PRECHECK
pdftotext / pdfinfo / pdftoppm / tesseract — MISSING at start; installed
poppler-utils + tesseract-ocr via apt (after apt-get update fixed stale index). All OK.

## PROTOCOL FILES (present)
- frameworks/Quarterly_Results_Review_Protocol_v1_2.md OK
- frameworks/Quarterly_Concall_Analysis_Protocol_v1_1.md OK (no concall supplied this run)
- frameworks/Master_Project_Prompt_v3.3.md OK

## DOCUMENT CLASS DETECTION
| input | pages | class | note |
|---|---|---|---|
| results_finkurve_q1fy27.pdf | 13 | results | Board Outcome + Unaudited Fin Results Q1FY27 + Limited Review Report (Reg 30/33/52/54) |
| presentation_finkurve_q1fy27.pdf | 37 | presentation | Analyst/Institutional Investor Meet deck (Reg 30) |
| reg32decl_finkurve_q1fy27.pdf | 2 | results (supporting) | Reg 32(1) use-of-proceeds declaration, preferential issue equity+warrants |

No concall document supplied. Role 5 not run this cycle; Role 4 (results) + presentation pre-processing only.

## COMPANY MEMORY
companies/FINKURVE.md — NONE (no local per-company memory file).

## NOTION (fetched live 2026-08-13)
Page: Finkurve Financial Services (Arvog) — 368bb2b9-d3ab-81eb-ad07-c62217ddc01a
Decision Status: WATCHLIST / AVOID (analysis dated 22 May 2026, CMP Rs 68)
Entry zone: Rs 25-31 | MoS Rs 25 (approx book)
Tripwires: (1) ROE fails to cross 14% by FY28; (2) GNPA above 1.5%; (3) dilutive equity raise below Rs 40; (4) price falls to ~Rs 30 (buy trigger)
Monitorables: NIM/CoF (~11.2% flat), LTV 72%, gold-price-driven growth, FY29 AUM target halved to Rs 5,000 Cr, D/E ramp to 4-4.5x, Augmont funnel activation, fee line (Rs 69.7 Cr expense pass-through), GNPA 0.09%/Stage-1 99%, Rs 40 Cr warrant cash FY27, Augmont RPT + extended-family governance (Prithviraj Kothari/RSBL probe)
Base FY27 model: AUM Rs 1,480 Cr, PAT Rs 43 Cr, EPS Rs 2.95, BV Rs 29.4, ROE ~11%

## STAGE STATUS
- [ ] A1 extract x3 (results / presentation / reg32)
- [ ] A2 ledger x3
- [ ] A3 forensics x3
- [ ] A4 merged review
- [ ] A5 adversary audit
- [ ] Notion save
- [ ] commit
