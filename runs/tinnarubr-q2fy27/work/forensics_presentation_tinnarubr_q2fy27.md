# A3 FORENSIC NOTES, TINNARUBR Q2 FY27, doctype: presentation (press release dated 22-Oct-2026, 3 pages, page 1 covering letter)

Agent: A3 forensics | model: claude-opus-5-5 | date: 2026-10-23
Inputs read: extracted/tinnarubr-presentation-q2fy27-structured.md (R001-R138), extracted/tinnarubr-presentation-q2fy27-fulltext.md (lines 1-144), work/ledger_presentation_tinnarubr_q2fy27.md. No source PDF and nothing under inputs/ was opened.
Prior-quarter fulltext: none (first run for this ticker). Notion checklist: none. PRE-THESIS READ.

## 0. LEDGER RECONCILIATION

Rows in ledger: 138 (R001-R138, orphan_ids none). Rows read verbatim at cited fulltext line: 138. Reconciled: 100%.

Non-material A1 cite drift found during the read (values are correct, the line or wording is slightly off). None changes a number.
| Row | A1 cite | Actual | Note |
|---|---|---|---|
| R019 | line 82 | line 83 | "Rs. 61 crore" sits on line 83; line 82 carries "standalone EBITDA exceeding" |
| R039 | line 99 | line 98 | "CARE A3+ for short-" is on line 98 |
| R091 | line 140 | line 141 | "South Africa." opens line 141 |
| R102 | line 130-131 | same | A1 quote is paraphrased; fulltext reads "Rising natural rubber prices and the industry's push for sustainable materials are further accelerating demand for recycled rubber." |
| R125 | line 37 | same | fulltext reads "half year ended on September 30, 2026"; A1 dropped "on" |
| header | "header 13 lines" | 16 lines | line numbers in the structured file still match the fulltext file's absolute lines |

Positional-pairing status of the KPI block (fulltext lines 72-74). The Q2 column (31% / 37% / 45%) is confirmed by the text at line 86. H1 EBITDA 50% is confirmed by the headline at line 65 (Q2 EBITDA is 37%, so 50% can only be H1). H1 revenue 25% (R008) and H1 PAT 60% (R014) rest on position only. Absolute rupee figures (313 / 157, 63 / 29, 38 / 17) sit next to their labels and are not positional.

## 1. FINDINGS TABLE

Derived figures are arithmetic on stated rounded Rs Cr values, shown with rounding bands. They are not estimates of missing numbers. A4 must confirm each against the quarterly columns of the results filing.

| id | check | ledger row ref | line | short verbatim quote | classification | forward implication |
|---|---|---|---|---|---|---|
| A3-01 | F16 | R007, R009, R013, R015, R017, R018, R006, R122 | 72, 74, 76, 65, 126 | "EBITDA   63 Cr ... EBITDA   29 Cr" (74); "powered by strong year-on-year growth in Q2" (126) | FORWARD-SIGNAL | The release reports YoY only. Derived Q1 FY27 = H1 minus Q2: revenue 156 Cr (band 155-157), EBITDA 34 Cr (33-35), PAT 21 Cr (20-22). Q2 EBITDA fell about 15% QoQ and PAT about 19% QoQ on flat revenue (157 vs 156). EBITDA margin moved from about 21.8% (Q1) to 18.5% (Q2), roughly 330 bps down; PAT margin from about 13.5% to 10.8%. Q1 made 54% of H1 EBITDA and 55% of H1 PAT. The "record H1" headline and the "powered by Q2" line lean on Q1. The Q2 exit run-rate is below the H1 average. A4 question: what drove the Q2 margin compression on flat QoQ revenue (waste-tyre input cost, mix toward Infrastructure, price, one-off)? |
| A3-02 | F16 | R008, R010, R011, R012, R014, R016, R023-R025 | 72-74, 86 | "Consolidated Q2FY27 revenue, EBITDA and PAT grew 31%, 37% and 45% YoY" (86) | AMBIGUOUS | Derived prior-year base (uses positional R008/R011/R014): H1 FY26 revenue about 250 Cr, EBITDA about 42 Cr, PAT about 24 Cr; Q2 FY26 about 120 / 21 / 12; Q1 FY26 about 131 / 21 / 12. Implied Q1 FY27 YoY: revenue about +19%, EBITDA about +63%, PAT about +75%. Q2 FY27 YoY: +31% / +37% / +45%. Revenue growth accelerated while profit growth decelerated: operating leverage reversed in Q2. Two readings: (a) seasonal monsoon-quarter dip, (b) structural margin step-down. Separating observation: in FY26, derived Q2 EBITDA margin (about 17.7%) was at or above Q1 (about 15.9%), so seasonality did not cut Q2 margin last year. That leans toward reading (b) until the results filing shows otherwise. A4 must verify the H1 YoY percentages against the filing because two of them are positional. |
| A3-03 | F16 | R037, R133, R038, R075, R045, R053, R028-R031 | 93-94, 98, 106, 116, 89 | "net debt-to-equity ratio improved to 0.32x IN H1FY27" (93-94); "CARE Ratings upgraded the Tinna's credit ratings to CARE BBB; Stable" (98) | AMBIGUOUS | Five claims carry no baseline. Net D/E "improved" with no FY26 figure. CARE "upgraded" with no prior rating and no action date. PCMB capacity "has expanded to 18,000 TPA" with no prior capacity and no date. Solar "savings of Rs. 2.37 Cr." with no period. Segment growth rates (38 / 19 / 11 / 8%) with no segment revenue amounts. A4 question: state the prior values and dates for each. |
| A3-04 | F2 | R013, R017, R019, R020, R021, R022, R130, R054-R056, R084 | 82-83, 74, 76, 118 | "standalone EBITDA exceeding Rs. 61 crore and PAT surpassing Rs. 36 crore" (82-83) | AMBIGUOUS | H1 consolidated minus standalone: EBITDA under about 2 Cr (upper bound about 2.5 Cr after rounding), PAT under about 2 Cr. Subsidiaries plus eliminations add 3-4% of consolidated EBITDA. Yet Oman ran at "90% capacity utilization" with "EBITDA margins improving to 11.5%" (118). If Oman alone filled the gap, its H1 revenue is at most about 22 Cr. Otherwise South Africa, the new Chile entity, or intra-group eliminations absorb Oman's EBITDA. Standalone revenue is not disclosed, so the gap cannot be split. Trend test needs a second period (not available on first run). A4 question: Oman H1 revenue and EBITDA; South Africa and Chile H1 result; elimination amount. |
| A3-05 | F6 | R096, R097, R040, R041, R115 | 101-103 | "will be commissioned by Q3 FY27" (101); "positioning the Company to become the world's largest producer of MRP" (102-103) | FORWARD-SIGNAL | Hard dated commitment: 3,500 MTPA MRP addition commissioned by 31-Dec-2026 (Q3 FY27). Derived existing MRP capacity: 20,000 minus 3,500 = 16,500 MTPA. Next quarter is the delivery test for the Role 5 tracker. "World's largest producer" is a capacity positioning claim with no source cited; capacity is not production. A4 question: current MRP utilisation, trial-run status, and the basis for the world's-largest claim. |
| A3-06 | F11 | R046, R047, R098, R048, R049, R099, R134, R033, R037, R132, R133 | 108-109, 92, 94 | "Completed Rs. 45 Cr. of capex in H1 FY27 against the planned Rs. 100 Cr. investment over FY27 - FY28" (108); "Plans to invest up to Rs. 250 crore over the next three years" (109) | FORWARD-SIGNAL | Capex stack: Rs 100 Cr plan (Rs 45 Cr done, Rs 55 Cr left over about 18 months) plus up to Rs 250 Cr Andhra over three years. The release does not say whether the Rs 100 Cr includes any Andhra spend. Balance sheet cross-check: debt Rs 111 Cr, net D/E 0.32x. Net debt is at most 111 Cr, so implied net worth is at most about Rs 347 Cr (equal only if cash is zero). The Andhra ceiling alone is at least 72% of that implied net worth. Funding source is not stated. Net debt basis is not defined (R133), and gross vs net debt for the Rs 111 Cr is not stated (R132). Statutory net worth is not in this document, so the tie-out stays open. A4 question: Andhra funding mix (accruals, debt, equity or warrants) and board approval status; tie net worth to the results-filing balance sheet. If equity is in the mix, F10 dilution watch opens. |
| A3-07 | F7 | R099, R100, R108, R101, R134, R138 | 109, 112, 141, 129 | "This facility is envisaged to be one of the largest" (112); "Future expansions are envisaged in Saudi Arabia and Chile" (141); "proposed mandates for modified bitumen" (129) | AMBIGUOUS | Zero hits on the F7 hedge lexicon, and no safe-harbour text anywhere (R138), although the release carries five-year targets. The hedging sits in soft verbs instead. The small item (MRP) is hard-dated. The large items (Andhra up to Rs 250 Cr, Saudi, Chile) carry "plans", "up to" and "envisaged", with no date, approval or land status. The policy tailwind rests on "proposed" mandates, which are not enacted. A4 question: Andhra land allotment or MoU status, board approval date, and the status of the bitumen mandate and EPR rules. |
| A3-08 | F6 | R057-R061, R103-R106, R123, R135, R026, R060 | 133-135, 86 | "growing at a CAGR of over 25%, while delivering profitability growth of over 33% CAGR, sustaining EBITDA margins above 18%" (133-134) | AMBIGUOUS | Internal tension. Profit compounding at more than 33% against revenue at more than 25% needs a profit margin about 20% higher in relative terms over three years. The EBITDA margin target is only "above 18%". That equals the Q2 FY27 print (18.5%, line 86) and sits below H1 (about 20.1%) and derived Q1 (about 21.8%). The expansion would then have to come below EBITDA, while up to Rs 350 Cr of capex raises depreciation and possibly interest. "Profitability" is not defined (R135). Base year is not stated. "Vision 2029" does not say FY29 or FY30. A ROCE above 30% has to hold during the capex. A4 question: define the profit metric, the base year and the end year; explain how ROCE stays above 30% through the Andhra build. |
| A3-09 | F14 | R062, R063, R107, R064, R090, R091, R092, R093, R082 | 135, 140-141, 109 | "as it expands its operations from 8 to 10 locations" (135); "Its current 8 plants in India and Oman ... it also operates in South Africa" (140-141) | AMBIGUOUS | Count does not reconcile. The target adds two locations. The release names three new sites (Andhra at line 109, Saudi Arabia and Chile at line 141). South Africa operates but appears to sit outside the "8 plants in India and Oman". A4 question: list the 8 current and 10 target locations, and say whether South Africa is a plant, a trading arm or a JV. |
| A3-10 | F14 | R032, R033, R034, R132, R133 | 92, 94 | "debt declining 9% to Rs. 111 Cr. from Rs. 121 Cr. in FY26" (92) | NEUTRAL-FACT | On the stated figures the fall is 8.3%. It rounds to 9% only if the unrounded values sit near the rounding edges (for example Rs 121.0 Cr to at most Rs 110.7 Cr). Debt fell by about Rs 10 Cr while Rs 45 Cr of capex was spent, so H1 capex was internally funded on the stated numbers. Minor drafting items: "IN H1FY27" (94), "the Tinna's credit ratings" (98), "Tinna Rubber And" (35) vs "Tinna Rubber and" (67). Each item is immaterial on its own. Together they form a governance data point. |
| A3-11 | F15 | R085, R086, R109, R091, R092, R093 | 121-122, 140-141 | "Established a wholly owned subsidiary, Tinna Rubber Chile SpA" (121) | FORWARD-SIGNAL | Entity addition. The release gives no incorporation date, capital commitment or consolidation status. The South Africa operation has no entity name or relationship (subsidiary, JV or branch). No prior consolidation list exists to diff (first run). A4 question: Chile SpA incorporation date, capital committed, whether a separate Reg 30 intimation was filed and when; South Africa entity structure and whether it is consolidated; Saudi entity status. |
| A3-12 | F16 | R042, R043, R044, R045, R077, R122 | 105-106, 127 | "PCMB revenue tripled to Rs. 27 Cr in H1FY27 from Rs. 8 Cr in H1FY26" (105) | FORWARD-SIGNAL | Derived: PCMB grew 3.4x and added about Rs 19 Cr. That is about 30% of the roughly Rs 63 Cr H1 consolidated revenue increase (H1 FY26 base is derived from positional R008). PCMB is about 8.6% of H1 revenue. Management cites "a growing share of high-value products" (127). Group margin still fell in Q2, so either PCMB margin is not high or something else compressed. PCMB's segment mapping and margin are not disclosed. A4 question: PCMB EBITDA margin, utilisation of 18,000 TPA, and which of the four segments carries PCMB. |
| A3-13 | F16 | R008, R011, R014, R016, R129, R137 | 70-74 | "H1 FY27 (YoY)                            Q2 FY27(YoY)" (70) | NEUTRAL-FACT | KPI-block percentages are paired by text-layer position. The release has no footnote markers (R137). Q2 percentages and H1 EBITDA 50% are independently confirmed (lines 86, 65). H1 revenue 25% and H1 PAT 60% are not. A3-02 and A3-12 depend on them. Pipeline note for A4: verify against the results filing before quoting. |

## 2. CHECKLIST SCORECARD

| Check | Status | Basis |
|---|---|---|
| F1 | N.A. | Press release has no financial-statement template; A2 zero_standing count 0. |
| F2 | FINDING | Deck carries both bases for H1; single-period decomposition shows subsidiaries add under about 2 Cr EBITDA / PAT despite Oman at 90% utilisation (A3-04). The 5 pp trend test is not runnable on one period. |
| F3 | N.A. | No cost lines in a press release. |
| F4 | N.A. | No auditor report or Other Matters paragraph. |
| F5 | N.A. | No going-concern or EoM text; no prior quarter to diff. |
| F6 | FINDING | Lexicon hits "will be commissioned" (101), "planned" (108), "Plans to invest" (109), "envisaged" (112, 141), Vision 2029 (133-135). Register below; A3-05, A3-08. |
| F7 | FINDING | Zero hedge-lexicon hits and no safe-harbour text; the hedging sits in soft verbs on the largest items (A3-07). |
| F8 | N.A. | No tax lines, PBT or ETR in the release. |
| F9 | N.A. | No OCI disclosure. |
| F10 | N.A. | Deck carries no share count, paid-up capital or EPS. Dilution watch opens only through A3-06 funding. |
| F11 | FINDING | Net D/E 0.32x with undefined net-debt basis implies net worth at most about Rs 347 Cr. No statutory figure here to tie to; funding of up to Rs 350 Cr capex is unstated (A3-06). |
| F12 | N.A. | No segment assets or liabilities; only segment YoY rates without amounts (logged under A3-03). |
| F13 | N.A. | Release carries no board outcome, AR approval, AGM or director items. The board meeting date and time are absent; the covering letter is signed 2026.10.22 15:49:27. |
| F14 | FINDING | Drafting inconsistencies inside the release: location count (A3-09), debt-decline arithmetic and typography (A3-10). Run on a presentation because the evidence exists; noted as a doctype departure. |
| F15 | FINDING | New entity Tinna Rubber Chile SpA; South Africa entity undefined (A3-11). No prior list to diff. |
| F16 | FINDING | No prior deck, so the dropped-metric diff is not assessable. Within-document reframing: YoY-only framing hides the QoQ decline (A3-01, A3-02), unbaselined claims (A3-03), PCMB attribution gap (A3-12), positional KPI pairing (A3-13). |
| F17 | N.A. | Not a concall; no Notion monitoring checklist exists (pre-thesis read, no companies/TINNARUBR.md). |

GATE A3: pass (17 of 17 marked, no blanks).

## 3. COMMITMENT REGISTER (from F6)

Status ladder used: planned (stated intent, no approval or start disclosed) < initiated < underway < completed. "planned" sits below the prompt's three words and is used where the release gives no start evidence.

| # | Commitment | Implied date | Ref | Status word |
|---|---|---|---|---|
| C1 | 3,500 MTPA MRP expansion commissioned | by 31-Dec-2026 (Q3 FY27) | line 101, R096/R115 | underway ("ongoing ... progressing as planned") |
| C2 | MRP capacity reaches 20,000 MTPA (from derived 16,500) | on C1 | line 102, R097/R041 | underway (contingent on C1) |
| C3 | Capex Rs 100 Cr over FY27-FY28; Rs 45 Cr done in H1 FY27 | by 31-Mar-2028 | line 108, R046/R047/R098 | underway (45% spent) |
| C4 | Andhra 40-acre integrated recycling facility (rubber, plastic, pyrolysis, rCB), up to Rs 250 Cr | "over the next three years", so by about Oct-2029 | line 109-113, R099/R100/R134 | planned (no approval, land or funding stated) |
| C5 | Vision 2029: revenue Rs 1,000 Cr, revenue CAGR over 25%, profitability CAGR over 33%, EBITDA margin above 18%, ROCE above 30% | 2029 (FY29 vs FY30 undefined; base year undefined) | lines 133-135, R103-R106 | planned (target) |
| C6 | Locations from 8 to 10 | 2029 | line 135, R107 | planned (target; count inconsistent, A3-09) |
| C7 | Expansions in Saudi Arabia and Chile | undated | line 141, R108 | planned ("envisaged") |
| C8 | Tinna Rubber Chile SpA established as a wholly owned subsidiary | date not stated | line 121, R085/R109 | completed (entity formed; operations not started on the evidence) |
| C9 | PCMB capacity expanded to 18,000 TPA | date not stated | line 106, R045 | completed |
| C10 | Renewable capacity raised from 1.23 MW to 4.48 MW | by H1 FY27 | line 116, R051/R052 | completed |
| C11 | CARE upgrade to BBB Stable / A3+ | action date not stated | line 98, R038/R039 | completed |

## 4. QUESTIONS FLAGGED FOR A4 (from FORWARD-SIGNAL and AMBIGUOUS findings)

A3-01, A3-02, A3-03, A3-04, A3-05, A3-06, A3-07, A3-08, A3-09, A3-11, A3-12. The question text is in each finding row. Priority order: A3-01 (Q2 margin compression), A3-06 (capex funding), A3-08 (Vision 2029 tension), A3-05 (MRP delivery test).

## 5. YAML BLOCK

```yaml
stage: A3-forensics
company: "TINNARUBR"
quarter: "Q2 FY27"
doctype: "presentation"
model: "claude-opus-5-5"
status: complete
forensics_path: "runs/tinnarubr-q2fy27/work/forensics_presentation_tinnarubr_q2fy27.md"
ledger_reconciled_pct: 100        # 138 rows read / 138 rows in ledger
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
  F10: N.A.
  F11: FINDING
  F12: N.A.
  F13: N.A.
  F14: FINDING
  F15: FINDING
  F16: FINDING
  F17: N.A.
findings:
  - {id: "A3-01", check: "F16", line: "72, 74, 76, 126", classification: "FORWARD-SIGNAL", implication: "Derived Q1 FY27 EBITDA 34 Cr / PAT 21 Cr vs Q2 29 / 17 on flat revenue (156 vs 157); EBITDA margin about 21.8% to 18.5%. YoY-only framing hides the QoQ fall; 'record H1' leans on Q1."}
  - {id: "A3-02", check: "F16", line: "72-74, 86", classification: "AMBIGUOUS", implication: "Implied Q1 FY27 YoY rev +19% / EBITDA +63% / PAT +75% vs Q2 +31/+37/+45: operating leverage reversed. FY26 Q2 margin was not seasonally lower than Q1, so lean structural until filing shows otherwise. Uses positional H1 %."}
  - {id: "A3-03", check: "F16", line: "89, 93-94, 98, 106, 116", classification: "AMBIGUOUS", implication: "Net D/E 'improved', CARE 'upgraded', PCMB capacity 'expanded', solar savings, segment growth all lack baseline or period."}
  - {id: "A3-04", check: "F2", line: "74, 76, 82-83, 118", classification: "AMBIGUOUS", implication: "Subsidiaries plus eliminations add under about 2 Cr H1 EBITDA/PAT despite Oman at 90% util and 11.5% margin; Oman H1 revenue at most about 22 Cr if it alone fills the gap, else other subs or eliminations absorb it."}
  - {id: "A3-05", check: "F6", line: "101-103", classification: "FORWARD-SIGNAL", implication: "Hard-dated MRP 3,500 MTPA commissioning by Q3 FY27 (derived base 16,500 MTPA); next-quarter delivery test. World's-largest claim unsourced."}
  - {id: "A3-06", check: "F11", line: "92, 94, 108, 109", classification: "FORWARD-SIGNAL", implication: "Up to Rs 350 Cr capex stack (55 Cr left on Rs 100 Cr plan plus up to 250 Cr Andhra) vs implied net worth at most about Rs 347 Cr; funding unstated; net-debt basis undefined; possible dilution watch."}
  - {id: "A3-07", check: "F7", line: "109, 112, 129, 141", classification: "AMBIGUOUS", implication: "No hedge-lexicon hits, no safe harbour; the largest items carry soft verbs ('up to', 'envisaged'), policy tailwind rests on 'proposed' mandates."}
  - {id: "A3-08", check: "F6", line: "86, 133-135", classification: "AMBIGUOUS", implication: "Profit CAGR over 33% vs revenue over 25% needs margin expansion, yet EBITDA floor 18% equals Q2 print; profit metric, base year, end year undefined; ROCE over 30% through capex."}
  - {id: "A3-09", check: "F14", line: "109, 135, 140-141", classification: "AMBIGUOUS", implication: "8 to 10 locations vs three named new sites (Andhra, Saudi, Chile) plus South Africa outside the 8."}
  - {id: "A3-10", check: "F14", line: "35, 67, 92, 94, 98", classification: "NEUTRAL-FACT", implication: "Debt 121 to 111 is 8.3%, stated 9% only at rounding edges; H1 capex internally funded; minor typography."}
  - {id: "A3-11", check: "F15", line: "121-122, 140-141", classification: "FORWARD-SIGNAL", implication: "New WOS Tinna Rubber Chile SpA: no date, capital or consolidation status; South Africa entity form undisclosed."}
  - {id: "A3-12", check: "F16", line: "105-106, 127", classification: "FORWARD-SIGNAL", implication: "PCMB 8 to 27 Cr adds about 30% of H1 revenue growth; margin and segment mapping undisclosed; 'high-value' mix claim sits against Q2 margin fall."}
  - {id: "A3-13", check: "F16", line: "70-74", classification: "NEUTRAL-FACT", implication: "H1 revenue 25% and H1 PAT 60% are positional only; verify against results filing before quoting."}
forward_signals: ["A3-01", "A3-05", "A3-06", "A3-11", "A3-12"]
ambiguous: ["A3-02", "A3-03", "A3-04", "A3-07", "A3-08", "A3-09"]
commitments:
  - {commitment: "3,500 MTPA MRP expansion commissioned", implied_date: "by 2026-12-31 (Q3 FY27)", ref: "line 101, R096", status_word: "underway"}
  - {commitment: "MRP capacity to 20,000 MTPA", implied_date: "on commissioning", ref: "line 102, R097", status_word: "underway"}
  - {commitment: "Capex Rs 100 Cr over FY27-FY28, Rs 45 Cr done H1", implied_date: "by 2028-03-31", ref: "line 108, R098", status_word: "underway"}
  - {commitment: "Andhra 40-acre integrated recycling facility, up to Rs 250 Cr", implied_date: "next three years, about 2029-10", ref: "line 109, R099", status_word: "planned"}
  - {commitment: "Vision 2029: Rs 1,000 Cr revenue, rev CAGR >25%, profit CAGR >33%, EBITDA margin >18%, ROCE >30%", implied_date: "2029 (FY undefined)", ref: "lines 133-135, R103-R106", status_word: "planned"}
  - {commitment: "Locations 8 to 10", implied_date: "2029", ref: "line 135, R107", status_word: "planned"}
  - {commitment: "Expansions in Saudi Arabia and Chile", implied_date: "undated", ref: "line 141, R108", status_word: "planned"}
  - {commitment: "Tinna Rubber Chile SpA WOS established", implied_date: "not stated", ref: "line 121, R085", status_word: "completed"}
  - {commitment: "PCMB capacity expanded to 18,000 TPA", implied_date: "not stated", ref: "line 106, R045", status_word: "completed"}
  - {commitment: "Renewable capacity 1.23 MW to 4.48 MW", implied_date: "by H1 FY27", ref: "line 116, R052", status_word: "completed"}
  - {commitment: "CARE upgrade to BBB Stable / A3+", implied_date: "not stated", ref: "line 98, R038", status_word: "completed"}
gate_a3: pass
blank_checks: []
token_use_estimate: "about 45k total (about 22k input read incl. prompt and three artifacts, about 23k reasoning and output)"
analyst_note: "The release reports YoY figures only. Subtracting Q2 from H1 shows Q2 EBITDA fell about 15% QoQ and margin fell about 330 bps on flat revenue. Q1 carried the 'record H1'. Management set its Vision 2029 EBITDA floor at 18%, exactly the Q2 print, while promising profit growth faster than revenue. That pairing is the central question for A4: is 18.5% the new run-rate, and what lifts profit faster than revenue through up to Rs 350 Cr of capex? The capex is large against an implied net worth of at most Rs 347 Cr, and its funding is unstated. MRP commissioning by Q3 FY27 is the one hard-dated item; it gives the next-quarter delivery test. The subsidiary gap (under Rs 2 Cr) sits oddly against Oman's 90% utilisation. Every derived number uses rounded Rs Cr. Two H1 YoY percentages are positional only. A4 must confirm both against the results filing before any number is quoted. A1 cite drift (R019, R039, R091, R102, R125) is non-material."
```
