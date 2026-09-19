# STAGE 12 VERIFIER C: FRAMEWORK ADHERENCE, SSWL (PHASE 1 SCOPE)

Run date: 2026-09-19 | Model: claude-opus-5 | Emits: B12c

Scope: Gate 0 (B01) and Emerging Moat (B07) only. The valuation audit (B10, B11, rules 4-7 and 11-15) is PENDING PHASE 3. Rule sources: prompts/01-gate-0-pipeline.md and prompts/07-emerging-moat-pipeline.md. Inputs: outputs/reports/01-gate0.md, outputs/blocks/B01-gate0.yaml, outputs/reports/07-emoat.md, outputs/blocks/B07-emoat.yaml.

This audit checks rule application. It does not check whether a number is in the source; Verifier A owns that. Every recomputation below uses the inputs as B01/B07 state them.

## HEADLINE

- 78 rules checked. 67 PASS, 11 FAIL. Acceptance 86%.
- 0 CRITICAL, 4 MAJOR, 7 MINOR.
- B01 arithmetic is clean. Every block score re-derives from the stated inputs and thresholds.
- The Gate 0 classification GOOD is fragile. Three rule readings move it. The strict partial-window reading gives AVERAGE (Core 47). The parallel M5 reading gives GOOD+ (4 moats, STRONG). B01 showed neither alternative. Operator ruling needed.
- B07 em_score 17 re-derives exactly (17.1). MODEST holds across every multiplier reading (16.5 to 18.1).
- B07 credits the captive-power investments twice, in B1 and H2. It avoided this double count for E2/H1 but not here.

## PART 1: GATE 0 (B01) COMPLIANCE TABLE

Inputs as stated in 01-gate0.md. Recomputed value beside every FAIL.

| # | Rule | B01 value | Re-derived | Result |
|---|---|---|---|---|
| 1 | Opening "Data available" line | 5 yrs FY22-FY26 | present | PASS |
| 2 | Source anchors on extracted numbers | present | present | PASS |
| 3 | ROCE formula fixed: EBIT / (TA - CL), no substitution | FY22-24 proxy Equity+Borrowings | see F1 | FAIL MAJOR |
| 4 | ROE = PAT / avg NW; earliest year closing-only stated | stated for FY22 | complies | PASS |
| 5 | WC Days formula, basis (revenue vs COGS) stated | basis not stated | see F4 | FAIL MINOR |
| 6 | FCF = CFO - capex, acquisitions excluded | "Purchase of fixed assets" | complies | PASS |
| 7 | CAGR formula | (End/Start)^(1/n)-1 | complies | PASS |
| 8 | CAGR edge rules (N/M on non-positive endpoint; loss-to-profit note) | endpoints positive, not N/M | complies; no swing across the window | PASS |
| 9 | A1 median ROCE | 18.40% = 3 | sorted 14.43/16.97/18.40/20.43/21.73, median 18.40, band 15-19.9 = 3 | PASS |
| 10 | A2 min ROCE | 14.43% = 3 | band 12-14.9 = 3 | PASS (on stated inputs; proxy-driven, see F1) |
| 11 | A3 median ROE | 18.57% = 4 | sorted 11.09/12.73/18.57/21.58/52.36, median 18.57 = 4 | PASS |
| 12 | A4 ROCE trend | -4.76pp = 1 | 16.97 - 21.73 = -4.76, band 3-5pp = 1 | PASS (mixed basis, see F1) |
| 13 | Block A sum | 11 | 3+3+4+1 = 11 | PASS |
| 14 | B1 cumulative CFO/PAT | 1.230 = 5 | 1,795.41 / 1,459.43 = 1.230, band >=1.00 = 5 | PASS |
| 15 | B2 FCF-positive proportion | 2/2 = 5 | arithmetic complies | PASS (window, see F2) |
| 16 | B3 cumulative FCF/PAT | 1.150 = 5 | (304.29+138.84) / (195.28+190.22) = 443.13 / 385.50 = 1.150 = 5 | PASS (window, see F2) |
| 17 | B4 WC Days change | +0.11 = 3 | 39.26 -> 39.37 (40.08+61.24-62.06; 42.88+67.05-70.56), band +/-5 = 3 | PASS (window, see F2) |
| 18 | Block B sum | 18 | 5+5+5+3 = 18 | PASS |
| 19 | C1 revenue CAGR | 9.85% = 1 | (5,182.80/3,559.95)^0.25 - 1 = 9.84-9.85%, band 5-9.9 = 1 | PASS |
| 20 | C2 PAT CAGR | -1.91% = 0 | (190.22/205.46)^0.25 - 1 = -1.91%, negative = 0 | PASS |
| 21 | C3 positive YoY years | 4/4 = 5 | 100% = 5 | PASS |
| 22 | C4 PAT minus revenue CAGR | -11.76pp = 0 | band < -8pp = 0 | PASS |
| 23 | Block C sum | 6 | 1+0+5+0 = 6 | PASS |
| 24 | D1 ND/EBITDA | 1.60x = 3 | 816.97 / 510.23 = 1.601, band 1-2x = 3 | PASS |
| 25 | D2 interest cover | 3.04x = 2 | 374.18 / 123.22 = 3.037, band 3-4.9 = 2 | PASS |
| 26 | D3 D/E | 0.459 = 4 | 828.37 / 1,804.82 = 0.459, band 0.1-0.5 = 4 | PASS |
| 27 | D4 current ratio | 1.006 = 1 | 1,635.79 / 1,626.46 = 1.006, band 1.0-1.19 = 1 | PASS |
| 28 | Block D sum | 10 | 3+2+4+1 = 10 | PASS |
| 29 | E1 promoter holding | 61.14% = 5 | band >=60 = 5 | PASS |
| 30 | E2 promoter change, 3 yrs | -0.10pp (1 yr) = 3 | band +/-1 = 3 on 1 yr | PASS arithmetic (window, see F2) |
| 31 | E3 pledge | 0% = 5 | = 5 | PASS |
| 32 | E4 contingent liabilities / NW | 3.34% = 5 | 60.22 / 1,804.82 = 3.34%. Robust: adding the ~24.9 Cr CARO disputes gives 4.72%, still < 5% = 5 | PASS |
| 33 | Block E sum | 18 | 5+3+5+5 = 18 | PASS |
| 34 | Core score | 63 | 11+18+6+10+18 = 63 | PASS |
| 35 | M1 pricing power | 1 | margin -2.88pp despite growth = 1 | PASS |
| 36 | M2 cost advantage | 1 | 9.84 - 11.29 = -1.45pp, +/-2pp = 1 | PASS |
| 37 | M3 capital efficiency | 3 | FAT 2.63x > 2, ROCE 16.97 > 15 = 3 | PASS |
| 38 | M4 customer stickiness | 5 | zero decline years, receivable days +2.64 (within 10) = 5 | PASS |
| 39 | M5 scale and dominance | 1 | reading-dependent: 0 / 1 / 3 | FAIL MAJOR, see F3 |
| 40 | M6 technology/R&D | 0, "N/A not in provided data" | data was in the AR; score still 0 | FAIL MINOR, see F5 |
| 41 | M7 regulatory | 0 | unregulated = 0 | PASS |
| 42 | M8 distribution | 0 | B2B OEM, none = 0 | PASS |
| 43 | M9 brand, GM proxy stated | 0 | 33.18 vs 34.76 median, at/below = 0 | PASS |
| 44 | M10 switching costs | 5 | grew every year, receivable days +2.64 = 5 | PASS |
| 45 | M11 network effects, <6 yrs conservative, stated | 0 | CAGR 9.85% < 15 = 0 | PASS |
| 46 | M12 negative WC/float | 1 | ~39 days, band 15-45 = 1 | PASS (window, see F2) |
| 47 | Moat sum, count, class | 17; 3 present; MODERATE | 1+1+3+5+1+0+0+0+0+5+0+1 = 17; M3/M4/M10; 2-3 = MODERATE | PASS |
| 48 | Data confidence, classification matrix, deal-breakers, history downgrade, FLAG-GATE0 condition, YAML schema | 5 yrs "lower" tier with full-cycle caveat; Core 60-79 + MODERATE = GOOD; 9 deal-breakers each tested with driving years; no downgrade; no FLAG-GATE0 (GOOD) | all comply | PASS |
| (rule) | Rule 5/6 treatment of partial-window metrics | favourable reading taken silently | see F2 | FAIL MAJOR |

Count note: the table rows 1-48 plus the partial-window rule give 49 lines; rows 15/16/17/30/46 carry the window issue under the single partial-window rule, and row 48 bundles six structural checks into one PASS. Rules counted for scoring: 48 (43 PASS, 5 FAIL).

### Gate 0 FAIL detail

**F1. ROCE formula substitution. MAJOR.**
The rule reads "FORMULA DEFINITIONS (fixed, do not substitute alternatives)". B01 computed FY22-FY24 capital employed as Equity + Total Borrowings, which substitutes a formula. B01 flagged the break openly (FLAG-DATA-GAP). The flag does not cure the substitution. It also treats Block A differently from Block B. Block B scored on the exact FY25-FY26 window; Block A filled FY22-FY24 with a proxy.
The proxy matters for A2. FY24 proxy CE is 2,490.61 against FY25 exact 2,028.30, and FY24 (14.43%) sets the minimum.
Recomputed on the exact-year window (FY25-FY26, the treatment B01 gave B2-B4): A1 median 17.69% = 3; A2 min 16.97% = 5; A3 = 4; A4 18.40 -> 16.97 = -1.43pp = 3. Block A = 15 (B01: 11). Core = 67 (B01: 63). Classification GOOD unchanged.
The proxy runs the other way on A4. If the proxy understates FY22 ROCE, as B01 says, the true FY22-to-FY26 decline exceeds 4.76pp and could pass 5pp, giving A4 = 0. Two readings: proxy-window A4 = 1 or less; exact-window A4 = 3. The separating observation is FY22-FY24 current liabilities from the FY23/FY24 ARs. Those ARs are not in the corpus.

**F2. Partial-window scoring against rules 5 and 6. MAJOR.**
Rule 6 sets a 3-year minimum history. Rule 5 says an unavailable data point is marked N/A and scored 0. B01 scored B2 (5), B3 (5), B4 (3) and M12 (1) on a 2-year window and E2 (3) on a 1-year window. Every one is below the 3-year minimum. The rules do not state a partial-window treatment. B01 took the favourable reading and did not show the strict one. Each line carries a flag. The classification consequence is not shown.
Recomputed on the strict reading (N/A = 0): B2 0, B3 0, B4 0, E2 0, M12 0. Block B = 5, Block E = 15, Core = 47, moat 16. Core 40-59 = AVERAGE. Deal-breaker 1/2 (Block B < 8, max GOOD) does not bind below AVERAGE.
The B01 Core of 63 sits 3 points above the 60 boundary. 13 of those points rest on 2-year windows. This is not a finding that B01 is wrong. It is a finding that the classification depends on an unruled reading. Operator ruling needed: does a metric with fewer than 3 computable years score on its window, or score 0?

**F3. M5 margin-rank set. MAJOR.**
Rule: "largest mcap in segment AND top margin among top 3 = 5 | top 3 mcap AND margin top 2 = 3 | top 5 mcap = 1". The 5-band ranks margin among the top-3 mcap set. B01 ranked margin across all four names, placing SSWL 3rd, and scored 1.
Parallel reading: the top-3 mcap set is UNOMINDA (74,146.79), SSWL (5,856.55), WHEELS (5,315.89). Margins in that set: 11.45%, 9.84%, 7.55%. SSWL is 2nd. "Top 3 mcap AND margin top 2" is met. M5 = 3. Moats present = 4 (M3, M4, M5, M10) = STRONG. Moat score 19. Core 63 + STRONG = GOOD+.
Strict reading: the rule says "segment". A 3-peer set is not a segment ranking. Rule: peer data not provided = 0, PEER DATA NEEDED. M5 = 0, moat 16, MODERATE, GOOD.
B01's score of 1 sits between these and follows neither. On a 4-name set, "top 5 mcap" is met by construction. The range runs GOOD to GOOD+. The separating observation is a full listed wheel/rim segment mcap and margin table.

**F4. WC Days basis not stated. MINOR.**
The formula requires "state which basis was used" for inventory and payable days. B01 does not state revenue or COGS basis for B4/M12. No score change is determinable. B4's +0.11-day change sits far inside the +/-5 band on either basis for the same basis both years.

**F5. M6 marked "N/A (not in provided data)" when data was present. MINOR.**
B07 found total R&D spend at 1.14% (FY25) and 0.40% (FY26) of turnover in the same FY26 AR (B07 cites AR p.2394-2397). As written, M6 = 0 (0.40% < 1%, margin below peer median). Score unchanged. The data_notes line calling it a genuine data gap is wrong.

### Gate 0 observations (not fails)

- M4 and M10 both score on the same two inputs (revenue-growth years and receivable-day drift). The rubric defines them that way, so B01 applied it as written. It gives 10 of the 17 moat points and 2 of the 3 moats present from one pattern. Noted for the operator; not a B01 fault.
- M4 cites FY26 receivable days 42.87; B4 cites 42.88. Rounding only; no score effect.
- E4 excludes ~Rs 24.9 Cr CARO disputed dues. Including them gives 4.72%, still band 5. Robust.

## PART 2: EMERGING MOAT (B07) COMPLIANCE TABLE

| # | Rule | Result |
|---|---|---|
| 1 | Six sections present, one response | PASS |
| 2 | Evidence taxonomy on every item | PASS |
| 3 | Source anchors (AR p.__, call, slide) | FAIL MINOR, see G4 |
| 4 | NO EVIDENCE FOUND where none, no force-fit | PASS |
| 5 | 1A pipeline table fields (status, type, launch, potential, difference) | PASS |
| 6 | 1B diversification direction | PASS |
| 7 | 1C mix shift table | PASS |
| 8 | 2A capex table | PASS |
| 9 | 2B utilisation per facility | PASS (tensions flagged, not resolved; acceptable) |
| 10 | 2C arithmetic shown on one basis | FAIL MINOR, see G5 |
| 11 | 2D geography | PASS |
| 12 | All 23 rows addressed (A1-A4, B1-B3, C1-C2, D1-D2, E1-E2, F1-F2, G1-G2, H1-H3, I1-I2, R1) | PASS |
| 13 | Section 3 summary table with count and recount line in the required form | PASS |
| 14 | Recount accuracy | FAIL MINOR, see G2 |
| 15 | Likelihood x impact mapping (HH 4, HM/MH 3, HL/MM/LH 2, ML/LM 1, LL 1) | PASS: A3 LL 1, B1 MM 2, B2 HH 4, C1 MM 2, E1 LM 1, F2 HM 3, H1 LL 1, H2 HM 3, H3 ML 1, R1 HM 3 |
| 16 | Multipliers from the defined set 1.0 / 0.7 / 0.5, applied consistently | FAIL MINOR, see G3 |
| 17 | No CLAIM-only category scored as DOC | PASS: A3, B2, C1, E1 all at 0.7 |
| 18 | Adjusted total arithmetic | PASS: 0.7+2.0+2.8+1.4+0.7+3.0+0.5+3.0+1.0+2.0 = 17.1 |
| 19 | Classification band | PASS: 12-24 = MODEST |
| 20 | I1/I2 contribution stated separately | PASS: 0.0 |
| 21 | Categories 21/22 present; I1 > 0 only with both legs and a DOC (b) leg; I2 > 0 only with a named sacrifice | PASS: both present, both 0 with reasons |
| 22 | One improvement, one mechanism | FAIL MAJOR, see G1 |
| 23 | Section 4 (4A, 4B, 4C) | PASS |
| 24 | Optionality register, table and YAML | PASS |
| 25 | 6A-6E present | PASS |
| 26 | 6C uses the injected B01 block correctly (Core 63, moat 17, 3 moats, GOOD) | PASS |
| 27 | 6D combined matrix not invented; NOT FOUND stated | PASS |
| 28 | Strength enum Strong/Moderate/Weak/None | FAIL MINOR, see G6 |
| 29 | YAML schema complete | PASS |
| 30 | Not conflated with FTTCP | PASS |

Rules counted: 30 (24 PASS, 6 FAIL).

### Emerging Moat FAIL detail

**G1. Captive-power investments credited twice. MAJOR.**
B07 credits Echanda Urja and Clean Max Astria in B1 (MM, DOC, 2.0). It cites them again in H2 ("also board-approved equity investments (DOC tier, Section 3 B1)"), and the recount counts them under both B1 and H2. B07 applied the one-mechanism rule to E2/H1 and not here. On the recomputation, H2's H x M = 3.0 can rest on the Arays/Hainan tripartite agreement alone (DOC). em_score 17 and MODEST do not change. The recount loses 2 items.

**G2. Completionist recount count. MINOR.**
The line states "15 documented items across 6 categories". The items it lists sum to 13: B1 2, F1 1, F2 4, H2 3, H3 2, R1 1. After the G1 duplicate, 11 are distinct. evidence_mix.documented = 15 carries the same overcount. The active count of 10 non-zero categories sits below the 12 trigger, so the guard did not have to fire.

**G3. Multipliers outside the defined set, applied unevenly. MINOR.**
- R1 uses a blended 0.67. The framework defines 1.0, 0.7 and 0.5 only. 0.67 is not even the midpoint of 1.0 and 0.7. R1's raw score is driven by the company-specific attribution, which B07 types CLAIM. At 0.7: 2.1 (B07: 2.0).
- H1 uses INFER 0.5 as a discount for the contradiction. The evidence is a management statement (CLAIM, 0.7). The multiplier grades evidence tier, not credibility. At 0.7: 0.7 (B07: 0.5). A reversed claim could instead argue for 0 under "never force-fit".
- F2 takes DOC 1.0 on a row B07's own summary types DOC/CLAIM. Two of the four DOC items are EBITDA/wheel beats, a management-reported metric, not an audited line. R1 got a blend and F2 did not. At 0.7: 2.1 (B07: 3.0).
Recomputed range across all readings: 16.5 to 18.1. MODEST (12-24) holds in every case.

**G4. Anchor format. MINOR.**
B07 anchors such as AR p.1190, p.2363, p.9666 and p.13238 exceed the AR page count (B01 cites Note 40 at AR p.225). They look like text-file line numbers labelled as pages. G1 anchors FY26 standalone cash to company memory and B00, not to the AR; B01 locates it at AR p.141. Company memory is weighed, never anchored evidence. Several items (export revenue 561 -> 454, Ind-Ra leverage) anchor to B03/B04 derived blocks, not to source documents. Anchor fidelity itself belongs to Verifier A. The format fail is recorded here.

**G5. Section 2C basis mix. MINOR.**
2C labels Rs 5,182.80 Cr as standalone revenue. B01 reports the same figure as consolidated and says it matched the AR consolidated statements. 2C's FAT of 2.85x uses standalone NFA including intangibles. B01's M3 FAT is 2.63x on consolidated net block. At 2.63x: 600 x 2.63 = Rs 1,578 Cr, ~30% above FY26 revenue (B07: 33%). The capex_embedded_growth_pct field feeds later stages, so the basis should be one basis, stated.

**G6. Strength enum. MINOR.**
H2 is graded "Moderate-Strong". The enum is Strong / Moderate / Weak / None. The value is carried into active_categories. Score unaffected.

### Emerging Moat observations (not fails)

- B2 is scored H x H (likelihood High) on CLAIM-only evidence, with no IATF-type certification found and the verifying disclosure stonewalled. The 0.7 multiplier is applied correctly, so this is within the rules. The High likelihood on unverified claims sits uneasily with stage 7 rule 4 ("be skeptical"). At M x H = 3: 2.1, total 16.4, MODEST unchanged.
- A3 and E1 appear in the optionality register and are also scored at 0.7. The register text says "scored 0 or rest only on CLAIM/INFER evidence ... never scored". The two clauses conflict for CLAIM-only scored rows. This is a prompt ambiguity; flag for the operator, not a B07 fault.

## PART 3: VALUATION (B11)

PENDING PHASE 3. Rules 4-7 and 11-15, the expectation ledger checks, and the Business Understanding Narrative check (rule 9) do not run in phase 1.

## RECOMPUTATION SUMMARY

| Item | Maker value | Re-derived on stated readings | Sensitivity range |
|---|---|---|---|
| B01 Core | 63 | 63 | 47 (strict partial window) to 67 (exact ROCE window) |
| B01 moat score / class | 17 / MODERATE (3) | 17 / MODERATE | 16 / MODERATE to 19 / STRONG (4) |
| B01 classification | GOOD | GOOD | AVERAGE to GOOD+ |
| B07 em_score | 17 (17.1) | 17.1 | 16.5 to 18.1 |
| B07 class | MODEST | MODEST | MODEST in every case |
| B07 capex_embedded_growth_pct | 33 | 33 on B07 basis | ~30 on B01 consolidated FAT |

Two operator rulings would settle the Gate 0 range. First, partial-window treatment under rules 5/6. Second, the M5 margin-rank set. Neither is a maker error in arithmetic. Both are unruled readings where B01 picked one without showing the other.

```yaml
stage: B12c
company: "SSWL"
run_date: "2026-09-19"
model: claude-opus-5
status: complete
scope: "PHASE 1 (Gate 0 B01 + Emerging Moat B07 only); valuation audit pending phase 3"
gate0:
  rules_checked: 48
  fails:
    - {rule: "Formula definitions (fixed, no substitution): ROCE = EBIT / (TA - CL)", severity: MAJOR, finding: "FY22-FY24 capital employed proxied as Equity + Borrowings, a substituted formula the rules forbid; A1/A2/A4 mix proxy and exact bases.", recomputed: "Exact-year window FY25-FY26 (same treatment B01 gave B2-B4): A1 median 17.69% = 3; A2 min 16.97% = 5; A3 = 4; A4 -1.43pp = 3; Block A 15 (was 11); Core 67 (was 63); classification GOOD unchanged."}
    - {rule: "Rule 5 N/A treatment and rule 6 3-year minimum, applied to partial-window metrics (B2, B3, B4, E2, M12)", severity: MAJOR, finding: "B2/B3/B4 scored full or mid marks on a 2-year window, E2 on a 1-year window, M12 on 2 years; the rules state no partial-window treatment, and B01 took the favourable reading without showing the other.", recomputed: "Strict reading (N/A scores 0): B2 0, B3 0, B4 0, E2 0, M12 0; Block B 5, Block E 15, Core 47, moat 16; classification AVERAGE. B01 reading: Core 63, GOOD. Core sits 3 points above the 60 boundary; operator ruling needed on partial windows."}
    - {rule: "M5 Scale and Dominance band reading", severity: MAJOR, finding: "B01 ranked margin across all 4 names (SSWL 3rd) and scored 1. The 5-band wording ranks margin among the top-3 mcap set; on that parallel reading SSWL (mcap 2nd, margin 2nd of UNOMINDA/SSWL/WHEELS) meets 'top 3 mcap AND margin top 2'. A strict 'segment' reading on a 3-peer set gives 0, PEER DATA NEEDED.", recomputed: "Parallel reading: M5 3, moats present 4 (M3, M4, M5, M10), STRONG, moat 19, Core 63 + STRONG = GOOD+. Strict segment reading: M5 0, moat 16, MODERATE, GOOD. Range GOOD to GOOD+."}
    - {rule: "WC Days formula: state inventory/payable basis (revenue vs COGS)", severity: MINOR, finding: "Basis not stated for B4/M12 inventory and payable days.", recomputed: "No score change determinable."}
    - {rule: "Rule 5 grounded claims (M6 marked N/A not in provided data)", severity: MINOR, finding: "B07 located total R&D spend at 1.14% (FY25) and 0.40% (FY26) of turnover in the same FY26 AR (AR p.2394-2397 per B07). Data existed.", recomputed: "M6 as written: 0.40% < 1% and margin below peer median = 0. Score unchanged."}
emoat:
  rules_checked: 30
  fails:
    - {rule: "One improvement, one mechanism (CLAUDE.md NEVER; B07 applied it to E2/H1)", severity: MAJOR, finding: "Echanda Urja and Clean Max Astria captive-power investments credited in B1 (Moderate, 2.0) and again cited in H2 (DOC, 3.0) and counted twice in the DOC recount.", recomputed: "H2 on the Arays/Hainan tripartite agreement alone likely holds H x M = 3.0; em_score 17, MODEST unchanged. Recount loses 2 items."}
    - {rule: "Completionist recount accuracy", severity: MINOR, finding: "Recount line claims 15 documented items; the items it lists sum to 13 (B1 2, F1 1, F2 4, H2 3, H3 2, R1 1), 11 distinct after the B1/H2 duplicate.", recomputed: "11 distinct documented items across 6 categories."}
    - {rule: "Evidence multiplier from the defined set (1.0 / 0.7 / 0.5)", severity: MINOR, finding: "R1 uses a blended 0.67 (not a defined tier, not even the 1.0/0.7 midpoint); H1 uses INFER 0.5 as a contradiction discount on evidence that is a management claim; F2 takes DOC 1.0 on a row the report itself types DOC/CLAIM (EBITDA/wheel is a management-reported metric).", recomputed: "Range 16.5 (F2 0.7, R1 0.7, H1 0.7) to 18.1 (R1 1.0); MODEST (12-24) holds under every combination."}
    - {rule: "Stage 7 rule 3 anchors (AR p.__)", severity: MINOR, finding: "Anchors such as AR p.1190, p.2363, p.9666, p.13238 exceed the AR page count (B01 cites Note 40 at p.225) and appear to be text-file line numbers labelled as pages; G1 anchors standalone cash to company memory/B00 rather than the AR (B01 has it at AR p.141); several items anchor to B03/B04 derived blocks rather than source documents.", recomputed: "n/a (anchor fidelity is Verifier A territory; format fail recorded here)."}
    - {rule: "Section 2C arithmetic on one basis", severity: MINOR, finding: "2C labels Rs 5,182.80 Cr as standalone revenue; B01 reports the same figure as consolidated. FAT 2.85x (standalone NFA incl. intangibles) vs B01 M3 FAT 2.63x (consolidated net block).", recomputed: "At 2.63x: 600 x 2.63 = Rs 1,578 Cr, ~30% (vs 33%)."}
    - {rule: "Section 3 strength enum (Strong/Moderate/Weak/None)", severity: MINOR, finding: "H2 graded 'Moderate-Strong', outside the enum, and carried into active_categories.", recomputed: "Moderate or Strong; score unaffected."}
valuation: {rules_checked: 0, fails: [], status: "PENDING PHASE 3 (B10/B11 not in scope)"}
expectation_ledger: {status: "PENDING PHASE 3", present: null, downside_row: null, all_rows_confirm_by: null, all_rows_metric_threshold: null, prob_in_range: null, decay_status_valid: null, off_ledger_credit: null, residual_pct_cmp: null, residual_starter_cap_ok: null, fails: []}
business_understanding_narrative: {status: "PENDING (stage 13 not in scope)", present: null, five_questions_answered: null, prose_only: null, section6_candidates_named: null, valuation_vocab_leak: null, fails: []}
recomputed_destination_pe: ""
recomputed_decision: ""
gate0_classification_sensitivity: "B01 GOOD (Core 63, MODERATE) holds on its own readings, but three rule readings move it: strict partial-window N/A = AVERAGE (Core 47); M5 parallel reading = GOOD+ (STRONG, 4 moats); exact-year ROCE window = GOOD (Core 67). Operator ruling needed on partial-window treatment and the M5 margin-rank set."
emoat_classification_sensitivity: "em_score 17 (17.1) MODEST; recomputed range 16.5 to 18.1 across all multiplier readings; classification robust."
findings:
  - {severity: MAJOR, location: "B01 Block A", rule: "ROCE formula substitution (proxy CE FY22-24)", recomputed: "Block A 15, Core 67, GOOD"}
  - {severity: MAJOR, location: "B01 B2/B3/B4/E2/M12", rule: "partial-window scoring vs rule 5/6", recomputed: "strict: Core 47, AVERAGE"}
  - {severity: MAJOR, location: "B01 M5", rule: "margin-rank set reading", recomputed: "parallel: M5 3, STRONG, GOOD+"}
  - {severity: MAJOR, location: "B07 B1 + H2 + recount", rule: "one improvement one mechanism", recomputed: "em_score 17 unchanged"}
  - {severity: MINOR, location: "B01 B4/M12", rule: "WC basis not stated", recomputed: ""}
  - {severity: MINOR, location: "B01 M6", rule: "R&D data marked N/A but present in AR", recomputed: "M6 0 unchanged"}
  - {severity: MINOR, location: "B07 Section 3 recount", rule: "recount count 15 vs 13 listed / 11 distinct", recomputed: ""}
  - {severity: MINOR, location: "B07 Section 5 R1/H1/F2", rule: "multiplier outside defined set / inconsistent", recomputed: "16.5-18.1, MODEST"}
  - {severity: MINOR, location: "B07 anchors", rule: "page anchors are line numbers; memory/derived-block anchors", recomputed: ""}
  - {severity: MINOR, location: "B07 2C", rule: "standalone/consolidated basis mix", recomputed: "~30% at 2.63x"}
  - {severity: MINOR, location: "B07 H2 strength", rule: "strength enum", recomputed: ""}
critical_count: 0
major_count: 4
minor_count: 7
acceptance_rate: 86   # 67 passed / 78 checked (gate0 43/48, emoat 24/30); phase-1 scope only
```
