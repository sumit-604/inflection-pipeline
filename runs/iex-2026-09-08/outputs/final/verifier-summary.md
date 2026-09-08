# VERIFIER SUMMARY

IEX | Indian Energy Exchange Ltd | Run date 2026-09-08 | Phase 1 scope

Scope: verifier A (numerical audit), verifier B (independent concall red flag
audit), verifier D (peer coverage audit), and the Gate 0 plus Emerging Moat
portion of verifier C (framework adherence). Verifier C's valuation adherence
audit is deferred to phase 3, because stages 10 and 11 have not run and the
valuation framework documents were deliberately withheld from this phase as
dead context.

## PROCESS NOTE ON VERIFIER B

Verifier B's 65 percent is a POST-REMEDIATION measurement. It is not a first
pass score and must not be read as one.

The sequence: verifier B measured stage 5 run 1 at 38 percent. Stage 5 was rerun
in full. Verifier B measured stage 5 run 2 at 36 percent strict, 68 percent with
partial catches. Stage 5 was then amended in a targeted way against those
findings. Verifier B measured stage 5 run 3 at 65 percent strict, 88 percent with
partials.

The three figures are not comparable to each other and must not be reported as a
trend. Each run measured a different artifact, and each later artifact had
already absorbed the previous round's findings, so run 3 measures what an
independent reader still out lists against a much harder residual set. The
verifier states this itself in its measurement note.

The REWORK gate fired twice during this run, at 38 and at 36, and was answered by
rework rather than by declaring a verdict. The run's honest confidence is the 65
percent overall, not the 98.9 percent numerical headline.

## CONFIDENCE DELTA AND ACCEPTANCE RATES

| Verifier | Model | Acceptance rate | CRITICAL | MAJOR | MINOR |
|---|---|---|---|---|---|
| A, numerical audit vs sources | claude-haiku-4-5 | 98.9 (92 numbers checked) | 0 | 0 | 1 |
| B, concall red flag audit (run 3, post remediation) | claude-opus-4-8 | 65 strict / 88 with partials | 0 | 6 | 7 |
| C, framework adherence (phase 1 scope) | claude-opus-4-8 | 84 (82 rules checked) | 0 | 2 | 11 |
| D, peer coverage audit (run 2) | claude-sonnet-5 | 90, peer utilisation 100 | 0 | 1 | 1 |

Confidence delta: numerical 98.9, red flag 65, framework 84, peer 100. Overall
65, the minimum of the four. Band 60 to 74, which downgrades a PROCEED verdict
one level. REWORK gate not triggered at close: zero verifier A CRITICAL findings
and no acceptance rate below 60.

## FINDINGS, SORTED BY SEVERITY

### CRITICAL

None. Across all four verifiers.

### MAJOR

| # | Verifier | Location anchor | Finding |
|---|---|---|---|
| 1 | B | B05, missed entirely | Nov-2025 p.8 "we are not aware about any developments" against Jul-2026 p.20 "for the four months period they have run this pilot", plus IEX's own unpublished simulation asserted as established fact in support of a live Supreme Court petition. The contradiction half is uncertain because the pilot may post date Nov-2025; the simulation as fact half stands regardless. |
| 2 | B | B05 report 1D and 2D; B05 red_flags | Partially caught. B05 holds the day ahead decline and the August buy bid figure, but never states that July 2026 was the first month IEX volume grew slower than national consumption (7.7 against 10.9 percent, Power Market Update Jul'26 p.2), nor that August cleared volume was sell side capped. Together these falsify the load bearing "majority of incremental growth came to exchanges" claim (Jul-2026 p.13). Hand to stage 11 explicitly. |
| 3 | B | B05 red_flags, filed LOW | Under weighted. All three 2023 launches (HP-DAM, HP-TAM, Ancillary Market) are management admitted failures for want of liquidity (Jul-2026 p.12). That is the observed base rate for IEX product launches, and the growth case rests on three further pending launches. Should be MAJOR: it is the cleanest available discount on the optionality stack. |
| 4 | B | B05 guidance row and timeline_slippages | Connection not drawn. The "another 15 to 20 billion units" sizing for the 11 month term ahead contract (Feb-2026 p.12) is contradicted by Goel's own July admission that contracts beyond three months are "not significant" (Jul-2026 p.40), alongside "more than two years since we have applied". Both facts sit in separate rows; neither references the other. |
| 5 | B | B05 YAML red_flags[] | Two findings B05 itself declares MAJOR never reach the handoff flag list, so they would not reach stage 11 or 13 unaided: the April 2026 CERC REC amendment framed as inventory enhancing one quarter before sell bids fell 86.1 percent, and the unqualified "no additional costs" answer on coupling operator integration. A finding recorded in prose but omitted from red_flags[] is functionally missed downstream. |
| 6 | B | B05 report, about one third of 35 sampled anchors; B06, MCX Aug-2026 | Citation anchor drift of one to three marker pages, plus two cross call quote misattributions ("we had no expertise when we started" cited Q4FY26 p.12-13, actually Q1FY27 p.39; "5,000+ industrial consumers" cited Q1FY27 p.17-18, actually Q4FY26 p.17). B05 asserts every citation was grep verified; that claim is not sustained. Every quote traced exists in the file named and in the substance claimed, so this is a precision and process claim defect, not an evidence defect. |
| 7 | C | B07 Section 5 scoring table / B07 em_score | Unauthorised evidence multiplier 0.85 applied to B3, D2 and H1. The framework grants only 1.0x, 0.7x and 0.5x and defines no blend. Recomputed 26.9 (all 0.7x) to 29.9 (all 1.0x) against 28 reported; STRENGTHENING band and the EM at or above 25 qualifier hold across the whole range. |
| 8 | C | B01 report, Block E metric E2 | Promoter holding change scored 3 on a one year window after the report itself states the required three year comparison is NOT FOUND. Operating rule 5 requires 0. Recomputed E2 = 0, Block E = 10, core = 82, still at or above 80, classification EXCELLENT unchanged. |
| 9 | D | B06-peers.yaml and 06-peers.md, entire document (absent); B05-concall.yaml lines 195-201 | B05 carries seven peer questions, not six. B06's rework note, header and triangulation summary all claim it answered "all six". Question 7, whether peers show degrading disclosure precision under competitive or regulatory threat, receives no verdict anywhere. A skipped claim. B06 already gathered overlapping evidence for it and never synthesised it. |

### MINOR

| # | Verifier | Location anchor | Finding |
|---|---|---|---|
| 10 | A | 04-bizmodel.md, p.88 | Technology expense Rs 13.65 crore is labelled as a technology expense in report context but is sourced from the consolidated other income line in the AR, not a separate technology spend disclosure. Arithmetic correct, semantics potentially misleading. Source fidelity flagged; does not affect any verdict card or decision figure. |
| 11 | B | B05 promise_delivery | Missing row that favours management: April 2026 p.10 guided IGX Q1FY27 to "not get any growth"; actual was plus 11.9 percent volume and plus 15.5 percent profit (Q1FY27 press release p.2). Omitted from a four, two, four tally. |
| 12 | B | B05 red_flags and promise_delivery | Internal tension. The treasury income recovery is booked as a delivered promise while the rising non operating share of pre tax profit that recovery mechanically produces is booked as a red flag. Same event, two rows, neither notes the other. |
| 13 | B | B05 report 1D | Mild overstatement. The claim of four consecutive months of collapsing sell bids and rising clearing prices does not hold for August 2026, which reports no sell bid figure and shows clearing prices down from June. Q1FY27 and July do support the claim. |
| 14 | B | B05 red_flags, filed MEDIUM | Severity understated. The same call contradiction, a 20, 30, 40 percent day ahead impact volunteered at Jul-2026 p.5 against "I don't see any loss in market share" at p.35, is the only sizing of the thesis's largest risk anywhere in the corpus, given and withdrawn inside one session. Should be HIGH. |
| 15 | B | B05, missed | Outright refusal on the coupling mitigation question (Nov-2025 p.15): "I do not think on this call, it will be possible to elaborate on those things." Distinct from the price war evasion already tracked, and answered properly only nine months later. |
| 16 | B | B05, missed | FY26 results call held without the Joint Managing Director or the Head of Market Operations (Apr-2026 p.3), on the quarter carrying the APTEL dismissal and the CERC draft coupling regulations. Soft signal only; both returned in July. |
| 17 | B | B05 red_flags, filed MEDIUM | Half caught. The Rs 747 crore against Rs 745 crore and Rs 202.8 crore against Rs 201 crore discrepancy is captured; the additive presentation "IEX standalone around 474 crores, IGX 42 crores and ICX" against Rs 493 crore consolidated profit, with IGX a 47.3 percent equity accounted associate, is not (Jul-2026 p.27). |
| 18 | C | B07 category C2 | Evidence tier mismatch. The scored proposition, customer base diversifying, is conceded in the report's own text to rest on management claim and implication, while the row is scored at documented 1.0x. At 0.7x, C2 = 1.4 and worst case em_score 26.3, band still STRENGTHENING. |
| 19 | C | B01 report, Block A metric A4 | Scored 5 where the band condition "latest at or above earliest" is false; the 0.16 percentage point decline falls in an undefined gap below the smallest band. The stage disclosed it and invited rescoring. Recomputed A4 = 3, Block A = 18, core = 83, classification unchanged. |
| 20 | C | B07 completionist_recount and evidence_mix.documented | Recount states 21 documented items across 8 categories; the itemisation sums to 20 unique across 9 named categories and double counts the R1 and A4 VPPA notification the clause says is counted once. The defect sits inside a framework mandated control; no score depends on it. |
| 21 | C | B07 Section 3 completionist guard paragraph | States "10 score None/0" then lists 11 categories. As written the paragraph sums to 22 of 23; the correct split is 9 active, 3 weak, 11 zero. |
| 22 | C | B07 Section 5 scoring table | The prompt requires a full 23 row scoring table; the table carries 14 scored rows plus one collapsed "all other categories" row. All 23 are addressed in the Section 3 summary, so the substantive requirement is met and the total is unaffected. |
| 23 | C | B07 Section 3 categories A2 and F1, and Section 2 | Source anchors given as extracted text line numbers (AR line 11332, AR line 4363, AR lines 4678-4711) rather than the page form the prompt specifies. All three sit in no evidence categories; a reader cannot resolve a line number to a page. |
| 24 | C | B07 Section 5 category C2 row | Likelihood and impact label written "H x L/M" but bracketed "(MM)". The two disagree; the assigned raw score of 2 is correct under either reading, so no score moves. |
| 25 | C | B01 report, formula notes section | ROCE computed without the prompt's required "computed" statement. The verifier checked the compute branch and found it correct: the screener source rows are label only and carry no values, so the source figure is genuinely absent. |
| 26 | C | B01 report, M5 | Four market capitalisation figures quoted with no per figure source anchor, against operating rule 4, which requires an anchor on every extracted number. |
| 27 | C | runs/iex-2026-09-08/outputs/reports/01-gate0.md | The report does not end with the fenced YAML block the prompt's output section requires; the block exists only as blocks/B01-gate0.yaml. 07-emoat.md does carry its block, so the run is internally inconsistent on this point. |
| 28 | C | runs/iex-2026-09-08/outputs/blocks/B01-gate0.yaml | Schema extras beyond the prompt's block: run_number, run_note, and input_gaps as a list of typed objects where the schema shows a bare list. Additive and useful for a rescore, but not the block as specified. |
| 29 | D | B06-peers.yaml peer_coverage_map, MCX Q4 FY26 (May 2026); 06-peers.md Part 3 table, same row | MCX's interoperability mechanics passage, the "100 percent similar product" argument for why liquidity would not migrate, is name checked as a substantive contribution but never analysed in Parts 1, 1B or 2. Real, quotable and on topic for the coupling theme, but functionally cited only. Not a rebuttal to any stated IEX claim, so treated as an industry context miss. |

## SOURCE FIDELITY

Verifier A recorded one finding with source_fidelity true, item 10 above. It is a
presentational label on a technology expense figure in the business model report.
It does not appear on any verdict card, in any Section 1B pillar input or in any
decision figure, and stages 10 and 11 have not run. No downstream step in this
phase carried it. The source fidelity gate is not engaged and no REWORK follows
from it.

Verifier A's controlling result: 91 of 92 checked figures verified clean against
the sources. No number in this evidence pack was fabricated or materially
misread.

## VERIFIER SELF ASSESSMENTS

Verifier B, on materiality: the residual gap would not change an investment
decision. Three of its 26 items are absent from the pipeline and two of those
three are texture rather than thesis; the third sits inside a coupling risk the
pipeline already flags at its highest severity across seven separate rows. Zero
pipeline flags are unsupported. All five promise delivery directions tested held.
It concurs with credibility grade D.

Verifier C, on Gate 0: re derived the grand total at 115 of 160 and the emerging
moat score at 28.4 against 28 reported. Both MAJORs were recomputed and neither
changes a classification. Nine deal breakers retested, zero triggered. Two
observations carried for operator sensitivity: Gate 0 data confidence reads 8
years off the profit and loss window while ROCE, free cash flow and working
capital days rest on a 3 year sub window; and the emerging moat scan scopes its
two highest scoring rows to exclude the live coupling threat, together 7.4 of
28.4, disclosed in the prose but gross rather than net in the score itself.

Verifier D: all 12 peer transcripts used substantively after the re pointing,
zero unsupported substantive claims, zero verdict discipline failures.
