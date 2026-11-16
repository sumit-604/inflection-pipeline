# SFL — Sheela Foam Ltd
Run folders read: runs/sfl-2026-07-14 (origin/main), runs/sfl-q1fy27 (origin/claude/sheela-quarterly-results-zxbbvj)
Company file: companies/SFL.md (origin/main)

## Our base case
| Revenue CAGR | 8% | 12% | 15% |   (Bear | Base | Bull)
| Core EBITDA margin FY30 | 12.0% | 13.5% | 15.0% |
Source: origin/main:runs/sfl-2026-07-14/outputs/reports/B11.md §2A/2B L121-122
"Revenue base FY26 = Rs 3,820.84 Cr."  Source: same file L129
| FY26 (actual) | 14.62 | 14.62 | 14.62 |
| FY27 | 17.6 | 21.5 | 25.4 |   (reported EPS Rs/share)
| FY29 (exit yr) | 26.6 | 38.3 | 48.9 |
Source: same file §2C L135-138
"SOM crosscheck: base rev CAGR 12% < SOM-implied 15.6% → consistent."  Source: same file L143
"Forward EPS not guided → derived from revenue x margin guidance, grade-B discounted"  Source: same file (YAML block) L334
Fair values Year-3 Track 1 Bear 549 / Base 884 / Bull 1,243. Source: same file L265
Quarterly Bear/Base/Bull in the Q1 review: "Explicit Bear/Base/Bull quarterly projection numbers were not passed inline to this agent → marked ND"
Source: origin/claude/sheela-quarterly-results-zxbbvj:runs/sfl-q1fy27/work/review_sfl_q1fy27.md §6A L322

## Management guidance and promised catalysts
guidance: {item: "Top-line growth target", number: "12-15% (India business, later framed 15%+)", timeframe: "3-5 year horizon", stated_in: "Q2 FY26 call; reiterated Q3/Q4 FY26 calls"}
guidance: {item: "EBITDA margin target", number: "12-12.5% next year, 14-15% year after", timeframe: "2-3 years", stated_in: "Q2 FY26 call; reiterated Q3 FY26 call"}
guidance: {item: "Debt-free / net-cash target", number: "Net cash by FY28", ...}
guidance: {item: "FY27 capex guidance", number: "Rs125-150cr consolidated", ...Q4 FY26 call}
guidance: {item: "FY27 depreciation guidance", number: "Rs140-145cr consolidated", ...Q4 FY26 call}
guidance: {item: "Synergy balance pending machine install", number: "Rs40-60cr", timeframe: "end-Q3 FY26 -> mid-Q4 FY26 -> Q1 FY27 (slipped)", ...}
Source: origin/main:runs/sfl-2026-07-14/outputs/blocks/B05-concall.yaml L35-38,L42-43
promise: "Top-line growth to reach 12-15%, margin to reach 12-12.5% next year", outcome: "partial" — "FY26 standalone growth landed at 11%, below range; framed as 'halfway there' rather than a miss (Q3 FY26 call)"
Source: same file L54
promise: "Kurlon synergy tail Rs40-60cr from new machine, installed end-Q3 FY26, results Q4 FY26", outcome: "missed" — "Overseas machine delivery/installation delay, now pushed to Q1 FY27 (Q4 FY26 call)"
Source: same file L52
Q1 FY27 call held 31 Jul 2026 but no transcript supplied: "No concall transcript supplied (investor call was 31 Jul 2026; no transcript in the set)."
Source: origin/claude/sheela-quarterly-results-zxbbvj:runs/sfl-q1fy27/work/run_log.md §0 (Document-class detection, last bullet)
Q2 FY27 guidance: NOT FOUND beyond the above.

## Reported results (Q4 FY26 / Q1 FY27 / Q2 or H1 FY27)
Standalone (Q1 FY26 | Q4 FY26 | Q1 FY27 | FY26):
| Revenue from Operations | 634.63 | 819.20 | 760.92 | 2,962.27 | R L145 |
| PAT | 10.70 | 75.52 | 43.94 | 130.57 | R L171 |
| Core Operating EBITDA margin | /Rev from Ops | 9.49% | 11.03% | **8.99%** | 10.05% |
Consolidated:
| Revenue from Operations | 821.41 | 1,050.06 | 1,031.94 | 3,820.84 | R L490 |
| PAT | 6.55 | 91.77 | 62.34 | 160.85 | R L518 |
| PAT attributable to parent | 6.54 | 91.28 | 61.44 | 159.61 | R L538 |
| Core Operating EBITDA margin | /Rev from Ops | 9.16% | 11.11% | **10.55%** | 10.29% |
Source: origin/claude/sheela-quarterly-results-zxbbvj:runs/sfl-q1fy27/work/review_sfl_q1fy27.md §1 L80,L99,L110,L123,L144,L145,L155
"Prior-run memory said FY26 core EBITDA '10.8%'; filing-anchored FY26 core EBITDA is standalone 10.05% / consolidated 10.29% ... the memory 10.8% does not reconcile exactly to either"
Source: same file §6A L333
B05 stated: "10.9% Q3, 11.5% Q4, FY26 full year 10.8% vs 8.5% FY25"  Source: origin/main:runs/sfl-2026-07-14/outputs/blocks/B05-concall.yaml L61
Q1 vs thesis (table): "Revenue (consol Q) | 1,031.94 | Growth strong; likely ≥ Base on top line"; "Core EBITDA margin (std) | 8.99% | Below-Bear signal — under 10% falsification line"; "PAT (consol Q) | 62.34 | Above Base on headline, but 23% non-recurring-aided"
Source: review_sfl_q1fy27.md §6A L326-329
"Standalone core EBITDA ex-OI = 8.99% ... BELOW the 10% Notion falsification line; CONSOLIDATED = 10.55%"  Source: same file L177
Q2 FY27 / H1 FY27: NOT FOUND (no file)

## Management's stated reasons
"Overseas machine delivery/installation delay, now pushed to Q1 FY27 (Q4 FY26 call)"  Source: B05-concall.yaml L52
Q1 FY27 press release, CMD: "We have started FY27 on a strong note, with both our mattress and foam businesses sustaining the healthy momentum built through FY26." (no reason given for the standalone margin)
Source: origin/claude/sheela-quarterly-results-zxbbvj:runs/sfl-q1fy27/work/pressrelease_sfl_q1fy27_layout.txt L105-110
Reason for standalone gross-margin fall: NOT FOUND ("What drove the domestic gross-margin collapse ...?" is an open management question). Source: review_sfl_q1fy27.md L411

## Risk flags raised before the result, and any overruling
"Q1 FY27 core EBITDA margin printing below 10% (compression above 150bps YoY) through the live TDI and polyol shock. That single print invalidates the operator margin override that carried the composite from plus 4 to plus 5, and simultaneously breaks the margin path, the Pillar 1 ROCE recovery and the SHARED CATALYST assumption at once."
Source: origin/main:runs/sfl-2026-07-14/outputs/final/fttcp-recommendation.md L92
"Q1 FY27 core EBITDA margin (ex other income) below 10%, or compression >150bps YoY in Q1 or Q2 FY27 → falsifies the recovery"
Source: origin/main:companies/SFL.md §ACTIVE TRIPWIRES L64-67
Kurlon: "Q1 FY27 call discloses further delay with no hard install date | SHARED CATALYST realized; re weight base case toward Poor (45/40/15); entry zone falls to ~Rs 235"
Source: origin/main:runs/sfl-2026-07-14/outputs/reports/B15.md L120
Operator override: "Margin forward verdict moved STAGNANT (0) → STARTING (+1), lifting the FTTCP composite +4 → +5 (BUY-candidate)... Held at +1 not FIRING +2 pending the Q1-Q2 FY27 margin print"
Source: origin/main:companies/SFL.md §OPERATOR RULINGS L32-39
Q1 result: "(c) Q1/Q2 FY27 core EBITDA ... Std core EBITDA 8.99% < 10% → the 'prints below 10%' limb is met on standalone basis ... FIRED on the standalone <10% limb (ambiguous-basis)"
Source: review_sfl_q1fy27.md §6C L356
"Decision: HOLD AVOID / WATCHLIST. No position action (name not held). New master gate = Q2 FY27 results."  Source: same file §8 L396

## Verdicts and dates
Run date 2026-07-14. Source: origin/main:runs/sfl-2026-07-14/manifest.yaml L5
"PROCEED WITH FLAGS" Source: origin/main:runs/sfl-2026-07-14/outputs/final/gate-recommendation.md L1
"[2026-07-14] AVOID (on valuation) → WATCHLIST-for-entry Rs 362 to Rs 453 (MoS Rs 362), after operator override #2 floored the destination PE at 20x." Source: origin/main:companies/SFL.md §DECISION STATUS L17-18
Q1 FY27 review 2026-08-04. Source: review_sfl_q1fy27.md L5

## Lessons archive mentions
- [2026-07-14] SFL phase 3 (finalize): clean run. Decision AVOID on valuation at CMP Rs807 while the evidence gate stayed PROCEED WITH FLAGS and FTTCP graded the business +5 BUY-candidate ... Source: origin/main LESSONS_ARCHIVE.md L57
- [2026-07-14] SFL phase 3 (post-finalize review): operator override #2 ... Source: LESSONS_ARCHIVE.md L59
- [2026-07-14] SFL phase 2 (fttcp): ... Operator moved Margin STAGNANT->STARTING ... Source: LESSONS_ARCHIVE.md L62
- [2026-07-14] SFL phase 1 (evidence): verdict PROCEED WITH FLAGS (rule 3), confidence overall 90 ... Source: LESSONS_ARCHIVE.md L64
