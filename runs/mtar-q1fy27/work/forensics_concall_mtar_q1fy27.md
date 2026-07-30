# A3 FORENSIC NOTES — MTAR Technologies Limited (MTAR), Q1 FY27, DOCTYPE = CONCALL

Source A1 extract: `/home/user/inflection-pipeline/runs/mtar-q1fy27/work/extract_concall_mtar_q1fy27.txt`
A2 ledger: `/home/user/inflection-pipeline/runs/mtar-q1fy27/work/ledger_concall_mtar_q1fy27.md`
Cross-doc extracts reconciled: results filing (Millions x0.1), presentation (Cr x1), press release (Cr x1)
Ledger reconciliation: 124/124 turns, 53/53 mgmt numbers, 32/32 questions, 22/22 forward-hedge rows read verbatim at cited line = **100%**.

Doctype rule applied: on a concall F6/F7/F17 are the live checks; balance-sheet checks are N.A.; F14 run in EXTENDED cross-document arithmetic mode per task. Transcript is auto-STT and garbled — garbled/ambiguous numbers are FLAGGED, never silently corrected. Conservative (lean-bear) bias on interpretation.

---

## 1. FINDINGS TABLE

| id | check | ledger row | line/turn | verbatim quote (short) | classification | forward implication |
|----|-------|-----------|-----------|------------------------|----------------|---------------------|
| FF-01 | F14 | N21 | line 7 | "gross margins we achieved as 45.61%... compared to the last year 47.65%" | FORWARD-SIGNAL | CFO benchmarks Q1FY27 GP against FY26 FULL-YEAR (47.7% deck) not Q1FY26 (54.2% deck). True like-for-like YoY GP compression is ~-8.7pp, not the -2pp implied. Directly softens the prior "margins scale-driven not gross-margin-driven" caveat — gross margin IS deteriorating. |
| FF-02 | F14 | N26 | line 7 | "cash flow from operations is at 247.69 crores in this quarter as against 191.66 crores" | AMBIGUOUS | Single most important reconciliation. No Q1 cash-flow statement exists in the filing; 191.66 reconciles to NO filed figure (FY26 CFO = 196.9, deck p28). If 247.69 is quarterly it is ~4.9x Q1 PAT (50.2) — implausible except via customer advances / WC release (Other Current Liab +~210 Cr Mar-26; WC days 172->59). Verbal, unverifiable; does NOT resolve the INDETERMINATE cash-conversion caveat. Caps at PROCEED WITH CAVEATS. |
| FF-03 | F14 | N27,N28,N29 | line 7 | "debt is at 423.6 crores as of 30th June 2026... investment of 379 crores... literally there is no debt in the company except some 20 30 crores after adjusting the cash" | FORWARD-SIGNAL | Gross debt ROSE 369.3 (Mar-26, deck p26 = 147.7+221.6) -> 423.6 (Jun-26). "Net 20-30 Cr" holds ONLY by treating all Rs 379 Cr investments (largely mutual funds; MF 215.3 at Mar-26, deck p27) as cash. On ex-MF basis Jun-26 net debt ~Rs 404 Cr vs Rs 348 Cr Mar-26 — net debt WORSENED ~+56 Cr QoQ while "no debt" narrative was presented. Reframes the net-debt basis. |
| FF-04 | F14 | N11,N12,N39,N46 | lines 5, 25, 27, 89 | "closing order book by end of this quarter already stands at 5,143 crores and we have received additional 800 crores of orders uh today"; CFO: "We received the 3,200... already communicated... incremental order is 800... 5,100 plus 800 plus" | AMBIGUOUS | Closing 5,143 Cr is SOLID (reconciles to deck p13 = 5,143.3). But "+800 Cr today" is post-quarter (not in 5,143), and the "3,200" reference matches nothing (Q1 incoming orders = 2,895.1 deck p13; Bala's "3,00 cr" line 25 garbled). Nuclear-only figure drifts 800 (N33) / 684+130=815 (N46). DEFINITION_WATCH: gross vs closing vs post-quarter order-book definitions blurred verbally. |
| FF-05 | F14 | N19,N20,N36 | lines 7, 23, 65 | "working capital days we... have achieved 59 days compared to... 172... we were expecting to maintain 100 days" | CONFIRMATORY-NEGATIVE | Deck p14 confirms 59 at Jun-26. Management EXPLICITLY guides WC UP to ~100 days for the year -> Q1 59 is NOT the sustainable level. Confirms the prior "advance-funded, not structural" WC caveat (F-13 in thesis). The 59 is a trough, not a run-rate. |
| FF-06 | F14 | N41,N42 | line 27 | "at least four five times of asset turnover" ... "asset turnover ratio at least six times" | AMBIGUOUS | Internal inconsistency in the SAME turn: 4-5x then "at least six times". Capital-efficiency target unfirm; A4 to clarify the denominator/basis. |
| FF-07 | F14 | N13 | line 5 | "guidance given earlier at 80% revenue load for the current fiscal year with an AITA margin of 24 plus minus 100 basis points" | FORWARD-SIGNAL | Concall 80% matches deck p4 (80% growth) — internally consistent — but is an UP-revision vs Notion-recorded FY27 guidance of 50% (May-26). Apparent guidance raise 50%->80%. MD adds "pretty confident to do better". A4 to confirm the revision and its dependence on the unverified order pipeline. |
| FF-08 | F6 | (F3 lexicon) | line 5 | "The offline and gas [Oil & Gas] facility will be operational by this October" | FORWARD-SIGNAL | Concall says Weatherford/O&G facility operational OCTOBER 2026; deck p21 says "commissioned by Q3 FY27". October sits inside Q3 FY27 so not contradictory, but the original Notion monitorable window was Jun-Sep 2026 — already a mild slip. Dated commitment to track in the promise-vs-delivery register. |
| FF-09 | F14 | N7,N51,N52 + 4b | lines 5, 9, 21, 117, 163 | "31 billion" (line 9); "10 megawatt reactors" (line 117); "actuator program about 142" (line 163); "exceeding more than 250" (line 5); "reduced from 78 to 145" (line 21) | NEUTRAL-FACT | GARBLED-number cluster (STT artifacts), flagged NOT corrected: "31 billion" today's order inconsistent with Rs 800 Cr; Mahi Banswara "10 MW" implausible for PHWR-scale; actuator "142 pages/value" unit ambiguous; defense ">250" unit truncated; analyst inventory "78 to 145" wrong-direction (deck: 208->145). Do not rely on any of these five figures. |
| FF-10 | F6 | N4,N5,N8,N32,N49,N53 etc. | lines 5,13,81,111,241 | "phase two to be commissioned by uh September October"; "phase three... completed in March of [2027]"; "double our revenues in aerospace and defense... current fiscal year" | FORWARD-SIGNAL | Dense dated forward-commitment register (see Section 3). Feeds Role 5 promise-vs-delivery tracker and FTTCP catalyst timeline. Multiple hard dates in the next 3 quarters create near-term falsifiability. |
| FF-11 | F7 | H6 | line 155 (Q24 @ line 153) | "See all this is unwanted noise. Uh I really wanted to express this very clearly... There is no issue at all." | AMBIGUOUS | Direct question on US data-center capex slippage at the key customer (Bloom) was DEFLECTED, not answered. The nearest-term demand/concentration risk left unresolved. A4 to convert into a pointed management question on Bloom order visibility and US-tariff exposure. |
| FF-12 | F7 | H1,H7 | lines 33, 161 | "I can't specify the numbers because of the [NDA] being signed"; "they can't get into the numbers because of the NDA side" | CONFIRMATORY-NEGATIVE | Hot-box UNIT volumes — the exact metric the thesis tracks (Notion monitorable #1: 12k Mar-26 / 20k Dec-26) — withheld twice citing NDA (Gorov Q6; Rohit Q25 re Bloom Fremont 5GW / >50,000 boxes). The core monitorable is unverifiable from this call. |
| FF-13 | F7 | H3,H8,H9,H10 | lines 77,167,235,237 | "probably we'll see by end of next quarter"; "I don't have the exact breakup... CFO... can give it little later"; "can't spell out the exact percentage"; "I can't say the exact number" | NEUTRAL-FACT | Routine deflections (guidance-upgrade timing, interest-cost breakup, market share, FY30 size). Individually immaterial; noted for completeness. |
| FF-14 | F17 | (silence) | not spoken; deck p31 | promoter holding "29.35%" (Jun-26), down from 30.44% (Mar-26) | CONFIRMATORY-NEGATIVE | SILENCE on the nearest-monitored governance tripwire (Tripwire #5: promoter <25%). Promoter stake fell -1.09pp QoQ (fastest of the four quarters shown). No analyst asked; management did not raise. Per Role 5, sustained silence on a deteriorating governance metric is a confirmatory negative. |
| FF-15 | F17 | (silence) | not spoken; results note 4/6 | "filed the scheme for the merger of its wholly owned subsidiaries, Gee Pee Aerospace... and Magnatar... with the National Company Law Tribunal" | CONFIRMATORY-NEGATIVE | NCLT merger of the two (loss-making: net loss Rs 7.22 mn Q1, results p8) subsidiaries never mentioned on the call. Governance/structure change silent. |
| FF-16 | F17 | (silence) | not spoken; results p7-9 | UDIN present; "Limited Review"; subs "reviewed by their respective independent auditors" | NEUTRAL-FACT | Audit/UDIN matter routine (clean limited review, no modification). Not discussed; no adverse signal, logged for the silence table. |
| FF-17 | F17 | (silence) | deflected only (see FF-11); deck p13 | export "81%" of revenue | CONFIRMATORY-NEGATIVE | Bloom customer CONCENTRATION and US-tariff/export risk (Notion: ~79% export, US-tariff risk) never substantively addressed — only deflected as "unwanted noise". Concentration never quantified on the call despite 81% export mix. |

Also silent (logged in Section 4, not separate findings): KMP SEBI insider-trading matter (Feb-26, Notion); promoter selling INTENT; Weatherford revenue contribution quantum.

---

## 2. CHECKLIST SCORECARD (all 17; exactly one status each — GATE A3)

| # | Status | One-line basis |
|---|--------|----------------|
| F1 | N.A. | Zero-value standing line items are a results-filing concept; no standing line items spoken on a concall. |
| F2 | N.A. | Standalone-vs-consolidated decomposition not presented on the call (CFO gave consolidated only, line 7); balance-sheet check, N.A. for concall. |
| F3 | N.A. | Shell-entity cost-line comparison requires the filing tables; not a concall check. |
| F4 | N.A. | Unaudited contribution ratio (subs Rs 16.79 mn rev / -7.22 mn PAT) sits in the auditor letter, not the call. |
| F5 | N.A. | Going-concern / EoM scope tracking is a filing/AR check; none spoken; first concall (no prior transcript to diff). |
| F6 | **FINDING** | Dense dated forward-commitment register mined (FF-08, FF-10) incl. Weatherford Oct-vs-Q3FY27 date discrepancy; feeds promise tracker. |
| F7 | **FINDING** | Material deflection on US data-center/Bloom demand (FF-11) + NDA-cover on hot-box volumes (FF-12); routine hedges (FF-13). |
| F8 | N.A. | Tax forensics (ETR, "adjustment of tax relating to earlier periods" = (8.26) mn, results p5/6) is a filing check; not spoken. |
| F9 | N.A. | OCI forensics require the filing; OCI = nil this quarter; not a concall check. |
| F10 | N.A. | Share count / EPS spread (3,07,59,591 shares, deck p31) not discussed on the call. |
| F11 | N.A. | Reserves / net-worth tie-out is a balance-sheet check; not spoken. |
| F12 | N.A. | Segment forensics — single reportable segment (results note 5); not a concall check. |
| F13 | N.A. | Board outcomes (AGM 28-Sep-26; AR/MD&A approved; director re-appointments) are in the results filing, not the call. |
| F14 | **FINDING** | EXTENDED cross-document reconciliation: gross-margin comparator (FF-01), CFO cash flow (FF-02), net-debt basis (FF-03), order-book drift (FF-04), WC-days guidance-up (FF-05), asset-turnover inconsistency (FF-06), guidance revision (FF-07), garbled cluster (FF-09). |
| F15 | N.A. | Entity-list diffs need a prior-quarter list; first concall; entity list (2 subs) is in the filing, unchanged, not spoken. |
| F16 | N.A. | Presentation-specific (dropped/reframed disclosures) — this is a concall; deck reframes are captured under F14 reconciliation, not re-run here. |
| F17 | **FINDING** | SILENCE AUDIT: promoter stake decline (FF-14), NCLT merger (FF-15), audit/UDIN (FF-16), Bloom concentration/US-tariff (FF-17); full table Section 4. |

Blank checks: NONE. GATE A3 = PASS.

---

## 3. COMMITMENT REGISTER (from F6 — dated / dateable management commitments)

| # | Commitment | Implied date | Turn / line ref | Status word |
|---|-----------|--------------|-----------------|-------------|
| C1 | Fuel-cell phase 1 capacity expansion | done | line 39 | completed |
| C2 | Fuel-cell phase 2 commissioning | Sep/Oct 2026 | line 5 (N4), line 37 (N45) | underway |
| C3 | Fuel-cell phase 3 (multifold) completed | Mar 2027 | line 5 (N5), lines 33/35 (N43/N44) | underway |
| C4 | O&G / Weatherford greenfield facility operational | Oct 2026 (concall) / Q3 FY27 (deck p21) | line 5 | underway — DATE DISCREPANCY |
| C5 | Aerospace & defense revenue to double | FY27 | line 5 (N8, F3) | underway |
| C6 | Aerospace ramp continuing off this base | next 3-4 years | line 5 (N9) | underway |
| C7 | Nuclear order-book execution commences | H2 FY27 | line 81 | initiated (commences H2) |
| C8 | Refurbishment orders Rs 130-140 Cr | this quarter (Q2 FY27) | line 13 (N32) | expected |
| C9 | +Rs 800 Cr orders received "today" | post 30-Jun-26 | line 5 (N12) | received (verbal, unverified) |
| C10 | Data-center Rs 45 Cr order executed | Feb/Mar FY27 | line 111 (N49) | underway |
| C11 | Data-center 8 infrastructure sets/yr + dedicated facility (8x headroom) | ongoing | lines 5, 111 (N6/N50) | initiated |
| C12 | FY30 size: products >Rs 1,000 Cr; aerospace Rs 600-700 Cr | FY30 (3-4 yrs) | line 241 (N53) | target |
| C13 | Guidance 80% revenue growth + 24% ±100bps EBITDA, "will do better" | FY27 | line 5 (N13/N14, F2) | reaffirmed / raised vs 50% prior |
| C14 | Closing order book Rs 5,000 Cr | FY27 year-end | line 5 (N10, F4) | achieved-ahead (5,143 already) |
| C15 | GST refund ~Rs 70 Cr/year | annual run-rate | line 23 (N35) | target |
| C16 | ROCE 23% | next year (FY28) | line 7 (N24) | target |
| C17 | Capex ~Rs 500 Cr | FY27 + FY28 combined | lines 7/27 (N30/N40) | underway |
| C18 | Asset turnover 4-6x | ongoing | line 27 (N41/N42) | target (internally inconsistent) |

---

## 4. "WHAT WAS NOT DISCUSSED" — SILENCE AUDIT (F17)

Cross-reference of the Notion monitoring checklist / tripwires and the F6 commitment register against the transcript. First concall in the pipeline, so consecutive-quarter silence counts start at 1.

| Item | Source of expectation | Addressed on call? | Qtrs silent | Classification |
|------|----------------------|--------------------|-------------|----------------|
| Promoter stake decline to 29.35% (-1.09pp QoQ) / selling intent | Tripwire #5 (promoter <25%); deck p31 | NO — no analyst asked, mgmt did not raise | 1 | CONFIRMATORY-NEGATIVE (nearest-monitored governance tripwire) |
| NCLT merger of Gee Pee Aerospace + Magnatar (loss-making subs) | Results notes 4/6; subs net loss -7.22 mn | NO | 1 | CONFIRMATORY-NEGATIVE |
| Bloom customer concentration + US-tariff / 81% export risk | Notion (US-tariff, ~79% export); deck p13 | DEFLECTED only ("unwanted noise", line 155) — not quantified | 1 | CONFIRMATORY-NEGATIVE |
| Hot-box UNIT volumes (12k Mar-26 / 20k Dec-26 track) | Notion monitorable #1 | ASKED (Q6, Q25) — DECLINED citing NDA | 1 | CONFIRMATORY-NEGATIVE |
| Consolidated auditor UDIN / audit matter | Results p7-9 (limited review, UDIN present) | NO — routine, clean | 1 | NEUTRAL-FACT |
| KMP SEBI insider-trading matter (COO/VP/DGM, Feb-26) | Notion named risk | NO | 1 | CONFIRMATORY-NEGATIVE |
| Weatherford O&G FY27 revenue contribution quantum | Notion monitorable #3 | PARTIAL — facility "operational by October" (line 5); no revenue quantum | 1 | AMBIGUOUS |
| Q1 cash-flow statement / cash conversion | CLAUDE.md INDETERMINATE caveat | VERBAL only (247.69 vs 191.66) — unverifiable, no statement filed | 1 | AMBIGUOUS |
| Subsidiary loan rollovers (Magnatar, Gee Pee) | Notion named risk | NO | 1 | NEUTRAL-FACT |

Addressed (for contrast, so silence is not overstated): WC-days drivers (Q4/Q11/Q12), capex quantum & split (Q5/Q16/Q17/Q23), nuclear order size & execution window (Q2/Q3/Q14/Q15/Q19), data-center order size & export status (Q18/Q24), products/aerospace ramp & FY30 size (Q7/Q9/Q22/Q28/Q29/Q32).

---

## 5. TOP RECONCILIATION FINDINGS (priority readout)

1. **GROSS MARGIN (FF-01, line 7):** CFO's "45.61% vs 47.65% last year" (-2pp) benchmarks against FY26 FULL-YEAR GP (deck 47.7%), not Q1FY26 (deck 54.2%). Like-for-like Q1 YoY compression is ~-8.7pp. Confirms gross margin IS deteriorating; the "scale-driven, not gross-margin-driven" caveat is understated by the chosen comparator. (Note: 45.61% is the STANDALONE GP; deck 45.5% is consolidated — CFO labelled the review "consolidated".)
2. **CASH FLOW (FF-02, line 7):** "CFO 247.69 Cr this quarter vs 191.66 Cr" is verbal, absent from the filing (no Q1 cash-flow statement), and 191.66 reconciles to no published figure. If quarterly, ~4.9x Q1 PAT — implausible except advance/WC-release driven (Other Current Liab +~210 Cr; WC days 172->59). Does NOT resolve INDETERMINATE cash conversion; caps at PROCEED WITH CAVEATS. THE single most important item for A4.
3. **NET DEBT (FF-03, line 7):** "No debt except 20-30 Cr" holds only if all Rs 379 Cr investments (mostly MF) count as cash. Gross debt actually ROSE 369.3 (Mar-26) -> 423.6 (Jun-26); ex-MF net debt worsened ~348 -> ~404 Cr QoQ.
4. **ORDER BOOK (FF-04, lines 5/25/27/89):** Closing 5,143 Cr is deck-solid; "+800 Cr today" (post-quarter) and "3,200" (matches nothing; Q1 inflow was 2,895.1) are verbal and blur gross vs closing vs post-quarter definitions. DEFINITION_WATCH.
5. **WC DAYS (FF-05, lines 7/23/65):** 59 vs FY26 172, guided UP to ~100 for the year — Q1 59 is a trough, not sustainable. CONFIRMS the advance-funded (not structural) WC caveat.

---

```yaml
stage: A3-forensics
company: "MTAR"
quarter: "Q1 FY27"
doctype: "concall"
model: claude-opus-4-8
status: complete
forensics_path: "/home/user/inflection-pipeline/runs/mtar-q1fy27/work/forensics_concall_mtar_q1fy27.md"
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
  F16: N.A.
  F17: FINDING
findings:
  - {id: "FF-01", check: "F14", line: "line 7 (N21)", classification: "FORWARD-SIGNAL", implication: "GP comparator uses FY26 full-year (47.7%) not Q1FY26 (54.2%); true YoY GP compression ~-8.7pp not -2pp"}
  - {id: "FF-02", check: "F14", line: "line 7 (N26)", classification: "AMBIGUOUS", implication: "Verbal CFO 247.69 vs 191.66 Cr; not in filing, comparator reconciles to nothing; if quarterly ~4.9x PAT (advance/WC-driven); INDETERMINATE cash conversion unresolved"}
  - {id: "FF-03", check: "F14", line: "line 7 (N27-N29)", classification: "FORWARD-SIGNAL", implication: "Gross debt rose 369.3->423.6 Cr QoQ; 'net 20-30 Cr' only if all Rs 379 Cr MF = cash; ex-MF net debt worsened ~348->404 Cr"}
  - {id: "FF-04", check: "F14", line: "lines 5,25,27,89 (N11,N12,N39,N46)", classification: "AMBIGUOUS", implication: "Closing 5,143 deck-solid but '+800 today' post-quarter and '3,200' undefined; order-book definitions blurred verbally"}
  - {id: "FF-05", check: "F14", line: "lines 7,23,65 (N19,N20,N36)", classification: "CONFIRMATORY-NEGATIVE", implication: "WC 59 days guided UP to ~100; Q1 trough not sustainable; confirms advance-funded not structural WC caveat"}
  - {id: "FF-06", check: "F14", line: "line 27 (N41,N42)", classification: "AMBIGUOUS", implication: "Asset turnover '4-5x' then 'at least six times' same turn; capital-efficiency target unfirm"}
  - {id: "FF-07", check: "F14", line: "line 5 (N13)", classification: "FORWARD-SIGNAL", implication: "80% revenue guidance (matches deck) is up-revision vs Notion 50% prior; confirm revision basis"}
  - {id: "FF-08", check: "F6", line: "line 5", classification: "FORWARD-SIGNAL", implication: "Weatherford/O&G facility 'operational by October' (concall) vs 'Q3 FY27' (deck) vs Jun-Sep (Notion) — mild slip, dated catalyst to track"}
  - {id: "FF-09", check: "F14", line: "lines 5,9,21,117,163 (N7,N51,N52)", classification: "NEUTRAL-FACT", implication: "Garbled STT numbers ('31 billion','10 MW reactors','142 pages','>250','78 to 145') flagged not corrected; do not rely on these five"}
  - {id: "FF-10", check: "F6", line: "lines 5,13,81,111,241", classification: "FORWARD-SIGNAL", implication: "Dense dated commitment register (18 items) — feeds Role 5 promise-vs-delivery + FTTCP timeline"}
  - {id: "FF-11", check: "F7", line: "line 155 (Q24 @153, H6)", classification: "AMBIGUOUS", implication: "US data-center/Bloom slippage question deflected as 'unwanted noise'; concentration/demand risk unresolved -> A4 question"}
  - {id: "FF-12", check: "F7", line: "lines 33,161 (H1,H7)", classification: "CONFIRMATORY-NEGATIVE", implication: "Hot-box unit volumes (core monitorable) withheld twice citing NDA; thesis metric unverifiable from call"}
  - {id: "FF-13", check: "F7", line: "lines 77,167,235,237 (H3,H8,H9,H10)", classification: "NEUTRAL-FACT", implication: "Routine deflections (guidance timing, interest breakup, market share, FY30 size)"}
  - {id: "FF-14", check: "F17", line: "silence; deck p31", classification: "CONFIRMATORY-NEGATIVE", implication: "Promoter stake 30.44->29.35% (-1.09pp QoQ) unaddressed; nearest governance tripwire; silence on deteriorating metric"}
  - {id: "FF-15", check: "F17", line: "silence; results note 4/6", classification: "CONFIRMATORY-NEGATIVE", implication: "NCLT merger of loss-making subsidiaries never mentioned on call"}
  - {id: "FF-16", check: "F17", line: "silence; results p7-9", classification: "NEUTRAL-FACT", implication: "Audit/UDIN routine (clean limited review); logged, no adverse signal"}
  - {id: "FF-17", check: "F17", line: "deflected FF-11; deck p13", classification: "CONFIRMATORY-NEGATIVE", implication: "Bloom concentration + US-tariff/81% export risk never quantified on call"}
forward_signals: ["FF-01", "FF-03", "FF-07", "FF-08", "FF-10"]
ambiguous: ["FF-02", "FF-04", "FF-06", "FF-11"]
commitments:
  - {commitment: "Fuel-cell phase 2 commissioning", implied_date: "Sep/Oct 2026", ref: "line 5 (N4) / line 37 (N45)", status_word: "underway"}
  - {commitment: "Fuel-cell phase 3 multifold expansion completed", implied_date: "Mar 2027", ref: "line 5 (N5) / lines 33,35 (N43,N44)", status_word: "underway"}
  - {commitment: "O&G / Weatherford facility operational", implied_date: "Oct 2026 (concall) / Q3 FY27 (deck)", ref: "line 5", status_word: "underway-date-discrepancy"}
  - {commitment: "Aerospace & defense revenue to double", implied_date: "FY27", ref: "line 5 (N8,F3)", status_word: "underway"}
  - {commitment: "Nuclear order-book execution commences", implied_date: "H2 FY27", ref: "line 81", status_word: "initiated"}
  - {commitment: "Refurbishment orders Rs 130-140 Cr", implied_date: "Q2 FY27", ref: "line 13 (N32)", status_word: "expected"}
  - {commitment: "+Rs 800 Cr orders received today", implied_date: "post 30-Jun-26", ref: "line 5 (N12)", status_word: "received-unverified"}
  - {commitment: "Data-center Rs 45 Cr order executed", implied_date: "Feb/Mar FY27", ref: "line 111 (N49)", status_word: "underway"}
  - {commitment: "Data-center 8 sets/yr + dedicated facility", implied_date: "ongoing", ref: "lines 5,111 (N6,N50)", status_word: "initiated"}
  - {commitment: "FY30 products >Rs 1,000 Cr; aerospace Rs 600-700 Cr", implied_date: "FY30", ref: "line 241 (N53)", status_word: "target"}
  - {commitment: "Guidance 80% revenue + 24% +/-100bps EBITDA, will do better", implied_date: "FY27", ref: "line 5 (N13,N14,F2)", status_word: "reaffirmed"}
  - {commitment: "Closing order book Rs 5,000 Cr", implied_date: "FY27 year-end", ref: "line 5 (N10,F4)", status_word: "achieved-ahead"}
  - {commitment: "GST refund ~Rs 70 Cr/year", implied_date: "annual", ref: "line 23 (N35)", status_word: "target"}
  - {commitment: "ROCE 23%", implied_date: "FY28", ref: "line 7 (N24)", status_word: "target"}
  - {commitment: "Capex ~Rs 500 Cr", implied_date: "FY27+FY28", ref: "lines 7,27 (N30,N40)", status_word: "underway"}
  - {commitment: "Asset turnover 4-6x", implied_date: "ongoing", ref: "line 27 (N41,N42)", status_word: "target-inconsistent"}
gate_a3: pass
blank_checks: []
```
