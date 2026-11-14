# PVR INOX (PVRINOX): verifier summary, phase 1, 2026-11-12

## Confidence delta (phase 1)

| Component | Value | Basis | Source |
|---|---|---|---|
| numerical_acceptance | 97 | 385 numbers checked; mandatory 125 of 125; 0 CRITICAL, 3 MAJOR, 2 MINOR | B12a |
| redflag_coverage | 69 | 9 of 13 material verifier found flags caught upstream (85 counting partial catches) | B12b |
| framework_adherence | 87.2 | Gate 0 46 of 52 (88.5), Emerging Moat 29 of 34 (85.3); 75 of 86. Valuation component PENDING PHASE 3 | B12c |
| peer_utilisation | 87.5 | 7 of 8 peer transcripts used substantively (1 cited only). Counted on peers it is 2 of 2, a denominator under 4 | B12d; confidence.yaml |
| overall | 69 | overall_set_by: redflag_coverage | confidence.yaml |
| band | 60 to 74 | PROCEED verdicts downgrade one level | confidence.yaml |

REWORK triggers: none. No CONFIRMED Verifier A CRITICAL. Lowest acceptance rate 69% on a denominator of 13; the OR-29 line is below 60% on 4 or more.

## Acceptance rates by verifier

| Verifier | Model | Acceptance rate | Denominator | CRITICAL | MAJOR | MINOR |
|---|---|---|---|---|---|---|
| A, numerical (source fidelity) | claude-sonnet-5-5 | 97 | 385 numbers checked; mandatory 125 of 125; material universe about 700 (estimate) | 0 | 3 | 2 |
| B, red flags | claude-opus-5-5 | 69 (85 counting partials) | 13 material of 37 items | 0 | 3 | 6 |
| C, framework (phase 1 scope) | claude-opus-5-5 | 87.2 | 86 rules (Gate 0 52, Emerging Moat 34) | 0 | 1 | 11 |
| D, peers | claude-sonnet-5-5 | 100 by peer (2 of 2 without MAJOR or CRITICAL); 87.5 by transcript in the confidence delta | 2 peers, 8 transcripts | 0 | 0 | 4 (plus 1 INFO) |

Verifier A struck 3 false positives. The net cash 132.4 Cr against 140.7 Cr gap is a correctly labelled basis difference and was struck.

Verifier C scope: the Gate 0 and Emerging Moat audits ran in phase 1. Verifier C's valuation half (B10 and B11 audit, expectation ledger rules 13 and 14) is PENDING PHASE 3. Its business narrative rule 9 fires at /finalize.

Verifier A shadow: not run in this folder. The one permitted shadow run was claimed by runs/kusumgar-2026-11-12.

Verifier runs: A 1, B 1, C 1, D 1. Remediation cycles: 0.

## Findings, sorted by severity

### CRITICAL

None. All four verifiers logged 0 CRITICAL findings.

### MAJOR

| # | Verifier | Location anchor | Note |
|---|---|---|---|
| 1 | A (source fidelity) | 01-gate0.md Block B, B2 (FY24 FCF line) and B3 cumulative FCF; Block B lease adjusted line | Claimed FY24 capex 627.9 Cr, FY24 FCF 1,351.1 Cr, cumulative FCF FY24 to FY26 4,889.5 Cr, FY24 lease repayment 1,054.7 Cr, anchor "screener-data; AR25 p.CF" (no page). Source: consolidated FY24 capex 6,344 mn = 634.4 Cr (AR25 consolidated cash flow, FY24 column); FY24 FCF = 1,979.0 less 634.4 = 1,344.6 Cr; cumulative FCF 4,883.0 Cr; consolidated FY24 lease repayment 10,589 mn = 1,058.9 Cr. The figures used (6,279 mn capex, 10,547 mn lease) are the standalone AR25 lines, while FY24 CFO 1,979.0 Cr is consolidated. Unlabelled standalone and consolidated mix in a Gate 0 input. B2 stays 5 and B3 stays literal 5 (4,883.0 / 22.5 = 217x); no score moves. FY25 (330.7 Cr) and FY26 (258.7 Cr) capex are consolidated and match AR26 p.241. |
| 2 | A (source fidelity) | 01-gate0.md Block B, B4 (WC days FY24 vs FY26) and Block F M12 | Claimed FY24 payables 6,511 mn (-20.6 days), FY26 594.8 Cr (-14.0 days), change +6.6 days, FY25 -18.1 on 6,062 mn, no basis label. Source: AR25 FY24 trade payables 6,511 mn are as originally filed and include supplier finance. AR26 FY26 payables 5,948 mn exclude supplier finance of 1,251 mn, moved to other financial liabilities (AR26 Note 2A(ii) p.258; Note 22 p.274; FY25 comparative moved 1,635 mn). Unlabelled basis difference (rule 5a), material because B4 scores on the FY24 to FY26 change (+6.6 days, 1 point) and M12 rests on the same days. Every figure is copied correctly from its own page; the finding is the missing basis label. |
| 3 | A (source fidelity) | 02-notes.md Section A, Top 15, rank 1, "Why it matters" cell | Claimed "a number larger than 5x tangible equity of 15,260 (derived)" (goodwill 57,367). Source: 57,367 / 15,260 = 3.76x; 5 x 15,260 = 76,300, above goodwill. Tangible equity 15,260 = 73,787 less 57,367 less 1,160 is correct (AR26 p.239). Derived multiple overstated by about 1.2x. YAML top_findings rank 1 does not repeat the 5x claim. |
| 4 | B (MISSED) | Feb 2026 call p.18; Jul 2026 call p.12; Nov 2026 call p.4 | ROCE pre-COVID benchmark shift from 18% (accepted by the CFO, "Correct", in Feb) to "above the pre-COVID benchmark of around 13%" (Oct) not caught; B05 D8 scores ROCE Delivered. Section 1B ROCE pillar and rung read affected. Fix: carry both benchmarks; separating observation is a filed FY19 or FY20 ROCE on the company definition. |
| 5 | B (MISSED) | May 2026 call p.4; Jul 2026 call p.12; Feb 2026 call p.5; Pres p.21 | FY26 FCF "all-time high of INR790 crores" likely includes Rs 226.8 Cr 4700BC proceeds; analyst "about INR570 crores, excluding the sale" undisputed; company surplus definition adds "any disposal proceeds"; derived operating FCF about Rs 563 Cr. Fix: use operating FCF as the cross check; resolve from the AR FY26 cash flow statement. |
| 6 | B (PARTIALLY CAUGHT) | 20260907 clarification p.1; 20260525 p.1, p.3; 20260723 p.1-2; May, Jul, Nov transcripts (absence) | Governance silence: B05 has both resignations but misses the April anonymous allegations, the external third party assessment, the 7 Sep "internal probe into alleged Rs 200-crore kickbacks" clarification (8% share fall) and the Oct call silence; developer counterparty link to the capital light pipeline. Fix: Halt 1 open item and Pillar 3 reader; tripwire is the final assessment outcome and a re-published signed pipeline against 138 (May p.9). |
| 7 | C (G0-51) | B01; GB l.16, l.53; G l.12, l.48, l.55, l.69 | Symmetric bar on sensitivities (CLAUDE.md Rule J). Claimed ex-lease core 44 AVERAGE, "AVOID only on the lease-inclusive reported basis". Recomputed: ex-gain core 27 AVOID with DB2 (B3 0, C2 1, C4 1, D2 0); ex-lease plus ex-gain core 35 AVOID; AVERAGE needs lease re-basing AND the 195.2 Cr one-time gain. Decision effect: none; AVOID of record stands; flag and analyst_note should carry all four readings. |

### MINOR

| # | Verifier | Location anchor | Note |
|---|---|---|---|
| 8 | A (source fidelity) | 01-gate0.md Block A table, FY17 row, Avg NW column | Claimed closing only 964.99; source 46.74 + 918.27 = 965.01 (screener Data Sheet, FY17 equity capital plus reserves). 0.02 Cr arithmetic slip. FY17 ROE 9.9% and FY18 average 1,020.2 unchanged. |
| 9 | A (source fidelity) | 09-tam.md Section 1A and Section 2 cross check | Claimed four stream revenue Rs 63,208 Mn = Rs 6,321 Cr (95.1% x 66,462) and net ticket sales Rs 35,291 Mn. Source: AR26 Note 24 p.275, tickets 35,301 + F&B 20,884 + advertising 4,636 + convenience fees 2,410 = 63,231 Mn = 6,323.1 Cr; tickets 35,301 Mn. Rebuilt from rounded mix percentages (0.04% off). No SAM or SOM conclusion moves. |
| 10 | B (PARTIALLY CAUGHT) | May 2026 call p.6; Nov 2026 call p.3-4, p.9 | May ad excuse (Toxic, Jana Nayagan moved = 7-8% growth lost) tested by both films releasing in Q2; Oct "no tentpole films" against the same call's "landmark quarter", Spider-Man Rs 608 Cr; B05 holds D15 and D18 unjoined. Fix: dated test, Q3 FY27 ad growth on the four films named at Nov p.9. |
| 11 | B (SCORING LABEL) | B05 2A D15, D19; Jul 2026 call p.8; Nov 2026 call p.5 | D15 and D19 scored Missed while FY27 is open; direction confirmed; label should be "tracking to miss". Fix: relabel at FY27 close. |
| 12 | B (ONE-SIDED) | Pres p.28 note (1); Nov 2026 call p.10 | Depreciation "does not reconcile" omits the Ind AS 8 effective date reading (Rs 21.1 Cr for H1 = about Rs 42 Cr a year, near the CFO's Rs 35-40 Cr). Fix: state both readings; the Q3 FY27 note separates. |
| 13 | B (PARTIALLY CAUGHT / MISSED) | UFO-May p.8; UFO-Aug p.3; UFO-Nov p.3; WON-Aug p.11; UFO-Feb p.8; Jul p.3, p.15; Nov p.4; Feb p.18 | Peer contrasts not drawn: UFO ad share gain (P2), UFO "southern regional subdued" against PVR "multifold" (P4), Toxic and Batwara under performance against PVR distribution silence (P5), Wonderla F&B inflation against PVR COGS down (P7); UFO advertiser read against PVR (P3) missed. Fix: synthesis cites P2 and P3 with the UFO +33% ad divergence. |
| 14 | B (MISSED / PARTIALLY CAUGHT) | Feb p.13; Nov p.14; Feb p.10; Jul p.8, p.13; May p.9, p.17 | Tone items: Karnataka "No conversations at all" against the Feb litigation answer; MD drop offs ("You do not need to connect Mr. Bijli back", Feb p.10; disconnected again, Jul p.8); analyst insistence ("the first question remains unanswered", Jul p.13); FOCO count 22 against "close to 18 or 19" and the "not capex, not opex" claim. Fix: record only. |
| 15 | B (OVERSTATED) | May p.14; Jul p.15; B05 2D, red flag 7 | Promoter buyback participation bundled into a governance red flag though no promise existed (B05's own words). Fix: split it from the resignation and probe silence; weight that silence up. |
| 16 | C (G0-03) | B01; G l.18; G l.30-31 | ROCE fixed formula EBIT/(TA-CL), no substitution (P01 l.27-31). Proxy capital employed used all 10 years; the fixed formula covers FY25-FY26 only, under the 3 year minimum; A1, A2, A4 NOT FOUND = 0; Block A 0, same as B01. Decision effect: none. |
| 17 | C (G0-29) | B01; G l.84 | M1 pricing power, no qualitative judgments (P01 l.13, l.102-104). M1 scored 3 on like for like 14.4% against 15.1%; rule literal M1 5 on screener series 15.1% to 31.5% (+16.4pp, revenue CAGR 13.5%); moat_score 22, grand_total 59; moats_confirmed 4, STRONG unchanged. Decision effect: none. |
| 18 | C (G0-43) | B01; GB l.28 | State which years drive each deal-breaker (P01 l.151-154). DB3 "median ROCE 6.3%" given with no years; driven by FY21-FY26, six of ten years under 10% (G l.26-31). Decision effect: none. |
| 19 | C (G0-45) | B01; G l.86, l.94, l.95 | Anchor on every extracted number (P01 l.15-18). M3 net block 13,373.0, M11 21.0% and 3.2% and selling % 6.65 and 5.51, M12 FY25 -18.1 days unanchored; FY25 WC components NOT FOUND in B01. Decision effect: none. |
| 20 | C (G0-47) | B01; G l.155; GB l.33-51 | Exact template block; report copy equals block file (P01 l.165-198). Report data_notes is a string pointer; block file holds a list of 18 items. Report copy to match. Decision effect: none. |
| 21 | C (E-05) | B07; E l.29, l.48-54, l.102, l.155, l.190, l.195, l.328 | Primary source anchors (P07 l.35-36). Rows anchored to B03, B04, B08 or "AR MD&A" without page. No positive raw score depends on these rows. Decision effect: none. |
| 22 | C (E-16) | B07; EB l.27 | Recount consistent with evidence tiers (Verifier C rule 3; P07 l.41-46, l.157-159). evidence_mix 9 documented, 6 claim, 0 inference against Section 3 tagged rows 15, 7, 0; guard result unchanged (7 categories under 12). Decision effect: none in phase 1; phase 3 re-checks any Pillar 3 use of evidence_mix. |
| 23 | C (E-19) | B07; E l.197 | I2 answered for each moat claimed (P07 l.140-142). Answered for scale, premium, D2, E1, H2; C1, F2, G1, H3 not answered; I2 score 0 stands. Decision effect: none. |
| 24 | C (E-20) | B07; E l.153, l.259, l.163-164, l.177 | One improvement, one mechanism (CLAUDE.md). F2 1.0 includes debt reduction and capital light share, the same facts scored in G1 and H2; F2 range 0 to 1.0; EM 8.4 to 9.4, NONE either way. Decision effect: none. |
| 25 | C (E-27) | B07; E l.320; EB l.47 | One combined classification (P07 l.203-204). AVOID and AVERAGE ex-lease both given; combined_assessment AVOID; the ex-lease reading is a sensitivity that falls to core 35 AVOID ex-gain (G0-51). Decision effect: none. |
| 26 | C (O-1, observation) | B07; E l.81-88; G l.86 | 2C FAT basis against B01 M3 (P07 l.60-62). capex_embedded_growth_pct 10.9 rests on a PPE only standalone FAT of 2.27x; on B01 FAT 0.50x: 3,100 Mn x 0.497 = 1,541 Mn / 66,462 Mn = 2.3%; 2C arithmetic itself correct. Decision effect: none in phase 1; stage 11 should show both readings before any CAPACITY basis use. |
| 27 | D (Q2) | UFO Q1 PDF p.3, p.5-6; UFO Q2 PDF p.7 (lines 362-366) | CONTRADICTED label overstated. It rests on one peer of a different business; UFO Q1 +33% is credited to Dhurandhar spillover "to a significant extent" (UFO Q1 PDF p.5) and UFO Q2 ad growth is NOT FOUND; B06 net read says "half-supported". Citations are real: +33% at UFO Q1 PDF p.3; 6 crore / 70% at UFO Q2 PDF p.7; 30-40% annual at Q1 PDF p.5-6. |
| 28 | D (Q3) | B06 Q3 verdict and net read | PARTIALLY VERIFIED against the net read "neither backs nor refutes"; should be UNVERIFIABLE or the net read reworded (UFO not silent on content selectivity, so not an upgrade from silence). |
| 29 | D (Q5) | Wonderla Q2 PDF p.4 (lines 152-155); WONDERLA-Concall_Feb_2026 .txt lines 65-66, 108-109, 124 (PDF pp.2-3) | Wonderla Q2 ATP -3% to Rs 983 is consolidated and includes Chennai at Rs 948, which an analyst says is 20% below the 3 quarter average; B06 does not state the mix effect; existing park ATP not split. Wonderla Q3 FY26 call unused: footfall flat (9.17 lakh Q3; 9M 23.4 against 23.7 lakh), growth described as ARPU and new parks, FY ARPU +8%; qualifies B06 "Wonderla chose volume". |
| 30 | D (Q4 / Part 2C) | WONDERLA-Concall_May_2026 .txt lines 385-393 (PDF p.11) | Wonderla Q4 FY26: "we recalibrated and we felt that we will do Tier 1 -- we will focus on Tier 1 more than the Tier 2 cities". B06 gives land and licences as the reason and calls Bhubaneswar the small format analogue; the strategy shift away from small parks is unused. |

### INFO

| # | Verifier | Location anchor | Note |
|---|---|---|---|
| 31 | D (all) | B06 whole | No VERIFIED verdict in B06 (0 of 9), so the two anchor rule is not triggered. All 9 peer_questions have a verdict. No upgrade from silence found. CINELINE NOT PROVIDED is correctly shown as not an unused file. |

## Verifier B spot checks and grade view

Promise delivery spot checks: 5 checked, 5 confirmed, 0 wrong. Credibility grade concurrence: "lower: to the B/C boundary; the financial-delivery leg rests partly on a ROCE benchmark moved from 18% (Feb p.18) to about 13% (Nov p.4) and an FY26 FCF headline that likely includes Rs 226.8 Cr of divestment proceeds, plus three calls of silence on the developer-kickback assessment (20260907 p.1)". Pipeline flags not supported: none.
