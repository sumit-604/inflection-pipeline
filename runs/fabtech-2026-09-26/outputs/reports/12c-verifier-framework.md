# STAGE 12 VERIFIER C: FRAMEWORK ADHERENCE (PHASE 1 SCOPE)

Company: Fabtech Technologies Ltd (FABTECH). Run date: 2026-09-26. Model: claude-opus-5-5.
Scope: Gate 0 (B01) and Emerging Moat (B07) only. Valuation audit (B10, B11), expectation
ledger (rules 13-14) and Business Understanding Narrative (rule 9) are pending phase 3 / stage 13.

Rule sources read: prompts/01-gate-0-pipeline.md, prompts/07-emerging-moat-pipeline.md.
Artifacts audited: outputs/reports/01-gate0.md, outputs/blocks/B01-gate0.yaml,
outputs/reports/07-emoat.md, outputs/blocks/B07-emoat.yaml.
Inputs re-read to re-derive scores (rule application, not number fidelity):
inputs/screening/screener-Data_Sheet.csv and
inputs/screening/FABTECH-screener-consolidated-2026-09-26.txt (Cash Flows and Ratios blocks).
Number fidelity against source PDFs belongs to Verifier A; nothing here overrides it.

## HEADLINE

- Gate 0: 41 rules checked, 9 fail (4 MAJOR, 5 MINOR). Classification AVERAGE CONCURS under every
  recomputation. Deal-breaker #4 (cumulative CFO/PAT 0.35 < 0.50) caps at AVERAGE regardless.
- Emerging Moat: 27 rules checked, 10 fail (3 MAJOR findings, 5 MINOR; two rule fails map onto the
  MAJOR findings). em_score 13.3 recomputes to 9.9 (11.7 on the two purely mechanical fixes alone).
  Classification flips MODEST -> NONE (NO MEANINGFUL EMERGING MOAT, < 12). Combined AVERAGE concurs.
- CRITICAL 0. MAJOR 7. MINOR 10. Acceptance 49/68 = 72.1% (above the 60% REWORK line).
- Carry-forward for Stage 11 (phase 3): Pillar 3 must use em_classification NONE or state why MODEST
  stands; B01 moat class is THIN or NONE depending on the M11 reading.

## GATE 0 (B01) COMPLIANCE TABLE

Data window: 7 years FY20-FY26 (B01 opening line present, PASS). ROCE series FY21-FY26.

| Rule | Stated | Recomputed / check | Result |
|---|---|---|---|
| Opening data line, anchors on numbers | present | present | PASS |
| A1 median ROCE | 27% -> 5 | median(14,22,26,28,31,48) = 27 -> 5 (FCS txt ROCE row) | PASS |
| A2 min ROCE | 14% -> 3 | 12-14.9 band -> 3 | PASS |
| A3 median ROE | 26.2% on FY21-26 -> 5 | Formula requires closing-NW fallback for earliest year; FY20 omitted. FY20 = 12.39 / 38.29 = 32.4% (Data_Sheet rows 24, 39-40). 7-yr median 27.8% -> 5 | FAIL (MINOR, no score change) |
| A4 ROCE trend | -12pp -> 0 | FY21 26 vs FY26 14 -> 0 | PASS |
| B1 CFO/PAT | 62/176 = 0.35 -> 0 | Data_Sheet rows 57 and 24 sum to 62.79 / 175.67 = 0.36 -> 0 | PASS |
| B2 FCF+ years | 3/7 -> 0 | if FY26 FCF <= 0 (see B3), 2/7; 0 either way | PASS |
| B3 FCF/PAT | 40/176 = 0.23 -> 1 | Fixed formula: FCF = CFO - purchase of PPE. Report used screener's FCF row, which shows FY26 FCF 5 against CFO 0.48 (FCS txt Free Cash Flow row; Data_Sheet row 57). Under the formula FCF cannot exceed CFO. Cumulative FCF ex-FY26 = 35; FY26 <= 0.48; total <= 35.5 / 176 = 0.20 boundary. B3 -> 0 unless FY26 PPE purchases < 0.3 Cr | FAIL (MAJOR) |
| B4 WC days change | screener "Working Capital Days" -19 -> 90, +109 -> 0 | Fixed formula is Receivable + Inventory - Payable days. The formula-shaped series is screener "Cash Conversion Cycle": FY20 51, FY26 55, +4 days, within +/-5 -> 3 (FCS txt Ratios block). Data_Sheet has no payables row, so the revenue-basis computation is not possible; the CCC row is the nearest compliant input and its basis (screener's) must be stated | FAIL (MAJOR) |
| C1 revenue CAGR | 20.7% -> 5 | (410.77/133.42)^(1/6) - 1 = 20.6% -> 5 | PASS |
| C2 PAT CAGR | 20.7% -> 5 | (38.36/12.39)^(1/6) - 1 = 20.7% -> 5 | PASS |
| C3 positive YoY years | 4/6 = 67% -> 1 | 50-74 band -> 1 | PASS |
| C4 PAT minus revenue CAGR | ~0pp -> 3 | +0.1pp -> 3 | PASS |
| CAGR edge rules | no negative endpoints; no annual loss-to-profit swing | correct; data_notes records quarterly losses | PASS |
| D1 ND/EBITDA | net cash -> 5 | net cash on either debt basis -> 5 | PASS |
| D2 interest cover | EBIT = OP - Dep = 29.7 / 4.16 = 7.1x -> 4 | EBIT basis undeclared. Block A uses screener ROCE, whose EBIT includes other income. On that basis (PBT 48.28 + Int 4.16) = 52.44 / 4.16 = 12.6x -> 5. Declare one EBIT basis for the scorecard | FAIL (MINOR) |
| D3 D/E | 69.64 / 419.77 = 0.17 -> 4 | D1 used 42.73 Cr (ex-lease), D3 used 69.64 Cr (incl. lease). 42.73 / 419.77 = 0.10, still 0.1-0.5 -> 4. No score change, basis inconsistent | FAIL (MINOR) |
| D4 current ratio | 2.50x -> 5 | 516.42 / 206.85 = 2.497 -> 5 | PASS |
| E1 promoter | 68.94% -> 5 | -> 5 | PASS |
| E2 promoter change 3y | N/A -> 0 | Grounded-claims rule allows N/A only where data is not provided. The report names the RHP among this stage's data sources and states it was not read. Score likely 0 either way (IPO dilution) | FAIL (MINOR) |
| E3 pledge | 0% -> 5 | -> 5 | PASS |
| E4 contingent liab. | N/A -> 0 | AR not a designated source; rule applied | PASS |
| M1 pricing power | peak FY24 15% to FY26 9%, -6pp -> 0 | Scorecard trend tests run endpoint to endpoint. FY20 OPM 14.22/133.42 = 10.66%, FY26 35.00/410.77 = 8.52% (Data_Sheet P&L rows), -2.1pp, revenue CAGR 20.6% -> "declined 2-5pp despite growth" = 1 | FAIL (MINOR) |
| M2 cost advantage | 9% vs peer median 15% -> 0 | -> 0 | PASS |
| M3 capital efficiency | FAT 5.3x, ROCE 14% -> 1 | -> 1 (latest-year ROCE is a reasonable reading) | PASS |
| M4 stickiness | 2 decline yrs -> 1 | -> 1 | PASS |
| M5 scale | PEER DATA NEEDED -> 0 | rule applied | PASS |
| M6 R&D | N/A -> 0 | -> 0 | PASS |
| M7 regulatory | unregulated -> 0 | -> 0 | PASS |
| M8 distribution | -> 0 | -> 0 | PASS |
| M9 brand | proxy 53.7%, peers PEER DATA NEEDED -> 0 | proxy stated, rule applied | PASS |
| M10 switching costs | -> 1 | -> 1 | PASS |
| M11 network effects | 3 (sole moat present) | (a) "3yr" windows are 2-yr CAGRs: FY24->26 and FY21->23. True 3-yr: FY23->26 = 28.4%, FY20->23 = 13.3%; latest > prior holds. (b) Selling % component: FY26 line blank (Data_Sheet row 17). Full-period selling % rose FY20 8.8% (11.75/133.42) to FY25 14.4% (46.94/326.67); latest window FY23 19.2% to FY25 14.4% fell. (c) Tier 3 and tier 5 need the same selling-% leg. Awarding 3 while withholding 5 on one missing data point has no rule basis; "score conservatively" applies only below 6 years. Strict grounded-claims reading: N/A = 0. Alternative reading on FY23-25: 5 | FAIL (MAJOR) |
| M12 negative WC | 0 | CCC basis: 4 of 7 years > 45 -> 0; unchanged | PASS |
| Block and core arithmetic | A13 B1 C14 D18 E10 = 56; F 6; grand 62 | sums correct on stated scores | PASS |
| Moat classification | 1 present -> THIN | correct on stated scores; recomputed 0 present -> NONE (strict M11) or 1 -> THIN (M11 = 5) | PASS on stated inputs |
| Data confidence | 7 yrs -> moderate, no downgrade | correct | PASS |
| Classification matrix | Core 56 -> AVERAGE | correct | PASS |
| Deal-breaker application | #2 and #4 triggered; others not | correct: #7 2/6 not majority; #8 FY24-26 PAT positive | PASS |
| Deal-breaker year attribution | FY25 and FY26 named, described as "post-IPO/recently-listed window" and (analyst_note) "FY25-FY26 post-listing window" | Listing date is 07-Oct-2025 (report's own statement). FY25 (Apr-2024 to Mar-2025) is pre-listing; FY26 straddles. The Gate 0 prompt names "documented post-IPO rebase" as the ground on which downstream sizing may override AVERAGE, so this label is load-bearing | FAIL (MAJOR) |
| FLAG-GATE0 raised when <= AVERAGE | present | present | PASS |
| block_b_trend with one number | present | present | PASS |

Gate 0 recomputation (rule-corrected):

| Block | Stated | Recomputed |
|---|---|---|
| A | 13 | 13 |
| B | 1 | 3 (B4 = 3, B3 = 0); 4 if B3 holds at 1 |
| C | 14 | 14 |
| D | 18 | 18; 19 on PBT + interest EBIT |
| E | 10 | 10 |
| Core | 56 | 58 (range 58-60) |
| Moat score | 6 | 4 (M1 = 1, M11 = 0) or 9 (M11 = 5) |
| Moats present / class | 1 / THIN | 0 / NONE (strict) or 1 / THIN |
| Classification | AVERAGE | AVERAGE. At core 60 the matrix gives GOOD, but deal-breaker #4 caps at AVERAGE. Deal-breaker #2 still triggers (Block B 3-4 < 8). |

## EMERGING MOAT (B07) COMPLIANCE TABLE

| Rule | Stated | Check | Result |
|---|---|---|---|
| All 23 rows addressed (22 + R1) | 23 rows in Section 3 table and Section 5 table | complete | PASS |
| Categories 21 and 22 present | I1, I2 present | present | PASS |
| I1 both legs | (a) not established, (b) moot, 0 | correct application | PASS |
| I2 named-sacrifice test | tested on SACE, "nothing" -> 0 | correct application | PASS |
| I1/I2 contribution stated separately | 0.0 stated | present | PASS |
| NO EVIDENCE FOUND discipline | used throughout | correct | PASS |
| Anchors on evidence items | present (call month, AR page, filing name) | correct | PASS |
| C1 multiplier | LL=1 x 0.7 = 0.7 | consistent with 🎙️ | PASS |
| E1 multiplier | HM=3 x 1.0 (📄 dominant) | Botswana/West Africa orders and the 62-country footprint (AR p.5, p.11) are 📄 but document presence, not first-mover status. The "first" claim rests on Djibouti, 🎙️, filing "not individually located". Defensible reading 3 x 0.7 = 2.1 | FAIL (MINOR) |
| G1 multiplier | ML=1 x 1.0 = 1.0 | consistent | PASS |
| H1 multiplier | HM=3 x 0.7 = 2.1 | consistent | PASS |
| H2 raw and multiplier | HH=4 x 0.7 = 2.8 | Text: "The SACE item alone would justify MODERATE ... without crossing into STRONG." HH is the top matrix cell, inconsistent with Moderate. SACE 51% stake already carries H1. With SACE removed, H2 holds KP Group (📄 named, no terms) and Optech (🎙️, vague): ML=1 x 1.0 = 1.0 | FAIL (MAJOR) |
| H3 multiplier / register | LL=1 x 0.7 = 0.7 | Text: "Carried to the optionality register rather than scored as a live category." Register rule: "Registered options are watched, never scored." KP Group is also H2's evidence. -> 0.0 | FAIL (MAJOR) |
| R1 multiplier | HM=3 x 1.0 ("📄 named funded projects") = 3.0 | Section 4B tags both tailwinds 🎙️ (localisation: Aug-2026 call 🎙️; DFI funding: Aug-2026 call 🎙️, no amount). 4A finds no approvals. The "named funded projects" are E1's evidence. Verifier C rule 3: a 🎙️ category scored as 📄 is a finding. 3 x 0.7 = 2.1 | FAIL (MAJOR) |
| One improvement, one mechanism | not addressed except A3 | Saudi SACE/localisation credited in H1, H2 and R1 (6B itself groups "H1/H2/R1 Saudi localisation" as one moat); KP Group in H2 and H3; Djibouti/Botswana in E1 and R1 | FAIL (MAJOR, captured in H2/H3/R1 rows) |
| Optionality register present, never scored | present, 8 rows | H3 is both registered and scored | FAIL (captured in H3 row) |
| Adjusted-total arithmetic | 13.3 | sums correctly on stated rows | PASS |
| Classification band | 13 -> MODEST | correct on stated total | PASS on stated inputs |
| Completionist recount performed | line present | present | PASS |
| Recount accuracy | "9 documented items across 6 categories" | the list names 7 categories (E1, H1, H2, G1, C2, F2, G2) and counts Djibouti, which the report says was not located as a filing | FAIL (MINOR) |
| Strong/Moderate count line | 5 incl. G1 "Weak-Moderate" | 4 (E1, H1, H2, R1); guard not triggered either way | FAIL (MINOR) |
| Report vs YAML consistency | E1, H2 "Moderate-Strong" in report, "Moderate" in YAML; H3 YAML "documented" vs scored 🎙️ 0.7; register 8 rows in report, 7 in YAML (FTCL data-centre row missing) | misaligned | FAIL (MINOR) |
| active_categories schema (Strong/Moderate only) | C1, G1, H3 (Weak) listed | schema breach | FAIL (MINOR) |
| 2C capex-embedded growth | NOT APPLICABLE in report; YAML value 0 | Missing-number rule: NOT FOUND is the only fill; numeric 0 reads as a measured 0% | FAIL (MINOR) |
| F2 cross-reference to B05 | done (grade C, 2/4/4 of 10) | present | PASS |
| 6C combined table from injected B01 | present | present | PASS |
| 6D combined classification | AVERAGE | matrix-consistent | PASS |

Emerging Moat recomputation:

| Row | Stated | Recomputed |
|---|---|---|
| C1 | 0.7 | 0.7 |
| E1 | 3.0 | 3.0 (2.1 on the stricter reading) |
| G1 | 1.0 | 1.0 |
| H1 | 2.1 | 2.1 |
| H2 | 2.8 | 1.0 |
| H3 | 0.7 | 0.0 |
| R1 | 3.0 | 2.1 |
| Total | 13.3 (MODEST) | 9.9 (NONE); 11.7 on the R1 and H3 fixes alone (NONE); 9.0 with E1 at 0.7 |

Classification: every recomputation lands below 12, so em_classification is NONE (NO MEANINGFUL
EMERGING MOAT). Combined assessment stays AVERAGE (core AVERAGE with NONE or MODEST). The EM >= 25
UA qualifier fails on both the stated and recomputed scores.

## FINDINGS (consolidated)

| ID | Severity | Location | Finding |
|---|---|---|---|
| G-B3 | MAJOR | 01-gate0.md B3 (and B2) | Screener FCF row substituted for the fixed formula; FY26 FCF 5 > CFO 0.48 cannot occur under CFO - purchase of PPE. B3 likely 1 -> 0 |
| G-B4 | MAJOR | 01-gate0.md B4 | Screener "Working Capital Days" substituted for the fixed formula; the CCC row gives +4 days -> B4 = 3 |
| G-M11 | MAJOR | 01-gate0.md M11 | Sole moat awarded on an unconfirmed component with mislabelled 2-yr windows; strict score 0, moat class NONE |
| G-DB-YEARS | MAJOR | 01-gate0.md deal-breakers; B01 analyst_note | FY25 labelled post-IPO/post-listing; it is pre-listing |
| G-A3 | MINOR | 01-gate0.md A3 | FY20 ROE omitted; median 27.8%; score unchanged |
| G-D2 | MINOR | 01-gate0.md D2 | EBIT basis undeclared and inconsistent with Block A; 4 -> 5 on PBT + interest |
| G-D1D3 | MINOR | 01-gate0.md D1, D3 | Two debt bases in one block; no score change |
| G-E2 | MINOR | 01-gate0.md E2 | RHP provided but not read; N/A misapplied; score likely unchanged |
| G-M1 | MINOR | 01-gate0.md M1 | Peak-to-latest used instead of endpoints; 0 -> 1 |
| E-R1 | MAJOR | 07-emoat.md Section 5 R1 vs 4B | 🎙️ tailwinds scored at 📄 1.0; 3.0 -> 2.1 |
| E-H3 | MAJOR | 07-emoat.md H3 | Registered optionality scored; KP Group double-credited; 0.7 -> 0 |
| E-H2 | MAJOR | 07-emoat.md H2 | SACE triple-credited (H1, H2, R1); HH contradicts Moderate; 2.8 -> 1.0. With E-R1 and E-H3, MODEST -> NONE |
| E-E1 | MINOR | 07-emoat.md E1 | First-mover status rests on 🎙️ Djibouti; 1.0x generous |
| E-RECOUNT | MINOR | 07-emoat.md Section 3 recount | 6 vs 7 categories; Djibouti counted as 📄 |
| E-YAML-CONSIST | MINOR | B07-emoat.yaml | Strength/tier labels differ from report; register 7 vs 8 rows; Weak rows in Strong/Moderate list |
| E-2C | MINOR | B07-emoat.yaml capex_embedded_growth_pct | Numeric 0 where NOT FOUND / NOT APPLICABLE belongs |
| E-SM-COUNT | MINOR | 07-emoat.md Section 3 count line | G1 counted as Moderate; true count 4 |

Out-of-scope observation passed to Verifier A (not scored here): 07-emoat.md Section 1C states Africa
"~19% combined" while the listed lines (Kenya 10.6%, Egypt 1.6%, Algeria 1.5%) sum to 13.7%.

## REWORK ASSESSMENT

No CRITICAL. Acceptance 49/68 = 72.1%, above the 60% REWORK line. Phase-1 rule 8: categories 21 and
22 present, PASS. Rule 6 (B09 downstream block) and rules 7, 9-15 are out of phase-1 scope. No stage
REWORK triggered by this verifier. Recommended orchestrator actions: carry em_classification NONE
(recomputed) and B01 moat class THIN/NONE to Halt 1 and Stage 11 with both readings named; correct
the FY25 "post-listing" label before any post-IPO rebase sizing argument.

## YAML

```yaml
stage: B12c
company: "FABTECH"
run_date: "2026-09-26"
model: "claude-opus-5-5"
status: complete
scope: "phase 1 (Gate 0 B01 + Emerging Moat B07 only); valuation audit pending phase 3"
gate0:
  rules_checked: 41
  fails:
    - {rule: "A3 ROE formula (earliest-year closing-NW fallback)", severity: MINOR, stated: "median 26.2% on FY21-FY26, FY20 omitted", recomputed: "FY20 ROE = 12.39/38.29 = 32.4% (Data_Sheet rows 24, 39-40); 7-yr median 27.8%; score 5 unchanged"}
    - {rule: "B3 FCF formula (FCF = CFO - purchase of PPE)", severity: MAJOR, stated: "screener FCF row; FY26 FCF +5 vs CFO +0.48; B3 = 1", recomputed: "FCF cannot exceed CFO under the fixed formula; cumulative FCF/PAT <= 35.5/176 = ~0.20 boundary; B3 1 -> 0 unless FY26 PPE purchases < 0.3 Cr; B2 stays 0"}
    - {rule: "B4 WC days formula (Receivable + Inventory - Payable days)", severity: MAJOR, stated: "screener Working Capital Days FY20 -19 to FY26 90, +109, B4 = 0", recomputed: "formula-shaped screener Cash Conversion Cycle FY20 51 to FY26 55, +4 days -> B4 = 3; Block B 1 -> 3 (4 if B3 holds)"}
    - {rule: "D2 EBIT basis", severity: MINOR, stated: "EBIT = OP - Dep = 29.7; IC 7.1x; D2 = 4", recomputed: "basis undeclared, inconsistent with Block A screener ROCE basis; PBT + Int = 52.44 / 4.16 = 12.6x -> 5"}
    - {rule: "D1/D3 debt basis consistency", severity: MINOR, stated: "D1 borrowings 42.73 Cr ex-lease; D3 69.64 Cr incl. lease", recomputed: "D/E 0.10 or 0.17, both in 0.1-0.5 band -> 4; net cash either way; declare one basis"}
    - {rule: "E2 grounded-claims rule", severity: MINOR, stated: "N/A; RHP named as stage source but not read", recomputed: "N/A allowed only for data not provided; score likely 0 either way (IPO dilution)"}
    - {rule: "M1 pricing-power window", severity: MINOR, stated: "peak FY24 15% to FY26 9%, score 0", recomputed: "endpoints FY20 10.66% to FY26 8.52% = -2.1pp with revenue CAGR 20.6% -> 1"}
    - {rule: "M11 network-effects test and grounded-claims rule", severity: MAJOR, stated: "3, sole moat present", recomputed: "windows are 2-yr CAGRs mislabelled 3-yr (true FY23-26 28.4% vs FY20-23 13.3%); FY26 selling line blank; selling% FY20 8.8% to FY25 14.4%. Missing component -> 0 strict (5 if FY23-25 accepted); tier 3 has no rule basis. Moats present 1 -> 0, class THIN -> NONE (strict)"}
    - {rule: "Deal-breaker year attribution", severity: MAJOR, stated: "FY25 and FY26 called post-IPO / post-listing window", recomputed: "listing 07-Oct-2025; FY25 is pre-listing, FY26 straddles; label feeds the post-IPO rebase sizing override"}
  recomputed_scores: {A: 13, B: "3 (4 if B3 holds at 1)", C: 14, D: "18 (19 on PBT+interest EBIT)", E: 10, core: "58 (range 58-60)", moat_score: "4 (M11=0) or 9 (M11=5)", moats_confirmed: "0 or 1", moat_class: "NONE or THIN"}
  classification_concur: true
  classification_note: "AVERAGE survives every recomputation. Core 58-59 is in the 40-59 band; at 60 the matrix gives GOOD but deal-breaker #4 (CFO/PAT 0.35 < 0.50) caps at AVERAGE. Deal-breaker #2 still triggers (Block B 3-4 < 8)."
emoat:
  rules_checked: 27
  fails:
    - {rule: "R1 evidence multiplier", severity: MAJOR, stated: "HM=3 x 1.0 = 3.0", recomputed: "Section 4B tags both tailwinds 🎙️; 4A no approvals; funded projects are E1 evidence. 3 x 0.7 = 2.1"}
    - {rule: "Optionality register never scored (H3)", severity: MAJOR, stated: "LL=1 x 0.7 = 0.7 while text routes H3 to the register", recomputed: "0.0; KP Group also credited in H2"}
    - {rule: "H2 raw score vs stated strength", severity: MAJOR, stated: "HH=4 x 0.7 = 2.8; text says SACE alone = MODERATE", recomputed: "SACE already carries H1; KP Group (📄 named) + Optech (🎙️) = ML=1 x 1.0 = 1.0"}
    - {rule: "One improvement, one mechanism", severity: MAJOR, stated: "SACE in H1, H2, R1; KP Group in H2, H3; Djibouti/Botswana in E1, R1", recomputed: "captured in H2, H3, R1 rows; no separate delta"}
    - {rule: "E1 evidence multiplier", severity: MINOR, stated: "HM=3 x 1.0", recomputed: "first-mover status rests on 🎙️ Djibouti claim; 3 x 0.7 = 2.1 on the stricter reading"}
    - {rule: "Completionist recount accuracy", severity: MINOR, stated: "9 items across 6 categories", recomputed: "list names 7 categories and counts Djibouti, not located as a filing"}
    - {rule: "Strong/Moderate count line", severity: MINOR, stated: "5 incl. G1 Weak-Moderate", recomputed: "4 (E1, H1, H2, R1)"}
    - {rule: "Report vs YAML consistency", severity: MINOR, stated: "E1/H2 Moderate-Strong vs Moderate; H3 documented vs 🎙️ 0.7; register 8 vs 7 rows", recomputed: "align block to report"}
    - {rule: "active_categories schema (Strong/Moderate only)", severity: MINOR, stated: "C1, G1, H3 Weak rows listed", recomputed: "remove or relabel"}
    - {rule: "Missing-number discipline (2C)", severity: MINOR, stated: "capex_embedded_growth_pct: 0", recomputed: "NOT FOUND / NOT APPLICABLE, not numeric 0"}
  em_score_stated: 13.3
  em_score_recomputed: "9.9 (11.7 on R1 and H3 fixes alone; 9.0 with E1 at 0.7)"
  em_classification_stated: "MODEST"
  em_classification_recomputed: "NONE (NO MEANINGFUL EMERGING MOAT, < 12)"
  combined_assessment_concur: true
  combined_note: "Combined AVERAGE unchanged. EM >= 25 UA qualifier fails either way. Stage 11 Pillar 3 must use NONE or state why MODEST stands."
valuation: {rules_checked: 0, fails: [], status: "pending phase 3"}
expectation_ledger: {status: "pending phase 3"}
business_understanding_narrative: {status: "pending stage 13"}
recomputed_destination_pe: ""
recomputed_decision: ""
findings:
  - {id: G-B3, severity: MAJOR, location: "01-gate0.md B3/B2", note: "screener FCF used; FY26 FCF 5 > CFO 0.48 impossible under fixed formula; B3 likely 1 -> 0"}
  - {id: G-B4, severity: MAJOR, location: "01-gate0.md B4", note: "Working Capital Days substituted for fixed formula; CCC row +4 days -> B4 = 3"}
  - {id: G-M11, severity: MAJOR, location: "01-gate0.md M11", note: "sole moat awarded on unconfirmed component, mislabelled windows; strict 0, moat class NONE"}
  - {id: G-DB-YEARS, severity: MAJOR, location: "01-gate0.md deal-breakers; B01 analyst_note", note: "FY25 labelled post-listing; it is pre-listing (listing 07-Oct-2025)"}
  - {id: G-A3, severity: MINOR, location: "01-gate0.md A3", note: "FY20 ROE omitted; median 27.8%; score unchanged"}
  - {id: G-D2, severity: MINOR, location: "01-gate0.md D2", note: "EBIT basis undeclared; 4 -> 5 on PBT + interest"}
  - {id: G-D1D3, severity: MINOR, location: "01-gate0.md D1, D3", note: "two debt bases in one block; no score change"}
  - {id: G-E2, severity: MINOR, location: "01-gate0.md E2", note: "RHP provided but not read; N/A misapplied"}
  - {id: G-M1, severity: MINOR, location: "01-gate0.md M1", note: "peak-to-latest instead of endpoints; 0 -> 1"}
  - {id: E-R1, severity: MAJOR, location: "07-emoat.md Section 5 R1 vs 4B", note: "🎙️ tailwinds scored 📄 1.0; 3.0 -> 2.1"}
  - {id: E-H3, severity: MAJOR, location: "07-emoat.md H3", note: "registered optionality scored; KP double credit; 0.7 -> 0"}
  - {id: E-H2, severity: MAJOR, location: "07-emoat.md H2", note: "SACE credited in H1, H2, R1; HH contradicts Moderate; 2.8 -> 1.0; with E-R1, E-H3: MODEST -> NONE"}
  - {id: E-E1, severity: MINOR, location: "07-emoat.md E1", note: "first-mover rests on 🎙️ Djibouti; 1.0x generous"}
  - {id: E-RECOUNT, severity: MINOR, location: "07-emoat.md Section 3 recount", note: "6 vs 7 categories; Djibouti counted 📄"}
  - {id: E-YAML-CONSIST, severity: MINOR, location: "B07-emoat.yaml", note: "labels differ from report; register 7 vs 8 rows; Weak rows listed"}
  - {id: E-2C, severity: MINOR, location: "B07-emoat.yaml capex_embedded_growth_pct", note: "numeric 0 where NOT FOUND belongs"}
  - {id: E-SM-COUNT, severity: MINOR, location: "07-emoat.md Section 3 count line", note: "G1 counted as Moderate; true count 4"}
critical_count: 0
major_count: 7
minor_count: 10
acceptance_rate: 72.1   # 49 of 68 rules passed (gate0 32/41, emoat 17/27); phase-1 scope only
```
