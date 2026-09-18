# STAGE 12 VERIFIER C: FRAMEWORK ADHERENCE, PHASE 1 (TRUALT, 2026-09-18)
Model: claude-opus-5 | Scope: Gate 0 (B01) and Emerging Moat (B07) only. Valuation audit (B10, B11), Expectation Ledger (rules 13-14), Business Understanding Narrative (rule 9) and skill fidelity (rule 15): PENDING PHASE 3.

Rule sources: prompts/01-gate-0-pipeline.md ("G0 prompt"), prompts/07-emerging-moat-pipeline.md ("EM prompt").
Artifacts audited: outputs/reports/01-gate0.md + outputs/blocks/B01-gate0.yaml; outputs/reports/07-emoat.md + outputs/blocks/B07-emoat.yaml.
Numbers are taken as stated in B01/B07 (Verifier A owns source fidelity). This audit re-derives scores from the stated inputs and checks rule application only.

---
## PART 1: GATE 0 (B01) COMPLIANCE

### 1A. Block re-derivation from stated inputs

| # | Rule | B01 input (as stated) | Recomputed | B01 score | Recomputed score | Result |
|---|---|---|---|---|---|---|
| 1 | Opening "Data available" line (G0 rule 6) | 4 yrs FY23-FY26 | present (01-gate0.md l.4) | - | - | PASS |
| 2 | Formula definitions (ROCE, ROE, WC days, FCF, CAGR) | EBIT = PBT + interest; CE = TA - CL; ROE on avg NW; WC on revenue basis (stated) | all arithmetic re-run, ties | - | - | PASS (see obs. O1) |
| 3 | A1 median ROCE | 5.96 / 10.76 / 13.85 / 15.29 | median 12.305% | 1 | 1 | PASS |
| 4 | A2 min ROCE | 5.96% (FY23) | <8% | 0 | 0 | PASS |
| 5 | A3 median ROE | 8.38 / 12.60 / 14.75 / 28.38 | median 13.675% | 2 | 2 | PASS |
| 6 | A4 ROCE trend | 10.76 vs 5.96 | latest >= earliest | 5 | 5 | PASS |
| 7 | B1 cumul CFO/PAT | 315.37 / 309.86 | 1.018 | 5 | 5 | PASS |
| 8 | B2 FCF-positive years | -42.05, -321.32, +82.43, -806.31 | 1 of 4 = 25% | 0 | 0 | PASS |
| 9 | B3 cumul FCF/PAT | -1,087.25 / 309.86 | -3.51 | 0 | 0 | PASS |
| 10 | B4 WC days change | -32.9 to +140.0 | +172.9 days | 0 | 0 | PASS |
| 11 | C1 revenue CAGR | 762.38 to 1,727.51, 3 yrs | 31.35% | 5 | 5 | PASS |
| 12 | C2 PAT CAGR | 35.46 to 95.95, 3 yrs | 39.35% | 5 | 5 | PASS |
| 13 | C3 positive YoY years | +60.5, +56.0, -9.4 | 66.7% (band 50-74) | 1 | 1 | PASS |
| 14 | C4 PAT CAGR - Rev CAGR | 39.4 - 31.4 | +8.0pp | 5 | 5 | PASS |
| 15 | D1 ND/EBITDA | 1,561.74 / 300.29 | 5.20x (5.39x on annual 289.75) | 0 | 0 | PASS (obs. O1) |
| 16 | D2 interest cover | 289.97 / 160.02 | 1.81x | 1 | 1 | PASS |
| 17 | D3 D/E | 1,651.51 / 1,520.33 | 1.086x | 1 | 1 | PASS |
| 18 | D4 current ratio | 1,478.75 / 1,084.73 | 1.363x | 2 | 2 | PASS |
| 19 | E1 promoter holding | 70.55% | >=60% | 5 | 5 | PASS |
| 20 | E2 promoter change over 3 yrs | no 3-yr series; B01 used Mar-2026 to Jun-2026 (3 months) | N/A per G0 rule 5 | 3 | 0 | **FAIL (MAJOR)** |
| 21 | E3 pledge | 36.85% of promoter holding (26.00% of total) | >15% on either basis | 0 | 0 | PASS |
| 22 | E4 contingent liab/NW | Nil (AR note 57) | 0% | 5 | 5 | PASS |

Block totals, as stated vs recomputed: A 8 / 8; B 5 / 5; C 16 / 16; D 4 / 4; E 13 / **10**. Core 46 / **43**.

**F-E2 (MAJOR).** G0 prompt rule 5: "If a data point is not available, mark it 'N/A (not in provided data)' and score it 0." Rule 2: "No qualitative judgments." E2 asks for the promoter holding change over 3 years. B01 states no 3-year series exists (listed 03-Oct-2025), then substitutes a 3-month window (Mar-2026 to Jun-2026, 0.00pp) and scores 3 (01-gate0.md l.229-240). The substitution and the "IPO dilution is not selling" reading are both judgment calls the rule does not permit. As written, E2 = N/A, score 0. The only filed actual comparison in the data (pre-offer 88.20% to 70.55%, prospectus p.24 and SHP Jun-2026) would also score 0 (decrease >3%). Either route gives 0. Recomputed: Block E 10, Core 43, Grand total 58 before the moat corrections below. Classification unchanged (Core 40-59 band = AVERAGE, then AVOID).

### 1B. Moat tests (Block F)

| # | Test | B01 reading | B01 score | Recomputed | Result |
|---|---|---|---|---|---|
| 23 | M1 pricing power | 13.78% to 16.77% (+2.99pp), rev CAGR 31.4% | 5 | 5 | PASS |
| 24 | M2 cost advantage | 16.77% vs peer median 8.72% (+8.05pp) | 5 | 5 | PASS |
| 25 | M3 capital efficiency | FAT 0.79x | 0 | 0 | PASS |
| 26 | M4 customer stickiness | 1 decline year (FY26), not recovered | 0 | 1 | **FAIL (MINOR)** |
| 27 | M5 scale and dominance | ranked 3rd of 4 by mcap, 1st by margin | 3 | 3 on provided set; unverified vs the segment B01 itself defines | **FAIL (MINOR)** |
| 28 | M6 technology/R&D | no R&D line | 0 | 0 | PASS |
| 29 | M7 regulatory/licence | "well over 10" listed players | 1 | 1, count unanchored | **FAIL (MINOR)** |
| 30 | M8 distribution | "no retail/distribution network" | 0 | 1 (conservative) to 3 (literal) | **FAIL (MAJOR)** |
| 31 | M9 brand | GM proxy +1.24pp vs median 25.99% | 1 | 1 | PASS |
| 32 | M10 switching costs | growth all but 1 yr, receivable days +44.4 | 0 | 0 (explicit "else 0") | PASS |
| 33 | M11 network effects | <6 yrs; qualitative "B2B commodity" | 0 | not computed; 0 to 3 | **FAIL (MINOR)** |
| 34 | M12 negative WC | negative 1 of 4 yrs, latest 140 days | 0 | 0 | PASS |
| 35 | Moat classification | 3 present (M1, M2, M5) | MODERATE | MODERATE (4 present = STRONG under the literal M8 reading) | PASS (fragile) |

**F-M4 (MINOR).** The M4 ladder is: 0 decline years = 5; max 1 decline year, fully recovered = 3; 2 decline years, CAGR positive = 1; 3+ decline years = 0. TRUALT has 1 decline year, not yet recovered, CAGR positive. It misses the 3 band. It is strictly better than the 1-band case (2 decline years, CAGR positive). The 0 band needs 3+ decline years, which is not met. B01 scored 0 and cited receivable-day instability, but the receivable condition applies only to the 5 band. Recomputed M4 = 1. Moat score +1. No change to moats present.

**F-M5 (MINOR).** M5 tests "largest mcap in segment". B01's own M7 line names at least 7 listed players in the segment (Balrampur, Triveni, EID Parry, Dalmia Bharat Sugar, Dhampur, Bajaj Hindusthan, Gulshan) (01-gate0.md l.317-321). M5 ranks TRUALT against only 3 of them. The top-3 mcap status is therefore not tested against the segment B01 defines. G0 prompt Block F: "If a test needs peer data that is not provided, score 0 and mark PEER DATA NEEDED." The as-written output is M5 = 3 on the provided set with a PEER DATA NEEDED note for EID Parry, Dalmia Bharat Sugar, Dhampur and Bajaj Hindusthan. Sensitivity: if M5 falls below 3, moats present = 2, still MODERATE. Classification unchanged.

**F-M7 (MINOR).** "Well over 10" listed players is asserted with 7 names and "and others" (l.317-321). No anchored count. Direction matters: at 10 or fewer players with margin stable within +/-5pp (FY23 13.78% to FY26 16.77%, +2.99pp), M7 = 3, a fourth present moat, and moat class STRONG. The score of 1 is plausible but carries no anchor. G0 rule 5 requires the count to be in the data.

**F-M8 (MAJOR).** B01 states the company "sells B2B direct to OMCs, no retail/distribution network" and scores 0 (l.322-323). The AR, a Gate 0 source (01-gate0.md source 2), discloses "7 retail fuel outlets, with 4 additional outlets under construction" (AR p.103, as cited in 07-emoat.md l.19 and l.55; 0 outlets pre-listing per l.55). The M8 "none" premise is contradicted by a document in the Gate 0 input set. As written: "network growing AND rev CAGR >=15% = 3" is literally met (7 live, 4 under construction; rev CAGR 31.4%). "Mentioned unquantified = 1" is the floor. A conservative reading (the revenue growth is not network-driven; retail is immaterial to revenue) gives 1. Recomputed range 1 to 3. Under the literal reading, moats present = 4 (M1, M2, M5, M8) and moat class moves MODERATE to STRONG. Gate 0 classification unchanged: the Core band is below 60, so moat class does not enter the matrix, and DB6 governs. Graded MAJOR because the moat class that B07 and Stage 11 read can flip on it.

**F-M11 (MINOR).** The rule allows fewer than 6 years with the instruction "score conservatively on the overall trend and state so". The overall-trend band is numeric: rev CAGR >=20% AND selling % stable/declining = 3; growth >15% but selling % rising = 1. Rev CAGR is 31.4%. B01 did not compute selling-expense % of revenue. It replaced the numeric test with a qualitative line ("no network-effect characteristics in a B2B commodity-fuel model"). G0 rule 2 and rule 3 (show every number) are not met. If the selling-expense row is not in the Data_Sheet, the correct fill is N/A = 0 stated as such. Outcome range 0 to 3.

### 1C. Classification, confidence, deal-breakers, edge rules

| # | Rule | B01 | Check | Result |
|---|---|---|---|---|
| 36 | Data confidence | 4 yrs = LIMITED, one-tier downgrade, history_downgrade: true | correct band | PASS (obs. O2) |
| 37 | Classification matrix | Core 46 = AVERAGE band; moat class not used below 60 | correct | PASS |
| 38 | DB1 Block A <8 | A = 8, not <8 | correct | PASS |
| 39 | DB2 Block B <8 | fires, max GOOD | correct | PASS |
| 40 | DB3 median ROCE <10% | 12.30%, no | correct | PASS |
| 41 | DB4 CFO/PAT <0.50 | 1.018, no | correct | PASS |
| 42 | DB5 pledge >15% | fires, max AVERAGE | correct | PASS |
| 43 | DB6 ND/EBITDA >3x AND IC <3x | 5.20x and 1.81x, fires, AVOID | correct on either EBITDA base (5.20x or 5.39x) | PASS |
| 44 | DB7 revenue declined majority | 1 of 3, no | correct | PASS |
| 45 | DB8 PAT negative last 3 yrs | annual PAT positive, no | correct | PASS |
| 46 | DB9 history <3 yrs | 4 yrs, no | correct | PASS |
| 47 | State WHICH years drive deal-breakers | DB6 FY26; DB5 Jun-2026 SHP; DB2 via block_b_trend FY26 vs FY25 | adequate | PASS |
| 48 | CAGR edge rules | both endpoints positive; no annual loss-to-profit swing; quarterly Q2FY26 loss noted as context | honoured | PASS |
| 49 | YAML schema and flags | all fields present; FLAG-GATE0 raised; analyst_note under 200 words | compliant | PASS (obs. O3) |

Final classification recomputed: **AVOID, concur.** The corrections move Core 46 to 43 and Grand total 61 to 60 (conservative M8 = 1, M4 = 1) or 62 (literal M8 = 3). None moves the letter.

### 1D. Observations (no rule fail; carried as MINOR findings)

- **O1 (MINOR).** Two EBITDA bases inside one scorecard. D1 uses the quarterly-summed 300.29cr. M1 and M2 use the annual formula 289.75cr (01-gate0.md l.199-203, l.279, l.299). B01 calls a 10.54cr (3.5%) gap "consistent". No score changes on either base. Pick one base, or show both at every use.
- **O2 (MINOR, presentational).** B01 says the LIMITED one-tier downgrade "has no further room to apply below AVOID" (l.399-402). Applied to the base AVERAGE, the downgrade itself yields AVOID. AVOID is reached by two independent routes: DB6, and Core band + LIMITED downgrade. DB5 caps at AVERAGE on a third route. B01 understates how robust the AVOID is. B07 then builds on that understatement (see F-EM-19).
- **O3 (MINOR).** Basis label mismatch. The B01 YAML data_notes call the Q2FY26 -37.94cr quarter a "standalone quarterly loss". The report sources it to screener quarters (l.188-191), which B01 states are consolidated throughout (l.40-41). Verifier A owns the number. The basis label must match across report and block.

---
## PART 2: EMERGING MOAT (B07) COMPLIANCE

### 2A. Score re-derivation (Section 5)

| Cat | L x I | Raw (matrix) | Multiplier | Adjusted | B07 | Result |
|---|---|---|---|---|---|---|
| A3 | HM | 3 | documented 1.0 | 3.0 | 3.0 | PASS |
| A4 | HL | 2 | claim 0.7 | 1.4 | 1.4 | PASS (conservative; documented AR p.164 spec exists) |
| E1 | HM | 3 | documented 1.0 | 3.0 | 3.0 | arithmetic PASS; tier see F-EM-15 |
| F2 | MH | 3 | claim 0.7 (blended) | 2.1 | 2.1 | PASS |
| H2 | HH | 4 | documented 1.0 | 4.0 | 4.0 | arithmetic PASS; overlap see F-EM-16 |
| R1 | HH | 4 | documented 1.0 | 4.0 | 4.0 | arithmetic PASS; overlap see F-EM-16 |
| I1, I2 | none | 0 | - | 0 | 0 | PASS |
| All others (15) | none | 0 | - | 0 | 0 | PASS |
| **Total** | | | | **17.5** | **17.5** | PASS |

Band: 17.5 sits in 12-24 = MODEST MOAT DEVELOPMENT. Correct as stated. The recomputed range after F-EM-16 is 14.2 to 17.5, MODEST in every case.

### 2B. Rule-by-rule compliance

| # | Rule (EM prompt) | Finding | Result |
|---|---|---|---|
| 1 | All six sections plus Optionality Register | Sections 1-6 and register present | PASS |
| 2 | Evidence taxonomy tag on every evidence item | tags present throughout | PASS |
| 3 | Source anchors on every evidence item | "AR p.191-ish per B02/B03" (07-emoat.md l.52); many anchors are second-hand to upstream blocks (B02, B03, B05) and not to the primary document | **FAIL (MINOR)** |
| 4 | All 22 categories + R1 addressed (23 rows) | A1-A4, B1-B3, C1-C2, D1-D2, E1-E2, F1-F2, G1-G2, H1-H3, I1, I2 + R1 | PASS |
| 5 | NO EVIDENCE FOUND stated where none; no force-fit | stated; A2, G1, G2 correctly scored 0 with the opposite finding documented | PASS |
| 6 | Section 3 summary table: all rows, type, strength, time; Strong/Moderate count | present; count 5 | PASS |
| 7 | Completionist recount performed and consistent | recount line says 14 documented items (l.256); YAML evidence_mix says documented: 17 (B07-emoat.yaml l.24); unreconciled | **FAIL (MINOR)** |
| 8 | L x I matrix mapping | HH=4, HM/MH=3, HL=2 applied correctly | PASS |
| 9 | Evidence multipliers applied | 1.0 / 0.7 applied as labelled | PASS |
| 10 | Adjusted total arithmetic | 17.5 re-derived | PASS |
| 11 | Classification band | MODEST, absolute bands, no rescale | PASS |
| 12 | I1/I2 contribution stated separately | 0.0 stated (l.335) | PASS |
| 13 | Category 21 I1: >0 only with both legs, (b) leg documented | scored 0, neither leg evidenced | PASS |
| 14 | Category 22 I2: >0 only with a specific named sacrifice | scored 0, "nothing must be destroyed" stated per claimed moat | PASS |
| 15 | Scores consistent with evidence tiers (claim not scored as documented) | E1 moat element ("first", peers lack it) is a company self-description, PENDING LIVE VERIFICATION, scored at 1.0x and labelled Strong; H2 counts a non-binding MoU (APEDB) as documented | **FAIL (MINOR)** |
| 16 | One improvement, one mechanism (CLAUDE.md NEVER; no double credit) | OMC status credited in E1 and R1; PM JI-VAN Rs150cr VGF and APEDB MoU credited in H2 and R1; court order sits in R1 table and in the optionality register | **FAIL (MAJOR)** |
| 17 | Section 2C arithmetic shown | 163.73 x 0.815 = 133.4; 7.7% of 1,727.51; re-derived | PASS (obs. O4) |
| 18 | Optionality register: format, scored-0 or claim-only items, carried in YAML | 8 rows, four columns, YAML optionality_register[] matches | PASS |
| 19 | 6C/6E use the injected Gate 0 block correctly | 6E lists existing moats as M2, M5, M9 (B01 present moats are M1, M2, M5; M9 = 1 is not present); 6D says the backward score is "only overridden by a mechanical leverage test" and "GOOD-adjacent" | **FAIL (MAJOR)** |
| 20 | 6A timeline, 6B risks per top moat, 6E card | all present | PASS |
| 21 | YAML schema complete, vocab valid (em_classification in EXPANSION/STRENGTHENING/MODEST/NONE) | complete; "MODEST"; analyst_note under 200 words | PASS |
| - | 6D combined classification per the standard matrix | the EM prompt names the eight labels but does not define the cells; TURNAROUND for AVOID-backward + MODEST-forward cannot be re-derived from the injected rule source | NOT VERIFIABLE (excluded from count) |

**F-EM-16 (MAJOR). Double credit across E1, H2 and R1.**
- OMC status is the E1 evidence (07-emoat.md l.158-162). It appears again as the first row of the R1 approvals table (l.268).
- The PM JI-VAN Rs150cr VGF and the APEDB MoU are two of the H2 "four separate, named, signed or approved counterparties" (l.196-202). Both are government scheme or state instruments. They reappear as R1 evidence (l.269, l.277-280).
- The Karnataka HC 15cr-litre order sits in the R1 table (l.271) and in the optionality register (l.351). The register rule is "watched, never scored".
- B07 scored H3 (ESG) 0 because the schemes are "shared equally by every ethanol/CBG peer" (l.204-208). Section 4C calls R1 "active, not emerging, and mostly sector-wide" (l.293). R1 is still scored at the maximum, HH = 4 at 1.0x.
Once the items credited elsewhere and the registered option are stripped out, R1 holds sector-shared schemes (0 by B07's own H3 logic) and the CBG CFA, which is a claim ("advanced stage", Inv. Pres. Q1FY27 p.16). Recomputed R1: MM documented = 2.0 (grant amount company-specific) down to ML claim = 0.7. Recomputed total: 15.5 to 14.2. MODEST unchanged. The UA "EM >= 25" qualifier stays unmet either way.

**F-EM-19 (MAJOR). Gate 0 misread in the combined assessment.**
(a) 6E (l.433-434) lists the existing moats as "M2, M5, M9". B01's present moats (score 3 or more) are M1, M2 and M5. M9 scored 1.
(b) 6D (l.406-409, l.419-420) says the AVOID comes from "a single, binding, numeric deal-breaker" and calls the backward read "GOOD-adjacent... only overridden by a mechanical leverage test". The injected Gate 0 shows three routes. DB5 (pledge 36.85%) caps at AVERAGE. DB2 caps at GOOD. The LIMITED-history downgrade of the AVERAGE Core band yields AVOID without DB6 (see O2). Core 46 is AVERAGE band, not GOOD-adjacent (GOOD needs Core 60+).
The TURNAROUND reasoning rests on the single-override premise. The premise is wrong, so the combined read carries upward drift (Master v3.7 Rule J, symmetric bar). The matrix cell cannot be re-derived from the rule source. The reasoning must be restated against all three routes.

**F-EM-15 (MINOR). Evidence tier on E1 and H2.** The documented fact behind E1 is the OMC-status grant and 7 live outlets (AR p.103). The moat element is that TruAlt is "the first biofuels company" and that peers lack the channel. B07 itself marks that element PENDING LIVE VERIFICATION (l.161). It is a company self-description, not a documented event. The E1 "Strong" label also conflicts with B07's own 4C and 6B text ("first is a lead, not a barrier"; retail immaterial and paused). In H2, the APEDB MoU is non-binding (l.199). A non-binding MoU is not a "contract signed". H2 keeps HH on the Sumitomo JVA/SPA and the GAIL infusion alone. No score change is forced, but both labels overstate the tier.

**F-EM-7 (MINOR).** The recount line says 14 documented items across 6 categories. evidence_mix.documented = 17. The gap of 3 is probably the opposite-direction documented items in G1, G2 and A2, which the recount excludes. B07 does not say so. Reconcile the two counts or state the exclusion.

**F-EM-3 (MINOR).** The anchor "AR p.191-ish per B02/B03" (l.52) is not a page anchor. Anchors such as "(📄 B02 rank 3)" and "(B05)" point to upstream blocks, not to the source document. The EM prompt rule 3 asks for (AR p.__), (Q_ FY__ call) or (Inv. Pres. slide __).

**O4 (MINOR, observation, no fail).** 2C uses only Note 56 remaining commitments (163.73cr). It excludes consolidated CWIP (67.71cr), which is capex already spent and not yet earning revenue. The FAT denominator includes CWIP. With CWIP counted as capex under execution: 231.44 x 0.815 = 188.6cr, 10.9% of revenue, against 7.7% stated. The document-reading protocols allow a conservative reading. State it as a choice with the sensitivity shown.

---
## PART 3: VALUATION (B11), EXPECTATION LEDGER, BUSINESS UNDERSTANDING NARRATIVE
PENDING PHASE 3. B10 and B11 do not exist at phase 1. Rules 4-7 and 9-15 were not run.

---
## SUMMARY

| Framework | Rules checked | Passed | Fails | Acceptance |
|---|---|---|---|---|
| Gate 0 (B01) | 49 | 43 | 6 (2 MAJOR, 4 MINOR) | 87.8% |
| Emerging Moat (B07) | 21 | 16 | 5 (2 MAJOR, 3 MINOR) | 76.2% |
| Combined phase 1 | 70 | 59 | 11 | 84.3% |

Findings: 0 CRITICAL, 4 MAJOR, 11 MINOR. The MINOR count is 7 rule fails plus 4 observations (O1-O4).
Recomputed Gate 0: Core 43 (was 46). Grand total 60 on the conservative M8 reading, 62 on the literal one (was 61). Moat class MODERATE (STRONG on the literal M8 reading). Classification **AVOID, concur.**
Recomputed Emerging Moat: 14.2 to 17.5 (was 17.5). **MODEST, concur.**
No finding changes a classification. The rework is local: B01 E2/M8 re-scored and the M4/M5/M7/M11 notes added; B07 R1 de-duplicated, and the 6D/6E Gate 0 read restated.

```yaml
stage: B12c
company: "TRUALT"
run_date: "2026-09-18"
model: "claude-opus-5"
status: complete
scope: "phase 1 (Gate 0 + Emerging Moat); valuation, expectation ledger and narrative pending phase 3"
gate0:
  rules_checked: 49
  fails:
    - {rule: "E2 promoter change over 3 years", severity: "MAJOR", stated: "3 (Mar-2026 to Jun-2026 window substituted)", recomputed: "0 (N/A per G0 rule 5; filed pre-offer 88.20% to 70.55% also scores 0)", effect: "Block E 13 to 10; Core 46 to 43; classification unchanged"}
    - {rule: "M8 distribution", severity: "MAJOR", stated: "0 (no retail network)", recomputed: "1 conservative to 3 literal (AR p.103 discloses 7 retail outlets live plus 4 under construction; rev CAGR 31.4%)", effect: "literal reading gives 4 moats present, class MODERATE to STRONG; Gate 0 classification unchanged"}
    - {rule: "M4 customer stickiness", severity: "MINOR", stated: "0", recomputed: "1 (1 decline year with positive CAGR beats the 2-decline-year band; 0 needs 3+ decline years)", effect: "moat score +1; moats present unchanged"}
    - {rule: "M5 scale and dominance", severity: "MINOR", stated: "3 on a 4-company set", recomputed: "3 on the provided set, PEER DATA NEEDED for segment peers B01 itself names (EID Parry, Dalmia Bharat Sugar, Dhampur, Bajaj Hindusthan)", effect: "if below 3, moats present 2, still MODERATE"}
    - {rule: "M7 regulatory licence", severity: "MINOR", stated: "1 (well over 10 players)", recomputed: "1, count unanchored (7 names given)", effect: "at 10 or fewer players M7 = 3 and class STRONG"}
    - {rule: "M11 network effects", severity: "MINOR", stated: "0 (qualitative)", recomputed: "numeric overall-trend test not run; outcome 0 to 3", effect: "moats present could rise; classification unchanged"}
emoat:
  rules_checked: 21
  fails:
    - {rule: "one improvement one mechanism", severity: "MAJOR", stated: "R1 HH 4.0 documented", recomputed: "R1 0.7 to 2.0 after removing OMC status (E1), PM JI-VAN VGF and APEDB MoU (H2), court order (optionality register); total 14.2 to 15.5", effect: "MODEST unchanged"}
    - {rule: "6C/6E use of injected Gate 0", severity: "MAJOR", stated: "existing moats M2, M5, M9; AVOID only via one leverage deal-breaker; GOOD-adjacent", recomputed: "present moats M1, M2, M5; AVOID also via Core AVERAGE band plus LIMITED downgrade; DB5 caps AVERAGE", effect: "TURNAROUND reasoning must be restated; matrix cell not derivable from rule source"}
    - {rule: "evidence tier consistency", severity: "MINOR", stated: "E1 Strong at 1.0x; APEDB non-binding MoU counted documented in H2", recomputed: "E1 first-mover element is a self-description PENDING LIVE VERIFICATION; non-binding MoU is not a signed contract", effect: "no forced score change"}
    - {rule: "completionist recount consistency", severity: "MINOR", stated: "recount 14 documented items", recomputed: "YAML evidence_mix documented 17; unreconciled", effect: "none"}
    - {rule: "source anchors", severity: "MINOR", stated: "AR p.191-ish; upstream-block anchors (B02, B03, B05)", recomputed: "primary-document page anchors required", effect: "none"}
valuation: {rules_checked: 0, fails: [], status: "pending phase 3"}
expectation_ledger: {present: false, downside_row: false, all_rows_confirm_by: false, all_rows_metric_threshold: false, prob_in_range: false, decay_status_valid: false, off_ledger_credit: false, residual_pct_cmp: 0, residual_starter_cap_ok: true, fails: [], status: "pending phase 3"}
business_understanding_narrative: {present: false, five_questions_answered: false, prose_only: false, section6_candidates_named: 0, valuation_vocab_leak: false, fails: [], status: "pending phase 3"}
recomputed_destination_pe: ""
recomputed_decision: ""
recomputed_gate0: {core_score: 43, grand_total: "60 conservative M8, 62 literal M8", moat_class: "MODERATE (STRONG on literal M8)", classification: "AVOID (concur)"}
recomputed_emoat: {em_score: "14.2 to 17.5", em_classification: "MODEST (concur)"}
findings:
  - {severity: "MAJOR", location: "01-gate0.md l.229-240, E2", note: "3-month window substituted for a 3-year change; as written N/A score 0"}
  - {severity: "MAJOR", location: "01-gate0.md l.322-323, M8", note: "no-network premise contradicted by AR p.103 (7 outlets live, 4 under construction); recomputed 1 to 3"}
  - {severity: "MAJOR", location: "07-emoat.md l.196-202, l.268-280, l.351, R1/E1/H2", note: "same evidence credited in two categories and a registered option scored; R1 recomputed 0.7 to 2.0"}
  - {severity: "MAJOR", location: "07-emoat.md l.404-434, 6D/6E", note: "Gate 0 misread: wrong existing-moat list (M9 for M1) and single-override premise for AVOID"}
  - {severity: "MINOR", location: "01-gate0.md l.305-308, M4", note: "scored 0 though 0 band needs 3+ decline years; recomputed 1"}
  - {severity: "MINOR", location: "01-gate0.md l.309-314, M5", note: "mcap rank tested on 3 peers while B01 names 7+ segment players; PEER DATA NEEDED"}
  - {severity: "MINOR", location: "01-gate0.md l.317-321, M7", note: "player count asserted, not anchored; at 10 or fewer M7 = 3"}
  - {severity: "MINOR", location: "01-gate0.md l.334-336, M11", note: "numeric overall-trend test replaced by qualitative line"}
  - {severity: "MINOR", location: "01-gate0.md l.199-203 vs l.279, l.299", note: "two EBITDA bases (300.29 vs 289.75) in one scorecard; no score change"}
  - {severity: "MINOR", location: "01-gate0.md l.399-402", note: "LIMITED downgrade independently yields AVOID; report understates robustness"}
  - {severity: "MINOR", location: "B01-gate0.yaml data_notes vs 01-gate0.md l.188-191", note: "Q2FY26 loss labelled standalone in YAML, consolidated screener in report"}
  - {severity: "MINOR", location: "07-emoat.md l.158-162, l.199", note: "E1 first-mover element and APEDB non-binding MoU tiered as documented"}
  - {severity: "MINOR", location: "07-emoat.md l.256 vs B07-emoat.yaml l.24", note: "recount 14 vs evidence_mix documented 17"}
  - {severity: "MINOR", location: "07-emoat.md l.52 and upstream-block anchors", note: "non-page anchors"}
  - {severity: "MINOR", location: "07-emoat.md l.73-89, 2C", note: "CWIP 67.71cr excluded; with it 10.9% vs 7.7%; conservative choice unstated as such"}
critical_count: 0
major_count: 4
minor_count: 11
acceptance_rate: 84.3
```
