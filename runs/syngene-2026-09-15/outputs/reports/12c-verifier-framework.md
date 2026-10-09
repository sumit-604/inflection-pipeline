# STAGE 12 VERIFIER C: FRAMEWORK ADHERENCE, SYNGENE (PHASE 1 SCOPE, AUDIT RUN 2)

Run date: 2026-09-15 | Emits: B12c | Scope: Gate 0 (B01) and Emerging Moat (B07) only.
Valuation audit (B10, B11), Expectation Ledger (rules 13-14), and Business Understanding Narrative (rule 9) are out of phase 1 scope. They are marked PENDING PHASE 3 in the YAML. The Section 1B layer set, Master Role 1, and FTTCP were not loaded.

Rule sources applied:
- prompts/01-gate-0-pipeline.md (scoring thresholds, CAGR edge rules, classification matrix, deal-breakers, output schema)
- prompts/07-emerging-moat-pipeline.md (22-category scan plus R1, evidence taxonomy, likelihood x impact matrix, multipliers, completionist guard, I1/I2 rules, output schema)
- prompts/12-verifiers-pipeline.md, Verifier C rules 2, 3, 8

Artifacts audited:
- runs/syngene-2026-09-15/outputs/blocks/B01-gate0.yaml and reports/01-gate0.md
- runs/syngene-2026-09-15/outputs/blocks/B07-emoat.yaml and reports/07-emoat.md

Verifier C audits rule application only. Source fidelity (does a number exist at its anchor) belongs to Verifier A and is not ruled on here. Where a framework check touches an anchor, the finding is about the rule, and the fidelity question is left to Verifier A.

---

## PART 1: GATE 0 (B01) COMPLIANCE

### 1.1 Block re-derivation from stated inputs

All inputs below are the values B01 states. Verifier C recomputed each score from the prompt thresholds.

| Rule | Stated input (B01) | Threshold band applied by Verifier C | B01 score | Recomputed | Result |
|---|---|---|---|---|---|
| Opening line (rule 6) | "Data available: 9 years (FY2018 to FY2026)" | Required form present | present | present | PASS |
| A1 Median ROCE | FY24 13.34%, FY25 13.20%, FY26 8.35%; median 13.20% | 10-14.9 = 1 | 1 | 1 | PASS |
| A2 Min ROCE | 8.35% (FY26) | 8-11.9 = 1 | 1 | 1 | PASS |
| A3 Median ROE | 9 values; sorted 6.62, 11.04, 12.94, 12.95, **13.43**, 16.21, 17.75, 17.98, 19.89 | 12-14.9 = 2 | 2 | 2 | PASS |
| A4 ROCE trend | 13.34% to 8.35% = -4.99pp | decline 3-5pp = 1 | 1 | 1 | PASS |
| Block A | 1+1+2+1 | sum | 5 | 5 | PASS |
| B1 Cum CFO/PAT | 6,983.9 / 3,637.1 = 1.92 | >=1.00 = 5 | 5 | 5 | PASS |
| B2 FCF-positive years | FY24 531.3, FY25 397.5, FY26 547.0 (3 of 3) | 100% = 5 | 5 | 5 | PASS |
| B3 Cum FCF/PAT | 1,475.8 / 1,322.9 = 1.116 | >=0.60 = 5 | 5 | 5 | PASS |
| B4 WC days change | FY24 44.41 to FY26 29.56 = -14.85 days (components recomputed: 46.20+24.95-26.73; 49.67+13.79-33.93) | decreased >5 = 5 | 5 | 5 | PASS |
| Block B | 5+5+5+5 | sum | 20 | 20 | PASS |
| C1 Revenue CAGR | (3,738.7/1,423.1)^(1/8)-1 = 12.83% | 10-14.9 = 3 | 3 | 3 | PASS |
| C2 PAT CAGR | (316.7/305.4)^(1/8)-1 = 0.46% | <5 = 0 | 0 | 0 | PASS |
| C3 Positive YoY revenue | 8 of 8 | 100% = 5 | 5 | 5 | PASS |
| C4 PAT CAGR minus Rev CAGR | 0.46 - 12.83 = -12.37pp | <-8pp = 0 | 0 | 0 | PASS |
| Block C | 3+0+5+0 | sum | 8 | 8 | PASS |
| CAGR edge rules | Both endpoints positive for C1 and C2; no loss-to-profit swing; C4 not N/M | No N/M trigger; no swing note needed | honoured | honoured | PASS |
| D1 ND/EBITDA | Borrowings 458.4 less cash 833.0 = net cash 374.6 | net cash = 5 | 5 | 5 | PASS |
| D2 Interest cover | 459.7 / 48.8 = 9.42x | 5-9.9 = 4 | 4 | 4 | PASS |
| D3 D/E | 458.4 / 4,839.1 = 0.095 | <0.1 = 5 | 5 | 5 | PASS |
| D4 Current ratio | 21,428 / 15,523 = 1.38 | 1.2-1.49 = 2 | 2 | 2 | PASS |
| Block D | 5+4+5+2 | sum | 16 | 16 | PASS |
| E1 Promoter holding | 52.59% (Jun-2026) | 50-59.9 = 4 | 4 | 4 | PASS |
| E2 3-year change | Jun-2023 point NOT FOUND | rule 5: N/A scored 0 | 0 | 0 | PASS |
| E3 Pledge | N/A | rule 5: N/A scored 0 | 0 | 0 | PASS |
| E4 Contingent liab / NW | 531.2 / 4,703.8 = 11.29% | 5-15 = 3 | 3 | 3 | PASS |
| Block E | 4+0+0+3 | sum | 7 | 7 | PASS |
| Core score | 5+20+8+16+7 | sum | 56 | 56 | PASS |

### 1.2 Block F moat tests

| Test | Stated input (B01) | Band applied | B01 | Recomputed | Result |
|---|---|---|---|---|---|
| M1 Pricing power | EBITDA margin -8.65pp, rev CAGR 12.83% | decline >5pp falls to "else 0" | 0 | 0 | PASS |
| M2 Cost advantage | 24.64% vs 3-peer median 28.91% (-4.27pp) | below = 0 | 0 | 0 | PASS |
| M3 Capital efficiency | FAT 1.25x, ROCE FY26 8.35% | fails FAT>1x AND ROCE>12% | 0 | 0 (see Obs G-O1) | PASS |
| M4 Customer stickiness | 0 decline years; receivable days -18.75 (outside +/-10) | fails 5 tier; "max 1 decline year" = 3 | 3 | 3 | PASS |
| M5 Scale | PEER DATA NEEDED | missing peer data = 0 | 0 | 0 (see Obs G-O2) | PASS |
| M6 R&D | R&D line blank, NOT FOUND | rule 5 = 0 | 0 | 0 | PASS |
| M7 Regulatory | player count PEER DATA NEEDED | missing peer data = 0 | 0 | 0 | PASS |
| M8 Distribution | none (B2B CRDMO) | none = 0 | 0 | 0 | PASS |
| M9 Brand (GM proxy) | +4.76pp vs median 71.06%, growth 12.83% | above peers, below 5pp tier; nearest tier = 1 (see Obs G-O3) | 1 | 1 | PASS |
| M10 Switching costs | revenue grew every year; receivable days fell (rise <=10) | = 5 | 5 | 5 | PASS |
| M11 Network effects | 9 yrs, two-window valid; FY23-26 5.40% < FY20-23 16.65% | no tier reachable | 0 | 0 | PASS |
| M12 Negative WC | 44.41, 33.08, 29.56 days, all 15-45 | 15-45 = 1 | 1 | 1 | PASS |
| Moat score | 0+0+0+3+0+0+0+0+1+5+0+1 | sum | 10 | 10 | PASS |
| Moats present (>=3) | M4, M10 | 2 = MODERATE (2-3 band) | MODERATE | MODERATE | PASS |
| Grand total | 56 + 10 | sum | 66 | 66 | PASS |

### 1.3 Classification, overrides, output

| Rule | Check | Result |
|---|---|---|
| Data confidence tier | 9 years = moderate (7-9); no downgrade. B01 states the 3-year ROCE and B2-B4 windows as per-metric gaps, not a history downgrade (see Obs G-O4) | PASS |
| Classification matrix | Core 56 in 40-59 = AVERAGE, moat tier irrelevant in this band | PASS |
| Deal-breaker 1 (Block A <8) | Block A 5, triggered, caps max GOOD, non-binding | PASS |
| Deal-breakers 2-9 | Each stated with input: B 20; median ROCE 13.20%; CFO/PAT 1.92; pledge N/A; net cash and IC 9.42x; no revenue decline; PAT positive FY24-26; 9 years | PASS |
| Deal-breaker years stated | Prompt: "state WHICH years drive any deal-breaker". Deal-breaker 1 line (report and YAML) names no years. FY26 as the driver is only inferable from the Block A table | **FAIL (MINOR) G-F1** |
| Rule 5 grounded claims | E2, E3, M6 scored 0 as N/A; M5, M7 marked PEER DATA NEEDED | PASS |
| WC days basis stated | Revenue basis stated, COGS absence explained | PASS |
| Rule 4 source anchors | FY24 capital employed row cites "AR2025 p. consol BS, Total current liabilities FY24" with no page number | **FAIL (MINOR) G-F4** |
| FLAG-GATE0 | Classification AVERAGE with named depressors; flag present | PASS |
| block_b_trend | "deteriorating" with the one number (CFO -21.6% YoY) | PASS |
| analyst_note length | about 167 words, under 200 | PASS |
| analyst_note accuracy | Says "peer-relative margin tests (M1, M2) failing against ANTHEM and SAILIFE". M1 is an own-history test (FY18 33.29% to FY26 24.64%), not peer-relative | **FAIL (MINOR) G-F2** |
| YAML schema | Block file B01-gate0.yaml carries non-schema key `run: 2`. The YAML embedded in 01-gate0.md does not. The two copies differ | **FAIL (MINOR) G-F3** |
| Output format | Prompt requires "moat profile bars" and a classification box in the dashboard. Report gives a moat table and a classification section, no profile bars | **FAIL (MINOR) G-F5** |

### 1.4 Gate 0 correction closure (run 1 audit items, as logged by B01)

| B01 log item | Verified in run 2 artifacts | Status |
|---|---|---|
| 1 A1 band | A1 = 1 on 13.20% | CLOSED |
| 2 B2/B3/B4/M12 window | 3-year window FY24-26 used, scores re-derived | CLOSED |
| 3 WC basis | Stated | CLOSED |
| 4 Deal-breakers 2 and 6 | Stated with inputs | CLOSED |
| 5 E2 proxy | E2 = 0 per rule 5 | CLOSED |
| 6 data_notes, M6 label | M9 proxy, M5/M7, M6 NOT FOUND notes present | CLOSED |
| 7 Site conflation | Unit 3 vs Bayview separated | CLOSED (fact fidelity: Verifier A) |
| 8 Exceptional total | Rs 766mn consolidated with components | CLOSED (fact fidelity: Verifier A) |
| 9 FCF re-check | Arithmetic consistent | CLOSED |

### 1.5 Gate 0 observations (no severity, not counted as fails)

- **G-O1 M3 ROCE basis.** B01 uses FY26 spot ROCE 8.35%. The rule does not name spot or median. On median ROCE 13.20% with FAT 1.25x, M3 = 1. Moat score would be 11 and grand total 67. Moats present (2), moat class, and classification do not change. B01 uses FY26 spot for M2 as well, so the choice is internally consistent.
- **G-O2 M5 peer set.** M2 and M9 accept the 3-peer set as the peer median. M5 rejects the same set as the segment universe. On the 4 supplied names Syngene ranks 4th, so a literal "top 5 mcap = 1" reading gives M5 = 1. That reading is trivial on 4 names. The PEER DATA NEEDED treatment is defensible. No moat-count effect either way.
- **G-O3 M9 band gap and proxy.** The M9 bands leave "above peers by under 5pp with growth at or above 8%" unassigned. B01 fills it with 1, the nearest tier. B01 also adjusts the stated proxy for change in inventory and states it.
- **G-O4 Data confidence keying.** The prompt keys the tier to "data available" years. B01 has 9 years for revenue, PAT, and CFO, and 3 years for ROCE and B2-B4. B01 follows the text. A reading keyed to the shortest scored window would give LIMITED (3-4 years) and move AVERAGE down one tier to AVOID. The prompt does not support that reading, so this is not a fail. It is an operator ruling candidate for the prompt.
- **G-O5 E4 basis.** Both legs are standalone, so the ratio is internally consistent. Elsewhere the scorecard runs on a consolidated basis. Basis traps belong to Verifier A.
- **G-O6 M4 and M10 overlap.** Both tests credit the same revenue-growth and receivable-day evidence. This is rubric design, not a stage error. It is noted for the one-improvement-one-mechanism rule downstream.

---

## PART 2: EMERGING MOAT (B07) COMPLIANCE

### 2.1 Structural and coverage rules

| # | Rule | Check | Result |
|---|---|---|---|
| E-1 | Not FTTCP, no conflation | Banner states separate analysis | PASS |
| E-2 | Evidence taxonomy on every item | DOC/CLAIM/INFER applied across Sections 1-4 | PASS |
| E-3 | Source anchors on every evidence item (rule 3) | Residual defects: approximate pages "p.~9", "p.~50", "p.~52", "p.~85", "p.~217"; "AR26 p.242/15706" in 2A (15706 reads as a text-file line number, the same defect type log item 1 says was fixed); pipeline-block anchors in place of document pages ("per B02 finding 3", "B03 monitorables, AR highlights", "Note 10, per B02", "B04, Ind AS 108") | **FAIL (MINOR) E-F1** |
| E-4 | NO EVIDENCE FOUND stated where none | A2, A4, B1, B3, D2, H1, I1 stated; F2 and G1 scored 0 as negative findings, stated | PASS |
| E-5 | Completionist guard and recount line | "📄 recount performed: 18 documented items across 10 categories" present; 4 Strong/Moderate, inside 3-6 | PASS |
| E-6 | Recount and evidence_mix accuracy | evidence_mix states 3 CLAIM, 2 INFER. Section 3 shows at least 4 CLAIM rows (B2 Amgen, D1, E2 x2) and 1 INFER row (A3), since the E1 inference row was removed. E1 is listed as a DOC category in the recount but scored at INFER in Section 5. The "23 rows across 22 categories + R1" total counts R1, which sits in Section 4 | **FAIL (MINOR) E-F2** |
| E-7 | Section 1 (1A, 1B, 1C) | Present | PASS |
| E-8 | Section 2 (2A-2D) | Present | PASS |
| E-9 | 2C arithmetic shown | 1,040 x (3,739/3,006 = 1.24) = 1,290; 1,290/3,739 = 34.5%. Recomputed and matches YAML 34.5 | PASS |
| E-10 | All 22 categories plus R1 addressed | 23 rows in summary table, each with evidence or NO EVIDENCE | PASS |
| E-11 | Section 3 summary table and Strong/Moderate count | Present, count 4 | PASS |
| E-12 | Category 21 I1 (Verifier rule 8) | Present; scored 0; part (a) and (b) both absent; no score above 0 | PASS |
| E-13 | Category 22 I2 (Verifier rule 8) | Present; tested per claimed moat (A1, B2/C1/H2, F1, H3); no named specific sacrifice; 0 | PASS |
| E-14 | Section 4 (4A, 4B, 4C) | Present | PASS |

### 2.2 Scorecard re-derivation (Section 5)

Matrix: HH=4, HM/MH=3, HL/MM/LH=2, ML/LM=1, LL=1, none=0. Multipliers: DOC 1.0, CLAIM 0.7, INFER 0.5.

| Cat | L/I stated | Raw (recomputed) | Tier stated in Section 5 | Tier stated in Section 3 | Adjusted (B07) | Recomputed | Result |
|---|---|---|---|---|---|---|---|
| A1 | MH | 3 | DOC | DOC (4 rows) | 3.0 | 3.0 | PASS |
| A3 | LL | 1 | INFER | INFER | 0.5 | 0.5 | PASS |
| B2 | MM | 2 | DOC | DOC, strength Weak | 2.0 | 2.0 arithmetic; label conflict | see E-F4 |
| C1 | LH | 2 | DOC | DOC, strength Weak | 2.0 | 2.0 arithmetic; label conflict | see E-F4 |
| C2 | LL | 1 | DOC | DOC | 1.0 | 1.0 | PASS |
| D1 | LL | 1 | CLAIM | CLAIM | 0.7 | 0.7 | PASS |
| E1 | LM | 1 | **INFER** | **DOC** (summary table and prose; inference row removed) | 0.5 | 1.0 if DOC; 0 if category has no first-mover basis | **FAIL E-F3** |
| E2 | LL | 1 | CLAIM | CLAIM | 0.7 | 0.7 | PASS |
| F1 | MM | 2 | DOC | DOC, strength Moderate | 2.0 | 2.0 | PASS |
| G2 | LL | 1 | DOC | DOC | 1.0 | 1.0 | PASS |
| H2 | MH | 3 | DOC | DOC | 3.0 | 3.0 | PASS |
| H3 | HL | 2 | DOC | DOC | 2.0 | 2.0 | PASS |
| R1 | LL | 1 | CLAIM | CLAIM | 0.7 | 0.7 | PASS |
| Others | none | 0 | n/a | n/a | 0 | 0 | PASS |
| **Total** | | | | | **19.1** | **19.1 as scored** | PASS (arithmetic) |

| # | Rule | Check | Result |
|---|---|---|---|
| E-15 | Raw score from L x I matrix | All 13 non-zero mappings correct | PASS |
| E-16 | Multiplier matches stated evidence tier | E1 scored at INFER 0.5 while Section 3 and the summary table tier it DOC, and the only INFER row was removed | **FAIL (MINOR) E-F3** |
| E-17 | Scores consistent with stated evidence and strength (no CLAIM scored as DOC; labels coherent) | No CLAIM-only category scored at DOC weight: PASS on that leg. Label leg fails. B2 (Weak, MM=2) and C1 (Weak, LH=2) carry the same raw 2 as Moderate rows F1 (MM=2) and H3 (HL=2). Log item 6 moved C2 from MM to LL because it was labelled Weak. The same logic applied to B2 and C1 gives raw 1 each | **FAIL (MINOR) E-F4** |
| E-18 | Adjusted total arithmetic | 19.1 | PASS |
| E-19 | Classification, absolute bands | 19 in 12-24 = MODEST | PASS |
| E-20 | I1/I2 contribution stated separately | "0 of the 19.1 total" | PASS |
| E-29 | One improvement, one mechanism | BMS 2035 credited once (H2): PASS. Bayview site: A1 credits the facility, application, and BioHub row. E1 now rests only on "the site exists" because its first-mover basis was marked NOT FOUND. That residual is the A1 evidence credited a second time (0.5 points) | **FAIL (MINOR) E-F3** |

**Sensitivity of the recomputed total (all within the MODEST band, 12-24):**
- E1 at DOC 1.0: 19.6.
- E1 at 0 (no first-mover basis, residual duplicates A1): 18.6.
- B2 and C1 at raw 1 each (Weak held): minus 2.0.
- Combined range across the readings: 16.6 to 19.6. em_classification MODEST holds in every case. The UA EM >= 25 qualifier stays unmet in every case.

### 2.3 Output, register, Section 6

| # | Rule | Check | Result |
|---|---|---|---|
| E-21 | Optionality register table and YAML | 8 rows, required columns, carried as optionality_register[] | PASS |
| E-22 | Register holds only 0-scored or CLAIM/INFER-only forward items, never scored | Bayview row is the forward customer-fill claim, distinct from A1's facility status; stage states this | PASS |
| E-23 | catalysts_12m inside 12 months | Sep-2026, FY27, FY27, H2 FY27; all before Sep-2027 | PASS |
| E-24 | 6A four windows | Present | PASS |
| E-25 | 6B risks per top moat with early warnings | A1/H2, H3, F1 covered | PASS |
| E-26 | 6C uses injected Gate 0 block | 56, 2, MODERATE, AVERAGE match B01 | PASS |
| E-27 | 6D combined classification with reasoning | AVERAGE; reasoning given. The matrix grid is not reproduced in the rule source, so Verifier C checks consistency with the named rows only | PASS |
| E-28 | 6E card and existing moats carried from the injected B01 block | 6E states "Existing (Gate 0, 2 confirmed): switching costs (dedicated R&D centres, BMS to 2035) and regulatory licence (USFDA/EMA/...)". B01's 2 confirmed moats are M4 Customer Stickiness (3) and M10 Switching Costs (5), both computed from revenue-growth and receivable-day arithmetic. M7 Regulatory scored 0, PEER DATA NEEDED. B01 names no BMS or dedicated-centre evidence. Section 3 B2/C1 and 4C repeat the claim that "Gate 0's moats_confirmed already counts" BMS and the regulatory pieces, and use it to justify the existing-moat exclusion. The rationale sources to B04's moats_present list, and B04 is not a stage 7 injected input. The de-duplication result stands on the no-double-credit rule alone. The stated basis is wrong, and the moat evolution map carries the error downstream. The 4C exclusion also runs inconsistently: it removes BMS from B2/C1 as "existing" but still scores the Unit 3 USFDA VAI row (which 4C itself calls existing-moat territory) under A1, and the certs row under B2 | **FAIL (MAJOR) E-F5** |
| E-30 | NOT FOUND discipline, no estimates or out-of-corpus numbers | (a) 1C carries "61% / 39% FY26 full year (B04, Ind AS 108 single-segment estimate)" in the Current % column: an estimate in a number cell. (b) 2A and input_gaps keep "$36.5mn (EXTERNAL, SEC/press disclosure; NOT FOUND IN THIS RUN'S CORPUS)": a number the stage itself says is not in corpus, with no document anchor. (c) 1B still names "Emergent BioSolutions" and "Mar-2025" while input_gaps says seller identity and date were removed as NOT FOUND. B01 separately cites the Bayview seller as "Emergent Manufacturing Operations Baltimore, LLC" at results FY26 audited p.9, note 8. The two stages disagree on whether the fact is in corpus. Verifier A owns the fidelity call | **FAIL (MINOR) E-F6** |
| E-31 | YAML schema, block embedded in report | Keys match schema; block file and embedded YAML identical; no placeholder key | PASS |
| E-32 | analyst_note <= 200 words | 192 words | PASS |

### 2.4 Emerging Moat correction closure (run 1 audit items, as logged by B07)

| B07 log item | Verified in run 2 artifacts | Status |
|---|---|---|
| 1 Company-memory anchors | Mostly re-anchored; residual block-anchors, approximate pages, and a line-number residue remain (E-F1) | PARTIALLY CLOSED |
| 2 BMS triple credit | Credited once under H2 | CLOSED (rationale defect E-F5) |
| 3, 10 USD-INR rate | INR conversion removed; $36.5mn external figure retained (E-F6) | PARTIALLY CLOSED |
| 4 Recount category count | 10 categories listed and stated | CLOSED on count; mix tally still off (E-F2) |
| 5 A1 tier | DOC 1.0, 3.0 | CLOSED |
| 6 C2 score vs Weak label | LL, 1.0 | CLOSED for C2; same logic not carried to B2, C1 (E-F4) |
| 7 I2 per moat | Applied to each claimed moat | CLOSED |
| 8 catalysts_12m window | All within 12 months | CLOSED |
| 9 YAML embed, placeholder key, mid-20s | All fixed | CLOSED |

### 2.5 Emerging Moat observations (no severity, not counted)

- **E-O1 Section 5A UA check.** This section is not part of the stage 7 rule set. The stage added it at operator request. The qualifier text ("Gate 0 core >= 60 OR EM >= 25; FII+DII < 3%; listed >= 12 months") cites Master/Amendment 3, which is out of phase 1 scope. Verification of the qualifier wording is deferred to phase 3. Section 5A treats high institutional ownership as a disqualifier from a mechanism, not as a risk, so the NEVER rule on institutional ownership holds. The section writes the EM score as "19/92" against a qualifier stated "/100". The difference is cosmetic.
- **E-O2 Completionist guard trigger.** The guard fires at "12 or more categories as active". The YAML schema defines active as Strong/Moderate (4). Thirteen categories carry a non-zero score. Under a "scored above zero" reading the guard would trigger. The stage performed the recount anyway.
- **E-O3 2C turnover basis.** 2C uses single-year FY26 FAT, not a multi-year "historical" FAT. The stage labels the result a ceiling, not a forecast.
- **E-O4 I2 location count.** The analyst_note says "all five claimed-moat locations" and lists four groupings (A1, B2/C1/H2, F1, H3). Cosmetic.
- **E-O5 R1 tier.** R1 is scored at CLAIM on sector policy tailwinds, although 4A lists the DOC Bayview pre-check application. Scoring R1 on that DOC item would credit Bayview a second time beside A1. The stage's choice avoids a double credit.

---

## PART 3: VALUATION (B11, B10), EXPECTATION LEDGER, BUSINESS UNDERSTANDING NARRATIVE

PENDING PHASE 3. Not audited in this run. No valuation framework document was opened. Verifier rules 4-7 and 9-14 were not applied.

---

## SUMMARY

| Scope | Rules checked | Fails | Passed |
|---|---|---|---|
| Gate 0 (B01) | 48 | 5 (all MINOR) | 43 |
| Emerging Moat (B07) | 32 | 7 rule fails, from 6 findings (1 MAJOR, 5 MINOR) | 25 |
| Valuation | 0 | PENDING PHASE 3 | n/a |
| **Total** | **80** | **12** | **68 (85%)** |

No finding changes a score band, a classification, a moat class, or a deal-breaker outcome. B01 AVERAGE / core 56 / MODERATE and B07 MODEST / 19 / combined AVERAGE survive every recomputed reading above. The one MAJOR (E-F5) is a wrong statement of what Gate 0 confirmed. It feeds the existing-moat map that downstream stages read.

```yaml
stage: B12c
company: "SYNGENE"
run_date: "2026-09-15"
model: claude-opus-5
status: complete
scope: "PHASE 1 (Gate 0 + Emerging Moat only); audit run 2 on corrected stage outputs"
gate0:
  rules_checked: 48
  fails:
    - {id: "G-F1", severity: "MINOR", rule: "Deal-breakers: state WHICH years drive any deal-breaker", detail: "Deal-breaker 1 (Block A 5 <8) line names no driving years in report or YAML; FY26 (ROCE 8.35%) only inferable from Block A table"}
    - {id: "G-F2", severity: "MINOR", rule: "analyst_note accuracy", detail: "Describes M1 as a peer-relative test failing against ANTHEM/SAILIFE; M1 is an own-history margin trend test (FY18 33.29% to FY26 24.64%)"}
    - {id: "G-F3", severity: "MINOR", rule: "Output YAML schema", detail: "B01-gate0.yaml carries non-schema key run: 2; embedded YAML in 01-gate0.md does not; the two copies differ"}
    - {id: "G-F4", severity: "MINOR", rule: "Rule 4 source anchors mandatory", detail: "FY24 capital employed / Total current liabilities cited 'AR2025 p. consol BS' with no page number; fidelity owned by Verifier A"}
    - {id: "G-F5", severity: "MINOR", rule: "Output dashboard format", detail: "Moat profile bars required by the output spec are absent (table only)"}
emoat:
  rules_checked: 32
  fails:
    - {id: "E-F1", severity: "MINOR", rule: "Rule 3 source anchors on every evidence item", detail: "Approximate pages (p.~9, p.~50, p.~52, p.~85, p.~217); 'AR26 p.242/15706' line-number residue in 2A; pipeline-block anchors (B02 finding 3, B03 monitorables, Note 10 per B02, B04) used in place of document pages"}
    - {id: "E-F2", severity: "MINOR", rule: "Completionist recount / evidence_mix accuracy", detail: "evidence_mix 3 CLAIM / 2 INFER does not reconcile to Section 3 rows (>=4 CLAIM: B2 Amgen, D1, E2 x2; 1 INFER: A3); E1 listed as DOC category but scored INFER; 23-row total counts R1 from Section 4"}
    - {id: "E-F3", severity: "MINOR", rule: "Multiplier matches stated tier; one improvement one mechanism", detail: "E1 scored INFER 0.5 while Section 3 and summary table tier it DOC and its INFER row was removed; residual E1 evidence (Bayview site exists) duplicates A1's credit. Recomputed E1 = 1.0 (DOC) or 0 (no first-mover basis); total 19.6 or 18.6; MODEST unchanged"}
    - {id: "E-F3b", severity: "MINOR", rule: "One improvement one mechanism (same root as E-F3)", detail: "Bayview site credited via A1 and E1; counted as a separate rule fail, single finding"}
    - {id: "E-F4", severity: "MINOR", rule: "Scores consistent with stated strength", detail: "B2 (Weak, MM=2) and C1 (Weak, LH=2) carry the same raw as Moderate F1/H3; stage's own log item 6 logic (Weak -> LL) gives raw 1 each; total minus 2.0; MODEST unchanged"}
    - {id: "E-F5", severity: "MAJOR", rule: "6C/6E carry existing moats from injected B01 block; no-double-credit rationale", detail: "6E, Section 3 B2/C1 and 4C state Gate 0 moats_confirmed counts BMS/dedicated centres and regulatory licence; B01 confirmed moats are M4 Customer Stickiness and M10 Switching Costs on revenue/receivable-day arithmetic, M7 Regulatory scored 0 PEER DATA NEEDED. Rationale sources to B04, not an injected stage 7 input; 4C exclusion applied to BMS but not to the Unit 3 USFDA VAI row scored in A1. Scores unchanged; moat evolution map misstated downstream"}
    - {id: "E-F6", severity: "MINOR", rule: "NOT FOUND discipline; no estimates", detail: "1C carries a B04 'single-segment estimate' 61%/39% in the Current % cell; 2A retains $36.5mn declared not in corpus; 1B names Emergent BioSolutions / Mar-2025 though input_gaps says removed, while B01 cites the Bayview seller at results FY26 audited p.9 note 8 (fidelity to Verifier A)"}
valuation: {rules_checked: 0, fails: [], status: "PENDING PHASE 3 - B10/B11 not in phase 1 scope"}
expectation_ledger: {present: false, downside_row: false, all_rows_confirm_by: false, all_rows_metric_threshold: false, prob_in_range: false, decay_status_valid: false, off_ledger_credit: false, residual_pct_cmp: 0, residual_starter_cap_ok: true, fails: [], status: "NOT AUDITED - PENDING PHASE 3 (rules 13-14); default values are placeholders, not findings"}
business_understanding_narrative: {present: false, five_questions_answered: false, prose_only: false, section6_candidates_named: 0, valuation_vocab_leak: false, fails: [], status: "NOT AUDITED - stage 13 not in phase 1 scope; default values are placeholders, not findings"}
recomputed_destination_pe: ""
recomputed_decision: ""
findings:
  - {severity: "MAJOR", location: "07-emoat.md 6E moat evolution map; Section 3 B2/C1; 4C", rule: "Existing moats carried from injected B01", finding: "Gate 0 confirmed moats misstated as BMS/dedicated centres + regulatory licence; B01 confirmed M4 and M10 only, M7 = 0", recomputed: "Existing (Gate 0, 2 confirmed): M4 Customer Stickiness (3), M10 Switching Costs (5); no score change"}
  - {severity: "MINOR", location: "07-emoat.md Section 5 row E1; Section 3 E1", rule: "Multiplier vs stated tier; one improvement one mechanism", finding: "E1 scored INFER 0.5 against DOC tier; residual evidence duplicates A1", recomputed: "E1 1.0 (total 19.6) or 0 (total 18.6); MODEST"}
  - {severity: "MINOR", location: "07-emoat.md Section 5 rows B2, C1", rule: "Scores consistent with strength label", finding: "Weak rows scored raw 2, same as Moderate rows; conflicts with log item 6 logic", recomputed: "raw 1 each; total 17.1 (or 16.6 with E1 at 0); MODEST"}
  - {severity: "MINOR", location: "B07-emoat.yaml evidence_mix, completionist_recount", rule: "Recount accuracy", finding: "3 CLAIM / 2 INFER does not reconcile to Section 3 rows", recomputed: ">=4 CLAIM, 1 INFER on Section 3 as written"}
  - {severity: "MINOR", location: "07-emoat.md 1A, 1C, 2A, 2D, C2, G2, H3", rule: "Rule 3 anchors", finding: "Approximate pages, line-number residue p.242/15706, pipeline-block anchors", recomputed: ""}
  - {severity: "MINOR", location: "07-emoat.md 1B, 1C, 2A; B07 input_gaps", rule: "NOT FOUND discipline", finding: "Estimate in 1C number cell; out-of-corpus $36.5mn retained; seller name retained while marked removed; conflicts with B01 note 8 citation", recomputed: ""}
  - {severity: "MINOR", location: "01-gate0.md Deal-breakers; B01 deal_breakers", rule: "State which years drive deal-breaker", finding: "No years named for deal-breaker 1", recomputed: "Driver: FY26 ROCE 8.35% (A2, A4); window FY24-FY26"}
  - {severity: "MINOR", location: "B01 analyst_note", rule: "analyst_note accuracy", finding: "M1 described as peer-relative", recomputed: "M1 = own-history margin trend, -8.65pp"}
  - {severity: "MINOR", location: "B01-gate0.yaml", rule: "YAML schema", finding: "Non-schema key run: 2; block and embedded YAML differ", recomputed: ""}
  - {severity: "MINOR", location: "01-gate0.md Block A table FY24 row", rule: "Rule 4 anchors", finding: "AR2025 page missing for FY24 current liabilities", recomputed: ""}
  - {severity: "MINOR", location: "01-gate0.md output", rule: "Dashboard format", finding: "Moat profile bars absent", recomputed: ""}
critical_count: 0
major_count: 1
minor_count: 10
acceptance_rate: 85             # 68 rules passed / 80 rules checked (gate0 43/48, emoat 25/32); valuation not in scope
observations_not_counted: "G-O4: Gate 0 data-confidence tier keys to 9-year 'data available' per prompt text; a shortest-window reading (3-year ROCE/B2-B4) would give LIMITED and move AVERAGE to AVOID; prompt does not support it; operator ruling candidate. G-O1: M3 on median ROCE would score 1 (moat 11, grand total 67), no class change. E-O1: Section 5A UA qualifier wording deferred to phase 3."
```
