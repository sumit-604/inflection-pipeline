# Verifier summary, KPL run 2026-11-15 (phase 1)

## Confidence delta (phase 1)

| Component | Value | Basis |
|---|---|---|
| numerical_acceptance | 99 | B12a: 390 numbers checked; mandatory tier 55 of 55; 0 CRITICAL, 0 MAJOR, 3 MINOR; 5 false positives struck; no source fidelity finding |
| redflag_coverage | 63 | B12b: 19 MATERIAL items (2 CRITICAL, 17 MAJOR) on an independent list of 32; 12 caught, 6 partly caught, 1 missed. Counting partials as caught gives 18 of 19 = 95% |
| framework_adherence | 86 | B12c phase 1 scope: 69 of 80 rules passed (Gate 0 53 rules, Emerging Moat 27 rules) |
| peer_utilisation | 90 | B12d: 9 of 10 peer transcripts used substantively; 1 cited only (LINCOLN Q4 FY24, stale) |
| overall | 63 | min of applicable components; set by redflag_coverage; band 60-74 |

Not applicable: none. Pending: the framework_adherence valuation component (B10, B11), deferred to phase 3.

## Acceptance rates

| Verifier | Model | Scope | Acceptance rate | CRITICAL | MAJOR | MINOR |
|---|---|---|---|---|---|---|
| A, numerical | claude-sonnet-5-5 | 390 numbers; 55 of 55 mandatory | 99 | 0 | 0 | 3 |
| B, red flags | claude-opus-5-5 | 32 independent items, 19 material | 63 | 0 | 7 | 12 |
| C, framework | claude-opus-5-5 | Gate 0 + Emerging Moat only | 86 | 0 | 1 | 10 |
| D, peers | claude-sonnet-5-5 | 10 peer transcripts | 100 | 0 | 0 | 3 |

Scope notes, as the verifiers wrote them:

- Verifier A: no MISMATCH, no ANCHOR NOT FOUND, no material UNANCHORED. Not checkable against the PDFs supplied: web figures in the promoter stage (registrationwala, Tofler, Trendlyne, DRAP recall alert, ValuePickr, AmbitionBox) and the market stage (IMARC, EMR, Pharmexcil, RBI, Towards Healthcare, EPO and hormone pools, India exports); the Step 1 brief P/E 41.1x; the 28-32 and 24-26 percent registration type EBITDA figures. Not opened: Q4 FY26 results PDF, the Caplin Q3 FY26 and Senores Q1 FY27 calls, the Lincoln calls.
- Verifier B: both CRITICAL items on its own list (F1 auditor evasion, F2 Middle East debtor evasion) were caught upstream, so it raises no CRITICAL against the pipeline. Credibility grade concurrence: "lower: C". Promise delivery spot checks: 5 checked, 4 confirmed, 1 wrong.
- Verifier C: the valuation half (B10, B11), the expectation ledger (rules 13-14) and the business understanding narrative check (rule 9) are PENDING phase 3 and /finalize. Rule 8 checked: Emerging Moat categories 21 and 22 present and scored 0 correctly. Concurrence: Gate 0 GOOD on the most evidenced reading; Emerging Moat class NONE (recomputed 11.6-11.9).
- Verifier A shadow: not run in this session (the single shadow run is assigned to the TD Power session).

## Findings, sorted by severity

### CRITICAL

None from any verifier.

### MAJOR

| Verifier | Target | Location anchor | Note |
|---|---|---|---|
| B | B05 | KPL-May [page 6], [page 8], [page 17], [page 21]; KPL-Aug [page 13], [page 18], [page 19] | MISSED F4: FY29 1,000 Cr guide composition; management downside ex-biologics 800-850 Cr; FY30 include/exclude contradiction |
| B | B05, B06 | KPL-Aug [page 4]-[page 5], [page 7]; CAP-May26 [page 5], [page 17]-[page 18]; SEN-Jul26 [page 15]-[page 16]; LIN-Feb26 [page 6] | PARTIALLY CAUGHT F5: registrations 2-3 a quarter vs 60-70 in three quarters; 1.5-2 million each fails under rupee (9-14 Cr a year vs 197-217 Cr FY27 increment, derived) and dollar (90-140 million USD, peers far lower) readings; B06 Q4 rupee reading untested |
| B | B06 | KPL-Aug [page 5]; CAP-Nov25 [page 5], [page 10]; CAP-May26 [page 6]; CAP-Aug26 [page 3]; SEN-Jul26 [page 12] | PARTIALLY CAUGHT F6: 'very less competition' in LATAM vs Caplin and Senores entering Mexico; B06 Q5 omits it |
| B | B05, B06 | KPL-May [page 15], [page 17]-[page 18]; KPL-Aug [page 11]; CAP-May26 [page 16] | PARTIALLY CAUGHT F8: Q4 FY26 gross margin war excuse contradicts same-call 'not much increase... API prices' and Caplin COGS rise under 2% |
| B | B05 | KPL-May [page 12]; KPL-Aug [page 3]-[page 4] | PARTIALLY CAUGHT F11: May called the EPO trial 'proceeding'; Aug shows pre-clinical just done and trials starting Nov-Dec 2026; B05 drops the 'Q4 of the next calendar year' self-correction, overstating the registration slip |
| B | B05 | KPL-May [page 4], [page 9]; KPL-Aug [page 15] | PARTIALLY CAUGHT F12: oncology headroom told to market (25-35% utilised) walked back to 65% then 75-80%; filed as industry intelligence; not linked to the oncology cut |
| B | B05 | KPL-May [page 8], [page 13], [page 18]; KPL-Aug [page 19] | PARTIALLY CAUGHT F20 and spot check wrong: 2A row 21 counts German registrations as partial with no evidence; corrected tally 9 delivered, 6 partial, 5 missed, 2 open; Aug FY28 Europe timing and May unfiled-registration claim unused |
| C | B01 (C-G03) | 01-gate0.md Block A; Gate 0 formula definitions (ROCE fixed, no substitutes; rule 5 NOT FOUND = 0) | ROCE computed on (NW + borrowings) for all 10 years, not the fixed EBIT / (TA - CL). Formula basis shown only FY25 23.0% and FY26 27.4% (proxy 17.0%, 21.7%). Mixed basis keeps Block A 13, core 61, GOOD; rule-5 NOT FOUND reading gives Block A 4, core 52, AVERAGE. Separating observation: TA and CL (or screener ROCE) for >= 3 years in the corpus. Decision effect: survives on most evidenced reading; decision-changing only if the corpus holds no TA and CL for >= 3 years |

### MINOR

| Verifier | Target | Location anchor | Note |
|---|---|---|---|
| A | B04 | 04-bizmodel.md analyst_note and B04 yaml (FY26 tax rate 24.7%) | Unlabelled standalone/consolidated mix in the denominator: 8,949.27 is STANDALONE PBT (AR p.30); consolidated PBT is 8,949.21 (AR p.188). Ratio is 24.75% either way; no decision effect. UNANCHORED (basis) under rule 5a; source_fidelity false |
| A | B05 | 05-concall.md trigger 3 kill_signal and B05 yaml (PAT guide cut to about 111-116 Cr) | From the report's own stated inputs the range reproduces as 113.8 to 116.3 Cr; the lower end 111 does not reproduce. Derived figure with unstated inputs at its low end; labelled derived and [INFERENCE]; source_fidelity false |
| A | B07 | 07-emoat.md anchors 'May call p.15', 'May call p.17', 'May call p.21', 'Aug call p.10' | Statements exist; on the [page N] markers they sit on May p.16, p.18, p.22 and Aug p.11 (footer = marker minus 1). Mixed page numbering convention, not stated in B07; anchor imprecise by one page; source_fidelity false |
| B | B05 | KPL-May [page 19]; KPL-Aug [page 16] | Auditor: Aug CFO misquotes his May timeline ('I told that in Q3 or Q4') vs May 'next quarter' |
| B | B05 | KPL-May [page 3]; KPL-Aug [page 9] | Aug reuses May 208-day cash conversion cycle as a debtor-day base |
| B | B05 | KPL-May [page 10] | 4D #9 OVERSTATED: BE margin fade quoted without the same-answer replacement mechanism |
| B | B06 | CAP-May26 [page 14] | Q2 attributes 'not your core market' to Caplin; analyst Richa said it |
| B | B06 | KPL-Aug [page 7]; CAP-Nov25 [page 5]; SEN-Oct26 [page 17] | FLAG-APPROVAL-SHARE-LOW OVERSTATED: KPL FY26 cohort ratio vs peer cumulative ratios; Caplin count includes partners |
| B | B06 | CAP-Feb26 [page 3]; CAP-May26 [page 7], [page 15], [page 18]; LIN-May24 [page 10]; LIN-Feb26 [page 6], [page 8] | FLAG-REGULATED-MARGIN-CONDITIONAL and cross-peer hypothesis OVERSTATED: Caplin Steriles is an ANDA owner at 30% vs group 38-39%; Lincoln does not attribute its guide change to Canada CDMO; Senores leg holds |
| B | B05 | KPL-Aug [page 8], [page 13], [page 15], [page 18] | PARTIALLY CAUGHT F19: hormone revenue told four ways in one call; only 150-200 recorded |
| B | B05 | KPL-Aug [page 12] | MISSED F25: 500 L bioreactor approval gap (deck shows expansion complete; only 100 L CDSCO-approved, 500 L approval awaited) |
| B | B05 | KPL-May [page 3], [page 11] | MISSED F27: 30% vs 40% receivables recovered |
| B | B05, B06 | KPL-Aug [page 17]; CAP-Aug26 [page 13]; SEN-Oct26 [page 16]-[page 17]; LIN-Feb26 [page 7] | MISSED F28: 'revenue immediately' from oncology expansion vs audits and peer timelines of 3-12 months |
| B | B06 | KPL-Aug [page 9]; CAP-Feb26 [page 16]; CAP-Nov25 [page 17] | PARTIALLY CAUGHT F29: Keytruda first-wave claim not tested against Caplin second-wave view and Chinese biosimilar density |
| B | B06 | LIN-Feb26 [page 7]; KPL-May [page 13] | PARTIALLY CAUGHT F30: Lincoln 'Germany was full' not tied to KPL German registration claim |
| C | B01 (C-G06) | 01-gate0.md Block B; Gate 0 formula definitions (FCF = CFO - capex excluding acquisitions) | FCF on CFO + CFI proxy FY17-FY24. FY25/FY26 cross-checks keep sign. B2/B3 for FY17-FY24 undetermined; GOOD holds on any Block B value |
| C | B01 (C-G39) | 01-gate0.md M5; Block F rule (peer data not provided = 0, PEER DATA NEEDED) | M5 scored 1 on a 4-name peer set with segment rank not evidenced. Recomputed M5 0, moat 18, grand total 79, MODERATE unchanged |
| C | B01 (C-G52) | 01-gate0.md fenced YAML vs outputs/blocks/B01-gate0.yaml | Report copy and block file differ in four text fields (input_gaps, deal_breakers, data_notes pointer, analyst_note). Scored fields match |
| C | B01 (C-G53) | 01-gate0.md E4; Note 34 GST items | E4 numerator gap (Rs 6.30 Cr + Rs 30.26 Cr inside or outside Rs 36.98 Cr) absent from input_gaps/data_notes. If outside: 22.3%, E4 1, Block E 10, core 59, AVERAGE, FLAG-GATE0 due. Presentational; class-sensitive; Note 34 read decides |
| C | B07 (C-E03) | 07-emoat.md A4 recount item; Section 2D | BE capitalisation Rs 4.34 Cr anchored 'AR via B03' with no AR page; Unit 6 CWIP 'via B03'; Section 2D items untagged. Recount 10, or 9 if the B03 route lacks an AR page. No score change |
| C | B07 (C-E10) | 07-emoat.md R1; Section 5 multiplier | R1 typed '📄 (2) and 🎙️' but scored 0.7 with no reason. Recomputed R1 2.0, total 10.9, NONE holds |
| C | B07 (C-E11) | 07-emoat.md G1, G2 | G1 scored 1.0 with core tests failed while G2 scored 0 with two indicators present. Same bar: G2 0.7-1.0 (total 11.0-11.3) or G1 0 (total 9.3). NONE holds |
| C | B07 (C-E12) | 07-emoat.md Section 3 labels; B07 active_categories | A4 labelled Moderate at raw 2 / adjusted 1.4 while E1, H2, R1 labelled Weak at the same score; active_categories inconsistent (B2 only, or five rows). Guard not triggered |
| C | B07 (C-E19) | 07-emoat.md analyst_note; Optionality Register | Report says pipeline items are 'in the register, not the score', but A4, R1, E1, H2 score 1.4 each (5.6 of 10.3) on registered items. Score stands under the 0.7x rule; statement wrong. Strict reading total 7.5, NONE holds. Forward double-credit risk at stage 11 (F-1) |
| C | B07 (C-E27) | B07 evidence_mix | Claim 9 and inference 3 do not reconcile with report tags (>= 14 🎙️ items; >= 8 🔍 items); counting basis not stated. Documented 10 reconciles |
| D | B06 | LINCOLN-Concall_Feb_2026_Transcript.txt lines 422-428 (page 10-11 boundary) | Lincoln INR 5-7 Cr a year registration spend not used in Q4 or Q8 |
| D | B06 | SENORES-Concall_Aug_2026_Transcript.txt lines 524-529 | Senores Apnar utilisation 80-90% not used in Q6 context |
| D | B06 | 06-peers.md Q8 verdict | Q8 PARTIALLY VERIFIED margin-gap leg rests on one peer (Senores, not assigned); both assigned peers give no gap. Verdict cap is right; wording should say single-peer on margin gap |

## Verifier C forward flags (phase 1)

| ID | Applies at | Note |
|---|---|---|
| F-1 | stage 11 Pillar 3 | em_score already credits R1/A4/E1/H2 for items also in catalysts_12m (Unit 6 licence, EPO, Pembrolizumab, BE dossiers, EU MAs); no second credit as catalyst proximity |
| F-2 | Halt 1 | Gate 0 core 61, line 60. Downside routes to AVERAGE: ROCE rule-5 reading (52), E4 composition (59), B1 knife-edge (59, Rs 2.02 Cr CFO headroom) |
| F-3 | operator ruling candidate | Mixed-tier multiplier rule absent in prompts/07 Section 5; decides NONE (10.3; recompute 11.6-11.9) vs MODEST (12.4-13.4) on this name |
| F-4 | Verifier A pointers | B1 headroom Rs 2.02 Cr; C1 0.11pp under 20%; D1 0.07x over 1.0x; Note 34 sum 36.56 vs 36.98; FAT 3.23x (B01, 155.57) vs 3.35x (B07, 150) |

Verifier C valuation half: PENDING phase 3 (stages 10 and 11 not run).
