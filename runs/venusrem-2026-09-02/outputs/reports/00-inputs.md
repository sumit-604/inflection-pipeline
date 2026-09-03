# Stage 0 — Input Validation (VENUSREM 2026-09-02)

## Spear gate
OPEN. `companies/VENUSREM.md` carries `Spear: OVERRIDE 2026-09-02 (operator)`.
Load-bearing facts recorded in B00; every stage checks them first.

## Corpus verdict
CORPUS CURRENT (freshness pairs OK). All four freshness pairs PASS or SKIPPED.
No mate-document gap. Run mode: NO-CONCALL (concalls_available:false).

## Inventory
- annual-report: 2 (FY2025-26 current, FY2024-25 prior)
- results: 3 (Q3 FY26 Q/E Dec 2025; Q4/FY26 audited full-year 26 May 2026; Q1 FY27 20 Jul 2026)
- announcements: 4 (37th AGM 20 Aug 2026 outcome set)
- peer-concalls: 23 (BETA, CAPLIPOINT, GLAND, KILITCH, LINCOLN, SHILPAMED, WOCKPHARMA)
- screening: 48 (Data_Sheet fully populated; P&L/BS/CF/Quarters shells empty — v3 defect)
- research: 2 (non-anchored; rpt1.pdf image-only, unreadable)
- prospectus / rating / shareholding / presentation / concalls: empty

## Gaps recorded (operator chose PROCEED WITH GAPS)
- rating (MEDIUM): Pillar 2 conservative default; Venus near net-debt-free, may be unrated.
- shareholding (MEDIUM): FII+DII unresolved, UA withheld, promoter/pledge from AR.
- presentation (LOW): Stage 4 from AR + results.
- prospectus (NONE): long-listed, not expected.
- screener-csv-defect (LOW): Data_Sheet carries all quant; Gate 0 uses it + PDFs.
- sector_cap_row (LOW): "Pharma / CDMO" auto-picked; flag for phase-3 Section 1B confirmation.

## Pre-extraction
34 PDFs extracted to page-marked .txt (===== PAGE n of M =====). Stages read
.txt, cite p.N, PDF alongside for image fallback. rpt1.pdf image-only.

See outputs/blocks/B00-inputs.yaml for the full block.
