# VERIFIER C: FRAMEWORK ADHERENCE (PHASE 1 SCOPE). SOUTHWEST, run 2026-11-09

Scope: Gate 0 (B01) and Emerging Moat (B07) only. The valuation audit (B10, B11) is pending phase 3.

Inputs read: prompts/12-verifiers-pipeline.md (Verifier C section), prompts/01-gate-0-pipeline.md, prompts/07-emerging-moat-pipeline.md, outputs/reports/01-gate0.md, outputs/blocks/B01-gate0.yaml, outputs/reports/07-emoat.md, outputs/blocks/B07-emoat.yaml. Nothing else was read: no source PDF, no other stage report, no other verifier output.

Verifier A owns the numbers. Every recomputation below uses only the inputs B01 and B07 state. Anchors are report line numbers (L) in 01-gate0.md and 07-emoat.md.

## 1. RESULT

| Audit | Rules checked | Passed | Failed |
|---|---|---|---|
| Gate 0 (B01) | 64 | 59 | 5 |
| Emerging Moat (B07) | 60 | 53 | 7 |
| Total | 124 | 112 | 12 |

Acceptance rate 112 / 124 = 90.3%. Findings: CRITICAL 1, MAJOR 2, MINOR 11. Three MINOR findings (F7, F8, F9) are not rule fails. F3 covers two rule fails.

Not testable, excluded from the count: B07 Section 6D. Prompt 07 names a "standard matrix" but neither rule file defines it. B07 discloses this (L232). The label GOOD cannot be re-derived.

Verifier C rule 8: categories 21 (I1) and 22 (I2) are present. No stage 7 REWORK arises from it.

Three findings need the operator's eye.

**F1 (CRITICAL). E1 is scored 5 on a data point B01 itself marks NOT FOUND.** Literal application gives core 57 and classification AVERAGE, not GOOD.

**F2 (MAJOR). M11 reads "rev CAGR" at 25.1% where M1 reads the same term at 14.1%.** On one basis M11 scores 0. Moat class stays MODERATE.

**F3 (MAJOR). B07 applies 1.0x to two mixed-evidence rows and 0.7x to a third.** One convention gives 11.3 (NONE) or 13.4 (MODEST). The filed 12.8 matches neither.

### Scorecard as filed and as recomputed

| Item | B01 as filed | E1 literal (F1) | E1 literal and M11 on C1 basis (F1, F2) |
|---|---|---|---|
| Block E | 8 | 3 | 3 |
| Core score | 62 | 57 | 57 |
| Moat score | 10 | 10 | 7 |
| Moats present | 3 | 3 | 2 |
| Moat class | MODERATE | MODERATE | MODERATE |
| Grand total | 72 | 67 | 64 |
| Classification | GOOD | AVERAGE | AVERAGE |

### What separates the two readings of E1

Reading 1: the rule scores promoter holding for the latest quarter. B01 marks that figure NOT FOUND (L50). Prompt 01 rule 5 says NOT FOUND scores 0. B01 scored E3 at 0 on the same empty folder (L52).

Reading 2: 31 Mar 2026 is a filed quarter-end and the latest figure in the inputs, with the date stated. GOOD stands on that reading.

The one observation that separates them: promoter holding in the shareholding pattern for the quarter ended 30 Sep 2026. B01 records promoter disposals in Jun to Sep 2026 as not netted (L50, L120), so the 31 Mar figure is known to be stale.

| Sep 2026 promoter holding | E1 | Core | Classification |
|---|---|---|---|
| 60% or above | 5 | 62 | GOOD |
| 50 to 59.9% | 4 | 61 | GOOD |
| 40 to 49.9% | 3 | 60 | GOOD |
| 30 to 39.9% | 1 | 58 | AVERAGE |
| below 30% | 0 | 57 | AVERAGE |

The same filing closes E3 (pledge) and deal-breaker 5. A 0% pledge adds 5 points to Block E. The table above holds E3 at 0.

## 2. GATE 0 COMPLIANCE (B01)

### 2.1 Operating rules and formula definitions

| # | Rule | B01 application | Result |
|---|---|---|---|
| 1 | Rule 6 opening line | Present, 10 years FY17 to FY26, 3-year items named (L3) | PASS |
| 2 | Rule 4 anchors on every number | AR FY25 figures carry no page (L17, L28, L32). AR FY26 8,512.63 lakh has no page (L18). Moat inputs 95.62, S&A % and yearly margins carry no anchor (L56, L61, L69) | FAIL (F5, MINOR) |
| 3 | ROCE formula | Computed and stated, EBIT = PBT + Interest, CE = Total assets less Current liabilities (L14). Screener supplies none | PASS |
| 4 | ROE formula | Average net worth, FY17 on closing, stated (L23) | PASS |
| 5 | WC days formula | Revenue basis stated (L32) | PASS |
| 6 | FCF formula | CFO less PPE and intangibles, no acquisitions (L28, L29) | PASS |
| 7 | CAGR formula | Applied (L37, L38) | PASS |
| 8 | CAGR edge: negative endpoint | Not triggered, both endpoints positive | PASS |
| 9 | CAGR edge: loss-to-profit swing note | Not triggered, PAT positive at both endpoints | PASS |
| 10 | CAGR edge: C4 when PAT CAGR is N/M | Not triggered | PASS |

### 2.2 Core blocks, re-derived

| Metric | Stated input | Band hit | B01 | Recomputed | Result |
|---|---|---|---|---|---|
| A1 Median ROCE | 12.44, 15.84, 23.11, median 15.84 (L21) | 15-19.9 = 3 | 3 | 3 | PASS |
| A2 Minimum ROCE | 12.44 (L22) | 12-14.9 = 3 | 3 | 3 | PASS |
| A3 Median ROE | 10 values, median (11.25 + 11.48) / 2 = 11.37 (L23) | below 12 = 0 | 0 | 0 | PASS |
| A4 ROCE trend | 23.11 vs 12.44 (L24) | latest above earliest = 5 | 5 | 5 | PASS |
| B1 Cum CFO / PAT | 119.06 / 116.02 = 1.03 (L27) | 1.00 or above = 5 | 5 | 5 | PASS |
| B2 FCF-positive years | 1 of 3 = 33% (L30) | below 50 = 0 | 0 | 0 | PASS |
| B3 Cum FCF / PAT | -32.87 / 57.73, negative (L31) | negative = 0 | 0 | 0 | PASS |
| B4 WC days change | 216.7 less 258.1 = -41.4 (L34) | decreased above 5 = 5 | 5 | 5 | PASS |
| C1 Revenue CAGR | (243.02 / 74.17)^(1/9) - 1 = 14.1% (L37) | 10-14.9 = 3 | 3 | 3 | PASS |
| C2 PAT CAGR | (33.03 / 5.70)^(1/9) - 1 = 21.6% (L38) | 20 or above = 5 | 5 | 5 | PASS |
| C3 Positive YoY years | 9 of 9 (L39) | 100% = 5 | 5 | 5 | PASS |
| C4 PAT less revenue CAGR | +7.5pp (L40) | +3pp or above = 5 | 5 | 5 | PASS |
| D1 ND / EBITDA | 68.42 / 58.70 = 1.17x (L44) | 1-2x = 3 | 3 | 3 | PASS |
| D2 Interest cover | 52.33 / 8.79 = 5.95x (L45) | 5-9.9 = 4 | 4 | 4 | PASS |
| D3 Debt / Equity | 80.14 / 203.53 = 0.39 (L46) | 0.1-0.5 = 4 | 4 | 4 | PASS |
| D4 Current ratio | 19,432.60 / 10,569.70 = 1.84 (L47) | 1.5-1.99 = 4 | 4 | 4 | PASS |
| E1 Promoter holding, latest quarter | 68.85% at 31 Mar 2026. Latest-quarter pattern marked NOT FOUND (L50) | Rule 5: NOT FOUND = 0 | 5 | 0 | FAIL (F1, CRITICAL) |
| E2 Promoter change, 3 years | -4.34pp in FY25, FY24 NOT FOUND (L51) | above 3 decrease = 0, and NOT FOUND = 0 | 0 | 0 | PASS |
| E3 Pledge | NOT FOUND (L52) | Rule 5: NOT FOUND = 0 | 0 | 0 | PASS |
| E4 Contingent / Net worth | 2,812.70 / 20,352.94 = 13.8%. Alternate reading 12.1%, same band (L53) | 5-15 = 3 | 3 | 3 | PASS |

Arithmetic note: L33 gives FY25 WC days as 154.5 + 93.6 - 37.8 = 210.4. The stated parts sum to 210.3. Rounding of the parts explains it. No band moves.

### 2.3 Moat block, re-derived

| Test | Stated input | B01 | Recomputed | Result |
|---|---|---|---|---|
| M1 Pricing | Margin -3.3pp, rev CAGR 14.1% (L59) | 1 | 1 | PASS |
| M2 Cost advantage | PEER DATA NEEDED (L60) | 0 | 0 | PASS on the stated input. See F9 |
| M3 Capital efficiency | FAT 2.54x, ROCE 23.1% (L61) | 3 | 3 | PASS |
| M4 Stickiness | 0 decline years, receivable days 73 to 175 (L62) | 3 | 3 | PASS |
| M5 Scale | PEER DATA NEEDED (L63) | 0 | 0 | PASS on the stated input. See F9 |
| M6 R&D | R&D spend NOT FOUND (L64) | 0 | 0 | PASS |
| M7 Regulatory | Listed-player count NOT FOUND (L65) | 0 | 0 | PASS |
| M8 Distribution | "none quantified" (L66) | 0 | 0 or 1 | FAIL (F4, MINOR). The phrase fits both "mentioned unquantified = 1" and "none = 0" |
| M9 Brand | PEER DATA NEEDED (L67) | 0 | 0 | PASS on the stated input. See F9 |
| M10 Switching | Receivable days rose far more than 10, 0 decline years (L68) | 0 | 0 | PASS |
| M11 Network | Tier 2 passed on FY23-26 CAGR 25.1%, S&A % 2.03 to 2.04 (L69) | 3 | 0 | FAIL (F2, MAJOR) |
| M12 Negative WC | 258, 210, 217 days (L70) | 0 | 0 | PASS |

### 2.4 Totals, classification, deal-breakers, output

| # | Rule | B01 | Recomputed from B01's stated scores | Result |
|---|---|---|---|---|
| 1 | Block A sum | 11 | 3 + 3 + 0 + 5 = 11 | PASS |
| 2 | Block B sum | 10 | 5 + 0 + 0 + 5 = 10 | PASS |
| 3 | Block C sum | 18 | 3 + 5 + 5 + 5 = 18 | PASS |
| 4 | Block D sum | 15 | 3 + 4 + 4 + 4 = 15 | PASS |
| 5 | Block E sum | 8 | 5 + 0 + 0 + 3 = 8 | PASS (arithmetic; F1 changes the input) |
| 6 | Core sum | 62 | 62 | PASS (arithmetic; F1 changes the input) |
| 7 | Moat sum | 10 | 1 + 3 + 3 + 3 = 10 | PASS (arithmetic; F2 changes the input) |
| 8 | Grand total | 72 | 72 | PASS (arithmetic) |
| 9 | Moat class | MODERATE, 3 present | 2-3 = MODERATE | PASS |
| 10 | Classification matrix | Core 60-79, else = GOOD | GOOD on core 62 | PASS on stated core. AVERAGE on core 57 (F1) |
| 11 | Data confidence | "10 years P&L, full", no downgrade, 3-year items stated (L75) | Rule keys to one year count | PASS on the text. See F7 |
| 12-20 | Deal-breakers 1 to 9 | None triggered (L76) | A 11, B 10, median ROCE 15.84%, CFO/PAT 1.03, ND/EBITDA 1.17x, 0 decline years, PAT positive FY24-26, 10 years. Pledge NOT FOUND, so breaker 5 is untested, and B01 says so | PASS (9 rules) |
| 21 | Output format | Scorecard, classification, strongest and weakest, decision line present. Moat profile bars absent | Bars required by Prompt 01 Output | FAIL (F6, MINOR) |
| 22 | YAML block schema | All fields present, analyst_note under 200 words | n/a | PASS |

## 3. EMERGING MOAT COMPLIANCE (B07)

### 3.1 All 23 rows

Matrix applied: HH=4, HM/MH=3, HL/MM/LH=2, ML/LM=1, LL=1, no evidence=0. Multipliers 1.0, 0.7, 0.5.

| ID | Addressed | L x I | Raw | x | B07 adj | Arithmetic | Tier consistency |
|---|---|---|---|---|---|---|---|
| A1 Rare capability | Yes (L70) | MM | 2 | 0.7 | 1.4 | PASS | PASS |
| A2 Patent | NO EVIDENCE (L71) | | 0 | | 0 | n/a | n/a |
| A3 Process | NO EVIDENCE (L72) | | 0 | | 0 | n/a | n/a |
| A4 Platform | NO EVIDENCE (L73) | | 0 | | 0 | n/a | n/a |
| B1 Backward | NO EVIDENCE (L76) | | 0 | | 0 | n/a | n/a |
| B2 Qualification | Yes (L77) | MM | 2 | 1.0 | 2.0 | PASS | PASS |
| B3 Network | NO EVIDENCE (L78) | | 0 | | 0 | n/a | n/a |
| C1 Embedded | Yes (L81) | HM | 3 | 1.0 | 3.0 | PASS | FAIL (F3) recomputed 2.1 |
| C2 Concentration | NO EVIDENCE, reverse (L82) | | 0 | | 0 | n/a | n/a |
| D1 Data | NO EVIDENCE (L85) | | 0 | | 0 | n/a | n/a |
| D2 Digital | NO EVIDENCE (L85) | | 0 | | 0 | n/a | n/a |
| E1 Access | Yes (L88) | LH | 2 | 1.0 | 2.0 | PASS | FAIL (F3) recomputed 1.4 |
| E2 China+1 | NO EVIDENCE (L89) | | 0 | | 0 | n/a | n/a |
| F1 Talent density | NO EVIDENCE (L92) | | 0 | | 0 | n/a | n/a |
| F2 Execution | Addressed, scored 0, B05 record used (L93) | | 0 | | 0 | n/a | n/a |
| G1 War chest | Yes (L96) | LL | 1 | 1.0 | 1.0 | PASS | PASS |
| G2 WC | NO EVIDENCE (L97) | | 0 | | 0 | n/a | n/a |
| H1 Consolidation | NO EVIDENCE (L100) | | 0 | | 0 | n/a | n/a |
| H2 Partnerships | Yes (L101) | MM | 2 | 1.0 | 2.0 | PASS | PASS |
| H3 ESG | NO EVIDENCE (L102) | | 0 | | 0 | n/a | n/a |
| I1 Talent asymmetry | NO EVIDENCE on both legs (L105) | | 0 | | 0 | n/a | n/a |
| I2 Cannibalization | Addressed, scored 0 (L106) | | 0 | | 0 | n/a | n/a |
| R1 Regulatory | Yes (L158) | MM | 2 | 0.7 | 1.4 | PASS | PASS |

Coverage: 23 of 23 PASS. Arithmetic: 7 of 7 PASS. Tier consistency: 5 of 7 PASS.

Total check: 1.4 + 2.0 + 3.0 + 2.0 + 1.0 + 2.0 + 1.4 = 12.8. Matches L186.

### 3.2 Finding F3 in detail

Three rows carry a documented item and a management claim that gives the row its moat content.

| Row | B07 statement | Multiplier used |
|---|---|---|
| C1 | "📄 (relationship depth 🎙️)" (L118). Markers: cross-sell not met; wallet share, AMC and workflow integration NOT FOUND (L81) | 1.0 |
| E1 | "The agreement is 📄, the economics are 🎙️" (L88). Impact H has no support other than the economics. The funded mine sits in the Optionality Register (L194), which is watched and never scored | 1.0 |
| R1 | "evidence mixed (aquifer awards 📄 but running off, forward items 🎙️)" (L158) | 0.7 |

Prompt 07 sets no mixed-evidence rule, so B07 needed one convention. It used two.

| Convention | C1 | E1 | R1 | Total | Band |
|---|---|---|---|---|---|
| As filed | 3.0 | 2.0 | 1.4 | 12.8 | MODEST |
| 0.7x on all three | 2.1 | 1.4 | 1.4 | 11.3 | NONE |
| 1.0x on all three | 3.0 | 2.0 | 2.0 | 13.4 | MODEST |
| 0.7x on C1 alone | 2.1 | 2.0 | 1.4 | 11.9 | NONE |

The 0.7x convention governs on Prompt 07 rule 4 ("Prioritise hard evidence over promises") and on the filed-evidence reading standard. That reading gives 11.3, NO MEANINGFUL EMERGING MOAT.

B07's FLAG-THRESHOLD-SENSITIVE names two moves below 12 (L189, YAML L268). It omits the multiplier. G1 at 0 (B07 itself writes "Not a war chest", L96) would also give 11.8.

The UA qualifier EM >= 25 stays unmet on every reading.

### 3.3 Other Emerging Moat rules

| # | Rule | B07 application | Result |
|---|---|---|---|
| 1 | Total sum | 12.8 (L186) | PASS |
| 2 | Band classification | 12-24 = MODEST on 12.8 | PASS on the filed total. See F3 |
| 3 | Completionist recount performed | Done, final line 11 items across 6 categories, plus 1 in 2A (L135). Sum 3+2+1+2+2+1 = 11 | PASS |
| 4 | Strong or Moderate count stated | 2, B2 and C1 (L134) | PASS |
| 5 | 12-category guard applied explicitly | 7 scored rows, below guard (L134) | PASS |
| 6 | I1 above 0 only with both legs (Verifier rule 8) | Scored 0 | PASS |
| 7 | I2 above 0 only with a named sacrifice (Verifier rule 8) | Scored 0 | PASS |
| 8 | I2 answered "for each moat claimed" | Answered for C1, B2, E1 (L106). Not for A1, G1, H2, R1. Score stays 0 | FAIL (F10, MINOR) |
| 9 | I1/I2 contribution stated separately | 0.0 (L188) | PASS |
| 10-15 | Sections 1 to 6 present | Each present in order | PASS (6 rules) |
| 16 | 2C arithmetic shown | 17.21 x 3.15 = 54.2 Cr, 22.3%; 24.98 x 3.15 = 78.7 Cr, 32.4%; closing-PPE range 45.6 to 66.2 Cr (L58, L59). Single-year FY26 turnover, range and caveat stated | PASS |
| 17 | Optionality Register table | Four required columns, 9 rows (L191 to L202) | PASS |
| 18 | Register carried in block | YAML holds 7 of 9 rows. Mineral block auctions (L200) and HZL ramp (L202) dropped (L287 to L294) | FAIL (F11, MINOR) |
| 19 | Taxonomy tag on every evidence item | Five Section 4B items carry no tag (L150, L151, L152, L153, L155) | FAIL (F12, MINOR) |
| 20 | Source anchors on every item | "AR p.?" (L71), "p.192 region" (L21), Board and secretarial report with no page (L92), secondary "per B05" and "B04" anchors (L16, L29, L47, L76) | FAIL (F13, MINOR) |
| 21 | 6C uses injected Gate 0 | Core 62, 3 moats, MODERATE, GOOD (L224 to L226). Matches B01 as filed | PASS |
| 22 | YAML block schema | All fields present, analyst_note under 200 words | PASS |
| 23 | evidence_mix item counts reproducible | YAML 12 / 11 / 3 (L277). Body tags: 24 management-claim tags, 1 inference tag (L61). Claim and inference counts do not reproduce. The recount line also shows its working twice, 12 then 11 (L135) | FAIL (F14, MINOR) |

## 4. FINDINGS

| ID | Severity | Location | Stated | Recomputed | Note |
|---|---|---|---|---|---|
| F1 | CRITICAL | B01 E1, L50 | E1 = 5 on 68.85% at 31 Mar 2026. Latest-quarter pattern marked NOT FOUND | E1 = 0, Block E 3, core 57, AVERAGE | Flips the Gate 0 decision line (L80). Two readings and separator in Section 1. GOOD stands at Sep 2026 promoter holding of 40% or above. If AVERAGE stands, the FLAG-GATE0 test opens and B07 6C and 6D need re-issue |
| F2 | MAJOR | B01 M11, L69 | M11 = 3 on FY23-26 CAGR 25.1% | M11 = 0, moats present 2, MODERATE, moat score 7, grand total 69 alone, 64 with F1 | M1 (L59) and C1 (L37) read "revenue CAGR" at 14.1%. Only tier 1 of M11 names a 3-year window. On 14.1%, tier 2 and tier 3 both fail. Second reading: tier 2 inherits tier 1's window, score stays 3. Separator: an operator clarification of the term. B01 itself says no network effect is evidenced (L71) |
| F3 | MAJOR | B07 C1 L81, E1 L88, R1 L158, total L186 | 12.8 MODEST on mixed multipliers | 11.3 NONE at 0.7x, 13.4 MODEST at 1.0x | Section 3.2. Moves the band, not a valuation input today |
| F4 | MINOR | B01 M8, L66 | "none quantified", score 0 | 0 or 1 | State which tier applies. Moat class does not move |
| F5 | MINOR | B01 L17, L18, L28, L32, L56, L61, L69 | Figures without page or source | n/a | Prompt 01 rule 4 |
| F6 | MINOR | B01 output | Moat profile bars absent | n/a | Prompt 01 Output section |
| F7 | MINOR | B01 L75, YAML data_years | 10 years, full, no downgrade | Text passes | 6 of 20 core metrics (A1, A2, A4, B2, B3, B4) rest on 3 years. The rule does not say how mixed coverage keys to the tiers. If keyed to the 3-year series, 3-4 LIMITED downgrades GOOD to AVERAGE. Operator ruling would close it |
| F8 | MINOR | B01 analyst_note, L128 | "not to evidence of a problem" | n/a | E2 scores 0 on "Decrease >3pp observed" (L51), and L80 flags promoter disposals. The note understates the observed fall |
| F9 | MINOR | B01 M2, M5, M9, L60, L63, L67, L123 | PEER DATA NEEDED, 0 | Not determinable | B01 input_gaps (L95) record Data_Sheet populated for main and peers. Rule scores 0 only if peer data is not provided. Verifier C's inputs cannot show what stage 1 received. Separator: the stage 1 dispatch input list. Upside direction: STRONG needs 4 or more moats present |
| F10 | MINOR | B07 I2, L106 | Answered for 3 of 7 scored rows | n/a | Score unchanged at 0 |
| F11 | MINOR | B07 YAML L287 to L294 | 7 of 9 register rows | 9 rows | Prompt 07 says the register is carried in the block. Two monitoring items are lost to synthesis if it reads the block only |
| F12 | MINOR | B07 L150 to L153, L155 | Five items untagged | n/a | Prompt 07 rule 2 |
| F13 | MINOR | B07 L16, L21, L29, L47, L71, L76, L92 | Placeholder or secondary anchors | n/a | Prompt 07 rule 3 |
| F14 | MINOR | B07 L135, L277 | evidence_mix 12 / 11 / 3 | Claim tags 24, inference tags 1 | Field cannot be reproduced from the body. Documented 12 is consistent with the recount |

Out of scope, not audited: B07 carries Q2 FY27 margin 14.38% (L54, YAML L296, L300) while B01 records that figure as not reproduced on filings (L8, YAML L125). This is a number and basis question for Verifier A.

```yaml
stage: B12c
company: "SOUTHWEST"
run_date: "2026-11-09"
model: "claude-opus-5-5"
status: complete
gate0:
  rules_checked: 64
  fails:
    - "E1: latest-quarter holding marked NOT FOUND but scored 5; recomputed 0, Block E 3, core 57, AVERAGE (F1, CRITICAL)"
    - "M11: rev CAGR read at 25.1% where M1 and C1 read 14.1%; recomputed 0, moats present 2, moat score 7 (F2, MAJOR)"
    - "M8: basis phrase none quantified does not identify the tier; 0 or 1 (F4, MINOR)"
    - "Rule 4 anchors: AR FY25 figures lack pages, moat inputs unanchored (F5, MINOR)"
    - "Output: moat profile bars absent (F6, MINOR)"
emoat:
  rules_checked: 60
  fails:
    - "C1 evidence tier: 1.0x on a row whose relationship depth is a management claim; recomputed 2.1 at 0.7x (F3, MAJOR)"
    - "E1 evidence tier: 1.0x with impact H resting on management-claim economics; recomputed 1.4 at 0.7x (F3, MAJOR)"
    - "I2: each-moat answer covers 3 of 7 scored rows; score unchanged (F10, MINOR)"
    - "Optionality register: block carries 7 of 9 rows (F11, MINOR)"
    - "Taxonomy: five Section 4B items untagged (F12, MINOR)"
    - "Anchors: AR p.? placeholder and secondary anchors (F13, MINOR)"
    - "evidence_mix claim and inference counts not reproducible (F14, MINOR)"
valuation: {rules_checked: 0, fails: []}  # pending: phase 3 (B10, B11 not in phase-1 scope)
expectation_ledger: {present: null, downside_row: null, all_rows_confirm_by: null, all_rows_metric_threshold: null, prob_in_range: null, decay_status_valid: null, off_ledger_credit: null, residual_pct_cmp: null, residual_starter_cap_ok: null, fails: []}  # pending: phase 3; null is not a finding; rules 13-14
# rule 9 (stage 13 narrative): pending, not in phase-1 scope; any fail = REWORK stage 13
recomputed_destination_pe: ""  # pending: phase 3
recomputed_decision: "Gate 0 only: GOOD (core 62) recomputes to AVERAGE (core 57) on E1 NOT FOUND = 0. GOOD stands if promoter holding for the quarter ended 30 Sep 2026 is 40% or above. EM band: MODEST (12.8) recomputes to NONE (11.3) on one 0.7x mixed-evidence convention."
findings:
  - {severity: CRITICAL, location: "B01 E1, 01-gate0.md L50", rule: "Prompt 01 rule 5; E1 latest quarter", stated: "E1 = 5 on 68.85% at 31 Mar 2026; latest-quarter pattern marked NOT FOUND", recomputed: "E1 = 0; Block E 3; core 57; AVERAGE", note: "E3 scored 0 on the same empty folder. Second reading: dated quarter-end is the latest available, GOOD stands. Separator: Sep 2026 shareholding pattern; GOOD stands at 40% or above."}
  - {severity: MAJOR, location: "B01 M11, 01-gate0.md L69", rule: "Prompt 01 M11 tier 2", stated: "M11 = 3 on FY23-26 CAGR 25.1%", recomputed: "M11 = 0; moats present 2; MODERATE; moat score 7; grand total 69 alone, 64 with F1", note: "M1 and C1 read revenue CAGR at 14.1%. Second reading: tier 2 inherits tier 1 window, score 3. Separator: operator clarification of the term."}
  - {severity: MAJOR, location: "B07 C1 L81, E1 L88, R1 L158, total L186", rule: "Prompt 12 Verifier C rule 3; Prompt 07 Section 5", stated: "12.8 MODEST; C1 and E1 at 1.0x, R1 at 0.7x, all three mixed", recomputed: "11.3 NONE at 0.7x on all three; 13.4 MODEST at 1.0x on all three; 11.9 NONE on C1 alone", note: "EM >= 25 UA qualifier unmet on every reading. FLAG-THRESHOLD-SENSITIVE omits the multiplier."}
  - {severity: MINOR, location: "B01 M8, L66", rule: "Prompt 01 M8", stated: "none quantified, 0", recomputed: "0 or 1", note: "State which tier applies."}
  - {severity: MINOR, location: "B01 L17, L18, L28, L32, L56, L61, L69", rule: "Prompt 01 rule 4", stated: "Figures without page or source", recomputed: "n/a", note: "AR FY25 pages and moat inputs."}
  - {severity: MINOR, location: "B01 output", rule: "Prompt 01 Output", stated: "Moat profile bars absent", recomputed: "n/a", note: "Presentational."}
  - {severity: MINOR, location: "B01 L75, data_years", rule: "Prompt 01 data confidence", stated: "10 years, full, no downgrade", recomputed: "Text passes", note: "6 of 20 core metrics rest on 3 years. Rule silent on mixed coverage. If keyed to 3 years, GOOD downgrades to AVERAGE. Operator ruling closes it."}
  - {severity: MINOR, location: "B01 analyst_note, L128", rule: "Consistency with E2 basis", stated: "not to evidence of a problem", recomputed: "n/a", note: "E2 scores 0 on an observed fall above 3pp (L51)."}
  - {severity: MINOR, location: "B01 M2, M5, M9, L95, L123", rule: "Prompt 01 Block F peer rule", stated: "PEER DATA NEEDED, 0", recomputed: "Not determinable", note: "input_gaps record Data_Sheet populated for peers. Separator: stage 1 dispatch input list."}
  - {severity: MINOR, location: "B07 I2, L106", rule: "Prompt 07 I2 each moat", stated: "Answered for C1, B2, E1", recomputed: "n/a", note: "A1, G1, H2, R1 not answered. Score stays 0."}
  - {severity: MINOR, location: "B07 YAML L287-L294", rule: "Prompt 07 Optionality Register", stated: "7 of 9 rows in block", recomputed: "9 rows", note: "Mineral block auctions and HZL ramp dropped."}
  - {severity: MINOR, location: "B07 L150-L153, L155", rule: "Prompt 07 rule 2", stated: "Five items untagged", recomputed: "n/a", note: "Section 4B policy rows."}
  - {severity: MINOR, location: "B07 L16, L21, L29, L47, L71, L76, L92", rule: "Prompt 07 rule 3", stated: "Placeholder or secondary anchors", recomputed: "n/a", note: "AR p.? at L71."}
  - {severity: MINOR, location: "B07 L135, L277", rule: "Prompt 07 evidence_mix item counts", stated: "12 / 11 / 3", recomputed: "Claim tags 24, inference tags 1", note: "Claim and inference counts do not reproduce from the body."}
critical_count: 1
major_count: 2
minor_count: 11
acceptance_rate: 90.3
```
