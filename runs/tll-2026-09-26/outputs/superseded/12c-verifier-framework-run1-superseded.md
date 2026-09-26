# VERIFIER C: FRAMEWORK ADHERENCE, TLL, run 2026-09-26 (PHASE 1 SCOPE)

Model: claude-opus-5-5. Scope: Gate 0 (B01) and Emerging Moat (B07) only.
The valuation audit (B10, B11, rules 4-7 and 9-15) is pending phase 3. No
valuation framework document was loaded.

Rule sources: prompts/01-gate-0-pipeline.md, prompts/07-emerging-moat-pipeline.md.
Artifacts audited: outputs/reports/01-gate0.md, outputs/blocks/B01-gate0.yaml,
outputs/reports/07-emoat.md, outputs/blocks/B07-emoat.yaml.
Re-derivation data: inputs/screening/screener-Data_Sheet.csv (INR Cr), peer
Data_Sheets (CAPLIPOINT, SENORES, INNOVACAP), inputs/shareholding/
screener-shareholding-pattern.csv, inputs/annual-report/Annual_Report_2026.txt
(INR lakh).

Verifier A owns source fidelity. This audit checks rule application. Where a
number was needed to re-derive a score, it is anchored below.

## Summary

- 0 CRITICAL, 3 MAJOR, 8 MINOR.
- No finding changes the Gate 0 classification (AVERAGE) or the Emerging Moat
  classification (NONE).
- Gate 0 moat_class moves from THIN to MODERATE under a rule-literal re-score.
  M4 alone causes the move.
- B07 Section 2C was computable. Recomputed capex-embedded growth = 28.8% of
  FY26 revenue.
- Acceptance: 52 of 66 rules passed = 78.8% (Gate 0 35/43 = 81.4%; EM 17/23 =
  73.9%).

---

## 1. GATE 0 (B01) COMPLIANCE TABLE

Recompute inputs (screener-Data_Sheet.csv unless noted). EBIT all-in = PBT +
Interest. EBIT op = PBT + Interest - Other Income. Capital employed = TA - CL,
CL from AR as cited in B01 (FY26 CL 8,789.27 lakh, Annual_Report_2026.txt line
9998, confirmed).

| Year | EBIT op | EBIT all-in | CE | ROCE op | ROCE all-in |
|---|---|---|---|---|---|
| FY24 | 8.69+0.65-2.08 = 7.26 | 9.34 | 66.82 | 10.87% | 13.98% |
| FY25 | 13.62+4.14-8.23 = 9.53 | 17.76 | 102.46 | 9.30% | 17.33% |
| FY26 | 27.19+4.12-9.27 = 22.04 | 31.31 | 148.94 | 14.80% | 21.02% |

| # | Rule | B01 value / score | Recomputed | Result |
|---|---|---|---|---|
| G1 | Opening "Data available" line, history adaptation stated | 5 yrs FY22-26; 3-yr sub-window stated per row | same | PASS |
| G2 | Source anchor on every extracted number | present (AR anchors are line-descriptive, not page) | n/a | PASS |
| G3 | ROCE = EBIT / (TA - CL), fixed formula | EBIT excludes Other Income | EBIT = PBT + Interest | FAIL (MAJOR, F1) |
| G4 | A1 median ROCE | 10.87% -> 1 | 17.33% -> 3 | FAIL |
| G5 | A2 minimum ROCE | 9.30% -> 1 | 13.98% -> 3 | FAIL |
| G6 | A3 median ROE | 23.10% -> 5 | FY22 82.6, FY23 23.9, FY24 12.9, FY25 20.0, FY26 23.1; median 23.1 -> 5 | PASS |
| G7 | A4 ROCE trend | 14.80 vs 10.87 -> 5 | 21.02 vs 13.98 -> 5 | PASS |
| G8 | B1 cumulative CFO/PAT | -22.53 / 47.10 = -0.478 -> 0 | same | PASS |
| G9 | FCF = CFO - capex (PPE + intangibles, excl. acquisitions) | proxy CFO + net CFI | AR line exists; FY26 FCF = 4.69 - 36.47 = -31.78 | FAIL (MINOR, F3) |
| G10 | B2 FCF-positive years | 0% -> 0 | CFO < 0 in FY22, FY23, FY25; FY24 and FY26 CFO below PPE purchase; 0 | PASS on score |
| G11 | B3 cumulative FCF/PAT | negative -> 0 | cumulative CFO already negative -> 0 | PASS on score |
| G12 | B4 WC days change | 151.1 -> 202.8, +51.7 -> 0 | FY24 109.9+102.9-61.7 = 151.1; FY26 208.4+103.1-108.7 = 202.8 -> 0 | PASS |
| G13 | C1 revenue CAGR | 56.05% -> 5 | (129.02/21.77)^0.25 - 1 = 56.03% -> 5 | PASS |
| G14 | C2 PAT CAGR | 48.16% -> 5 | 48.17% -> 5 | PASS |
| G15 | C3 positive YoY years | 4/4 -> 5 | 4/4 -> 5 | PASS |
| G16 | C4 PAT CAGR - Rev CAGR | -7.89pp -> 1 | -7.86pp -> 1 | PASS |
| G17 | D1 ND/EBITDA | 68.77/28.11 = 2.45x -> 1 | op EBITDA 28.11 equals sum of screener FY26 quarterly Operating Profit (5.17+6.86+5.09+10.99); screener convention -> 1 | PASS |
| G18 | D2 interest cover | 5.35x -> 4 | all-in 7.60x -> 4 | PASS |
| G19 | D3 D/E | 0.68x -> 3 | 72.99/100.40 = 0.73x -> 3 | PASS |
| G20 | D4 current ratio | 1.59x -> 4 | 13,951.49/8,789.27 = 1.59x -> 4 | PASS |
| G21 | E1 promoter holding | 62.59% -> 5 | Jun-2026 62.59% (shareholding csv) -> 5 | PASS |
| G22 | E2 3-yr change | -7.45pp -> 0 | Sep-2023 70.04% is the earliest column; -7.45 -> 0 | PASS |
| G23 | E3 pledge | NOT FOUND -> 0 | rule 5: N/A scores 0 | PASS |
| G24 | E4 contingent liab / NW | 5.17% -> 3 | 500.00/9,667.56 lakh = 5.17% -> 3 | PASS |
| G25 | One net worth basis across rows | A3 100.40, D3 107.89, E4 96.68 | E4 on A3 basis 4.98% -> 5 | FAIL (MINOR, F4) |
| G26 | M1 pricing power | 12.5% -> 21.8%, +9.3pp -> 5 | 2.72/21.77 = 12.49%; 28.11/129.02 = 21.79% -> 5 | PASS |
| G27 | M2 cost advantage | 21.8 vs median 26.6 -> 0 | CAPLIPOINT 765.03/2,187.19 = 34.98%; SENORES 168.32/632.63 = 26.61%; INNOVACAP 242.92/1,630.02 = 14.90% -> 0 | PASS |
| G28 | M3 capital efficiency | FAT 2.12x, ROCE 14.80% -> 1 | FAT 2.12x, ROCE 21.02% -> 3 | FAIL (root F1) |
| G29 | M4 customer stickiness | 1 (judgment) | tier 3 fits literally -> 3 | FAIL (MAJOR, F2) |
| G30 | M5 scale | 0 PEER DATA NEEDED | peer mcaps in the same sheets; 4th of 4 -> 1 literally | FAIL (MINOR, F5) |
| G31 | M6 R&D | NOT FOUND -> 0 | same | PASS |
| G32 | M7 regulatory | regulated, >10 players -> 1 | same | PASS |
| G33 | M8 distribution | mentioned, unquantified -> 1 | same | PASS |
| G34 | M9 brand (GM proxy) | 46.4 vs median 57.5 -> 0 | CAPLIPOINT 57.51, SENORES 60.23, INNOVACAP 48.58; TLL 46.43 -> 0 | PASS |
| G35 | M10 switching costs | 0 | tier 3 needs "AND stable"; tier 1 needs 2+ decline years; else 0 | PASS |
| G36 | M11 network effects (<6 yrs fallback) | selling % 3.9 -> 6.3 rising -> 1 | 0.84/21.77 = 3.86%; 5.45/86.92 = 6.27% -> 1 | PASS |
| G37 | M12 negative WC | >45 days -> 0 | same | PASS |
| G38 | Moat classification mechanics | 1 present -> THIN | mechanics correct on B01's own scores | PASS |
| G39 | Data confidence adjustment | 5 yrs -> flag, no downgrade | 5-6 band -> flag; no downgrade | PASS |
| G40 | Classification matrix | Core 48 -> AVERAGE | Core 52 -> AVERAGE | PASS |
| G41 | Deal-breakers 1-9 | #2 and #4 triggered, #4 binds | same; #3 not triggered on either basis (10.87% / 17.33%) | PASS |
| G42 | CAGR edge rules | no negative endpoint, no swing | PAT positive all 5 yrs; FY22 PAT > PBT from tax credit is not a swing | PASS |
| G43 | YAML schema, FLAG-GATE0, block_b_trend | present | present | PASS |

Rules checked 43. Passed 35. Acceptance 81.4%.

### Gate 0 findings

**F1 (MAJOR). EBIT basis substituted.** B01 computes EBIT as PBT + Interest -
Other Income (01-gate0.md lines 69-72). The formula block is fixed: "do not
substitute alternatives". Operating rule 2 bars qualitative judgment. EBIT
without qualifier is PBT + Interest. Screener's own ROCE, which the rule
prefers, also includes other income. Rule-literal scores: A1 = 3, A2 = 3,
Block A = 16, M3 = 3 (present). D1 is correct as filed: its op EBITDA equals
screener's Operating Profit convention. D2 does not change (band 4 either way).
The analyst's reasoning has merit: Other Income is 60.4% of FY25 PBT and 34.1%
of FY26 PBT. Carry the operating basis as a disclosed sensitivity, not as the
scored figure. B01's analyst_note asked the verifier to confirm the choice. This
audit does not confirm it.

**F2 (MAJOR). M4 scored by judgment against a literal tier.** M4 tier 3 reads
"max 1 decline year, fully recovered = 3". It has no receivable-days leg. TLL
has zero decline years, so tier 3 applies. B01 states "no literal tier fits"
(01-gate0.md line 225). That is incorrect. M4 = 3, a present moat. M10 differs:
its tier 3 carries "AND stable", so M10 = 0 stands.

**F3 (MINOR). FCF proxy rests on a false input gap.** B01 input_gaps[3] states
the AR cash flow cannot separate PPE purchase from acquisition outflows. The FY26
AR consolidated cash flow shows "Purchase of Fixed Assets" 3,647.24 lakh (FY26)
and 1,109.95 lakh (FY25). "Purchase of Equity Shares" sits on its own line,
794.67 / 565.80 lakh (Annual_Report_2026.txt lines 10383-10390). Defined FCF:
FY26 4.69 - 36.47 = -31.78 Cr; FY25 -10.24 - 11.10 = -21.34 Cr. B2 and B3 stay
0. The false gap propagated into B07 Section 2C (see M1 below).

**F4 (MINOR). Three net worth bases.** A3 uses screener equity 100.40 Cr. That
figure includes 3.73 Cr share application money pending allotment (AR line 9949,
372.67 lakh) inside reserves. D3 adds minority 7.49 Cr to 100.40. E4 uses AR
shareholders' funds 96.68 Cr (1,193.30 + 8,474.26 lakh, AR lines 9933-9938). On
the A3 basis E4 = 4.98%, band <5% = 5. The E4 basis is defensible. The report
must state one basis and use it throughout.

**F5 (MINOR). M5 peer data was in the corpus.** The three peer Data_Sheets used
for M2 and M9 carry Market Capitalization: TLL 487.49, SENORES 6,241.18,
INNOVACAP 7,330.51, CAPLIPOINT 21,550.08 Cr (row 8 of each sheet). On that set
TLL ranks 4th, which literally meets "top 5 mcap = 1". Score 1, or state why
the four-name set is not the segment. M5 is not a present moat either way.

### Gate 0 recomputation (rule-literal)

| Field | B01 | Recomputed |
|---|---|---|
| Blocks A/B/C/D/E | 12/0/16/12/8 | 16/0/16/12/8 |
| Core score | 48 | 52 |
| Moat score | 10 | 14 (M3 3, M4 3) |
| Moats confirmed | 1 | 3 (M1, M3, M4) |
| Moat class | THIN | MODERATE |
| Grand total | 58 | 66 |
| Classification | AVERAGE | AVERAGE (Core 40-59; deal-breaker #4 binds) |

If the operator keeps the operating EBIT basis, only F2 applies: core 48, moat
12, 2 present, MODERATE. The moat class moves under either basis.

---

## 2. EMERGING MOAT (B07) COMPLIANCE TABLE

| # | Rule | B07 | Result |
|---|---|---|---|
| E1 | All 23 rows (22 categories + R1) addressed | 23 rows in Section 3 and Section 5 | PASS |
| E2 | NO EVIDENCE FOUND stated where none | stated per row | PASS |
| E3 | Evidence taxonomy on every item | applied | PASS |
| E4 | Raw likelihood x impact matrix values | LL 1, HL 2, HM 3, ML 1 correct | PASS |
| E5 | Multipliers applied correctly | rounding inconsistent; unrounded 7.3, reported 8 | FAIL (MINOR) |
| E6 | Scores consistent with stated tiers | E1 counted 📄 in recount, scored 🎙️ 0.7x | FAIL (MINOR) |
| E7 | Completionist recount line performed | "📄 recount performed: 4 documented items across 4 categories" | PASS |
| E8 | Section 3 summary table + Strong/Moderate count | present, count 1 | PASS |
| E9 | Category 21 I1 present; >0 only with both legs, (b) with 📄 | 0, neither leg evidenced | PASS |
| E10 | Category 22 I2 present; >0 only with a named sacrifice | 0, "nothing must be destroyed" | PASS |
| E11 | I1/I2 contribution stated separately | 0 of 8 | PASS |
| E12 | Classification band | 8 -> NONE; recomputed 7.3 (8.2 at 📄 E1) -> NONE | PASS |
| E13 | Section 2C arithmetic shown | not run; NOT FOUND | FAIL (MAJOR) |
| E14 | No numeric fill for a missing number | YAML capex_embedded_growth_pct: 0 | FAIL (MINOR) |
| E15 | active_categories only Strong/Moderate | 6 rows incl. Weak | FAIL (MINOR) |
| E16 | Optionality register present, in YAML | present | PASS |
| E17 | Register holds all 0-scored or 🎙️/🔍-only advantages | C1 and A4 absent | FAIL (MINOR) |
| E18 | Section 4 R1 (4A/4B/4C) | present; 0 for no company-specific capture | PASS |
| E19 | 6C uses injected Gate 0 block | core 48, moat 10, THIN, AVERAGE as injected | PASS |
| E20 | 6D in the standard class set | AVERAGE | PASS |
| E21 | F2 cross-reference (NO-CONCALL substitution) | AR-timeline test, stated | PASS |
| E22 | Not conflated with FTTCP | explicit disclaimer | PASS |
| E23 | All six sections present | Sections 1-6 + register | PASS |

Rules checked 23. Passed 17. Acceptance 73.9%.

### Emerging Moat findings

**M1 (MAJOR). Section 2C not computed though its input exists.** The 2C formula
is total capex under execution x historical fixed asset turnover. Consolidated
CWIP is 1,749.91 lakh = 17.50 Cr at FY26 (Annual_Report_2026.txt line 10021;
screener-Data_Sheet.csv CWIP row, 17.5). The AR states TLL Parenterals is in the
CWIP stage (line 14198). FAT FY26 = 129.02 / 60.73 = 2.12x (B01 M3 basis).
Implied incremental revenue = 17.50 x 2.12 = 37.2 Cr = 28.8% above FY26 revenue
of 129.02 Cr. B07 gave two blockers. The first (PPE purchase not separable) is
false per Gate 0 F3 and does not bear on CWIP. The second (FAT distorted by
pre-revenue subsidiaries) is a caveat to print beside the number. It is not a
reason to omit the arithmetic. em_score is unaffected. The figure feeds the stage
11 CAPACITY basis, so its absence matters downstream.

**M2 (MINOR). Multiplier rounding.** A4 1 x 0.5 = 0.5 shown as 1. C1 1 x 0.7 =
0.7 shown as 1. E1 3 x 0.7 = 2.1 shown as 2. Unrounded total 7.3. Band unchanged.

**M3 (MINOR). E1 tier inconsistency.** The recount counts E1 as 📄. Section 5
scores it at 🎙️ 0.7x. The reasoning ("forward value claim dominates") is stated
and conservative. Pick one tier and apply it in both places. At 1.0x the total is
8.2. Band unchanged.

**M4 (MINOR). YAML fill.** capex_embedded_growth_pct is emitted as 0. NOT FOUND
appears only in a YAML comment, which parsers drop. A consumer reads 0% capacity
growth. Emit 28.8 (with the caveat) or the string "NOT FOUND".

**M5 (MINOR). active_categories schema.** The schema says only Strong/Moderate
rows. The block lists six rows. Section 3 states the Strong/Moderate count is 1
(E1).

**M6 (MINOR). Register completeness.** The register covers advantages scored 0
or resting only on 🎙️/🔍 evidence. C1 (🎙️-only cross-sell) and A4 (🔍-only
platform breadth) qualify and are missing.

Confirmed correct: I1 = 0 and I2 = 0. A2 scored None on the deck-versus-AR
conflict (AR Technology Absorption "NIL", R&D "Not applicable"). This is the
conservative document-reading rule applied as written. F2, G1 and G2 are
correctly held at 0 with the counter-evidence recorded.

Cross-stage note: B07 6C carries B01 moat_class THIN. The Gate 0 recompute moves
it to MODERATE. 6D stays AVERAGE.

---

## 3. VALUATION (B10, B11)

Pending phase 3. Rules 4-7 and 9-15 were not run. No valuation framework
document was loaded.

---

```yaml
stage: B12c
company: "TLL"
run_date: "2026-09-26"
model: "claude-opus-5-5"
status: "partial: phase 1 scope (Gate 0 + Emerging Moat only; valuation audit pending phase 3)"
gate0:
  rules_checked: 43
  items_checked: 43
  passed: 35
  fails:
    - "G3 ROCE EBIT definition (EBIT taken as PBT + Interest - Other Income; fixed formula is EBIT, not operating EBIT)"
    - "G4 A1 scored 1; rule-literal all-in median ROCE 17.33% scores 3"
    - "G5 A2 scored 1; rule-literal all-in minimum ROCE 13.98% scores 3"
    - "G9 FCF formula substituted (CFO + net investing CF) although AR carries a separate Purchase of Fixed Assets line"
    - "G25 net worth basis inconsistent across A3 (100.40 Cr), D3 (107.89 Cr), E4 (96.68 Cr)"
    - "G28 M3 scored 1; with all-in ROCE 21.02% and FAT 2.12x scores 3 (present)"
    - "G29 M4 scored 1 by judgment; literal tier 'max 1 decline year, fully recovered' fits zero-decline company, scores 3 (present)"
    - "G30 M5 scored 0 PEER DATA NEEDED although peer market caps were in the same Data_Sheets used for M2/M9"
  findings:
    - {severity: "MAJOR", location: "01-gate0.md Block A lines 69-106; Block F M3 line 220; B01 data_notes[0]", description: "EBIT computed excluding Other Income. Gate 0 formula block is fixed ('do not substitute alternatives') and 'no qualitative judgments'. Rule-literal EBIT = PBT + Interest gives ROCE FY24 13.98%, FY25 17.33%, FY26 21.02%; A1 = 3 (not 1), A2 = 3 (not 1), Block A = 16 (not 12); M3 = 3 (FAT 2.12x > 2 AND ROCE 21.02% > 15), a present moat. D1 and D2 unaffected (D1 op EBITDA 28.11 Cr matches screener quarterly Operating Profit sum; D2 all-in 7.60x same band 4). Operating basis is analytically reasonable given Other Income 34-60% of PBT; carry it as a sensitivity, not the scored figure. Classification unchanged (AVERAGE)."}
    - {severity: "MAJOR", location: "01-gate0.md Block F M4 lines 223-227; B01 data_notes[4]", description: "M4 scored 1 by stated judgment. Rule tier 3 reads 'max 1 decline year, fully recovered = 3' with no receivable-days leg; zero decline years satisfies it literally. Recomputed M4 = 3 (present). With M4 alone corrected, moats confirmed 1 -> 2 and moat_class THIN -> MODERATE; with finding 1 also applied, 3 present, moat total 14, still MODERATE. Classification unchanged. M10 = 0 is correct (its tier 3 carries 'AND stable')."}
    - {severity: "MINOR", location: "01-gate0.md Block B B2/B3 lines 113-121; B01 input_gaps[3]", description: "FCF proxied as CFO + net investing CF on the claim that PPE purchase cannot be separated from acquisition outflows. The FY26 AR consolidated cash flow carries 'Purchase of Fixed Assets' 3,647.24 lakh (FY26) and 1,109.95 lakh (FY25) as a line separate from 'Purchase of Equity Shares' 794.67 / 565.80 lakh (Annual_Report_2026.txt lines 10383-10390). Defined FCF FY26 = 4.69 - 36.47 = -31.78 Cr; FY25 = -10.24 - 11.10 = -21.34 Cr. B2 and B3 stay 0 (CFO negative in 3 of 5 years; cumulative CFO negative). The false input gap propagated into B07 Section 2C."}
    - {severity: "MINOR", location: "01-gate0.md A3 line 99, D3 lines 157-159, E4 lines 182-189", description: "Three net worth bases in one scorecard. A3 uses screener equity 100.40 Cr (includes 3.73 Cr share application money pending allotment in reserves), D3 adds minority 7.49 Cr on top of 100.40, E4 uses AR shareholders funds 96.68 Cr (1,193.30 + 8,474.26 lakh, Annual_Report_2026.txt lines 9931-9939). E4 on the A3 basis = 5.00/100.40 = 4.98%, band <5% = 5 (not 3). The E4 choice is defensible; the inconsistency is not stated. Classification unchanged (Core max 50)."}
    - {severity: "MINOR", location: "01-gate0.md Block F M5 line 228", description: "M5 marked PEER DATA NEEDED while the same three peer Data_Sheets (used for M2 and M9) carry Market Capitalization (TLL 487.49, SENORES 6,241.18, INNOVACAP 7,330.51, CAPLIPOINT 21,550.08 Cr). On a four name set TLL ranks 4th, which literally meets 'top 5 mcap = 1'; either score 1 or state why the four name set is not the segment. Not a present moat either way."}
  recomputed:
    blocks: {A: 16, B: 0, C: 16, D: 12, E: 8}
    core_score: 52
    moat_score: 14
    moats_confirmed: 3
    moat_class: "MODERATE"
    grand_total: 66
    classification: "AVERAGE"
    note: "Rule-literal recompute (all-in EBIT, M4 = 3). Classification unchanged: Core 40-59 band and deal-breaker #4 (cumulative CFO/PAT -0.478) both give AVERAGE. moat_class moves THIN -> MODERATE under either EBIT basis because of M4."
  acceptance_rate: 81.4
emoat:
  rules_checked: 23
  items_checked: 23
  passed: 17
  fails:
    - "E5 multiplier rounding inconsistent (A4 0.5 -> 1, C1 0.7 -> 1 rounded up; E1 2.1 -> 2 rounded down); unrounded total 7.3, reported 8"
    - "E6 E1 evidence tier inconsistent (counted as documented in the recount, scored at claim 0.7x)"
    - "E13 Section 2C arithmetic not run although CWIP 17.50 Cr (1,749.91 lakh) is on the balance sheet"
    - "E14 YAML capex_embedded_growth_pct emitted as 0 instead of NOT FOUND"
    - "E15 active_categories lists Weak rows; schema says only Strong/Moderate rows"
    - "E17 optionality register omits C1 (claim-only) and A4 (inference-only)"
  findings:
    - {severity: "MAJOR", location: "07-emoat.md Section 2C lines 87-97; B07 capex_embedded_growth_pct", description: "2C formula is total capex under execution x historical fixed asset turnover. Consolidated CWIP 1,749.91 lakh = 17.50 Cr FY26 (Annual_Report_2026.txt line 10021; screener-Data_Sheet.csv CWIP row 17.5), mostly the TLL Parenterals plant (AR line 14198). FAT FY26 = 129.02 / 60.73 = 2.12x (B01 M3). Implied incremental revenue = 17.50 x 2.12 = 37.2 Cr = 28.8% above FY26 revenue 129.02 Cr. The stated blocker (Purchase of Fixed Assets not separable) is false (see gate0 finding 3) and irrelevant to CWIP. The distortion caveat on FAT may be shown beside the number; it does not justify omitting the arithmetic. em_score and classification unaffected; feeds the stage 11 CAPACITY basis."}
    - {severity: "MINOR", location: "07-emoat.md Section 5 lines 321-346", description: "Multiplier products rounded inconsistently: A4 LL 1 x 0.5 = 0.5 shown 1; C1 LL 1 x 0.7 = 0.7 shown 1; E1 HM 3 x 0.7 = 2.1 shown 2. Unrounded adjusted total 7.3, not 8. Band unchanged (<12, NONE)."}
    - {severity: "MINOR", location: "07-emoat.md Section 3 E1 lines 176-184, recount line 281, Section 5 line 334", description: "E1 listed as a documented item in the completionist recount but scored at the claim multiplier 0.7x. The choice is conservative and reasoned, but tier use must be one or the other. At 1.0x E1 = 3 and total = 8.2; band unchanged."}
    - {severity: "MINOR", location: "B07-emoat.yaml capex_embedded_growth_pct", description: "Numeric 0 emitted for a figure the report marks NOT FOUND; the NOT FOUND sits only in a YAML comment, which parsers drop. Downstream reads 0% capacity growth. Emit the recomputed value or the string NOT FOUND."}
    - {severity: "MINOR", location: "B07-emoat.yaml active_categories", description: "Schema says only Strong/Moderate rows; block lists six rows including four Weak/Weak-Moderate. Report Section 3 states Strong/Moderate count = 1 (E1). A consumer counting active_categories reads 6."}
    - {severity: "MINOR", location: "07-emoat.md Optionality Register lines 364-375", description: "Register holds forward advantages scored 0 or resting only on claim/inference evidence. C1 (claim-only cross-sell) and A4 (inference-only platform breadth) meet that test and are absent."}
  recomputed:
    em_score: 7.3
    em_score_if_E1_documented: 8.2
    em_classification: "NONE"
    capex_embedded_growth_pct: 28.8
    note: "Classification unchanged. I1 = 0 and I2 = 0 confirmed correct (both legs absent; honest answer 'nothing must be destroyed'). 6C carries B01 moat_class THIN; gate0 recompute moves it to MODERATE, which does not change 6D AVERAGE."
  acceptance_rate: 73.9
valuation: "pending phase 3"
expectation_ledger: "pending phase 3"
business_understanding_narrative: "pending phase 3 (stage 13)"
recomputed_destination_pe: "pending phase 3"
recomputed_decision: ""
critical_count: 0
major_count: 3
minor_count: 8
acceptance_rate: 78.8
acceptance_basis: "52 of 66 phase-1 rules passed (gate0 35/43, emoat 17/23); no CRITICAL; no decision or classification change"
```
