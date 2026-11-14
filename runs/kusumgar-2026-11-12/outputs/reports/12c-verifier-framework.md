# VERIFIER C (B12c): FRAMEWORK ADHERENCE, PHASE 1 SCOPE. KUSUMGAR, run 2026-11-12

Scope. Phase 1 only: Gate 0 (B01) and Emerging Moat (B07). The valuation audit did not run. No B10 or B11 exists. Rules 4, 6, 7 and 9 to 15 of the Verifier C rubric are out of scope here. The valuation section of B12c is PENDING PHASE 3.

Rule sources (the only two loaded): prompts/01-gate-0-pipeline.md, prompts/07-emerging-moat-pipeline.md.

Artifacts audited: outputs/reports/01-gate0.md, outputs/blocks/B01-gate0.yaml, outputs/reports/07-emoat.md, outputs/blocks/B07-emoat.yaml. For each stage, the YAML at the end of the report and the block file are identical (checked line by line).

Method. I re-derived each score from the inputs the artifact states, against the thresholds in the rule file. I take each number as the artifact states it. Whether a number sits in the source PDF is Verifier A's question, not this one. Line references: "01 L55" = prompts/01 line 55; "07 L172" = prompts/07 line 172; "B01 rpt L29" = 01-gate0.md line 29; "B07 rpt L105" = 07-emoat.md line 105.

Result. 51 rules checked. 43 pass. 8 fail: 0 CRITICAL, 2 MAJOR, 6 MINOR. Acceptance rate 84.3% (43 / 51). No REWORK trigger in scope. Rule 8 (categories 21 and 22 present and gated) passes, so there is no REWORK for stage 7. The Gate 0 classification (AVERAGE before the downgrade, AVOID after it) holds under every recomputation and every disclosed sensitivity.

## A. GATE 0 (B01) COMPLIANCE

| # | Rule (source) | Artifact value | Re-derived | Result |
|---|---|---|---|---|
| G01 | Opening data-availability line; history adaptation (01 L23-25) | "Data available: 4 years (FY2023 to FY2026). Scoring adapted to 4-year history." (B01 rpt L3) | As stated | PASS |
| G02 | Anchor after every extracted number (01 L15-18) | Anchors on every scored input; screener print marked SECONDARY | Every scored row checked | PASS |
| G03 | Missing data = NOT FOUND, scored 0, no estimates (01 L19-22) | FY23 ROCE, FY23 payables, FY23 capex, E2 series, Sep 2026 pledge, M7, M8 marked NOT FOUND | No filled gap found | PASS |
| G04 | ROCE: use the source figure; compute only when absent (01 L29-31) | Prospectus ROCE 55.87 / 42.89 / 24.76%, same formula, re-derived | 1,213.93 / 2,172.82 = 55.87%; 1,654.14 / 3,857.08 = 42.89%; 1,609.36 / 6,500.84 = 24.76% | PASS |
| G05 | ROE: earliest year on closing net worth, stated (01 L32-33) | FY23 ROE "NOT FOUND (no FY22 equity)" (B01 block data_notes) | FY23 closing equity 1.99 + 53.62 = 55.61 Cr is in the artifact (B01 rpt L29). 37.22 / 55.61 = 66.9%. 4-year median 61.6% | **FAIL (MINOR), C-G05.** A3 stays 5 |
| G06 | WC days formula; basis stated (01 L34-38) | Revenue basis stated; 104.3 / 68.3 / 190.6 | 32.95 + 112.10 - 40.78 = 104.27; 26.29 + 64.14 - 22.12 = 68.31; 123.05 + 102.78 - 35.21 = 190.62 | PASS |
| G07 | FCF = CFO - capex, capex = PPE + intangibles (01 L39-40) | +1,229.22 / -2,617.14 / -413.29 INR m | Subtractions and sum (-1,801.21) correct. See observation 4 | PASS |
| G08 | CAGR = (End / Start)^(1/years) - 1 (01 L41) | Revenue 31.9%, PAT 38.2% | (692.0 / 301.65)^(1/3) - 1 = 31.9%; (98.2 / 37.22)^(1/3) - 1 = 38.2% | PASS |
| G09 | CAGR edge rules (01 L43-50) | Endpoints positive; "No loss-to-profit swing" in data_notes; C4 computed | No N/M case arises | PASS |
| G10 | Block A thresholds (01 L54-59) | 5 / 5 / 5 / 0 = 15 | Median ROCE 42.89 (>=25) = 5; min 24.76 (>=15) = 5; median ROE 56.26 (>=20) = 5; 24.76 - 55.87 = -31.1pp (>5pp) = 0 | PASS |
| G11 | Block B thresholds (01 L61-68) | 0 / 0 / 0 / 0 = 0 | 91.82 / 331.81 = 0.277 (<0.50) = 0; 1 of 3 = 33% (<50) = 0; -1,801.21 / 2,945.84 negative = 0; +86.3 days (>15) = 0 | PASS |
| G12 | Block C thresholds (01 L70-74) | 5 / 5 / 1 / 5 = 16 | 31.9% = 5; 38.2% = 5; 2 of 3 = 67% = 1; +6.3pp = 5 | PASS |
| G13 | Block D thresholds (01 L76-86) | 4 / 4 / 4 / 5 = 17 | 1,755.21 / 1,878.50 = 0.93x = 4; 1,609.36 / 259.78 = 6.19x = 4; 2,235.82 / 5,029.54 = 0.44 = 4; 5,332.20 / 2,549.88 = 2.09 = 5 | PASS |
| G14 | Block E thresholds (01 L88-95) | 5 / 0 / 5 / 1 = 11 | 75.01% = 5; E2 NOT FOUND as a series and -14.43pp both give 0; 0% pledge = 5; 1,089.70 / 5,029.54 = 21.7% = 1 | PASS |
| G15 | Core score | 59 | 15 + 0 + 16 + 17 + 11 = 59 | PASS |
| G16 | Moat test bands M1-M12 (01 L97-135) | M4 = 0 | M4 gives 0 only for "3+ decline years" and has no "else 0". Record: 1 decline year. Recomputed M4 = 1 (fiscal-year reading) or 3 (trailing-twelve-month reading) | **FAIL (MINOR), C-G16.** Moat score 14 (or 16) |
| G17 | PEER DATA NEEDED scores 0, marked (01 L99-100) | M2, M5, M9 = 0, marked | As stated | PASS |
| G18 | M11 with fewer than 6 years: overall trend, stated (01 L129-133) | 3 on the overall trend, stated, with a 0 sensitivity | 31.9% (>=20) and selling plus admin 5.07% to 4.54% (declining) = 3 on the literal band | PASS (observation 5) |
| G19 | Moat present count and class (01 L137-138) | 13; 3 present; MODERATE | 5 + 5 + 3 = 13; 3 present = MODERATE | PASS |
| G20 | Classification matrix (01 L146-149) | AVERAGE before downgrade | Core 59 is in the 40-59 band = AVERAGE | PASS |
| G21 | Data confidence (01 L142-144) | 4 years LIMITED, one tier down = AVOID | 3-4 years = one-tier downgrade; AVERAGE to AVOID | PASS |
| G22 | Deal-breakers 1-9 (01 L155-159) | DB2 (max GOOD) and DB4 (max AVERAGE) fire; others do not | DB2: Block B 0 (<8). DB4: 0.277 (<0.50). DB7: 1 of 3 decline years, not a majority. DB8: PAT positive every year. DB6: 0.93x and 6.19x | PASS |
| G23 | Years that drive each deal-breaker stated (01 L151-154) | DB4: FY25 and FY26 against FY24. DB2: year-by-year drivers in the FLAG-GATE0 reason | Present | PASS |
| G24 | FLAG-GATE0 when class <= AVERAGE with depressors (01 L175-177) | Raised; depressors named with years | AVOID <= AVERAGE | PASS |
| G25 | No qualitative judgments (01 L13) | analyst_note: "the pre-downgrade AVERAGE is the cleaner reading" | A judgment against the rule result | **FAIL (MINOR), C-G25** |
| G26 | YAML schema; analyst_note <= 200 words (01 L168-198) | All fields present; note about 158 words | As stated | PASS |

Gate 0: 26 rules checked, 23 pass, 3 fail (all MINOR). No block score, core score, or classification changes.

Sensitivity re-check (B01's own disclosures):
- Restated years only (FY24-FY26). C1 21.61% = 5, C2 7.87% = 1, C3 1 of 2 = 50% = 1, C4 7.87 - 21.61 = -13.7pp = 0. Block C = 7. Core = 50. Still AVERAGE.
- Leases inside debt. D1 1.28x = 3. Core = 58. Still AVERAGE.
- Both together. Core = 49. Still AVERAGE.
- M3 on closing PPE (2.94x) = 3. M3 stays present.
- M4 at 1 or 3 (finding C-G16). AVERAGE in both. In the 40-59 core band the matrix gives AVERAGE whatever the moat class.
After the LIMITED-history downgrade, every case gives AVOID.

## B. EMERGING MOAT (B07) COMPLIANCE

| # | Rule (source) | Artifact value | Re-derived | Result |
|---|---|---|---|---|
| E01 | All six sections plus the register, one response (07 L28) | Sections 1-6 and the Optionality Register present | As stated | PASS |
| E02 | Evidence taxonomy on every evidence item (07 L29-34) | [DOC] / [CLAIM] / [INF] mapped to the three tiers and multipliers | Every scored row is tagged. Untagged lines sit only in zero-score or contrary rows | PASS |
| E03 | Source anchor on every evidence item (07 L35-36) | At least 11 items anchored only to B03 or B05 outputs | B03 is not a stage 7 input (07 L7, L246-264) | **FAIL (MINOR), C-E03** |
| E04 | NO EVIDENCE FOUND stated; no force-fit (07 L39-40) | A2, A3, B1, B3, D1, D2, E1, F1, G1, G2, H1, I1, I2 so stated | As stated | PASS |
| E05 | 22 categories plus R1, 23 scored rows (07 L65-67, L171-174) | 22-row summary; 23-row scorecard | Count matches | PASS |
| E06 | Likelihood x impact matrix (07 L171-172) | A1 MH 3; A4 LL 1; B2 HM 3; C1 ML 1; C2 MM 2; E2 HM 3; F2 LL 1; H2 HM 3; H3 LL 1; R1 MM 2 | Every cell matches the matrix | PASS |
| E07 | Evidence multipliers 1.0 / 0.7 / 0.5 (07 L172-173) | 2.1, 0.5, 3.0, 1.0, 2.0, 3.0, 0.5, 3.0, 1.0, 1.4 | Every product correct | PASS |
| E08 | Adjusted total | 17.5 | 2.1 + 0.5 + 3.0 + 1.0 + 2.0 + 3.0 + 0.5 + 3.0 + 1.0 + 1.4 = 17.5 | PASS |
| E09 | Absolute bands; UA qualifier stated (07 L175-181) | MODEST; "EM >= 25" not met, stated | 12-24 = MODEST | PASS |
| E10 | I1/I2 contribution stated separately (07 L180-181) | 0.0 of 17.5 | As stated | PASS |
| E11 | Category 21 (I1): both legs, (b) leg with a documented source (verifier rule 8; 07 L122-138) | 0; neither leg evidenced | Gate honoured | PASS |
| E12 | Category 22 (I2): a specific named sacrifice (verifier rule 8; 07 L139-153) | 0; "nothing must be destroyed" | Gate honoured | PASS (observation 6) |
| E13 | Completionist recount in the mandated form; 12-category guard (07 L41-46, L157-159) | "15 documented items across 7 categories"; 10 rows above zero | Performed; guard not reached | PASS (recount accuracy sits in C-E15) |
| E14 | No claim-only category scored as documented (verifier rule 3) | A1 and R1 at 0.7x; A4 and F2 at 0.5x | None found | PASS |
| E15 | One improvement, one mechanism (B07's own control, B07 rpt L105; CLAUDE.md NEVER list) | Three evidence items each credited in two categories | em_score 15.5 to 17.5, depending on allocation | **FAIL (MAJOR), C-E15** |
| E16 | 2C arithmetic shown; block field matches (07 L60-62) | 101.04 x 3.40 = 343.5; 4.96% stated as 5.0 | 101.04 x 3.40 = 343.5; 343.5 / 6,920.03 = 4.96%. Sensitivities 4.29% and 7.83% also correct | PASS |
| E17 | 1A status vocabulary (07 L49-51) | LAUNCHED-recent, UNDER DEVELOPMENT, ANNOUNCED, CONCEPT | All from the list | PASS |
| E18 | Section 4 (R1): 4A, 4B with amounts and sharing, 4C (07 L161-168) | Present; PLI NOT FOUND | As stated | PASS |
| E19 | Register covers forward items scored 0 or resting on claim/inference only (07 L183-196) | 11 rows; no A1 row | A1 rests on claims only by B07's own recount | **FAIL (MINOR), C-E19** |
| E20 | 6C uses the injected Gate 0 block (07 L202-203) | Core 59; moat 13/60, 3 confirmed, MODERATE; AVOID; MODEST | Matches B01 | PASS |
| E21 | 6D combined class on the injected inputs; HIGH POTENTIAL and TURNAROUND reasoned (07 L203-208) | AVERAGE | AVOID expected on the injected backward class | **FAIL (MAJOR), C-E21** |
| E22 | 6A, 6B, 6E present (07 L199-210) | Present | As stated | PASS |
| E23 | catalysts_12m evidence_type follows the taxonomy (07 L29-34, L231-232) | Catalyst 2 tagged DOCUMENTED | ANALYST INFERENCE | **FAIL (MINOR), C-E23** |
| E24 | F2 cross-references the injected promise-delivery record (07 L106-107) | B05 one-quarter record used as a supplement only | As stated | PASS |
| E25 | YAML schema; active_categories only Strong/Moderate; note <= 200 words (07 L216-243) | 5 Moderate rows; note about 139 words | As stated | PASS |

Emerging Moat: 25 rules checked, 20 pass, 5 fail (2 MAJOR, 3 MINOR). em_classification MODEST holds under every recomputation. The EM >= 25 UA qualifier stays unmet in every case.

## C. FINDINGS (each FAIL, with the recomputed value)

**C-G05 (MINOR). Gate 0 ROE fallback not applied.**
Rule (01 L32-33): "if opening net worth unavailable for the earliest year, use closing and state so."
Claimed: FY23 ROE "NOT FOUND (no FY22 equity)" (B01 block data_notes).
Recomputed: FY23 closing equity 1.99 + 53.62 = 55.61 Cr is in the artifact (B01 rpt L29). FY23 PAT is 37.22 Cr (B01 rpt L11, screener-data). FY23 ROE = 37.22 / 55.61 = 66.9% on closing equity. The 4-year median ROE is (56.26 + 66.9) / 2 = 61.6%, against the 3-year 56.26%.
Effect: A3 stays 5. No change to scores or classification. FY23 carries the screener basis caveat that B01 already states.

**C-G16 (MINOR). M4 scored 0 with no band that gives 0.**
Rule (01 L109-111): "zero revenue-decline years AND receivable days stable ±10 = 5 | max 1 decline year, fully recovered = 3 | 2 decline years, CAGR positive = 1 | 3+ decline years = 0". M4 has no "else 0", unlike M1, M3, M6, M10 and M11.
Claimed: 0, "one revenue-decline year (FY26) not recovered on a full-year basis" (B01 rpt L113).
Recomputed: the record is 1 decline year with a positive CAGR (31.9%). The literal 0 band needs 3 or more decline years. Two readings:
- Fiscal-year reading (the one B01 chose): no recovery yet. The nearest band that covers 1 unrecovered decline year with a positive CAGR is the 1-band (a record with fewer declines cannot rank below "2 decline years, CAGR positive"). M4 = 1.
- Trailing-twelve-month reading: revenue = 692.0 - 261.25 + 498.19 = 928.94 Cr, derived from B01's screener-data figures (B01 rpt L12), against the FY25 peak of 779.0 Cr. That is fully recovered, so M4 = 3.
The rule text does not say which reading applies.
Effect: moat score 14 (fiscal) or 16 (TTM). Grand total 73 or 75. Moats present 3 (MODERATE) or 4 (STRONG). Classification unchanged: core 59 sits in the 40-59 band, which gives AVERAGE whatever the moat class.

**C-G25 (MINOR). Qualitative judgment in the Gate 0 analyst_note.**
Rule (01 L13): "No qualitative judgments. Only numbers and the scoring rules provided."
Claimed: "The AVOID label stacks a LIMITED-history downgrade on an AVERAGE; the pre-downgrade AVERAGE is the cleaner reading." (B01 block analyst_note.)
Recomputed: the first clause is fact and stands. "The cleaner reading" judges against the result the rules produce. The rule file's route for a post-IPO rebase is downstream position sizing (01 L152-154), not a second classification. B07 6D cites this sentence to set its combined class (C-E21). That is how the judgment spread.
Effect: none on B01 values. It is the source of C-E21.

**C-E03 (MINOR). Evidence anchored to upstream stage outputs, not to source documents.**
Rule (07 L35-36): "SOURCE ANCHORS on every evidence item: (AR p.__), (Q_ FY__ call), (Inv. Pres. slide __)." B03 is not among the stage 7 inputs (07 L7; injected inputs 07 L246-264 are B01, the B05 promise-delivery record, AR, transcripts, presentation).
Claimed: items whose only anchor is B03 or B05:
- B2 counter-evidence that sets Impact at M, not H: "Customer 1 fell from 2,225.88 (FY25) to 751.27; an A&D Fabrics order of 2,045.75 ... 'not re-ordered' (B03 fact 2)" (B07 rpt L135).
- G2: "customer advances 1,264.61 to 87.59 (B03 Phase 3B)" (L183).
- F1: "The CEO holds 94.7% of options (B03 Phase 2H)" (L168).
- I1: "executive pay 54.70, B03 Phase 5C" (L205).
- A3: "inventory credit (B03 Phase 3C)" (L117).
- 2A: "PPE additions 613.69 (FY25), 1,118.88 (FY26) (B03 fact 3)"; "HDFC term loans incl. new 950.00 tranche; CCPS 1,244.94 (B03 Phase 2F, 3A)" (L63).
- 2B: "MD&A basis (B03 fact 3)" (L82).
- F2: "three-year FCF -1,801.21 (B03)" (L179).
- C2: "Names withheld for nine of the top ten customers (B03)" (L153).
- 6B and catalysts: "B05 red flags", "B05 trigger 1/3/4/6", "B05 timeline_slippages" (L84, L312-314, L325).
Recomputed: re-anchor each item to the prospectus or results page, or mark it as carried from B03/B05.
Effect: weak anchors only. Verifier A owns whether each number exists at a source page.

**C-E15 (MAJOR). Three evidence items credited in two categories each.**
Rule: B07's own double-credit control (B07 rpt L105): "Certifications, approvals and tender fulfilment are credited in B2 only ... Licensed A&D Solutions revenue is credited in H2 only." CLAUDE.md: "Never credit one quality improvement through two mechanisms."
Claimed:
1. Prospectus p.212 certificate list. B2 row: "AS9100D, IATF 16949, ISO 9001/14001, GRS, Oeko-Tex held | [DOC]" (L129). H3: "[DOC] GRS, Oeko-Tex, ISO 14001 held (Prospectus p.212)" (L202). H3's 1.0 rests only on these certificates. The recount counts them twice ("B2: certifications" and "H3: ESG certifications = 1", L236).
2. Prospectus p.210 automotive tape customer case. B2 row: "two-year qualification ... Nylon 66 qualified ... Nylon 6 substitute" (L131). C1: "[DOC] one co-development case that moved across three products at the same customer (Nylon 66, Nylon 6, EV yarn) (Prospectus p.210)" (L141). C1's 1.0 rests only on this case. The recount lists no C1 document, yet C1 carries the 1.0x multiplier.
3. Prospectus p.210 parachute partner case. B2 row: "first bulk orders 2021, then localisation of a high-altitude system for an Indian government customer" (L132). H2 row for the US airborne partner: "(case study: first bulk orders 2021) | [DOC] Prospectus p.195, p.210" (L192). This is the licensed A&D Solutions line, which the control puts in H2 only.
Recount accuracy, same root. A4's "[DOC] over 1,000 SKUs (Prospectus p.189)" (L119) is not recounted. The Toray partnership counts twice inside H2 ("four exclusive written agreements plus the Toray holding = 5"; the Japanese conglomerate row is one of the four).
Recomputed: each item must sit in one category. em_score as reported is 17.5. It becomes 15.5 if C1 and H3 go to 0 and B2 is scored as before. It stays 17.5 if the three items leave B2 and B2 holds H x M = 3 on what remains (AS9100D, IATF 16949, the rucksack tender). Whether B2 holds is stage 7's judgment, not this audit's. The documented recount falls from 15 to 14 on the exact p.212 duplicate alone.
Effect: band MODEST (12-24) in every allocation. The EM >= 25 UA qualifier stays unmet in every allocation. em_score is a Pillar 3 input in phase 3. Until stage 7 assigns each item once, carry it as the range 15.5 to 17.5.

**C-E19 (MINOR). A1 missing from the Optionality Register.**
Rule (07 L184-189): the register lists "forward advantages that scored 0 or rest only on [claim]/[inference] evidence", each with the documentation that would convert it.
Claimed: 11 register rows, none for A1. B07's own recount says "A1 has no separate documented item and was scored at 0.7x on its claim-heavy evidence" (L236). A1's score rests on three claims: "only one of two suppliers globally" of zero-porosity parachute fabric, "only Indian manufacturer of Kevlar filament fabrics", and fine denier (Concall p.5, L111).
Recomputed: add one A1 row. Converting evidence: an independent manufacturer count, or a customer qualification document that names the company as sole or dual source.
Effect: monitoring coverage only. No score change.

**C-E21 (MAJOR). 6D combined class set on the pre-downgrade Gate 0 class, not the injected one.**
Rule (07 L202-205): 6C uses "the INJECTED Gate 0 block (core score, existing moat count, both classifications)"; 6D gives the "combined classification per the standard matrix".
Claimed: combined_assessment AVERAGE. 6D reasoning: "Gate 0 is AVOID only because four years of history triggers a one-tier downgrade of AVERAGE (B01) ... B01's own note calls the pre-downgrade AVERAGE the cleaner reading." (L342.) 6C shows the injected AVOID correctly (L335). 6D then reasons from AVERAGE.
Recomputed: B07 rejects both uplift rows itself. HIGH POTENTIAL: "Forward score is 17.5, not 40+" (L344). TURNAROUND: "cash conversion has not repaired" (L345). A MODEST forward score gives no lift. So the only route from the injected AVOID to AVERAGE is the swap to the pre-downgrade class. On the injected backward class the expected result is AVOID. One caveat: if the standard matrix maps AVOID with MODEST to AVERAGE, AVERAGE stands. prompts/07 names the matrix but does not define it, so the orchestrator confirms the mapping against the matrix text.
Effect: combined_assessment feeds synthesis and the gate recommendation. Flags propagate and nothing halts, so the decision likely survives. The B01 rule's route for a post-IPO rebase is position sizing (01 L152-154). Stage 7 does not reclassify.

**C-E23 (MINOR). Catalyst evidence tier overstated.**
Rule (07 L29-34): DOCUMENTED = "capex committed, patent filed, contract signed, plant under construction, product launched, regulatory application submitted."
Claimed: catalysts_12m item 2, "Trade receivable days fall below 90 and CFO above 50% of EBITDA", evidence_type "DOCUMENTED", anchor "B05 trigger 3; Q2 results p.11-12".
Recomputed: ANALYST INFERENCE. It is a monitoring threshold taken from a B05 trigger, and no document evidences it. Management's own stated full-year cycle is 100-120 days (Q2 Q&A 17, quoted at B07 rpt L183), which is the opposite of the threshold. Item 1 is mixed: the 2,371.96 INR mn order is documented, but the "80% by Mar 2027" path comes from a B05 trigger.
Effect: none at phase 1. Phase 3 carry: catalysts_12m "feeds Pillar 3 catalyst proximity" (07 L231). The phase 3 audit checks that stage 11 does not credit catalyst 2 as documented.

## D. OBSERVATIONS (not scored; no rule FAIL)

1. B07 analyst_note: "Concentration improved ... but the 100% offer for sale and the loss of the FY25 single orders drive part of it." An offer for sale changes the shareholding. It cannot move customer revenue shares. The order roll-off half of the sentence stands. The OFS half has no mechanism.
2. Numbers that differ between B01 and B07. Verifier A is the authority. They are listed here so the orchestrator does not lose them:
   - Pre-offer promoter holding: 89.44% (B01, prospectus p.59) against 89.79% (B07 rpt L14, Prospectus p.28 via B03 fact 4).
   - Offer-for-sale share count: 15,521,350 (B01, Q2 FY27 results p.7) against 15,521,698 (B07 rpt L14).
   - H1 FY27 CFO: 340.73 INR m, standalone (B01 rpt L71, Q2 FY27 results p.6) against 248.85 INR mn (B07 rpt L11, Q2 results p.12). This looks like a standalone versus consolidated basis trap. The two artifacts read H1 cash in opposite directions: B01 says "first evidence of collection"; B07 says "cash conversion has not repaired".
3. Q2 FY27 call. B01 says "The Q2 FY27 call transcript was not published at collection." B07 says "no Q2 FY27 call was held, a written Investor Q&A replaced it." These are two different facts. Stage 0 or the corpus record settles which one is true.
4. B01 capex is "PPE purchase net of subsidy + intangibles" (B01 data_notes). The formula (01 L39-40) says purchase of PPE plus intangibles. If the subsidy were added back, FCF would fall further. B2 and B3 stay 0 either way.
5. M11 depends on the window. With the FY23 start, selling plus admin goes from 5.07% to 4.54% (declining, band 3). With the restated FY24 start, it goes from 4.17% to 4.54% (rising, band 1). With M11 at 1, moats present = 2, still MODERATE. B01 disclosed the 0 case.
6. B07 I2 answers "what must be destroyed" for A1, B2, H2 and E2 only. C1, A4, F2, H3 and R1 get no answer of their own. I2 = 0 either way.
7. R1's evidence tag differs across B07. The scorecard says CLAIM (0.7x). The recount counts it as documented ("incentive receipts = 1") and also as inference. The 0.7x weight is the lower of the documented and claim options, so nothing is inflated.

## E. NOT IN SCOPE THIS PHASE

- Rule 4 (valuation growth symmetry and pillar mechanics), the valuation leg of rule 5, rule 7 (method plurality), rules 11-15 (v3.8 exit construction, A19 FV path, Expectation Ledger, ledger gates, skill-to-source fidelity): PENDING PHASE 3. They need B10 and B11.
- Rule 6 (B09 downstream candidates): B09 is not among this invocation's inputs. Not checked.
- Rule 9 (Business Understanding Narrative): it checks the stage 13 synthesis. Not checked.
- Rule 10 (Halt 1 dossier B09b): it fires at /finalize. The phase 1 structural check sits in run-pipeline step 6b.

## F. PHASE 3 CARRY-FORWARD

- Use em_score as the range 15.5 to 17.5 until stage 7 assigns each double-credited item once (C-E15). Band MODEST either way. UA EM >= 25 unmet either way.
- Catalyst 2 in catalysts_12m is ANALYST INFERENCE, not DOCUMENTED (C-E23). The Pillar 3 audit checks how stage 11 credits it.
- combined_assessment AVERAGE rests on the pre-downgrade class (C-E21). Synthesis should read the injected Gate 0 AVOID, with the post-IPO rebase handled in position size.

```yaml
stage: B12c
company: "KUSUMGAR"
run_date: "2026-11-12"
model: "claude-opus-5-5"  # must equal .claude/agents frontmatter; the orchestrator compares it
status: complete
gate0: {rules_checked: 26, fails: ["C-G05", "C-G16", "C-G25"]}
emoat: {rules_checked: 25, fails: ["C-E03", "C-E15", "C-E19", "C-E21", "C-E23"]}
valuation: {rules_checked: 0, fails: [], status: "PENDING PHASE 3: phase-1 scope invocation, no B10 or B11 exists"}
expectation_ledger: {status: "PENDING PHASE 3", present: null, downside_row: null, all_rows_confirm_by: null, all_rows_metric_threshold: null, prob_in_range: null, decay_status_valid: null, off_ledger_credit: null, residual_pct_cmp: null, residual_starter_cap_ok: null, fails: []}  # rules 13-14; any fail = REWORK stage 11
business_narrative: {status: "NOT IN SCOPE: rule 9 checks the stage 13 synthesis", fails: []}  # rule 9; any fail = REWORK stage 13
recomputed_destination_pe: ""  # blank if concur; else both values
recomputed_decision: ""        # blank if concur
findings:
  - {id: "C-G05", framework: "gate0", rule: "ROE earliest year on closing net worth, stated (prompts/01 L32-33)", severity: "MINOR", claimed: "FY23 ROE NOT FOUND (no FY22 equity)", recomputed: "FY23 ROE 66.9% = PAT 37.22 Cr / closing equity 55.61 Cr (1.99 + 53.62, screener-data, B01 rpt L29); 4-year median ROE 61.6% vs 56.26%", effect: "A3 stays 5; no score or classification change"}
  - {id: "C-G16", framework: "gate0", rule: "M4 band ladder; 0 only for 3+ decline years, no else-0 (prompts/01 L109-111)", severity: "MINOR", claimed: "M4 = 0 (1 decline year FY26, not recovered)", recomputed: "M4 = 1 on the fiscal-year reading B01 chose; M4 = 3 on a TTM reading (TTM revenue 692.0 - 261.25 + 498.19 = 928.94 Cr vs FY25 779.0 Cr, derived from B01 screener-data figures); moat score 14 or 16, grand total 73 or 75, moats present 3 (MODERATE) or 4 (STRONG)", effect: "classification unchanged: core 59 in 40-59 band = AVERAGE whatever the moat class; LIMITED downgrade = AVOID"}
  - {id: "C-G25", framework: "gate0", rule: "No qualitative judgments (prompts/01 L13)", severity: "MINOR", claimed: "analyst_note: the pre-downgrade AVERAGE is the cleaner reading", recomputed: "drop the judgment; keep the fact that AVOID = AVERAGE plus one LIMITED-history tier; the rule route for a post-IPO rebase is downstream position sizing (prompts/01 L152-154)", effect: "no B01 value changes; it is the source of C-E21"}
  - {id: "C-E03", framework: "emoat", rule: "Source anchor on every evidence item (prompts/07 L35-36); B03 not a stage 7 input (L7, L246-264)", severity: "MINOR", claimed: "at least 11 evidence items anchored only to B03 or B05 (e.g. B2 counter-evidence Customer 1 2,225.88 to 751.27 at B03 fact 2; G2 customer advances at B03 Phase 3B; F1 options at B03 Phase 2H; I1 executive pay at B03 Phase 5C)", recomputed: "re-anchor to prospectus or results pages, or mark as carried from B03/B05", effect: "weak anchors; Verifier A owns existence at source"}
  - {id: "C-E15", framework: "emoat", rule: "One improvement, one mechanism (B07 own control at rpt L105; CLAUDE.md)", severity: "MAJOR", claimed: "em_score 17.5 with p.212 certificates in B2 and H3, p.210 automotive tape case in B2 and C1, p.210 parachute partner case in B2 and H2; recount 15 documented items", recomputed: "em_score 15.5 (C1 and H3 to 0, B2 as scored) to 17.5 (items leave B2 and B2 holds HxM = 3 on AS9100D, IATF 16949 and the rucksack tender); documented recount 14 on the exact p.212 duplicate alone; A4 SKU item (p.189) not recounted; Toray counted twice inside H2", effect: "band MODEST in every allocation; UA EM >= 25 unmet in every allocation; carry em_score as range 15.5-17.5 into Pillar 3 until stage 7 assigns each item once"}
  - {id: "C-E19", framework: "emoat", rule: "Optionality register covers forward items scored 0 or resting only on claim/inference (prompts/07 L184-189)", severity: "MINOR", claimed: "11 register rows; no A1 row though B07 recount states A1 has no separate documented item", recomputed: "add an A1 row: one-of-two global zero-porosity supplier and only-Indian Kevlar filament claims; converting evidence an independent manufacturer count or a customer qualification document naming sole or dual source", effect: "monitoring coverage only; no score change"}
  - {id: "C-E21", framework: "emoat", rule: "6C/6D on the INJECTED Gate 0 block, combined class per standard matrix (prompts/07 L202-205)", severity: "MAJOR", claimed: "combined_assessment AVERAGE, reasoned from the pre-downgrade class (B01 note: cleaner reading)", recomputed: "AVOID expected on the injected backward class: B07 itself rejects HIGH POTENTIAL (17.5 not 40+) and TURNAROUND (cash conversion not repaired), and MODEST gives no forward lift; the matrix text is not in prompts/07, so the orchestrator confirms whether AVOID + MODEST maps to AVERAGE", effect: "feeds synthesis and the gate recommendation; flags propagate, decision likely survives"}
  - {id: "C-E23", framework: "emoat", rule: "Evidence taxonomy applied to catalysts_12m (prompts/07 L29-34, L231)", severity: "MINOR", claimed: "catalyst 2 (receivable days below 90, CFO above 50% of EBITDA) evidence_type DOCUMENTED", recomputed: "ANALYST INFERENCE: a B05-trigger threshold with no documented basis; management states a 100-120 day cycle (Q2 Q&A 17); catalyst 1 is mixed (order documented, 80% by Mar 2027 path from a B05 trigger)", effect: "none at phase 1; phase 3 checks stage 11 does not credit catalyst 2 as documented in Pillar 3"}
critical_count: 0
major_count: 2
minor_count: 6
acceptance_rate: 84.3             # rules passed / rules checked, %: 43 / 51 (gate0 23/26, emoat 20/25); phase-1 scope only
```
