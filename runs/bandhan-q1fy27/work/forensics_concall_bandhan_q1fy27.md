# FORENSIC NOTES — A3 — BANDHAN — Q1 FY27 — Doctype: concall (earnings call)

Source extract: runs/bandhan-q1fy27/work/extract_concall_bandhan_q1fy27.txt (70 turns, 206 source lines)
Ledger reconciled: runs/bandhan-q1fy27/work/ledger_concall_bandhan_q1fy27.md
Ledger reconciliation: 100% — every ledger row (Sections 1-7, all flags in the Summary block) read verbatim at its cited line before judging. Line citations below follow the ledger's turn/line convention.

Doctype handling: this is a concall, so the balance-sheet / auditor checks (F2, F3, F4, F5, F8, F9, F10, F11, F13, F15) are N.A. with a one-line reason each. The concall-relevant checks are applied in full per the task brief: forward commitments (F6), hedge/tone (F7), segment strategy (F12), attribution/naming inconsistency (F14), guidance-change & internal-numeric consistency (F16, applied in its concall sense), and the silence audit (F17). F1 is addressed against the one ZERO_STANDING ledger row.

---

## HEADLINE (flagged for A4/A5)
The marquee event is a **ROA guidance cut of ~40 bps** — aspiration lowered from 1.6-1.8% to **1.2-1.4% at exit Q4 FY27**, with the timeline itself pushed out ("could extend beyond the timeline we had originally envisaged"). Management attributes the cut **100% to external factors** (energy crisis / Middle East war, funding cost, tech cost +65%) and explicitly denies any internal driver ("no internal factors has any impact", turn 7/line 105). The forensic tension: analysts repeatedly probe an unexplained residual (the "other 20 bps", Q5a) and an opex-to-asset ratio **already breached** (4.3% actual vs a guide variously stated as 4% and 4.2%), both of which point to internal cost overreach that the external-only narrative downplays.

**Notion tripwires touched:** #2 wholesale segment (explicitly acknowledged ROA/margin-dilutive, +38% YoY, 33% of advances — see F-04). CASA 29.4% (tripwire #4 <27% NOT breached). Credit cost 1.8% / EB 3.3% (tripwire #1 >2.5% — bank level clear; EB level elevated but guidance 1.6-1.8% maintained). Governance churn (tripwire-adjacent): a "New EB head Surojit" surfaces (turn 19) and CFO succession is met with total silence (see F-10).

---

## FINDINGS TABLE

| id | check | ledger row ref | line/turn | short verbatim quote | classification | forward implication |
|----|-------|----------------|-----------|----------------------|----------------|---------------------|
| F-06 | F16 | Sec4 turn 3/69 GUIDANCE_CHANGE; turn 35/161 KEY BRIDGE | TURN 3 / line 69; TURN 35 / line 161 | "an ROA in the range of 1.2% to 1.4% at the exit of Q4 FY27 would be probable"; bridge "roughly around 30 basis points stretch... on NIMs and roughly around 10 basis point stretch... on the opex" | FORWARD-SIGNAL | FY27 exit ROA reset 40bps lower AND timeline slipped ("could extend beyond the timeline we had originally envisaged"). Even the reduced 1.2-1.4% band starts from a 1.0% (1.1% ex-gratuity) base with NIM only "held", so the bridge to 1.4% rests on ~20bps other-income + marginal credit-cost gains — thin. Model the low end. |
| F-07 | F16 | Sec4 turn 26/143 & turn 35/161 GUIDANCE_VS_ACTUAL | TURN 26 / line 143 (MD "4%"); TURN 35 / line 161 & TURN 43 / line 177 (CFO "4.2%") | MD: "OPEX we had said should be 4%, but already we have reached 4.3 in Q1"; CFO: "our guidance was that opex to asset ratio would be around 4.2% but we've already seen it hovering around 4.3%" | FORWARD-SIGNAL | Two guided baselines (4% vs 4.2%) cited by two speakers on the same call for the same metric, and the metric is ALREADY breached at 4.3% with management saying "this is going to continue" (turn 26). Opex is a live, worsening drag, not a one-quarter blip — the +10bps opex leg of the ROA cut is likely understated. |
| F-08 | F16 | Sec4 turn 35/161 (NIM path) | TURN 35 / line 161 | "we had a line of sight towards wanting to go towards 6.5% by the end of Q4 FY27, but given that the cost of funds... has gone up... our revised guidance is to see how exactly we can maintain" | FORWARD-SIGNAL | The prior 6.5% NIM ceiling is quietly withdrawn; new bar is merely holding 6.2% ("great achievement... to hold on to the NIMs", turn 17). Savings-bank CoF already +20-25bps (turns 7, 34); Q1 benefit "may not be available Q2 onwards". NIM downside, not upside, is the base case for FY27. |
| F-09 | F16 | Sec4 NUMBER_DISCREPANCY (ARC 291 vs 290; gratuity 61 vs 60) | TURN 4 / line 87 (291); TURN 65 / line 221 (290); gratuity TURN 4/93 & 60/211 (61) vs TURN 16/123 analyst (60) | "sale of 291 crore of housing NPA loans to an ARC" vs "ARC sale of the housing finance portfolio amounting to roughly 290 crore" | NEUTRAL-FACT | ARC quantum 291 vs "roughly 290" is a rounding within one call — immaterial but logged; recoveries this quarter include ~120cr ARC-linked cash, i.e. the flattering recovery/upgrade number is partly one-off, not run-rate (relevant to Q9b). Gratuity 61 vs 60 is an analyst mishearing, NOT a management restatement (mgmt consistent at 61cr). |
| F-01 | F6 | Sec6 phrases #5,7,10,14,15,16,17; Sec4 turns 19,40,41,46,63 | multiple (register below) | e.g. "the credit card we are just waiting to launch, probably in this quarter or year" (turn 40/171); "after 18 months or so we should see the outcome" (turn 55/201) | FORWARD-SIGNAL | 11 dateable management commitments extracted (register below). Feed Role 5 promise-vs-delivery tracker. Key milestones: LOS build + branch-channel sourcing (200cr/mo -> >900cr/qtr, status: underway), credit card launch (Q2FY27/FY27), other-income +10-20bps (FY27), opex efficiencies only "beyond FY28". |
| F-02 | F7 | Sec6 (11 of 19 phrases are HEDGE-type) | TURN 3 / line 69; TURN 17 / line 125; TURN 34 / line 159 | "the realization of this aspiration could extend beyond the timeline"; "it will be a great achievement for the bank to hold on to the NIMs"; "the actual impact will be felt 2-3 months later... remains difficult to assess at this stage" | FORWARD-SIGNAL | Hedge/uncertainty density is high and clustered on ROA/NIM/opex — every forward metric is qualified ("probable", "may hold good", "great achievement to hold", "difficult to assess"). Pre-emptive lowering of the bar: read as management signalling further guidance risk into Q2 FY27. |
| F-03 | F7 | Sec4 turn 7/105; turn 3/69 (repeated external attribution) | TURN 7 / line 105 | "this is on account of the external factors and no internal factors has any impact on devising the guidance" | AMBIGUOUS | External-only causal framing is asserted at least three times (turns 3, 7, 26) yet contradicted by the same speaker admitting past internal "lacuna or gaps" (turn 3/line 71) and by an internally-driven opex breach (F-07) and a self-chosen margin-dilutive wholesale build (F-04). Attribution is not fully external. -> A4 question: quantify the internal (opex overreach + mix) contribution to the 40bps. |
| F-04 | F12 | Sec4 turn 4/75-77 (wholesale +38%, 33% of book); turn 46/183 | TURN 45 / line 181 (analyst); TURN 46 / line 183 (mgmt) | analyst: "growing at about 35-40%... why you are growing this business given margins are diluting"; mgmt: "right now definitely the ROA is less because I have to lend to these big corporates... at very competitive rates" | AMBIGUOUS | Management concedes wholesale (33% of advances, +38% YoY, "0% ROA" per analyst framing of secured book) is margin/ROA-dilutive today, justified only by HOPED-FOR future other income (forex/LC/trade "gradually entering"). Touches Notion tripwire #2 (wholesale segment loss > Rs400cr FY27). -> A4 question: current wholesale segment ROA and the fee-income offset actually booked to date. |
| F-05 | F14 | Sec1 SPEAKER_UNATTRIBUTED (turns 24,41,47,63); Sec4 turn 19 | TURN 47 / line 185 ("Satish"); TURN 19 / line 129 ("New EB head Surojit") | "[Satish]: The book we are building in wholesale banking..."; "[New EB head Surojit:] Presently we continue to be at around 40" | AMBIGUOUS | Two named executives (Satish; "New EB head Surojit") speak/are cited but appear NOWHERE in the MANAGEMENT PRESENT header (5 named only); four management turns (24, 41, 47, 63) are unattributed; header even carries a dual surname for the MD ("Partha Pratim Singh Gupta (Sengupta)"). Cumulatively a governance/attribution data point; the "New EB head" wording is itself a personnel-change signal against the thesis's CXO-churn watch. -> A4: confirm EB-head change and its date. |
| F-10 | F17 | Notion monitoring checklist (inline) | whole transcript, lines 43-231 (absence) | (no line — item never raised) | CONFIRMATORY-NEGATIVE | Silence audit: CFO succession / Mantri last-working-day 25-Sep-26 NOT mentioned (Mantri answers as CFO throughout, zero reference to his departure); 25-Jun Capital Plan NOT discussed; Axis Bank Mantri disclosure NOT discussed; the 5th-CXO-in-24-months governance pattern NOT addressed (yet a new EB head appears, F-05). Sustained silence on CFO transition amid a ROA cut = confirmatory negative for governance instability. |

---

## CHECKLIST SCORECARD (all 17)

| Check | Status | One-line basis |
|-------|--------|----------------|
| F1  | PASS  | Only ZERO_STANDING ledger row is the "senior management team" header collective (Sec1 #6): a benign courtesy listing, no filing template line item exists on a concall; the substantive unattributed-speaker points are carried into F14/F-05. |
| F2  | N.A.  | Concall — no standalone-vs-consolidated statements presented. |
| F3  | N.A.  | Concall — no cost-line comparison / subsidiary structure disclosed. |
| F4  | N.A.  | Concall — no auditor Other Matters / unaudited-contribution disclosure. |
| F5  | N.A.  | Concall — no Going Concern / EoM paragraph; no prior-quarter extract supplied to diff. |
| F6  | FINDING | 11 dateable forward commitments extracted (F-01); commitment register below. |
| F7  | FINDING | High hedge density on ROA/NIM/opex (F-02) and external-only causal attribution contradicted by internal evidence (F-03). |
| F8  | N.A.  | Concall — no effective-tax-rate / deferred-tax disclosure. |
| F9  | N.A.  | Concall — no OCI / actuarial disclosure. |
| F10 | N.A.  | Concall — no share count / basic-vs-diluted EPS spread disclosed. |
| F11 | N.A.  | Concall — no Other Equity / net-worth tie-out (CAR 18.2% / Tier-1 17.5% stated but not reconcilable to net worth here). |
| F12 | FINDING | Wholesale banking (33% of advances, +38% YoY) conceded ROA/margin-dilutive; touches Notion tripwire #2 (F-04). |
| F13 | N.A.  | Concall — no AR/AGM/board-resolution/director-appointment outcome disclosed on the call. |
| F14 | FINDING | Off-header named speakers (Satish, "New EB head Surojit") + four unattributed management turns + dual MD surname (F-05). |
| F15 | N.A.  | Concall — no consolidation entity list to diff. |
| F16 | FINDING | Applied in concall sense: ROA cut (F-06), opex guidance-vs-actual inconsistency + breach (F-07), NIM 6.5% ceiling dropped (F-08), ARC/gratuity numeric discrepancies (F-09). |
| F17 | FINDING | Silence on CFO succession/Mantri exit, capital plan, Axis disclosure, CXO churn (F-10). |

No blank checks. GATE A3: pass.

---

## COMMITMENT REGISTER (from F6)

| # | commitment | implied date | note/turn ref | status word |
|---|------------|--------------|---------------|-------------|
| 1 | ROA 1.2-1.4% at exit Q4 FY27 (revised aspiration) | Q4 FY27 (may slip beyond) | TURN 3 / line 69 | guided (softened) |
| 2 | Credit growth 14% FY27 (EB 5-10%, non-EB 20%+) | FY27 | TURN 29 / line 149 | on-track (Q1 16%) |
| 3 | Credit cost 1.6-1.8% maintained | FY27 | TURN 37 / line 165 | reaffirmed |
| 4 | Other income +10-20bps uplift | FY27 | TURN 17 / line 125 | expected |
| 5 | IT cost held within ~10% of opex, then toward 8% | FY27 then multi-year | TURN 29 / line 149 | committed |
| 6 | EB book lifted to 5-10% growth (from flat) | as environment improves | TURN 53 / line 197 | intended |
| 7 | PSLC share to be moved up from ~40% | "over this quarter" (Q2 FY27) | TURN 19 / line 129 | initiated |
| 8 | Gold-loan sourcing back to normal, "take it up" | Q2 FY27 | TURN 63 / line 190 | recovering/underway |
| 9 | Credit card launch | "this quarter or year" (Q2/FY27) | TURN 40 / line 171 | pending launch |
| 10 | Branch-channel asset sourcing scale-up (200cr/mo -> >900cr/qtr; reduce DSA dependency) | ongoing | TURN 41 / line 173 | underway |
| 11 | IT productivity gains / opex tapering | "after 18 months" and "beyond FY28" | TURN 55 / line 201; TURN 43 / line 177 | future (not yet) |

Status-change note for Role 5: the branch-channel commitment (#10) shows a concrete milestone move (200cr/month -> >900cr/quarter) = "initiated -> underway" confirmation; opex efficiency (#11) is explicitly deferred to beyond FY28, i.e. no near-term relief.

---

## WHAT WAS NOT DISCUSSED (F17 silence audit)

| item (Notion monitoring checklist) | addressed? | consecutive-quarter silence | note |
|---|---|---|---|
| Replacement CFO / Mantri exit (LWD 25-Sep-26) | No | 1+ (this call) | Mantri presents/answers as CFO throughout; no reference to his departure or succession. Confirmatory negative given governance-churn thesis. |
| 25-Jun Capital Plan | No | 1+ | Not raised by management or analysts. |
| Axis Bank Mantri disclosure | No | 1+ | Not raised. |
| Governance: 5th CXO exit / 24 months; 2nd CFO / 3 years | No (indirect only) | 1+ | Not addressed; a "New EB head Surojit" instead surfaces without transition context (F-05). |
| CASA <27% tripwire | Yes | — | CASA 29.4% disclosed; above tripwire, not breached. |
| Credit cost >2.5% tripwire | Yes | — | Bank 1.8%; EB 3.3% (elevated but guidance 1.6-1.8% held). |
| Wholesale segment loss >Rs400cr tripwire | Partial | — | Wholesale growth/margin-dilution discussed; no segment P&L / loss figure given (F-04). |

---

## RECONCILIATION STATEMENT
All A2 ledger rows read verbatim at cited lines before judging: Participants (16), Turns (70), Questions (25), Management numbers (149 tokens grouped in 38 rows), Analyst numbers (13), Forward/hedge phrases (19), Targeted guidance figures (11), and every flag in the Summary block (MULTI_PART, REPEAT_QUESTION, MERGED_Q_A, ANALYST_NAME_NOT_GIVEN, FIRM_AMBIGUOUS, SPEAKER_UNATTRIBUTED, ZERO_STANDING, GUIDANCE_CHANGE x2, NUMBER_DISCREPANCY x2, GUIDANCE_VS_ACTUAL). Ledger reconciled 100%.
