# A3 FORENSIC NOTES — RSYSTEMS Q2 CY2026 — Doctype: PRESENTATION (investor deck)

Source extract: `/home/user/inflection-pipeline/runs/rsystems-q2cy26/work/extract_deck_rsystems_q2cy26.txt`
Ledger reconciled: `/home/user/inflection-pipeline/runs/rsystems-q2cy26/work/ledger_deck_rsystems_q2cy26.md`
Ledger rows read at cited line: 238/238 enumerated units (100%). Every KPI tile, chart series, table line item, and footnote in the A2 ledger was read verbatim at its line before judging.
Doctype note: management-authored marketing collateral for the 05-Aug-2026 analyst call (Reg. 30 filing, "Un-audited"). Balance-sheet / audit-report / entity-list checks that require a Reg. 33 statement are marked N.A. with a one-line reason. F16 (presentation reframing) and the F6/F8/F9/F10 numbers the deck carries are the live checks.

---

## FINDINGS TABLE

| id | check | ledger ref | slide / line | short verbatim quote | classification | forward implication |
|---|---|---|---|---|---|---|
| A3-01 | F16 | §4 tiles / §6 slide-14 | S5 L153; S14 L558 | tile: "Adj. Net Profit: INR 629M ($6.6M) … YoY 35.4%" vs table: "Net profit ^ … 555.7 … 758.5" | CONFIRMATORY-NEGATIVE | Deck headlines adjusted PAT +35.4% while REPORTED PAT fell 758.5->555.7 = -26.7% YoY (buried in appendix, never in a tile). Base-year Q2'25 reported was inflated by a Rs 409.3M land-sale gain (L552) stripped in "adjusted"; current adjusted is lifted by hedge-accounting (A3-03). The +35.4% is engineered on both ends. |
| A3-02 | F8 | §6 slide-14 | S14 L556-557 | "Income before income tax 805.1 … Tax expense 249.4" | FORWARD-SIGNAL | ETR 31.0% (Q2'26) vs 27.0% (Q1'26) vs 23.5% (Q2'25), all above 25.17% statutory; ~750bps YoY step-up. Rising ETR is a structural drag on future REPORTED PAT that the adjusted headline hides. No "earlier-year tax" line disclosed. |
| A3-03 | F9 | §7 fn slide-7/14 | S7 L237-239; S14 L563 | "other income for Q1 2026 was higher by ₹180.47 million, as changes in the fair value of designated hedging instruments were recognized in … (OCI)" | AMBIGUOUS | New Ind AS 109 cash-flow-hedge policy (effective 01-Jan-2026) moved ₹180.47M of FX fair-value into a Hedge Reserve and "Adj. Net Profit … further reflect" it — the adjusted definition CHANGED mid-comparison. Hedge reserve "will be reclassified to profit and loss … when the corresponding hedged transactions occur" (L564): future other-income timing item. Verify assumptions/reserve balance at Annual Report. |
| A3-04 | F16 | §5 EBITDA bridge | S5 L156-166; S6 L193-204 | "Rupee depreciation +98 … Standard operations -47" (Q2); "Rupee depreciation +552 … Standard operations +247" (H1) | FORWARD-SIGNAL | Management's own bridge shows QoQ Adj. EBITDA rose entirely on rupee depreciation (+98) while STANDARD OPERATIONS fell -47; H1 FX (+552) > operations (+247). Margin held at 20.1% via FX, not core delivery. If USD/INR reverts (monitoring #5), margin reverts. Implied rate 94.6 (Q2'26) vs 85.6 (Q2'25). |
| A3-05 | F16 | §5 ACV chart | S11 L436-450 | "84 / 82 … 68" axis; "82.3 … 82.9" | AMBIGUOUS | TTM ACV chart y-axis truncated at 68 (not 0), magnifying a 12% climb; but the data reveal deceleration: Q1'26 82.3 -> Q2'26 82.9 = +0.6 QoQ after +5.8 prior. Above the $82m stall line, well below the $88m target (monitoring #2). Approaching stall. |
| A3-06 | F15 | §5 fn slide-9 | S9 L312 (dup L390) | "# Basis Trailing Twelve months and excluding the new acquisition of Novigo" | FORWARD-SIGNAL | New acquired entity "Novigo" is named only to be CARVED OUT of the DSO/utilization ops metrics; its revenue and margin are nowhere disclosed. Headline revenue +30.2% therefore includes an undisclosed inorganic Novigo slug. Directly opens monitoring #3 (Novigo revenue >Rs 55 Cr/qtr) and organic-growth question (#1). |
| A3-07 | F16 | §6 slide-14 | S14 L554; S15 L589 | "Interest expense (94.8) … (21.4)" | FORWARD-SIGNAL | Interest expense +343% YoY (21.4->94.8; H1 36.3->190.7) signals acquisition/leverage funding (Novigo). Coverage still ~9.6x (EBIT 908.6/94.8) so monitoring #8 (>6x) holds, but the trajectory is the signal. Other income also swung negative to (8.7) as hedge gains left P&L (A3-03). |
| A3-08 | F10 | §4 tiles / §6 tables | S5 L158; S14 L547 | "Adj. EPS: INR 5.3"; table "Cost of RSUs 62.4" | AMBIGUOUS | Deck shows only Adj. BASIC EPS; no diluted EPS despite an active RSU plan (Cost of RSUs 62.4M/qtr). Implied share count ~118.6M (628.7/5.3) roughly flat YoY, but dilution from unvested RSUs is unquantified. Flag spread absence for A4. |
| A3-09 | F16 | §5 charts | S9 L281-296; S9 L298-310 | "Revenue by Geography (%) … Client Concentration (%)"; utilization/DSO charts axis-only | NEUTRAL-FACT | NEW disclosures vs filing: geography split (Americas 71.5%, +220bps QoQ, concentration rising), client concentration buckets (Top-10 24.4%). Utilization and DSO charts are axis-only (no data labels, L174/L181 of ledger) — a shape with no verifiable numbers, so monitoring #7 (debtor turnover) is NOT verifiable from the deck. |
| A3-10 | F6 | §8 key wins | S10 L402,409,420 | "will drive smarter decision-making"; "GCC will drive AI-powered lending innovation, modernize core platforms"; "will modernize customer acquisition" | NEUTRAL-FACT | Forward "will"-lexicon hits are aspirational deal-outcome language, not dated deliverables; logged in the commitment register at low weight. No numeric guidance anywhere (NOT FOUND, ledger §9). |
| A3-11 | F14 | §7 fn slide-14/15 | S14 L558,560,562; S15 L595 | "Net profit ^"; footnote "^ Adjusted Net Profit …"; "finding fees paid for Chief Revenue Officer" | NEUTRAL-FACT | Drafting: the "^" symbol tags the REPORTED "Net profit" row (555.7) yet its footnote states the ADJUSTED figure (628.7) — same marker, two different numbers, an ambiguity that eases the reported/adjusted conflation in A3-01. "finding fees" (x2) is a typo for "finder's fees." Cumulatively a minor governance-hygiene data point. |
| A3-12 | F17 | monitoring list | see silence table | (multiple) | AMBIGUOUS / FORWARD-SIGNAL | Presentation silence audit vs the 9-item Notion checklist — see "What The Deck Does / Does Not Answer" below. |

Reconciliation of the enumerator-flagged pair (task-directed): slide-14 footnote "^ Adjusted Net Profit … Rs. 628.7 M (US$ 6.6 M) for Q2 2026" (L562) vs slide-5 tile "Adj. Net Profit: INR 629M ($6.6M)" (L153) — CONSISTENT within rounding (628.7 -> 629). No discrepancy; the headline tile equals the footnote adjusted figure, confirming the deck's headline is the ADJUSTED, not the reported (555.7), number.

---

## WHAT THE DECK DOES / DOES NOT ANSWER (F17 presentation silence audit vs Notion monitoring checklist)

| # | Monitoring item | Deck status | Cite / value | Verdict |
|---|---|---|---|---|
| 1 | Organic CC revenue growth >5% (<3% STAGNANT) | SILENT (partial) | INR rev +30.2%, US$ rev +17.8% (54.0->63.6, L539); FX ~+10.5% and Novigo inorganic both embedded | AMBIGUOUS -> concall Q: organic constant-currency growth ex-Novigo, ex-FX? Headline heavily FX/inorganic-inflated. |
| 2 | TTM ACV bookings >$88m (<$82m stall) | ANSWERED | 82.9 (L440), QoQ +0.6, decelerating | FORWARD-SIGNAL: above stall, below target, momentum collapsing. |
| 3 | Novigo revenue >Rs 55 Cr/qtr | SILENT | named only to exclude it (L312) | AMBIGUOUS -> concall Q: Novigo quarterly revenue and margin uplift. |
| 4 | Adj. EBITDA margin >=18.5% (<17% reverts) | ANSWERED | 20.1% (L146) | PASS on metric, but FX-propped (A3-04). |
| 5 | USD/INR >89 | ANSWERED (implied) | implied avg 94.6 (6017.0/63.6, L539) | Above 89; primary EBITDA driver this quarter. |
| 6 | Fixed-price mix >18% | SILENT | not disclosed | AMBIGUOUS -> concall Q. |
| 7 | Debtor turnover >=1.45x (<1.4x break) | SILENT | DSO chart axis-only, no labels (L298-310) | AMBIGUOUS -> concall Q: DSO in days; chart shows shape only. |
| 8 | Interest coverage >6x | ANSWERED (derivable) | EBIT 908.6 / Int 94.8 = 9.6x (L553-554) | PASS, but interest +343% YoY (A3-07). |
| 9 | Annualised ROCE >20% | SILENT | no balance-sheet/capital-employed in deck | AMBIGUOUS -> concall Q. |

THESIS-BROKEN triggers vs deck: organic-revenue-negative (cannot assess, #1 silent); Novigo margin uplift >40bps miss (silent, #3); Blackstone exit <Rs 300 (no share price in deck); KMP fraud / audit qualification (none; deck is un-audited, no auditor report). None confirmed-broken from the deck; two (organic, Novigo margin) are un-checkable and must be forced on the call.

---

## CHECKLIST SCORECARD (all 17)

| Check | Status | One-line basis |
|---|---|---|
| F1 ZERO-VALUE STANDING ITEMS | N.A. | Ledger zero_standing = 0 (L280); every table line carries a value in every period. No standing-zero rows to interrogate. |
| F2 STANDALONE vs CONSOLIDATED | N.A. | Deck carries consolidated contribution analysis only; no standalone column to decompose. |
| F3 SHELL-ENTITY DETECTION | N.A. | No entity-level / standalone cost lines in a deck; cannot compare S-vs-C cost identity. |
| F4 UNAUDITED CONTRIBUTION RATIO | N.A. | No auditor "Other Matters"; whole deck is "Un-audited" (L536,571) with no component-auditor split. |
| F5 GOING CONCERN / EoM | N.A. | No audit report / EoM paragraph in a deck. |
| F6 FORWARD-COMMITMENT PHRASES | FINDING | A3-10: "will drive / will modernize" deal-outcome language (L402,409,420); aspirational, no dated deliverable, no numeric guidance. |
| F7 HEDGE PHRASES | PASS | Only boilerplate forward-looking disclaimer, "results … could differ" (L91-94); no newly-added risk/concentration hedge in the notes. |
| F8 TAX FORENSICS | FINDING | A3-02: ETR 31.0% > 27.0% > 23.5% (Q2'26/Q1'26/Q2'25), rising above 25.17% statutory. |
| F9 OCI FORENSICS | FINDING | A3-03: new Ind AS 109 hedge policy shifted ₹180.47M FX into OCI/Hedge Reserve; adjusted PAT redefined mid-comparison (L237-239, L563). |
| F10 SHARE COUNT / DILUTION | FINDING | A3-08: only Adj. Basic EPS shown, no diluted EPS despite Cost of RSUs 62.4M (L158, L547). |
| F11 RESERVES / NET WORTH | N.A. | No balance-sheet, paid-up capital or other-equity figures in the deck to tie out. |
| F12 SEGMENT FORENSICS | N.A. | No segment assets/liabilities; geography % is a revenue split only (logged as NEW disclosure under A3-09). |
| F13 BOARD OUTCOME | N.A. | No board/AGM/director-appointment items in the deck. |
| F14 NOTE DRAFTING INCONSISTENCIES | FINDING | A3-11: "^" marks reported "Net profit" row yet footnote states adjusted figure; "finding fees" typo x2 (L558,560,562,595). |
| F15 ENTITY LIST DIFFS | FINDING | A3-06: new acquisition "Novigo" named only to be excluded from ops metrics (L312); no prior ledger, but the entity is new and revenue undisclosed. |
| F16 DROPPED / REFRAMED DISCLOSURES | FINDING | A3-01/04/05/07/09: leads with adjusted, buries reported PAT -26.7%; FX-driven EBITDA bridge; truncated ACV axis (base 68); axis-only utilization/DSO; new geography/concentration splits. |
| F17 SILENCE AUDIT | FINDING | A3-12: 5 of 9 monitoring items silent or unverifiable (organic CC, Novigo rev, fixed-price mix, debtor turnover, ROCE). |

GATE A3: PASS — all 17 checks carry an explicit status; every FINDING cites a slide/line and a verbatim quote.

---

## COMMITMENT REGISTER (from F6)

| commitment | implied date | slide / line | status word |
|---|---|---|---|
| Telecom/media client engagement "will drive smarter decision-making, optimize operations" | none (aspirational) | S10 L402 | initiated |
| U.S. small-business-lender GCC "will drive AI-powered lending innovation, modernize core platforms" | none | S10 L409 | initiated |
| Financial-services client "R Systems will modernize customer acquisition, engagement, onboarding" (Dynamics 365) | none | S10 L420 | initiated |
| "Agentic Business Operations seeing traction" | ongoing | S12 L498 | underway |
| "Modernization continues to be big theme" / "TRENDS SHAPING 2026 continues…" | CY2026 | S12 L499,503 | underway |

No dated, quantified management commitment (project completion date, revenue/margin target) exists in the deck — numeric guidance is NOT FOUND (ledger §9, L335).

---

```yaml
stage: A3-forensics
company: "RSYSTEMS"
quarter: "Q2 CY2026"
doctype: "presentation"
model: claude-opus-4-8
status: complete
forensics_path: "/home/user/inflection-pipeline/runs/rsystems-q2cy26/work/forensics_deck_rsystems_q2cy26.md"
ledger_reconciled_pct: 100
checklist:
  F1: N.A.
  F2: N.A.
  F3: N.A.
  F4: N.A.
  F5: N.A.
  F6: FINDING
  F7: PASS
  F8: FINDING
  F9: FINDING
  F10: FINDING
  F11: N.A.
  F12: N.A.
  F13: N.A.
  F14: FINDING
  F15: FINDING
  F16: FINDING
  F17: FINDING
findings:
  - {id: "A3-01", check: "F16", line: "S5 L153 / S14 L558", classification: "CONFIRMATORY-NEGATIVE", implication: "Headlines adjusted PAT +35.4% while reported PAT -26.7% YoY sits only in the appendix; growth engineered via prior-year one-off removal + current hedge adjustment"}
  - {id: "A3-02", check: "F8", line: "S14 L556-557", classification: "FORWARD-SIGNAL", implication: "ETR 23.5%->27.0%->31.0%, rising above 25.17% statutory; structural drag on future reported PAT"}
  - {id: "A3-03", check: "F9", line: "S7 L237-239 / S14 L563", classification: "AMBIGUOUS", implication: "New Ind AS 109 hedge policy moved 180.47M FX to OCI and redefined adjusted PAT mid-comparison; hedge reserve reclassifies to P&L later"}
  - {id: "A3-04", check: "F16", line: "S5 L156-166 / S6 L193-204", classification: "FORWARD-SIGNAL", implication: "EBITDA bridge shows QoQ growth is entirely rupee depreciation (+98) with standard operations -47; margin FX-propped, reverts if USD/INR falls"}
  - {id: "A3-05", check: "F16", line: "S11 L436-450", classification: "AMBIGUOUS", implication: "TTM ACV chart axis truncated at 68; data show deceleration to +0.6 QoQ (82.3->82.9), nearing the $82m stall, far below $88m target"}
  - {id: "A3-06", check: "F15", line: "S9 L312", classification: "FORWARD-SIGNAL", implication: "New acquisition Novigo named only to be excluded from ops metrics; its revenue/margin undisclosed, inflating headline +30.2% inorganically"}
  - {id: "A3-07", check: "F16", line: "S14 L554 / S15 L589", classification: "FORWARD-SIGNAL", implication: "Interest expense +343% YoY (21.4->94.8) signals acquisition leverage; other income swung negative as hedge gains left P&L"}
  - {id: "A3-08", check: "F10", line: "S5 L158 / S14 L547", classification: "AMBIGUOUS", implication: "Only Adj. Basic EPS shown, no diluted EPS despite active RSU plan (Cost of RSUs 62.4M); dilution unquantified"}
  - {id: "A3-09", check: "F16", line: "S9 L281-310", classification: "NEUTRAL-FACT", implication: "New geography/concentration splits disclosed; utilization & DSO charts axis-only, so debtor-turnover monitoring item not verifiable"}
  - {id: "A3-10", check: "F6", line: "S10 L402,409,420", classification: "NEUTRAL-FACT", implication: "Aspirational 'will drive/modernize' deal language, no dated deliverable or numeric guidance"}
  - {id: "A3-11", check: "F14", line: "S14 L558,560,562", classification: "NEUTRAL-FACT", implication: "'^' marks reported Net profit row yet footnote gives adjusted figure; 'finding fees' typo x2; eases reported/adjusted conflation"}
  - {id: "A3-12", check: "F17", line: "monitoring checklist §", classification: "AMBIGUOUS", implication: "5 of 9 monitoring items silent/unverifiable in deck: organic CC growth, Novigo revenue, fixed-price mix, debtor turnover, ROCE"}
forward_signals: ["A3-02", "A3-04", "A3-06", "A3-07"]
ambiguous: ["A3-03", "A3-05", "A3-08", "A3-12"]
commitments:
  - {commitment: "Telecom/media analytics engagement 'will drive smarter decision-making'", implied_date: "none", ref: "S10 L402", status_word: "initiated"}
  - {commitment: "U.S. lender GCC 'will drive AI-powered lending innovation, modernize core platforms'", implied_date: "none", ref: "S10 L409", status_word: "initiated"}
  - {commitment: "Financial-services client 'will modernize customer acquisition' via Dynamics 365", implied_date: "none", ref: "S10 L420", status_word: "initiated"}
  - {commitment: "'Agentic Business Operations seeing traction'", implied_date: "ongoing", ref: "S12 L498", status_word: "underway"}
  - {commitment: "'Modernization continues to be big theme' / 'TRENDS SHAPING 2026 continues'", implied_date: "CY2026", ref: "S12 L499,503", status_word: "underway"}
gate_a3: pass
blank_checks: []
```
