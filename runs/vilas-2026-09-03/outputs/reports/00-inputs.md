# B00 — Input Validation and Corpus Audit — VILAS

Run: vilas-2026-09-03 | Operator: Keerti Kaushik | Orchestrator stage 0.

## Spear gate
Spear: OVERRIDE 2026-09-03 (operator). Gate satisfied. Run proceeds.
Framing (operator ruling 2026-09-03): the run answers "is this worth
tracking to Rs 227", not "is this a buy today". Spear verdict WATCH at
CMP Rs 353, entry Rs 227.

## Manifest
- company: Vilas Transcore Ltd | ticker: VILAS
- cmp: 349.0 (manifest) / Rs 353 (operator live, 02-Sep close)
- market_cap_cr: 854 (manifest) / Rs 864 Cr (operator live)
- run_date: 2026-09-03 | run_type: full | concalls_available: true
- sector_cap_row: "Pharma / CDMO" — WRONG. Auto-picked by collector.
  VILAS is a CRGO / electrical-steel converter. Carry CONVERTER
  (Amendment 17). Flagged for correction at stage 10 (phase 3).
- listed: FY24 (FY25 AR: "our first full financial year as a listed
  company"). Recently listed, within ~3 years. Prospectus MANDATORY to
  attempt; its absence is a HIGH gap.

## Anchors carried (operator-verified live, not re-derived)
CMP Rs 353 | Mkt cap Rs 864 Cr | 2.448 Cr shares | FY26 Revenue Rs 460.7 Cr |
EBITDA Rs 51.5 Cr (11.17%) | PAT Rs 39.6 Cr | EPS Rs 16.16 | P/E 21.8x |
ROCE 16% | Book value Rs 134 | FY26 CRGO 19,856 MT vs 36,000 MTPA (55%).

## Folder inventory
| Folder | Count | Files used | Note |
|---|---|---|---|
| prospectus | 0 | none | ABSENT. HIGH gap (listed FY24). FY20-FY22 restated not in corpus. |
| annual-report | 2 | FY25 (SME_AR..2024_2025), FY24 (Annual_Report_2024) | Latest AR = FY25. FY26 AR NOT filed. |
| results | 2 | H1 FY26 (13-11-2025), FY26 audited (11-05-2026) | Both used. |
| rating | 1 | ICRA 14-Jul-2025 (136305.pdf) | Full rationale, 7 pp. Reaffirmed A-(Stable)/A2+. |
| concalls | 4 | May-2025, Nov-2025, May-2026 (3 most recent, oldest first) | Nov-2024 available, not in top-3 (contract cap 3). |
| peer-concalls | 12 | 544310 (4), JAYBEE (4), PITTIENG (4) | 3 peers with calls. RAMRAT has screening only. |
| presentation | 1 | Investor_Presentation FY26 (11-05-2026) | Ind-AS restated, unaudited FY26 optics. |
| research | 3 | rpt1, rpt2, operator ops digest | NON-ANCHORED, leads only. |
| screening | 6 (company) | screener-*.csv | Plus peer CSVs (544310/JAYBEE/PITTIENG/RAMRAT). |
| shareholding | 1 | operator-ferried screener table (Mar 2026) | Aggregator tier. Primary SHP filing absent. |
| announcements | 1 | GPCB CCA 01-05-2026 (operator-ferried) | PARTIAL. No primary Reg-30 PDFs (AGM text, raises). |
| other | 0 | none | n/a |

## Concall quarter map (chronological, confirmed by filename)
1. Concall_May_2025 -> FY25 full year (ended 31-Mar-2025)
2. Concall_Nov_2025 -> H1 FY26 (ended 30-Sep-2025)
3. Concall_May_2026 -> FY26 full year (ended 31-Mar-2026)
(Concall_Nov_2024 -> H1 FY25; available, not passed to stage 5.)

## Input gaps
- prospectus: ABSENT, HIGH (listed FY24). Backward baseline built on
  post-listing years (FY24-FY26) plus corpus FY23 from FY24 AR. FY20-FY22
  restated NOT IN CORPUS. Extraction 4 FY20-FY22 leg rests on operator
  spear numbers (memory tier). Group map web/AR-derived, not DRHP-anchored.
- FY26 annual report: ABSENT. Freshness mate to the FY26 audited annual
  results. Drives CORPUS GAPPED-FRESHNESS (below).
- announcements primary PDFs: ABSENT except GPCB CCA (ferried). Documented-
  action record thin; intent-and-action cross-check runs on concall/AR/
  ferried-event evidence.
- shareholding primary SHP filing: ABSENT. Aggregator table ferried;
  affirms holding trend and UA qualifier with provenance; pledge not shown.

## Freshness pair check
| Pair | Trigger | Mate expected | Status | Missing |
|---|---|---|---|---|
| 1 Results->Concall | FY26 results (11-05-2026) | FY26 concall (12-05-2026) | PASS | none |
| 2 Rating->Rationale | ICRA bulletin | Full rationale | PASS | none (full rationale present) |
| 3 SEBI order->text | none referenced | order text | PASS | none (no trigger) |
| 4 AR->latest audited annual | FY26 audited annual results (11-05-2026) | FY26 AR | FAIL | FY26 annual report |

freshness_verdict: CORPUS GAPPED-FRESHNESS.
Consequence: gate recommendation caps at PROCEED WITH CAVEATS regardless
of flag count. FY26 annual report is named as the FIRST line of
gate-recommendation.md. Expected source: BSE SME / company filing once the
FY26 AR is published (FY26 audited results already filed 11-05-2026).

## Corpus audit verdict
CORPUS GAPPED-FRESHNESS. FY26 visible only through the audited results
filing (11-05-2026), the investor presentation (11-05-2026, unaudited
restated optics), and the May-2026 concall. The FY26 annual report, its
notes, RPT table, and segment disclosures are not yet in corpus. Latest
full AR in corpus is FY25. Prospectus HIGH gap stacks on this.

## Priority extractions carried to stage 09b (operator ruling 2026-09-03)
The ten Standing Extraction Annex questions were answered off-session on
2026-09-03; NOT re-run this pass. Stage 09b Section 6 instead answers the
operator's five priority extractions (corpus only, quote-then-comment,
filename+page anchor, NOT DISCLOSED where silent):
1. FY24 and FY25 segment/product revenue with CRGO tonnage -> per-kg
   realisation series FY23-FY25.
2. Single-customer concentration (ICRA: one customer 40-55% for 4 yrs);
   find whether any company filing names/quantifies it, else NOT DISCLOSED.
3. Atlas Transformers full transaction history FY23-FY25 both directions,
   plus FY25 AGM resolution text on the Rs 65 Cr RPT limit.
4. WC / inventory / receivable days FY23-FY25 from corpus (FY20-FY22 not
   in corpus): confirm or overturn the spear STRUCTURAL ruling.
5. Capex schedule: spent, on what, CWIP remaining. FY26 capex Rs 60 Cr,
   FY27 guided Rs 30-40 Cr.

## Credibility split carried (operator, binding)
TRUST physical build and volume (4/4 plants; Units 1+2 above nameplate).
HAIRCUT rupee revenue guidance (CRGO price is ~2/3 of revenue misses) and
new-line timelines by 2-4 quarters. Grade by category, do not collapse.
