# Verifier summary, AEQUS, run 2026-09-05 (phase 1)

## Confidence delta

| Component | Verifier | Source block | Acceptance | CRITICAL | MAJOR | MINOR |
|---|---|---|---|---|---|---|
| Numerical acceptance | A (numerical, haiku) | B12a | 97.5 | 0 | 1 | 0 |
| Red flag coverage | B (red flags, opus) | B12b | 30 | 1 | 17 | 6 |
| Framework adherence | C (framework, opus) | B12c | 86 | 0 | 5 | 15 |
| Peer utilisation | D (peers, sonnet) | B12d | 100 | 0 | 2 | 6 |
| **Overall** | min of four | confidence.yaml | **30** | 1 | 25 | 27 |

Band: under 60, forced REWORK.

Coverage notes as the verifiers wrote them:
- A checked 40 material figures; 39 clean. Verdict card inputs 4 of 4 verified,
  scorecard pillar inputs 12 of 12, financial statement totals 15 of 15,
  customer and segment detail 8 of 8, cash flow and working capital metrics 6 of
  6, contingent liabilities and audit quality 5 of 5. No unanchored or estimated
  figures found.
- B found 30 independent flags; 9 caught upstream, 10 partially caught, 11
  missed outright. Promise delivery spot checks: 6 checked, 4 confirmed, 2 wrong.
  B would grade credibility C, not B.
- C ran phase 1 scope only: Gate 0 (57 of 63 rules passed, 90 percent) and
  Emerging Moat (55 of 67, 82 percent). **C's valuation half is pending phase 3**
  and is not scored here. C also recorded that stage 13 synthesis was not in
  phase 1 scope at the time of its pass, so the business understanding narrative
  was not evaluated and is deferred to the stage 13 verifier pass.
- D audited 9 peer transcripts; 9 of 9 substantive, 0 unsupported. Internal
  citation acceptance 78 percent. All 9 stage 5 peer questions addressed. No
  verdict discipline fails.

## Findings, sorted by severity

### CRITICAL (1)

| Verifier | Location anchor | Finding |
|---|---|---|
| B | B05 red_flags / credibility_basis / 2D; B06 Part 2 cross-read. Anchors Jun-2026 PDF p.6 vs Aug-2026 PDF p.5 | MISSED: other income is inside reported EBITDA and inside segment EBITDA. Q4 FY26 operational EBITDA Rs 42 mn against a headline Rs 321 mn; the Rs 279 mn gap was disclosed only in the next call. Materially changes the FY26 earnings base that the FY27 doubling guide and the FY26 aerospace ROCE of 20 percent are read against. Graded CRITICAL under the header severity scale. |

### MAJOR (25)

| Verifier | Location anchor | Finding |
|---|---|---|
| A | 05-concall.md, Section 1B table, row "Aerospace segment EBITDA margin". Q4 FY26 transcript p.3; Q1 FY27 transcript p.3 | SOURCE FIDELITY (non-overridable). Report cites "at 20%" (Q4 FY26) and "above 20%" (Q1 FY27) as one guidance line. The transcripts carry two different framings. No numerical error: FY26 actual of 26.9 percent exceeds both bars. The report does not flag the phrasing shift or say whether it is a tightening or a clarification. |
| B | B05 (absent throughout). Aug-2026 PDF p.6 | MISSED: Rs 90 mn exceptional gain inside the Q4 FY26 PAT loss of Rs 541 mn, undisclosed on the Q4 call. With the CRITICAL above, two favourable items totalling Rs 369 mn were omitted from one results presentation. |
| B | B05 §1B guidance row 6 and YAML guidance list. Aug-2026 PDF p.15 vs Jun-2026 PDF p.6 | MISCLASSIFIED: the Rs 180 cr doubling operational EBITDA figure recorded as confirmed rather than flagged as irreconcilable with Rs 154.5 cr FY26 reported EBITDA. The two statements reconcile only if about Rs 600-650 mn of FY26 EBITDA was other income, a figure NOT FOUND in any transcript. |
| B | B05 (absent throughout). Jun-2026 PDF p.4, p.10, p.15-16; Aug-2026 PDF p.3 | MISSED: new parts added fell 433 to 86 QoQ against management's own "100-plus, 150 parts per month" moat claim from the intervening call. |
| B | B05 (absent). Feb-2026 PDF p.8 vs Jun-2026 PDF p.6 | MISSED: total assets fell Rs 3,595 mn between Dec-2025 and Mar-2026, unexplained, in a quarter of heavy consumer capitalisation and record revenue. |
| B | B05 red_flags (only two restatements logged). Feb-2026 PDF p.8 vs Jun-2026 PDF p.6 | MISSED: FY25 fixed asset turnover restated 1.3x to 1.84x between calls. Raises the restatement count from two to four and changes the character of the finding from imprecision to a systematic disclosure quality problem. |
| B | B05 §1B guidance rows. Jun-2026 PDF p.3, p.19; Aug-2026 PDF p.12 | MISSED: MoU headline commitments of Rs 4,756 cr do not reconcile to the funded USD 350-400 mn five year plan. Reconciliation and funding split both declined by management. |
| B | B05 §3C. Jun-2026 PDF p.18 | MISSED: management's answer to the ecosystem margin question, "if we increase our margin, our win rate might come down", an admission of price set by competition. Bears on the quality ladder rung and on the durability of the 20 percent margin guide. |
| B | B05 §1B/§4A (absent). Jun-2026 PDF p.17-18 | MISSED: consumer revenue target of about Rs 2,000 cr by FY29, about 10x FY26 consumer revenue, stated once and unsupported. |
| B | B05 §1C utilisation row, §4A trigger 3. Feb-2026 PDF p.10; Jun-2026 PDF p.4; Aug-2026 PDF p.7-9 | UNDER-WEIGHTED: consumer utilisation fell three consecutive quarters (31, 23, 22) while the 40 to 50 percent FY27 exit target held unchanged, and management substituted a revenue metric when pressed twice. The 31 to 23 drop is never reconciled. This is the sole gate on FY27 consolidated guidance. |
| B | B05 §2E Repeated Question Tracker. Jun-2026 PDF p.15; Aug-2026 PDF p.7 | UNDER-WEIGHTED: yield and rejection rates refused across two consecutive calls while yield is offered as the explanation for revenue rising on falling utilisation. Not registered as a repeated evasion. If B05's coverage reads as insufficient this becomes a MISSED repeated evasion and therefore CRITICAL under rule 5. |
| B | B05 §2D (FY26 cash flow silence). Aug-2026 PDF p.6 | UNDER-WEIGHTED and partly OVERSTATED: B05 says the cash flow statement never came up. Management volunteered a negative Rs 414 mn operating cash flow and framed it in the same paragraph as "better conversion of the higher operating scale into cash". The self contradiction is a stronger finding than the absence B05 reported. |
| B | B05 §3B/§3C (China exchange logged as MANAGEMENT VIEW). Jun-2026 PDF p.12-13 | UNDER-WEIGHTED: the DRHP flagged China critical equipment dependency question was put in two parts and neither was answered. Not classified as a dodge anywhere. Gates the consumer electronics ramp. |
| B | B05 §1B guidance rows (consumer ROCE/margin). Feb-2026 PDF p.22; Jun-2026 PDF p.10, p.15; Aug-2026 PDF p.6, p.9 | UNDER-WEIGHTED: the 18 to 20 percent consumer steady state EBITDA and ROCE targets carry a management stated precondition of 75 to 80 percent utilisation, far outside the 40 to 50 percent FY27 target, from a current minus 49 percent segment margin with utilisation falling. Recorded as guidance without the precondition gap. |
| B | B05 §2A promise delivery row 3 and §4C. Jun-2026 PDF p.9 | OVERSTATED: "Aerospace FY27 +25-30% at >20% segment margin, delivered, above both bands." The 23 percent Q1 margin is on an other income inclusive, unallocated cost exclusive basis; the 20 percent guide was defined on the exclusive basis. Revenue leg is clean; margin leg is not established. Load bearing for credibility grade B and trigger 1. |
| B | B06 Q9 net read and partially_verified row 2. AZAD Aug-2026 PDF p.17, AZAD Nov-2025 PDF p.6-7 vs AEQUS Aug-2026 PDF p.18 | OVERSTATED, direction inverted: AZAD Sunflag and Star Wire evidence is used to corroborate the Aequs claim that India qualified raw material is not possible anytime soon. AZAD states it has already qualified two Indian mills for critical grades with GE and Siemens approval, cutting raw material cost from about 12 to about 5 percent of sales. Verdict should be COMPLICATED, not corroborating. |
| B | B05 §4D red_flags (99 percent import listed LOW). Aug-2026 PDF p.3-4 vs p.17-18 | UNDER-WEIGHTED: the "100% Make in India" framing of the Safran wheels win sits in the same call as "our raw material is like 99% is imported", about 15 pages apart. The narrow product claim is defensible; the headline framing is not. |
| B | B06 Part 2 cross-read (demand, pricing_inputs, capex_cycle only). AZAD Aug-2026 PDF p.5, p.9; UNIMECH Aug-2026 PDF p.6 | MISSED peer contrast on disclosure practice: both listed comparators separated non operating income from operating performance in the same quarter Aequs embedded it in the headline. Converts the earnings quality finding into a demonstrated departure from peer norm and partly explains B06's own peer margin gap finding. |
| C | 01-gate0.md L119-125 (D1) vs L128-133 (D3) | Net debt basis excludes lease liabilities in D1 while D3 includes them, same block and same date. B07 cites the AR's own p.46 net debt to equity of 0.23x, implying net debt of about Rs 342 cr against the Rs 250.05 cr used. Recomputed D1 = 1, Block D = 9, core = 23, grand total = 32. Classification unchanged AVOID; deal breaker 6 still does not fire at 2.14x. |
| C | 07-emoat.md Optionality Register vs Section 5 rows A1/E1/B2/C2/H2 | Hosur, the two Farnborough Tier 1 agreements and the Ajna JV are entered in the Optionality Register and also scored. prompts/07 L195-196: registered options are watched, never scored. Recomputed total falls to between 29.4 and 32.4; STRENGTHENING band unchanged. |
| C | 07-emoat.md L191-199 (B2), L238-244 (E1) | Two of the three Strong rows score already realised, in financials advantages inside a scan defined as moats currently forming. Both rows state the base is already realised, then score H x H = 4 without separating base from increment. A1 handled this correctly by naming its row the Hosur increment. Realised moat is already priced in Gate 0 Block F. |
| C | 07-emoat.md L273-284 (F2) and L533 (6A), against 01-gate0.md L246-252 | F2 scores execution delivery against FY27 aerospace guidance of +25-30 percent revenue at above 20 percent segment margin. B01 recorded that exact guidance as NOT FOUND in corpus and attributed it to company memory. A memory derived figure re-enters as a documented benchmark and propagates into the 6A timeline. |
| C | 07-emoat.md L91-114 (2C) and B07-emoat.yaml L44 | capex_embedded_growth_pct = 63 is built on the claim grade FY27 capex guidance of Rs 660 cr, not on capex under execution as prompts/07 L61-63 specifies. The report's own 2A gives the audited commitment of Rs 21.01 cr, which recomputes to 1.7 percent; Q1 FY27 actual spend of Rs 83 cr gives 8.0 percent. The block carries 63 as a bare integer with no evidence tier for downstream consumption. |
| D | B06 Part 1 Q3, AZAD Q3 FY26 (Feb-2026) margin guide | B06 prose states "36-38% guided long-term" EBITDA margin but the transcript quote cited in the same sentence (Ronak Jajoo) reads "33% to 35%... sustainable". No 36-38 figure exists in the transcript. Directional conclusion survives (33-35 percent still above the Aequs 20-27 percent band) but the reported number is wrong. |
| D | B06 Part 1 Q8 / Part 3 coverage map, UNIMECH Hobel acquisition update call (28-Apr / 04-May-2026), cited "Management, p.10-11" | The all cash and internal funds financing quote is real but sits at the end of the transcript, roughly 10 pages after the cited location; p.10-11 instead carry the customer concentration and valuation multiple discussion. The claim stays supported by AZAD's independent financing detail, so the Q8 verdict is unaffected, but a reader following the stated anchor would not find it. |

### MINOR (27)

| Verifier | Location anchor | Finding |
|---|---|---|
| B | B05 §1B/§4A trigger 9. Aug-2026 PDF p.15 vs p.18 | MISSED: same call contradiction between Harish Bang (40 to 60 percent consumer over five years) and Aravind Melligeri (consumer stays below aerospace for five years). |
| B | B05 §2A promise delivery row 6. Aug-2026 PDF p.12, p.15-16, p.18 | MISSED: an analyst's 80 percent aerospace utilisation figure and mismatched capacity hours figures were left uncorrected on the Q1 FY27 call; B05 treats a different analyst's unchallenged 70 percent figure as evidence of on track delivery. |
| B | B05 §CFO note (top of report). Jun-2026 PDF p.6, p.4 vs Feb-2026 transcript | MISSED: the CFO's "I announced earlier this year" claim is unsupported by the only prior call of the year. |
| B | B05 §3D order book. Feb-2026 PDF p.6; Jun-2026 PDF p.5; Aug-2026 PDF p.4, p.12; AZAD May-2026 PDF p.16 | UNDER-WEIGHTED: no additions, executions or cancellations bridge is disclosed for an order book that grew 23 percent in two quarters, and the two largest wins are excluded from it with no value attached. Mitigated by peer norm (AZAD discloses only a rolling number). |
| B | B05 §2D cash flow paragraph. Aug-2026 PDF p.6 | OVERSTATED as written: "the cash-flow statement itself... never came up, not from management, and no analyst asked either" is false for the Q1 FY27 call, where management volunteered a negative Rs 414 mn operating cash flow. |
| B | B05 triggers 5 and 8; B06 Q8. Aug-2026 PDF p.4, p.6, p.16; Jun-2026 PDF p.15 | NOT ASSESSED TOGETHER: Q1 FY27 combined Rs 830 mn capex, Rs 414 mn operating outflow, Rs 675 mn cash decline, a flagged aerospace capex acceleration, debt plus accrual funding and a possible USD 150 mn raise. Components are individually present; the combination is not evaluated. |
| C | 01-gate0.md L64-69 and B01-gate0.yaml data_notes entry 3 | B3 reached score 0 through a declared override of the scoring band. Stage operating rule 2 forbids qualitative judgments. The same 0 is reachable through the band's own "below 0.20 or negative = 0" clause read against the negative cumulative FCF. Outcome stands; the route is off rule. Framework should disambiguate what "negative" attaches to. |
| C | 01-gate0.md L59-61 | FCF capex taken as acquisition of property, plant and equipment only. The formula definition is purchase of PPE plus intangibles. The intangibles leg is neither included nor declared absent. Both computable FCF years sit far from the B2 and B3 band edges, so no score moves. |
| C | 01-gate0.md L176 (M6) | Anchor reads "AR p.?, Directors Report technology-absorption section, grep-located, page marker not captured in extract". An anchor without a page fails the mandatory source anchor rule. The M6 score of 0 is not in doubt. |
| C | 01-gate0.md L218-224 and B01-gate0.yaml deal_breakers[] | prompts/01 L155 requires stating which years drive any deal breaker. Only entry 8 names its years. Entries 3 and 4 rest on materially different windows (median ROCE on FY25-FY26 only; cumulative CFO/PAT on FY23-FY26) and the windows appear only in data_notes. |
| C | B01-gate0.yaml L19 | The block carries freshness_verdict, a field the stage 1 schema does not define, against an instruction to end with exactly the specified YAML block. B07 carries no equivalent field. If the run-pipeline orchestrator mandates it, this is a rule source conflict to reconcile rather than a maker error. |
| C | 07-emoat.md L142-144 and Section 1A row 1 | A1 evidence labelled documented on the basis of MoU plus capex committed. The report's own Section 2A shows the audited contracted commitment is Rs 21.01 cr and the reciprocal state incentive package is NOT FOUND. The signed MoU is fairly documented; capex committed is not supported by the report's own finding. At the claim multiplier A1 falls 3.0 to 2.1, band unchanged. |
| C | 07-emoat.md Section 5, E2 row | E2 applies a "mixed 0.7x" multiplier. The taxonomy defines only documented 1.0x, claim 0.7x and inference 0.5x. Using the claim multiplier for a mixed category is conservative but the tier is undefined. At 1.0x the total is 36.0, band unchanged. |
| C | 07-emoat.md L26 and L196-197 against L222-223 | The two Farnborough Tier 1 agreements are graded documented in Section 1A and in B2, and claim/documented in C2. One evidence item carries two tiers in the same report. |
| C | 07-emoat.md Section 6C table | prompts/07 L201-203 requires the combined table to carry the injected core score, existing moat count and both classifications. The moat score 9/60 is carried but the existing moat count (2 confirmed, moat_class MODERATE) is not. Core score and both classifications match B01 exactly. |
| C | B07-emoat.yaml L37 against L38 | evidence_mix.documented is 47 while the completionist recount states about 26 distinct documented items. Two documented counts on two definitions, unreconciled in the same block. The completionist guard turns on this count, so the ambiguity is not cosmetic. |
| C | 07-emoat.md Section 3, all categories | prompts/07 L66-67 requires an evidence table or NO EVIDENCE FOUND for each category. Categories are written as anchored prose paragraphs. Content is complete and every claim carries an anchor, and the consolidated 22 row summary table is present; only the mandated per category form is missing. |
| C | B07-emoat.yaml L40-41 | Two of four catalysts_12m are typed evidence_type documented where the dated catalyst event is forward looking management commentary: ECMS PLI first eligible income year FY27, and the Farnborough agreements entering the order book in Q2 FY27. Both are anchored to concalls. A documented fact underlies each, but the dated event is a claim. This feeds Pillar 3 catalyst proximity downstream. |
| C | 07-emoat.md L146-151 (A2) and L450 (4B SEZ row) | Two evidence anchors carry no page reference: "AR Board's Report, Form B" and "AR consolidated tax reconciliation". prompts/07 L35-36 requires a page or slide anchor on every evidence item. Neither item carries a score. |
| C | prompts/07-emerging-moat-pipeline.md L203-208 and 07-emoat.md Section 6D | FRAMEWORK GAP, not a maker error, not counted as an adherence fail. The combined Gate0 plus Emerging Moat lookup matrix is absent from the rule source, which names the eight labels but prints no mapping. The maker declared the gap, reasoned transparently and logged it in input_gaps, which is the compliant response. TURNAROUND is therefore unverifiable; AVERAGE and AVOID are also available and defensible for an AVOID backward score paired with STRENGTHENING forward. Operator ruling needed before combined_assessment travels downstream. |
| C | prompts/07-emerging-moat-pipeline.md L170-171 and 07-emoat.md rows B1, G1, G2 | FRAMEWORK GAP, not a maker error, not counted as an adherence fail. The likelihood times impact matrix has no cell for evidence that contradicts a category; its floor for any evidenced category is LL = 1. B1, G1 and G2 therefore add 3.0 points for three categories the report explicitly says the evidence argues against. Removing all three gives 32.4, band unchanged. Consider a contradicted evidence cell scoring 0. |
| D | B06 Part 1 Q6, AZAD Q4 FY26 (May-2026) | The working capital day quote ("H1 about 200 tapering to H2 160-170") is attributed to Ronak Jajoo (CFO) but was actually spoken by Rakesh Chopdar (Chairman and CEO); page and content are correct. |
| D | B06 Part 1 Q2, UNIMECH Q3 FY26 (Feb-2026), "52 weeks" citation | Cited page (about p.10) is roughly two pages before the quote's actual location; speaker attribution correct. |
| D | B06 Part 2A / risks register, UNIMECH Q4 FY26 (Jun-2026) geopolitical caution quote | Cited page (about p.3) is roughly two pages before the quote's actual location; speaker and content correct. |
| D | B06 Part 1, systemic across citations | Page citations inconsistently mix PDF page count and printed in document page number conventions with no stated rule, the proximate cause of the three MINOR anchor location findings above; every citation checked resolves to correct content within 0 to 2 pages once the applicable convention is identified. |
| D | B06 Part 1 Q3, UNIMECH Q1 FY27 (Aug-2026) | B06 does not cite UNIMECH's explicit refusal to disclose per business line margins, which would have reinforced the report's own cross peer reticence observation (echoing the Q5 finding on concentration) by extending it to margin disclosure. Quote: "we don't want to disclose margins on each businesses rather than only on a consolidated basis" (Aakash Jaiswal, about p.13). |
| D | B06 Part 2, AZAD all four calls | The running DRDO and GTRE indigenous jet engine delivery narrative across all four AZAD calls is not referenced anywhere in B06; tangential to all nine B05 claims, so the omission does not reduce coverage completeness. |

## Not covered in this pass

- Verifier C's valuation half is **pending phase 3**. Stages 10 and 11 did not
  run, so recomputed_destination_pe and recomputed_decision are empty in B12c and
  no valuation rule set was audited.
- Verifier C recorded stage 13 synthesis as outside phase 1 scope at the time of
  its pass (`business_understanding_narrative.present: false`, scope_note:
  "Stage 13 synthesis is not in phase-1 scope and does not exist for this run.
  Not evaluated, not a REWORK trigger here. Deferred to the stage 13 verifier
  pass."). This file and the two beside it are that stage 13 output and are
  therefore unverified.
- Verifier B logged no `pipeline_flags_not_supported`: every flag the pipeline
  raised is supported by the source.
- Verifier D logged no `substantive_unsupported` peers and no
  `verdict_discipline_fails`.
