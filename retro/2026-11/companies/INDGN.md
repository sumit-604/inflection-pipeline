# INDGN — Indegene Ltd
Run folders read: runs/indgn-2026-08-03 (origin/main), runs/indgn-agm-2026-08-13 (origin/claude/transcript-indigene-analysis-5zmus0), runs/indgn-q1fy27 (origin/claude/run-pipeline-indgn-6wej1t)
Company file: companies/INDGN.md (origin/claude/run-pipeline-indgn-6wej1t)

## Our base case
"Base (large deals recognized, margin recovers to 20% H2 FY27) | 4,300 (+22.5%) | 4,945 (+15%) | 5,637 (+14%) | 6,370 (+13%) | 18.0 / 19.5 / 20.0 / 20.0%"
"Bear (organic stalls ~10-12%, no margin recovery) | 4,050 (+15.4%) | 4,455 | 4,900 | 5,390 | 17.0 / 17.5 / 18.0 / 18.0%"
"Bull ... | 4,450 (+26.8%) | 5,340 | 6,275 | 7,215 | 18.5 / 20.5 / 21.0 / 21.0%"
Source: origin/main:runs/indgn-2026-08-03/outputs/reports/B11.md §Revenue and margin paths L138-143
BASE EPS ladder: "| FY27 | 4,300 | 774.0 | 116.4 | 20.0 | 637.6 | 150.5 | 487.1 | 20.22 |"; BEAR FY27 PAT 421.8 EPS 17.51; BULL FY27 PAT 524.8 EPS 21.78. Source: B11.md L151-170
"Base revenue path is bounded BELOW the SOM-implied 3yr CAGR of 20.0% (B09) ... Q1 FY27 annualized (1,063.1 x 4 = 4,252) sets the FY27 floor" Source: B11.md L134-136
Timing: "Q1 FY27 actual: revenue 1,063.1, PAT 116.2, EPS 4.81 (16.9% EBITDA margin, compressed by amortization/integration drag)." Source: B11.md L129-130 (base built 2026-08-03 with Q1 actual in hand)
"base EBITDA margin capped at the FY25-era 20% (mgmt ~20% target discounted for grade-B credibility)" Source: B11.md L382, L436
Q1 review on numeric bands: "supplies the destination-PE / entry / MoS spine and the qualitative FY27 path ... but not numeric Bear/Base/Bull revenue/margin/PAT bands -> those cells ND" Source: origin/claude/run-pipeline-indgn-6wej1t:runs/indgn-q1fy27/work/review_indgn_q1fy27.md §6A L226

## Management guidance and promised catalysts
"Margin recovery target | "back to the levels...around 20% and a little north of that" | 6-8 quarters from Q2 FY26 | Q2 FY26 call, Suhas Prabhu, p.11" Source: B05.md §1B L41
"Margin - full reversion to earlier higher levels | Qualitative (no fresh % restated) | H2 FY27 | Q4/Annual FY26 call, Suhas Prabhu, p.11" Source: B05.md L55
"No formal revenue guidance | Policy, held every quarter" Source: B05.md L58
Q1 FY27 call (31 Jul 2026), Manish: "it's not going to be 6 to 8, it's going to be 6. By March end, we get back to that 19% to 20% range" (L640-641). Source: review_indgn_q1fy27.md L461
AGM 13 Aug 2026: "Recover to 19%-20% by Q4 FY27; sustained thereafter"; ">USD 10 mn ACV outcome-based deal signed Dec'25, revenue from Q3 FY27, +1.0%-1.5%"; "amortisation to reduce ~INR 50 cr/quarter starting Q3 FY27"; "USD 19 mn BioPharm earn-out due 2027"; "we don't give guidance" (Tr p.21). Source: origin/claude/transcript-indigene-analysis-5zmus0:runs/indgn-agm-2026-08-13/outputs/INDGN_AGM_concall_analysis.md L52,L97-108

## Reported results (Q4 FY26 / Q1 FY27 / Q2 or H1 FY27)
(Rs cr; columns Q1 FY26, Q4 FY26, Q1 FY27, FY26)
| Revenue from Operations (L216) | 760.8 | 1,003.4 | 1,063.1 | 3,510.5 |
| PAT (L238) | 116.4 | 79.7 | 116.2 | 401.1 |
| Operating EBITDA margin | 20.41% | 16.31% | 16.39% | 17.63% |
| Memo: Management/deck EBITDA | 20.2% | 16.4% | 16.9% | ND |
Source: review_indgn_q1fy27.md L68,L84,L90-95
"Q1 FY27 EBITDA margin reads as 16.9% (management/deck, +50 bps QoQ), 16.4% (operating ...), and ~190 bps DOWN on the honest ex-MTM basis ... YoY ... -330 bps (deck), -402 bps (operating)" Source: review L103
6A table: "Operating EBITDA margin | ND | ~16.4%->20% path | ~20% | 16.4% (op) / 16.9% (deck); underlying declined | Below the recovery glide-path this quarter"; "PAT ... 116.2 (-0.2% YoY)"; "Revenue growth YoY ... +39.7% INR / +26.5% USD". Source: review L228-235
FY26: "FY26 PAT declined -1.4% YoY (Rs 406.7->401.1 cr) despite +23.6% revenue" Source: B10.md L243
Q2 FY27: NOT FOUND.

## Management's stated reasons
"the prior quarter carried an adverse impact of roughly 240 basis points from the mark-to-market... adjusting for that impact... our margins declined sequentially" (L386-388). Source: review L386-388 (§Exchange 1)
"margins deliberately absorbed heavy AI + integration investment" (AGM, FY26 PAT). Source: AGM analysis L67
"We're not breaking up organic and inorganic growth from a BioPharm perspective, anymore." Source: review L704-706
FY26 PAT drivers: "Rs 20.3 cr TCPA litigation provision, ~Rs 42 cr fall in other income" Source: B10.md L243

## Risk flags raised before the result, and any overruling
Stage 15: "No-margin-recovery Hurdle: on the model's own bear FY27 EPS 17.51 the current forward PE is 31.14x and HR falls to 1.56, BELOW the Tier B 1.728 threshold. The Hurdle PASS exists only because the disputed margin recovery is assumed into both the denominator and the destination multiple." Source: origin/main:runs/indgn-2026-08-03/outputs/blocks/B15-devil.yaml L13
"Correct verdict at CMP is WATCHLIST until the Q2-..." Source: B15-devil.yaml L20
"PRIMARY: operating margin fails to expand sequentially for two consecutive quarters from 16.4% (Q2-Q3 FY27) ... This IS the thesis" Source: companies/INDGN.md L47-49
Overruling: operator 2026-08-03 FTTCP gate: "take the forward PE method"; "take price-to-earnings of 31.5"; "Operator did not dispute the FTTCP composite"; BUY (on-dips) recorded. Source: companies/INDGN.md L17-40
Q1 outcome: "Tripwire scorecard 1 FIRED / 2 BLINDED / 4 NOT FIRED"; "Decision Status UNCHANGED". Source: companies/INDGN.md L90

## Verdicts and dates
2026-08-03: gate "PROCEED WITH FLAGS" (gate-recommendation.md L1); "BUY (on-dips)" at CMP Rs 545.25; "Destination PE 31.5x additive ... Hurdle 2.12 PASS" (companies/INDGN.md L17-26).
2026-08-06 Q1 FY27 review: "Net thesis impact: WEAKENED (not broken)"; "Evidence-gate verdict: PROCEED WITH FLAGS". Source: review_indgn_q1fy27.md L595-599.
Listing: "BSE 544172 | NSE INDGN" (AGM analysis L5).

## Lessons archive mentions
LESSONS_ARCHIVE.md L167-182: "INDGN phase 3 (finalize): clean run. Decision BUY (on-dips) at CMP Rs 545 while the evidence gate stayed PROCEED WITH FLAGS and FTTCP was +5 BUY-candidate"; "the devil's advocate earned its keep ... B15 WEAKENED BUT ALIVE, valuation_safety DESTROYED: it rebuilt the Hurdle on the model's OWN no-margin-recovery bear FY27 EPS (17.51) and got forward PE 31.14x, HR 1.56 < 1.728".
