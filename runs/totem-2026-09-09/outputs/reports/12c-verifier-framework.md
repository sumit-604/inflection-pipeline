# VERIFIER C — FRAMEWORK ADHERENCE (PHASE 1 SCOPE) — TOTEM

Run: runs/totem-2026-09-09/ | Stage 12c (B12c) | Model: claude-opus-4-8 | 2026-09-09

Scope: Gate 0 (B01) rules 2 and 3, Emerging Moat (B07) rules 3 and 8,
downstream signal candidates (B09) rule 6. The valuation audit (rules 4, 7),
the stage 13 narrative check (rule 9) and the Halt 1 dossier check (rule 10)
are OUT OF SCOPE this phase. B10 and B11 do not exist yet.

Rule sources loaded: prompts/01-gate-0-pipeline.md, prompts/07-emerging-moat-pipeline.md.
No valuation framework document was read.

Artifacts audited: outputs/reports/01-gate0.md, outputs/blocks/B01-gate0.yaml,
outputs/reports/07-emoat.md, outputs/blocks/B07-emoat.yaml,
outputs/blocks/B09-tam.yaml (rule 6 only).

Underlying data re-read for independent re-derivation:
inputs/screening/screener-Data_Sheet.csv, KENNAMET-Data_Sheet.csv,
WENDT-Data_Sheet.csv, BIRLAPREC-Data_Sheet.csv.

I audit rule application. Verifier A owns whether a number exists in a source.

---

## HEADLINE

Concur with the Gate 0 classification. **AVOID stands.**
Concur with the moat classification. **STRONG (4 of 12) stands.**
Concur with the Emerging Moat classification. **NONE (9.7 / 92) stands.**

Every block score re-derives to the reported value. All 12 moat tests
re-derive. All 23 emerging-moat rows are present and scored. The four
peer EBITDA margins and the peer median re-derive exactly from the CSVs.

One MAJOR finding: the B07 report carries **run 2's** Gate 0 moat figures
(5 of 12, 22/60) in Sections 6C, 6D and 6E. B01 run 3 says 4 of 12, 20/60.

Nine findings total: 0 CRITICAL, 1 MAJOR, 8 MINOR.

---

## PART 1 — GATE 0 (B01), RULE 2

### 1.1 Block A — Return on Capital

Source basis check first. The stage rule says use the source's own ROCE
where the source provides it. The screener export holds no ratio block, so
the report used AR-disclosed ROCE and ROE. I re-derived both against the
stage's own fixed formulas to test whether the AR figures are the same
animal:

| Year | AR ROCE | My EBIT / (Total − Other Liabilities) | AR ROE | My PAT / avg NW |
|---|---|---|---|---|
| FY24 | 28% | (39.83+1.16)/(202.60−56.02) = 27.96% | 43% | 29.71/68.90 = 43.1% |
| FY25 | 22% | (40.88+1.13)/(250.03−61.31) = 22.26% | 19% | 28.75/152.00 = 18.9% |
| FY26 | 22% | (39.50+1.66)/(251.32−66.10) = 22.22% | 17% | 28.77/167.41 = 17.2% |

(inputs/screening/screener-Data_Sheet.csv, P&L and Balance Sheet blocks)

The AR figures reconcile to the stage formula to within 0.3pp. Basis is sound.

| Test | Rule band | Report input | Report score | My re-derivation | Verdict |
|---|---|---|---|---|---|
| A1 | median ROCE 20-24.9 = 4 | median(28,22,22)=22 | 4 | 22 → 4 | PASS |
| A2 | min ROCE ≥15 = 5 | 22 | 5 | 22 → 5 | PASS |
| A3 | median ROE 15-19.9 = 4 | median(43,19,17)=19 | 4 | 19 → 4 | PASS |
| A4 | decline >5pp = 0 | 22 vs 28 = −6pp | 0 | −6pp → 0 | PASS |
| **Block A** | | | **13** | **13** | **PASS** |

The FY24 43% ROE is a demerger base artifact and the report says so. It is
still the disclosed ratio and the rule gives no exclusion route. Keeping it
is correct. Note it does not bind: A3's median is 19% either way.

### 1.2 Block B — Cash Generation Quality

| Test | Rule band | Report | My re-derivation | Verdict |
|---|---|---|---|---|
| B1 | ≥1.00 = 5 | 88.33/87.23 = 1.013 | 1.0126 → 5 | PASS |
| B2 | 50-74% = 2 | 2 of 3 = 66.7% | 66.7% → 2 | PASS |
| B3 | negative = 0 | −55.58/87.23 = −0.637 | −0.637 → 0 | PASS |
| B4 | increased 5-15 = 1 | +5.0072 days | see below | PASS |
| **Block B** | | **8** | **8** | **PASS** |

**B4, the recomputation claim, tested line by line.** Rebuilt from the
stated primary balance-sheet inputs using the stage's fixed formula
(revenue basis, stated):

FY24: 2,944.40/22,849.66×365 = 47.034 ; 3,846.87/22,849.66×365 = 61.450 ;
2,169.42/22,849.66×365 = 34.654. WC = 47.034 + 61.450 − 34.654 = **73.830**.
Report: 73.8291.

FY26: 3,019.59/25,101.13×365 = 43.909 ; 5,642.15/25,101.13×365 = 82.044 ;
3,240.15/25,101.13×365 = 47.116. WC = 43.909 + 82.044 − 47.116 = **78.837**.
Report: 78.8363.

Delta = **+5.007 days**. Report: +5.0072. Reproduced.

Band application: "±5 days = 3 | increased 5-15 = 1". +5.007 exceeds 5.00,
so the ±5 band closes and "increased 5-15" opens. Score 1 is the rule as
written. The report states the boundary explicitly, which is what run 2
failed to do. **PASS.**

Knife-edge sensitivity, because 0.007 days is not a margin: if B4 were 3,
Block B = 10 and Core = 60, which crosses into the 60-79 band → GOOD+ on
STRONG moat. The pledge deal-breaker then caps at AVERAGE and the LIMITED
history downgrade pulls to **AVOID**. Same final answer. The classification
does not turn on this boundary. Recorded so no one has to re-run it.

### 1.3 Block C — Growth

| Test | Rule band | Report | My re-derivation | Verdict |
|---|---|---|---|---|
| C1 | <5% = 0 | (251.01/228.50)^0.5−1 = 4.81% | 4.810% → 0 | PASS |
| C2 | negative = 0 | (28.77/29.71)^0.5−1 = −1.60% | −1.595% → 0 | PASS |
| C3 | 100% = 5 | 2 of 2 | 2 of 2 → 5 | PASS |
| C4 | −3 to −8pp = 1 | −6.41pp | −6.41pp → 1 | PASS |
| **Block C** | | **6** | **6** | **PASS** |

CAGR edge rules honoured. Both endpoints of both CAGRs are positive, so
"N/M (negative endpoint)" does not fire and a real CAGR is required, not
suppressed. No loss-to-profit swing in the FY24-FY26 window, so no
data_notes entry is owed. C4's own edge rule ("when PAT CAGR is N/M, score
C4 = 0") does not fire because PAT CAGR is computable at −1.60%; C4 = 1 is
correct, not a missed zero. **PASS.**

### 1.4 Block D — Balance Sheet Strength

| Test | Rule band | Report | My re-derivation | Verdict |
|---|---|---|---|---|
| D1 | 0-1.0x = 4 | (16.64−6.28)/52.62 = 0.197x | 0.1969 → 4 | PASS |
| D2 | ≥10x = 5 | (39.50+1.66)/1.66 = 24.8x | 24.79 → 5 | PASS |
| D3 | <0.1 = 5 | 16.64/168.58 = 0.099 | 0.0987 → 5 | PASS |
| D4 | 1.5-1.99 = 4 | 1.84 | 1.84 → 4 | PASS |
| **Block D** | | **18** | **18** | **PASS** |

D3 is a second knife edge (0.0987 vs a 0.1 boundary; the AR's own narrower
D/E prints 10%). If D3 = 4, Core = 57, still the 40-59 AVERAGE band, still
AVOID. No flip. The report discloses the two bases and names the one used.

D1's mutual-fund exclusion: the stage's fixed formula defines net debt but
gives no cash-equivalent instruction. Excluding a separate Investments line
from cash is the literal reading. The report names the alternative, names
its consequence (D1 = 5, net cash) and leaves it to the operator. That is
the correct handling of an unresolved input under the stage's own rules.
**PASS.**

**EBITDA basis governance claim, tested.** The rule that matters is
within-test consistency, since the framework fixes no EBITDA definition.
Checked all four affected tests:
- D1, D2: filed-audited basis, single entity, one basis. Consistent.
- M1: filed basis on BOTH endpoints (FY24 51.38, FY26 52.62). Consistent.
- M2, M9: Data_Sheet basis on subject AND all three peers. Consistent.

No test mixes bases across its own inputs. The declared governance rule is
followed, not merely asserted. **PASS.**

Materiality of the split: FY26 EBITDA 52.62 vs 52.94 is 0.32 cr, 0.13pp of
margin. D1 = 0.197x on one basis and 0.196x on the other. No score anywhere
is sensitive to the choice. The report's claim that the M1 basis correction
does not move the tier is confirmed: −1.52pp on the filed basis, −1.40pp on
the Data_Sheet basis, and M1's only sub-10%-CAGR tier requires a 2-5pp
decline, which neither reaches.

I also re-derived the subject's Data_Sheet EBITDA independently from the
stated formula: 251.01 − 93.32 − 7.94 − 41.04 − 51.88 − 12.45 − 3.96 +
12.52 = **52.94** (21.09%). Cross-checks against the Quarters block
Operating Profit sum (8.41+14.58+11.73+18.23 = 52.95). Reconciles.

### 1.5 Block E — Shareholder Alignment

| Test | Rule band | Report | My re-derivation | Verdict |
|---|---|---|---|---|
| E1 | ≥60% = 5 | 73.85% | → 5 | PASS |
| E2 | ±1% = 3 | unchanged over 12 months | see below | MINOR |
| E3 | >15% = 0 | 94.4% | → 0 | PASS |
| E4 | <5% = 5 | 0.1681/168.58 = 0.0997% | → 5 | PASS |
| **Block E** | | **13** | **13** | **PASS on total** |

**E2 finding (MINOR).** The rule reads "Promoter holding change over 3
years". The corpus holds three shareholding filings spanning 12 months and
the company listed 11-Jun-2024, so the 3-year window does not exist. Two
stage rules pull opposite ways: rule 5 says an unavailable data point is
"N/A (not in provided data)" and scores 0; rule 6 says use whatever history
exists and adapt the scoring. The report took rule 6, scored 3 on a
12-month proxy, and flagged the window as provisional in both the report
and the block. That is defensible and disclosed, but the deviation from the
rule's literal window is not named as a deviation.

Sensitivity: E2 = 0 gives Block E = 10, Core = 55, still 40-59 AVERAGE,
still AVOID. No flip. MINOR.

### 1.6 Core score

13 + 8 + 6 + 18 + 13 = **58**. Reported 58. **PASS.**

### 1.7 Block F — the 12 moat tests

Peer EBITDA margins re-derived by me from the CSVs, using the report's own
stated formula (Sales − RM − P&F − OtherMfr − Employee − S&A − OtherExp +
Change in Inventory):

| Company | My FY26 computation | Margin | Report | Verdict |
|---|---|---|---|---|
| TOTEM | 52.94 / 251.01 | 21.089% | 21.09% | MATCH |
| Kennametal (Jun-26) | 303.7 / 1510.7 | 20.103% | 20.09% | MATCH |
| Birla (Mar-26) | 17.17 / 247.13 | 6.948% | 6.95% | MATCH |
| Wendt (Mar-26) | 32.43 / 236.32 | 13.723% | 13.72% | MATCH |

Peer median of {20.09, 6.95, 13.72} = **13.72%**. Confirmed.

| Test | Rule | Report | My re-derivation | Verdict |
|---|---|---|---|---|
| M1 | pricing power | 0 | −1.52pp margin, 4.81% CAGR: fails ≥10%-CAGR tiers, decline <2pp so fails the 2-5pp tier → 0 | PASS |
| M2 | ≥5pp above peer median = 5 | 5 | 21.09 − 13.72 = +7.37pp → 5 | PASS |
| M3 | FAT>2x AND ROCE>15% = 3 | 3 | 251.01/113.40 = 2.21x, ROCE 22%; FAT <3x so top tier fails → 3 | PASS |
| M4 | zero decline yrs + recv ±10 = 5 | 5 | 0 decline years; 47.03→43.91 = −3.12 days → 5 | PASS |
| M5 | segment rank | 0, PEER DATA NEEDED | see below | PASS |
| M6 | R&D tiers | 0 | no R&D line in any of the four exports, none disclosed → else = 0 | PASS |
| M7 | unregulated = 0 | 0 | cutting tools is not a licensed segment → 0 | PASS |
| M8 | mentioned unquantified = 1 | 1 | see below | PASS |
| M9 | above peers, growth below = 1 | 1 | +6.57pp GM, CAGR 4.81% < 8% → 1 | PASS |
| M10 | grew every yr + recv rose ≤10 = 5 | 5 | grew every year; receivable days FELL 3.12 → 5 | PASS |
| M11 | <6yr conservative rule | 0 | 3 years, rule invoked and stated, 4.8% CAGR → else = 0 | PASS |
| M12 | >45 days = 0 | 0 | 73.83, 65.2, 78.84 all >45 → 0 | PASS |

**Moat score** = 0+5+3+5+0+0+0+1+1+5+0+0 = **20 / 60**. Reported 20. PASS.
**Moats present (≥3)** = M2, M3, M4, M10 = **4**. Reported 4. PASS.
**Moat class**: rule "4-5 = STRONG". 4 → **STRONG**. Reported STRONG. PASS.
**Grand total** = 58 + 20 = **78 / 160**. Reported 78. PASS.

M9 gross-margin proxy re-derived: subject (251.01−93.32)/251.01 = 62.82%;
Kennametal 492.7/1510.7 = 32.61%; Birla 150.26/247.13 = 60.80%; Wendt
132.94/236.32 = 56.25%. Median 56.25%. Delta +6.57pp. The proxy basis is
stated and applied identically to all four companies, as the rule requires.
PASS.

**M5, the PEER DATA NEEDED ruling — tested.** The Block F preamble is
explicit: "If a test needs peer data that is not provided, score 0 and mark
PEER DATA NEEDED (never guess peer figures)." M5's own language is
segment-scoped ("largest mcap **in segment**"). The report's position is
that three listed peers do not constitute a segment dominated by unlisted
and imported supply, so a within-4-company rank would be a guess at a
segment rank. That reading is available on the rule text and it is the
conservative one. **PASS.**

Score consequence, stated for the record: run 2's M5 = 3 gave 5 moats and
23 points on the current M8; run 3 gives 4 moats and 20 points. Both land
in the same 4-5 STRONG band. The re-score does not move moat_class and
does not touch Core. It is a correctness fix, not a verdict change.

One precision gap (MINOR, listed below): the phrase "this run holds market
cap and margin data for exactly 3 listed peers" is true, but each of the
four Data_Sheet.csv files DOES carry a Market Capitalization line in its
META block (TOTEM 856.27, Kennametal 10,356.69, Wendt 1,640.07, Birla
385.64). The missing input is a segment definition, not a market-cap
figure. A downstream reader could take "PEER DATA NEEDED" to mean no
market-cap data exists in the run. It should say segment-completeness data.

**M8, the Information Memorandum scope ruling — tested.** The stage prompt
places no restriction on which corpus document may be cited; it requires
only that the figure exist in the provided data with an anchor. The
Information Memorandum is a filed corpus document listed in the run's
sources. Ruling it in scope is correct. The band landing is also correct:
tier 5 needs reach quantified AND growing AND revenue-per-outlet, and no
growth or per-outlet metric exists; tier 3 needs revenue CAGR ≥15% against
an actual 4.8%; the business is neither "none" nor "purely digital", so the
only remaining rung is 1. **PASS.** Worth one line for the operator: the
disclosure is 2024-vintage prospectus data used in a FY26 test with no
refresh in either later AR, and the prospectus carries its own
reliance disclaimer. Score effect nil (1 point, below the ≥3 moat bar).

**Kennametal June year-end handling — tested, defensible, not a basis
error.** Kennametal's FY26 column covers Jul-2025 to Jun-2026 against the
subject's Apr-2025 to Mar-2026, a 3-month offset. The tests it feeds (M2,
M9) are ratios, not levels, which limits the damage, and the report
discloses the offset and runs a substitution check. I ran three treatments:

| Kennametal treatment | Its margin | Peer set | Median | M2 delta | M2 score |
|---|---|---|---|---|---|
| FY26 as filed (Jun-26) | 20.09% | {20.09, 6.95, 13.72} | 13.72% | +7.37pp | 5 |
| FY25 substituted (report's own check) | 14.71% | {14.71, 6.95, 13.72} | 13.72% | +7.37pp | 5 |
| March-aligned, built from the Quarters block (Jun25+Sep25+Dec25+Mar26: OP 223.9 / Sales 1356.5) | 16.51% | {16.51, 6.95, 13.72} | 13.72% | +7.37pp | 5 |

The median is Wendt's 13.72% under every treatment, because Kennametal sits
above the median and Birla below it in all three. The year-end mismatch has
literally zero effect on M2. Same result on M9: substituting Kennametal
FY25 GM (44.61%) leaves the median at Wendt's 56.25%. **Defensible.**

**The Kennametal re-bucketing reconciliation claim — tested, it holds.**
The artifact is real: the 2026-06-30 column blanks Power & Fuel, Other Mfr.
Exp and Selling & Admin, and shows Change in Inventory Rs 225.0 cr (prior
Rs 21.5 cr) and Other Expenses Rs 226.8 cr (prior Rs 7.8 cr).

Annual computation from the raw column:
1510.7 − 1018.0 − 187.2 − 226.8 + 225.0 = **303.7**, margin **20.10%**.

Quarters-block cross-check for the same Jul-2025 to Jun-2026 window:
Operating Profit 52.7 + 44.8 + 77.0 + 129.0 = **303.5**; Sales 296.0 +
334.0 + 403.1 + 477.6 = **1510.7** (an exact match to the annual Sales
line), margin **20.09%**.

Difference Rs 0.2 cr, 0.01pp of margin. **The claim is TRUE.** The blanked
lines were folded into the surviving buckets and the aggregate nets out.
M2 and M9 are unaffected by the artifact at the EBITDA level.

One qualification (MINOR, listed below). The report writes: "Any test that
read Change in Inventory or Other Expenses as standalone lines for
Kennametal FY26 (this run's tests do not) would be unreliable." M9 reads
**Raw Material Cost** standalone for Kennametal FY26, and that line moved
with the same event: RM/Sales jumped from 55.4% (FY25) to 67.4% (FY26)
while inventory rose Rs 313.9 cr. On an inventory-netted basis Kennametal's
GM would read 47.5%, not 32.61%. The named-anomaly list is one line short.

Score effect: none. Peer set {47.5, 60.81, 56.25} still medians at Wendt's
56.25%, so M9 = 1 either way. Flagged for basis honesty, not for the score.

### 1.8 Classification, deal-breakers, confidence adjustment

**Matrix.** Core 58 → the 40-59 row → AVERAGE. That row does not branch on
moat tier, so Block F's STRONG is correctly non-operative here. The report
says exactly this. **PASS.**

**Deal-breakers.** All nine checked and each given a verdict. Only #5
(pledge >15%) fires, and the report names the driving fact and the window
(94.4% of the 73.85% stake, Shapoorji Pallonji, stable across Jun-2025,
Mar-2026, Jun-2026), which satisfies the "state WHICH years drive any
deal-breaker" instruction. **PASS.**

Deal-breaker #9 ("history <3 years → AVERAGE") correctly NOT triggered at
exactly 3 years, and correctly distinguished from the data-confidence
downgrade, which is a separate rule. **PASS.**

**Confidence adjustment.** 3 years → the "3-4 LIMITED, downgrade
classification one tier" rule. AVERAGE → AVOID. The tier ladder in the
matrix runs EXCELLENT > GOOD+ > GOOD > AVERAGE > AVOID, so one tier below
AVERAGE is AVOID. **PASS.**

**Double-counting test, as tasked.** The pledge deal-breaker and the
LIMITED-history downgrade rest on two different facts: a Shapoorji Pallonji
promoter-financing pledge, and a Mar-2024 demerger with a Jun-2024 listing.
They are not the same fact. **No double-count.**

Stronger point the operator should have: the two are not even additive
here. At Core 58 the baseline is ALREADY AVERAGE, so the pledge cap
("max AVERAGE") does no work at all. The **only** rule moving the
classification from AVERAGE to AVOID is the 3-year history downgrade.

- Remove the pledge deal-breaker → still AVOID.
- Remove the history downgrade → AVERAGE.

The report states this correctly ("Absent that downgrade, the mechanical
floor here is AVERAGE"). I confirm it. The AVOID is a data-depth artifact
sitting on top of a governance flag that is currently non-binding on the
score. **PASS, and I concur with AVOID.**

**Flags.** The flags rule requires a FLAG-GATE0 entry when classification
≤ AVERAGE with historical depressors identified. Present, with the
depressors named. FLAG-CASH and FLAG-RESTATEMENT are extra, permitted, and
each carries its number. **PASS.**

**Grounded-claims rule (never estimate).** M5 and M6 gaps are marked, not
filled. LBF-2's unreproducible 146/255-day magnitude is marked unverified
and explicitly excluded from scoring rather than approximated. The
Rs 590 lakh Labour Codes correction is anchored to three filings. No
estimate substitutes for a missing figure anywhere in the report.
**PASS.** (Whether each cited figure sits at its cited anchor is Verifier
A's call, not mine.)

**LBF-4 correction — tested for rule compliance, not for source
fidelity.** The correction replaces a NOT FOUND with three anchors and
records the direction of the error. The 52% Q3-to-FY26 revision is
correctly flagged and correctly NOT scored: Gate 0 has no formula slot for
a past-service-cost estimate revision, and inventing one would breach the
"no qualitative judgments, only the scoring rules provided" rule.
**PASS.**

### 1.9 Gate 0 presentational and YAML checks

- Rule 6 opening line. The rule says "Open with: Data available: [X]
  years...". The report opens with a 55-line "WHY THIS IS RUN 3" section
  and reaches the mandated sentence at line 59. **MINOR.**
- Dashboard. Blocks, line items, classification box, strongest and weakest
  block, decision line all present. "Moat profile bars" are not rendered
  per moat (moats present are listed as text), and the block bar lengths do
  not share a scale (Block A 13/20 draws 12 characters, Block E 13/20 draws
  14). **MINOR, cosmetic.**
- Anchors. Rule 4 requires an anchor on every extracted number. One
  exception: FY25 WC days of 65.2 is carried as "prior-run figure,
  unchanged this run" into both M12 and block_b_trend, while its FY24 and
  FY26 siblings were rebuilt to four decimals. No score effect (M12 needs
  only >45). **MINOR.**
- YAML schema. All required keys present. blocks match the report
  (A13 B8 C6 D18 E13), core 58, moat 20, grand 78, moats_confirmed 4,
  moat_class STRONG, classification AVOID, history_downgrade true,
  deal_breakers populated, data_notes populated, block_b_trend carries its
  one number. analyst_note is inside the 200-word cap. **PASS.**

### Gate 0 tally

58 rule checks. 53 PASS, 5 MINOR fails, 0 MAJOR, 0 CRITICAL.
No recomputed score differs from the reported score anywhere in Blocks A
through F. **Classification concur: AVOID.**

---

## PART 2 — EMERGING MOAT (B07), RULES 3 AND 8

### 2.1 Category completeness

All 23 rows (22 categories + R1) are addressed in narrative AND in the
Section 3 summary table AND in the Section 5 scoring table. I checked each
of the three lists against the prompt's family roster:

A1 A2 A3 A4 | B1 B2 B3 | C1 C2 | D1 D2 | E1 E2 | F1 F2 | G1 G2 | H1 H2 H3 |
I1 I2 | R1 = **23**. None missing, none duplicated. **PASS.**

Eighteen rows carry an explicit "NO EVIDENCE FOUND", several with the
finding stated as negative rather than absent (B1, E2, G1, G2), which is
the correct handling under rule 5 (state it and move on, never force-fit).
No category is silently skipped. **PASS — no REWORK trigger.**

### 2.2 Rule 8 — categories 21 and 22

**I1 TALENT ASYMMETRY (Category 21). Present. Scored 0.** The gate in my
rubric bites only above 0, so a 0 clears it automatically. But I checked
the reasoning is the category's, not a shrug: the report runs the (a) leg
(no named inventor on any patent, none exist per A2; no ex-DRDO/ex-HAL
concentration verifiable from the corpus; the AR remuneration annexure
shows sitting fees and standard managerial ratios, not a class of
above-norm technical pay) and then names the exclusion pattern the category
is built for ("a hiring/organisation story with no structural-economics
leg"). The (b) leg is never asserted. **PASS.**

**I2 CANNIBALIZATION BARRIER (Category 22). Present. Scored 0.** The
category requires testing every moat claimed anywhere in the scan. The
report does that: A3 and B2 are tested and both answer "capital and
calendar time only", and the report reaches the category's own zero
condition verbatim ("nothing must be destroyed"). It then applies the
category's exclusion rule to F2 by name: an execution lead is not a
configuration moat. No unnamed or vague sacrifice is credited. **PASS.**

**I1/I2 contribution stated separately**, as the operator's 20-Aug-2026
ruling requires for the review checkpoint: "I1/I2 contribution to the
total: 0.0 ... no threshold crossing was achieved via I1/I2 points".
**PASS.**

### 2.3 Evidence multipliers and scoring consistency

Matrix: HH=4, HM/MH=3, HL/MM/LH=2, ML/LM=1, LL=1, none=0. Multipliers:
📄 1.0, 🎙️ 0.7, 🔍 0.5.

| Row | Likelihood x Impact | Raw claimed | Raw correct? | Evidence in narrative | Multiplier | Adjusted | Verdict |
|---|---|---|---|---|---|---|---|
| A3 | High x Medium = HM | 3 | yes | 📄, 5 documented items across 3 ARs | 1.0 | 3.0 | PASS |
| B2 | High x Medium = HM | 3 | yes | 📄, 6 named certifications | 1.0 | 3.0 | PASS |
| C1 | Medium x Low = ML | 1 | yes | 📄 (thread mill software) + 🎙️ (IM sales engineers) | 0.7 | 0.7 | PASS |
| F2 | Medium x Medium = MM | 2 | yes | 📄 capex-completion chain | 1.0 | 2.0 | PASS |
| H3 | Medium x Low = ML | 1 | yes | 📄 solar kWh disclosure | 1.0 | 1.0 | PASS on value |

Adjusted total = 3.0 + 3.0 + 0.7 + 2.0 + 1.0 = **9.7**. Reported 9.7.
Band "<12 = NO MEANINGFUL EMERGING MOAT". 9.7 → **NONE**. **PASS.**

The specific trap my rubric names — "a 🎙️-only category scoring as if 📄"
— does not occur. C1 runs the opposite way: it is a MIXED row whose lead
item is 📄 (the thread mill software is a shipped, AR-disclosed artifact),
and the scorer applied the LOWER 0.7 multiplier on a stated
"🎙️ (majority)" judgment. Downward, conservative, and consistent with the
prompt's rule 4 skepticism instruction. **PASS.**

The two 📄 rows that could have been inflated were both capped by explicit
inference notes instead. A3's impact is held at MEDIUM because the Q1 FY27
margin bridge (verified in B01 LBF-1) traces to opex compression on volume,
not yield. B2's impact is held at MEDIUM because the certifications are
table stakes a global major already holds. Both caps cost the scan a point
each and both are argued, not asserted. This is the correct direction of
discipline for this stage.

**H3 label (MINOR).** The scoring table writes H3's pair as "1 (LM)" while
its own Likelihood and Impact columns read Medium and Low, which is ML. The
matrix values ML and LM are both 1, so the score is right and the total is
unaffected. Transposed letters only. **MINOR, presentational.**

### 2.4 Completionist recount

Prompt form required: "📄 recount performed: [n] documented items across
[m] categories."

Report line: "📄 recount performed: 15 documented items across 5 categories
(A3: 5 items ... B2: 6 items ... F2: 2 items ... C1: 1 item ... H3: 1
item)." Arithmetic: 5+6+2+1+1 = **15 across 5**. Internally consistent.
Mirrored into the YAML completionist_recount field. **PASS.**

Guard threshold: the guard fires at 12 or more active categories. This scan
has 5 rows with any evidence and 3 clearing Strong/Moderate, well inside
the stated 3-6 base rate. The guard was not needed, and the recount was
performed anyway because the prompt asks for the line explicitly. **PASS.**

A sparse scan that skipped categories would be a finding. This one did not
skip: 23 of 23 addressed, 18 explicitly negative or empty with reasons and
anchors. The sparseness is a result, not a gap.

### 2.5 Section completeness and the 2C arithmetic

Sections 1A, 1B, 1C, 2A, 2B, 2C, 2D, 3, 4A, 4B, 4C, 5, Optionality
Register, 6A, 6B, 6C, 6D, 6E all present in one response. **PASS.**

2C requires the arithmetic shown. Re-derived from the CSV:
FAT FY24 228.50/89.32 = 2.558; FY25 232.66/110.01 = 2.115; FY26
251.01/109.84 = 2.285; average = **2.319 ≈ 2.32x**. CWIP Rs 3.56 cr ×
2.32 = **Rs 8.26 cr**; / Rs 251.01 cr = **3.29% ≈ 3.3%**. Matches the
report and the YAML field. **PASS.**

The narrowing of "capex under execution" to CWIP only, excluding
commissioned capex already inside the actuals, is the correct reading of
"under execution" and is argued in place rather than left implicit.
**PASS.**

Optionality Register: 5 rows, all four mandated columns populated
(optionality, converting 📄 evidence, where it first appears, conversion
window), and the "registered options are watched, never scored" line is
present. None of the five appears in the scoring table. **PASS.**

6D: combined classification AVOID, with HIGH POTENTIAL and TURNAROUND both
considered and rejected with reasons, as the prompt specifically demands.
**PASS.**

### 2.6 MAJOR — B07 carries run 2's Gate 0 figures

Section 6C's combined table states the Gate 0 existing-moat cell as
"5 of 12 confirmed, moat block 22/60, class STRONG". Section 6D repeats
"Gate 0's own STRONG existing moat block (22/60)". Section 6E repeats
"Existing (Gate 0 moat block, STRONG, 5/12 confirmed)".

B01-gate0 run 3 states **4 of 12 confirmed, 20/60**.

Those are run 2's numbers. B07 consumed a superseded B01 block. Three
places in the report carry it.

The stage prompt says 6C uses "the INJECTED Gate 0 block", so if run 2's
block was what the orchestrator injected, stage 7 complied with its input
and the defect is an orchestration sequencing one. That does not change
what the artifact now says. As it stands the B07 report contradicts the
run's own B01 on a number a downstream reader will lift.

Scope of the damage, bounded:
- Core 58 in 6C is current-correct.
- Gate 0 classification AVOID in 6C is current-correct.
- Moat class STRONG is correct under BOTH versions (4 and 5 both sit in
  the 4-5 STRONG band), so 6D's reasoning does not break.
- em_score 9.7, em_classification NONE, combined_assessment AVOID and
  combined_reasoning are all unaffected. The B07 YAML carries none of the
  stale figures.

So no classification flips and no B07 score moves. But two stated scores
inside a mandated deliverable table are wrong by 2 points and 1 moat.
**MAJOR.** Fix is a three-line alignment edit to 6C, 6D and 6E, in the same
commit, per the dependency-alignment rule.

### 2.7 Two further MINOR findings

**evidence_mix scope undeclared.** The block reports
`{documented: 15, claim: 1, inference: 0}`. The report body carries
materially more than one 🎙️ item (1A upgraded tapping geometries; 1B
geographic and vertical rows; 1C's four qualitative direction reads; 2D
Far East/GCC re-entry; C1's IM sales-engineer claim) and more than zero 🔍
items (the 1C export-percentage computation, the 2A capacity-percentage
arithmetic, the 2C capex inference, and the A3, B2 and F2 impact-capping
inferences are each labelled 🔍 in the text). If the field is scoped to the
Section 3 scan only, the counts are defensible; the field never states its
scope. No score effect, since multipliers were applied per category from
the narrative evidence, not from this tally. **MINOR.**

**catalysts_12m evidence_type.** All five catalysts are labelled
"DOCUMENTED" (one as "DOCUMENTED (future filing)") while describing events
that have not happened yet. Under the stage's own taxonomy, 📄 DOCUMENTED
means capex committed, contract signed, product launched. A future filing
is not documented evidence. The anchors point to the existing baseline
documents, which is the sensible intent, but the label as written mis-tiers
future events. This field feeds Pillar 3 catalyst proximity in phase 3, so
the tier should be right before stage 11 reads it. All five windows do fall
inside 12 months of the run date. **MINOR.**

### Emerging Moat tally

33 rule checks. 29 PASS, 1 MAJOR fail, 3 MINOR fails, 0 CRITICAL.
**Classification concur: NONE (9.7 / 92).**

---

## PART 3 — RULE 6, DOWNSTREAM SIGNAL CANDIDATES (B09)

Rule: B09 contains downstream_candidates with ≥3 items, OR
demand_externally_verifiable = false with the exact sentence present.

B09-tam.yaml carries **6** downstream_candidates (IMTMA machine-tool data;
SIAM automotive volumes; Kennametal India quarterly results; US/Mexico
tariff policy; HSS/tungsten-carbide import prices; defence and aerospace
procurement budget). Each carries signal, entity_type, demand_link,
likely_source, cadence and shared. `demand_externally_verifiable: true`, so
the NOT EXTERNALLY VERIFIABLE branch does not apply and the exact sentence
is correctly absent.

**PASS. No REWORK for stage 9.**

The second half of rule 6 (stage 11 catalysts each citing a candidate or
carrying the MODERATE cap) cannot be tested. B11 does not exist. Deferred
to phase 3.

---

## FINDINGS TABLE

| # | Sev | Location | Finding | Recomputed value | Score effect |
|---|---|---|---|---|---|
| 1 | MAJOR | 07-emoat.md 6C, 6D, 6E | Gate 0 existing-moat figures are run 2's (5 of 12, 22/60); B01 run 3 says 4 of 12, 20/60 | 4 of 12, 20/60 | none on B07; corrupts the combined table a downstream stage lifts |
| 2 | MINOR | 01-gate0.md, E2 | 3-year promoter-holding window does not exist; scored 3 on a 12-month proxy under rule 6, deviation from the rule's literal window not named as such | E2 = 0 gives Core 55, still AVOID | none on classification |
| 3 | MINOR | 01-gate0.md, opening | Mandated "Data available: X years" sentence sits at line 59 behind a 55-line run-3 preamble; rule 6 says open with it | n/a | none |
| 4 | MINOR | 01-gate0.md, M12 and block_b_trend | FY25 WC days 65.2 carried unanchored from a prior run while FY24 and FY26 were rebuilt to four decimals | n/a (M12 needs only >45) | none |
| 5 | MINOR | 01-gate0.md, Block F anomaly note | Anomaly list names Change in Inventory and Other Expenses; Kennametal FY26 Raw Material Cost moved with the same event (RM/Sales 55.4% to 67.4%) and M9 reads it standalone | Kennametal GM 47.5% on an inventory-netted basis vs 32.61% used | none: peer median stays 56.25% (Wendt), M9 = 1 either way |
| 6 | MINOR | 01-gate0.md, M5 wording | "PEER DATA NEEDED" reads as if no market-cap data exists; all four Data_Sheet.csv META blocks carry Market Capitalization. The missing input is a segment definition | n/a | none |
| 7 | MINOR | 01-gate0.md, dashboard | Moat profile bars not rendered per moat; block bar lengths not on a common scale | n/a | none |
| 8 | MINOR | B07-emoat.yaml, evidence_mix | `{documented: 15, claim: 1, inference: 0}` scope undeclared; report body carries more 🎙️ and 🔍 items than the tally | n/a | none: multipliers applied per category from the narrative |
| 9 | MINOR | B07-emoat.yaml, catalysts_12m | All five future events tiered "DOCUMENTED"; a not-yet-existing filing is not 📄 evidence. Field feeds Pillar 3 catalyst proximity in phase 3 | n/a | none in phase 1 |

---

## WHAT I TESTED THAT PASSED, STATED PLAINLY

The five claims the run makes about itself were each tested against the
rules and the data, not taken on the report's word:

1. **M5 = 0, PEER DATA NEEDED.** Correct application of the "never guess
   peer figures" rule against segment-scoped test language. Moves moats
   from 5 to 4 and points from 23 to 20; both sit in the 4-5 STRONG band,
   so nothing downstream flips.
2. **B4 = +5.0072 days.** Reproduced from the primary inputs at +5.007.
   Band call correct as written. Sensitivity run: the alternative call
   still ends at AVOID.
3. **M8 = 1 on the Information Memorandum.** IM is in scope; the band
   landing is forced by the failure of tiers 5 and 3 and the business being
   neither absent from distribution nor purely digital.
4. **EBITDA basis governance.** No test mixes bases across its own inputs.
   The split is immaterial to every score it touches.
5. **LBF-4 correction.** Anchored three times, correctly flagged and
   correctly not scored.

And the two the task named:

6. **Kennametal June year end.** Defensible, not a basis error. The peer
   median is Wendt's 13.72% under the as-filed, the FY25-substituted, and a
   March-aligned quarters-built treatment. Zero effect on M2 or M9.
7. **The re-bucketing reconciliation claim.** True. Annual 303.7 (20.10%)
   against quarters-summed 303.5 (20.09%), on an exactly matching Sales
   line of 1510.7. One line short in the anomaly list (finding 5), with no
   score consequence.

And the classification structure:

8. **Pledge deal-breaker and LIMITED-history downgrade are not double
   counting.** Different facts, and not additive here: at Core 58 the
   baseline is already AVERAGE, so the pledge cap does no work. The history
   downgrade alone produces AVOID.

---

## VERDICT

**Gate 0: concur. AVOID.** 58 / 100 core, 20 / 60 moat, 78 / 160 grand
total, 4 moats confirmed, STRONG. Every figure re-derives.

**Emerging Moat: concur. NONE, 9.7 / 92.** All 23 categories addressed,
multipliers correct, recount performed, categories 21 and 22 present and
correctly gated at 0.

**Rule 6: PASS.** Six downstream candidates in B09.

No CRITICAL. No REWORK trigger from this verifier. One MAJOR requiring a
three-line alignment edit to 07-emoat.md Sections 6C, 6D and 6E.

92 rule checks, 83 passed, acceptance rate 90.2%.

Valuation adherence (rules 4, 7, 11 to 14), the stage 13 Business
Understanding Narrative (rule 9) and the Halt 1 dossier (rule 10) are
deferred to phase 3.

---

```yaml
stage: B12c
company: "TOTEM"
run_date: "2026-09-09"
model: claude-opus-4-8
status: complete
scope: "phase-1 (Gate 0 + Emerging Moat + B09 rule 6); valuation audit deferred to phase 3"
gate0:
  rules_checked: 58
  fails:
    - {severity: MINOR, rule: "E2 promoter-holding change over 3 years", detail: "3-year window does not exist (listed Jun-2024); scored 3 on a 12-month proxy under stage rule 6 without naming the deviation from the rule's literal window", recomputed: "E2=0 gives Block E 10, Core 55, still 40-59 AVERAGE, still AVOID"}
    - {severity: MINOR, rule: "stage rule 6 opening statement", detail: "mandated 'Data available: X years' line appears at line 59 behind a 55-line run-3 preamble instead of opening the report", recomputed: "n/a"}
    - {severity: MINOR, rule: "stage rule 4 source anchors", detail: "FY25 WC days 65.2 carried unanchored as a prior-run figure into M12 and block_b_trend while FY24/FY26 were rebuilt to four decimals", recomputed: "no effect; M12 band needs only >45 days"}
    - {severity: MINOR, rule: "Block F peer-data integrity note", detail: "Kennametal FY26 anomaly list names Change in Inventory and Other Expenses only; Raw Material Cost moved with the same event (RM/Sales 55.4% to 67.4%) and M9 reads it standalone", recomputed: "Kennametal GM 47.5% inventory-netted vs 32.61% used; peer median stays 56.25% (Wendt), M9=1 either way"}
    - {severity: MINOR, rule: "M5 PEER DATA NEEDED wording", detail: "reads as if no market-cap data exists; all four Data_Sheet.csv META blocks carry Market Capitalization (TOTEM 856.27, KENNAMET 10356.69, WENDT 1640.07, BIRLAPREC 385.64). Missing input is a segment definition, not a peer figure", recomputed: "n/a; M5=0 ruling itself is correct"}
    - {severity: MINOR, rule: "dashboard format", detail: "moat profile bars not rendered per moat; block bar lengths not on a common scale", recomputed: "n/a"}
  blocks_rederived: {A: 13, B: 8, C: 6, D: 18, E: 13}
  core_rederived: 58
  moat_rederived: 20
  moats_confirmed_rederived: 4
  moat_class_rederived: "STRONG"
  grand_total_rederived: 78
  classification_rederived: "AVOID"
  concur: true
  deal_breaker_double_count: false
  deal_breaker_note: "pledge cap and LIMITED-history downgrade rest on different facts and are not additive here; at Core 58 the baseline is already AVERAGE so the pledge cap is non-operative, and the history downgrade alone produces AVOID"
  cagr_edge_rules_honoured: true
  peer_year_end_handling: "defensible; peer median is Wendt 13.72% under as-filed Jun-FYE, FY25-substituted, and March-aligned quarters-built treatments; zero effect on M2 or M9"
  kennametal_rebucketing_claim: "VERIFIED TRUE; annual 303.7 (20.10%) vs quarters-summed 303.5 (20.09%) on an exactly matching Sales line of 1510.7"
emoat:
  rules_checked: 33
  fails:
    - {severity: MAJOR, rule: "6C/6D/6E use the injected Gate 0 block", detail: "B07 carries run 2 Gate 0 moat figures (5 of 12 confirmed, 22/60) in Sections 6C, 6D and 6E; B01 run 3 states 4 of 12, 20/60", recomputed: "4 of 12, 20/60; moat class STRONG under both, em_score/classification/combined_assessment unaffected; B07 YAML carries no stale figure", fix: "three-line alignment edit to 07-emoat.md 6C, 6D, 6E in the same commit"}
    - {severity: MINOR, rule: "likelihood x impact matrix labelling", detail: "H3 pair written '1 (LM)' while its own columns read Medium likelihood x Low impact (ML)", recomputed: "ML=1 and LM=1; value and total correct"}
    - {severity: MINOR, rule: "evidence_mix counts", detail: "{documented:15, claim:1, inference:0} scope undeclared; report body carries more labelled MANAGEMENT CLAIM and ANALYST INFERENCE items than the tally", recomputed: "no score effect; multipliers were applied per category from the narrative evidence"}
    - {severity: MINOR, rule: "evidence taxonomy on catalysts_12m", detail: "all five future events tiered DOCUMENTED; a not-yet-existing filing is not documented evidence. Field feeds Pillar 3 catalyst proximity in phase 3", recomputed: "n/a in phase 1; all five windows do fall inside 12 months"}
  categories_addressed: 23
  categories_expected: 23
  cat21_present: true
  cat21_score: 0
  cat21_gate_ok: true
  cat22_present: true
  cat22_score: 0
  cat22_gate_ok: true
  multipliers_correct: true
  completionist_recount_performed: true
  completionist_recount_line: "documented recount performed: 15 documented items across 5 categories (A3 5, B2 6, F2 2, C1 1, H3 1); arithmetic reproduced"
  em_score_rederived: 9.7
  em_classification_rederived: "NONE"
  capex_embedded_growth_rederived: 3.3
  concur: true
downstream_candidates_b09: {present: true, count: 6, demand_externally_verifiable: true, exact_sentence_required: false, pass: true, stage11_catalyst_citation_check: "deferred to phase 3"}
valuation: {rules_checked: 0, fails: [], status: "PENDING PHASE 3 - B10 and B11 do not exist yet; valuation framework documents not loaded in phase-1 scope"}
expectation_ledger: {present: false, downside_row: false, all_rows_confirm_by: false, all_rows_metric_threshold: false, prob_in_range: false, decay_status_valid: false, off_ledger_credit: false, residual_pct_cmp: 0, residual_starter_cap_ok: true, fails: [], status: "PENDING PHASE 3"}
business_understanding_narrative: {present: false, five_questions_answered: false, prose_only: false, section6_candidates_named: 0, valuation_vocab_leak: false, fails: [], status: "PENDING PHASE 3 - stage 13 has not run"}
recomputed_destination_pe: ""   # out of scope phase 1
recomputed_decision: ""         # blank: concur with AVOID
findings:
  - {severity: MAJOR, location: "outputs/reports/07-emoat.md Sections 6C, 6D, 6E", note: "stale run-2 Gate 0 moat figures (5 of 12, 22/60) against B01 run 3 (4 of 12, 20/60); no classification flips, alignment edit required"}
  - {severity: MINOR, location: "outputs/reports/01-gate0.md Block E, E2", note: "12-month proxy for a 3-year window, disclosed but not named as a rule deviation"}
  - {severity: MINOR, location: "outputs/reports/01-gate0.md opening", note: "mandated data-availability sentence not at the open"}
  - {severity: MINOR, location: "outputs/reports/01-gate0.md M12 / block_b_trend", note: "FY25 WC days 65.2 carried unanchored from a prior run"}
  - {severity: MINOR, location: "outputs/reports/01-gate0.md Block F anomaly note", note: "Kennametal FY26 Raw Material Cost also distorted by the re-bucketing event and is read standalone by M9; score unaffected"}
  - {severity: MINOR, location: "outputs/reports/01-gate0.md M5", note: "PEER DATA NEEDED wording implies absent market-cap data; the gap is a segment definition"}
  - {severity: MINOR, location: "outputs/reports/01-gate0.md dashboard", note: "moat profile bars absent, block bars not on a common scale"}
  - {severity: MINOR, location: "outputs/blocks/B07-emoat.yaml evidence_mix", note: "scope of the item counts undeclared and inconsistent with the report body"}
  - {severity: MINOR, location: "outputs/blocks/B07-emoat.yaml catalysts_12m", note: "future events tiered DOCUMENTED; mis-tiers evidence that feeds Pillar 3 in phase 3"}
critical_count: 0
major_count: 1
minor_count: 8
acceptance_rate: 90.2          # 83 of 92 rule checks passed (58 gate0 + 33 emoat + 1 B09 rule 6)
```
