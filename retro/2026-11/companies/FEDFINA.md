# FEDFINA — Fedbank Financial Services Ltd
Run folders read: runs/fedfina-2026-07-15 (origin/claude/fedfina-pipeline-run-3mq2uj); runs/fedfina-q1fy27 (origin/claude/fedfina-call-analysis-ggpjgq); runs/fedfina-q2fy27 (origin/run/quarterly-q2fy27-2026-10-17)
Company file: companies/FEDFINA.md (origin/claude/fedfina-pipeline-run-3mq2uj)

## Our base case
"| EPS CAGR logic | ... | Historical PAT CAGR 18.5% discounted for grade-B delivery + ESOP/future dilution | Management guidance at face value (grade B permits); AUM ~20%, gold-branch maturation |"
"| EPS CAGR | 10% | **15%** | 20% |"
Source: origin/claude/fedfina-pipeline-run-3mq2uj:runs/fedfina-2026-07-15/outputs/reports/11-valuation.md §2A L155-L156
"| EPS (from 9.12) | 9.12 x 1.10^3 = 12.14 | 9.12 x 1.15^3 = 13.87 | 9.12 x 1.20^3 = 15.76 |" and "| Est. ROE trajectory | ~11.5% | ~14.5% | ~17% |"
Source: same file §2B L164, L167 (Year 0 = FY26; Y3 = FY29)
"Historical anchors: PAT 3-yr CAGR 18.5%, revenue 17.3%, AUM 19.8% (B10). Base 15% sits below all three" (L158)
Fair values: "track1: {bear: 117, base: 150, bull: 186}"; "expected_cagr_prob_weighted: -3.1"; "entry_range: {low: 68, high: 77}"; "decision: AVOID (on valuation)"
Source: ...:runs/fedfina-2026-07-15/outputs/blocks/B11-valuation.yaml L37-L43
Valuation date: "Run date 2026-07-15. Finalize date 2026-07-16." (fttcp-recommendation.md L5)
No FY27E revenue, margin or PAT line exists. Q2 FY27 review: "No Notion base projection exists (ND), so no base-case comparison is possible." (origin/run/quarterly-q2fy27-2026-10-17:runs/fedfina-q2fy27/work/review_fedfina_q2fy27.md L240)
"| Revenue (NII) | ND | ND | ND | 403.67 / 775.55 | ND (no P&L projections on the Notion page) |" (same file L407-L413)

## Management guidance and promised catalysts
FY26 (B05, calls Q1-Q3 FY26): "Credit cost | 1% +/- 10bps | FY26 | Q1 FY26 call, reiterated Q2 and Q3"; "FY27 credit cost / opex guidance | to be given | by Q4 FY26 call"; "Tier 2 capital supplementation | planned | H2 FY26"; "New gold branches | 100-150 branches | FY26".
Source: ...:runs/fedfina-2026-07-15/outputs/blocks/B05-concall.yaml L19-L20, L27-L28
Slippage: "ST LAP collections in-housing: promised complete early Q2 FY26, still incomplete as of Q3 FY26, now targeted for Q4 FY26" (B05 L78)
FY27 (Q1 FY27 call): "Entity AUM growth | 20-22% (line 838); '20-25%' also said"; "Gold AUM growth | 25-30% if price flat"; "Credit cost (THE critical one) | Sub-1% FY27 (lines 736, 205)"; "Branch / geography expansion | 200 branches FY27 (premises identified, ZERO opened in Q1); spillover Q2"
Source: origin/claude/fedfina-call-analysis-ggpjgq:runs/fedfina-q1fy27/work/review_fedfina_q1fy27.md §Step 2L L111-L124
Q2 FY27 call (ASR): "AUM growth 20-25% for FY27 held even at a flat gold price; ROA +30-40 bps on FY26 2.4 'might be an upside'; target ROA 3 (and ROE ~18%) 'sooner than we had promised'; credit cost 'way below 1%'; GNPA below 2%; tonnage +10-12% a year"; "At least another 150 branches in the second half" (about 75 in Q3, push to about 100 in Q4); "best quarter compared to the last eight or nine quarters" (ST LAP, Q3).
Source: origin/run/quarterly-q2fy27-2026-10-17:runs/fedfina-q2fy27/work/concall-readout_fedfina_q2fy27.md L19, L30, L32; review_fedfina_q2fy27.md L579

## Reported results (Q4 FY26 / Q1 FY27 / Q2 or H1 FY27)
Q4 FY26 (filing dated April 28, 2026, Rs lakh): "I Total Revenue from Operations 61,645 55,517 53,623 2,22,360 2,06,187"; "VII Net Profit 10,053 8,791 7,165 34,360 22,518"; "Net profit margin(%) 16.28% 15.82% 13.33% 15.43% 10.83%"
Source: origin/claude/fedfina-pipeline-run-3mq2uj:runs/fedfina-2026-07-15/derived/results-B.txt L216, L232, L598-L599
"FY26 audited: PAT 343.60, NII 1,229.75, opex 770.99, impairment 115.27, AUM 20,153 ... CRAR 22.40% ... gold tonnage 12.6t, branches 757." (runs/fedfina-q2fy27/work/notion-thesis.md L50)
"FLAG-Q4-FY26-DATA-GAP. The Q4 FY26 result filing (out 29 Apr 2026 per the ICICI note) is not in the run inputs. Non-anchored ICICI claims: credit cost 0.6%, RoA 2.6%, RoE 14%." (fttcp-recommendation.md L50; note the results-B.txt filing is dated April 28, 2026: both stated in files)
Q1 FY27 (filing dated July 15, 2026): "Total Revenue from Operations 66,993 61,645 51,660 2,22,360"; "Net Profit 11,438 10,053 7,501 34,360"; "Net profit margin (%) 17.07% 16.28% 14.50% 15.43%"; "Basic 3.05 2.69 2.01 9.20"
Source: ...:runs/fedfina-2026-07-15/derived/results-A.txt L147, L162, L230, L233-L236
Q1 call: "PAT ₹114.4 Cr, +52.5% YoY; ROA 2.6%; ROE 15.4%"; "AUM +35% YoY to ₹21,136 Cr"; "Credit costs 0.8%, within guided sub-1%"; "Cost-to-income 52.8% (from 57.2% FY26 annualised)"
Source: ...q1fy27/work/review_fedfina_q1fy27.md L67, L78, L80, L94
Q2 FY27 (quarter ended 30 Sep 2026), Rs Cr: Interest Income 692.01; NII 403.67; Other/Fee Income 27.78; Provisions 27.08; PBT 178.00; PAT 130.75 (Q2 FY26 80.15; Q1 FY27 114.38); H1 FY27 PAT 245.13; EPS basic printed 3.56 (derived 3.49)
Source: ...q2fy27/work/review_fedfina_q2fy27.md §1L table L116-L129
"Cost-to-Income ... 52.47%"; "Credit cost ... 0.6% (Deck R1048); 0.59% derived"; "ROE 17.0% Q2; 16.2% H1"; "AUM 22,035"
Source: review_fedfina_q2fy27.md L143-L149, L436
Status vs Q1 promises: "200 branches in FY27 | 74 in H1 ... | BEHIND"; "Entity AUM +20-22% ... +9.3% in H1 ... | DELAYED"; "Gold AUM +25-30% ... | AT RISK"; "Credit cost below 1% FY27 | 0.69% H1 annualised ... | ON TRACK"
Source: review_fedfina_q2fy27.md L202-L207

## Management's stated reasons
Q1 FY27 gold growth: "+1% tonnage, -4 to -5% price, LTV moved 61%->68% = 7%, that is 10%... that's the math" (Parvez, call line 646, as quoted in review); branches: "Premises identified, openings slipped, spillover Q2 (934-944)".
Source: review_fedfina_q1fy27.md L170, L191
Q2 FY27: "CFO: Stage 2 rose 2.7% to 3.6% and Stage 3 1.6% to 1.8%, 'entirely on account of' the gold shift from bullet to periodic interest"; "PCR fell 38.4% to 35.5% 'due to a higher proportion of gold loans in stage three'".
Source: concall-readout_fedfina_q2fy27.md L17-L18
Q4 FY26: NOT FOUND.

## Risk flags raised before the result, and any overruling
Before Q1 FY27 result (same-day run files, 2026-07-15): "Industry gold tonnage growth of 10 to 15% ... is contradicted by Manappuram's disclosed 2.8% year on year tonnage ... Reframes the 52% gold AUM print as price driven." (gate-recommendation.md L42); "Q4 FY26 credit cost printing above 1.1% of average assets does the most damage" (L61); B05 red flag: "Collections in-housing completion date slipped from early Q2 FY26 to by Q4 FY26" (B05-concall.yaml L69).
Before Q2 FY27 result: "PCR thins below 32% | <32% | 38.36% ... management guiding it DOWN | NOT FIRED — but 38.36% and falling toward the 32% line; the tripwire most at risk" (review_fedfina_q1fy27.md L322); "Pillar 2L ... CONDITIONALLY LIVE" (L323); "Maintained but slipped" for 200 branches (L124).
Company file tripwires: "Q4 FY26 credit cost above 1.1% ... ROE fails to cross 14% by FY28. PCR thins below 32%." (companies/FEDFINA.md L17-L19)
Overruling: "2026-07-16: Flipped the Pillar 2L Asset-Quality Multiplier from the analyst's 0.80x (Stressed) to 1.00x (Sound)... self-withdraws to 0.80x if Q4 FY26 credit cost breaks 1.1% or PCR thins further." (companies/FEDFINA.md L13)
Q2 FY27: "(Pillar 2L clause, not a tripwire) override self-withdraws if credit cost > 1.1% or PCR thins further | PCR 38.36% to 35.37% QoQ; vs FY26 32.29% higher | CONDITION MET QoQ; NOT MET vs FY26. FLAG; operator decides." (review_fedfina_q2fy27.md L438); "No thesis-broken condition has FIRED." (L440)

## Verdicts and dates
"PROCEED WITH CAVEATS" (gate-recommendation.md L1, 2026-07-15 Phase 1); "decision: AVOID (on valuation)" (B11-valuation.yaml L43); "As of the 2026-07-15 run: AVOID (on valuation) at CMP Rs 164. DEEP WATCH ... Entry Rs 68 to 77, MoS Rs 61." (companies/FEDFINA.md L9)
Q1 FY27 review: "REMAIN ON DEEP WATCH — AVOID at CMP; entry zone Rs 68-77 UNCHANGED." (review_fedfina_q1fy27.md L348)
Q2 FY27 review: "A4 complete ...: PROCEED WITH FLAGS; Decision UNCHANGED WATCHLIST / AVOID" (run-log.md L19, 2026-10-17)
Manifest: run_date 2026-07-15; sector cap row corrected to "Banks / NBFCs / MFIs" (manifest.yaml L5, L9). Archetype: "lender (NBFC-ND-SI, gold loans plus LAP), Lender Transition Set" (fttcp-handoff.md L5). Board: NOT FOUND.

## Lessons archive mentions
NOT FOUND (no mention of FEDFINA or Fedbank in LESSONS_ARCHIVE.md or LESSONS_ARCHIVE_offmain_lines.md)
