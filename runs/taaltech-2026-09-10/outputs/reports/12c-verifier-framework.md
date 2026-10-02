# STAGE 12C — VERIFIER C: FRAMEWORK ADHERENCE AUDIT
TAALTECH | Run: taaltech-2026-09-10 | Model: claude-opus-4-8
**SCOPE: PHASE 1 ONLY — Gate 0 (B01) and Emerging Moat (B07).**

Valuation adherence (B10 / B11) does NOT run in this pass. Stages 10 and 11
have not run. No Section 1B layer, no Master Prompt, no FTTCP file was read.
The valuation, expectation-ledger, and business-understanding sections of the
B12c block are marked PENDING PHASE 3.

## RULE SOURCES USED
- prompts/01-gate-0-pipeline.md
- prompts/07-emerging-moat-pipeline.md

## ARTIFACTS AUDITED
- runs/taaltech-2026-09-10/outputs/reports/01-gate0.md
- runs/taaltech-2026-09-10/outputs/blocks/B01-gate0.yaml
- runs/taaltech-2026-09-10/outputs/reports/07-emoat.md
- runs/taaltech-2026-09-10/outputs/blocks/B07-emoat.yaml

## METHOD
Every sub-score was re-derived from the report's own stated inputs against the
rule file's own bands. Numbers were not checked against source PDFs; that is
Verifier A's non-overridable domain. This audit asks one question only: was
the rule applied as written.

---

# PART 1 — GATE 0 (B01) COMPLIANCE

## 1.1 Re-derivation of every sub-score

### BLOCK A — RETURN ON CAPITAL (claimed 15/20)

ROCE series stated in the report: 34.2 / 42.1 / 60.3 / 50.5 / 26.6 / 34.0 /
28.5 / 24.2 / 25.6 / 22.5.

| Test | Rule band | Report input | Re-derived | Claimed | Verdict |
|---|---|---|---|---|---|
| A1 | >=25% = 5 | median of 10 | sorted: 22.5, 24.2, 25.6, 26.6, **28.5, 34.0**, 34.2, 42.1, 50.5, 60.3 -> (28.5+34.0)/2 = **31.25%** -> 5 | 5 | PASS |
| A2 | >=15% = 5 | min year | **22.5%** (FY2026) -> 5 | 5 | PASS |
| A3 | >=20% = 5 | median ROE | sorted: 22.2, 25.3, 25.9, 26.6, **28.0, 34.8**, 36.5, 44.4, 50.2, 62.3 -> **31.4%** -> 5 | 5 | PASS |
| A4 | decline >5pp = 0 | 22.5 vs 34.2 | **-11.7pp** -> 0 | 0 | PASS |

Block A total re-derived: 5+5+5+0 = **15**. Matches. PASS.

ROE spot re-derivation from the stated net-worth and PAT series (PAT / average
net worth): FY18 15.61/25.065 = 62.3%; FY21 31.80/63.395 = 50.2%; FY23
31.23/111.43 = 28.0%; FY26 56.72/224.59 = 25.3%. All match the report. The
FY2017 closing-only basis is stated as the rule requires.

**FINDING F1 (MINOR) — ROCE denominator substituted.** The rule file's
FORMULA DEFINITIONS section is headed "fixed, do not substitute alternatives"
and defines ROCE = EBIT / (Total Assets - Current Liabilities). The report
used Total Assets - "Other Liabilities" (01-gate0.md, Block A preamble),
which the report itself validates as equity + borrowings. Cross-check on
FY2026: 270.93 - 24.88 = 246.05 = net worth 245.14 + borrowings 0.91, exactly.
The mandated denominator for FY2026 is 270.93 - 25.79 = 245.14, giving ROCE
22.62% against the reported 22.54%. Immaterial at FY2026. Earlier-year current
liabilities are not in the corpus, so the deviation is not quantifiable for
FY2017-FY2025. Score impact: none demonstrable. A1 (31.25% vs a 25% band edge)
and A2 (22.5% vs a 15% band edge) hold with wide margin. A4 already sits at
the floor score of 0, so any correction can only raise Block A. The deviation
is disclosed in data_notes. Severity MINOR on that basis, but the deviation
from a "do not substitute" formula is real and should be corrected at source.

Note on the numerator: EBIT excludes Other Income (Rs19.40cr, largely treasury
return) while the denominator retains the Rs143.89cr investment book that
generates it. The rule file does not define EBIT's treatment of other income,
so this is not a rule breach. It is recorded because it biases ROCE downward
and the report does not say so.

### BLOCK B — CASH GENERATION QUALITY (claimed 14/20)

| Test | Rule band | Re-derived | Claimed | Verdict |
|---|---|---|---|---|
| B1 | 0.85-0.99 = 4 | cum CFO 258.57 (sum verified) / cum PAT 292.44 (sum verified) = **0.8842** -> 4 | 4 | PASS |
| B2 | 100% = 5; 75-99 = 4 | see F2 | 5 | FAIL (MINOR) |
| B3 | >=0.60 = 5 | 181.16 / 256.83 = **0.7054** -> 5 | 5 | PASS (arithmetic slip, F3) |
| B4 | N/A -> 0 | inputs absent, 0 | 0 | PASS |

Cumulative CFO re-added: 2.41+14.59+23.24+32.59+39.98+29.63+21.96+34.41+41.02
+18.74 = 258.57. Cumulative PAT re-added: 292.44. Both match.
B3 denominator re-derived: 292.44 - 3.81 (FY17) - 31.80 (FY21) = 256.83. Matches.

**FINDING F2 (MINOR) — B2 denominator excludes two years, raising the score
one band.** The rule reads "FCF-positive years **as proportion**: 100% = 5 |
75-99 = 4". The report computed 8 of 8 *computable* years = 100% -> 5,
excluding FY2017 and FY2021 from both numerator and denominator
(01-gate0.md, Block B). Operating rule 5 of the rule file says a data point
that is not available is marked N/A and **scored 0**, never gap-filled. On the
stricter reading the proportion is 8 of 10 = 80% -> band 75-99 -> **B2 = 4**.
Recomputed cascade under the stricter reading: Block B 13/20, core score
**69/100**, grand total 80/160. Classification band is unchanged (Core 60-79 +
MODERATE = GOOD). Decision survives; the treatment is labelled, not hidden,
and the rule file does not explicitly govern partial-year availability inside
a proportion metric. Recorded MINOR, not MAJOR, on that ambiguity, and flagged
to the framework owner as a rule gap worth closing.

**FINDING F3 (MINOR) — cumulative FCF arithmetic off by Rs0.01cr.** FY2026 FCF
is stated as 18.62 (01-gate0.md, FCF table) but CFO 18.74 - capex 0.13 =
**18.61**. Cumulative FCF is therefore 181.15, not 181.16, and B3 is 0.70533
rather than 0.70537. No band effect. Cosmetic.

FCF definition check: the rule defines capex as purchase of PPE + intangibles
from the cash flow statement. The report used a delta-Net-Block-plus-
depreciation proxy for FY2018-2024 in the absence of a filed capex line,
labelled "computed, proxy basis", validated against the FY2025 filed figure
(1.65 proxy vs 1.62 filed), and excluded the two years where the proxy breaks.
Both derivation inputs come from the provided data, so this is computation,
not the gap-filling with typical-industry values the rule prohibits. PASS with
the note that the rule file authorises "compute only when absent" explicitly
for ROCE and only implicitly for capex.

B4 is a **defensible zero, correctly labelled**: Trade Payables do not exist
for FY2017 in the corpus, the latest-vs-earliest basis the rule mandates
cannot be built, the report says so, scores 0 per operating rule 5, and keeps
the one computable year as unscored directional evidence. This is exactly what
the rule requires. Not a finding.

### BLOCK C — GROWTH (claimed 12/20)

| Test | Rule band | Re-derived | Claimed | Verdict |
|---|---|---|---|---|
| C1 | 5-9.9% = 1 | (197.43/92.06)^(1/9)-1 = **8.85%** -> 1 | 1 | PASS |
| C2 | >=20% = 5 | (56.72/3.81)^(1/9)-1 = **35.0%** -> 5 | 5 | PASS |
| C3 | 50-74% = 1 | 6 of 9 = **66.7%** -> 1 | 1 | PASS |
| C4 | >=+3pp = 5 | 35.0 - 8.85 = **+26.15pp** -> 5 | 5 | PASS |

Block C total re-derived: 1+5+1+5 = **12**. Matches. PASS.

Period count check: 10 data points FY2017-FY2026, exponent 1/9. Correct. A
common error (using 1/10) is not present.

**CAGR edge rules — all three checked, all correctly handled.**
- Negative or zero endpoint: none in either CAGR window (revenue 92.06 to
  197.43; PAT 3.81 to 56.72). "N/M (negative endpoint)" correctly not invoked.
- Loss-to-profit swing: none. data_notes states "No loss-to-profit PAT swing in
  the window; CAGR N/M edge rules do not apply". This is the rule's required
  disclosure, correctly made as a negative.
- C4 when PAT CAGR is N/M: not triggered; C4 scored on a live number.
PASS on all three.

The report attaches a FLAG to C2 and C4 for FY2017-base sensitivity and states
the FY2022-2026 alternative window (+4.3pp spread against the scored +26.15pp).
The rule file mandates mechanical scoring with no qualitative judgment
(operating rule 2), so scoring the mandated window and flagging the
sensitivity separately is the correct handling. PASS.

### BLOCK D — BALANCE SHEET STRENGTH (claimed 20/20)

D1 net cash Rs26.87cr -> "net cash = 5" -> 5. PASS.
D2 55.46 / 0.50 = 111x -> ">=10x = 5" -> 5. PASS.
D3 0.91 / 245.14 = 0.0037 -> "<0.1 = 5" -> 5. PASS.
D4 135.68 / 25.79 = 5.26x -> ">=2.0 = 5" -> 5. PASS.
Block D total 20. Matches. PASS.

### BLOCK E — SHAREHOLDER ALIGNMENT (claimed 9/20)

E1 50.80% -> "50-59.9 = 4" -> 4. PASS. Observation: the rule says "latest
quarter"; the report used the 31-Mar-2026 AR disclosure because no later
shareholding-pattern filing is in the corpus. Anchored and defensible, but the
substitution is not listed in input_gaps.
E2 NOT FOUND -> 0. **Defensible zero, correctly labelled** per operating rule
5. Not a finding.
E3 NOT FOUND -> 0. **Defensible zero, correctly labelled.** Not a finding.
E4 9.38 / 245.14 = 3.83% -> "<5% = 5" -> 5. PASS.
Block E total 4+0+0+5 = **9**. Matches. PASS.

### BLOCK F — QUANTITATIVE MOAT (claimed 11/60)

| Test | Rule application | Verdict |
|---|---|---|
| M1 = 0 | Margin expanded >=2pp but revenue CAGR 8.85% < 10%, so no band qualifies; "else 0" correctly reached | PASS |
| M2 = 0 | PEER DATA NEEDED, marked, not guessed | PASS |
| M3 = 5 | FAT 197.43/2.95 = 66.9x > 3x AND ROCE 22.5% > 20% -> top band | PASS |
| M4 = 0 | 3 decline years -> "3+ decline years = 0" | PASS |
| M5 = 0 | PEER DATA NEEDED, marked | PASS |
| M6 = 0 | R&D 0.376/197.43 = 0.19% < 1% floor -> 0 | PASS |
| M7 = 0 | unregulated -> 0 | PASS |
| M8 = 0 | no distribution network -> 0 | PASS |
| M9 = 0 | PEER DATA NEEDED, marked | PASS |
| M10 = 1 | overall growth with 3 (>=2) decline years -> band 1 | PASS |
| M11 = 5 | see F4 | FAIL (MINOR) |
| M12 = 0 | both computable years 72.3 and 88.4 days > 45 -> 0 | PASS |

Moat score re-added: 0+0+5+0+0+0+0+0+0+1+5+0 = **11**. Matches.
Moats present at >=3: M3 and M11 = **2**. Band "2-3 = MODERATE". Matches. PASS.

**FINDING F4 (MINOR) — M11 cannot be re-derived from the report's own stated
inputs.** M11 scores 5, which requires latest-3yr revenue CAGR > prior-3yr AND
selling expense percentage declining. The report states 7.45% vs 7.01%
(01-gate0.md, M11 row) but does not show the FY2020 and FY2023 revenue
endpoints anywhere in the report, so the 0.44pp margin that decides the test
cannot be reconstructed. Operating rule 3 requires "Show every number you
extract". Two further points: the rule says "selling exp % declining" and the
report substituted a comparison of two 3-year averages (9.18% vs 8.86%), a
reasonable but unmandated reading; and the >=6-year precondition for the
two-window test is met (10 years), so the conservative-fallback branch
correctly did not apply. Consequence if M11 were 0: moat_score 6, moats
confirmed 1, moat_class THIN. Classification is **unchanged at GOOD** either
way, because the matrix routes both MODERATE and THIN through "Core 60-79 +
else = GOOD". The report itself flags M11 as borderline. MINOR.

M2, M5 and M9 are **defensible zeros, correctly labelled** with the rule's own
"PEER DATA NEEDED" wording and carried into input_gaps. Not findings. M1 and
M3 are scored strictly per formula with the artifact flagged separately, which
is what operating rule 2 requires.

## 1.2 Totals, classification and overrides

| Line | Re-derived | Claimed | Verdict |
|---|---|---|---|
| Core score | 15+14+12+20+9 = **70** | 70 | PASS |
| Moat score | **11** | 11 | PASS |
| Grand total | 70+11 = **81** | 81 | PASS |
| Moat class | 2 present -> **MODERATE** | MODERATE | PASS |
| Classification | Core 70 in 60-79 + not STRONG/FORTRESS -> **"Core 60-79 + else = GOOD"** | GOOD | PASS |

Blocks in B01-gate0.yaml {A:15, B:14, C:12, D:20, E:9} match the report body
exactly. core_score, moat_score, grand_total, moats_confirmed, moat_class and
classification all reconcile. No block total contradicts its parts.

**Deal-breaker overrides, all nine re-tested against the rule text:**

| # | Rule | Actual | Should fire? | Report | Verdict |
|---|---|---|---|---|---|
| 1 | Block A <8 -> max GOOD | A=15 | No | N/A | PASS |
| 2 | Block B <8 -> max GOOD | B=14 | No | N/A | PASS |
| 3 | median ROCE <10% -> max AVERAGE | 31.25% | No | N/A | PASS |
| 4 | cum CFO/PAT <0.50 -> max AVERAGE | 0.884 | No | N/A | PASS |
| 5 | pledge >15% -> max AVERAGE | NOT FOUND | No (rule keys to a measured >15%, not to absence) | "cannot confirm, not scored as breach" | PASS |
| 6 | ND/EBITDA >3x AND IC <3x -> AVOID | net cash, IC 111x | No | N/A | PASS |
| 7 | revenue declined in majority of years -> max AVERAGE | 3 of 9 = 33% | No | N/A | PASS |
| 8 | PAT negative in any of last 3 years -> max AVERAGE | positive FY24, FY25, FY26 | No | N/A | PASS |
| 9 | history <3 years -> AVERAGE | 10 years | No | N/A | PASS |

deal_breakers: [] is correct. No deal-breaker that should have fired failed to
fire. The rule's "state WHICH years drive any deal-breaker" instruction is
vacuous here because none fired.

**FINDING F5 (MAJOR) — history_downgrade set true against its rule
definition.** The rule file defines this field in exactly one place: "Data
confidence: 10+ yrs full | 7-9 moderate | 5-6 lower, flag 'may not have seen
full cycle' | 3-4 LIMITED, **downgrade classification one tier** | <3 auto
AVERAGE." The downgrade trigger is a year count of 3-4. TAALTECH has 10 years
(data_years: 10, fy_range FY2017 to FY2026), which is the "full" tier. No
downgrade condition exists under the rule.

The report set `history_downgrade: true` (B01-gate0.yaml line 21; 01-gate0.md
CLASSIFICATION section and the classification box) on a different basis: an
unresolved pre-FY2022 business-mix comparability question. That is a real
analytical concern, but the rule file does not attach it to this field.

Two consequences, both live:
1. **The block asserts a downgrade condition while the classification shows
   none.** Classification stayed GOOD. Under the rule as written, if
   history_downgrade were genuinely true the classification would have to drop
   one tier to AVERAGE. As emitted, the boolean and the classification
   contradict each other on the rule's own terms.
2. **Downstream consumption risk.** history_downgrade is a boolean in the block
   payload. A later stage reading it at face value may apply a one-tier
   downgrade (GOOD -> AVERAGE) that the rule file does not authorise. GOOD and
   AVERAGE are different rows of the transition decision matrix and different
   position-sizing inputs.

Rule-correct value: `history_downgrade: false`, with the comparability concern
carried where the report already also carries it, in flags[] (the FLAG-GATE0
row) and in data_notes. The report's narrative is honest and explicit
("flagged, not silently scored across"), which is why this is MAJOR rather
than CRITICAL: a reader of the prose will not be misled, only a machine
consumer of the boolean.

**Observation, not a finding — FLAG-GATE0 fired outside its stated trigger.**
The rule file's flags[] comment says add FLAG-GATE0 "if classification <=
AVERAGE with historical depressors identified". Classification is GOOD, above
AVERAGE, so the stated trigger did not fire. The report added the flag anyway.
Over-flagging is not a rule breach and CLAUDE.md holds that flags propagate.
Recorded so the framework owner can decide whether the trigger condition
should be widened; not charged against the stage.

## 1.3 Output-format compliance

| Requirement | Verdict |
|---|---|
| Opening line "Data available: [X] years (FY__ to FY__). Scoring adapted to [X]-year history." | PASS, verbatim form |
| Every number followed by a source anchor | PASS, with F4 the one gap |
| All blocks, all line items, moat profile bars, classification box, strongest/weakest block, decision line | PASS, all present |
| YAML schema fields all present and typed | PASS |
| analyst_note <= 200 words | PASS, 156 words |
| block_b_trend = direction + the one number showing it | PASS ("deteriorating - CFO/PAT fell from 0.84x (FY2025) to 0.33x (FY2026)") |

The YAML block sits in outputs/blocks/B01-gate0.yaml rather than at the end of
the report file. That is the pipeline's artifact-split convention, not a stage
defect. Not a finding.

## 1.4 Gate 0 scorecard

**51 rules checked. 5 fails (1 MAJOR, 4 MINOR). 46 passed. 90.2%.**

---

# PART 2 — EMERGING MOAT (B07) COMPLIANCE

## 2.1 Coverage

All 22 categories plus R1 = 23 rows appear in the Section 3 summary table:
A1-A4 (4), B1-B3 (3), C1-C2 (2), D1-D2 (2), E1-E2 (2), F1-F2 (2), G1-G2 (2),
H1-H3 (3), I1-I2 (2) = 22, plus R1. Every row is either scored on named
evidence or carries an explicit NO EVIDENCE FOUND. No category is silently
dropped. PASS.

All six sections executed in one response: Section 1 (1A/1B/1C), Section 2
(2A/2B/2C/2D), Section 3, Section 4 (4A/4B/4C), Section 5, Section 6
(6A/6B/6C/6D/6E), plus the Optionality Register. PASS.

2C arithmetic: capex under execution = Rs0, implied incremental revenue = 0%
of current revenue, with the negative fixed-asset movement shown
(Rs279.07 lakh decline). capex_embedded_growth_pct: 0 in the YAML matches.
PASS.

## 2.2 Re-derivation of the score

| # | Raw | Matrix label | Multiplier | Adjusted | Re-check |
|---|---|---|---|---|---|
| C1 | 2 | HL/MM/LH = 2 | doc 1.0 | 2.0 | correct |
| F1 | 1 | LL = 1 | doc 1.0 | 1.0 | correct |
| H3 | 1 | LL = 1 | doc 1.0 | 1.0 | correct |
| all other 20 rows | 0 | no evidence = 0 | — | 0.0 | correct |
| **TOTAL** | | | | **4.0** | **matches em_score 4** |

Matrix check against the rule (HH=4, HM/MH=3, HL/MM/LH=2, ML/LM=1, LL=1, no
evidence=0): every raw score carries the correct label, and every label maps to
the correct integer. PASS.

**Classification band.** Rule: ">=40 EXPANSION | 25-39 STRENGTHENING | 12-24
MODEST | <12 NONE", bands ABSOLUTE per the 20-Aug-2026 operator ruling, no
rescale, ceiling 92. em_score 4 < 12 -> **NO MEANINGFUL EMERGING MOAT**.
em_classification: "NONE" matches the enum. The report states the ceiling as
23 rows x 4 = 92, which matches the rule file. PASS.

**Evidence-tier arithmetic.** The rule requires raw x 1.0 for documented, 0.7
for management claim, 0.5 for analyst inference. All three scored rows rest on
filed AR facts and take 1.0x:
- C1: AR p.37 tenure statement and AR p.102 Note 42 concentration table.
- F1: AR p.94 / p.146 actuarial attrition assumption.
- H3: AR p.37 Ecovadis certification mention.
No category scored above zero on a claim-tier or inference-tier item. The
specific failure mode the verifier rubric names — a claim-only category scoring
as if documented — is **not present**. The claim tier is structurally empty
this run (no concalls, no investor presentation), which the report states and
carries into input_gaps. PASS.

Boundary note, not a finding: H3's Ecovadis item is an MD&A sentence with no
rating tier. The taxonomy's claim tier is defined as "stated in concall or
presentation", which an AR sentence is not, so the documented tier is reached
by elimination. Even at 0.7x the row moves 1.0 to 0.7 and the total to 3.7,
band unchanged.

**Completionist guard.** The rule fires the recount when 12 or more categories
score as active. Three categories are active, so the threshold is not near.
The report performed and stated the recount anyway, in the mandated form.
PASS on the guard itself.

**FINDING F6 (MINOR) — the recount line's count does not match the items it
enumerates.** The line reads "5 documented items across 3 categories (C1: p.37
tenure statement, p.102 Note 42 concentration table; F1: p.94/p.146 attrition
assumption; H3: p.37 Ecovadis mention)" (07-emoat.md Section 3, and
B07-emoat.yaml completionist_recount). The parenthesis enumerates **four**
distinct items, not five. The fifth appears only if the standalone (p.94) and
consolidated (p.146) presentations of the same actuarial assumption are
counted as two items, which double-counts one fact. evidence_mix.documented: 5
carries the same count. No scoring consequence: the guard threshold is 12 and
neither 4 nor 5 approaches it. But the recount is the one place the rule asks
for an exact count of documented items, and the count does not match its parts.

**FINDING F7 (MINOR) — G1 excluded by a constraint outside both rule files.**
The rule's G1 what-to-look-for list is "net cash growing while investing,
undrawn lines, internally funded capex, rating upgrade, cost of debt vs
peers". TAALTECH is debt-free both years, internally funds capex, and holds a
Rs143.89cr investment book, so on the category's own list some evidence exists.
The report scored G1 = 0, citing "this scan's constraint 2" (07-emoat.md,
Family G), an injected run constraint that appears in neither
prompts/01-gate-0-pipeline.md nor prompts/07-emerging-moat-pipeline.md and
which this verifier therefore cannot validate. The report is transparent about
the choice and routes the underlying facts into the optionality register as a
risk-framed item rather than discarding them. Band impact: even a generous
raw 2 x 1.0 lifts em_score to 6, still far below the 12 threshold. NONE holds.
MINOR, and flagged so the operator can confirm constraint 2 was genuinely
injected for this run.

**I1 and I2 (categories 21 and 22), both present, both scored 0.**
- I1 scores 0 because part (a) fails on the AR's own median remuneration of
  Rs9.40 lakh, with no named patent inventors and no verifiable ex-major-firm
  concentration. The rule requires BOTH legs and scores part (a) alone as 0.
  Correctly applied. The verifier rubric's "above 0 only if both legs evidenced
  with the (b) leg carrying >=1 documented source" is not engaged.
- I2 scores 0 because the honest answer to the sacrifice question is "nothing
  must be destroyed" — the rule's own explicit zero condition. Correctly
  applied.
- The mandated separate statement is present: "I1/I2 contribution: 0.0 points",
  with the review-checkpoint note that TAALTECH crosses no threshold at all.
PASS on all three.

Both are **defensible zeros, correctly labelled and reasoned against the
category's own two-leg structure**. Not findings.

## 2.3 Optionality register

Rule: "A table of forward advantages that scored 0 or rest only on claim /
inference evidence. Each row: the optionality in one line; the specific
documentation that would convert it to documented; where that evidence would
first appear (AR note, exchange filing, concall, order announcement);
realistic conversion window."

Seven rows, four columns, present in both the report table and
B07-emoat.yaml optionality_register with matching content. Every row names a
specific converting document and a specific first-appearance location. PASS on
those two columns.

**FINDING F8 (MINOR) — two of seven register rows carry no conversion
window.** Row 3 (I1 specialist workforce) and row 5 (F1 talent density) both
state "Unclear, no signal currently" in the conversion-window column. The rule
requires a "realistic conversion window" on every row. "Unclear" is an absence
of a window, not a window. The other five rows comply (12-24 months x2,
12 months x2, 2-4 quarters). Register items are watched and never scored, so
there is no scoring consequence; the defect is that two watch items enter the
monitoring checklist with no review date attached.

**FINDING F9 (MINOR) — two register rows sit outside the register's defined
scope.** The register is defined for advantages that "scored 0 or rest only on
claim/inference evidence". The H3 row and the F1 row correspond to categories
that scored 1.0 each on documented evidence. The report is not double-crediting
(the register is explicitly "watched, never scored", and the C1 credited fact
is kept out of the register), so this is a scope-definition deviation with no
adverse effect. Recorded because the rule as written would put a scored,
documented category outside the register.

The register does honour the rule's harder discipline: no register item is
also scored. PASS on that.

## 2.4 Catalyst list

Rule schema: catalysts_12m entries carry {catalyst, window, evidence_type,
anchor} and feed Pillar 3 catalyst proximity downstream. The task's test:
does every catalyst carry an observable first-appearance source and a window.

| # | Catalyst | Observable first-appearance source | Window | Verdict |
|---|---|---|---|---|
| 1 | Q2 FY27 results confirm/reverse the revenue acceleration | Q2 FY27 results filing; anchor Results_Q1FY27 Rs64.81cr base | on/around Nov 2026 | PASS |
| 2 | Next AR Note 42 top-customer share vs 28-30% | next AR Note 42; anchor AR p.102 FY26 base 24.05% | on/around Aug 2027 | PASS |
| 3 | Disclosed Ecovadis rating tier | next AR or interim Ecovadis renewal announcement; anchor AR p.37 | on/around Aug 2027 or interim | PASS |
| 4 | Next AR gratuity-note attrition assumption | next AR; anchor AR p.94/p.146 | on/around Aug 2027 | PASS |
| 5 | Any BSE filing naming a patent/design/IP filing | BSE filing; anchor is an absence ("NOT FOUND in Annual_Report_2026") | "any filing within 12 months; none scheduled or flagged" | PASS, weak |

Every catalyst names an observable source that a monitor can watch and a
window. All five windows fall inside 12 months of the 2026-09-10 run date
(Aug 2027 is 11.7 months out), so the catalysts_12m field is used within its
stated horizon. PASS.

**FINDING F10 (MINOR) — two catalysts carry an evidence_type outside the
taxonomy.** Catalysts 3 and 5 use `evidence_type: "documented if it appears"`.
The rule's taxonomy has exactly three values (documented / claim / inference).
A conditional is not a tier. Both catalysts are genuinely unevidenced today —
catalyst 5's own anchor is the absence of any IP mention across 164 pages —
so the honest tier is inference or a null. Downstream this field feeds Pillar 3
catalyst proximity; a non-enum value there is a parsing and weighting risk.

## 2.5 Combined assessment with Gate 0

**6C, the combined table.** The rule requires the table to use the INJECTED
Gate 0 block and to carry core score, existing moat count, and both
classifications. Checked cell by cell against B01-gate0.yaml:

| Element | 6C table | B01 block | Verdict |
|---|---|---|---|
| Core score | 70/100 | core_score: 70 | match |
| Existing moat score | 11/60 | moat_score: 11 | match |
| Grand total / class | 81/160, GOOD | 81, "GOOD" | match |
| Moats confirmed / class | 2, MODERATE | 2, "MODERATE" | match |
| Forward score / class | em_score 4, ceiling 92, NONE | — | internally consistent |

No injected figure was altered, rounded or re-derived. PASS.

**6D, the combined classification.** The report reasons GOOD backward + NONE
forward -> **GOOD**, declines to lift to GOOD+ or HIGH POTENTIAL, gives its
reasoning, and expressly notes that this is NOT one of the GOOD/AVERAGE-plus-
EXPANSION transition setups the operation hunts. combined_assessment: "GOOD"
is inside the rule's allowed set (EXCEPTIONAL / EXCELLENT+ / HIGH POTENTIAL /
GOOD+ / GOOD / TURNAROUND / AVERAGE / AVOID). The rule's "give HIGH POTENTIAL
and TURNAROUND rows full reasoning" does not fire, since neither is claimed.
combined_reasoning is one line as required. PASS.

**FINDING F11 (MINOR, against the rule file, not the stage) — the 6D "standard
matrix" is never defined.** prompts/07-emerging-moat-pipeline.md 6D names the
eight output labels but supplies no cell definitions mapping a backward class
and a forward class to a combined label. The stage's GOOD+NONE -> GOOD
derivation is the only sensible reading available and is reasoned in prose,
but it cannot be independently re-derived from the rule text. This is a
framework-file gap for the operator to close. It is listed here for
visibility and is **excluded from the stage's acceptance-rate denominator**.

## 2.6 Internal consistency of the B07 block

| Field | Check | Verdict |
|---|---|---|
| em_score 4 | equals the scoring table total | PASS |
| em_classification NONE | matches the <12 band and the enum | PASS |
| active_categories | only C1 listed; F1 and H3 are Weak and correctly excluded from a "Strong/Moderate rows only" field | PASS |
| evidence_mix documented 5 | see F6 | FAIL (MINOR) |
| evidence_mix inference 4 | see F12 | FAIL (MINOR) |
| capex_embedded_growth_pct 0 | matches 2C | PASS |
| combined_assessment / reasoning | match 6D prose | PASS |
| top_moat_risks | 3 rows, all traceable to 6B | PASS |
| analyst_note word count | ~120 words, under the 200 cap | PASS |
| analyst_note consistency | see F13 | FAIL (MINOR) |

**FINDING F12 (MINOR) — the four inference items are not enumerated.**
evidence_mix reports {documented: 5, claim: 0, inference: 4}. The report
enumerates its documented items in the recount line but never lists the four
inference items, so the count cannot be traced to specific passages. Candidates
exist in the margin section (the C1 bill-rate inference, the lean-overhead
inference, the revenue-comparability hypothesis, the 2C distributed-delivery
reading) but the mapping is not stated. No scoring consequence: no inference
item was scored, so the 0.5x multiplier is nowhere in play.

**FINDING F13 (MINOR) — analyst_note contradicts the report body on the
no-evidence count.** analyst_note opens "22 of 23 rows return NO EVIDENCE
FOUND or the reverse of the category's claim". Three rows carry evidence (C1,
F1, H3), so the correct figure is 20 of 23, which is exactly what the report
body and the recount line say ("19 of 22 categories plus R1 returned NO
EVIDENCE FOUND"). The analyst_note figure understates the evidence base by two
rows. Cosmetic; the block's own fields are correct.

## 2.7 Emerging Moat scorecard

**47 rules checked. 7 fails (0 MAJOR, 7 MINOR). 40 passed. 85.1%.**

---

# PART 3 — VALUATION ADHERENCE

**PENDING PHASE 3.** Stages 10 and 11 have not run. No B10 or B11 artifact
exists for this run. No Section 1B layer file, Master Prompt section, or FTTCP
document was read. Verifier C rules 4, 6, 7, 9, 11, 12, 13 and 14 (valuation
mechanics, destination PE, Hurdle Ratio, sector cap, method plurality,
downstream-candidate cap on stage 11 catalysts, expectation ledger, ledger and
residual gates, business understanding narrative) are **not evaluated in this
pass** and are not counted in any denominator.

Verifier C rule 8 (stage 7 categories 21 and 22 present) IS in phase-1 scope
and is discharged in section 2.2 above: both present, both scored 0, both
correctly reasoned against their two-leg structures. No REWORK for stage 7 on
that rule.

---

# PART 4 — CONSOLIDATED FINDINGS

| ID | Sev | Location | Finding | Recomputed |
|---|---|---|---|---|
| F5 | MAJOR | B01-gate0.yaml:21 / 01-gate0.md CLASSIFICATION | history_downgrade = true with 10 years of data; the field's only rule trigger is a 3-4 year history. Boolean asserts a downgrade the classification does not apply. | rule-correct value `false` |
| F1 | MINOR | 01-gate0.md Block A preamble | ROCE denominator = Total Assets - Other Liabilities, not the mandated Total Assets - Current Liabilities, under a "do not substitute" heading | FY26 22.62% vs 22.54%; no band change |
| F2 | MINOR | 01-gate0.md Block B, B2 | FCF-positive proportion computed on 8 computable years, not 10 available years, lifting B2 one band | B2 = 4, Block B 13, core 69, class unchanged GOOD |
| F3 | MINOR | 01-gate0.md FCF table | FY2026 FCF 18.62 stated; 18.74 - 0.13 = 18.61 | cum FCF 181.15; B3 0.7053, no band change |
| F4 | MINOR | 01-gate0.md Block F, M11 | M11 = 5 not re-derivable: FY2020 and FY2023 revenue endpoints never shown; 0.44pp decision margin | if 0: moat 6, THIN, class still GOOD |
| F6 | MINOR | 07-emoat.md Section 3 / B07 completionist_recount | recount states 5 documented items, enumerates 4 | documented = 4 |
| F7 | MINOR | 07-emoat.md Family G, G1 | G1 zeroed by "constraint 2", which is in neither rule file | even raw 2: em_score 6, band NONE holds |
| F8 | MINOR | 07-emoat.md Optionality Register rows 3, 5 | conversion window given as "Unclear, no signal currently"; rule requires a realistic window | — |
| F9 | MINOR | 07-emoat.md Optionality Register rows 4, 5 | H3 and F1 rows registered though both scored above 0 on documented evidence; register scope is "scored 0 or claim/inference-only" | no double credit |
| F10 | MINOR | B07-emoat.yaml catalysts_12m[3], [5] | evidence_type "documented if it appears" is outside the three-value taxonomy; feeds Pillar 3 downstream | — |
| F12 | MINOR | B07-emoat.yaml evidence_mix | inference: 4 not enumerated anywhere in the report | no multiplier consequence |
| F13 | MINOR | B07-emoat.yaml analyst_note | "22 of 23 rows return NO EVIDENCE FOUND" contradicts the body's 20 of 23 | 20 of 23 |
| F11 | MINOR | prompts/07-emerging-moat-pipeline.md 6D | rule file names the eight combined-classification labels but defines no matrix cells; 6D output cannot be independently re-derived. Framework gap, not a stage defect; excluded from the acceptance denominator. | — |

## Rules that should have fired and did not
None found. All nine Gate 0 deal-breakers were tested against their own
thresholds and none was due. The classification matrix routed correctly. The
CAGR edge rules were checked and correctly reported as not applicable. The
completionist guard was not due at 3 active categories and was run anyway. The
I1 and I2 zero conditions fired exactly as written.

## Rules the reports claim to apply where the arithmetic disagrees
Two: F2 (B2's "as proportion" applied to a reduced denominator) and F6 (the
recount line's stated count against its enumerated items). Both are labelled
in the reports themselves; neither is concealed.

## Zeros checked against the rule and cleared
B4, E2, E3, M2, M5, M9, M12, I1, I2, R1 and every NO EVIDENCE FOUND row in the
22-category scan. In each case the rule file requires the treatment the report
gave, or the category's own definition is unmet on filed evidence. None is a
finding.

## Decision impact
No finding changes the Gate 0 classification (GOOD holds under every
recomputation above, including the stricter B2 reading and an M11 = 0 reading),
and no finding changes the Emerging Moat band (NONE holds up to em_score 6
against a 12 threshold). The one MAJOR finding is a downstream-consumption
risk in a boolean field, not an error in any score.

## Acceptance rate
Gate 0: 46 of 51 = 90.2%.
Emerging Moat: 40 of 47 = 85.1%.
Combined: **86 of 98 = 87.8%.** Above the 60% REWORK floor. F11 sits outside
the denominator as a framework-file gap.

---

```yaml
stage: B12c
company: "TAALTECH"
run_date: "2026-09-10"
model: claude-opus-4-8
status: complete
scope: "PHASE 1 ONLY — Gate 0 (B01) and Emerging Moat (B07). Valuation adherence deferred."
gate0:
  rules_checked: 51
  fails:
    - {id: "F5", severity: "MAJOR", rule: "Data confidence / history downgrade", location: "B01-gate0.yaml:21 + 01-gate0.md CLASSIFICATION", detail: "history_downgrade=true with data_years=10; the rule's only downgrade trigger is a 3-4 year history (10+ yrs = full). Classification correctly NOT downgraded, so the boolean and the classification contradict each other on the rule's own terms, and a machine consumer may apply an unauthorised GOOD->AVERAGE drop.", recomputed: "history_downgrade: false; comparability concern belongs in flags[]/data_notes, where it already also sits"}
    - {id: "F1", severity: "MINOR", rule: "FORMULA DEFINITIONS (fixed, do not substitute)", location: "01-gate0.md Block A preamble", detail: "ROCE denominator = Total Assets - 'Other Liabilities' (= equity + borrowings) instead of the mandated Total Assets - Current Liabilities.", recomputed: "FY2026 22.62% vs 22.54% reported; A1/A2 hold with wide margin, A4 already at floor 0; no block-score change demonstrable"}
    - {id: "F2", severity: "MINOR", rule: "B2 FCF-positive years as proportion", location: "01-gate0.md Block B", detail: "Proportion computed over 8 computable years (100%) rather than the 10 available years; FY2017 and FY2021 excluded from the denominator. Operating rule 5 scores unavailable data 0.", recomputed: "8/10 = 80% -> B2 = 4; Block B 13; core 69; grand total 80; classification unchanged GOOD"}
    - {id: "F3", severity: "MINOR", rule: "FCF = CFO - Capex", location: "01-gate0.md FCF table, FY2026 row", detail: "FY2026 FCF shown as 18.62; 18.74 - 0.13 = 18.61.", recomputed: "cumulative FCF 181.15; B3 = 0.7053; no band change"}
    - {id: "F4", severity: "MINOR", rule: "Operating rule 3, show every number extracted", location: "01-gate0.md Block F, M11", detail: "M11 = 5 rests on a 0.44pp gap (7.45% vs 7.01%) whose FY2020 and FY2023 revenue endpoints are never shown, so the test cannot be re-derived. Selling-expense leg substituted a 3-year-average comparison for the rule's 'declining'.", recomputed: "if M11 = 0: moat_score 6, moats_confirmed 1, moat_class THIN; classification still GOOD (Core 60-79 + else)"}
emoat:
  rules_checked: 47
  fails:
    - {id: "F6", severity: "MINOR", rule: "Completionist guard recount line", location: "07-emoat.md Section 3 + B07-emoat.yaml completionist_recount / evidence_mix", detail: "States '5 documented items' but enumerates 4; the fifth exists only by counting the same actuarial attrition assumption twice (standalone p.94 and consolidated p.146).", recomputed: "documented = 4; guard threshold is 12, no consequence"}
    - {id: "F7", severity: "MINOR", rule: "G1 war chest what-to-look-for list", location: "07-emoat.md Family G", detail: "G1 scored 0 citing 'constraint 2', an injected run constraint present in neither rule file, though debt-free status and internally funded capex are on the category's own list.", recomputed: "even raw 2 x 1.0 -> em_score 6; band NONE holds against the 12 threshold"}
    - {id: "F8", severity: "MINOR", rule: "Optionality register: realistic conversion window on every row", location: "07-emoat.md register rows 3 and 5 / B07-emoat.yaml optionality_register[2], [4]", detail: "Window column reads 'Unclear, no signal currently' on two of seven rows. Two watch items enter the monitoring checklist with no review date.", recomputed: ""}
    - {id: "F9", severity: "MINOR", rule: "Optionality register scope (scored 0 or claim/inference-only)", location: "07-emoat.md register rows 4 and 6 / B07-emoat.yaml optionality_register[3], [4]", detail: "H3 and F1 rows registered although both categories scored 1.0 on documented evidence. No double credit occurs (register items are never scored).", recomputed: ""}
    - {id: "F10", severity: "MINOR", rule: "Evidence taxonomy, three values only", location: "B07-emoat.yaml catalysts_12m[2] and [4]", detail: "evidence_type 'documented if it appears' is a conditional, not a tier. This field feeds Pillar 3 catalyst proximity downstream.", recomputed: ""}
    - {id: "F12", severity: "MINOR", rule: "Evidence taxonomy applied to every item", location: "B07-emoat.yaml evidence_mix", detail: "inference: 4 is never enumerated in the report, so the count is untraceable. No scoring consequence: no inference item was scored, so the 0.5x multiplier is nowhere in play.", recomputed: ""}
    - {id: "F13", severity: "MINOR", rule: "Internal consistency of block vs report", location: "B07-emoat.yaml analyst_note", detail: "'22 of 23 rows return NO EVIDENCE FOUND or the reverse' contradicts the body and the recount line, which both give 20 of 23 (C1, F1, H3 carry evidence).", recomputed: "20 of 23"}
valuation:
  status: "PENDING PHASE 3"
  rules_checked: 0
  fails: []
  note: "B10/B11 do not exist for this run. No Section 1B layer, Master Prompt Role 1, or FTTCP file was read. Verifier C rules 4, 6, 7, 9, 11, 12 not evaluated."
expectation_ledger:
  status: "PENDING PHASE 3"
  present: false
  downside_row: false
  all_rows_confirm_by: false
  all_rows_metric_threshold: false
  prob_in_range: false
  decay_status_valid: false
  off_ledger_credit: false
  residual_pct_cmp: 0
  residual_starter_cap_ok: true
  fails: []
  note: "Stage 11 artifact. Not in phase-1 scope; absence here is not a REWORK trigger."
business_understanding_narrative:
  status: "PENDING PHASE 3"
  present: false
  five_questions_answered: false
  prose_only: false
  section6_candidates_named: 0
  valuation_vocab_leak: false
  fails: []
  note: "Stage 13 artifact. Not in phase-1 scope; absence here is not a REWORK trigger."
stage7_categories_21_22: {present: true, cat21_score: 0, cat22_score: 0, both_legs_rule_applied: true, rework: false}
recomputed_destination_pe: ""
recomputed_decision: ""      # concur: Gate 0 GOOD and Emerging Moat NONE hold under every recomputation above
framework_gaps:
  - {id: "F11", severity: "MINOR", location: "prompts/07-emerging-moat-pipeline.md section 6D", detail: "The 'standard matrix' for combined classification names its eight output labels but defines no cells mapping backward class x forward class to a label. The stage's GOOD + NONE -> GOOD reading is reasoned but not independently re-derivable. Rule-file gap, not a stage defect; excluded from the acceptance denominator."}
findings:
  - {severity: "MAJOR", location: "B01-gate0.yaml:21 / 01-gate0.md CLASSIFICATION", description: "history_downgrade set true on a business-mix comparability concern; the field's only rule trigger is a 3-4 year history and TAALTECH has 10. Classification correctly stayed GOOD, so the boolean contradicts the classification and risks an unauthorised downstream one-tier drop."}
  - {severity: "MINOR", location: "01-gate0.md Block A preamble", description: "ROCE computed on Total Assets minus Other Liabilities instead of the mandated Total Assets minus Current Liabilities, under a formula heading that says do not substitute. FY2026 effect 0.08pp; no score change demonstrable."}
  - {severity: "MINOR", location: "01-gate0.md Block B, B2", description: "FCF-positive proportion taken over 8 computable years rather than 10 available years, lifting B2 from 4 to 5. Recomputed core score 69, classification unchanged."}
  - {severity: "MINOR", location: "01-gate0.md FCF table, FY2026", description: "FY2026 FCF stated 18.62 against 18.74 minus 0.13 = 18.61; cumulative FCF 181.15 not 181.16. No band change."}
  - {severity: "MINOR", location: "01-gate0.md Block F, M11", description: "M11 = 5 turns on a 0.44pp CAGR gap whose FY2020 and FY2023 revenue endpoints are never shown, so the scored test is not re-derivable from the report's own inputs. Classification is GOOD whether M11 is 5 or 0."}
  - {severity: "MINOR", location: "07-emoat.md Section 3 completionist recount", description: "Recount claims 5 documented items and enumerates 4; the fifth double-counts one actuarial assumption filed twice. evidence_mix.documented carries the same overcount."}
  - {severity: "MINOR", location: "07-emoat.md Family G, G1", description: "G1 scored 0 on 'constraint 2', a run constraint absent from both rule files, despite debt-free status and internally funded capex sitting on the category's own evidence list. Band NONE holds regardless."}
  - {severity: "MINOR", location: "07-emoat.md optionality register rows 3 and 5", description: "Two of seven register rows give 'Unclear, no signal currently' where the rule requires a realistic conversion window, so two watch items carry no review date into the monitoring checklist."}
  - {severity: "MINOR", location: "07-emoat.md optionality register rows 4 and 6", description: "H3 and F1 rows registered though both scored above zero on documented evidence; the register is defined for items that scored 0 or rest only on claim/inference evidence. No double credit results."}
  - {severity: "MINOR", location: "B07-emoat.yaml catalysts_12m entries 3 and 5", description: "evidence_type given as 'documented if it appears', outside the three-value evidence taxonomy, in a field that feeds Pillar 3 catalyst proximity."}
  - {severity: "MINOR", location: "B07-emoat.yaml evidence_mix", description: "inference: 4 is not enumerated anywhere in the report; the count cannot be traced to specific passages. No multiplier consequence, since no scored row rests on inference."}
  - {severity: "MINOR", location: "B07-emoat.yaml analyst_note", description: "Opens '22 of 23 rows return NO EVIDENCE FOUND or the reverse'; the body and the recount line both give 20 of 23. Cosmetic inconsistency."}
  - {severity: "MINOR", location: "prompts/07-emerging-moat-pipeline.md section 6D", description: "FRAMEWORK GAP, not a stage defect: the combined-classification 'standard matrix' names eight labels but defines no cells, so 6D output cannot be independently re-derived. Excluded from the acceptance denominator."}
critical_count: 0
major_count: 1
minor_count: 12
acceptance_rate: 88            # 86 of 98 phase-1 rule checks passed (gate0 46/51, emoat 40/47); F11 excluded as a rule-file gap
rework_triggered: false        # no CRITICAL, acceptance_rate above the 60% floor
```
