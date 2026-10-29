# A3 FORENSIC NOTES: CORRECTION LOOP 1 ADDENDUM (presentation + concall), UNIMECH Q2 FY27

Company: Unimech Aerospace and Manufacturing Limited (UNIMECH). Quarter: q2fy27.
Model: claude-opus-5-5. Loop: 1. Scope: two A5 audit items only (C1, M2 in runs/unimech-q2fy27/work/audit_unimech_q2fy27.md l.177-178).
The base forensics files stay as written. This addendum adds two findings: D-A3-28 (presentation) and C-A3-26 (concall).
Inputs read: deck, results and concall fulltext and structured extracts; A2 ledgers (presentation, concall); the monitoring checklist. Nothing under inputs/ was opened.

Abbreviations: deck = unimech-presentation-q2fy27-fulltext.md; res = unimech-results-q2fy27-fulltext.md; call = unimech-concall-q2fy27-fulltext.md; checklist = work/monitoring_checklist_unimech.md.

## 1. Ledger rows read for this loop (verbatim at cited line)

| Doc | Row | Line | Verbatim at line | A2 ledger entry |
|---|---|---|---|---|
| deck | R222 | l.369 (p14) | "Joint Investment in JV : ~USD 30 Mn" | slide 14 group R222-R228 (ledger_presentation l.33) |
| deck | R223 / R224 | l.373-374 | "Unimech (51%) :" / "Kanoo Group (49%)" | same group |
| deck | R225 / R226 / R664 | l.396 | "First tranche of capital infusion of SAR 15.3 Mn by Unimech and SAR 14.7 Mn by YBAK completed" | same group (R664 QUALIFIER) |
| deck | (p6, no new row) | l.130-132 | "Completed the first equity tranche for the Kanoo– Unimech JV, of ~USD 4mn" | p6 group |
| deck | (p19) | l.529-532 | "Infused SAR 15.3 Mn (51%) and SAR 14.7 Mn (49%) ... completing the SAR 30 Mn first equity tranche in their Saudi JV" | p19 group |
| deck | R253 | l.576 (also l.563-564) | "~65% Capacity Utilization" | p20 group |
| res | (note 7 SA) | l.341 | "on October 01, 2026, the Company made an Overseas Direct Investment (ODI) ... amounting to INR 3,935.72 lakhs, towards equity investment for a 51% stake" | results ledger, SA notes |
| res | (note 8 CO) | l.717 | same text, consolidated notes | results ledger, CO notes |
| res | CO BS | l.527, l.529-530, l.545, l.551 | investments 18,084.80; cash 4,553.66; other bank 5.08; borrowings 3,028.51 (NC) and 13,069.95 (C), Rs lakh | results ledger, CO BS |
| call | R011 | l.97 | "Our initial equity investment of approximately USD $4 billion deployed at least this month" | ASR; R011 flagged mishearing candidate |
| call | R143 | l.98 | "fully capitalizes this space, funding the infrastructure, readiness" | ASR |
| call | R022 | l.227 | "Following our initial USD 4 million equity investment" | ASR |
| call | R085 / R184 | l.574-575 (T31, UNIDENTIFIED mgmt) | "we are putting up a capex for the Saudi JV ... roughly a 200 to 250 crore of outlay" | ASR |
| call | R245 | l.366-369 (T05, CFO) | "expect to consider an equity fund raise in early calendar year ... subject to final requirement and market conditions" | qualifier |
| call | R064 | l.352 (T05, CFO) | "operating at approximately 65% utilization, which" | mgmt_number (ledger_concall l.199) |
| call | R065 | l.353 (T05, CFO) | "includes about 50% to 20% of our available capacity." | MISHEARING_CANDIDATE (ledger_concall l.200) |
| call | R244 | l.352-356 (T05, CFO) | qualifier, full quote in C-A3-26 detail | qualifier (ledger_concall l.374) |
| call | (T30 / T31) | l.558-559; l.564-567 | "70% blended level utilization by the end of FY27" (analyst); "And we have still some capacity." (mgmt) | turn ledger l.65-66 |

Rows in loop scope: 16 structured IDs (deck R222, R223, R224, R225, R226, R253, R664; call R011, R022, R064, R065, R085, R143, R184, R244, R245), plus the results notes and BS lines above. All read at their lines. Reconciled 100% of loop scope.

## 2. FINDINGS TABLE

| id | check | ledger row ref | line | short verbatim quote | classification | forward implication |
|---|---|---|---|---|---|---|
| D-A3-28 | F6 (presentation) | R222, R223-R226, R664; res notes 7/8; call R011, R022, R085, R245 | deck l.369; l.396; l.130-132; res l.341, l.717; call l.97-98, l.227, l.574-575 | "Joint Investment in JV : ~USD 30 Mn" | FORWARD-SIGNAL | Unimech's 51% of the joint figure leaves about Rs 108.2 Cr still to fund after the first tranche (my arithmetic). That exceeds Sep-26 net cash of Rs 65.45 Cr. A second-tranche cash call is coming, with the equity/debt split and the date unstated. |
| C-A3-26 | F17 (concall; checklist item 4) | R064, R065, R244; deck R253 | call l.351-356; deck l.563-564, l.576; checklist l.118 | "includes about 50% to 20% of our available capacity." | AMBIGUOUS | The ~65% includes NPI, prototype and qualification work. On every plausible reading of the garbled band, serial-production utilisation is 45-55% [INFERENCE], under the "<60%" red line. The red line cannot be tested on a serial basis from filed evidence. |

### D-A3-28 detail

**What the filed figure is.** Deck p14 (R222, l.369) states "Joint Investment in JV : ~USD 30 Mn". The deck does not call it equity, does not split equity from debt, and gives no date or tranche schedule. The same slide shows the 51:49 split (l.373-374) and the completed first tranche: "SAR 15.3 Mn by Unimech and SAR 14.7 Mn by YBAK" (l.396). Deck p6 calls that tranche "the first equity tranche ... of ~USD 4mn" (l.130-132). Deck p19 calls it "the SAR 30 Mn first equity tranche" (l.531-532). The results filing confirms the Unimech leg in rupees: "INR 3,935.72 lakhs, towards equity investment for a 51% stake in the overseas subsidiary" on 01-Oct-2026 (res l.341 SA note 7; l.717 CO note 8).

**FX rate used.** Rs 25.724 per SAR, implied by the filing: Rs 3,935.72 lakh / SAR 15.3 Mn (res l.341; deck l.396) [my arithmetic]. Rs 96.46 per USD = Rs 25.724 x 3.75 SAR per USD. The 3.75 is the Saudi riyal's fixed USD peg. No extract states it: it is an EXTERNAL reference, not filed. Cross-check from filed text: the deck pairs SAR 15.3 Mn with "~USD 4mn" (l.130-132; call l.227 "USD 4 million"). That implies about 3.83 SAR per USD, or about Rs 98.4 per USD, consistent within the "~" rounding [my arithmetic]. Sensitivity at Rs 98.4 is shown where it matters.

**Arithmetic (all "my arithmetic").**

| Item | Value | Basis |
|---|---|---|
| Joint investment in rupees | Rs 289.4 Cr (Rs 295.2 Cr at Rs 98.4/USD) | USD 30 Mn x 96.46 |
| Joint investment in SAR | SAR 112.5 Mn | USD 30 Mn x 3.75 |
| First tranche as share of joint | 26.7% | SAR 30 Mn / SAR 112.5 Mn (deck l.396, l.531) |
| Call capex in USD | USD 20.7-25.9 Mn | Rs 200-250 Cr / 96.46 (call l.574-575) |
| Capex as share of joint investment | 69-86% | USD 20.7-25.9 Mn / USD 30 Mn |
| Joint investment above capex | Rs 39.4-89.4 Cr | 289.4 - 250 / 289.4 - 200 |
| Unimech 51% of joint | USD 15.3 Mn = Rs 147.6 Cr | 0.51 x USD 30 Mn |
| Unimech paid, first tranche | Rs 39.36 Cr (USD 4.08 Mn) | res l.341 |
| **Unimech remaining, Reading A** | **Rs 108.2 Cr (USD 11.22 Mn)** | 147.6 - 39.36 |
| Unimech remaining, Reading B (51% of call capex only) | Rs 62.6-88.1 Cr | 0.51 x 200-250 - 39.36 |
| Unimech remaining on A4's SAR 60M figure | Rs 39.4 Cr | 0.51 x SAR 60 Mn x 25.724 - 39.36; SAR 60M has NO anchor in any extract (Notion memory only), so this reading is not filed evidence |
| Kanoo first tranche in rupees | Rs 37.81 Cr | SAR 14.7 Mn x 25.724 |
| Sep-26 consolidated net cash (leases excluded) | Rs 65.45 Cr | (18,084.80 + 4,553.66 + 5.08) - (3,028.51 + 13,069.95) = 6,545.08 lakh (res l.527, l.529-530, l.545, l.551) |
| Net cash after the 01-Oct ODI, parent funding view | Rs 26.09 Cr | 65.45 - 39.36; before Q3 CFO and any other flow |
| Reading A remaining vs Sep-26 net cash | exceeds by Rs 42.8 Cr (1.65x) | 108.2 vs 65.45 |
| Reading A remaining vs post-ODI net cash | exceeds by Rs 82.1 Cr | 108.2 vs 26.09 |

Consolidation note. The JV is a 51% subsidiary (res l.341). In the consolidated balance sheet, the ODI moves cash into the subsidiary and Kanoo's Rs 37.81 Cr enters group cash with a matching NCI. The parent funding view (Rs 26.09 Cr) measures Unimech's own capacity to meet its next tranche. Group cash leaves only when the JV spends on capex.

**Relation to the call's Rs 200-250 Cr capex.** The call figure is "outlay", not funding source (call l.574-575). At Rs 96.46/USD, the filed joint investment (Rs 289.4 Cr) covers the capex with Rs 39-89 Cr left over, plausibly working capital and start-up cost [INFERENCE]. So the base files' "funding gap of about Rs 46-96 Cr" leg (concall C-A3-12, "Rs 200-250 Cr outlay exceeds ~Rs 154 Cr planned equity", forensics_concall l.228) rests on SAR 60M, which no extract carries. D-A3-28 replaces that leg. The funding question moves from the JV to Unimech's own balance sheet.

**Two readings and the separating observation.**
- Reading A (bear-leaning): USD 30 Mn is total joint equity, paid 51:49. Unimech owes about Rs 108.2 Cr more, 1.65x its Sep-26 net cash. The parent needs debt or the equity raise "subject to final requirement and market conditions" (call l.366-369).
- Reading B: USD 30 Mn is total project funding, part at JV-level debt. Unimech's further equity is lower (Rs 62.6-88.1 Cr if it funds 51% of capex in equity, less if the JV borrows). A parent guarantee on JV debt may then sit off the parent balance sheet.
- Separating observation: the amount and date of the second-tranche ODI, or JV-level borrowings, NCI and any guarantee note in the Q3 FY27 consolidated filing.
- Drafting point: the call says the first tranche "fully capitalizes this space" (l.98, ASR; "space" is probably "phase" [INFERENCE]). The deck calls it the "first tranche" (l.396), 26.7% of the joint figure. Read on conservative bias: more tranches follow. Low weight: the joint figure "~USD 30 Mn" and the first tranche "SAR 30 Mn" (l.531) share the number 30. A currency mislabel cannot be excluded from the extract alone, but "first tranche" on two slides argues against it.

**For A4 (management question).** "Is the ~USD 30 Mn joint investment all equity at 51:49? What are the amount and date of Unimech's next tranche? How will Unimech fund about Rs 108 Cr against Rs 65 Cr net cash at Sep-26? Will the parent guarantee any JV debt?"

### C-A3-26 detail

**Verbatim (call l.351-356, T05, CFO Ram Krishna Kamosala; ASR, management tier, UNVERIFIED):**
> [00:22:40] Our manufacturing presidents are currently
> [00:22:42] operating at approximately 65% utilization, which
> [00:22:45] includes about 50% to 20% of our available capacity.
> [00:22:48] He is dedicated to new production reduction,
> [00:22:51] provost, and customer qualification orders
> [00:22:53] to secure future production volumes.

ASR repair candidates, all [INFERENCE]: "presidents" = "facilities"; "50% to 20%" = "15% to 20%" (a descending "50 to 20" range is not coherent; R065 is ledgered MISHEARING_CANDIDATE); "new production reduction" = "new product introduction" (NPI); "provost" = "prototype". The deck carries "~65% Capacity Utilization" with no qualifier and no denominator (deck l.563-564; l.576, R253).

**Serial-production utilisation, INFERENCE only (my arithmetic):**

| Reading of the garbled band | Serial-production utilisation |
|---|---|
| 15-20 percentage points of AVAILABLE capacity (the call says "of our available capacity") | 65 - 20 to 65 - 15 = 45-50% |
| 15-20% of USED capacity | 65 x 0.80 to 65 x 0.85 = 52.0-55.3% |
| 5-20 points of available capacity (other ASR reading) | 45-60% |

Every reading lands at or below 60%. The text's own wording ("of our available capacity") favours the 45-50% reading.

**Can the Notion threshold be tested on this basis?** No. Checklist item 4 (l.118): Green ">70% by mid-FY27", Red "<60% through FY27".
- Headline basis: 65% at Sep-26 (mid-FY27) misses green and clears red. The status is AMBER. The red line is a full-year test, so one quarter cannot fire it either way.
- Serial basis: untestable on filed evidence. The qualifier's number is ASR-garbled and unverified. The deck gives no qualifier. The checklist does not define its basis. On the plausible readings the serial figure sits under the red line [INFERENCE]. Lean bear: carry item 4 as AMBER with a flag "serial basis below 60% unconfirmed", not as clean AMBER.
- Comparability: the Q1 baseline "utilisation about 58%" (checklist l.351, Notion) has no stated basis. The 58% to 65% rise (base finding C-A3-25) may include growth in NPI and qualification work, not serial load. Note the analyst's "70% blended level utilization" (call l.558-559) and management's "we have still some capacity" (l.567).
- This corrects the base concall file, which lists utilisation as "Addressed on the call (removed from silence)" (forensics_concall l.176). It was addressed, with a qualifier that leaves the threshold untestable.

**For A4 (management question).** "What share of capacity runs NPI, prototype and qualification work: 15-20%? Is that share of available or of used capacity? What is serial-production utilisation? Was Q1's ~58% on the same basis?"

## 3. CHECKLIST SCORECARD (loop delta only)

The base checklists stand as filed. forensics_presentation_unimech_q2fy27.md and forensics_concall_unimech_q2fy27.md each carry all 17 checks, gate_a3 pass. This loop changes no status.

| Check | Doc | Status | Basis |
|---|---|---|---|
| F6 | presentation | FINDING (unchanged; adds D-A3-28) | "~USD 30 Mn" joint investment with first tranche completed (l.369, l.396) |
| F17 | concall | FINDING (unchanged; adds C-A3-26) | Checklist item 4 addressed with a qualifier that makes the red line untestable on a serial basis (l.351-356) |
| F1-F5, F7-F16 (both docs); F6 (concall); F17 (presentation) | both | unchanged from base files | not in loop scope |

## 4. COMMITMENT REGISTER (loop additions)

| Commitment | Implied date | Ref | Status word |
|---|---|---|---|
| Kanoo-Unimech JV joint investment ~USD 30 Mn, 51:49; further tranches after the first | undated (production readiness "March or April 27", call l.229) | deck l.369, l.396; res l.341 | initiated (first tranche completed 01-Oct-2026) |
| Saudi JV capex "roughly a 200 to 250 crore of outlay" | undated | call l.574-575 | initiated |
| Equity fund raise "in early calendar year ... subject to final requirement and market conditions" | early CY2027 (hedged) | call l.366-369 | initiated (evaluating) |

## 5. YAML BLOCK

```yaml
stage: A3-forensics
company: "UNIMECH"
quarter: "q2fy27"
doctype: "presentation+concall (loop 1 addendum)"
model: "claude-opus-5-5"
status: complete
loop: 1
forensics_path: "runs/unimech-q2fy27/work/forensics_loop1_addendum_unimech_q2fy27.md"
ledger_reconciled_pct: 100        # loop scope: deck R222-R226, R253, R664; call R011, R022, R064, R065, R085, R143, R184, R244, R245; res l.341, l.717, CO BS lines
checklist:                        # loop delta; all other checks unchanged in base files (both gate_a3 pass)
  presentation_F6: FINDING        # adds D-A3-28
  concall_F17: FINDING            # adds C-A3-26
findings:
  - {id: "D-A3-28", check: "F6", line: "deck 369; 396; 130-132; res 341; 717; call 97-98; 574-575", classification: "FORWARD-SIGNAL", implication: "Filed '~USD 30 Mn' joint investment = Rs 289.4 Cr at Rs 96.46/USD (my arithmetic), above Rs 200-250 Cr call capex; Unimech 51% leaves ~Rs 108.2 Cr to fund after the Rs 39.36 Cr first tranche (Rs 62.6-88.1 Cr if only 51% of capex), vs Sep-26 net cash Rs 65.45 Cr (Rs 26.09 Cr after ODI); equity/debt split and tranche date unstated; supersedes SAR 60M funding-gap leg of C-A3-12"}
  - {id: "C-A3-26", check: "F17", line: "call 351-356; deck 563-564; 576; checklist 118", classification: "AMBIGUOUS", implication: "~65% utilisation includes NPI/prototype/qualification capacity ('about 50% to 20%', ASR-garbled); serial-production utilisation ~45-50% (of available) or ~52-55% (of used) [INFERENCE], under the <60% red line; red line untestable on serial basis from filed evidence; item 4 AMBER with flag; Q1 58% basis unknown"}
forward_signals: ["D-A3-28"]
ambiguous: ["C-A3-26"]
commitments:
  - {commitment: "Kanoo-Unimech JV joint investment ~USD 30 Mn at 51:49; further tranches", implied_date: "undated; readiness Mar/Apr-2027", ref: "deck l.369, l.396; res l.341", status_word: "initiated"}
  - {commitment: "Saudi JV capex Rs 200-250 Cr outlay", implied_date: "undated", ref: "call l.574-575", status_word: "initiated"}
  - {commitment: "Equity fund raise early CY2027, subject to requirement and market conditions", implied_date: "early CY2027", ref: "call l.366-369", status_word: "initiated"}
gate_a3: pass
blank_checks: []
analyst_note: "FX: Rs 25.724/SAR is implied by the filed ODI (res l.341 / deck l.396). The USD rate uses the 3.75 SAR/USD peg, which is EXTERNAL and in no extract; the deck's own '~USD 4mn' pairing implies about Rs 98.4/USD, within rounding. D-A3-28 moves the Saudi funding question from the JV to the parent. The JV's filed joint investment covers the call capex. Unimech's own remaining 51% share does not fit inside its Sep-26 net cash on Reading A. The A4 flag on SAR 60M has no filed anchor and should be restated. C-A3-26: the deck states 65% with no qualifier and the call qualifies it with a garbled band. Every plausible repair puts serial load at or under 60%. Carry checklist item 4 as AMBER with a flag; do not call it tested. Ask for the basis of the Q1 58% figure before reading the QoQ rise as serial demand."
```
