# VERIFIER C: FRAMEWORK ADHERENCE, EMUDHRA 2026-09-19 (PHASE 1 SCOPE)

Model: claude-opus-5. Fresh context. Scope: Gate 0 (B01) and Emerging Moat
(B07) only. Valuation audit (B10, B11, rules 4-7 and 11-15) is PENDING PHASE 3.
Rules 9 and 10 (stage 13 narrative, 09b dossier) are out of scope in phase 1.

Rule sources read: prompts/01-gate-0-pipeline.md, prompts/07-emerging-moat-pipeline.md.
Artifacts read: outputs/reports/01-gate0.md, outputs/blocks/B01-gate0.yaml,
outputs/reports/07-emoat.md, outputs/blocks/B07-emoat.yaml.
Re-derivation sources: inputs/screening/screener-Data_Sheet.csv (INR Cr);
inputs/annual-report/Annual_Report_2026.mupdf.txt (INR Mn, [page N] = PDF page).

Boundary note. Verifier A owns whether a number exists in the source. This
audit cites source figures only where a scoring rule was applied to a wrong
premise (for example "N/A, not in provided data" when the figure is present).
The source-fidelity question stays with Verifier A.

---

## PART 1: GATE 0 (B01) RULE-BY-RULE

### 1.1 Re-derivation of stated inputs

ROCE, computed basis (EBIT = PBT + Interest; CE = Equity + Reserves + Borrowings, screener-data):

| Year | EBIT (Cr) | CE (Cr) | Computed ROCE | B01 used |
|---|---|---|---|---|
| FY19 | 21.91 | 104.37 | 20.99% | 20.99% computed |
| FY20 | 23.69 | 133.92 | 17.69% | 17.69% computed |
| FY21 | 32.02 | 158.68 | 20.18% | 20.18% computed |
| FY22 | 55.02 | 219.94 | 25.02% | 25.02% computed |
| FY23 | 76.76 | 416.92 | 18.41% | 18.41% computed |
| FY24 | 95.67 | 663.93 | 14.41% | 19.5% AR p.57 disclosed |
| FY25 | 108.55 | 745.32 | 14.56% | 18.2% AR p.57 disclosed |
| FY26 | 136.38 | 939.91 | 14.51% | 15.0% AR p.57 disclosed |

B01 arithmetic on its own mixed series is correct: median 18.955%, min 15.0%,
trend -5.99pp. ROE series and median 18.675% re-derive exactly (the computed
FY24-26 ROE of 14.33 / 12.08 / 13.01% gives the same median).

Cumulative CFO 443.14 Cr, cumulative PAT 422.12 Cr, ratio 1.05x: re-derived exactly.
Revenue CAGR 31.8%, PAT CAGR 29.7%, gap -2.1pp: re-derived exactly.
M11 windows 41.3% vs 28.8%, S&A 12.77% to 8.86%: re-derived exactly.
F total 17, 4 moats present (M2, M4, M5, M11), STRONG: re-derived exactly.
Core 71, grand total 88: arithmetic correct on the stated block scores.

### 1.2 Compliance table

| # | Rule | Result | Note / recomputed value |
|---|---|---|---|
| G1 | Data-years opening line, confidence tier (8 yrs = moderate, no downgrade) | PASS | |
| G2 | Anchors on extracted numbers | PASS | |
| G3 | A1 median ROCE band | PASS | 18.955% -> 3; 18.05% on consistent basis -> 3 |
| G4 | A2 minimum single-year ROCE | **FAIL (MAJOR)** | Mixed-basis series. FY24-26 swap computed values for AR-disclosed values; minimum lands on 15.0%, exactly on the >=15% edge. Consistent computed series gives min 14.41% (FY24) -> band 12-14.9 -> **3, not 5**. Block A 12 -> **10**. |
| G5 | A3 median ROE | PASS | 18.675% -> 4 |
| G6 | A4 ROCE trend | PASS | -5.99pp (or -6.48pp consistent) -> 0 |
| G7 | B1 cum CFO/PAT | PASS | 1.05x -> 5 |
| G8 | B2 FCF-positive proportion | PASS (with window caveat) | n=2 (FY25-26), 50% -> 2; see G10 |
| G9 | B3 cum FCF/PAT | PASS | -17.7% -> 0 |
| G10 | B4 change in WC days | **FAIL (CRITICAL)** | Scored "N/A (not in provided data)" on the premise that consolidated trade payables are OCR-scrambled. The provided mupdf AR prints them cleanly: consolidated balance sheet, AR p.216 (Trade payables MSE 68.06 + others 532.86 Mn FY26; 28.79 + 285.55 Mn FY25) and Note 18, AR p.255 (Total 600.92 Mn FY26 / 314.34 Mn FY25). Re-derived on the formula (revenue basis): FY25 WC days = 102.2 rec + 1.0 inv - 22.1 pay = **81.1d**; FY26 = 98.4 + 2.0 - 31.3 = **69.2d**; change **-11.9d -> "decreased >5 days" -> 5**. The stage accepted an n=2 window (FY25-26) for B2 and B3 but refused the same window for B4 on a false premise. Recomputed below under two readings. |
| G11 | C1 revenue CAGR | PASS | 31.8% -> 5 |
| G12 | C2 PAT CAGR | PASS | 29.7% -> 5 |
| G13 | C3 positive YoY years | PASS | 7/7 -> 5 |
| G14 | C4 PAT minus revenue CAGR | PASS | -2.1pp -> 3 |
| G15 | D1 net debt/EBITDA | **FAIL (MINOR)** | Input error, score unchanged. B01 used Cash & Bank 107.31 Cr, which is the FY25 column. FY26 = 65.20 Cr (screener-data; = AR p.216 cash 582.33 + bank 69.71 Mn). Net cash = 65.20 - 28.78 = **36.42 Cr**, not 78.53 Cr. Still net cash -> 5. |
| G16 | D2 interest coverage | PASS | 26.9x -> 5 |
| G17 | D3 debt/equity | PASS | 0.032x -> 5 |
| G18 | D4 current ratio | **FAIL (MINOR)** | Scored on standalone 2.90x (Note 50) because consolidated CA/CL were called unextractable. Consolidated BS, AR p.216, is clean: total current assets 4,355.64 Mn / total current liabilities 1,578.00 Mn = **2.76x** -> >=2.0 -> 5. Score unchanged; basis fixed. |
| G19 | E1 promoter holding | PASS | 54.40% -> 4 |
| G20 | E2 promoter 3-yr change | PASS | N/A, 0; data truly absent |
| G21 | E3 pledge | PASS | 0% -> 5 |
| G22 | E4 contingent liabilities / NW | PASS (flag honoured) | 0.38% -> 5 on the quantified note. Two readings: quantified total only (stage) vs include the 3i Infotech allegation (> Rs 128 Cr, AR Note 36 narrative; management states "there will not be any economic outflow"): 14.4% -> 3, Block E 12. The separating observation is whether the company or its auditor ever moves the claim into the quantified contingent-liability total. The stage named the tail risk prominently. No classification effect under either reading. |
| G23 | M1 pricing power | **FAIL (MINOR)** | Method error, score unchanged. EBITDA subtracts Change in Inventory; screener convention adds it (check: EBITDA + OI - Dep - Int must equal PBT). Correct FY19 EBITDA 32.21 Cr (31.71%), FY26 159.12 Cr (**22.68%**, not 21.97%). Decline 9.03pp -> still 0. The corrected margin also leaves M2 (5, +11.1pp over peer median) and M5 (2nd on margin) unchanged. |
| G24 | M2 cost advantage | PASS | |
| G25 | M3 capital efficiency | PASS | FAT 0.97x -> 0 |
| G26 | M4 customer stickiness | PASS | 3 |
| G27 | M5 scale & dominance | PASS | 3, peer-set caveat stated |
| G28 | M6 technology/R&D | PASS | 0; "consistently" not met. Observation: tier 3 (>=1% AND margin above peer median) is ambiguous on one year of capitalised development; a 1 would not make a moat present |
| G29 | M7 regulatory | PASS | PEER DATA NEEDED -> 0 per rule |
| G30 | M8 distribution | PASS | 1 |
| G31 | M9 brand | PASS | PEER DATA NEEDED -> 0 |
| G32 | M10 switching costs | PASS | literal rubric -> 0 |
| G33 | M11 network effects | PASS | 5 |
| G34 | M12 negative WC / float | **FAIL (MINOR)** | Labelled N/A on the same false premise as B4. Consolidated WC days are 81.1d (FY25) and 69.2d (FY26), >45 -> **0**. Score unchanged; label wrong. |
| G35 | Moat count and class | PASS | 4 -> STRONG |
| G36 | Core / grand total arithmetic | PASS | on stated scores |
| G37 | Classification matrix | PASS on stated inputs | changes with G10, see 1.3 |
| G38 | Deal-breakers, driving years stated | PASS on stated inputs | #2 trigger depends on G10, see 1.3 |
| G39 | CAGR edge rules | PASS | no negative endpoints; no loss-to-profit swing |
| G40 | FLAG-GATE0 condition | PASS | classification > AVERAGE, not required |
| G41 | YAML schema, analyst_note <=200 words | PASS | ~145 words |

### 1.3 Recomputed Gate 0 classification (G4 + G10 applied)

Two readings of the sub-window question. One observation separates them: an
operator ruling on whether a Block B metric may run on a window shorter than
the full 8-year history when the full window is not extractable. The ruling
must apply to B2, B3 and B4 alike. The stage applied it to B2/B3 and not to B4.

| Reading | A | B | C | D | E | Core | Moat | Deal-breaker #2 | Classification |
|---|---|---|---|---|---|---|---|---|---|
| Stage as filed | 12 | 7 (5+2+0+0) | 18 | 20 | 14 | 71 | STRONG | triggered | GOOD |
| R1: n=2 window accepted for B2-B4 (the stage's own convention) | 10 | 12 (5+2+0+5) | 18 | 20 | 14 | 74 | STRONG | not triggered | **GOOD+** |
| R2: n=2 window rejected for B2-B4 alike | 10 | 5 (5+0+0+0) | 18 | 20 | 14 | 67 | STRONG | triggered | GOOD |
| R1 with E4 including 3i claim | 10 | 12 | 18 | 20 | 12 | 72 | STRONG | not triggered | GOOD+ |

The filed result is the one combination that is internally inconsistent. It
accepts a 2-year window where it lowers the score (B2/B3) and rejects it where
it would raise the score (B4), on a premise the corpus disproves. Under the
stage's own convention the classification flips GOOD -> GOOD+. That is a
decision-changing misapplication: CRITICAL. The block_b_trend field
("deteriorating") also needs a second number: WC days improved 11.9d in the
same year FCF turned negative.

Remedy: REWORK stage 1. Re-score B4 and M12 from AR p.216 / Note 18 p.255
(mupdf), D4 on consolidated 2.76x, D1 on FY26 cash, A2 on one basis; state one
window convention for B2-B4 and flag the operator ruling it needs.

---

## PART 2: EMERGING MOAT (B07) RULE-BY-RULE

### 2.1 Scorecard re-derivation

| Row | L x I | Raw | Tier | Mult | Adjusted | Check |
|---|---|---|---|---|---|---|
| A4 | MH | 3 | 📄 | 1.0 | 3.0 | OK |
| B2 | MM | 2 | 📄 | 1.0 | 2.0 | OK |
| C1 | MH | 3 | 🎙️ | 0.7 | 2.1 | OK (conservative dominant tier) |
| C2 | HL | 2 | 📄 | 1.0 | 2.0 | OK ("new customer additions" is a listed signal) |
| E1 | HH | 4 | 📄 | 1.0 | 4.0 | tier issue, see E9 |
| H1 | MH | 3 | 📄 | 1.0 | 3.0 | OK (bolt-ons named in category text) |
| H2 | HM | 3 | 📄 | 1.0 | 3.0 | OK |
| R1 | HH | 4 | 📄 | 1.0 | 4.0 | consistency issue, see E10 |
| Others (15 rows) | | 0 | | | 0 | OK |
| Total | | | | | **23.1** | arithmetic correct; band 12-24 MODEST correct |

### 2.2 Compliance table

| # | Rule | Result | Note / recomputed value |
|---|---|---|---|
| E1 | All six sections present | PASS | |
| E2 | All 23 rows addressed (22 + R1) | PASS | |
| E3 | NO EVIDENCE FOUND discipline, no force-fit | PASS | |
| E4 | Anchors on evidence items | PASS | one unanchored clause folded into E9 |
| E5 | L x I raw mapping | PASS | |
| E6 | Evidence multipliers applied | PASS | |
| E7 | Adjusted total arithmetic | PASS | 23.1 |
| E8 | Classification band | PASS | MODEST |
| E9 | Scores consistent with evidence tiers (rule 3) | **FAIL (MAJOR)** | E1 scored HH at 📄 1.0x (max). The events are 📄 (Almaty office, East Africa NPKI case study, UAE CWIP), but the category's defining attribute, first-mover status, rests on unanchored 🔍: "ahead of most listed Indian identity/security peers" carries no source. "One of East Africa's first nations" describes the customer nation, not eMudhra's lead over peers. The UAE leg is a pending licence already slipped once (the stage's own FLAG-REGULATORY-DEPENDENCY). Recomputed: HM/MH at 📄 = 3.0 (em_score **22.1**) or HH at 🔍 = 2.0 (em_score **21.1**). Band unchanged (MODEST); still below the EM >=25 UA qualifier. |
| E10 | Narrative and score agree (R1) | **FAIL (MINOR)** | Section 4C states the shared, non-exclusive nature "tempers R1's score", then scores R1 at the maximum HH = 4. Either the tempering applies (HM = 3, em_score -1.0) or the sentence goes. No band change. |
| E11 | Completionist recount performed | PASS | "19 documented items across 8 categories" sums correctly (4+1+1+1+3+2+3+4); 8 active < 12 guard; re-examination stated anyway |
| E12 | Count consistency | **FAIL (MINOR)** | YAML evidence_mix {documented: 24, claim: 10, inference: 6} does not reconcile to the 19-item 📄 recount, and no reconciliation is given. Report says "none of the 14 None/Weak rows"; the table has 15 (23 - 8). |
| E13 | Category 21 (I1) present, scored 0 unless both legs evidenced with 📄 (b) | PASS | 0; (a) is a hiring story, (b) not found |
| E14 | Category 22 (I2) present, >0 only with a specific named sacrifice | PASS | 0; sacrifice unsupported by a 📄 competitor source |
| E15 | I1/I2 contribution stated separately | PASS | 0.0 |
| E16 | 2C capex-embedded growth arithmetic | **FAIL (MAJOR)** | Basis mismatch. The multiplier is FAT on net PP&E only (5.43x, excludes intangibles), but "capex under execution" includes Rs 105.92 Mn intangible assets under development. The run's own Gate 0 FAT (M3, net block incl. intangibles) is 0.97x. Same inputs on the run-consistent basis: 291.76 x 0.965 = Rs 281.6 Mn = **4.0%** of FY26 revenue, not 22.6%. PP&E FAT applied to the PP&E CWIP alone gives 185.84 x 5.43 = Rs 1,009 Mn = 14.4%. The template also asks for "historical" FAT; a single FY26 year was used. capex_embedded_growth_pct = 22.6 is the high end of a 4.0-22.6 range and may feed a CAPACITY revenue basis at stage 11. The low-confidence caveat is present but the number itself is off-basis. |
| E17 | No estimated fills (NOT FOUND is the only valid fill) | **FAIL (MINOR)** | Section 1C marks Services FY27 growth NOT FOUND, then fills it with an assumed ~16.5% and derives FY27E Services Rs 1,716.42 Mn, total Rs 8,674.16 Mn and "implied +23.6%". The fill is disclosed and not carried in the YAML, but the derived totals must go or be marked NOT FOUND. |
| E18 | Optionality register, four columns, in YAML | PASS | 10 rows |
| E19 | 6C uses injected B01 block | PASS | 71 / 4 STRONG / 88 / GOOD match the filed B01. Note: 6C inherits the B01 classification, which is under CRITICAL rework (Part 1.3) |
| E20 | 6D combined classification | PASS with framework gap | The "standard matrix" named in prompts/07 section 6D does not exist in prompts/ or frameworks/ (verified: "HIGH POTENTIAL" appears only in prompts/07, Section_1B_v3.3 Amendment 4.3 and section-1b chunk 06, none of which defines the lookup). The stage flagged the gap and did not invent a table. Operator item: the label feeds the Amendment 4.3 hurdle tier (TURNAROUND / HIGH POTENTIAL -> Tier A). If B01 moves to GOOD+, the first-principles 6D label must be re-read. |
| E21 | One improvement, one mechanism | PASS | allocation stated; CA/B Forum scored once (R1), not in B2 |
| E22 | YAML schema, analyst_note <=200 words | PASS | extra capex fields are additive |

---

## PART 3: VALUATION (B10 / B11)

PENDING PHASE 3. B10 and B11 do not exist. Rules 4-7 and 11-15 not run.
Expectation ledger and Business Understanding Narrative checks not run.

---

## FINDINGS SUMMARY

| # | Sev | Location | Finding | Recomputed |
|---|---|---|---|---|
| 1 | CRITICAL | B01 Block B, B4 | N/A on a false premise; consolidated payables clean at AR p.216 / Note 18 p.255. Window convention applied to B2/B3 but not B4 | B4 = 5 (WC 81.1d -> 69.2d); Block B 12; deal-breaker #2 off; GOOD+ under the stage's own convention; GOOD only if the sub-window is rejected for B2-B4 alike (Block B 5) |
| 2 | MAJOR | B01 Block A, A2 | Mixed computed/disclosed ROCE series; min sits on the 15% edge | Consistent basis min 14.41% -> A2 = 3; Block A 10 |
| 3 | MAJOR | B07 E1 row | First-mover attribute rests on unanchored 🔍, scored HH at 📄 | 3.0 or 2.0; em_score 22.1 or 21.1; band unchanged |
| 4 | MAJOR | B07 Section 2C / capex_embedded_growth_pct | PP&E-only FAT applied to a CWIP + intangibles base; single-year FAT | 4.0% on run-consistent FAT (0.97x); range 4.0-22.6% |
| 5 | MINOR | B01 D1 | FY25 cash used for FY26 | Net cash 36.42 Cr; score 5 unchanged |
| 6 | MINOR | B01 D4 | Standalone current ratio used; consolidated available | 2.76x (AR p.216); score 5 unchanged |
| 7 | MINOR | B01 M1/M2/M5 EBITDA | Change in Inventory sign reversed | FY26 EBITDA 159.12 Cr, 22.68%; scores unchanged |
| 8 | MINOR | B01 M12 | N/A label on false premise | 69.2d -> 0; score unchanged |
| 9 | MINOR | B07 R1 / Section 4C | Narrative says tempered, score is max | HM = 3 if tempered; em_score -1.0 |
| 10 | MINOR | B07 evidence_mix, Section 3 count | evidence_mix unreconciled with the 19-item recount; 14 vs 15 None/Weak rows | reconcile or explain |
| 11 | MINOR | B07 Section 1C | Estimated Services growth filled where NOT FOUND is required | remove FY27E Services and total, or mark NOT FOUND |

Rules checked: Gate 0 41 (6 fail), Emerging Moat 22 (5 fail). Total 63; 52 pass.
Acceptance rate 52 / 63 = 82.5%.

REWORK routing for the orchestrator: finding 1 is a CRITICAL rule misapplication
that changes the Gate 0 classification under the stage's own convention. REWORK
stage 1 (B01) with the remedy in Part 1.3, and put the sub-window question to the
operator as a ruling. Stage 7 needs no REWORK on phase-1 rules (rule 8 passes, no
band change). It should correct findings 3, 4, 9, 10 and 11 in the same pass, and
re-read 6C/6D after B01 is reworked.
