# STAGE 12 VERIFIER C: FRAMEWORK ADHERENCE, PHASE 1 SCOPE
SUSAN (Susan Electricals India Ltd) | Run date 2026-09-19 | Model: claude-opus-5

Scope: Gate 0 (B01) and Emerging Moat (B07) only. The valuation audit (B10/B11, rules 4-7 and 11-15) is deferred to phase 3. Rule 9 (narrative, stage 13) and rule 10 (dossier, /finalize) fall outside this scope.

Rule sources read: prompts/01-gate-0-pipeline.md, prompts/07-emerging-moat-pipeline.md.
Artifacts audited: outputs/reports/01-gate0.md, outputs/blocks/B01-gate0.yaml, outputs/reports/07-emoat.md, outputs/blocks/B07-emoat.yaml.

Method: every score was re-derived from the inputs the report states, using the thresholds in the rule files. This audit judges rule application only. Whether a number exists in the source is Verifier A's question, and this report does not answer it. Where a finding cites a figure, the figure is the stage report's own stated input (report file, line).

---

## PART 1: GATE 0 (B01) COMPLIANCE

### 1A. Block re-derivation

| Rule | Stated input (01-gate0.md line) | Threshold band | Stage score | Recomputed | Result |
|---|---|---|---|---|---|
| A1 median ROCE | 17.46% (L73) | 15-19.9 = 3 | 3 | 3 | PASS |
| A2 min ROCE | 9.47% FY24 (L75) | 8-11.9 = 1 | 1 | 1 | PASS |
| A3 median ROE | 46.72% (L77) | >=20 = 5 | 5 | 5 | PASS |
| A4 ROCE trend | 29.05 vs 9.47 (L77-78) | latest >= earliest = 5 | 5 | 5 | PASS |
| Block A | | | 14 | 14 | PASS |
| B1 cum CFO/PAT | -2,915.97 / 2,537.32 Lakh = -1.15 (L91-93) | <0.50 = 0 | 0 | 0 | PASS (arithmetic re-run: -1.149) |
| B2 FCF+ years | 1 of 4 = 25% (L99-103) | <50 = 0 | 0 | 0 | PASS. The FY23 capex proxy is flagged. The score holds even if FY23 turns negative. |
| B3 cum FCF/PAT | -4,235.80 / 2,537.32 = -1.67 (L104-106) | negative = 0 | 0 | 0 | PASS |
| B4 WC days change | 60.64 to 105.96, +45.32 (L114-117) | increased >15 = 0 | 0 | 0 | PASS (row sums re-run: 45.96+36.84-22.16 = 60.64; 62.74+68.65-25.43 = 105.96) |
| Block B | | | 0 | 0 | PASS |
| C1 revenue CAGR | (268.91/48.59)^(1/5)-1 (L137) | >=20 = 5 | 5 | 5 (40.8%) | PASS |
| C2 PAT CAGR | (18.25/0.08)^(1/5)-1 (L139) | >=20 = 5 | 5 | 5 (~196%) | PASS |
| C3 positive YoY years | 5 of 5 (L144) | 100% = 5 | 5 | 5 | PASS |
| C4 PAT minus rev CAGR | +155pp (L146) | >=+3pp = 5 | 5 | 5 | PASS |
| Block C | | | 20 | 20 | PASS |
| D1 ND/EBITDA | 65.87 / 32.08 = 2.05x (L162) | 2-3x = 1 | 1 | 1 | PASS |
| D2 EBIT/interest | 30.56 / 6.55 = 4.67x (L163) | 3-4.9 = 2 | 2 | 2 | PASS |
| D3 D/E | 1.73x (L165) | >1.5 = 0 | 0 | 0 | PASS |
| D4 current ratio | 1.22 (L167) | 1.2-1.49 = 2 | 2 | 2 | PASS |
| Block D | | | 5 | 5 | PASS |
| E1 promoter holding | 66.97% (L180) | >=60 = 5 | 5 | 5 | PASS (see finding G-M3) |
| E2 3yr change | N/A (L182) | N/A scores 0 (rule 5) | 0 | 0 | PASS |
| E3 pledge | 0% (L187) | 0% = 5 | 5 | 5 | PASS |
| E4 CL/NW | 480.49 / 3,847.74 = 12.49% (L189-191) | 5-15 = 3 | 3 | 3 | PASS |
| Block E | | | 13 | 13 | PASS |
| Core score | 14+0+20+5+13 | | 52 | 52 | PASS |

### 1B. Block F (moat tests)

| Test | Stage score | Rule as written | Recomputed | Result |
|---|---|---|---|---|
| M1 pricing power | 5 | +8.4pp margin AND rev CAGR >=10% = 5 | 5 | PASS. Minor note: L205 states the FY24-26 revenue CAGR as 61.3%. The same inputs give 61.8%, and L242 prints 61.8%. The band does not change. |
| M2 cost advantage | 0 (PEER DATA NEEDED) | peer median missing = 0 | 0 | PASS |
| M3 capital efficiency | 5 | FAT 21.0x >3 AND ROCE 29.05% >20 = 5 | 5 | PASS |
| M4 stickiness | 3 | "max 1 decline year, fully recovered = 3" | 3 | PASS. B01 calls this a judgment call (L219-221, data_notes). It is not one. "Max 1" includes zero decline years, so the 3 band fits the rule text. Downstream stages should not discount M4 as a judgment call. |
| M5 scale | 0 (PEER DATA NEEDED) | | 0 | PASS |
| M6 R&D | 0 (N/A) | R&D not disclosed = 0 | 0 | PASS |
| M7 regulatory | 0 | unregulated = 0 | 0 | FAIL (MINOR, finding G-m1). The score stands. The basis names ten or more listed players from "general industry knowledge", with no anchor (L226-230). That breaks operating rules 4-5. The unregulated band needs no player count. The count reads like the "regulated but >10 players = 1" band, which confuses the reasoning. |
| M8 distribution | 0 | none = 0 | 0 | PASS (resting on the stage's own statement that it found no network disclosure) |
| M9 brand | 0 (PEER DATA NEEDED) | | 0 | PASS |
| M10 switching costs | 3 | 5: grew every year AND receivable days rose <=10. 3: growth all but 1 year AND **stable**. 1: overall growth, 2+ decline years. Else 0. | **0** (1 on the most generous monotone reading) | **FAIL (MAJOR, finding G-M1)** |
| M11 network effects | 5 | latest-window CAGR > prior AND selling % declining = 5 | 5 | PASS. Minor note: the windows labelled "3yr" are 2-year CAGRs (FY21-23, FY24-26). The selling % trend covers FY24-26 only. A 3-year FY23-26 window gives about 50.8% against 27.0%, so the result holds. The construct-fit caveat is a note, not a rule breach. The rule tells the stage to apply the test mechanically. |
| M12 negative WC | 0 | >45 days = 0 | 0 | PASS |
| Block F total | 21 | | **18** | FAIL (follows from M10) |
| moats_confirmed | 5 | score >=3 | **4** (M1, M3, M4, M11) | FAIL (follows from M10) |
| moat_class | STRONG | 4-5 = STRONG | STRONG | PASS (class unchanged) |
| grand_total | 73 | core + moat | **70** | FAIL (follows from M10) |

M10 detail. The receivable-days inputs in B01 run 45.96 (FY24) to 62.74 (FY26), a rise of +16.78 days (L236-238). The 3 band has two conditions: "growth all but 1 year AND stable". The stability condition fails. The top band uses a 10-day tolerance, and M4 uses a +/-10 tolerance, so +16.78 days is not stable on either test. The 1 band needs "2+ decline years", and SUSAN has zero. The only literal outcome is "else 0". Two readings: (a) literal gives 0; (b) a monotone reading gives 1, on the view that zero declines should never score below two declines. Neither reading reaches the "present" threshold of 3. B01 reached 3 by copying its M4 logic across (data_notes 4: "Same rubric-fit gap as M4"). M4's 3 band has no receivables condition. M10's 3 band does. The decision survives: moat_class stays STRONG (4 of 12) and classification stays AVERAGE, because Core 40-59 gives AVERAGE whatever the moat class. The moat count also feeds B07 Section 6C (L443, "5 confirmed"), so B07 carries the error forward.

### 1C. Classification, confidence, deal-breakers, CAGR edge rules

| Rule | Stage output | Rule as written | Result |
|---|---|---|---|
| Data-available opening line | 6 years raw, FY21-26 (L4-10) | "Data available: [X] years..." | PASS (wording differs, content is present) |
| Formula: ROCE from source where given | RHP Annexure 33 ROCE used (L60-65) | source figure first, compute only when absent | PASS |
| Formula: ROE on average net worth | RHP ROE used | fixed formula | PASS. FY26 64.64% fits an average-NW basis. Closing NW gives about 47.4%. A3 is 5 either way. |
| WC days basis stated | revenue basis stated (data_notes 6) | state basis | PASS |
| FCF definition | FY23 investing-outflow proxy, flagged | capex excluding acquisitions | PASS (proxy disclosed, score unaffected) |
| CAGR edge rules | no negative or zero endpoint. No loss-to-profit swing. C4 computed. Base-effect note added. | N/M on a negative endpoint; note any swing | PASS |
| Data confidence tier | 6 years puts SUSAN in the "5-6 lower confidence" band (L265-267) | 5-6 years: flag "may not have seen full cycle" | FAIL (MINOR, G-m2). The report text names the band. The YAML flags[] does not carry the required "may not have seen full cycle" flag, and downstream stages read the YAML. |
| history_downgrade field | `true` (YAML L27) with no tier downgrade applied (L270-273) | downgrade only at 3-4 years (LIMITED) | **FAIL (MAJOR, G-M2)**. Recomputed: `false`. |
| Classification matrix | Core 52 gives AVERAGE | Core 40-59 = AVERAGE | PASS |
| Deal-breakers fired | #2 (Block B 0 <8), #4 (CFO/PAT -1.15 <0.50) | recorded, cap applied | PASS. Not-triggered list re-checked: #1, #3, #5, #6, #7, #8, #9 all correctly not fired. |
| Deal-breaker driving years | YAML deal_breakers give the actual values only | "state WHICH years drive any deal-breaker" | FAIL (MINOR, G-m3). The years are in the Block B prose (FY24-26 negative CFO) but not in the deal_breakers entries. |
| FLAG-GATE0 | 2 flags, classification <= AVERAGE with depressors named | required when <= AVERAGE with depressors | PASS |
| Output format | dashboard, classification, strongest/weakest block and decision line present | "moat profile bars" required | FAIL (MINOR, G-m4). No moat profile bars. |
| PEER DATA NEEDED handling | M2, M5, M9 scored 0 and marked | score 0, never guess | PASS |
| YAML schema | all schema fields present | | PASS |

G-M2 detail. The YAML says `history_downgrade: true`. The report says the 3-4 year downgrade rule "does not" trigger (L271-272), and classification stays at the matrix output, AVERAGE. The field therefore tells downstream stages that a one-tier downgrade was applied. A reader of the YAML alone could infer a GOOD classification before downgrade, which never existed. Two readings: (a) as written, data_years is 6, so the tier is "5-6 lower confidence", no downgrade applies, and the field should be `false`; (b) the ratio-driven blocks (A, half of D) and cash flow (B) rest on only 3-4 years, so the LIMITED tier binds and AVERAGE drops one tier to AVOID. This audit adopts reading (a). The rule keys confidence to years of history available, and B01 itself declares data_years: 6. Reading (b) would flip the classification. If the operator prefers (b), the item becomes CRITICAL. Either way the current state, `true` with no downgrade, matches neither reading. The operator should rule on it.

### 1D. Gate 0 observations (rule outcome unchanged)

- G-m5 (MINOR): E1 uses the pre-listing SHP dated 17-Jun-2026 (L176-179). The text says "per input_gaps", but B01 input_gaps[] lists no missing post-listing SHP (June 2026 quarter). Add the gap line.
- G-m6 (MINOR): M1 CAGR shown as 61.3% (L205). The stated inputs give 61.8%, the figure L242 uses. Internal inconsistency only. Band unchanged.
- G-m7 (MINOR): M11 window labels. The "3yr" windows are 2-year CAGRs. The selling-expense trend covers FY24-26 only. Result unchanged.

Gate 0 tally: 50 rules checked, 6 FAIL (2 MAJOR: M10, history_downgrade; 4 MINOR: M7 anchor, confidence flag, deal-breaker years, moat bars). The Block F total, moats_confirmed and grand_total FAIL rows derive from M10 and are not counted again. Recomputed values: Block F 18 (was 21), moats_confirmed 4 (was 5), grand_total 70 (was 73), history_downgrade false (was true). moat_class STRONG, core 52 and classification AVERAGE are unchanged.

---

## PART 2: EMERGING MOAT (B07) COMPLIANCE

### 2A. Structure and coverage

| Rule | Result | Note |
|---|---|---|
| All six sections plus optionality register present | PASS | Sections 1, 2, 3, 4, 5, register, 6 |
| Section 3: all 22 rows with evidence, type, strength, timing | PASS | Summary table L282-305 |
| Scorecard: all 23 rows (22 + R1) | PASS | L352-376 |
| "NO EVIDENCE FOUND" stated where none, no force-fit | PASS | 16 categories carry 0 |
| Categories 21 (I1) and 22 (I2) present (verifier rule 8) | PASS | Both present, both 0 |
| I1: >0 only with both legs, (b) leg with >=1 documented source | PASS | Leg (a) fails, scored 0, no "management quality" substitute |
| I2: >0 only with a named, specific sacrifice | PASS | Tested against B2, F2, A3, R1. "Nothing must be destroyed" in each case, scored 0 |
| I1/I2 contribution stated separately | PASS | 0.0 (L380) |
| Completionist guard: recount line in the mandated form | PASS | "recount performed: 7 documented items across 5 categories" |
| Completionist guard: active count against base rate | PASS | 5 categories scored >0, well under 12 |
| Not conflated with FTTCP | PASS | Header L2-3 |
| Section 4 (R1): 4A/4B/4C, with "competitors share the benefit" answered | PASS | L319-343 |
| Section 6: 6A-6E, 6C built from the injected Gate 0 block | PASS | 6C carries B01's "5 confirmed". See G-M1: the recomputed count is 4. |
| Optionality register: table in the mandated columns and in the YAML | PASS | 7 rows. HT/MVCC 20-25% margin is registered, not scored. |
| F2: cross-reference to the promise-delivery record | PASS (note) | F2 cites B05's view that the pace is thin (L222-223). The phrase "NO-CONCALL adaptation" (L220) sits oddly beside a Q1 FY27 transcript the report lists as a source (L4). |
| YAML schema complete; em_classification in the enum | PASS | "NONE" |

### 2B. Scoring re-derivation

| Cat | L x I | Raw per matrix | Tier | Mult | Stage adj | Recomputed | Result |
|---|---|---|---|---|---|---|---|
| A3 | M x L | ML = 1 | documented | 1.0 | 1.0 | 1.0 | PASS |
| B2 | H x M | HM = 3 | documented | 1.0 | 3.0 | 3.0 | PASS |
| C2 | M x M | MM = 2 | documented | 1.0 | 2.0 | 2.0 | PASS |
| E1 | L x L | LL = 1 | claim | 0.7 | 0.7 | 0.7 | PASS |
| F2 | M x M | MM = 2 | documented | 1.0 | 2.0 | 1.4 (claim tier) | FAIL (MINOR, E-m2) |
| R1 | H x L | HL = 2 | documented | 1.0 | 2.0 | 2.0 | PASS |
| All others | none | 0 | | | 0 | 0 | PASS |
| Total | | | | | 10.7 | 10.7 as stated; 10.1 with the E-m2 fix | PASS (arithmetic) |
| Band | | | | | <12 NONE | <12 NONE either way | PASS |

E-m2 detail. F2 (execution moat) is credited at the documented multiplier. The document is the Monitoring Agency report, which shows "No" deviation and Rs 1.20 Cr of Rs 10.30 Cr used at 30-Jun-2026 (L216-219). That document shows the IPO money went to its stated purpose. It does not show what F2 looks for: capex delivered on time and on budget across annual reports, or ramp speed after commissioning. The on-time claim, commercial operations in Feb-2027, rests on the RHP plan and on management's restatement at the Q1 FY27 call (L17), which is a claim tier. This is the rule-3 pattern: a category credited at documented weight where the load-bearing part is a claim. Recomputed at 0.7x: F2 = 1.4 and the total = 10.1. The band stays NONE, so the direction is downward and nothing changes. MINOR.

### 2C. Findings

- **E-M1 (MAJOR): capex_embedded_growth_pct does not carry the 2C method.** The rule (Section 2C, and the YAML comment "from 2C") defines the metric as capex under execution x historical fixed asset turnover, expressed as a percentage of current revenue. B07 shows that arithmetic: 10.30 x 21.0 = about Rs 216 Cr, about 80% (L81-89). It then puts 22.8% in the field, taken from a substitute capacity-based cross-check (L99-113). The substitution is transparent and flagged (FLAG-EMOAT 4), and the stage's reasoning is sound: 38.38% of FY26 revenue is asset-light trading, which inflates FAT. The field still breaks the method as written. This field can feed the stage 11 CAPACITY revenue basis, so the swap matters downstream. Recomputed per rule: about 80% on the Rs 10.30 Cr IPO-funded figure the stage used, or about 84% on the Rs 10.81 Cr total project cost it also reports (L63). Two readings: (a) as written, the field is about 80% and 22.8% sits beside it as a labelled cross-check; (b) the operator rules that trading-heavy revenue bases may substitute the capacity method. Until the operator rules, downstream stages should read both numbers from the report, not the YAML field alone. The decision likely survives because the flag sits beside the field.
- **E-m1 (MINOR): anchors.** Rule 3 requires a source anchor on each evidence item. G1, G2 and H1 cite pipeline blocks (B01, B04, B00), not primary documents. The Monitoring Agency report and several transcript items carry no page or question number. No score depends on these items except F2.
- **E-m2 (MINOR): F2 evidence tier.** See 2B.
- **E-m3 (MINOR): evidence count mismatch.** The YAML evidence_mix says documented: 14. The completionist recount says 7 documented items. Neither the report nor the YAML explains the gap. It probably reflects a count across Sections 1-2 against a count of scored categories only. The field should state its basis.

Emerging Moat tally: 30 rules checked, 4 FAIL (1 MAJOR: capex_embedded_growth_pct; 3 MINOR: anchors, F2 tier, evidence count). em_score 10.7 and em_classification NONE stand. With E-m2 applied, em_score is 10.1, still NONE.

---

## PART 3: DEFERRED (PHASE 3)

Valuation (B11) rules 4-7 and 11-15, the Expectation Ledger (rules 13-14) and destination PE recomputation are pending phase 3. The Business Understanding Narrative (rule 9) is pending stage 13, and the Halt 1 dossier (rule 10) is pending /finalize.

## SUMMARY

- Rules checked: 80 (Gate 0: 50; EMoat: 30). Rules passed: 70. Acceptance: 87.5% (phase-1 scope).
- CRITICAL 0 | MAJOR 3 | MINOR 10 (7 FAIL rows plus 3 observations whose rule outcome is unchanged).
- No finding changes a classification. Gate 0 stays AVERAGE, moat_class stays STRONG, and EMoat stays NONE. G-M2 becomes CRITICAL only if the operator adopts reading (b), which would give AVOID.
- REWORK: not triggered. The acceptance rate is above 60%, and Verifier C has no CRITICAL-driven REWORK path. Recommended light fixes: stage 1 sets M10 to 0, history_downgrade to false and adds the confidence flag. Stage 7 carries the 2C mechanical value in capex_embedded_growth_pct, with 22.8% as a labelled cross-check, or the operator rules on the substitution.
