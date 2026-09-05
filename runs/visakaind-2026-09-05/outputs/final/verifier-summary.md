# Verifier summary, Phase 1
Visaka Industries Ltd (VISAKAIND) | Run: runs/visakaind-2026-09-05 | Run date:
2026-09-05

Phase 1 scope. Verifier C ran its Gate 0 and Emerging Moat portion only; its
valuation portion is pending Phase 3, because stages 10 and 11 did not run. No
commentary is added beyond what the verifiers wrote.

---

## Confidence delta and acceptance rates

| Component | Score | Verifier | Block | CRITICAL | MAJOR | MINOR |
|---|---|---|---|---|---|---|
| Numerical acceptance | 100 | A (haiku-4-5) | B12a | 0 | 0 | 0 |
| Red flag coverage | 53 | B (opus-4-8) | B12b | 1 | 12 | 7 |
| Framework adherence, Phase 1 portion | 82 | C (opus-4-8) | B12c | 0 | 2 | 14 |
| Peer utilisation | 100 | D (sonnet-5) | B12d | 0 | 0 | 6 |
| **Overall** | **53** | min of the four available | confidence.yaml | 1 | 14 | 27 |

Band: FORCED REWORK, below 60.
Rework trigger: B12b red flag coverage 53%, below the 60% floor. No B12a
CRITICAL.
Rework scope: stage 5 concall analysis transcript red flag coverage, and stage
6 peer verification on two verdicts. Verifier A source fidelity is clean, so
the numbers stand.
Framework adherence valuation component: PENDING PHASE 3.

Acceptance rate denominators as the verifiers set them:
- B12a: 62 numbers checked. Source fidelity gate PASS.
- B12b: 16 caught of 30 independently found transcript red flags, plus 5
  partially caught and 9 missed. 8 transcripts read (4 main company, 4 BirlaNu)
  against a rubric that assumes 15.
- B12c: 16 fails across 90 rules checked (Gate 0 54, Emerging Moat 36).
- B12d: 1 of 1 peer with transcripts used substantively and correctly. Everest
  and Ramco carry zero transcripts and were excluded from the substantive use
  test, not penalised for a corpus gap they cannot fill.

---

## Verifier A, numerical acceptance (B12a)

Findings: none. Acceptance rate 100. Source fidelity gate PASS.

| Severity | Location | Note |
|---|---|---|
| (none) | (none) | Zero mismatches identified across 62 numbers |

Coverage note as written: all material financial statement line items verified
(P&L, balance sheet, cash flow, FY26 to FY24), the 10 year historical ROCE and
ROE series, working capital components, related party and ICD transactions,
segment revenue and profit, capital commitments and capex, dividend, dealer
network, subsidiary investments. Four minor anchor drifts on rounding and
screener aggregation, each under 0.3%, none affecting decision thresholds. All
verified figures match source documents within audit tolerance.

---

## Verifier B, red flag coverage (B12b)

20 findings. Acceptance rate 53.

| # | Severity | Location | Note |
|---|---|---|---|
| 1 | CRITICAL | B05 Section 2E, final paragraph | Missed repeated evasion across 2 or more quarters: segment margin disclosure was requested four times across three calls and deferred every time, but B05 states it was requested once in Q2 FY23 and not repeated. The stated fact is wrong and the item never enters repeated_evasions. Anchors: Q4 FY22 p.8 (Deep Gandhi); Q1 FY23 p.8 (Ankit) and p.11 (Deep Gandhi); Q2 FY23 p.16 (Rajat Setiya) |
| 2 | MAJOR | B05 Section 1B "Vnext margin (reiterated)"; Section 4A trigger 1 | Gross versus EBITDA basis conflation carried forward unflagged; a Section 1B margin assumption built on this rests on an unresolved basis ambiguity. Anchor: Q1 FY24 call, Vamsi Krishna / Dhananjay Mishra, p.8 |
| 3 | MAJOR | B05 Section 3D distribution bullet | Inverted inference: a falsified distribution growth claim read as one of the few quantitatively consistent claims in the corpus. Anchors: Q2 FY23 p.17; Q1 FY24 p.14 |
| 4 | MAJOR | B05 Section 1B and Section 4A | Missed internal guidance contradiction between the Rs 1,000 Cr by 2030 target, about 14% a year, and the 25% to 30% growth guidance given in the same call; both carried forward unreconciled. Anchor: Q1 FY24 call p.5, p.8, p.10 (Madhur Rathi exchange) |
| 5 | MAJOR | B05 Section 1B roofing utilisation row | Missed volunteered negative, "though rural income is down at the moment", paired with utilisation above 100% and a halved segment EBIT of Rs 27 Cr against Rs 53 Cr. The corpus's clearest price taker evidence, thesis critical for the Quality Ladder rung. Anchor: Q1 FY24 call, Vamsi Krishna, p.4 and p.6 |
| 6 | MAJOR | B05 Section 2A row 2 and Section 2B | A management figure that was re-based to sequential and then partly retracted on the call is adopted as established fact (the 30% asbestos input cost figure). Anchor: Q2 FY23 call p.6 and p.8 (Dhananjay Mishra exchange) |
| 7 | MAJOR | B05 Section 2D and Section 4D | Missed governance contradiction in the Vigilant Security Services exchange on a promoter controlled small cap; the exchange contradicts itself across three turns and is absent from B05 in full. Anchor: Q1 FY23 call, Vamsi Krishna / Ankit, p.7-8 |
| 8 | MAJOR | B05 Section 1B FX row and Section 2D | Missed unanswered hedging policy question and a unit ambiguous, implausible exposure figure of "40 to 45 lakhs", both carried forward as guidance. Anchor: Q2 FY23 call, Shafiulla / Sunny Wadhwa, p.11-12 |
| 9 | MAJOR | B05 Section 1C Vnext row | Under weighted same call contradiction: 43% volume growth against 5% to 10% revenue growth, implying a 25% to 30% realisation fall nobody explained; two different utilisation figures in the same call merged into a range |
| 10 | MAJOR | B06 Claim 5 and Part 4 | Overstated CONTRADICTED verdict resting on unaudited peer self description and an unreconciled two base utilisation comparison; billed downstream as the run's strongest peer finding. Anchors: BirlaNu Q1 FY26 p.17; Q2 FY26 p.5 |
| 11 | MAJOR | B06 Claim 1 verdict and net read | Under weighted contradiction: the verdict reads as corroborating management when the peer evidence contradicts the specific "one off" claim Visaka made; B06's own Section 2B has the correct reading. Anchors: Q2 FY23 p.5, p.6; BirlaNu Q1 FY26 p.20, Q4 FY26 p.9-10 |
| 12 | MAJOR | B06 Claim 8, flags, risks_peers_raise | The peer's 400 to 600 bps profitability lead over its whole competitor set, the most valuation relevant peer number in the four transcripts, is used only as evidence of a competitor naming policy and never reaches any claim, flag or risk line |
| 13 | MAJOR | B05 red_flags, promoter pledge row | Severity understated at Low-Medium for a 57% pledge on one promoter's holding, disclosed only under a retail investor's question with the aggregate issued after the CEO's closing remarks |
| 14 | MINOR | B05 Section 1C debt row and Section 4D | Debt reduction guidance flagged correctly, but not that it was conditional on no further expansion and the condition was broken inside the same call; the Rs 75 Cr Hyderabad land purchase with no stated use is absent |
| 15 | MINOR | B05 Section 2A row 4 | The Rs 60 to 70 Cr ATUM figure attributed to the Q1 FY23 call; it was floated in the Q2 FY23 call, p.9. Row direction otherwise correct |
| 16 | MINOR | B05 Section 2A row 2 | Blended Building Products EBIT of 4.4% compared directly against a Vnext only 12% claim; the basis problem is stated in 2A-bis but not where the comparison is drawn |
| 17 | MINOR | B05 red_flags row 3 and Section 2A-bis ATUM row | "Zero revenue disclosure across three calls" overshoots the record; Q1 FY23 p.12-13 gives FY22 ATUM revenue of about Rs 20 Cr and a Q1 range of Rs 5 to 8 Cr, which B05's own body text acknowledges |
| 18 | MINOR | B05 Section 2A-bis yarn row and guidance list | The Q2 FY23 "15%" yarn figure originated in the analyst's question, not management's answer; the Q1 FY24 "15% upwards" is management's own and does support the flag |
| 19 | MINOR | B05 anchors throughout against B06 anchors throughout | Divergent anchor conventions in one run, differing by one; risks false ANCHOR NOT FOUND downstream. One B06 anchor also off by one within its own convention |
| 20 | MINOR | B05 Section 2C and Section 4D | Missed presentational flag: the Q1 FY24 script leads with plus 35% sequential EBITDA and buries minus 42% year on year in the same breath, and mislabels the year ago PAT comparator as "the previous quarter" |

Other verifier B records:
- Pipeline flags not supported by evidence: none. No pipeline flag is
  fabricated.
- Pipeline flags overstated: 2, both in B06 (Claim 5 verdict, Claim 1 net read).
- Pipeline inference inverted: 1, in B05 Section 3D.
- Promise delivery spot checks: 6 checked, 6 confirmed, 0 wrong. Two rows carry
  internal imprecisions that do not change the verdict.
- Credibility grade: concur, D (Poor), reached from the transcripts alone before
  any annual report evidence. B05's audited delivery record makes D generous;
  the verifier would place it at the bottom of the band and would not grade
  higher.
- Peer quote fidelity: 10 B06 peer quotes checked against the four BirlaNu
  transcripts. All exist and are accurately rendered. 9 of 10 anchors land on
  the cited PDF page; 1 is off by one. No fabricated peer quote found.
- Acceptance rate note: reported unadjusted. The denominator is deliberately
  granular, because a coarser flag list would score higher and hide the specific
  defects. The rate measures transcript level red flag coverage only; B05's
  audited FY24 to FY26 delivery work in Section 2A-bis is strong and found
  material items unreachable from transcripts alone. The deficits are one
  inverted inference, two overstated peer verdicts, and nine genuine misses.

---

## Verifier C, framework adherence, Gate 0 and Emerging Moat portion (B12c)

16 findings. Acceptance rate 82. Valuation portion: pending Phase 3, 0 rules
checked, 0 fails.

| # | Severity | Location | Note |
|---|---|---|---|
| 1 | MAJOR | B01 Block E, E2 | Mandated 3 year promoter change window replaced by a 1 year window and scored at the maximum band of 5, on a plus 4.82pp move the same report calls unexplained and unverified, with 0.00% change in both named individual promoters. Rule 5 directs N/A and 0 when a data point is unavailable. Recomputed E2 = 0, Block E 9/20, core 51. Classification stays AVERAGE |
| 2 | MAJOR | B07 YAML, evidence_mix | evidence_mix {documented 16, claim 13, inference 5} is not reconcilable to the report body. No analyst inference item is tagged anywhere, so the count of 5 has zero supporting items. The documented count of 16 contradicts the body, which enumerates 13 items supporting the Moderate rows plus at least 5 further documented facts. No effect on em_score because multipliers apply per category |
| 3 | MINOR | B01 Formula Notes and Block A | Two capital employed bases blended in one 10 year ROCE series against the fixed formula rule. Disclosed in input_gaps and cross validated at FY26 (proxy 12.57% against AR 11.87%). No effect on A1, A2 or A4. Consequential at M3: on the proxy basis FY26 ROCE clears the above 12% leg and M3 would score 1, moat score 13, no class change |
| 4 | MINOR | B01 Block B | B1 runs on 10 years while B2, B3 and B4 run on 3 years, so the 17/20 block total mixes windows. B3's 1.367 ratio is flattered by an FY24 to FY26 PAT denominator of 90.50 containing both trough years and the FY26 one off. Disclosed. Deal breaker 2 cannot fire in any variant because B1 and B4 alone hold Block B at or above 10 |
| 5 | MINOR | B01 Block D, D2 | Interest coverage of 4.34x scores 2 on an EBIT numerator containing the Rs 59.70 Cr land gain. The report computes the ex exceptional 2.53x and calls it the decision relevant figure, then scores the higher band. Recomputed D2 = 1, Block D 12/20, core 55. Classification stays AVERAGE. D1 tested and robust: ex exceptional net debt to EBITDA is 1.858x, same band |
| 6 | MINOR | B01 Block F, M8 | The M8 rubric has no band for a network that is quantified and shrinking. Band 1 reads mentioned and unquantified, band 0 reads none or purely digital; neither fits 4,974 dealers down from 5,246. The report chose 0 and stated why. Conservative and disclosed. The defect is in the rubric. Alternate reading M8 = 1 gives moat score 13, no class change. Framework amendment candidate |
| 7 | MINOR | B01 M3 and M1 | Two scored inputs carry no anchor at the point of use. M3's Net Block of 676.89 is unsourced and does not reconcile to B07's AR sourced net PP&E of 675.98. M1's FY17 operating EBITDA margin of 12.20% is unsourced and its components are not shown. Rule 4 states an unanchored number counts against the stage. Existence routed to Verifier A |
| 8 | MINOR | B01 output format | The mandated dashboard format requires moat profile bars and a classification box. Neither is present. All blocks, line items, strongest and weakest block, and the decision line are present. Presentational only |
| 9 | MINOR | B07 Section 3 recount against YAML completionist_recount | The body attributes the 13 documented items as A3 5, G2 3, R1 3, plus 2 capex table items. The YAML attributes them as A3 5, G2 3, R1 5, folding the 2 capex items into R1 without explanation. Both total 13. The recount is the completionist guard artifact and must be exact |
| 10 | MINOR | B07 Sections 1A, 1C, 6B | Several evidence items name a document but give no page or slide, against the mandated (AR p.__) anchor format. Examples: the yarn margin series cited to AR2025 and AR2026 segment notes; the 3 ATUM Life stores cited to AR FY26 BRSR; the 22% to 25% input cost rise cited to the Aug-2023 call |
| 11 | MINOR | B07 scorecard rows B1 and H3 | Both are mixed evidence rows graded at the documented 1.0 multiplier. B1's headline raw material security claim rests on a concall quote, with only the captive solar plant documented. H3's "among the few" GreenPro exclusivity claim is self assessed and unverified against peers, with only the certificates documented. Grading to the documented leg over credits 0.6 points. em_score 13.9 on the stricter read. Band unchanged |
| 12 | MINOR | B07 scorecard row A3 | A3 is graded HM, raw 3, adjusted 3.0, while Section 6E of the same report calls A3 the smallest in likely financial impact. An HL grade gives raw 2 and em_score 13.5. Band unchanged |
| 13 | MINOR | B07 YAML, catalysts_12m | Two of five entries carry a 12 to 24 month window inside a field named for 12 months. The field feeds Pillar 3 catalyst proximity at Stage 11, where a 12 to 24 month catalyst is less proximate. Each entry does state its own window, so a careful Stage 11 read recovers the truth |
| 14 | MINOR | B07 Section 6E against YAML catalysts_12m | The body lists dealer count reversal as a 12 month catalyst; the YAML omits it and substitutes total debt holding at or below Rs 350 Cr. Both are defensible. The two lists should agree |
| 15 | MINOR | B07 against B01, cross artifact | Three divergences with no reconciling note. FY26 capex of Rs 36.75 Cr anchored to AR FY26 p.155 in B07 and p.158 in B01. The nil R&D statement anchored to p.92 in B07 and p.95 in B01. Total debt stated as Rs 579 Cr FY24 and Rs 350 Cr FY26 in B07 against Rs 534.98 Cr and Rs 303.44 Cr in B01, a lease liability definition gap B01 flags at D3 and B07 never names. B07 also carries WC tenure of 94 and 81 days against B01's computed 110.51 and 92.42 days; different series, both anchored. Page anchor truth routed to Verifier A |
| 16 | MINOR | B07 Section 5 | em_score of 14.5 sits 2.5 points above the 12 point NONE floor, and G2 alone carries 3.0 of it, or 21%. Excluding G2 gives 11.5 and flips em_classification from MODEST to NONE. G2 is graded already realised, which sits awkwardly against the scan's forming moat scope line, though the G2 category text does contemplate a realised trend. The sensitivity is not disclosed anywhere in B07 |

Rule level fails as recorded:
- Gate 0, 54 rules checked, 7 fails: G-06 ROCE formula fidelity; G-13 Block B
  window consistency; G-22 D2 interest coverage on an EBIT basis containing the
  Rs 59.70 Cr one off (recomputed D2 = 1); G-27 E2 promoter change window
  (recomputed E2 = 0); G-38 M8 distribution band fit; G-49 Rule 4 anchors (Net
  Block 676.89 and FY17 operating margin 12.20% unanchored at point of use);
  G-51 output format (moat profile bars and classification box absent).
- Emerging Moat, 36 rules checked, 9 fails: E-11 completionist recount; E-13
  Rule 3 anchors; E-14 evidence_mix not reconcilable; E-17 rows B1 and H3
  over credit 0.6; E-18 A3 impact grading conflict; E-31 catalysts_12m window
  field; E-32 Section 6E and YAML catalyst lists disagree; E-35 cross artifact
  divergence with B01; E-36 em_score sensitivity not disclosed.
- Business Understanding Narrative check: NOT ASSESSED. Stage 13 was not among
  the Phase 1 inputs; deferred to the finalize verifier pass.
- recomputed_destination_pe and recomputed_decision: empty. Valuation pending
  Phase 3.

---

## Verifier D, peer utilisation (B12d)

6 findings. Acceptance rate 100. Peers audited 6 rows: BirlaNu across four
quarters, all SUBSTANTIVE and all with real, findable citations verified against
the transcript text, plus the Everest and Ramco no transcript rows. Substantive
unsupported: none. Verdict discipline fails: none. All claims addressed.

| # | Severity | Location | Peer and quarter | Note |
|---|---|---|---|---|
| 1 | MINOR | B06 Claim 5, peer evidence row | BirlaNu Q2 FY26 | Quote "nearing full utilization" (Chennai Line 2) cited as p.5; actual location is transcript marker PAGE 3, opening remarks. Content and speaker correct, page wrong |
| 2 | MINOR | B06 Claim 1, peer evidence row, Q4 FY26 sentence | BirlaNu Q4 FY26 | Fibre and cement input cost quote cited as p.9-10; actual quote spans transcript markers PAGE 10-11, Akshat Seth. Correct anchor is p.10-11 |
| 3 | MINOR | B06 Part 2, cross read item (a), rural demand paragraph | BirlaNu Q4 FY26 | "Underlying resilience in the rural economy" plus the steel price gap quote cited as p.9; actual location is transcript marker PAGE 10, Akshat Seth |
| 4 | MINOR | B06 Part 2, section 2A demand environment | BirlaNu Q4 FY26 | "Strong bounce back from H1" quote cited as p.6; actual location is transcript marker PAGE 4, Akshat Seth, opening remarks, Roofs segment. Largest anchor drift found, 2 pages |
| 5 | MINOR | B06 Claim 7 and peer coverage map, Q1 FY27 row | BirlaNu Q1 FY27 | Granular Nellore, OPVC and Hyderabad capex phasing figures on pp.23-25 not cited; would have sharpened but not changed the Claim 7 capex scale benchmark |
| 6 | MINOR | B06 Claim 4 and Claim 8, industry structure context | BirlaNu Q1 FY27 | Boards industry structure detail, 5 to 7 organized players and 15% to 20% import share, p.16, not cited; industry context miss, does not change any verdict |

Unused but relevant peer material recorded: the Q1 FY27 capex phasing (Nellore
Boards Rs 127 Cr, OPVC Rs 40 Cr completed, Hyderabad plant at 0.9x asset turn
targeting about Rs 140 Cr revenue) at pp.23-25, and the boards industry
structure detail at p.16.

Denominator used: peers with transcripts provided to this run, BirlaNu = 1.

---

## Verifier disagreement log

none.

Verifier A logged no source fidelity finding, so no downstream step's conclusion
had a flagged number to conflict with. No re derivation leaned on a flagged
figure, no step sought to keep a figure Verifier A flagged, and no source re
check cleared a flag.

---

## Anchor convention split

Recorded by Verifier B as anchor_convention_defect: true.

Stage 5 anchors on the transcripts' printed footer page numbers. Stage 6 anchors
on PDF pages. The two differ by one throughout the run. A downstream re check of
a stage 5 anchor against a PDF page lands one page early and can produce a false
ANCHOR NOT FOUND. Verifier B logged this as MINOR finding 19; Verifier D's six
findings are all anchor drifts inside stage 6's own PDF page convention, the
largest being 2 pages.
