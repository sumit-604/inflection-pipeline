# STAGE 12 VERIFIER C: FRAMEWORK ADHERENCE, CAPILLARY (phase-1 scope)

Run date: 2026-09-19 | Model: claude-opus-5 | Emits: B12c
Scope: PHASE 1 ONLY. Gate 0 (B01) and Emerging Moat (B07) compliance.
The valuation audit (B10, B11, rules 4-7 and 11-15) does not run in this
phase. The valuation, expectation-ledger and business-understanding
sections of B12c are left pending phase 3 / stage 13.

Rule sources: prompts/01-gate-0-pipeline.md; prompts/07-emerging-moat-pipeline.md.
Artifacts audited: outputs/reports/01-gate0.md + blocks/B01-gate0.yaml;
outputs/reports/07-emoat.md + blocks/B07-emoat.yaml. Source rows re-read
only where a rule check needed them (screening/screener-Data_Sheet.csv,
Annual_Report_2026.txt, Concall_May_2026_Transcript.txt).

Verifier C audits rule application. It does not own number existence
(Verifier A does). Where this report quotes a source row, it does so to
test a rule reading, not to rule on source fidelity.

---

## PART 1: GATE 0 (B01) COMPLIANCE TABLE

Re-derivation of every block score from the stated inputs and thresholds.

| # | Rule | B01 value | Re-derived | Result |
|---|---|---|---|---|
| 1 | Opening "Data available: X years" line (op. rule 6) | 6 yrs FY21-FY26, sub-windows disclosed | same | PASS |
| 2 | A1 median ROCE (4 values) | -1.83% -> 0 | (-8.22+4.56)/2 = -1.83 -> 0 | PASS |
| 3 | A2 min ROCE | -33.63% -> 0 | 0 | PASS |
| 4 | A3 median ROE | -39.13% -> 0 | (-62.09-16.16)/2 = -39.13 -> 0 | PASS (note O2) |
| 5 | A4 ROCE trend | 8.82 vs -33.63 -> 5 | 5 | PASS |
| 6 | B1 cum CFO/PAT | 189.14 / -202.71 -> 0 | ratio -0.93, below 0.50 band -> 0 | PASS |
| 7 | B2 FCF-positive share | 2/4 = 50% -> 2 | 2 | PASS |
| 8 | B3 cum FCF/PAT | 28.84 / -79.04 -> 0 | "negative = 0" -> 0 | PASS |
| 9 | B4 WC days change | 24.0 -> 52.8, +28.8 -> 0 | 0 | PASS |
| 10 | C1 revenue CAGR | 33.88% -> 5 | (734.60/170.91)^(1/5)-1 = 33.86% -> 5 | PASS |
| 11 | C2 PAT CAGR edge rule | N/M -> 0 | negative endpoint -> 0 | PASS |
| 12 | C3 positive YoY years | 5/5 -> 5 | 5 | PASS |
| 13 | C4 with PAT N/M | 0 | 0 per edge rule | PASS |
| 14 | D1 ND/EBITDA | net cash -> 5 | 5 | PASS |
| 15 | D2 interest cover | 10.36x -> 5 | literal EBIT/interest 10.36x -> 5 | PASS (note O1) |
| 16 | D3 D/E | 0.04 -> 5 | 5 | PASS |
| 17 | D4 current ratio | 2.80 -> 5 | 5 | PASS |
| 18 | E1 promoter holding | 51.45% -> 4 | 4 | PASS |
| 19 | E2 3-yr promoter change | N/A -> 0 | 0 per grounded-claims rule | PASS |
| 20 | E3 pledge | 0% -> 5 | 5 | PASS |
| 21 | E4 contingent/NW | 0.04% -> 5 | 5 (AR note 34 quantifies only bank guarantees 3.91; Annual_Report_2026.txt p.244) | PASS |
| 22 | M1 pricing power | 5 | -7.37% -> 12.64%, CAGR 33.9% -> 5 | PASS |
| 23 | M2 cost advantage | 0 | 12.64 vs peer median 19.22 -> below -> 0 | PASS |
| 24 | M3 capital efficiency | 0 | FAT 1.60x, ROCE 8.82% -> 0 | PASS |
| 25 | M4 customer stickiness | 3 | 0 decline yrs, rec. days moved -27 (outside +/-10) -> 3 | PASS |
| 26 | M5 scale & dominance | 1 | literal "top 5 mcap" on a 4-name set -> 1 | PASS (note O3) |
| 27 | M6 technology / R&D | 0, "N/A, no R&D disclosure found" | score 0 holds; the N/A basis is false | **FAIL (F-G3)** |
| 28 | M7 regulatory | 0 | 0 | PASS |
| 29 | M8 distribution | 0 | "purely digital = 0" | PASS |
| 30 | M9 brand | 0, not scorable | literal proxy ties all four at ~100% -> "at/below = 0" | PASS |
| 31 | M10 switching costs | 5 | grew every yr, rec. days fell -> 5 | PASS |
| 32 | M11 network effects | 3 | **1** (see F-G1) | **FAIL (F-G1)** |
| 33 | Moat count and class | 4, STRONG | 3, MODERATE (derived from F-G1, not a separate fail) | PASS (derived) |
| 34 | Core score arithmetic | 51 | 5+2+10+20+14 = 51 | PASS |
| 35 | Grand total arithmetic | 68 | 51+17 = 68 as stated; 66 after F-G1 | PASS |
| 36 | Data-confidence band and downgrade | 5-6 band, flag stated, no downgrade | literal reading of 6 data years holds | PASS (note O4) |
| 37 | Classification matrix | Core 51 -> AVERAGE | AVERAGE | PASS |
| 38 | Deal-breakers applied, driving years named | #1,#2 non-binding; #3,#4,#8 binding; FY24 named | same | PASS |
| 39 | CAGR edge rules and loss-to-profit note | noted in data_notes | present | PASS |
| 40 | FLAG-GATE0 raised at <= AVERAGE with depressors | present | present | PASS |
| 41 | block_b_trend / FLAG-CASH states the number that shows the trend | trend direction right, mechanism wrong | see F-G2 | **FAIL (F-G2)** |
| 42 | Source anchors on extracted numbers | present throughout | present | PASS |
| 43 | Peer data rule (no guessed peer figures) | peer exports used, anchored | PASS | PASS |
| 44 | analyst_note <= 200 words | about 208 words | over cap | **FAIL (F-G4)** |

Gate 0: 44 rules checked, 40 PASS, 4 FAIL. Classification AVERAGE holds
under every correction below.

### Gate 0 findings

**F-G1 (MAJOR). M11 network-effects test read on a mismatched window.**
B01 tests the revenue leg on the latest 3-year window (FY23->FY26 CAGR
31.57%) but reads the selling-expense leg on FY21->FY26 and on "the last
two years". On the same latest 3-year window, B01's own proxy series
rises: 32.5% (FY23) to 39.2% (FY26) (screener-Data_Sheet.csv rows 17-18:
FY23 98.52+6.50 = 105.02 on sales 322.68; FY26 268.46+19.43 = 287.89 on
sales 734.60). The rubric's top tier pairs the latest 3-year CAGR with the
selling-% trend, so one window governs both legs.
- Reading 1 (same window): growth >15% but selling % rising -> M11 = 1.
- Reading 2 (B01's): full-period decline 53.9% -> 39.2% -> M11 = 3.
- Separating observation: the rubric's own top tier couples the two legs
  on the latest 3-year window; B01 used that window for the revenue leg.
  The two-year "declining" window is an ad hoc third window.
Recomputed: M11 = 1; moat score 17 -> 15; moats present 4 -> 3; moat
class STRONG -> MODERATE; grand total 68 -> 66. Classification stays
AVERAGE (Core 51 sits below 60, so the matrix does not use moat class).
The STRONG label propagates into B07 Section 6C and B07's combined
reasoning, so the fix must carry downstream.

**F-G2 (MAJOR). FLAG-CASH and block_b_trend name the wrong mechanism.**
Both say the FY26 CFO improvement "leans on payable-days compression
(66.6 to 37.0 days) rather than receivable discipline". Three problems,
all from B01's own numbers:
1. 66.6 -> 37.0 is the FY23->FY26 move. It is not the FY26 move.
2. Payable-days compression consumes cash. It cannot lift CFO.
3. In FY26 receivable days fell 98.3 -> 89.8 and payable days rose
   30.9 -> 37.0 (B01 Block B4). Both helped FY26 CFO. So FY26 did show
   receivable discipline. B01's own LBF4 paragraph says a "large payables
   build" helped FY26 CFO, which contradicts the flag text.
Correct statement: WC days worsened 24.0 -> 52.8 over FY23-FY26, driven by
payable days falling 66.6 -> 37.0. The FY26 CFO swing was helped by both a
receivable-days fall and a payable build, and by the Rs 24.96 Cr one-off
indemnity receipt year. The flag direction (deteriorating on the
multi-year WC trend) stands. The error propagated verbatim into B07 G2.

**F-G3 (MINOR for B01; root of F-E6). M6 "no R&D disclosure found" is
false.** Annual_Report_2026.txt p.41 (Directors' Report, Rule 8(3)
technology absorption, item iv): "the expenditure incurred on Research and
Development. (incl. ESOP) H 1,212 Mn." M6 still scores 0: the 3 and 5
tiers need EBITDA >= 15-20% (12.64%), and the 1 tier needs margin above
peer median (it is below). The N/A label and the input_gap "no
R&D/technology spend disclosure found in AR or screener data" must be
corrected; the gap fed B07 (F-E6). Verifier A owns whether the figure's
basis (standalone vs consolidated) is as stated.

**F-G4 (MINOR). analyst_note over the 200-word cap.** About 208 words;
per the template the excess is truncated, which cuts the promoter-holding
sentence. That fact survives in input_gaps, so no information is lost.

### Gate 0 observations (rules passed; recorded for the operator)

- **O1 (MINOR). D2 exceptional-item treatment is inconsistent with M1/M2.**
  B01 strips the Rs 24.96 Cr Kognitiv indemnity gain from EBITDA for
  M1/M2 but keeps it in EBIT for D2. Literal formula: EBIT 56.57 / 5.46 =
  10.36x -> 5 (PASS). Recurring reading: (56.57-24.96)/5.46 = 5.79x -> 4.
  Separating observation: whether the gain is inside screener PBT (B01's
  own reconciliation 13.73+24.96 = 38.69 says it is). Effect: Core 51 ->
  50, classification AVERAGE unchanged.
- **O2 (MINOR). ROE and ROCE series mix bases.** ROE FY25/FY26 use AR
  published figures; the rubric allows the source's own figure for ROCE
  only. Computed values match (13.28/553.61 = 2.40%; 52.39/795.87 =
  6.58%), so no score moves. ROCE FY25/FY26 are AR published while FY23/24
  are computed on the fixed formula; the fixed formula gives about 5.4%
  for FY26 (56.57/1,042.82). No score moves. data_notes also says ROCE
  "FY21-FY24 are computed", but FY21-FY22 ROCE was not computed.
- **O3 (MINOR). M5 on a 4-name universe.** "Top 5 mcap" is true by
  construction when the segment holds four names. Score 1 vs a possible
  0 does not change the moat count.
- **O4 (rule passed, ambiguity). History downgrade.** B01 keys the
  data-confidence band to 6 P&L years; Block A and B4 run on 4
  balance-sheet years. Reading the band on the 4-year window would trigger
  the LIMITED one-tier downgrade (AVERAGE -> AVOID). B01's reading is the
  literal one (data_years = 6) and is disclosed. Flagged for an operator
  ruling, not scored as a fail.

---

## PART 2: EMERGING MOAT (B07) COMPLIANCE TABLE

| # | Rule | B07 | Result |
|---|---|---|---|
| 1 | All six sections present | 1-6 plus register | PASS |
| 2 | All 23 rows addressed or NO EVIDENCE (A1-A4, B1-B3, C1-C2, D1-D2, E1-E2, F1-F2, G1-G2, H1-H3, I1-I2, R1) | 23 of 23 | PASS |
| 3 | Source anchors on evidence items | present | PASS |
| 4 | Likelihood x impact values (HH4, HM3, MM2, LM1, LL1) | correct mapping | PASS |
| 5 | Adjusted total arithmetic | 24.0 re-summed | PASS |
| 6 | Band (12-24 MODEST) | MODEST | PASS |
| 7 | I1/I2 contribution stated separately | 0.0 stated | PASS |
| 8 | Cat 21 (I1): >0 only with both legs, (b) with a documented source | 0 | PASS |
| 9 | Cat 22 (I2): sacrifice test run "for each moat claimed" | run on H1 only | **FAIL (F-E1)** |
| 10 | Completionist guard threshold (12+) | 6 active, not triggered | PASS |
| 11 | Documented recount line accurate | "18 items across 6 categories" | **FAIL (F-E4)** |
| 12 | Tier consistency: A3 (claim 0.7) | consistent | PASS |
| 13 | Tier consistency: A4 (claim 0.7) | consistent | PASS |
| 14 | Tier consistency: B2 (documented 1.0) | consistent (note O6) | PASS |
| 15 | Tier consistency: C1 (documented 1.0) | documented anchor does not evidence the C1 criterion | **FAIL (F-E2)** |
| 16 | Tier consistency: C2 (claim 0.7) | consistent | PASS |
| 17 | Tier consistency: D1 (claim 0.7) | consistent | PASS |
| 18 | Tier consistency: D2 (claim 0.7) | consistent | PASS |
| 19 | Tier consistency: F1 (claim 0.7) | consistent on its stated basis | PASS |
| 20 | Tier consistency: F2 (documented 1.0) | stated tier mixed, scored at 1.0, evidence shared with H1 | **FAIL (F-E3)** |
| 21 | Tier consistency: G1 (claim 0.7) | consistent | PASS |
| 22 | Tier consistency: H1 (claim 0.7) | consistent | PASS |
| 23 | Tier consistency: H2 (claim 0.7) | consistent | PASS |
| 24 | Zero rows not force-fit (A1, A2, B1, B3, E1, E2, G2, H3, I1, I2, R1) | honest zeros | PASS |
| 25 | Evidence gaps correctly declared ("NOT FOUND" only when absent) | R&D spend declared undisclosed; it is disclosed | **FAIL (F-E6)** |
| 26 | 2C capex-embedded growth | N/A stated with reason; 0 in YAML | PASS (note O7) |
| 27 | Optionality register complete and in scope | two risk items inside; D1/H2/A4 claim-only rows absent | **FAIL (F-E5)** |
| 28 | 6C uses injected B01 | yes | PASS (carries F-G1) |
| 29 | 6D combined classification per matrix; HIGH POTENTIAL / TURNAROUND reasoned | AVERAGE, reasoned | PASS (note O8) |
| 30 | 6A timeline, 6B risks, 6E card present | present | PASS |
| 31 | YAML fields complete (incl. optionality_register, catalysts_12m) | complete | PASS (note O9) |

Emerging Moat: 31 rules checked, 25 PASS, 6 FAIL.

### Emerging Moat findings

**F-E1 (MAJOR). I2 sacrifice test applied to one moat, not each.** The
rubric: "For each moat claimed anywhere in this scan, answer: what
SPECIFIC thing would the best-resourced competitor have to destroy". B07
runs the test on H1 only. C1, D1, B2, A3 and F2 are untested. The most
relevant untested candidate is the one B07's own 6E map carries from B04:
"counter-positioning aiRA usage pricing". Usage or outcome pricing against
seat-priced incumbents is the textbook cannibalization-barrier candidate
(a pricing regime the incumbent would have to give up). B07 must run the
test on it and on C1. Score effect: the top band needs a documented
competitor source, which the corpus likely lacks; a claim-tier ML/LM
score adds 0.7 at most. Band survives.

**F-E2 (MAJOR). C1 scored at the documented multiplier on an anchor that
evidences a new-logo win, not an embedded relationship.** B07 calls the
USD 20m Fortune 50 retailer deal "a real cross-sell". Management files it
under new logos: "Second axis of growth for us is the new customer wins.
So, this is net new logos ... We also announced a very large Fortune 50
retailer, a $20 million deal" (Concall_May_2026_Transcript.txt lines
195-198); closing remarks: "winning a Fortune 50 customer" (line 755). A
multi-product first contract is documented; the C1 criteria (cross-sell
into the base, wallet share, workflow integration) rest on "Farming 44%
of new ACV" and NRR commentary, which B07 itself grades as claims.
- Reading 1: the C1 moat evidence is claim-tier -> HH 4 x 0.7 = 2.8.
- Reading 2 (B07): the signed contract is documented -> 4.0.
- Separating observation: an audited or filed NRR / cross-sell metric
  (for example, an AR MD&A NRR line). None is cited.
Recomputed C1: 2.8 (-1.2).

**F-E3 (MAJOR). F2 scored at 1.0 on a stated mixed tier, and part of its
evidence is credited twice.** Section 3 grades F2 "documented/claim"; the
scorecard applies 1.0. F2's support includes "the three completed M&A
turnarounds ... each show a genuine multi-year margin recovery pattern
(see H1)". H1 grades those same margin numbers as claims (0.7). The same
improvement is credited through two rows at two tiers, which breaches
one-improvement-one-mechanism. The documented leg (15 consecutive quarters
of revenue growth) is growth history, not the F2 criteria list (capex on
time, ramp speed, revenue per employee, guidance delivery). Guidance
delivery is B05's claim-derived record.
Recomputed F2: 3 x 0.7 = 2.1 (-0.9).

**F-E4 (MINOR). Documented recount line misstates the category count.**
"18 documented items across 6 categories" counts "general company
profile" (analyst placements, CRISIL report, uptime, capex) as a
category. The documented items fall in five scan categories: B2, C1, H1,
H2, F2. The report then says "the recount confirms the sparse 6-category
read", which conflates the recount's six with the six Strong/Moderate
rows (C1, H1, B2, A3, D1, F2). Of those six, A3 and D1 carry zero
documented items and H1 is scored at claim tier. Correct line: "📄
recount performed: 12 documented items across 5 categories, plus 6
company-profile items outside the scan; 3 of 6 active rows score at the
documented multiplier (B2, C1, F2), 2 after F-E2."

**F-E5 (MINOR). Optionality register scope.** The rubric defines the
register as forward advantages that scored 0 or rest only on claim or
inference evidence. Two rows are risk resolutions, not advantages: the
FY26 concentration disclosure and the Czech fraud forensic close. Those
belong in monitoring and flags. Claim-only rows D1 (data asset), H2
(partnerships) and A4 (platform) have no register line with their
converting evidence.

**F-E6 (MAJOR). R&D spend declared undisclosed; it is disclosed.** B07
carries B01's false gap (F-G3) and reasons on it in A4 ("R&D spend itself
is undisclosed"), F1 ("no R&D headcount split ... B01 gap"), and the
analyst_note ("R&D spend ... genuinely undisclosed"). Annual_Report_2026.txt
p.41 states R&D expenditure incl. ESOP of Rs 1,212 Mn. A4 and F1 were
scored on a false evidence base. The rows sit in a scan 1.0 point below
the 25 threshold that is also the Amendment 3 UA qualifier, so the
rescore must be done, not assumed. A4's rubric test (SKU growth without
proportional R&D) and F1's (R&D headcount, specialists, retention) need
more than a spend line, so a large move is unlikely.

### Emerging Moat observations (rules passed)

- **O5.** G2's score of 0 is correct (WC days rose), but its text copies
  B01's wrong mechanism (F-G2). Fix with F-G2.
- **O6 (MINOR). B2 impact grade vs B07's own text.** B07 grades B2 HM (3)
  yet calls the certifications "table-stakes for any credible enterprise
  SaaS vendor" and "not a differentiator" (6E). Consistent with that text,
  impact L gives HL = 2 (-1.0). Judgment call; not scored as a fail.
- **O7 (MINOR). 2C.** N/A with a stated reason is acceptable for an
  asset-light name with zero IPO-object utilisation, but the YAML writes
  capex_embedded_growth_pct: 0, which a consumer reads as a computed 0.
  The Section 2A reading paragraph also says "The ₹394 Cr FY26 cash capex";
  the table beside it says ₹39.4 Cr (Rs 394 mn). A 10x unit slip in prose.
  Verifier A owns the number.
- **O8 (MINOR). 6D scope leak.** The 6D reasoning cites "already reflected
  in a 75x trailing P/E (step-1 brief)". Pricing and the recognition gap
  belong to Stage 11. The P/E is also unanchored to a corpus row. The
  AVERAGE outcome follows from backward AVERAGE plus forward MODEST
  without it.
- **O9 (MINOR).** catalysts_12m uses evidence_type "documented_pending",
  outside the three-tier taxonomy. Use "management_claim" or restate the
  item as a monitoring line.

---

## RECOMPUTED VALUES

| Item | Stage value | Recomputed | Decision effect |
|---|---|---|---|
| B01 M11 | 3 | 1 | none on classification |
| B01 moat score / count / class | 17 / 4 / STRONG | 15 / 3 / MODERATE | carries into B07 6C and later readers |
| B01 grand total | 68 | 66 | none |
| B01 core (O1 alternative reading only) | 51 | 50 | none |
| B01 classification | AVERAGE | AVERAGE | unchanged (O4 alternative reading gives AVOID; operator ruling) |
| B07 C1 | 4.0 | 2.8 | lowers score |
| B07 F2 | 3.0 | 2.1 | lowers score |
| B07 em_score | 24.0 | 21.9 (before F-E1 and F-E6 rescoring) | MODEST unchanged |
| B07 band after worst-case upward rescoring | n/a | 21.9 + I2 at most 0.7 + A4/F1 R&D rescore; crossing 25 needs +3.1, i.e. F1 at HH on documented evidence, which a spend line cannot carry | MODEST survives |

No finding is CRITICAL. No correction flips the Gate 0 classification,
the EM band, or the EM >= 25 UA qualifier.

## REWORK ROUTING (for the orchestrator)

- Stage 1 (B01): fix M11 (F-G1), moat class, grand total; rewrite
  FLAG-CASH and block_b_trend mechanism (F-G2); correct the M6 basis and
  the R&D input_gap (F-G3); trim analyst_note (F-G4). Scoped corrections.
  They are not a full rerun.
- Stage 7 (B07): run I2 on each claimed moat, counter-positioning first
  (F-E1); rescore C1 and F2 (F-E2, F-E3); rescore A4 and F1 against the
  disclosed R&D line (F-E6); correct the recount line (F-E4) and the
  register (F-E5); carry B01's corrected moat class into 6C.
- Acceptance rate 86.7% (65 of 75). Above the 60% floor; no automatic
  REWORK trigger from Verifier C.

## PENDING PHASE 3

Valuation (B10/B11), rules 4-7 and 11-15, expectation ledger (rules
13-14): not run in this phase. Business Understanding Narrative (rule 9)
belongs to stage 13. Halt 1 dossier (rule 10) fires at /finalize.

```yaml
stage: B12c
company: "CAPILLARY"
run_date: "2026-09-19"
model: "claude-opus-5"
status: complete
scope: "phase-1 (gate0 + emoat only); valuation pending phase 3"
gate0:
  rules_checked: 44
  fails:
    - {id: F-G1, rule: "M11 network effects", severity: MAJOR, stated: "3 (moat 17, 4 present, STRONG, total 68)", recomputed: "1 (moat 15, 3 present, MODERATE, total 66)", note: "selling-% leg read on a different window than the revenue leg; FY23->FY26 proxy rises 32.5% -> 39.2% (screener-Data_Sheet.csv rows 17-18); classification AVERAGE unchanged"}
    - {id: F-G2, rule: "block_b_trend / FLAG-CASH mechanism", severity: MAJOR, stated: "FY26 CFO leans on payable-days compression 66.6 -> 37.0 rather than receivable discipline", recomputed: "66.6 -> 37.0 is FY23->FY26 and consumes cash; FY26 receivable days fell 98.3 -> 89.8 and payable days rose 30.9 -> 37.0, both helping FY26 CFO; multi-year WC deterioration (24.0 -> 52.8) stands"}
    - {id: F-G3, rule: "M6 grounded-claims / N/A basis", severity: MINOR, stated: "no R&D disclosure found", recomputed: "R&D expenditure incl. ESOP Rs 1,212 Mn disclosed (Annual_Report_2026.txt p.41, Directors' Report technology absorption item iv); M6 score 0 unchanged"}
    - {id: F-G4, rule: "analyst_note <= 200 words", severity: MINOR, stated: "about 208 words", recomputed: "trim; truncated sentence survives in input_gaps"}
emoat:
  rules_checked: 31
  fails:
    - {id: F-E1, rule: "I2 test for each moat claimed", severity: MAJOR, stated: "test run on H1 only", recomputed: "run on C1, D1, B2, A3, F2 and B04's aiRA usage-pricing counter-positioning; claim-tier score at most +0.7, band survives"}
    - {id: F-E2, rule: "C1 evidence tier", severity: MAJOR, stated: "HH x 1.0 = 4.0", recomputed: "HH x 0.7 = 2.8; the documented Fortune 50 deal is a net new logo (Concall_May_2026_Transcript.txt lines 195-198, 755), cross-sell evidence is claim-tier"}
    - {id: F-E3, rule: "F2 evidence tier and single credit", severity: MAJOR, stated: "HM x 1.0 = 3.0 on a stated mixed tier", recomputed: "HM x 0.7 = 2.1; M&A margin turnarounds credited in both F2 and H1"}
    - {id: F-E4, rule: "documented recount line", severity: MINOR, stated: "18 items across 6 categories", recomputed: "12 items across 5 scan categories plus 6 company-profile items; 3 of 6 active rows at documented multiplier, 2 after F-E2"}
    - {id: F-E5, rule: "optionality register scope", severity: MINOR, stated: "7 rows incl. concentration disclosure and fraud forensic close", recomputed: "move the 2 risk items to monitoring; add D1, H2, A4 claim-only rows"}
    - {id: F-E6, rule: "evidence gaps correctly declared", severity: MAJOR, stated: "R&D spend undisclosed (A4, F1, analyst_note)", recomputed: "disclosed Rs 1,212 Mn (Annual_Report_2026.txt p.41); rescore A4 and F1; crossing 25 would need F1 at HH documented, not supportable by a spend line"}
valuation: {rules_checked: 0, fails: [], status: "PENDING PHASE 3"}
expectation_ledger: {status: "NOT IN SCOPE, PENDING PHASE 3", present: false, downside_row: false, all_rows_confirm_by: false, all_rows_metric_threshold: false, prob_in_range: false, decay_status_valid: false, off_ledger_credit: false, residual_pct_cmp: 0, residual_starter_cap_ok: true, fails: []}
business_understanding_narrative: {status: "NOT IN SCOPE, STAGE 13", present: false, five_questions_answered: false, prose_only: false, section6_candidates_named: 0, valuation_vocab_leak: false, fails: []}
recomputed_destination_pe: ""
recomputed_decision: ""
recomputed_gate0: {moat_score: 15, moats_confirmed: 3, moat_class: "MODERATE", grand_total: 66, core_score: 51, classification: "AVERAGE"}
recomputed_em_score: "21.9 before F-E1/F-E6 rescoring (stated 24.0); band MODEST unchanged"
findings:
  - {id: F-G1, stage: B01, severity: MAJOR, summary: "M11 window mismatch; moat class STRONG -> MODERATE, total 68 -> 66"}
  - {id: F-G2, stage: B01, severity: MAJOR, summary: "FLAG-CASH / block_b_trend mechanism contradicts B01's own B4 numbers; propagated into B07 G2"}
  - {id: F-G3, stage: B01, severity: MINOR, summary: "false 'no R&D disclosure' gap; M6 score unchanged"}
  - {id: F-G4, stage: B01, severity: MINOR, summary: "analyst_note over 200 words"}
  - {id: O1, stage: B01, severity: MINOR, summary: "D2 keeps Rs 24.96 Cr one-off in EBIT while M1/M2 strip it; recurring reading 5.79x -> D2 4, core 50; AVERAGE unchanged; rule passed"}
  - {id: O2, stage: B01, severity: MINOR, summary: "ROE/ROCE series mix AR-published and computed bases; values reconcile or do not move scores; data_notes wrongly says FY21-FY22 ROCE computed"}
  - {id: O3, stage: B01, severity: MINOR, summary: "M5 top-5 tier trivially met on a 4-name peer set; moat count unaffected"}
  - {id: O4, stage: B01, severity: MINOR, summary: "rule passed, ambiguity for operator ruling: 4-year balance-sheet window would trigger LIMITED downgrade (AVERAGE -> AVOID) if the band keyed to it; B01 keyed to 6 P&L years"}
  - {id: F-E1, stage: B07, severity: MAJOR, summary: "I2 sacrifice test run on H1 only; aiRA usage-pricing counter-positioning untested"}
  - {id: F-E2, stage: B07, severity: MAJOR, summary: "C1 documented multiplier rests on a new-logo contract; 4.0 -> 2.8"}
  - {id: F-E3, stage: B07, severity: MAJOR, summary: "F2 mixed tier scored at 1.0 and double-credits H1 M&A margins; 3.0 -> 2.1"}
  - {id: F-E4, stage: B07, severity: MINOR, summary: "recount counts a non-category; 5 scan categories, not 6"}
  - {id: F-E5, stage: B07, severity: MINOR, summary: "register holds 2 risk items, omits D1/H2/A4"}
  - {id: F-E6, stage: B07, severity: MAJOR, summary: "R&D spend Rs 1,212 Mn disclosed (AR p.41); A4/F1 reasoned on a false gap 1.0 below the 25 threshold"}
  - {id: O6, stage: B07, severity: MINOR, summary: "B2 graded impact M while text calls it table-stakes; HL would give 2.0"}
  - {id: O7, stage: B07, severity: MINOR, summary: "2C N/A written as 0 in YAML; prose says Rs 394 Cr capex vs table Rs 39.4 Cr"}
  - {id: O8, stage: B07, severity: MINOR, summary: "6D cites an unanchored 75x P/E; pricing belongs to stage 11"}
  - {id: O9, stage: B07, severity: MINOR, summary: "catalyst evidence_type 'documented_pending' outside the three-tier taxonomy"}
critical_count: 0
major_count: 6
minor_count: 12
acceptance_rate: 86.7
```
