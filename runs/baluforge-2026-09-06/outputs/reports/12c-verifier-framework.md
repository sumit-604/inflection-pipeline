# STAGE 12C — VERIFIER C: FRAMEWORK ADHERENCE AUDIT
# BALUFORGE | Run date 2026-09-06 | Model: claude-opus-4-8 | Emits: B12c
# SCOPE: PHASE 1. Gate 0 (B01) and Emerging Moat (B07) only.
# Valuation adherence (B10/B11) NOT run: those stages do not exist yet.

## SCOPE AND METHOD

Rule sources read in full:
- /home/user/inflection-pipeline/prompts/01-gate-0-pipeline.md (governs B01)
- /home/user/inflection-pipeline/prompts/07-emerging-moat-pipeline.md (governs B07)

Artifacts audited:
- runs/baluforge-2026-09-06/outputs/reports/01-gate0.md + blocks/B01-gate0.yaml
- runs/baluforge-2026-09-06/outputs/reports/07-emoat.md + blocks/B07-emoat.yaml

Per the task instruction, the Master Project Prompt, the Section 1B layer set and
FTTCP v2.1 were NOT loaded. They govern the deferred valuation audit only.

I re-derived every formula the prompts fix. To do that I read the primary
screening inputs directly:
- inputs/screening/screener-Data_Sheet.csv
- inputs/screening/screener-Balance_Sheet.csv
- inputs/screening/HAPPYFORGE-Data_Sheet.csv

That reading is for arithmetic re-derivation only. Whether a number exists in a
source PDF at its cited anchor is Verifier A's exclusive and non-overridable
call. Nothing below downgrades, dismisses or reasons around a Verifier A
source-fidelity finding.

---

## PART 1: GATE 0 (B01) COMPLIANCE

### 1.1 Formula re-derivations

Every fixed formula in the prompt was recomputed from screener-Data_Sheet.csv.

**ROCE (EBIT / (Total Assets - Current Liabilities))**

| FY | EBIT recomputed | Capital Employed | ROCE mine | ROCE B01 | Verdict |
|---|---|---|---|---|---|
| 2021 | 9.74+6.61 = 16.35 | 77.52+26.00 = 103.52 | 15.79% | 15.79% | MATCH |
| 2022 | 39.09+5.23 = 44.32 | 158.62+47.40 = 206.02 | 21.51% | 21.51% | MATCH |
| 2023 | 50.56+10.53 = 61.09 | 210.16 (AR) | 29.07% | 29.07% | MATCH |
| 2024 | 113.67+13.64 = 127.31 | 578.73 (AR) | 22.00% | 22.00% | MATCH |
| 2025 | 253.94+10.96 = 264.90 | 1,070.46 (AR) | 24.75% | 24.75% | MATCH |
| 2026 | 306.04+16.45 = 322.49 | 1,594.52+151.87 = 1,746.39 | 18.47% | 18.47% | MATCH |

A1 median of six = mean of 21.51 and 22.00 = 21.755 -> band 20-24.9 -> 4. CORRECT.
A2 minimum = 15.79 -> >=15 -> 5. CORRECT.
A4 latest 18.47 >= earliest 15.79 -> 5. CORRECT, and the proxy-basis caveat is
stated at the line, which is what basis note 4 requires.

**ROE (PAT / average net worth)** — all six recomputed from Equity Share Capital
+ Reserves: FY21 9.83% (closing only, correctly stated per the rule since no
FY2020 opening net worth exists), FY22 25.27%, FY23 21.84%, FY24 24.91%,
FY25 25.38%, FY26 19.55%. Median = (21.84+24.91)/2 = 23.38%. B01 reports 23.38%.
MATCH. A3 -> >=20 -> 5. CORRECT.

**Cumulative CFO / PAT** — CFO sum 17.33-57.74+26.16-31.73+148.24+31.70 = 133.96.
PAT sum = 632.61. Ratio 0.2118. B01: 0.21. MATCH. B1 -> <0.50 -> 0. CORRECT.

**FCF (CFO - capex)** — all six recomputed; cumulative -802.89. MATCH.
B2 = 2 of 6 positive = 33% -> <50 -> 0. CORRECT.
B3 = -802.89/632.61 = -1.269 -> negative -> 0. CORRECT.

**Working Capital Days** — recomputed on the revenue basis from Receivables,
Inventory and the AR-sourced payables:
FY23 235.24+38.91-73.18 = 200.97 (B01: 201.01)
FY24 142.45+58.33-52.53 = 148.25 (B01: 148.28)
FY25 129.34+38.76-46.63 = 121.47 (B01: 121.48)
MATCH within rounding. Revenue basis is the correct basis: the prompt permits a
COGS basis only if COGS is explicitly available, and screener-Data_Sheet carries
Raw Material Cost, not COGS. B4 change -79.5 days -> decreased >5 -> 5. CORRECT.

**CAGR** — Revenue (1107.37/142.09)^(1/5)-1 = 50.78%. B01: 50.79%. PAT
(258.89/7.62)^(1/5)-1 = 102.41%. B01: 102.42%. MATCH within rounding.
C4 = +51.6pp -> >=3pp -> 5. CORRECT.

**CAGR edge rules** — no endpoint is negative or zero; PAT is positive in all six
years so no loss-to-profit swing; C4's N/M branch is not reached. B01 states all
three non-triggers (data note 14). CORRECT.

**Block D** — Net debt 151.87-89.00 = 62.87; EBITDA 322.49+9.96 = 332.45;
ratio 0.189x -> 0-1.0x -> 4. IC 322.49/16.45 = 19.60x -> 5. D/E 151.87/1594.52
= 0.0952 -> <0.1 -> 5. Current ratio 56,768.07/18,172.60 = 3.124x -> 5. ALL CORRECT.

**Block F margins** — the maker's expense reconstruction (basis note 1) was tested
by back-solving PBT and it holds to the rupee:
BALUFORGE FY25: 923.62 - 672.51 = 251.11 op EBITDA; 251.11+17.14-3.35-10.96 =
253.94 = reported PBT. EXACT.
BALUFORGE FY26: 1107.37 - 807.84 = 299.53; 299.53+32.92-9.96-16.45 = 306.04 =
reported PBT. EXACT.
This matters: FY26 "Selling and admin" is blank in screener-Data_Sheet, which
would normally inflate the FY26 operating margin. The PBT reconciliation proves
the FY26 selling cost was reclassified into Other Expenses (63.09 vs 9.93 the
prior year), not lost. The M1 margin is therefore sound. Good practice.
HAPPYFORGE FY25 recomputed on the identical basis: 1408.89-1002.08 = 406.81 ->
28.87%, and 406.81+37.33-77.06-7.53 = 359.55 = reported PBT. EXACT. The peer
comparison in M2 is basis-consistent with the company. Peer median 19.41%,
gap +7.78pp -> >=5pp -> M2 = 5. CORRECT.
GM proxy: (923.62-(607.75-5.11))/923.62 = 34.75%, matching B01, and the
"Material Cost consumed" label states the net-of-inventory-change basis.
HAPPYFORGE on the same basis = 58.00%, matching B01. Basis-consistent. M9 = 0.
CORRECT.
M3 FAT 1107.37/546.58 = 2.026x with ROCE 18.47% -> FAT>2x AND ROCE>15% -> 3. CORRECT.
M11 windows recomputed: FY23->FY26 = 50.22%; FY21->FY24 = 57.93%. B01: 50.2% and
58.0%. MATCH. Latest < prior so the top band fails; CAGR >=20% with selling
expense declining (10.19% FY21 -> 5.01% FY25) -> 3. CORRECT.
M12 WC days 201/148/121, all >45 -> 0. CORRECT.
Moat sum 5+5+3+3+3+0+0+0+0+5+3+0 = 27. MATCH. Tests scoring >=3: M1 M2 M3 M4 M5
M10 M11 = 7. 7 >= 6 -> FORTRESS. CORRECT.

### 1.2 Rule-by-rule table

| # | Rule (prompt 01) | Verdict | Recomputed / note |
|---|---|---|---|
| G1 | Opening "Data available: X years" line | PASS | 6 years, FY2021-FY2026, format as written |
| G2 | Source anchor on every extracted number | PASS | Anchors present throughout; fidelity is Verifier A's call |
| G3 | Grounded claims; missing data -> N/A and score 0 | PASS | E3 pledge and M6 R&D both N/A-and-0 with reason |
| G4 | Use available history, min 3 max whatever exists | PASS | 6 years used |
| G5 | ROCE: use source figure if provided, else compute and state "computed" | **FAIL (MINOR)** | Screener provides no ROCE (Balance_Sheet.csv is a header-only blank template; Data_Sheet has no ROCE row), so computing was mandatory and correct. The literal word "computed" is never stated. Formula, inputs and per-year basis labels ("proxy" / "AR-precise") are all shown, so the rule's intent is met. Labelling formality only. |
| G6 | ROE formula, earliest-year closing-net-worth exception stated | PASS | All six re-derived; FY21 exception stated |
| G7 | WC Days formula + state which basis | PASS | Revenue basis correct (no COGS line exists); basis stated |
| G8 | FCF = CFO - capex | PASS | Proxy substitution for FY21/22/26 disclosed in basis note 5 |
| G9 | CAGR formula | PASS | Both re-derived to within 0.01pp |
| G10 | CAGR edge rules (negative endpoint / swing / C4 N/M) | PASS | All three non-triggers stated |
| G11 | A1-A4 thresholds | PASS | All re-derived |
| G12 | B1-B4 thresholds | PASS | All re-derived. B4 runs on the FY23-25 window because payables exist only in the ARs; disclosed twice (basis note 6, data note 3). Prompt rule 6 (use available history) governs over rule 5 here, and the substitution is transparent. |
| G13 | C1-C4 thresholds | PASS | All re-derived |
| G14 | D1-D4 thresholds | PASS | D4 runs on FY2025 because screener has no current/non-current split; period mismatch flagged at the line and in data note 10 |
| G15 | E1-E4 thresholds | PASS | E2 scored 0 mechanically despite the dilution explanation, which is the correct discipline |
| G16 | M1-M12 scoring | PASS | M1 M2 M3 M9 M10 M11 M12 re-derived; all correct |
| G17 | Peer-data absent -> score 0 and mark "PEER DATA NEEDED" | **FAIL (MINOR)** | Peer data WAS supplied for 3 peers, so the zero-and-flag branch never engages and M2/M5/M9 are legitimately scored. The maker invented the label "PEER DATA LIMITED", which is not in the prompt, and carried it into data_notes where the prompt names "PEER DATA NEEDED items". Non-standard vocabulary in a defined field. No score impact. |
| G18 | Moat classification (6+ = FORTRESS) | PASS | 7 present -> FORTRESS |
| G19 | Core score derivation | **FAIL (MAJOR)** | B01 sets core = A+B+C+D = 63/80, excluding Block E. Recomputed core = A+B+C+D+E = 19+5+20+19+9 = **72/100**. Three reasons the A-E reading governs: (a) the prompt defines five 20-point blocks A-E plus a separate 60-point Block F, so the matrix bands (>=80 / 60-79 / 40-59 / <40) are calibrated to a 100-point scale — on an 80-point scale the ">=80" band would require a literally perfect score and be dead; (b) the report's own grand total is A+B+C+D+E+F = 99, so core 63 + moat 27 = 90 does not reconcile with its own 99; (c) the block payload lists blocks A through E and then core_score. **Decision-neutral: 63 and 72 both fall in the 60-79 band, so the matrix lookup and the final classification are unchanged.** |
| G20 | Classification matrix lookup | PASS | Core 60-79 + FORTRESS -> GOOD+ before overrides. Correct on either core value |
| G21 | Deal-breaker application, stating which years drive it | PASS | #2 and #4 fire, correctly identified; the driving years are named (FY22 -57.74 and FY24 -31.73 CFO) in the weakest-block line and the decision line. #5 pledge correctly NOT triggered on unknown data rather than assumed |
| G22 | Tighter cap governs | PASS | #4 (max AVERAGE) governs over #2 (max GOOD) -> AVERAGE |
| G23 | Data confidence band and history downgrade | PASS | 6 years -> "may not have seen full cycle" flag, no tier downgrade, history_downgrade false. Correct: downgrade applies at 3-4 years only |
| G24 | Grand total = A+B+C+D+E+F | PASS | 99, re-added and correct |
| G25 | FLAG-GATE0 emission when classification <= AVERAGE with depressors | PASS | Flag present with the depressors named |
| G26 | Block YAML field completeness and 200-word analyst_note cap | PASS | All fields present; analyst_note approx 150 words |
| G27 | block_b_trend carries the one number showing it | PASS | "deteriorating", 72.7% -> 12.2% CFO/PAT |
| G28 | Evidence series behind M4/M10 complete | **FAIL (MINOR)** | The receivable-days series is printed as "156->235->142->129->140", five values for six years. FY2022 (164.5 days, recomputed 128.96/286.08x365) is silently omitted. Both M4 and M10 rest on this series. Re-scored with FY22 included: M4 still fails "stable +/-10" -> 3 unchanged; M10 period change still -15.9 days, inside "rose <=10" -> 5 unchanged. No score impact. |

**Gate 0: 28 rules checked, 24 PASS, 4 FAIL (1 MAJOR, 3 MINOR).**

**Gate 0 recomputed outcome: core_score 72 (not 63); classification AVERAGE — I
concur.** The deal-breaker cap binds regardless of which core reading is used.

---

## PART 2: EMERGING MOAT (B07) COMPLIANCE

### 2.1 Scorecard re-derivation

The prompt fixes two things in Section 5: the likelihood x impact map
(HH=4, HM/MH=3, HL/MM/LH=2, ML/LM=1, LL=1, none=0) and the evidence multiplier
(documented 1.0x, claim 0.7x, inference 0.5x). Both were re-derived on all nine
scored rows.

| Row | Stated pair | Correct raw | Stated multiplier | Recomputed | B07 | Verdict |
|---|---|---|---|---|---|---|
| A1 | MM | 2 | 0.5x (inference) | 1.0 | 1.0 | MATCH |
| A3 | ML | 1 | 1.0x (documented) | 1.0 | 1.0 | MATCH |
| B2 | MH | 3 | 0.7x (claim) | 2.1 | 2.1 | MATCH |
| C1 | ML | 1 | 0.5x (inference) | 0.5 | 0.5 | MATCH |
| E2 | MM | 2 | 0.7x (claim) | 1.4 | 1.4 | MATCH |
| F1 | LM | 1 | 0.7x (claim) | 0.7 | 0.7 | MATCH |
| G1 | ML | 1 | 1.0x (documented) | 1.0 | 1.0 | MATCH |
| H2 | LM | 1 | 0.7x (claim) | 0.7 | 0.7 | MATCH |
| R1 | HM | 3 | 0.7x (claim) | 2.1 | 2.1 | MATCH |

Sum = 1.0+1.0+2.1+0.5+1.4+0.7+1.0+0.7+2.1 = **10.5**. B07: 10.5. MATCH.
10.5 < 12 -> NONE (NO MEANINGFUL EMERGING MOAT). The bands are applied as
absolute per the 20-Aug-2026 operator ruling, which the report states. CORRECT.
I1/I2 contribution stated separately as 0.0, as the ruling requires. CORRECT.

Category count: A1-A4, B1-B3, C1-C2, D1-D2, E1-E2, F1-F2, G1-G2, H1-H3, I1-I2 =
22, plus R1 = **23 rows**, all present in both the Section 3 summary table and the
Section 5 scoring table. No category is silently skipped.

### 2.2 Evidence-tier discipline

Verifier C rule 3 asks specifically whether a category with only management-claim
evidence was scored as if documented. It was not, in any row. The discipline runs
the conservative way throughout:
- B2: the held certifications are 📄, but the SCORED item is the forming aerospace
  qualification, which is 🎙️, and 0.7x is applied. Correct and conservative.
- E2: revenue growth and export share are 📄, but the China+1 causal framing is
  🎙️, and 0.7x is applied to the whole row. Conservative.
- A1: capacity figures are 📄, but the "rare" characterisation is 🔍, and 0.5x is
  applied. Conservative.
- G1: the war-chest category has two legs. The rating-upgrade leg is 📄 and is
  credited at 1.0x; the net-cash-growing-while-investing leg is explicitly NOT met
  and explicitly NOT credited. This is the correct single-credit behaviour.
- H3: ESG targets are documented as stated commitments but current renewable
  consumption is nil, so the row scores 0 and moves to the optionality register
  rather than being credited as a forming moat. Correct.
No inflation found. This is the strongest part of the artifact.

### 2.3 Rule-by-rule table

| # | Rule (prompt 07) | Verdict | Note |
|---|---|---|---|
| E1 | All six sections executed in one response | PASS | Sections 1-6 all present |
| E2 | Evidence taxonomy applied to every single piece of evidence | **FAIL (MINOR)** | High coverage but not total. Untagged items include the 2A Mercedes Benz row, the 2A capacity-addition column and parts of 1C. |
| E3 | Source anchor on every evidence item | **FAIL (MINOR)** | Roughly 15 anchors use an approximate page marker ("p.[[PAGE ~13]]", "p.[[PAGE ~168]]", "p.[[PAGE ~213]]", "p.[[PAGE ~8]] ... area"). A tilde is not a page. Separately, "Concall PPT Nov 2025 p.559-561" is an implausible slide number for a deck and looks like a concatenated-corpus index; it is the sole anchor for MOOWR, which is the only company-specific 📄 item carrying R1. Referred to Verifier A for fidelity; logged here as an anchoring-rule gap. |
| E4 | Skeptical stance, hard evidence over promises | PASS | Strongly met. The Naya Energy Works impairment catch, the AOC-1 "no joint venture" contradiction, the dropped E-Mobility segment and the nil-renewables check against the 2035 target are all adversarial reads the rule asks for. |
| E5 | "NO EVIDENCE FOUND" where absent, never force-fit | PASS | 14 categories carry it explicitly with reasons |
| E6 | Completionist guard, 📄 recount performed | **FAIL (MAJOR)** | The recount itself is performed and correctly scoped: 6 documented items feeding 4 scored categories, well inside the 3-6 base rate. But the block payload reports `evidence_mix: {documented: 18, claim: 21, inference: 6}`. Eighteen documented items against a recount of six, unreconciled anywhere in report or block. The completionist guard exists precisely to make the 📄 count honest, so publishing two 📄 counts that differ by 3x defeats it. A downstream stage reading evidence_mix draws a materially different picture than one reading completionist_recount. No score impact (only A3, F2 and G1 carry a 1.0x multiplier, and F2 is zero-rated). Clearable by stating the scope difference. |
| E7 | Section 1A/1B/1C complete | PASS | 1C's missing 3-year target is marked NOT FOUND rather than estimated |
| E8 | Section 2A/2B/2D complete | PASS | 2B is NOT FOUND with a stated reason, which is compliant |
| E9 | Section 2C: capex under execution x historical FAT, arithmetic shown | **FAIL (MINOR)** | The prescribed method was computed (417.11 x 10.8 = approx 4,505 Cr, arithmetic shown and correct) and then discarded as unusable, with a proxy (forging-capacity ratio, +50%) substituted into the block field. Discarding a prompt-fixed formula is a deviation. Three mitigations: the substitution is disclosed in the report, the block and analyst_note; the deemed-cost artefact behind the inflated turnover is documented and real; and my own recomputation corroborates the answer. The maker computed FAT on FY25 average net PPE (10.8x) while B01's M3 computed FAT on FY26 net block (2.03x) — an unreconciled cross-stage basis split. Applying the prescribed method on the B01-consistent basis and the latest capex under execution: FY26 CWIP 277.31 x 2.03 = 563 Cr = **+50.8% of FY26 revenue**, against the reported 50. The reported figure survives the prescribed method; only the route to it is non-compliant. |
| E10 | All 22 categories plus R1 addressed | PASS | 23 rows, verified above |
| E11 | Categories 21/22 present; I1 above 0 only with both legs, (b) leg 📄; I2 above 0 only with a specific named sacrifice | PASS | Both present, both 0. I1 is refused at the (a) leg on the median-remuneration evidence, so the (b) leg question never arises. I2 gives the honest "nothing must be destroyed" answer and correctly reclassifies the NATO/aerospace firsts as an execution lead, which the category definition excludes. This is exactly the designed outcome for a typical company. |
| E12 | Section 3 summary table with all rows and the strength counts | **FAIL (MINOR)** | The count line is published self-contradictory: "Weak: 6 (A1, A3, C1, E2, F1, G1, H2 — 7 actually, see below)". Seven is right and 14 None reconciles to 23, but an uncorrected contradiction was shipped. Related: E2 is labelled "Weak-Moderate", which straddles the Moderate bar that governs the `active_categories` field. E2 was excluded from active_categories, the conservative choice, but the label should resolve to one side. |
| E13 | Section 4 4A/4B/4C complete | PASS | 4B carries amounts, duration, enrolment status and the competitors-share column as required |
| E14 | Section 5 raw matrix mapping | PASS | All nine rows re-derived |
| E15 | Evidence multipliers applied correctly | PASS | All nine rows re-derived |
| E16 | Adjusted total arithmetic | PASS | 10.5, re-added |
| E17 | Classification bands absolute, no rescale | PASS | <12 -> NONE, ruling cited |
| E18 | I1/I2 contribution stated separately | PASS | 0.0, stated |
| E19 | Scores consistent with stated evidence tiers | PASS | See 2.2. No 🎙️ row scored as 📄 |
| E20 | Optionality register: 0 or 🎙️/🔍-only rows, four columns, carried in block | PASS | 7 rows, all four columns, mirrored in the block. Nothing registered is also scored |
| E21 | Section 6 6A-6E complete | PASS | 6E's moat evolution map is delivered on the emerging side only. The existing side is not itemised because the prompt injects `{{B01_YAML}}`, which carries `moats_confirmed: 7` and `moat_class` but no per-test M1-M12 list. The maker states this limitation rather than inventing the map. Correct NOT-FOUND-with-reason behaviour. |
| E22 | F2 executed per the category definition (NO-CONCALL substitution) | **FAIL (MINOR)** | The substitution itself is fully compliant and well handled — see 2.4. The gap is coverage inside F2: the category names four legs (capex on time and budget, ramp speed post-commissioning, revenue per employee trend, guidance delivery). Two were tested (capex timing, and guidance delivery via B05, though the latter is discussed at 6D rather than inside F2). Ramp speed and revenue-per-employee trend were not tested at all. Revenue per employee looks computable: revenue is known and the AR carries a Rule 5(1) remuneration annexure. Both untested legs are positive-direction legs, so omitting them can only have suppressed the score, and the score is already floored at 0 by two adverse findings. No score impact, but two of four defined legs were skipped without being marked absent. |
| E23 | Block YAML field completeness | PASS | All fields present; analyst_note approx 85 words, inside the 200 cap. One `catalysts_12m` entry carries window "12-24m" in a field named for 12 months — cosmetic, folded into E12 rather than counted separately |
| E24 | 6D combined classification from the standard set | PASS | AVERAGE, from the permitted set, with the reasoning the prompt demands for the transition-setup case; the report correctly states this is NOT the GOOD/AVERAGE-backward-plus-EXPANSION-forward setup the strategy hunts |

**Emerging Moat: 24 rules checked, 18 PASS, 6 FAIL (1 MAJOR, 5 MINOR).**

### 2.4 Judgement on the F2 no-concall substitution (asked for explicitly)

**Verdict: compliant, and better than a substitution needed to be.**

The reasoning matters, so I will state it. F2's own definition in prompt 07 reads:
"execution moat (capex on time and budget across ARs, ramp speed post-
commissioning, revenue per employee trend, guidance delivery; cross-reference the
injected concall promise-delivery record)." Capex-on-time-and-budget-across-ARs is
the FIRST named test inside the category, not a fallback invented to plug a hole.
So in no-concall mode the maker did not substitute a foreign test for the
prescribed one. It ran the category's own leading test and lost only the
cross-reference leg, which had no input to reference.

Four things were done right:
1. The substitution is declared twice, in the sources header and again at F2
   itself, naming it as the orchestrator's rule rather than a silent choice.
2. Two dated, AR-sourced commitments were identified and tested against later
   sources: the Mercedes Benz unit ("fully operational Q2 FY25", FY2024 AR) and
   the defence forging line ("H1 FY26", FY2025 AR).
3. The finding is adverse and is scored as adverse. Two of two testable
   commitments slipped. The row scores 0 and the report states explicitly that
   this is "evidence AGAINST an execution moat, not for one" and "a genuine
   finding, not an absence of data". That distinction is the right one: an
   absence would have been NO EVIDENCE FOUND, and this is not that.
4. Nothing was credited from the substitution in either direction beyond what the
   evidence supports. The finding propagates to a FLAG-EXECUTION in the block.

The only gap is the coverage one logged at E22, and it cannot have inflated
anything.

### 2.5 Judgement on the degradation map (asked for explicitly)

The corpus has no results filings, no rating report, no shareholding pattern, no
announcements and no prospectus. The test is whether dependent categories are N/A
with a stated reason rather than silently skipped. Checked:
- B01 E3 (promoter pledge): depends on a shareholding-pattern filing. Marked
  "N/A (not in provided data)", scored 0, reason stated at the line, in data note
  8 and in the block data_notes. COMPLIANT.
- B01 E1/E2 (promoter holding): fell back to the AR corporate-governance
  disclosure, with the 18-month staleness stated at the line and in data note 6.
  COMPLIANT.
- B01 D4 (current ratio): no FY2026 split exists, so FY2025 is used, and the
  period mismatch against D1-D3 is flagged at the line and in data note 10.
  COMPLIANT.
- B01 B4 / M12 (WC days): payables exist only in the ARs, so a 3-year window is
  used. Disclosed in basis note 6 and data note 3. COMPLIANT.
- B01 M6 (R&D): no R&D/revenue percentage anywhere in corpus. Scored 0 and marked
  N/A with reason. COMPLIANT.
- B07 2B (utilisation): NOT FOUND with an explanation of why the gap matters.
  COMPLIANT.
- B07 input_gaps: names both the missing concalls and the missing FY2026 AR.
  COMPLIANT.
No silently skipped category was found in either artifact. Both makers also
declined to fill any gap with an estimate. The NEVER rule on estimation holds.

I note without grading it that the six-year history is assembled from screener
data for the years no annual report covers, and that both artifacts say so
repeatedly and label every affected line ("proxy" vs "AR-precise" in B01,
"unaudited"/"deck-only" in B07). The freshness limitation is disclosed, not
concealed.

---

## PART 3: RULES NOT IN PHASE-1 SCOPE

| Verifier C rule | Status |
|---|---|
| 4 (valuation B11, deepest audit) | NOT RUN — stage 11 not executed. Deferred to phase 3 |
| 5 (destination PE / Hurdle severity ladder) | NOT REACHED — no valuation to grade |
| 6 (downstream signal candidates, B09) | NOT RUN — B09 not among phase-1 inputs |
| 7 (method plurality, B11) | NOT RUN — deferred to phase 3 |
| 9 (Business Understanding Narrative, stage 13) | NOT RUN — stage 13 not executed. The block fields are emitted false as placeholders and must NOT be read as failures |
| 10 (Halt 1 dossier B09b) | NOT MINE NOW — the rule text places this at the /finalize verifier pass; the phase-1 structural check is mechanical inside run-pipeline step 6b |
| 11 (v3.8 exit construction) | NOT RUN — deferred to phase 3 |
| 12 (Amendment 19 FV path) | NOT RUN — deferred to phase 3 |

---

## PART 4: CONSOLIDATED FINDINGS

| Severity | Location | Finding | Recomputed value |
|---|---|---|---|
| MAJOR | B01 CLASSIFICATION; B01 block core_score | Core score computed as A+B+C+D, excluding Block E. The A-E reading governs: the matrix bands are calibrated to 100, and the report's own grand total (99) does not reconcile with core 63 + moat 27 = 90 | core_score = **72**, not 63. Band 60-79 unchanged; matrix lookup GOOD+ unchanged; final classification AVERAGE unchanged |
| MAJOR | B07 block evidence_mix vs completionist_recount | `documented: 18` in evidence_mix against 6 documented items in the completionist recount, unreconciled. Defeats the purpose of the guard the prompt mandates | No score change; em_score 10.5 stands |
| MINOR | B01 Block A / basis note 4 | ROCE computed (correctly, since the screener export supplies none) but never labelled "computed" as the formula rule requires | No change |
| MINOR | B01 Block F header / data note 11 | "PEER DATA LIMITED" substituted for the prompt's defined "PEER DATA NEEDED" vocabulary | No change; peer data existed so the zero-and-flag branch does not apply |
| MINOR | B01 M4 / M10 | Receivable-days series printed with five values for six years; FY2022 (164.5 days) omitted | M4 stays 3, M10 stays 5 |
| MINOR | B07 Section 2C | Prompt-fixed capex x FAT method computed then discarded for a self-designed capacity proxy; FAT basis (FY25 average net PPE, 10.8x) unreconciled with B01 M3 (FY26 net block, 2.03x) | Prescribed method on the B01-consistent basis and latest capex: 277.31 x 2.03 = 563 Cr = **+50.8%**, against the reported **50**. Reported figure survives |
| MINOR | B07 Section 3 summary count line | Published self-contradiction: "Weak: 6 ... 7 actually". E2's "Weak-Moderate" label straddles the bar governing active_categories | Weak = 7; Moderate = 2; None = 14; total 23 reconciles |
| MINOR | B07 F2 | Two of the category's four named legs (ramp speed, revenue per employee) untested and unmarked | Score 0 unchanged; untested legs are positive-direction only |
| MINOR | B07 evidence taxonomy | Several evidence items untagged (2A Mercedes row, 2A capacity column, parts of 1C) | No change |
| MINOR | B07 anchors | Approximately 15 approximate page markers ("~"); one implausible deck anchor (p.559-561) carrying the load-bearing MOOWR item | Referred to Verifier A for fidelity |

**Observations, not graded as failures:**
- R1 scores raw 3 while 4C itself concludes the tailwind is "shared across the
  entire Indian defence-vendor base, not company-exclusive". The likelihood x
  impact assignment is judgment the prompt does not fix, and the shared-benefit
  question was asked and answered as required, so this is not a rule breach. It is
  decision-neutral in any case: zeroing R1 gives 8.4, still NONE.
- B07 6C repeats "Gate 0 core score 63/80" faithfully from the injected block.
  That is correct behaviour by B07; the defect belongs to B01 and is graded once.
- B01's PBT back-solve as a control on the screener expense-sign convention is
  better practice than the prompt requires. It is what allowed me to confirm the
  FY26 blank selling-and-admin line does not inflate the M1 margin.

---

## PART 5: VERDICT

Neither artifact contains a CRITICAL framework failure. No misapplication found
in phase-1 scope changes a classification or a decision.

- **Gate 0: AVERAGE. I concur.** Recomputed core is 72 rather than 63, but both
  land in the 60-79 band, and deal-breaker #4 (cumulative CFO/PAT 0.21 < 0.50)
  caps the classification at AVERAGE regardless of the matrix result. The
  deal-breaker chain, the tighter-cap rule and the confidence-band handling are
  all applied as written.
- **Emerging Moat: NONE (10.5). I concur.** The scorecard re-derives exactly. The
  band is applied as absolute per the operator ruling. All 23 categories are
  scored or explicitly refused. Evidence tiering is conservative in every row and
  no management claim is dressed as documented.
- **Combined AVERAGE.** Concur.

Acceptance rate 81% (42 of 52 rules passed), above the 60% REWORK trigger. No
REWORK is recommended for stage 1 or stage 7 on framework grounds.

Two items are worth the orchestrator's attention before the artifacts are
consumed downstream, neither blocking: the B01 `core_score` field (72, not 63)
because a later stage may read it as an input, and the B07 `evidence_mix`
documented count (18) which contradicts the stage's own completionist recount (6).

---

```yaml
stage: B12c
company: "BALUFORGE"
run_date: "2026-09-06"
model: claude-opus-4-8
status: complete
gate0:
  rules_checked: 28
  fails:
    - {rule: "G19 core score derivation", severity: "MAJOR", detail: "core computed as A+B+C+D=63; correct basis A+B+C+D+E=72. Report's own grand total 99 does not reconcile with 63+27=90. Band 60-79 and final classification AVERAGE unchanged."}
    - {rule: "G5 ROCE 'computed' label", severity: "MINOR", detail: "screener supplies no ROCE so computing was mandatory and correct; the literal word 'computed' is never stated. Formula and per-year basis are shown."}
    - {rule: "G17 PEER DATA NEEDED vocabulary", severity: "MINOR", detail: "maker substituted the non-prompt label 'PEER DATA LIMITED'. Peer data existed, so the zero-and-flag branch correctly did not apply. No score impact."}
    - {rule: "G28 receivable-days series completeness", severity: "MINOR", detail: "five values printed for six years; FY2022 (164.5 days) omitted. Re-scored with FY22 included, M4 stays 3 and M10 stays 5."}
emoat:
  rules_checked: 24
  fails:
    - {rule: "E6 completionist guard consistency", severity: "MAJOR", detail: "block evidence_mix documented:18 contradicts the completionist recount of 6 documented items, unreconciled in report or block. Recount itself performed correctly. No score impact."}
    - {rule: "E9 Section 2C prescribed capex x FAT method", severity: "MINOR", detail: "prescribed method computed then discarded for a self-designed capacity proxy; FAT basis 10.8x (FY25 avg net PPE) unreconciled with B01 M3 2.03x (FY26 net block). Recomputed on the B01-consistent basis: 277.31 x 2.03 = 563 Cr = +50.8% vs the reported 50. Reported figure survives."}
    - {rule: "E12 Section 3 summary count line", severity: "MINOR", detail: "published self-contradiction 'Weak: 6 ... 7 actually'; E2 labelled 'Weak-Moderate' straddles the bar governing active_categories. Counts reconcile to 23."}
    - {rule: "E22 F2 leg coverage", severity: "MINOR", detail: "no-concall capex substitution itself fully compliant; but ramp speed and revenue-per-employee legs untested and unmarked. Both are positive-direction legs; score 0 unchanged."}
    - {rule: "E2 evidence taxonomy coverage", severity: "MINOR", detail: "several evidence items untagged (2A Mercedes row, 2A capacity column, parts of 1C)."}
    - {rule: "E3 source anchor precision", severity: "MINOR", detail: "approx 15 approximate page markers ('p.[[PAGE ~n]]'); one implausible deck anchor (Nov 2025 p.559-561) carries the load-bearing MOOWR item. Fidelity referred to Verifier A."}
valuation: {rules_checked: 0, fails: []}   # PENDING PHASE 3 - stages 10 and 11 not executed; B10/B11 do not exist
business_understanding_narrative: {present: false, five_questions_answered: false, prose_only: false, section6_candidates_named: 0, valuation_vocab_leak: false, fails: ["NOT APPLICABLE IN PHASE 1 - stage 13 not executed; false values are placeholders, NOT failures, and must not trigger REWORK"]}
recomputed_destination_pe: ""
recomputed_decision: ""
findings:
  - {severity: "MAJOR", location: "B01 CLASSIFICATION section / B01 block core_score", claimed: "core_score 63/80 (A+B+C+D)", recomputed: "core_score 72/100 (A+B+C+D+E)", note: "Decision-neutral: both values sit in the 60-79 band; matrix GOOD+ then deal-breaker #4 caps at AVERAGE either way. Flagged because a downstream stage may consume the field."}
  - {severity: "MAJOR", location: "B07 block evidence_mix vs completionist_recount", claimed: "documented: 18", recomputed: "recount states 6 documented items across 4 scored categories", note: "Unreconciled. Defeats the completionist guard the prompt mandates. Clearable by stating the scope difference. em_score 10.5 unaffected."}
  - {severity: "MINOR", location: "B01 Block A / basis note 4", claimed: "ROCE table", recomputed: "all six years re-derived and matching", note: "Rule requires stating 'computed' when the source supplies no ROCE. Screener export supplies none (Balance_Sheet.csv is a header-only template), so computing was correct; only the label is missing."}
  - {severity: "MINOR", location: "B01 Block F header / data note 11", claimed: "PEER DATA LIMITED", recomputed: "n/a", note: "Non-prompt vocabulary in a field the prompt defines as 'PEER DATA NEEDED items'. Substantive rule (never guess peer figures) was honoured."}
  - {severity: "MINOR", location: "B01 M4 / M10", claimed: "156->235->142->129->140", recomputed: "156.0 / 164.5 / 235.2 / 142.5 / 129.3 / 140.1", note: "FY2022 omitted from a six-year series that carries two moat tests. Neither score changes."}
  - {severity: "MINOR", location: "B07 Section 2C / capex_embedded_growth_pct", claimed: "50 (capacity-ratio proxy, prescribed method declared unusable)", recomputed: "+50.8% via the prescribed method on the B01-consistent asset basis and FY26 CWIP (277.31 x 2.03 = 563 Cr)", note: "Route non-compliant, answer sound. Cross-stage FAT basis split (10.8x vs 2.03x) should be reconciled before stage 11 consumes either."}
  - {severity: "MINOR", location: "B07 Section 3 summary count line", claimed: "Weak: 6 ... 7 actually", recomputed: "Weak 7, Moderate 2, None 14, total 23", note: "Uncorrected self-contradiction shipped; E2 'Weak-Moderate' straddles the bar governing active_categories."}
  - {severity: "MINOR", location: "B07 F2", claimed: "capex-completion substitution, scored 0", recomputed: "0 confirmed", note: "Substitution itself fully compliant and correctly declared. Ramp speed and revenue-per-employee legs untested and unmarked; both positive-direction, so no inflation possible."}
  - {severity: "MINOR", location: "B07 Sections 1C and 2A", claimed: "various evidence items", recomputed: "n/a", note: "Evidence taxonomy tag missing on several items where the prompt requires one on every piece of evidence."}
  - {severity: "MINOR", location: "B07 throughout", claimed: "p.[[PAGE ~n]] anchors; Concall PPT Nov 2025 p.559-561", recomputed: "n/a", note: "Approximate page markers are not pages. The MOOWR anchor is implausible as a deck slide and carries the only company-specific documented item behind R1. Fidelity is Verifier A's call."}
critical_count: 0
major_count: 2
minor_count: 8
acceptance_rate: 81            # 42 of 52 phase-1 rules passed (Gate 0 24/28 + Emerging Moat 18/24)
```
