# VERIFIER SUMMARY: CYIENTDLM, run 2026-09-06 (PHASE 1)

Scope: verifier A (numerical), verifier B (red flags), verifier D (peers), and the Gate 0 plus emerging moat portion of verifier C (framework). Verifier C's valuation adherence audit is PENDING phase 3, because stages 10 and 11 did not run. Verifier C's business understanding narrative check is not applicable in phase 1.

## PHASE 1 CONFIDENCE DELTA

| Component | Score | Verifier | Basis |
|---|---|---|---|
| Numerical acceptance | 100 | B12a (run 2) | 67 of 67 numbers matched source; zero findings; zero source fidelity findings |
| Red flag coverage | 54 | B12b | 13 of 24 independently found red flags carried upstream (8 caught, 5 partial, 11 missed) |
| Framework adherence | 87 | B12c | Phase 1 scope only: Gate 0 94%, emerging moat 77% |
| Peer utilisation | 100 | B12d | 3 of 3 peers, 12 of 12 transcripts substantive |
| **Overall** | **54** | orchestrator | Minimum of the four. Band: below 60. Consequence: FORCED REWORK. |

## ACCEPTANCE RATES

| Verifier | Model | Acceptance rate | Checks run | CRITICAL | MAJOR | MINOR | Rework trigger |
|---|---|---|---|---|---|---|---|
| A — numerical (B12a, run 2) | claude-haiku-4-5 | 100% | 67 numbers checked | 0 | 0 | 0 | false |
| B — red flags (B12b) | claude-opus-5 | 33% | 24 independent flags found | 1 | 8 | 7 | true |
| C — framework (B12c) | claude-opus-4-8 | 87% | 106 rules checked, 92 passed | 0 | 3 | 11 | false |
| D — peers (B12d) | claude-sonnet-5 | 100% | 45 citations checked | 0 | 0 | 9 | false |

Verifier C sub scopes: Gate 0 acceptance 94% (62 rules checked, 58 passed); emerging moat acceptance 77% (44 rules checked, 34 passed).

Totals across all four: 1 CRITICAL, 11 MAJOR, 27 MINOR.

## CRITICAL

| Verifier | Location | Anchor | Finding |
|---|---|---|---|
| B | B05 2E / 4D / 4A row 3 | Apr-2026 call p.19; Jul-2026 call p.14; Kaynes Aug-2026 call p.15 and p.19; Syrma Aug-2026 call p.4 and p.9 | Repeated two quarter plus evasion on gross margin compression missed entirely. The Q1 FY27 answer attributes a gross margin decline to operating expense investments, which is mechanically impossible. The industry wide component and PCB cost shock disclosed in detail by both Kaynes and Syrma in the same window is absent from the 21-Jul-2026 call, yet B05 rates double digit EBITDA sustainability at conviction HIGH. |

## MAJOR

| Verifier | ID | Location | Anchor | Finding |
|---|---|---|---|---|
| B | — | B05 2A row 5 / 4D | Oct-2025 call p.6; Jan-2026 call p.5 and p.7; Apr-2026 call p.5 and p.7 | The order book bridge fails to reconcile in every FY26 quarter, about Rs30cr in Q2, Rs26cr in Q3 and Rs120cr for the full year against the claimed 1.5x book to bill. No cancellation, de scope or FX disclosure appears anywhere. B05 derives one quarter's gap but does not identify the systematic pattern or qualify its DELIVERED verdict on book to bill. |
| B | — | B05 3D / 4D | Apr-2026 call p.4 and p.8 | Exports share stated two ways inside one call: 60 plus percent of revenue from exports, and rest of world accounting for over 90% of revenues. Neither report flags the contradiction. |
| B | — | B05 1A / 4D | Apr-2026 call p.3, p.7, p.8; Jul-2026 call p.8 | One order book figure is described three ways in the same call: highest it has ever been, highest level in the last 10 quarters, and highest since 2.5 years. The Rs21.3bn base is assigned to Q1 FY25 in one call and Q1 FY26 in the next. Unflagged. |
| B | — | B05 2C / 4C | Oct-2025 call p.2 (Shrinivas Kulkarni); Jan-2026 call p.2 and p.3 (R.M. Subramanian, his first investor call as CFO) | An unexplained CFO change between the Oct-2025 and Jan-2026 calls is absent from the credibility assessment and from the red flag list. The same window contains the Altek earn out reversal, a written off acquisition, and the introduction of normalized reporting. |
| B | — | B05 4A row 3 / 1A | Jul-2026 call p.3 and p.7; Jan-2026 call p.7 | The claim of double digit EBITDA for four consecutive quarters holds only on the normalized basis. Reported Q3 FY26 EBITDA margin was 9.1%. B05 repeats the claim at conviction HIGH without the qualifier. |
| B | — | B05 ANALYST NOTE | Apr-2026 call p.6; Jul-2026 call p.6-7 | The fact B05 uses to hold the credibility grade at C, Q1 FY27 revenue up 34.3% YoY, is not adjusted for the sequential picture. Sequentially revenue was up only 1.3% QoQ and EBITDA margin fell 120bps from 11.7% to 10.5%, with absolute EBITDA down from Rs431mn to Rs392mn. The YoY figure is measured against a depressed base. |
| B | — | B06 Q3 / Part 4 | Avalon Feb-2026 call p.2 and p.3; Apr-2026 call p.13 and p.17 | A peer contradiction held in hand and left unused. B06 quotes Avalon's 50% to 18% tariff settlement of 5-Feb-2026 to verify exposure, but never tests it against the Cyient DLM claim on 21-Apr-2026 that there is no clarity and the cloud has not gone away. |
| B | — | B05 1B / 1C / 4D | Oct-2025 call p.11 and p.15-16; Jan-2026 call p.5 and p.15-16; Apr-2026 call p.12; Jul-2026 call p.8-9 | B2S disclosure withdrawal is under weighted. The share was quantified at 5%, then 6-7%, then refused in Q4 FY26 with the statement that last year we did not have this, this is the first year we are having it, which contradicts the Oct-2025 disclosure. The FY27 double digit target was silently dropped. B2S is the thesis's primary margin uplift mechanism. |
| C | F-G01 | B01 report, data availability declaration and Classification section | B01 report | The declared 4 year scoring window is outcome determining and unratified. At 4 years the LIMITED confidence tier fires a one tier downgrade that turns AVERAGE into AVOID. The company's own ROCE series reaches FY2022, and on a 5 year declaration the tier carries no downgrade, leaving AVERAGE even with A4 falling to 0 (core 40, still inside the 40-59 band). The report discloses the A4 sensitivity but never runs the confidence tier consequence. OPERATOR RULING REQUIRED before AVOID travels downstream. |
| C | F-G02 | B01 report, Block F, test M4 | B01 report, M4 | M4 scored 1 where no prompt band is satisfied. One revenue decline year, unrecovered, fails the 3 band condition "fully recovered", and the 1 band's stated condition is "2 decline years". The score was awarded by analogy, while M10 two tests later applies the strict else-0 reading on the identical receivable days leg. Recomputed Block F is 3/60 and the grand total 46/160. Moats confirmed, moat class THIN and classification AVOID are all unchanged. |
| C | F-E01 | B07 Section 5 scorecard, row B2 | B07 report Sections 5, 6D, 6E | B2 qualification lock in is scored HH=4 at 1.0x, the largest single row, while the report itself states in 6D and 6E that the advantage predates FY26 and is not emerging. The genuinely new increment (IATF16949, NADCAP cable harness re scope) is already scored at R1=3.0, and the report's own recount concedes B2 and R1 share the certification evidence base. That credits one quality improvement through two mechanisms. Recomputed em_score is 20.0 rescoring B2 on the increment, or 17.0 removing it, against 21.0 reported. The MODEST band and the EM 25 UA miss hold in every case. |

## MINOR

| Verifier | ID | Location | Anchor | Finding |
|---|---|---|---|---|
| B | — | B05 3D | Jul-2026 call p.8-9 | The Q1 FY27 product category mix sums to 80%, not 100% (PCBA 48, box build 21, mechanical and others 10, cables 1). Twenty points of revenue mix are unaccounted for, with B2S inside the residual. |
| B | — | B05 1B / 4D | Jan-2026 call p.8; Apr-2026 call p.8 | IPO proceeds move from 93.2% total and 15.4% capex utilisation at Dec-2025 to fully utilised and closed one quarter later, unexplained, and the date is stated as March 2025, a year wrong. |
| B | — | B05 2A row 8 | Jan-2026 call p.5; Apr-2026 call p.14 | Management confirmed an analyst's incorrect restatement of its own disclosure, four new clients in the defence vertical against the actual two transportation, one industrial, one defence. B05 scores the same exchange DELIVERED. |
| B | — | B05 2B / 4D | (no anchor recorded by the verifier) | The Israel and West Asia flip from named tailwind in Oct-2025 to primary excuse in Apr-2026 is not flagged as an unacknowledged narrative reversal. |
| B | — | B05 3A / B06 Q2 | (no anchor recorded by the verifier) | Neither report notes that management answers an order BOOK growth question with an order INTAKE statistic, a non comparable metric, and supplies no figures for either. |
| B | — | B06 Q4 / Part 2A | (no anchor recorded by the verifier) | Avalon's explicit "nothing that we see is critical", on the same Middle East PCB and raw material disruption Cyient DLM blames for its entire Q4 miss, is not surfaced as a magnitude contradiction. |
| B | — | B05 2D / 4C | (no anchor recorded by the verifier) | The FY26 headline that reported PAT increased 7.7% is produced entirely by reversing an earn out that was reversed BECAUSE the acquisition missed its targets, while normalized PAT fell 24%. The framing consequence is not flagged. |
| C | F-G03 | B01 report, B4 and M12 | B01 report | The prompt's fixed working capital days formula (receivable plus inventory minus payable) was replaced by the company disclosed NWC days KPI, against the instruction not to substitute alternatives. Disclosed with cause and score invariant. |
| C | F-G04 | B01 report, M4 line | B01 report | The M4 line says judgment flagged, see analyst_note. The analyst_note does not mention M4. A dangling cross reference on the one line item that most needed the explanation. |
| C | F-E02 | B07 Section 3 | B07 report | The prompt asks for an evidence table or NO EVIDENCE FOUND per category. Categories are presented as anchored prose instead. The 23 row summary table supplies the required structure, so the loss is presentational. |
| C | F-E03 | B07 report body and block evidence_mix | B07 report and block | The analyst inference tier is never applied anywhere and evidence_mix reports inference 0, although the report makes and labels inferences in prose (the C2 consolidation artifact reading, the 2C utilisation not capex conclusion, the 6E base rate argument). No score effect. |
| C | F-E04 | B07 Section 3, completionist recount line | B07 report | The mandated recount line states 13 documented items across 6 categories, then names seven (B1, B2, C2, F1, G2, H3, R1), and the block says seven. The stated count contradicts its own list and the block. |
| C | F-E05 | B07 categories H2 and G1 | B07 report | A few evidence items carry no page anchor, for example "related party term loan structure, AR consolidated notes". The prompt requires an anchor on every evidence item. |
| C | F-E06 | B07 Section 3, category I2 | B07 report | The cannibalisation test is answered for B2 only; C1, C2 and R1 are covered by a generalising sentence rather than individually. The score would remain 0 in each case. |
| C | F-E07 | B07 optionality register against block optionality_register | B07 report and block | Nine rows in the report table, eight in the block. The rung jump B2S row is not carried, so it is lost to synthesis. Its content overlaps the carried B2S transform phase row. |
| C | F-E08 | B07 Section 3 summary table and block | B07 report and block | Strength labels depart from the prompt's Strong / Moderate / Weak / None set: Weak-Moderate, None (negative), Moderate (artifact-caveated). Boundary case B1 was resolved conservatively and excluded from active_categories, so there is no outcome effect. |
| C | F-E09 | B07 block, evidence_mix | B07 block | The claim count of 22 is not enumerated or reconcilable from the report body, unlike the documented count of 13, which is itemised. It cannot be checked from the artifact. |
| C | F-E10 | B07 block | B07 block | Five fields sit outside the mandated schema: em_score_scale, ua_qualifier_threshold, ua_qualifier_met, capex_embedded_growth_note, orchestrator_note. All informative, none contradictory; the risk is only to a strict downstream parser. |
| D | — | B06 Part 1 Q7 / KAYNES Q4 FY26 citation | cited p.2, actual p.4 | The 122 days for FY26 NWC figure is cited as p.2; the actual location is p.4, in the same paragraph as the correctly cited 83 to 53 day core EMS figure. |
| D | — | B06 Part 1 Q4 / KAYNES Q1 FY27 citation | cited p.14-15, actual p.5 | The phrase "6 to 8 months even for order booking" is folded into a p.14-15 citation range with the 30-35% price rise quote; the order booking phrase actually appears on p.5 of the same call, in a different discussion. |
| D | — | B06 Part 3 map / KAYNES Q1 FY27 citation | cited p.14, actual p.13 | Receivables to INR1,925 crores cited p.14; actual location p.13. |
| D | — | B06 Part 1 Q3 / SYRMA Q2 FY26 citations | cited p.6, actual p.7 | The tariff exposure quote (5-6% of revenue) and the "last ball is yet to be born" quote are both cited p.6; both are actually on printed p.7. |
| D | — | B06 Part 1 Q6 / SYRMA Q3 FY26 citation | cited p.12, actual p.11 | The "gestation period is pretty long, lumpy" quote cited p.12; actual location p.11. |
| D | — | B06 Part 2A and Part 1 Q7 / SYRMA Q4 FY26 citations | cited p.5 and p.4, actual p.4 and p.5 | FY26 revenue +27% cited p.5 (actual p.4); OCF INR290cr and the 63-58 day NWC cited p.4 (actual p.5). The slips run in opposite directions within the same transcript. |
| D | — | B06 Part 1 Q1 / SYRMA Q4 FY26 citations | cited p.14, actual p.13 | The "$1 billion company", Jabil, $20bn/$25bn and the $600 million addressable market quotes are both cited p.14; actual location p.13. |
| D | — | B06 Part 2D / SYRMA Q4 FY26 citation | cited p.15, actual p.12 | The L&T INR50bn EMS capex competitive threat flag cited p.15; actual location p.12. The largest single page gap found, 3 pages. |
| D | — | B06 Part 1 Q7 / SYRMA Q1 FY27 citations | cited p.5, actual p.6 | The NWC to 71 days and net cash INR122cr figures are both cited p.5; actual location p.6. |

## VERIFIER A: FINDINGS AND ADJUDICATIONS

Verifier A returned zero findings on run 2. 67 of 67 numbers matched source. Zero fabrications, zero material misreads, zero source fidelity findings. Run 1 is preserved at outputs/reports/12a-verifier-numerical-run1.md; its three routed conflicts moved to adjudications on run 2 and are logged in outputs/final/verifier-disagreement-log.md.

Three adjudications, each a ruling on a company disclosure inconsistency the pipeline stages surfaced correctly.

| Conflict | Sources checked | Ruling | Downstream must use |
|---|---|---|---|
| DSCR, FY25 comparability break | AR FY2025-26 Note 35 standalone p.136 (FY25 1.67x, FY26 0.62x); AR FY2024-25 Note 35 standalone p.215 (FY25 0.15x, FY24 0.20x) | Both figures present at their cited anchors. Neither report misread its source. The two ARs are not comparable on this ratio. | FY26 DSCR of 0.62x is reliable. Do NOT use the 1.67x to 0.62x fall as evidence of a one year covenant coverage collapse. DO use the negative CFO trend and the sub 1.0x FY26 fact. |
| Build to Spec revenue share, 25% against 6% | AR FY2025-26 BRSR Section 16 p.62-63 (25% of turnover); SET framework infographic p.7 ($8.8M of $141.9M, 6.19%); Note 20 p.144 (services transferred over time, 10.3% of standalone revenue) | Both figures present at their cited anchors and both internally accurate on different reporting bases. The AR provides no reconciliation. | Use 6% for FY26 operational analysis. Treat 25% as a statutory classification on an unmapped basis. Reconcile with management before any valuation use. Do not average the two. |
| M&A evaluation one off, currency mismatch | Q3 FY26 concall p.9 ($17.75 million); Q4 FY26 concall p.9 (INR 17.75 million) | Both transcripts say what stage 5 reported. Stage 5 transcribed faithfully and flagged the discrepancy correctly. | Use INR 17.75 million from the Q4 call, post audit close and consistent with the surrounding rupee figures. Do not use $17.75 million. Confirm with the company in writing. |

Coverage note recorded by verifier A: 67 load bearing numbers verified across all 11 stage reports for stages 0 to 9. 100% of verdict card and block score inputs verified; about 40 material finding anchors spot checked; all repeated cross report figures tracked; full adjudication of the three routed conflicts. Scope is about 45% of all numerical claims. Not verified: intermediate ratio components, peer concall figures (verifier D scope), forward guidance, rounding noise.

## VERIFIER NOTES CARRIED VERBATIM IN SUBSTANCE

Verifier B, credibility grade concurrence: "NO. Would grade lower, C-minus to D rather than C. The B05 grade omits the unexplained CFO change, the normalized-basis dependency of both headline margin claims, three internal figure contradictions inside single calls, and a mechanically impossible answer to the one input-cost question both peers answered in full." Promise delivery spot checks: 6 checked, 6 confirmed, 0 wrong. Pipeline flags not supported: none.

Verifier C, headline classifications: Gate 0 AVOID and emerging moat MODEST both survive every recomputation. Grand total 46 recomputed against 47 reported; em_score 17.0 to 20.0 recomputed against 21.0 reported. Neither band moves and the UA conclusion is unchanged. One operator ruling required: F-G01.

Verifier D, root cause of all nine findings: the KAYNES and SYRMA transcript PDFs carry a filing cover page, so the printed footer page number runs behind the raw PDF page number. The pipeline's page marked extraction stamps the raw PDF page and stage 6 anchored to that. Content is correct in every case. Zero fabrications, zero misattributions, zero content errors across 45 plus discrete citations. Verdict discipline held: no VERIFIED claim rests on a single peer anchor, no verdict was upgraded from peer silence, no injected question was skipped.
