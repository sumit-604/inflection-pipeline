# STAGE 12, VERIFIER C: FRAMEWORK ADHERENCE, PHASE 1 SCOPE

Company: eMudhra Ltd (EMUDHRA). Run date: 2026-09-19. Model: claude-opus-5.
Scope: Gate 0 (B01) and Emerging Moat (B07) only. The valuation audit
(B10, B11, rules 4, 7, 11 to 15) is deferred to phase 3. Rules 6, 9 and 10
depend on B09, stage 13 and the 09b dossier. They are out of scope here.

Rule sources: prompts/01-gate-0-pipeline.md, prompts/07-emerging-moat-pipeline.md.
Artifacts audited: outputs/reports/01-gate0.md, outputs/blocks/B01-gate0.yaml,
outputs/reports/07-emoat.md, outputs/blocks/B07-emoat.yaml. Both artifacts
carry earlier correction passes. This audit re-derives every score fresh
from the source data and the rule text. It does not rely on the stated
corrections.

Re-derivation sources: inputs/screening/screener-Data_Sheet.csv (INR Cr)
and inputs/annual-report/Annual_Report_2026.mupdf.txt (INR Mn).

---

## PART 1: GATE 0 (B01) COMPLIANCE TABLE

### Re-derivation summary

| Item | Stage value | Recomputed | Source |
| --- | --- | --- | --- |
| EBIT FY19 / FY26 (PBT + Interest) | 21.91 / 136.38 Cr | 21.91 / 136.38 Cr | screener rows 21-22 |
| ROCE series (Equity + Reserves + Borrowings basis) | 20.99, 17.69, 20.18, 25.02, 18.41, 14.41, 14.56, 14.51% | same | screener rows 39-41 |
| ROCE FY26 on the prompt formula EBIT / (TA - CL) | not computed | 136.38 / (12,134.33 - 1,578.00 Mn = 1,055.63 Cr) = 12.92% | AR p.216 (mupdf lines 10431, 10463) |
| ROCE FY25 on the prompt formula | not computed | 108.55 / (8,681.35 - 973.61 Mn = 770.77 Cr) = 14.08% | AR p.216 (mupdf lines 10431, 10463) |
| Median ROE | 18.675% | 18.675% (17.50, 19.85 middle pair) | screener rows 24, 39-40 |
| Cumulative CFO / PAT | 443.14 / 422.12 = 1.05x | 1.05x | screener rows 24, 57 |
| Revenue CAGR FY19-26 | 31.8% | (701.58 / 101.58)^(1/7) - 1 = 31.8% | screener row 11 |
| PAT CAGR FY19-26 | 29.7% | (107.79 / 17.44)^(1/7) - 1 = 29.7% | screener row 24 |
| EBITDA FY19 / FY26 | 32.21 / 159.12 Cr | 32.21 / 159.12 Cr (ties to PBT 21.65 / 131.31) | screener rows 11-22 |
| Net debt FY26 | 28.78 - 65.20 = net cash | net cash | screener rows 41, 51 |
| Trade payables FY26 / FY25 | 600.92 / 314.34 Mn | present | AR p.216 / Note 18 (mupdf line 12682) |
| WC days FY25 / FY26 | 81.12 / 69.21 | 81.12 / 69.21 | AR p.216, Note 18 |
| M11 3-year CAGR, latest / prior | 41.3% / 28.8% | 41.3% / 28.8% | screener row 11 |

### Rule-by-rule table

| # | Rule (prompts/01) | Stage application | Verdict | Recomputed value if FAIL |
| --- | --- | --- | --- | --- |
| G1 | Opening line states data years and adaptation | "Data available: 8 years (FY19 to FY26)" | PASS | |
| G2 | ROCE = EBIT / (Total Assets - Current Liabilities); fixed, no substitute | Capital employed = Equity + Reserves + Borrowings. This treats all Other Liabilities as current. The report discloses the substitution. | FAIL (MINOR) | FY26 12.92%, FY25 14.08% on the prompt formula. A1 stays 3 (median 18.05%), A2 stays 3 (min 12.92%, band 12-14.9), A4 stays 0 (decline >5pp on any FY19 value between 18.33% and 20.99%). Score-neutral. |
| G3 | Source ROCE used when the data source provides it | Screener ROCE absent (B00). Computed and stated "computed". AR p.57 figures kept as cross-check. | PASS | |
| G4 | A1 median ROCE bands | 18.05% -> 3 | PASS | |
| G5 | A2 minimum ROCE bands | 14.41% (FY24) -> 3, one basis | PASS | |
| G6 | A3 median ROE bands, opening-worth rule | 18.675% -> 4; FY19 closing-only stated | PASS | |
| G7 | A4 trend bands | -6.48pp -> 0 | PASS | |
| G8 | B1 cumulative CFO / PAT bands | 1.05x -> 5 | PASS | |
| G9 | B2 FCF-positive years proportion | 1 of 2 available years -> 50% -> 2. Capex exists only for FY25-26 (AR p.218). The proportion over available years is a defensible reading of operating rule 6 ("use whatever history is available"). | PASS (with observation) | |
| G10 | B3 cumulative FCF / PAT bands | -17.7% -> 0 | PASS | Score is 0 on every reading. |
| G11 | B4 WC days change, "latest vs earliest" | Earliest taken as FY25. Change -11.91 days -> 5. | FAIL (MAJOR) | See finding F1. Earliest year of the scored history is FY19 (the stage itself uses FY19 as "earliest" in A4). FY19 trade payables are not in the provided data. Operating rule 5: "If a data point is not available, mark it N/A and score it 0." Recomputed B4 = 0. Block B = 5 + 2 + 0 + 0 = 7. Core = 69. Deal-breaker 1B/#2 (Block B < 8) triggers. Classification = GOOD. |
| G12 | C1 revenue CAGR bands | 31.8% -> 5 | PASS | |
| G13 | C2 PAT CAGR bands | 29.7% -> 5 | PASS | |
| G14 | C3 positive YoY years | 7 of 7 -> 5 | PASS | |
| G15 | C4 PAT CAGR minus revenue CAGR | -2.1pp -> 3 | PASS | |
| G16 | CAGR edge rules (negative endpoint, loss-to-profit swing, C4 on N/M) | No negative endpoint; PAT positive every year; noted in data_notes | PASS | |
| G17 | D1 net debt / EBITDA | Net cash -> 5 (FY26 cash column corrected to 65.20) | PASS | |
| G18 | D2 interest cover | 26.9x -> 5 | PASS | |
| G19 | D3 debt / equity | 0.032x -> 5 | PASS | |
| G20 | D4 current ratio | 2.76x consolidated -> 5 | PASS | |
| G21 | E1 promoter holding | 54.40% -> 4 | PASS | |
| G22 | E2 3-year promoter change | N/A, score 0 per rule 5 | PASS | |
| G23 | E3 pledge | 0% -> 5 | PASS | |
| G24 | E4 contingent liabilities / net worth | 0.38% -> 5, 3i Infotech claim flagged | PASS | |
| G25 | M1 pricing power | Margin -9.04pp -> 0 | PASS | |
| G26 | M2 cost advantage vs peer median | +11.10pp -> 5 | PASS | Peer figures not re-derived here (peer files not in scope). |
| G27 | M3 capital efficiency | FAT 0.97x -> 0 | PASS | |
| G28 | M4 customer stickiness | 0 decline years; receivable days +21.7 fails top tier -> 3 | PASS | |
| G29 | M5 scale and dominance | 2nd mcap, 2nd margin of 4 -> 3, caveat stated | PASS | |
| G30 | M6 technology / R&D | Scored 0 on "not consistently disclosed". | FAIL (MINOR) | See finding F2. The word "consistently" sits in the 5-point tier only. The 3-point and 1-point tiers carry no consistency condition. FY26 capitalised product development Rs 601.00 Mn (124.62 + 476.38, AR p.156) = 8.57% of revenue. With EBITDA 22.68% and revenue CAGR 31.8%, the 3-point tier text is met on one year. Possible M6 = 3. F = 20, grand total 94, moats 5, class still STRONG. Classification unchanged. The report also labels the 8.6% as "Rs 814.21 Mn"; 814.21 includes Rs 213.21 Mn data centre spend and equals 11.6% of revenue (numeric point for Verifier A). |
| G31 | M7 regulatory / licence | PEER DATA NEEDED -> 0 | PASS | Margin (-9pp) fails the stability legs of the 5 and 3 tiers on any count, so the maximum reachable is 1. |
| G32 | M8 distribution | One-year quantified mix, no growth metric -> 1 | PASS | |
| G33 | M9 brand | Peer GM proxy distorted, PEER DATA NEEDED -> 0 | PASS | |
| G34 | M10 switching costs | Receivable days +21.7 fails 5 and 3 tiers; no decline years for the 1 tier -> 0 | PASS | |
| G35 | M11 network effects, 6-year two-window test | 41.3% > 28.8%, selling % 12.77 -> 8.86 -> 5 | PASS | |
| G36 | M12 negative WC / float | 81.12d, 69.21d, both >45 -> 0 | PASS | |
| G37 | Moat count and class | 4 present (M2, M4, M5, M11) -> STRONG | PASS | |
| G38 | Data confidence tier | 8 years -> moderate, no downgrade | PASS | |
| G39 | Classification matrix on stated inputs | Core 74, STRONG -> GOOD+ | PASS (mechanical) | Recomputed classification follows F1: GOOD. |
| G40 | Deal-breaker table, driving years stated | All nine listed, both readings shown | PASS (mechanical) | Under F1, #2 triggers. |
| G41 | Source anchors on every extracted number | Present throughout | PASS | |
| G42 | YAML schema | block_b_trend must be "improving / stable / deteriorating, with the one number". Filed as "mixed, two numbers". | FAIL (MINOR) | Enum value not used. Downstream FLAG-CASH logic reads this field. Suggest "deteriorating (FCF +18.41 Cr FY25 to -52.52 Cr FY26)" with WC improvement kept in analyst_note. |

Gate 0: 42 rules checked, 4 FAIL (1 MAJOR, 3 MINOR).

### Finding F1 (MAJOR): B4 scored on a shortened window against rule 5

The stage files B4 = 5 on a FY25 to FY26 change. Three rule texts read
against this:

1. B4 says "latest vs earliest". The scored history is FY19 to FY26. The
   stage reads "earliest" as FY19 for A4 in the same scorecard. For B4 it
   reads "earliest" as FY25. One word carries two meanings in one
   scorecard.
2. Operating rule 5: "If a data point is not available, mark it 'N/A (not
   in provided data)' and score it 0." FY19 trade payables are not in the
   provided data.
3. Operating rule 6 sets a 3-year minimum history. The stage names the
   prompt "silent". It is silent at the sub-metric level, but rules 5 and
   6 are the nearest text, and both point to N/A.

B2 differs. B2 is a proportion over years, and "use whatever history is
available" (rule 6) supports scoring the available years. B2 and B3 are
therefore not failed here.

Effect: B4 = 0 gives Block B = 7. Core = 69. Deal-breaker #2 (Block B
< 8) caps at GOOD. Classification moves from GOOD+ to GOOD. The combined
label in B07 6D moves from GOOD+ to GOOD with it.

Why MAJOR, not CRITICAL: the stage does not hide the issue. It carries
the alternative reading (GOOD) in the block as FLAG-OPERATOR-RULING and in
classification_alternative. The flag reaches the operator. But the FILED
value should be the rule-faithful one. Recommendation: file GOOD as the
primary classification and carry GOOD+ as the reading that needs an
operator ruling, not the reverse. The ruling itself stays with the
operator.

Note on the stage's own alternative table: it zeroes B2 as well
(Block B = 5). The rule-faithful reading here zeroes B4 only (Block B = 7).
Both trigger deal-breaker #2. Both give GOOD.

### Finding F2 (MINOR): M6 tier reading

See G30. The stage applied the 5-point tier's "consistently" test to all
tiers. On the text, the 3-point tier can score on the one disclosed year.
The data is thin (one year, capitalised spend, not expensed R&D). A score
of 0 or 3 is defensible, but the reason given ("consistently") is not the
rule for the lower tiers. No classification effect.

### Finding F3 (MINOR): ROCE formula substitution

See G2. The prompt fixes ROCE = EBIT / (TA - CL). The stage used
Equity + Reserves + Borrowings for all 8 years, disclosed as a
substitution. The AR gives consolidated TA and CL for FY25 and FY26. On
the prompt formula FY26 ROCE is 12.92%, not 14.51%. The FY26 gap comes
mainly from Rs 881.45 Mn non-current contingent consideration and
Rs 173.54 Mn other non-current liabilities (AR p.216, mupdf lines
10445-10448). These count in capital employed on the prompt formula and
drop out on the substitute. All four Block A scores hold on either basis.
Record the prompt-formula values beside the substitute so the downstream
ROCE reads do not inherit the higher figure.

### Finding F4 (MINOR): block_b_trend enum

See G42.

---

## PART 2: EMERGING MOAT (B07) COMPLIANCE TABLE

### Re-derivation of the scorecard

| Row | L x I | Raw | Tier | Mult | Adjusted | Rule check |
| --- | --- | --- | --- | --- | --- | --- |
| A4 | MH | 3 | 📄 | 1.0 | 3.0 | OK |
| B2 | MM | 2 | 📄 | 1.0 | 2.0 | OK |
| C1 | MH | 3 | 🎙️ (dominant) | 0.7 | 2.1 | OK; 0.7 is the conservative tier for a mixed row |
| C2 | HL | 2 | 📄 | 1.0 | 2.0 | See F6 |
| E1 | MH | 3 | 📄 | 1.0 | 3.0 | OK |
| H1 | MH | 3 | 📄 | 1.0 | 3.0 | OK |
| H2 | HM | 3 | 📄 | 1.0 | 3.0 | Label: see F7 |
| R1 | HH | 4 | 📄 | 1.0 | 4.0 | OK |
| 15 other rows | none | 0 | none | none | 0 | OK |
| Total | | | | | 22.1 | Matches stage |

22.1 falls in 12-24 -> MODEST MOAT DEVELOPMENT. Matches stage.
📄 recount: 4 + 1 + 1 + 1 + 3 + 2 + 3 + 4 = 19. Matches the stated line.

### Rule-by-rule table

| # | Rule (prompts/07, verifier rules 3 and 8) | Stage application | Verdict | Recomputed value if FAIL |
| --- | --- | --- | --- | --- |
| M-1 | All six sections in one response | Sections 1-6 present | PASS | |
| M-2 | All 23 rows addressed or explicit NO EVIDENCE | 22 categories + R1, each with evidence or "NO EVIDENCE FOUND" / "WEAK" call | PASS | |
| M-3 | Evidence taxonomy on every evidence item | Tier marks on all items | PASS | |
| M-4 | Source anchors on evidence items | Present. One incomplete anchor ("p. of applicable-laws list", A2) sits on a no-evidence row. | PASS | |
| M-5 | No force-fit; NO EVIDENCE FOUND where absent | A1, A2, A3, B1, B3, E2, G1, G2, H3 called; D1, D2, F1, F2 reasoned to 0 | PASS | |
| M-6 | L x I matrix values correct per row | HH=4, HM/MH=3, MM/HL=2 applied correctly | PASS | |
| M-7 | Evidence multipliers correct | 📄 1.0, 🎙️ 0.7 applied correctly | PASS | |
| M-8 | Adjusted total arithmetic | 22.1 | PASS | |
| M-9 | Classification band (absolute, no rescale) | 12-24 -> MODEST | PASS | |
| M-10 | Completionist guard: recount line stated | "📄 recount performed: 19 documented items across 8 categories" | PASS | 8 active rows, below the 12-row trigger. |
| M-11 | evidence_mix item counts reconcile to the report | documented 19 reconciles. claim 10 and inference 6 have no itemised tally in the report. | FAIL (MINOR) | See F5. |
| M-12 | Scores consistent with evidence tiers (verifier rule 3) | C2 scored at 📄 1.0x while the report states the category test (top-5/10 share declining) "cannot be confirmed" | FAIL (MINOR) | See F6. C2 at 🔍 0.5x = 1.0. em_score 21.1. Band unchanged (MODEST). |
| M-13 | Strength labels consistent with scores | H2 labelled Strong at raw 3 (HM). A4, E1, H1 labelled Moderate at the same raw 3. | FAIL (MINOR) | See F7. H2 should read Moderate, or its L x I should be HH. Score unchanged. |
| M-14 | Category 21 (I1) present; >0 only with both legs and a 📄 (b) leg (verifier rule 8) | Present, 0; leg (b) NOT FOUND | PASS | |
| M-15 | Category 22 (I2) present; >0 only with a specific named sacrifice (verifier rule 8) | Present, 0; sacrifice named for retail DSC but no 📄 support; others execution lead | PASS | |
| M-16 | I1/I2 contribution stated separately | 0.0, checkpoint list unaffected | PASS | |
| M-17 | One improvement, one mechanism | Allocation note present; B2/R1 split stated; Cryptas split between H1 (acquisition) and C1 (cross-sell outcome) | PASS | C1's 🎙️ weight comes from the Cryptas wins. H1 credits the Cryptas purchase. Distinct mechanisms, but watch for a third credit downstream. |
| M-18 | Section 2C arithmetic shown | 291.76 Mn x 0.97x = 283.1 Mn = 4.0%; three readings shown | PASS | The text says screener Net Block "includes CWIP". Screener lists CWIP separately (row 45, 29.18 Cr). The number is right; the description is wrong. Cosmetic. |
| M-19 | Section 4 (R1) 4A / 4B / 4C | Present; score/narrative contradiction resolved | PASS | |
| M-20 | Optionality register in report and block | 11 rows, four columns, carried in YAML | PASS | |
| M-21 | 6C uses the injected Gate 0 block | Uses B01 filed and alternative readings | PASS | Combined label inherits F1: GOOD on the rule-faithful B01 reading. |
| M-22 | 6D combined classification per the standard matrix | Matrix not present in prompts/07 or the rule sources. Stage derives from the stated transition logic and records an input_gap. | PASS (prompt gap) | Prompt defect, not a stage defect. The 8-label matrix needs a written table in prompts/07. |
| M-23 | YAML schema | All required fields present; extra fields are additive | PASS | |
| M-24 | NOT FOUND is the only fill | Section 1C estimate removed, marked NOT FOUND | PASS | |

Emerging Moat: 24 rules checked, 3 FAIL (all MINOR).

### Finding F5 (MINOR): evidence_mix claim and inference counts unreconciled

The block states claim 10, inference 6. The report itemises only the 19
documented items. A reader cannot rebuild the 10 and the 6. List them, or
state the count rule.

### Finding F6 (MINOR): C2 credited at documented tier on an input, not the test

The C2 test is "top 5/10 share declining". The report says this "cannot
be confirmed, only the customer-addition input to it". The 240 new
customers (MD&A p.151) are 📄, but the step from additions to declining
concentration is inference. Tier the row 🔍: 2 x 0.5 = 1.0. em_score
22.1 -> 21.1. Band MODEST unchanged. EM stays below the >=25 UA
qualifier either way.

### Finding F7 (MINOR): H2 strength label

H2 carries "Strong" at HM = 3, the same raw score as four "Moderate" rows.
The block's active_categories carries the same label. Downstream Pillar 3
inputs read strength labels. Align the label to the score.

---

## PART 3: VALUATION (B10, B11)

PENDING. Deferred to phase 3. B10 and B11 do not exist for this run.
Rules 4, 7, 11, 12, 13, 14 and 15 not checked. Rules 6 (B09 downstream
candidates), 9 (stage 13 narrative) and 10 (09b dossier) out of phase-1
scope.

---

## SUMMARY

| Framework | Rules checked | PASS | FAIL | Critical | Major | Minor |
| --- | --- | --- | --- | --- | --- | --- |
| Gate 0 (B01) | 42 | 38 | 4 | 0 | 1 | 3 |
| Emerging Moat (B07) | 24 | 21 | 3 | 0 | 0 | 3 |
| Valuation (B11) | pending | | | | | |
| Total | 66 | 59 | 7 | 0 | 1 | 6 |

Acceptance rate: 59 / 66 = 89.4%. Denominator is 4 or more, so the rate
applies. It is above 60%. No REWORK trigger from this verifier.

Recomputed classification: Gate 0 GOOD (filed GOOD+). Emerging Moat
21.1, MODEST (filed 22.1, MODEST). Combined label GOOD (filed GOOD+).
The Gate 0 change rests on F1 and routes to the operator ruling the stage
already raised.

```yaml
stage: B12c
company: "EMUDHRA"
run_date: "2026-09-19"
model: "claude-opus-5"
status: complete
scope: "phase 1 (Gate 0 + Emerging Moat); valuation deferred to phase 3"
gate0:
  rules_checked: 42
  fails:
    - {rule: "B4 WC days change, latest vs earliest (+ operating rules 5, 6)", severity: MAJOR, filed: "B4=5 on FY25->FY26 (-11.91d); Block B 12; core 74; GOOD+", recomputed: "earliest = FY19 (as in A4); FY19 trade payables not in provided data -> N/A, 0; Block B 7; core 69; deal-breaker #2 triggers; GOOD", note: "stage already carries FLAG-OPERATOR-RULING and classification_alternative; file GOOD as primary, GOOD+ as the reading pending ruling"}
    - {rule: "ROCE formula fixed as EBIT/(TA-CL)", severity: MINOR, filed: "Equity+Reserves+Borrowings basis, FY26 14.51%", recomputed: "FY26 12.92% (1,055.63 Cr CE), FY25 14.08% (AR p.216); A1 3, A2 3, A4 0 unchanged"}
    - {rule: "M6 tier bands", severity: MINOR, filed: "0, 'not consistent'", recomputed: "'consistently' binds the 5-point tier only; FY26 product development 601.00 Mn = 8.57% of revenue meets the 3-point tier text; M6 0 or 3; if 3, F 20, grand 94, moats 5, still STRONG; 814.21 Mn label on the 8.6% is wrong (814.21 = 11.6%)"}
    - {rule: "YAML block_b_trend enum", severity: MINOR, filed: "mixed, two numbers", recomputed: "use improving | stable | deteriorating with one number"}
emoat:
  rules_checked: 24
  fails:
    - {rule: "evidence_mix reconciles to report", severity: MINOR, filed: "claim 10, inference 6", recomputed: "not itemised in report; unverifiable"}
    - {rule: "scores consistent with evidence tiers", severity: MINOR, filed: "C2 HL=2 at documented 1.0x = 2.0", recomputed: "category test unconfirmed; inference tier 0.5x = 1.0; em_score 21.1; band MODEST unchanged"}
    - {rule: "strength label consistent with score", severity: MINOR, filed: "H2 Strong at HM=3", recomputed: "Moderate (same raw as A4, E1, H1)"}
valuation: {rules_checked: 0, fails: [], status: "PENDING - phase 3; B10/B11 not present"}
expectation_ledger: {present: false, downside_row: false, all_rows_confirm_by: false, all_rows_metric_threshold: false, prob_in_range: false, decay_status_valid: false, off_ledger_credit: false, residual_pct_cmp: 0, residual_starter_cap_ok: true, fails: [], status: "PENDING - phase 3"}
business_understanding_narrative: {present: false, five_questions_answered: false, prose_only: false, section6_candidates_named: 0, valuation_vocab_leak: false, fails: [], status: "OUT OF SCOPE - stage 13 not in phase 1"}
recomputed_destination_pe: ""
recomputed_decision: ""
recomputed_gate0_classification: "GOOD (filed GOOD+); rests on B4 N/A per operator rule 5; routes to the operator ruling B01 already raised"
recomputed_em_score: "21.1 MODEST (filed 22.1 MODEST); band unchanged"
recomputed_combined_assessment: "GOOD (filed GOOD+), follows the Gate 0 recompute"
findings:
  - {id: F1, stage: B01, severity: MAJOR, summary: "B4 scored on FY25 as 'earliest' while A4 uses FY19; rule 5 requires N/A and 0 for the missing FY19 payables; Block B 7, deal-breaker #2, GOOD not GOOD+"}
  - {id: F2, stage: B01, severity: MINOR, summary: "M6 scored 0 on a 'consistently' test that binds only the 5-point tier; possible 3; no classification effect"}
  - {id: F3, stage: B01, severity: MINOR, summary: "ROCE computed on a substitute basis; prompt formula gives FY26 12.92%, FY25 14.08%; Block A scores unchanged"}
  - {id: F4, stage: B01, severity: MINOR, summary: "block_b_trend not in the schema enum"}
  - {id: F5, stage: B07, severity: MINOR, summary: "evidence_mix claim/inference counts not itemised"}
  - {id: F6, stage: B07, severity: MINOR, summary: "C2 credited at documented tier on customer additions while the concentration test is unconfirmed; 1.0 not 2.0; em_score 21.1"}
  - {id: F7, stage: B07, severity: MINOR, summary: "H2 labelled Strong at raw 3"}
  - {id: O1, stage: prompts/07, severity: OBSERVATION, summary: "Section 6D names an 8-label combined matrix that no rule source defines; prompt defect, not a stage fail"}
critical_count: 0
major_count: 1
minor_count: 6
acceptance_rate: 89.4
```
