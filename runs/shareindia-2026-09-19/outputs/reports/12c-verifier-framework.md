# STAGE 12 VERIFIER C: FRAMEWORK ADHERENCE (B12c), PHASE 1 SCOPE
Company: SHAREINDIA | Run date: 2026-09-19 | Model: claude-opus-5

Scope: Gate 0 (B01) and Emerging Moat (B07) only. The valuation audit (B10, B11,
rules 4-7 and 9-15) is pending phase 3. No valuation framework document was
read or cited.

Rule sources: prompts/01-gate-0-pipeline.md (cited as G0 with line numbers),
prompts/07-emerging-moat-pipeline.md (cited as EM with line numbers).
Audited artifacts: outputs/reports/01-gate0.md, outputs/blocks/B01-gate0.yaml,
outputs/reports/07-emoat.md, outputs/blocks/B07-emoat.yaml. One input file was
opened to test a rule-application claim, not to verify numbers:
inputs/screening/SHAREINDIA-screener-consol-ratios.csv (rows 2-6, day-count
rows). Verifier A owns number fidelity.

---

## 1. GATE 0 (B01) COMPLIANCE TABLE

Every block score was re-derived from the inputs the report states, using the
G0 thresholds.

| # | Rule (G0 line) | Stated input | Band applied | Verdict | Recomputed / note |
|---|---|---|---|---|---|
| 1 | Opening data-availability line (G0 L23-25) | 11 yrs FY16-FY26 | n/a | PASS | Present, report L5-8 |
| 2 | A1 median ROCE (L55) | sorted 18..57, median (28+32)/2 = 30% | >=25 = 5 | PASS | 5 |
| 3 | A2 min ROCE (L56) | 18% | >=15 = 5 | PASS | 5 |
| 4 | A3 median ROE (L57, formula L31-32) | 11 values, 6th of sorted = 26.67% | >=20 = 5 | PASS | 5; FY16 closing-NW basis stated per L32 |
| 5 | A4 ROCE trend (L58-59) | FY26 18 vs FY17 28, -10pp | >5pp decline = 0 | PASS | 0; FY17 used as earliest because FY16 ROCE absent, stated |
| 6 | Block A sum | 5+5+5+0 | | PASS | 15 |
| 7 | B1 cum CFO / cum PAT (L62) | 152 / 1,787 = 0.085 | <0.50 = 0 | PASS | 0; sums re-added, match |
| 8 | B2 FCF-positive years (L64) | 8 of 11 = 72.7% | 50-74 = 2 | PASS | 2 |
| 9 | B3 cum FCF / cum PAT (L65) | 81 / 1,787 = 0.045 | <0.20 = 0 | PASS | 0; sums re-added, match |
| 10 | B4 change in WC days (L67, formula L33-38) | screener "Working Capital Days" 29 to -139 | decreased >5 = 5 | FAIL (MINOR) | Formula substituted. See finding G-3 |
| 11 | Block B sum | 0+2+0+5 | | PASS (arithmetic) | 7 as stated; 2 under strict B4 reading |
| 12 | C1 revenue CAGR (L71, L41) | (1,470/74)^(1/10)-1 = 34.8% | >=20 = 5 | PASS | 5 |
| 13 | C2 PAT CAGR (L72) | (324/6)^(1/10)-1 = 49.0% | >=20 = 5 | PASS | 5 |
| 14 | C3 positive YoY years (L73) | 9 of 10 = 90% | 75-99 = 3 | PASS | 3 |
| 15 | C4 PAT minus revenue CAGR (L74) | +14.2pp | >=+3pp = 5 | PASS | 5 |
| 16 | Block C sum | | | PASS | 18 |
| 17 | D1 CAR route (L77-79) | CAR N/A | N/A = 0 (L20-21) | PASS | 0 |
| 18 | D2 PCR route (L80-81) | proxy 38.1%, subsidiary level | <60 = 0 | PASS | 0; proxy labelled; strict N/A would also give 0 |
| 19 | D3 financials default (L84) | default 3 | | PASS | 3 |
| 20 | D4 current ratio (L85-86) | N/A | 0 | PASS | 0 |
| 21 | Block D route choice | financials substitution per B00 row | | PASS with note | 3. General-corporate route gives D1 0 (net debt not buildable), D2 2 (IC 4.36x), D3 4 (D/E 0.26), D4 0 = 6; core 49; still AVERAGE. Route flagged by maker for Phase 3 |
| 22 | E1 promoter holding (L89) | 48.62% | 40-49.9 = 3 | PASS | 3 |
| 23 | E2 promoter change (L91-92) | -4.19pp over ~2.75 yrs | >3% decrease = 0 | PASS with note | 0; short window stated, nearest endpoints |
| 24 | E3 pledge (L93) | 57.80% of promoter holding (28.10% of total) | >15 = 0 | PASS | 0 on either basis |
| 25 | E4 contingent liab / NW (L94-95) | 3,233.44 / 2,635 = 122.7% | >30 = 0 | PASS | 0 |
| 26 | Block E sum | | | PASS | 3 |
| 27 | M1 pricing power (L102-104) | OPM +20pp, rev CAGR 34.8% | top band = 5 | PASS | 5 |
| 28 | M2 cost advantage (L105-106) | 39 vs peer median 35, +4pp | 2-5pp = 3 | PASS | 3 |
| 29 | M3 capital efficiency (L107-108) | FAT 22.6x, ROCE FY26 18% | FAT>2 and ROCE>15 = 3 | PASS with note | 3; rule does not say latest vs median ROCE; median (30%) would give 5; present either way |
| 30 | M4 customer stickiness (L109-111) | 1 decline year; FY26 1,470 < FY24 1,483 | "max 1 decline year, fully recovered = 3" | FAIL (MAJOR) | Not fully recovered. See finding G-1. Recomputed 1 |
| 31 | M5 scale (L112-113) | mcap not in data | PEER DATA NEEDED = 0 (L99-100) | PASS | 0 |
| 32 | M6 R&D (L114-116) | N/A | 0 | PASS | 0 |
| 33 | M7 regulatory (L117-119) | ">10 listed players" from general market knowledge | regulated >10 = 1 | FAIL (MINOR) | Player count not in provided data (G0 L19-21). See finding G-4. Recomputed 0 |
| 34 | M8 distribution (L120-122) | quantified, not growing | 0 | PASS with note | 0; no band fits "quantified, not growing"; resolved downward. See G-1 on asymmetry |
| 35 | M9 brand (L123-125) | OPM +4pp vs peers, CAGR 34.8% | 0 | PASS with note | 0; OPM used in place of the L125 GM proxy (stated); band gap resolved downward |
| 36 | M10 switching costs (L126-128) | growth all but 1 yr; debtor days 91 to 9 | 3 | PASS | 3 |
| 37 | M11 network effects (L129-133) | latest 3y 10.6% < prior 3y 68.4%; selling % N/A | 0 | PASS | 0 |
| 38 | M12 negative WC / float (L134-135) | screener WC days negative 10 of 11 yrs | majority negative = 5 | FAIL (MAJOR) | Same formula substitution as B4, and here it decides the moat test. See finding G-2. Recomputed 0 |
| 39 | Moat count and class (L98-99, L137-138) | 6 present = FORTRESS | | FAIL (MAJOR, consequential) | Present under rules as written: M1, M2, M3, M10 = 4 = STRONG. M4 alone flips the label to STRONG (5) |
| 40 | Core score sum | 15+7+18+3+3 = 46 | | PASS (arithmetic) | 46 as stated; 41 under strict B4 reading |
| 41 | Data confidence (L142-144) | 11 yrs, full | | PASS | No downgrade |
| 42 | Classification matrix (L147-149) | Core 40-59 = AVERAGE | | PASS | AVERAGE at 46, 41, or 49 (general D route); moat class irrelevant in this band |
| 43 | Deal-breakers (L151-159) | #2, #4, #5 triggered; #6 not evaluable | | PASS | Re-checked all nine. #6 would not trigger on general-corporate inputs either (IC 4.36x > 3x). Driving years named per L152-154 |
| 44 | CAGR edge rules (L43-50) | revenue and PAT endpoints positive; no loss-to-profit swing | | PASS | Honoured; no synthetic CAGR |
| 45 | FLAG-GATE0 and block_b_trend (L175-177, L191) | flag present, trend "deteriorating" with numbers | | PASS | |
| 46 | analyst_note cap (L193-197) | ~140 words | <=200 | PASS | |
| 47 | YAML/report internal consistency | analyst_note "six of twelve tests are 0" | | FAIL (MINOR) | Zero-scored tests are M5, M6, M8, M9, M11 = 5, not 6. See finding G-5 |

Gate 0 tally: 47 rules checked, 41 PASS, 6 FAIL (2 MAJOR, 1 MAJOR
consequential, 3 MINOR).

### Gate 0 recomputation under rules as written

| Field | B01 value | Recomputed | Change driver |
|---|---|---|---|
| M4 | 3 | 1 | G-1 |
| M7 | 1 | 0 | G-4 |
| M12 | 5 | 0 | G-2 |
| moat_score | 23 | 15 | sum of the three |
| moats_confirmed | 6 | 4 | M4, M12 drop below 3 |
| moat_class | FORTRESS | STRONG | L137 |
| B4 / Block B / core | 5 / 7 / 46 | 0 / 2 / 41 under strict N/A reading; unchanged under a receivable-days-only reading | G-3 |
| classification | AVERAGE | AVERAGE (no change) | core band 40-59 either way |
| deal_breakers | #2, #4, #5 | #2, #4, #5 (no change) | Block B stays <8 |

The Gate 0 classification survives. The existing-moat label does not. B07
Section 6C and any downstream reader of moat_class carry FORTRESS; the rules
as written give STRONG.

### Gate 0 findings

**G-1 (MAJOR). M4 scored 3 against a band whose condition is not met.**
G0 L109-111: "max 1 decline year, fully recovered = 3". B01 report L236-242
states FY26 revenue 1,470 Cr is 99.1% of the FY24 peak 1,483 Cr, so the peak
is not re-taken. The maker flagged it as a judgment call but still scored the
upper band. No band covers "1 decline year, not recovered". The next defined
band down is "2 decline years, CAGR positive = 1". Recomputed M4 = 1. This
alone moves moats_confirmed from 6 to 5 and moat_class from FORTRESS to STRONG.
The band-gap handling is also asymmetric inside the same block: the M8 and M9
gaps were resolved to the lower score (report L262-271, "most conservative
literal reading"), while the M4 gap was resolved to the higher score. The rule
bar must be the same in both directions.

**G-2 (MAJOR). M12 rests on a substituted working-capital formula.**
G0 L27 fixes the formulas: "fixed, do not substitute alternatives". G0 L33-38
defines WC Days = Receivable Days + Inventory Days - Payable Days. Only ROCE
carries a "use the source's figure" carve-out (L29-31). B01 used screener's own
"Working Capital Days" row (report L284-286; B01 data_notes line 31). The
source file shows screener's row is not the G0 formula: FY16 Debtor Days 91
with Inventory and Payable Days blank, yet screener WC Days = 29
(SHAREINDIA-screener-consol-ratios.csv rows 2-6). Inventory Days and Days
Payable are blank for every year except FY25 (620 and 1,466). Under G0 L19-21
the formula input is "N/A (not in provided data)" and scores 0. Recomputed
M12 = 0. With G-1, moats_confirmed = 4, STRONG.
Note for the operator: the negative float is economically plausible for a
broker holding client funds as payables. Admitting screener's WC Days for
financial intermediaries would need an operator ruling that extends the ROCE
carve-out. No such ruling is in the rule source.
Also imprecise: B01 report L77-79 says the Receivable-day component is blank
for FY16-FY24. Debtor Days is populated FY16-FY26 (91 to 9, row 2). Only the
Inventory and Payable components are blank.

**G-3 (MINOR). B4 uses the same substituted formula.**
Same rule and source as G-2. Strict N/A reading: B4 = 0, Block B = 2, core
41. A receivable-days-only reading (91 to 9, decrease of 82 days) keeps B4 at
5. Neither reading changes the AVERAGE band or the deal-breaker set, so the
grade is MINOR. The report should state which reading it used and why.

**G-4 (MINOR). M7 player count is not from provided data.**
G0 L19-21: "confirm it exists in the provided data ... Never fill gaps".
B01 report L250-253 states the ">10 listed players" count is "general market
knowledge of listed brokers, not a filed number". Recomputed M7 = 0 (N/A).
Moat score -1. No moat-count effect.

**G-5 (MINOR). analyst_note miscounts zero-scored moat tests.**
B01-gate0.yaml line 39: "six of twelve tests are 0". Zero scores are M5, M6,
M8, M9, M11 = 5 (report L243-283). The report body (L292-297) says "six of
twelve" rest on thin or borderline evidence, which is a different claim.
The YAML note conflates the two.

---

## 2. EMERGING MOAT (B07) COMPLIANCE TABLE

| # | Rule (EM line) | Verdict | Note |
|---|---|---|---|
| 1 | All six sections present (EM L28) | PASS | Sections 1-6 plus Optionality Register |
| 2 | Evidence taxonomy applied with anchors (EM L29-36) | PASS with note | Report L5-9 widens DOCUMENTED to "disclosed KPI" and "filed order", beyond the EM L30-32 list. No score depends on the widening except as noted in rule 11 |
| 3 | 22 categories plus R1 = 23 rows in Section 3 summary and Section 5 (EM L155, L171-174; Verifier C rule 3) | PASS | A1-A4, B1-B3, C1-C2, D1-D2, E1-E2, F1-F2, G1-G2, H1-H3, I1-I2, R1 = 23 rows in both tables |
| 4 | Unevidenced categories marked NO EVIDENCE FOUND (EM L39-40) | PASS | 16 rows explicit, each with a reason |
| 5 | Raw score matrix (EM L171-172) | PASS | ML=1, HM=3, LM=1 mapped correctly on every scored row |
| 6 | Multiplier: H1 (EM L172-173) | FAIL (MINOR) | See finding E-1. Recomputed 0.5 |
| 7 | Multiplier: I2 tier | FAIL (MINOR) | See finding E-2. Recomputed 0.5 |
| 8 | Multipliers on C1, C2, D1, D2, R1 | PASS | 0.7, 3.0, 0.7, 3.0, 0.5 |
| 9 | Adjusted total arithmetic | PASS | 0.7+3.0+0.7+3.0+1.0+0.7+0.5 = 9.6 |
| 10 | Classification band (EM L175-176) | PASS | <12 = NO MEANINGFUL EMERGING MOAT. Recomputed total 8.9 stays in the same band |
| 11 | Score consistent with evidence tier; no claim-only row scored as documented (Verifier C rule 3) | PASS with note | C2 trend uses three concall counts (claim tier) plus one AR figure (AR p.11); D2 growth leg uses the investor presentation (claim tier) plus AR p.11 level. Each row has a filed anchor, so neither is claim-only. Likelihood H on both leans on the claim-tier trend points |
| 12 | Completionist recount line (EM L41-46, L157-159) | PASS | "📄 recount performed: 4 documented items across 3 categories" (report L160). 7 active rows, below the 12 trigger |
| 13 | I1/I2 contribution stated separately (EM L180-181) | PASS | Report L216 |
| 14 | Category 21 (I1): above 0 only with both legs, (b) leg documented (Verifier C rule 8, EM L122-138) | PASS | Scored 0; "management quality" language correctly excluded |
| 15 | Category 22 (I2): above 0 only with a specific named sacrifice (Verifier C rule 8, EM L139-153) | PASS (borderline) | Named: a zero-branch discount broker would sacrifice its low-cost economics to build Tier-3 physical MTF distribution. That fits "an internal cost structure" (EM L145). Top band correctly withheld (no competitor filing) |
| 16 | Section 2C arithmetic shown or not fabricated (EM L60-62) | PASS | Declared not computable, reasons given; no estimate |
| 17 | YAML capex_embedded_growth_pct fill | FAIL (MINOR) | See finding E-3 |
| 18 | Optionality register present, in block (EM L183-196) | PASS | 8 rows, mirrored in B07 block |
| 19 | Optionality register completeness (EM L184: "scored 0 or rest only on 🎙️/🔍") | FAIL (MINOR) | See finding E-4 |
| 20 | F2 cross-references the injected promise-delivery record (EM L105-107) | PASS | 5 delivered / 3 partial / 2 missed, grade C (report L112) |
| 21 | 6C uses the injected Gate 0 block (EM L202-203) | PASS with note | Faithful copy of B01. It carries FORTRESS, which G-1/G-2 recompute to STRONG. Not a B07 error |
| 22 | 6D combined classification from the standard label set (EM L203-207) | PASS | AVERAGE; AVERAGE backward with NONE forward is not a transition cell |
| 23 | em_score = adjusted total (EM L224) | FAIL (MINOR) | See finding E-5 |
| 24 | active_categories only Strong/Moderate (EM L227) | PASS | C2, D2 |
| 25 | One improvement, one mechanism (A3/A4 folded into D2) | PASS | Stated at report L85-86 |

Emerging Moat tally: 25 rules checked, 20 PASS, 5 FAIL (all MINOR).
Recomputed adjusted total: 8.9 (9.6 - 0.5 H1 - 0.2 I2). Classification
unchanged: NO MEANINGFUL EMERGING MOAT.

### Emerging Moat findings

**E-1 (MINOR). H1 scored at the documented multiplier on mixed evidence.**
The Section 3 table (report L151) grades H1 "Documented (deals), inference
(causal link)". The category is "industry consolidation beneficiary". The
deals are documented, but the report itself says the beneficiary link is
NOT FOUND (L121). Section 5 applies 1.0x (L208). The load-bearing part of the
category claim is inference, so 0.5x applies. Recomputed 0.5. Bolt-on
acquisitions do appear in the EM L116-117 look-for list, so a documented tier
is arguable. The report should state which part the score rests on.

**E-2 (MINOR). I2 tier overstated.**
The management claim (Q1 FY27 call) says discount brokers have limited Tier-3
MTF options. That is a reach claim. The sacrifice itself (discount brokers
cannibalising their low-cost economics) is the scanner's own construction
(report L128, "implying"). That is analyst inference, 0.5x, not 0.7x.
Recomputed 0.5.

**E-3 (MINOR). capex_embedded_growth_pct carries 0 for a figure not found.**
B07-emoat.yaml line 30 fills 0 with a comment that it is NOT APPLICABLE. The
house rule is that NOT FOUND is the only valid fill for a missing number. A
consumer that reads the field without the comment sees a computed zero.
Fill "NOT FOUND" (or null plus the reason) instead.

**E-4 (MINOR). Optionality register omits claim-only rows.**
EM L184 registers every forward advantage that scored 0 or rests only on 🎙️
or 🔍 evidence. C1 (cross-sell, 0.7, claim only) and D1 (proprietary data,
0.7, claim only) are not registered. Also absent: the Silverleaf HFT revenue
line (claim, report L24), the Share India Cred Rs 500 Cr issuance target
(claim for the number, L21), and the "third-party countries" expansion
(concept, L26). Synthesis merges the register into the monitoring checklist,
so these would drop out of monitoring.

**E-5 (MINOR). em_score rounded.**
EM L224 defines em_score as the adjusted total. B07-emoat.yaml line 17 carries
10, with 9.6 in a comment. The schema does not require an integer. Carry 9.6
(8.9 on this verifier's recompute). No band effect: both sit below 12.

---

## 3. VALUATION (B10, B11)

Pending phase 3. Not audited in this run. Expectation ledger, Business
Understanding Narrative, downstream-candidate, method-plurality, exit
construction, Amendment 19, and skill-to-source checks (Verifier C rules 4-7,
9-15) all wait for their artifacts.

---

## 4. SUMMARY

- Critical: 0. Major: 2 (G-1, G-2). Minor: 8 (G-3, G-4, G-5, E-1 to E-5).
- Rules checked: 72 (47 Gate 0, 25 Emerging Moat). Passed: 61. Acceptance
  rate 84.7%.
- No finding changes the Gate 0 classification (AVERAGE), the deal-breaker
  set, the EM band (NONE), or the 6D combined assessment (AVERAGE).
- One label changes: the Gate 0 existing-moat class is STRONG under the rules
  as written, not FORTRESS. The maker already warned readers against the
  aggregate label; the rule recompute confirms that warning.
- Operator decision offered, not taken: whether screener's Working Capital
  Days may stand in for the G0 formula for financial intermediaries (G-2,
  G-3). That needs an operator ruling on prompts/01-gate-0-pipeline.md, on a
  framework branch, not in this run.

```yaml
stage: B12c
company: "SHAREINDIA"
run_date: "2026-09-19"
model: "claude-opus-5"
status: complete
scope: "phase 1 (Gate 0 B01 + Emerging Moat B07); valuation audit pending phase 3"
gate0: {rules_checked: 47, fails: ["M4 scored 3 but 'fully recovered' not met (FY26 1,470 < FY24 1,483); recomputed 1", "M12 uses screener WC Days, not the G0 L33-38 formula; inventory/payable components N/A; recomputed 0", "moat_class FORTRESS -> STRONG (moats_confirmed 6 -> 4; moat_score 23 -> 15) consequential on M4/M12/M7", "B4 uses screener WC Days (same substitution); strict reading B4 0, Block B 2, core 41; AVERAGE unchanged", "M7 '>10 listed players' from general market knowledge, not provided data; recomputed 0", "analyst_note says six moat tests score 0; actual count is 5 (M5, M6, M8, M9, M11)"]}
emoat: {rules_checked: 25, fails: ["H1 scored at 1.0x though the beneficiary link is inference/NOT FOUND; recomputed 0.5", "I2 sacrifice is analyst-constructed; tier 0.5x not 0.7x; recomputed 0.5", "capex_embedded_growth_pct filled 0 instead of NOT FOUND", "optionality register omits claim-only rows C1, D1 and claim items Silverleaf HFT, Cred Rs 500 Cr target, third-party-country expansion", "em_score carried as 10, adjusted total is 9.6 (verifier recompute 8.9); band NONE unchanged"]}
valuation: {rules_checked: 0, fails: []}   # pending phase 3
expectation_ledger: {present: false, downside_row: false, all_rows_confirm_by: false, all_rows_metric_threshold: false, prob_in_range: false, decay_status_valid: false, off_ledger_credit: false, residual_pct_cmp: 0, residual_starter_cap_ok: true, fails: []}  # pending phase 3, not audited
business_understanding_narrative: {present: false, five_questions_answered: false, prose_only: false, section6_candidates_named: 0, valuation_vocab_leak: false, fails: []}  # pending stage 13, not audited
recomputed_destination_pe: ""   # not applicable in phase 1
recomputed_decision: ""         # concur: Gate 0 AVERAGE, EM NONE, combined AVERAGE all survive
findings:
  - {id: G-1, severity: MAJOR, location: "01-gate0.md L236-242; B01 moats_confirmed/moat_class", rule: "prompts/01-gate-0-pipeline.md L109-111", issue: "M4 scored 3 on 'fully recovered' band though FY26 revenue is 99.1% of FY24 peak; band gaps resolved upward here but downward for M8/M9", recomputed: "M4 1; alone flips FORTRESS to STRONG"}
  - {id: G-2, severity: MAJOR, location: "01-gate0.md L284-286; B01 data_notes line 31", rule: "prompts/01-gate-0-pipeline.md L27, L33-38, L19-21", issue: "M12 uses screener Working Capital Days, which is not Rec+Inv-Pay (FY16 debtor days 91, screener WC days 29); inventory/payable days blank except FY25", recomputed: "M12 0; with G-1 moats_confirmed 4, moat_class STRONG, moat_score 15 (with G-4)"}
  - {id: G-3, severity: MINOR, location: "01-gate0.md L75-80", rule: "prompts/01-gate-0-pipeline.md L27, L33-38, L67-68", issue: "B4 uses the same substituted WC Days; report also misstates debtor days as blank FY16-FY24", recomputed: "strict: B4 0, Block B 2, core 41, still AVERAGE; receivable-only reading keeps 5"}
  - {id: G-4, severity: MINOR, location: "01-gate0.md L250-253", rule: "prompts/01-gate-0-pipeline.md L19-21, L117-119", issue: "M7 player count taken from general market knowledge, not provided data", recomputed: "M7 0; no moat-count effect"}
  - {id: G-5, severity: MINOR, location: "B01-gate0.yaml line 39", rule: "internal consistency", issue: "analyst_note says six moat tests score 0; five do", recomputed: "5 of 12"}
  - {id: E-1, severity: MINOR, location: "07-emoat.md L151, L208", rule: "prompts/07-emerging-moat-pipeline.md L172-173", issue: "H1 scored 1.0x while the category's beneficiary link is inference/NOT FOUND", recomputed: "0.5"}
  - {id: E-2, severity: MINOR, location: "07-emoat.md L128, L212", rule: "prompts/07-emerging-moat-pipeline.md L172-173", issue: "I2 sacrifice is the scanner's inference, scored at claim tier", recomputed: "0.5; total 8.9, band unchanged"}
  - {id: E-3, severity: MINOR, location: "B07-emoat.yaml line 30", rule: "CLAUDE.md NEVER: NOT FOUND is the only valid fill", issue: "capex_embedded_growth_pct carries 0 for a not-computable figure", recomputed: "NOT FOUND"}
  - {id: E-4, severity: MINOR, location: "07-emoat.md L224-237; B07 optionality_register", rule: "prompts/07-emerging-moat-pipeline.md L183-196", issue: "register omits claim-only rows C1, D1 and claim items Silverleaf HFT, Cred Rs 500 Cr target, third-party-country expansion", recomputed: "add 5 rows"}
  - {id: E-5, severity: MINOR, location: "B07-emoat.yaml line 17", rule: "prompts/07-emerging-moat-pipeline.md L224", issue: "em_score rounded to 10; adjusted total is 9.6", recomputed: "9.6 (verifier 8.9)"}
critical_count: 0
major_count: 2
minor_count: 8
acceptance_rate: 84.7             # 61 passed / 72 checked (47 Gate 0 + 25 EM)
```
