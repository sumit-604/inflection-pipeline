# A3 FORENSIC NOTES: Kross Limited (KROSS) Q2 FY27, doctype presentation (press release)

Model: claude-opus-5-5. Date: 2026-10-19.
Inputs: A1 structured `runs/kross-q2fy27/extracted/kross-pressrelease-q2fy27-structured.md`, A1 fulltext `runs/kross-q2fy27/extracted/kross-pressrelease-q2fy27-fulltext.md`, A2 ledger `runs/kross-q2fy27/work/ledger_pressrelease_kross_q2fy27.md`, Notion checklist transcription `runs/kross-q2fy27/work/notion-thesis.md` (memory, not evidence). Prior-quarter fulltext: none supplied. Source PDF and inputs/ not opened.

## 0. Ledger reconciliation

- Ledger IDs: 135. Read at fulltext line: 135. Reconciled: 100%.
- R094-R135 (canonical table, image transcription L116-124) were read cell by cell. R004-R045 (superseded twins, scrambled text layer L30-40) were read at L30-40. Every superseded value matches its canonical twin. No value conflict.
- R001-R003 (L23-24), R046-R053 (L44-50) and the CMD quote (L79-80) restate the table. All tie.
- Arithmetic recompute from L118-124 (filed numbers only):
  - EBITDA = Revenue minus Total Expenditure: 2,350.9 - 2,044.9 = 306.0; 1,309.2 - 1,161.7 = 147.5; 4,194.3 - 3,661.1 = 533.2; 2,702.8 - 2,393.5 = 309.3 vs 309.2 printed (rounding).
  - Margins: 13.02% / 11.27% (175 bps); 12.71% / 11.44% (127 bps); PAT 8.38% / 6.17% (220 bps); 7.91% / 6.95% (96 bps). All tie.
  - YoY: revenue 79.6%, expenditure 76.0%, EBITDA 107.4%, PAT 143.5% (196.9/80.8 = 143.7%, inside rounding of 80.8), H1 lines tie.
  - EPS does NOT tie. See A3-06.
- A1 citation drift (pipeline note, not a source finding): structured line refs for R055, R057, R059, R066, R067, R068, R069, R076, R077, R078, R086, R087 and R092 run one line early against the fulltext. Examples: R059 cites L76, but "Mr. Sudhir Rai" sits at L77. R092 cites L105, but "Disclaimer" sits at L106. R080 cites L22, but the quarter title sits at L21. Every finding below cites the verified fulltext line.

## 1. FINDINGS TABLE

| id | check | ledger row ref | line | short verbatim quote | classification | forward implication |
|---|---|---|---|---|---|---|
| A3-01 | F6 | R061, R054 | L61-62 | "Commercial production has commenced; current utilisation approximately 60-65%." | FORWARD-SIGNAL | Milestone confirmed (status word: completed for commissioning, underway for ramp). The plant has 35-40% headroom. The utilisation path is the Q3 tracker metric. Ask: volumes and OEM adoption of the extruded beam at 60-65%, and the target exit utilisation for FY27. |
| A3-02 | F6 | R062, R071, R085 | L63 | "Mills installed, production trials targeted for February-March 2027." | FORWARD-SIGNAL | Dated commitment for the catalyst timeline: trials in Q4 FY27. Commercial start date not stated. See A3-07 for the reframing against Q1 guidance. |
| A3-03 | F6 | R060, R070, R084 | L59-60 | "Supplies progressing in line with plan; further volume scale-up expected in H2 FY27." | AMBIGUOUS | No kit volume disclosed. The Notion record (memory) shows 226 kits in Q1 and a 500/month ramp "running behind". "In line with plan" conflicts with that record. Ask: Q2 kits per month, the H2 FY27 target, and whether the plan was reset. |
| A3-04 | F6 | R064, R065, R074, R075 | L68-72 | "Strategic increase in shaft manufacturing capacity & enhanced investment in Robotic Automation" / "Forward Integration into manufacturing of Cold Drawn Tubes" | FORWARD-SIGNAL | Two capex lines with no amount, no date and no funding source. Neither is on the Notion growth-lever list (memory). They add capex load to a name with negative FCF in FY24-FY26 (memory). Ask: capex in Rs Cr per line, commissioning dates, and the debt and equity split. |
| A3-05 | F6 | R076, R077, R078, R079, R086 | L81-83 | "utilisation expected to improve in the coming quarters" / "healthy order books" / "multiple capacity expansion initiatives nearing completion, Kross is well positioned to deliver healthy growth in FY27" | AMBIGUOUS | The CMD outlook carries no number: no revenue guide, no margin guide, no order-book value. "Nearing completion" does not name which initiatives. Ask: order book in Rs Cr, FY27 revenue and EBITDA-margin guidance, and the list of projects "nearing completion" with dates. |
| A3-06 | F10 | R130-R135, R118-R123 | L124, L122 | "EPS (Rs.) \| 3.08 \| 1.25 \| 146.4 \| 5.14 \| 2.91 \| 76.5" | AMBIGUOUS | Implied weighted shares = PAT / EPS: Q2 FY27 196.9/3.08 = 63.93 mn (63.83-64.03 mn across EPS rounding). Q2 FY26 = 64.64 mn. H1 FY27 = 64.51 mn. H1 FY26 = 64.54 mn. The pre-issue count is 64.51 mn (6,45,09,422, memory). Q2 FY27 implies FEWER shares than pre-issue. EPS growth (146.4%) exceeds PAT growth (143.5%), so the share count fell YoY. That is impossible after a share issue. Cross-check: H1 EPS 5.14 less Q2 EPS 3.08 gives Q1 2.06, but Q1 PAT 134.7 mn on 64.51 mn gives 2.09. Q2 EPS on 64.51 mn = 3.05. The H1 EPS (5.14) fits no allotment inside H1 weighting. Two readings: (a) the Q2 EPS cell is misstated and the Aug-2026 preferential was not allotted by 30-Sep; (b) a different share basis is in use. The filed results EPS line and paid-up capital separate them. A4: ask allotment date, shares outstanding at 30-Sep-2026, and the Q2 EPS basis. |
| A3-07 | F16 | R062, R071, R085 | L63 | "production trials targeted for February-March 2027" | AMBIGUOUS | Baseline is Q1 call guidance per Notion (memory, prior deck NOT FOUND): "seamless tube commercial Q4 FY27". The release now says trials, not commercial production, in the same window. If trials run in Feb-Mar 2027, commercial output likely starts in FY28. Lean bear: the Rs 167 Cr project (memory) carries cost before revenue for longer. Ask: commercial production date, and first-revenue quarter. |
| A3-08 | F16 | R112-R117, R093 | L121; L55-56 | "EBITDA Margin (%) \| 13.0 \| 11.3 \| 175 bps" / "helped support performance amid input cost pressures" | AMBIGUOUS | Q1 call guidance per Notion (memory) was a 14-15% EBITDA margin. The release does not restate a margin guide. Q2 prints 13.0% and names "input cost pressures" without a number. Lean bear: the guide may be softened by omission. Ask: is 14-15% still the guide, when, and what share of the input-cost increase is pass-through. |
| A3-09 | F16 | R106-R111, R118-R123 (ledger note: table omits other income, D&A, interest, PBT, tax) | L120, L122 | "EBITDA \| 306.0 \| 147.5" / "Profit After Tax \| 196.9 \| 80.8" | AMBIGUOUS | The table jumps from EBITDA to PAT. PAT/EBITDA conversion: Q2 FY27 64.3%, Q2 FY26 54.8%, implied Q1 FY27 59.3% (H1 less Q2). The below-EBITDA drag rose only to Rs 109.1 mn from Rs 66.7 mn while EBITDA doubled. This happened in the quarter the extrusion plant went commercial (new depreciation) and while the seamless tube build is debt-funded (memory). Candidate drivers: other income, capitalised interest, lower tax rate. None is disclosed. F8 cannot run on this document. Ask: Q2 other income, depreciation, finance cost (expensed and capitalised), and ETR. |
| A3-10 | F16 | R097, R109, R121 less R094, R106, R118 | L118, L120, L122 | "Revenue from Operations \| 2,350.9 \| 1,309.2 \| 79.6 \| 4,194.3" | AMBIGUOUS | Implied Q1 FY27 (H1 less Q2): revenue Rs 1,843.4 mn, EBITDA Rs 227.2 mn (12.33%), PAT Rs 134.7 mn. Revenue matches the Notion record (Rs 184.3 Cr). EBITDA margin (12.2%) and PAT (Rs 13.3 Cr) do not. The Notion record is memory, so this may be a recording error. It may also be a Q1 restatement inside the H1 figures. Low priority. A4: verify against the filed Q1 FY27 results before any QoQ claim. |
| A3-11 | F17 | R088 (basis), R094-R135 (table scope) | L30 | "Financial Highlights (Standalone):" | AMBIGUOUS | The release carries no balance sheet, cash flow or auditor report. Silent on checklist items: debtor days (re-engage trigger 1, leg 2), H1 CFO and cash, ROCE (trigger 2), and Limited Review Report qualification. This silence is normal for the doctype. Resolve it from the results filing and the concall. Do not score it as evasion. |
| A3-12 | F17 | R063, R073 | L66-67 | "High-pressure moulding line (Foundry) Progressing as planned to double existing casting capacity." | AMBIGUOUS | Q1 call guidance per Notion (memory): HP moulding line due Sept-2026. On 17-Oct-2026 the release says "progressing", not commissioned. The line slipped past its date, or the plan moved, or the memory date is wrong. Lean bear. Ask: commissioning date, and the reason for any slip. |
| A3-13 | F17 | R074, R075, R062 (no funding row exists) | L74-75 | "These investments underscore Kross Limited's commitment to adopting innovative technologies" | AMBIGUOUS | The release lists seven capacity lines (L59-72) but states no capex amount and no funding. Silent on checklist items: Aug-2026 preferential allotment status, promoter warrant upfront, seamless tube debt vs equity, and identity of the four non-promoter allottees. A3-06 bears on the allotment question. Ask all four. |
| A3-14 | F17 | R091, R066, R067 | L51-54; L97-98 | "Broad-based segmental growth was supported by strong demand in the M&HCV and trailer segments" / "Company is a key supplier to various OEMs, including leading players in the commercial vehicle and tractor segments." | AMBIGUOUS | No segment split, no customer named, no export share. Silent on checklist items: segment split, top-5 customer de-growth (FY24-26, memory), and tractor and export share targets. Ask: Q2 revenue split by trailer axle and suspension, forged and machined OEM components, tractor, and exports. Ask also for top-5 customer share for H1. |

## 2. CHECKLIST SCORECARD

| check | status | basis |
|---|---|---|
| F1 Zero-value standing items | N.A. | Ledger shows zero ZERO_STANDING rows. A press release has no statutory line-item template (table L118-124 has 7 rows, none nil). |
| F2 Standalone vs consolidated | N.A. | Standalone only (L30 "Financial Highlights (Standalone)"). No consolidated column to decompose. |
| F3 Shell-entity detection | N.A. | No cost-line detail and no consolidated statement in the document. |
| F4 Unaudited contribution ratio | N.A. | No auditor report or Other Matters paragraph in a press release. |
| F5 Going concern / EoM tracking | N.A. | No EoM paragraph. No prior-quarter fulltext supplied. |
| F6 Forward-commitment mining | FINDING | 9 commitments extracted (register below). Lexicon hits: "commenc" L61, "expected" L60 and L81, "will drive" L88. Status phrases: "targeted" L63, "on track" L64, "as planned" L66, "nearing completion" L83. A3-01 to A3-05. |
| F7 Hedge phrase mining | PASS | No lexicon hit ("may sometimes", "could have an effect", "no assurance", "subject to", "evaluating", "exploring", "in discussions", "endeavour"). The only hedge language is the standard safe harbour at L106-115 ("Many factors could cause the actual results", L112). It names no revenue-lumpiness or customer-concentration risk. |
| F8 Tax forensics | N.A. | No tax, PBT or deferred-tax line in the document. The EBITDA-to-PAT bridge gap is logged under F16 (A3-09). |
| F9 OCI forensics | N.A. | No OCI line. |
| F10 Share count and dilution | FINDING | No paid-up capital disclosed. EPS (L124) implies Q2 FY27 weighted shares of 63.93 mn, below the 64.51 mn pre-issue count. EPS YoY (146.4%) exceeds PAT YoY (143.5%). A3-06. |
| F11 Reserves and net worth tie-out | N.A. | No paid-up capital, other equity or net worth figure in the document. |
| F12 Segment forensics | N.A. | No segment table. The segment driver text (R091, L51-54) is qualitative. The silence is logged under F17 (A3-14). |
| F13 Board outcome beyond results | N.A. | The release reports no board outcome, AGM, record date or director change. |
| F14 Note drafting inconsistencies | PASS | Headline L23-24, bullets L44-50 and CMD quote L79-80 tie to the table L118-124. Margins and YoY recompute within rounding. Entity name is consistent ("Kross Limited" / "Kross Ltd"). The EPS discrepancy is taken under F10. |
| F15 Entity list diffs | N.A. | No consolidation list. No prior quarter supplied. |
| F16 Dropped / reframed disclosures | FINDING | Prior deck NOT FOUND. The baseline is the Q1 FY27 call guidance on the Notion page (memory). Seamless tube is reframed to trials (A3-07). The 14-15% margin guide is not restated (A3-08). The EBITDA-to-PAT bridge is omitted while conversion jumps (A3-09). Implied Q1 differs from the record (A3-10). |
| F17 Silence audit | FINDING | Run because the orchestrator supplied the Notion checklist. 14 checklist and guidance items checked. 4 addressed or partly addressed, 10 silent (table below). A3-11 to A3-14. |

## 3. COMMITMENT REGISTER (F6)

| commitment | implied date | ref | status word |
|---|---|---|---|
| Tipping jacks: further volume scale-up | H2 FY27 (Oct-2026 to Mar-2027) | L59-60, R070/R084 | underway |
| Axle beam extrusion plant: commercial production, utilisation 60-65% | commenced by 17-Oct-2026 | L61-62, R061/R054 | completed (commissioning); underway (ramp) |
| Seamless tube: mills installed, production trials | February-March 2027 | L63, R071/R085 | underway |
| Forging capacity expansion "on track" | undated | L64-65, R072 | underway |
| HP moulding line to double casting capacity, "progressing as planned" | undated in release (Sept-2026 per Q1 call, memory) | L66-67, R073 | underway |
| Axle shaft robotic forging and machining capacity increase | undated | L68-70, R074 | initiated |
| Cold drawn tubes forward integration | undated | L72, R075 | initiated |
| Utilisation to improve | "coming quarters" | L81, R076 | underway |
| Healthy growth in FY27; initiatives "nearing completion"; new products to drive growth | FY27 (by Mar-2027) | L83, L87-88, R077/R078/R079/R086 | underway |

## 4. WHAT WAS NOT DISCUSSED (F17 silence audit, press release)

Consecutive quarters of silence counts only press releases. No prior-quarter release reached this run, so each count is 1 (this document), prior NOT FOUND.

| checklist / guidance item (Notion, memory) | addressed in release? | line | quarters silent |
|---|---|---|---|
| Re-engage trigger 1, leg 1: EBITDA margin above ~14% | Addressed: 13.0% | L121 | 0 |
| Re-engage trigger 1, leg 2: debtor days falling | NOT addressed | none | 1 |
| Re-engage trigger 2: ROCE toward 20% | NOT addressed | none | 1 |
| Limited Review Report qualification | NOT addressed (no auditor report in doctype) | none | 1 |
| FY27 base needs ~13.2% EBITDA margin over Q2-Q4 | Addressed: Q2 13.0% | L121 | 0 |
| HP moulding line commissioned (due Sept-2026) | Partly: "Progressing as planned", not commissioned | L66-67 | 1 (status not confirmed) |
| H1 CFO and cash | NOT addressed | none | 1 |
| Aug-2026 preferential allotted; shares 6,45,09,422 to 6,60,09,422 | NOT addressed; EPS points to no allotment in H1 weighting (A3-06) | L124 | 1 |
| Seamless tube funding, debt vs equity | NOT addressed | none | 1 |
| Segment split | NOT addressed (qualitative only) | L51-54 | 1 |
| Top-5 customer de-growth | NOT addressed; no customer named | L97-98 | 1 |
| Extruded-beam OEM adoption | Partly: utilisation 60-65%, no OEM named | L61-62 | 1 (adoption) |
| Identity of four non-promoter allottees | NOT addressed | none | 1 |
| Q1 call guidance: margin 14-15%; tipping jacks 500/month; seamless tube commercial Q4 FY27 | Not restated; jack volume not given; seamless tube reframed to trials | L121, L59-60, L63 | 1 |

## 5. YAML BLOCK

```yaml
stage: A3-forensics
company: "KROSS"
quarter: "Q2 FY27"
doctype: "presentation"
model: "claude-opus-5-5"
status: complete
forensics_path: "runs/kross-q2fy27/work/forensics_pressrelease_kross_q2fy27.md"
ledger_reconciled_pct: 100
checklist:
  F1: N.A.
  F2: N.A.
  F3: N.A.
  F4: N.A.
  F5: N.A.
  F6: FINDING
  F7: PASS
  F8: N.A.
  F9: N.A.
  F10: FINDING
  F11: N.A.
  F12: N.A.
  F13: N.A.
  F14: PASS
  F15: N.A.
  F16: FINDING
  F17: FINDING
findings:
  - {id: "A3-01", check: "F6", line: "L61-62", classification: "FORWARD-SIGNAL", implication: "Extrusion plant commercial, utilisation 60-65%; 35-40% headroom; utilisation path is the Q3 tracker; ask OEM adoption and FY27 exit utilisation"}
  - {id: "A3-02", check: "F6", line: "L63", classification: "FORWARD-SIGNAL", implication: "Seamless tube trials Feb-Mar 2027; commercial start date not stated; feeds catalyst timeline"}
  - {id: "A3-03", check: "F6", line: "L59-60", classification: "AMBIGUOUS", implication: "Tipping jacks 'in line with plan' with no kit volume; conflicts with memory record of ramp running behind 500/month; ask Q2 kits/month and H2 target"}
  - {id: "A3-04", check: "F6", line: "L68-72", classification: "FORWARD-SIGNAL", implication: "Two new capex lines (robotic axle shaft, cold drawn tubes) with no amount, date or funding; adds capex load to a negative-FCF name; ask Rs Cr, dates, funding split"}
  - {id: "A3-05", check: "F6", line: "L81-83", classification: "AMBIGUOUS", implication: "CMD outlook unquantified: no revenue or margin guide, order book not valued, 'nearing completion' projects unnamed"}
  - {id: "A3-06", check: "F10", line: "L124", classification: "AMBIGUOUS", implication: "Q2 EPS 3.08 implies 63.93 mn weighted shares, below 64.51 mn pre-issue; EPS YoY 146.4% exceeds PAT YoY 143.5%; H1 EPS 5.14 fits no allotment; Q2 EPS on 64.51 mn = 3.05; ask allotment date, 30-Sep share count, EPS basis"}
  - {id: "A3-07", check: "F16", line: "L63", classification: "AMBIGUOUS", implication: "Seamless tube reframed from commercial Q4 FY27 (Q1 guide, memory) to trials Feb-Mar 2027; commercial revenue likely FY28; lean bear"}
  - {id: "A3-08", check: "F16", line: "L121; L55-56", classification: "AMBIGUOUS", implication: "14-15% margin guide (memory) not restated; Q2 13.0% with unquantified input cost pressures; ask if guide stands"}
  - {id: "A3-09", check: "F16", line: "L120, L122", classification: "AMBIGUOUS", implication: "EBITDA-to-PAT bridge omitted; PAT/EBITDA 64.3% vs 54.8% YoY and 59.3% implied Q1, during a commissioning quarter; ask other income, D&A, finance cost expensed and capitalised, ETR"}
  - {id: "A3-10", check: "F16", line: "L118, L120, L122", classification: "AMBIGUOUS", implication: "Implied Q1 (H1 less Q2) EBITDA 12.33% and PAT Rs 134.7 mn differ from memory record 12.2% and Rs 13.3 Cr; verify filed Q1 before any QoQ claim; low priority"}
  - {id: "A3-11", check: "F17", line: "L30", classification: "AMBIGUOUS", implication: "No balance sheet, CFO, cash, debtor days, ROCE or review report; doctype-normal silence; resolve from results filing and concall, not evasion"}
  - {id: "A3-12", check: "F17", line: "L66-67", classification: "AMBIGUOUS", implication: "HP moulding line still 'progressing' on 17-Oct-2026 against a Sept-2026 date (memory); possible slip; ask commissioning date"}
  - {id: "A3-13", check: "F17", line: "L74-75", classification: "AMBIGUOUS", implication: "Seven capacity lines, no capex or funding stated; silent on preferential allotment, warrant upfront, seamless tube debt vs equity, allottee identity"}
  - {id: "A3-14", check: "F17", line: "L51-54; L97-98", classification: "AMBIGUOUS", implication: "No segment split, no customer named; silent on top-5 customer de-growth, tractor and export share; ask Q2 split and H1 top-5 share"}
forward_signals: ["A3-01", "A3-02", "A3-04"]
ambiguous: ["A3-03", "A3-05", "A3-06", "A3-07", "A3-08", "A3-09", "A3-10", "A3-11", "A3-12", "A3-13", "A3-14"]
commitments:
  - {commitment: "Tipping jacks further volume scale-up", implied_date: "H2 FY27", ref: "L59-60 R070", status_word: "underway"}
  - {commitment: "Axle beam extrusion commercial production, utilisation 60-65%", implied_date: "commenced by 17-Oct-2026", ref: "L61-62 R061", status_word: "completed"}
  - {commitment: "Seamless tube production trials", implied_date: "Feb-Mar 2027", ref: "L63 R071", status_word: "underway"}
  - {commitment: "Forging capacity expansion on track", implied_date: "undated", ref: "L64-65 R072", status_word: "underway"}
  - {commitment: "HP moulding line to double casting capacity", implied_date: "undated (Sept-2026 per Q1 call, memory)", ref: "L66-67 R073", status_word: "underway"}
  - {commitment: "Axle shaft robotic forging and machining capacity", implied_date: "undated", ref: "L68-70 R074", status_word: "initiated"}
  - {commitment: "Cold drawn tubes forward integration", implied_date: "undated", ref: "L72 R075", status_word: "initiated"}
  - {commitment: "Utilisation to improve", implied_date: "coming quarters", ref: "L81 R076", status_word: "underway"}
  - {commitment: "Healthy FY27 growth; initiatives nearing completion; new products drive growth", implied_date: "FY27", ref: "L83, L87-88 R077-R079", status_word: "underway"}
gate_a3: pass
blank_checks: []
analyst_note: "Two-page standalone press release. All 135 IDs reconciled; superseded R004-R045 match their R094-R135 twins. A1 line refs for R055, R057, R059, R066-R069, R076-R078, R086-R087 and R092 run one line early; findings cite verified fulltext lines. Top item: Q2 EPS 3.08 implies 63.93 mn weighted shares, below the 64.51 mn pre-issue count, and EPS growth beats PAT growth, which cannot follow a share issue. H1 EPS 5.14 fits no allotment inside H1. The filed results EPS line and paid-up capital settle whether the Aug-2026 preferential was allotted. Second: PAT/EBITDA conversion rose to 64.3% from 54.8% in a commissioning quarter, and the release hides the bridge. Third: seamless tube reads trials Feb-Mar 2027, not commercial Q4 FY27, and the HP moulding line is still progressing past Sept-2026. Both baselines are Notion memory, not evidence. F17 ran because the orchestrator supplied the checklist. Balance-sheet silence is normal for this doctype, so A4 resolves it from the results filing and does not score it as evasion."
```
