# A3 FORENSIC NOTES — EXICOM TELE-SYSTEMS (EXICOM) — Q1 FY27 — DOCTYPE: CONCALL

Source extract: `/home/user/inflection-pipeline/runs/exicom-q1fy27/work/extract_concall_exicom_q1fy27.txt`
Ledger: `/home/user/inflection-pipeline/runs/exicom-q1fy27/work/ledger_concall_exicom_q1fy27.md`
Prior context: `/home/user/inflection-pipeline/runs/exicom-q1fy27/work/prior_context.md` (first quarterly-pipeline run; no prior-quarter extract to verbatim-diff)
Ledger reconciliation: 127/127 management numbers, 14/14 commitments, 11/11 hedges, 50/50 turns, 13/13 questions read at cited line. 100%.
Line/turn numbers below are the extract's embedded numbering (per ledger convention; file line = embedded + 15).

Doctype scope: F6 (forward commitments), F7 (hedges), F17 (silence audit) are the core pass. F10 N.A. (no share count spoken). F1-F5, F8, F9, F11-F16 are N.A. for a concall EXCEPT the one balance-sheet number the transcript states that contradicts the filing (consolidated debt ~Rs370 cr) — captured as F17-05 cross-reference.

---

## FINDINGS TABLE

| id | check | ledger ref | line/turn | verbatim quote | classification | forward implication |
|---|---|---|---|---|---|---|
| F17-01 | F17 | M8/M79, Q1 | 18, 20, 28 | "moved back to 22 cr a loss in Q1"; "21.9 Ks had a 6.6 margin% margin negative" | CONFIRMATORY-NEGATIVE | Pre-committed Q1 FY27 metric (consol EBITDA >=0 Bull / < -Rs20 cr Bear) printed the BEAR outcome (~ -Rs22 cr), reversing the Q4 FY26 +Rs0.3 cr breakeven. Trigger T1 (2nd-consec breakeven) did NOT confirm. Flag prominently for A4; decision stays human. |
| F17-02 | F17 | H1, M90, turn 30 | 18, 30 | "profitability is still not in black"; "unreasonably high margins... now... not as high as we were enjoying earlier" | AMBIGUOUS | Management frames the reversal as seasonality (Q4 strongest) + erosion of low-cost acquired Tritium inventory — i.e. a mix/timing story, not structural. A4 question: is the margin give-back one-off (inventory run-off) or a permanent Tritium gross-margin reset now that acquisition inventory is exhausted? |
| F17-03 | F6/F17 | C7, C8, C9, H4 | 30, 34 | "break even in quarter two or"; "I can't specify whether quarter two or three"; "3x revenue growth... as well as a break even in quarter 47" | FORWARD-SIGNAL | Two dated breakeven promises now on the record: consolidated Q2 OR Q3 FY27; Tritium Q4 FY27. Feeds Role 5 promise-vs-delivery. The consolidated date is a soft band ("two or three"), so the earliest testable milestone is the Q2 FY27 print. |
| F17-04 | F7 | C3, C4, H3, M51, M52 | 18 | "if these trials are successful Tridium can be awarded more than 20 to$30 million contract for calendar 7"; "subject to successful trials can be expected to... $20 million of contract for C by 27" | AMBIGUOUS | The entire Tritium/US revenue-scale narrative ($20-30M + $20M CY27) rests on trials at "mid-stages to advanced stages" that are explicitly conditional. No FAT sign-off date, no binary pass/fail milestone given (monitoring Q4 unmet). A4 question: what is the FAT sign-off date and what happens to the 3x claim if a trial fails? |
| F17-05 | F17 | M89 | 20 | "consolidate debt stood at about 370 crores as on 30th June 26" | AMBIGUOUS | Transcript balance-sheet number contradicts the filing memory: prior Q4 FY26 net debt ~Rs649 cr incl lease / ~Rs378 cr ex-lease. Rs370 cr is not reconciled to a basis (gross vs net vs ex-lease). Either a ~Rs279 cr one-quarter deleveraging (implausible without a raise) or an undisclosed basis change. A4 must ask management to state the basis; this also touches monitoring Q1 (net-debt ceiling). |
| F17-06 | F7 | H7, M108, M109, Q6 | 44, 46, 48 | "I will uh... check this uh again... take your coordinates and come back to you with an exact answer" | AMBIGUOUS | AC-charger capacity cannot be reconciled on the call: annual report 42,000 (analyst) vs 48,000 single-shift (mgmt) vs 220,000 (mgmt). A named-number disclosure discrepancy left ANSWER_DEFERRED. A4: pin the true installed AC capacity and reconcile the AR figure. |
| F17-07 | F17 | M12/M13 vs M57/M58 | 18 vs 20 | "revenue of 177 crores which was 73% higher" (CEO) vs "Critical power grew by 80%... to 176 crores" (CFO) | AMBIGUOUS | Same segment, same quarter, two growth rates (73% vs 80%) and two revenue values (Rs177 vs Rs176) from the two speakers on one call. Data-quality/governance data point; the 7-pt growth spread is not pure rounding. A4: confirm the actual critical-power YoY growth. |
| F17-08 | F17 | M4/M65, Q6-monitoring | 18, 20 | "iita margins to 8.8%"; "8.8% margin" | CONFIRMATORY-NEGATIVE | Standalone EBITDA margin printed 8.8%, BELOW the ~10.6% Q4 FY26 level flagged in the monitoring checklist (item 6). Sustainability question was never addressed forward; the number itself already softened ~180 bps. Monitor for further slippage as BharatNet (fixed-price) scales. |
| F17-09 | F17 | monitoring checklist 2/5/7/9/10 | (silence) | not spoken anywhere in turns 14-112 | CONFIRMATORY-NEGATIVE | FIVE carried monitoring items got ZERO airtime, now 2nd consecutive quarter of silence: (2) Tritium 7.8% foreign holder / implied valuation / OCD origin; (5) payable-days / bill-discounting durability; (7) Corporate Promoter loan (Note 4) / residual RPTs; (9) Tritium India vs Delhi DCFC named customers; (10) Hyderabad Tritium-brand DCFC line. Per Role 5 sustained silence on unresolved items is a confirmatory negative. See Silence Table. |
| F17-10 | F6 | C1, M19 | 18 | "get the export sales to nearly double of 8%... to roughly about 15% of... critical power sales in a year" | FORWARD-SIGNAL | Dated FY27 commitment: critical-power exports 8% -> 15% within the fiscal year. Testable each quarter (Q1 was 8%, Rs15 cr). Feeds catalyst timeline. |
| F17-11 | F6 | C10, C13, M98, M99, M114 | 36, 64 | "monthly run rate will almost grow by 50% in the next uh 3 months" | FORWARD-SIGNAL | Dated capacity commitment: AC-charger monthly run-rate +50% within 3 months (by ~Nov 2026). A near-term, verifiable milestone. Note it is a run-rate claim, not a revenue guarantee. |
| F17-12 | F7 | H10, M120-M122 | 98 | "we're doing one foot of that today"; "the turnaround which is underway and hopefully the frag end of it" | AMBIGUOUS | US/Tritium plant running at ~25% ("one foot" ≈ one-fourth) of the 2.5x capacity — i.e. heavy fixed-cost under-absorption underpinning the consol EBITDA loss. Turnaround "underway", timing hedged with "hopefully". A4: quantify Tritium plant utilization and the fixed-cost drag until legacy backlog + strategic projects fill it. |
| F17-13 | F17 | M40-M42, monitoring 8 | 18 | "Delhi has outlaid 4 years 15,000 cr EV policy to... put in almost 30,000 plus EV charging points" | AMBIGUOUS | Delhi EV policy cited as an industry tailwind but with ZERO quantified Exicom/EVSE-India order-book impact from the aggregator fleet mandate (monitoring item 8 only partially addressed). A4: convert to a question on named Delhi orders won/pipeline. |
| F17-14 | F6 | opening remarks | 18 | "from quarter four we also expect to start supplying decommissioned batteries to a large... tower companies" | FORWARD-SIGNAL | Dated revenue stream deferred to Q4 FY27 only ("most of that will only come in the last quarter"). Back-half-loaded; adds to the H2-FY27 execution concentration risk already visible in BharatNet and Tritium timing. |
| F17-15 | F7 | H9, M118 | 80 | "this is uh uh my my estimation not from research report but I think for charger share still would be north of 50%" | NEUTRAL-FACT | Blended market-share figure explicitly flagged by management as personal estimate, not researched. Do not carry the "north of 50%" as anchored evidence; the only sourced share number is the 60% DRHP wallbox figure (historical). |

Findings flagged for A4 to convert into management questions (FORWARD-SIGNAL + AMBIGUOUS): F17-02, F17-03, F17-04, F17-05, F17-06, F17-07, F17-10, F17-11, F17-12, F17-13, F17-14.

---

## F17 SILENCE AUDIT — "WHAT WAS NOT DISCUSSED" (PRIORITY)

11 carried-forward monitoring questions cross-referenced against turns 14-112. Silence baseline: all were already unaddressed at the May Q4 FY26 call, so "not discussed" now = 2nd consecutive quarter.

| # | Monitoring question | Status this call | Cite | Consec. quarters silent | Note |
|---|---|---|---|---|---|
| 1 | FY27 fresh capital raise needed? net-debt ceiling | PARTIAL | 20 | 2 (on the ceiling) | CFO asserts "adequate headroom to fund both growth investment and working capital"; no net-debt ceiling, no raise decision. Headroom claim, not an answer. |
| 2 | Note 5 — name 7.8% Tritium-holdco foreign holder, implied valuation, OCD origin | NOT DISCUSSED | — | 2 | Zero mention of the minority holder or Tritium implied valuation anywhere. |
| 3 | Tritium contracted vs opportunity revenue; reconcile backlog to "3x" | PARTIAL | 34 | 2 | $20M backlog + 3x reaffirmed, but no contracted-vs-opportunity split; "large strategic opportunities... hoping to convert" left un-sized. |
| 4 | Hyperscaler FAT sign-off date + binary milestone | PARTIAL | 18 | 2 | Grid Flex "being tried at a hyperscale customer... subject to successful trials" — hyperscaler referenced but NO FAT date, NO binary milestone. |
| 5 | Payable-days / bill-discounting durability | NOT DISCUSSED | — | 2 | CFO covered inventory + receivables WC only; payables/bill-discounting untouched. |
| 6 | Standalone ~10.6% margin sustainability into FY27 | PARTIAL / ADVERSE | 18, 20 | 2 | Not addressed forward; the printed 8.8% is already ~180 bps below the 10.6% being monitored (see F17-08). |
| 7 | Corporate Promoter loan (Note 4) status / residual RPTs | NOT DISCUSSED | — | 2 | No RPT / promoter-loan reference at all. |
| 8 | EVSE India order-book impact from Delhi aggregator fleet mandate (quantified) | PARTIAL | 18 | 2 | Delhi policy cited as tailwind; no quantified Exicom order-book impact (see F17-13). |
| 9 | Tritium India positioning vs Delhi DCFC tenders (named customers) | NOT DISCUSSED | — | 2 | No Tritium-India-vs-Delhi-tender discussion, no named DCFC customers. |
| 10 | Manufacturing capacity for Indian-made DCFC under Tritium brand (Hyderabad Tritium line) | NOT DISCUSSED | — | 2 | Hyderabad discussed only as Exicom AC/DC line; no Tritium-brand India DCFC line mentioned. |
| 11 | EVSE India FY27 revenue guidance revision | PARTIAL | 46 | 2 | Directional only ("mix... similar", 70/30 or 65/35, growth vs last year); explicit "I don't want to commit on the target"; no revised number. |

Fully silent (2nd consecutive quarter, confirmatory negative): items 2, 5, 7, 9, 10 (=5).
Partial / deflected: items 1, 3, 4, 6, 8, 11 (=6).

### Pre-committed metric assessment
The May-set "single cleanest metric" was consol quarterly EBITDA >= 0 through the soft quarter (Bull >=0; Bear < -Rs20 cr). Q1 FY27 printed ~ -Rs22 cr (M8 "22 1/2 cr", M79 "21.9 Ks"), breaching the -Rs20 cr Bear line and reversing the Q4 FY26 +Rs0.3 cr breakeven. Management framing (turn 30): seasonality (Q4 is the peak quarter) plus erosion of low-cost inventory acquired with Tritium ("earlier enjoying unreasonably high margins... now... not as high"). Neither driver was quantified, and the framing avoids the structural question of whether Tritium's normalized gross margin is permanently lower. Breakeven re-guided to consolidated Q2 OR Q3 FY27 and Tritium Q4 FY27 — but the consolidated date is a soft band and the CFO could not narrow it ("I can't specify whether quarter two or three"). This is the BEAR outcome; flag prominently for A4.

---

## COMMITMENT REGISTER (F6)

| commitment | implied date | turn ref | status word |
|---|---|---|---|
| Tritium 3x revenue growth vs last year | FY27 | 34 (C9, M94) | reaffirmed/underway |
| Tritium EBITDA breakeven | Q4 FY27 | 30, 34, 56 (C7/C9/C12) | committed (dated) |
| Consolidated EBITDA breakeven | Q2 or Q3 FY27 | 30 (C8) | committed (soft band) |
| Critical-power exports 8% -> 15% of segment sales | within FY27 | 18 (C1, M19) | in progress (8% at Q1) |
| AC-charger monthly run-rate +50% | +3 months (~Nov 2026) | 36, 64 (C10/C13) | underway (+50% already achieved once, further +50% guided) |
| Tritium/Faradium fleet-trial contract $20-30M | CY27 (calendar) | 18 (C3, M51) | conditional ("if trials successful") |
| Grid Flex hyperscaler contract $20M | CY27 (calendar) | 18 (C4, M52) | conditional ("subject to successful trials") |
| Trials unlocking "double-digit large million dollar" orders | through CY2027 | 18 (C2) | in trial (mid-to-advanced) |
| Secure majority of CY27-execution orders | within calendar 2026 | 18 (C5) | targeted |
| BharatNet open orders Rs700 cr + Rs800 cr service | service over next 10 years | 18 (M22/M23) | open / to follow |
| BSNL phase-2 ~2,000 towers, Rs90-100 cr | FY27 (allocation pending "conversations") | 18 (M25-M27) | expected (not awarded) |
| Decommissioned-battery supply to tower cos | Q4 FY27 | 18 (F17-14) | expected (deferred to H2) |
| Charger order book ~180 to run | till October 2026 | 18 (C6, M45) | in execution |
| Tritium R&D revenue journey | next 5-7 years | 52 (C11) | asserted |
| Step-up in Tritium top-line/bottom-line starting point | Q4 FY27 | 56 (C12, M113) | committed (dated) |
| Results visible on standalone AND consolidated | "couple of quarters away" | 110 (C14) | closing framing |

## HEDGE REGISTER (F7)

| hedge | turn | pairs with |
|---|---|---|
| "profitability is still not in black" | 18 (H1) | F17-01 |
| "I don't want to commit on the target at this point" (EV charger export %) | 18 (H2) | commitment declined |
| "if these trials are successful" / "subject to successful trials" | 18 (H3) | F17-04, C3, C4 |
| "I can't specify whether quarter two or three" (consol breakeven) | 30 (H4) | F17-03, C8 |
| "large double-digit million numbers... which we are hoping to convert" | 34 (H5) | 3x claim / C9 |
| "some of the challenges today is not capacity, it's supply chain disruption" | 36 (H6) | utilization M100-M104 |
| "I will check this again... come back to you with an exact answer" (capacity figure) | 48 (H7) | F17-06, Q6 |
| "in business there are... too many factors" | 56 (H8) | C12 |
| "blended I would not know... my estimation, not from a research report" | 80 (H9) | F17-15, M118 |
| "hopefully the frag end of it" (US turnaround timing) | 98 (H10) | F17-12 |
| "I cannot say exactly about the accuracy of the report" (third-party 30-35% non-functional stat) | 106 (H11) | M127 |

---

## CHECKLIST SCORECARD (F1-F17)

| Check | Status | One-line basis |
|---|---|---|
| F1 Zero-value standing line items | N.A. | Concall transcript carries no standing financial line items; ledger flags ZERO_STANDING as not applicable to this doctype. |
| F2 Standalone vs consolidated decomposition | N.A. | No filed S/C statements in a concall; the discussed EV 50% (consol) vs 15% (standalone) gap is captured behaviourally, not decomposed here. |
| F3 Shell-entity detection | N.A. | Requires cost-line statements not present in a transcript. |
| F4 Unaudited contribution ratio | N.A. | No auditor Other-Matters paragraph in a concall. |
| F5 Going concern / EoM scope | N.A. | No auditor language on a concall; prior auditor unmodified, no EoM (Q4 FY26). |
| F6 Forward-commitment phrase mining | FINDING | 16 dated/dateable commitments mined into the Commitment Register; key ones F17-03, F17-10, F17-11, F17-14. |
| F7 Hedge phrase mining | FINDING | 11 hedges mined (Hedge Register); material conditional-forward and deferral hedges F17-04, F17-06, F17-12, F17-15. |
| F8 Tax forensics | N.A. | No ETR / deferred-tax detail spoken on the call. |
| F9 OCI forensics | N.A. | No OCI / actuarial disclosure on a concall. |
| F10 Share count and dilution | N.A. | No paid-up capital or share count spoken this call (task rule: N.A. unless mentioned). |
| F11 Reserves / net worth tie-out | N.A. | No equity/reserves figures spoken. |
| F12 Segment forensics | N.A. | No segment assets/liabilities on a concall (segment revenue only). |
| F13 Board outcome beyond results | N.A. | No board/AR/AGM/director-term items on this call. |
| F14 Note drafting inconsistencies | N.A. | No notes/auditor-letter text on a concall (speaker-level number discrepancy captured under F17-07). |
| F15 Entity list diffs | N.A. | No consolidation entity list on a concall; first quarterly-pipeline run, no prior extract to diff. |
| F16 Dropped/reframed disclosures | N.A. | Presentation-specific check; no prior-quarter deck/extract available to diff on this first run. |
| F17 Silence audit (concall-specific) | FINDING | Pre-committed metric hit the BEAR case (~ -Rs22 cr, F17-01); 5 monitoring items in full 2nd-consecutive-quarter silence (F17-09); debt basis contradiction (F17-05); plus F17-02/06/07/08/12/13. |

Every check marked exactly one of PASS / FINDING / N.A. No blanks. GATE A3: pass.

---

```yaml
stage: A3-forensics
company: "EXICOM"
quarter: "Q1 FY27"
doctype: "concall"
model: claude-opus-4-8
status: complete
forensics_path: "/home/user/inflection-pipeline/runs/exicom-q1fy27/work/forensics_concall_exicom_q1fy27.md"
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
  F14: N.A.
  F15: N.A.
  F16: N.A.
  F17: FINDING
findings:
  - {id: "F17-01", check: "F17", line: "18/20/28", classification: "CONFIRMATORY-NEGATIVE", implication: "Pre-committed metric printed BEAR (~ -Rs22 cr consol EBITDA), reversing Q4 FY26 +Rs0.3 cr breakeven; T1 did not confirm."}
  - {id: "F17-02", check: "F17/F7", line: "18/30", classification: "AMBIGUOUS", implication: "Reversal framed as seasonality + Tritium acquired-inventory run-off, not structural; unquantified. Is the Tritium GM reset permanent?"}
  - {id: "F17-03", check: "F6/F17", line: "30/34", classification: "FORWARD-SIGNAL", implication: "Dated breakevens: consol Q2 or Q3 FY27 (soft band), Tritium Q4 FY27; earliest testable = Q2 FY27 print."}
  - {id: "F17-04", check: "F7", line: "18", classification: "AMBIGUOUS", implication: "Tritium $20-30M + Grid Flex $20M CY27 wholly conditional on trials; no FAT date / binary milestone (monitoring Q4 unmet)."}
  - {id: "F17-05", check: "F17", line: "20", classification: "AMBIGUOUS", implication: "Consol debt Rs370 cr contradicts prior Rs649 cr incl-lease / Rs378 ex-lease; basis unstated (gross vs net vs ex-lease). Ask management."}
  - {id: "F17-06", check: "F7", line: "44/46/48", classification: "AMBIGUOUS", implication: "AC capacity 42,000 (AR) vs 48,000 vs 220,000 not reconciled; ANSWER_DEFERRED 'will check and come back'."}
  - {id: "F17-07", check: "F17", line: "18/20", classification: "AMBIGUOUS", implication: "Critical power stated 73%/Rs177 (CEO) vs 80%/Rs176 (CFO) same call; 7-pt growth spread not pure rounding."}
  - {id: "F17-08", check: "F17", line: "18/20", classification: "CONFIRMATORY-NEGATIVE", implication: "Standalone EBITDA margin 8.8%, ~180 bps below the 10.6% being monitored; sustainability never addressed forward."}
  - {id: "F17-09", check: "F17", line: "silence", classification: "CONFIRMATORY-NEGATIVE", implication: "Five monitoring items (2,5,7,9,10) in full 2nd-consecutive-quarter silence; sustained silence = confirmatory negative per Role 5."}
  - {id: "F17-10", check: "F6", line: "18", classification: "FORWARD-SIGNAL", implication: "Critical-power exports 8% -> 15% within FY27; testable quarterly (Q1 was 8%/Rs15 cr)."}
  - {id: "F17-11", check: "F6", line: "36/64", classification: "FORWARD-SIGNAL", implication: "AC-charger monthly run-rate +50% within 3 months (~Nov 2026); near-term verifiable milestone."}
  - {id: "F17-12", check: "F7", line: "98", classification: "AMBIGUOUS", implication: "US/Tritium plant ~25% utilized ('one foot'); fixed-cost under-absorption drives consol loss; turnaround timing hedged 'hopefully'."}
  - {id: "F17-13", check: "F17", line: "18", classification: "AMBIGUOUS", implication: "Delhi Rs15,000 cr EV policy cited as tailwind with zero quantified Exicom/EVSE order-book impact (monitoring 8 partial)."}
  - {id: "F17-14", check: "F6", line: "18", classification: "FORWARD-SIGNAL", implication: "Decommissioned-battery revenue deferred to Q4 FY27; adds to H2-FY27 execution concentration."}
  - {id: "F17-15", check: "F7", line: "80", classification: "NEUTRAL-FACT", implication: "'North of 50%' market share explicitly a personal estimate, not researched; do not carry as anchored evidence."}
forward_signals: ["F17-03", "F17-10", "F17-11", "F17-14"]
ambiguous: ["F17-02", "F17-04", "F17-05", "F17-06", "F17-07", "F17-12", "F17-13"]
commitments:
  - {commitment: "Tritium 3x revenue growth vs last year", implied_date: "FY27", ref: "turn 34 / C9", status_word: "reaffirmed"}
  - {commitment: "Tritium EBITDA breakeven", implied_date: "Q4 FY27", ref: "turn 30/34/56 / C7", status_word: "committed"}
  - {commitment: "Consolidated EBITDA breakeven", implied_date: "Q2 or Q3 FY27", ref: "turn 30 / C8", status_word: "committed-soft"}
  - {commitment: "Critical-power exports 8% -> 15% of segment sales", implied_date: "within FY27", ref: "turn 18 / C1", status_word: "in-progress"}
  - {commitment: "AC-charger monthly run-rate +50%", implied_date: "+3 months (~Nov 2026)", ref: "turn 36/64 / C10", status_word: "underway"}
  - {commitment: "Tritium/Faradium fleet-trial contract $20-30M", implied_date: "CY27", ref: "turn 18 / C3", status_word: "conditional"}
  - {commitment: "Grid Flex hyperscaler contract $20M", implied_date: "CY27", ref: "turn 18 / C4", status_word: "conditional"}
  - {commitment: "Trials unlocking double-digit million-dollar orders", implied_date: "through CY2027", ref: "turn 18 / C2", status_word: "in-trial"}
  - {commitment: "Secure majority of CY27-execution orders", implied_date: "within CY2026", ref: "turn 18 / C5", status_word: "targeted"}
  - {commitment: "BharatNet Rs700 cr open + Rs800 cr service", implied_date: "service over 10 years", ref: "turn 18 / M22-M23", status_word: "open"}
  - {commitment: "BSNL phase-2 ~2,000 towers Rs90-100 cr", implied_date: "FY27", ref: "turn 18 / M25-M27", status_word: "expected"}
  - {commitment: "Decommissioned-battery supply to tower cos", implied_date: "Q4 FY27", ref: "turn 18", status_word: "expected"}
  - {commitment: "Charger order book ~180 to run", implied_date: "till October 2026", ref: "turn 18 / C6", status_word: "in-execution"}
  - {commitment: "Tritium R&D revenue journey", implied_date: "next 5-7 years", ref: "turn 52 / C11", status_word: "asserted"}
  - {commitment: "Tritium top-line/bottom-line step-up starting point", implied_date: "Q4 FY27", ref: "turn 56 / C12", status_word: "committed"}
  - {commitment: "Results visible standalone AND consolidated", implied_date: "couple of quarters away", ref: "turn 110 / C14", status_word: "framing"}
gate_a3: pass
blank_checks: []
```
