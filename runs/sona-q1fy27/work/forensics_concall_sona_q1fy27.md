# A3 FORENSIC NOTES — Sona BLW Precision Forgings / Sona Comstar (SONACOMS) — Q1 FY27 — DOCTYPE: CONCALL

Source: `extract_concall_sona_q1fy27.txt` (25 pages, 1269 lines). Ledger: `ledger_concall_sona_q1fy27.md`.
Prior-quarter extract: **NONE** (first pipeline run for SONACOMS; no verbatim EoM/entity/slide diff possible — every diff-based check degrades to baseline-only or N.A. and is marked so, never blank).
Ledger reconciliation: **100%** — every row of Tables 1-5 read at its cited line before judging. Key numbers spot-verified at source: N23 rev 12,310 (l.564), N27 EBITDA 23.1% (l.572), N28 PAT 181 (l.577), N20 order book 240bn/EV 64% (l.499), N42 robotics SOP (l.1145), N34/N35 capex intensity (l.768/772), N41 VA 4.5x (l.1099), N44 consumption 32x (l.1197).

This is a strategy/announcement-heavy call (Sona Comstar 2.0 + DENSO JV + robotics entry). The forensic posture below treats every guidance/hedge/dodge as a FORWARD-SIGNAL or AMBIGUOUS item for A4, and audits management's answers against the ten Notion tripwires and the ten filing/deck flags (a)-(j). Units: Rs Crore x1 (transcript states figures in Rs Crore; note management mixes "billion" = Rs 100 Crore in the order-book discussion — 8bn = Rs 800 Cr, 240bn = Rs 24,000 Cr).

---

## 1. FINDINGS TABLE

| id | check | ledger ref | line / turn | verbatim quote (short) | classification | forward implication |
|----|-------|-----------|-------------|------------------------|----------------|---------------------|
| A3-F01 | F6 | F3 / N/A | l.455-456, turn 3 | "we expect that these recovery measures will become progressively more visible from quarter 2 onwards" | FORWARD-SIGNAL | Datable margin-recovery promise (Q2 FY27). Promise-vs-delivery anchor: if 23.1% does not lift in Q2, credibility gap. Pairs with tripwire (6). |
| A3-F02 | F6 | N42 | l.1145, turn 75 | "Actually, 1 is this quarter, 1 is next quarter, 1 within 15 months" | FORWARD-SIGNAL | Three datable robotics-order SOP milestones (Q2 FY27 / Q3 FY27 / by ~Q2 FY28). First hard delivery checkpoints for the Rs 800 Cr robotics book (N17). |
| A3-F03 | F6 | F2 | l.400-401, turn 3 | "our ambition for the next decade is to build another 10X company" | FORWARD-SIGNAL | Decade-horizon ambition frame; low falsifiability, monitorable only. |
| A3-F04 | F6/F7 | F6 | l.707-711 turn 14; l.1068-1070 turn 61 | "we are restricted by confidentiality agreements on it" / "we can't comment on the timeline" | AMBIGUOUS | JV2 SOP/revenue-recognition date dodged twice (Pramod Q2, Kapil relay Q16) with identical non-answer. A4 management question: earliest JV revenue-recognition quarter. |
| A3-F05 | F17 | — (flag a) | absence; l.276-278; l.707-711 | "our suspension motor business... remain completely outside the scope of this transaction" (scope stated, terms not) | CONFIRMATORY-NEGATIVE | Call gives strategic narrative but is SILENT on every financial term of the DENSO deal: Rs 1,750 Cr EV, Denso 49%, slump-sale mechanism, close date, P&L gain geography/quantum. Deck disclosed the divestment as a note only; call avoids the numbers. A4 must ask valuation, gain quantum, close date, and whether the core EV-motors (traction) subsidiary is being divested. |
| A3-F06 | F14 | — | Slide 8: l.267-272 vs l.283-285, turn 3 | "The first will focus on high voltage... for 4 and 4+ wheel vehicles" vs "JV2 will pay royalties to Denso for its high voltage technologies" | AMBIGUOUS | Internal entity-label inconsistency within one slide: high-voltage JV is called both "the first [JV]" and "JV2." Q&A compounds it (Pramod/mgmt call high voltage = JV2). Control, royalty geography and lead/lag sequencing all hinge on which is which. A4 clarification. |
| A3-F07 | F17 | — (flag c) | absence (whole transcript) | (no mention of forex anywhere) | CONFIRMATORY-NEGATIVE | +Rs 12.18 Cr YoY forex swing embedded in revenue never disclosed; the headline "+54%" revenue growth (N23) is not forex-adjusted on the call. A4: quantify forex contribution to reported revenue. |
| A3-F08 | F17 | N7 | l.204 (only mention), turn 3 | "acquisitions of Comstar, Novelic, and the Railway Business" | CONFIRMATORY-NEGATIVE | Novelic named only inside a Rs 2,750 Cr acquisition-cost bucket. KAM carrying value / impairment status entirely SILENT — this is Notion tripwire (3) (impairment > Rs 350 Cr) AND a buyable-trigger precondition ("Novelic KAM resolved"). Sustained silence on a live-monitored item = Role 5 confirmatory negative. |
| A3-F09 | F17 | — (flag d) | l.590-592, turn 5 | "Our return ratios continue to show gradual improvement" | AMBIGUOUS | No ROCE figure (15.8%), no normalised vs un-normalised split, no path back to >18%. Notion tripwire (1) (ROCE <14% two yrs) cannot be checked. A4: ROCE bridge + 18% timeline. |
| A3-F10 | F17 | N34/N35 | l.766-772 (intensity only); l.595-598, turns 21/5 | "best quarter from an operational cash flow perspective" (no number) | AMBIGUOUS | Deck disclosed ZERO capex. Call gives capex INTENSITY ratios (Rs1 → Rs8-9; 11-12x) but no absolute FY27-28 capex, no Q1 CFO figure, no CFO/PAT ratio. Tripwire (4) (CFO/PAT <1.0x) unverifiable; a "best-ever cash flow" claim sits on no disclosed number. A4: absolute capex + Q1 CFO + CFO/PAT. |
| A3-F11 | F16 | N20/N21 | l.499-501, turn 3 | "our net order book stands at 240 billion, with EVs accounting for 64%... robotics and physical AI... a small 3%" | AMBIGUOUS | EV share eased to 64% — bottom of the Notion (9) 64-70% band (CONFIRMED). Order book stated "net" (implies a haircut) but the delay-discount + EOL haircut methodology and gross-to-net bridge are undisclosed; new 3% robotics category mechanically dilutes EV %. A4: gross vs net order-book bridge. |
| A3-F12 | F16 | N44 | l.1183-1198, turns 84-86 | "if we consumed orders worth 15 billion, how are the revenues only 13 billion?" / "multiplied by 32 times" | AMBIGUOUS | Even the host analyst cannot reconcile gross order consumption to revenue; management's 8-yr-life / 32x multiplier answer explains direction, not the number. Order-book quality opaque. A4 reconciliation question (feeds Role 5 arithmetic check vs the filing baseline). |
| A3-F13 | F17 | — (flag/tripwire 7) | l.596-598, turn 5 | "a significant reduction in debtor days, which also made this as our best quarter from an operational cash flow perspective" | AMBIGUOUS | Management asserts a REVERSAL of the FY26 receivable-days stretch (+22 days, tripwire 7) but gives no debtor-days number. Claimed improvement without data — verify. A4: actual Q1 debtor days. |
| A3-F14 | F17 | Table 1 row 6; l.498, l.511-514 | roll-call l.90-91; railway mentions l.498/511-514 | Amit Mishra "introduced by name... but never speaks — zero speaking turns" (ledger); railway = "additional business wins in... railways" | CONFIRMATORY-NEGATIVE | Railway (FY26 Rs 973 Cr rev, Rs 149 Cr PAT — tripwire 8) never quantified on the call; the named Head of Railway Business does not speak once despite railway being a stated diversification pillar. A4: railway Q1 revenue/PAT. |
| A3-F15 | F7 | F9 | l.848-851, turn 34 | "this is just one quarter of data, let me have 2-3 data points... then we know that it's actually inflection" | AMBIGUOUS | Despite BEV +107% (N24), management refuses to call EV inflection — hedges that BEV momentum may not be structural. Tripwire (9) BEV-anchor read: monitor next 2-3 quarters. |
| A3-F16 | F7 | F14/F15 | l.1209 turn 90; l.1220-1227 turns 93/95 | "that is actually a very good question, Jay, and I don't think I know" | AMBIGUOUS | On the THIRD repeat of the robotics-ramp-timeline question management concedes it cannot date the execution cycle; the Rs 800 Cr robotics book has undefined revenue conversion. Repeat-question + dodge cluster (ledger Q8/Q21/Q25). |
| A3-F17 | F7 | F4 | l.419-421, turn 3 | "this... may continue to create some pressure on margin as a percentage" | FORWARD-SIGNAL | Management pre-warns of further margin pressure from the cost-pass-through lag; conservative read = 23.1% is not the trough and Q2 recovery (F01) is not assured. Pairs with tripwire (6). |
| A3-F18 | F17 | — (flag i) | l.471-473, turn 3 | "our EV business is no longer dependent on a handful of customers or one particular geography" | AMBIGUOUS | Diversification asserted but the single-customer / North-American-OEM concentration % is not quantified. A4: top-customer and NA-OEM revenue share to test the claim. |
| A3-F19 | F17 | — (flag j) | absence (no analyst raised it; mgmt did not address) | (governance items not discussed) | CONFIRMATORY-NEGATIVE | Auditor-signed-before-board-start and note-only DENSO disclosure governance items were neither raised by any analyst nor addressed by management. Concall is not the venue, but the silence is logged for Role 5 / the AR deep dive. |

---

## 2. CHECKLIST SCORECARD (all 17, exactly one status each — GATE A3)

| Check | Status | One-line basis |
|-------|--------|----------------|
| F1 Zero-value standing line items | **N.A.** | Concall transcript; no financial-statement line items / no ZERO_STANDING ledger rows. |
| F2 Standalone vs consolidated | **N.A.** | No S-vs-C tables in a concall; ledger carries none. |
| F3 Shell-entity detection | **N.A.** | No cost-line tables to compare across entities. |
| F4 Unaudited contribution ratio | **N.A.** | No auditor "Other Matters" paragraph in a concall. |
| F5 Going concern / EoM scope | **N.A.** | No EoM paragraph in a concall; also no prior quarter to diff. |
| F6 Forward-commitment phrase mining | **FINDING** | A3-F01/F02/F03/F04 + commitment register below; multiple datable promises. |
| F7 Hedge phrase mining | **FINDING** | A3-F15/F16/F17 — inflection hedge, robotics "I don't think I know," margin "may continue." |
| F8 Tax forensics | **N.A.** | No ETR / deferred-tax / tax-earlier-years disclosure in a concall. |
| F9 OCI forensics | **N.A.** | No OCI / actuarial data in a concall. |
| F10 Share count & dilution | **N.A.** | No paid-up-capital / basic-vs-diluted EPS in the transcript; QIP referenced qualitatively (l.591) with no share numbers. |
| F11 Reserves & net-worth tie-out | **N.A.** | No other-equity / net-worth figures in a concall. |
| F12 Segment forensics | **N.A.** | No segment assets/liabilities tables; only qualitative geo/product mix. |
| F13 Board outcome beyond results | **N.A.** | No Board Outcome / AGM / director-term agenda in a concall (DENSO JV board approval referenced but no meeting agenda items). |
| F14 Note drafting inconsistencies | **FINDING** | A3-F06 — internal JV1/JV2 high-voltage entity-label inconsistency within slide 8, compounded in Q&A. |
| F15 Entity list diffs | **N.A.** | No consolidation entity list + no prior-quarter ledger; no diff possible. |
| F16 Presentation-specific / reframed disclosure | **FINDING** | A3-F11/F12 — "net" order-book definition, EV share eased to 64%, robotics 3% added, gross-to-net haircut undisclosed, consumption arithmetic opaque. |
| F17 Concall silence audit | **FINDING** | A3-F05/F07/F08/F09/F10/F13/F14/F18/F19 — see "What Was NOT Discussed" below. |

Blank checks: none. GATE A3: **pass**.

---

## 3. COMMITMENT REGISTER (from F6 — promise-vs-delivery baseline; first run, so status = as-stated, no prior delivery to score)

| # | Commitment | Implied date | Turn / line ref | Status word |
|---|-----------|--------------|-----------------|-------------|
| C1 | Cost-pass-through recovery measures "progressively more visible from quarter 2 onwards" | Q2 FY27 | turn 3, l.455-456 | underway |
| C2 | Robotics order SOPs: "1 this quarter, 1 next quarter, 1 within 15 months" | Q2 FY27 / Q3 FY27 / ~Q2 FY28 | turn 75, l.1145 (corr. Rohit turn 74, l.1137 "12 to 15 months max") | initiated |
| C3 | Short-range exterior ADAS radar "under commercialization this quarter," meeting upcoming GoI ADAS regulations | Q1 FY27 (this qtr) + reg deadline | turn 4, l.530-533 | underway |
| C4 | AMR prototype shown at CES; "development continues to progress fairly rapidly" | ongoing | turn 3, l.353-354 | underway |
| C5 | JV1 (2W/3W) "will kickstart faster"; JV2 (high voltage) "following it" — SOP timeline itself withheld | undated (confidential) | turn 17, l.719-721 | initiated |
| C6 | JV2 global (ex-India) expansion "definitely on the anvil, but yes, it will take time" (phase two) | undated, phase 2 | turn 59, l.1063 | initiated |
| C7 | 2W/3W India traction-motor share to move from ~25% to ">50%" | undated ambition | turn 56, l.1044-1046 | initiated |
| C8 | "build another 10X company" over the next decade | ~10 yr | turn 3, l.400-401 | initiated |
| C9 | Robotics ramp expected "faster, much faster, probably" than the Year-4/5/7-8 EV framework (N36) | undated, "too early to tell" | turn 36, l.869-872 | initiated |

---

## 4. "WHAT WAS NOT DISCUSSED" TABLE (F17 silence audit vs Notion checklist + filing flags)

Consecutive-quarter silence count = **1 (this quarter)** for every row — no prior concall ledger exists, so this run establishes the baseline count; A4/Role 5 increment from here.

| Item (source) | On the call? | Verdict | Cite |
|---------------|--------------|---------|------|
| DENSO deal financial terms — Rs 1,750 Cr EV, 49%, slump-sale, close date, P&L gain (flag a) | Narrative yes, numbers no | SILENT on all terms | A3-F05, l.276-278 / l.707-711 |
| EBITDA margin bridge 23.1% (flag b / tripwire 6) | Yes — qualitative | ADDRESSED + CONFIRMED tripwire; no bps bridge | N27 l.572-575; Vivek l.452-460 |
| Net forex gain in revenue +Rs 12.18 Cr (flag c) | No | SILENT | A3-F07 |
| ROCE 15.8% normalised & path to >18% (flag d / tripwire 1) | Vague only | SILENT on the number | A3-F09, l.590-592 |
| Absolute capex FY27-28 + Q1 CFO + CFO/PAT (flag e / tripwire 4) | Intensity ratios only | SILENT on quantum | A3-F10, l.766-772 / l.595-598 |
| Novelic India / KAM carrying value & impairment (flag f / tripwire 3) | No (name only) | SILENT | A3-F08, l.204 |
| Order book gross vs net + EOL/delay haircut (flag g) | "Net" stated, method not | PARTIAL / method SILENT | A3-F11/F12, l.499-501 |
| BEV quarterly share (flag h) | Yes — 44% of auto sales | ADDRESSED | N25 l.566 |
| Single-customer / NA-OEM concentration % (flag i / tripwire 9) | Claimed diversified, unquantified | PARTIAL / % SILENT | A3-F18, l.471-473 |
| Governance items — auditor sign sequence, note-only DENSO disclosure (flag j) | No | SILENT | A3-F19 |
| Railway Rs 973 Cr rev / Rs 149 Cr PAT (tripwire 8) | Mentioned, unquantified; Head Railway silent | SILENT on quantum | A3-F14, l.498/511-514 |
| Working-capital / debtor-days (tripwire 7) | Claimed improved, unquantified | PARTIAL / number SILENT | A3-F13, l.596-598 |
| Corporate guarantee expansion (tripwire 5) | No | SILENT | absence |
| Forced block sale / control dispute (tripwire 2) | JV cedes control in JV1/EV-motors; framed as partnership, not dispute | ADDRESSED as partnership | l.267-278 |
| India revenue mix / eastern markets (tripwire 10) | Yes — eastern 59% vs 56% | ADDRESSED | N22 l.508-509 |

---

## 5. CROSS-CHECKS FOR A4 / A5

- **Repeat-and-dodge clusters (from ledger Table 3):** JV2 timeline (Q2/Q16 — identical confidentiality non-answer, A3-F04); robotics ramp timeline (Q8/Q21/Q25 — third ask yields "I don't think I know," A3-F16); e-axle JV structuring (Q10/Q14). These are the call's stress points and should convert to management questions.
- **Best-quarter framing risk:** "best ever quarter for revenue, BEV revenue, BEV revenue share" (l.406-407) and "best quarter from an operational cash flow perspective" (l.598) both sit against an undisclosed forex tailwind (A3-F07) and a margin that compressed 0.7pp (A3-F17). Conservative read: headline superlatives are gross of the forex boost and net of margin give-up; A4 to separate volume/mix/forex.
- **Order-book load-bearing reconciliation:** N20 (Rs 24,000 Cr net) vs N44 (8-yr life, 32x consumption) vs the deck's ZERO capex and the gross-to-net haircut is the single arithmetic knot for Role 5 (A3-F11/F12).
- **First-run caveat:** no prior concall ledger — all diff-based checks (F5, F15, F16 baseline-shift, F17 silence-count) are baselined this quarter, not compared.

```yaml
stage: A3-forensics
company: "SONACOMS"
quarter: "Q1 FY27"
doctype: "concall"
model: claude-opus-4-8
status: complete
forensics_path: "/home/user/inflection-pipeline/runs/sona-q1fy27/work/forensics_concall_sona_q1fy27.md"
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
  F14: FINDING
  F15: N.A.
  F16: FINDING
  F17: FINDING
findings:
  - {id: "A3-F01", check: "F6", line: "455-456", classification: "FORWARD-SIGNAL", implication: "Q2 FY27 margin-recovery promise; delivery anchor vs 23.1%"}
  - {id: "A3-F02", check: "F6", line: "1145", classification: "FORWARD-SIGNAL", implication: "Robotics SOP milestones Q2FY27/Q3FY27/~Q2FY28"}
  - {id: "A3-F03", check: "F6", line: "400-401", classification: "FORWARD-SIGNAL", implication: "Decade 10X ambition; low falsifiability monitorable"}
  - {id: "A3-F04", check: "F6/F7", line: "707-711;1068-1070", classification: "AMBIGUOUS", implication: "JV2 SOP timeline dodged twice; ask revenue-recognition quarter"}
  - {id: "A3-F05", check: "F17", line: "276-278;707-711", classification: "CONFIRMATORY-NEGATIVE", implication: "DENSO deal terms (Rs1750Cr EV,49%,slump-sale,close,P&L) all silent"}
  - {id: "A3-F06", check: "F14", line: "267-272;283-285", classification: "AMBIGUOUS", implication: "JV1/JV2 high-voltage label inconsistency; clarify control/royalty geography"}
  - {id: "A3-F07", check: "F17", line: "absent", classification: "CONFIRMATORY-NEGATIVE", implication: "+Rs12.18Cr forex in revenue undisclosed; 54% growth not forex-adjusted"}
  - {id: "A3-F08", check: "F17", line: "204", classification: "CONFIRMATORY-NEGATIVE", implication: "Novelic KAM carrying value/impairment silent; buyable-trigger precondition unaddressed"}
  - {id: "A3-F09", check: "F17", line: "590-592", classification: "AMBIGUOUS", implication: "No ROCE 15.8%, no path to >18%; ask ROCE bridge"}
  - {id: "A3-F10", check: "F17", line: "766-772;595-598", classification: "AMBIGUOUS", implication: "Capex quantum & Q1 CFO/CFO-PAT silent vs deck ZERO capex"}
  - {id: "A3-F11", check: "F16", line: "499-501", classification: "AMBIGUOUS", implication: "EV share eased to 64%; gross-to-net order-book haircut undisclosed"}
  - {id: "A3-F12", check: "F16", line: "1183-1198", classification: "AMBIGUOUS", implication: "Order consumption vs revenue not reconcilable; ask gross-net bridge"}
  - {id: "A3-F13", check: "F17", line: "596-598", classification: "AMBIGUOUS", implication: "Debtor-days improvement claimed, unquantified; verify vs tripwire 7"}
  - {id: "A3-F14", check: "F17", line: "498;511-514", classification: "CONFIRMATORY-NEGATIVE", implication: "Railway rev/PAT silent; Head of Railway zero turns"}
  - {id: "A3-F15", check: "F7", line: "848-851", classification: "AMBIGUOUS", implication: "Refuses to call EV inflection despite BEV +107%; monitor 2-3 qtrs"}
  - {id: "A3-F16", check: "F7", line: "1209;1220-1227", classification: "AMBIGUOUS", implication: "Robotics execution timeline unknown; Rs800Cr book undated conversion"}
  - {id: "A3-F17", check: "F7", line: "419-421", classification: "FORWARD-SIGNAL", implication: "Pre-warns further margin pressure; 23.1% may not be trough"}
  - {id: "A3-F18", check: "F17", line: "471-473", classification: "AMBIGUOUS", implication: "Customer concentration claim unquantified; ask top-customer/NA-OEM share"}
  - {id: "A3-F19", check: "F17", line: "absent", classification: "CONFIRMATORY-NEGATIVE", implication: "Governance items (auditor sign order, note-only DENSO) not raised; carry to AR"}
forward_signals: ["A3-F01", "A3-F02", "A3-F03", "A3-F17"]
ambiguous: ["A3-F04", "A3-F06", "A3-F09", "A3-F10", "A3-F11", "A3-F12", "A3-F13", "A3-F15", "A3-F16", "A3-F18"]
commitments:
  - {commitment: "Cost-pass-through recovery visible from Q2 onwards", implied_date: "Q2 FY27", ref: "turn 3 / l.455-456", status_word: "underway"}
  - {commitment: "Robotics order SOPs 1 this qtr / 1 next qtr / 1 within 15 months", implied_date: "Q2 FY27; Q3 FY27; ~Q2 FY28", ref: "turn 75 / l.1145", status_word: "initiated"}
  - {commitment: "ADAS short-range radar under commercialization this quarter", implied_date: "Q1 FY27", ref: "turn 4 / l.530-533", status_word: "underway"}
  - {commitment: "AMR development progressing rapidly (CES prototype)", implied_date: "ongoing", ref: "turn 3 / l.353-354", status_word: "underway"}
  - {commitment: "JV1 (2W/3W) kickstarts faster; JV2 (high voltage) follows; SOP withheld", implied_date: "undated/confidential", ref: "turn 17 / l.719-721", status_word: "initiated"}
  - {commitment: "JV2 global expansion phase two, on the anvil, will take time", implied_date: "undated phase 2", ref: "turn 59 / l.1063", status_word: "initiated"}
  - {commitment: "2W/3W India traction-motor share 25% to >50%", implied_date: "undated ambition", ref: "turn 56 / l.1044-1046", status_word: "initiated"}
  - {commitment: "Build another 10X company over the next decade", implied_date: "~10 yr", ref: "turn 3 / l.400-401", status_word: "initiated"}
  - {commitment: "Robotics ramp faster than Year-4/5/7-8 EV framework", implied_date: "undated, too early", ref: "turn 36 / l.869-872", status_word: "initiated"}
gate_a3: pass
blank_checks: []
```
