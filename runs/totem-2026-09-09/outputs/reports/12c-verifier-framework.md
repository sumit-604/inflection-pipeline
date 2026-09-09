# VERIFIER C — FRAMEWORK ADHERENCE (PHASE 1 SCOPE) — TOTEM

Run: runs/totem-2026-09-09/ | Stage 12c (B12c) | Model: claude-opus-4-8 | 2026-09-09

**Scope.** Phase 1 only. Rules 2 (Gate 0), 3 (Emerging Moat), 6 (B09
downstream_candidates block requirement) and 8 (categories 21/22). Rules 4,
7, 9 to 14 are out of scope: B10 and B11 do not exist yet and stage 13 has
not run. The valuation framework documents were not loaded and were not
audited.

**Rule sources used.** prompts/01-gate-0-pipeline.md and
prompts/07-emerging-moat-pipeline.md only.

**Artifacts audited.** outputs/reports/01-gate0.md, outputs/blocks/B01-gate0.yaml,
outputs/reports/07-emoat.md, outputs/blocks/B07-emoat.yaml, and
outputs/blocks/B09-tam.yaml (rule 6 block-presence check only).

**Re-derivation basis.** All Gate 0 block scores were recomputed from
inputs/screening/screener-Data_Sheet.csv, KENNAMET-, WENDT- and
BIRLAPREC-Data_Sheet.csv, plus trade-payable figures read directly from
work/text/annual-report__Annual_Report_2026.txt and __2025.txt. I did not
take the report's word on any score-driving number that the CSVs could
settle.

**Headline.** The Gate 0 classification (AVOID) and the Emerging Moat
classification (NONE) both survive re-derivation. No CRITICAL. Two MAJOR
findings, both score-level, neither flips a classification. Ten MINOR
findings. Acceptance rate 96.8%.

---

## PART 1 — GATE 0 (B01), RULE-BY-RULE

### 1.1 Operating rules and formula definitions

| # | Rule (prompt 01) | Verdict | Note |
|---|---|---|---|
| 1 | "Open with: Data available: [X] years..." | PASS (minor) | Line present verbatim in substance at line 30, behind a "WHY THIS IS RUN 2" preamble. Not literally the opening line. MINOR-1. |
| 2 | Minimum 3 years, maximum whatever exists | PASS | FY23 in the CSV is a shell stub (Total assets Rs 0.05 cr, PBT Rs -0.01 cr, Sales blank). Excluding it is correct and disclosed; including it would still land in the 3-4 LIMITED band and would force N/M on every CAGR under the edge rule. |
| 3 | ROCE: use source's own figure and anchor it | PASS | AR-disclosed ratio note used (FY25 AR p.100, FY26 AR p.118), not computed. Correct precedence. |
| 4 | ROE definition / opening net worth caveat | PASS | AR-disclosed ratio used. FY24's 43% base-effect artifact named, flagged, not silently dropped. |
| 5 | WC Days = Rec + Inv − Pay, revenue basis, basis stated | PASS | Basis stated explicitly ("COGS is not a single explicit P&L line so revenue basis is used and stated"). Re-derived below. |
| 6 | FCF = CFO − Capex | PASS | FY24 9.46−97.26, FY25 51.32−28.26, FY26 27.55−18.39. CFO ties to Data_Sheet CASH FLOW rows. |
| 7 | CAGR = (End/Start)^(1/years) − 1 | PASS | 2-year exponent correctly used on a 3-point series. |
| 8 | CAGR edge rule, negative/zero endpoint → N/M, score 0 | PASS | Both endpoints positive on the FY24-FY26 window. Rule not engaged because FY23 is correctly excluded. |
| 9 | CAGR edge rule, C4 when PAT CAGR is N/M → 0 | N/A PASS | PAT CAGR is negative but computable (−1.60%), not N/M. C4 correctly scored on the band, not zeroed. |
| 10 | Anchors mandatory on every extracted number | PASS | Blocks A-E anchored per line. Block F anchored in bulk (file + P&L rows 11-18 + column dates) rather than per figure; acceptable, and the rows resolve. |
| 11 | Never estimate; NOT FOUND is the only fill | PASS | LBF-2 (146→255 inventory days) and LBF-4 (Rs 5.9 cr Labour Codes charge) both recorded as unverified and excluded from scoring rather than approximated. Correct behaviour. |
| 12 | YAML schema, exactly the prompt's fields | PASS | All 19 fields present, correct names, flags in {type, reason} form. |

### 1.2 Block A — re-derived

ROCE 28 / 22 / 22, ROE 43 / 19 / 17 (AR-disclosed).

| Item | Rule band | Re-derived | Report | Verdict |
|---|---|---|---|---|
| A1 | median ROCE 20-24.9 = 4 | median(28,22,22) = 22 → 4 | 4 | PASS |
| A2 | min single-year ROCE ≥15 = 5 | min = 22 → 5 | 5 | PASS |
| A3 | median ROE 15-19.9 = 4 | median(43,19,17) = 19 → 4 | 4 | PASS |
| A4 | latest vs earliest, decline >5pp = 0 | 22 − 28 = −6pp → 0 | 0 | PASS |

**Block A = 13/20. CONCUR.**

### 1.3 Block B — re-derived

CFO 9.46 / 51.32 / 27.55; PAT 29.71 / 28.75 / 28.77; FCF −87.80 / 23.06 / 9.16.

Working capital days, recomputed independently on the prescribed formula
(revenue basis), using Data_Sheet receivables and inventory and trade
payables read from the ARs (FY24 Rs 2,169.42 lakh, AR FY25 p.102; FY25
Rs 2,341.59 lakh, same page; FY26 Rs 3,240.15 lakh, AR FY26 maturity table):

| Year | Rec days | Inv days | Pay days | WC days |
|---|---|---|---|---|
| FY24 | 47.02 | 61.45 | 34.65 | **73.82** |
| FY25 | 51.83 | 50.09 | 36.74 | **65.18** |
| FY26 | 43.92 | 82.04 | 47.13 | **78.83** |

My figures reproduce the report's 73.8 / 65.2 / 78.9 to one decimal. The
formula was applied as written.

| Item | Rule band | Re-derived | Report | Verdict |
|---|---|---|---|---|
| B1 | cum CFO/PAT ≥1.00 = 5 | 88.33/87.23 = 1.0126 → 5 | 5 | PASS |
| B2 | FCF-positive 50-74% = 2 | 2/3 = 66.7% → 2 | 2 | PASS |
| B3 | cum FCF/PAT negative = 0 | −55.58/87.23 = −0.637 → 0 | 0 | PASS |
| B4 | ±5 days = 3 \| increased 5-15 = 1 | delta = 78.83 − 73.82 = **+5.01 days** | 1, on a stated delta of "+5.0" | **FAIL, MAJOR** |

**FINDING G0-1 (MAJOR). B4 sits exactly on the band boundary and the
report's own stated delta contradicts the band it applied.** The report
writes "78.9 − 73.8 = +5.0 days" and then scores the "increased 5-15" band
(1). On its own displayed value of +5.0 the correct band is "±5 days" = 3.
On my exact recomputation the delta is +5.01 days, which does fall outside
±5 and does support a score of 1 — but by 0.01 of a day, on figures whose
inputs are rounded to two decimals of a crore. The rule bands overlap at
exactly +5 and the prompt gives no tie-break, so the boundary call needed
to be stated and defended. It was not; the arithmetic shown is simply wrong
by 0.01 and the score silently takes the other side of it.

Impact, traced through: B4 = 3 gives Block B = 10 and Core = 60. Core 60-79
with a STRONG moat block reads GOOD+ on the matrix rather than AVERAGE. The
pledge deal-breaker then caps at max AVERAGE, and the LIMITED-history
downgrade takes one further tier: **AVOID either way**. The final
classification is insensitive to this finding, which is why it is MAJOR and
not CRITICAL. It is not cosmetic, because the intermediate core score
crosses a matrix band and the report's own narrative ("Core score 58 falls
in the 40-59 band") is what stage 13 and the operator will read.

**Block B = 8/20 as scored; 10/20 on the report's own displayed delta.**

block_b_trend "deteriorating" with the CFO 51.32 → 27.55 number attached:
correct per the field definition. PASS.

Deal-breaker 2 (Block B <8 → max GOOD): Block B = 8 exactly, not below 8.
Correctly not triggered. Note this is a second knife-edge: had B4 been
scored 0, Block B = 7 would have fired deal-breaker 2.

### 1.4 Block C — re-derived

Revenue 228.50 / 232.66 / 251.01; PAT 29.71 / 28.75 / 28.77.

| Item | Rule band | Re-derived | Report | Verdict |
|---|---|---|---|---|
| C1 | rev CAGR <5% = 0 | (251.01/228.50)^0.5 − 1 = 4.81% → 0 | 0 | PASS |
| C2 | PAT CAGR negative = 0 | (28.77/29.71)^0.5 − 1 = −1.60% → 0 | 0 | PASS |
| C3 | positive YoY years 100% = 5 | 2 of 2 YoY steps positive → 5 | 5 | PASS |
| C4 | −3 to −8pp = 1 | −1.60 − 4.81 = −6.41pp → 1 | 1 | PASS |

**Block C = 6/20. CONCUR.** C3 correctly runs on 2 YoY comparisons from 3
data years rather than inventing a third.

### 1.5 Block D — re-derived

| Item | Rule band | Re-derived | Report | Verdict |
|---|---|---|---|---|
| D1 | 0-1.0x = 4 | (16.64 − 6.28)/52.62 = 0.197x → 4 | 4 | PASS (minor) |
| D2 | ≥10x = 5 | (39.50 + 1.66)/1.66 = 24.8x → 5 | 5 | PASS |
| D3 | <0.1 = 5 | 16.64/168.58 = 0.0987 → 5 | 5 | PASS (minor) |
| D4 | 1.5-1.99 = 4 | 1.84 AR-disclosed → 4 | 4 | PASS |

**Block D = 18/20. CONCUR.**

MINOR-2: D1 excludes Rs 23.23 cr of mutual-fund investments from cash.
Including them flips the company to net cash and scores 5. The report
states the exclusion and its consequence, so this is a disclosed
conservative judgment, not a concealed one. Core would move 58 → 59, still
inside 40-59.

MINOR-3: two EBITDA bases coexist in the same report. D1 uses Rs 52.62 cr
(from the FY26 audited results); the Block F margin table implies Rs 52.94
cr (21.09% of 251.01), which is what the Data_Sheet formula and the
four-quarter Operating Profit sum both give (8.41 + 14.58 + 11.73 + 18.23 =
52.95). The gap is immaterial to both scores but the report should have
said which basis governs where.

MINOR-4: D3 at 0.0987 against a 0.1 threshold is a knife-edge, and the
report itself notes the AR's own narrower D/E is exactly 10%, which scores
4. Disclosed. Core would move 58 → 57, still inside 40-59.

### 1.6 Block E — re-derived

| Item | Rule band | Re-derived | Report | Verdict |
|---|---|---|---|---|
| E1 | ≥60% = 5 | 73.85% → 5 | 5 | PASS |
| E2 | ±1% = 3 | unchanged over the ~12 months held → 3 | 3 | PASS (minor) |
| E3 | >15% = 0 | 94.4% of promoter holding (69.7% of total shares) → 0 | 0 | PASS |
| E4 | <5% = 5 | 0.1681/168.58 = 0.0997% → 5 | 5 | PASS |

**Block E = 13/20. CONCUR.**

MINOR-5: E2 asks for the change "over 3 years". Only Jun-2025, Mar-2026 and
Jun-2026 shareholding filings exist, and the company listed 11-Jun-2024, so
a 3-year window cannot exist. Prompt rule 5 ("if a data point is not
available, mark N/A and score it 0") and prompt rule 6 ("use whatever
history is available") point in opposite directions here. The report chose
rule 6, scored 3, and flagged the window as provisional in both the report
and input_gaps. I accept that as the better reading of a genuinely
conflicting pair of rules. Had E2 been zeroed, Core = 55, still AVERAGE.

**CORE SCORE = 13 + 8 + 6 + 18 + 13 = 58/100. CONCUR.**

### 1.7 Block F — the 12 moat tests, re-derived

I recomputed every peer margin myself from the four Data_Sheet.csv files
using the report's stated formula, and independently cross-checked each
against the four-quarter Operating Profit sums in each file's Quarters
block. The report's claim that this cross-check reconciles is true:

| Company | FY26 EBITDA margin, P&L rows | FY26 via 4-quarter Operating Profit | Agree? |
|---|---|---|---|
| TOTEM | 52.94/251.01 = 21.09% | 52.95/251.01 = 21.10% | yes |
| Kennametal (Jun-26) | 303.7/1510.7 = 20.10% | 303.5/1510.7 = 20.09% | yes |
| Wendt (Mar-26) | 32.43/236.32 = 13.72% | — | yes |
| Birla (Mar-26) | 17.17/247.13 = 6.95% | — | yes |

Peer median FY26 = 13.72%. Kennametal FY25 (Jul-24 to Jun-25) recomputes to
172.2/1170.4 = 14.71%, and substituting it leaves the median at 13.72%. The
sensitivity claim is true as stated.

| Test | Rule band | Re-derived | Report | Verdict |
|---|---|---|---|---|
| M1 | else = 0 | margin −1.40pp (within ±2pp) but rev CAGR 4.8% < 10%; no band fits | 0 | PASS |
| M2 | ≥5pp above peer median = 5 | 21.09 − 13.72 = +7.37pp → 5 | 5 | PASS (minor) |
| M3 | FAT>2x AND ROCE>15% = 3 | 251.01/113.40 = 2.21x, ROCE 22% → 3 | 3 | PASS |
| M4 | zero decline years AND rec days ±10 = 5 | 0 decline years; 47.0 → 43.9 → 5 | 5 | PASS |
| M5 | top 3 mcap AND margin top 2 = 3 | see finding G0-2 | 3 | **FAIL, MAJOR** |
| M6 | else = 0 | no R&D line in any of the four exports; FY26 R&D Nil per AR | 0 | PASS |
| M7 | unregulated = 0 | cutting tools not a licensed segment | 0 | PASS |
| M8 | none = 0 \| mentioned unquantified = 1 | not in this stage's inputs → 0 | 0 | PASS (minor) |
| M9 | above peers but growth below = 1 | GM 62.82% vs median 56.25% = +6.57pp; CAGR 4.81% < 8% → 1 | 1 | PASS |
| M10 | grew every year AND rec days rose ≤10 = 5 | grew every year; rec days fell 3.1 → 5 | 5 | PASS |
| M11 | <6 years, score conservatively and state so | stated, 0 | 0 | PASS |
| M12 | >45 days = 0 | 73.8 / 65.2 / 78.9, all >45 → 0 | 0 | PASS |

**FINDING G0-2 (MAJOR). M5 was scored 3 on a comparison set the report
itself says is not the segment, against the block's explicit
peer-data-missing instruction.** The Block F header rule is unambiguous:
"If a test needs peer data that is not provided, score 0 and mark PEER DATA
NEEDED (never guess peer figures)." M5's bands are written against a
segment ("largest mcap in segment", "top 3 mcap", "top 5 mcap"). What this
run holds is three named peers. "Top 3 of 4" is close to vacuous: only
Birla Precision sits below the subject, and the report's own caveat
concedes the ranking is "relative to this 4-company set, not a verified
full-segment ranking". The rule's escape hatch for exactly this situation
is score 0 / PEER DATA NEEDED, and it was not taken. To the report's
credit, no peer figure was invented and the limitation is stated plainly;
the defect is that the limitation should have produced a 0, not a flagged 3.

Recomputed: Block F = 19/60, moats present = 4 (M2, M3, M4, M10). Moat
class = **STRONG** (the 4-5 band), unchanged. Grand total = 77/160. Core
score unchanged at 58, so the classification is unchanged. MAJOR, not
CRITICAL.

MINOR-6: M2 is the single largest mover between run 1 and run 2 (0 → 5),
and with exactly three peers the "peer median" is one peer's number, Wendt's
13.72%. Wendt's own margin fell from 22.73% (FY25) to 13.72% (FY26) — a
single-year collapse. The sensitivity the report ran tests the Kennametal
year-end alignment; it does not test the fragility of resting a +7.37pp
"cost advantage" on one peer's one bad year. The rule was applied
correctly. The robustness note is missing.

MINOR-7: M8 scored 0 as "not disclosed in any filed source read this run".
That is correct for this stage's inputs. It is inconsistent with B07, which
records "200+ distributors" and "12 divisional sales offices" from the 2024
Information Memorandum (B07 Section 3, C1). Under M8's "mentioned
unquantified = 1" band that evidence would score 1. Impact: moat 22 → 23,
moats present unchanged at 5, no class change. Flagged as a corpus-scope
mismatch between stages, not as a Gate 0 rule breach.

**Block F as scored = 22/60, 5 moats, STRONG. Arithmetic re-added:
0+5+3+5+3+0+0+0+1+5+0+0 = 22. CONCUR on the arithmetic; see G0-2 on M5.**

**GRAND TOTAL = 58 + 22 = 80/160. CONCUR.**

### 1.8 The June-versus-March peer year-end question

**Verdict: defensible application, not a basis error.**

Kennametal India's FY26 column ends 30-Jun-2026 and overlaps 9 of the
subject's 12 FY26 months. The prompt's Block F says nothing about period
alignment for peer comparisons, so no rule is broken on its face. What
makes it defensible rather than merely undisclosed is that the report did
three things the framework's spirit requires: it named the misalignment
explicitly, it ran the alternative (Kennametal FY25, ended 30-Jun-2025) as
a sensitivity on every peer-dependent test, and it stated why the choice
does not bind. I verified that last claim independently and it holds:

- M2: median is 13.72% under both alignments, because Birla (6.95%) and
  Wendt (13.72%) bracket Kennametal on either choice. Score 5 either way.
- M9: median is 56.25% under both alignments (Kennametal's GM is 32.61% at
  FY26 and 44.61% at FY25, below Wendt either way). Score 1 either way.
- M5: mcap is a live snapshot, not year-end dependent; margin rank 1 for the
  subject holds under both. Score unaffected by the alignment (it is
  affected by G0-2, which is a different problem).

The one thing left unsaid: a 3-month lag matters most when the lagged
period is anomalous, and Kennametal's Jun-2026 year is exactly that — its
margin jumps 14.71% to 20.09% on a Change-in-Inventory line of Rs 225.0 cr
against Rs 21.5 cr the prior year. That did not change any score here, but
it should have been named alongside the alignment note. MINOR-8.

### 1.9 Classification, deal-breakers, confidence adjustment

| Check | Rule | Verdict |
|---|---|---|
| Matrix band | Core 40-59 = AVERAGE, flat, no moat branch | PASS. Report states the flatness correctly and notes Block F would only matter at Core 60-79 or ≥80. |
| Data confidence | 3-4 years = LIMITED, downgrade one tier | PASS. 3 years → LIMITED → one tier. |
| Deal-breaker 1 | Block A <8 → max GOOD | PASS, not triggered (13). |
| Deal-breaker 2 | Block B <8 → max GOOD | PASS, not triggered (8, at the line, correctly read as not-below). |
| Deal-breaker 3 | median ROCE <10% → max AVERAGE | PASS, not triggered (22%). |
| Deal-breaker 4 | cum CFO/PAT <0.50 → max AVERAGE | PASS, not triggered (1.01). |
| Deal-breaker 5 | pledge >15% → max AVERAGE | PASS, triggered and applied. 94.4% of promoter holding; 69.7% of total shares. Over the threshold on either denominator. |
| Deal-breaker 6 | ND/EBITDA >3x AND IC <3x → AVOID | PASS, not triggered. |
| Deal-breaker 7 | revenue declined in majority of years | PASS, not triggered. |
| Deal-breaker 8 | PAT negative in any of last 3 years | PASS, not triggered. |
| Deal-breaker 9 | history <3 years → AVERAGE | PASS, correctly NOT triggered at exactly 3 years, and correctly distinguished from the confidence downgrade. |
| "State WHICH years drive any deal-breaker" | prompt requirement | PASS. Jun-2025, Mar-2026, Jun-2026 named for the pledge. |
| Sequencing | matrix → cap → downgrade | PASS, stated explicitly. |

**Is the pledge deal-breaker double-counting the history downgrade?**
No. They key to different facts (a pledged controlling stake versus the
length of the audited record), they come from different sections of the
prompt (Deal-breaker overrides versus Data confidence), and they do
different work here. The pledge cap is non-binding on these numbers: the
matrix already produces AVERAGE, so "max AVERAGE" changes nothing. All of
the movement from AVERAGE to AVOID comes from the one-tier LIMITED-history
downgrade. The report says this in as many words ("Absent that downgrade,
the mechanical floor here is AVERAGE"), which is the correct and honest
statement of what each rule contributed. No double-count.

**Does the matrix produce AVOID from these inputs?** Yes.
Core 58 → 40-59 band → AVERAGE → pledge cap (max AVERAGE, non-binding) →
LIMITED-history downgrade one tier on the EXCELLENT / GOOD+ / GOOD /
AVERAGE / AVOID ladder → **AVOID**. Order of operations does not matter
here: capping first or downgrading first both land on AVOID.

**Robustness of AVOID against my own two MAJOR findings.** Taken together
and in the worst case (B4 → 3 and M5 → 0): Core = 60, moats = 4, class
STRONG. Matrix reads Core 60-79 + STRONG = GOOD+. Pledge cap → AVERAGE.
History downgrade → **AVOID**. The verdict is unchanged under every
combination of my findings. This is why neither finding is CRITICAL.

**recomputed_decision: none. I concur with AVOID.**

---

## PART 2 — EMERGING MOAT (B07), RULE-BY-RULE

### 2.1 Category completeness (verifier rule 3, all 23 addressed)

Counted from the Section 3 summary table: A1 A2 A3 A4 (4) + B1 B2 B3 (3) +
C1 C2 (2) + D1 D2 (2) + E1 E2 (2) + F1 F2 (2) + G1 G2 (2) + H1 H2 H3 (3) +
I1 I2 (2) = 22, plus R1 = **23 rows. All present.** Every zero-scored row
carries either "NO EVIDENCE FOUND" or an explicitly negative finding
(B1, E2, G1, G2 are recorded as evidence pointing the other way, which is
stronger than a bare NO EVIDENCE and is the correct treatment under prompt
rule 5's "never force-fit"). The Section 5 scoring table repeats all 23
rows. **PASS.**

### 2.2 Evidence multipliers against stated tiers

| Row | Body's evidence tier | Multiplier applied | Correct? |
|---|---|---|---|
| A3 | 📄 (5 named installed items across FY24-FY26 AR Annexures) | 1.0 | yes |
| B2 | 📄 (5 certifications named and scoped, FY25 AR p.28; ISO 26000 FY26 AR p.40) | 1.0 | yes |
| C1 | 📄 + 🎙️ mixed, 🎙️ in the majority | 0.7 | yes, and conservative |
| F2 | 📄 for the capex-completion leg (AR Annexures + CWIP no-overdue note) | 1.0 | yes |
| H3 | 📄 (solar kWh disclosed, FY26 AR p.40) | 1.0 | yes |

No row scores a 🎙️-only or 🔍-only category at 📄 weight. C1 is the only
mixed row and it takes the lower multiplier. **PASS on verifier rule 3's
specific test.**

Likelihood x impact values: A3 HM = 3 ✓, B2 HM = 3 ✓, C1 ML = 1 ✓,
F2 MM = 2 ✓, H3 = 1 ✓.

MINOR-9: H3's matrix label reads "1 (LM)" while the same row states
Likelihood Medium and Impact Low, which is ML. ML and LM both map to 1, so
the value is right and the label is wrong. Presentational only.

Adjusted total re-added: 3.0 + 3.0 + 0.7 + 2.0 + 1.0 = **9.7**. CONCUR.

Classification: 9.7 < 12 → **NO MEANINGFUL EMERGING MOAT**. The bands were
applied absolutely per the 20-Aug-2026 operator ruling, with no rescale
against the 92 ceiling, which is what the ruling requires. **PASS.**

### 2.3 Completionist guard

The mandated line is present and in the mandated form: "📄 recount
performed: 15 documented items across 5 categories", itemised per category
(A3: 5, B2: 6, F2: 2, C1: 1, H3: 1 = 15, which re-adds correctly). The
guard's base rate (3 to 6 categories with genuine evidence) is quoted and
the result checked against it. The recount was performed even though the
guard's trigger condition (12+ active categories) never fired, which is
what the Section 3 summary instruction separately requires. **PASS.**

A sparse scan is not itself a finding. This one is sparse *and* complete:
every one of the 23 rows was visited, five carry evidence, three clear the
bar. Nothing was skipped.

### 2.4 Categories 21 and 22 (verifier rule 8)

**I1 TALENT ASYMMETRY — present, scored 0, gate correctly applied.** The
rule permits a score above 0 only when both legs are evidenced and the (b)
leg carries at least one 📄 source. The report finds neither leg: no named
inventor (no patents exist, per A2), no verifiable ex-DRDO / ex-HAL /
ex-global-major concentration, and no remuneration annexure showing
technical staff paid above sector norms. It scores 0 and states the reason
in the category's own terms ("a hiring/organisation story with no
structural-economics leg, exactly the pattern the category is built to
exclude"). **PASS.**

**I2 CANNIBALIZATION BARRIER — present, scored 0, gate correctly applied.**
The rule requires the score to be 0 when the honest answer is "nothing must
be destroyed". The report runs the test against its own findings (A3 and
B2), concludes both need only capital and calendar time to replicate
because Kennametal already holds equivalent certifications and process
technology, and scores 0. It also correctly excludes F2 from I2 credit,
citing the category's own rule that an execution lead is configuration-free
and closes. **PASS.**

**I1/I2 contribution stated separately: 0.0, with the operator's review
checkpoint named.** Required by the Section 5 ruling. **PASS.** No
threshold was crossed via I1/I2 points on this name, which is the fact the
checkpoint wants recorded.

### 2.5 Section completeness and remaining rules

| Rule | Verdict | Note |
|---|---|---|
| All six sections executed in one response | PASS | Sections 1-6 all present, plus the Optionality Register. |
| 1A status taxonomy, 1B direction, 1C mix table | PASS | 1C correctly returns NOT FOUND at the numeric level with the one-segment AR note anchored (FY26 AR Note 38, p.126), rather than fabricating a mix. |
| 2A capex table with all seven columns | PASS | Undisclosed cells carry NOT FOUND, not estimates. |
| 2B utilisation | PASS | NOT FOUND, with the reason (no utilisation % published, single plant). |
| 2C arithmetic shown | PASS | Rs 3.56 cr CWIP x 2.32x / Rs 251.01 cr = 3.3%. The choice to use CWIP only ("capex still under execution") is the literal reading of the rule and the report explains why the commissioned Rs 14.99 cr is realised, not embedded, growth. Correct and unusually well reasoned. |
| 2D new geography | PASS | Correctly classified as re-entry, not first entry, and scored as such. |
| Section 4 / R1 4A-4C | PASS | R1 = 0 on the "whether competitors share the benefit" test, which is the rule's own criterion. |
| Section 3 summary: 23 rows, evidence?, type, strength, time | PASS | All four columns populated. |
| Count with Strong/Moderate stated | PASS | 3 (A3, B2, F2). |
| Optionality register: 4 columns, only 0-scored or 🎙️/🔍-only rows | PASS | 5 rows (A4, G1, I1, H1, E2), all zero-scored. C1 and H3 correctly excluded, since both carry a 📄 item. |
| Section 6, 6A-6E, incl. HIGH POTENTIAL / TURNAROUND reasoning | PASS | Both were explicitly considered and rejected with reasons, which the rule requires. 6C correctly quotes the injected B01 block (Core 58, 5/12, 22/60, STRONG). |
| Emerging-Moat / FTTCP separation (CLAUDE.md) | PASS | Stated at the head of the report. |
| YAML schema | PASS (minor) | All mandated fields present and correctly typed. |

MINOR-10: two fields not in the prompt's schema were added to B07-emoat.yaml
(`em_score_scale`, `capex_embedded_growth_basis`). The prompt says "exactly
this fenced YAML block". Both additions are useful and neither displaces a
mandated field; recorded so the schema drift is visible.

MINOR-11: `evidence_mix: {documented: 15, claim: 1, inference: 0}` is scoped
to the five evidenced categories only, and matches the completionist
recount on that scope. The report body carries at least eight further 🎙️
items (1A tapping geometries, 1B geographic and vertical, four 1C
directional reads, 2D re-entry) and at least six labelled 🔍 inferences (A3,
B2, F2, 2C, the 1C export-share computation, the 2A ~6.7% capacity
arithmetic). `inference: 0` is therefore true of the scored rows and false
of the document. The scoping is defensible; it is not stated.

### 2.6 Consistency between the B07 report and the B07 block

em_score 9.7 ✓, em_classification NONE ✓, three active_categories matching
the three Strong/Moderate rows ✓, capex_embedded_growth_pct 3.3 matching
2C ✓, five optionality rows matching the register ✓, combined_assessment
AVOID matching 6D ✓, completionist_recount line carried ✓. No drift.

**recomputed em_score: none. I concur with 9.7 and NONE.**

---

## PART 3 — RULE 6, B09 DOWNSTREAM CANDIDATES (BLOCK REQUIREMENT ONLY)

The rule: B09 contains `downstream_candidates` with ≥3 items, OR
`demand_externally_verifiable: false` with the exact sentence present.
Missing block = REWORK for stage 9.

B09-tam.yaml contains `downstream_candidates` with **6 items** (IMTMA
machine-tool data, SIAM automotive volumes, Kennametal India quarterly
results, US/Mexico tariff policy, HSS/tungsten-carbide import prices,
defence and aerospace procurement). Each carries signal, entity_type,
demand_link, likely_source, cadence and shared. `demand_externally_verifiable`
is true, consistent with a populated candidate list.

**PASS. No REWORK trigger for stage 9.** The second half of rule 6 (stage 11
catalysts each citing a candidate or carrying the MODERATE cap) is phase 3
and was not assessed.

---

## FINDINGS SUMMARY

| # | Severity | Location | Finding | Recomputed |
|---|---|---|---|---|
| G0-1 | MAJOR | 01-gate0.md, Block B, B4 | Stated delta "+5.0 days" scores the "increased 5-15" band (1); on the report's own displayed value the ±5 band gives 3. Exact recomputation is +5.01 days, so the score survives by 0.01 of a day. Boundary call not stated or defended. | B4 = 1 or 3; Block B = 8 or 10; Core = 58 or 60. Classification AVOID either way. |
| G0-2 | MAJOR | 01-gate0.md, Block F, M5 | Scored 3 for "top 3 mcap" on a 4-company set the report itself says is not the segment. Block F's own rule for missing peer data is score 0 / PEER DATA NEEDED. | M5 = 0; Block F = 19/60; moats = 4; class STRONG unchanged; grand total 77/160; classification AVOID unchanged. |
| G0-3 | MINOR | 01-gate0.md line 30 | "Data available" opening line placed behind a run-2 preamble rather than opening the report. | — |
| G0-4 | MINOR | 01-gate0.md, D1 | Rs 23.23 cr mutual funds excluded from cash; including them scores 5 (net cash). Disclosed. | Core 59, band unchanged. |
| G0-5 | MINOR | 01-gate0.md, D1 vs Block F | Two FY26 EBITDA bases coexist, Rs 52.62 cr and Rs 52.94 cr; governing basis not declared. | Immaterial to both scores. |
| G0-6 | MINOR | 01-gate0.md, D3 | 0.0987 against a 0.1 threshold; the AR's own 10% would score 4. Disclosed. | Core 57, band unchanged. |
| G0-7 | MINOR | 01-gate0.md, E2 | 3-year rule scored on a ~12-month window. Prompt rules 5 and 6 conflict; rule 6 chosen and flagged provisional. Accepted. | Core 55, band unchanged. |
| G0-8 | MINOR | 01-gate0.md, Block F, M2 | Peer median with three peers is one peer's number (Wendt 13.72%), and Wendt's margin collapsed from 22.73% in one year. Alignment sensitivity was run; single-peer fragility was not. | No score change. |
| G0-9 | MINOR | 01-gate0.md, Block F, M8 | Scored 0 as not disclosed; B07 records 200+ distributors and 12 sales offices from the 2024 IM, which would score 1 under "mentioned unquantified". Corpus-scope mismatch between stages. | Moat 23/60, moats present unchanged. |
| G0-10 | MINOR | 01-gate0.md, peer alignment note | Kennametal's Jun-2026 year is itself anomalous (Change in Inventory Rs 225.0 cr vs Rs 21.5 cr prior). Not named beside the alignment disclosure. | No score change. |
| EM-1 | MINOR | 07-emoat.md, Section 5, H3 | Matrix label "(LM)" against a stated Medium likelihood / Low impact (ML). Both map to 1. | No score change. |
| EM-2 | MINOR | B07-emoat.yaml | Two non-schema fields added (em_score_scale, capex_embedded_growth_basis). | — |
| EM-3 | MINOR | B07-emoat.yaml | evidence_mix scoped to the five evidenced rows; `inference: 0` is false of the document, which carries ≥6 labelled 🔍 items. Scoping defensible, unstated. | — |

CRITICAL: 0. MAJOR: 2. MINOR: 11.

## COVERAGE AND ACCEPTANCE

Rules checked: 42 Gate 0, 19 Emerging Moat, 1 B09 block requirement = 62.
A rule is counted failed when it produced a MAJOR or CRITICAL finding.
Passed 60 of 62 = **96.8%**. On the stricter convention where any finding
(including MINOR) counts against the rule, 51 of 62 = 82.3%. Both are well
clear of the 60% REWORK threshold.

No REWORK trigger fires from this verifier. Stage 7 categories 21 and 22
are present and correctly gated (no stage 7 REWORK). B09's
downstream_candidates block is present with 6 items (no stage 9 REWORK).

## WHAT I DID NOT AUDIT

Valuation adherence (verifier rule 4), method plurality in B11 (rule 7),
the stage 13 Business Understanding Narrative (rule 9), the Expectation
Ledger and decomposition gates (rules 13-14), and Role 1 exit construction
(rules 11-12): all deferred to phase 3, when B10 and B11 exist. The Halt 1
dossier structural check (rule 10) is run mechanically by the orchestrator
at step 6b and is outside this invocation. Whether a cited number exists in
its source PDF is Verifier A's non-overridable call, not mine; where I
re-derived figures above, I did so from the CSVs and page-marked text to
test rule application, not to adjudicate source fidelity.

---

```yaml
stage: B12c
company: "TOTEM"
run_date: "2026-09-09"
model: claude-opus-4-8
status: complete
scope: "phase-1 (Gate 0 + Emerging Moat + B09 block requirement); valuation audit deferred to phase 3"
gate0:
  rules_checked: 42
  fails:
    - {rule: "Block B / B4 change in WC days", severity: "MAJOR", detail: "Stated delta '+5.0 days' scored under the 'increased 5-15' band (1); the ±5 band gives 3 on that same displayed value. Exact recomputation from Data_Sheet receivables/inventory and AR trade payables is +5.01 days (FY24 73.82, FY26 78.83), so the score survives by 0.01 of a day. Boundary call neither stated nor defended.", recomputed: "B4 = 1 or 3; Block B = 8 or 10; Core = 58 or 60; classification AVOID either way"}
    - {rule: "Block F / M5 Scale & Dominance + the 'peer data not provided -> score 0, mark PEER DATA NEEDED' rule", severity: "MAJOR", detail: "Scored 3 for 'top 3 mcap AND margin top 2' on a 4-company set the report itself concedes is not the segment. M5's bands are written against a segment ranking that this run does not hold.", recomputed: "M5 = 0; Block F = 19/60; moats present = 4; moat class STRONG unchanged; grand total 77/160; classification AVOID unchanged"}
emoat:
  rules_checked: 19
  fails: []
b09_downstream_candidates: {present: true, item_count: 6, demand_externally_verifiable: true, rework_stage9: false}
categories_21_22: {i1_present: true, i1_score: 0, i1_gate_ok: true, i2_present: true, i2_score: 0, i2_gate_ok: true, rework_stage7: false}
valuation: {rules_checked: 0, fails: [], status: "PENDING PHASE 3 - B10/B11 do not exist yet"}
expectation_ledger: {status: "PENDING PHASE 3"}
business_understanding_narrative: {status: "PENDING PHASE 3 - stage 13 has not run"}
recomputed_destination_pe: ""
recomputed_decision: ""
recomputed_gate0_classification: "AVOID (concur)"
recomputed_gate0_core: 58
recomputed_gate0_moat_class: "STRONG (concur; holds at 4 moats if M5 is corrected to 0)"
recomputed_em_score: 9.7
recomputed_em_classification: "NONE (concur)"
findings:
  - {severity: "MAJOR", location: "01-gate0.md Block B, B4", note: "Displayed delta +5.0 contradicts the band applied (1). True delta +5.01 days. Core crosses a matrix band if scored 3; final classification unchanged."}
  - {severity: "MAJOR", location: "01-gate0.md Block F, M5", note: "Segment ranking scored on a 3-peer set; Block F's missing-peer-data rule requires 0 / PEER DATA NEEDED. Moat class and classification unchanged."}
  - {severity: "MINOR", location: "01-gate0.md line 30", note: "'Data available' line not the opening line; sits behind the run-2 preamble."}
  - {severity: "MINOR", location: "01-gate0.md D1", note: "Rs 23.23 cr mutual funds excluded from cash; including them scores 5. Disclosed judgment."}
  - {severity: "MINOR", location: "01-gate0.md D1 vs Block F", note: "Two FY26 EBITDA bases coexist (52.62 and 52.94); governing basis not declared."}
  - {severity: "MINOR", location: "01-gate0.md D3", note: "D/E 0.0987 against a 0.1 threshold; AR's own 10% scores 4. Disclosed."}
  - {severity: "MINOR", location: "01-gate0.md E2", note: "3-year promoter-holding-change rule scored on a ~12-month window. Prompt rules 5 and 6 conflict; rule 6 chosen and flagged provisional. Accepted."}
  - {severity: "MINOR", location: "01-gate0.md Block F, M2", note: "With 3 peers the median is Wendt alone (13.72%), whose margin fell from 22.73% in one year. Year-end sensitivity run; single-peer fragility not tested."}
  - {severity: "MINOR", location: "01-gate0.md Block F, M8", note: "Scored 0 as not disclosed; B07 records 200+ distributors and 12 sales offices from the 2024 IM, which scores 1 under 'mentioned unquantified'. Cross-stage corpus-scope mismatch."}
  - {severity: "MINOR", location: "01-gate0.md peer-alignment note", note: "Kennametal's Jun-2026 year carries a Rs 225.0 cr Change in Inventory vs Rs 21.5 cr prior; the anomaly is not named beside the year-end alignment disclosure."}
  - {severity: "MINOR", location: "07-emoat.md Section 5, H3", note: "Matrix label '(LM)' against stated Medium likelihood / Low impact (ML). Both map to 1; value correct."}
  - {severity: "MINOR", location: "B07-emoat.yaml", note: "Two non-schema fields added (em_score_scale, capex_embedded_growth_basis)."}
  - {severity: "MINOR", location: "B07-emoat.yaml evidence_mix", note: "Scoped to the five evidenced rows only; inference: 0 is false of the document, which carries at least six labelled analyst inferences. Scoping defensible, unstated."}
critical_count: 0
major_count: 2
minor_count: 11
acceptance_rate: 97
acceptance_note: "60 of 62 rules passed (96.8%), counting a rule failed only on a MAJOR or CRITICAL finding. On the stricter convention where any finding counts against the rule, 51 of 62 = 82.3%. Both clear the 60% REWORK threshold."
peer_year_end_verdict: "DEFENSIBLE, not a basis error. Kennametal's Jun-FYE misalignment was named, a FY25 sensitivity was run on every peer-dependent test, and I independently confirmed the peer median is 13.72% (M2) and 56.25% (M9) under both alignments, so no score moves."
deal_breaker_double_count_verdict: "NO DOUBLE-COUNT. Pledge cap (max AVERAGE) and LIMITED-history downgrade (one tier) key to different facts and different prompt sections. The pledge cap is non-binding on a Core of 58; all movement from AVERAGE to AVOID comes from the history downgrade, and the report states this."
classification_matrix_verdict: "CONFIRMED. Core 58 -> 40-59 AVERAGE (flat band, no moat branch) -> pledge cap (non-binding) -> one-tier LIMITED-history downgrade -> AVOID. Robust to both MAJOR findings applied together (Core 60 + STRONG = GOOD+ -> cap AVERAGE -> downgrade -> AVOID)."
emoat_completeness_verdict: "CONFIRMED. All 23 rows addressed, 18 as NO EVIDENCE FOUND or explicitly negative. 5 rows carry evidence, 3 clear Strong/Moderate. Completionist recount performed and itemised (15 documented items across 5 categories). No category skipped. Sparse and complete."
```
