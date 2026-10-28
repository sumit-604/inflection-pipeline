# A3 FORENSIC NOTES: WEWORK q2fy27, doctype presentation (file tag press; 5-page media release)

Company: WeWork India Management Ltd (WEWORK). Quarter: Q2 FY27 (quarter and half year ended 30-Sep-2026).
Inputs read: A1 structured extraction (runs/wework-q2fy27/extracted/wework-press-q2fy27-structured.md), A1 fulltext (runs/wework-q2fy27/extracted/wework-press-q2fy27-fulltext.md), A2 ledger (runs/wework-q2fy27/work/ledger_press_wework_q2fy27.md). Source PDF and inputs/ not opened.
Prior-quarter fulltext: none (first quarterly review of this name). Quarter-on-quarter document diffs are untestable.
Notion checklist: none (pre-thesis). F17 runs against the operator batch watch list.
Line numbers below are fulltext file lines. "Derived" means arithmetic on stated figures in this release only; no outside number is used, and nothing missing is estimated.

## 0. LEDGER RECONCILIATION

- Ledger rows: 197 (R001-R197). Rows read at cited fulltext line: 197. Reconciled: 100%.
- All 136 NUMBER values match the fulltext. All restatements (RESTATED flags) carry identical values across pages 2, 3 and 4. No value conflicts.
- A2's five LINE_ANCHOR_OFF rows confirmed. True lines: R005 line 70, R074 line 115, R088 line 136, R116 line 150, R118 line 151.
- Anchor defects A2 did not flag (values correct, location wrong):
  - R168 (safe harbour forward-looking statement): A1 says page 4 line 201. True location page 5, line 226 ("This Release may include forward-looking statements"). Line 201 is the FY26 listing sentence.
  - R197 (third-party projections not endorsed): A1 says page 4 line 207. True location page 5, lines 232-234. Line 207 is "Company Secretary & Compliance Officer".
  - Minor: R137/R138 exchange names at line 33 (A1 says 32); R143 "CBRE" at line 116 (A1 says 114, sentence start); R179 "last 12 months" at line 127 (A1 says 128).
- Internal arithmetic, tested: revenue, EBITDA and PAT QoQ and YoY growth, margins and bps changes, Q2 plus Q1 equals H1, desks (133.6k + 11.7k = 145.3k), members (113.4k + 8.3k = 121.7k), LTM 29.8k / 30.8k = 96.8% ("97%"). All tie within rounding except the FCFO QoQ rate (A3-10e).

### Derived quarter bridge (from stated growth rates; Rs Cr, IGAAP-equivalent)

| Metric | Q1 FY26 | Q2 FY26 | Q1 FY27 | Q2 FY27 (stated) | H1 FY26 | H1 FY27 (stated) |
|---|---|---|---|---|---|---|
| Revenue | 543.3 | 584.1 | 698.0 | 768.7 | 1,127.4 | 1,466.7 |
| EBITDA | 81.6 | 118.4 | 138.3 | 162.9 | 200.0 | 301.2 |
| EBITDA margin | 15.0% | 20.3% | 19.8% | 21.2% | 17.7% | 20.5% |
| PAT | 8.4 | 39.3 | 53.2 | 65.8 | 47.7 | 119.0 |
| FCFO | NOT FOUND | 95.4 | 142.1 | 237.7 | 148.0 | 379.8 |
| FCFF | NOT FOUND | -14.1 | -46.1 | 61.9 | NOT FOUND | 15.8 (derived) |
| Members (k) | NOT FOUND | 91.9 | 113.4 | 121.7 | | |
| Operational desks (k) | NOT FOUND | 114.5 | 133.6 | 145.3 | | |
| Members / desks | NOT FOUND | 80.3% | 84.9% | 83.8% (stated portfolio occupancy 83.7%) | | |

## 1. FINDINGS TABLE

| id | check | ledger row ref | line | short verbatim quote | classification | forward implication |
|---|---|---|---|---|---|---|
| A3-01 | F16 | R184, R185, R154 | 191-194 | "presented on an IGAAP-equivalent basis ... without the benefit of non-cash rent straight-lining under IndAS 116, and are net of ESOP costs. A detailed IndAS to IGAAP-equivalent reconciliation is included in the investor presentation" | AMBIGUOUS | Every number in the release (revenue, EBITDA, PAT, FCFO, FCFF, ROCE, net cash) sits on a non-statutory basis. No Ind AS figure appears. The release does not show lease liabilities, rent, or right-of-use assets. "Net of ESOP costs" has two readings: ESOP expense deducted, or ESOP expense excluded. A4: take the Ind AS-to-IGAAP bridge from the deck forensics. Ask which reading of "net of ESOP costs" applies. Ask whether the bridge items are the same as last quarter's. |
| A3-02 | F16 | R072, R071, R014, R009, R046, R016, R085, R049 | 105; 74-75; 129; 90 | "portfolio occupancy stood at 83.7%"; "member growth outpaces capacity growth YoY"; "nearly one new member for every desk added" | FORWARD-SIGNAL | Almost every metric in the release has a QoQ comparator. Portfolio occupancy has none, and mature occupancy "improved" has no prior figure. Members over desks tracks the stated occupancy within 0.1 pp. On that proxy, occupancy fell from about 84.9% to 83.8% QoQ (about -110 bps). Q2 alone absorbed 8.3k members against 11.7k desks, or 71%. The release shows the 97% LTM figure instead. Capacity grew 8.8% QoQ and members grew 7.3% QoQ; the headline uses the YoY comparison. Another 4.5k desks opened in early October (149.8k desks). Holding 83.7% then needs about 125.4k members, or +3.7k before any gain. Q3 portfolio occupancy dilution is the base reading. A4: ask for Q1 FY27 portfolio and mature occupancy, and occupancy by centre vintage. |
| A3-03 | F16 | R194, R054, R055, R129, R050 | 146; 148-149 | "fully funding its first-half capital expenditure through operating cash flows"; "improved by +76.0 Cr YoY to 61.9 Cr (+108.0 Cr QoQ), turning positive" | FORWARD-SIGNAL | The release states no capex amount (NOT FOUND). Derived Q1 FY27 FCFF is -46.1 Cr (61.9 - 108.0), so Q1 alone was not self-funded. H1 FCFF is about +15.8 Cr. If FCFF = FCFO - capex (formula not stated, R196), H1 capex is about 364 Cr against 379.8 Cr FCFO, a 4% cushion. The H1 claim rests on one quarter where FCFO was 1.46x EBITDA. With more openings coming (4.5k desks in October, a 3.2 mn sq ft pipeline), H2 self-funding is not assured. A4: ask for H1 capex, the FCFF formula, and H2 capex guidance. |
| A3-04 | F16 | R053, R109, R196, R050 | 92-93; 147-148 | "Free Cash Flow from Operations stood at 237.7 Cr ... representing 1.5x EBITDA conversion" | AMBIGUOUS | FCFO exceeds EBITDA by 74.8 Cr in Q2. Derived Q1 conversion was about 1.03x (142.1 / 138.3). The release defines neither FCFO nor the conversion ratio. Bull reading: a timing gain from member security deposits and advances on 11.7k new desks. Bear reading: a working-capital release that reverses when openings slow. The two readings separate on the Q2 FCFO bridge (EBITDA, working capital, member deposits, landlord deposits, tax). Also ask whether "Free" FCFO is after maintenance capex. |
| A3-05 | F16 | R116, R117, R180, R060, R145 | 150-151 | "moved to a net cash position of 23.1 Cr, from net debt of 310.5 Cr a year ago" | AMBIGUOUS | The swing is 333.6 Cr. Derived H1 FY27 FCFF of about 15.8 Cr explains about 5% of it. The release gives no net debt at 31-Mar-2026, no gross debt and no cash (NOT FOUND), so the source of the swing is not stated. Under the IGAAP-equivalent basis, net cash excludes Ind AS 116 lease liabilities. Cost of borrowing of 8.5% implies gross debt exists. A4: ask for the gross debt and cash split, the 31-Mar-2026 net debt, the source of the deleveraging (operating, equity or other), and lease liabilities on the Ind AS balance sheet. |
| A3-06 | F16 | R057, R058, R059, R113-R115 | 94; 149 | "ROCE improved to 34.5% (+590 bps QoQ; +1,235 bps YoY)" | AMBIGUOUS | Derived prior values: 28.6% in Q1 FY27 and 22.2% in Q2 FY26. A 590 bps one-quarter rise came during record capex. That points to an annualised single-quarter numerator or a capital-employed base that nets off cash or excludes right-of-use assets. The release states no formula. A4: ask for the ROCE formula and its numerator period, and whether lease assets and liabilities are in capital employed. |
| A3-07 | F16 | R013, R041, R125, R039, R123, R027, R096 | 75; 84-86; 81 | "PAT rising 149.5%"; "margins expanding to 20.5% (+279 bps)"; "+92 bps YoY" | FORWARD-SIGNAL | The H1 headline growth comes mostly from a low Q1 FY26 base: derived PAT 8.4 Cr and EBITDA margin about 15.0%, against 20.3% in Q2 FY26. YoY EBITDA margin expansion slowed from about +480 bps in Q1 FY27 to +92 bps in Q2 FY27. Revenue growth rose (Q1 YoY about 28.5%, Q2 31.6%). The base effect is now spent, so H2 FY27 YoY margin gains should be small. Use the Q2 YoY rates (+37.6% EBITDA, +67.4% PAT) as the run-rate, not the H1 rates. A4: ask what depressed Q1 FY26 PAT and margin. |
| A3-08 | F6 | R068, R069, R070, R087, R131, R189, R192, R159 | 103-104; 132-133; 185 | "a total committed footprint of 13.0 million sq. ft., including signed leases and LOIs" | AMBIGUOUS | Derived pipeline (committed minus operational): about 2.26 mn sq ft a year ago, 2.85 in Q1, 3.2 now. At the current 67 sq ft per desk, 3.2 mn sq ft is about 47k desks, or +33% capacity. The release does not split signed leases from non-binding LOIs and gives no opening dates. The pipeline size is soft. Its delivery drives capex and occupancy dilution (A3-02, A3-03). A4: ask for the signed vs LOI split, the opening schedule by quarter, and the LOI conversion history. |
| A3-09 | F14 | R061, R091, R144, R188 | 98; 137 | "GCCs contributed 40.8% of core revenue" | AMBIGUOUS | The release does not define "core revenue" or give its amount. Total revenue is 768.7 Cr. GCC concentration therefore cannot be stated on total revenue, and digital products (29.2 Cr, line 142) may sit outside the base. A4: ask for the core revenue definition and amount, and the GCC share of total revenue and its trend. |
| A3-10 | F14 | R186, R145, R132, R182, R050, R051, R129, R190 | 43; 95; 198; 92, 175; 74 | (a) "Unaudited Standalone and Consolidated Financial Results"; (b) "the company's A+ credit rating"; (c) "largest operator by total revenue for the past three fiscal years"; (e) "237.7 Cr (+67.5% QoQ" with "379.8 Cr during H1 FY27"; (f) "the largest half-year of openings in the company's history" | NEUTRAL-FACT | Drafting gaps, each small. (a) The cover letter cites standalone and consolidated results. The body never says which set its figures come from. (b) The rating agency and instrument are not named. (c) The leadership claim has no source; the CBRE claim at line 116 has one. (e) H1 minus Q2 gives Q1 FCFO of 142.0-142.2 Cr, which implies 67.1-67.4% QoQ. The stated 67.5% falls outside rounding. The gap is about 0.2 Cr; it may mean a Q1 restatement. (f) The record claim gives no prior comparator. Together these are a minor governance data point. They need no management question, except (a) if the deck is also silent. |
| A3-11 | F17 | R184, R185, R194, R116, R071, R072 | 191-193; 146; 150; 104-105 | "without the benefit of non-cash rent straight-lining under IndAS 116"; "reconciliation is included in the investor presentation" | AMBIGUOUS | Silence audit against the batch watch list (table in Section 4). The release is silent on rent-to-revenue, Ind AS 116 lease liabilities, gross debt and cash, capex amount, and pipeline opening dates. Its basis note excludes the lease items by design. 1 consecutive quarter of silence (first review; prior untestable). This is not yet a confirmatory negative, because no deterioration is evidenced. A4 should take these items from the deck and letter forensics. If the deck is also silent, route them to management questions. |

## 2. CHECKLIST SCORECARD

| check | status | basis |
|---|---|---|
| F1 Zero-value standing items | N.A. | No financial tables. A2 ZERO_STANDING count is 0 (ledger section 10). |
| F2 Standalone vs consolidated | N.A. | The release gives one unlabelled set of figures. No S-vs-C split exists to decompose. The missing basis label is recorded at F14 (A3-10a). |
| F3 Shell-entity detection | N.A. | No cost lines and no entity-level statements in a media release. |
| F4 Unaudited contribution ratio | N.A. | No auditor report or Other Matters paragraph. The results are unaudited (lines 41, 43). |
| F5 Going concern / EoM scope | N.A. | No EoM or going-concern language, and no prior-quarter text to diff. |
| F6 Forward-commitment phrases | FINDING | Lexicon sweep: "will be" at line 154 (CEO market outlook, not a commitment) and line 217 (safe-harbour boilerplate). "completed" at line 125. No hits for expected to/by, is underway, commenc, intends to, proposes to, board has approved, subject to approval, or in the process of. Commitments come from narrative (register below). A3-08 covers the LOI-inclusive pipeline. |
| F7 Hedge phrases | PASS | The only lexicon contact is safe-harbour boilerplate at lines 226-230 ("could cause actual results ... to differ materially"). The body has no hedges. No prior release exists to test for newly added hedges. |
| F8 Tax forensics | N.A. | No tax, ETR or deferred-tax data in the release. |
| F9 OCI forensics | N.A. | No OCI data. |
| F10 Share count and dilution | N.A. | No EPS, share count or paid-up capital in the release. The ESOP basis wording is recorded at A3-01. |
| F11 Reserves / net worth tie-out | N.A. | The release states no net worth or other equity. The net cash figure is tested at F16 (A3-05). |
| F12 Segment forensics | N.A. | No segment assets or liabilities. The customer and product splits (GCC share, digital products) are tested at F14 (A3-09). |
| F13 Board outcome beyond results | N.A. | The cover letter forwards the media release only. No board items, AGM, appointments or enabling resolutions. |
| F14 Drafting inconsistencies | FINDING | A3-09 (core revenue undefined). A3-10 (basis label, unnamed rating agency, unsourced leadership claim, 0.2 Cr FCFO arithmetic gap, record claim with no comparator). |
| F15 Entity list diffs | N.A. | No consolidation list and no prior quarter. |
| F16 Dropped / reframed disclosures | FINDING | No prior release, so dropped-since-last-quarter is untestable. Reframing inside this document is testable: A3-01 basis, A3-02 occupancy without comparator, A3-03 capex claim, A3-04 FCFO, A3-05 net cash, A3-06 ROCE, A3-07 H1 base effect. |
| F17 Silence audit | FINDING | The doctype is a release, not a concall. The caller directed the audit against the batch watch list. Five items are silent, each for 1 quarter (A3-11; table in Section 4). |

## 3. COMMITMENT REGISTER (F6)

| commitment | implied date | ref | status word |
|---|---|---|---|
| 4.5k further desks operational | first week of October 2026 (Q3 FY27) | lines 90, 130-131; R049, R086, R157, R158 | completed (post-quarter). Q3 test: operational desks of at least 149.8k, net of closures |
| Total committed footprint 13.0 mn sq ft, signed leases plus LOIs; derived pipeline 3.2 mn sq ft above the 9.8 operational | undated | lines 103-104, 132-133, 185; R068, R159, R189 | initiated (no opening schedule; LOI share NOT FOUND) |
| "accelerates investments to support long-term growth" | undated, ongoing | lines 112-113; R164 | underway |
| H1 capex fully funded through operating cash flows | H1 FY27 (claim); H2 untested | line 146; R194 | completed for H1. Capex amount NOT FOUND |
| "continues to maintain a strong financial foundation for sustained expansion" | undated | lines 150-152; R163 | no status word (intent) |
| "largest half-year of capacity openings in its history" | H1 FY27 | line 125; R190 | completed (no comparator) |

## 4. SILENCE AUDIT TABLE (F17, against the operator batch watch list)

| watch item | addressed in release? | ref | consecutive quarters silent |
|---|---|---|---|
| Occupancy | Partly. Levels only (mature 87.7%, portfolio 83.7%). No prior figures. | lines 104-105 | 0 (comparator omission at A3-02) |
| Desks | Yes. Adds, total, QoQ, YoY, post-quarter adds. | lines 88-90 | 0 |
| Rent-to-revenue | No | none | 1 (first review) |
| Net debt | Partly. Net cash 23.1 Cr on the IGAAP-equivalent basis. Gross debt and cash NOT FOUND. | line 150 | 1 for the gross split |
| Lease liabilities (Ind AS 116) | No. Excluded by the basis note. | lines 191-192 | 1 (first review) |
| IGAAP-equivalent vs reported Ind AS | Basis disclosed. No Ind AS figure. Reconciliation in the deck only. | lines 191-194 | 1 for Ind AS figures in this document |
| F6: capex amount behind the funding claim | No | line 146 | 1 |
| F6: pipeline opening dates and LOI share | No | lines 103-104, 132 | 1 |

## 5. NOTES FOR A4

- Q&A conversion queue (FORWARD-SIGNAL plus AMBIGUOUS): A3-01, A3-02, A3-03, A3-04, A3-05, A3-06, A3-07, A3-08, A3-09, A3-11.
- Run A3-02 and A3-03 first. Q3 FY27 occupancy dilution and H2 self-funding are the two forward tests this release carries. Both turn on the pace of pipeline openings (A3-08).
- Cross-check A3-01, A3-05 and A3-06 against the deck forensics. The deck holds the Ind AS bridge (R185), so these questions may already be answered there.

```yaml
stage: A3-forensics
company: "WEWORK"
quarter: "q2fy27"
doctype: "presentation (press)"
model: "claude-opus-5-5"
status: complete
forensics_path: "runs/wework-q2fy27/work/forensics_press_wework_q2fy27.md"
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
  F10: N.A.
  F11: N.A.
  F12: N.A.
  F13: N.A.
  F14: FINDING
  F15: N.A.
  F16: FINDING
  F17: FINDING
findings:
  - {id: "A3-01", check: "F16", line: "191-194", classification: "AMBIGUOUS", implication: "All figures IGAAP-equivalent, Ind AS 116 excluded; no Ind AS number, lease liability or rent in release; 'net of ESOP costs' reads two ways; bridge only in deck"}
  - {id: "A3-02", check: "F16", line: "105; 74-75; 129; 90", classification: "FORWARD-SIGNAL", implication: "Portfolio occupancy given with no comparator; members/desks proxy fell ~84.9% to 83.8% QoQ; Q2 absorption 71% (8.3k/11.7k) vs 97% LTM framing; +4.5k Oct desks need +3.7k members to hold 83.7%; Q3 dilution base case"}
  - {id: "A3-03", check: "F16", line: "146; 148-149", classification: "FORWARD-SIGNAL", implication: "H1 capex self-funding rests on Q2: derived Q1 FCFF -46.1 Cr, H1 FCFF ~+15.8 Cr (4% cushion on 379.8 FCFO); capex amount NOT FOUND; H2 self-funding at risk as openings accelerate"}
  - {id: "A3-04", check: "F16", line: "92-93", classification: "AMBIGUOUS", implication: "FCFO 1.5x EBITDA (74.8 Cr excess) vs ~1.03x in Q1; formula undefined; deposit/working-capital timing gain that reverses vs durable; ask for Q2 FCFO bridge"}
  - {id: "A3-05", check: "F16", line: "150-151", classification: "AMBIGUOUS", implication: "333.6 Cr net debt swing; H1 FCFF explains ~5%; source, Mar-26 net debt, gross debt and cash NOT FOUND; net cash excludes lease liabilities"}
  - {id: "A3-06", check: "F16", line: "94", classification: "AMBIGUOUS", implication: "ROCE +590 bps QoQ during record capex; formula, numerator period and treatment of ROU assets/cash undefined"}
  - {id: "A3-07", check: "F16", line: "75; 84-86; 81", classification: "FORWARD-SIGNAL", implication: "H1 PAT +149.5% and +279 bps margin ride a weak Q1 FY26 base (derived PAT 8.4 Cr, margin ~15.0%); YoY margin expansion slowed ~+480 bps (Q1) to +92 bps (Q2); H2 YoY margin gains likely small"}
  - {id: "A3-08", check: "F6", line: "103-104; 132-133", classification: "AMBIGUOUS", implication: "Committed 13.0 mn sq ft includes non-binding LOIs; derived pipeline 3.2 mn sq ft (~47k desks, +33%), undated, LOI share NOT FOUND"}
  - {id: "A3-09", check: "F14", line: "98", classification: "AMBIGUOUS", implication: "GCC 40.8% of undefined 'core revenue'; concentration on total revenue not stateable"}
  - {id: "A3-10", check: "F14", line: "43; 95; 198; 92, 175; 74", classification: "NEUTRAL-FACT", implication: "S/C basis of release figures unstated; rating agency unnamed; leadership claim unsourced; FCFO QoQ 67.5% vs 67.1-67.4% implied by H1-Q2 (~0.2 Cr); record claim with no comparator"}
  - {id: "A3-11", check: "F17", line: "191-193; 146; 150", classification: "AMBIGUOUS", implication: "Silent on rent-to-revenue, lease liabilities, gross debt/cash, capex amount, pipeline dates; 1 quarter (first review); pull from deck forensics before routing to management"}
forward_signals: ["A3-02", "A3-03", "A3-07"]
ambiguous: ["A3-01", "A3-04", "A3-05", "A3-06", "A3-08", "A3-09", "A3-11"]
commitments:
  - {commitment: "4.5k further desks operational", implied_date: "first week Oct 2026", ref: "lines 90, 130-131", status_word: "completed"}
  - {commitment: "Committed footprint 13.0 mn sq ft incl signed leases and LOIs (pipeline ~3.2 mn sq ft)", implied_date: "undated", ref: "lines 103-104, 132-133, 185", status_word: "initiated"}
  - {commitment: "Accelerating investments for long-term growth", implied_date: "undated", ref: "lines 112-113", status_word: "underway"}
  - {commitment: "H1 capex fully funded by operating cash flows", implied_date: "H1 FY27; H2 untested", ref: "line 146", status_word: "completed"}
  - {commitment: "Largest half-year of capacity openings", implied_date: "H1 FY27", ref: "line 125", status_word: "completed"}
gate_a3: pass
blank_checks: []
analyst_note: "Five-page release; statement checks N.A. Value sits in wording versus arithmetic. The release attaches QoQ comparators to almost every metric except portfolio occupancy, the one that fell (members/desks proxy matches stated 83.7% within 0.1 pp and implies about -110 bps QoQ). The headline picks YoY member versus capacity growth because QoQ ran the other way (desks +8.8%, members +7.3%). The capex self-funding claim and FCFF turning positive both depend on a single quarter of FCFO at 1.46x EBITDA, after a Q1 with derived FCFF of -46.1 Cr. That makes Q3 the test: 4.5k October desks plus a 3.2 mn sq ft LOI-inclusive pipeline press occupancy and cash at once. Derived capex assumes FCFF = FCFO minus capex; formula unstated, so capex stays NOT FOUND. H1 growth rates ride a weak Q1 FY26 base; use Q2 YoY. Pipeline note: A1 anchors R168 and R197 point to page 4 lines 201/207; true location page 5 lines 226 and 232-234. A2 did not flag these; values unaffected."
```
