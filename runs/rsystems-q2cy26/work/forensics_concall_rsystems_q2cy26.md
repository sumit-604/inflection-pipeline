# A3 FORENSIC NOTES — RSYSTEMS Q2 CY2026 — doctype: CONCALL (earnings call, 05-Aug-2026)

Master-gate addendum. One document: the 05-Aug-2026 earnings call ASR transcript
(A1 extract lines 28-100; A2 ledger Tables A-F). Every spoken figure below was
cross-checked against the already-extracted deck (`extract_deck_*`) and Reg 33
filing (`extract_results_*`) before being treated as a finding. ASR mis-hearings
are tagged GARBLE, not management contradiction.

- extract (A1): runs/rsystems-q2cy26/work/extract_concall_rsystems_q2cy26.txt
- ledger (A2): runs/rsystems-q2cy26/work/ledger_concall_rsystems_q2cy26.md
- xref deck: runs/rsystems-q2cy26/work/extract_deck_rsystems_q2cy26.txt
- xref filing: runs/rsystems-q2cy26/work/extract_results_rsystems_q2cy26.txt
- Notion monitoring checklist: runs/rsystems-q2cy26/work/notion_thesis_rsystems.md
- Ledger reconciliation: 100% (all 73 turns / M1-M73 / Tables A-F read at cited lines)

Classification taxonomy (per task): CONFIRMED / AMBIGUOUS / FORWARD-SIGNAL /
NEUTRAL-FACT / GARBLE. FORWARD-SIGNAL and AMBIGUOUS flagged for A4 to convert
into management questions.

---

## FOUR MASTER-GATE ANSWERS — grading (ANSWERED / PARTIALLY / DODGED)

The Notion gate (notion_thesis line 15) required this call to answer four things:
revenue (organic growth trajectory), deal wins, margin uplift, organic growth.

### GATE Q1 — ORGANIC constant-currency revenue growth: **DODGED**
- Cite line 43 (Ashish Das / Systematix ask at line 42: *"organic growth remains
  very muted ... when we can expect some revival"*). Management: *"we have
  consistently uh shown organic growth quarter over over last many quarters ...
  In this quarter as well we have grown positively organically."*
- Cite line 81 (Manish Chan / MNCL ask embedded: *"when do you expect DC [CC]
  revenue growth to return to 3 4% range"*). Management: *"constant currency
  growth uh coming to 3 to 4% range is is something that we also keep keep
  tracking ... it's only uh a matter of uh time."*
- Verdict: NO organic % ever given (ledger ND7, lines 42-43/81). "Grown positively
  organically" is directional only. The analyst's own framing "return to 3-4%"
  presupposes current CC growth is BELOW 3-4% — and management did not rebut it.
  Bears directly on thesis-broken trigger "2 consecutive quarters organic revenue
  negative" and on the STAGNANT-vs-STARTING call (monitoring item 1, threshold
  >5% to confirm STARTING; <3% reverts to STAGNANT). Signal: sits in the muted
  <3-4% zone, un-quantified. GATE NOT CLEARED on this leg.

### GATE Q2 — NOVIGO revenue / margin: **DODGED (3rd consecutive quarter → EVASION FLAG)**
- Cite line 44: *"our ACV wins uh ... is is not uh influenced by uh by the
  acquisition ... both organizations growing in in in in the same manner. Uh
  Novigo of course has a uh a ongoing geopolitical challenge ... due to the
  geopolitical situation in the Middle East."*
- Cite line 89 (Deepak Malotra / Capro probes directly): *"while Novivo as a much
  smaller entity had a had a certain organic growth clip we are currently matching
  the pace."*
- Verdict: NO Novigo standalone revenue or margin number, despite two separate
  direct analyst probes (ledger ND6, lines 43-44 and 89). Monitoring item 3
  (threshold >Rs 55 Cr quarterly; "silence = 3rd evasion flag") is TRIPPED. Also
  bears on thesis-broken trigger "Novigo margin uplift missed by >40 bps." New
  negative colour: an active Middle East geopolitical drag on Novigo, disclosed
  for the first time, with no sizing.

### GATE Q3 — MARGIN quality / FX: **ANSWERED (candidly conceded FX-propped; implies normalization DOWN)**
- Cite line 47 (CEO): *"quite a large portion of it also comes from uh the uh the
  forex uh uh or exchange rate or rupee appreciation which we u ... cannot take for
  granted beyond our control"* and *"we continue to stay focused uh to uh stay in
  that 18 18 x% uh adjusted ITA on a sustainable basis."*
- Cite line 30 (CFO): *"The company has been able to report robust margin ...
  improved revenue mix and favorable exchange rates."*
- Cross-check: deck page 5 Adj-EBITDA bridge (extract_deck lines 156-164) shows
  Q1'26 1,157M → **Rupee depreciation +98M** → **Standard operations −47M** →
  Q2'26 1,207M. FX MORE THAN fully explains the +50M step-up; underlying operations
  DECLINED. Deck confirms the call. (CEO's spoken "rupee appreciation" is an ASR/verbal
  slip — the tailwind is rupee DEPRECIATION, 89.88→94.84; see GARBLE G1.)
- Verdict: management conceded the 20.1% is FX-propped AND guided the sustainable
  run-rate to "18-x%" — i.e. BELOW the reported 20.1%. Implied margin normalization
  DOWN of roughly 150-200 bps once the FX tailwind is stripped. Monitoring item 4
  (>=18.5% floor) held this quarter but the guided sustainable floor brushes it.

### GATE Q4 — ACV / bookings deceleration to $82.9m (from $82.3m, +0.6 QoQ): **PARTIALLY (backward explained, forward DODGED)**
- Cite line 51 (CEO): *"last year we had had a few large deal wins in Q2. This year
  again we have had a few large wins in Q2 which has which has effectively filled up
  for what would have been an ACV uh significant ACV uptick."* (high-base explanation)
- Cite line 53 (H2 outlook ask): *"that's a that's a million dollar question. Uh ...
  It's a it's a very difficult question."* — no forward ACV number (ledger ND4).
- Cross-check: deck page 11 (extract_deck lines 438-449) confirms TTM ACV 82.3 → 82.9.
  Monitoring item 2: threshold >$88m to confirm, <$82m = stall. $82.9m is in the
  muted band — above the stall floor, well short of confirmation. Backward reason
  given; forward number withheld.

**Gate scorecard: 1 ANSWERED, 1 PARTIALLY, 2 DODGED.** The two thesis-critical
quantitative asks (organic CC %, Novigo size) were both dodged; the one candid
answer (FX-propped margin) is a bear tell that reported 20.1% normalizes toward 18%.

---

## FINDINGS TABLE

| id | check | ledger ref | line/turn | verbatim quote (short) | class | forward implication |
|----|-------|-----------|-----------|------------------------|-------|---------------------|
| A1 | F17 | ND6, Table B t62 | 44, 89 | "not uh influenced by ... the acquisition ... both organizations growing in tandem" | CONFIRMED | 3rd straight non-disclosure of Novigo revenue/margin trips monitoring item 3 evasion flag; sustained silence on a probed metric = confirmatory negative. New: Middle East geopolitical drag, unsized. |
| A2 | F17 | ND7, Q5/Q16/Q20 | 42-43, 81 | "we have grown positively organically" / CC "3 to 4% range ... a matter of time" | FORWARD-SIGNAL | No organic CC % given; analyst framing "return to 3-4%" implies current below. Un-resolvable STAGNANT-vs-STARTING; feeds 2-consecutive-negative-quarter tripwire watch. |
| A3 | F17 | monitoring 6, notion 17-18 | (silence) | — (fixed-price mix, OCRPS/Novigo CCPS dilution never raised) | FORWARD-SIGNAL | Fixed-price/annuity mix (monitoring item 6) and the OCRPS 5.16 Cr (Nov-2027) + Novigo CCPS (2028) dilution overhang got zero call time; dilution overhang un-addressed into a master gate. |
| A4 | F7 | M-series (bridge), G-refs | 47, 30 | "large portion ... comes from ... forex ... which we ... cannot take for granted" | FORWARD-SIGNAL | Pre-emptive hedge on the margin's biggest driver. Deck bridge: FX +98M vs net +50M, standard ops −47M. Strip FX and Q2 margin fell. |
| A5 | F6 | G2 (Table E) | 47 | "stay in that 18 18 x% uh adjusted ITA on a sustainable basis" | FORWARD-SIGNAL | Sustainable margin guide (~18%) sits BELOW reported 20.1% → guided normalization DOWN ~150-200 bps; the "record 20.1%" is not the run-rate. |
| A6 | F8 | M67-M69 | 30 | "effective tax rate is around 31% ... non-deductibility of ... intangible acquired through acquisition ... normalized ... 28 to 29%" | FORWARD-SIGNAL | ETR structurally above statutory 25.17% while Novigo intangible amortizes (deck: intangible D&A 10.5 cr/qtr). Persistent EPS drag; normalized 28-29% still a step-up. Filing ties: 249.37/805.07 = 30.98%. |
| A7 | F16 | M13-M20, M70 | 30 | "strongest quarters ... record ... adjusted" (leads adjusted); "decrease of ... 17.1% ... one-time ... currency hedging ... 18 cr rupees" | AMBIGUOUS | Leads with record adjusted EBITDA; reported PAT down QoQ −15.0% (555.7 vs 654.1) and YoY −26.7%. Adjusted-PAT −17.1% QoQ pinned on a Q1 one-time ~Rs 18 Cr hedging benefit — legitimate but headline-avoidant framing. |
| A8 | F16 | ND1, ND2 | 36, 57 | "I do not think we have ... disclosed uh the percentage of revenue separately"; "we don't share a explicit percentage" (data+cloud) | AMBIGUOUS | Three revenue-mix breakouts declined on one call (GCC %, data+cloud exact %, Novigo #). Selective disclosure: happy to say data+cloud ">50%", won't give the precise splits that would let analysts triangulate organic vs inorganic. |
| A9 | F6 | Table E G1/G3/G4/G5/G6/G7 | 36, 53, 69, 81, 89 | "we do not provide uh guidance"; "million dollar question"; "we don't ... provide forward-looking guidance" | FORWARD-SIGNAL | Specificity is high on every backward number, ~zero on any forward number. Commitments are all undated/hedged (see register). Credibility pattern: precise on delivered, evasive on promised. |
| A10 | F7 | ND3-ND5, G3 | 36, 53, 69 | "that's a million dollar question ... very difficult question" | AMBIGUOUS | Repeated refusal to quantify H2 ACV / deal-win / full-year growth across 4 analysts (Anmul, Sep, "D", Manish) = REPEAT_QUESTION cluster the gate could not force open. |
| N1 | F6/F16 | M66, line 57/77 | 30, 57, 77 | "$43.32 million with average rate of 93.27"; data+cloud "crossed 50%"; "2x productivity and 55% ... turnaround" | NEUTRAL-FACT | NEW disclosures not in deck/filing: forward cover $43.32m@93.27, data+cloud >50% of revenue, 2x productivity / 55% turnaround via EXIQO/OptimaAI, wage hike taken this quarter, annuity revenue "still not very high". Backward/qualitative; logged for A4 baseline, no forward number attached. |
| G1 | ASR xref | M1,M8,M11,M12,M25,M69,M70,M72 | 30, 43, 47 | "1,200 7 crore ... IITa"; "94 ... 94.5 crores"; "18% quarter over quarter"; "rupee appreciation" | GARBLE | Reconciled to deck/filing, NOT management contradiction — see reconciliation block below. Prevents ASR noise being mis-read as an internal inconsistency. |

---

## GARBLE RECONCILIATION (G1) — ASR mis-hearings resolved against deck/filing (NOT contradictions)

| ledger flag | as spoken (line) | reconciled truth (source) | resolution |
|---|---|---|---|
| M8 / M11 | "1,200 7 crore ... IITa ... $12.8 billion" (30) | Adj EBITDA INR 1,207M = **120.7 cr**, $12.8m, 20.1% (deck p5/p7, lines 145/219) | Units slip: slide "1,207" is INR **million**, spoken as "crore"; the 120.7 cr at M11 is the correct crore value. Billion=million. Reconciled. No 10x error. |
| M12 | "281 basis points increase or a six basis points increase" (30) | 281 bps **YoY**; (6) bps **QoQ** (deck p7, line 222) | Two different comparators in one breath, both correct. Not self-contradictory. NEUTRAL. |
| M25 | H1'25 "94 crores ... 94.5 crores" (30) | H1'25 revenue INR 9,045M = **904.5 cr** (deck p6, line 178) | Digit-drop. Reconciled. |
| M69 | normalized ETR "28 to 19 29%" (30) | **28-29%** (stray "19") | ASR artefact. Reconciled. |
| M70 | reported PAT Q1 "65.4 cr" vs adjusted Q1 "75.8 cr" (30) | Reported Q1 654.1M=65.4 cr; **Adjusted** Q1 758.1M=75.8 cr (deck p14 fn, line 562) | NOT a garble and NOT an inconsistency: reported-vs-adjusted definitional difference, both confirmed in deck. Resolved. |
| M72 | "18% quarter over quarter growth ... without ... headcount" (43) vs "18% ... year on year" (47) | Revenue growth: YoY 17.7% USD / 30.2% INR; QoQ 1.2% USD / 4.7% INR (deck p7) | "18%" ≈ 17.7% USD **YoY**. The "quarter over quarter" at line 43 is a verbal slip; correct basis is YoY. AMBIGUOUS→resolved to YoY. |
| forex | "rupee appreciation" (47) | Rupee **depreciation** 89.88→94.84 (filing note 6, line 230; deck bridge "Rupee depreciation" line 164) | Weaker rupee = exporter tailwind. Spoken "appreciation" is the A1 garble-map slip. The FX-prop finding (A4) stands on the deck bridge, not the mis-spoken word. |

---

## CHECKLIST SCORECARD (F1-F17)

| # | check | status | one-line basis |
|---|-------|--------|----------------|
| F1 | Zero-value standing line items | N.A. | Reg 33 line-item template check; a concall transcript has no standing template rows. |
| F2 | Standalone vs consolidated decomposition | N.A. | Requires the S and C statements; call gives consolidated commentary only. |
| F3 | Shell-entity detection | N.A. | Needs standalone-vs-consol cost lines; not in a transcript. |
| F4 | Unaudited contribution ratio | N.A. | From auditor Other-Matters (filing: 21 subs, Rs 114.58M Q2 PAT ≈ 20.6% of consol — belongs to results forensics, not this call). |
| F5 | Going concern / EoM scope | N.A. | No EoM language on a call; no prior-quarter concall ledger supplied to diff. |
| F6 | Forward-commitment phrase mining | **FINDING** | Commitments present but ALL undated/hedged (A5, A9; register below) — high backward specificity, ~zero forward. |
| F7 | Hedge phrase mining | **FINDING** | Pre-emptive hedge on FX-propped margin (A4) + repeated refusal-to-guide hedges (A10). |
| F8 | Tax forensics | **FINDING** | ETR ~31% vs statutory 25.17%; normalized 28-29%; structural non-deductible Novigo intangible (A6). |
| F9 | OCI forensics (actuarial) | N.A. | Actuarial gains/losses are a filing check; the hedge-reserve OCI (18.04 cr) discussed on call is captured under FX/margin (A4). |
| F10 | Share count and dilution | N.A. | Paid-up/EPS-spread reconciliation is a filing check; OCRPS/CCPS dilution silence logged under F17 (A3). |
| F11 | Reserves and net-worth tie-out | N.A. | Balance-sheet reconciliation; not in a transcript. |
| F12 | Segment forensics | N.A. | Segment assets/liabilities check; filing itself states these are not disclosed (Ind AS 108). |
| F13 | Board outcome beyond results | N.A. | Board/AGM/director-term items live in the results filing (postal ballot, 3 IDs 5-yr terms); not on this call. |
| F14 | Note drafting inconsistencies | N.A. | Note-vs-auditor drafting check applies to the filing, not a transcript. |
| F15 | Entity list diffs | N.A. | Consolidation-list diff is a filing check (Novigo entities w.e.f 13-Nov-2025 there). |
| F16 | Dropped / reframed disclosures | **FINDING** | Concall analog: selective adjusted-vs-reported framing with reported PAT down (A7) + declined GCC%/data+cloud/Novigo breakouts (A8); NEW disclosures logged (N1). |
| F17 | Silence audit | **FINDING** | Novigo # silence 3rd qtr (A1), organic CC % never given (A2), fixed-price mix + dilution overhang silent (A3) — cross-referenced to Notion monitoring checklist. |

Every check carries exactly one status. No blanks. GATE A3: PASS.

---

## "WHAT WAS NOT DISCUSSED" TABLE (F17 silence audit vs Notion monitoring checklist)

| monitoring item | asked on call? | disclosed? | consecutive-qtr silence | note |
|---|---|---|---|---|
| 1. Organic CC revenue growth % (>5% confirm / <3% revert) | Yes (Ashish L42, Manish L81) | No number | probed & withheld this qtr | Only "positively organically"; analyst "3-4%" framing implies <3-4%. |
| 2. TTM ACV bookings (>$88m confirm / <$82m stall) | Yes (Sep L50) | Yes: $82.9m (L30, deck p11) | disclosed | Muted band; above stall floor, short of confirm. Forward number DODGED (L53). |
| 3. Novigo revenue (>Rs 55 Cr qtr; silence = 3rd evasion flag) | Yes (Ashish L43, Deepak L89) | No | **3rd consecutive** → EVASION FLAG | A1. Middle East geopolitical drag newly flagged, unsized. |
| 4. Adj EBITDA margin (>=18.5%) | Yes (Ashish L45) | Yes: 20.1% (L30) | disclosed | But guided sustainable "18-x%" is below reported (A5). |
| 5. USD/INR avg (>89 sustained) | Implied | Partial: fwd cover $43.32m@93.27; range 92.6-96.5 (L30) | disclosed | Tailwind acknowledged as non-repeatable (A4). |
| 6. Fixed-price / annuity mix (>18%) | Touched (Anmul L37) | No % | silent on the number | "annuity ... still not very high" (L38), no figure. |
| 7. Debtor turnover (>=1.45x) | No | No (DSO qualitative only, ~55-56 / ~75 days) | not raised | Filing carries 1.47x; not quantified on call. |
| 8. Interest coverage (>6x) | No | No | not raised | — |
| 9. Annualised ROCE (>20%) | No | No | not raised | — |
| (extra) OCRPS 5.16 Cr + Novigo CCPS dilution overhang | No | No | silent into a master gate | A3; notion lines 17-18. |

---

## COMMITMENT REGISTER (F6)

| commitment | implied date | line/turn ref | status word |
|---|---|---|---|
| Hold ~18-x% adjusted EBITDA "on a sustainable basis" | ongoing / undated | 47 | reaffirmed (guidance) |
| H1 wins "will become revenues in the next half" (lag effect) | H2 CY2026 | 36, 55 | underway |
| "might be able to have a reportable annuity revenue at some point" | undated | 38 | intends to (aspirational) |
| CC growth return to 3-4% "only a matter of time" | undated | 81 | expects (no date/number) |
| "continue to report our deal wins ... on a trailing 12 month basis" | ongoing cadence | 69 | ongoing |
| "continue to be on the lookout" for further M&A ("organic plus inorganic ambition") | undated | 89 | evaluating |

Observation: not one commitment carries a date or a number. Every dateable/quantifiable
forward ask was explicitly declined (A9/A10). This is the credibility signature of the
call — specificity high on backward numbers, zero on forward.

---

## FOR A4 (management questions to generate)
FORWARD-SIGNAL: A2, A3, A4, A5, A6, A9. AMBIGUOUS: A7, A8, A10.
Priority: (1) force the organic CC % (A2) and Novigo standalone revenue/margin (A1)
given the 3rd-quarter evasion flag; (2) reconcile the guided "~18%" sustainable margin
against reported 20.1% and the FX bridge (A4/A5); (3) surface the un-discussed
OCRPS/CCPS dilution timeline (A3).

Output path: /home/user/inflection-pipeline/runs/rsystems-q2cy26/work/forensics_concall_rsystems_q2cy26.md

```yaml
stage: A3-forensics
company: "RSYSTEMS"
quarter: "Q2CY26"
doctype: "concall"
model: claude-opus-4-8
status: complete
forensics_path: "/home/user/inflection-pipeline/runs/rsystems-q2cy26/work/forensics_concall_rsystems_q2cy26.md"
ledger_reconciled_pct: 100
checklist:
  F1: N.A.
  F2: N.A.
  F3: N.A.
  F4: N.A.
  F5: N.A.
  F6: FINDING
  F7: FINDING
  F8: FINDING
  F9: N.A.
  F10: N.A.
  F11: N.A.
  F12: N.A.
  F13: N.A.
  F14: N.A.
  F15: N.A.
  F16: FINDING
  F17: FINDING
findings:
  - {id: "A1", check: "F17", line: "44,89", classification: "CONFIRMED", implication: "Novigo revenue/margin undisclosed 3rd straight quarter -> monitoring-item-3 evasion flag; Middle East drag newly flagged, unsized"}
  - {id: "A2", check: "F17", line: "42-43,81", classification: "FORWARD-SIGNAL", implication: "No organic CC % given; analyst '3-4% return' framing implies current below; STAGNANT-vs-STARTING unresolved"}
  - {id: "A3", check: "F17", line: "silence", classification: "FORWARD-SIGNAL", implication: "Fixed-price mix and OCRPS/CCPS dilution overhang got zero call time into a master gate"}
  - {id: "A4", check: "F7", line: "47,30", classification: "FORWARD-SIGNAL", implication: "Margin FX-propped; deck bridge FX +98M vs net +50M, standard ops -47M; tailwind 'cannot take for granted'"}
  - {id: "A5", check: "F6", line: "47", classification: "FORWARD-SIGNAL", implication: "Sustainable margin guide ~18% is below reported 20.1% -> normalization DOWN ~150-200bps"}
  - {id: "A6", check: "F8", line: "30", classification: "FORWARD-SIGNAL", implication: "ETR ~31% vs statutory 25.17%, normalized 28-29%, structural via non-deductible Novigo intangible amortization -> persistent EPS drag"}
  - {id: "A7", check: "F16", line: "30", classification: "AMBIGUOUS", implication: "Leads with record adjusted EBITDA while reported PAT down QoQ -15.0% and YoY -26.7%; adj-PAT -17.1% pinned on Q1 one-time ~Rs18Cr hedge benefit"}
  - {id: "A8", check: "F16", line: "36,57", classification: "AMBIGUOUS", implication: "Three mix breakouts declined (GCC%, data+cloud exact %, Novigo #) preventing organic/inorganic triangulation"}
  - {id: "A9", check: "F6", line: "36,53,69", classification: "FORWARD-SIGNAL", implication: "All forward commitments undated/hedged; specificity high on backward numbers, ~zero forward -> credibility signature"}
  - {id: "A10", check: "F7", line: "36,53,69", classification: "AMBIGUOUS", implication: "Repeated refusal to quantify H2 ACV/deal-win/full-year growth across 4 analysts; gate could not force it open"}
  - {id: "N1", check: "F16", line: "30,57,77", classification: "NEUTRAL-FACT", implication: "New backward disclosures: fwd cover $43.32m@93.27, data+cloud >50%, 2x productivity/55% turnaround, wage hike this qtr, annuity 'still not very high'"}
  - {id: "G1", check: "ASR-xref", line: "30,43,47", classification: "GARBLE", implication: "ASR mis-hearings (1,207 cr units, 94.5cr, 18% QoQ vs YoY, 'rupee appreciation', 65.4 vs 75.8 reported-vs-adjusted) reconciled to deck/filing; NOT management contradictions"}
forward_signals: ["A2", "A3", "A4", "A5", "A6", "A9"]
ambiguous: ["A7", "A8", "A10"]
commitments:
  - {commitment: "Hold ~18-x% adjusted EBITDA on a sustainable basis", implied_date: "ongoing/undated", ref: "line 47", status_word: "reaffirmed"}
  - {commitment: "H1 wins become revenues in the next half (lag effect)", implied_date: "H2 CY2026", ref: "line 36,55", status_word: "underway"}
  - {commitment: "Reportable annuity revenue at some point", implied_date: "undated", ref: "line 38", status_word: "intends-to"}
  - {commitment: "CC growth returns to 3-4% 'a matter of time'", implied_date: "undated", ref: "line 81", status_word: "expects"}
  - {commitment: "Continue reporting deal wins on trailing-12-month basis", implied_date: "ongoing", ref: "line 69", status_word: "ongoing"}
  - {commitment: "Continue on the lookout for further M&A", implied_date: "undated", ref: "line 89", status_word: "evaluating"}
gate_a3: pass
blank_checks: []
```
