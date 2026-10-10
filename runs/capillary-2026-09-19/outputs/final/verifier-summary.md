=== FILE: verifier-summary.md ===

# CAPILLARY verifier summary (phase 3, finalize, 10 Oct 2026)

Scope: Verifiers A, B and D in full (phase 1, run 2026-09-19). Verifier C in two halves: phase 1 on Gate 0 (B01) and Emerging Moat (B07) in outputs/blocks/B12c.yaml; phase 3 on the valuation half (B10, B11, expectation-ledger.md), Role 2 extended scope (B14) and check 15 skill to source, in outputs/blocks/B12c-phase3.yaml (merged into B12c.yaml under phase3_merge).

## Confidence delta (phase 3)

| Component | Score | Source | Basis |
|---|---|---|---|
| numerical_acceptance | 100 | B12a | 41 of 41 checked figures clean; material universe 47; phase 1 scope |
| redflag_coverage | 70 | B12b | rubric basis: 1 caught + 6 partially caught of 10 material; 3 MAJOR missed |
| redflag_coverage (strict, for the operator) | 40 | B12b | only partials the pipeline flagged as a concern (#3, #7, #9): 4 of 10; below the 60 REWORK line |
| framework_adherence | 91.2 | B12c + B12c-phase3 | (65 phase 1 + 131 phase 3) / (75 + 140) checks |
| peer_utilisation | 100 | B12d | 12 of 12 peer transcripts used substantively |
| overall | 70 | min of four, set by redflag_coverage | band 60 to 74 |

The orchestrator used the rubric basis as written. The strict basis is surfaced, not resolved. The operator chooses.

## Acceptance rates

| Verifier | Model (block string) | Acceptance | CRITICAL | MAJOR | MINOR |
|---|---|---|---|---|---|
| A (numerical) | claude-haiku-4-5 | 100 (41/41) | 0 | 0 | 0 |
| B (concall red flags) | claude-opus-5 | 70 rubric / 40 strict | 0 | 9 | 16 |
| C phase 1 (Gate 0, Emerging Moat) | claude-opus-5 | 86.7 (65/75) | 0 | 6 | 12 |
| C phase 3 (valuation, Role 2, check 15) | claude-opus-5-5 | 93.6 (131/140); valuation half 94.2 (114/121); Role 2 extended 89.5 (17/19) | 0 | 1 | 8 |
| D (peer utilisation) | claude-sonnet-5 | 92 (11 of 12 peers clean) | 0 | 1 | 0 |
| Total | | | 0 | 17 | 36 |

Verifier A source fidelity: 0 findings with source_fidelity true. No MISMATCH, ANCHOR NOT FOUND or material UNANCHORED items. Verifier disagreement log for this run: none.

Verifier C phase 3 REWORK triggers: none fired. Rules 7, 11, 12, 13 and 14 pass; acceptance 93.6% on a denominator of 140. Verifier C phase 3: "No finding changes the decision. Every reading gives no position at Rs 566.65."

## CRITICAL

None.

## MAJOR

| # | Verifier | Location | Finding |
|---|---|---|---|
| 1 | C (phase 3) | chunk 15 l.92; 11-valuation.md l.245-248, l.684, l.740; B11 YAML l.66; 14-thesis.md l.341 (F-V1) | Chunk 15 drops "that sets the entry zone" from Section 1B v3.9 A20.5 (l.40). B11 used Track 2 16.8x and printed a relative route threshold of 24.0x and a pillar gap of 44.0%. On the source reading the governing track is Track 1 (sets the entry zone under OR-1 as written, B11 l.217): threshold 13.055 / 0.70 = 18.7x; gap 56.5%. 30x still needs an adjusted base of 30x or more. Decision survives. Fix the chunk. |
| 2 | B | B05 1B guidance row, 4A | Organic growth misreported ("20-23% incl. 6% currency"). Transcript: 23% incl ~6% FX = ~17% organic (Q1 FY27 [p18] L742-747); analyst ~11% Q1 organic (L727-731); FY27 plan organic ~Rs 673 Cr vs FY26 acquisition linked Rs 80-100 Cr of 735 implies +3-6% [INFERENCE] (Q1 [p11] L464-469; Q4 [p11] L463-465). Separating observation: H1 FY27 constant currency organic revenue. |
| 3 | B | B05 3B/3D | Healthcare customer contradiction not linked or flagged: Q3 FY26 top 5 payer member base +50% with CY26 revenue bump (Q3 [p10-11] L432-449) vs Q1 FY27 largest (healthcare) customer did not grow, NRR 111% vs 116% ex it (Q1 [p4] L166-167, [p18] L744-745; Anant [p21] L870). Identity of account unconfirmed. MISSED. |
| 4 | B | B05 1C, 2A aiRA | aiRA sizing read as "rising each quarter". Q4: few million $ and 4-5% of revenues from AI stack, not all live (Q4 [p4] L155, [p17] L719-720); Q1: $2-2.5M run rate, <10 paying (Q1 [p10] L393, [p19] L782, [p6] L239-240). Sizing regressed: Q4 4-5% of Rs 734 Cr = Rs 29-37 Cr vs ~Rs 21-28 Cr [INFERENCE]. |
| 5 | B | B05 3D | SessionM $35M business / 40+ logos (Q4 [p5] L203, [p11] L468) restated to $32M ARR / 45-odd customers (Q1 [p7] L266-269, [p9] L364) without comment. Benign reading: revenue vs ARR basis. MISSED. |
| 6 | B | B05 1C, 2C | "$20m gross / Rs 17 Cr net after debt true-up" scored as transparency positive. Anant: adjusted for net debt items; Aneesh: debt free entities (Q1 FY27 [p22] L911-921). ~$18M non debt adjustment unexplained; payback claim rests on Rs 17 Cr ([p7] L279-285). |
| 7 | B | B05 4D | Kognitiv churn indemnity Rs 25 Cr, triggered because seller failed agreed commitments (Q4 FY26 Anant [p9-10] L396-399), logged only as a Low normalisation item; inorganic NRR 96% to 94%. Acquired book retention signal missed. |
| 8 | B | B05 2C | Gross margin contradiction: platform 69-70% (Q3 [p6] L245, [p13] L558) vs organic >75% "for the last few quarters" (Q1 [p5] L195-198). B05 says the numbers were "repeated identically". Direct input to the 26.2 margin bridge. MISSED. |
| 9 | B | B05 4A trigger 6, 1B | New ACV +75% carried unqualified; it holds only ex one customer (Q1 [p8] L326-330). FY26 ACV Rs 121 Cr "similar to LY" (Q4 [p9] L390-391). 30-40% guide base unstated (Q1 [p23] L944-946); "Rs 121 Cr" anchor not in transcript. |
| 10 | B | B06 2E, risks_peers_raise | NOT SUPPORTED: build it yourself (vibe coding) AI risk "not named anywhere in Capillary concalls". Raised and rebutted on Q1 FY27 call (Achint/Aneesh [p17-18] L694-717; Chintan/Anant [p21] L888-906). |
| 11 | C (phase 1) | B01 M11 network effects (F-G1) | Selling % leg read on a different window than the revenue leg; FY23 to FY26 proxy rises 32.5% to 39.2% (screener-Data_Sheet.csv rows 17-18). M11 3 to 1; moat 17 to 15; moats 4 to 3; STRONG to MODERATE; total 68 to 66. Classification AVERAGE unchanged. |
| 12 | C (phase 1) | B01 block_b_trend / FLAG-CASH (F-G2) | Mechanism wrong. 66.6 to 37.0 payable days is FY23 to FY26 and consumes cash. FY26 receivable days fell 98.3 to 89.8 and payable days rose 30.9 to 37.0, both helping FY26 CFO. Multi year WC deterioration (24.0 to 52.8) stands. Propagated into B07 G2. |
| 13 | C (phase 1) | B07 I2 test (F-E1) | Sacrifice test run on H1 only. Must run on C1, D1, B2, A3, F2 and B04's aiRA usage pricing counter positioning. Claim tier score at most +0.7; band survives. |
| 14 | C (phase 1) | B07 C1 evidence tier (F-E2) | HH x 1.0 = 4.0 rests on the Fortune 50 deal, which is a net new logo (Concall_May_2026_Transcript.txt lines 195-198, 755). Cross sell evidence is claim tier: HH x 0.7 = 2.8. |
| 15 | C (phase 1) | B07 F2 evidence tier and single credit (F-E3) | Mixed tier scored at 1.0 and M&A margin turnarounds credited in both F2 and H1. HM x 0.7 = 2.1. |
| 16 | C (phase 1) | B07 evidence gaps (F-E6) | R&D spend declared undisclosed; disclosed Rs 1,212 Mn (Annual_Report_2026.txt p.41). Rescore A4 and F1; crossing 25 would need F1 at HH documented, not supportable by a spend line. |
| 17 | D | B06 report, Q6 verdict table, NEWGEN cell | "NEWGEN concedes agentic workflows will disrupt... low-code companies". Source: Virender Jeet says low code companies are "the ones who are going to win" that segment (NEWGEN Jan 2026 call, lines 603-611). Fragments verbatim; connecting prose reverses who wins. Q6 verdict (PARTIALLY VERIFIED) holds. |

## MINOR

| # | Verifier | Location | Finding |
|---|---|---|---|
| 18 | C (phase 3) | chunk 06 l.92 (F-V2) | Chunk reads "revise the exit PE and recalculate"; source Master 4G l.897 reads "revise the exit PE downward and recalculate". No B11 value changes. |
| 19 | C (phase 3) | chunk 08 l.31; prompts/11-valuation-pipeline.md l.133-140 (F-V3) | A24 tier multiple sentences conflict when an approved base exists without a peer table. Source v3.9 A24 l.110-112 with A20.9 l.58: approved base governs, pillar as sensitivity. B11 already applied this; no value changes. |
| 20 | C (phase 3) | 11-valuation.md l.136-141, l.232 (F-V4) | Pillar 1 current endpoint shown only on TTM 6.84% ("Section 1B supports about 17x"). Reading (b) on the A21 run rate endpoint 13.56%: Pillar 1 14.9%, base 15.0x, C 17.25x, Track 2 about 19.3x (deliberation l.82: 19.2x), Track 1 about 15.2x. Operator approved TTM stands; disclose both. |
| 21 | C (phase 3) | 11-valuation.md l.263-267 (F-V5) | Market implied Reading 1 solved at r 14.5% (FY30 EPS Rs 9.75, EPS CAGR 11.9%), not at the 25% required return. At 25%: end FY29 value Rs 1,106.7, FY30 EPS Rs 12.90, EPS CAGR 22.8%. Flag unchanged. |
| 22 | C (phase 3) | 11-valuation.md l.744 (item 6), l.370 (F-V6) | B7 Year 3 net debt unresolved input lacks both readings and the separating observation. Reading (b), no new M&A, interim base FCF Rs 389.4 Cr accrues: +Rs 47.3 per share, weighted base FV Rs 687.4, 25% entry Rs 351.9, 30% entry Rs 312.9, base CAGR 6.6%. Separating observation: FY27 AR cash and any Reg 30 acquisition. Decision unchanged. |
| 23 | C (phase 3) | B10-valinputs.yaml l.112 (F-V7) | Phase 1 F-G2 cash mechanism correction not carried: cash_evidence repeats "FY26 helped by payable days 66.6 to 37.0". No B11 value depends on it (O3 governs); B14 corrected it. |
| 24 | C (phase 3) | 14-thesis.md l.234; B14 YAML l.30 (F-R1) | Pillar FV CAGR cross-check (33.7%, Rs 173.9 to Rs 415.4) credits Pillar 3 before the A16 crossover. Today (FY27, ROCE 11.7% < r 14.5%) at C 14.835x = Rs 160.3; FV CAGR about 37.4%. Label COMPOUNDER unchanged. |
| 25 | C (phase 3) | B14 YAML l.8 (F-R2) | position_size "Small" on an AVOID verdict whose box says "NONE at CMP". Should read none (ceiling Small); schema enum lacks a none value (.claude/agents/stage-14-thesis.md l.61). |
| 26 | B | B05 timeline_slippages | Kognitiv slippage only. SessionM upgrades 2-3 years, not starting till end of year (Q1 [p9] L359-362); generic cycle 12-18 to 18-24 months (Q4 [p6] L248-250; Q1 [p11] L454-455). Partial capture. |
| 27 | B | B05 2A Q1 margin softness row | "Delivered, better than guided" is wrong. Adj EBITDA margin ~19% Q4 FY26 (Q4 [p6] L250-251) to 17% Q1 FY27 (Q1 [p8] L316); guided softness occurred; YoY base misapplied. |
| 28 | B | B05 2A row, 4D flag OCF/EBITDA | "Missed / never reconciled" OVERSTATED. Q4 FY26 Anant: bill and collect upfront in growing business ([p10] L409-412); Q3 105-110% was a norm, not a promise. |
| 29 | B | B05 2A SessionM row | "Delivered, ahead of schedule" overstated. Break even was the Y1 promise (Q4 [p12] L497-501); evidence is Rs 5-6 Cr cash in 2 months (Q1 [p7] L270-273); cash is not EBITDA in an upfront billing model. |
| 30 | B | B06 flag 1, Q6 | "Capillary less candid on AI risk than peers" OVERSTATED. Q3 FY26 Aneesh names disrupted segments, SMB, seat based pricing ([p9-10] L387-422). |
| 31 | B | B06 Q4, flag 3 | Basis mismatch: INTELLECT single digit is operating margin (Feb 2026 L619-620); Capillary 65-75% is gross, 45% contribution (Q4 [p12] L511). |
| 32 | B | B06 2E NEWGEN Qatar | "Volunteered on-call" OVERSTATED; raised by analyst Sanjay Gupta (NEWGEN Nov 2025 L621-625). |
| 33 | B | B06 Q2 | UNIECOM NRR "100%+" omits "excluding churn of top 10 client" qualifier (UNIECOM May 2026 L517-519; Aug 2026 L557-558); parallels Capillary ex one customer NRR. |
| 34 | B | B05 (absent), item 11 | Margin guide declined on two consecutive calls (Q3 [p15] L652; Q4 [p11] L456-459); steady state range given. |
| 35 | B | B05 (absent), item 12 | Tax narrative shifts each quarter (Q3 [p8] L341-343; Q4 [p10] L418-420; Q1 [p8] L311). |
| 36 | B | B05 (absent), item 13 | ROCE "about 3%" volunteered, reframed as cash ROIC 22% (Q4 FY26 Anant [p10] L414-416). |
| 37 | B | B05 (absent), item 14 | FY25 growth disputed: "13%" called wrong, ~20% on net basis after gross to net accounting change (Q1 FY27 Aneesh [p18] L733-742). |
| 38 | B | B05 (absent), item 15 | Product mix shares exceed 100% (loyalty ~90, Engage 5-7, Rewards 5-7, AI 4-5); Insights monetisation statements conflict (Q4 [p4] L145-156, [p17] L719; Q1 [p3] L154-155). |
| 39 | B | B05 (absent), item 22 | D&A split (acquisition intangibles vs capitalised tech) asked, answered without split (Q3 FY26 Rishi/Anant [p11] L452-462). |
| 40 | B | B05 (absent), item 23 | On call unit and label slips: 142% as INR 142 crores; USD as INR million; PAT vs normalised PAT swapped (Q3 L363; Q4 L468, L514; Q1 L336-337). |
| 41 | B | B05 (absent), item 24 | Analyst challenge: headcount flat but costs growing near revenue; answered by US sales ramp (Q4 FY26 Bharat Gulati/Aneesh [p15] L613-629). |
| 42 | C (phase 1) | B01 M6 (F-G3) | False "no R&D disclosure" gap; R&D incl. ESOP Rs 1,212 Mn disclosed (Annual_Report_2026.txt p.41, Directors' Report technology absorption item iv). M6 score 0 unchanged. |
| 43 | C (phase 1) | B01 analyst_note (F-G4) | About 208 words, over the 200 word cap; truncated sentence survives in input_gaps. |
| 44 | C (phase 1) | B01 D2 (O1, rule passed) | D2 keeps the Rs 24.96 Cr one off in EBIT while M1/M2 strip it; recurring reading 5.79x gives D2 4, core 50; AVERAGE unchanged. |
| 45 | C (phase 1) | B01 ROE/ROCE series (O2, rule passed) | Series mix AR published and computed bases; values reconcile or do not move scores; data_notes wrongly says FY21-FY22 ROCE computed. |
| 46 | C (phase 1) | B01 M5 (O3, rule passed) | Top 5 tier trivially met on a 4 name peer set; moat count unaffected. |
| 47 | C (phase 1) | B01 data confidence band (O4, rule passed) | Ambiguity for operator ruling: a 4 year balance sheet window would trigger the LIMITED downgrade (AVERAGE to AVOID); B01 keyed to 6 P&L years. |
| 48 | C (phase 1) | B07 recount line (F-E4) | "18 items across 6 categories" counts a non category; correct: 12 items across 5 scan categories plus 6 company profile items; 3 of 6 active rows at documented multiplier, 2 after F-E2. |
| 49 | C (phase 1) | B07 optionality register (F-E5) | Register holds 2 risk items (concentration disclosure, fraud forensic close); move to monitoring; add D1, H2, A4 claim only rows. |
| 50 | C (phase 1) | B07 B2 (O6) | Impact graded M while text calls certifications table stakes; HL would give 2.0. |
| 51 | C (phase 1) | B07 2C (O7) | N/A written as 0 in YAML; prose says Rs 394 Cr capex vs table Rs 39.4 Cr (10x unit slip). |
| 52 | C (phase 1) | B07 6D (O8) | Cites an unanchored 75x P/E; pricing belongs to stage 11. |
| 53 | C (phase 1) | B07 catalysts_12m (O9) | Evidence_type "documented_pending" outside the three tier taxonomy. |

## Verifier C phase 3: observations for the operator (not counted as fails)

| ID | Location (as cited by Verifier C) | Observation |
|---|---|---|
| O-1 | v3.9 A24 l.108-113; 11-valuation.md A24 table | Net cash placement in A24 (source silent). Bridge in T1: T1 46.9%, residual 15.0%, starter Rs 415. Bridge outside the tiers: T1 36.9%, T1 + T2 44.9%, residual 25.0%, starter about Rs 339. Re-entry gate moves Rs 76. Rule it. |
| O-2 | Master l.897; v3.9 l.58; prompts/11 l.184-186 | Master 4G "revise downward" vs A20.9 approved base. B11 followed the approved base and reported check 6 FAIL (30x vs a Year 3 metric pillar of about 24x). Re-rule O5 at /finalize or record that 4G yields. |
| O-3 | Master l.1129 vs l.1521 | Verdict conflict AVOID (Role 2 Section 7) vs WATCHLIST (RULES Gate 0 below 60; B11). Stage 13 must reconcile; a standing ruling closes it, as KISSHT. |
| O-4 | Master l.296 vs FTTCP l.438, chunk 01 | Master carries the banned hybrid label "RECOVERING-to-FIRING (probability >60%)". Fix the Master. |
| O-5 | Master l.1168 vs v3.9 l.241 | Master omits Gate 0 from what binds the A25 ladder; v3.9 includes it. B14 followed v3.9. Align the Master. |
| O-6 | Master l.559; chunk 15 l.26 | "Fundamental Base PE" undefined. On C Track 1 is 13.1x; on F it would be 14.8x. Define it. |
| O-7 | deliberation l.17; SKILL.md; CLAUDE.md | O1 is a standing rule for all names but sits in neither SKILL.md's ruled list nor CLAUDE.md OPERATOR RULINGS. It displaces the Route A 20% test (19.0% on unutilised IPO proceeds at 30-Jun-2026). Record it. |
| O-8 | prompts/11 l.235-240 | Wrapper ambiguity: probability weighted EPS CAGR 26.7% has no YAML field; B11 carries the 4D expected return (1.3%). Add a field. |
| O-9 | 11-valuation.md l.340 | Margin bridge lever sizes are an allocation of the approved total in draft C.2 proportions; the bridge does not independently evidence the 22.0% FY30 margin. |
| O-10 | 11-valuation.md l.536, l.566 | Scenario weights put 75% on base or better; the ledger gives the base revenue lift p 0.45 and credits 47.5% of the base increment. Ratify or replace the ledger probabilities at /finalize. |
| O-11 | 14-thesis.md l.193 | Three B14 chain monitors (Chains 1, 2, 3) are not yet on expectation-ledger.md or the tracker. Add them. |
| O-12 | outputs/blocks/B12c.yaml l.4 | Phase 1 block model string "claude-opus-5" differs from frontmatter claude-opus-5-5. The phase 3 block carries the correct string. |

## Verifier B supplementary records

- Promise delivery spot checks: 5 checked, 3 confirmed, 2 wrong (rows 27 and 28 above).
- Credibility grade concurrence: lower (B- to C+). Direction and playbook consistent, but aiRA size, SessionM ARR, platform gross margin and organic growth moved between calls unacknowledged, and ACV/NRR re-based by excluding one customer; 3 quarter record. Operator ruling O9 (10-Oct-2026) holds grade B.
- Pipeline flags not supported: row 10 above.

## Verifier C recomputed values

| Item | Stage value | Recomputed |
|---|---|---|
| Gate 0 moat score / moats / class | 17 / 4 / STRONG | 15 / 3 / MODERATE |
| Gate 0 grand total | 68 | 66 |
| Gate 0 core | 51 | 51 (50 on the O1 alternative reading only) |
| Gate 0 classification | AVERAGE | AVERAGE (AVOID on the O4 alternative reading; operator ruling) |
| EM C1 / F2 | 4.0 / 3.0 | 2.8 / 2.1 |
| EM score | 24.0 | 21.9 before F-E1 and F-E6 rescoring; MODEST unchanged |
| Destination PE (phase 3) | Track 2 16.8x, Track 1 13.1x, governing 30x | concur |
| Decision (phase 3) | no position at Rs 566.65 | concur |
| Step 1C relative route threshold | 24.0x | 18.7x (Track 1 source reading) |
| Track 2 on A21 current ROCE endpoint | not shown | about 19.3x (sensitivity) |
| Net cash reading (b), interim FCF accrues | not shown | base weighted FV Rs 687.4; 25% entry Rs 351.9 |
| Market implied Reading 1 at 25% | EPS CAGR 11.9% (at r) | 22.8% |
| B14 pillar FV CAGR with A16 timing | 33.7% | about 37.4% |

Check 15 (skill to source): 24 rows, 3 divergences: references/15-cost-of-capital-relative-valuation.md l.92 (MAJOR), references/06-summary-sanity-hurdle.md l.92 (MINOR), references/08-run-rate-base-price-decomposition.md l.31 (MINOR). B11 self report: none found; B11 opened no Section 1B source file.

No correction flips the Gate 0 classification, the EM band, the EM 25 qualifier, the destination PE or the decision. Verifier C rework routing: scoped corrections to stages 1 and 7 (phase 1); chunk text fixes on a framework branch (phase 3).
