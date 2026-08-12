# A3 FORENSIC NOTES — JNK India Limited (JNKINDIA) — Q1 FY27 — DOCTYPE: RESULTS (Reg 33 filing)

Source extract: `extract_results_jnkindia_q1fy27.txt` (902 lines, 14 pages).
Ledger: `ledger_results_jnkindia_q1fy27.md`. Ledger reconciliation: **100%** — every
ledger row read verbatim at its cited line before judging.
Units: statement is INR Millions (x0.1 to Crores). **All findings state figures in Rs Crores.**
Prior-quarter extract: **none provided** (`NO_PRIOR_LEDGER`). F5 EoM and F15 entity-list
verbatim quarter-over-quarter diffs **could not be run**; this is flagged, not fabricated.
Doctype applicability: F1-F15 apply; **F16 and F17 are N.A.** (results filing, not a deck or concall).

---

## KEY DERIVED FIGURES (Rs Crores; millions ÷ 10)

STANDALONE (Q1FY27 / Q4FY26 / Q1FY26 / FY26):
- Revenue: 163.55 / 299.53 / 98.83 / 755.61
- PBT: 18.54 / 40.67 / 2.03 / 84.64
- PAT: 13.55 / 31.66 / 1.17 / 64.87
- Total tax: 5.00 / 9.00 / 0.86 / 19.77  → ETR 27.0% / 22.1% / 42.4% / 23.4%

CONSOLIDATED (Q1FY27 / Q4FY26 / Q1FY26 / FY26):
- Revenue: 179.96 / **338.44** / 99.10 / 818.55  (Q4FY26 printed "238440" is an OCR 3→2 error; Combustion 303.15 + Process 35.29 = 338.44 confirms via segment total line 601)
- PBT: 14.64 / 42.65 / 1.98 / 85.22
- PAT (total): 9.63 / 33.04 / 0.13 / 64.82; attributable to owners 11.47 / 32.65 / 0.13 / 64.95; NCI (1.84) / 0.39 / nil / (0.13)
- Total tax: 5.01 / 9.61 / 0.85 / 20.40  → ETR 34.2% / 22.5% / 43.0% / 23.9%

Operating EBITDA (PBT + Dep + Finance − Other Income):
- Standalone Q1FY27 = 18.54 + 1.84 + 3.40 − 6.59 = **17.19 Cr; margin 10.5%**
- Consolidated Q1FY27 = 14.64 + 2.87 + 4.44 − 6.04 = **15.90 Cr; margin 8.8%**

---

## FINDINGS TABLE

| id | check | ledger row ref | line(s) | verbatim quote | classification | forward implication |
|----|-------|----------------|---------|----------------|----------------|---------------------|
| F1-a | F1 | §2 L219 / §5 L515 `ZERO_STANDING` (Exceptional Items) + Note VII goodwill | 219, 515, 678 | "Exceptional ltems … =" (dash all periods) ; "resultant goodwill of Rs. 17.19 Million is also recognised" | FORWARD-SIGNAL | Exceptional-items line is a live impairment channel. Rs 1.72 Cr goodwill sits on Chemdist, which posted a segment loss this quarter (F12) — a future impairment would first populate this dormant line. |
| F1-b | F1 | §2 L230 / §5 L526 `ZERO_STANDING` (items reclassified to P&L) | 230, 526 | "Trems that will be reclassified to Profit or Loss: =" (dash all periods) | NEUTRAL-FACT | No FCTR / hedge reclassification despite a foreign subsidiary (JNK India Private FZE) — consistent with that FZE being near-dormant (F3). Line stands ready if overseas ops (Iraq branch) scale. |
| F2-a | F2 | §5 L521/L531/L532 vs §2 L225 | 225, 521, 531, 532 | "Non Controlling Interest (18.42)" ; consol PAT "96.25" vs standalone "135.46" | FORWARD-SIGNAL | Consolidated PAT Rs 9.63 Cr is **Rs 3.92 Cr BELOW** standalone Rs 13.55 Cr (−28.9% of standalone PAT) despite consolidated revenue being Rs 16.4 Cr HIGHER. Gap swung from +4.4% (Q4FY26) to −28.9% (Q1FY27) = ~33pp swing, far above the 5pp trigger. Subsidiaries add revenue but subtract profit; Chemdist NCI drag Rs 1.84 Cr. Even owner-attributable PAT (11.47) trails standalone by Rs 2.08 Cr. |
| F2-b | F2 | §5 L514 vs §2 L218; Notion item 3/T2 | 514, 218 | consol "Profit before Exceptional Items and Tax … 146.35" vs standalone "185.41" | AMBIGUOUS | Consolidated operating EBITDA margin 8.8% vs standalone 10.5% — **both below the 13% thesis target; consolidated is below the 10% kill line** on an operating basis (14.5%/12.2% if other income is included). Definition-dependent — generate a concall question on the company's own EBITDA-margin definition and the Process-Equipment drag. |
| F3-a | F3 | §10 L436 Other Matters; §12 L400-403 | 436-438 | "two subsidiaries reflects total income of Rs. 2.87 million, total net loss after tax of Rs. 0.69 million" | CONFIRMATORY-NEGATIVE | Two of three subsidiaries (the FZE + one other, per Other Matters) are near-dormant: combined Rs 0.29 Cr income, Rs 0.07 Cr loss for the quarter. Not shells in the balance-sheet-cleanup sense (no going-concern EoM to reconcile), but negligible operations. The material subsidiary is Chemdist (Process Equipment). |
| F6-a | F6 | §1 agenda 2/3; §13 B.1; §14 B.2; §6 Note VI | 53-59, 668, 802-813 | "amendment to the Main Object Clause … for the adoption of new line of business" ; "setting up of Branch Office … in the Republic of Iraq" ; "will be evaluated and accounted for … in the period in which they are notified" | FORWARD-SIGNAL | Dated/dateable commitments: (1) MOA amendment into marine/offshore/heavy-industrial EPC, subject to shareholder approval → EGM/postal-ballot incoming; (2) Iraq branch office → overseas execution build; (3) new-line capex "funded through … internal accruals and/or borrowings" → leverage signal; (4) Labour-Code accounting pending rule notification. See Commitment Register. |
| F7-a | F7 | §14 B.2 L802-813; §6 Note VI L664-669 | 803-813, 667-668 | "incurred incrementally based on specific project requirements, contract awards, and operational needs … as deemed appropriate by the Management from time to time" ; "The Government is in the process of notifying related rules" | AMBIGUOUS | Two pre-emptive hedges: capex quantum for the new business is deliberately un-numbered (`NO_QUANTUM`), and the consolidated Labour-Code note adds "in the process of notifying / will be evaluated" language the standalone note omitted. Both defer a future cost. Question: expected capex range and gearing for the marine/offshore pivot. |
| F8-a | F8 | §5 L519/L518; §6 Note VII L678-680 | 519, 518, 678 | consol "Deferred Tax Expense/(Income) (539) / (22.55) / (1.16) / (32.94)" ; "deferred tax assets of Rs. 7.07 million … recognised on acquisition" | FORWARD-SIGNAL | Consolidated deferred tax is a **credit in all four periods** (DTA recognition, incl. Rs 0.71 Cr Chemdist acquisition DTA + subsidiary-loss DTA), shielding ~390 bps of FY26 ETR. As losses reverse / DTA exhausts, consolidated ETR steps up. Consolidated Q1FY27 ETR is already **34.2% vs 25.17% statutory** — consolidated current tax (Rs 5.55 Cr) equals standalone despite lower consolidated PBT, so loss-making subsidiaries inflate the group ETR while the parent pays full freight. Double drag on consolidated PAT. No "earlier-years" tax adjustment line present. |
| F9-a | F9 | §2 L228 / §5 L524 | 228, 524 | standalone "Remeasurement gains / (loss) of Defined benefit plans (7.99)" vs FY26 "3.92" | AMBIGUOUS | Single-quarter actuarial OCI **loss of Rs 0.80 Cr in Q1FY27 exceeds (and flips the sign of) the full prior-year FY26 gain of Rs 0.39 Cr** — checklist trigger for an assumption change (likely discount-rate cut). Standalone and consolidated remeasurement are identical (7.99m), confirming gratuity sits almost entirely in the parent. Verify actuarial assumptions (discount rate, salary escalation) at the Annual Report. |
| F12-a | F12 | §7b L606 segment result | 606, 600 | Process Equipment segment result "(13.30)" ; revenue "162.53 / 352.87" | FORWARD-SIGNAL | Process Equipment (Chemdist) swung from a Rs 1.50 Cr profit (Q4FY26) to a **Rs 1.33 Cr loss (Q1FY27)** as segment revenue more than halved (Rs 35.29 → Rs 16.25 Cr). This is the engine of the consolidated PAT drag (F2-a) and the goodwill-impairment risk (F1-a). |
| F12-b | F12 | §7c L617 / §7d L624 segment assets & liabilities | 617, 624 | Process Equipment assets "996.79 / 1,139.86" ; liability "624.55 / 679.25" | AMBIGUOUS | Process Equipment assets fell Rs 14.3 Cr and liabilities Rs 5.5 Cr Q4→Q1 alongside the revenue collapse — WC unwinding on completed contracts OR order-book exhaustion. Ambiguous direction → concall question. (By contrast Combustion assets +Rs 234 Cr YoY and liabilities +Rs 194 Cr YoY = core order-book/WC build, healthy.) |
| F13-a | F13 | §1 agenda 2/3; §13; §14 | 53-59 | "amendment to the Main Object Clause … new line of business" ; "setting up of Branch Office … in the Republic of Iraq" | FORWARD-SIGNAL | Board is enabling a strategic pivot into marine/offshore + heavy-industrial EPC (steel/cement/mining/oil&gas) and an Iraq branch. This is the **NARRATIVE-ROTATION RISK materialising at the charter level** — away from the core fired-heater franchise. MOA change needs shareholder approval (EGM/postal ballot). Capital-raising enabling resolutions are ABSENT this meeting; funding named as accruals/borrowings only. |
| F13-b | F13 | §15 Annexure C `SMP_DESIGNATION_ENDED`; Notion item 4 | 829-851 | "Ceased to be designated as a Senior Management Personnel w.e.f. August 11, 2026 (from closure of business hours)" ; "no cessation of employment" | CONFIRMATORY-NEGATIVE | SMP changes = 2 designations added (Pulujkar–procurement; Phatak–projects) + 1 ended (Ravikumar Mudali Vallathur, employment continues). **NO CFO appointment or resignation** anywhere in the Board Outcome or SMP annexure → the "permanent CFO" monitorable (thesis item 4) is **UNRESOLVED**; interim-CFO status persists this quarter. No independent-director renewal/non-renewal; no AR/AGM/dividend items (`AGENDA_SCOPE_LIMITED`). |
| F14-a | F14 | §3 Note III vs §6 Note III; §6 Note VI; §8 vs §4; §6 Note VII | 274-275, 585, 673, 658 vs 290 | standalone "for the first time in the unaudited consolidated financial … quarter ended December 31, 2025" vs consolidated "for the first time in the audited consolidated financial results" ; "Chemdist Technologies Private Limited" (JNK dropped, L673) | NEUTRAL-FACT | Cumulative drafting inconsistencies: (a) segment-first-disclosure described as "unaudited Dec-2025 quarter" (standalone) vs "audited" FY26 (consolidated); (b) entity named "JNK Chemdist Technologies Private Limited" (L403) vs "Chemdist Technologies Private Limited" (L673); (c) Labour-Code note quantified standalone (Rs 0.92 Cr) but hedged/forward in consolidated; (d) IPO WC "proposed" printed 2,626.90 standalone (L290) vs 2,620.00 consolidated (L658) — same Rs 279.74 Cr total, `DISCREPANCY_VS_STANDALONE`, likely a single OCR digit-swap. Individually immaterial, collectively a governance data point. |
| F15-a | F15 | §12 L400-403; §6 Note VII `BUSINESS_COMBINATION`/`COMPARABILITY`; `NO_PRIOR_LEDGER` | 400-403, 681-683 | "numbers pertaining to the quarters … are not comparable with quarter ended June 30, 2025 to the extent of aforesaid acquisition accounting" | FORWARD-SIGNAL | 3-entity list (FZE, Renewable, Chemdist). Verbatim quarter-over-quarter diff **could not be run (no prior ledger)** — flagged, not fabricated. In-document YoY diff IS runnable: Chemdist/Process Equipment was nil in Q1FY26 (pre-acquisition, 1 Oct 2025) and is consolidated now → Q1FY27-vs-Q1FY26 growth is inorganic to the extent of Chemdist; management itself flags non-comparability. Prior-quarter (Q4FY26) entity add/drop/rename cannot be confirmed this run. |

---

## CHECKLIST SCORECARD (all 17)

| Check | Status | One-line basis |
|-------|--------|----------------|
| F1 | **FINDING** | 4 `ZERO_STANDING` lines read at L219/230/515/526. Exceptional-items line = live impairment channel for Rs 1.72 Cr Chemdist goodwill (F1-a); reclassify-to-P&L line dormant despite foreign sub (F1-b). |
| F2 | **FINDING** | S-vs-C decomposed for all 4 periods. Consol PAT Rs 3.92 Cr BELOW standalone (−28.9%), gap swing ~33pp > 5pp trigger (F2-a); consol EBITDA margin 8.8% < 13% target / below 10% kill (F2-b). |
| F3 | **FINDING** | Cost lines differ S vs C (Chemdist has real ops — not a shell) but Other Matters shows two subsidiaries with only Rs 0.29 Cr income / Rs 0.07 Cr loss = near-dormant (F3-a). No going-concern EoM to reconcile. |
| F4 | **PASS** | Unaudited-by-principal portion (two subs via other auditors) = Rs 0.29 Cr income, Rs 0.07 Cr net loss = 0.7% of consol PAT — below the 10% threshold. Material subsidiary (Chemdist) is principal-auditor reviewed. Trend unavailable (no prior ledger). |
| F5 | **PASS** | Standalone conclusion (L162-173) and consolidated conclusion (L405-432) both **unmodified/clean**; **no EoM, no Going Concern** para in either (`EOM_ABSENT`, `GOING_CONCERN_ABSENT`). Verbatim: "nothing has come to our attention that causes us to believe … it contains any material misstatement" (L162-173). **Caveat flagged: prior-quarter verbatim EoM diff could not be run (`NO_PRIOR_LEDGER`).** |
| F6 | **FINDING** | Lexicon hits mined from notes + cover letter: MOA/Iraq "subject to approval", capex "will be … funded", Labour-Code "will be evaluated" (F6-a). See Commitment Register. |
| F7 | **FINDING** | New pre-emptive hedges: un-numbered capex ("as deemed appropriate by the Management from time to time") and consolidated-only Labour-Code deferral language (F7-a). |
| F8 | **FINDING** | Consolidated deferred tax a credit in all 4 periods (DTA build, ~390bps FY26 shield); consol ETR 34.2% vs 25.17% statutory; consol current tax = standalone despite lower consol PBT (F8-a). No earlier-year tax adjustment line. |
| F9 | **FINDING** | Q1FY27 actuarial OCI loss Rs 0.80 Cr exceeds and inverts full FY26 gain Rs 0.39 Cr = assumption-change flag; verify at AR (F9-a). |
| F10 | **PASS** | Basic EPS = Diluted EPS in every period (nil spread → no live dilutive instruments); restated diluted EPS still equals basic. No corporate action on share count this quarter (IPO was FY25). Standalone paid-up value OCR-gapped (L233-234) — cannot fully verify, but consolidated paid-up captured and no issuance disclosed. |
| F11 | **PASS** | Other Equity: standalone Rs 555.38 Cr vs consolidated Rs 556.46 Cr (annual column only) — gap Rs 1.08 Cr (~0.2%) < 5%; reconciles to subsidiary reserves net of NCI/elimination. No third-party (rating) number in scope to cross-check. Standalone paid-up OCR-gapped. |
| F12 | **FINDING** | Process Equipment result swung profit→loss (Rs 1.50 Cr → −Rs 1.33 Cr) on halved revenue (F12-a); segment assets/liabilities fell = ambiguous WC unwind (F12-b). Core Combustion assets/liabilities both up = order-book build. |
| F13 | **FINDING** | MOA pivot to marine/offshore/heavy-EPC + Iraq branch (F13-a); SMP designation ended + **no permanent-CFO appointment** (F13-b); `AGENDA_SCOPE_LIMITED`. |
| F14 | **FINDING** | Drafting inconsistencies: segment-first-disclosure audited-vs-unaudited wording, Chemdist name variant, Labour-Code note divergence, IPO WC figure discrepancy (F14-a). |
| F15 | **FINDING** | 3-entity list; Chemdist inorganic YoY, management flags non-comparability (F15-a). Prior-quarter verbatim diff not runnable (`NO_PRIOR_LEDGER`) — flagged. |
| F16 | **N.A.** | Results/Reg-33 filing, not a presentation deck. |
| F17 | **N.A.** | Results/Reg-33 filing, not a concall transcript. (Monitorable-silence items captured in the note below for A4.) |

GATE A3: all 17 marked, no blanks → **pass**.

---

## COMMITMENT REGISTER (from F6)

| Commitment | Implied date | Note / ref | Status word |
|------------|--------------|------------|-------------|
| MOA Main-Object amendment (new line of business: marine/offshore + heavy-industrial EPC) | Next EGM / postal ballot (subject to shareholder + regulatory approval) | Agenda 2, L53-56; Annexure B.1 L729-758 | board has approved (pending shareholder) |
| Setting up overseas Branch Office in Republic of Iraq | On "necessary approval" (undated) | Agenda 3, L58-59 | board has approved (pending approval) |
| Capex for new line of business ("Initial investments … towards establishing foundational engineering and execution capabilities"; funded by internal accruals and/or borrowings) | Incremental / undated, per contract awards | Annexure B.2, L802-813 | proposes to / intends to (no quantum) |
| New Labour Codes — impact "will be evaluated and accounted for … in the period in which they are notified" | On Government rule notification | Consolidated Note VI, L664-669 | in the process of (external) |
| IPO proceeds fully utilised (Rs 281.70 Cr) as on 30 Jun 2026, nil unutilised | Achieved | Notes V, L293 / L661 | has been completed |
| IPO of 1,56,49,967 equity shares | FY25 (30 Apr 2024 listing) | Note IV, L276-282 | has completed |
| Chemdist "Process Equipment" segment became operational | FY26 | Consolidated Note III, L583-584 | became operational (completed) |

---

## MONITORABLES UNRESOLVED FROM THIS DOCUMENT (for A4; F17 is N.A. on a Reg-33 filing)

A Reg-33 quarterly filing carries no cash-flow statement, no balance sheet detail and no
MD&A/concall. The following Notion monitorables therefore **cannot be resolved from this doc**
and remain open — sustained silence on a deteriorating metric is a confirmatory negative:

1. **Operating CFO positive** — no cash-flow statement in this filing. UNRESOLVED.
2. **Debtor days < 180** — no receivables/balance-sheet breakdown. UNRESOLVED.
3. **EBITDA margin ≥ 13% (kill < 10%)** — COMPUTABLE and flagged: consol operating margin 8.8%, standalone 10.5% (F2-b). Below target; consol below the operating kill line.
4. **Permanent CFO** — no appointment; interim status persists (F13-b). UNRESOLVED / confirmatory-negative.
5. **Dangote / export commentary** — none; the only overseas signal is the Iraq branch (F6-a/F13-a). UNRESOLVED.
6. **T1 — BPCL Bina Rs 1,050 Cr sub-contract, Rs 80-130 Cr/qtr recognition + note** — **no explicit note or disclosure** in this filing. Combustion segment revenue is +65% YoY (Rs 99.10 → Rs 163.71 Cr) and could embed Bina, but it is not broken out or named. Silence flagged.
7. **T2 — margin 14-16% (kill < 10%)** — see item 3; consolidated operating margin below range.
8. **JNK Global = 82% of order book** — order-book composition not disclosed in filing. UNRESOLVED.

---

## NOTES ON LEDGER RECONCILIATION / OCR CROSS-CHECKS

- Consolidated revenue Q4FY26 printed "238440" (ledger §5 read as 2,384.40) is reconciled to
  **Rs 338.44 Cr** via segment total L601 (Combustion 303.15 + Process 35.29) — OCR 3→2 error, not a restatement. Relevant to F2/F14.
- Consolidated depreciation Q4FY26 "0.05" (L511) is an OCR digit-drop (FY 85.30, standalone Q4 21.24); immaterial to findings.
- `DISCREPANCY_VS_STANDALONE` (IPO WC proposed L290 vs L658) resolves to the same Rs 279.74 Cr total — single OCR digit-swap, logged under F14, not a genuine restatement.
- All 4 `ZERO_STANDING`, `BUSINESS_COMBINATION`, `NEW_LINE_OF_BUSINESS`, `NEW_SEGMENT`,
  `NCI_PRESENT`, `UNAUDITED_BY_PRINCIPAL_AUDITOR`, `EOM/OTHER_MATTERS/GOING_CONCERN ABSENT`,
  `RESTATEMENT`, `SMP_DESIGNATION_ENDED`, `AGENDA_SCOPE_LIMITED` ledger flags read at source and mapped to F1/F2/F3/F4/F5/F6/F8/F13/F14/F15. 100% reconciled.

```yaml
stage: A3-forensics
company: "JNKINDIA"
quarter: "Q1 FY27"
doctype: "results"
model: claude-opus-4-8
status: complete
forensics_path: "/home/user/inflection-pipeline/runs/jnkindia-q1fy27/work/forensics_results_jnkindia_q1fy27.md"
ledger_reconciled_pct: 100
checklist:
  F1: FINDING
  F2: FINDING
  F3: FINDING
  F4: PASS
  F5: PASS
  F6: FINDING
  F7: FINDING
  F8: FINDING
  F9: FINDING
  F10: PASS
  F11: PASS
  F12: FINDING
  F13: FINDING
  F14: FINDING
  F15: FINDING
  F16: N.A.
  F17: N.A.
findings:
  - {id: "F1-a", check: "F1", line: "219/515/678", classification: "FORWARD-SIGNAL", implication: "Exceptional-items line is a live impairment channel for Rs 1.72 Cr Chemdist goodwill on a now-loss-making segment"}
  - {id: "F1-b", check: "F1", line: "230/526", classification: "NEUTRAL-FACT", implication: "No FCTR/hedge reclassification despite foreign FZE sub; line ready if Iraq/overseas ops scale"}
  - {id: "F2-a", check: "F2", line: "225/521/531/532", classification: "FORWARD-SIGNAL", implication: "Consol PAT Rs 3.92 Cr below standalone (-28.9%); gap swing ~33pp > 5pp; subsidiaries add revenue but subtract profit"}
  - {id: "F2-b", check: "F2", line: "514/218", classification: "AMBIGUOUS", implication: "Consol operating EBITDA margin 8.8% below 13% target and below 10% kill line; definition-dependent, needs concall clarification"}
  - {id: "F3-a", check: "F3", line: "436", classification: "CONFIRMATORY-NEGATIVE", implication: "Two subsidiaries near-dormant (Rs 0.29 Cr income); Chemdist is the only material sub"}
  - {id: "F6-a", check: "F6", line: "53-59/668/802-813", classification: "FORWARD-SIGNAL", implication: "Dated commitments: MOA new-business, Iraq branch, borrowings-funded capex, pending Labour-Code accounting"}
  - {id: "F7-a", check: "F7", line: "803-813/667-668", classification: "AMBIGUOUS", implication: "New hedges: un-numbered capex quantum + consolidated-only Labour-Code deferral; capex/gearing question"}
  - {id: "F8-a", check: "F8", line: "519/518/678", classification: "FORWARD-SIGNAL", implication: "Persistent consol deferred-tax credits (~390bps FY26 shield) + elevated consol ETR 34.2% vs 25.17%; future ETR step-up"}
  - {id: "F9-a", check: "F9", line: "228/524", classification: "AMBIGUOUS", implication: "Q1FY27 actuarial OCI loss Rs 0.80 Cr exceeds full FY26 gain Rs 0.39 Cr = assumption change; verify at AR"}
  - {id: "F12-a", check: "F12", line: "606/600", classification: "FORWARD-SIGNAL", implication: "Process Equipment swung to Rs 1.33 Cr loss on halved revenue; engine of consol PAT drag and goodwill-impairment risk"}
  - {id: "F12-b", check: "F12", line: "617/624", classification: "AMBIGUOUS", implication: "Process Equipment assets/liabilities fell = WC unwind vs order-book exhaustion; concall question"}
  - {id: "F13-a", check: "F13", line: "53-59", classification: "FORWARD-SIGNAL", implication: "MOA pivot into marine/offshore/heavy-EPC + Iraq branch = narrative-rotation risk at charter level; EGM/postal ballot incoming"}
  - {id: "F13-b", check: "F13", line: "829-851", classification: "CONFIRMATORY-NEGATIVE", implication: "No permanent-CFO appointment; interim-CFO status persists; SMP designation ended (employment continues)"}
  - {id: "F14-a", check: "F14", line: "274-275/585/673/658", classification: "NEUTRAL-FACT", implication: "Cumulative drafting inconsistencies (segment wording, Chemdist name, Labour-Code note, IPO WC figure) = governance data point"}
  - {id: "F15-a", check: "F15", line: "400-403/681-683", classification: "FORWARD-SIGNAL", implication: "Chemdist inorganic YoY, management flags non-comparability; prior-quarter verbatim entity diff not runnable (NO_PRIOR_LEDGER)"}
forward_signals: ["F1-a", "F2-a", "F6-a", "F8-a", "F12-a", "F13-a", "F15-a"]
ambiguous: ["F2-b", "F7-a", "F9-a", "F12-b"]
commitments:
  - {commitment: "MOA Main-Object amendment (new line of business: marine/offshore + heavy-industrial EPC)", implied_date: "next EGM/postal ballot", ref: "Agenda 2 L53-56; Annexure B.1 L729-758", status_word: "board has approved"}
  - {commitment: "Overseas Branch Office in Republic of Iraq", implied_date: "on necessary approval (undated)", ref: "Agenda 3 L58-59", status_word: "board has approved"}
  - {commitment: "Capex for new line of business, funded by internal accruals and/or borrowings", implied_date: "incremental/undated", ref: "Annexure B.2 L802-813", status_word: "proposes to (no quantum)"}
  - {commitment: "New Labour Codes accounting on rule notification", implied_date: "on Government notification", ref: "Consolidated Note VI L664-669", status_word: "in the process of"}
  - {commitment: "IPO proceeds fully utilised (Rs 281.70 Cr), nil unutilised", implied_date: "as on 30-Jun-2026", ref: "Notes V L293/L661", status_word: "has been completed"}
  - {commitment: "IPO of 1,56,49,967 equity shares", implied_date: "FY25 (listed 30-Apr-2024)", ref: "Note IV L276-282", status_word: "has completed"}
  - {commitment: "Chemdist Process Equipment segment operational", implied_date: "FY26", ref: "Consolidated Note III L583-584", status_word: "became operational"}
gate_a3: pass
blank_checks: []
```
