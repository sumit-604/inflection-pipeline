# STAGE 12C: VERIFIER C — FRAMEWORK ADHERENCE (PHASE 1 SCOPE)

Company: AEQUS (Aequs Ltd). Run date: 2026-09-05.
Scope: Gate 0 (B01) against prompts/01-gate-0-pipeline.md, and Emerging Moat
(B07) against prompts/07-emerging-moat-pipeline.md. The valuation audit (B10,
B11) is DEFERRED to phase 3. No frameworks/ document was opened; none is in
scope for this run.

Artifacts audited:
- /home/user/inflection-pipeline/runs/aequs-2026-09-05/outputs/reports/01-gate0.md
- /home/user/inflection-pipeline/runs/aequs-2026-09-05/outputs/blocks/B01-gate0.yaml
- /home/user/inflection-pipeline/runs/aequs-2026-09-05/outputs/reports/07-emoat.md
- /home/user/inflection-pipeline/runs/aequs-2026-09-05/outputs/blocks/B07-emoat.yaml

Boundary honoured: I audit rule application. I do not adjudicate whether a
number exists in a source PDF. That is Verifier A's non-overridable gate. Where
a finding below touches a number, it touches which number the rule selects, not
whether the number is real.

Model note: the B12c schema fixes `model: claude-opus-4-8`. I emit the schema
value. The executing model string differs from that fixed template value.

---

## PART 1 — GATE 0 (B01) COMPLIANCE

63 rule checks. 57 PASS, 6 FAIL. Adherence 90%.

### 1.1 Operating rules and formula definitions (11 checks)

| # | Rule (source line) | Verdict | Note / recomputed value |
|---|---|---|---|
| G01 | Opening "Data available: X years (FY__ to FY__)" line, prompt L25-26 | PASS | "Data available: 4 years (FY23 to FY26)... Scoring adapted to 4-year history" (01-gate0.md L6-7) |
| G02 | Source anchor on every extracted number, prompt L15-19 | PASS | Blocks A-E anchored to (screener-data) or (AR p.227/231/252/282). One moat-test gap handled at G53 |
| G03 | Grounded claims; missing data = "N/A (not in provided data)", score 0, prompt L20-23 | PASS | E1/E2/E3 marked N/A and scored 0 (L146-148). No gap filled with an estimate |
| G04 | Use whatever history exists, min 3 years, prompt L24-26 | PASS | 4 years used; the 2-year sub-constraint on ROCE/WC/FCF is declared up front (L8-13), not silently narrowed |
| G05 | ROCE = EBIT ÷ (Total Assets − Current Liabilities); use source ROCE if provided, else state "computed", prompt L30-32 | PASS | Screener Data_Sheet carries no ratios tab; computed and stated (L23-27) |
| G06 | ROE = PAT ÷ average Net Worth; earliest year may use closing, state so, prompt L33-34 | PASS | FY23 uses closing NW 278.61 and says so (L37-39) |
| G07 | WC Days = Rec + Inv − Pay, state revenue vs COGS basis, prompt L35-39 | PASS | Revenue basis stated ("COGS not separately disclosed", L73) |
| G08 | FCF = CFO − capex, capex = purchase of PPE **+ intangibles**, exclude acquisitions, prompt L40-41 | **FAIL** | Capex taken as "Acquisition of property, plant and equipment" alone (L59-61). The intangibles leg of the definition is neither included nor declared absent. Direction of error unknown but small; FY25/FY26 FCF are −239.02 and −441.30, both far from the B2/B3 band edges, so no score moves |
| G09 | CAGR = (End ÷ Start)^(1/years) − 1, prompt L42 | PASS | C1 recomputed: (1230.44/812.13)^(1/3) − 1 = 14.85%. Concur |
| G10 | CAGR edge rule: negative/zero endpoint → "N/M", score 0, prompt L45-46 | PASS | C2 endpoints −98.83 and −113.25; marked N/M, scored 0 (L90-91) |
| G11 | CAGR edge rule: loss-to-profit swing noted in data_notes, prompt L47-49 | PASS | No swing occurred; the report states so affirmatively in data_notes rather than staying silent |

### 1.2 Block A — Return on Capital (5 checks)

Inputs restated: ROCE FY25 −2.51%, FY26 1.22% (2 of 4 years computable).

| # | Line | Stated | Re-derived | Verdict |
|---|---|---|---|---|
| G12 | A1 median ROCE | 0 | median(−2.51, 1.22) = −0.65% → <10% → 0 | PASS |
| G13 | A2 minimum single-year ROCE | 0 | −2.51% → <8% → 0 | PASS |
| G14 | A3 median ROE | 0 | −35.47, −3.15, −18.17, −10.28 → median (−18.17 + −10.28)/2 = −14.23% → <12% → 0. Averaging NW recomputed at each year and ties out | PASS |
| G15 | A4 ROCE trend latest vs earliest | 5 | FY26 1.22% ≥ FY25 −2.51% → 5. Applied as written on the only computable window; the report flags the 2-year limitation itself (L44-46) | PASS |
| G16 | Block A total | 5/20 | 0+0+0+5 = 5 | PASS |

### 1.3 Block B — Cash Generation Quality (5 checks)

| # | Line | Stated | Re-derived | Verdict |
|---|---|---|---|---|
| G17 | B1 cumulative CFO ÷ cumulative PAT | 0 | CFO sum −81.91; PAT sum −325.27; ratio 0.2518 → <0.50 → 0 | PASS |
| G18 | B2 FCF-positive years proportion | 0 | 0 of 2 computable years positive → <50% → 0 | PASS |
| G19 | B3 cumulative FCF ÷ cumulative PAT | 0 | cum FCF −680.32, cum PAT −215.60, arithmetic ratio +3.155 | **FAIL** (see below) |
| G20 | B4 change in WC days | 0 | 131.87 → 151.44 = +19.57 days → increased >15 → 0 | PASS |
| G21 | Block B total | 0/20 | 0+0+0+0 = 0 | PASS |

G19 detail. The band reads "≥0.60 = 5 ... <0.20 or negative = 0". The report
reached 0 by declaring an **override** of the band (L64-69, and data_notes entry
3). Stage operating rule 2 forbids qualitative judgments. The correct route to
the same answer is the band's own "or negative" clause read against the negative
cumulative FCF, not an override. Outcome 0 stands and is the conservative
reading; the justification is off-rule. Recomputed value under a literal
ratio-only reading would be 5, giving Block B 5/20 and core 30/80 — still
below 40, so the classification does not move. Graded MINOR, with a
recommendation that the framework text disambiguate what "negative" attaches to.

### 1.4 Block C — Growth (5 checks)

| # | Line | Stated | Re-derived | Verdict |
|---|---|---|---|---|
| G22 | C1 revenue CAGR | 3 | 14.85% → 10-14.9 → 3 | PASS |
| G23 | C2 PAT CAGR | 0 | N/M, negative endpoints → 0 | PASS |
| G24 | C3 positive YoY revenue years | 1 | 2 of 3 = 66.7% → 50-74 → 1 | PASS |
| G25 | C4 PAT CAGR minus revenue CAGR | 0 | PAT CAGR N/M → C4 = 0 per prompt L51, and noted | PASS |
| G26 | Block C total | 4/20 | 3+0+1+0 = 4 | PASS |

### 1.5 Block D — Balance Sheet Strength (5 checks)

| # | Line | Stated | Re-derived | Verdict |
|---|---|---|---|---|
| G27 | D1 Net Debt ÷ EBITDA | 3 | 250.05 ÷ 160.56 = 1.56x → 1-2x → 3 on the chosen input | **FAIL** on input basis (see below) |
| G28 | D2 interest coverage | 0 | 22.87 ÷ 94.36 = 0.24x → <1.5 → 0 | PASS |
| G29 | D3 Debt ÷ Equity | 4 | 700.93 ÷ 1,486.49 = 0.4716 → 0.1-0.5 → 4 | PASS |
| G30 | D4 current ratio | 4 | 1,303.03 ÷ 822.65 = 1.584 → 1.5-1.99 → 4 | PASS |
| G31 | Block D total | 11/20 | 3+0+4+4 = 11 as stated | PASS |

G27 detail, the run's largest Gate 0 finding. D1 uses net debt Rs 250.05 cr (AR
Note 29, p.282), which excludes lease liabilities: 403.58 borrowings less cash
gives 250.05, and 250.05 ÷ 1,486.49 = 0.17x, the ratio the report
cross-validates against. D3, one line below, uses debt of Rs 700.93 cr, which
**includes** Rs 297.35 cr of lease liabilities. The same block therefore prices
leases as debt in D3 and not in D1, on the same date.

The lease-inclusive reading is not merely the screener's: B07 cites the AR's own
p.46 net debt/equity of 0.23x for FY26 (07-emoat.md L288-289). At equity
1,486.49, 0.23x implies net debt of about Rs 342 cr, which is the screener
figure (Rs 344.28 cr) the report declined to use. Two AR pages carry two net
debt definitions and the report selected the lower one without reconciling
them.

Recomputed on the lease-inclusive basis: 344.28 ÷ 160.56 = **2.14x → band 2-3x
→ D1 = 1**. Block D = 9/20. Core score = **23/80**. Grand total = **32/140**.
Classification **unchanged: AVOID** (core still <40). Deal-breaker 6 still does
not fire (2.14x does not exceed 3x). Decision survives, so MAJOR, not CRITICAL.

### 1.6 Block E — Shareholder Alignment (5 checks)

| # | Line | Stated | Re-derived | Verdict |
|---|---|---|---|---|
| G32 | E1 promoter holding | 0 | Shareholding ABSENT → N/A → 0 per prompt L20-23 | PASS |
| G33 | E2 promoter holding change | 0 | ABSENT → N/A → 0 | PASS |
| G34 | E3 promoter pledge | 0 | ABSENT → N/A → 0 | PASS |
| G35 | E4 contingent liabilities ÷ net worth | 5 | 14.96 ÷ 1,486.49 = 1.01% → <5% → 5 | PASS |
| G36 | Block E total | 5/20 | 0+0+0+5 = 5 | PASS |

Note, not a fail: E4 excludes unquantified related-party corporate guarantees
(AR Note 30(x), Note 34) and says so. Excluding an unquantified item is correct
under prompt L20-23; the caveat is carried.

### 1.7 Core score (1 check)

| # | Item | Stated | Re-derived | Verdict |
|---|---|---|---|---|
| G37 | Core = A+B+C+D+E | 25/80 | 5+0+4+11+5 = 25 | PASS (23 under the G27 recomputation) |

### 1.8 Block F — 12 moat tests (12 checks)

| # | Test | Stated | Re-derived | Verdict |
|---|---|---|---|---|
| G38 | M1 pricing power | 5 | Margin 7.96% → 13.05% = +5.09pp (≥2pp) AND revenue CAGR 14.85% (≥10%) → 5 | PASS |
| G39 | M2 cost advantage | 0 | Peer median of 3 peers = 44.94%; AEQUS 13.05% below → 0. Ex-other-income cross-check shown | PASS |
| G40 | M3 capital efficiency | 0 | FAT 1.15x >1x but ROCE 1.22% fails >12% → else → 0 | PASS |
| G41 | M4 customer stickiness | 3 | 1 decline year, fully recovered → 3 | PASS |
| G42 | M5 scale and dominance | 1 | #2 of 4 by mcap but margin last, so the "top 3 mcap AND margin top 2" tier fails; "top 5 mcap" → 1 | PASS |
| G43 | M6 technology / R&D | 0 | R&D expenditure NIL → 0 | PASS on score |
| G44 | M7 regulatory / licence | 0 | Classified unregulated, with the alternative reading tested and shown to fail the stability bands either way | PASS |
| G45 | M8 distribution | 0 | No outlet model → 0 | PASS |
| G46 | M9 brand | 0 | GM proxy declared as prompt L126 requires; 57.55% vs peer median 74.55% → at/below → 0 | PASS |
| G47 | M10 switching costs | 0 | Growth-all-but-one-year met, receivable days +16.7 fails the stable leg; the "2+ decline years" tier does not apply at 1 decline year, so else → 0 | PASS |
| G48 | M11 network effects | 0 | <6 years available; scored conservatively and stated so per prompt L130-131 | PASS |
| G49 | M12 negative WC / float | 0 | 131.9 and 151.4 days, both >45 → 0 | PASS |

Observation on G38, not a fail. M1 = 5 depends on an EBITDA basis that includes
other income. The report declares the basis and validates it against the
company-reported FY26 EBITDA of Rs 154.5 cr, so the choice is anchored. But an
ex-other-income basis would put FY26 at 7.46% (the report's own M2 figure)
against FY23 at 7.96% incl. other income, which would not clear the +2pp
expansion test. If M1 fell to 1, moats_confirmed would fall to 1 and moat_class
would move MODERATE → THIN. Classification stays AVOID either way. The
non-monotonic margin path (7.96 → 17.88 → 7.97 → 13.05) is flagged by the maker.
Recorded for Verifier A and the operator, not scored as a fail.

### 1.9 Moat aggregation and classification (7 checks)

| # | Rule | Stated | Re-derived | Verdict |
|---|---|---|---|---|
| G50 | Moat score sum | 9/60 | 5+0+0+3+1+0+0+0+0+0+0+0 = 9 | PASS |
| G51 | Moats present at score ≥3 | 2 | M1 (5), M4 (3) → 2 | PASS |
| G52 | Moat class band, prompt L138-139 | MODERATE | 2 present → 2-3 band → MODERATE | PASS |
| G53 | "PEER DATA NEEDED" rule, prompt L100-101 | none | Peer Data_Sheets present and used for M2/M5/M9; data_notes records "PEER DATA NEEDED: none" | PASS |
| G54 | Anchor completeness on moat tests, prompt L15-19 | — | M6 cites "(AR p.?, Directors' Report technology-absorption section, grep-located, page marker not captured)" (L176). An anchor without a page is not an anchor | **FAIL** (MINOR; score 0 is not in doubt) |
| G55 | Grand total | 34/140 | 25 + 9 = 34 | PASS (32 under G27) |
| G56 | Data confidence band and history_downgrade, prompt L143-145 | LIMITED, true | 4 years → "3-4 LIMITED, downgrade one tier"; history_downgrade true; AVOID is the matrix floor so the downgrade is inert, and the report says so | PASS |

### 1.10 Classification, deal-breakers, output (7 checks)

| # | Rule | Stated | Re-derived | Verdict |
|---|---|---|---|---|
| G57 | Classification matrix, prompt L147-150 | AVOID | Core 25 <40 → AVOID | PASS |
| G58 | Deal-breakers 1-9 evaluated, prompt L156-160 | 1,2,3,4,8 fire | Recomputed: 1 (A=5<8) fires; 2 (B=0<8) fires; 3 (median ROCE −0.65%<10%) fires; 4 (CFO/PAT 0.25<0.50) fires; 5 not evaluable, data absent, correctly stated; 6 does not fire at 1.56x and still does not fire at the recomputed 2.14x; 7 does not fire (1 of 3 YoY declines); 8 fires (PAT negative FY24, FY25, FY26); 9 does not fire (4 years). All nine addressed | PASS |
| G59 | "State WHICH years drive any deal-breaker", prompt L155 | partial | Only entry 8 names its years. Entries 1, 2, 3, 4 carry values but no driving years, and entries 3 and 4 rest on materially different windows (median ROCE on FY25-FY26 only; CFO/PAT on FY23-FY26). The windows appear in data_notes but not against the deal-breaker | **FAIL** (MINOR) |
| G60 | Dashboard output format, prompt L163-166 | — | All blocks, line items with anchors, moat profile bars, classification box, strongest/weakest block, decision line all present | PASS |
| G61 | B01 YAML matches the schema field set exactly, prompt L167-199 | — | All 21 schema fields present, plus one field the schema does not define: `freshness_verdict: FRESHNESS PAIRS OK` (B01-gate0.yaml L19). B07's block carries no equivalent | **FAIL** (MINOR) |
| G62 | Block file matches the report's handoff block | — | B01-gate0.yaml is byte-equivalent to 01-gate0.md L322-396 on every field checked: blocks, core_score 25, moat_score 9, grand_total 34, moats_confirmed 2, moat_class, classification, deal_breakers, history_downgrade, data_years 4, fy_range, all 12 input_gaps, all 12 data_notes | PASS |
| G63 | flags rule and analyst_note cap, prompt L176-198 | — | FLAG-GATE0 required at classification ≤ AVERAGE with depressors named: present, with six named depressors. analyst_note is about 170 words, inside the 200-word cap. block_b_trend gives "deteriorating" plus the CFO swing number | PASS |

### 1.11 Gate 0 verdict

Score arithmetic is clean end to end. Every block total, the core score, the
moat score, the moat class, the classification matrix, the CAGR edge rules and
all nine deal-breakers re-derive to the stated values. The AVOID classification
stands under my recomputation and under every sensitivity I tested.

The one substantive adherence failure is the D1 net-debt basis, which is
internally inconsistent with D3 and selects the lower of two AR figures. It
costs 2 points and changes nothing.

---

## PART 2 — EMERGING MOAT (B07) COMPLIANCE

67 rule checks. 55 PASS, 12 FAIL. Adherence 82%. Two further findings are
recorded as framework gaps and are NOT counted as adherence failures.

### 2.1 Pipeline operating rules (6 checks)

| # | Rule (source line) | Verdict | Note |
|---|---|---|---|
| E01 | All six sections in one response, prompt L28 | PASS | Sections 1-6 plus the Optionality Register all present |
| E02 | Evidence taxonomy applied to every item, prompt L29-34 | PASS | Declared at L10-14 and carried per item throughout |
| E03 | Source anchors on every evidence item, prompt L35-36 | **FAIL** | Two anchors carry no page: A2 "(AR Board's Report, Form B)" (L150-151) and the 4B SEZ line "(AR consolidated tax reconciliation)" (L450). Both are MINOR; neither carries a score |
| E04 | Be skeptical, prioritise hard evidence, prompt L37-38 | PASS | Strong evidence of skepticism: B1, G1 and G2 are scored down explicitly because the evidence found argues against the category |
| E05 | "NO EVIDENCE FOUND" where absent, never force-fit, prompt L39-40 | PASS | Stated for A2, B3, D1, D2, H1, I1, I2 |
| E06 | Completionist guard: recount 📄 items before finalising, prompt L41-46 | PASS | Recount line present (L411-432). Under the block schema's own definition of "active" (Strong/Moderate rows), 7 active is well under the 12 alarm. Noted: 16 of 23 rows score above zero, so the guard's alarm depends on which definition of "active" is used; the maker used the schema's and did the recount anyway |

### 2.2 Sections 1 and 2 (7 checks)

| # | Rule | Verdict | Note |
|---|---|---|---|
| E07 | 1A pipeline table with status, evidence type, launch, revenue potential, differentiation | PASS | Five rows, all six columns, NOT FOUND used for absent revenue figures |
| E08 | 1B diversification direction with evidence and timeline | PASS | Five directions, each tiered |
| E09 | 1C revenue mix table: current %, expected % in 3 years, margin direction, profit impact | PASS | 3-year figure declared NOT FOUND first, then an interpolation offered and explicitly tagged 🔍 "not a management figure". It enters no score. The no-estimate rule is honoured because NOT FOUND is stated and the inference is labelled |
| E10 | 2A capex programme table | PASS | Five projects with funding source, status, commissioning, capacity. The Rs 21.01 cr audited commitment versus Rs 660 cr guidance tension is surfaced, not blended (L63-70) |
| E11 | 2B utilisation trajectory per facility | PASS | Both facilities, with the three-source reconciliation failure flagged rather than smoothed |
| E12 | 2C arithmetic shown | PASS on arithmetic | 660 × 1.18 = 778.8; 778.8 ÷ 1,230.44 = 63.3%. Ties out |
| E13 | 2C input is "total capex under execution", prompt L61-63 | **FAIL** | See below |

E13 detail. The rule specifies capex **under execution**. The report uses the
FY27 capex **guidance** of Rs 660 cr, a 🎙️ figure whose largest slice (Rs 500 cr
Consumer) management has since made conditional on a utilisation ramp that has
gone 23% → 22% over two quarters (the report's own 2B). The report's own 2A
gives the audited under-execution figure: capital commitments of Rs 21.01 cr
(AR Note 31, p.283), and states that the two numbers "should not be blended".
2C then blends them by using the guidance number for the execution input.

Recomputed on the audited commitment: 21.01 × 1.18 ÷ 1,230.44 = **1.7%** versus
the reported 63%. On Q1 FY27 capex actually spent (Rs 83 cr): 8.0%. The honest
band is very wide and the block carries the single number 63 with no evidence
tier. capex_embedded_growth_pct is consumed downstream as a growth input, so a
🎙️-grade number travelling as a bare integer is a live risk. MAJOR.

### 2.3 Section 3 — the 22-category scan (24 checks)

Coverage: all 22 categories addressed. Seven carry an explicit NO EVIDENCE
FOUND. The Section 3 summary table carries all 22 rows with the four required
columns.

| # | Check | Verdict | Note |
|---|---|---|---|
| E14-E35 | Each of A1, A2, A3, A4, B1, B2, B3, C1, C2, D1, D2, E1, E2, F1, F2, G1, G2, H1, H2, H3, I1, I2 addressed or explicitly NO EVIDENCE (22 checks) | PASS ×20, **FAIL** ×2 | A1 and F2 fail on evidence grade, detailed below. The other 20 are compliant |
| E36 | Summary table: 22 rows, four columns, prompt L155-157 | PASS | Present |
| E37 | Strong/Moderate count stated, prompt L157-159 | PASS | "7 categories scored Strong or Moderate", inside the guard paragraph |

A1 (E14) detail. The evidence label reads "📄 (MoU, capex committed)"
(07-emoat.md L142-144, and 1A row 1). "Capex committed" is contradicted by the
same report's Section 2A: the audited contracted-but-not-executed figure is
Rs 21.01 cr, and the state MoU's reciprocal incentive package is NOT FOUND. A
signed MoU is fairly graded 📄 as a signed instrument; describing it as
committed capex is not supported by the report's own finding. If A1 dropped to
the 🎙️ multiplier, 3.0 → 2.1 and the total moves 35.4 → 34.5, band unchanged.
MINOR.

F2 (E29) detail, the most consequential B07 finding. F2 credits execution
against a specific benchmark: "FY27 guidance of +25-30% revenue at >20% segment
margin was matched almost exactly by Q1 FY27's +40% YoY at 23% segment margin",
graded "📄 (the actual reported numbers)" (07-emoat.md L273-284). But B01's own
Load-Bearing Facts Check records that exact guidance as **NOT FOUND** in the
corpus: "The specific FY27 aerospace guidance quoted in company memory
('aerospace revenue +25-30%, segment EBITDA margin above 20%, ~20%
manufacturing ROCE') is NOT FOUND verbatim in the AR or the Q1 FY27
presentation text in this corpus (likely sourced from a news article outside
the provided documents)" (01-gate0.md L246-252, and B01 data_notes entry 9).

So a company-memory figure that Gate 0 could not source has re-entered the
pipeline one stage later as a 📄 baseline against which delivery is scored. It
then propagates: Section 6A lists "first FY27 full-year delivery against the
+25-30% Aerospace revenue/>20% margin guide" as a 12-24 month milestone. Per
CLAUDE.md, company memory is "memory to weigh, never anchored evidence". F2
carries 2.0 points; at 0 the total is 33.4, band unchanged. MAJOR on
provenance, not on score.

### 2.4 Section 4 — regulatory and policy (4 checks)

| # | Check | Verdict | Note |
|---|---|---|---|
| E38 | 4A approvals table: body, status, timeline, what it unlocks, competitors | PASS | ECMS PLI row complete; competitor status marked NOT FOUND |
| E39 | 4B policy tailwinds with amounts, duration, enrolment, shared-or-not | PASS | Five rows. The distinction between investment BY Aequs and incentive TO Aequs is drawn explicitly and is good practice |
| E40 | 4C active vs emerging, time to kick in, sustainability | PASS | All three addressed; PLI duration marked NOT FOUND |
| E41 | R1 scored as the 23rd row | PASS | H × M = 3, 📄 1.0x = 3.0 |

Observation, not a fail: R1's Moderate impact rests on one company-specific item
(the ECMS PLI, quantum undisclosed, FY26 income nil) plus two the report itself
calls sector-wide or shrinking. At L impact, R1 would be 2.0 and the total 34.4,
band unchanged.

### 2.5 Section 5 — scorecard (6 checks)

| # | Check | Verdict | Re-derived |
|---|---|---|---|
| E42 | All 23 rows present, prompt L171-174 | PASS | 22 categories + R1 = 23 rows |
| E43 | Raw score matches the likelihood × impact matrix, prompt L170-171 | PASS | All 16 scored rows re-derived: MH=3 (A1), HL=2 (A3), HM=3 (A4), LL=1 (B1), HH=4 (B2), MM=2 (C1), ML=1 (C2), HH=4 (E1), MM=2 (E2), LL=1 (F1), MM=2 (F2), LL=1 (G1), LL=1 (G2), HH=4 (H2), HM=3 (H3), HM=3 (R1). Every one matches |
| E44 | Evidence multipliers 📄 1.0 / 🎙️ 0.7 / 🔍 0.5, prompt L172-173 | **FAIL** | C1 correctly discounted at 🔍 0.5 (2 → 1.0). E2 uses "mixed 0.7x", a tier the taxonomy does not define. Conservative and decision-neutral (at 1.0x the total is 36.0, band unchanged), but undefined. MINOR |
| E45 | Adjusted total arithmetic | PASS | Re-added independently: 3.0+0+2.0+3.0+1.0+4.0+0+1.0+1.0+0+0+4.0+1.4+1.0+2.0+1.0+1.0+0+4.0+3.0+0+0+3.0 = **35.4**. Reported 35.4, em_score 35. Concur |
| E46 | Classification band, prompt L175-176 | PASS | 35 in the 25-39 band → MOAT STRENGTHENING. Bands applied absolute, no rescale, per the 20-Aug-2026 ruling |
| E47 | I1/I2 contribution stated separately, prompt L179-181 | PASS | "I1/I2 contribution to the total: 0.0", with the explicit statement that no threshold crossing occurred via I1/I2. This is exactly the input the operator's 10-15 scan review checkpoint needs |

### 2.6 Verifier rule 8 — categories 21 and 22 (3 checks)

| # | Check | Verdict | Note |
|---|---|---|---|
| E48 | I1 and I2 both present in the B07 output | PASS | Both scored rows and both narrative sections present |
| E49 | I1 above 0 only if both legs evidenced with the (b) leg carrying ≥1 📄 | PASS | Scored 0. The reasoning is exemplary: it rejects the single ex-Apple lateral hire as "one hire, not a documented CLASS", cites the absence of patents, and cites the −16.82% fall in median remuneration as evidence against paying up for scarce talent. Part (b) correctly recorded as entirely absent |
| E50 | I2 above 0 only if the named sacrifice is specific | PASS | Scored 0, applying the framework's own "nothing must be destroyed → execution lead, not configuration" rule, and correctly rejecting the Safran case because the sacrifice there is the customer's, not a competitor's |

### 2.7 Optionality Register (3 checks)

| # | Check | Verdict | Note |
|---|---|---|---|
| E51 | Table present with the four mandated columns, prompt L191-192 | PASS | Six rows, all four columns |
| E52 | Membership: items that scored 0 or rest only on 🎙️/🔍, prompt L184-185 | PASS on the 0-scored and 🎙️ rows | I1/I2, the Consumer capex and the equity raise all qualify |
| E53 | "Registered options are watched, never scored", prompt L195-196 | **FAIL** | See below |

E53 detail. Three register rows are also scored:
- "Hosur aero-engine/landing-gear ecosystem" is registered, and is also the
  entire basis of A1 (the scoring table names the row "Rare manufacturing
  capability (**Hosur increment**)", 3.0) and part of E1's 4.0 ("Hosur
  increment 24-36 months out").
- "Two unbooked Farnborough Tier-1 agreements" is registered, and is also cited
  inside B2's 4.0 and C2's 1.0.
- "Ajna Aerospace & Defence" is registered, and is also cited inside H2's 4.0.

The rule is unambiguous: registered options are watched, never scored. The same
forward advantage cannot be both. Recomputation range: removing A1 entirely
gives 32.4; also trimming E1 to 2.0 and B2 to 3.0 gives 29.4. Both remain in
the 25-39 STRENGTHENING band, so the classification survives. MAJOR.

### 2.8 Scan scope — emerging versus realised (1 check)

| # | Check | Verdict | Note |
|---|---|---|---|
| E54 | Scored rows capture moats **currently forming** that do not yet show in the financials, prompt L21-24 | **FAIL** | See below |

E54 detail. Two of the three Strong rows rest substantially on already-realised
advantages, and the report says so in its own text. B2: "the base is already in
the financials; the incremental Safran/Farnborough wins are new lock-in layered
on top" (L197-199), yet the row scores H × H = 4 without separating base from
increment. E1: "base already realised; Hosur increment 24-36 months out"
(L243-244), scored H × H = 4 on the same undivided basis. The realised base
(the 2009 SEZ notification, the existing hydraulic press, existing approvals,
>90% single-source on quoted parts) is backward-looking moat, which Gate 0
Block F already prices. A1 avoided this correctly by naming its row "Hosur
increment". B2 and E1 did not. This double-counts realised moat inside a
forward score. Band-neutral on every variant I tested. MAJOR.

### 2.9 Section 6 (5 checks)

| # | Check | Verdict | Note |
|---|---|---|---|
| E55 | 6A timeline across all four windows | PASS | 12m, 12-24m, 24-36m, 3-5yr all populated with a named milestone |
| E56 | 6B risks per top-scoring moat with early warning signs | PASS | B2/H2, E1, H3, R1 each carry a risk and a warning sign; where no warning sign exists it is marked NOT FOUND rather than invented |
| E57 | 6C combined table uses the injected B01 fields: core score, **existing moat count**, both classifications, prompt L201-203 | **FAIL** | Core 25/80, moat score 9/60, grand total 34/140 and both classifications are present and match B01 exactly. The existing moat **count** (2 confirmed, moat_class MODERATE) is not carried. MINOR |
| E58 | 6D combined classification, with full reasoning for a TURNAROUND row, prompt L203-208 | PASS on process | Full reasoning given, as the rule requires for TURNAROUND. The label itself is unverifiable in this scope: see the framework gap below |
| E59 | 6E final card: moat evolution map per family, 12m catalysts, biggest risk | PASS | All three present; the map runs existing → emerging per family, including the honest "no genuine emerging improvement found" entry for Financial/Structural |

### 2.10 Block and schema (9 checks)

| # | Check | Verdict | Note |
|---|---|---|---|
| E60 | B07 YAML carries every schema field, no undefined extras | PASS | All 19 schema fields present; no extra fields |
| E61 | Block file matches the report's YAML | PASS | B07-emoat.yaml is identical to 07-emoat.md L633-708 on every field checked |
| E62 | active_categories = Strong/Moderate rows only | PASS | B2, E1, H2 Strong; A1, A4, H3, R1 Moderate. Matches the summary table exactly |
| E63 | evidence_mix item counts | **FAIL** | evidence_mix.documented = 47 against completionist_recount "approximately 26 distinct 📄 items". Two 📄 counts on two definitions, unreconciled, in the same block. The completionist guard turns on the 📄 count, so the ambiguity is not cosmetic. MINOR |
| E64 | completionist_recount line present and in the mandated form | PASS | Present, and the 7 + 9 + 7 = 23 row split ties to the scoring table |
| E65 | catalysts_12m structure and evidence typing | **FAIL** | Four catalysts, all four fields populated. Two are typed `documented` where the catalyst **event** is forward-looking management commentary: "ECMS PLI first eligible income year, FY27" (anchored to a Q4 FY26 call statement) and "Two Farnborough Tier-1 agreements enter disclosed order book, Q2 FY27" (anchored to a Q1 FY27 call). In both cases a documented fact underlies the catalyst (the PLI approval; the signed agreements) but the dated event is a claim. The other two are correctly typed `claim`. This feeds Pillar 3 catalyst proximity downstream. MINOR |
| E66 | capex_embedded_growth_pct carried from 2C | PASS on carry | 63 matches 2C. The input basis fails at E13 |
| E67 | combined_assessment, combined_reasoning, top_moat_risks, analyst_note | PASS | combined_reasoning is one sentence as the schema asks; analyst_note is about 110 words, inside the cap; four top_moat_risks, each anchored |

### 2.11 Section 3 presentation (1 check)

| # | Check | Verdict | Note |
|---|---|---|---|
| E68 | "For each: evidence table or NO EVIDENCE FOUND", prompt L66-67 | **FAIL** | Categories are written as anchored prose paragraphs, not per-category evidence tables. Content is complete and every claim carries an anchor; only the mandated form is missing. The consolidated 22-row summary table is present. MINOR, presentational |

(Check count reconciliation: E01-E68 minus the three sub-numbers folded into the
E14-E35 range = 67 discrete checks.)

### 2.12 Two framework gaps, recorded but NOT counted as adherence failures

FG-1. The combined Gate 0 + Emerging Moat lookup matrix does not exist in the
rule source. prompts/07 L203-208 names the eight output labels but prints no
mapping from backward/forward pairs to a label. The maker did the right thing:
declared the gap, reasoned to a label from the allowed set, and logged it in
input_gaps. I therefore cannot rule the label right or wrong. What I can say:
AVOID backward paired with STRENGTHENING forward is two notches below the
setup the prompt describes as the target, and TURNAROUND is the most generous
label in the allowed set that the reasoning supports. AVERAGE and AVOID are also
available and also defensible. **Operator action: supply the matrix, or rule the
mapping, before combined_assessment travels further downstream.** MINOR.

FG-2. The likelihood × impact matrix has no cell for evidence that CONTRADICTS
a category. Its floor for any evidenced category is LL = 1. So B1 (raw material
99% imported, which argues against backward integration), G1 (war chest funded
by IPO proceeds against negative CFO) and G2 (WC days rising) each score 1.0,
adding 3.0 points to em_score for three categories the report explicitly says
the evidence argues against. Removing all three gives 32.4, band unchanged. The
maker applied the matrix as written; the matrix is the problem. **Operator
action: consider a contradicted-evidence cell scoring 0.** MINOR.

### 2.13 Emerging Moat verdict

The scorecard arithmetic is clean. Every raw score matches the likelihood ×
impact matrix, every multiplier except the undefined "mixed" tier is correct,
the adjusted total re-adds to 35.4, and the band is right. Categories 21 and 22
are present and both correctly scored 0 with reasoning that is the strongest
part of this report. The completionist recount was performed.

The failures cluster on evidence grading rather than on arithmetic: three
register items also scored, two Strong rows scored on a realised base, an
unsourced guidance figure used as a delivery benchmark, and a guidance capex
number carried as the embedded-growth input. None of the four MAJORs moves the
em_score out of the 25-39 STRENGTHENING band. Each of them makes the forward
picture look slightly firmer than the corpus supports, and they all point the
same way, which is the pattern worth naming.

---

## PART 3 — VALUATION ADHERENCE

DEFERRED to phase 3. B10 and B11 do not exist for this run. Per the task scope,
no valuation framework document was loaded and no valuation rule was checked.
Verifier C rules 4, 6, 7, 9, 11 and 12 are not evaluated here. Rule 10 (the
Halt 1 dossier) fires at the /finalize verifier pass, not here.

---

## PART 4 — CROSS-ARTIFACT CONSISTENCY (B01 → B07)

The B01 → B07 hand-off is otherwise sound and worth recording:

- 6C carries B01's core 25/80, moat 9/60, grand total 34/140 and AVOID exactly.
- G1 cites the injected B01 block for FY26 CFO of −Rs 98.75 cr, matching B01.
- G2's WC days of 132 → 151, sourced independently to the Q4 FY26 call, matches
  B01's AR-computed 131.87 → 151.44. Two independent routes to the same number.
- combined_reasoning cites 34/140 and 35/92 correctly.

Two inconsistencies, both already captured above: the FY27 guidance provenance
(Part 2.3, F2) and the net debt definition (Part 1.5, D1 at 0.17x against B07's
citation of the AR's own 0.23x).

---

## PART 5 — CONSOLIDATED FINDINGS

| ID | Severity | Location | Finding |
|---|---|---|---|
| C-01 | MAJOR | 01-gate0.md L119-125 (D1) vs L128-133 (D3) | Net debt basis excludes lease liabilities in D1 while D3 includes them, same block, same date. AR p.46's own 0.23x net debt/equity implies net debt ~Rs 342 cr. Recomputed D1 = 1, Block D = 9, core = 23, grand total = 32. Classification unchanged AVOID; deal-breaker 6 still does not fire |
| C-02 | MAJOR | 07-emoat.md Optionality Register vs Section 5 rows A1/E1/B2/C2/H2 | Hosur, the Farnborough agreements and Ajna are registered as optionality AND scored. Prompt L195-196: registered options are watched, never scored. Recomputed range 29.4 to 32.4; band unchanged |
| C-03 | MAJOR | 07-emoat.md L191-199 (B2), L238-244 (E1), Section 5 | Already-realised, in-financials advantages scored inside a scan defined as moats currently forming. Both rows say the base is already realised, then score H × H = 4 undivided. A1 handled this correctly by scoring the increment only |
| C-04 | MAJOR | 07-emoat.md L273-284 (F2), L533 (6A) vs 01-gate0.md L246-252 | Execution moat scored against FY27 guidance (+25-30% revenue, >20% margin) that B01 recorded as NOT FOUND in corpus and attributed to company memory. Company memory is memory to weigh, never anchored evidence |
| C-05 | MAJOR | 07-emoat.md L91-114 (2C), B07-emoat.yaml L44 | capex_embedded_growth_pct = 63 uses 🎙️ FY27 capex guidance of Rs 660 cr, not "capex under execution" per prompt L61-63. The audited commitment is Rs 21.01 cr, giving 1.7%; Q1 FY27 actual spend gives 8.0%. The block carries 63 with no evidence tier |
| C-06 | MINOR | 01-gate0.md L64-69, B01 data_notes entry 3 | B3 reached score 0 by a declared "override" of the band. Stage rule 2 forbids qualitative judgments. The same 0 is reachable through the band's own "or negative" clause. Outcome stands; the route is off-rule |
| C-07 | MINOR | 01-gate0.md L59-61 | FCF capex uses PPE only. The formula definition is PPE + intangibles. The intangibles leg is neither included nor declared absent |
| C-08 | MINOR | 01-gate0.md L176 (M6) | Anchor reads "(AR p.?...page marker not captured in extract)". An anchor without a page is not an anchor |
| C-09 | MINOR | 01-gate0.md L218-224, B01 deal_breakers[] | Prompt L155 requires the driving years for any deal-breaker. Only entry 8 names them; entries 1-4 do not, and entries 3 and 4 rest on different windows |
| C-10 | MINOR | B01-gate0.yaml L19 | `freshness_verdict` is not in the stage 1 schema, which says "exactly this fenced YAML block". If the orchestrator mandates the field, this is a rule-source conflict to reconcile rather than a maker error |
| C-11 | MINOR | 07-emoat.md L142-144, 1A row 1 | A1 evidence labelled "📄 (MoU, capex committed)". The report's own 2A shows audited commitments of Rs 21.01 cr and the state incentive package NOT FOUND. The MoU is fairly 📄; "capex committed" is not supported |
| C-12 | MINOR | 07-emoat.md Section 5, E2 row | Multiplier "mixed 0.7x" is a tier the taxonomy does not define. Conservative; at 1.0x the total is 36.0, band unchanged |
| C-13 | MINOR | 07-emoat.md L26 and L196-197 (📄) vs L222-223 (🎙️/📄) | The two Farnborough Tier-1 agreements carry two different evidence tiers in the same report |
| C-14 | MINOR | 07-emoat.md 6C table | The injected existing-moat count (2 confirmed, MODERATE) is not carried, though prompt L201-203 asks for it. Core score and both classifications are correct |
| C-15 | MINOR | B07-emoat.yaml L37 vs L38 | evidence_mix.documented = 47 against a completionist_recount of ~26 📄 items. Two counts, two definitions, unreconciled. The guard turns on this count |
| C-16 | MINOR | 07-emoat.md Section 3, all categories | Categories written as prose, not the per-category evidence tables prompt L66-67 mandates. Content complete and anchored; form missing |
| C-17 | MINOR | B07-emoat.yaml L40-41 | Two of four catalysts_12m typed `documented` where the dated event is management commentary. Feeds Pillar 3 catalyst proximity downstream |
| C-18 | MINOR | 07-emoat.md L146-151 (A2), L450 (4B SEZ row) | Two evidence anchors carry no page reference |
| C-19 | MINOR | prompts/07-emerging-moat-pipeline.md L203-208; 07-emoat.md 6D | FRAMEWORK GAP, not a maker error. The combined classification matrix is absent from the rule source, so TURNAROUND cannot be verified. The maker declared the gap and logged it. Operator ruling needed before the label travels downstream |
| C-20 | MINOR | prompts/07-emerging-moat-pipeline.md L170-171; 07-emoat.md rows B1/G1/G2 | FRAMEWORK GAP, not a maker error. The matrix floor is 1 for any evidenced category, so three categories whose evidence argues AGAINST the moat still add 3.0 points |

Counts: CRITICAL 0, MAJOR 5, MINOR 15. Total 20.

Adherence: Gate 0 57/63 = 90%. Emerging Moat 55/67 = 82% (C-19 and C-20 are
recorded as framework gaps and are not counted as failures). Phase-1 combined
112/130 = 86%.

No REWORK trigger fires from this verifier: zero CRITICAL, and both section
rates and the combined rate sit well above the 60% threshold.

## RECOMPUTED VERDICTS

I concur with both auditable verdicts. Gate 0 classification AVOID stands under
my recomputation and under every sensitivity tested, including the D1 net-debt
basis correction (core 23, grand total 32) and the M1 EBITDA-basis sensitivity.
Emerging Moat classification MOAT STRENGTHENING stands: the adjusted total
re-adds to 35.4 exactly, and every correction I identified leaves it inside the
25-39 band, with the widest plausible correction landing at 29.4.

The combined assessment TURNAROUND is not disputed and not confirmed. It is
unverifiable in this scope because the matrix it claims to apply is not in the
rule source. That is C-19 and it needs an operator ruling.

```yaml
stage: B12c
company: "AEQUS"
run_date: "2026-09-05"
model: claude-opus-4-8
status: complete
scope: "phase 1 only — Gate 0 (B01) and Emerging Moat (B07). Valuation audit deferred to phase 3."
gate0:
  rules_checked: 63
  rules_passed: 57
  acceptance_pct: 90
  fails:
    - "D1 net debt basis excludes lease liabilities while D3 includes them; recomputed D1 = 1, Block D = 9, core = 23, grand total = 32, classification unchanged AVOID"
    - "B3 scored 0 by declared override of the band rather than via the band's own 'or negative' clause; stage rule 2 forbids qualitative judgments; outcome 0 stands"
    - "M6 anchor incomplete: 'AR p.?', page marker not captured"
    - "FCF capex taken as PPE only; formula definition is PPE + intangibles, and the intangibles leg is not declared absent"
    - "deal_breakers[] entries 1-4 omit the driving years that prompt L155 requires; only entry 8 names them"
    - "B01 YAML carries freshness_verdict, a field the stage 1 schema does not define"
emoat:
  rules_checked: 67
  rules_passed: 55
  acceptance_pct: 82
  fails:
    - "Optionality register items also scored: Hosur (A1, E1), Farnborough agreements (B2, C2), Ajna (H2); prompt L195-196 says registered options are watched, never scored; recomputed range 29.4-32.4, band unchanged"
    - "Already-realised, in-financials advantages scored inside an emerging-moat scan: B2 and E1 both state the base is realised, then score H x H = 4 undivided"
    - "F2 scores execution against FY27 guidance that B01 recorded as NOT FOUND in corpus and attributed to company memory; propagates into 6A"
    - "2C uses FY27 capex guidance (Rs 660 cr, claim-grade) instead of capex under execution (audited commitment Rs 21.01 cr); capex_embedded_growth_pct 63 vs 1.7 recomputed on the audited figure"
    - "A1 evidence labelled 'capex committed', contradicted by the report's own 2A audited commitment of Rs 21.01 cr"
    - "E2 uses an undefined 'mixed 0.7x' multiplier tier; taxonomy defines only 1.0/0.7/0.5"
    - "Farnborough Tier-1 agreements graded documented in 1A and B2 but claim/documented in C2"
    - "6C omits the injected existing-moat count (2 confirmed, MODERATE) that prompt L201-203 requires"
    - "evidence_mix.documented 47 unreconciled with completionist_recount of ~26 documented items"
    - "Section 3 categories presented as prose, not the per-category evidence tables prompt L66-67 mandates"
    - "Two of four catalysts_12m typed documented where the dated event is management commentary; feeds Pillar 3 catalyst proximity"
    - "Two evidence anchors carry no page reference: A2 Form B, 4B SEZ tax reconciliation"
  framework_gaps_not_counted_as_fails:
    - "Combined Gate0+EmergingMoat lookup matrix absent from prompts/07; 6D TURNAROUND label unverifiable; maker declared the gap and logged it in input_gaps; operator ruling needed"
    - "Likelihood x impact matrix has no cell for contradicting evidence; floor LL=1 gives B1, G1, G2 three points for categories the report says argue against the moat"
valuation: "pending phase 3"
business_understanding_narrative:
  present: false
  five_questions_answered: false
  prose_only: false
  section6_candidates_named: 0
  valuation_vocab_leak: false
  fails: []
  scope_note: "Stage 13 synthesis is not in phase-1 scope and does not exist for this run. Not evaluated, not a REWORK trigger here. Deferred to the stage 13 verifier pass."
recomputed_destination_pe: ""
recomputed_decision: ""
findings:
  - {severity: "MAJOR", location: "runs/aequs-2026-09-05/outputs/reports/01-gate0.md L119-125 (D1) vs L128-133 (D3)", description: "Net debt basis excludes lease liabilities in D1 while D3 includes them, same block and same date. B07 cites the AR's own p.46 net debt/equity of 0.23x, implying net debt of about Rs 342 cr against the Rs 250.05 cr used. Recomputed D1 = 1, Block D = 9, core = 23, grand total = 32. Classification unchanged AVOID; deal-breaker 6 still does not fire at 2.14x."}
  - {severity: "MAJOR", location: "runs/aequs-2026-09-05/outputs/reports/07-emoat.md Optionality Register vs Section 5 rows A1/E1/B2/C2/H2", description: "Hosur, the two Farnborough Tier-1 agreements and the Ajna JV are entered in the Optionality Register and also scored. prompts/07 L195-196: registered options are watched, never scored. Recomputed total falls to between 29.4 and 32.4; STRENGTHENING band unchanged."}
  - {severity: "MAJOR", location: "runs/aequs-2026-09-05/outputs/reports/07-emoat.md L191-199 (B2), L238-244 (E1)", description: "Two of the three Strong rows score already-realised, in-financials advantages inside a scan defined as moats currently forming. Both rows state the base is already realised, then score H x H = 4 without separating base from increment. A1 handled this correctly by naming its row the Hosur increment. Realised moat is already priced in Gate 0 Block F."}
  - {severity: "MAJOR", location: "runs/aequs-2026-09-05/outputs/reports/07-emoat.md L273-284 (F2) and L533 (6A), against runs/aequs-2026-09-05/outputs/reports/01-gate0.md L246-252", description: "F2 scores execution delivery against FY27 aerospace guidance of +25-30% revenue at >20% segment margin. B01 recorded that exact guidance as NOT FOUND in corpus and attributed it to company memory, likely a news article outside the provided documents. A memory-derived figure re-enters as a documented benchmark and propagates into the 6A timeline."}
  - {severity: "MAJOR", location: "runs/aequs-2026-09-05/outputs/reports/07-emoat.md L91-114 (2C) and runs/aequs-2026-09-05/outputs/blocks/B07-emoat.yaml L44", description: "capex_embedded_growth_pct = 63 is built on the claim-grade FY27 capex guidance of Rs 660 cr, not on capex under execution as prompts/07 L61-63 specifies. The report's own 2A gives the audited commitment of Rs 21.01 cr, which recomputes to 1.7%; Q1 FY27 actual spend of Rs 83 cr gives 8.0%. The block carries 63 as a bare integer with no evidence tier for downstream consumption."}
  - {severity: "MINOR", location: "runs/aequs-2026-09-05/outputs/reports/01-gate0.md L64-69 and B01-gate0.yaml data_notes entry 3", description: "B3 reached score 0 through a declared override of the scoring band. Stage operating rule 2 forbids qualitative judgments. The same 0 is reachable through the band's own '<0.20 or negative = 0' clause read against the negative cumulative FCF. Outcome stands; the route is off-rule. Framework should disambiguate what 'negative' attaches to."}
  - {severity: "MINOR", location: "runs/aequs-2026-09-05/outputs/reports/01-gate0.md L59-61", description: "FCF capex taken as acquisition of property, plant and equipment only. The formula definition is purchase of PPE plus intangibles. The intangibles leg is neither included nor declared absent. Both computable FCF years sit far from the B2 and B3 band edges, so no score moves."}
  - {severity: "MINOR", location: "runs/aequs-2026-09-05/outputs/reports/01-gate0.md L176 (M6)", description: "Anchor reads 'AR p.?, Directors Report technology-absorption section, grep-located, page marker not captured in extract'. An anchor without a page fails the mandatory source-anchor rule. The M6 score of 0 is not in doubt."}
  - {severity: "MINOR", location: "runs/aequs-2026-09-05/outputs/reports/01-gate0.md L218-224 and B01-gate0.yaml deal_breakers[]", description: "prompts/01 L155 requires stating which years drive any deal-breaker. Only entry 8 names its years. Entries 3 and 4 rest on materially different windows (median ROCE on FY25-FY26 only; cumulative CFO/PAT on FY23-FY26) and the windows appear only in data_notes."}
  - {severity: "MINOR", location: "runs/aequs-2026-09-05/outputs/blocks/B01-gate0.yaml L19", description: "The block carries freshness_verdict, a field the stage 1 schema does not define, against an instruction to end with exactly the specified YAML block. B07 carries no equivalent field. If the run-pipeline orchestrator mandates it, this is a rule-source conflict to reconcile rather than a maker error."}
  - {severity: "MINOR", location: "runs/aequs-2026-09-05/outputs/reports/07-emoat.md L142-144 and Section 1A row 1", description: "A1 evidence labelled documented on the basis of MoU plus capex committed. The report's own Section 2A shows the audited contracted commitment is Rs 21.01 cr and the reciprocal state incentive package is NOT FOUND. The signed MoU is fairly documented; capex committed is not supported by the report's own finding. At the claim multiplier A1 falls 3.0 to 2.1, band unchanged."}
  - {severity: "MINOR", location: "runs/aequs-2026-09-05/outputs/reports/07-emoat.md Section 5, E2 row", description: "E2 applies a 'mixed 0.7x' multiplier. The taxonomy defines only documented 1.0x, claim 0.7x and inference 0.5x. Using the claim multiplier for a mixed category is conservative but the tier is undefined. At 1.0x the total is 36.0, band unchanged."}
  - {severity: "MINOR", location: "runs/aequs-2026-09-05/outputs/reports/07-emoat.md L26 and L196-197 against L222-223", description: "The two Farnborough Tier-1 agreements are graded documented in Section 1A and in B2, and claim/documented in C2. One evidence item carries two tiers in the same report."}
  - {severity: "MINOR", location: "runs/aequs-2026-09-05/outputs/reports/07-emoat.md Section 6C table", description: "prompts/07 L201-203 requires the combined table to carry the injected core score, existing moat count and both classifications. The moat score 9/60 is carried but the existing moat count (2 confirmed, moat_class MODERATE) is not. Core score and both classifications match B01 exactly."}
  - {severity: "MINOR", location: "runs/aequs-2026-09-05/outputs/blocks/B07-emoat.yaml L37 against L38", description: "evidence_mix.documented is 47 while completionist_recount states approximately 26 distinct documented items. Two documented counts on two definitions, unreconciled in the same block. The completionist guard turns on this count, so the ambiguity is not cosmetic."}
  - {severity: "MINOR", location: "runs/aequs-2026-09-05/outputs/reports/07-emoat.md Section 3, all categories", description: "prompts/07 L66-67 requires an evidence table or NO EVIDENCE FOUND for each category. Categories are written as anchored prose paragraphs. Content is complete and every claim carries an anchor, and the consolidated 22-row summary table is present; only the mandated per-category form is missing."}
  - {severity: "MINOR", location: "runs/aequs-2026-09-05/outputs/blocks/B07-emoat.yaml L40-41", description: "Two of four catalysts_12m are typed evidence_type documented where the dated catalyst event is forward-looking management commentary: ECMS PLI first eligible income year FY27, and the Farnborough agreements entering the order book in Q2 FY27. Both are anchored to concalls. A documented fact underlies each, but the dated event is a claim. This feeds Pillar 3 catalyst proximity downstream."}
  - {severity: "MINOR", location: "runs/aequs-2026-09-05/outputs/reports/07-emoat.md L146-151 (A2) and L450 (4B SEZ row)", description: "Two evidence anchors carry no page reference: 'AR Board's Report, Form B' and 'AR consolidated tax reconciliation'. prompts/07 L35-36 requires a page or slide anchor on every evidence item. Neither item carries a score."}
  - {severity: "MINOR", location: "prompts/07-emerging-moat-pipeline.md L203-208 and runs/aequs-2026-09-05/outputs/reports/07-emoat.md Section 6D", description: "FRAMEWORK GAP, not a maker error, and not counted as an adherence fail. The combined Gate0 plus Emerging Moat lookup matrix is absent from the rule source, which names the eight labels but prints no mapping. The maker declared the gap, reasoned transparently and logged it in input_gaps, which is the compliant response. TURNAROUND is therefore unverifiable; AVERAGE and AVOID are also available and defensible for an AVOID backward score paired with STRENGTHENING forward. Operator ruling needed before combined_assessment travels downstream."}
  - {severity: "MINOR", location: "prompts/07-emerging-moat-pipeline.md L170-171 and runs/aequs-2026-09-05/outputs/reports/07-emoat.md rows B1, G1, G2", description: "FRAMEWORK GAP, not a maker error, and not counted as an adherence fail. The likelihood times impact matrix has no cell for evidence that contradicts a category; its floor for any evidenced category is LL = 1. B1, G1 and G2 therefore add 3.0 points for three categories the report explicitly says the evidence argues against. Removing all three gives 32.4, band unchanged. Consider a contradicted-evidence cell scoring 0."}
critical_count: 0
major_count: 5
minor_count: 15
acceptance_rate: 86
```
