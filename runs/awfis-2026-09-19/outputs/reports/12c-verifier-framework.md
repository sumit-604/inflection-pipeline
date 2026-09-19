# STAGE 12 VERIFIER C: FRAMEWORK ADHERENCE, AWFIS (PHASE 1 SCOPE)
Run date: 2026-09-19 | Model: claude-opus-5 | Emits: B12c

Scope: Gate 0 (B01) and Emerging Moat (B07) only. The valuation audit
(B10/B11, rules 4-7 and 11-15) is PENDING PHASE 3. Rules 9 and 10
(Business Understanding Narrative, Halt 1 dossier) fire at stage 13 and
/finalize, so they are also pending.

Rule sources: prompts/01-gate-0-pipeline.md, prompts/07-emerging-moat-pipeline.md.
Artifacts audited: outputs/reports/01-gate0.md + outputs/blocks/B01-gate0.yaml;
outputs/reports/07-emoat.md + outputs/blocks/B07-emoat.yaml.
Re-derivation data: inputs/screening/screener-Data_Sheet.csv (AWFIS),
SMARTWORKS-, INDIQUBE-, DEVX-Data_Sheet.csv. One source check on E4:
inputs/annual-report/AR-FY26-with-AGM-notice.txt, Note 33(i) (text line 16419-16427).

This audit judges rule application only. Verifier A owns whether each
number exists in its source.

---

## PART 1: GATE 0 (B01) COMPLIANCE TABLE

Every block score was re-derived from the Data_Sheet rows (CSV row numbers
below) and from the Prospectus/AR inputs B01 states, using the stated
thresholds.

| # | Rule | B01 value | Recomputed | Result | Note |
|---|------|-----------|------------|--------|------|
| 1 | Opening data-window statement | 8 yrs FY19-FY26, adapted | same | PASS | |
| 2 | ROCE source rule (use source ROCE, else compute and say so) | computed | computed | PASS | Data_Sheet carries no ROCE line |
| 3 | A1 median ROCE | 4.01% -> 0 | {-2.43, 0.98, 4.01, 11.51, 13.47} median 4.01% -> 0 | PASS | EBIT = PBT + Interest (CSV rows 21-22) checked for all 5 years |
| 4 | A2 min ROCE | -2.43% -> 0 | -2.43% -> 0 | PASS | |
| 5 | A3 median ROE | 14.01% (FY26 only) -> 2 | 25.58% -> 5 | **FAIL** | See G-1 |
| 6 | A4 ROCE trend | 13.47 vs 0.98 -> 5 | 5 | PASS | |
| 7 | B1 cum CFO / cum PAT | negative -> 0 | 1,523.81 / -155.74, negative -> 0 | PASS | CSV rows 57, 24 |
| 8 | B2 FCF-positive year share | 5/5 = 100% -> 5 | 5/7 = 71.4% -> 2 | **FAIL** | See G-2 |
| 9 | B3 cum FCF / cum PAT | negative -> 0 | 0 | PASS | Unchanged even with FY19/FY20 negative FCF added |
| 10 | B4 WC-days change | -16.46 d -> 5 | FY21 -24.9, FY26 -41.4 -> 5 | PASS | Earliest year = first year with payables data |
| 11 | C1 revenue CAGR | 38.3% -> 5 | (1,493.48/154.05)^(1/7)-1 = 38.3% -> 5 | PASS | |
| 12 | C2 PAT CAGR | N/M -> 0 | negative endpoint FY19 -> 0 | PASS | CAGR edge rule honoured |
| 13 | C3 positive YoY years | 6/7 -> 3 | 85.7% -> 3 | PASS | |
| 14 | C4 PAT minus revenue CAGR | N/M -> 0 | 0 | PASS | Edge rule honoured |
| 15 | D1 ND/EBITDA | 2.57x -> 1 | (1,501.18 - 89.59) / 549.78 = 2.57x -> 1 | PASS | Reported (Ind AS 116) basis correctly held as scored basis |
| 16 | D2 interest cover | 1.39x -> 0 | 258.51 / 186.26 = 1.39x -> 0 | PASS | |
| 17 | D3 D/E | 2.72x -> 0 | 1,501.18 / 552.45 = 2.72x -> 0 | PASS | |
| 18 | D4 current ratio | 0.68x -> 0 | 0.68x -> 0 | PASS | |
| 19 | E1 promoter holding | 17.00% -> 0 | 0 | PASS | FII+DII alternate correctly left untested (NOT FOUND) |
| 20 | E2 promoter change | -3.40pp -> 0 | 0 on any available window | PASS | 1-year window substituted for 3-year, stated; post-Offer 28.25% to 17.00% also scores 0 |
| 21 | E3 pledge | 0% -> 5 | 5 | PASS | |
| 22 | E4 contingent liabilities / NW | N/A -> 0 | 0% -> 5 | **FAIL** | See G-3 |
| 23 | M1 pricing power | 5 | 5 | PASS | Holds on any post-Ind AS 116 base (FY21 29.8% -> FY26 36.8%) |
| 24 | M2 cost advantage vs peer median | 0 | peer FY26 margins 64.3 / 60.7 / 48.4, median 60.7 vs 36.8 -> 0 | PASS | Peer rows 19-22 re-derived |
| 25 | M3 capital efficiency | 0 | FAT 0.88x -> 0 | PASS | |
| 26 | M4 customer stickiness | 3 | 1 decline year, recovered -> 3 | PASS | |
| 27 | M5 scale and dominance | 1 | mcap rank 3 of 4, margin rank 4 -> 1 | PASS | |
| 28 | M6 technology/R&D | 0 | 0 | PASS | |
| 29 | M7 regulatory/licence | 0 | 0 | PASS | |
| 30 | M8 distribution | 5 | 5 | PASS | MINOR G-6: per-centre revenue "implied" on signed, not operational, centres |
| 31 | M9 brand (GM proxy) | 0 | 0 on literal bands | PASS | MINOR G-7: unmapped rubric state |
| 32 | M10 switching costs | 0 | 0 on literal bands | PASS | MINOR G-7: unmapped rubric state |
| 33 | M11 network effects | 5 | 0 | **FAIL** | See G-4 |
| 34 | M12 negative WC / float | 5 | 5 of 8 years negative = majority -> 5 | PASS | Majority holds even if the 3 NOT FOUND years were positive |
| 35 | Moat classification | 5 present, STRONG | 4 present, STRONG | PASS | Class unchanged after G-4 |
| 36 | Core arithmetic | 7+10+8+1+5 = 31 | own arithmetic correct | PASS | |
| 37 | Classification matrix | Core <40 -> AVOID | Core 36 <40 -> AVOID | PASS | |
| 38 | Data confidence adjustment | 8 yrs, moderate, no downgrade | same | PASS | |
| 39 | Deal-breaker application | 1, 3, 4, 8 triggered | on recomputed blocks: 2, 3, 4, 8 triggered; 1 not | PASS | Correct against its own block scores; the set shifts only as a consequence of G-1, G-2 |
| 40 | CAGR edge rules and loss-to-profit data_note | present | present | PASS | |
| 41 | FLAG-GATE0 and YAML schema | present | present | PASS | |
| 42 | Block payload consistent with report body | "2-of-8-year window" | body says 5 of 8 | **FAIL** | See G-5 |

Gate 0 rules checked: 42. Passed: 37. Failed: 5.

### Recomputed Gate 0 summary

| Item | B01 | Recomputed |
|------|-----|-----------|
| Block A | 7 | 10 (A3 2 -> 5) |
| Block B | 10 | 7 (B2 5 -> 2) |
| Block C | 8 | 8 |
| Block D | 1 | 1 |
| Block E | 5 | 10 (E4 0 -> 5) |
| Core | 31 | 36 |
| Moat score | 24 | 19 (M11 5 -> 0) |
| Moats present / class | 5 / STRONG | 4 / STRONG |
| Grand total | 55 | 55 |
| Classification | AVOID | AVOID (unchanged) |
| Deal-breakers triggered | 1, 3, 4, 8 | 2, 3, 4, 8 |
| Strongest block | B (10) | A and E tie (10) |

The classification survives. The deal-breaker set changes: #1 (Block A <8)
clears and #2 (Block B <8) fires. Both caps sit above AVOID, so neither binds.
The "strongest block = cash generation" line in B01 no longer holds on the
recomputed scores. Downstream stages that cite B01's block ranking should
use the recomputed one.

### Gate 0 findings

**G-1 (MAJOR) A3 median ROE: an exclusion rule the scorecard does not contain.**
B01 dropped FY25 as "sign-crossing" net worth. The stage 1 formula is
ROE = PAT / average net worth. FY25 average net worth is positive:
(-93.81 + 459.22) / 2 = Rs182.71 Cr (screener-Data_Sheet.csv rows 39-40).
FY25 ROE = 67.87 / 182.71 = 37.15% (row 24). Median of {37.15%, 14.01%}
= 25.58% -> band >=20% -> score 5, not 2. B01 excludes negative-denominator
years by analogy to the CAGR edge rule. That analogy is reasonable, and
it removes FY19-FY24. It does not reach FY25, whose denominator is
positive. The fully literal reading, with no exclusions, gives a median
near 117% and also scores 5. Only B01's extra "crossing" test produces 2.
Stage 1 rule 2 bars qualitative judgment. Effect: Block A 7 -> 10, and
deal-breaker #1 clears. Classification unchanged.

**G-2 (MAJOR) B2 FCF-positive share: two determinable negative years dropped.**
B01 scored 5 of 5 positive by excluding FY19, FY20 and FY24 as capex NOT
FOUND. FY19 and FY20 CFO are negative: -Rs11.48 Cr and -Rs7.79 Cr
(screener-Data_Sheet.csv row 57). Capex (PPE + intangibles purchased)
cannot be below zero, so FCF = CFO - capex is negative in both years
whatever the capex amount. No estimate is needed to know the sign. FY24
stays NOT FOUND (CFO +228.96, capex not isolated). Determinable years:
5 positive of 7 = 71.4% -> band 50-74% -> score 2. Effect: Block B 10 -> 7.
Deal-breaker #2 (Block B <8 -> max GOOD) fires, non-binding. B01's
block_b_trend "improving" stays valid; its "Strongest block: B" line does
not.

**G-3 (MAJOR) E4 contingent liabilities: a filed nil scored as missing data.**
B01 marked E4 N/A and scored 0 under stage 1 rule 5. The data point is
not missing. AR FY26 Note 33(i), "Contingent liabilities", is present. It
states that the ongoing proceedings "do not meet the recognition or
disclosure criteria of a contingent liability under Ind AS 37" (AR text
line 16419-16427, standalone; consolidated equivalent cited by B01 at
p.155). The filed disclosed contingent liability is therefore nil.
Nil / Rs552.45 Cr = 0% -> band <5% -> score 5. The two readings: (a)
filed nil, score 5; (b) unquantified exposure, score 0. The observation
that separates them is a quantified amount in a later filing: the
May-Jun 2026 GST show-cause notices (B00, LBF3). Those notices post-date
the AR, and E4 scores the latest filed figure. Reading (a) is the rule
as written. Carry the SCN exposure as a flag, not as a score. Effect:
Block E 5 -> 10.

**G-4 (MAJOR) M11 network effects: an N/A leg filled by substitution.**
M11 needs "latest 3yr rev CAGR > prior 3yr AND selling exp % declining".
The latest window is FY23-FY26. The revenue leg uses FY26. The
selling-expense leg has no FY26 value: the Data_Sheet FY26 "Selling and
admin" cell is blank, and screener folded the FY26 cost lines into "Other
Expenses" Rs781.94 Cr (rows 17-18). B01 substituted FY25. Stage 1 rule 5
says a missing data point is marked N/A and scores 0. Every M11 band
above 0 needs the selling-expense direction, so no band can be evaluated.
Recomputed M11 = 0. Even on B01's FY25 proxy the "decline" is 19.78% ->
19.64% (0.14pp), after FY24 at 19.15% (rows 11, 17). That is flat, not a
trend. Effect: moat score 24 -> 19, moats present 5 -> 4. Class stays STRONG.

**G-5 (MINOR) Payload contradicts the report body on the data window.**
The B01 body states the balance-sheet window is 5 of 8 years (FY21,
FY22, FY23, FY25, FY26). The FLAG-GATE0 reason, the analyst_note and the
decision line all say "2-of-8-year" / "only FY25-FY26". B07 inherited
the wrong figure into 6C, 6D and combined_reasoning. Fix the payload
text to 5 of 8.

**G-6 (MINOR) M8 per-centre revenue basis.** The Rs5.97 Cr vs Rs5.78 Cr
per-centre figures are marked "implied" and divide revenue by signed
supply (250+), not operational centres. The score of 5 likely survives,
but the anchor is weak. Verifier A owns the figures themselves.

**G-7 (MINOR, rubric observation for the operator, not a B01 error).**
M9: AWFIS sits 1.37pp above the peer median with 38.3% growth. No band
maps this state ("above peers but growth below = 1" is for weaker
growth). B01 read it as 0. Monotonicity argues 1. M10: one decline year
plus rising receivable days falls to 0, while two decline years scores
1. Neither gap changes a present/absent call. Recorded for a rubric fix.

**G-8 (MINOR) Block A table rows FY25/FY26 are garbled** (EBIT column shows
20.48 and 25.85, and one cell reads "consol 68.76 differs from AR consol
68.76"). The note below the table corrects them and scoring uses the
corrected values. Presentational.

---

## PART 2: EMERGING MOAT (B07) COMPLIANCE TABLE

| # | Rule | Result | Note |
|---|------|--------|------|
| 1 | Six sections plus optionality register present | PASS | |
| 2 | All 23 categories addressed or NO EVIDENCE FOUND | PASS | Summary table carries 23 rows |
| 3 | Section 5 scoring table shows all 23 rows | **FAIL** | E-3, grouped zero rows |
| 4 | Raw scores use the matrix values (HH 4, HM/MH 3, HL/MM/LH 2, ML/LM/LL 1) | PASS | |
| 5 | Evidence multipliers applied correctly | PASS | C1 3x0.7 = 2.1; F2 1x0.7 = 0.7; G1 4x1.0 = 4.0; H2 3x1.0 = 3.0; H3 2x1.0 = 2.0; R1 1x0.7 = 0.7 |
| 6 | Adjusted total arithmetic | PASS | Sum = 12.5 |
| 7 | No 🎙️-only category scored as 📄 | PASS | C1 took the lower 0.7 tier; G1/H2/H3 carry 📄 anchors |
| 8 | Contrary evidence handled consistently across categories | **FAIL** | E-1, F2 |
| 9 | One evidence item credited once | **FAIL** | E-2, WELL in H2 and H3 |
| 10 | Completionist guard applied, 📄 recount line stated | PASS | 8 items / 4 categories; 6 rows scored, far below the 12 trigger |
| 11 | evidence_mix consistent with the scan | **FAIL** | E-4 |
| 12 | Classification band applied to the stated total | PASS | 12.5 -> MODEST as stated; recomputed total flips (E-1) |
| 13 | Category 21 (I1) present, scored above 0 only with both legs | PASS | 0, leg (a) absent |
| 14 | Category 22 (I2) present, scored above 0 only with a named sacrifice | PASS | 0, "nothing must be destroyed" reasoned per claimed moat |
| 15 | I1/I2 contribution stated separately | PASS | 0.0 |
| 16 | Optionality register: 4 columns, carried in YAML | PASS | 7 rows |
| 17 | 2C capex arithmetic shown | PASS | MINOR E-6 on basis |
| 18 | 6C uses the injected B01 block | PASS | Inherits G-5 window error |
| 19 | 6D TURNAROUND given full reasoning | PASS | As written; its "MODEST, not NONE" premise fails after E-1 |
| 20 | Source anchors on every evidence item | **FAIL** | E-5 |
| 21 | G2 excluded for double credit with B01 B4/M12 | PASS | Consistent with the CLAUDE.md one-improvement-one-mechanism rule |
| 22 | YAML block schema complete | PASS | |

Emerging Moat rules checked: 22. Passed: 17. Failed: 5.

### Recomputed Emerging Moat score

| Reading | F2 | H2 | H3 | EM total | Class |
|---------|----|----|----|----------|-------|
| B07 as filed | 0.7 | 3.0 | 2.0 | 12.5 | MODEST |
| E-1 only (F2 -> 0) | 0.0 | 3.0 | 2.0 | 11.8 | NONE |
| E-2 only, fix (b): WELL kept in H2, H3 -> 0 | 0.7 | 3.0 | 0.0 | 10.5 | NONE |
| E-2 only, fix (a): WELL moved to H3, H2 re-rated HM -> MM | 0.7 | 2.0 | 2.0 | 11.5 | NONE |
| E-2 only, fix (a) with H2 not re-rated | 0.7 | 3.0 | 2.0 | 12.5 | MODEST |
| E-1 + E-2 (range) | 0.0 | 2.0-3.0 | 0.0-2.0 | 9.8-11.8 | NONE |

The EM classification flips from MODEST (12-24) to NO MEANINGFUL EMERGING
MOAT (<12) under every recomputed reading except one: F2 left in place
AND WELL moved out of H2 with no re-rating of H2. The filed 12.5 sits 0.5
above the band floor. Any single 0.7 item decides the class.

### Emerging Moat findings

**E-1 (MAJOR) F2 scored positive on evidence B07 itself calls net-negative.**
B07 rates F2 "Weak, explicitly net-negative ... a caution flag more than
a moat" and then scores it ML = 1 x 0.7 = 0.7. The same report scores C2
at 0 because the evidence runs the other way ("worsening"). It scores B1
at 0 because the opposite was found. The consistent application scores
F2 at 0. Stage 7 rule 5 ("never force-fit") points the same way. The
evidence under F2 is a credibility grade C and 2 delivered, 4 partial and
3 missed of 9 tracked promises (B05, as cited in B07 6E). That is evidence
an execution moat is not forming. Recomputed EM = 11.8 -> NONE.
Why MAJOR, not CRITICAL: phase 1 carries no destination PE or decision
to flip. **Escalation note for phase 3:** if stage 11 Pillar 3 reads
em_classification or em_score, re-test this finding against the >1x
destination-PE line. At that point it may be CRITICAL.

**E-2 (MAJOR) WELL certification credited in two categories.**
The same item, "three simultaneous WELL certifications ... via The
Instant Group" (Investor Pres. p.28; AR p.8), is H2's second 📄 leg. It
is also H3's only positive evidence (H3: "same anchor as H2"). B07 applied
the one-improvement-one-mechanism rule to exclude G2, but did not apply
it here. The H2 category definition covers JVs with global leaders,
exclusivity, inbound tech licensing, co-development and strategic equity
investors. A third-party certification is none of those. Its natural home
is H3. The 6E moat map also lists WELL as an existing brand moat, a third use.
Two fixes are possible. (a) Keep WELL in H3 only. H2 then rests on one 📄
item (Malpani, which B07 calls "a single, unproven instance") plus 🎙️
pipeline talk, and needs a maker re-rate. At MM it is 11.5. (b) Keep WELL
in H2. H3 then has no positive evidence, only the zero-renewables
contradiction, and scores 0, giving 10.5. The stage 7 maker must choose
and re-rate. This verifier does not substitute its own likelihood/impact
call.

**E-3 (MINOR) Section 5 table groups zero rows.** A1-A4, B1-B3, D1-D2 and
E1-E2 sit on 4 grouped rows. Stage 7 asks for "all 23 rows". The zeros are
correct. Presentational.

**E-4 (MINOR) evidence_mix does not reconcile.** The YAML gives documented
14 / claim 9 / inference 4. The recount line gives 8 📄 items. No 🔍 item
appears in any Section 3 evidence table. The scope difference (whole report
vs scored categories) is not stated. Also, 6C says "2 more Weak (F2, H3,
R1)" and then lists 3.

**E-5 (MINOR) Anchor format.** Several anchors cite AR "pages" that are
text-file line numbers: A2 "p.11748-11761", D2 "p.10860, p.11703", F1
"p.4685-5851", H3 "p.6444-6457". The header defines [page N] as the PDF
page. These anchors will not resolve for Verifier A or the operator.

**E-6 (MINOR) 2C basis.** Stage 7 multiplies "capex under execution" by
historical fixed-asset turnover. B07 used FY27 capex guidance (Rs200-210 Cr,
🎙️, labelled as such) and the company's gross-block turnover of 1.5x
(Investor Pres. p.8), which uses co-working revenue only. On B01's
Sales / Net Block turnover of 0.88x, the same capex implies 12.1%, not
20.6%. Both bases are defensible if labelled. capex_embedded_growth_pct =
20.6 should carry the basis note when stage 9/11 consume it.

**E-7 (consequential, no separate count) 6D TURNAROUND premise.** 6D
separates AWFIS from "a flat AVOID-with-no-forward-case" because the scan
reads "MODEST, not NONE". After E-1 and E-2 the scan reads NONE. 6D also
leans on B01's wrong "2-of-8-year" window (G-5). The combined-matrix
table itself is not in the stage 7 rule file, so this verifier cannot
re-derive the cell. Stage 7 should re-state 6D on the corrected score.

---

## PART 3: VALUATION (B11), EXPECTATION LEDGER, NARRATIVE

PENDING PHASE 3. B10 and B11 do not exist yet. Rules 4-7 and 11-15 are
not run. Rule 6 (B09 downstream candidates) and rule 9 (stage 13
narrative) belong to that pass. Rule 10 (B09b dossier) fires at /finalize.

---

## PART 4: SUMMARY

| Framework | Rules checked | Passed | Failed | Critical | Major | Minor |
|-----------|---------------|--------|--------|----------|-------|-------|
| Gate 0 (B01) | 42 | 37 | 5 | 0 | 4 | 4 |
| Emerging Moat (B07) | 22 | 17 | 5 | 0 | 2 | 4 |
| Total | 64 | 54 | 10 | 0 | 6 | 8 |

Minor counts include findings that are not rule fails (G-6, G-7, G-8, E-6).

Acceptance rate: 54 / 64 = 84.4%. The denominator is at least 4, so the
rate is applicable. It is above 60%, so it does not trigger REWORK.

What changes for the operator:
1. Gate 0 stays AVOID. Core moves 31 -> 36. The block ranking and the
   deal-breaker set change (#1 clears, #2 fires).
2. The Emerging Moat class most likely moves MODEST -> NONE (9.8-11.8 vs
   filed 12.5). The 6D TURNAROUND rationale then loses its stated premise.
3. Fix the B01 "2-of-8-year" payload text before the Halt 1 dossier cites it.

---

```yaml
stage: B12c
company: "AWFIS"
run_date: "2026-09-19"
model: claude-opus-5
status: complete
scope: "PHASE 1 (Gate 0 + Emerging Moat only); valuation, expectation ledger and narrative audits PENDING PHASE 3"
gate0:
  rules_checked: 42
  fails:
    - "A3 median ROE: FY25 excluded as sign-crossing though its average net worth is positive (Rs182.71 Cr); FY25 ROE 37.15%, median 25.58% -> score 5 not 2 (MAJOR)"
    - "B2 FCF-positive share: FY19/FY20 CFO negative so FCF negative regardless of capex; 5 of 7 determinable = 71.4% -> score 2 not 5 (MAJOR)"
    - "E4 contingent liabilities: AR Note 33(i) files a nil disclosed contingent liability; 0% -> score 5 not 0 (MAJOR)"
    - "M11 network effects: FY26 selling-expense % NOT FOUND, FY25 substituted; stage 1 rule 5 -> score 0 not 5 (MAJOR)"
    - "Payload says 2-of-8-year balance-sheet window; report body says 5 of 8 (FY21-23, FY25-26); propagated into B07 (MINOR)"
  recomputed: {blocks: {A: 10, B: 7, C: 8, D: 1, E: 10}, core_score: 36, moat_score: 19, moats_confirmed: 4, moat_class: "STRONG", grand_total: 55, classification: "AVOID", deal_breakers_triggered: [2, 3, 4, 8]}
  classification_concur: true
emoat:
  rules_checked: 22
  fails:
    - "F2 scored 0.7 on evidence B07 calls net-negative; C2/B1 contrary evidence scored 0 in the same report; F2 -> 0, EM 11.8 NONE (MAJOR)"
    - "WELL certification credited in both H2 and H3 (same anchor); one-evidence-one-credit breached; EM 10.5-11.5 on either fix (MAJOR)"
    - "Section 5 scoring table groups zero rows instead of 23 rows (MINOR)"
    - "evidence_mix 14/9/4 does not reconcile with 8-item recount; no inference items visible; 6C count says 2 lists 3 (MINOR)"
    - "AR anchors cite text-file line numbers as page numbers (A2, D2, F1, H3) (MINOR)"
  recomputed_em_score: "9.8-11.8 (filed 12.5)"
  recomputed_em_classification: "NONE (filed MODEST)"
  classification_concur: false
valuation: {rules_checked: 0, fails: [], status: "PENDING PHASE 3 (B10/B11 not yet produced)"}
expectation_ledger: {present: null, downside_row: null, all_rows_confirm_by: null, all_rows_metric_threshold: null, prob_in_range: null, decay_status_valid: null, off_ledger_credit: null, residual_pct_cmp: null, residual_starter_cap_ok: null, fails: [], status: "PENDING PHASE 3"}
business_understanding_narrative: {present: null, five_questions_answered: null, prose_only: null, section6_candidates_named: null, valuation_vocab_leak: null, fails: [], status: "PENDING STAGE 13"}
recomputed_destination_pe: ""
recomputed_decision: ""
findings:
  - {id: G-1, severity: MAJOR, location: "01-gate0.md Block A, A3", finding: "FY25 ROE excluded by an unwritten sign-crossing rule", recomputed: "A3 5 (median 25.58%); Block A 7 -> 10; deal-breaker 1 clears"}
  - {id: G-2, severity: MAJOR, location: "01-gate0.md Block B, B2", finding: "FY19/FY20 determinably FCF-negative (CFO -11.48, -7.79) dropped as NOT FOUND", recomputed: "B2 2 (71.4%); Block B 10 -> 7; deal-breaker 2 fires, non-binding"}
  - {id: G-3, severity: MAJOR, location: "01-gate0.md Block E, E4", finding: "Filed nil contingent liability (AR Note 33(i)) scored as missing data", recomputed: "E4 5; Block E 5 -> 10; GST SCN exposure carried as flag"}
  - {id: G-4, severity: MAJOR, location: "01-gate0.md Block F, M11", finding: "Missing FY26 selling-expense leg filled with FY25; FY25 proxy shows only -0.14pp", recomputed: "M11 0; moat score 24 -> 19; 4 present, STRONG unchanged"}
  - {id: G-5, severity: MINOR, location: "B01-gate0.yaml flags/analyst_note; 01-gate0.md decision line", finding: "2-of-8-year window contradicts body's 5-of-8; propagated to B07 6C/6D", recomputed: "text fix only"}
  - {id: G-6, severity: MINOR, location: "01-gate0.md M8", finding: "Per-centre revenue implied on signed supply, not operational centres", recomputed: "score likely unchanged"}
  - {id: G-7, severity: MINOR, location: "prompts/01-gate-0-pipeline.md M9, M10", finding: "Rubric gaps: unmapped states (M9 above peers with higher growth; M10 one decline year with unstable receivables)", recomputed: "operator rubric fix; no present/absent change"}
  - {id: G-8, severity: MINOR, location: "01-gate0.md Block A table", finding: "FY25/FY26 rows garbled; corrected in note", recomputed: "presentational"}
  - {id: E-1, severity: MAJOR, location: "07-emoat.md Section 5, F2", finding: "Net-negative F2 scored 0.7 while contrary-evidence C2/B1 scored 0", recomputed: "F2 0; EM 11.8 -> NONE; escalate re-test at phase 3 if Pillar 3 consumes em_classification"}
  - {id: E-2, severity: MAJOR, location: "07-emoat.md H2 and H3", finding: "WELL certification double-credited (H2 and H3, same anchor; also listed as existing brand moat in 6E)", recomputed: "EM 10.5 (fix b) or 11.5 (fix a, H2 re-rated MM); maker to choose and re-rate"}
  - {id: E-3, severity: MINOR, location: "07-emoat.md Section 5", finding: "Zero rows grouped; stage 7 asks for all 23 rows", recomputed: "presentational"}
  - {id: E-4, severity: MINOR, location: "B07-emoat.yaml evidence_mix; 07-emoat.md 6C", finding: "evidence_mix does not reconcile with recount; 6C says 2 Weak, lists 3", recomputed: "text fix"}
  - {id: E-5, severity: MINOR, location: "07-emoat.md A2, D2, F1, H3", finding: "AR anchors are text line numbers labelled as pages", recomputed: "re-anchor to PDF pages"}
  - {id: E-6, severity: MINOR, location: "07-emoat.md 2C; B07 capex_embedded_growth_pct", finding: "Guided (not under-execution) capex x company gross-block FAT 1.5x; B01 FAT 0.88x basis gives 12.1%", recomputed: "20.6% stands if basis labelled downstream"}
critical_count: 0
major_count: 6
minor_count: 8
acceptance_rate: 84.4
```
