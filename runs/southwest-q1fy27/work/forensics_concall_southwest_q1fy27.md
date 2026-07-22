# A3 FORENSIC NOTES — SOUTHWEST (South West Pinnacle Exploration Ltd) — Q1 FY27 — CONCALL

Source extract: `extract_concall_southwest_q1fy27.txt` (187 lines, verbatim ASR, uncorrected).
Ledger: `ledger_concall_southwest_q1fy27.md`. Prior-quarter extract: none (first concall for this ticker).
Ledger reconciliation: 100% — every A2 row (47 number rows / 83 turns / 35 strict + 7 implied questions /
14 participants / 18 curated hedge rows) read verbatim at its cited line before judging.
ASR garbles interpreted through the supplied glossary but CITED as the verbatim line.

Doctype note: on a concall F6/F7/F17 are the load-bearing checks; balance-sheet checks (F1, F3, F5, F8,
F9, F12, F13, F15) are largely N.A. because no statements/auditor letter/segment tables are filed with a
call. Where a call surfaced a check's substance anyway (JV consolidation for F2/F4, warrant conversion for
F10, the debt reconciliation for F11, presentation-vs-call conflicts for F16), the check is marked FINDING
with the caveat noted.

---

## FINDINGS TABLE

| id | check | ledger ref | line/turn | verbatim quote | classification | forward implication |
|----|-------|-----------|-----------|----------------|----------------|---------------------|
| F2-01 | F2 | Tbl4 r29; Tbl1 t11/t44 | line 47/109, turn 13/44 | "we don't add line by line revenue... we only add the profit figure in the consolidated balance sheet... 1.32 crores to be precise in this quarter" | FORWARD-SIGNAL | JV is equity-method; the 1.32 Cr share is ~14% of the 9.3 Cr consolidated PAT and carries no revenue/EBITDA — strip it to see the operating-only quality of the "best ever quarter". |
| F4-01 | F4 | Tbl4 r29 | line 109, turn 44 | "the profits are much higher... 1.32 crores to be precise in this quarter" | AMBIGUOUS | ~14% of PAT rests on JV numbers whose audited-vs-management-furnished status is never stated on the call (Role 4 Q16 open). Above the 10%-of-PAT trip. A4 question. |
| F6-01 | F6 | Tbl3 H1-H18; Tbl4 r16/r46 | multiple (see register) | "we will commence mine development activities... commencing coal production by the financial year 2829" | FORWARD-SIGNAL | 16 dated/dateable commitments extracted (register below) feed the Role 5 promise-vs-delivery tracker; DGR, mining plan, Oman JV2 GR and Reliance-extension start are the near-term milestones to check next quarter. |
| F6-02 | F6 | Tbl4 r22 | line 73/149, turn 26/64 | "in this town we've just kicked off... one and a half months back... maybe it would take around 3 months and then onwards for the next three and a half four years" | FORWARD-SIGNAL | HZL Rs 307 Cr order (~40% of the 761 Cr book) contributes MINIMALLY to Q1; it is the FY25 award only now commencing, not fresh inflow. Contradicts the deck's "all-time-high order book" framing as a Q1 revenue driver. HZL segment-rev buy-gate (>Rs 15 Cr) cannot be cleared from this call. |
| F7-01 | F7 | Tbl3 H8 | line 77/79, turn 28/29 | "we cannot divulge uh this detail... this is the confidential detail... we can't diverge this figures" | CONFIRMATORY-NEGATIVE | Management REFUSED Reliance and HZL as % of Q1 revenue. The refusal itself is the finding: concentration is being managed as undisclosed. |
| F7-02 | F7 | Tbl3 H9/H10; Tbl4 r30 | line 69/111/145, turn 24/45/62 | "Q1 you will see generally subdued as compared to Q4 and Q2... our business is quite dynamic and quite cyclical... Let's hope for the best" | CONFIRMATORY-NEGATIVE | Management EXPLICITLY validates the Role 4 seasonality / exit-pace flag: H1 weakest, H2 strongest, Q1<Q4 and Q1<Q2. Do not annualise Q1 x4. |
| F10-01 | F10 | Tbl4 r3 (75%) | line 27/183, turn 3/81 | "the balance 75% consideration against warrant issued on preferential basis was also received resulting in their conversion into equity shares" | AMBIGUOUS | Warrant dilution crystallised THIS quarter but no post-conversion share count or basic/diluted EPS given (Role 4 Q5 open). Future promoter dilution left open: "it all depends future... which we cannot answer right now" (line 183). |
| F11-01 | F11 | Tbl4 r28/r47; r30 | line 93/181/111, turn 36/80/45 | "it is around around 15 crores at the moment with a very good debt equity of less than 39" | AMBIGUOUS | Management debt ~15 Cr / D/E <0.39 vs the presentation's gross borrowings ~78.6 Cr / net debt ~77 Cr — a >5x reconciliation gap. Candidate reconciling items: net-of-cash, fund vs non-fund-based, or an ASR mis-statement. Garbled "78 versus 62" (line 111) may be gross-debt-78 vs revenue-62. A4 question; do not accept the "getting to debt-free" line until reconciled. |
| F14-01 | F14 | Tbl4 r11/r44 | line 47 vs 173, turn 13 vs 76 | "$125 million million 10-year contract" (line 47) vs "11-year contract of 125 million" (line 173) | AMBIGUOUS | Alara/Oman JV1 headline contract stated as both 10-year and 11-year within one call, unreconciled. Immaterial alone; a governance/data-hygiene point that also gates any DCF of the JV cash. |
| F14-02 | F14 | Tbl1 t34; Tbl4 r26 | line 89, turn 34 | "that's a listed entity in Australia where I'm also the director in the company" | NEUTRAL-FACT | Related-party: CMD sits on the Alara Resources (Australia) board while SWPD subscribes to Alara's rights issue (Rs 2.8 Cr, up to 1M AUD) and holds all three Oman JVs with Alara. Related-party capital allocation; monitor sizing and independence of the decision. |
| F16-01 | F16 | Tbl4 r47; r3/r16/r46 | line 181, turn 80 | "the presentation makes a reference to commencing coal production in 2728 but... we are expecting revenue only in 2829... that understanding would be right correct yeah" | FORWARD-SIGNAL | Coal timeline CONFLICT: presentation FY27-28 vs concall FY28-29, stated FY28-29 four times (lines 27, 59, 179, 181), an analyst forced confirmation. Resolve toward FY28-29. This CONTRADICTS the Role 4 F6.1 read that coal was "earlier than FY29" — coal optionality slips a year; de-rate near-term. |
| F16-02 | F16 | Tbl4 r3/r21/r24; r35 | line 27/79/131 | "Our total order book has reached an all-time high of INR 761 crores" vs "this is from the past contract... work has not started yet. It should be starting this quarter" | AMBIGUOUS | Order-book framing: the 761 Cr headline mixes a not-yet-started Reliance CBM extension (line 131) and a just-commenced HZL order (line 73). Concentration confirmed: "almost these two contracts... cover about 60% of the total order book... 60% of the revenue are coming from these two contracts" (line 79). Burn/conversion schedule not given. |
| F17-01 | F17 | Tbl4 r30; silence | line 105/111, turn 42/45 | "the actual cash received is what the dividend... repetration will gradually happen once... everything is stabilized... it is happening now it will happen very soon" | CONFIRMATORY-NEGATIVE | THE decisive gate. NO CFO, NO CFO/PAT number given anywhere on the call. JV cash NOT yet repatriated -> the 1.32 Cr JV share (~14% of PAT) is NON-CASH this quarter. All three verify-and-buy gates (CFO/PAT>0.50, HZL seg-rev>Rs 15 Cr, receivable days<=185) are UN-CLEARABLE from this call. |
| F17-02 | F17 | Tbl3 H8; Tbl4 r24 | line 79/123, turn 29/51 | "it is difficult for us to give exactly what is coming out of coal right now" | CONFIRMATORY-NEGATIVE | Three explicit refusals compounded: (a) Reliance & HZL % of Q1 revenue "confidential" (line 77); (b) coal % of order book/revenue "difficult to give" (line 123); (c) actual JV cash received "declined/deflected" (line 111). Sustained opacity on the exact metrics that gate the buy. |

---

## CHECKLIST SCORECARD (all 17, exactly one status each)

| Check | Status | Basis (one line) |
|-------|--------|------------------|
| F1 ZERO-VALUE STANDING ITEMS | N.A. | No line-item template on a concall; A2 `zero_standing: 0`. Nothing to interrogate. |
| F2 STANDALONE vs CONSOLIDATED | FINDING | Mgmt confirmed equity-method JV: 1.32 Cr share (~14% of 9.3 Cr PAT), no line-by-line revenue (line 47/109). See F2-01. |
| F3 SHELL-ENTITY DETECTION | N.A. | No standalone-vs-consolidated cost lines disclosed on a call; cannot compare Cost of Materials/Employee/Depreciation. |
| F4 UNAUDITED CONTRIBUTION RATIO | FINDING | JV share 1.32 Cr > 10%-of-PAT trip; audited vs mgmt-furnished status never stated (line 109). See F4-01. |
| F5 GOING CONCERN / EoM SCOPE | N.A. | No auditor EoM on a call; no prior-quarter transcript to verbatim-diff. |
| F6 FORWARD-COMMITMENT MINING | FINDING | 16-row commitment register extracted (coal FY28-29, DGR, mining plan, Oman JV2 GR, Reliance-ext start, rig orders). See F6-01/F6-02 + register. |
| F7 HEDGE PHRASE MINING | FINDING | "confidential/cannot divulge" concentration hedge + "cyclical/subdued Q1/hope for the best" seasonality hedges. See F7-01/F7-02. |
| F8 TAX FORENSICS | N.A. | No ETR, no deferred-tax sign, no "earlier years" line disclosed; only headline PAT 9.3 Cr. |
| F9 OCI FORENSICS | N.A. | No OCI figure/actuarial detail on the call (Role 4 Q11 OCI swing is a silence item, logged in F17). |
| F10 SHARE COUNT & DILUTION | FINDING | Warrant balance 75% received -> conversion completed this quarter; no post-conversion count/EPS; promoter dilution left open. See F10-01. |
| F11 RESERVES / NET WORTH TIE-OUT | FINDING | Debt ~15 Cr / D/E <0.39 (call) vs ~78.6 Cr gross / ~77 Cr net (deck) — >5x reconciliation gap. See F11-01. |
| F12 SEGMENT FORENSICS | N.A. | No segment assets/liabilities tables filed with a call; segment/vertical splits were requested and REFUSED (captured under F7-01/F17-02). |
| F13 BOARD OUTCOME BEYOND RESULTS | N.A. | No AR/AGM/record-date/director-term/board-resolution disclosed. Credit-rating upgrade CRISIL/"ISEL" BBB->BBB+ (line 93) noted as a neutral corporate event, not a board outcome; Ritolia Ind-vs-NE (Role 4 Q15) not addressed -> F17. |
| F14 DRAFTING INCONSISTENCIES | FINDING | 10-yr vs 11-yr Alara contract conflict; related-party CMD Alara directorship while subscribing Alara rights. See F14-01/F14-02. |
| F15 ENTITY LIST DIFFS | N.A. | No consolidation list on a call and no prior quarter to diff; new names (Alara Australia direct stake, AML JV) noted but not diff-able. |
| F16 PRESENTATION-REFRAME | FINDING | Call surfaces presentation-vs-call conflicts: coal FY27-28 vs FY28-29 and 761 Cr order-book framing vs not-started/just-started large orders. See F16-01/F16-02. (Caveat: deck content inferred from analyst statements on the call.) |
| F17 SILENCE AUDIT | FINDING | No CFO/CFO-PAT; JV cash not repatriated (non-cash); receivable days / OCI / EPS / cost composition / standalone PAT all silent; all three buy-gates un-clearable. See F17-01/F17-02 + tables below. |

Scorecard tally: FINDING x9 (F2, F4, F6, F7, F10, F11, F14, F16, F17); N.A. x8 (F1, F3, F5, F8, F9, F12, F13, F15); PASS x0; blanks 0. GATE A3 = pass.

---

## COMMITMENT REGISTER (from F6) — management promises with implied dates

| # | commitment | implied date | ref (line/turn) | status word |
|---|-----------|--------------|-----------------|-------------|
| C1 | Commence coal production, Jharkhand block | FY28-29 | line 59/27, turn 19/3 | underway (exploration completed) |
| C2 | Definite Geological Report submission to MoC | "early submission" (near-term) | line 27/51/115, turn 3/15/47 | underway ("under preparation") |
| C3 | Mining plan preparation & MoC approval | after DGR (FY27) | line 51, turn 15 | initiated (next step) |
| C4 | Environmental/forest clearance & mining lease | after mining plan | line 51, turn 15 | not started (sequenced) |
| C5 | Oman JV2 (exploration block) geological report | near-term | line 27/47, turn 3/13 | underway (airborne survey done) |
| C6 | Reliance CBM extension execution begins | "this quarter" (Q2 FY27) | line 131, turn 55 | initiated ("should be starting this quarter") |
| C7 | Oil India (2024, Rs 60 Cr) last phase revenue | "this quarter" (Q2 FY27) | line 139, turn 59 | underway ("under execution") |
| C8 | Aquifer-mapping balance 35% completion | "after the monsoon" (H2 FY27) | line 141, turn 60 | underway (65% done) |
| C9 | Additional drilling rigs/equipment delivery | near-term | line 27/127, turn 3/53 | initiated (POs placed) |
| C10 | Alara Australia rights-issue subscription | ongoing | line 85, turn 32 | underway (up to 1M AUD) |
| C11 | JV cash repatriation to SWPD | "very soon" (undated) | line 111, turn 45 | initiated/pending — KEY, non-cash until done |
| C12 | ~20% medium-term revenue CAGR / "significant growth" FY27 | FY27+ | line 69/143, turn 24/62 | guidance |
| C13 | Maintain ~24% margin | FY27 | line 171, turn 75 | guidance ("hopeful") |
| C14 | Reliance = 35-40% (+/-5%) of FY27 revenue | FY27 | line 155/157, turn 67/68 | guidance |
| C15 | Getting toward debt-free | "next 2-3 years" | line 181, turn 80 | guidance |
| C16 | AML/Oman + Jharkhand coal revenue; ~Rs 200 Cr total invest | ~2030 (AML/Oman); FY28-29 (coal) | line 179, turn 79 | contingent ("depends on exploration results") |

---

## ANSWERED vs EVADED AUDIT — Role 4 open questions (1-19)

| # | Question | Verdict | line/turn | note |
|---|----------|---------|-----------|------|
| 1 | CFO / CFO-PAT | EVADED | line 105/111, t42/45 | No CFO given; deflected to "we mention in the balance sheet". Non-cash JV. |
| 2 | HZL/Rajasthan Q1 recognition split | PARTIAL (quantum EVADED) | line 73/77, t26/28 | "just kicked off 1.5 months back, ~3 months to gear up" = minimal Q1; exact % refused. |
| 3 | Receivable/debtor days | NOT ADDRESSED | — | Total silence. |
| 4 | Standalone PAT & S-vs-C gap | PARTIAL | line 109, t44 | Only consolidated 9.3 Cr; JV share 1.32 Cr named; no standalone. |
| 5 | Post-warrant share count / basic EPS | NOT ADDRESSED | line 27, t3 | Conversion confirmed; no count/EPS. |
| 6 | Coal GR date & FY27-28 vs FY29 | ANSWERED | line 27/181, t3/80 | GR "under preparation"; production FY28-29, conflict resolved toward FY29. |
| 7 | New rig capex amount/timeline | PARTIAL | line 27/127, t3/53 | "placed orders / raised POs"; no Rs amount or date. |
| 8 | Order-book conversion/burn & ~59% concentration | PARTIAL | line 39/79, t9/29 | Concentration confirmed (60% book & revenue); no burn schedule. |
| 9 | RIL % of revenue/book | PARTIAL (Q1 % EVADED) | line 77/155, t28/67 | Q1 % refused; forward 35-40% +/-5% FY27 given. |
| 10 | Oman JV2 timeline / Alara structure / stake | ANSWERED | line 43-89/175, t11-34/77 | Two JVs, 35% JV1, 1.25% direct Alara, 17.5% AML, 1400 sqkm, rights 2.8 Cr; 10/11-yr ambiguity remains. |
| 11 | OCI swing nature | NOT ADDRESSED | — | Total silence. |
| 12 | Net worth / D-E / ROE-ROCE + ROCE 23-vs-16 | PARTIAL | line 93/181, t36/80 | D/E <0.39 given (debt figure conflicts deck); no net worth/ROE/ROCE. |
| 13 | Cash-tax outflow | NOT ADDRESSED | — | Total silence. |
| 14 | QoQ vs Q4 FY26 / seasonality | ANSWERED (confirmatory) | line 69/111/145, t24/45/62 | H1 weakest, Q1<Q4 & Q1<Q2, cyclical, monsoon. Validates Role 4 flag. |
| 15 | Ritolia Independent-vs-Non-Executive | NOT ADDRESSED | — | Total silence. |
| 16 | JV audited vs mgmt-furnished + catch-up vs run-rate | PARTIAL / NOT ADDRESSED | line 109, t44 | Share named; audited status and run-rate not stated; "much higher" claim internally inconsistent (1.32<1.5). |
| 17 | Intangibles-under-development | NOT ADDRESSED | — | Total silence. |
| 18 | OIL empanelment pipeline | PARTIAL | line 27/139, t3/59 | Empaneled for 2D/3D seismic; old 2024 OIL 60 Cr (~20 left) under execution; empanelment not a booked order. |
| 19 | Cost composition & margin durability | PARTIAL | line 171, t75 | Margin ~24% "maintainable", entry barriers high; no cost composition. |

EVASIONS explicitly flagged as findings (per emphasis): Q1 (CFO), Q2/Q9 (RIL/HZL % "confidential"), Q1/Q16 (actual JV cash repatriated), coal % of book/revenue (line 123). See F7-01, F17-01, F17-02.

---

## "WHAT WAS NOT DISCUSSED" — F17 silence audit (Notion monitoring checklist)

First concall for this ticker, so consecutive-quarters-of-silence = 1 (baseline) unless noted.

| Monitoring item | On the call? | line if partial |
|-----------------|--------------|-----------------|
| CFO / operating cash flow & CFO/PAT | SILENT (decisive) | — |
| HZL segment revenue recognised (buy-gate >Rs 15 Cr) | REFUSED / implied minimal | line 73/77 |
| Receivable / debtor days (buy-gate <=185) | SILENT | — |
| Segment liabilities | SILENT | — |
| Coal GR + mine timeline | ADDRESSED (FY28-29) | line 27/181 |
| RIL concentration % (Q1) | REFUSED "confidential" | line 77 |
| Oman JVs | ADDRESSED | line 43-89 |
| Order-book conversion/burn | PARTIAL (concentration only) | line 79 |
| Accreditation / OIL empanelment | PARTIAL | line 27/139 |
| Warrant dilution / EPS | PARTIAL (event yes, EPS no) | line 27 |
| Standalone-vs-consolidated & unaudited-JV share | PARTIAL (JV share yes; audited status no) | line 109 |
| Cost composition / margin durability | PARTIAL (qualitative) | line 171 |

Three binding verify-and-buy gates status from this call: CFO/PAT>0.50 = UN-CLEARABLE (no CFO); HZL seg-rev>Rs 15 Cr = UN-CLEARABLE (minimal Q1, refused quantum); receivable days<=185 = UN-CLEARABLE (silent). Position is WATCHLIST/BUY, NOT held; no tripwire fired, but none of the three buy conditions is satisfiable on this transcript — the call does not move the ticker to buy.

---

## NOTE FOR A4 (questions to convert)
FORWARD-SIGNAL findings to convert into monitorables: F2-01 (strip 14% JV non-cash PAT), F6-01/F6-02
(milestone tracker; HZL ramp), F16-01 (coal slips to FY28-29). AMBIGUOUS findings to convert into direct
management questions: F4-01 (are JV numbers audited?), F10-01 (post-conversion share count & basic EPS?),
F11-01 (reconcile Rs 15 Cr call vs ~Rs 78 Cr deck debt), F14-01 (10-yr or 11-yr Alara contract?), F16-02
(order-book burn schedule and net-of-not-started framing?).

```yaml
stage: A3-forensics
company: "SOUTHWEST"
quarter: "Q1 FY27"
doctype: "concall"
model: claude-opus-4-8
status: complete
forensics_path: "/home/user/inflection-pipeline/runs/southwest-q1fy27/work/forensics_concall_southwest_q1fy27.md"
ledger_reconciled_pct: 100
checklist:
  F1: N.A.
  F2: FINDING
  F3: N.A.
  F4: FINDING
  F5: N.A.
  F6: FINDING
  F7: FINDING
  F8: N.A.
  F9: N.A.
  F10: FINDING
  F11: FINDING
  F12: N.A.
  F13: N.A.
  F14: FINDING
  F15: N.A.
  F16: FINDING
  F17: FINDING
findings:
  - {id: "F2-01", check: "F2", line: "47/109", classification: "FORWARD-SIGNAL", implication: "JV equity-method share 1.32 Cr ~14% of PAT, no revenue/EBITDA; strip to see operating-only quality"}
  - {id: "F4-01", check: "F4", line: "109", classification: "AMBIGUOUS", implication: "14% of PAT on JV numbers of undisclosed audited status; >10% trip; A4 question"}
  - {id: "F6-01", check: "F6", line: "27/59/131", classification: "FORWARD-SIGNAL", implication: "16 dated commitments; DGR/mining-plan/Oman-GR/Reliance-start are next-quarter milestones"}
  - {id: "F6-02", check: "F6", line: "73/149", classification: "FORWARD-SIGNAL", implication: "HZL 307 Cr just kicked off 1.5 months ago; minimal Q1; deck order-book-as-driver framing overstated; HZL seg-rev gate un-clearable"}
  - {id: "F7-01", check: "F7", line: "77/79", classification: "CONFIRMATORY-NEGATIVE", implication: "Refused RIL/HZL % of Q1 revenue as confidential; concentration managed as undisclosed"}
  - {id: "F7-02", check: "F7", line: "69/111/145", classification: "CONFIRMATORY-NEGATIVE", implication: "Mgmt validates seasonality flag: Q1<Q4 and Q1<Q2, cyclical; do not annualise Q1x4"}
  - {id: "F10-01", check: "F10", line: "27/183", classification: "AMBIGUOUS", implication: "Warrant conversion crystallised; no post-conversion share count/EPS; future promoter dilution left open"}
  - {id: "F11-01", check: "F11", line: "93/181/111", classification: "AMBIGUOUS", implication: "Debt ~15 Cr/D-E<0.39 (call) vs ~78.6 Cr gross/~77 Cr net (deck); >5x gap; reconcile before crediting debt-free"}
  - {id: "F14-01", check: "F14", line: "47/173", classification: "AMBIGUOUS", implication: "Alara/$125M contract stated 10-yr and 11-yr within one call; unreconciled; gates JV cash math"}
  - {id: "F14-02", check: "F14", line: "89", classification: "NEUTRAL-FACT", implication: "Related-party: CMD on Alara board while SWPD subscribes Alara rights & holds Oman JVs; monitor sizing/independence"}
  - {id: "F16-01", check: "F16", line: "181", classification: "FORWARD-SIGNAL", implication: "Coal production FY27-28 (deck) vs FY28-29 (call, x4); resolve to FY28-29; contradicts Role 4 F6.1; de-rate near-term coal"}
  - {id: "F16-02", check: "F16", line: "27/79/131", classification: "AMBIGUOUS", implication: "761 Cr all-time-high book blends not-started Reliance ext + just-started HZL; 60% two-contract concentration; no burn schedule"}
  - {id: "F17-01", check: "F17", line: "105/111", classification: "CONFIRMATORY-NEGATIVE", implication: "No CFO/CFO-PAT; JV cash not repatriated so 14%-of-PAT JV share is non-cash; all three buy-gates un-clearable"}
  - {id: "F17-02", check: "F17", line: "77/123/111", classification: "CONFIRMATORY-NEGATIVE", implication: "Three compounded refusals (RIL/HZL %, coal %, actual JV cash); opacity on the exact buy-gating metrics"}
forward_signals: ["F2-01", "F6-01", "F6-02", "F16-01"]
ambiguous: ["F4-01", "F10-01", "F11-01", "F14-01", "F16-02"]
commitments:
  - {commitment: "Commence Jharkhand coal production", implied_date: "FY28-29", ref: "line 59/27 t19", status_word: "underway"}
  - {commitment: "Definite Geological Report submission to MoC", implied_date: "near-term FY27", ref: "line 27/115 t3/47", status_word: "underway"}
  - {commitment: "Mining plan preparation & MoC approval", implied_date: "FY27 post-DGR", ref: "line 51 t15", status_word: "initiated"}
  - {commitment: "Environmental/forest clearance & mining lease", implied_date: "post mining-plan", ref: "line 51 t15", status_word: "initiated"}
  - {commitment: "Oman JV2 geological report", implied_date: "near-term", ref: "line 47 t13", status_word: "underway"}
  - {commitment: "Reliance CBM extension execution begins", implied_date: "Q2 FY27", ref: "line 131 t55", status_word: "initiated"}
  - {commitment: "Oil India 2024 contract last-phase revenue", implied_date: "Q2 FY27", ref: "line 139 t59", status_word: "underway"}
  - {commitment: "Aquifer-mapping balance 35% completion", implied_date: "H2 FY27 post-monsoon", ref: "line 141 t60", status_word: "underway"}
  - {commitment: "Additional drilling rigs/equipment delivery", implied_date: "near-term", ref: "line 27/127 t3/53", status_word: "initiated"}
  - {commitment: "Alara Australia rights-issue subscription up to 1M AUD", implied_date: "ongoing FY27", ref: "line 85 t32", status_word: "underway"}
  - {commitment: "JV cash repatriation to SWPD", implied_date: "very soon (undated)", ref: "line 111 t45", status_word: "initiated"}
  - {commitment: "~20% medium-term revenue CAGR / significant FY27 growth", implied_date: "FY27+", ref: "line 69/143 t24/62", status_word: "initiated"}
  - {commitment: "Maintain ~24% margin", implied_date: "FY27", ref: "line 171 t75", status_word: "initiated"}
  - {commitment: "Reliance 35-40% (+/-5%) of FY27 revenue", implied_date: "FY27", ref: "line 155/157 t67/68", status_word: "initiated"}
  - {commitment: "Move toward debt-free", implied_date: "next 2-3 years", ref: "line 181 t80", status_word: "initiated"}
  - {commitment: "AML/Oman + Jharkhand coal ~Rs 200 Cr invest & revenue", implied_date: "~2030 / FY28-29", ref: "line 179 t79", status_word: "initiated"}
gate_a3: pass
blank_checks: []
```
