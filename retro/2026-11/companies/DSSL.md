# DSSL — Dynacons Systems & Solutions Ltd
Run folders read: runs/dssl-2026-07-27 (origin/claude/dssl-pipeline-run-onx7hd), runs/dssl-q1fy27 (origin/claude/quarterly-results-analysis-3y7lxn)
Company file: companies/DSSL.md (origin/claude/dssl-pipeline-run-onx7hd)

## Our base case
"| Revenue CAGR | **12%** | **18%** | **25%** |" and "| Revenue Yr3 (FY29) | 2,001.1 | 2,340.2 | 2,782.6 |" (base year FY26 = Rs 1,424.28cr)
Source: origin/claude/dssl-pipeline-run-onx7hd:runs/dssl-2026-07-27/outputs/reports/B11-valuation.md §2A L104-111
"| EBITDA margin | 8.5% ... | ~10.0% (near FY26, above 3yr avg 8.7%) | ~11.5% ..." ; "| PAT margin | **4.8%** | **5.8%** (roughly holds FY26, slight haircut) | **6.8%** |"
Source: same file §2B L119-122
"| PAT (Rs cr) | 84.78 | 96.05 | 135.73 | 189.22 |" (Yr0 FY26, Bear/Base/Bull Yr3)
Source: same file §2C L131
"Forward guidance NOT FOUND — base revenue CAGR 18% from discounted order-book conversion (< SOM 33.9%); bear 12%, bull 25%"
Source: origin/claude/dssl-pipeline-run-onx7hd:runs/dssl-2026-07-27/outputs/blocks/B11-valuation.yaml L49
No FY27E or FY28E figure found in the exported files.

## Management guidance and promised catalysts
"Revenue/margin guidance for FY27 or medium term | explicitly NONE — "as per company policy we do not give any forward-looking numbers" | both calls"
Source: origin/claude/dssl-pipeline-run-onx7hd:runs/dssl-2026-07-27/outputs/reports/B05-concall.md L68
"RBI Rs750.82cr order go-live undated = single point of failure"
Source: origin/claude/dssl-pipeline-run-onx7hd:runs/dssl-2026-07-27/outputs/blocks/B11-valuation.yaml L14
"Q4 FY26 call: ... Q3 FY26 call: 'Currently do not see material [input cost] pressures that would impact margins'" (promise missed)
Source: origin/claude/dssl-pipeline-run-onx7hd:runs/dssl-2026-07-27/outputs/reports/B05-concall.md L108
"Order-book execution timeline (revised framing) | ~18-24 months average | forward | Q4 FY26 call"
Source: same file L62

## Reported results (Q4 FY26 / Q1 FY27 / Q2 or H1 FY27)
| Revenue from Operations (Net Sales) | 328.8517 | 402.4485 | 313.6883 | 1,424.2834 | 465 |   (cols: Q1 FY26, Q4 FY26, Q1 FY27, FY26; CON, Rs cr)
| PAT (Net Profit for period) | 19.6451 | 18.9903 | 19.7955 | 84.8124 | 477 |
Source: origin/claude/quarterly-results-analysis-3y7lxn:runs/dssl-q1fy27/work/review_dssl_q1fy27.md §1A L63, L75
| Operating EBITDA margin | OpEBITDA / Revenue | CON | 9.66% | 9.02% | 12.81% | 10.25% |
Source: same file §1C L110
"Revenue from Operations | 328.8517 | 313.6883 | −4.61% | contracted"; "Op EBITDA margin (pp) | 9.66% | 12.81% | +315 bps | expanded"
Source: same file §2A L132-134
Q3 FY26 margin: "Q4 FY26 EBITDA margin 9.02% (from 11.92% Q3)"
Source: origin/claude/dssl-pipeline-run-onx7hd:runs/dssl-2026-07-27/outputs/blocks/B11-valuation.yaml L16
Q2/H1 FY27: NOT FOUND (no file).
Variance table: "| Revenue | FY26 run-rate ~356 cr/qtr | 313.6883 | below run-rate (−4.6% YoY) |"; "| Op EBITDA margin | green ≥11% / red <9% | 12.81% | above green threshold |"
Source: review_dssl_q1fy27.md §6A L258-266 ("Explicit Bear/Base/Bull quarterly projections were not passed inline for this run")

## Management's stated reasons
"management calls this "short-term," "a temporary blip," "normal quarterly variations... rather than any structural change," repeated in near-identical language to four separate Q4 FY26 analysts"
Source: origin/claude/dssl-pipeline-run-onx7hd:runs/dssl-2026-07-27/outputs/reports/B05-concall.md §2B L120-125
Q1 FY27: NOT FOUND ("no concall transcript, presentation deck, or investor call was filed", review L6).

## Risk flags raised before the result, and any overruling
"Shared catalyst single point of failure: the undated RBI Rs750.82cr order carries BOTH the Pillar 3 +3x premium AND the RECOVERING ROCE; a 2 to 3 year slip unwinds both and dead-money drifts the stock at a 25% opportunity cost."
Source: origin/claude/dssl-pipeline-run-onx7hd:runs/dssl-2026-07-27/outputs/blocks/B15-devil.yaml L18 (stage 15 devil)
"Falsifier / thesis-broken: Q1 FY27 EBITDA margin near 9% (below 11%) for two consecutive quarters" 
Source: origin/claude/dssl-pipeline-run-onx7hd:companies/DSSL.md L31
Overrides (operator, 2026-07-27): "Cash conversion DECLINING -> STAGNANT", "ROCE DECLINING -> RECOVERING", "Sector cap 25x -> 30x" 
Source: companies/DSSL.md L24-26; devil: "Three of four destination-multiple inputs are operator overrides of a more conservative draft" (B15-devil.yaml L16)
Q1 FY27 outcome: "No pre-committed thesis-broken trigger has formally fired on this filing. Decision Status is NOT re-rated." (review L295)

## Verdicts and dates
2026-07-27: "PROCEED WITH CAVEATS" (gate-recommendation.md L1); WATCHLIST (BUY-ON-DIPS on Q1 FY27 confirmation); FTTCP composite +3 DEEP WATCH; devil WEAKENED BUT ALIVE (companies/DSSL.md L14-15)
Q1 FY27 review: "PROCEED WITH CAVEATS" (review L394); "the pre-committed buy gate is half-satisfied and therefore NOT met" (L338)
Board: "Company: Dynacons Systems & Solutions Ltd (BSE 532365 / NSE DSSL)" (review L4)
Archetype: NOT FOUND. Fair values: "track1: {bear: 1810, base: 2558, bull: 3565}" (B11-valuation.yaml L40)

## Lessons archive mentions
NOT FOUND
