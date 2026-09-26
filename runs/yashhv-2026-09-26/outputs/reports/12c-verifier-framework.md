# STAGE 12 VERIFIER C: FRAMEWORK ADHERENCE, YASHHV, 2026-09-26 (PHASE 1 SCOPE)

Model: claude-opus-5-5. Fresh context.
Scope: Gate 0 (B01) and Emerging Moat (B07) only. The valuation audit (B11, rules 4, 6, 7, 9 to 15) is PENDING PHASE 3. No valuation framework document was read.
Rule sources: prompts/01-gate-0-pipeline.md, prompts/07-emerging-moat-pipeline.md.
Artifacts audited: outputs/reports/01-gate0.md (run 2, corrected), outputs/blocks/B01-gate0.yaml, outputs/reports/07-emoat.md (run 2, corrected), outputs/blocks/B07-emoat.yaml. No other file in outputs/ was read.
This verifier audits rule application. Verifier A owns whether a number exists in the source. Where this report recomputes a value, it recomputes from the inputs the report itself states.

---

## PART 1. GATE 0 (B01) COMPLIANCE

### 1a. Block re-derivation from stated inputs

| Block | Stated | Re-derived | Result | Note |
|---|---|---|---|---|
| A1 median ROCE (FY24-26 exact) | 27.5% = 5 | sorted 41.8/42.3, 20.2, 27.5; median 27.5% = 5 | PASS | see F-G3 on FY24 CE arithmetic |
| A2 min ROCE | 20.2% = 5 | 15569.46L CE, 31.44/155.69 = 20.2% = 5 | PASS | |
| A3 median ROE | 25.9% = 5 | median of 7 stated values = 25.9% = 5 | PASS | FY20 closing-NW basis stated, as the formula requires |
| A4 ROCE trend | -14.8pp = 0 | 27.5 vs 41.8 (corrected CE) = -14.3pp; both >5pp = 0 | PASS | score unchanged |
| Block A | 15 | 15 | PASS | |
| B1 CFO/PAT | 58.50/97.96 = 0.597 = 1 | sums re-added: 58.50, 97.96; 0.597 = 1 | PASS | |
| B2 FCF+ years | 5/7 = 71.4% = 2 | 71.4% = 2 (60% ex-proxy, same band) | PASS | |
| B3 FCF/PAT | -67.15/97.96 = 0 | FCF sum re-added -67.15; negative = 0 | PASS | |
| B4 WC days | 79.1 to 118.9 = 0 | 47.4 + 103.4 - 31.9 = 118.9; +39.8 days = 0 | PASS | FY22 used as earliest because FY20-21 payables NOT FOUND; stated |
| Block B | 3 | 3 | PASS | |
| C1 Rev CAGR | 35.6% = 5 | (235.16/37.85)^(1/6) - 1 = 35.6% = 5 | PASS | |
| C2 PAT CAGR | 53.9% = 5 | (37.34/2.81)^(1/6) - 1 = 53.9% = 5 | PASS | |
| C3 +YoY years | 5/6 = 3 | 83.3% = 3 | PASS | |
| C4 PAT minus Rev CAGR | +18.3pp = 5 | +18.3pp = 5 | PASS | |
| Block C | 18 | 18 | PASS | |
| D1 ND/EBITDA | 0.31x = 4 | 17.49/56.71 = 0.31x = 4 | PASS | |
| D2 IC | 13.58x = 5 | 54.05/3.98 = 13.58x = 5 | PASS | |
| D3 D/E | 0.204 = 4 | 37.55/184.00 = 0.204 = 4 | PASS | |
| D4 CR | 1.96x = 4 | 13,243.43/6,770.80 = 1.956x = 4 | PASS | |
| Block D | 17 | 17 | PASS | |
| E1 promoter | 57.94% = 4 | 1,65,43,595/2,85,51,249 = 57.94% = 4 | PASS | |
| E2 3-yr change | -21.5pp = 0 | 79.48% to 57.94%; decreased >3% = 0 (N/A path also scores 0) | PASS (score) | see F-G6 on the cause note |
| E3 pledge | 0% = 5 | 5 | PASS | |
| E4 CL/NW | 0.44% = 5 | 0.805/184.00 = 0.44% = 5 | PASS | capital commitments correctly excluded |
| Block E | 14 | 14 | PASS | |
| Core | 67 | 15+3+18+17+14 = 67 | PASS | |

### 1b. Moat tests (Block F)

| Test | Stated | Rubric check | Result |
|---|---|---|---|
| M1 | 5 | EBITDA margin 15.9% to 24.1% (+8.2pp), rev CAGR 35.6% | PASS |
| M2 | 0, PEER DATA NEEDED | rule followed | PASS |
| M3 | 5 | FAT 4.54x >3x, ROCE 27.5% >20% | PASS |
| M4 | 3 | one decline year (FY21), recovered | PASS |
| M5 | 0, PEER DATA NEEDED | rule followed | PASS |
| M6 | 0 | R&D/Rev 0.43% FY26, 0.74% FY25, below 1% | PASS |
| M7 | 0 | unregulated per evidence | PASS |
| M8 | 0 | rubric: "mentioned unquantified = 1". Distribution/agency agreements (Weidmann, Electrolink, Ensales) are in the AR front matter per B07 | FAIL (MINOR), recomputed 1 |
| M9 | 0, PEER DATA NEEDED, GM proxy stated | rule followed | PASS |
| M10 | 3 | growth all but 1 year; receivable days fell 20.2 (rubric caps a rise, not a fall) | PASS |
| M11 | 5 | 3-yr CAGR 37.5-37.6% > prior 33.7%; ratio falling 9.3% to 7.5% | PASS (mechanical); proxy label gap, see F-G5 |
| M12 | 0 | WC days >45 every year | PASS |
| Moat score | 21/60 | re-added 21; with M8 = 1, 22/60 | FAIL (MINOR), recomputed 22 |
| Moats present | 5, STRONG | M8 at 1 is below the 3 presence line; still 5, STRONG | PASS |

### 1c. Classification, confidence, deal-breakers, CAGR edge rules

| Rule | Result | Note |
|---|---|---|
| Data-years opener stated | PASS | "Data available: 7 years (FY20 to FY26)" |
| Data confidence tier (7-9 = moderate, no downgrade) | PASS | ROCE sub-window of 3 years disclosed. It does not trigger the tier rule, which keys to history available. |
| Classification matrix: Core 67 + STRONG = GOOD+ | PASS | |
| Deal-breaker #2 (Block B 3 < 8) caps at GOOD; years named (FY25, FY26) | PASS | all nine deal-breakers tested, each with its value |
| Deal-breaker #4 (CFO/PAT 0.597 >= 0.50) | PASS | 0.097 above the line; correctly not triggered |
| CAGR edge rules (no negative endpoints; no loss-to-profit swing) | PASS | noted in data_notes |
| FLAG-GATE0 requirement | PASS | not required: classification GOOD is above AVERAGE |
| Grand total 88 | PASS on stated moat score; 89 if F-G4 accepted | no classification effect |
| YAML schema and consistency with report | PASS | analyst_note under 200 words |

### 1d. Gate 0 findings

| ID | Severity | Rule | Finding | Recomputed |
|---|---|---|---|---|
| F-G1 | MINOR | Rule 5 (grounded, N/A scores 0) | FY20-21 capex is still proxied by screener "Cash from Investing Activity". The formula defines capex as purchase of PPE plus intangibles and says do not substitute. The proxy is disclosed and has no score effect (B2 = 2, B3 = 0 either way). | none |
| F-G2 | MINOR | Rule 4 (anchors mandatory) | E4 anchor carries an unfilled placeholder: "AR FY26 Note 37, [page in extracted text]". Several anchors use bracketed page guesses ("p.[103]", "p.[145]", "RHP p.[273]"). | fill the page numbers |
| F-G3 | MINOR | Block A re-derivation | FY24 CE is stated as 47.13 Cr. The report's own inputs give 7,117.73L - 2,346.98L = 4,770.75L = 47.71 Cr. ROCE FY24 = 19.92/47.71 = 41.8%, not 42.3%. A4 trend becomes -14.3pp. A1, A2, A4 scores unchanged. | FY24 ROCE 41.8%; A4 -14.3pp, score 0 |
| F-G4 | MINOR | M8 rubric | Scored 0 as "not in provided data". The rubric band "mentioned unquantified = 1" fits the agency and distribution agreements disclosed in the AR (per B07 anchors, AR p.5; Ensales Reg 30 filing). No moat-presence or classification change. | M8 = 1; moat 22/60; grand total 89 |
| F-G5 | MINOR | M11 rubric, data_notes proxy rule | M11 tests "selling exp %". The report uses "Selling & admin expense", a broader line. The substitution is not listed in data_notes as a proxy basis. Score 5 likely survives. | label the proxy |
| F-G6 | MINOR | Rule 2/5 (grounded, no qualitative judgment) | The E2 note states "CAUSE FOUND" and "not an ongoing... sell-down". Two gaps: (1) the promoter count fell 10,60,000 shares, but the RHP OFS was up to 11,30,000; a 70,000-share gap stays unexplained. (2) "No further sell-down since listing" rests on the 30-Sep-2025 and 31-Mar-2026 patterns only. The window from listing (19-Dec-2024) to 30-Sep-2025 is not observed. The score (0) is unaffected. The note overstates what the evidence proves and feeds the Role 2 promoter read. | reword to "consistent with the RHP OFS; 70,000-share gap and Dec-2024 to Sep-2025 window NOT VERIFIED" |

Gate 0: 19 rules checked, 6 fails, all MINOR. No score change moves a block band that alters Core (67), moat class (STRONG) or classification (GOOD).

---

## PART 2. EMERGING MOAT (B07) COMPLIANCE

### 2a. Structure and category coverage

| Rule | Result | Note |
|---|---|---|
| All six sections plus optionality register present | PASS | 1A-1C, 2A-2D, Section 3, 4A-4C, Section 5, register, 6A-6E |
| 22 categories + R1 = 23 rows addressed, NO EVIDENCE stated where absent | PASS | 23 rows in both the Section 3 summary and Section 5 table |
| Categories 21 (I1) and 22 (I2) present (verifier rule 8) | PASS | both scored 0 with the two-leg (I1) and named-sacrifice (I2) tests shown |
| I1/I2 contribution stated separately | PASS | 0.0, no threshold crossing |
| Taxonomy note (not FTTCP) | PASS | |

### 2b. Scoring mechanics

| Row | L x I | Raw | Tier | Mult | Adj | Check |
|---|---|---|---|---|---|---|
| A3 | MM | 2 | DOC | 1.0 | 2.0 | PASS |
| A4 | ML | 1 | DOC | 1.0 | 1.0 | PASS |
| B1 | HH | 4 | DOC | 1.0 | 4.0 | PASS. Taxonomy lists "plant under construction" as documented. Tech transfer (MGMT) not scored. |
| B2 | MM | 2 | DOC | 1.0 | 2.0 | PASS on mechanics; see F-E1 |
| C1 | ML | 1 | DOC | 1.0 | 1.0 | PASS |
| E2 | HM | 3 | DOC/MGMT | 1.0 | 3.0 | PASS. Scored legs (signed agreements, audited export growth) are DOC. The MGMT 20% target is not the scored leg. |
| F2 | MM | 2 | DOC | 1.0 | 2.0 | PASS |
| H2 | HL | 2 | DOC | 1.0 | 2.0 | PASS. Run-1 double credit with E2 removed. |
| R1 | LM | 1 | MGMT | 0.7 | 0.7 | PASS |
| Total | | | | | 17.7 | PASS, re-added 17.7 |
| Band | 12-24 | | | | MODEST | PASS |

No MGMT-only category is scored at the DOC multiplier. Matrix values (HH=4, HM=3, MM/HL=2, ML/LM=1) match the rubric.

### 2c. Completionist guard, evidence mix, arithmetic, combined assessment

| Rule | Result | Note |
|---|---|---|
| Completionist guard (12+ active triggers re-examination) | PASS | 9 non-zero rows, 6 Strong/Moderate |
| Recount line present | PASS (presence) | |
| One evidence, one credit (recount "no item counted in two categories") | FAIL (MINOR) | F-E1 |
| evidence_mix item counts | FAIL (MINOR) | F-E2 |
| Source anchors on every evidence item | FAIL (MINOR) | F-E3 |
| 2C prescribed formula run and shown | PASS | 153 x 4.54 = 694.6 Cr = 295% of 235.16 Cr; caveat attached |
| 6C uses the injected Gate 0 block | FAIL (MINOR) | F-E4 |
| 6D combined classification | PASS | The "standard matrix" is named but not defined in prompts/07. The GOOD + MODEST = GOOD reasoning is internally consistent. Not re-derivable from the rule source. |
| Optionality register present, in YAML | PASS | see observation O-1 |
| A1 zero reasoning | FAIL (MINOR) | F-E5 |
| M10 confirm / M11 override handled | PASS | 6C moat count 16/60, 4 present, STRONG, consistent with override |
| YAML schema, enum values, analyst_note length | PASS | em_classification "MODEST" in enum; note under 200 words |

### 2d. Emerging Moat findings

| ID | Severity | Rule | Finding | Recomputed |
|---|---|---|---|---|
| F-E1 | MINOR | One evidence, one credit (recount rule, CLAUDE.md) | B2 credits "550kV test infrastructure under construction at Vadodara" as a separate documented item. The report's own 1A row places the 550 kV testing infrastructure inside the Rs153 Cr Vadodara capex (Board's Report; concall May-2026 line 602), which B1 already credits. The recount line "no item counted in two categories" is therefore false for this item. B2 keeps two independent legs (IEEE US, CENELEC Europe), so MM = 2 likely survives. | recount 13 unique documented items, not 14; em_score unchanged 17.7 |
| F-E2 | MINOR | evidence_mix (item counts) | evidence_mix documented: 14 counts only the six Strong/Moderate categories. Documented items in scored Weak rows are omitted: A4 (5% new-product revenue, AR p.63; SKU launches, AR p.5), C1 (retrofit Rs16.0 Cr, AR p.69; 150+ customers, AR p.28), and E2's "13 new export geographies". | documented count understated by about 5; no score effect |
| F-E3 | MINOR | Rule 3 (anchors on every evidence item) | Many items cite "Board's Report" with no page (1A rows, B2 legs, catalyst "Board's Report, AR"). Some cite other stages ("B03", "B05") instead of the primary page. | add AR page numbers |
| F-E4 | MINOR | 6C (injected Gate 0 block) | 6C shows Core 70 (B01 run 1). The current B01 (run 2) states Core 67. Both sit in the 60-79 band, so GOOD holds. The artifact pair is out of sync. | Core 67 |
| F-E5 | MINOR | Evidence taxonomy, Section 5 multipliers | A1 is zeroed by importing I1's leg (a) bar ("a bare claim, unconfirmed, scores 0"). That bar is specific to Family I. Section 5 scores MGMT-only evidence at 0.7x. The zero holds on a different ground: "12-13 global makers" is an existing-state fact, not a forming moat (the test applied to E1). Worst case if scored: 0.7, total 18.4, still MODEST. | cite the existing-vs-emerging ground |

Observation O-1 (prompt, not stage): prompts/07 says the register holds items "scored 0 or rest only on MGMT/INF evidence" and "never scored". Section 5 also scores MGMT-only rows at 0.7x. R1 sits in both places, as the prompt permits. The B1 and B2 register rows are read as conversion milestones on scored categories. This ambiguity belongs to the prompt. No finding against B07.

Emerging Moat: 17 rules checked, 5 fails, all MINOR. em_score 17.7 and MODEST hold under every recomputation.

---

## PART 3. VALUATION (B11)

PENDING PHASE 3. Rules 4, 6, 7, 9 to 15 are not run in this scope. Expectation-ledger and Business Understanding Narrative fields are left pending.

---

## SUMMARY

Rules checked 36. Passed 25. Failed 11, all MINOR. Acceptance rate 25/36 = 69.4%. Denominator is 4 or more, so the rate applies. It is above the 60% REWORK line.
No finding changes Core (67), moat class (STRONG), Gate 0 classification (GOOD), em_score (17.7), EM class (MODEST) or combined assessment (GOOD).
Run-1 CRITICAL CR-1 (E2/H2 double credit) is confirmed fixed. Run-1 MJ-1, MJ-2, MJ-3 and MJ-4 are confirmed addressed. F-E1 is a smaller recurrence of the MJ-1 pattern (Vadodara capex evidence split across B1 and B2). F-G6 is a residual of MJ-3.
Recommended REWORK: none. The fixes are optional touch-ups at next edit: F-G3, F-G6, F-E1, F-E4.

```yaml
stage: B12c
company: "YASHHV"
run_date: "2026-09-26"
model: "claude-opus-5-5"
status: complete
scope: "phase 1 (Gate 0 + Emerging Moat); valuation audit pending phase 3"
gate0: {rules_checked: 19, fails: ["F-G1 MINOR FY20-21 capex proxied by CFI against the fixed capex formula; no score effect", "F-G2 MINOR E4 anchor placeholder '[page in extracted text]' and bracketed page guesses", "F-G3 MINOR FY24 CE 47.13 stated vs 47.71 from stated inputs (7117.73L-2346.98L); FY24 ROCE 41.8% not 42.3%; A4 -14.3pp, score 0 unchanged", "F-G4 MINOR M8 scored 0; rubric 'mentioned unquantified = 1' fits disclosed agency agreements; moat 22/60, grand total 89, class unchanged", "F-G5 MINOR M11 uses selling-and-admin ratio for 'selling exp %' without a data_notes proxy label", "F-G6 MINOR E2 note overclaims 'CAUSE FOUND/not ongoing': 70,000-share gap vs 11,30,000 OFS unexplained; listing to 30-Sep-2025 window unobserved"]}
emoat: {rules_checked: 17, fails: ["F-E1 MINOR 550kV test infra (inside Rs153cr Vadodara capex credited in B1) also counted as a B2 documented item; recount 13 not 14; score unchanged", "F-E2 MINOR evidence_mix documented=14 omits documented items in scored Weak rows A4, C1 and E2 export-geography count", "F-E3 MINOR 'Board's Report' anchors without page; secondary-stage anchors (B03/B05)", "F-E4 MINOR 6C carries B01 run-1 Core 70; current B01 Core 67; band and GOOD unchanged", "F-E5 MINOR A1 zeroed by importing the Family I leg-(a) bar; valid ground is existing-vs-emerging; worst case 18.4, still MODEST"]}
valuation: {rules_checked: 0, fails: []}   # PENDING PHASE 3
expectation_ledger: {present: false, downside_row: false, all_rows_confirm_by: false, all_rows_metric_threshold: false, prob_in_range: false, decay_status_valid: false, off_ledger_credit: false, residual_pct_cmp: 0, residual_starter_cap_ok: true, fails: []}  # PENDING PHASE 3, not audited
business_understanding_narrative: {present: false, five_questions_answered: false, prose_only: false, section6_candidates_named: 0, valuation_vocab_leak: false, fails: []}  # PENDING PHASE 3 / finalize, not audited
recomputed_destination_pe: ""
recomputed_decision: ""
findings:
  - {id: F-G1, severity: MINOR, location: "01-gate0.md Block B capex FY20-21", rule: "Gate 0 rule 5 / capex formula", recomputed: "none (B2=2, B3=0 either way)"}
  - {id: F-G2, severity: MINOR, location: "01-gate0.md E4, Block B/B4 anchors", rule: "Gate 0 rule 4 anchors", recomputed: "fill page numbers"}
  - {id: F-G3, severity: MINOR, location: "01-gate0.md Block A table FY24", rule: "ROCE formula re-derivation", recomputed: "CE 47.71cr, ROCE 41.8%, A4 -14.3pp, score 0"}
  - {id: F-G4, severity: MINOR, location: "01-gate0.md M8", rule: "M8 rubric band 1", recomputed: "M8=1, moat 22/60, grand 89, STRONG, GOOD"}
  - {id: F-G5, severity: MINOR, location: "01-gate0.md M11, data_notes", rule: "proxy basis disclosure", recomputed: "label selling-and-admin as proxy"}
  - {id: F-G6, severity: MINOR, location: "01-gate0.md E2 note, B01 data_notes", rule: "Gate 0 rules 2 and 5 grounded claims", recomputed: "reword to consistent-with-OFS; gaps NOT VERIFIED"}
  - {id: F-E1, severity: MINOR, location: "07-emoat.md B2, recount line", rule: "one evidence one credit", recomputed: "recount 13; em_score 17.7 unchanged"}
  - {id: F-E2, severity: MINOR, location: "B07 evidence_mix", rule: "evidence_mix item counts", recomputed: "documented about 19, not 14"}
  - {id: F-E3, severity: MINOR, location: "07-emoat.md 1A, B2, catalysts", rule: "B07 rule 3 anchors", recomputed: "add AR pages"}
  - {id: F-E4, severity: MINOR, location: "07-emoat.md 6C", rule: "6C injected Gate 0 block", recomputed: "Core 67"}
  - {id: F-E5, severity: MINOR, location: "07-emoat.md A1", rule: "Section 5 multipliers / Family I scope", recomputed: "zero holds on existing-vs-emerging ground; worst case 18.4 MODEST"}
critical_count: 0
major_count: 0
minor_count: 11
acceptance_rate: 69.4
```
