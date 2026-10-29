# A3 FORENSIC NOTES: CORRECTION LOOP 1 ADDENDUM (concall + press release, new rows only)
Company: Dynamic Cables Limited (DYCL) | Quarter: q2fy27 | Model: claude-opus-5-5
Scope: six ledger rows added by A2 in correction loop 1, all MISSING_FROM_STRUCTURED.
Base files stand unchanged: work/forensics_concall_dycl_q2fy27.md (A3-01 to A3-15),
work/forensics_pressrelease_dycl_q2fy27.md (A3-01 to A3-13). New IDs continue as CC-A3-16 on
and PR-A3-14 on.

Inputs read: concall fulltext L025-L058 and L381-L390 (context); press release fulltext lines
103-134; results fulltext lines 200-238 (balance sheet) and 470-514 (cash flow); results
structured R017-R022, R061-R064, R107-R112, R290-R299, R320-R321. Nothing under inputs/ opened.
Units: results filing in Rs lakhs; press release in Rs crore.

Source tier: the concall is a machine (ASR) transcript (L001). Every concall quote is
management tier and unverified. Filed numbers come from the H1 results filing.

## 1. ROW RECONCILIATION (6 of 6 read verbatim = 100%)

Row | Ledger | Line | Verbatim at line (A1 fulltext) | Matches ledger text | Status
--- | --- | --- | --- | --- | ---
M06 | concall s.8 | L030-L032 | "We have continued to build our industry demand," / "discipline and execution," / "and our focus on operational efficiency." | yes (ASR garble in "build our industry demand") | FINDING CC-A3-17
M07 | concall s.8 | L033-L034 | "Our performance reflects the resilience of our business" / "and our ability to navigate a dynamic operating environment." | yes | READ, PASS (no figure, no lexicon hit, no testable claim)
M08 | concall s.8 | L044-L047 | "We continue to focus on expanding our market reach," / "strengthening customer relationships" / "and capitalizing on emerging opportunities" / "across the domestic and international markets." | yes | FINDING CC-A3-18
M09 | concall s.8 | L050-L051 | "Commodity, price, volatility, and geopolitical developments" / "continue to influence the business environment." | yes (ASR commas) | FINDING CC-A3-19
M10 (MATERIAL) | concall s.8 | L052-L054 | "Our emphasis remains on disciplined execution," / "prudent working capital management," / "and operational excellence." | yes | FINDING CC-A3-16
M3 | press release | lines 108-110 | "We have always" (end of 108) / "followed disciplined approach towards execution, expanding our market reach and strengthening our" (109) / "position as a trusted partner of evolving Indian power landscape." (110) | yes | FINDING PR-A3-14

## 2. M10 TEST: "prudent working capital management" against the H1 filing

Filed item (Rs lakhs) | 30-Sep-2026 / H1 FY27 | 31-Mar-2026 / H1 FY26 | Change | Cite
--- | --- | --- | --- | ---
Inventories | 24,343.32 | 17,278.62 | +7,064.70 (+40.9%) | results line 209 (R017, R018)
Trade receivables | 27,443.56 | 28,788.07 | -1,344.51 (-4.7%) | line 211 (R021, R022)
Trade payables (MSE + others) | 16,819.51 | 15,936.20 | +883.31 (+5.5%) | lines 231-232 (R061-R064)
Net trade working capital (inv + rec - pay) | 34,967.37 | 30,130.49 | +4,836.88 (+16.1%) | derived from lines 209, 211, 231-232
CF: increase in inventories, H1 | (7,064.70) | (479.12) | 14.7x the prior-year H1 build | line 480 (R290, R291)
CF: trade receivables, H1 | 1,391.64 | (52.03) | release in FY27 | line 481 (R292, R293)
CF: trade payables, H1 | 880.58 | (3,581.90) | inflow in FY27 | line 484 (R298, R299)
CF: total working capital changes, H1 | (5,381.98) | (2,855.94) | 70.3% of pre-WC operating profit vs 48.2% | lines 479, 492
Net cash from operating activities, H1 | 666.37 | 2,018.63 | -67.0% YoY | line 495 (R320, R321)
P&L: change in FG/WIP/stock-in-trade, H1 | (4,974.34) | (2,880.86) | FG/WIP build 148% of full FY26 (3,366.75) | line 334 (R110-R112)

Reading. The claim holds on receivables: they fell 4.7% while H1 revenue rose 31% YoY
(press release line 114, 712.3 vs 543.6 Cr), and the release states ~59 receivable days
(line 129). The claim fails on inventory: stock rose Rs 70.6 Cr (40.9%) in six months, and the
build alone took 92% of pre-WC operating profit (7,064.70 / 7,653.45). OCF fell to 666.37 lakhs,
9.0% of H1 EBITDA against 34.9% a year earlier (results forensics A3-10).

Management's own explanation does not cover the size. At L386-L387 the call says "September
inventory is typically a little higher than the annual inventory because we are H2 heavy".
The same H2 seasonality applied in H1 FY26, when the inventory build was only 479.12 lakhs
(line 480). Seasonality explains a build of that order, not one 14.7 times larger. The second
reason given, at L389, "the value of the material has also increased", is a price effect and
is unquantified. At L385 the call says "in number of days ... the inventory has not increased
very significantly"; results forensics A3-10 computes 76.1 days against 65.4 (+10.7 days).

Funding consequence (already recorded, results A3-11, not re-counted here): mutual fund
investments fell from 3,062.04 to 92.85 (line 210; redemption 2,834.58 at line 503) to fund
capex of 1,952.11 (line 496) and the WC build. The treasury buffer is used up.

## 3. FINDINGS TABLE

id | check | ledger row | line | short verbatim quote | classification | forward implication
--- | --- | --- | --- | --- | --- | ---
CC-A3-16 | F17 (narrative vs filing) | M10 (MATERIAL) | concall L052-L054; vs results lines 209, 211, 231-232, 334, 480, 484, 492, 495; concall L385-L389 | "Our emphasis remains on disciplined execution, prudent working capital management" | FORWARD-SIGNAL | Filed H1 contradicts the claim on inventory and OCF. Inventory +40.9% (+7,064.70 L), 14.7x the H1 FY26 build under the same stated seasonality; OCF 666.37 vs 2,018.63 (-67%); WC absorbed 70.3% of pre-WC operating profit. Receivables (-4.7%) support the claim. Two readings: (a) pre-stocking for the H2 plant start and H2-heavy dispatch, which unwinds by March 2027; (b) slower offtake or FG awaiting dispatch, bought at high metal prices while metal dips (L317, base A3-10), which means an H2 inventory loss and a weak FY27 OCF. Separating observation: inventory and OCF at Q3 and at the FY27 balance sheet. MANAGEMENT QUESTION flagged.
CC-A3-17 | F17 (narrative vs filing) | M06; M10 tail | concall L032, L054; vs press release line 116 | "and our focus on operational efficiency." / "and operational excellence." | NEUTRAL-FACT | Efficiency claim stands beside the lowest operating margin in the release table: Q2 FY27 10.0% vs Q1 10.9% and Q2 FY26 11.0% (line 116). No new question. It folds into base concall A3-04 and press release A3-05, which already ask the cause of the margin decline. Do not count this as a second margin debit. ASR garble at L030 ("build our industry demand"); do not read a demand claim into it.
CC-A3-18 | F6 (forward commitment) | M08 | concall L044-L047; vs press release lines 114, 131 | "We continue to focus on expanding our market reach" ... "across the domestic and international markets." | NEUTRAL-FACT | Undated, unquantified intent. Baseline for "international": exports ~56 Cr in H1 (line 131), 7.9% of H1 operating revenue 712.3 Cr (line 114). The export forward question sits in base A3-08 (exports conditional on macros, near term hard to predict). Logged in the commitment register as initiated. Role 5 tests it on the export share in H2.
CC-A3-19 | F7 (hedge / qualifier) | M09 | concall L050-L051; vs press release line 108 | "Commodity, price, volatility, and geopolitical developments" / "continue to influence the business environment." | NEUTRAL-FACT | Same speaker, two framings: the call says these factors "continue to influence"; the release says the environment "has improved despite crude price volatility and geo political disruptions" (line 108). The release names crude (polymer inputs); the call names commodity broadly (metal included). No new question. Commodity risk to H2 margin and inventory value is already open in base A3-04 (10-20% fixed-price exposure) and A3-10 (high-cost September stock).
PR-A3-14 | F17 (narrative vs filing) | M3 | press release lines 108-110; vs lines 129, 116; results lines 209, 495 | "We have always followed disciplined approach towards execution, expanding our market reach" | NEUTRAL-FACT | Scripted qualifier. The same words appear on the call at L044 and L052, so the claim is the house line, not a quarter-specific statement. "Always" is a historical claim and this document cannot test it. The release supports it with receivable days (~59, line 129) and leaves out the inventory build and the OCF fall (results lines 209, 495). That selective disclosure is already base press release A3-12 (AMBIGUOUS). The test of "disciplined execution" on working capital is CC-A3-16; one question covers both.

## 4. MANAGEMENT QUESTION (flag for A4)
From CC-A3-16 (PR-A3-14 routes here):
"H1 FY27 inventory rose Rs 70.6 Cr, or 40.9%, to Rs 243.4 Cr. In H1 FY26 the build was
Rs 4.8 Cr under the same H2-heavy seasonality. Operating cash flow fell to Rs 6.7 Cr from
Rs 20.2 Cr. Please split the build into metal-price effect, pre-stock for the new plant, and
finished goods awaiting dispatch. What inventory days and operating cash flow do you target at
31 March 2027? With the mutual fund buffer now at Rs 0.9 Cr, how will H2 working capital and
capex be funded?"

## 5. CHECKLIST SCORECARD (loop-1 scope; base-file statuses stand for everything else)

Check | Status (new rows) | Basis
--- | --- | ---
F1 | N.A. | No new row is a zero-standing line item; results base file governs
F2 | N.A. | No new row touches S-vs-C; base file governs
F3 | N.A. | Same
F4 | N.A. | Same
F5 | N.A. | Same
F6 | FINDING | CC-A3-18 (M08 undated market-reach commitment); M10 logged as an ongoing claim
F7 | FINDING | CC-A3-19 (M09 commodity / geopolitical qualifier vs release line 108)
F8 | N.A. | No new row touches tax
F9 | N.A. | No new row touches OCI
F10 | N.A. | No new row touches share count
F11 | N.A. | No new row touches net worth
F12 | N.A. | No new row touches segments
F13 | N.A. | No new row touches board outcomes
F14 | N.A. | No new row touches note drafting
F15 | N.A. | No new row touches the entity list
F16 | N.A. | No new row is a deck metric; release selective disclosure stays in base PR A3-12
F17 | FINDING | CC-A3-16 (M10 vs H1 filing), CC-A3-17 (M06), PR-A3-14 (M3)

## 6. COMMITMENT REGISTER (additions)

commitment | implied date | ref | status word
--- | --- | --- | ---
Expand market reach, strengthen customer relationships, capture opportunities in domestic and international markets | undated | concall T03 L044-L047 | initiated
Emphasis on disciplined execution, prudent working capital management, operational excellence | ongoing; testable at the 31-Mar-2027 balance sheet | concall T03 L052-L054 | underway (H1 filing contradicts on inventory and OCF)
Disciplined approach towards execution, expanding market reach (historical claim, "always") | not dated | press release lines 108-110 | underway

```yaml
stage: A3-forensics
company: "DYCL"
quarter: "q2fy27"
doctype: "concall + pressrelease (correction loop 1, new rows only)"
model: "claude-opus-5-5"
status: complete
forensics_path: "runs/dycl-q2fy27/work/forensics_loop1_addendum_dycl_q2fy27.md"
loop: 1
rows_reviewed:
  - {row: "concall M06", line: "L030-L032", status: "FINDING CC-A3-17"}
  - {row: "concall M07", line: "L033-L034", status: "PASS (read, no finding)"}
  - {row: "concall M08", line: "L044-L047", status: "FINDING CC-A3-18"}
  - {row: "concall M09", line: "L050-L051", status: "FINDING CC-A3-19"}
  - {row: "concall M10 (MATERIAL)", line: "L052-L054", status: "FINDING CC-A3-16"}
  - {row: "pressrelease M3", line: "108-110", status: "FINDING PR-A3-14"}
ledger_reconciled_pct: 100        # 6 of 6 new rows read verbatim
checklist:                        # loop-1 scope; base-file statuses stand
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
  F14: N.A.
  F15: N.A.
  F16: N.A.
  F17: FINDING
findings:
  - {id: "CC-A3-16", check: "F17", line: "concall L052-L054; results 209, 211, 231-232, 334, 480, 484, 492, 495; concall L385-L389", classification: "FORWARD-SIGNAL", implication: "'Prudent working capital management' contradicted on inventory and OCF: inventory +40.9% (+7,064.70 L), 14.7x the H1 FY26 build (479.12) under the same stated seasonality; OCF 666.37 vs 2,018.63 (-67%); WC took 70.3% of pre-WC operating profit. Receivables -4.7% support the claim. Pre-stock for H2 plant vs slow offtake at high metal cost; Q3 and FY27 inventory and OCF separate them. Management question flagged."}
  - {id: "CC-A3-17", check: "F17", line: "concall L032, L054; pressrelease 116", classification: "NEUTRAL-FACT", implication: "Operational efficiency/excellence claim beside Q2 OPM 10.0% (lowest of 10.9% Q1, 11.0% Q2 FY26); folds into base CC A3-04 and PR A3-05; no second margin debit; ASR garble at L030"}
  - {id: "CC-A3-18", check: "F6", line: "concall L044-L047; pressrelease 114, 131", classification: "NEUTRAL-FACT", implication: "Undated market-reach intent; export baseline ~56 Cr = 7.9% of H1 revenue 712.3 Cr; forward question already in base CC A3-08"}
  - {id: "CC-A3-19", check: "F7", line: "concall L050-L051; pressrelease 108", classification: "NEUTRAL-FACT", implication: "Call says commodity/geopolitics 'continue to influence'; release says environment 'has improved despite' crude volatility; commodity risk to H2 already open in base CC A3-04 and A3-10"}
  - {id: "PR-A3-14", check: "F17", line: "pressrelease 108-110; 129; results 209, 495", classification: "NEUTRAL-FACT", implication: "Scripted 'disciplined execution' line mirrored at concall L044/L052; release cites receivable days ~59 and omits the inventory build and OCF fall (base PR A3-12); WC test routes to CC-A3-16 question"}
forward_signals: ["CC-A3-16"]
ambiguous: []
management_questions:
  - {from: "CC-A3-16 (PR-A3-14 routes here)", question: "H1 inventory rose Rs 70.6 Cr (40.9%) vs Rs 4.8 Cr in H1 FY26 under the same H2 seasonality; OCF fell to Rs 6.7 Cr from Rs 20.2 Cr. Split the build into metal price, new-plant pre-stock and FG awaiting dispatch. Target inventory days and OCF at 31-Mar-2027? With MF buffer at Rs 0.9 Cr, how are H2 WC and capex funded?"}
commitments:
  - {commitment: "Expand market reach and customer relationships, domestic and international", implied_date: "undated", ref: "concall T03 L044-L047", status_word: "initiated"}
  - {commitment: "Disciplined execution, prudent working capital management, operational excellence", implied_date: "ongoing; test 31-Mar-2027 balance sheet", ref: "concall T03 L052-L054", status_word: "underway"}
  - {commitment: "Disciplined approach towards execution, expanding market reach (historical 'always')", implied_date: "not dated", ref: "pressrelease lines 108-110", status_word: "underway"}
gate_a3: pass
blank_checks: []
analyst_note: "Only M10 carries new forensic weight. The working-capital claim is half true: receivables fell while revenue grew 31%, so collection discipline is real. Inventory is the problem. Management's own reason, H2-heavy seasonality (L386-L387), was present in H1 FY26 too, when the build was 479.12 lakhs against 7,064.70 now. Seasonality cannot carry a build 14.7 times larger. What remains is metal price (L389, unquantified), pre-stock for the new plant, or slow offtake. The bear reading matters because metal is now dipping (base A3-10): high-cost stock then meets lower realisations in H2. The funding side is in results A3-11 and is not counted again. M06, M08, M09 and PR M3 are scripted lines repeated across the call and the release; each folds into an existing base finding. They add no new question, so no improvement or debit is counted twice. All concall quotes are ASR, management tier, unverified; every number used here comes from the filed H1 results."
```
