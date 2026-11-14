# Verifier B (B12b): Communication red-flag audit, Narmada Gelatines (SHAWGELTIN), run 2026-11-12

Model claude-opus-5-5. NO-CONCALL MODE (manifest `concalls_available: false`). The company holds no earnings calls, so this audit reads the company's written voice instead of transcripts. Units: AR and results in Rs lakh, CARE in Rs crore.

## 0. Scope and sources

Read fresh, before opening any comparison:
- AR FY2025-26 OCR text (`inputs/annual-report/NGL-Annual-Report-FY2025-26.txt`): Board's Report PDF pp.5-10, MD&A pp.11-12, Annexures pp.13-21, CG Report risk and communication sections (pp.32, ~p.36), Notes 4, 6, 10, 18, 28, 35, 37, 39, 43, 48 (pp.61-79).
- Results: Q1 FY27 (PDF p.2 table image), Q4 FY26 audited (text plus PDF p.4 table image), Q3 FY26 (text; table read from the Q4 FY26 comparative column). None carries management commentary.
- CARE press release 06-Mar-2026 (`inputs/rating/`).
- All 14 announcement files. The AGM outcome, scrutinizer report and AGM notice were read in the relevant parts.
- Peer transcripts: NATCAPSUQ Q4 FY25, Q2 FY26, Q4 FY26, read at every gelatine passage and at each page B06 cites.

One out-of-list raw source: `inputs/other/CARE-Narmada-Gelatines-2025-04-14.txt` (CARE, 08-Apr-2025). No second-period management text exists otherwise, because the FY2024-25 AR in `other/` has no OCR text (manifest collector_warnings). Items that rest on it carry the tag [OUT-OF-LIST]. It is a corpus document, not maker reasoning, so it does not break verifier independence.

Not read: the B03 report, other verifier outputs, screener tables.

## 1. Independent red-flag list (from the sources alone)

The rubric's classes need analogues here. Dodged question becomes silence on a known item. Guidance walkback becomes a plan reset. Contradiction between analysts becomes contradiction between audiences (rater, MD&A, audited notes).

| # | Item | Class | Anchor | Severity |
|---|---|---|---|---|
| M1 | The MD&A reverses the direction of the largest cost line. It says "Material consumed in fiscal 2025-26 increased by 1.29%, which is due to Lower cost of Raw material". Note 28 shows 11,259.84 against 11,407.13, a fall of 1.29%. In the same AR, EBITDA Rs 40.88 Cr carries two growth rates: +55.81% (Board's Report) and +59.58% (MD&A). Other expenses are printed at 8.94% of revenue against 1,646/21,541 = 7.64%. Employee cost is printed at 9.26% against 2,008/21,541 = 9.32%. | Narrative misstatement | AR p.12, p.5; Note 28 p.68; Q4 FY26 results PDF p.4 (FY26 column) | MAJOR |
| M2 | The capacity plan exists only in the rater's words: Rs 33 Cr, +600 MT gelatine, +1,500 MT DCP, Rs 25 Cr term loan, commercial production Jan-2027. The AR "Outlook" heading holds no company number. The Board's Report says "no material changes and commitments". The Q3 FY26, Q4 FY26 and Q1 FY27 results and the AGM record carry no capex word. At the AGM the MD briefed members on "achievements during the year 2025-26" only. The long-term facility was enhanced from 16.40 to 31.35 Cr, and the company's cover letter states the enhancement without its purpose. | Silence on a known item | CARE 2026 p.2; AR p.10, p.11; results files; agm-outcome p.3; announcements/20260306 p.1 | MAJOR |
| M3 | Raw-material import: the three audiences hear three versions. CARE (06-Mar-2026) says NGL "has started importing some part of its raw material requirement". The MD&A (25-May-2026) says the opportunity "is being utilized to import/purchase raw material, which will help import raw material at Competitive price", in future tense. The audited record shows no import. Annexure III foreign-exchange outgo lists spare parts 31.88 lakh, travel 3.34 and subscriptions 7.87, with no raw-material line. Note 43 says NGL "sources its major raw material requirement from domestic suppliers" and "is not exposed to foreign currency risk at the respective reporting dates". | Contradiction across audiences | CARE 2026 p.2; AR p.11, p.19; Note 43 p.77 | MAJOR |
| M4 | The company gives four different causes for the margin gain, with no metric for any of them. Note 48 credits ROE +44.74% and net margin +45.67% only to "Better Yield, Optimum Capacity Utilization of plant". The MD&A credits PBT growth to "better yield and lower consumption of power and fuel", and the cost lines to raw-material price and coal. Annexure III claims "Improvement in product mix giving better realization", but gelatine ASP fell 5.20%. CARE credits process steps, solar, coal and DCP price. The words "yield" and "utilization" appear only at p.12 and p.79, and neither page gives a number. | Unsupported self-credit | Note 48 p.79; AR p.12, p.19; CARE 2026 p.1 | MAJOR |
| M5 | [OUT-OF-LIST] The capex plan was reset with no company statement. CARE 08-Apr-2025 shows Rs 33.30 Cr over two years (FY25 16.64, FY26 16.66), including the 2.15 MW solar plant, with an Rs 18 Cr term loan (FY25 9.75, FY26 8.25). CARE 06-Mar-2026 shows Rs 33.00 Cr over two years, excluding solar, with an Rs 25 Cr term loan and commercial production from Jan-2027. Solar cost Rs 8.89 Cr (AR p.19), so the non-solar scope moved from about Rs 24.41 Cr to Rs 33.00 Cr (+35%) [COMPUTED]. Its date moved from FY25-FY26 to Jan-2027. The term loan fell from 798.08 to 728.65 lakh. With 195.00 scheduled for repayment, that implies an FY26 draw of about 125.57 lakh against Rs 8.25 Cr planned [COMPUTED]. AR Note 4 says "There is no cost overrun / time delay in the project." | Plan reset (walkback) | other/CARE-2025 p.2; CARE 2026 p.2; AR p.19, Note 4 p.61, Note 18 p.65 | MAJOR |
| m1 | Promoter-group channels are absent from the MD&A. NGL bought raw material worth 1,481.92 lakh from promoter Pioneer Jellice (FY25 1,524.64; GST-inclusive, about 13% of materials consumed). FY26 adds technical consultancy 24.00 and lease rent 11.60. Note 37 labels Pioneer Jellice "Associate Co." under "Enterprise where the control exists", although it is the promoter holding 40.06%. NGL carries IGCL at 4,115.31 against attributable net worth 2,737.02. | Omission | Note 37 p.72-73; share note p.64; AOC-1 p.21 | MINOR |
| m2 | The buyer peer says "gelatin manufacturers are also consolidating... One of the larger companies has acquired two other companies". [INFERENCE] This fits NGL's own promoter group: PJG took 75% of NGL in Jun-2023 and, with NGL, about 53% of IGCL in Dec-2024. The buyer adds that it does not "foresee much challenge" because it imports 18-20% duty free. | Peer statement bearing on the company | NATCAPSUQ Q2 FY26 p.11; CARE 2026 p.1 | MINOR |
| m3 | The MD is 79. He was re-appointed for 2 years only (to 31-May-2028) and is "overall in-charge of the Company embracing the whole gamut of operations". No successor is named. The Vice Chairman is 77 and one independent director is 75. | Volunteered fact (key person) | Q4 FY26 filing PDF p.17; AR p.7 | MINOR |
| m4 | The AGM held a members' question session: "The Managing Director/CFO appropriately responded to the queries raised by them". The content is not recorded. The meeting was video-recorded and webcast on CDSL. | Unrecorded Q&A | agm-outcome p.3, p.6 | MINOR |
| m5 | The MD's bonus keys to an undefined "Operating EBITDA": Rs 5 lakh at Rs 25 Cr, plus 1% of the excess. The FY26 level is about Rs 41-42 Cr, so the threshold is already cleared. The AR prints FY26 EBITDA on an inconsistent basis (see M1). | Incentive on undefined metric | AGM notice PDF p.14 | MINOR |
| m6 | The Board's Report says key business risks and mitigation plans "are set out in the Corporate Governance Report". The CG Report gives only the committee's scope and names no risk. The committee met once (20-Mar-2026). | Hollow cross-reference | AR p.6 vs p.32 | MINOR |
| m7 | Note 48 prints the Debt-Equity change (0.11 to 0.06) and the DSCR change (3.33 to 7.71) both as "100%" variance. Neither gives the reason the format requires above 25%. | Reporting accuracy | Note 48 p.79 | MINOR |
| m8 | The AR calls receivable concentration "low" because the customer base is "widely spread". CARE puts the top 10 customers at about 42% of FY25 sales. | Contradiction across audiences | Note 43 p.76; CARE 2026 p.2 | MINOR |
| m9 | The AR calls plant-based substitutes "one of the primary market barriers". The buyer peer puts HPMC at 5% of its volume and says pharma "out of compulsion" stays on gelatine, which grows 4-6%. | Peer statement versus company | AR p.11; NATCAPSUQ Q2 FY26 p.10, p.20-21 | MINOR |
| m10 | [OUT-OF-LIST] In Apr-2025 CARE forecast the FY26 bone-price fall from reduced European bone-gelatine output, "with manufacturers likely to import raw materials". It also changed the group-synergy wording: "higher bargaining power for raw material procurement" (2025) became "enhanced technical expertise, improved access to export markets" (2026). | Cross-period rater tone | other/CARE-2025 p.1, p.2; CARE 2026 p.1 | MINOR |

Non-flags checked and set aside:
- Q1 FY27 revenue fell 8.6% from Q4 FY26 (5,637 vs 6,170). Q1 FY26 fell 8.0% from Q4 FY25 (4,577 vs 4,977), so the dip is a seasonal pattern.
- The scrutinizer report shows no dissent on any of the five AGM resolutions.
- The 5.20% gelatine price fall is stated plainly. That is an honest admission, not a flag.

## 2. Comparison against B05 and B06

| # | Status | Where the pipeline has it | Note |
|---|---|---|---|
| M1 | CAUGHT | B05 2A contradiction table; 4D row 1; FLAG-AR-MISSTATEMENT | All four lines found. B05 grades it "Medium", which matches MAJOR. |
| M2 | CAUGHT | B05 1B, 1C, 2D; 4D row 2; FLAG-NO-FORWARD-GUIDANCE | The core is right. One clause is overstated (Section 3). |
| M3 | PARTIALLY CAUGHT | B05 2A row 3 ("import is unverified", Partial) | The CARE-versus-AR contradiction is not flagged. Note 43's domestic-sourcing and nil-FX lines are not cited. The item is not on the red-flag list. B06's analyst note still carries "cheaper imported bone" as a live NGL-specific reading. Under-weighted. |
| M4 | CAUGHT | B05 2B (self-credit); 4D row 3; red_flags[2] | The Annexure III "product mix" claim is not cited. The core is found. |
| M5 | MISSED | B05 1C says "Timeline slippage: none can be seen"; the block has `timeline_slippages: []` | The corpus contradicts both. The cause is input scope: the 2025 release sits in `other/`, outside stage 5's bounded dispatch. |
| m1 | PARTIALLY CAUGHT | B05 2D ("Pioneer Jellice pricing"), 3A (IGCL) | The raw-material channel and the "Associate Co." label are not named. |
| m2 | PARTIALLY CAUGHT | B06 Q5 and risks_peers_raise[0] | B06 records the consolidation but leaves the consolidator unnamed. |
| m3 | MISSED | none | Belongs to B08. Routed. |
| m4 | MISSED | B05 2E says "No analyst questions exist" | Questions exist. Their content is the gap. |
| m5 | MISSED | none | Belongs to B08. Routed. |
| m6 | MISSED | none | Same pattern as M1. |
| m7 | MISSED | none | Same pattern as M1. |
| m8 | CAUGHT | B05 2D | |
| m9 | CAUGHT | B06 Q4 | |
| m10 | MISSED | none | Out-of-list source. |

Tally: 15 listed; 5 caught, 3 partially caught, 7 missed.

## 3. Pipeline flags tested against the sources

| Pipeline flag | Verdict | Evidence |
|---|---|---|
| B05: MD&A reverses materials direction | SUPPORTED | AR p.12 vs Note 28 p.68 |
| B05: no company outlook; capex only in CARE, "silent in AR, results and announcements"; block: "no AR or Reg 30 disclosure" | SUPPORTED in core, OVERSTATED in one clause | On 06-Mar-2026 the company filed the CARE press release under Reg 30, capex paragraph included (`announcements/20260306-credit-rating.txt` p.1 cover letter, p.2-3 press release). B05 lists "credit rating" among the 14 files, then says none names the capex. The silence in the company's own words stands. |
| B05: yield and utilisation claimed with no metric | SUPPORTED | AR p.12, Note 48 p.79 |
| B05: EBITDA 40.88 vs 42.08 Cr | SUPPORTED | 3,819 + 102 + 287 = 4,208 (Q4 FY26 PDF p.4). FY25 2,279 + 122 + 222 = 2,623 matches the AR's own 26.23, so the FY26 figure breaks the AR's own method. |
| B05: other expenses 8.94% vs 7.64% | SUPPORTED | 1,646 / 21,541 |
| B05: no calls, no presentation | SUPPORTED | CG Report "Means of Communication" names results, newspapers and the website only |
| B06 FLAG-SINGLE-PEER | SUPPORTED | Only NATCAPSUQ transcripts in `peer-concalls/` |
| B06 FLAG-GELATINE-DEFLATION-INDUSTRYWIDE-BUYER-SIDE | SUPPORTED | Q2 FY26 p.11: "FY'25, we saw gelatin prices drop by around 4%. Current six months also... at least about 4% to 5%" |
| B06 FLAG-PEER-INCONSISTENCY (HPMC 10% vs about 5%) | SUPPORTED, low weight | Q2 FY26 p.10; Q4 FY26 p.10 (163 + 8 Cr). The US tariff stoppage after July 2025 explains it (Q4 FY26 p.20-21). |
| B06 page anchors spot-checked: Q4 FY26 p.4, p.6, p.10, p.11, p.17 (errata), p.18, p.20, p.21; Q2 FY26 p.10, p.11, p.20-21 | All found at the cited page | |

No pipeline flag is NOT SUPPORTED. The analyses invented no signal.

## 4. Promise-delivery spot checks

| B05 row | Earlier statement present? | Later outcome as stated? | Result |
|---|---|---|---|
| 1. Solar commissioned, power and fuel down | Yes. AR p.19: "The solar plant within the Factory premises commissioned", Rs 8.89 Cr. CARE 2025 p.2 had planned it [OUT-OF-LIST]. | Yes. Power and fuel 2,333 vs 2,456, -5.0%; ratio 10.83% vs 13.00% (Q4 FY26 PDF p.4). Q1 FY27 672/5,637 = 11.9% vs Q1 FY26 583/4,577 = 12.7% (Q1 FY27 PDF p.2). | CONFIRMED |
| 3. Raw material imported or bought at competitive price | Yes. AR p.11. | The purchase half holds: materials 11,259.84 vs 11,407.13 on volume +16.17%; raw-material stock 1,265.65 vs 856.24 (Note 10 p.62); Q1 FY27 materials ratio (2,720 + 131)/5,637 = 50.6%. The import half shows no FY26 trace (M3). | CONFIRMED (Partial is the right label; the weight is low, see M3) |
| 4. CARE PBILDT 18-20% near term | Yes. CARE 2026 p.1. | FY26 4,130/21,541 = 19.2%; Q3 FY26 1,067/5,673 = 18.8%; Q4 FY26 1,376/6,170 = 22.3%; Q1 FY27 1,172/5,637 = 20.8% (results tables). | CONFIRMED |
| 5. CARE FY26 TOI growth over 15% | Yes. CARE 2026 p.2. | Revenue +14.02% (AR p.5, p.12). | CONFIRMED (near miss) |
| 7. Capex Rs 33 Cr, Jan-2027, Pending | Yes. CARE 2026 p.2. | CWIP 528.97 (Note 4 p.61) and commitments 1,194.06 (Note 35 p.72) hold. The Q1 FY27 filing is P&L only (PDF p.2). | CONFIRMED for direction. The "52% of Rs 33 Cr" reading as project progress is not supported: the same sum was 1,933.03 at Mar-2025 (678.29 + 1,254.74), before the plan was restated. |

5 checked, 5 confirmed, 0 wrong.

## 5. Credibility grade

I concur with C. Management owns no forward number to test. The AR misstates four cost lines (M1). The 2025-to-2026 CARE record shows a capex reset the company never acknowledged (M5), so nothing supports B. The solar and fuel saving is delivered and visible in the quarterly cost lines, so nothing forces a lower grade.

The capex should stay a rater-relayed plan until the company says something on its own. The first company-side evidence would be a Reg 30 commissioning notice, or Note 4 CWIP ageing with a named project.

## 6. Consolidated findings

| Sev | Location | Pipeline says | Source shows | Note |
|---|---|---|---|---|
| MAJOR | B05 1C, `timeline_slippages`, 2A row 7 | No slippage; the plan first appears in CARE Mar-2026 | CARE Apr-2025 p.2 vs CARE Mar-2026 p.2; AR p.19, p.61, p.65 (M5) | MISSED. A routing gap, not a reading error. Carry to Halt 1 open items. |
| MAJOR | B05 2A row 3; B06 analyst_note reading (b) | Import "unverified"; imported bone kept as a live NGL-specific reading | CARE p.2 vs AR p.11, p.19, Note 43 p.77 (M3) | PARTIALLY CAUGHT. Two readings: imports began after 31-Mar-2026, or they run through an intermediary such as Pioneer Jellice [INFERENCE]. Separating observation: a raw-material line in the FY27 foreign-exchange outgo, or a rise in Note 37 purchases. |
| MINOR | B05 red_flags[1], input_gaps[3] | "no AR or Reg 30 disclosure" | announcements/20260306-credit-rating.txt p.1-3 | OVERSTATED clause |
| MINOR | B05 2A row 7 | 52% of Rs 33 Cr | 1,933.03 at Mar-2025 vs 1,723.03 at Mar-2026 | Not a progress measure |
| MINOR | B05 (absent) | n/a | MD aged 79, 2-year term (m3) | MISSED; route to B08 |
| MINOR | B05 2E | No questions exist | AGM Q&A held, content unrecorded (m4) | MISSED; request the recording |
| MINOR | B05 (absent) | n/a | MD bonus on undefined Operating EBITDA (m5) | MISSED; route to B08 |
| MINOR | B05 4C | Four contradictions | Hollow risk cross-reference (m6) | MISSED |
| MINOR | B05 4C | Four contradictions | Note 48 variance errors (m7) | MISSED |
| MINOR | B05 2D, 3A | "Pioneer Jellice pricing" | Note 37 raw-material channel, "Associate Co." label, IGCL premium (m1) | PARTIALLY CAUGHT; route to B08 and B03 |
| MINOR | B06 Q5 | Consolidator unnamed | PJG fits [INFERENCE] (m2) | PARTIALLY CAUGHT |
| MINOR | B05 3B; B06 | n/a | CARE 2025 cyclical forecast and synergy wording (m10) | MISSED, out-of-list |

CRITICAL 0, MAJOR 2, MINOR 10. The rule for CRITICAL is a missed evasion repeated over 2 or more quarters. The capex silence repeats across five filings, but B05 caught it, so it does not qualify.

## 7. Scoring

The material items are M1 to M5: 5, all MAJOR. M1, M2 and M4 were caught. M3 was partially caught and counts as caught, since the pipeline had it but under-weighted it. M5 was missed. Acceptance is 4 of 5 = 80%.

On named sources alone, 4 of 4 = 100%. The strict count, with no credit for the partial, is 3 of 5 = 60%. That is not below the 60% REWORK line. No reading of the arithmetic triggers REWORK.

## 8. Routing for the orchestrator (Halt 1 open items)

1. Feed the Apr-2025 CARE release to the B05 capex row and to Stage 7's F2 capex-completion test. M5 changes "no slippage" to "one silent reset".
2. Ask the operator for the AGM 19-Aug-2026 webcast. It is the only recorded forum where members questioned the MD.
3. Route m1, m3 and m5 to B08 (governance): promoter raw-material channel, MD succession, MD bonus metric.
4. Mark B06 reading (b), "cheaper imported bone", with this condition: FY26 shows no import footprint (M3).

No stuck-rule trigger. Q2 FY27 results (board meeting 12-Nov-2026) are not in the corpus.

```yaml
stage: B12b
company: "SHAWGELTIN"
run_date: "2026-11-12"
model: "claude-opus-5-5"  # must equal .claude/agents frontmatter; the orchestrator compares it
status: complete
independent_flags_found: 15
caught: 5
partially_caught: 3
missed:
  - {severity: "MAJOR", item: "Capex plan reset across CARE releases with no company statement. CARE 08-Apr-2025: Rs 33.30 Cr over two years (FY25 Rs 16.64 Cr, FY26 Rs 16.66 Cr) including the 2.15 MW solar plant, term loan Rs 18 Cr (FY25 9.75, FY26 8.25). CARE 06-Mar-2026: Rs 33.00 Cr over two years excluding solar, term loan Rs 25 Cr, commercial production from Jan-2027. Solar cost Rs 8.89 Cr, so the non-solar scope moved from about Rs 24.41 Cr to Rs 33.00 Cr [COMPUTED] and from FY25-FY26 to Jan-2027. Term loan fell 798.08 to 728.65 lakh, implied FY26 draw about 125.57 lakh against Rs 8.25 Cr planned [COMPUTED]. AR Note 4 says no cost overrun or time delay. Contradicts B05 1C 'Timeline slippage: none can be seen' and timeline_slippages: []. Source is in inputs/other/, outside the named input set and stage 5's bounded dispatch", anchor: "inputs/other/CARE-Narmada-Gelatines-2025-04-14.txt p.2; rating/CARE-Narmada-Gelatines-2026-03-13.txt p.2; AR PDF p.19 (solar Rs 8.89 Cr), p.61 (Note 4), p.65 (Note 18)"}
  - {severity: "MINOR", item: "MD Ashok K Kapur, aged 79, re-appointed for 2 years only (01-Jun-2026 to 31-May-2028); he is 'overall in-charge of the Company embracing the whole gamut of operations'; no successor named. Term ends inside a 3-5 year hold. Route to B08", anchor: "results/20260525-Q4FY26-audited-results PDF p.17 (Annexure D); AR PDF p.7"}
  - {severity: "MINOR", item: "AGM 19-Aug-2026 held a members' question session ('The Managing Director/CFO appropriately responded to the queries raised by them'); question content is not recorded; proceedings were video-recorded and webcast on CDSL. B05 2E says no questions exist. The recording is a candidate source for the capex question", anchor: "announcements/20260819-agm-outcome.txt p.3, p.6"}
  - {severity: "MINOR", item: "MD performance bonus keys to an undefined 'Operating EBITDA': Rs 5 lakh at Rs 25 Cr plus 1% of the excess. The threshold sits below the FY26 level, and the AR prints FY26 EBITDA 40.88 Cr on a basis that matches neither 42.08 Cr (incl. other income) nor 41.30 Cr (excl.). Route to B08", anchor: "announcements/20260721-agm65-notice.txt PDF p.14; AR PDF p.5, p.12; results Q4 FY26 PDF p.4"}
  - {severity: "MINOR", item: "Board's Report says key business risks and mitigation plans are set out in the CG Report; the CG Report gives only the Risk Management Committee's scope and names no risk", anchor: "AR PDF p.6 vs p.32"}
  - {severity: "MINOR", item: "Note 48 ratio table: Debt-Equity 0.11 to 0.06 and DSCR 3.33 to 7.71 both printed as '100%' variance, no reason given for either although both exceed the 25% disclosure line. Adds to the AR accuracy pattern", anchor: "AR PDF p.79 (Note 48)"}
  - {severity: "MINOR", item: "CARE 08-Apr-2025 forecast the FY26 bone-price fall from reduced European bone-gelatine output, 'with manufacturers likely to import raw materials' (supports the cyclical reading of the margin reset). Group-synergy wording moved from 'higher bargaining power for raw material procurement' (2025) to 'enhanced technical expertise, improved access to export markets' (2026). Out-of-list source", anchor: "inputs/other/CARE-Narmada-Gelatines-2025-04-14.txt p.1, p.2; rating/CARE-Narmada-Gelatines-2026-03-13.txt p.1"}
pipeline_flags_not_supported: []
promise_delivery_spot_checks: {checked: 5, confirmed: 5, wrong: 0}
credibility_grade_concur: "concur: C. Management owns no forward number to test, the AR narrative misstates four cost lines, and the 2025-to-2026 CARE record shows a capex reset the company never acknowledged, so nothing supports B; the solar and fuel delivery is real, so nothing forces a lower grade"
findings:
  - {severity: "MAJOR", location: "B05 1C, B05 block timeline_slippages, B05 2A row 7", claimed: "Timeline slippage: none can be seen; the capex plan first appears in CARE 06-Mar-2026", source_truth: "CARE 08-Apr-2025 p.2: Rs 33.30 Cr over FY25-FY26 incl. 2.15 MW solar, term loan Rs 18 Cr. CARE 06-Mar-2026 p.2: Rs 33.00 Cr excl. solar, term loan Rs 25 Cr, commercial production Jan-2027. Solar Rs 8.89 Cr (AR p.19). Term loan 798.08 to 728.65 lakh (Note 18, AR p.65)", note: "MISSED. Non-solar scope about Rs 24.41 Cr became Rs 33.00 Cr [COMPUTED] and the date moved to Jan-2027 with no company statement; AR Note 4 (p.61) says no time delay. Source sits in inputs/other/, outside stage 5's dispatch: a routing gap, not a reading error. Carry to Halt 1 open items"}
  - {severity: "MAJOR", location: "B05 2A row 3 and 4D (not listed); B06 analyst_note reading (b)", claimed: "Raw-material import 'unverified', outcome Partial; B06 keeps 'cheaper imported bone' as a live NGL-specific structure reading", source_truth: "CARE 06-Mar-2026 p.2: NGL 'has started importing some part of its raw material requirement'. AR p.11: the import opportunity 'is being utilized ... will help import raw material at Competitive price'. AR p.19: foreign-exchange outgo shows spare parts 31.88 lakh, no raw material. AR Note 43 p.77: major raw material sourced from domestic suppliers; no foreign currency exposure at the reporting dates", note: "PARTIALLY CAUGHT. The cross-audience contradiction is not flagged. The FY26 audited record shows no NGL raw-material import, so the FY26 cost relief cannot rest on imported bone. Two readings: imports began after 31-Mar-2026, or imports run through an intermediary such as promoter Pioneer Jellice (raw-material purchases 1,481.92 lakh, Note 37 p.73) [INFERENCE]. Separating observation: a raw-material line in FY27 AR foreign-exchange outgo, or a rise in Note 37 purchases"}
  - {severity: "MINOR", location: "B05 block red_flags[1], input_gaps[3], 4D row 2", claimed: "Rs 33 Cr capex announced by CARE only, with no AR or Reg 30 disclosure; no Reg 30 announcement names the capex", source_truth: "announcements/20260306-credit-rating.txt p.1 (company Reg 30 cover letter, long-term facility enhanced 16.40 to 31.35 Cr) and p.2-3 (CARE press release with the capex paragraph, filed by the company)", note: "OVERSTATED clause. The company put the rater's capex text on BSE itself. The core flag stands: the AR, all three results filings and the AGM record carry no capex word"}
  - {severity: "MINOR", location: "B05 2A row 7, 4A trigger 1", claimed: "CWIP 528.97 + commitments 1,194.06 = 1,723.03 lakh = 52% of Rs 33 Cr", source_truth: "Mar-2025: CWIP 678.29 + commitments 1,254.74 = 1,933.03 lakh (Note 4 AR p.61, Note 35 AR p.72), before the Mar-2026 plan", note: "Arithmetic correct; reading it as project progress is not supported, since the sum fell in the year the plan was restated. The 'Pending' direction stands"}
  - {severity: "MINOR", location: "B05 (absent); route B08", claimed: "not mentioned", source_truth: "MD aged 79, 2-year term to 31-May-2028, overall in charge of all operations (Q4 FY26 filing PDF p.17; AR p.7)", note: "MISSED. Key-person term ends inside the hold horizon; no successor named"}
  - {severity: "MINOR", location: "B05 2E", claimed: "No analyst questions exist because the company holds no calls", source_truth: "AGM 19-Aug-2026: members were invited to ask questions and the MD/CFO responded; content unrecorded; proceedings video-recorded and webcast on CDSL (announcements/20260819-agm-outcome.txt p.3, p.6)", note: "MISSED. Questions exist; their content is a corpus gap, and the recording is a source to request at Halt 1"}
  - {severity: "MINOR", location: "B05 (absent); route B08", claimed: "not mentioned", source_truth: "MD bonus Rs 5 lakh at annual 'Operating EBITDA' of Rs 25 Cr plus 1% above it (AGM notice PDF p.14); AR prints FY26 EBITDA 40.88 Cr (p.5, p.12) vs 42.08 Cr computed incl. other income", note: "MISSED. Undefined metric; threshold below the FY26 level"}
  - {severity: "MINOR", location: "B05 4C reporting accuracy", claimed: "four AR-versus-note contradictions", source_truth: "Board's Report p.6 points to the CG Report for key risks; CG Report p.32 names none", note: "MISSED. A fifth instance of the same pattern; the B05 read 'Weak' stands"}
  - {severity: "MINOR", location: "B05 4C reporting accuracy", claimed: "four AR-versus-note contradictions", source_truth: "Note 48 p.79: Debt-Equity 0.11 to 0.06 and DSCR 3.33 to 7.71 printed '100%' variance, no reason given", note: "MISSED. A sixth instance of the same pattern"}
  - {severity: "MINOR", location: "B05 2D, 3A", claimed: "'Pioneer Jellice pricing' listed as unsaid; IGCL named as a related player", source_truth: "Note 37 AR p.72-73: raw-material purchases from Pioneer Jellice 1,481.92 lakh (FY25 1,524.64), new technical consultancy 24.00 and lease rent 11.60; Pioneer Jellice labelled 'Associate Co.'. AOC-1 AR p.21: IGCL carrying 4,115.31 vs attributable net worth 2,737.02", note: "PARTIALLY CAUGHT. The MD&A is silent on the group's role in procurement. The channel was flat year on year, so it cannot explain the 511 bp; route to B08 and B03"}
  - {severity: "MINOR", location: "B06 Q5, risks_peers_raise[0]", claimed: "one larger gelatine company acquired two others (unnamed)", source_truth: "NATCAPSUQ Q2 FY26 p.11; CARE 2026 p.1: PJG took 75% of NGL (Jun-2023) and with NGL about 53% of IGCL (Dec-2024)", note: "PARTIALLY CAUGHT. [INFERENCE] the consolidator the buyer describes fits NGL's own promoter group. The buyer says its 18-20% duty-free import access neutralises the consolidation, which bears on any pricing-power claim"}
  - {severity: "MINOR", location: "B05 3B; B06 analyst_note", claimed: "not mentioned", source_truth: "CARE 08-Apr-2025 p.2: bone prices 'expected to decrease in FY26' on reduced European bone-based gelatine output, 'with manufacturers likely to import raw materials'; p.1 synergy 'higher bargaining power for raw material procurement' vs CARE 2026 p.1 'technical expertise, export access, best practices'", note: "MISSED, out-of-list source. Supports cyclical reading (a) of load-bearing fact 1; it is not the separating observation"}
critical_count: 0
major_count: 2
minor_count: 10
material_found: 5
material_caught: 4
acceptance_rate: 80             # material_caught / material_found, %; PARTIALLY CAUGHT counted as caught
coverage_basis: "5 material (all MAJOR, 0 CRITICAL) of 15 listed; 3 caught, 1 partially caught (counted: the pipeline had it, under-weighted), 1 missed. The missed item rests on inputs/other/CARE-Narmada-Gelatines-2025-04-14.txt, outside the named input set and stage 5's bounded dispatch; on named sources alone, 4 material, 4 caught (100%). Strict count with partial not credited: 3 of 5 = 60%, not below the 60% REWORK line. Promise-delivery rows 1, 3, 4, 5, 7 checked against the results tables and AR notes"
```
