# FORENSICS | AEQUS | q2fy27 | doctype presentation (file label `pressrelease`: press release with Reg 30 cover letter) | Rs Mn (x0.1 to Rs Cr)

Inputs read: extracted/aequs-pressrelease-q2fy27-structured.md (R001-R171), extracted/aequs-pressrelease-q2fy27-fulltext.md (245 lines), work/ledger_pressrelease_aequs_q2fy27.md, work/monitoring-checklist.md. Prior-quarter fulltext: none available. Source PDF and inputs/ not opened.
Model: claude-opus-5-5.

## 0. LEDGER RECONCILIATION
- Ledger accounts for 171 of 171 structured IDs (orphans: none). Every row was read at its cited fulltext line. Reconciled: 171/171 = 100%.
- All 171 values match the fulltext verbatim. A1 line anchors drift by 1-2 lines on 11 rows; the value sits on the adjacent line. No value is wrong. Drift: R004/R005 (cited 32, value on 33), R014 (cited 18, "For Aequs Limited" on 40), R015 (cited 59, on 57), R018 (cited 48, on 49), R076 (cited 102, on 101), R104 (cited 119, "₹401 Mn" on 118), R120 (cited 132, "grew 9% QoQ" on 131), R154 (cited 185, "₹6,500 Mn" on 184), R170/R171 (cited 239, on 241). Findings below cite the true fulltext line.
- A1 garble note R071 (Q1 FY27 PAT cells "( 5 32)" / "( 1 3) %", line 90/92) is consistent with H1 arithmetic: 522 + 532 = 1,054 (R059).
- Arithmetic tie-outs that hold: revenue 4,091 + 3,955 = 8,046; EBITDA 245 + 215 = 460; segment revenue 3,514 + 577 = 4,091 (Q2) and 6,736 + 1,310 = 8,046 (H1); YoY/QoQ % on revenue, EBITDA, PAT all recompute within rounding; JV-inclusive QoQ (4%, 8%) recompute from H1 less Q2.

## 1. FINDINGS TABLE
Derived figures show the formula. Prior-year bases implied from stated growth rates carry a rounding range.

| id | check | ledger row ref | line | short verbatim quote | classification | forward implication |
|---|---|---|---|---|---|---|
| A3-01 | F17 | R104, R105, R106 | 118-119 | "EBITDA loss widened to ₹401 Mn in Q2 from ₹361 Mn in Q1" | CONFIRMATORY-NEGATIVE | Falsification line leg 1 FIRED: Q2 consumer EBITDA loss Rs 40.1 cr is wider than the Rs 36.1 cr threshold. Leg 2 (consumer utilisation at or below 23%) is NOT DISCLOSED in this document. Thesis-broken test is half-met; A4 must get Q2 utilisation before the test resolves. |
| A3-02 | F16 | R100, R101, R102, R103, R146 | 114, 118, 169 | "Consumer revenue increased 52% YoY to ₹577 Mn in Q2 and 107% YoY to ₹1,310 Mn in H1" | FORWARD-SIGNAL | Derived Q1 FY27 consumer revenue = 1,310 - 577 = 733 Mn. Q2 consumer revenue FELL 21% QoQ (733 to 577). The release gives only YoY; the chairman's "more than doubling" (line 169) rests on Q1. Q1 YoY growth was about +190% (Q1 FY26 implied 1,310/2.07 - 577/1.52 = 633 - 380 = 253); Q2 decelerated to +52%. Consumer EBITDA margin moved from -49% (Q1) to -70% (Q2). Company capacity rose to 4.93m hours (line 151) while consumer revenue fell, so consumer utilisation likely fell below the 22% Q1 level [INFERENCE]. |
| A3-03 | F16 | R151, R152 | 179-181 | "we are recalibrating the path to Consumer EBITDA breakeven" | FORWARD-SIGNAL | Guidance softened. The Notion checklist carries a Q4 FY27 consumer EBITDA breakeven and an H1 FY28 group PAT breakeven gated on 40-50% FY27 exit utilisation. The release gives no new date and does not restate the utilisation target. Treat both dates as withdrawn until management restates them. |
| A3-04 | F7 | R138, R150 | 154-155, 178 | "We view this as a timing-related shift rather than a change in the underlying opportunity" | FORWARD-SIGNAL | Pre-emptive framing. It names two causes, "extended qualification timelines and supply chain constraints" (line 154-155). A supply-chain cause is outside customer qualification and can recur. Lexicon hits ("subject to" line 223, "assurance" line 228) are safe-harbor boilerplate only. |
| A3-05 | F16 | R088-R096, R145 | 109-111, 175 | "EBITDA increased 24% YoY to ₹783 Mn" | FORWARD-SIGNAL | Aerospace EBITDA grew 24% against revenue +44%. Derived Q2 margin 783/3,514 = 22.3%; Q2 FY26 implied (783/1.24)/(3,514/1.44) = 25.9% (range 25.7-26.1%); compression about 360 bps YoY (340-380). Q1 FY27 derived 731/3,222 = 22.7%, so margin also slipped 40 bps QoQ. H1 22.5% vs 24.7% implied. The release says "strong growth and profitability" (line 175) and gives no segment margin. Spear floor (above 20%) still holds; the trend runs toward it. |
| A3-06 | F16 | R038-R045, R054-R061, R114-R118, R116 | 126 | "higher depreciation and finance costs largely offset the sequential EBITDA increase" | FORWARD-SIGNAL | D&A, finance cost, other income, tax and JV share are not disclosed. Derived net below-EBITDA charge (EBITDA minus PAT): Q1 FY26 359 (841-443 = 398 EBITDA; PAT -167+206 = +39), Q2 FY26 649, Q1 FY27 747, Q2 FY27 767 Mn. At the Q2 run rate, group PAT breakeven needs quarterly EBITDA of about 767 Mn, 3.1x the Q2 figure of 245. Finance costs rose QoQ after a listing whose lock-in ends about Dec-2026 (checklist), so borrowing is rising. |
| A3-07 | F10 | R131, R132, R154 | 144-145 | "₹6,500 Mn promoter-group investment through preferential warrants" | FORWARD-SIGNAL | Dilution is pending. Warrant count, issue price, upfront tranche and conversion window are NOT FOUND in this document; no share count or EPS is given. "Investment" overstates cash received if only an upfront tranche is paid. A4: cross-check terms and the promoter's funding source against the proposed pledge tripwire (facility above Rs 200 Cr). |
| A3-08 | F6 | R133, R155 | 145-147, 185 | "supports the Company's next phase of capacity expansion, strategic JV investments and working capital requirements" | FORWARD-SIGNAL | The use of proceeds differs inside the document. Line 185 says only "the next phase of expansion, including Hosur". Line 146-147 adds working capital (funding losses) and "strategic JV investments" (a new or enlarged JV entity). Ask for the split by use. |
| A3-09 | F2 | R077-R087, R038, R041 | 104-107 | "Including proportionate JV contributions, Q2 revenue reached ₹4,480 Mn" | AMBIGUOUS | No standalone figures; decomposition runs on JV-inclusive minus consolidated. Q2 FY27: revenue 389, EBITDA 86 Mn (JV margin 22.1%). Q1 FY27 (H1 less Q2): revenue 346, EBITDA 92 (26.6%). Q2 FY26 implied: revenue about 295 (284-306), EBITDA about 74 (70-78). JV EBITDA as % of reported EBITDA: about 17% (Q2 FY26), 43% (Q1 FY27), 35% (Q2 FY27). Gap widened about 18 pp YoY. The JV basis turns a reported -45% EBITDA into "down 36% YoY" (line 105-106). JV names, JV PAT share and eliminations are NOT FOUND. JV margin fell 450 bps QoQ. |
| A3-10 | F12 | R093, R095, R104-R106, R038, R041, R043 | 110, 118-119, 85 | "EBITDA increased 24% YoY to ₹783 Mn" | AMBIGUOUS | Segment EBITDA does not sum to consolidated. Q2: 783 - 401 = 382 vs 245, unallocated -137 Mn (56% of reported EBITDA). Q1: 731 - 361 = 370 vs 215, unallocated -155. H1: 751 vs 460, -291. Segment EBITDA basis (with or without other income) is not stated; monitorable 2 needs aerospace margin excluding other income. No segment assets or liabilities in the release. |
| A3-11 | F16 | R046-R053, R062-R069 | 87, 92 | "EBITDA ... 6%     16% (>100) bps  5%     100 bps" | AMBIGUOUS | Margin labels favour the issuer. EBITDA margin YoY shown "(>100) bps"; computed 5.99% vs 15.73% = -974 bps (H1 -994 bps). QoQ shown "100 bps"; computed +55 bps. PAT margin Q2 shown "(12)%"; computed on revenue -12.76%, which rounds to (13)%, equal to Q1, so the "100 bps" QoQ PAT improvement (computed +69 bps) depends on truncation. The PAT margin basis may be total income (other income NOT FOUND). |
| A3-12 | F6 | R128, R130, R155 | 142, 185 | "leveraging Belagavi and upcoming Hosur manufacturing ecosystems" | AMBIGUOUS | Hosur is "upcoming" with no commissioning date, capex budget or segment. Tracker item (Hosur commissioning date) stays open. The warrant is named as its funding. |
| A3-13 | F14 | R129, R156, R157, R119, R147 | 139, 186, 131, 170 | "Following quarter-end, new Safran agreements expanded our relationships to six entities." | AMBIGUOUS | Line 139 lists "Signed new long-term supply agreements" as a Q2 business highlight; line 186 dates them after quarter-end. It is not stated whether the USD 1,096 Mn order book (line 170) includes these post-quarter agreements. Order book definition (firm vs LTA run-rate, customers covered) is not given. Safran award value is NOT FOUND. |
| A3-14 | F13 | R140, R141 | 158 | "Reenah Joseph was appointed Chief Financial Officer" | AMBIGUOUS | No effective date, no board-approval reference, no KMP designation. Monitorable 7 needs a KMP appointment filing or a CFO certification on the results; this release supplies neither. Results approval itself is in a separate filing. |
| A3-15 | F16 | R153 | 184 | "H1 FY27 capital expenditure stood at ₹1,597 Mn" | AMBIGUOUS | H1 capex Rs 159.7 cr = 24% of the Rs 660 cr FY27 plan (spear fact 2). With Q1 capex Rs 83 cr (checklist), Q2 is about Rs 76.7 cr. No segment split. Two readings: consumer capex phased down after the utilisation miss (monitorable 3), or H2 back-loading. The segment split separates them. |
| A3-16 | F17 | (absences; no row) | n/a: see silence table below, anchored to the document's full span lines 17-245 | Silence table (Section 4) | AMBIGUOUS | 11 checklist items are absent from this release. Count is 1 quarter each; no prior release was available to extend the count. A press release omits by design, so this silence weighs less than concall silence. Utilisation, cash flow and DTA silences matter most. |
| A3-17 | F14 | R123, R124, R161 | 135-136, 199 | "5,978 SKUs, adding 238 parts" / "5,978 qualified parts" | NEUTRAL-FACT | Unit terms are mixed (SKUs, parts, qualified parts) for the same number. The 238 new parts are up from 86 in Q1 and down from 433 in Q4 FY26 (monitorable 4). This is consistent with the Safran award showing in the count. |
| A3-18 | F16 | R119, R120, R147 | 131, 170 | "Our Aerospace order book stood at USD 1,096 Mn" | NEUTRAL-FACT | 1,096 / 1,004 (spear fact 4) = +9.2%, consistent with "Order book grew 9% QoQ" (line 131). The headline "USD 1.1 billion" is the rounded figure. |

## 2. CHECKLIST SCORECARD
| check | status | basis |
|---|---|---|
| F1 | N.A. | Press release has no statutory P&L template; ledger ZERO_STANDING count 0. |
| F2 | FINDING | No standalone figures; JV-inclusive vs consolidated gap decomposed instead (A3-09). |
| F3 | N.A. | No standalone cost lines to compare. |
| F4 | N.A. | No auditor report or Other Matters paragraph in a press release. |
| F5 | N.A. | No EoM / going-concern language; no prior fulltext to diff. |
| F6 | FINDING | 10 FORWARD rows; all undated. Warrant use-of-proceeds inconsistency (A3-08), Hosur undated (A3-12). Register in Section 3. |
| F7 | FINDING | Consumer framing hedge, "timing-related shift" (A3-04). Lexicon hits are boilerplate only. |
| F8 | N.A. | No tax line, ETR or deferred tax in the release. |
| F9 | N.A. | No OCI disclosure. |
| F10 | FINDING | Rs 6,500 Mn preferential warrants, terms NOT FOUND; no share count or EPS (A3-07). |
| F11 | N.A. | No net worth, other equity or paid-up figures in the release. |
| F12 | FINDING | Segment results present; unallocated EBITDA gap -137/-155 Mn; segment basis unstated; no segment assets (A3-10). |
| F13 | FINDING | CFO appointment with no effective date or board reference (A3-14). |
| F14 | FINDING | Safran agreement timing inconsistency (A3-13); SKU/parts terminology (A3-17). |
| F15 | N.A. | No consolidation list; no prior quarter to diff. JV names not given (see A3-09). |
| F16 | FINDING | Consumer QoQ fall omitted (A3-02), breakeven recalibrated (A3-03), aero margin compression undisclosed (A3-05), below-EBITDA lines dropped (A3-06), margin labels (A3-11), capex vs plan (A3-15), order book reconcile (A3-18). No prior deck to diff for dropped slides. |
| F17 | FINDING | Checklist supplied by orchestrator; silence audit run against the release. Falsification leg 1 fired (A3-01); 11 items silent (A3-16). |

Counts: PASS 0 | FINDING 9 | N.A. 8 | blank 0.

## 3. COMMITMENT REGISTER (F6)
| commitment | implied date | ref | status word |
|---|---|---|---|
| Consumer EBITDA breakeven path | none (prior Notion target Q4 FY27 no longer stated) | line 179-180, R151 | recalibrating (regressed from a dated target) |
| Consumer: complete remaining milestones, reach sustained production volumes | none | line 155-156, R139 | underway |
| Near-term focus: improve utilisation, convert installed capacity to profitable growth | "near-term", undated | line 180-181, R152 | underway |
| Rs 6,500 Mn warrant proceeds to capacity expansion, strategic JV investments, working capital | none (EGM 22-Oct per checklist, not in release) | line 144-147, 184-185; R131, R133, R155 | initiated |
| Hosur manufacturing ecosystem | none ("upcoming") | line 142, 185; R130 | initiated |
| New long-term Safran supply agreements, six entities | signed after 30-Sep-2026 | line 139-142, 186; R129, R156 | completed |
| Safran A320 wheels serial-production contract, tenure above 15 years | signed; deliveries FY28 per spear fact 4 (not restated) | line 131-133, 171-172; R121, R122 | completed |
| Aerospace: broaden manufacturing scope, deepen customer relationships | none | line 111-112, R097 | underway |
| Disciplined execution and stronger returns | none | line 187-188, R158 | intent only |
| CFO appointment (Reenah Joseph) | effective date NOT FOUND | line 158, R140 | completed |

## 4. SILENCE AUDIT (F17: checklist items NOT addressed in this release)
| checklist item | addressed? | consecutive quarters silent | note |
|---|---|---|---|
| Monitorable 1: consumer utilisation (31%, 23%, 22%; 40-50% FY27 exit target) | NO | 1 (prior not testable) | Leg 2 of the falsification line depends on it. Revenue fell 21% QoQ (A3-02). |
| Monitorable 2: aerospace margin ex other income at or above 20% | PARTIAL | 1 | Segment EBITDA 783/3,514 = 22.3% derived; other-income basis unstated (A3-10). |
| Monitorable 3: consumer capex phase-down | NO | 1 | H1 capex given without segment split (A3-15). |
| Monitorable 4: new aerospace part numbers | YES | 0 | 238 in Q2 (line 136). |
| Monitorable 5: operating cash vs capex (FLAG-CASH INDETERMINATE) | NO | 1 | No cash flow in the release; check the H1 cash flow statement filed with the results. Warrant names "working capital requirements" (line 146-147). |
| Monitorable 6: DTA on merged-entity losses | NO | 1 | No tax disclosure. |
| Monitorable 7: auditor, CARO, CFO seat | PARTIAL | 1 | CFO named (line 158); no KMP filing or certification here. |
| Tracker: Safran award value/tenure; Hosur commissioning date | PARTIAL | 1 | Tenure above 15 years stated; value and Hosur date absent. |
| Tracker: amalgamation route (S.233 rejected 14-Oct; refile or NCLT S.232) | NO | 1 | Not mentioned. |
| Tracker: non-promoter institutional holding; IPO lock-in about Dec-2026 | NO | 1 | Not mentioned. |
| Tracker: Rs 650 Cr warrants (EGM 22-Oct) | PARTIAL | 0 | Amount and uses stated; approval status and terms absent (A3-07). |
| Tracker: Aequs Cookware JV Rs 30.05 cr receivable at 12% | NO | 1 | Not mentioned. |
| Proposed pledge tripwire | NO | 1 | No pledge disclosure; warrant funding source unknown. |
| Falsification line | PARTIAL | n/a | Leg 1 met (A3-01); leg 2 undisclosed. |
| Spear fact 1: aero FY27 revenue +25-30%, margin above 20% | YES | 0 | H1 aero +42% (line 110); margin about 22.5% derived. |
| Spear fact 3: cash conversion and balance sheet | NO | 1 | No balance sheet or cash flow. |

## 5. ITEMS FOR A4 (FORWARD-SIGNAL and AMBIGUOUS)
Forward signals: A3-02, A3-03, A3-04, A3-05, A3-06, A3-07, A3-08.
Ambiguous: A3-09, A3-10, A3-11, A3-12, A3-13, A3-14, A3-15, A3-16.

```yaml
stage: A3-forensics
company: "AEQUS"
quarter: "q2fy27"
doctype: "presentation"
model: "claude-opus-5-5"
status: complete
forensics_path: "runs/aequs-q2fy27/work/forensics_pressrelease_aequs_q2fy27.md"
ledger_reconciled_pct: 100
checklist:
  F1: N.A.
  F2: FINDING
  F3: N.A.
  F4: N.A.
  F5: N.A.
  F6: FINDING
  F7: FINDING
  F8: N.A.
  F9: N.A.
  F10: FINDING
  F11: N.A.
  F12: FINDING
  F13: FINDING
  F14: FINDING
  F15: N.A.
  F16: FINDING
  F17: FINDING
findings:
  - {id: "A3-01", check: "F17", line: "118-119", classification: "CONFIRMATORY-NEGATIVE", implication: "Falsification leg 1 fired: Q2 consumer EBITDA loss Rs 40.1 cr vs Rs 36.1 cr threshold; leg 2 (utilisation <=23%) not disclosed"}
  - {id: "A3-02", check: "F16", line: "114, 118, 169", classification: "FORWARD-SIGNAL", implication: "Consumer revenue fell 21% QoQ (733 to 577 Mn, derived); release shows YoY only; consumer EBITDA margin -49% to -70%"}
  - {id: "A3-03", check: "F16", line: "179-181", classification: "FORWARD-SIGNAL", implication: "Consumer breakeven path 'recalibrating', undated; Q4 FY27 breakeven and 40-50% utilisation target not restated"}
  - {id: "A3-04", check: "F7", line: "154-155, 178", classification: "FORWARD-SIGNAL", implication: "'timing-related shift' framing; causes include supply chain constraints that can recur"}
  - {id: "A3-05", check: "F16", line: "109-111, 175", classification: "FORWARD-SIGNAL", implication: "Aero margin 22.3% vs about 25.9% Q2 FY26 (derived, -340 to -380 bps) and 22.7% Q1; undisclosed; trending toward 20% floor"}
  - {id: "A3-06", check: "F16", line: "126", classification: "FORWARD-SIGNAL", implication: "Below-EBITDA net charge 359/649/747/767 Mn (Q1 FY26 to Q2 FY27, derived); PAT breakeven needs about 3.1x Q2 EBITDA"}
  - {id: "A3-07", check: "F10", line: "144-145", classification: "FORWARD-SIGNAL", implication: "Rs 6,500 Mn warrants: count, price, upfront tranche NOT FOUND; dilution pending; check promoter funding vs pledge tripwire"}
  - {id: "A3-08", check: "F6", line: "145-147, 185", classification: "FORWARD-SIGNAL", implication: "Warrant uses differ in-document: working capital and strategic JV investments (146-147) vs expansion incl Hosur (185)"}
  - {id: "A3-09", check: "F2", line: "104-107", classification: "AMBIGUOUS", implication: "JV EBITDA share about 17% to 35% of reported EBITDA YoY; JV basis softens -45% to -36%; JV margin -450 bps QoQ; JV names NOT FOUND"}
  - {id: "A3-10", check: "F12", line: "85, 110, 118-119", classification: "AMBIGUOUS", implication: "Unallocated EBITDA -137 Mn Q2, -155 Mn Q1 (derived); segment EBITDA basis vs other income unstated"}
  - {id: "A3-11", check: "F16", line: "87, 92", classification: "AMBIGUOUS", implication: "'(>100) bps' labels a -974 bps EBITDA margin fall; QoQ '100 bps' vs +55 bps computed; PAT margin (12)% vs -12.76% computed"}
  - {id: "A3-12", check: "F6", line: "142, 185", classification: "AMBIGUOUS", implication: "Hosur 'upcoming' with no commissioning date or budget"}
  - {id: "A3-13", check: "F14", line: "139, 186, 170", classification: "AMBIGUOUS", implication: "Safran agreements shown as Q2 highlight but dated after quarter-end; order book inclusion and definition unstated"}
  - {id: "A3-14", check: "F13", line: "158", classification: "AMBIGUOUS", implication: "CFO appointment with no effective date or board reference; KMP filing still needed"}
  - {id: "A3-15", check: "F16", line: "184", classification: "AMBIGUOUS", implication: "H1 capex Rs 159.7 cr = 24% of Rs 660 cr plan; no segment split; phase-down vs back-loading"}
  - {id: "A3-16", check: "F17", line: "17-245 (whole document)", classification: "AMBIGUOUS", implication: "11 checklist items silent for 1 quarter: utilisation, cash flow, DTA, amalgamation, holding, cookware JV, pledge, capex split, Hosur date, Safran value, balance sheet"}
  - {id: "A3-17", check: "F14", line: "135-136, 199", classification: "NEUTRAL-FACT", implication: "SKUs vs qualified parts terminology; 238 new parts up from 86 in Q1"}
  - {id: "A3-18", check: "F16", line: "131, 170", classification: "NEUTRAL-FACT", implication: "Order book USD 1,096 Mn = +9.2% on spear USD 1,004 Mn, consistent with stated 9% QoQ"}
forward_signals: ["A3-02", "A3-03", "A3-04", "A3-05", "A3-06", "A3-07", "A3-08"]
ambiguous: ["A3-09", "A3-10", "A3-11", "A3-12", "A3-13", "A3-14", "A3-15", "A3-16"]
commitments:
  - {commitment: "Consumer EBITDA breakeven path", implied_date: "none (prior Q4 FY27 not restated)", ref: "line 179-180, R151", status_word: "recalibrating"}
  - {commitment: "Consumer remaining milestones to sustained production volumes", implied_date: "none", ref: "line 155-156, R139", status_word: "underway"}
  - {commitment: "Improve consumer utilisation", implied_date: "near-term, undated", ref: "line 180-181, R152", status_word: "underway"}
  - {commitment: "Rs 6,500 Mn warrant proceeds to capacity expansion, JV investments, working capital", implied_date: "none", ref: "line 144-147, 184-185, R133, R155", status_word: "initiated"}
  - {commitment: "Hosur manufacturing ecosystem", implied_date: "none", ref: "line 142, 185, R130", status_word: "initiated"}
  - {commitment: "Safran long-term supply agreements, six entities", implied_date: "signed after 30-Sep-2026", ref: "line 139-142, 186, R129, R156", status_word: "completed"}
  - {commitment: "Safran A320 wheels serial-production contract above 15 years", implied_date: "deliveries FY28 (spear, not restated)", ref: "line 131-133, R121, R122", status_word: "completed"}
  - {commitment: "Aerospace scope broadening", implied_date: "none", ref: "line 111-112, R097", status_word: "underway"}
  - {commitment: "Disciplined execution and stronger returns", implied_date: "none", ref: "line 187-188, R158", status_word: "intent only"}
  - {commitment: "CFO appointment Reenah Joseph", implied_date: "effective date NOT FOUND", ref: "line 158, R140", status_word: "completed"}
gate_a3: pass
blank_checks: []
analyst_note: "Consumer is the swing factor. Falsification leg 1 fired: Q2 consumer EBITDA loss Rs 40.1 cr vs the Rs 36.1 cr threshold (line 118). Leg 2, utilisation at or below 23%, is absent. Consumer revenue fell 21% QoQ (733 to 577 Mn, derived) while company capacity rose, so utilisation likely fell further [INFERENCE]. The release offsets this with YoY-only framing, a JV-inclusive EBITDA (-36% vs reported -45%), a 'timing-related shift' hedge and an undated breakeven recalibration. Aerospace holds the spear margin floor at 22.3% but compressed about 360 bps YoY, undisclosed. Below-EBITDA charges run about 767 Mn a quarter, so PAT breakeven needs about 3.1x current EBITDA. The Rs 650 cr warrant names working capital and new JV investments in one place and only Hosur in another; A4 should ask for the split, the terms and the promoter funding source (pledge tripwire link). Prior-year bases come from stated growth rates; ranges are in the report. A1 line anchors drift 1-2 lines on 11 rows; all values match."
```
