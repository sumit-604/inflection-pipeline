# A3 FORENSIC NOTES — TEJAS NETWORKS (TEJASNET) — Q1 FY27 — DOCTYPE: CONCALL

Source extract: `/home/user/inflection-pipeline/runs/tejasnet-q1fy27/work/extract_concall_tejasnet_q1fy27.txt`
Reconciliation contract: `/home/user/inflection-pipeline/runs/tejasnet-q1fy27/work/ledger_concall_tejasnet_q1fy27.md`
Prior-quarter extract: none (first pipeline run — no verbatim diff base for F5/F15/F16 available)
Ledger reconciliation: 100% (14 participants / 109 turns / 37 questions / 40 mgmt-number rows / 27 phrase rows all read at cited line before judging)

Doctype gating: this is a concall. F6 (forward-commitment), F7 (hedge) and F17 (silence audit) are the core and apply. F14 applies for verbal-vs-filing inconsistency. All balance-sheet checks (F1-F5, F8, F9, F11, F12, F15, F16), share count (F10) and board outcome (F13) are N.A. to a transcript. Conservative bias: where direction is uncertain, leaned bear and generated an A4 question rather than resolving.

---

## FINDINGS TABLE

| id | check | ledger row ref | line/turn | short verbatim quote | classification | forward implication |
|----|-------|----------------|-----------|----------------------|----------------|---------------------|
| F6-1 | F6 | Phrases #1,#2; Num #14/#27; Q1/Q11/Q20/Q28 | line 34 / turn 4 (also line 196 / turn 85) | "it's in the final stages of uh of conclusion ... materialize uh very soon uh probably in this quarter" | AMBIGUOUS | BSNL 4G add-on now framed "26,000 sites" vs thesis-memory 18,700 sites / ~Rs 1,526 cr — site count grew ~39% with no order value given; 6th consecutive quarter of "expected soon"; NOT in order book. A4: reconcile the site count and press on why award keeps slipping. |
| F6-2 | F6 | Phrase #3; Q1 | line 46 / turn 10 | "we expect a lot of the PSN [BSNL] receivables to also get cleared during the quarter" | FORWARD-SIGNAL | Dated (this-quarter) collection commitment. Net receivables 1,907->2,232 (+325). If not cleared in Q2 FY27, working-capital thesis breaks. Trackable in Role 5. |
| F6-3 | F6 | Phrases #7,#8; Num #28; Q8 | line 78 / turn 26 | "our first target will be uh positive [EBITDA] and [EBIT] ... 12 to 18 months is a reasonable time" | FORWARD-SIGNAL | SOFTENING vs AGM-26 commitment "EBITDA-positive Q4 FY27." 12-18 months from Q1 FY27 (Jul-2026) pushes even the EBITDA milestone to H2 FY28 / H1 FY29, past the prior Q4 FY27 date. Net profitability is sequenced after that. A4: is this a formal walk-back of the AGM-26 guidance? |
| F6-4 | F6 | Phrases #11,#12,#17; Num #31; Q12/Q13/Q21/Q22/Q23 | lines 96,100,140,150 / turns 35,37,57,62 | "the AMC's are going to start after site acceptance and the warranty period getting over" | FORWARD-SIGNAL | Unstarted, unquantified higher-margin annuity; 8-year recognition; circle-by-circle multi-year POs. Real future margin lever but zero size given ("have not yet shared the AMC numbers"). A4: request AMC contract value and start quarter. |
| F6-5 | F6 | Phrases #4,#5; Num #6,#7,#9,#10; Q9 | line 74 / turn 24 (decomposition at line 32 / turn 3) | "we expect a lot of that to uh get go away reducing our working capital requirements for the future" | FORWARD-SIGNAL | The entire WC/inventory-unwind case is contingent on the add-on order (F6-1) arriving. CFO decomposed the net-debt rise (line 32) as (a) net trade receivables 1,907->2,232, (b) "increased schedule payouts" to suppliers, (c) "continued investments in terms of capex." Inventory only fell 2,438->2,358 (-80). Deleveraging depends on an order that has slipped six quarters. |
| F6-6 | F6 | Phrase #13; Num #11/#26/#29; Q14/Q15/Q16 | line 114 / turn 44 (mix at lines 104/110) | "we hope to change that profile uh going forward" | AMBIGUOUS | Revenue ~50/50 India/international this quarter (>15% green on monitoring #6) BUT order book only 7% international / 93% domestic. International revenue is front-loaded 5G-radio shipments not backed by sustained backlog — the green mix number is not durable. A4: what international backlog underpins the 50% run-rate? |
| F7-1 | F7 | Phrases #9,#10; Q10 | line 88 / turn 31 (analyst at line 86 / turn 30) | "this has been a one-off case ... the warranty costs are expected to normalize" | AMBIGUOUS | Direct tension: analyst states warranty has been "a recurring item on the P&L for the last couple of quarters"; filing carries Rs 35.11 cr warranty provision. Management calls a repeating charge "one-off." Conservative read: recurring cost mislabelled. A4: quantify per-quarter warranty run-rate and the normalization date. |
| F7-2 | F7 | Phrase #20; Q3 | line 52 / turn 13 | "I think the preferred partner is probably the right word to use" | AMBIGUOUS | Analyst asked whether Tejas is NEC's "exclusive partner"; management downgraded live to "preferred." Exclusivity on NEC 5G radios is a thesis pillar; the hedge weakens it. A4: is there any contractual exclusivity, brownfield or greenfield? |
| F7-3 | F7 | Phrase #18; Num #32; Q27 | line 182 / turn 78 | "if the rollout happens nationwide to the scale at which we anticipate ... then it could be close to a billion dollars" | NEUTRAL-FACT | D2M TAM is triple-hedged (conditional on tender, nationwide scale, phasing). Prasar Bharati tender not out; "no clarity on when." Optionality only; do not size into base case. |
| F7-4 | F7 | Phrases #16,#21; Num #39,#40; Q4/Q2/Q14 | lines 56,148,104,50 / turns 15,61,39,12 | "we have not yet shared the AMC numbers"; "I don't have those numbers with me right now" | CONFIRMATORY-NEGATIVE | Enumerated DECLINED_DISCLOSURES: (1) NEC's 5G market size (line 56), (2) AMC contract size (line 148), (3) wireless-vs-wireline revenue split (line 104: "we don't give that"), (4) number of 5G sites NEC/Europe/S.America (line 50: "I don't have permission from the customers"). Four quantifications refused in one call. A4 should convert each into a standing information request. |
| F7-5 | F7 | Q5/Q6 | lines 64,68 / turns 19,21 | "There is no payment link to uh those performances ... it varies between uh 60 to 90 days" | NEUTRAL-FACT | Positive cash-conversion contrast: international orders carry NO performance-linked payment (unlike BSNL) and 60-90 day cycles. Structurally better working capital on the international book than on BSNL. |
| F14-1 | F14 | Num #8,#9,#10 | line 32 / turn 3 | "cash position ... stands at 489 crores" | NEUTRAL-FACT | Spoken cash "489" contradicts the filed press release: gross borrowing 4,866 − net borrowing 4,277 = 589. ASR error (489 vs 589) per ledger ARITHMETIC_CHECK; the 4,866 / 4,277 pair CONFIRMS the filing, so reconcile cash to 589. Flagged so A4/A5 do not carry 489. |
| F14-2 | F14 | Num #3,#4 | lines 30,32 / turns 2,3 | "slight 20% growth" (CEO) vs "a 21% uh quarteron quarter increase" (CFO) | NEUTRAL-FACT | Minor internal inconsistency in the same-call QoQ revenue-growth figure (20% vs 21% on 402 vs ~332-335). Immaterial alone; logged for governance-consistency trend. |
| F14-3 | F14 | Phrase #9,#10; Q10 | line 88 / turn 31 | "this has been a one-off case" | AMBIGUOUS | Verbal-vs-filing inconsistency: the filing books Rs 35.11 cr warranty as a recurring provision line; the call labels it "one-off." Same substance as F7-1, logged here as a filing-vs-verbal drafting mismatch. A4 question. |
| F14-4 | F14 | Num #5 | line 32 / turn 3 | "PBT is around -271 uh compared to 281 crores in quarter 4" | NEUTRAL-FACT | Confirms CFO is quoting on a CONSOLIDATED basis: Q4 consolidated PBT was -280.80 (~ -281), not standalone -287.92. No inconsistency; anchors A4/A5 to the consolidated baseline. |
| F17-1 | F17 | (silence) | entire call — zero hits | (no mention) | CONFIRMATORY-NEGATIVE | Monitoring #8 PLI income collapsed FY26 Rs 468->6 cr. PLI was not mentioned once on the call. Silence on a collapsed subsidy line is itself a signal. Consecutive-silence count: 1 (first tracked run). |
| F17-2 | F17 | (silence) | entire call — zero hits | (no mention) | CONFIRMATORY-NEGATIVE | TBC intangibles-under-development impairment (Rs 950 cr) never raised, despite continued-capex narrative (line 32). Silence count: 1. |
| F17-3 | F17 | (silence) | entire call — zero hits | (no mention) | CONFIRMATORY-NEGATIVE | TBC DTA reversal (Rs 365 cr / 52% of equity) — no tax or DTA discussion anywhere. With PBT still negative (-271), DTA recoverability is live. Silence count: 1. |
| F17-4 | F17 | (silence) | entire call — zero hits | (no mention) | FORWARD-SIGNAL | QIP / equity-dilution optionality (reintroduced at AGM-26) NOT addressed while net debt is 4,277 (monitoring #4 RED, >4,000) and rising on WC + capex. Management pointed only to the add-on order to deleverage. Silence on the equity lever amid red-zone net debt is the most important non-answer on the call. A4: is a raise on the table? |
| F17-5 | F17 | (silence) | entire call — zero hits | (no mention) | CONFIRMATORY-NEGATIVE | BharatNet Phase III (thesis core catalyst) not mentioned. Absence on a results call this size is a confirmatory-negative on catalyst timing. Silence count: 1. |
| F17-6 | F17 | (silence) | entire call — zero hits | (no mention) | CONFIRMATORY-NEGATIVE | Vodafone Idea backhaul (thesis core catalyst) not mentioned; only generic "5G back hall" wins (line 34), no named VIL engagement. Confirmatory-negative on that catalyst. Silence count: 1. |

---

## CHECKLIST SCORECARD (all 17)

| Check | Status | One-line basis |
|-------|--------|----------------|
| F1 ZERO-VALUE STANDING LINE ITEMS | N.A. | No financial statement table in a concall transcript; no ZERO_STANDING ledger rows (ledger confirms none apply). |
| F2 STANDALONE vs CONSOLIDATED | N.A. | No S-vs-C statements in transcript. Note: F14-4 confirms CFO quotes consolidated basis. |
| F3 SHELL-ENTITY DETECTION | N.A. | No cost-line tables to compare. |
| F4 UNAUDITED CONTRIBUTION RATIO | N.A. | No auditor Other-Matters paragraph in a transcript. |
| F5 GOING CONCERN / EoM SCOPE | N.A. | No EoM paragraph; and no prior-quarter extract for verbatim diff. |
| F6 FORWARD-COMMITMENT PHRASE MINING | FINDING | Six commitments extracted (F6-1..F6-6): BSNL award/receivables, path-to-profitability softening, AMC start, WC unwind contingency, international-mix aspiration. See Commitment Register. |
| F7 HEDGE PHRASE MINING | FINDING | Warranty "one-off", NEC "preferred not exclusive", conditional D2M TAM, four declined disclosures, plus positive intl payment-terms contrast (F7-1..F7-5). |
| F8 TAX FORENSICS | N.A. | No ETR / deferred-tax tables; DTA not discussed (captured as silence F17-3). |
| F9 OCI FORENSICS | N.A. | No OCI actuarial data in transcript. |
| F10 SHARE COUNT AND DILUTION | N.A. | No paid-up capital / EPS spread; QIP optionality captured as silence F17-4. |
| F11 RESERVES / NET WORTH TIE-OUT | N.A. | No equity reconciliation in transcript. |
| F12 SEGMENT FORENSICS | N.A. | No segment asset/liability tables; management declined wireless/wireline split (F7-4). |
| F13 BOARD OUTCOME BEYOND RESULTS | N.A. | No board/AGM/AR-approval item on this call. |
| F14 NOTE DRAFTING / VERBAL-vs-FILING | FINDING | Cash 489 vs 589 (F14-1), 20% vs 21% growth (F14-2), warranty "one-off" vs Rs 35.11 cr recurring filing (F14-3); PBT basis confirmed consolidated (F14-4). |
| F15 ENTITY LIST DIFFS | N.A. | No consolidation list; no prior extract to diff. |
| F16 DROPPED / REFRAMED DISCLOSURES | N.A. | Presentation/filing check, not a transcript check; and no prior deck to diff. Declined disclosures routed to F7-4; guidance softening to F6-3. |
| F17 CONCALL SILENCE AUDIT | FINDING | Six silences: PLI, intangibles impairment (950), DTA reversal (365), QIP/dilution, BharatNet Ph-III, VIL backhaul (F17-1..F17-6). |

Blank checks: none. GATE A3 satisfied (every check carries exactly one status).

---

## COMMITMENT REGISTER (from F6 / F7 forward-commitment phrases)

| Commitment | Implied date | Line/turn ref | Status word |
|------------|--------------|---------------|-------------|
| BSNL 4G add-on order (26,000 sites) awarded | "this quarter" (Q2 FY27) | line 34 / turn 4; restated line 196 / turn 85 | underway — "final stages of conclusion" (6th consecutive quarter of "soon") |
| BSNL receivables cleared | "during the quarter" (Q2 FY27) | line 46 / turn 10 | expected (not started) |
| Positive EBITDA + EBIT, then net profitability | "12 to 18 months" (H2 FY28 - H1 FY29) | line 78 / turn 26 | targeted — SOFTENED vs AGM-26 "EBITDA-positive Q4 FY27" |
| AMC / service revenue commences (8-yr recognition, higher margin, circle-by-circle) | "next few quarters" after acceptance + warranty | lines 96,100,140,150,154,158 | not started ("have not yet shared the AMC numbers") |
| Working-capital / inventory drawdown | on add-on order arrival (contingent) | line 74 / turn 24 | expected (conditional) |
| International order-book mix improvement | "going forward" | line 114 / turn 44 | aspirational |
| Employee costs held flat | "for some more times" | line 128 / turn 51 | ongoing |
| New 1.6T DCI / BCI product customer deployment | "end of the financial year or early financial year" | line 220 / turn 97 | underway — PoC / field trials |
| 6G product launch | "probably in 2029" | line 226 / turn 100 | pre-commercial (standards-dependent, 3GPP 2030) |

---

## "WHAT WAS NOT DISCUSSED" TABLE (F17 detail)

| Item | Source (checklist / commitment register) | Discussed? | Consecutive-quarter silence | Read |
|------|------------------------------------------|-----------|------------------------------|------|
| PLI income (FY26 468 -> 6 cr) | Monitoring #8 | No | 1 | Confirmatory-negative; subsidy line quietly gone |
| Intangibles-under-development impairment (Rs 950 cr) | TBC | No | 1 | Unaddressed capitalized-R&D risk |
| DTA reversal (Rs 365 cr / 52% equity) | TBC | No | 1 | No tax/DTA recoverability discussion while PBT negative |
| QIP / equity-dilution optionality | TBC (AGM-26) | No | 1 | FORWARD-SIGNAL — net debt RED (4,277) yet equity lever un-mentioned |
| BharatNet Phase III | Thesis core catalyst | No | 1 | Confirmatory-negative on catalyst |
| Vodafone Idea backhaul | Thesis core catalyst | No | 1 | Confirmatory-negative on catalyst |
| Revenue run-rate (#2, 402 cr) | Monitoring #2 | Yes (line 30/32) | — | Discussed; ~402 marginally above Rs 400 red-line, Q4 ~332-335 below |
| Net debt (#4, 4,277 cr) | Monitoring #4 | Yes (line 32) | — | Discussed; RED (>4,000) |
| International mix (#6) | Monitoring #6 | Yes (lines 104/114) | — | Discussed; revenue green but backlog only 7% (F6-6) |

Note on silence counts: this is the first tracked pipeline run for TEJASNET (no prior extract). All silence counts initialize at 1; Role 5 should increment against this baseline next quarter.

---

## HANDOFF TO A4

- FORWARD-SIGNAL findings (convert to management questions): F6-2, F6-3, F6-4, F6-5, F17-4.
- AMBIGUOUS findings (convert to management questions): F6-1, F6-6, F7-1, F7-2, F14-3.
- Highest-priority A4 questions: (1) formal status of AGM-26 "EBITDA-positive Q4 FY27" now that management says "12-18 months" (F6-3); (2) equity-raise intent given RED net debt and no QIP mention (F17-4); (3) reconcile BSNL add-on 26,000 sites vs 18,700-site thesis-memory and order value (F6-1); (4) warranty run-rate: recurring vs "one-off" (F7-1/F14-3); (5) durable international backlog behind the 50% revenue mix (F6-6).
- Anchor correction for the whole downstream chain: cash = 589 (not spoken "489"), consolidated PBT basis, net debt 4,277.

---

```yaml
stage: A3-forensics
company: "TEJASNET"
quarter: "Q1 FY27"
doctype: "concall"
model: claude-opus-4-8
status: complete
forensics_path: "/home/user/inflection-pipeline/runs/tejasnet-q1fy27/work/forensics_concall_tejasnet_q1fy27.md"
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
  - {id: "F6-1", check: "F6", line: "34", classification: "AMBIGUOUS", implication: "BSNL add-on 26,000 sites vs 18,700 thesis-memory; 6th qtr of 'final stages / very soon'; not in order book"}
  - {id: "F6-2", check: "F6", line: "46", classification: "FORWARD-SIGNAL", implication: "Dated this-quarter BSNL receivables clearance; WC thesis hinges on it"}
  - {id: "F6-3", check: "F6", line: "78", classification: "FORWARD-SIGNAL", implication: "'12 to 18 months' softens AGM-26 'EBITDA-positive Q4 FY27'"}
  - {id: "F6-4", check: "F6", line: "96", classification: "FORWARD-SIGNAL", implication: "AMC annuity not started, unquantified 8-yr higher-margin lever"}
  - {id: "F6-5", check: "F6", line: "74", classification: "FORWARD-SIGNAL", implication: "Deleveraging contingent on the slipping add-on order; net-debt rise = receivables + supplier payouts + capex"}
  - {id: "F6-6", check: "F6", line: "114", classification: "AMBIGUOUS", implication: "50% intl revenue vs 7% intl order book; green mix not backlog-durable"}
  - {id: "F7-1", check: "F7", line: "88", classification: "AMBIGUOUS", implication: "Warranty 'one-off / expected to normalize' vs analyst 'recurring last couple of quarters'"}
  - {id: "F7-2", check: "F7", line: "52", classification: "AMBIGUOUS", implication: "NEC exclusivity downgraded live to 'preferred partner'"}
  - {id: "F7-3", check: "F7", line: "182", classification: "NEUTRAL-FACT", implication: "D2M TAM triple-hedged, optionality only"}
  - {id: "F7-4", check: "F7", line: "148", classification: "CONFIRMATORY-NEGATIVE", implication: "Four declined disclosures: NEC TAM, AMC size, wireless/wireline split, 5G site counts"}
  - {id: "F7-5", check: "F7", line: "68", classification: "NEUTRAL-FACT", implication: "International orders no performance-linked payment, 60-90 day cycles: better WC than BSNL"}
  - {id: "F14-1", check: "F14", line: "32", classification: "NEUTRAL-FACT", implication: "Spoken cash 489 vs filing-derived 589 (4,866-4,277); ASR error, anchor to 589"}
  - {id: "F14-2", check: "F14", line: "32", classification: "NEUTRAL-FACT", implication: "QoQ growth 20% (CEO) vs 21% (CFO) internal inconsistency"}
  - {id: "F14-3", check: "F14", line: "88", classification: "AMBIGUOUS", implication: "Verbal 'one-off' vs Rs 35.11 cr recurring warranty provision in filing"}
  - {id: "F14-4", check: "F14", line: "32", classification: "NEUTRAL-FACT", implication: "PBT -271 vs -281 confirms consolidated basis (Q4 consol -280.80, not standalone -287.92)"}
  - {id: "F17-1", check: "F17", line: "n/a-silence", classification: "CONFIRMATORY-NEGATIVE", implication: "PLI (468->6 cr) unmentioned; silence on collapsed subsidy"}
  - {id: "F17-2", check: "F17", line: "n/a-silence", classification: "CONFIRMATORY-NEGATIVE", implication: "Rs 950 cr intangibles-under-development impairment unaddressed"}
  - {id: "F17-3", check: "F17", line: "n/a-silence", classification: "CONFIRMATORY-NEGATIVE", implication: "Rs 365 cr DTA reversal / no tax discussion while PBT negative"}
  - {id: "F17-4", check: "F17", line: "n/a-silence", classification: "FORWARD-SIGNAL", implication: "QIP/dilution unmentioned despite RED net debt 4,277"}
  - {id: "F17-5", check: "F17", line: "n/a-silence", classification: "CONFIRMATORY-NEGATIVE", implication: "BharatNet Phase III catalyst not mentioned"}
  - {id: "F17-6", check: "F17", line: "n/a-silence", classification: "CONFIRMATORY-NEGATIVE", implication: "Vodafone Idea backhaul catalyst not mentioned"}
forward_signals: ["F6-2", "F6-3", "F6-4", "F6-5", "F17-4"]
ambiguous: ["F6-1", "F6-6", "F7-1", "F7-2", "F14-3"]
commitments:
  - {commitment: "BSNL 4G add-on (26,000 sites) awarded", implied_date: "Q2 FY27", ref: "line 34 / turn 4", status_word: "underway (final stages, 6th qtr)"}
  - {commitment: "BSNL receivables cleared", implied_date: "Q2 FY27", ref: "line 46 / turn 10", status_word: "expected"}
  - {commitment: "Positive EBITDA + EBIT then net profit", implied_date: "12-18 months (H2FY28-H1FY29)", ref: "line 78 / turn 26", status_word: "targeted (softened vs AGM-26 Q4FY27)"}
  - {commitment: "AMC / service revenue commences (8-yr, higher margin)", implied_date: "next few quarters post acceptance+warranty", ref: "lines 96/100/140/150", status_word: "not started"}
  - {commitment: "Working-capital / inventory drawdown", implied_date: "on add-on order arrival", ref: "line 74 / turn 24", status_word: "expected (contingent)"}
  - {commitment: "International order-book mix improvement", implied_date: "going forward", ref: "line 114 / turn 44", status_word: "aspirational"}
  - {commitment: "Employee costs flat", implied_date: "some more time", ref: "line 128 / turn 51", status_word: "ongoing"}
  - {commitment: "1.6T DCI/BCI product customer deployment", implied_date: "end FY27 / early FY28", ref: "line 220 / turn 97", status_word: "PoC / field trials"}
  - {commitment: "6G product launch", implied_date: "2029", ref: "line 226 / turn 100", status_word: "pre-commercial"}
gate_a3: pass
blank_checks: []
```
