# VERIFIER C: FRAMEWORK ADHERENCE (PHASE 3 VALUATION SCOPE), ANAWIL, 2026-11-12

Stage B12c, phase 3. Model claude-opus-5-5, effort xhigh (.claude/agents/verifier-c-framework.md lines 5-6). This is the deferred valuation half of the one Verifier C run for this Phase 1 (prompts/12-verifiers-pipeline.md lines 2-3; manifest.yaml line 13 `verifier_runs: {..., C: 1, ...}`). It is not a re-run.

## Scope

- Audited: B10 (block and 10-assembly.md), B11 (block and 11-valuation.md), outputs/expectation-ledger.md, and B14 decision rules and position sizing (block and 14-thesis.md Sections 3G, 5, 7, 8 and the Rule H table).
- Authority: the operator-signed deliberation (outputs/final/fttcp-deliberation.md, SIGNED OFF 2026-11-17). I audit the frameworks as written. Where an approved value departs from the framework text, I report the departure and its size. I do not overturn the ruling. The operator decides.
- Rule sources read: the Verifier C section of prompts/12; Master v3.7 Role 1 and Role 2 Section 7 (frameworks/Master_Project_Prompt_v3_6.md); section-1b SKILL.md and chunks 01 to 17. For check 15: Section_1B_v3.3_Amendments.md, Section_1B_v3_6/v3_7/v3_8/v3_9/v3_10_Amendments.md, FTTCP_v2_1_Consolidated.md and Market_Implied_Assumptions_v1_0.md, at the lines cited.
- Rules in scope: 4, 5, 6, 7, 11, 12, 13, 14, 15, plus the Role 2 extension (B14). Rule 9 is NOT ASSESSED: B13 does not exist yet. Rule 10 fires at /finalize. Rules 2, 3 and 8 were done in phase 1. The gate0 and emoat block sections are copied unchanged from B12c.yaml.
- Verifier A owns whether a number exists in its source. I re-derive arithmetic only to test rule application, on the maker's stated inputs. My own arithmetic is labelled [verifier arithmetic].
- Anchor key: V l.N = 11-valuation.md line N; T l.N = 14-thesis.md; EL l.N = expectation-ledger.md; DLB l.N = fttcp-deliberation.md; B10 l.N = B10-valinputs.yaml; ch NN l.N = .claude/skills/section-1b/references chunk NN; Master l.N = Master_Project_Prompt_v3_6.md; v3.x l.N = the Section 1B layer file; FTTCP l.N = FTTCP_v2_1_Consolidated.md; MIA l.N = Market_Implied_Assumptions_v1_0.md.

## Headline

- Findings: 2 CRITICAL, 4 MAJOR, 10 MINOR. Rules checked 114, passed 97. Acceptance rate 85.1%.
- No REWORK trigger fires. Rules 7, 11, 12, 13 and 14 pass. A Verifier C CRITICAL is not itself a REWORK trigger (prompts/12 lines 11-14).
- Decision of record: I concur with B14. The Master rules as written give AVOID on two triggers, Gate 0 AVERAGE and upside/downside 0.26x (Master l.1129). No reading I tested opens a position at Rs 381.
- Both CRITICALs sit in operator-approved inputs. Neither is a stage 11 error. Stage 11 reported both and kept the approved base, as the deliberation told it to (DLB l.140).
- P1 (CRITICAL). The 4G check fails. The framework says "revise the exit PE downward and recalculate" (Master l.897). The governing Track 1 stays at 16.1x. B11's own Year-3-consistent figure is 14.4x (V l.271). The gap is 1.7x. The entry zone moves from Rs 202-227 to about Rs 181-204 [verifier arithmetic].
- P2 (CRITICAL). Pillar 3a pays +2x on two qualifiers. One is the order book that base revenue already credits at 100%. The other clears its 15% bar only on FY26 revenue. Either ground sets 3a to +0x. Track 2 falls from 20.3x to 18.3x. Track 1 sets the entry zone, so the decision does not move.
- Framework as written lands at Track 1 14.4x and Track 2 16.4x (P1 with P2). The approved card is 16.1x and 20.3x.
- The bar is symmetric. Two readings in this card point up, not down: the Amendment 14 path (N4) and the Route A test on the September 2026 balance sheet (N5). I record both.

## PART 1: GROWTH SYMMETRY (rule 4, first block)

| # | Rule | Result | Stated / recomputed (anchor) |
|---|---|---|---|
| V-01 | 2C-w line present; basis declared; historical CAGR beside it (26.1) | PASS | ORDER-BOOK (FY27), RUN-RATE (FY28), A14 fade (FY29-FY31); historical 77.1% (V l.451) |
| V-02 | No HISTORICAL base where forward evidence exists | PASS | Base runs on the Rs 395.58 Cr book and the H1 FY27 print (V l.339-341) |
| V-03 | Divergence above 10 pp named with observation and date; fed to the ledger | PASS | -39.7 pp; H2 FY27 revenue Rs 228 Cr or more and 34 towers or more by 31-Mar-2027 (V l.367); ledger row B1 (EL l.24) |
| V-04 | Margin bridge lever by lever, evidence on each; no-evidence levers dropped (26.2) | PASS | +145 bps order-book mix (Pres p.21); operating leverage and steel pass-through dropped (V l.391-397) |
| V-05 | Trailing 3-year average not the base; bear per OR-11 | PASS | 40.6% trailing average not used; margin-reset name, bear from the evidence bridge (V l.387, l.403-405) |
| V-06 | No per-input shading (26.3) | PASS | FY27 H2 at the JSW-lag reading with the pull as a p 0.4 slice; FY28 247 towers with readings 196 / 258 and the 34-tower observation (V l.345-348); filed 20.75% tax rate with the 115BAB denial as its own downside row (V l.435). No input is lowered "to be conservative" |
| V-07 | 4D weights keyed to trailing four quarters; period stated (26.4) | PASS | Grade C, 35/45/20; period under four quarters, stated (V l.606) |
| V-08 | 2D standing check answered | PASS | V l.465 |
| V-09 | Catalyst split stated; nothing credited twice (26.1 with Amendment 4) | **FAIL (CRITICAL)** | Split stated (V l.451). Track 2 credits the order book at 100% in revenue and again as a 3a qualifier. See P2 |
| V-10 | Pillar 3 line on the Entrepreneur Ledger (Rule G) | PASS | "does not support the premium because ..." (T l.136) |
| V-11 | A14 fade shown year by year; industry anchor named (18.0) | PASS | V l.372-383; anchor named as an assumption off B10 (V l.341, l.765) |

## PART 2: PILLAR MECHANICS AND ROLE 1 SECTIONS 1 TO 4 (rule 4, second block; rule 5)

| # | Rule | Result | Stated / recomputed (anchor) |
|---|---|---|---|
| V-12 | A17.0 gate before pillar math; tests a/b/c; ambiguity stated | PASS | Model 3 CONVERTER, Models 1-2 NON-CONVERTER; test (c) untestable; steel clause NOT FOUND; OR-6 default (V l.147-148; v3.7 l.11) |
| V-13 | A17.1 through-cycle ROCE for the converter slice; both numbers shown | PASS | Spot 26.87%; through-cycle 21.59% = midpoint of 26.79% and FY24 16.39%; blend 23.45% (V l.149, l.161). FY24 is a ramp year, not a steel-cycle trough. It is the lowest printed year, and the basis is stated |
| V-14 | A17.2 volume test; fork stated | PASS | WC per tower 8.8 / 21.1 / 20.5 / 18.2 lakh; input-price fork closed (V l.150) |
| V-15 | A17.3 bear steel year to the 5-year median spread | **FAIL (MINOR)** | Median spread NOT FOUND; stand-in Rs 25.6 lakh (V l.405). See P11 |
| V-16 | Continuous Pillar 1 formula | PASS | 0.5 x 21.61 + 7.5 = 18.305, 18.3x (V l.158) |
| V-17 | FTTCP ROCE verdict as sole Pillar 1 authority | **FAIL (MAJOR)** | FIRING maps to current ROCE (ch 01 l.23; FTTCP l.437). Used the 21.61% midpoint (DLB l.61-62). See P3 |
| V-18 | Normalisation route declared | PASS | NONE; Route A 19.1% at 31-Mar-2026 (V l.160). See N5 |
| V-19 | ROCE recovery single credit; route stated | PASS | "credited via: Pillar 1"; strategic +0x (V l.155, l.218) |
| V-20 | Pillar 2 matches the stated determination; offset rules; no offset on structural | PASS | INDETERMINATE (DLB Ruling 5); 1.00x approved; OR-5 open; structural 0.65x and growth-induced 0.80 + 0.20 shown with the separating observation and date (V l.193-201). See N3 |
| V-21 | A16 eligibility gate | PASS | B2 YES from FY27; base ROCE path above r 14.5% (V l.207) |
| V-22 | Pillar 3 components match EM, catalyst and evidence; +6x cap | PASS on mechanics | 3a two filed qualifiers, grade C cap +2x; 3b +0x (EM 10.8 below 25); 3c +0x (book 1.55x trailing revenue, 8-month execution) (V l.209-211). The single credit fails at V-09 |
| V-23 | Strategic premium | PASS | +0x; 13 approved makers on EN-156 (V l.218) |
| V-24 | UA in Amendment 3 order; three qualifiers evidenced | PASS | Listed 12m NO; Gate 0 core 66 YES; FII+DII 11.96% NO; UA N (V l.222) |
| V-25 | Sector cap absolute; Category-Break Override | PASS | 25x Cables / Industrial products (operator 2026-11-15), not binding; override N on conditions 1 and 4 (V l.223-224) |
| V-26 | Range H ±7.5%, rounded to the nearest 0.5x | **FAIL (MINOR)** | Approved 18.8-21.8x and 14.9-17.3x; rule gives 19.0-22.0x and 15.0-17.5x. See P7 |
| V-27 | r worksheet line; each adjustment with its basis | **FAIL (MINOR)** | "durability adj 0 (band: Unproven ...)" with no basis for 0 (V l.246). See P8 |
| V-28 | RRM formula and bounds | PASS | 1 + (13.5 - 14.5) x 0.12 = 0.88; 18.3 x 0.88 = 16.1x (V l.248-249) |
| V-29 | Both tracks carried through every FV, entry and the card | PASS | V l.257-260, 4A, 4C, 4E, A19, 4H |
| V-30 | Conservative track sets the entry zone above 15% divergence; fit stated | PASS | 26%; Track 1; three reasons (V l.262) |
| V-31 | Relative PE expression; B8; macro stamp; stale flag | PASS | V l.282, l.253 |
| V-32 | Step 1C PENDING LIVE PEER TABLE; no recalled multiples | PASS | V l.286 |
| V-33 | Hurdle Ratio on the A21 base with the probability-weighted EPS CAGR; forward-consistent current PE | PASS | 1.173^3 x 16.1 / 21.98 = 1.18; Track 2 1.49 (V l.308-314; ch 06 l.37-40; v3.9 l.117) |
| V-34 | Bull row credibility gate | PASS | Grade C: 17.3 + 5 = 22.3%; 1.34 / 1.69; STOP; caps no verdict (V l.309-316) |
| V-35 | Tier line | PASS | Tier A, 25%; Tier B quality gates fail (V l.307, l.703; ch 06 l.54-55) |
| V-36 | A21 base: latest quarter annualised, trailing-4q for a seasonal name | **FAIL (MINOR)** | FY27 forward scenario by operator Ruling 1 (V l.471; DLB l.33-36). See P9 |
| V-37 | Operating earnings only (B4) | PASS | Other income Rs 0.22 Cr stripped (V l.412) |
| V-38 | Consumption clause | PASS | Debt Capacity and Market-Implied blocks NOT FOUND, gaps named, no estimate; Part B consumed (V l.65-73) |
| V-39 | Single-credit map; one improvement, one mechanism | **FAIL (MAJOR)** | Map at V l.75-88. The approved FY28 ROCE input holds half the JSW pull; T3 credits it again. See P4 |
| V-40 | Single credit: EN-182 slice against base volume | **FAIL (MINOR)** | Split not stated. See P10 |
| V-41 | A22: operator-assigned probability on every credited row | **FAIL (MAJOR)** | D1 0.35 and D2 0.30 are proposals (EL l.21-22; V l.482). See P5 |
| V-42 | Unresolved inputs: both readings, separating observation, no silent fill | PASS | Seven rows, each with readings, observation and date (V l.753-759) |
| V-43 | SOM cross-check | PASS | 37.4% / 27.9% against 49.3% / 35.1% (V l.368) |
| V-44 | Rule 7: Section 1A matrix, two or more methods, weights | PASS | P/E 70%, EV/EBITDA 30%, reasons per method (V l.96-137) |
| V-45 | Method application (Master Section 3) | PASS | 3x3 matrices, reverse-engineered entry, EV/EBITDA at the 0.6x end for capex intensity (V l.499-544) |
| V-46 | 4A both tracks; 4B; 4C | PASS | V l.569-602 |
| V-47 | Entry formula (OR-8); 30% price; MoS row; A25 MoS as size | PASS | 443.3 / 1.953125 = 227.0; / 2.197 = 201.8; reference 158.9 (V l.640-645) |
| V-48 | 4F upside/downside | PASS | 16.4% / 63.4% = 0.26x (V l.677) |
| V-49 | 4G validation; a failed check acted on | **FAIL (CRITICAL)** | Row 1 FAIL, row 3 "No" (V l.683, l.685); exit PE not revised (V l.690). See P1 |
| V-50 | A18.0 exit haircut | PASS, note | Not applied, judged a credible Year 4-5 story; sensitivity 15.1x / 19.3x shown; flagged for ruling (V l.275). v3.6 l.71 conditions the haircut on "None with no credible Year 4 to Year 5 story". See N6 |
| V-51 | 4H-pre four elements | PASS | V l.692-697 |
| V-52 | Market-implied flag per the protocol reading | **FAIL (MINOR)** | See P12 |
| V-53 | 4H card fields (Master l.933-950) | PASS | Every field present (V l.699-737) |
| V-54 | DECISION field against the Master decision rules | **FAIL (MAJOR)** | WATCHLIST with a starter band at Rs 339 (V l.734). See P6 |
| V-55 | Recognition gap; transition posture | PASS | CLOSED; PRICED NARRATIVE (TRAP) (V l.292-293) |
| V-56 | Dispersion sizing | PASS | (710.7 - 139.5) / 443.3 = 128.9%, Small (V l.696) |
| V-57 | Edge declaration | PASS | PROCESS, with the named public facts (V l.697) |

## PART 3: DOWNSTREAM SIGNALS, EXIT CONSTRUCTION, FV PATH (rules 6, 11, 12)

| # | Rule | Result | Stated / recomputed (anchor) |
|---|---|---|---|
| V-58 | Rule 6: three or more downstream candidates; catalysts cite one or carry the MODERATE cap | PASS | B10 carries 8 candidates, demand_externally_verifiable true (B10 l.216-225); each slice cites a tracker row (V l.477-480) |
| V-59 | Rule 11: Year 4 committed, bear/base/bull | PASS | FY30 and FY31 rows in all three cases (V l.416-447) |
| V-60 | Exit basis equals entry basis; both stated | PASS | Forward: FY27 at entry, FY30 EPS at the FY29 exit (V l.327-328) |
| V-61 | Resolution Calendar per slice | PASS | Four slices with window, class, event and tracker row (V l.475-480) |
| V-62 | Within-hold slices resolved at exit on their own multiple; bear all FAILURE; no beyond-hold slices | PASS | V l.477-478, l.484, l.548 |
| V-63 | Transition dual display | PASS | V l.550-554 |
| V-64 | Rule 12: FV path, today to end-Year-3, governing track | PASS | V l.653-658 |
| V-65 | FV CAGR line and label, on the card and in Role 2 Section 5 | PASS | 12.3% HYBRID (V l.660-661, l.721; T l.426, l.435) |
| V-66 | Decomposition line; FV-step lines | PASS | V l.662-668 |

## PART 4: EXPECTATION LEDGER AND GATES (rules 13, 14)

| # | Rule | Result | Stated / recomputed (anchor) |
|---|---|---|---|
| L-01 | Appendix A schema | PASS | Columns at EL l.15 match v3.9 l.139 |
| L-02 | At least one downside row | PASS | D1, D2, D3, each negative with its own probability (EL l.21-23) |
| L-03 | Confirm-by on every row | PASS | EL l.17-25 |
| L-04 | Metric and threshold on every row | PASS | EL l.17-25 |
| L-05 | Probability in [0.00, 1.00]; tier matches | PASS | 0.50 T2; 0.40, 0.40, 0.25 T3. Downside rows net against T2, as A24 and the E2E case do (v3.9 l.111, l.168). B1 and B2 are base-case confirm rows with no increment |
| L-06 | Status valid; decay shown where decayed | PASS | All OPEN; none decayed (EL l.17-25) |
| L-07 | 14(a) no credit off-ledger | PASS | Every T2 and T3 item, every FV-today slice and every exit slice maps to rows 1-4, D1 or D2 (V l.623-625, l.655, l.521) |
| L-08 | 14(b) residual starter cap | PASS | Residual 16.0%, at or below 25%; no position (V l.626) |
| V-67 | Confirming threshold sized to the credited increment (A23 "confirming evidence") | **FAIL (MINOR)** | Row 2. See P13. Not a rule-13 REWORK condition |

Ledger gates: 8 of 8 pass. No REWORK for stage 11 under rules 13-14.

## PART 5: SKILL-TO-SOURCE FIDELITY (rule 15)

B11 cites all 17 chunks. For each chunk I compared the rules B11 applied with the source text it names, with later layers governing.

| # | Chunk | Rule B11 applied | Source compared | Result |
|---|---|---|---|---|
| C-01 | 01 | Formula; ROCE selection table | Master l.282, l.291-299; FTTCP l.288, l.433-441 | **FAIL (MINOR)**. Formula matches. Row 2 differs between the Master and FTTCP; the chunk follows FTTCP. See P15 |
| C-02 | 02 | Bands; structural test; offsets; OR-5 | Master l.315-339 | PASS |
| C-03 | 03 | 3a qualifiers and award; 3b; 3c; single credit | v3.3 l.140-150; Master l.375-385, l.617; v3.10 l.79 | PASS |
| C-04 | 04 | Strategic premium; single-credit map; shared-catalyst flag | Master l.301, l.385, l.391-401; FTTCP l.447 | PASS |
| C-05 | 05 | UA order and qualifiers; cap row; override conditions | Master l.406-450, l.452-510 | PASS |
| C-06 | 06 | Summary; range; dual track; Hurdle; tiers; 4G | Master l.522-578, l.884-897; v3.3 l.95; v3.9 l.117 | **FAIL (MINOR)**. The 4G line drops "downward". See P14 |
| C-07 | 07 | 26.1 basis; 26.2 bridge; A14; bear and bull; cyclical override | v3.10 l.24-56, l.85; v3.6 l.64-71; Master l.600-662 | PASS |
| C-08 | 08 | A21; A24; A25 | v3.9 l.62-131 | PASS. Chunk l.31 adds "the operator-approved base where one exists"; consistent with Master l.132 and v3.9 20.9 (v3.9 l.250) |
| C-09 | 09 | A22; A23; Appendix A; downside netting | v3.9 l.74-97, l.137-144, l.165-168 | PASS |
| C-10 | 10 | A18.0 to 18.7 | v3.8 l.11-38; Master l.628; v3.6 l.71 | PASS |
| C-11 | 11 | A17.0 to 17.4 | v3.7 l.11-19 | PASS |
| C-12 | 12 | A16 gate; A19.0 to 19.5 | Master l.371; v3.8 l.44-61 | PASS |
| C-13 | 13 | Gap handling when the block is absent | Master l.114, l.118 | PASS |
| C-14 | 14 | Readings 1 and 2; recognition gap | MIA l.21-32 | PASS |
| C-15 | 15 | RRM; r rules 12A-12C and 13; relative PE; Step 1C display | Master l.545-564; v3.9 l.250 (Amendment 20 summary, including 20.1 and 20.9) | PASS. B11 used only the PENDING display and 20.9 of Amendment 20 |
| C-16 | 16 | Verdict consumption; FIRING mapping | FTTCP l.281-288 | PASS |
| C-17 | 17 | 2C-w line; Rule E; 4D weights; grade gates | v3.10 l.66-68, l.94; Master l.852-858 | PASS |

## PART 6: ROLE 2 DECISION RULES AND POSITION SIZING (B14, extension)

| # | Rule (Master Role 2 Section 7) | Result | Stated / recomputed (anchor) |
|---|---|---|---|
| R2-01 | Verdict box fields (Master l.1104-1121) | PASS | T l.472-503 |
| R2-02 | AVOID rule applied as written | PASS | Gate 0 AVERAGE and upside/downside 0.26x both fire (T l.513; Master l.1129) |
| R2-03 | BUY NOW, BUY ON DIPS, WATCHLIST tests | PASS | T l.509-511 (Master l.1125-1127) |
| R2-04 | INSUFFICIENT CONVICTION not a substitute for AVOID | PASS | T l.512 (Master l.1148) |
| R2-05 | Hurdle band shown; caps no verdict | PASS | T l.514 (Master l.1130) |
| R2-06 | Transition-Alpha Filter default | PASS | WATCH-FOR-INFLECTION (T l.523; Master l.1131) |
| R2-07 | Entry conjunction in the verdict box | PASS | T l.496-499 (Master l.1132) |
| R2-08 | A17.4 converter cycle position | PASS | NOT FOUND, PENDING LIVE VERIFICATION, ceiling stated (T l.451; ch 11 l.38-42) |
| R2-09 | Rule I value-trap test | PASS | "success catalogue pending" with the separating observable (T l.525) |
| R2-10 | Transition matrix posture | PASS | PRICED NARRATIVE (TRAP): "AVOID or hard WATCH"; consistent (T l.516) |
| R2-11 | Size tiers tested | PASS | Conviction Outlier, Large and Medium fail; Small only on a BUY (T l.531-534; Master l.1155-1158) |
| R2-12 | Promoter cap; OR-14 | PASS | CAUTION bars the TRUSTWORTHY-gated tiers; OR-14 not engaged (T l.134, l.537; Master l.1159) |
| R2-13 | Dispersion cap; tightest cap wins | PASS | 128.9%, Small (T l.536; Master l.1161) |
| R2-14 | A25 flag, basis and ladder | PASS | Forward Revenue FIRING (OR-12); +166.6% FY27 (T l.439-449; Master l.1163-1168) |
| R2-15 | A25 starter dependency stated correctly | **FAIL (MINOR)** | "Starter fails either way" (T l.550). D1 is also unruled. Same root as V-41; see P5 |
| R2-16 | Position size consistent with the verdict | **FAIL (MINOR)** | See P16 |
| R2-17 | Section 5 rows; A19 lines; HR band; return-matrix counts | PASS | Track 1 0/9 at 25% or more, 1/9 at 15% or more; Track 2 1/9 and 3/9; recounted from V l.501-515 (T l.415-435) |
| R2-18 | Section 8 specific and measurable | PASS | 14 rows with source, green and red thresholds (T l.564-579; Master l.1180) |
| R2-19 | Entrepreneur Ledger 3G; OR-14 head count; Pillar 3 line | PASS | Rows filled or NOT FOUND; 3 of 4 heads; Pillar 3 line (T l.124-136; ch 03 l.75) |
| R2-20 | Rule F five or more chains with [INFERENCE]; Rule H readiness | PASS | Nine chains, each with a Link 3 [INFERENCE] (T l.155, 189, 225, 255, 279, 299, 321, 346, 372); readiness table (T l.607-612) |
| R2-21 | Thesis-broken trigger specific; exit triggers absolute | PASS | T l.487-490 |
| R2-22 | Position-size override recorded, or none | PASS | None (T l.541) |

## PART 7: RULE 9 (BUSINESS UNDERSTANDING NARRATIVE): NOT ASSESSED

B13 is not produced. The block field holds nulls. A null means "not assessed", not "failed".

## RECOMPUTED VALUES: APPROVED CARD AGAINST THE FRAMEWORK AS WRITTEN

All framework-as-written values use B11's own inputs and B11's period-end ROCE method, which is also the method the approved input uses (DLB l.63-71).

| Item | Approved / stated (B11) | Framework as written | Driver |
|---|---|---|---|
| Pillar 1 input | 21.61%, base 18.3x | FIRING: 23.45%, 19.2x; then 4G revision to the FY29 ROCE 17.72%, 16.4x | P3, P1 |
| Pillar 3 | +2x | +0x | P2 |
| Track 2 destination | 20.3x (18.8-21.8x) | 16.4x (15.0-17.5x) | P1, P2, P7 |
| Track 1 destination (governs) | 16.1x (14.9-17.3x) | 14.4x (13.5-15.5x) | P1, P7 |
| Track 1 Year-3 base FV | Rs 443.3 | About Rs 398 [verifier arithmetic: P/E 26.16 x 14.4 + 23.2 = 399.9; EV/EBITDA 8.64x on 111.05 less 33.41, plus 23.2 = 393.6; 70/30] | P1 |
| Track 1 entry zone | Rs 202-227 | About Rs 181-204 | P1 |
| FV today / FV CAGR | Rs 313.8 / 12.3% HYBRID | About Rs 284 / about 12.0% HYBRID | P1 |
| Hurdle Ratio, Track 1 | 1.18, STOP | 1.614 x 14.4 / 21.98 = 1.06, STOP | P1 |
| A24 at Rs 381, Track 1 | T1 73.2%, T1 + T2 66.8%, residual 16.0% | T1 65.5%, T1 + T2 59.8%, residual 24.9% (just under the 25% cap line) | P1 |
| A25 starter at Rs 381 | FAILS | FAILS on the proposed D1/D2. Passes on the approved card if downside netting is Rs 0.76 Cr PAT or less | P5 |
| Decision | B11: WATCHLIST. B14: AVOID | AVOID (concur with B14) | P6 |

## FINDINGS

| ID | Sev | Rule rows | Location | Stated | Framework as written / recomputed | Effect |
|---|---|---|---|---|---|---|
| P1 | CRITICAL | V-49 | V l.683-690; B11 FLAG-4G-ROCE; DLB l.140 | Governing Track 1 16.1x, Track 2 20.3x. 4G row 1 FAIL and row 3 "No" reported. Approved base kept | Master l.897: "If any check fails, revise the exit PE downward and recalculate." On B11's FY29 base ROCE of 17.72%: base 16.4x, Track 2 18.4x, Track 1 14.4x (V l.271). Year-3 base FV about Rs 398; entry about Rs 181-204; FV today about Rs 284 [verifier arithmetic] | Track 1 -1.7x, Track 2 -1.9x: CRITICAL under rule 5. The decision of record does not change (AVOID, no position). Not a stage 11 error: the deliberation binds the base and predates the 4G result, and B11 reported it in full. Readings: approved 16.1x / Year-3-consistent 14.4x. Separating observation: a Kutch customer approval by 31-Mar-2027, the operator's own falsifier for FIRING (DLB l.46). Without it the falling ROCE path stands. Operator ruling needed before /finalize |
| P2 | CRITICAL | V-09 (with V-22) | V l.209, l.213, l.451; DLB l.61, l.127 | 3a +2x on two qualifiers: order book 2.76x FY26 revenue and capex-embedded growth 22.5%. Approved under "SHARED CATALYST 2" | Ground 1: the order book is the ORDER-BOOK base revenue at 100% (V l.339, l.451). A catalyst credited in revenue "is NOT credited again in Pillar 3 at full weight" (Master l.617; v3.10 l.79; ch 03 l.51). The SHARED CATALYST permission covers a capex commissioning shared by Pillar 1 and Pillar 3 (Master l.385; ch 04 l.51), not revenue and Pillar 3. Ground 2: capex-embedded growth is 30.69 x 1.05 / revenue: 22.5% on FY26 revenue of 143.27, 12.6% on TTM revenue of 255.86 [verifier arithmetic], below the 15% bar (ch 03 l.18). The numerator is the 30-Sep-2026 CWIP. On either ground one qualifier remains, so 3a = +0x. Track 2 18.3x; Track 2 base FV about Rs 504, not Rs 556.6 [verifier arithmetic]; divergence 14% | Track 2 -2.0x: CRITICAL under rule 5. Track 1 carries no Pillar 3 and sets the entry zone (OR-1). The decision and the entry zone do not move. Track 2 FVs, the Track 2 Hurdle Ratio (1.49 to 1.34, still STOP) and the 26% divergence are overstated. Operator re-ruling on 3a needed |
| P3 | MAJOR | V-17 (C-01 bears on it) | V l.155-159, l.270; DLB l.44-47, l.61-62, l.122 | Pillar 1 21.61% (midpoint) under a FIRING verdict | FIRING maps to current ROCE (ch 01 l.23; FTTCP l.437): 23.45%, 19.2x / 21.2x / 16.9x | -0.9x on Track 2, -0.8x on Track 1: within tolerance. An operator override, recorded and flagged by DLB, B10 and B11. The operator's words were "RECOVERING-to-FIRING, probability above 60%" (DLB l.44). That label matches the stale Master row (l.296), which maps to the midpoint. FTTCP bans the label (FTTCP l.288). The deliberation recorded FIRING to score the composite at 4 (DLB l.47). The run uses FIRING for the composite and the RECOVERING midpoint for Pillar 1. Moot if P1 is ruled for the 4G revision |
| P4 | MAJOR | V-39 | DLB l.64-71; V l.163-184, l.479, l.655 | Approved FY28 ROCE 19.76% on 277 towers held flat | 277 is the midpoint of 247 (JSW lag) and 307 (JSW pull) (DLB l.65). It holds 30 of the 60 JSW-pull towers as a lasting FY28 level. B11 credits the JSW pull again as T3 row 3 (+Rs 5.07 Cr weighted) and in FV today (+Rs 31.8 a share). The deliberation kept Kutch out of this base for that reason (DLB l.65: "counts each rupee of Kutch profit once"). JSW is the same kind of p 0.4 slice (DLB l.137). On B11's 247-tower base: FY28 ROCE 17.64%, input 20.54%, 17.8x / 19.8x / 15.7x (V l.180-182) | -0.5x on Track 2, -0.4x on Track 1: within tolerance. B11 printed the gap as a sensitivity but did not name it a double credit. Subsumed if P1 is ruled for the 4G revision |
| P5 | MAJOR | V-41, R2-15 | EL l.21-22, l.47-48; V l.482, l.630-631; T l.550 | T2 net -Rs 3.78 Cr after D1 (p 0.35) and D2 (p 0.30); starter FAILS; "Starter fails either way" | A22: each probability is "assigned by the operator" (v3.9 l.79; ch 09 l.8). The starter needs T1 + T2 of Rs 714.37 Cr, so downside netting of Rs 0.76 Cr PAT or less. D1 alone at p 0.17 or lower, with D2 struck, passes the starter at Rs 381 (T1 + T2 75.0%, residual 7.9%) [verifier arithmetic] | The A25 starter result rests on unruled inputs. B11 and B14 tested only "without D2". The decision of record does not change: AVOID fires on Gate 0 and upside/downside, not on the starter. Operator to rule the D1 and D2 probabilities (B11 FLAG-DOWNSIDE-UNRULED; T 7.3 ruling 4) |
| P6 | MAJOR | V-54 | V l.734; B11 decision; T l.505-521 | B11 DECISION: WATCHLIST, hard watch; band "starter test met at Rs 339 or lower" | Master l.1129: AVOID on Gate 0 AVERAGE OR upside/downside below 2x. Upside/downside is 0.26x at Rs 381 and 0.52x at Rs 339. It reaches 2x at about Rs 241 (T l.519). The Role 1 card DECISION field uses the Master verdict set (Master l.947) | B11's label and its Rs 339 band contradict the AVOID rule. B14 applies AVOID and carries WATCHLIST as operator ruling 7. The action today is the same (no position). B13 must carry AVOID and print WATCHLIST only as the open ruling |
| P7 | MINOR | V-26 | V l.240-249 | 18.8-21.8x; 14.9-17.3x (approved, DLB l.75-76) | v3.3 l.95, Master l.538, ch 06 l.22: round to the nearest 0.5x, so 19.0-22.0x and 15.0-17.5x. Track 1 bear FV about Rs 140.8 (stated 139.5), bull about Rs 717.5 (710.7); width about 130% [verifier arithmetic]. V l.242 calls the A6 ruling open; SKILL.md lists no such open ruling | No decision change. The dispersion cap stays Small. Upside/downside stays 0.26x |
| P8 | MINOR | V-27 | V l.246; V l.755 | Durability adj 0 for the Unproven band; governance adj 0 | The numeric table is NOT FOUND (SKILL.md l.96). Ch 15 l.38: "State the adjustment used and its basis." Under 12C (ch 15 l.36) the Unproven band is the only home of short-record risk | At 0 the short record is priced nowhere. Governance carries a second reading in the unresolved list; durability carries none. The operator-approved r of 14.5% stands |
| P9 | MINOR | V-36 | V l.471; DLB l.33-36 | A21 base = FY27 forward scenario, PAT Rs 43.33 Cr | v3.9 l.67-70: latest-quarter run-rate, trailing-4q for seasonal names; the annual model is the cross-check and floor. On the trailing two halves (Rs 48.09 Cr): T1 81.3%; T1 + T2 74.9% without D3 and 67.0% with D3, the row written for a trailing base (EL l.23) [verifier arithmetic] | The starter fails on every combination. No decision change. Operator-ruled |
| P10 | MINOR | V-40 | V l.345-347, l.477; EL l.17 | EN-182 slice: +Rs 3.6 Cr PAT a year on top of base | Base FY28 of 247 towers needs up to 51 new towers at the trailing pace. That pace was the two filed orders, one of them the first EN-182 order (V l.346). A repeat EN-182 order is part of that inflow | Overlap up to Rs 3.6 Cr PAT: Rs 23.2 a share of the Year-3 base (about 5% of Rs 444.4). State the split, or credit only the per-tower margin difference over Rs 33.72 lakh |
| P11 | MINOR | V-15 | V l.403-405 | Bear FY28 steel year at Rs 25.6 lakh a tower, a stand-in | The A17.3 5-year median spread is NOT FOUND. The stand-in is the median of four printed per-tower figures, one of them "about 22". Per-tower EBITDA also mixes contract models | Bear FY28 row only. The Year-3 bear FV runs on FY30 EPS and does not change. Label the row NOT FOUND, or show both readings |
| P12 | MINOR | V-52 | V l.294-303, l.729 | Flag PRICED-WE-ARE-LATE, set on the 16.1x destination reading | MIA l.30 and ch 14 l.19: reading 2 uses the sector cap or the live peer base. At 25x the price implies 9.7% EPS growth against 17.3% evidence, which reads OPPORTUNITY (V l.301-303) | Both readings sit in 1B.12. The card carries one. The flag never sets the verdict (ch 14 l.56). Carry both flags on the card until the claude.ai block runs |
| P13 | MINOR | V-67 | EL l.18; V l.478 | Row 2 credits 58 towers a year (+Rs 12.65 Cr mid). It confirms on "Gujarat revenue above Rs 8.78 Cr a half" | Rs 8.78 Cr was 16 towers (Pros p.232, cited at EL l.18): about 16 a half, 32 a year, 55% of 58. A threshold sized to the credit is about Rs 16 Cr a half at Rs 0.55 Cr a tower [verifier arithmetic] | A CONFIRMED status would fold the full Rs 12.65 Cr into T1 on about half the volume. The row has a metric, a threshold and a date, so this is not a rule-13 REWORK condition |
| P14 | MINOR | C-06 | ch 06 l.92; Master l.897 | Chunk: "If any check fails, revise the exit PE and recalculate." | Source: "If any check fails, revise the exit PE downward and recalculate." No later layer amends the line | No B11 value changes. Fix the chunk |
| P15 | MINOR | C-01 | Master l.296; FTTCP l.288, l.433, l.438; ch 01 l.24 | Master: "RECOVERING-to-FIRING (probability >60%) \| Midpoint" | Chunk and FTTCP: "RECOVERING, probability >60% with Strong catalysts \| Midpoint". FTTCP bans the hybrid label and calls its table "the only mapping". The chunk follows FTTCP. The Master base text is stale | No B11 value changes (verdict recorded FIRING). Fix Master l.296 on a framework branch. See P3 |
| P16 | MINOR | R2-16 | B14 block l.8; T l.484-485 | position_size "Small" with verdict AVOID | Master l.1158: Small is "Everything else that qualifies as BUY" | The report says zero now, ceiling Small. The block field can be read as a Small position by B13 or the Notion payload. Write "zero (ceiling Small)" |

Counts: CRITICAL 2, MAJOR 4, MINOR 10. Fail rows 17 (P5 carries two rows). Phase-1 counts stay separate: CRITICAL 0, MAJOR 2, MINOR 7.

Severity basis: rule 5. A misapplication that moves a destination PE by more than 1x, or flips the Hurdle band or the decision, is CRITICAL. A misapplication inside that tolerance is MAJOR. A presentational gap, or a gap that changes no B11 value, is MINOR. No finding flips the Hurdle band (STOP on every reading) or the decision of record (AVOID).

## NOTES FOR THE OPERATOR (not scored)

- N1. Template defect, carried from phase 1. prompts/12-verifiers-pipeline.md line 379 still holds `(same line, comment "# rule 9; any fail = REWORK stage 13")` in place of a field. I emitted the intended `business_understanding_narrative` field again.
- N2. B11 `expected_cagr_prob_weighted: 17.3` holds the probability-weighted EPS CAGR. The 4D expected price CAGR at Rs 381 is -3.0% on Track 1 and 4.7% on Track 2 (V l.613). B13 must print -3.0% as the expected return, not 17.3%.
- N3. Pillar 2. CRISIL p.2 says the company "needs to extend high credit period to customers and hold work-in-process and raw material inventory to meet business requirement" (B10 l.213). The 0.65x row reads "Structurally negative, rating agency confirms persistent WC" (Master l.321). The rating-agency assessment "takes precedence over single-year improvements" (Master l.330). The determination is INDETERMINATE by operator Ruling 5, and OR-5 is open. This is the largest single swing in the card: Track 1 16.1x against 10.5x.
- N4. Amendment 14, the upward reading. v3.10 l.85: "26.1 sets the level the fade starts from, not the fade." EM None fades to industry growth from Year 1. A 26.1 level of 247 towers in FY27, then industry growth, gives about 278 / 309 / 371 towers for FY28 to FY30 and FY30 EPS of about Rs 30.56, against the base Rs 26.16 [verifier arithmetic]. B11 reads A14 as a ceiling for a name that is losing share. It shows both readings and names the separating observation (34 towers or more by 31-Mar-2027). Operator Ruling 6 sets A14 as a sensitivity. I treat the base as compliant. A ruling on whether A14 can lift a base above its evidenced path would close the point.
- N5. Route A on the 30-Sep-2026 balance sheet. CWIP is Rs 30.69 Cr against capital employed of Rs 253.87 Cr, 12.1%. The September capital advances are not in my inputs. If they stayed near the March figure of Rs 30.04 Cr, the test would read about 23.9%, above 20%, and Route A (operational ROCE, a higher Pillar 1 input) would open [verifier arithmetic]. The run uses the March basis throughout, and does so consistently.
- N6. A18.0 haircut. B11's judgment stands, but it names no separating observation. One candidate: FY29 tower order intake against the wind roadmap, read at the H1 FY28 print.
- N7. Bear-consistent pillars. The framework applies one destination range to all scenarios. On the A16-shut bear pillars (Track 1 11.1x, V l.276) the Track 1 bear FV would be about Rs 103 and upside/downside about 0.22x [verifier arithmetic]. This is not a rule. Shown for symmetry with N4.
- N8. No REWORK trigger fires from this verifier. remediation_cycles is already 1 (manifest.yaml line 12), so a second cycle would be refused. P1 to P6 need operator rulings, not maker rework. They belong in the /finalize open items with the readings given here. Each states the approved value, the framework-as-written value and the observation that separates them.

## BLOCK

```yaml
stage: B12c
company: "ANAWIL"
run_date: "2026-11-12"
model: "claude-opus-5-5"  # must equal .claude/agents frontmatter; the orchestrator compares it
status: complete
scope: "phase-3 valuation: B10, B11, expectation ledger, B14 decision rules and position sizing; gate0 and emoat copied unchanged from phase-1 B12c; rule 9 not assessed (B13 absent)"
gate0: {rules_checked: 52, fails: ["G0-06 CAGR formula: revenue CAGR stated 177.1%, recomputed 77.1% from 25.78 and 143.2669 (B01 l.74)", "G0-20 C4: stated 0 on -85.2pp, recomputed 5 on +14.8pp; Block C 15 to 20, core 61 to 66", "G0-25 'latest' read as 31-Mar-2026 for Block D and 30-Sep-2026 for E1/E3; Block D 15 on the Sep-26 basis", "G0-40 M11: stated 3, recomputed 1 under the fewer-than-6-years conservative clause; moats 2 to 1, MODERATE to THIN", "G0-51 report-embedded YAML differs from the block file and a line follows it"]}
emoat: {rules_checked: 27, fails: ["EM-02 Meet Outcome 2026-10-05 tagged DOC; it is a management claim; no score change", "EM-10 recount text names 6 claim categories as 5; B1 documented item is the unattributed CWIP rise; count unchanged", "EM-21 R1 scored 0.7 on claim-only evidence but has no optionality register row", "EM-24 6C states core as 61 of 140; core maximum is 100; carries uncorrected Gate 0 values"]}
valuation: {rules_checked: 106, fails: ["V-09 order book credited 100% in base revenue and again as a 3a qualifier; capex-embedded growth 22.5% on FY26 revenue, 12.6% on TTM; 3a +0x on either ground; Track 2 20.3x to 18.3x (CRITICAL, P2)", "V-15 A17.3 bear steel year on a stand-in Rs 25.6 lakh for a NOT FOUND 5-year median spread (MINOR, P11)", "V-17 FIRING maps to current ROCE 23.45% (19.2x/21.2x/16.9x); operator midpoint 21.61% used (18.3x/20.3x/16.1x) (MAJOR, P3)", "V-26 range not rounded to nearest 0.5x: 19.0-22.0x and 15.0-17.5x per A6 (MINOR, P7)", "V-27 durability adj 0 for the Unproven band with no stated basis; short record priced nowhere under 12C (MINOR, P8)", "V-36 A21 base is the FY27 forward scenario, not trailing-4q for a seasonal name; starter fails either way (MINOR, P9)", "V-39 approved FY28 ROCE on 277 towers holds half the JSW pull as a level while T3 and FV today credit JSW; own base gives Track 1 15.7x (MAJOR, P4)", "V-40 EN-182 slice overlaps the base FY28 new-order assumption; split not stated (MINOR, P10)", "V-41 D1 and D2 probabilities are proposals, not operator-assigned (A22); starter passes at Rs 381 if downside netting <= Rs 0.76 Cr PAT (MAJOR, P5)", "V-49 4G fails (FY29 ROCE 17.72%); exit PE not revised downward; governing Track 1 16.1x vs 14.4x; entry about Rs 181-204 (CRITICAL, P1)", "V-52 market-implied flag set on the destination reading; protocol reading 2 at the 25x cap gives OPPORTUNITY (MINOR, P12)", "V-54 B11 decision WATCHLIST with a starter band at Rs 339 contradicts the Master AVOID rule (U/D 0.26x, 0.52x at Rs 339; Gate 0 AVERAGE) (MAJOR, P6)", "V-67 ledger row 2 threshold Rs 8.78 Cr a half confirms about 55% of the credited 58 towers a year (MINOR, P13)", "C-01 Master l.296 hybrid row vs FTTCP l.438 and chunk 01 l.24; chunk follows FTTCP (MINOR, P15)", "C-06 chunk 06 l.92 drops 'downward' from Master l.897 (MINOR, P14)", "R2-15 B14 says the starter fails either way; D1 is also unruled (MINOR, with P5)", "R2-16 B14 position_size 'Small' under verdict AVOID (MINOR, P16)"]}  # 67 Role 1 rows + 17 check-15 rows + 22 Role 2 rows
expectation_ledger: {present: true, downside_row: true, all_rows_confirm_by: true, all_rows_metric_threshold: true, prob_in_range: true, decay_status_valid: true, off_ledger_credit: false, residual_pct_cmp: 16.0, residual_starter_cap_ok: true, fails: []}  # rules 13-14; any fail = REWORK stage 11; 8 of 8 gates pass; B1/B2 are base-case confirm rows with no increment; row-2 threshold sizing is a valuation MINOR (V-67), not a rule-13 condition
business_understanding_narrative: {present: null, five_questions_answered: null, prose_only: null, section6_candidates_named: null, valuation_vocab_leak: null, fails: []}  # rule 9; any fail = REWORK stage 13; NOT ASSESSED, B13 not produced; null = not assessed
recomputed_destination_pe: "approved (governing): Track 1 16.1x (14.9-17.3x), Track 2 20.3x (18.8-21.8x); framework as written: Track 1 14.4x (13.5-15.5x) on the 4G Year-3 revision (P1), Track 2 16.4x (15.0-17.5x) with 3a +0x (P1, P2); Pillar 1 FIRING rule alone 19.2x/21.2x/16.9x (P3); A18.0 haircut not applied (judgment, would be -1.0x)"
recomputed_decision: "concur AVOID (B14; Master l.1129: Gate 0 AVERAGE and U/D 0.26x); no position on every reading; B11 WATCHLIST label and Rs 339 starter band do not follow the AVOID rule (P6); Track 1 entry zone about Rs 181-204 on the 4G reading vs Rs 202-227 approved"
recomputed_gate0: {blocks: {A: 20, B: 3, C: 20, D: 8, E: 15}, core_score: 66, moat_score: 5, grand_total: 71, moats_confirmed: 1, moat_class: "THIN", classification: "AVERAGE"}  # copied unchanged from phase 1
recomputed_emoat: {em_score: 10.8, em_classification: "NONE"}  # copied unchanged from phase 1
findings:
  - {id: P1, severity: CRITICAL, framework: valuation, rule: "V-49 (Master 4G l.897)", location: "11-valuation.md l.683-690; B11 FLAG-4G-ROCE; DLB l.140", stated: "governing Track 1 16.1x, Track 2 20.3x; 4G FAIL reported, approved base kept", recomputed: "revise downward on FY29 ROCE 17.72%: base 16.4x, Track 2 18.4x, Track 1 14.4x; Year-3 base FV about Rs 398; entry about Rs 181-204; FV today about Rs 284", effect: "-1.7x Track 1; decision of record unchanged (AVOID); not a maker error; operator ruling before /finalize; separating observation Kutch approval by 31-Mar-2027"}
  - {id: P2, severity: CRITICAL, framework: valuation, rule: "V-09 (Master l.617; v3.10 l.79; chunk 03 l.18, l.51)", location: "11-valuation.md l.209, l.213, l.451; DLB l.61, l.127", stated: "3a +2x on order book 2.76x and capex-embedded growth 22.5%; SHARED CATALYST 2", recomputed: "order book already in base revenue at 100%; capex-embedded growth 12.6% on TTM revenue; 3a +0x; Track 2 18.3x; Track 2 base FV about Rs 504", effect: "-2.0x Track 2; Track 1 governs, decision and entry zone unchanged; Track 2 FVs and 26% divergence overstated; operator re-ruling on 3a"}
  - {id: P3, severity: MAJOR, framework: valuation, rule: "V-17 (chunk 01 l.23; FTTCP l.437)", location: "11-valuation.md l.155-159, l.270; DLB l.44-47, l.61-62", stated: "Pillar 1 21.61% midpoint under FIRING", recomputed: "current ROCE 23.45%: 19.2x / 21.2x / 16.9x", effect: "within tolerance; operator override, flagged; composite uses FIRING, Pillar 1 uses the RECOVERING midpoint; moot if P1 ruled"}
  - {id: P4, severity: MAJOR, framework: valuation, rule: "V-39 (one improvement, one mechanism)", location: "DLB l.64-71; 11-valuation.md l.163-184, l.479, l.655", stated: "approved FY28 ROCE 19.76% on 277 towers", recomputed: "277 holds 30 of the 60 JSW-pull towers as a level while T3 and FV today credit JSW; own 247-tower base: 20.54%, 17.8x / 19.8x / 15.7x", effect: "-0.4x Track 1; deliberation applied the count-once rule to Kutch, not JSW; subsumed if P1 ruled"}
  - {id: P5, severity: MAJOR, framework: valuation, rule: "V-41, R2-15 (A22 v3.9 l.79)", location: "expectation-ledger.md l.21-22, l.47-48; 11-valuation.md l.630-631; 14-thesis.md l.550", stated: "D1 0.35, D2 0.30 (proposals); starter FAILS; 'fails either way'", recomputed: "starter passes at Rs 381 if downside netting <= Rs 0.76 Cr PAT (D1 p <= 0.17 with D2 struck): T1+T2 75.0%, residual 7.9%", effect: "A25 starter rests on unruled inputs; decision of record unchanged (AVOID on Gate 0 and U/D); operator to rule D1/D2"}
  - {id: P6, severity: MAJOR, framework: valuation, rule: "V-54 (Master l.1129, l.947)", location: "11-valuation.md l.734; B11 decision; 14-thesis.md l.505-521", stated: "WATCHLIST, hard watch; starter band at Rs 339 or lower", recomputed: "AVOID: U/D 0.26x at Rs 381, 0.52x at Rs 339, 2x at about Rs 241; Gate 0 AVERAGE", effect: "B14 applies AVOID; B13 must carry AVOID with WATCHLIST as operator ruling 7; action unchanged"}
  - {id: P7, severity: MINOR, framework: valuation, rule: "V-26 (v3.3 A6 l.95)", location: "11-valuation.md l.240-249", stated: "18.8-21.8x; 14.9-17.3x", recomputed: "19.0-22.0x; 15.0-17.5x; Track 1 bear about Rs 140.8, bull about Rs 717.5, width about 130%", effect: "no decision change"}
  - {id: P8, severity: MINOR, framework: valuation, rule: "V-27 (chunk 15 l.36, l.38)", location: "11-valuation.md l.246, l.755", stated: "durability adj 0, Unproven band, no basis", recomputed: "basis required; 12C leaves short record unpriced at 0; no second reading named", effect: "operator-approved r 14.5% stands"}
  - {id: P9, severity: MINOR, framework: valuation, rule: "V-36 (v3.9 A21 l.67-70)", location: "11-valuation.md l.471; DLB l.33-36", stated: "A21 base FY27 forward scenario PAT 43.33", recomputed: "trailing two halves 48.09: T1 81.3%; T1+T2 74.9% without D3, 67.0% with D3", effect: "starter fails on every combination; operator-ruled"}
  - {id: P10, severity: MINOR, framework: valuation, rule: "V-40 (single credit)", location: "11-valuation.md l.345-347, l.477; expectation-ledger.md l.17", stated: "EN-182 slice +3.6 Cr PAT on top of base", recomputed: "base FY28 already assumes new orders at a pace set by the first EN-182 order; overlap up to Rs 23.2 a share of Year-3 base", effect: "about 5% of base FV; state the split"}
  - {id: P11, severity: MINOR, framework: valuation, rule: "V-15 (A17.3)", location: "11-valuation.md l.403-405", stated: "bear FY28 Rs 25.6 lakh a tower stand-in", recomputed: "5-year median spread NOT FOUND; stand-in uses an 'about 22' point and mixed contract models", effect: "bear FY28 row only; Year-3 bear FV unchanged"}
  - {id: P12, severity: MINOR, framework: valuation, rule: "V-52 (MIA l.30; chunk 14 l.19)", location: "11-valuation.md l.294-303, l.729", stated: "PRICED-WE-ARE-LATE on the 16.1x reading", recomputed: "protocol reading 2 at 25x cap: price implies 9.7% vs 17.3% evidence, OPPORTUNITY", effect: "both readings in 1B.12; card carries one; flag never sets the verdict"}
  - {id: P13, severity: MINOR, framework: valuation, rule: "V-67 (A23 confirming evidence)", location: "expectation-ledger.md l.18; 11-valuation.md l.478", stated: "row 2 credits 58 towers a year; confirms on Rs 8.78 Cr a half", recomputed: "Rs 8.78 Cr = 16 towers, about 55% of the credited volume; sized threshold about Rs 16 Cr a half", effect: "confirmation would fold full Rs 12.65 Cr into T1 on half the volume; not a rule-13 REWORK condition"}
  - {id: P14, severity: MINOR, framework: check15, rule: "C-06", location: "chunk 06 l.92; Master l.897", stated: "revise the exit PE and recalculate", recomputed: "revise the exit PE downward and recalculate", effect: "no B11 value changes; fix the chunk"}
  - {id: P15, severity: MINOR, framework: check15, rule: "C-01", location: "Master l.296; FTTCP l.288, l.433, l.438; chunk 01 l.24", stated: "Master: RECOVERING-to-FIRING (probability >60%) -> midpoint", recomputed: "FTTCP and chunk: RECOVERING, probability >60% with Strong catalysts -> midpoint; hybrid banned", effect: "no B11 value changes; fix Master l.296 on a framework branch"}
  - {id: P16, severity: MINOR, framework: role2, rule: "R2-16 (Master l.1158)", location: "B14-thesis.yaml l.8; 14-thesis.md l.484-485", stated: "position_size Small under verdict AVOID", recomputed: "zero (ceiling Small)", effect: "presentational; avoids a Small position being read downstream"}
critical_count: 2
major_count: 4
minor_count: 10
acceptance_rate: 85.1             # phase 3: 97 of 114 rules passed (valuation 89/106 incl. check-15 15/17 and Role 2 20/22; ledger gates 8/8); combined with phase 1 (70/79): 167/193 = 86.5%
```
