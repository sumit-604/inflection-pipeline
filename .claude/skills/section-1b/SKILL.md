---
name: section-1b
description: Resolved Section 1B exit-multiple authority for the Inflection Alpha pipeline, carrying the combined result of the v3.3 base through v3.10 (Amendment 26, Growth Symmetry), FTTCP v2.3, Debt Capacity v1.0, Market-Implied Assumptions v1.0 and the macro sheet, split into 17 chunks so a stage loads only what it needs. Use whenever the operator says "run Role 1", "value this company", "what is the destination PE", "derive the exit multiple", "run Section 1B", or "run Stage 11", and whenever a valuation stage of the pipeline runs (stage 11, the /fttcp pillar-approval gate, Verifier C's valuation audit, /finalize), even if Section 1B is not named. Also use for any question about a pillar, the sector cap, the Hurdle Ratio, the entry zone, price decomposition, the Expectation Ledger, or FTTCP verdict mechanics.
---

# Section 1B: resolved exit-multiple authority

This skill carries the Section 1B layer set as one resolved rulebook. The layers stack in this precedence order, and a later layer governs the items it names:

v3.10 (Amendment 26) > v3.9 (Amendments 20 to 25) > v3.8 (Amendments 18, 19) > v3.7 (Amendment 17) > v3.6 (Amendments 11 to 16) > v3.5.1 (consolidated Amendment 9) > v3.3 Amendments file (Amendments 1 to 8, 4.1 to 4.4) > Master Prompt v3.7 Section 1B base text.

Every chunk states the resolved rule only. Where a later layer replaced an earlier rule, the chunk carries the later rule and nothing of the earlier text.

The source files stay in `frameworks/` and remain the legal text. If a chunk and a source file ever disagree, the source file wins and the chunk is out of date: report the disagreement and fix the chunk.

## Standing rules (apply in every chunk)

- Section 1B is the sole exit-multiple authority. No exit PE comes from anywhere else. No round-number default is ever asserted without running the pillar calculation.
- There is no numeric exit-PE ceiling other than the sector cap (Amendment 26.5).
- Projections state the most evidenced path. Where evidence is thin, show both readings and the single observation that separates them, then size the position for the doubt (Amendments 26.3, 25). Individual projection inputs are never shaded.
- A missing number is NOT FOUND. It is never estimated.
- One quality improvement, one mechanism. Chunk 04 holds the full single-credit map.
- Role 1 consumes the Debt Capacity block, the FTTCP Part B Output Sheet and the Market-Implied block. It never recomputes them.
- Probability weights and every grade-gated rule take the Role 5 trailing-four-quarter credibility grade (Rule E). Once a quarterly history exists, that grade comes from the `quarterly-review` skill; in the pipeline it arrives as `B10.credibility_grade`. This skill carries no grading logic of its own (chunk 17).
- Live-web steps (the Step 1C peer table, counterparty links) belong to Claude web. Claude Code marks them PENDING LIVE PEER TABLE or PENDING LIVE VERIFICATION and never fills them from memory.
- Section 1A method selection (the Method Suitability Matrix and triangulation) stays in the Master Prompt. It is mandatory before any Section 1B math, and this skill does not replace it.

## Rule labels

Rules B, C and E are labels from the operator's claude.ai instruction copy; they are not defined in `frameworks/`. This skill uses the operator's mapping: Rule B = Amendment 26.1 base-case revenue basis, Rule C = Amendment 26.2 margin bridge, Rule E = Amendment 26.4 relevant-period track record. Rules F to J are defined in Master Prompt v3.7.

## Chunk index

Load only the chunks the current step needs. Paths are relative to this skill folder.

| # | File | Carries | Loaded by (Role 1 section / pipeline stage) |
|---|---|---|---|
| 01 | `references/01-pillar1-roce-base.md` | ROCE base formula, FTTCP ROCE selection table, Routes A and B | Role 1 §1B Pillar 1 (row A). Stage 11; Verifier C (12c); /fttcp pillar-approval gate |
| 02 | `references/02-pillar2-cash-conversion.md` | Cash multiplier bands, structural vs growth-induced test, growth offsets, lender 2L, SOTP BOO rule | Role 1 §1B Pillar 2 (row B). Stage 11; stage 10 (carries the determination into B10); Verifier C |
| 03 | `references/03-pillar3-growth-visibility.md` | 3a/3b/3c premium ladder, +6x cap, Entrepreneur Ledger input | Role 1 §1B Pillar 3 (row D). Stage 11; stage 14 (Role 2 §3G feeds the Pillar 3 line) |
| 04 | `references/04-strategic-premium-single-credit.md` | Strategic asset premium, ROCE re-rating optionality, full single-credit map | Role 1 §1B Strategic Premium (row E). Stage 11; stage 15 (shared-catalyst stress test); Verifier C |
| 05 | `references/05-sector-cap.md` | UA multiplier, sector cap table, quality uplift, Category-Break Override, cap review | Role 1 §1B rows F2, G, G2, G3. Stage 11; /step1 (manifest sector cap row); /fttcp; Verifier C |
| 06 | `references/06-summary-sanity-hurdle.md` | Eight-row summary, range, dual track, Hurdle Ratio and tiers, 2D checks with the standing check, entry price, MoS, dispersion sizing, conclusion elements | Role 1 §1B summary, §2D, §4E to §4H. Stage 11; stage 13 synthesis; /finalize; Verifier C |
| 07 | `references/07-revenue-basis-margin-bridge.md` | Rule B revenue basis hierarchy, Rule C margin bridge, bear and bull rules, fade horizon, cyclical override | Role 1 §2A, §2B. Stage 11; stage 15 (Rule H preconditions); Verifier C |
| 08 | `references/08-run-rate-base-price-decomposition.md` | A21 run-rate earnings base, A24 T1/T2/T3/residual, A25 size-based margin of safety | Role 1 earnings base and §4 verdict. Stage 11; stage 14 (A25 sizing); quarterly review (A21 refresh) |
| 09 | `references/09-catalyst-credit-expectation-ledger.md` | A22 probabilistic credit, FTTCP C.2 table, A23 ledger, decay and retirement | FTTCP Step 2 C.2; Role 1 §4. Stage 11 (writes expectation-ledger.md); /fttcp; stage 09b; Verifier C; quarterly review |
| 10 | `references/10-exit-basis-option-resolution.md` | A18 horizon, exit-basis symmetry, Option Resolution Calendar, exit-state pricing | Role 1 §2 horizon and §4 exit table. Stage 11; stage 15 (18.7 question) |
| 11 | `references/11-converter-amendment-17.md` | CONVERTER gate, through-cycle ROCE, volume WC fork, bear mean reversion, entry conjunction | Role 1 §1B opening gate; Role 2 verdict card. Stage 11; stage 14 (17.4); stage 15; /fttcp (cash feed) |
| 12 | `references/12-amendments-16-19.md` | A16 growth premium eligibility gate, A19 FV path, FV CAGR, return-source label | Role 1 §1B Pillar 3 gate and §4 FV path. Stage 11; stage 14 (A19 lines in Role 2 §5); stage 13 |
| 13 | `references/13-debt-capacity.md` | Mid-cycle debt capacity, coverage trend, verdict block | Consumed by Role 1 (consumption clause) and FTTCP Module B7. Runs in claude.ai before FTTCP; no pipeline stage loads it today |
| 14 | `references/14-market-implied.md` | Reverse-engineered growth, implied story, spread flag | Consumed by Role 1 §1 and §4H-pre value-vs-price. Runs in claude.ai after FTTCP; no pipeline stage loads it today |
| 15 | `references/15-cost-of-capital-relative-valuation.md` | Macro sheet inputs, RRM Track 1 and r table, terminal growth cap, DCF, relative PE, Step 1C | Role 1 §1B RRM track, relative PE, Step 1C; §3 DCF and P/B. Stage 11 (marks Step 1C pending); claude.ai (live peers) |
| 16 | `references/16-fttcp-verdict-logic.md` | FTTCP backward and forward verdicts, scoring, Kernex cap, Step 2E, lender set, Part B handoff | FTTCP Part A and Part B; Role 1 inputs. /fttcp; claude.ai FTTCP run; stage 11 reads the verdicts |
| 17 | `references/17-worksheet-track-record-weighting.md` | 2C-w worksheet line, Rule E weighting, 4D weights, grade-gated rules | Role 1 §2C-w and §4D. Stage 11; stage 10 (credibility_grade); stage 05 (produces the grade); stage 15 (Rule H); Verifier C |

## Run order for a full Role 1

1. Chunk 16: confirm FTTCP ran (Part A verdicts, C.2 table with a downside row, Part B Output Sheet). Chunks 13 and 14: read the consumed blocks.
2. Chunk 11: state CONVERTER or NON-CONVERTER before any pillar math.
3. Chunks 01, 02, 03 (with the A16 gate in 12), 04, 05: build rows A to H.
4. Chunk 06: summary table and destination range. Chunk 15: RRM Track 1, relative PE, Step 1C.
5. Chunks 07 and 17: Section 2 projections and the 2C-w worksheet line. Chunk 10: horizon, exit basis, option slices.
6. Chunk 08: A21 base, price decomposition, A25 sizing. Chunk 09: Expectation Ledger.
7. Chunk 06: Hurdle Ratio, 2D checks, entry price, margin of safety, dispersion cap, conclusion. Chunk 12: FV path and return-source label.

## Ruled (operator, 2026-09-15)

- OR-2. Hurdle Ratio. Amendment 24 governs: the Hurdle Ratio is a feasibility check, not a verdict cap. Its PASS / CONDITIONAL / STOP band is computed and shown on the verdict card; it caps no verdict. Chunk 06.
- OR-6. Amendment 17.0 default for ambiguous classification. Kept as written: "Ambiguous cases classify CONVERTER (conservative default)", with the ambiguity stated. Chunk 11.
- OR-8. Entry divisor. Confirmed: entry = exit-consistent fair value ÷ (1 + tier hurdle)^N, with 1.25 for Tier A and 1.20 for Tier B. Chunk 06.

## Open rulings (carried as written until the operator rules)

- OR-1. Dual-track entry zone. Master §1B RRM and §4A carry "the more conservative track sets the entry zone". Amendment 26.3 limits itself to Role 1 projections, so it does not reach this rule. Chunk 06.
- OR-3. Pillar 3 evidence gates against Amendment 22. 3a and 3c pay on 📄 evidence only, and the 3b table keys on evidence mix. Amendment 22 says evidence symbols feed the probability and no longer unlock a premium tier by themselves. No rule converts probability into 3a/3b/3c turns. Chunks 03, 04.
- OR-4. Raising the sector cap. The Master calls the Category-Break Override the only mechanism that raises a cap, and also carries a routine ×1.25 quality uplift on UA-qualified names; the v3.5 reconciliation note treats both as live. Section 1B v3.9 Appendix C R1 (a blended infra-plus-platform cap row) is also pending. Chunk 05.
- OR-5. Pillar 2 with an INDETERMINATE or Mixed structural/growth determination. No Section 1B layer sets a multiplier for it. CLAUDE.md caps the run verdict at PROCEED WITH CAVEATS with the missing evidence named. Chunk 02.
- OR-7. Macro sheet regime note. The August 2026 sheet tells destination PEs where to sit inside their bands and suggests a regime stress on BUY verdicts. Section 1B places H inside its range through Amendment 15 and FTTCP B8 only. The note is not carried into this skill. Chunk 15.

## NOT FOUND in frameworks/

- Amendment 10 (intrinsic cross-check) trigger and mechanics. v3.5.1 cites it; its text is not in the repo.
- The numeric r adjustments for the durability and governance bands. The r table is cited; only the cyclical surcharge range (+0.75 to +1.5) and the A12/A13 items are given.
- A cash multiplier for a Mixed or INDETERMINATE structural determination (OR-5).

## Source files

`frameworks/Master_Project_Prompt_v3_6.md` (content v3.7), `Section_1B_v3.3_Amendments.md`, `Section_1B_v3_5_1_Reconciliation.md`, `Section_1B_v3_6_Amendments.md`, `Section_1B_v3_7_Amendments.md`, `Section_1B_v3_8_Amendments.md`, `Section_1B_v3_9_Amendments.md`, `Section_1B_v3_10_Amendments.md`, `FTTCP_v2_1_Consolidated.md` (content v2.3), `Debt_Capacity_Assessment_v1_0.md`, `Market_Implied_Assumptions_v1_0.md`, and `macro-sheet.md` at the repo root (refreshed monthly; always read the live file).
