# VERIFIER C: FRAMEWORK ADHERENCE. INVPRECQ, run 2026-11-15 (PHASE 1 SCOPE)

Model: claude-opus-5-5 (matches .claude/agents/verifier-c-framework.md frontmatter). Emits: B12c.

## 0. SCOPE, INPUTS, METHOD

Scope. This pass covers phase 1 only: Gate 0 (B01) and Emerging Moat (B07). The valuation half (B10, B11; verifier rules 4, 5 as applied to B11, 6 second half, 7, 11 to 15) runs in phase 3, after B11. Rule 9 (stage 13 narrative) and rule 10 (B09b at /finalize) are out of this pass. Rule 6 first half (B09 downstream candidates) is out of this pass because B09 is not among my named artifacts.

Inputs read, and nothing else:
- Rule sources: prompts/12-verifiers-pipeline.md (VERIFIER C section), prompts/01-gate-0-pipeline.md, prompts/07-emerging-moat-pipeline.md.
- Artifacts: runs/invprecq-2026-11-15/outputs/blocks/B01-gate0.yaml, runs/invprecq-2026-11-15/outputs/reports/01-gate0.md, runs/invprecq-2026-11-15/outputs/blocks/B07-emoat.yaml, runs/invprecq-2026-11-15/outputs/reports/07-emoat.md.
- Model check only: .claude/agents/verifier-c-framework.md.

Method. I re-derived every Gate 0 metric from the inputs the report states. I used the thresholds in prompts/01. I re-derived every Emerging Moat raw score, multiplier and total against prompts/07. I did not test whether a number exists at its source. Verifier A owns that question.

Anchor key. "G L12" = 01-gate0.md line 12. "E L291" = 07-emoat.md line 291. "B01y L27" = B01-gate0.yaml line 27. "B07y L52" = B07-emoat.yaml line 52. "(derived)" = my arithmetic on the cited inputs.

Result. 86 rules checked. 77 PASS, 9 FAIL. 0 CRITICAL, 4 MAJOR, 5 MINOR. Acceptance rate 89.5% (77 / 86, derived). The denominator is 4 or more and the rate is above 60%, so this verifier sets no REWORK trigger.

Two items go to the operator at Halt 1:
1. Gate 0 used two substitute formulas, for ROCE and FCF. Each one alone leaves the class at AVERAGE. If both are scored strictly as written (NOT FOUND, score 0), core falls from 49 to 38 and the class becomes AVOID. See section 1e.
2. Stage 7 applied an "offset" rule that prompts/07 does not contain. On the written matrix the score is 10.8 to 12.6, not 7.8. The top of that range crosses the MODEST edge of 12. Prompts/07 does not settle the point, so an operator ruling is needed. See section 2b.

## 1. GATE 0 (B01) COMPLIANCE

### 1a. Process and formula rules

| ID | Rule (prompts/01) | Stage application | Result | Recomputed value / note |
|---|---|---|---|---|
| G-01 | Rule 6: open with the data-availability line | "Data available: 10 years (FY17 to FY26). Scoring adapted to 10-year history." (G L3) | PASS | |
| G-02 | Rule 4: every extracted number carries an anchor | C1 endpoints 92.04 and 188.45, C2 endpoints 4.17 and 11.76, C3 decline years (G L26-L28) and M11 window CAGRs 3.5% and 21.4% (G L57) carry no inline anchor | FAIL (MINOR) | 188.45 is anchored at G L9. The rest are unanchored. No score change. Routed to Verifier A as unanchored Gate 0 inputs (OR-32 scope). |
| G-03 | Rule 5: NOT FOUND scores 0 | B4 0 (G L23), E2 0 (G L39), M2, M5, M9 PEER DATA NEEDED 0 (G L48, L51, L55), M6 0 (G L52), M12 0 (G L58) | PASS | Correct where the stage applied it. G-04 and G-07 cover where it did not. |
| G-04 | ROCE = EBIT / (Total Assets - Current Liabilities), fixed; use the source ROCE if given; compute only when absent | Computed as EBIT / (equity + reserves + borrowings), because the sheet does not split current liabilities (B01y L27; G L12) | FAIL (MAJOR) | As written: A1 0, A4 0, M3 0, Block A 0, core 43, AVERAGE. Section 1e. |
| G-05 | ROE = PAT / average net worth; state closing basis for the earliest year | "7.02 (closing basis FY17)" (G L15) | PASS | |
| G-06 | WC days formula; state the basis | Revenue basis stated; payables NOT FOUND FY17-FY24 (B01y L29) | PASS | |
| G-07 | FCF = CFO - capex (purchase of PPE + intangibles; exclude acquisitions), fixed | CFO + CFI used as the FCF proxy (G L21; B01y L28) | FAIL (MAJOR) | As written: B2 0, B3 0, Block B 5, core 44, AVERAGE. Section 1e. |
| G-08 | CAGR = (End / Start)^(1/years) - 1 | C1 8.29%, C2 12.21%, 9 years (G L26-L27) | PASS | Re-derived 8.29% and 12.21% (derived). |
| G-09 | Edge rule: negative or zero endpoint = N/M, score 0 | FY17 and FY26 PAT positive (B01y L30) | PASS | Not triggered. |
| G-10 | Edge rule: note a loss-to-profit swing across the window | FY20 loss of 0.72 Cr recorded; no swing between the endpoints (B01y L30) | PASS | "Additionally" ties the note to the N/M case. The stage read it that way and still recorded the FY20 loss. |
| G-11 | Edge rule: C4 = 0 when PAT CAGR is N/M | PAT CAGR computed | PASS | Not triggered. |

### 1b. Block scores, re-derived from the stated inputs

An asterisk (*) means the band is correct on the stated input, but the input basis is the subject of G-04 or G-07.

| ID | Metric | Stated input (anchor) | Band (prompts/01) | Filed | Re-derived | Result |
|---|---|---|---|---|---|---|
| G-12 | A1 median ROCE | 10.71%: (10.28 + 11.14) / 2 of the ten values at G L12 | 10-14.9 = 1 | 1 | 1 | PASS* |
| G-13 | A2 minimum ROCE | 4.15% FY20 (G L12) | <8 = 0 | 0 | 0 | PASS* |
| G-14 | A3 median ROE | 7.19%: (7.02 + 7.35) / 2 of the ten values at G L15 | <12 = 0 | 0 | 0 | PASS |
| G-15 | A4 ROCE trend | FY26 13.32% vs FY17 11.20% (G L16) | latest >= earliest = 5 | 5 | 5 | PASS* |
| G-16 | Block A | 1 + 0 + 0 + 5 | | 6 | 6 | PASS* |
| G-17 | B1 cumulative CFO / PAT | 138.98 / 53.08 = 2.62 (G L19) | >=1.00 = 5 | 5 | 5 | PASS |
| G-18 | B2 FCF-positive years | 7 of 10 = 70% (G L21) | 50-74 = 2 | 2 | 2 | PASS* |
| G-19 | B3 cumulative FCF / PAT | 26.36 / 53.08 = 0.497; ten-year sum re-added to 26.36 (G L21-L22) | 0.40-0.59 = 3 | 3 | 3 | PASS* |
| G-20 | B4 change in WC days | NOT FOUND for FY17 (G L23) | rule 5 = 0 | 0 | 0 | PASS |
| G-21 | Block B | 5 + 2 + 3 + 0 | | 10 | 10 | PASS* |
| G-22 | C1 revenue CAGR | 8.29% (G L26) | 5-9.9 = 1 | 1 | 1 | PASS |
| G-23 | C2 PAT CAGR | 12.21% (G L27) | 10-14.9 = 3 | 3 | 3 | PASS |
| G-24 | C3 positive YoY years | 7 of 9 = 77.8% (G L28) | 75-99 = 3 | 3 | 3 | PASS |
| G-25 | C4 PAT CAGR minus revenue CAGR | +3.92pp (G L29) | >=+3pp = 5 | 5 | 5 | PASS |
| G-26 | Block C | 1 + 3 + 3 + 5 | | 12 | 12 | PASS |
| G-27 | D1 net debt / EBITDA | 67.70 / 30.90 = 2.19x (G L32) | 2-3x = 1 | 1 | 1 | PASS |
| G-28 | D2 interest cover | 2,308.95 / 617.97 = 3.74x (G L33) | 3-4.9 = 2 | 2 | 2 | PASS |
| G-29 | D3 debt / equity | 0.68 (G L34) | 0.5-1.0 = 3 | 3 | 3 | PASS |
| G-30 | D4 current ratio | 10,420.71 / 8,703.22 = 1.197 (G L35) | below 1.2, so 1.0-1.19 = 1 | 1 | 1 | PASS. Edge disclosed (B01y L32). At 1.2 the score is 2 and core is 50, still AVERAGE (derived). |
| G-31 | Block D | 1 + 2 + 3 + 1 | | 7 | 7 | PASS |
| G-32 | E1 promoter holding | 51.97% (G L38) | 50-59.9 = 4 | 4 | 4 | PASS |
| G-33 | E2 3-year promoter change | NOT FOUND (G L39) | rule 5 = 0 | 0 | 0 | PASS. The partial window of +0.06pp scores 3 and gives core 52; the stage disclosed this (B01y L31). |
| G-34 | E3 pledge | 0% (G L40) | 0% = 5 | 5 | 5 | PASS |
| G-35 | E4 contingent liabilities / net worth | 11.94 / 10,278.09 = 0.12% (G L41) | <5% = 5 | 5 | 5 | PASS |
| G-36 | Block E | 4 + 0 + 5 + 5 | | 14 | 14 | PASS |
| G-37 | Core score | 6 + 10 + 12 + 7 + 14 | | 49 | 49 | PASS |

### 1c. Block F moat tests

| ID | Test | Stated input (anchor) | Band | Filed | Result | Recomputed value / note |
|---|---|---|---|---|---|---|
| G-38 | M1 pricing power | Margin 16.17% to 16.46%, +0.29pp (G L44); revenue CAGR 8.29%, below 10% | else = 0 | 0 | PASS | |
| G-39 | M2 cost advantage | PEER DATA NEEDED (G L48) | 0 | 0 | PASS | |
| G-40 | M3 capital efficiency | FAT 188.45 / 100.82 = 1.87x; ROCE 13.32% (G L49) | FAT >1 and ROCE >12 = 1 | 1 | FAIL (MINOR) | The denominator 100.82 is not named and not anchored. On the AR Note 2 figures in B07 (E L87-L88): net-block FAT 1.91x scores 1; gross-block FAT 0.93x scores 0, which gives moat 2 and grand total 51 (derived). Class unchanged. The ROCE leg depends on G-04. |
| G-41 | M4 customer stickiness | 2 decline years (FY20, FY25), CAGR positive (G L50) | 2 decline years, CAGR positive = 1 | 1 | PASS | |
| G-42 | M5 scale | PEER DATA NEEDED (G L51) | 0 | 0 | PASS | |
| G-43 | M6 technology / R&D | R&D amount not quantified (G L52) | 0 | 0 | PASS | |
| G-44 | M7 regulatory | "unregulated product" (G L53) | unregulated = 0 | 0 | PASS | Observation O-4. |
| G-45 | M8 distribution | none (G L54) | 0 | 0 | PASS | |
| G-46 | M9 brand | PEER DATA NEEDED (G L55) | 0 | 0 | PASS | |
| G-47 | M10 switching costs | overall growth, 2 decline years (G L56) | 1 | 1 | PASS | |
| G-48 | M11 network effects | 10 years, so the two-window test runs; latest 3-year CAGR 3.5% is below the prior 21.4%; no CAGR of 20% or more (G L57) | 0 | 0 | PASS | |
| G-49 | M12 negative WC | FY26 121.6 and FY25 139.2 days, both above 45; earlier years NOT FOUND (G L58) | >45 = 0 | 0 | PASS | 0 on any reading. |
| G-50 | Moat score, moats present, moat class | 0+0+1+1+0+0+0+0+0+1+0+0 = 3; 0 tests at 3 or more (G L59) | 0 present = NONE | 3; 0; NONE | PASS | |
| G-51 | Grand total | 49 + 3 (G L62) | | 52 | PASS | |

### 1d. Classification, overrides, output

| ID | Rule | Stage application | Result |
|---|---|---|---|
| G-52 | Data confidence tier | 10 years = full; history_downgrade false (G L62; B01y L25) | PASS |
| G-53 | Classification matrix | Core 40-59 = AVERAGE (G L62) | PASS |
| G-54 | Deal-breakers 1 to 9 tested; driving years stated | DB1 fires (Block A 6 < 8, max GOOD; years FY20-FY22 and FY25 named, G L63; B01y L24). On the stated inputs DB2 to DB9 do not fire: Block B 10; median ROCE 10.71%; CFO/PAT 2.62; pledge 0%; ND/EBITDA 2.19x with cover 3.74x; 2 decline years of 9; PAT positive FY24-FY26; 10 years of history | PASS |
| G-55 | FLAG-GATE0 when the class is AVERAGE or lower with depressors named | Raised with depressors (B01y L12) | PASS |
| G-56 | YAML schema | All 21 keys present; values match the report body | PASS |
| G-57 | analyst_note cap of 200 words | About 80 words (B01y L36) | PASS |
| G-58 | Dashboard elements | All blocks, all line items, moat profile (as a table, G L45-L58), classification, strongest and weakest block, decision line (G L61-L65) | PASS |

Gate 0 tally: 58 rules checked, 54 PASS, 4 FAIL (G-02 MINOR, G-04 MAJOR, G-07 MAJOR, G-40 MINOR).

### 1e. FAIL detail: G-04 and G-07 (formula substitution)

The rule. Prompts/01 says "FORMULA DEFINITIONS (fixed, do not substitute alternatives)". ROCE is EBIT / (Total Assets - Current Liabilities). FCF is CFO minus purchase of PPE and intangibles. Rule 5 says a data point that is not available is NOT FOUND and scores 0.

What the stage did. The screener sheet has no ROCE, no current-liability split and no capex line (B01y L7). The stage computed ROCE on equity + reserves + borrowings (B01y L27). It used CFO + CFI as FCF (B01y L28). It disclosed both. For FY25 and FY26 it checked FCF against AR capex and got the same B3 band, 0.48 (B01y L28). It ran no matching check on ROCE. The AR balance sheet it cites already carries FY26 current liabilities of 8,703.22 lakh (G L35).

The inconsistency. The stage applied rule 5 strictly to B4 (payables missing, G L23), M12 (G L58) and E2 (3-year change missing, G L39). It applied a proxy to ROCE and FCF. The framework has one rule for both cases.

Recomputed values (derived):

| Reading | A1 | A4 | M3 | Block A | B2 | B3 | Block B | Core | Moat | Grand total | Class |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Filed (proxies) | 1 | 5 | 1 | 6 | 2 | 3 | 10 | 49 | 3 | 52 | AVERAGE |
| G-04 strict alone | 0 | 0 | 0 | 0 | 2 | 3 | 10 | 43 | 2 | 45 | AVERAGE |
| G-07 strict alone | 1 | 5 | 1 | 6 | 0 | 0 | 5 | 44 | 3 | 47 | AVERAGE |
| Both strict | 0 | 0 | 0 | 0 | 0 | 0 | 5 | 38 | 2 | 40 | AVOID |

With both strict, DB1 (Block A 0) and DB2 (Block B 5) fire. Each caps at GOOD, so neither binds.

Bounds on the true values (derived from the thresholds, not from data):
- ROCE basis alone. A3 is 0 whatever the ROCE basis, so Block A can run from 0 to 15. Core then runs from 43 to 58. The class is AVERAGE for any true TA - CL value.
- FCF basis alone. B1 stays 5 and B4 stays 0, so Block B can run from 5 to 15. Core then runs from 44 to 54. The class is AVERAGE for any true capex value.
- Both together. Core runs from 38 to 63. The class is AVOID only if Block A plus Block B is below 7. It is GOOD only if they reach 27. The filed sum is 16.

Severity: MAJOR for each. The filed lines do not use the framework's formulas. The best-evidenced reading keeps AVERAGE. The ROCE basis alone cannot move the class, and the FY25-FY26 capex check holds the B3 band. The class flips only when both items take the strict score together. That flip comes from scoring missing inputs at 0. It is not a measured fall in returns or cash. The operator sees it at Halt 1, and the decision stays human.

Two readings and the observation that separates them:
- Reading 1 (stage). The proxies are close substitutes and are disclosed. Core 49, AVERAGE.
- Reading 2 (letter of prompts/01). No substitute formula is allowed, and NOT FOUND scores 0. Core 38, AVOID.
- Separating observation: per-year current liabilities and per-year PPE purchases for FY17-FY24 from the prior annual reports, or a screener export that carries its own ROCE column. The cheapest first step is FY25 and FY26 ROCE on TA - CL from AR p.107, compared with the filed 9.77% and 13.32% (G L12).

Framework note. Rule 5 and the fixed formulas assume a screener export that carries ROCE. This export did not. An operator ruling on disclosed proxies with a cross-check would close the gap for later runs.

### 1f. FAIL detail: G-02 and G-40 (MINOR)

- G-02. Block C has no anchor line, unlike Blocks A, B and F (G L12, L19, L44). The C1 and C2 endpoints and the C3 decline years have no source. The M11 window CAGRs also have no source. Verifier A will treat these as unanchored Gate 0 inputs. No score changes here.
- G-40. Prompts/01 does not define the FAT basis, and the stage did not name it. The basis decides M3: net block scores 1, gross block scores 0. The moat count stays 0 and the class stays NONE either way.

## 2. EMERGING MOAT (B07) COMPLIANCE

### 2a. Rule table

| ID | Rule (prompts/07; verifier rules 3 and 8) | Stage application | Result | Recomputed value / note |
|---|---|---|---|---|
| EM-01 | Rule 1: all six sections plus the Optionality Register | Sections 1 to 6 and the register present (E L21-L387) | PASS | |
| EM-02 | Rule 2: evidence taxonomy on each item | Text tags [DOC], [CLAIM], [INF] mapped to the three symbols at 1.0, 0.7, 0.5 (E L9); tables tagged; the ledger (E L257-L260) backs the untagged narrative items | PASS | |
| EM-03 | Rule 3: source anchor on each evidence item | Some items anchor to upstream blocks rather than a document page: power and fuel 8.99% "B05 from results" (E L148); outside processing "B04 from AR Note 30" (E L45); solar funding "B03" (E L66); auto 90.8% of increment "B03" (E L172); finance cost +40.6% "B05" (E L209) | FAIL (MINOR) | No scored row rests on these alone. B1 rests on Reg 30 31-Mar-2026 and AR p.74 (E L145). The B05 anchor for F2 guidance delivery (E L202) is sanctioned by prompts/07 and is not counted. |
| EM-04 | Rule 5: "NO EVIDENCE FOUND" where none exists | A2, A4, B3, D1, D2, E1, H1, I1 stated (E L127-L225) | PASS | |
| EM-05 | Verifier rule 3: all 23 categories addressed | Summary table has 23 rows, A1 to I2 plus R1 (E L229-L253) | PASS | |
| EM-06 | Section 1A: each item has a status from the prescribed set | GTRE row reads "PO received 12-Feb-2026" (E L28); MKU row reads "PO received 16-Apr-2026" (E L29) | FAIL (MINOR) | Each row needs a prescribed label. On the stated facts (PO in hand, schedule NOT FOUND) both read ANNOUNCED. The other 7 rows comply. |
| EM-07 | Section 1B and 1C | Diversification table (E L39-L45); mix table with both segment definitions (E L49-L57) | PASS | |
| EM-08 | Section 2: 2A, 2B, 2C with arithmetic shown, 2D | Present (E L61-L109). 2C re-derived: 383.89 x 0.9256 = 355.3 lakh, 1.9%; 383.89 x 1.910 = 733.2, 3.9%; 10,000 x 0.9256 = 9,255.7, 49.1%; 10,000 x 1.910 = 19,100, 101.4% (derived). Only the CWIP is "under execution" | PASS | |
| EM-09 | Section 4: 4A, 4B, 4C | Present (E L266-L285) | PASS | |
| EM-10 | Section 5: raw score from the likelihood x impact matrix | A1 MxM 2, A3 LxM 1, B1 MxL 1, B2 HxM 3, F2 MxL 1, R1 LxM 1 (E L293-L315) | PASS | All six cells re-derived. |
| EM-11 | Section 5: "no evidence = 0"; LL = 1; Section 3: "evidence table or NO EVIDENCE FOUND" | An offset rule not in prompts/07 zeroes rows that carry tagged evidence (B07y L52) | FAIL (MAJOR) | Written matrix: 10.8 to 12.6, NONE to MODEST. Section 2b. |
| EM-12 | Section 5: multiplier by evidence tier | A1 at 0.7 on [DOC] plus [INF] evidence, with no [CLAIM] leg (E L293; B07y L21) | FAIL (MAJOR) | 0.5: A1 1.0, total 7.4. 1.0: A1 2.0, total 8.4. Section 2c. |
| EM-13 | Verifier rule 3: no claim-only row scored as documented | A3 (all [CLAIM]) at 0.7; R1 at 0.7 (E L295, L315) | PASS | |
| EM-14 | Adjusted total | 1.4 + 0.7 + 1.0 + 3.0 + 1.0 + 0.7 = 7.8 (E L316) | PASS | Arithmetic correct on the filed multipliers. |
| EM-15 | Classification band on the filed score | 7.8 is below 12, so NO MEANINGFUL EMERGING MOAT (E L320) | PASS | The band change under EM-11 is carried there, not here. |
| EM-16 | Rule 6 guard: count of Strong and Moderate rows stated; test against 12 | 2 Moderate (A1, B2); 6 of 23 rows scored (E L255) | PASS | |
| EM-17 | Rule 6: documented recount performed and stated | Recount line present (E L262; B07y L24) | PASS | |
| EM-18 | Recount line and evidence_mix agree with the evidence tables | Line says "16 documented items across 9 categories ... plus the Section 2 approval" (E L262); evidence_mix 16 / 15 / 6 (B07y L23) | FAIL (MINOR) | 15 items sit in the 9 categories, plus 1 in Section 2. The ledger leaves out 3 [DOC] and 2 [CLAIM] items that the Section 3 tables tag. Documented is at least 19, claim at least 17. Section 2d. |
| EM-19 | Verifier rule 8: category 21 (I1) present; above 0 only with both legs and one documented (b)-leg source | Present; legs (a) and (b) NOT FOUND; score 0 (E L223) | PASS | |
| EM-20 | Verifier rule 8: category 22 (I2) present; above 0 only with a specific named sacrifice | Present; "no competitor must destroy a pricing regime, channel or product line"; score 0; government-tier leg addressed (E L225) | PASS | |
| EM-21 | Section 5: I1 and I2 contribution stated separately | "I1/I2 contribution: 0.0 of 7.8" (E L318) | PASS | |
| EM-22 | One improvement, one mechanism | PLR repeat order under B2 only (E L170); end-market diversification under B2 only (E L172); renewables under B1 only (E L219); import substitution under R1 only (E L215) | PASS | |
| EM-23 | Optionality Register: qualifying rows, four columns, carried in the block | 11 rows, each scored 0 or resting on claim or inference evidence (E L330-L342); mirrored row for row in B07y L33-L44 | PASS | |
| EM-24 | F2 cross-references the B05 promise-delivery record | "B05: 5 delivered, 1 partial, 0 missed" (E L202) | PASS | |
| EM-25 | Section 6: 6A to 6E; 6C uses the injected B01 block | 6C values 49, 3, 52, 0, NONE, AVERAGE match B01y L16-L22 (E L364-L371) | PASS | |
| EM-26 | 6D: full reasoning on the HIGH POTENTIAL and TURNAROUND rows | Both reasoned (E L374-L375) | PASS | The matrix text is absent from prompts/07 (observation O-2). |
| EM-27 | YAML schema | All 19 keys present; em_classification "NONE" is in the enum; active_categories hold only the Moderate rows A1 and B2 (B07y L19-L22) | PASS | |
| EM-28 | analyst_note cap of 200 words | About 115 words (B07y L52) | PASS | |

Emerging Moat tally: 28 rules checked, 23 PASS, 5 FAIL (EM-03 MINOR, EM-06 MINOR, EM-11 MAJOR, EM-12 MAJOR, EM-18 MINOR).

### 2b. FAIL detail: EM-11 (offset rule not in prompts/07)

The rule. Section 3 of prompts/07 gives two states per category: "evidence table or NO EVIDENCE FOUND". Section 5 scores from the matrix "HH=4, HM/MH=3, HL/MM/LH=2, ML/LM=1, LL=1, no evidence=0", then applies the multiplier. Zero is the score for no evidence. The LL cell scores 1 and covers weak, unlikely evidence.

What the stage did. It added a precondition: "a row scores only when a dated, anchored item shows a company-specific advantage forming and no same-corpus evidence offsets it" (B07y L52). The stage calls this "a rule choice" (B07y L52). The summary table then shows a third state that prompts/07 does not have. G1 and G2 read "No (offset)" with type DOC (E L246-L247). H2 reads "No" with type CLAIM (E L249). E2 reads "Partial (not scored)" with type DOC / CLAIM (E L243).

Recomputed values. These use the written matrix with LL = 1 as the floor, and the stage's own multiplier convention, the weakest load-bearing leg (E L289).

| Row | Filed | Evidence in the stage's own text | Prompts/07 indicator it matches | Written-matrix floor |
|---|---|---|---|---|
| E2 | 0 | Foreign exchange earned +36.3% [DOC] AR p.74 (E L185); China+1 language [CLAIM] AR p.76 (E L187) | export growth; supply-chain-shift language | 0.7 (1.0 if the export leg alone carries the row) |
| G1 | 0 | CARE upgrade BBB- to BBB [DOC] CARE p.1 (E L209) | rating upgrade | 1.0 |
| G2 | 0 | Operating cycle 150 to 133 days [DOC] CARE p.3 (E L211) | WC days declining | 1.0 |
| H2 | 0 | TOT-DRDO superalloy core [CLAIM] Deck Q4 p.5 (E L217) | inbound tech licensing | 0.7 |
| C1 | 0 | Co-development [CLAIM] AR p.37 (E L170) | co-development | 0.7 |
| F1 | 0 | "80+ engineers" [CLAIM] Deck H1 p.4 (E L193; ledger claim 6, E L259) | R&D headcount growth | 0.7 |
| C2 | 0 | The positive legs are credited once, under B2; documented concentration moved from 47% to 50%, against the row (E L172) | n/a | 0 (the single-credit rule holds) |

| Set | Added | Total with A1 as filed (0.7) | Total with A1 at 0.5 (EM-12) | Band |
|---|---|---|---|---|
| Filed | 0 | 7.8 | 7.4 | NONE |
| Narrow: rows whose summary line carries an evidence type (E2, G1, G2, H2) | 3.4 | 11.2 | 10.8 | NONE |
| Wide: the narrow set plus C1 and F1 | 4.8 | 12.6 | 12.2 | MODEST (edge 12) |
| Stage's own sensitivity: 7 rows at 0.7, C2 included (E L326) | 4.9 | 12.7 | 12.3 | MODEST |

Guard check on the wide set. Twelve rows would carry a score. Rule 6 of prompts/07 then asks for a re-examination of claims credited as documented. The four claim rows already sit at 0.7, so that re-examination changes nothing. The guard is a recount, not a rule that sets rows to zero.

Effect. The band is NONE or MODEST. The UA qualifier (EM of 25 or more) fails under every reading. On the stage's band logic the 6D combined class stays AVERAGE. The Pillar 3 effect is NOT ASSESSED in phase 1. The phase-3 audit checks which EM reading B11 uses.

Severity: MAJOR. The filed score departs from the written matrix. The decision likely survives.

Two readings and the item that separates them:
- Reading 1 (stage). Evidence that same-corpus evidence offsets is not evidence that an advantage is forming. Prompts/07 rules 4 to 6 support this: "Be skeptical", "Never force-fit", "An honest sparse scan beats an inflated complete one".
- Reading 2 (written matrix). Any row with tagged evidence takes a matrix cell, with LL as the floor. The L rating and the multiplier carry the doubt.
- Separating item: an operator ruling on one question. Does same-corpus counter-evidence set a row to 0, or does the row score LL? Prompts/07 does not say. Until the ruling, carry both scores into the dossier: 7.8 as filed, and 10.8 to 12.6 on the written matrix.

### 2c. FAIL detail: EM-12 (A1 multiplier)

The filed A1 multiplier is 0.7, "capability documented, rarity unproven" (E L293). A1's evidence carries [DOC] items, the CONSARC vacuum furnace and the GTRE order (E L120-L121). It also carries one [INF] item, rarity (E L123). No A1 item carries [CLAIM]. The block confirms this: "DOCUMENTED capability, INFERENCE rarity" (B07y L21). 0.7 is the claim multiplier, and it matches no tier the row holds.

Recomputed values (derived):
- By the stage's own weakest-leg convention (E L289), rarity [INF] gives 0.5. A1 adjusted 1.0, total 7.4.
- If the long-lead vacuum furnace, a listed A1 indicator, carries the row and rarity is not load-bearing, the multiplier is 1.0. A1 adjusted 2.0, total 8.4.

The filed 0.7 sits above the stage's own convention and below the documented-indicator reading. The band is NONE under both on the filed set, and MODEST under both on the EM-11 wide set (12.2 and 13.2). Severity MAJOR: the value is wrong, and the decision survives.

### 2d. FAIL detail: EM-03, EM-06, EM-18 (MINOR)

- EM-18. The ledger maps documented items as follows: A1 2, B2 5, B1 1, F2 2, R1 1, E2 1, G1 1, G2 1, C2 1. That is 15 items in 9 categories, plus item 12 in Section 2, for 16 in all (E L258). The headline line reads as 16 in the 9 categories plus the approval (E L262; B07y L24). The ledger also leaves out five tagged Section 3 items. Three are [DOC]: B1 power and fuel 8.99% vs 9.17% (E L148), E2 exports 22.27 Cr (E L186), F2 disclosure quality (E L200). Two are [CLAIM]: B2 CEMILAC and HAL approved supplier (E L156), A3 vacuum-expert hire (E L133). On the stage's own tags, documented is at least 19 and claim at least 17, against 16 and 15 in evidence_mix. The guard outcome does not change: 6 of 23 rows are scored, 2 are Moderate, and 9 categories hold documented items.
- EM-03 and EM-06 are listed in table 2a. Neither changes a score.

## 3. VALUATION (B10, B11): PENDING PHASE 3

This audit did not run. B10 and B11 do not exist in phase 1. Verifier rules 4, 5 (B11 application), 6 (stage 11 catalysts), 7, and 11 to 15 run in the phase-3 valuation pass. The valuation, expectation_ledger, recomputed_destination_pe and recomputed_decision fields in B12c are left pending. Phase-3 carry-forward: check which EM reading (EM-11) and which Gate 0 reading (G-04, G-07) feed Pillar 3 and any Gate 0 input to B11.

## 4. OBSERVATIONS (not scored)

- O-1. Template defect. prompts/12-verifiers-pipeline.md line 379 holds the placeholder text "(same line, comment "# rule 9; any fail = REWORK stage 13")" where the rule 9 key set should be. I emitted a `narrative` key marked pending. The operator should fix this in a framework PR.
- O-2. Framework gap. Prompts/07 Section 6D names the labels of the "standard matrix" but does not define the matrix. The stage disclosed this (E L373). Neither the stage nor this verifier can test 6D beyond band logic.
- O-3. Framework gap. Prompts/07 does not say whether same-corpus counter-evidence sets a row to 0 or scores LL. This is the root of EM-11. An operator ruling is needed.
- O-4. M7 basis. The basis line says "unregulated product" (G L53), but the A&D line holds DGAQA and CEMILAC approvals (E L155-L156). If the A&D line counts as a regulated segment, the test needs a player count and reads PEER DATA NEEDED. The score is 0 under both readings, so this is not a finding.
- O-5. Cross-stage items routed to Verifier A and the orchestrator. Not scored here. (a) B01 puts note 6 on results page 7, OCR-illegible (G L8; B01y L10). B07 cites "Board outcome 14-Nov-2026 p.3 note 6" (E L18). (b) The B01 M3 denominator of 100.82 Cr (G L49) differs from the B07 net block of 9,866.35 lakh (E L88).

## 5. COUNTS

| Framework | Rules checked | PASS | FAIL | CRITICAL | MAJOR | MINOR |
|---|---|---|---|---|---|---|
| Gate 0 (B01) | 58 | 54 | 4 | 0 | 2 | 2 |
| Emerging Moat (B07) | 28 | 23 | 5 | 0 | 2 | 3 |
| Valuation (B11) | 0 (phase 3) | | | | | |
| Total | 86 | 77 | 9 | 0 | 4 | 5 |

Acceptance rate 89.5% (77 / 86, derived).

```yaml
stage: B12c
company: "INVPRECQ"
run_date: "2026-11-15"
model: "claude-opus-5-5"  # must equal .claude/agents frontmatter; the orchestrator compares it
status: complete  # phase-1 scope: gate0 + emoat only; valuation half runs in phase 3 after B11
gate0: {rules_checked: 58, fails: ["G-02 rule 4 anchors missing on C1/C2 endpoints, C3 decline years, M11 window CAGRs (MINOR)", "G-04 ROCE fixed formula substituted with EBIT/(equity+reserves+borrowings) (MAJOR)", "G-07 FCF fixed formula substituted with CFO+CFI (MAJOR)", "G-40 M3 FAT denominator 100.82 unnamed and unanchored; gross-block basis scores 0 (MINOR)"]}
emoat: {rules_checked: 28, fails: ["EM-03 evidence items anchored to B03/B04/B05 blocks, not document pages (MINOR)", "EM-06 1A status labels missing on GTRE and MKU rows (MINOR)", "EM-11 offset rule not in prompts/07 zeroes rows with tagged evidence; written matrix 10.8-12.6 vs filed 7.8 (MAJOR)", "EM-12 A1 multiplier 0.7 matches no tier the row holds (DOC + INF) (MAJOR)", "EM-18 recount line miscounts (15 in 9 categories + 1 Section 2) and ledger omits 3 DOC + 2 CLAIM table items (MINOR)"]}
valuation: {rules_checked: 0, fails: []}  # PENDING PHASE 3: B10/B11 do not exist in phase 1
expectation_ledger: {present: null, downside_row: null, all_rows_confirm_by: null, all_rows_metric_threshold: null, prob_in_range: null, decay_status_valid: null, off_ledger_credit: null, residual_pct_cmp: null, residual_starter_cap_ok: null, fails: []}  # rules 13-14; PENDING PHASE 3, not checked in phase 1; any fail = REWORK stage 11
narrative: {checked: false, fails: []}  # rule 9; PENDING, stage 13 not yet run, fires at /finalize; any fail = REWORK stage 13
recomputed_destination_pe: ""  # PENDING PHASE 3
recomputed_decision: ""        # PENDING PHASE 3
findings:
  - {id: "G-04", framework: "Gate 0", severity: "MAJOR", rule: "ROCE fixed as EBIT / (Total Assets - Current Liabilities); missing input = NOT FOUND, score 0", filed: "EBIT / (equity + reserves + borrowings); A1 1, A4 5, M3 1; Block A 6; core 49", recomputed: "as written: A1 0, A4 0, M3 0; Block A 0; core 43, AVERAGE; any true TA-CL ROCE keeps core 43-58 (AVERAGE)", decision_effect: "none alone; with G-07 also strict, core 38 = AVOID; flag for Halt 1"}
  - {id: "G-07", framework: "Gate 0", severity: "MAJOR", rule: "FCF fixed as CFO - purchase of PPE and intangibles; missing input = NOT FOUND, score 0", filed: "CFO + CFI proxy; B2 2, B3 3; Block B 10", recomputed: "as written: B2 0, B3 0; Block B 5; core 44, AVERAGE; FY25-FY26 AR capex check holds the B3 band (0.48)", decision_effect: "none alone; with G-04 also strict, core 38 = AVOID; separating observation: FY17-FY24 current liabilities and PPE purchases from prior ARs"}
  - {id: "G-02", framework: "Gate 0", severity: "MINOR", rule: "rule 4 anchor on every extracted number", filed: "C1/C2 endpoints 92.04, 4.17, 11.76, C3 decline years, M11 3.5% and 21.4% carry no anchor", recomputed: "no score change; routed to Verifier A", decision_effect: "none"}
  - {id: "G-40", framework: "Gate 0", severity: "MINOR", rule: "M3 basis stated and anchored", filed: "FAT 188.45/100.82 = 1.87x, M3 1; denominator unnamed", recomputed: "net block 1.91x = 1; gross block 0.93x = 0, moat 2, grand total 51", decision_effect: "none; moats_confirmed 0 and class NONE either way"}
  - {id: "EM-11", framework: "Emerging Moat", severity: "MAJOR", rule: "Section 5 matrix: no evidence = 0, LL = 1; Section 3: evidence table or NO EVIDENCE FOUND", filed: "unwritten offset rule zeroes E2, G1, G2, H2, C1, F1; em_score 7.8 NONE", recomputed: "written matrix: narrow set 10.8-11.2 (NONE); wide set 12.2-12.6 (MODEST, edge 12)", decision_effect: "band NONE vs MODEST; UA qualifier (EM >=25) unmet either way; Pillar 3 effect checked in phase 3; operator ruling needed on offset evidence"}
  - {id: "EM-12", framework: "Emerging Moat", severity: "MAJOR", rule: "multiplier by evidence tier: DOC 1.0, CLAIM 0.7, INF 0.5", filed: "A1 at 0.7; A1 evidence is DOC (furnace, GTRE order) + INF (rarity), no CLAIM", recomputed: "0.5 by the stage's weakest-leg convention: A1 1.0, total 7.4; 1.0 on the documented furnace: A1 2.0, total 8.4", decision_effect: "none; NONE either way on the filed set"}
  - {id: "EM-03", framework: "Emerging Moat", severity: "MINOR", rule: "rule 3 document anchor on each evidence item", filed: "items anchored to B03, B04 and B05 (beyond the promise record) at E L45, L66, L148, L172, L209", recomputed: "no score change; no scored row rests on these alone", decision_effect: "none"}
  - {id: "EM-06", framework: "Emerging Moat", severity: "MINOR", rule: "Section 1A status from the prescribed set", filed: "GTRE and MKU rows read PO received", recomputed: "ANNOUNCED for both on the stated facts", decision_effect: "none"}
  - {id: "EM-18", framework: "Emerging Moat", severity: "MINOR", rule: "recount line and evidence_mix match the evidence tables", filed: "16 documented across 9 categories plus the approval; evidence_mix 16/15/6", recomputed: "15 in 9 categories + 1 Section 2 = 16; ledger omits 3 DOC and 2 CLAIM table items: documented >=19, claim >=17", decision_effect: "none; guard outcome unchanged (6 of 23 scored)"}
critical_count: 0
major_count: 4
minor_count: 5
acceptance_rate: 89.5             # rules passed ÷ rules checked, %
```
