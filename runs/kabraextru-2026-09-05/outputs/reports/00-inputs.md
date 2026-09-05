# Stage 0 — Input validation: KABRAEXTRU 2026-09-05

Run folder: runs/kabraextru-2026-09-05. Manifest parsed. Run type full.
concalls_available: false, so NO-CONCALL MODE. CMP Rs 579.0, market cap Rs 2,025 Cr.

## Spear gate
No companies/KABRAEXTRU.md existed. /run-pipeline was invoked directly on the
collector corpus (PR #151, corpus commit 8374c2f); no step1 brief exists. The
orchestrator recorded "Spear: OVERRIDE 2026-09-05 (operator standing ruling
2026-09-05: Step-1 intake replaces the web spear)" per step1.md section G, with
four verification priorities drawn from the manifest notes and the screener
Data_Sheet (memory, never anchored evidence).

## Inventory
| folder | count | detail |
|---|---|---|
| prospectus | 0 | long-listed (43rd AGM); not expected |
| annual-report | 2 | FY2025-26 (170pp, primary) and FY2024-25 (168pp, prior year) |
| results | 0 | HIGH gap; screener shows quarters to Jun-2026 |
| rating | 0 | HIGH gap; AR FY26 discloses CRISIL downgrades, rationale absent |
| concalls | 0 | declared absent |
| peer-concalls | 5 | RAJOOENG May-2023, Nov-2023, Apr-2024, Nov-2025; HBLENGINE Sep-2025; no WINDMACHIN transcript |
| announcements | 0 | gap |
| shareholding | 0 | gap |
| research | 0 | .gitkeep planted |
| screening | 24 | main + 3 peers; only Data_Sheet CSVs populated |
| presentation | 1 | Q3 FY24 deck (Dec-2023), stale |

## Freshness pair check
Pair 1 skipped (no calls). Pair 2 FAIL: the AR FY26 credit-rating disclosure
names CRISIL downgrades to A-/Stable and A2+ (w.e.f. 13-May-2026) and the
rationale is absent. Pair 3 PASS. Pair 4 PASS. Verdict: CORPUS GAPPED-FRESHNESS.
The gate recommendation caps at PROCEED WITH CAVEATS; the CRISIL rationale is
the first line of gate-recommendation.md.

## Tooling
pypdf cffi backend repaired; poppler-utils installed; Read-tool PDF render
verified on the presentation. All 8 PDFs pre-extracted to page-marked .txt twins.

## Operator confirmation
Empty-folder question asked once. Operator: proceed with the gaps (2026-09-05).
