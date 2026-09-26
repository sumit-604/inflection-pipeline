# STAGE 12 VERIFIER C: FRAMEWORK ADHERENCE, YASHHV (run 2026-09-26)

Scope: PHASE 1 only. Gate 0 (B01) and Emerging Moat (B07) audits.
Valuation audit (B10/B11, rules 4-7 and 9-15) is NOT RUN. It is pending phase 3.
No valuation framework document was loaded.

Rule sources read:
- prompts/01-gate-0-pipeline.md (Gate 0 thresholds, formulas, CAGR edge rules, matrix, deal-breakers)
- prompts/07-emerging-moat-pipeline.md (22-category scan plus R1, scoring matrix, multipliers, bands, completionist guard)

Artifacts audited:
- runs/yashhv-2026-09-26/outputs/reports/01-gate0.md and blocks/B01-gate0.yaml
- runs/yashhv-2026-09-26/outputs/reports/07-emoat.md and blocks/B07-emoat.yaml

Method: every block score re-derived from the inputs the report states, against the thresholds in the rule source.
Raw source numbers are not re-checked here. Verifier A owns source fidelity.
All arithmetic below uses the figures B01/B07 print, with the B01/B07 line cited.

---

## PART 1: GATE 0 (B01) COMPLIANCE

### 1.1 Block scores re-derived

| Rule | B01 input (B01 line) | Threshold band | B01 score | Recomputed | Result |
|---|---|---|---|---|---|
| A1 median ROCE | 31.9% (01-gate0.md L41) | >=25 = 5 | 5 | 5 | PASS |
| A2 min ROCE | 20.2% FY25 (L44) | >=15 = 5 | 5 | 5 | PASS |
| A3 median ROE | 25.9% (L58) | >=20 = 5 | 5 | 5 | PASS |
| A4 ROCE trend | FY26 27.5% vs FY20 28.3% (L60) | see finding MJ-2 | 3 | 0 | FAIL |
| B1 cum CFO/PAT | 58.50 / 97.96 = 0.597 (L106) | 0.50-0.69 = 1 | 1 | 1 | PASS |
| B2 FCF-positive years | 5/7 = 71.4% (L109) | 50-74 = 2 | 2 | 2 | PASS |
| B3 cum FCF/PAT | -67.15 / 97.96 = -0.686 (L112) | negative = 0 | 0 | 0 | PASS |
| B4 WC days change | 79.1 FY22 to 118.9 FY26, +39.8 (L135) | >15 up = 0 | 0 | 0 | PASS |
| C1 revenue CAGR | (235.16/37.85)^(1/6)-1 = 35.6% (L152) | >=20 = 5 | 5 | 5 | PASS |
| C2 PAT CAGR | (37.34/2.81)^(1/6)-1 = 53.9% (L154) | >=20 = 5 | 5 | 5 | PASS |
| C3 positive YoY years | 5/6 = 83.3% (L157) | 75-99 = 3 | 3 | 3 | PASS |
| C4 PAT minus revenue CAGR | +18.3pp (L160) | >=+3 = 5 | 5 | 5 | PASS |
| D1 ND/EBITDA | 17.49 / 56.71 = 0.31x (L171) | 0-1.0x = 4 | 4 | 4 | PASS |
| D2 interest cover | 54.05 / 3.98 = 13.58x (L174) | >=10 = 5 | 5 | 5 | PASS |
| D3 D/E | 37.55 / 184.00 = 0.204 (L176) | 0.1-0.5 = 4 | 4 | 4 | PASS |
| D4 current ratio | 13,243.43L / 6,770.80L = 1.956 (L179) | 1.5-1.99 = 4 | 4 | 4 | PASS |
| E1 promoter holding | 57.94% (L188) | 50-59.9 = 4 | 4 | 4 | PASS |
| E2 promoter change | 79.48% to 57.94%, -21.5pp (L195) | >3 down = 0 | 0 | 0 | PASS (score). Note FAIL, see MJ-3 |
| E3 pledge | 0% (L203) | 0% = 5 | 5 | 5 | PASS |
| E4 contingent/NW | 0.805 / 184.00 = 0.44% (L210) | <5 = 5 | 5 | 5 | PASS |

Arithmetic spot checks done by this verifier on B01's own figures:
- FCF column (L92-98): each row CFO minus capex reproduces. Sum -67.15 reproduces.
- CFO sum 58.50 and PAT sum 97.96 reproduce.
- EBITDA FY26 50.07+3.98+6.33-3.67 = 56.71 reproduces. EBIT 50.07+3.98 = 54.05 reproduces.

Block totals, as stated: A 18, B 3, C 18, D 17, E 14. Core 70.
Block totals, recomputed: A 15, B 3, C 18, D 17, E 14. Core 67.

### 1.2 Moat tests (Block F) re-derived

| Test | B01 input | B01 score | Recomputed | Result |
|---|---|---|---|---|
| M1 pricing power | EBITDA margin 15.9% to 24.1%, +8.2pp; rev CAGR 35.6% (L225-227) | 5 | 5 | PASS |
| M2 cost advantage | PEER DATA NEEDED (L229) | 0 | 0 | PASS (rule followed) |
| M3 capital efficiency | FAT 235.16/51.80 = 4.54x; ROCE FY26 27.5% (L231) | 5 | 5 | PASS |
| M4 customer stickiness | 1 decline year FY21, recovered (L234) | 3 | 3 | PASS |
| M5 scale | PEER DATA NEEDED (L237) | 0 | 0 | PASS |
| M6 technology/R&D | R&D spend NOT FOUND (L240) | 0 | 0 | PASS, see MN-2 |
| M7 regulatory | no licence evidence (L244) | 0 | 0 | PASS |
| M8 distribution | no reach data (L248) | 0 | 0 | PASS |
| M9 brand | GM proxy 47.1%, no peer (L251) | 0 | 0 | PASS |
| M10 switching costs | rev grew all but 1 year; recv days 67.6 to 47.4 (L255) | 3 | 3 | PASS |
| M11 network effects | 3yr CAGR 37.6% > prior 33.7%; selling % 9.3 to 7.5 (L259) | 5 | 5 | PASS (mechanical, as the rubric demands) |
| M12 negative WC | WC days 62-119, all >45 (L267) | 0 | 0 | PASS |

Moat score 21/60. Moats present 5 (M1, M3, M4, M10, M11). Class STRONG (4-5 band). All reproduce.
B07 later overrides M11 on mechanism grounds. The Gate 0 rubric is numeric, so B01 applied its rule correctly.
With the B07 override the count is 4, still STRONG. See MN-3.

### 1.3 Classification, confidence, deal-breakers, edge rules

| Rule | B01 application | Result |
|---|---|---|
| Opening data-years line | "Data available: 7 years (FY20 to FY26)" (L3) | PASS |
| Data confidence | 7 years, moderate, no downgrade (L291) | PASS |
| CAGR edge rules | no zero/negative endpoints; no loss-to-profit swing noted (L154, data_notes) | PASS |
| Classification matrix | Core 70 (60-79) + STRONG = GOOD+ (L299) | PASS. Recomputed core 67, same cell |
| Deal-breakers 1-9 | #2 fires (Block B 3 <8), cap GOOD; driving years FY25-26 named (L301-316) | PASS |
| FLAG-GATE0 rule | flag only if classification <= AVERAGE; GOOD, so flags [] | PASS |
| ROCE formula fidelity ("fixed, do not substitute") | FY20-23 CE on NW+Debt proxy (L20-27) | FAIL, MJ-2 |
| FCF formula fidelity | FY20-21 capex proxied by total investing cash flow (L79-81) | FAIL, MN-1 (no score change) |
| Grounded claims (rule 5) in flags/notes | E2 "not a sell-down" note contradicts B01's own share counts | FAIL, MJ-3 |
| Anchors mandatory | present on material lines | PASS |

Final classification GOOD. Recomputed classification GOOD. Concur.
Recomputed grand total: 88 (Core 67 + Moat 21). With the B07 M11 override applied: 83.

---

## PART 2: EMERGING MOAT (B07) COMPLIANCE

### 2.1 Scorecard mechanics

| Row | L x I | Raw | Mult | Adj | Mechanics check |
|---|---|---|---|---|---|
| A1 | HH | 4 | 1.0 | 4.0 | matrix PASS; evidence overlap with B2, MJ-1 |
| A2 | none | 0 | | 0 | PASS |
| A3 | MM | 2 | 1.0 | 2.0 | PASS |
| A4 | ML | 1 | 1.0 | 1.0 | PASS |
| B1 | HH | 4 | 1.0 | 4.0 | PASS (capex committed is DOC per taxonomy) |
| B2 | HH | 4 | 1.0 | 4.0 | matrix PASS; overlap with A1, MJ-1 |
| B3, C2, D1, D2, E1, F1, G1, G2, H1, H3 | none | 0 | | 0 | PASS |
| C1 | ML | 1 | 1.0 | 1.0 | PASS |
| E2 | HM | 3 | 1.0 | 3.0 | matrix PASS; shares evidence with H2, CR-1 |
| F2 | MM | 2 | 1.0 | 2.0 | PASS |
| H2 | HH | 4 | 1.0 | 4.0 | FAIL, double credit, CR-1 |
| I1 | none | 0 | | 0 | PASS (two-leg test, both legs absent) |
| I2 | none | 0 | | 0 | PASS (no named sacrifice) |
| R1 | LM | 1 | 0.7 | 0.7 | PASS (MGMT-only at 0.7) |

Sum as printed: 25.7. Arithmetic reproduces.

### 2.2 Rule-by-rule

| # | Rule (07-emerging-moat-pipeline.md) | Result |
|---|---|---|
| 1 | All 23 rows (22 + R1) addressed | PASS (07-emoat.md L199-223) |
| 2 | Absent categories say NO EVIDENCE FOUND | PASS |
| 3 | Evidence taxonomy applied to each item | PASS |
| 4 | Source anchors on evidence items | PASS |
| 5 | L x I matrix values correct | PASS |
| 6 | Multipliers per evidence tier | PASS |
| 7 | Adjusted total arithmetic | PASS (25.7) |
| 8 | Band on the stated total | PASS (25-39 STRENGTHENING on 25.7) |
| 9 | I1/I2 contribution stated separately | PASS (L227) |
| 10 | Category 21 (I1) two-leg test | PASS (0, leg a and leg b absent) |
| 11 | Category 22 (I2) named specific sacrifice | PASS (0, honest "nothing must be destroyed") |
| 12 | Completionist recount performed | PASS (L171) |
| 13 | Recount and count statements accurate | FAIL, MN-4 |
| 14 | Scores consistent with evidence tiers (no MGMT-only row scored as DOC) | PASS |
| 15 | One evidence item, one credit (CLAUDE.md "never credit one quality improvement through two mechanisms") | FAIL, CR-1 and MJ-1 |
| 16 | Section 1 (1A/1B/1C) | PASS |
| 17 | Section 2A/2B | PASS |
| 18 | Section 2C prescribed formula (capex x historical FAT) | FAIL, MJ-4 |
| 19 | Section 2D | PASS |
| 20 | Section 4 (4A/4B/4C) | PASS |
| 21 | Optionality register present and in block | PASS (7 rows) |
| 22 | 6A timeline and 6B risks | PASS |
| 23 | 6C uses the injected Gate 0 block consistently | FAIL, MN-3 |
| 24 | 6E output card | PASS |
| 25 | YAML schema complete | PASS |
| 26 | Not conflated with FTTCP | PASS (L3) |
| 27 | evidence_mix counts traceable to the report | FAIL, MN-5 |

6D combined classification (GOOD+): NOT VERIFIABLE. The rule source says "per the standard matrix" but does not print the matrix. Excluded from the rule count. Its EM input changes under CR-1.

Recomputed em_score: 19.7 to 24.7. Recomputed class: MODEST (12-24). See CR-1.

---

## PART 3: FINDINGS

### CR-1 [CRITICAL] B07: three agreements credited in both E2 and H2; the fix drops em_score below the 25 band edge
- Location: 07-emoat.md L106 (E2) and L127 (H2); recount L171.
- E2 evidence: "Signed, dated agreements: Ensales (US, 19 states...), Weidmann (Europe/North Africa), Electrolink (UK/Ireland)".
- H2 evidence: "Four separate signed/executed agreements in FY26 alone: Sukrut... Weidmann agency... Electrolink... Ensales".
- The same three documents score in two categories. The recount counts them twice as well ("E2: 3 signed distribution/representation agreements"; "H2: Sukrut JV + 3 partnership agreements").
- H2 on its own unique evidence: the Sukrut 50% JV with an Indian peer, Rs5.24cr (DOC), plus the expired Swiss tech transfer (MGMT). That supports HM (3) or MM (2), not HH (4).
- Recomputed: H2 falls by 1 to 2 points. em_score 24.7 to 23.7 from this fix alone.
- Why CRITICAL: 25.7 sits 0.7 above the 25 band edge. The 07 prompt header names "EM >=25" as a UA qualifier. Any correction of 0.8 or more flips STRENGTHENING to MODEST and fails that qualifier. A failed UA qualifier moves the destination PE at phase 3.
- Action: stage 7 rescore of E2/H2 with each agreement credited once. Phase 3 must not treat "EM >=25" as met on the current block.

### MJ-1 [MAJOR] B07: A1 and B2 rest on the same qualification evidence; the scan also applies its "existing, not emerging" test unevenly
- Location: 07-emoat.md L10, L68 (A1), L84 (B2).
- A1 documented evidence: AR p.47 qualification-cycle language and PGCIL/NTPC/NPCIL/DRDO approvals (2016-2018).
- B2 documented evidence: the same approvals (AR p.49) plus ISO/NABL certificates.
- B07 itself says at L10 that the AR p.47 mechanism "is the same mechanism scored under Category B2".
- A1's only unique item is the "12-13 independent bushing makers" claim, tagged MGMT and pending verification.
- Uneven test: E1 (L103) and H1 (L124) score 0 as "existing-moat facts already captured in B01, not emerging". A1 and B2 are "already active" since 2016-2018, and B2's mechanism is the one B07 uses to confirm B01 M10. Both score 4.
- Recomputed: A1 on unique evidence = HH x 0.7 = 2.8 (-1.2). Under the E1/H1 standard, A1 = 0 (-4).
- Combined with CR-1: em_score 23.5 (minimum fixes) to 19.7 (maximum fixes). Class MODEST in every case.

### MJ-2 [MAJOR] B01: ROCE formula substituted for FY20-23; A4 recomputes from 3 to 0
- Location: 01-gate0.md L20-27, L60.
- The rule source says formulas are "fixed, do not substitute alternatives". It also says a missing data point is "N/A... score it 0".
- B01 used Equity+Reserves+Borrowings for FY20-23 CE. It used Total Assets minus Current Liabilities for FY24-26.
- A4 then compares a proxy FY20 (28.3%) with an exact FY26 (27.5%). The -0.8pp decline also falls in the gap between the ">= earliest" and "decline 1-3pp" bands.
- On the formula-compliant series (FY24-26 only): latest 27.5% vs earliest 42.3% = -14.8pp. Band ">5pp decline" = 0. If treated as N/A, also 0.
- A1 and A2 do not change on the exact-only series: median 27.5% (5), minimum 20.2% (5).
- Recomputed: A4 = 0, Block A = 15, Core = 67, grand total 88. Classification GOOD is unchanged (60-79 band, deal-breaker #2 cap).

### MJ-3 [MAJOR] B01: the E2 "dilution, not sell-down" note conflicts with B01's own share counts and dates
- Location: 01-gate0.md L192-201; B01-gate0.yaml data_notes line 35.
- The score of 0 is correct. The note that feeds downstream is not grounded.
- B01's own figures: pre-offer promoter shares 1,76,03,595 (RHP p.30). 31-Mar-2026 promoter shares 1,65,43,595. The share count fell by 10,60,000.
- Arithmetic on B01's figures: with no fall in share count, promoters would hold 1,76,03,595 / 2,85,51,249 = 61.66%. The actual figure is 57.94%. So 3.72pp of the 21.5pp decline is a fall in promoter share count, not dilution. The cause (offer for sale or transfer) is NOT FOUND in the inputs to this verifier.
- The note also names the Aug-2026 preferential allotment as a cause. That allotment post-dates the 31-Mar-2026 pattern that B01 measures. It cannot explain that figure.
- The "evidence against sell-down" covers only 30-Sep-2025 to 31-Mar-2026. It does not cover the IPO window.
- Action: correct the note to "about 17.8pp dilution, 3.72pp promoter share-count reduction at or after the IPO, cause NOT FOUND". Downstream stages must not treat E2 as fully explained.

### MJ-4 [MAJOR] B07: Section 2C prescribed formula not run; proxy base contradicts B07's own capacity table
- Location: 07-emoat.md L54-59; B07-emoat.yaml capex_embedded_growth_pct: 67.
- The rule: total capex under execution x historical fixed-asset turnover = implied incremental revenue, as % of current revenue.
- B07 says FAT is NOT FOUND. The run already holds FAT = 4.54x (B01 M3, 235.16 / 51.80, 01-gate0.md L231). The net block sits in the AR balance sheet, which is in stage 7's inputs.
- Prescribed arithmetic on the run's own figures: 153 x 4.54 = 694.6cr, which is 295% of FY26 revenue of 235.16cr. This number is mechanical. Historical FAT on an old, depreciated block overstates new-plant turnover. The stage must still show it, then add its caveat, not replace it.
- The proxy's base is inconsistent. B07 backs out a pre-Vadodara total of 9,000 units/yr (L56). Its own 2A row 2 (L48) puts OIP capacity alone at 10,000 units/yr after the FY26 expansion. The 9,000 base and the 67% result cannot both hold unless the 15,000 figure covers a subset of lines, and the report does not say so.
- The YAML field carries 67 with no inline caveat. The caveat sits only in input_gaps. A downstream Pillar 3 reader could take it as embedded revenue growth.
- Action: show the prescribed figure with its caveat. Reconcile the capacity base or mark it NOT FOUND. Label the YAML field value as a unit-capacity proxy.

### MN-1 [MINOR] B01: FY20-21 capex proxied by total investing cash flow
- Location: 01-gate0.md L79-81. This substitutes for the fixed FCF formula.
- No score change. Excluding FY20-21: B2 = 3/5 = 60% (2). B3 FY22-26 sum = -72.57 (0).

### MN-2 [MINOR] B01: M6 R&D search terms may be too narrow
- Location: 01-gate0.md L240. B01 searched for "Research and Development" and "R&D expenditure" and found no match.
- B07 L110 documents DSIR-recognised in-house R&D (AR p.28). A Board's Report technology-absorption annexure usually states R&D spend.
- The M6 band-3 test needs R&D/revenue >=3%. The other two legs pass (EBITDA margin 24.1% >=15%; revenue CAGR 35.6% >=10%). A found figure of 3% or more would add one moat.
- No classification change is possible, because the deal-breaker #2 cap holds.

### MN-3 [MINOR] B07: 6C carries B01's moat count after B07 overrode M11
- Location: 07-emoat.md L250, L256 ("5/5 confirmed types", 21/60).
- After B07's own M11 override: 4 moats, 16/60, still STRONG. The class does not change. The table is stale.

### MN-4 [MINOR] B07: count statements are wrong, and the recount is inflated by double counts
- Location: 07-emoat.md L169. The report says "Strong x4, Moderate x2". Its table shows Strong x5 (A1, B1, B2, E2, H2) and Moderate x2 (A3, F2).
- Recount L171 says 13 documented items. The three agreements count twice (E2, H2). The approvals count twice (A1, B2). About 9 items are unique.

### MN-5 [MINOR] B07: evidence_mix claim and inference counts cannot be traced
- Location: B07-emoat.yaml evidence_mix {documented: 13, claim: 8, inference: 2}.
- The report lists no MGMT or INF items that add up to 8 and 2. The 13 documented items are listed. The other counts cannot be audited.

---

## PART 4: VALUATION SCOPE

NOT RUN. Pending phase 3. B10/B11, the Section 1B layer set, FTTCP, the expectation ledger, and the Business Understanding Narrative are outside this invocation. No rule 4-7 or 9-15 check was made.

Carry-forward for the phase-3 audit: CR-1 and MJ-1 put the "EM >=25" UA qualifier in doubt. The phase-3 verifier should check whether B11 relied on it.

---

## PART 5: COUNTS

- Gate 0 rules checked: 42 (20 block lines, 12 moat tests, moat class, confidence, matrix, deal-breakers, CAGR edge, FLAG-GATE0 rule, opening line, ROCE formula, FCF formula, grounded notes). Fails: 4 (A4, ROCE formula, FCF formula, E2 note). Passed: 38.
- Emerging Moat rules checked: 27 (6D excluded as not verifiable). Fails: 5 (rules 13, 15, 18, 23, 27). Passed: 22.
- Total: 60 passed of 69 checked = 87.0%.
- Findings: 1 CRITICAL, 4 MAJOR, 5 MINOR.
- Gate 0 classification: concur (GOOD). Recomputed core 67 vs stated 70.
- Emerging Moat classification: do not concur. Recomputed MODEST (19.7 to 24.7) vs stated STRENGTHENING (25.7).

```yaml
stage: B12c
company: "YASHHV"
run_date: "2026-09-26"
model: "claude-opus-5-5"
status: complete
scope: "PHASE 1 ONLY: Gate 0 (B01) + Emerging Moat (B07). Valuation audit pending phase 3."
gate0: {rules_checked: 42, fails: ["A4 ROCE trend: B01 3, recomputed 0 (formula-compliant FY24-26 series 42.3% to 27.5% = -14.8pp); Block A 18 -> 15; core 70 -> 67; grand total 91 -> 88; classification GOOD unchanged", "ROCE formula substituted (NW+Debt proxy FY20-23) against 'fixed, do not substitute' rule", "FCF formula: FY20-21 capex proxied by total investing cash flow; no score change", "E2 data_note 'dilution, not sell-down' ungrounded: B01's own share counts show promoter shares 1,76,03,595 -> 1,65,43,595 (-10,60,000), 3.72pp of the 21.5pp decline; Aug-2026 allotment post-dates the 31-Mar-2026 measurement; score 0 unchanged"]}
emoat: {rules_checked: 27, fails: ["Rule 15 double credit: Ensales/Weidmann/Electrolink agreements scored in both E2 and H2; H2 on unique evidence HM/MM, -1 to -2", "Rule 15 double credit: A1 and B2 on the same approval/qualification evidence (AR p.47/p.49); A1 unique evidence MGMT-only, -1.2 to -4; existing-vs-emerging test applied to E1/H1 but not A1/B2", "Recomputed em_score 19.7 to 24.7 vs stated 25.7; class MODEST vs stated STRENGTHENING; EM>=25 UA qualifier fails on every recompute", "Rule 18 Section 2C: prescribed capex x FAT not run though FAT 4.54x exists in B01; prescribed arithmetic 153 x 4.54 = 694.6cr = 295% of FY26 revenue; proxy 9,000-unit base conflicts with B07's own OIP 10,000 units/yr; YAML value 67 carries no inline caveat", "Rule 13 counts: 'Strong x4' vs table Strong x5; recount 13 inflated by double counts (about 9 unique)", "Rule 23 6C: moats_confirmed 5 / 21/60 stale after B07's own M11 override (4, 16/60, still STRONG)", "Rule 27 evidence_mix claim 8 / inference 2 not enumerated in report"]}
valuation: {rules_checked: 0, fails: []}  # PENDING PHASE 3, not in scope for this invocation
expectation_ledger: {present: false, downside_row: false, all_rows_confirm_by: false, all_rows_metric_threshold: false, prob_in_range: false, decay_status_valid: false, off_ledger_credit: false, residual_pct_cmp: 0, residual_starter_cap_ok: true, fails: []}  # NOT CHECKED: phase 3 scope; field values are schema defaults, not findings
business_understanding_narrative: {present: false, five_questions_answered: false, prose_only: false, section6_candidates_named: 0, valuation_vocab_leak: false, fails: []}  # NOT CHECKED: stage 13 not in phase 1 scope; field values are schema defaults, not findings
recomputed_destination_pe: ""  # not in scope (phase 3)
recomputed_decision: ""        # not in scope (phase 3); Gate 0 classification GOOD concur
findings:
  - {severity: CRITICAL, location: "07-emoat.md L106/L127/L171; B07 em_score", finding: "E2 and H2 both credit the same three agreements (Ensales, Weidmann, Electrolink); em_score 25.7 is 0.7 above the 25 band edge and the EM>=25 UA qualifier; removing the duplicate drops H2 by 1-2 and the score to 24.7-23.7, class MODEST", recomputed: "em_score 19.7-24.7, MODEST (with MJ-1)"}
  - {severity: MAJOR, location: "07-emoat.md L10/L68/L84/L103/L124", finding: "A1 and B2 rest on the same approval/qualification evidence; A1's unique item is MGMT-only; E1/H1 zeroed as existing-moat facts while A1/B2 (active since 2016-2018) score 4 each", recomputed: "A1 2.8 (MGMT) or 0"}
  - {severity: MAJOR, location: "01-gate0.md L20-27/L60", finding: "ROCE CE proxy for FY20-23 breaks the fixed-formula rule; A4 compares proxy FY20 with exact FY26", recomputed: "A4 0; Block A 15; core 67; grand total 88; classification GOOD unchanged"}
  - {severity: MAJOR, location: "01-gate0.md L192-201; B01 data_notes", finding: "E2 'not a sell-down' note conflicts with B01's own share counts (-10,60,000 promoter shares, 3.72pp of the decline) and cites an Aug-2026 allotment for a 31-Mar-2026 figure", recomputed: "score 0 unchanged; note to be corrected"}
  - {severity: MAJOR, location: "07-emoat.md L54-59; B07 capex_embedded_growth_pct", finding: "Section 2C prescribed formula not run though FAT 4.54x exists in B01; proxy base 9,000 units conflicts with B07 2A OIP 10,000 units/yr; YAML 67 uncaveated", recomputed: "prescribed: 153 x 4.54 = 694.6cr = 295% of FY26 revenue (mechanical, caveat required)"}
  - {severity: MINOR, location: "01-gate0.md L79-81", finding: "FY20-21 capex proxied by total investing cash flow", recomputed: "no score change (B2 3/5 = 60% -> 2; B3 -72.57 -> 0)"}
  - {severity: MINOR, location: "01-gate0.md L240", finding: "M6 R&D search terms narrow; B07 documents DSIR-recognised R&D; a spend >=3% would add a moat (other M6 legs pass)", recomputed: "no classification change (deal-breaker #2 cap)"}
  - {severity: MINOR, location: "07-emoat.md L250/L256", finding: "6C carries 5 moats, 21/60 after B07's own M11 override", recomputed: "4 moats, 16/60, STRONG"}
  - {severity: MINOR, location: "07-emoat.md L169/L171", finding: "'Strong x4' vs table Strong x5; recount 13 includes double counts", recomputed: "about 9 unique documented items"}
  - {severity: MINOR, location: "B07-emoat.yaml evidence_mix", finding: "claim 8 / inference 2 not enumerated in report", recomputed: "NOT FOUND"}
critical_count: 1
major_count: 4
minor_count: 5
acceptance_rate: 87.0             # 60 passed / 69 checked (Gate 0 38/42, EM 22/27)
```
