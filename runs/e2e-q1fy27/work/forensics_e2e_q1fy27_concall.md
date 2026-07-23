# A3 FORENSIC NOTES — E2E Networks Limited (E2E) — Q1 FY27 — DOCTYPE: CONCALL

Inputs read verbatim and reconciled 100%:
- A1 extract: `runs/e2e-q1fy27/work/extract_concall_e2e_q1fy27.txt` (39 turns, source lines 1-76)
- A2 ledger: `runs/e2e-q1fy27/work/ledger_concall_e2e_q1fy27.md` (all rows read at cited line/turn: Participants P1-P19; Turns 1-39; Questions Q1-Q31; Numbers N1-N24; Forward/Hedge F1-F21)
- Cross-ref filing: `runs/e2e-q1fy27/work/extract_results_e2e_q1fy27.txt` (Rs Lakhs, x0.01 -> Cr)
- Cross-ref deck: `runs/e2e-q1fy27/work/extract_presentation_deck_e2e_q1fy27.txt` (Rs Millions, x0.1 -> Cr)

Ledger reconciliation: 24/24 NUMBERS rows, 39/39 TURNS, 31/31 QUESTIONS, 21/21 FORWARD rows, 19/19 PARTICIPANT rows read at source. No unread row. 100%.

Doctype note: this is a concall transcript. Per the checklist's doctype-applicability rule, F6/F7/F17 apply; balance-sheet / auditor / statement-table checks (F1-F5, F8-F14, F16) are structurally N.A. to a transcript and are marked so with a one-line reason. F15 is normally a results/consolidation check but is elevated to FINDING here because the transcript itself names entities that diff against the audited consolidation list (cross-reference mandate).

---

## FINDINGS TABLE

| id | check | ledger row ref | line / turn / slide | short verbatim quote | classification | forward implication |
|---|---|---|---|---|---|---|
| FN-01 | F17 | N19 | Turn 32 (extract line 118) | "the loan which stands as of now is broadly 450 CR ... it would be increasing across ... in the near term" | FORWARD-SIGNAL | First-ever labelled debt figure, absent from filing and deck. Mar-26 audited borrowings were Rs103.2 Cr (deck p21, 1,032 Mn); ~4.4x in one quarter. Net cash ~Rs239 Cr at Mar-26 (current financial assets 3,982 Mn less borrowings 1,032 Mn less lease 559 Mn) very likely flips to NET DEBT now. Corroborated by finance cost +173% QoQ (deck p19: 101 vs 37 Mn; filing line 88: 1,005.15 vs 368.04 lakhs). Peak-for-year figure requested and NOT given. |
| FN-02 | F7 | Q24 supp / F17 | Turn 32 (line 118) | "possible to quantify that sir total loan amount peak bid for the year quantifying that" [no management response captured] | CONFIRMATORY-NEGATIVE | Peak-loan guidance requested; turn ends with no answer. Deflection on the one metric that would size the leverage ramp just disclosed in FN-01. |
| FN-03 | F7 | F4 / Q11 | Turn 12 (line 58) | "We don't provide a guidance on MR[R]" | CONFIRMATORY-NEGATIVE | Explicit guidance decline. One node in a serial pattern: MRR, full-year capex (x2), peak loan, customer-mix %, SovCloud funding structure all declined; zero customers named all call. |
| FN-04 | F15 | ENTITY note (ledger p226) | Turn 16 (line 70) | "we recently set up ... entities in Delware and the GPU infrastructure entity and the soft cloud" | FORWARD-SIGNAL | Transcript names THREE entities (Delaware US-sales entity; a separate "GPU infrastructure entity"; SovCloud). Audited consolidation lists only ONE WOS: "Sovcloud Technologies Limited" (filing note 9, lines 227-228; auditor consolidated para 4, lines 370-372). Delaware entity and the separate GPU-infra entity are NOT in the consolidation. SovCloud's stated purpose — "hold and contract large scale GPU clusters" (Turn 10) plus deck p14 "enabling funding arrangements" — is an off-balance-sheet-SPV / GPU-vehicle watch. Funding structure declined ("very early days"). |
| FN-05 | F17 | N16/N16b/N17 | Turn 30 (line 112) | "India revenue was about like 20 21% ... international was like closer to 37 ... and rest is like all domestic revenue" | AMBIGUOUS | (a) Management's ~20-21% India vs analyst's stated recollection of ~40% "last quarter" (N16b) — unreconciled, neither side clarifies which quarter. (b) India 20-21% + international ~37% + "rest all domestic" does not coherently sum (India is itself domestic). Filing is single-segment (note 6, line 138), so no geographic disclosure exists to verify against — first-time, unauditable split. |
| FN-06 | F17 | N21/N22/N23/N24 | Turn 34 (line 124) | "nearly 5100 is the current capacity which is live ... does not include the ... another 1,024 B200 we are expecting soon" | AMBIGUOUS | 3,900 (Q4 call = "APU and GPU storage all capacities put together") is replotted on this deck's "GPU Trajectory" chart (p11, FY26=3,900) as a GPU count beside a GPU-only 5,100 — basis change unreconciled. Direct deck-vs-concall contradiction: deck p11 states "~5100 GPUs live, (including 1024 B200)" whereas the call says 5,100 EXCLUDES the incoming 1,024 B200. Whether the already-live 1,024 Blackwell (N10, Turn 5) and the "expecting soon" 1,024 B200 (N24) are the same lot restated or two lots is not disambiguated. |
| FN-07 | F17 | N6 | Turn 6 (line 40) | "IDA margin expended 1450 basis points compared to Q4 2026" | NEUTRAL-FACT | CFO's spoken +1450 bps matches the deck's rounded figure (p19: "1450 bps") rather than the precise filing-derived delta (75.2% vs 60.7% ≈ +1444-1446 bps). Immaterial in magnitude; confirms the call reads from the deck, not the audited statement. Low priority. |
| FN-08 | F6 | F11 / Q20 / N.A. | Turn 24 (line 94); reinforced Turn 8 (line 46), Turn 20 (line 82) | "you intimated a price increase going live then you rolled it back ... pushed it out"; "increase the contract length from normal 1 month to about say a year ... pay you like some advance" | FORWARD-SIGNAL | Beat attributed to capacity + utilisation + operating leverage, NOT pricing ("very moderate impact" Turn 8; "our numbers reflect the increased capacity and increased operating leverage more than anything else" Turn 20). July hike (CPU especially, memory-cost driven; some GPU) intimated, rolled, pushed. Reads two ways: no pricing tailwind yet baked into the 75.2% EBITDA margin (potential upside) vs memory-cost inflation as a cost headwind. Customers shifting 1-month -> 1/2/3-year contracts, paying advances to lock price = annuity/visibility improvement (addresses contract-duration monitorable, checklist item 5). |
| FN-09 | F6 | N13/N14 | Turn 26 (line 100) | "at least ... the minimum a six year life cycle for all the GPU generations ... we don't ... foresee that there is a massive price compression" | AMBIGUOUS | Management ASSERTION (not evidence) reaffirming 6-yr GPU life, older gens "run very strong." Bears directly on depreciation/asset-life risk: filing D&A Rs60.6 Cr this quarter (line 87), annualising toward ~Rs242 Cr on PPE Rs1,497 Cr at Mar-26 (deck p21, 14,966 Mn) — an implied life far short of 6 years if sustained. Unverifiable claim; Role 5 promise-vs-delivery tracking item. |
| FN-10 | F15 | Q28/Q29 | Turn 36 (line 130) | "L[&]N ... is an arms length partner ... we are a buyer over there ... they are the buyers ... jointly ... we do go to customers" | NEUTRAL-FACT | Re-rates checklist item 4: L&T is an arm's-length mutual buyer/seller + joint GTM, NOT a marquee commercial contract. Note deck p12 lists Shrimati Ambastha, "CEO, L&T-Cloudfiniti DC business," as a Non-Executive Non-Independent Director — a board link exists, but the commercial relationship is explicitly arm's-length. Related-party watch, not a revenue anchor. |

---

## CHECKLIST SCORECARD (all 17; one status each — GATE A3)

| Check | Status | One-line basis |
|---|---|---|
| F1 ZERO-VALUE STANDING ITEMS | N.A. | Transcript carries no standing financial-statement table; ZERO_STANDING not applicable to concall (ledger line 184). |
| F2 STANDALONE vs CONSOLIDATED | N.A. | No S-vs-C tables spoken on the call. (Filing shows S=C: sole subsidiary incorporated 17-Jun-26, non-operational; comparatives are standalone.) |
| F3 SHELL-ENTITY DETECTION | N.A. | No cost-line comparison in a transcript. (Sovcloud is a pre-operational entity per filing note 9 — a results-doctype check.) |
| F4 UNAUDITED CONTRIBUTION RATIO | N.A. | Auditor "Other Matters" language does not appear in a transcript. |
| F5 GOING CONCERN / EoM SCOPE | N.A. | No EoM/going-concern paragraph in a transcript; auditor issued unmodified review conclusion (filing pages 5, 7). |
| F6 FORWARD-COMMITMENT MINING | FINDING | Dated/dateable commitments mined: B200 next lot "next couple of months" (Turn 12/22), July price hike rolled+pushed (Turn 24), loan "increasing ... near term" (Turn 32), capacity into "Varin" (Turn 22), +1,024 B200 "expecting soon" (Turn 34). See FN-08/FN-09 and Commitment Register. |
| F7 HEDGE PHRASE MINING | FINDING | Dense hedging + serial guidance declines: "very early days" (Turn 16/32), "let us not do this today" (Turn 18), "I haven't decided what percentage" (Turn 28), peak-loan unanswered (Turn 32). FN-02, FN-03. |
| F8 TAX FORENSICS | N.A. | Tax not discussed on the call. (ETR/deferred-tax analysis — filing Q1 deferred-tax charge 1,474.43 lakhs, ETR ~25.15% vs 25.17% statutory — is a results-doctype check.) |
| F9 OCI FORENSICS | N.A. | OCI not mentioned on the call. (Filing OCI swing -505 lakhs this Q vs +125 lakhs FY26 is flagged for the results-doctype A3 run.) |
| F10 SHARE COUNT / DILUTION | N.A. | No paid-up-capital / EPS table in a transcript. 10:1 split (filing note 4; deck p14) not discussed on the call. |
| F11 RESERVES / NET WORTH TIE-OUT | N.A. | No reserves/net-worth figures spoken on the call. |
| F12 SEGMENT FORENSICS | N.A. | Single business segment (filing note 6); no segment table in a transcript. |
| F13 BOARD OUTCOME BEYOND RESULTS | N.A. | Board-meeting outcome/agenda lives in the results filing (pages 1-2), not the transcript. |
| F14 NOTE DRAFTING INCONSISTENCIES | N.A. | No notes / auditor letter text in a transcript to diff. |
| F15 ENTITY LIST DIFFS | FINDING | Concall names Delaware + separate GPU-infra entity + SovCloud (Turn 16); audited consolidation lists only Sovcloud Technologies Ltd (filing note 9; auditor consol para 4). FN-04, FN-10. |
| F16 PRESENTATION-SPECIFIC | N.A. | F16 applies to the presentation doctype; this run's doctype is concall. (The 3,900-redefinition surfaced on the call is carried under F17/FN-06.) |
| F17 CONCALL SILENCE AUDIT | FINDING | Silence/deflection table below + cross-document numeric reconciliation vs filing/deck (FN-01, FN-05, FN-06, FN-07). |

Blank checks: none. GATE A3 = PASS.

---

## COMMITMENT REGISTER (from F6)

| commitment | implied date | ref | status word |
|---|---|---|---|
| Next lot of B200 GPUs delivered/deployed | "next couple of months" | Turn 12 (F3), Turn 22 (F10) | expected / underway |
| +1,024 B200 GPUs added on top of 5,100 live | "expecting soon" | Turn 34 (N24) | expected |
| July price hike (CPU especially, some GPU) | intimated, rolled back, pushed further out | Turn 24 (Q20) | deferred |
| Loan outstanding to rise from ~Rs450 Cr | "increasing across ... in the near term" | Turn 32 (N19/F15) | underway |
| Capacity expansion into "Varin" [garbled locale] | undated | Turn 22 (F10) | intends |
| Shift capacity mix toward 2-3 year contracts | ongoing, "haven't decided what percentage" | Turn 28 (F13) | underway |
| SovCloud large-scale GPU build + funding arrangement | "very early days ... we'll obviously announce" | Turn 16 / Turn 32 (F5/F16) | initiated |
| Next-gen architecture planning (B300 / Vera Rubin) | "planning underway" (deck p11) | Turn 26 (Q21) | initiated |

---

## WHAT WAS NOT DISCUSSED / DECLINED (F17 silence audit)

Prior-quarter ledger NOT provided, so consecutive-quarter silence counts rely on in-call analyst references to "last quarter" plus the deck; flagged for Role 5 to attach counts.

| Item | Status on this call | Turn(s) | Note |
|---|---|---|---|
| MRR / exit-MRR guidance (full year) | Declined, explicit | 12 | "We don't provide a guidance on MR[R]." |
| Full-year capex plan | Declined x2 (REPEAT_QUESTION) | 22, 32 | No figure either time. |
| Peak loan for the year | Asked, unanswered (trails off) | 32 | Quantum of leverage ramp left open (FN-02). |
| Customer mix % by segment | Declined | 18 | "let us not do this today." |
| Named customers | Zero named all call | throughout | Consistent with deck (no customer names). Persists. |
| SovCloud funding structure | Declined x2 (REPEAT_QUESTION) | 16, 32 | "very early days." |
| Preferential-issue utilisation itemisation | Declined on call | 34 | (Deck p17 DOES provide the utilisation table — Rs1,326.79 Mn balance unutilised; call declined it anyway.) |
| 2-year-out GPU count ambition | Declined | 30 | No figure. |
| Training vs inference revenue/margin split | Declined | 14 | "hard to pin down the fungibility of compute." |
| Interest / DC-cost granularity | Vague only | 30 | "not ... super granular numbers"; DC cost "close to 20" (unit unstated, N18). |

---

## CLASSIFICATION SUMMARY

- FORWARD-SIGNAL (flag for A4 questions / Role 5): FN-01, FN-04, FN-08
- AMBIGUOUS (flag for A4 questions): FN-05, FN-06, FN-09
- CONFIRMATORY-NEGATIVE (Role 5 tone/promise-vs-delivery): FN-02, FN-03
- NEUTRAL-FACT: FN-07, FN-10

Tone/specificity read (Role 5): management is fluent and confident on narrative (sovereign AI, "day zero," "super cycle") but systematically declines every quantitative forward metric — MRR, capex, peak loan, customer mix, SovCloud funding, GPU ambition. The one hard forward number volunteered (loan ~Rs450 Cr) is the one that cuts against the story (net-cash-to-net-debt flip). Archetype: qualitative-expansive / quantitative-evasive. Conservative read: lean bear on the leverage ramp and the unconsolidated Delaware + GPU-infra entities until FN-01 and FN-04 are answered.

```yaml
stage: A3-forensics
company: "E2E"
quarter: "q1fy27"
doctype: "concall"
model: claude-opus-4-8
status: complete
forensics_path: "runs/e2e-q1fy27/work/forensics_e2e_q1fy27_concall.md"
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
  F15: FINDING
  F16: N.A.
  F17: FINDING
findings:
  - {id: "FN-01", check: "F17", line: "Turn 32", classification: "FORWARD-SIGNAL", implication: "Loan ~Rs450 Cr first disclosed; vs Mar-26 borrowings Rs103.2 Cr (4.4x); net cash ~Rs239 Cr likely flips to net debt; +173% QoQ finance cost corroborates; peak-loan declined"}
  - {id: "FN-02", check: "F7", line: "Turn 32", classification: "CONFIRMATORY-NEGATIVE", implication: "Peak-loan-for-year requested, no answer captured; deflection on the metric sizing the leverage ramp"}
  - {id: "FN-03", check: "F7", line: "Turn 12", classification: "CONFIRMATORY-NEGATIVE", implication: "Explicit MRR-guidance decline; node in serial declines (capex, peak loan, mix, SovCloud funding, named customers)"}
  - {id: "FN-04", check: "F15", line: "Turn 16", classification: "FORWARD-SIGNAL", implication: "Concall names Delaware + GPU-infra entity + SovCloud; audited consolidation lists only Sovcloud Technologies Ltd; off-balance-sheet-SPV/funding watch, funding declined"}
  - {id: "FN-05", check: "F17", line: "Turn 30", classification: "AMBIGUOUS", implication: "India mix ~20-21% vs analyst recollection ~40% last quarter; India+intl+domestic does not sum; single-segment filing gives no geo to verify"}
  - {id: "FN-06", check: "F17", line: "Turn 34", classification: "AMBIGUOUS", implication: "3,900 (Q4 = GPU+storage) replotted on GPU-only trajectory beside 5,100; deck says 5,100 includes 1,024 B200, call says excludes; 1,024 same-vs-new lot unresolved"}
  - {id: "FN-07", check: "F17", line: "Turn 6", classification: "NEUTRAL-FACT", implication: "CFO spoken +1450 bps matches deck rounding; precise filing delta ~1444-1446 bps; call reads from deck not filing; immaterial"}
  - {id: "FN-08", check: "F6", line: "Turn 24", classification: "FORWARD-SIGNAL", implication: "July price hike intimated/rolled/pushed; beat is capacity+utilisation+leverage not price; customers moving 1mo->1-3yr contracts with advances = annuity build; margin durability read"}
  - {id: "FN-09", check: "F6", line: "Turn 26", classification: "AMBIGUOUS", implication: "Management assertion of min 6-yr GPU life / no major price compression; unverifiable; tension with D&A run-rate (~Rs242 Cr annualised on PPE Rs1,497 Cr); Role 5 tracking"}
  - {id: "FN-10", check: "F15", line: "Turn 36", classification: "NEUTRAL-FACT", implication: "L&T arm's-length mutual buyer/seller + JGTM, not a marquee contract; board link via L&T-Cloudfiniti director (deck p12); related-party watch, re-rates checklist item 4"}
forward_signals: ["FN-01", "FN-04", "FN-08"]
ambiguous: ["FN-05", "FN-06", "FN-09"]
commitments:
  - {commitment: "Next lot of B200 deployed", implied_date: "next couple of months", ref: "Turn 12/22", status_word: "expected"}
  - {commitment: "+1,024 B200 added on top of 5,100 live", implied_date: "soon", ref: "Turn 34", status_word: "expected"}
  - {commitment: "July price hike (CPU esp., some GPU)", implied_date: "rolled/pushed further out", ref: "Turn 24", status_word: "deferred"}
  - {commitment: "Loan rising from ~Rs450 Cr", implied_date: "near term", ref: "Turn 32", status_word: "underway"}
  - {commitment: "Capacity expansion into 'Varin' locale", implied_date: "undated", ref: "Turn 22", status_word: "initiated"}
  - {commitment: "Shift mix toward 2-3yr contracts", implied_date: "ongoing", ref: "Turn 28", status_word: "underway"}
  - {commitment: "SovCloud GPU build + funding arrangement", implied_date: "undated (very early days)", ref: "Turn 16/32", status_word: "initiated"}
  - {commitment: "Next-gen (B300/Vera Rubin) planning", implied_date: "planning underway", ref: "Turn 26", status_word: "initiated"}
gate_a3: pass
blank_checks: []
```
