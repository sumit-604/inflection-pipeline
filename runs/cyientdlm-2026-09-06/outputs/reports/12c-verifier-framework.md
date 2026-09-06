# STAGE 12C: VERIFIER C — FRAMEWORK ADHERENCE AUDIT
Cyient DLM Ltd (CYIENTDLM) | Run date: 2026-09-06 | Model: claude-opus-4-8
Scope: PHASE 1 ONLY. Gate 0 (B01) and Emerging Moat (B07) compliance.
Valuation adherence (B10/B11) deferred to phase 3; stages 10 and 11 have not run.

Rule sources used:
- /home/user/inflection-pipeline/prompts/01-gate-0-pipeline.md
- /home/user/inflection-pipeline/prompts/07-emerging-moat-pipeline.md

Artifacts audited:
- outputs/reports/01-gate0.md + outputs/blocks/01-gate0.yaml
- outputs/reports/07-emoat.md + outputs/blocks/07-emoat.yaml

Ownership boundary honoured throughout: I audit rule application and judgment.
Whether a number exists in a source PDF at the cited anchor is Verifier A's call
alone. Where a figure looked odd to me, I say so as a framework question and hand
the source question to Verifier A.

---

## HEADLINE

Both stages applied their frameworks well. Every block total, the core score,
the moat score, the grand total, and the 23-row emerging-moat adjusted total
re-derive exactly from the reports' own stated inputs. No CRITICAL finding.
No finding changes either headline classification.

Two adherence issues carry real weight: one moat test scored into a band whose
stated condition was not met (Gate 0, M4), and one emerging-moat category scored
at the top of the matrix while the report itself states the advantage is not
emerging (B07, B2). One further Gate 0 item is not a defect but an
outcome-determining choice the operator should ratify: the declared 4-year
scoring window drives the history downgrade that turns AVERAGE into AVOID.

Findings: 0 CRITICAL, 3 MAJOR, 11 MINOR.
Framework adherence (Gate 0 + Emerging Moat scope): 87%.

---

# PART 1: GATE 0 (B01) COMPLIANCE

## 1.1 Re-derivation of every block score

I re-derived each line item from the report's own stated inputs against the
prompt's bands. Column "recomputed" is blank where I concur.

### Block A: Return on Capital (max 20)

| Test | Stated input | Prompt band | Report score | Recomputed | Verdict |
|---|---|---|---|---|---|
| A1 median ROCE | 13, 11, 11, 11.4 → median 11.2% | 10-14.9 = 1 | 1 | — | PASS |
| A2 min single-year ROCE | 11% | 8-11.9 = 1 | 1 | — | PASS |
| A3 median ROE | 16.04, 11.06, 7.33, 7.47 → median 9.27% | <12 = 0 | 0 | — | PASS |
| A4 ROCE trend | 11.4 vs 13.0 = −1.6pp | decline 1-3pp = 3 | 3 | — | PASS (window caveat, F-G01) |
| Subtotal | | | **5** | 5 | PASS |

Median of four values taken as the mean of the two middle values: A1 (11 + 11.4)/2
= 11.2, A3 (7.47 + 11.06)/2 = 9.265. Both correct.

ROE formula check: average net worth used as prompt requires. FY2024 (197.88 +
908.98)/2 = 553.43; FY2025 (908.98 + 949.44)/2 = 929.21; FY2026 (949.44 +
1,012.10)/2 = 980.77. FY2023 uses closing net worth with the exception stated, as
the prompt directs. All three quotients re-derive: 11.06%, 7.33%, 7.47%. PASS.

ROCE taken as source-provided and anchored, computation skipped, per the prompt's
explicit preference. PASS.

### Block B: Cash Generation Quality (max 20)

| Test | Stated input | Prompt band | Report score | Recomputed | Verdict |
|---|---|---|---|---|---|
| B1 cum CFO ÷ cum PAT | −25.07 ÷ 234.29 = −0.11 | <0.50 = 0 | 0 | — | PASS |
| B2 FCF-positive years | 1 of 3 = 33% | <50 = 0 | 0 | — | PASS |
| B3 cum FCF ÷ cum PAT | −207.47 ÷ 202.56 = −1.02 | <0.20 or negative = 0 | 0 | — | PASS |
| B4 change in WC days | 48 → 145 = +97 days | increased >15 = 0 | 0 | — | PASS on score, FAIL on basis (F-G03) |
| Subtotal | | | **0** | 0 | PASS |

Arithmetic re-derived: cumulative CFO 53.96 − 70.54 − 62.39 + 53.90 = −25.07.
Cumulative PAT 31.73 + 61.20 + 68.08 + 73.28 = 234.29. FCF FY24 −104.31, FY25
−112.40, FY26 +9.24, sum −207.47. Three-year PAT 202.56. All correct.

Missing FY2023 capex handled without estimation, which the prompt demands. The
report narrowed B2 and B3 to a matched 3-year window rather than scoring the
missing year 0. Under the prompt's own rule 5 route (N/A → 0), B2 would be 1 of 4
= 25%, still band 0. Score-invariant either way. PASS.

### Block C: Growth (max 20)

| Test | Stated input | Prompt band | Report score | Recomputed | Verdict |
|---|---|---|---|---|---|
| C1 revenue CAGR | (1,261.49/832.03)^(1/3) − 1 = 14.88% | 10-14.9 = 3 | 3 | — | PASS |
| C2 PAT CAGR | (73.28/31.73)^(1/3) − 1 = 32.18% | ≥20 = 5 | 5 | — | PASS |
| C3 positive YoY revenue years | 2 of 3 = 66.7% | 50-74 = 1 | 1 | — | PASS |
| C4 PAT CAGR − revenue CAGR | +17.3pp | ≥+3pp = 5 | 5 | — | PASS |
| Subtotal | | | **14** | 14 | PASS |

C1 sits one basis point below the band boundary (14.88% against the 15.0% line
into the 4-point band). I recomputed independently and confirm the 3-point band.
CAGR edge rules honoured: both endpoints positive on C1 and C2, no N/M case, no
loss-to-profit swing, and the absence of a swing is recorded in data_notes as the
prompt requires. PASS.

The report flags that FY2026 PAT growth contains a one-off earn-out reversal and
declines to re-score, on the ground that screener PAT is the fixed-formula input.
That is the correct call under the prompt: the formula is fixed and the
distortion belongs in data_notes, which is where it went. PASS, and the flag is
good practice.

### Block D: Balance Sheet Strength (max 20)

| Test | Stated input | Prompt band | Report score | Recomputed | Verdict |
|---|---|---|---|---|---|
| D1 net debt ÷ EBITDA | (172.27 − 125.80) ÷ 126.80 = 0.37x | 0-1.0x = 4 | 4 | — | PASS |
| D2 interest coverage | 120.33 ÷ 27.17 = 4.43x | 3-4.9 = 2 | 2 | — | PASS |
| D3 debt ÷ equity | 172.27 ÷ 1,012.10 = 0.17x | 0.1-0.5 = 4 | 4 | — | PASS |
| D4 current ratio | 12,223.01 ÷ 4,915.73 = 2.49x | ≥2.0 = 5 | 5 | — | PASS |
| Subtotal | | | **15** | 15 | PASS |

Net debt positive, so the "net cash = 5" band correctly not taken. EBIT built as
PBT + interest (93.16 + 27.17 = 120.33), consistent across D1 and D2. Consolidated
basis held across all four tests, with the standalone alternative for D4 disclosed
and rejected for consistency. That is the right discipline. PASS.

### Block E: Shareholder Alignment (max 20)

| Test | Stated input | Prompt band | Report score | Recomputed | Verdict |
|---|---|---|---|---|---|
| E1 promoter holding | 52.12% | 50-59.9 = 4 | 4 | — | PASS |
| E2 3-year change | not in corpus | N/A → 0 (rule 5) | 0 | — | PASS |
| E3 pledge | not in corpus | N/A → 0 (rule 5) | 0 | — | PASS |
| E4 contingent liabilities ÷ NW | nil = 0% | <5% = 5 | 5 | — | PASS |
| Subtotal | | | **9** | 9 | PASS |

E3 deserves explicit credit. The report found a CARO clause about the company's
own borrowing against subsidiary shares and correctly refused to read it as a
promoter-pledge disclosure. Absence of disclosure was scored 0, not 5. That is
exactly the grounded-claims rule applied against the report's own interest.
The professionally-managed alternative on E1 correctly not invoked: a promoter
(Cyient Limited) is identified.

### Block F: Quantitative Moat (max 60)

| Test | Stated input | Prompt band | Report score | Recomputed | Verdict |
|---|---|---|---|---|---|
| M1 pricing power | margin −0.50pp (stable ±2pp), rev CAGR 14.9% ≥10% | 3 | 3 | — | PASS |
| M2 cost advantage | no peer data | PEER DATA NEEDED → 0 | 0 | — | PASS |
| M3 capital efficiency | FAT 3.56x, ROCE 11.4% (<12%) | no band met → 0 | 0 | — | PASS |
| M4 customer stickiness | 1 decline year, unrecovered; RD +18.0 days | no band met | 1 | **0** | **FAIL (F-G02)** |
| M5 scale & dominance | no peer data | PEER DATA NEEDED → 0 | 0 | — | PASS |
| M6 technology / R&D | no R&D disclosure | else 0 | 0 | — | PASS |
| M7 regulatory / licence | no peer count | 0 | 0 | — | PASS |
| M8 distribution | B2B contract manufacture, no network | none = 0 | 0 | — | PASS |
| M9 brand | proxy GM stated, no peer median | PEER DATA NEEDED → 0 | 0 | — | PASS |
| M10 switching costs | growth all but 1 year, RD +18 days (not stable) | else 0 | 0 | — | PASS |
| M11 network effects | <6 years, conservative, stated | 0 | 0 | — | PASS |
| M12 negative WC / float | NWC days 48/79/127/145, all >45 | >45 = 0 | 0 | — | PASS |
| Subtotal | | | **4** | **3** | FAIL |

M4 is the one substantive scoring departure. The prompt's bands are: zero decline
years and receivable days stable ±10 = 5; max 1 decline year, fully recovered = 3;
2 decline years, CAGR positive = 1; 3+ decline years = 0. The company has one
decline year (FY2026, −17.0%) that is unrecovered because it is the terminal year,
and receivable days moved +18.0 days. The 3-band fails on "fully recovered". The
1-band's stated condition is "2 decline years", which is not the case here. The
report awarded 1 by analogy and labelled the move a judgment.

Two reasons this is a departure rather than an open judgment. First, the prompt
says "Apply the 12 moat tests exactly as specified". Second, the same report
applied the strict reading two tests later: M10 fails its 3-band on the identical
receivable-days leg and drops to 0 rather than to the 1-band by analogy. The
treatment is internally inconsistent, and the M4 direction is generous while the
M10 direction is strict.

Recomputed: Block F = 3/60, grand total = 46/160. Moats present at ≥3 is
unchanged at 1 (M1 only), so moat_class stays THIN and the classification is
untouched. MAJOR, not CRITICAL.

M11's conservative treatment is correct and explicitly stated, as the prompt
requires when fewer than 6 years exist. The four PEER DATA NEEDED marks are
correct and no peer figure was guessed anywhere. M9's proxy basis is stated, as
the prompt demands.

## 1.2 Totals, classification, deal-breakers

| Item | Report | My re-derivation | Verdict |
|---|---|---|---|
| Core score A+B+C+D+E | 43 | 5 + 0 + 14 + 15 + 9 = 43 | PASS |
| Moat score | 4 | 3 (after F-G02) | FAIL, MAJOR |
| Grand total | 47 | 46 (after F-G02) | FAIL, MAJOR |
| Moats confirmed (≥3) | 1 | 1 (M1) | PASS |
| Moat class (1 present) | THIN | THIN | PASS |
| Classification band (core 40-59) | AVERAGE | AVERAGE | PASS |
| Data confidence (4 years) | LIMITED | LIMITED | PASS |
| history_downgrade | true, one tier | AVERAGE → AVOID | PASS |
| Final classification | AVOID | AVOID | PASS |

Deal-breaker application, all nine evaluated:

| # | Rule | Report | Verdict |
|---|---|---|---|
| 1 | Block A <8 → max GOOD | triggered (A=5), no incremental effect | PASS |
| 2 | Block B <8 → max GOOD | triggered (B=0), no incremental effect | PASS |
| 3 | median ROCE <10% → max AVERAGE | not triggered (11.2%) | PASS |
| 4 | cum CFO/PAT <0.50 → max AVERAGE | triggered (−0.11), driver years FY24/FY25 named | PASS |
| 5 | pledge >15% → max AVERAGE | not evaluable, stated unresolved | PASS |
| 6 | ND/EBITDA >3x AND IC <3x → AVOID | not triggered (0.37x) | PASS |
| 7 | revenue declined in majority of years | not triggered (1 of 3) | PASS |
| 8 | PAT negative in last 3 years | not triggered | PASS |
| 9 | history <3 years → AVERAGE | not triggered (4 years) | PASS |

The prompt's instruction to "state WHICH years drive any deal-breaker" is
honoured on #4 in the report body, in the deal-breaker section and in the block.
Good compliance.

Order of operations: matrix band → deal-breaker cap → confidence downgrade. The
prompt does not fix the order. The report's order is the natural reading and no
alternative order produces a different label here (the cap is at AVERAGE and the
downgrade takes AVERAGE to AVOID either way). Not a finding.

## 1.3 The window question (F-G01, MAJOR)

The report declares a 4-year window (FY2023 to FY2026) and states the reason:
full financial statements exist only for those years in the corpus. It then
discloses, twice and unprompted, that the company's own KPI chart carries ROCE
back to FY2022 (18%) and FY2021 (11%), and that A4 scored on the fuller series
would be 0, not 3.

I do not rule the maker wrong. Reading rule 6's "maximum whatever exists" as
maximum full-financial history is defensible, and blocks B, D and E cannot be
scored on a partial KPI chart. The disclosure is complete and honest.

The issue is that the declaration is outcome-determining and no one has ratified
it. Declared at 4 years, data confidence is LIMITED and a one-tier downgrade
fires, taking AVERAGE to AVOID. Declared at 5 years, the confidence tier becomes
"5-6 lower, flag may not have seen full cycle", which carries no downgrade, and
the classification would stand at AVERAGE even after A4 falls to 0 (core 40, still
inside the 40-59 band).

So the single most visible output of this stage, AVOID against AVERAGE, rests on
a window declaration the prompt leaves ambiguous for partial series. That deserves
an operator ruling before the classification is carried forward. MAJOR, with the
explicit note that the maker disclosed the sensitivity rather than hiding it.

## 1.4 Formula and presentation checks

| Rule | Verdict | Note |
|---|---|---|
| Opening "Data available: X years (FY__ to FY__)" line | PASS | present, with basis added |
| Anchors on extracted numbers | PASS | dense; per-line anchors thin in Block C/D but the input series above each block is anchored. Anchor-to-source truth is Verifier A's call |
| Grounded claims, N/A → 0, never estimate | PASS | E2, E3, FY2023 capex all handled correctly |
| ROCE source-provided rule | PASS | used and stated |
| ROE average net worth + earliest-year exception | PASS | |
| WC days = RD + ID − PD | **FAIL, MINOR (F-G03)** | company-disclosed NWC-days KPI substituted for B4 and M12 |
| FCF = CFO − capex, acquisitions excluded | PASS | FY2025 acquisition outflow correctly excluded |
| CAGR formula and edge rules | PASS | |
| Dashboard output elements (blocks, bars, classification, strongest/weakest, decision line) | PASS | all present |
| YAML schema complete, matches report | PASS | every field populated, block values tie to the report |
| FLAG-GATE0 condition (classification ≤ AVERAGE with depressors) | PASS | correctly fired with depressors named |
| analyst_note ≤200 words | PASS | roughly 140 words |
| M4 cross-reference "see analyst_note" | **FAIL, MINOR (F-G04)** | analyst_note does not discuss M4 |

On F-G03: the prompt marks its formula definitions "fixed, do not substitute
alternatives", and B4 and M12 both use the company's NWC-days KPI instead. The
substitution is disclosed with its reason (trade payables unavailable for all four
years), and it is score-invariant: the AR MD&A DSO/DIO/DPO route gives FY2024 104
days and FY2025 148 days, which lands in the same B4 band (increase >15 → 0) and
the same M12 band (>45 → 0). The prompt's own missing-data route (N/A → 0) also
gives 0. No band moves, so MINOR rather than MAJOR.

Minor observation, not scored as a finding: the classification section attributes
the position-sizing override language to CLAUDE.md. That sentence is in the Gate 0
prompt itself, at the deal-breaker note. Harmless.

## 1.5 Gate 0 tally

62 rules checked. 4 fails: 2 MAJOR (F-G01 window sensitivity, F-G02 M4 band),
2 MINOR (F-G03 WC-days basis, F-G04 dangling cross-reference).
Gate 0 rule pass rate: 58/62 = 94%.

Recomputed classification: AVOID, concur.
Recomputed grand total: 46/160 against the reported 47/160.

---

# PART 2: EMERGING MOAT (B07) COMPLIANCE

## 2.1 Category completeness

All 22 categories plus R1 are addressed, none skipped, none force-fitted. Roll
call against the prompt's families:

- Family A: A1, A2, A3, A4 — all four present. A2 explicit NO EVIDENCE FOUND.
- Family B: B1, B2, B3 — present. B3 explicit NO EVIDENCE FOUND.
- Family C: C1, C2 — present.
- Family D: D1, D2 — both explicit NO EVIDENCE FOUND.
- Family E: E1, E2 — present. E1 explicit NO EVIDENCE FOUND.
- Family F: F1, F2 — present. F2 cross-references the injected B05
  promise-delivery record as the prompt requires.
- Family G: G1, G2 — present.
- Family H: H1, H2, H3 — present.
- Family I: I1, I2 — present, both scored 0 with reasoning.
- R1 — present, worked in Section 4.

Count = 23 scored rows in both the Section 3 summary table and the Section 5
scorecard. PASS.

Section coverage: all six sections executed plus the optionality register. 1A/1B/1C,
2A/2B/2C/2D, Section 3 with the summary table, 4A/4B/4C, Section 5 with the
classification, and 6A through 6E. PASS.

## 2.2 Scorecard re-derivation

Matrix per the prompt: HH=4, HM/MH=3, HL/MM/LH=2, ML/LM=1, LL=1, no evidence=0.
Multipliers: 📄 1.0x, 🎙️ 0.7x, 🔍 0.5x.

| # | Matrix code | Raw stated | Raw per matrix | Tier | Multiplier | Adjusted | My check |
|---|---|---|---|---|---|---|---|
| A1 | MM | 2 | 2 | 🎙️ | 0.7 | 1.4 | ✓ |
| A2 | — | 0 | 0 | — | — | 0 | ✓ |
| A3 | LL | 1 | 1 | 🎙️ | 0.7 | 0.7 | ✓ |
| A4 | LM | 1 | 1 | 🎙️ | 0.7 | 0.7 | ✓ |
| B1 | MM | 2 | 2 | 📄 | 1.0 | 2.0 | ✓ |
| B2 | HH | 4 | 4 | 📄 | 1.0 | 4.0 | ✓ arithmetic, see F-E01 |
| B3 | — | 0 | 0 | — | — | 0 | ✓ |
| C1 | HM | 3 | 3 | 🎙️ | 0.7 | 2.1 | ✓ |
| C2 | HL | 2 | 2 | 📄 | 1.0 | 2.0 | ✓ |
| D1 | — | 0 | 0 | — | — | 0 | ✓ |
| D2 | — | 0 | 0 | — | — | 0 | ✓ |
| E1 | — | 0 | 0 | — | — | 0 | ✓ |
| E2 | MM | 2 | 2 | 🎙️ | 0.7 | 1.4 | ✓ |
| F1 | ML | 1 | 1 | 📄 | 1.0 | 1.0 | ✓ |
| F2 | — | 0 | 0 | — | — | 0 | ✓ |
| G1 | ML | 1 | 1 | mixed → 0.7 | 0.7 | 0.7 | ✓ conservative |
| G2 | — | 0 | 0 | 📄 | — | 0 | ✓ |
| H1 | — | 0 | 0 | — | — | 0 | ✓ |
| H2 | — | 0 | 0 | — | — | 0 | ✓ |
| H3 | HL | 2 | 2 | 📄 | 1.0 | 2.0 | ✓ |
| I1 | — | 0 | 0 | — | — | 0 | ✓ |
| I2 | — | 0 | 0 | — | — | 0 | ✓ |
| R1 | HM | 3 | 3 | 📄 | 1.0 | 3.0 | ✓ |

Every matrix code maps to the prompt's stated raw value. Every multiplier matches
the stated tier. Sum re-derived: 1.4 + 0.7 + 0.7 + 2.0 + 4.0 + 2.1 + 2.0 + 1.4 +
1.0 + 0.7 + 2.0 + 3.0 = **21.0**. The report's 21.0 is correct.

Classification: 21 falls in 12-24 → MODEST MOAT DEVELOPMENT. Correct against the
prompt's absolute bands (≥40 EXPANSION, 25-39 STRENGTHENING, 12-24 MODEST, <12
NONE). No rescale attempted, ceiling correctly stated as 92 with I1/I2. The
"EM ≥25" UA qualifier is correctly reported as not met, and the block carries it
explicitly as ua_qualifier_met: false. PASS.

I1/I2 contribution stated separately as 0.0, which the 20-Aug-2026 operator ruling
requires for the review checkpoint. PASS.

## 2.3 Evidence taxonomy applied to the prompt's standard

Tier assignments checked item by item against the prompt's definitions
(📄 = capex committed, patent filed, contract signed, plant under construction,
product launched, regulatory application submitted; 🎙️ = stated in call or deck,
not backed by committed capital or signed contracts; 🔍 = inference from data
patterns).

Correctly tiered and conservative:
- A1 carries both a 📄 certification list and a 🎙️ rarity claim, and is scored at
  0.7x on the claim leg. The conservative choice is the right one, since the
  scored proposition (rarity) is the unquantified one.
- C1 mentions a "📄-adjacent" balance sheet item but is still scored 0.7x as a
  claim. Conservative, correct.
- G1 is mixed and scored 0.7x. Conservative, correct.
- C2, F1, H3 rest on audited notes and BRSR disclosures, scored 1.0x. Correct.
- R1 rests on certifications actually received (IATF16949 letter of confirmation,
  NADCAP audit completed), which is squarely inside the 📄 definition. Correct.
- The report refuses to credit PLI/ECMS at company level because no
  company-specific enrolment is disclosed, and says so explicitly in 4B. That is
  the taxonomy applied against the report's own interest. Good.
- The dropped automotive/EV item is tracked as "🎙️ then quietly dropped" rather
  than being carried as pipeline. Good discipline.

Borderline but acceptable: B1 at 📄 rests on the AR sentence "procured critical
components in advance and secured long-term vendor commitments". The venue is a
filed report and the action is stated as completed, so 📄 holds. Had it been
tiered 🎙️, the adjusted score would fall from 2.0 to 1.4 and the total from 21.0
to 20.4, with no band change. Not scored as a finding.

Taxonomy gap (F-E03): the 🔍 ANALYST INFERENCE tier is never used anywhere in the
report, and evidence_mix reports inference: 0. The report does make inferences and
labels them as such in prose (the C2 Altek-consolidation artifact reading, the
base-rate argument in 6E, the "utilisation story not capex story" conclusion in
2C). The prompt says the taxonomy applies "to every single piece of evidence".
Tagging those as 🔍 would not move any score, because the categories they touch
are already scored on their 📄 or 🎙️ legs, but the mix counts are understated.
MINOR.

Related, F-E09: evidence_mix reports claim: 22 items. The report enumerates its
13 documented items but never enumerates or reconciles the 22 claim items, so the
figure cannot be checked from the artifact. MINOR, completeness only.

## 2.4 Completionist guard

The prompt requires the recount line in a fixed form and requires the analyst to
re-examine at 12 or more active categories.

The recount was performed and the 13 documented items are individually named,
which is exactly what the guard asks for. That is good practice and rare.

F-E04, MINOR: the mandated line reads "13 documented items ... across 6
categories (B1, B2, C2, F1, G2, H3, R1 ...)". The parenthetical names seven
categories, and the block's completionist_recount field says seven. The stated
count of 6 contradicts both. The report's justification ("B2 and R1 share the
certification evidence base") explains an overlap in evidence but does not reduce
the category count. No score effect.

Observation, not scored as a finding: 12 of 23 rows carry a non-zero adjusted
score. Read as "12 or more categories active", that is exactly the guard's
trigger. Read against the prompt's own definition of active_categories
("only Strong/Moderate rows"), the count is 4, comfortably inside the 3-6 base
rate. The report asserts "the scan did not need to be re-examined for
over-crediting", which is only true on the second reading. The guard's required
action, the 📄 recount, was performed either way, and the eight weak rows are all
🎙️ at 0.7x, which is the discount the guard exists to enforce. Substantively
compliant. Flagged so the operator sees the ambiguity.

## 2.5 The B2 question (F-E01, MAJOR)

This is my one substantive emerging-moat finding.

The stage's own definition, stated in the prompt's first line of standing
instruction, is "EMERGING competitive advantages: moats currently FORMING that do
not fully show in historical financials yet but could become significant within
1-5 years".

B2 (qualification lock-in) is scored HH = 4 raw at 1.0x, giving 4.0, the single
largest row in the scorecard and 19% of the total. The report then states, in
6D: "The one genuinely strong category found (B2, qualification lock-in) is a
real, durable structural feature, but it is not new or forming — the
certifications and long customer relationships behind it predate this filing
year." Section 6E repeats it: "existing qualification-cert stack (STRONG, but not
'emerging' — it predates FY26)".

So the scan's top-scoring row is expressly described by the scan itself as not
emerging. Under the prompt's definition, what belongs in this scan is the
incremental new evidence, which is the FY26 IATF16949 confirmation and the NADCAP
cable-harness re-scope. Those are already scored, separately, at R1 = 3.0. The
report acknowledges the overlap in its own recount line ("B2 and R1 share the
certification evidence base"), which is the double-credit pattern the operation's
standing rule against crediting one improvement through two mechanisms exists to
prevent.

Recomputation. Score B2 on the emerging increment only, at HM = 3 × 1.0 = 3.0,
and the total falls from 21.0 to 20.0. Remove B2 entirely as a pre-existing
advantage and the total falls to 17.0. Both stay inside the 12-24 MODEST band, and
both stay below the EM ≥25 UA qualifier. Classification and UA outcome unchanged,
so MAJOR, not CRITICAL.

Worth saying plainly: the report is not hiding anything here. It names the tension
in three places and its narrative conclusion is the conservative one. The defect
is that the scorecard and the narrative disagree, and the scorecard is the field
that travels downstream in em_score.

## 2.6 I1 and I2

| Rule | Verdict |
|---|---|
| Category 21 (I1) present | PASS |
| I1 scored above 0 only if both legs evidenced, (b) leg with ≥1 📄 | PASS, scored 0, both legs found absent and named |
| Category 22 (I2) present | PASS |
| I2 scored above 0 only if the sacrifice is specific | PASS, scored 0 |
| I2 answered "for each moat claimed anywhere in this scan" | **FAIL, MINOR (F-E06)** |

I1's reasoning is exactly what the operator ruling asks for: it checks for named
inventors on patent filings (none exist, since no patents exist), ex-DRDO/ex-HAL
concentration (not disclosed), and the remuneration annexure against sector norms
(no benchmarking disclosed), then scores 0 because neither leg is evidenced. Clean.

I2 is well reasoned. The report answers the sacrifice question for B2, concludes
"nothing needs to be destroyed", correctly classifies the certification barrier as
an entry-cost and time barrier rather than a configuration sacrifice, and uses the
CFO's own words to confirm the framing. It then confirms no PSU-rigidity or
incumbent-institutional-relationship argument exists for any named competitor.

The departure is procedural: the prompt says "For each moat claimed anywhere in
this scan, answer...", and the report explicitly answers for one (B2). C1, C2 and
R1 are not run through the test individually. The generalising sentence covers the
field in substance and the score would remain 0, so MINOR.

## 2.7 Sections 1, 2, 4, 6 and the register

| Rule | Verdict | Note |
|---|---|---|
| 1A pipeline table with status, evidence type, launch, revenue potential, differentiation | PASS | all columns present; NOT FOUND used where undisclosed |
| 1B diversification with evidence and timeline | PASS | four directions covered |
| 1C mix shift with current %, expected % in 3 years, margin direction, profit impact | PASS | the 3-year % column is NOT FOUND and said so; margin bands substituted with the gap named, not estimated |
| 2A capex table, all seven columns | PASS | NOT FOUND fills throughout, no estimates |
| 2B utilisation trajectory | PASS | single point 50-60% disclosed, absence of facility/quarter detail stated |
| 2C arithmetic shown | PASS | numerator NOT FOUND, computation declared impossible, no estimate; capex_embedded_growth_pct set 0 with an explanatory note |
| 2D new geography | PASS | |
| 4A approvals with body, status, timeline, unlock, competitor holding | PASS | competitor holding marked NOT FOUND |
| 4B policy tailwinds with amounts, duration, enrolment status, competitor sharing | PASS | industry-level vs company-level distinction drawn explicitly and correctly |
| 4C regulatory moat assessment (active vs emerging, time, sustainability) | PASS | |
| Optionality register, four columns, rows that scored 0 or rest on 🎙️/🔍 | PASS | 9 rows, all qualify |
| Register carried in the block | **FAIL, MINOR (F-E07)** | 9 rows in the report, 8 in optionality_register[]; the "rung-jump via B2S" row is dropped |
| 6A timeline across four windows | PASS | |
| 6B risks with early-warning signs | PASS | per top-scoring category |
| 6C combined table using the injected B01 block | PASS | core 43, moat_score 4, moats_confirmed 1, THIN, AVOID all tie to the B01 YAML |
| 6D combined classification from the allowed label set, with the transition-setup reminder addressed | PASS | AVOID, and the GOOD/AVERAGE-backward-plus-EXPANSION-forward case is explicitly considered and ruled out |
| 6E output card: evolution map, 12m catalysts, biggest risk | PASS | |

On F-E07: the prompt says the register is carried in the block and that synthesis
merges register items into the monitoring checklist. A dropped row is a lost watch
item. The dropped row (sustained double-digit B2S revenue % for two consecutive
quarters tied to a named mass-production order) overlaps substantially with the
carried B2S/transform-phase row, which is why this is MINOR rather than MAJOR.

## 2.8 Presentation and block schema

| Rule | Verdict | Note |
|---|---|---|
| Section 3: evidence table or NO EVIDENCE FOUND per category | **FAIL, MINOR (F-E02)** | prose paragraphs per category; the 23-row summary table compensates |
| Source anchors on every evidence item | **FAIL, MINOR (F-E05)** | dense overall, but a few items unanchored: H2 "related-party term loan structure, AR consolidated notes" (no page), G1 same note reference |
| Strength labels from Strong / Moderate / Weak / None | **FAIL, MINOR (F-E08)** | "Weak-Moderate" (B1), "None (negative)" (F2, G2), "Moderate (artifact-caveated)" (C2 in the block) |
| Count with Strong/Moderate stated | PASS | 4 (B2, C1, C2, R1) |
| active_categories carries only Strong/Moderate rows | PASS | B1 at "Weak-Moderate" correctly excluded |
| "end with exactly this fenced YAML block" | **FAIL, MINOR (F-E10)** | five fields outside the schema: em_score_scale, ua_qualifier_threshold, ua_qualifier_met, capex_embedded_growth_note, orchestrator_note |
| catalysts_12m with anchors | PASS | four entries, each anchored |
| analyst_note ≤200 words | PASS | roughly 130 words |
| combined_assessment, combined_reasoning, top_moat_risks populated | PASS | |

F-E08 matters slightly beyond cosmetics because "Weak-Moderate" sits on the
boundary of the Strong/Moderate count that feeds active_categories. The report
resolved it the conservative way (excluded B1). Noted for consistency, not for
outcome.

F-E10: the extra fields are informative and none contradicts the schema. The risk
is only to a strict downstream parser.

## 2.9 Emerging Moat tally

44 rules checked. 10 fails: 1 MAJOR (F-E01 B2 scored as emerging), 9 MINOR.
Emerging Moat rule pass rate: 34/44 = 77%.

Recomputed em_score: 17.0 to 20.0 depending on the B2 treatment, against the
reported 21.0. Classification MODEST either way. UA qualifier not met either way.
Recomputed classification: MODEST, concur.

---

# PART 3: VALUATION ADHERENCE

NOT RUN. Stages 10 and 11 have not executed in this phase; B10 and B11 do not
exist as artifacts. The valuation framework documents (Master Prompt v3.6 Role 1,
the Section 1B layer set, FTTCP v2.1) were deliberately not loaded, per the
phase-1 scoping rule in my instruction file. Deferred to phase 3.

Also out of scope in phase 1 and therefore not assessed: the Business
Understanding Narrative check (stage 13), the Halt 1 dossier structural check
(B09b), the downstream signal candidate check (B09) and the method plurality
check (B11).

---

# PART 4: CONSOLIDATED FINDINGS

| ID | Severity | Location | Description |
|---|---|---|---|
| F-G01 | MAJOR | B01 report, "Data available" line and Classification section | The declared 4-year scoring window is outcome-determining and unratified. At 4 years the LIMITED confidence tier fires a one-tier downgrade, turning AVERAGE into AVOID. At 5 years (the company's own ROCE series reaches FY2022) the tier carries no downgrade and the classification would be AVERAGE even with A4 falling to 0 (core 40, still in the 40-59 band). The report discloses the A4 sensitivity but never runs the confidence-tier consequence. The choice is defensible under rule 6 read as full-financial history; it needs an operator ruling before AVOID travels downstream. |
| F-G02 | MAJOR | B01 report, Block F, M4 | M4 scored 1 where no prompt band is satisfied. One decline year, unrecovered, fails the 3-band ("fully recovered"); the 1-band's stated condition is "2 decline years". Score awarded by analogy while M10 two tests later applies the strict else-0 reading on the identical receivable-days leg. Recomputed: Block F 3/60, grand total 46/160. Moats confirmed, moat class and classification unchanged. |
| F-G03 | MINOR | B01 report, B4 and M12 | The prompt's fixed formula (Receivable + Inventory − Payable days) was replaced by the company-disclosed NWC-days KPI, against "fixed, do not substitute alternatives". The substitution is disclosed with cause (payables unavailable), and is score-invariant: the MD&A DSO/DIO/DPO route (FY24 104, FY25 148) lands in the same B4 and M12 bands, as does the prompt's own N/A → 0 route. |
| F-G04 | MINOR | B01 report, M4 | The M4 line says "judgment flagged; see analyst_note". The analyst_note does not mention M4. Dangling cross-reference on the one line item that most needed the explanation. |
| F-E01 | MAJOR | B07 Section 5 scorecard, row B2 | B2 is scored HH = 4 at 1.0x, the largest row in the scan, while the report itself states in 6D and 6E that the advantage predates FY26 and is "not emerging". The stage's definition covers moats currently FORMING. The genuinely new increment (IATF16949, NADCAP re-scope) is already scored at R1 = 3.0, and the report's own recount line concedes "B2 and R1 share the certification evidence base", which is one improvement credited through two mechanisms. Recomputed em_score 20.0 (B2 rescored on the increment) or 17.0 (B2 removed), against 21.0 reported. MODEST band and the EM ≥25 UA miss hold in every case. |
| F-E02 | MINOR | B07 Section 3 | The prompt asks for an evidence table or NO EVIDENCE FOUND per category. Categories are presented as anchored prose. The 23-row summary table supplies the required structure, so the loss is presentational. |
| F-E03 | MINOR | B07 throughout; block evidence_mix | The 🔍 ANALYST INFERENCE tier is never applied, and evidence_mix reports inference: 0, although the report makes and labels inferences in prose (C2 consolidation artifact, 2C utilisation-not-capex conclusion, 6E base-rate argument). The taxonomy is meant to be applied to every piece of evidence. No score effect. |
| F-E04 | MINOR | B07 Section 3, completionist recount line | The mandated line states "13 documented items ... across 6 categories" then names seven (B1, B2, C2, F1, G2, H3, R1). The block says seven. The stated count contradicts its own list and the block. |
| F-E05 | MINOR | B07 H2 and G1 | A few evidence items carry no page anchor ("related-party term loan structure, AR consolidated notes"). The prompt requires an anchor on every evidence item. Whether the referenced content exists at any page is Verifier A's call, not mine. |
| F-E06 | MINOR | B07 Section 3, I2 | The prompt requires the cannibalization test to be answered "for each moat claimed anywhere in this scan". It is answered for B2 only; C1, C2 and R1 are covered by a generalising sentence rather than individually. Score would remain 0 in each case. |
| F-E07 | MINOR | B07 optionality register against block optionality_register[] | Nine rows in the report table, eight in the block. The "rung-jump: converter-to-value-added-supplier via B2S" row is not carried. The prompt states the register is carried in the block and merged into the monitoring checklist, so the row is lost to synthesis. Content overlaps the carried B2S transform-phase row. |
| F-E08 | MINOR | B07 Section 3 summary table and block | Strength labels depart from the prompt's Strong / Moderate / Weak / None set: "Weak-Moderate", "None (negative)", "Moderate (artifact-caveated)". The boundary case (B1 at "Weak-Moderate") was resolved conservatively and excluded from active_categories, so no outcome effect. |
| F-E09 | MINOR | B07 block, evidence_mix | claim: 22 is not enumerated or reconcilable from the report body, unlike documented: 13, which is itemised. Cannot be checked from the artifact. |
| F-E10 | MINOR | B07 block | The prompt says "end with exactly this fenced YAML block". Five fields sit outside the schema: em_score_scale, ua_qualifier_threshold, ua_qualifier_met, capex_embedded_growth_note, orchestrator_note. All informative, none contradictory; risk is only to a strict parser. |

## What I checked and did not fault

Worth recording, because a findings list alone reads harsher than the artifacts
deserve:

- Every block subtotal, the core score, the moat score, the grand total and the
  23-row adjusted total re-derive exactly from the reports' own stated inputs.
  The only arithmetic difference I carry is the consequence of F-G02.
- Both reports refuse to estimate. FY2023 capex, promoter pledge, promoter
  holding history, peer medians, capex rupee figures, the 3-year revenue mix and
  company-specific PLI enrolment are all NOT FOUND or N/A, never filled.
- The four PEER DATA NEEDED marks are correct and no peer figure is guessed.
- Gate 0 scores E3 at 0 for absence of pledge disclosure rather than assuming
  0% pledge. That is the grounded-claims rule applied against the report's own
  interest.
- Gate 0 flags the FY2026 one-off earn-out reversal inside C2/C4 and correctly
  declines to re-score a fixed-formula input, routing the distortion to
  data_notes instead.
- B07 refuses to credit the PLI/ECMS narrative at company level, refuses to read
  consolidated customer concentration as organic diversification, and scores F2
  and G2 at 0 with active negative evidence named rather than as mere absence.
- B07's I1 and I2 both score 0 with the operator ruling's two-leg tests applied
  as written.
- Both blocks' YAML values tie to their report bodies field by field, except
  where recorded in F-E04 and F-E07.

## Tally

| Scope | Rules checked | Passed | Fails | Rate |
|---|---|---|---|---|
| Gate 0 (B01) | 62 | 58 | 4 | 94% |
| Emerging Moat (B07) | 44 | 34 | 10 | 77% |
| Valuation (B11) | 0 | 0 | 0 | pending, phase 3 |
| **Total in scope** | **106** | **92** | **14** | **87%** |

CRITICAL 0 | MAJOR 3 | MINOR 11.
No REWORK trigger from this verifier: no CRITICAL, and the acceptance rate is
above 60% in both scopes and in aggregate.

Recomputed classifications: Gate 0 AVOID (concur), Emerging Moat MODEST (concur).
Recomputed numbers carried: Gate 0 grand total 46/160 against 47/160 reported;
B07 em_score 17.0-20.0 against 21.0 reported. Neither moves a band.

---

```yaml
stage: B12c
company: "CYIENTDLM"
run_date: "2026-09-06"
model: claude-opus-4-8
status: complete
scope: "phase-1: Gate 0 (B01) and Emerging Moat (B07) only"
gate0:
  rules_checked: 62
  rules_passed: 58
  acceptance_rate: 94
  recomputed_core_score: 43        # concur
  recomputed_moat_score: 3         # reported 4, see F-G02
  recomputed_grand_total: 46       # reported 47
  recomputed_classification: "AVOID"   # concur
  fails:
    - "F-G01 MAJOR: 4-year window declaration is outcome-determining (LIMITED tier downgrade turns AVERAGE into AVOID); disclosed but unratified"
    - "F-G02 MAJOR: M4 scored 1 with no prompt band satisfied; strict reading gives 0, Block F 3/60, grand total 46/160"
    - "F-G03 MINOR: B4 and M12 substitute the company NWC-days KPI for the prompt's fixed WC-days formula; disclosed, score-invariant"
    - "F-G04 MINOR: M4 cross-reference to analyst_note is dangling; analyst_note does not discuss M4"
emoat:
  rules_checked: 44
  rules_passed: 34
  acceptance_rate: 77
  categories_addressed: 23
  categories_required: 23
  arithmetic_verified: true
  recomputed_em_score: "17.0 to 20.0"   # reported 21.0, see F-E01
  recomputed_classification: "MODEST"   # concur
  ua_qualifier_met: false               # concur, EM 25 threshold not met on any recomputation
  fails:
    - "F-E01 MAJOR: B2 scored HH=4 as the top row while the report states it predates FY26 and is not emerging; certification evidence shared with R1=3.0"
    - "F-E02 MINOR: Section 3 uses prose per category, not the evidence table the prompt asks for"
    - "F-E03 MINOR: analyst-inference tier never applied; evidence_mix inference count 0 despite inferences in the text"
    - "F-E04 MINOR: completionist recount line says 6 categories, names 7, block says 7"
    - "F-E05 MINOR: a few evidence items carry no page anchor (H2, G1 related-party note)"
    - "F-E06 MINOR: I2 answered for B2 only, not for each moat claimed in the scan"
    - "F-E07 MINOR: optionality register has 9 rows in the report, 8 in the block; rung-jump row dropped"
    - "F-E08 MINOR: strength labels outside the Strong/Moderate/Weak/None set"
    - "F-E09 MINOR: evidence_mix claim count of 22 not enumerated or reconcilable from the report"
    - "F-E10 MINOR: block carries five fields outside the mandated schema"
valuation:
  status: pending
  reason: "Stages 10 and 11 have not run; B10 and B11 do not exist. Valuation adherence audit deferred to phase 3 of this pipeline. Master Prompt v3.6, the Section 1B layer set and FTTCP v2.1 were deliberately not loaded, per the phase-1 scoping rule."
  rules_checked: 0
  fails: []
business_understanding_narrative:
  status: not_applicable_phase_1
  reason: "Stage 13 has not run; the narrative check belongs to the phase-3 or finalize verifier pass."
  present: false
  five_questions_answered: false
  prose_only: false
  section6_candidates_named: 0
  valuation_vocab_leak: false
  fails: []
recomputed_destination_pe: ""   # out of scope in phase 1
recomputed_decision: ""         # concur on both in-scope classifications: Gate 0 AVOID, Emerging Moat MODEST
findings:
  - {severity: "MAJOR", location: "B01 report, data-availability declaration and Classification section", description: "The declared 4-year scoring window is outcome-determining and unratified. At 4 years the LIMITED confidence tier fires a one-tier downgrade that turns AVERAGE into AVOID. The company's own ROCE series reaches FY2022, and on a 5-year declaration the tier carries no downgrade, leaving AVERAGE even with A4 falling to 0 (core 40, still inside 40-59). The report discloses the A4 sensitivity but never runs the confidence-tier consequence. The reading is defensible under rule 6 taken as full-financial history; it needs an operator ruling before AVOID travels downstream."}
  - {severity: "MAJOR", location: "B01 report, Block F, test M4", description: "M4 scored 1 where no prompt band is satisfied. One revenue-decline year, unrecovered, fails the 3-band condition 'fully recovered', and the 1-band's stated condition is '2 decline years'. Score awarded by analogy, while M10 two tests later applies the strict else-0 reading on the identical receivable-days leg. Recomputed Block F 3/60 and grand total 46/160; moats confirmed, moat class THIN and classification AVOID all unchanged."}
  - {severity: "MAJOR", location: "B07 Section 5 scorecard, row B2", description: "B2 qualification lock-in is scored HH=4 at 1.0x, the largest single row, while the report states in 6D and 6E that the advantage predates FY26 and is not emerging. The stage scores moats currently forming. The genuinely new increment (IATF16949, NADCAP cable-harness re-scope) is already scored at R1=3.0, and the report's own recount concedes B2 and R1 share the certification evidence base, which credits one improvement through two mechanisms. Recomputed em_score 20.0 rescoring B2 on the increment, or 17.0 removing it, against 21.0 reported. MODEST band and the EM 25 UA miss hold in every case."}
  - {severity: "MINOR", location: "B01 report, B4 and M12", description: "The prompt's fixed working-capital-days formula (Receivable + Inventory - Payable) was replaced by the company-disclosed NWC-days KPI, against the instruction not to substitute alternatives. The substitution is disclosed with cause and is score-invariant: the MD&A DSO/DIO/DPO route and the prompt's own N/A-to-zero route both land in the same bands."}
  - {severity: "MINOR", location: "B01 report, M4 line", description: "The M4 line says 'judgment flagged; see analyst_note'. The analyst_note does not mention M4. Dangling cross-reference on the one line item that most needed the explanation."}
  - {severity: "MINOR", location: "B07 Section 3", description: "The prompt asks for an evidence table or NO EVIDENCE FOUND per category. Categories are presented as anchored prose instead. The 23-row summary table supplies the required structure, so the loss is presentational."}
  - {severity: "MINOR", location: "B07 report body and block evidence_mix", description: "The analyst-inference tier is never applied anywhere and evidence_mix reports inference 0, although the report makes and labels inferences in prose (the C2 consolidation artifact reading, the 2C utilisation-not-capex conclusion, the 6E base-rate argument). The taxonomy is meant to cover every piece of evidence. No score effect."}
  - {severity: "MINOR", location: "B07 Section 3, completionist recount line", description: "The mandated recount line states 13 documented items across 6 categories, then names seven (B1, B2, C2, F1, G2, H3, R1), and the block says seven. The stated count contradicts its own list and the block."}
  - {severity: "MINOR", location: "B07 categories H2 and G1", description: "A few evidence items carry no page anchor, for example 'related-party term loan structure, AR consolidated notes'. The prompt requires an anchor on every evidence item. Whether the referenced content exists at any page is Verifier A's call, not mine."}
  - {severity: "MINOR", location: "B07 Section 3, category I2", description: "The prompt requires the cannibalization test to be answered for each moat claimed anywhere in the scan. It is answered for B2 only; C1, C2 and R1 are covered by a generalising sentence rather than individually. The score would remain 0 in each case."}
  - {severity: "MINOR", location: "B07 optionality register against block optionality_register", description: "Nine rows in the report table, eight in the block. The rung-jump B2S row is not carried. The prompt states the register is carried in the block and merged into the monitoring checklist, so the row is lost to synthesis. Its content overlaps the carried B2S transform-phase row."}
  - {severity: "MINOR", location: "B07 Section 3 summary table and block", description: "Strength labels depart from the prompt's Strong / Moderate / Weak / None set: 'Weak-Moderate', 'None (negative)', 'Moderate (artifact-caveated)'. The boundary case B1 was resolved conservatively and excluded from active_categories, so no outcome effect."}
  - {severity: "MINOR", location: "B07 block, evidence_mix", description: "The claim count of 22 is not enumerated or reconcilable from the report body, unlike the documented count of 13, which is itemised. It cannot be checked from the artifact."}
  - {severity: "MINOR", location: "B07 block", description: "The prompt says to end with exactly the specified fenced YAML block. Five fields sit outside the schema: em_score_scale, ua_qualifier_threshold, ua_qualifier_met, capex_embedded_growth_note, orchestrator_note. All informative, none contradictory; the risk is only to a strict downstream parser."}
critical_count: 0
major_count: 3
minor_count: 11
rules_checked_total: 106
rules_passed_total: 92
acceptance_rate: 87
framework_adherence: 87            # percent, Gate 0 and Emerging Moat scope only
rework_trigger: false              # no CRITICAL, acceptance above 60% in both scopes
```
