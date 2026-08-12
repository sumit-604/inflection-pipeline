# Run Log — Quarterly Analysis Pipeline: INDIQUBE Q1 FY27

**Ticker:** INDIQUBE (IndiQube Spaces Limited) | NSE: INDIQUBE | BSE: 544454
**Quarter:** Q1 FY27 (quarter ended 30 June 2026)
**Run date:** 2026-08-12
**Orchestrator:** /run-quarterly (quarterly-00-orchestrator v1.0)

## 0b. Protocol-file check
- frameworks/Quarterly_Results_Review_Protocol_v1_2.md — OK
- frameworks/Quarterly_Concall_Analysis_Protocol_v1_1.md — OK (not exercised; no concall supplied)
- frameworks/Master_Project_Prompt_v3.3.md — OK

## 0c. Toolchain precheck
- pdftotext, pdfinfo, pdftoppm — installed via apt-get (poppler-utils; initial index stale/404, resolved with apt-get update)
- tesseract — installed (tesseract-ocr 5.3.4)
- Read-tool PDF rendering NOT used as extraction substitute (per orchestrator rule).

## 0d. Document-class detection (from content, not filename)
| # | inputs/ file | Class | Basis |
|---|---|---|---|
| 1 | results_filing.pdf | results | Reg 33 board outcome + limited-review report + Statement of Unaudited Financial Results Q1FY27 |
| 2 | press_release.pdf | presentation | Reg 30 press release; curated management numbers + Ind AS↔IGAAP reconciliation table + operational KPIs |
| 3 | investor_presentation.pdf | presentation | 35-slide deck (pdfinfo), chart/KPI-heavy |
| 4 | monitoring_agency_report.pdf | results | Reg 32(6) CRISIL Monitoring Agency Report; tabular IPO-proceeds utilisation disclosure |
| 5 | agm_proceedings.pdf | results | Reg 30 summary of 12th AGM proceedings (Aug 12 2026); board/governance corporate action |

No concall transcript in scope — earnings call scheduled Thu 13 Aug 2026 (per press release), after this filing set. Role 5 not exercised this run.

## 0e. Run folder
- runs/indiqube-q1fy27/inputs/ (5 source PDFs staged)
- runs/indiqube-q1fy27/work/ (agent artifacts)

## 0f. Company memory + live Notion thesis (passed inline to A3/A4)
- companies/INDIQUBE.md — does NOT exist (new to pipeline; IPO listed 30 Jul 2025). First quarterly pipeline run for this ticker → no prior-quarter A1/A2 artifacts for verbatim diff.
- Notion page fetched LIVE (2026-08-12): "IndiQube Spaces Ltd" (id 36cbb2b9-d3ab-81e3-8872-f83fdddc261e).

### Live Notion thesis snapshot
- **Decision Status: AVOID** (WATCHLIST branch). Position Size: None.
- Entry zone: ₹110–₹138 (₹138 = 25% CAGR entry; ₹110 = Margin of Safety). CMP baseline ~₹170.
- Destination PE: 18–20x sector-capped (real estate). Current ~28x IGAAP.
- IGAAP-override framework applied (Ind AS 116 distorts statutory metrics — capitalises ~₹4,714–4,917 Cr landlord rent as lease liability → optical losses, inflated debt, depressed ROCE). Economic quality GOOD+.
- Governance overlay is the binding AVOID constraint, not fundamentals. FTTCP baseline: 3-of-4 transitions firing + 1 partial.
- Management Grade A (operational), held pending Q1 FY27 concall restatement test (7 of 10 Q4 forward numerics DROPPED in AR narrative; 2+ DROPPEDs triggers downgrade to B).

### Quarterly Monitoring Checklist (Notion) — GREEN / RED tripwires
1. Occupancy (RPA basis): >83% sustained / <80% for 2 consecutive Qs
2. IGAAP-adjusted PAT: positive & growing YoY / turns negative
3. Related-party transactions: RPT declining, no new promoter entities / any new promoter-linked RPT
4. Auditor & board: clean unmodified opinion, stable board / qualification or resignation
5. Net debt (IGAAP ex-lease): <0.5x IGAAP EBITDA / >1.5x without clear ROI
6. VAS share of revenue: crossing 15%+ / stalling below 12%
7. CMP vs IGAAP EPS: re-rates, enters ₹110–138 / CMP > ₹200

### Pre-committed Top-3 Q1 FY27 questions (from AR review, 08 Jul 2026)
1. Innoprop trade receivable ballooning (₹4→₹14 Cr, 3.5x vs ~₹5 Cr annual invoicing) — driver & collection expectation
2. Prior auditor identity & transition rationale (pre-WCCL; Big-4 exit claim unverified)
3. IPO proceeds ₹374 Cr unutilized — FY27 deployment plan & any promoter-linked recipient anticipated

### Active governance flags carried in
- Innoprop Spaces (promoter-linked) RPT confirmed; Grub Group F&B RPT verified ₹27.14 Cr FY26 (+28% YoY, partnership firm).
- Commingling (CEO personal a/c) + Big-4 auditor resignation — UNVERIFIED.
- CS turnover high (3 in 15 months); audit-trail deficiencies (Note 42).
- Promoter+group holding 60.10% post-IPO.

## Prior-quarter artifacts
NONE — first pipeline run for INDIQUBE. A2 PRIOR_LEDGER_PATH and A3 PRIOR_EXTRACT_PATH passed as NONE; F5 verbatim auditor-diff runs best-effort against Notion memory only, flagged where memory (not a prior extract) is the sole reference.

## Agent dispatch plan
Full A1→A2→A3 chain on all 5 documents (keeps A5 coverage audit consistent — every extract carries a ledger). Then A4 once (merged, Role 4 only — no concall), then A5 once.
