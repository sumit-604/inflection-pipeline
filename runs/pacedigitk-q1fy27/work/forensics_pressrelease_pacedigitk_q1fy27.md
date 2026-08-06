# A3 FORENSIC NOTES — pacedigitk — Q1FY27 — doctype: PRESS RELEASE

Source under review: `extract_pressrelease_pacedigitk_q1fy27.txt` (4 pages, 189 embedded lines).
Ledger reconciled: `ledger_pressrelease_pacedigitk_q1fy27.md` — all rows read verbatim at cited lines.
Cross-check filing: `extract_results_pacedigitk_q1fy27.txt` (consolidated unaudited P&L, unit Millions, x0.1 = Crores).
Thesis context (memory to weigh, not evidence): `notion_thesis_inline.md`.

Ledger reconciliation: 36 disclosure blocks + 56 numbers + 7 forward signals + 1 mgmt quote + 1 safe harbour = 101 rows, every one read at its cited line. 100% reconciled. No unread rows, no count disputes with A2 (A2 GATE passed; I re-swept the two A2-noted line-wrap artifacts at lines 84-85 and 158-159 and confirm both).

---

## HEADLINE NUMBER RECONCILIATION (priority focus #1)

Every press-release headline number that has a statutory counterpart TIES to the results filing (consolidated, unit-converted). No figure fails to tie.

| PR figure (line) | PR value | Results-filing line | Filing value (mn) | = Cr | Tie |
|---|---|---|---|---|---|
| Revenue Q1FY27 (60,74,140,147) | 555.4 | 438 | 5,553.64 | 555.4 | yes |
| Revenue Q1FY26 (74) | 367.1 | 438 | 3,670.79 | 367.1 | yes |
| Revenue FY26 (74) | 2,641.3 | 438 | 26,412.70 | 2,641.3 | yes |
| PAT Q1FY27 (61,77,142) | 62.5 | 458 | 625.05 | 62.5 | yes |
| PAT Q1FY26 (77) | 54.7 | 458 | 546.98 | 54.7 | yes |
| PAT FY26 (77) | 307.3 | 458 | 3,072.64 | 307.3 | yes |
| Order book total (60,151) | 10,803.3 | none (KPI) | — | — | internally ties: 8,453 + 2,350.3 = 10,803.3 |
| Rev YoY (74) 51.3% | 555.4/367.1 = 51.3% | — | — | — | yes |
| PAT YoY (77) 14.3% | 62.5/54.7 = 14.3% | — | — | — | yes |

EBITDA (86.1 / 80.1) and ALL margin percentages are company-defined non-GAAP with NO line item in the statutory filing (A2 flagged CROSS_CHECK). I re-derived them from filed lines:
- EBITDA Q1FY27 = PBT 816.29 + Dep 44.37 + Fin 283.41 − Other income 283.41 = 860.66 mn = 86.1 cr. Ties.
- EBITDA Q1FY26 = PBT 738.79 + Dep 20.87 + Fin 97.23 − Other income 56.36 = 800.53 mn = 80.1 cr. Ties.
- Definition is consistent across both periods: EBITDA EXCLUDES other income. Margins (86.1/555.4 = 15.5%; 80.1/367.1 = 21.8%) tie.

So the numbers themselves are genuine and definition-consistent. The forensic issue is not falsification; it is (a) the unexplained margin collapse and (b) what the release stays silent on. See F16.

Filing-side oddity noted for A4 (not a press-release figure): consolidated Other income (line 439) and Finance costs (line 447) are BOTH exactly 283.41 mn in Q1FY27. Flagged as a coincidence to verify at the AR / concall, not asserted as an error.

---

## FINDINGS TABLE

| id | check | ledger row ref | line | verbatim quote | classification | forward implication |
|---|---|---|---|---|---|---|
| FND-01 | F6 | Tbl3 #1,#3,#6 | 84-86, 113-115, 157-158 | "Subsequent to the quarter, the Company has also operationalized its additional BESS manufacturing platform with an installed capacity of 2.5 GWh, bringing its total BESS manufacturing capacity to 5 GWh" | FORWARD-SIGNAL | 5 GWh BESS capacity stated COMPLETED subsequent to quarter (by Aug 05). Confirms Notion trigger #3 GREEN (commissioning on time). Verify actual date/throughput at concall. |
| FND-02 | F6 | Tbl3 #4 | 118 | "remains on track to commission its in-house container fabrication facility" | FORWARD-SIGNAL | Dateable commitment: Notion trigger #4 expects first containers Q2 FY27, Red if slips past Q3 FY27. Status = on-track, not yet done. Track to next print. |
| FND-03 | F6 | Tbl3 #4,#7 | 117-119, 158-159 | "phased expansion of its BESS manufacturing capacity from 5 GWh to 10 GWh and remains on track" | FORWARD-SIGNAL | Undated capex/capacity commitment (5→10 GWh). No cost, no funding source disclosed. Capex intensity feeds the CFO/receivables bear thesis. |
| FND-04 | F6 | Tbl3 #5; Disc #27 | 123-127, 129-135 | "OEM partnership with NEC XON Systems... to market, distribute and deploy its grid-scale BESS... across South Africa, Botswana, Mozambique, Namibia and Mauritius"; "strategic cooperation agreement with MEGMEET... AI data center power infrastructure" | AMBIGUOUS | These are PARTNERSHIPS / cooperation agreements and an R&D center — capability, NOT booked orders or revenue. Notion trigger #10 (NEC XON) needs a SIGNED CONTRACT to go Green; a partnership is not that. Non-government revenue pathway (Section 22 condition c) still unproven. A4 question: any order value / first shipment date? |
| FND-05 | F6 | Disc #22-23; Tbl2 #37 | 101-106 | "received an Advance Work Order from Bharat Sanchar Nigam Limited (BSNL)... contract value of ₹264 crore" | CONFIRMATORY-NEGATIVE | The one new order disclosed is a PSU (BSNL). Reinforces ~96% government/PSU concentration bear thesis; does not advance the non-govt pathway. Also "Advance Work Order" is pre-firm — verify it converts to a definitive order. |
| FND-06 | F7 | Tbl3 #2; Disc #19 | 91-92 | "Commercial & Industrial (C&I) energy storage prototype solutions, which are currently under evaluation for commercial deployment" | FORWARD-SIGNAL | Pre-emptive hedge: C&I is at prototype/evaluation stage, not commercial. Tells us C&I contributes no near-term revenue. A4 question: expected commercial launch window? |
| FND-07 | F16 | Tbl2 #17,#18,#19,#20 | 76 (also 75) | "EBITDA Margin (%) 15.5% 21.8% ... 17.2% 19.8%" | AMBIGUOUS | EBITDA margin down 630 bps YoY (15.5% vs 21.8%) with revenue +51.3% but EBITDA only +7.5%. Multi-period DOWNTREND: FY25 19.8% → FY26 17.2% → Q1FY27 15.5%. Filing shows the mechanism: Cost of materials consumed jumped 396.55→3,753.16 mn (line 442) with EPC project expense falling 2,248.67→974.54 mn (line 443) and a 732.23 mn inventory build (line 445) — a mix shift toward lower-margin BESS MANUFACTURING. Release narrates none of it. A4 question: is 15.5% the new structural margin for a manufacturing-weighted mix, or a transient inventory-timing effect? |
| FND-08 | F16 | Tbl2 #27,#28 | 78 | "PAT Margin (%) 11.3% 14.9%" | CONFIRMATORY-NEGATIVE | PAT margin fell 360 bps YoY. The headline "PAT... up 14.3% YoY" (line 61) is purely volume-driven; on a margin basis profitability deteriorated. Selective framing. |
| FND-09 | F16 | (omission) | n/a (absent) | — no CFO, receivables, inventory, customer-mix, segment-revenue, or ROCE line anywhere in the release — | CONFIRMATORY-NEGATIVE | The release is silent on the single most thesis-relevant number this quarter: Q1 FY27 operating cash flow (the binding EXIT gate, Notion #1). Also silent on receivables (#2), inventory (#7), Tier-1/Tier-3 and PSU/private mix, segment revenue (#5,#6), ROCE (#8,#16). Per Role 5, sustained silence on a historically deteriorating metric (cumulative CFO/PAT = −1.07x) is a confirmatory negative. The CFO gate is NOT resolved by this document; it awaits the concall / cash-flow statement. |
| FND-10 | F16 | (omission; cross-doc) | n/a (absent) | — no EPS disclosed in the release — | CONFIRMATORY-NEGATIVE | Release touts "PAT up 14.3%" but omits EPS. Filing shows consolidated basic EPS actually DECLINED YoY: 3.03 → 2.84 (line 485), because IPO lifted paid-up capital 356.88 → 431.70 mn (line 481). Per-share earnings fell while absolute PAT rose. Omission flatters. |
| FND-11 | F16 | Tbl2 #2,#32,#36 | 60, 83, 99, 151 | "Order Book at ₹ 10,803.3 crore"; "executable Energy order book stood at ₹ 8,453 crore, ... as of Aug 05, 2026" | AMBIGUOUS | Order book is stated "as on Aug 05, 2026" (the release date, POST quarter-end) not as of June 30, 2026 the reporting date — period-boundary mixing against a June-30 P&L. "Executable" is an undefined qualifier (vs gross / vs pending). A4 question: order book as of June 30, and the executable vs gross definition. |
| FND-12 | F16 / CROSS_CHECK | Tbl2 #11-#20,#44-#46,#49 | 75-76, 141, 143 | "EBITDA 86.1 ... EBITDA Margin (%) 15.5%" | NEUTRAL-FACT | EBITDA and every margin are company-defined non-GAAP with no statutory line item; independently re-derived and they TIE (see reconciliation). Reconciled, but a transparency gap: the reader cannot verify EBITDA from the release alone. No misstatement. |
| FND-13 | F2 (cross-doc) | Tbl2 #1,#5 | 60, 74 | "Revenue from Operations at ₹555.4 crore" (consolidated) | NEUTRAL-FACT | Consolidated revenue 555.4 cr vs standalone 264.24 cr (filing line 158) — over half of group revenue is subsidiary-sourced (Lineage Power / the BESS build). The release presents consolidated only and does not attribute the revenue split; the whole BESS growth story sits in subsidiaries. Context for A4, not a defect. |
| FND-14 | F16 | Tbl2 #3 | 61 | "PAT stood at ₹62.5 crore" | NEUTRAL-FACT | Headline PAT 62.5 cr is consolidated TOTAL PAT including non-controlling interest (11.82 mn, line 470). PAT attributable to owners is 613.23 mn = 61.3 cr (line 469). Standard practice, but headline is ~1.9% above owners' earnings. |

---

## CHECKLIST SCORECARD (all 17)

| # | Status | Basis |
|---|---|---|
| F1 ZERO-VALUE STANDING ITEMS | N.A. | Press release carries no financial-statement notes / standing line items; A2 confirms no ZERO_STANDING items (that enumeration belongs to the results doctype). |
| F2 STANDALONE vs CONSOLIDATED | N.A. | Release presents CONSOLIDATED headline figures only; no standalone column to decompose. Cross-doc observation captured as FND-13 (>50% of revenue is subsidiary-sourced). |
| F3 SHELL-ENTITY DETECTION | N.A. | No standalone-vs-consolidated cost lines in the release. |
| F4 UNAUDITED CONTRIBUTION RATIO | N.A. | No auditor Other Matters in the release. (Filing side, for context: unreviewed subsidiaries' net profit Rs 0.75 mn + Rs NIL — immaterial, <1% of PAT — but that is results-doctype forensics.) |
| F5 GOING CONCERN / EoM | N.A. | No auditor report / EoM in a press release. |
| F6 FORWARD-COMMITMENT MINING | FINDING | 7 A2 forward signals mined; lexicon hits "operationalized", "commissioned", "remains/remain on track", "under evaluation", "continued investing". FND-01..06. Commitment register below. |
| F7 HEDGE PHRASE MINING | FINDING | Substantive hedge "under evaluation for commercial deployment" (line 92, FND-06). Safe Harbour (185-189) "subject to numerous risks and uncertainties" is boilerplate = NEUTRAL. |
| F8 TAX FORENSICS | N.A. | No tax lines / ETR in the release. |
| F9 OCI FORENSICS | N.A. | No OCI in the release. |
| F10 SHARE COUNT & DILUTION | N.A. | No share count / EPS in the release. EPS-decline omission captured cross-doc as FND-10. |
| F11 RESERVES / NET WORTH | N.A. | No balance sheet in the release. |
| F12 SEGMENT FORENSICS | N.A. | Release gives segment ORDER BOOK only (Energy 8,453; Telecom 2,350.3), no segment revenue / assets / liabilities. (Filing segment note appears blank in extract, lines 490-494.) |
| F13 BOARD OUTCOME BEYOND RESULTS | N.A. | Press release is not the board-outcome document; carries no AGM / AR / director-term disclosures. |
| F14 NOTE DRAFTING INCONSISTENCIES | PASS | Checked entity naming across the release ("Pace Digitek Limited (Formerly...)", subsidiary "Lineage Power Private Limited" line 172-173, "Pace-Lineage Research Center" line 132) — internally consistent. No notes / auditor letter to cross-check. Ref No Q02_24 (PR) differs from Q02_21 (results), same date — routine sequence, not an inconsistency. |
| F15 ENTITY LIST DIFFS | N.A. | Release carries no consolidation list; no prior-quarter release in scope to diff. |
| F16 DROPPED / REFRAMED / OMITTED | FINDING | Margin collapse unexplained (FND-07,08); silence on CFO/receivables/inventory/customer-mix/EPS (FND-09,10); order-book period-boundary and "executable" framing (FND-11); non-GAAP transparency (FND-12). |
| F17 CONCALL SILENCE AUDIT | N.A. | No transcript in scope. The Notion-checklist silence audit was performed against THIS document and recorded under F16/FND-09 (a press release cannot host a transcript-based silence audit). |

---

## COMMITMENT REGISTER (from F6)

| commitment | implied date | ref (line) | status word |
|---|---|---|---|
| Operationalize additional 2.5 GWh BESS platform → 5 GWh total | subsequent to quarter, by Aug 05 2026 | 84-86 | completed |
| Commission additional 2.5 GWh BESS line → 5 GWh total installed | subsequent to quarter, by Aug 05 2026 | 113-115, 157-158 | completed |
| Commission in-house container fabrication facility | Q2 FY27 (per Notion trigger #4) | 118 | underway / on-track |
| Phased expansion BESS capacity 5 GWh → 10 GWh | undated | 117-119, 158-159 | underway / on-track |
| C&I energy storage prototype → commercial deployment | undated | 91-92 | initiated / under-evaluation |
| NEC XON OEM partnership (Africa go-to-market, 5 countries) | entered, during/around quarter | 123-127 | completed (partnership signed; NOT an order) |
| MEGMEET strategic cooperation (AI data center power) + Pace-Lineage R&D Center, Pune | following quarter-end | 129-135 | completed (agreement signed / center established) |

---

## NOTION MONITORING CHECKLIST — WHAT THIS DOCUMENT ADDRESSES vs LEAVES SILENT (priority focus #4)

| Trigger | Addressed by press release? | Note |
|---|---|---|
| #1 Q1 FY27 CFO (BINDING gate) | NO — silent | The single most thesis-relevant number; unresolved by this doc. FND-09. |
| #2 Receivables | NO — silent | FND-09. |
| #3 5 GWh BESS commissioning (Green: on time Jul 2026) | YES | FND-01 — 5 GWh stated commissioned subsequent to quarter. Leans GREEN; verify exact date. |
| #4 Container fab commissioning | PARTIAL | FND-02 — "remains on track", no first-container date. |
| #5 BOO revenue >= Rs150 Cr | NO — silent | BOO mentioned qualitatively (line 94-96), not quantified. |
| #6 Energy segment revenue | NO — silent | Only Energy ORDER BOOK (8,453) given, not revenue. |
| #7 Inventories | NO — silent | Filing shows a 732 mn inventory build (line 445); release silent. FND-09. |
| #8/#9/#16/#17 ROCE | NO — silent | FND-09. |
| #10 NEC XON Africa orders (Green: signed contract) | PARTIAL | FND-04 — partnership only, no order. Not yet Green. |
| #11 Rs740 Cr RPT classification | NO — silent | Not a press-release topic. |
| #12 Subsidiary purposes disclosure | NO — silent | Belongs to FY26 AR. |
| #13 New CARO observation | NO — silent | Belongs to audit / AR. |
| #14 Net D/E | NO — silent | No balance sheet in release; capex ramp (FND-03) raises the question. |
| #15 MSEDCL VGF disbursement | NO — silent | Not mentioned. (Filing note 6 references the PREPL/MSEDCL BESS project capex, results doctype.) |

Bottom line for A4: the release emphasises revenue growth, order book and capacity milestones (all real), while staying silent on every cash-and-quality metric the binding thesis gate depends on. The margin trajectory (19.8% → 17.2% → 15.5%) is disclosed in the table but never narrated.

---

```yaml
stage: A3-forensics
company: "pacedigitk"
quarter: "q1fy27"
doctype: "pressrelease"
model: claude-opus-4-8
status: complete
forensics_path: "/home/user/inflection-pipeline/runs/pacedigitk-q1fy27/work/forensics_pressrelease_pacedigitk_q1fy27.md"
ledger_reconciled_pct: 100
checklist:
  F1: N.A.
  F2: N.A.
  F3: N.A.
  F4: N.A.
  F5: N.A.
  F6: FINDING
  F7: FINDING
  F8: N.A.
  F9: N.A.
  F10: N.A.
  F11: N.A.
  F12: N.A.
  F13: N.A.
  F14: PASS
  F15: N.A.
  F16: FINDING
  F17: N.A.
findings:
  - {id: "FND-01", check: "F6", line: "84-86,113-115,157-158", classification: "FORWARD-SIGNAL", implication: "5 GWh BESS capacity stated commissioned subsequent to quarter; confirms Notion trigger #3, verify date/throughput"}
  - {id: "FND-02", check: "F6", line: "118", classification: "FORWARD-SIGNAL", implication: "Container fab 'remains on track'; Notion trigger #4 expects Q2 FY27 first containers"}
  - {id: "FND-03", check: "F6", line: "117-119,158-159", classification: "FORWARD-SIGNAL", implication: "Undated 5->10 GWh capex ramp; funding source undisclosed, feeds CFO bear thesis"}
  - {id: "FND-04", check: "F6", line: "123-127,129-135", classification: "AMBIGUOUS", implication: "NEC XON / MEGMEET are partnerships not orders; non-govt revenue pathway still unproven, Notion trigger #10 not Green"}
  - {id: "FND-05", check: "F6", line: "101-106", classification: "CONFIRMATORY-NEGATIVE", implication: "Only new order is PSU (BSNL Rs264cr); reinforces ~96% govt concentration; 'Advance Work Order' is pre-firm"}
  - {id: "FND-06", check: "F7", line: "91-92", classification: "FORWARD-SIGNAL", implication: "C&I 'under evaluation' hedge; no near-term C&I revenue; ask commercial launch window"}
  - {id: "FND-07", check: "F16", line: "76", classification: "AMBIGUOUS", implication: "EBITDA margin -630bps YoY (rev +51.3% vs EBITDA +7.5%), multi-period downtrend; filing shows mix shift to materials-heavy BESS mfg + 732mn inventory build; ask if 15.5% is structural"}
  - {id: "FND-08", check: "F16", line: "78", classification: "CONFIRMATORY-NEGATIVE", implication: "PAT margin -360bps; 'PAT up 14.3%' is volume-only, masks profitability decline"}
  - {id: "FND-09", check: "F16", line: "n/a-omission", classification: "CONFIRMATORY-NEGATIVE", implication: "Silent on Q1 FY27 CFO (binding EXIT gate), receivables, inventory, customer mix, segment revenue, ROCE; CFO gate unresolved by this doc"}
  - {id: "FND-10", check: "F16", line: "n/a-omission", classification: "CONFIRMATORY-NEGATIVE", implication: "EPS omitted; filing shows basic EPS fell 3.03->2.84 YoY on IPO dilution while PAT rose"}
  - {id: "FND-11", check: "F16", line: "60,83,99,151", classification: "AMBIGUOUS", implication: "Order book stated as of Aug 05 2026 (post quarter-end) vs June-30 P&L; 'executable' undefined; ask June-30 figure and definition"}
  - {id: "FND-12", check: "F16", line: "75-76", classification: "NEUTRAL-FACT", implication: "EBITDA/margins non-GAAP with no filing line item; re-derived and tie (EBITDA excludes other income); transparency gap, no misstatement"}
  - {id: "FND-13", check: "F2", line: "60,74", classification: "NEUTRAL-FACT", implication: ">50% of consolidated revenue is subsidiary-sourced (standalone 264.2 vs consol 555.4cr); BESS growth story sits in subsidiaries; release consolidated-only"}
  - {id: "FND-14", check: "F16", line: "61", classification: "NEUTRAL-FACT", implication: "Headline PAT 62.5cr includes NCI; owners' PAT 61.3cr"}
forward_signals: ["FND-01", "FND-02", "FND-03", "FND-06"]
ambiguous: ["FND-04", "FND-07", "FND-11"]
commitments:
  - {commitment: "Operationalize additional 2.5 GWh BESS platform -> 5 GWh total", implied_date: "subsequent to quarter, by Aug 05 2026", ref: "L84-86", status_word: "completed"}
  - {commitment: "Commission additional 2.5 GWh BESS line -> 5 GWh installed", implied_date: "subsequent to quarter, by Aug 05 2026", ref: "L113-115,157-158", status_word: "completed"}
  - {commitment: "Commission in-house container fabrication facility", implied_date: "Q2 FY27 (Notion trigger #4)", ref: "L118", status_word: "underway"}
  - {commitment: "Phased expansion BESS capacity 5 GWh -> 10 GWh", implied_date: "undated", ref: "L117-119,158-159", status_word: "underway"}
  - {commitment: "C&I energy storage prototype -> commercial deployment", implied_date: "undated", ref: "L91-92", status_word: "initiated"}
  - {commitment: "NEC XON OEM partnership (Africa go-to-market)", implied_date: "during/around quarter", ref: "L123-127", status_word: "completed"}
  - {commitment: "MEGMEET strategic cooperation (AIDC) + Pace-Lineage R&D Center Pune", implied_date: "following quarter-end", ref: "L129-135", status_word: "completed"}
gate_a3: pass
blank_checks: []
```
