# A3 FORENSIC NOTES — Tejas Networks (TEJASNET) — Q1 FY27 — Doctype: RESULTS

Source extract: `extract_results_tejasnet_q1fy27.txt` (486 lines, 8 pages, pages 2-8 OCR'd)
Ledger: `ledger_results_tejasnet_q1fy27.md`
Prior extract: none (first pipeline run) — diffs use thesis-memory baselines, labelled as such, never treated as a prior extract.

## RECONCILIATION STATEMENT
100% of A2 ledger rows read at their cited lines before judging.
Ledger sections read verbatim: Count Test (l.6-15); Reconciliation notes (l.18-25); Notes standalone 6 rows (l.33-38); Notes consolidated 8 rows (l.44-51); Standalone P&L 36 rows (l.60-95); Consolidated P&L 37 rows (l.101-137); Consolidated Note-4 summary 3 rows (l.144-146); Board Outcome 2 rows (l.152-153); Standalone auditor 4 paras (l.160-164); Consolidated auditor 6+1 paras (l.171-178); Entity list 4 rows (l.186-189); Signature blocks 5 rows (l.199-203); Flags roll-up (l.207-212). Line-item categories reconcile: 76 line_items, 14 notes, 5 zero_standing, 1 agenda_item, 11 auditor_paras, 4 entities, 5 signature_blocks — all matched to the extract at their cited lines.

---

## FINDINGS TABLE

| id | check | ledger row ref | line | verbatim quote | classification | forward implication |
|---|---|---|---|---|---|---|
| A3-F2 | F2 | Std row 17 / Cons row 17 (PBT); Std row 11/15 vs Cons row 11/15 | 169 & 375; 163/167 & 369/373 | "Profit/(Loss) before tax (III - IV) (270.81)" [standalone l.169] and "(270.81)" [consolidated l.375] | AMBIGUOUS | Subsidiary net PBT contribution collapsed from +7.12 cr (Q4 FY26) to exactly 0.00 cr this quarter, making consolidated PBT identical to standalone to the paisa, while gross components diverge (employee benefit +4.18: 101.06 vs 105.24; other expenses -4.01: 136.03 vs 132.02). Magnitude is below the 5pp mechanical threshold but the exact identity plus the Q4→Q1 contribution collapse warrant a management question on what drove Q4 FY26 subsidiary profit and its disappearance. |
| A3-F3 | F3 | Std vs Cons cost lines rows 8,13,14 vs auditor para 6 | 165 & 371 (dep); 166 & 372 (ECL); 325-328 | "Depreciation and amortization expense 94.35" [std l.165] = "94.35" [cons l.371]; "total revenue of Rs. 0.86 crores, total net loss after tax of Rs. 0.00 crores" [l.326-327] | NEUTRAL-FACT | Consolidated depreciation identical to standalone to the paisa (94.35=94.35), identical ECL (8.08), identical inventory changes/purchases → the 3 subsidiaries carry no depreciable asset base and no independent provisioning. With aggregate Rs 0.86 cr revenue and Rs 0.00 cr net loss they are operationally near-dormant captive/service entities (incl. Saankhya Labs, the chip-IP acquisition) — consistent with IP/assets sitting in the parent (thesis-memory intangibles-under-development Rs 950 cr). |
| A3-F8 | F8 | Std/Cons row 20 (Deferred tax) & row 19 (Current tax) | 172 & 378; 171 & 377 | "Deferred tax expense/(benefit) (68.57)" [l.172]; "Current tax expense/(benefit) - " [l.171] | FORWARD-SIGNAL | Entire Rs 68.57 cr tax line is a deferred-tax benefit; standalone current tax is zero every period. ETR 25.32% (68.57/270.81) sits at statutory 25.17%, i.e. full DTA recognised on the quarter's loss. This adds ~Rs 68.57 cr to a DTA already flagged as Rs 365 cr = 52% of equity (FY26 KAM, thesis-memory). A growing DTA on an entity with no taxable profits carries reversal/impairment risk = future equity write-down. If DTA recognition halts, the reported quarterly loss widens by ~25%. ETR trend fell from 34.79% (Q1 FY26) toward statutory — the tax-benefit cushion is normalising down. |
| A3-F9 | F9 | Std row 28 / Cons row 28 (cash flow hedges) | 181 & 387 | "Gains/(losses) in cash flow hedges (7.72)" [l.181] | FORWARD-SIGNAL | Cash-flow-hedge OCI swung from +6.78 (Q4 FY26) to (7.72) this quarter, a QoQ swing of 14.50 that exceeds the entire FY26 movement of +11.81. Outstanding hedges are now underwater and will reclassify to P&L (cost of materials / revenue) as the hedged forecast transactions occur → future margin pressure and earnings volatility. Secondary: consolidated remeasurement-OCI (recorded 1.68, l.383) diverges from standalone (1.08, l.177) for the first time (prior periods identical), and consolidated TCI (208.94) ties better if that value is ~1.05 — an OCR/drafting ambiguity to verify at the Annual Report. |
| A3-F13 | F13 | Board Outcome row 2 (meeting timing) | 35 | "The Meeting started at 1.30 P.M. (IST) and ended at 4:40 P.M. (IST)" | AMBIGUOUS | The board met 3h10m to approve a single disclosed agenda item (results only; no AR/AGM/dividend/director/capital-raising resolution anywhere in this filing, l.29-33). Long duration for one item invites a question on undisclosed deliberations, especially given management reintroduced QIP/dilution optionality at AGM-26 (thesis-memory) and a separate same-day Reg 30 filing designated COO Preetham Uthaiah as SMP effective 2026-07-27 (out of scope here, flagged for A4 to reconcile, not analysed in this doc). |
| A3-F14 | F14 | Entity list rows 2 & 4 | 312/426; 314/429 | "Tejas Communications Pte. Limited" [auditor l.312] vs "Tejas Communication Pte. Limited" [Note 1 l.426]; "Saankhya Labs Inc" [l.314] vs "Saankhya Labs Inc." [l.429] | NEUTRAL-FACT | Entity names inconsistent within the same filing (auditor entity list vs consolidated Note 1): "Communications"/"Communication" (missing "s") and "Inc"/"Inc." punctuation. Individually immaterial, cumulatively a drafting/governance-control data point. Note text and auditor letter are otherwise consistent (both describe a limited review of "Unaudited" results — no audit/review mislabel). |

---

## CHECKLIST SCORECARD (all 17)

| Check | Status | Basis (one line) |
|---|---|---|
| F1 ZERO-VALUE STANDING | PASS | 5 ZERO_STANDING rows are explained by a loss-making entity: standalone current tax nil (l.171) and tax-on-OCI nil (l.179, l.182) anticipate a future current-tax charge once carryforward losses exhaust; consolidated tax-on-OCI nil (l.385, l.389). Structural, not anomalous; the zero-current-tax / deferred-benefit dynamic is carried to F8. |
| F2 STANDALONE vs CONSOLIDATED | FINDING | A3-F2: subsidiary PBT contribution collapsed +7.12→0.00, identical S/C PBT to the paisa; below 5pp threshold but flagged with a question. |
| F3 SHELL-ENTITY DETECTION | FINDING | A3-F3: identical depreciation/ECL/inventory lines + Rs 0.86 cr revenue / Rs 0.00 cr net loss → 3 subsidiaries operationally near-dormant. No Going Concern EoM anywhere to reconcile against. |
| F4 UNAUDITED CONTRIBUTION | PASS | Other Matters (l.325-328): unreviewed subs = revenue Rs 0.86 cr (0.21% of cons revenue 402.16), net loss after tax Rs 0.00 cr (~0% of cons PAT -202.24), TCI Rs 0.03 cr. All 3 subs management-furnished but immaterial; below 10% threshold; historically 3 subs, no YoY jump. |
| F5 GOING CONCERN / EoM | PASS | Both review reports UNMODIFIED (l.101-107, l.316-323). No Going Concern, no Emphasis of Matter; only an Other Matters para (unreviewed subs, non-GC). No prior extract to verbatim-diff; KAMs absent as expected in a limited review (vs FY26 audit's 2 KAMs). |
| F6 FORWARD-COMMITMENT PHRASES | PASS | Notes-section sweep (l.211-226, l.418-472) found no dateable forward commitments. Only past-tense governance ("approved by the Board of Directors", l.226/472) and a provision basis ("anticipated warranty claims", l.222/465), neither a qualifying commitment. Commitment register empty. |
| F7 HEDGE PHRASES | PASS | No pre-emptive risk hedges in notes. Only procedural "to the extent applicable" (l.292) and "subjected to limited review" (l.224/468). No newly-added hedge on revenue lumpiness or customer concentration. |
| F8 TAX FORENSICS | FINDING | A3-F8: 100% deferred-tax benefit, zero current tax, ETR ~25.3% at statutory; growing DTA (already 52% of equity KAM) = reversal/impairment risk. No "earlier-years" tax adjustment line present. |
| F9 OCI FORENSICS | FINDING | A3-F9: cash-flow-hedge QoQ swing 14.50 exceeds full FY26 movement 11.81; underwater hedges to reclassify to P&L; plus a first-time S/C remeasurement-OCI divergence to verify. |
| F10 SHARE COUNT / DILUTION | PASS | Equity capital 181.01→181.25 (l.184/391) = +Rs 0.24 cr, routine ESOP allotment (~0.13% of capital). Basic = diluted EPS every period (potential shares anti-dilutive in a loss). No QIP/dilution resolution in this filing (thesis-memory optionality only). |
| F11 RESERVES / NET WORTH | PASS | FY26-audited net worth: standalone 2,750.70+181.01=2,931.71; consolidated 2,749.86+181.01=2,930.87; gap 0.84 cr (0.03%, <5%). Ties to thesis-memory book value ~Rs 162/sh (2,931.71/18.1 cr sh = 161.9). Interim reserves shown as dash per Ind AS 34 convention — no Q1 tie-out possible. |
| F12 SEGMENT FORENSICS | PASS | Single reportable segment declared (Note 2 std l.216 / Note 3 cons l.436): "telecom and data networking related products and services...hence no segment information has been provided." No segment assets/liabilities to trend. Note: single-segment reporting hides thesis-memory monitoring metrics (international mix #6, PLI income #8, BSNL concentration) from this filing. |
| F13 BOARD OUTCOME | FINDING | A3-F13: sole agenda item is results approval; 3h10m single-item meeting duration flagged for a question; separate same-day Reg 30 SMP designation noted but out of scope. |
| F14 NOTE DRAFTING INCONSISTENCIES | FINDING | A3-F14: intra-filing entity-name inconsistencies ("Communication(s)", "Inc"/"Inc."); cumulative governance data point. |
| F15 ENTITY LIST DIFFS | PASS | 3 subsidiaries listed (l.312-314 / l.426-429): Tejas Communications Pte (Singapore), Tejas Communications Nigeria, Saankhya Labs Inc (USA). Consistent with thesis-memory baseline of 3; no additions/deletions/relationship changes. No prior extract for formal ENTITY_CHANGE; the name variant is intra-filing (see F14), not period-over-period. |
| F16 PRESENTATION-SPECIFIC | N.A. | Doctype is a results filing, not an investor presentation. |
| F17 CONCALL SILENCE AUDIT | N.A. | Doctype is a results filing, not a concall transcript. |

---

## COMMITMENT REGISTER (from F6)

| commitment | implied date | note/turn ref | status word |
|---|---|---|---|
| (none) | — | Notes l.211-226 (std), l.418-472 (cons) | — |

No dateable management commitments in the notes. Non-qualifying phrases logged for completeness: "approved by the Board of Directors" (Note 6 l.226 / Note 8 l.472 — past-tense governance, results approval); "anticipated warranty claims" (Note 4 l.222 / Note 6 l.465 — provision estimation basis, Rs 35.11 cr this quarter vs Rs 39.30 cr Q4, a future cash-outflow signal but not a commitment).

---

## FORWARD CROSS-REFERENCES FOR A4 (management questions to draft)
- A3-F8 (FORWARD-SIGNAL): DTA recoverability — will the company continue recognising deferred-tax benefit at statutory rate on losses, and what taxable-profit horizon supports a DTA now ~Rs 434 cr (365 + 68.57)? Ties thesis-memory tripwire (DTA reversal = 52% equity).
- A3-F9 (FORWARD-SIGNAL): quantum and timing of cash-flow-hedge reclassification to P&L; net FX exposure direction (import payables vs export receivables) driving the (7.72) reserve.
- A3-F2 (AMBIGUOUS): what drove Q4 FY26 subsidiary PBT of +7.12 cr and its collapse to zero; any one-time subsidiary item.
- A3-F13 (AMBIGUOUS): scope of the 3h10m single-agenda board meeting; reconcile against the separate same-day Reg 30 SMP designation of the COO and reintroduced QIP optionality.
- Context (not a finding): net worth ~2,931 cr eroding ~209 cr/quarter (Q1 TCI -208.91) → ~14 quarters of runway absent a raise; press-release net debt Rs 4,277 cr (thesis-memory) breaches the red monitoring level (>Rs 4,000 cr) and approaches the Rs 4,500 cr thesis-break tripwire — for A4 to weigh against the balance-sheet, which this interim filing does not disclose.

```yaml
stage: A3-forensics
company: "TEJASNET"
quarter: "Q1 FY27"
doctype: "results"
model: claude-opus-4-8
status: complete
forensics_path: "/home/user/inflection-pipeline/runs/tejasnet-q1fy27/work/forensics_results_tejasnet_q1fy27.md"
ledger_reconciled_pct: 100
checklist:
  F1: PASS
  F2: FINDING
  F3: FINDING
  F4: PASS
  F5: PASS
  F6: PASS
  F7: PASS
  F8: FINDING
  F9: FINDING
  F10: PASS
  F11: PASS
  F12: PASS
  F13: FINDING
  F14: FINDING
  F15: PASS
  F16: N.A.
  F17: N.A.
findings:
  - {id: "A3-F2", check: "F2", line: "169,375", classification: "AMBIGUOUS", implication: "Subsidiary PBT contribution collapsed +7.12->0.00; identical S/C PBT to the paisa while gross components diverge; management question on Q4 subsidiary profit driver."}
  - {id: "A3-F3", check: "F3", line: "165,371,325", classification: "NEUTRAL-FACT", implication: "3 subsidiaries near-dormant (identical depreciation/ECL, Rs 0.86cr revenue, Rs 0.00cr net loss); IP/assets sit in parent."}
  - {id: "A3-F8", check: "F8", line: "172,171", classification: "FORWARD-SIGNAL", implication: "All-deferred tax benefit, zero current tax, ETR 25.3% at statutory; growing DTA (~52% equity KAM) = reversal/equity-writedown risk."}
  - {id: "A3-F9", check: "F9", line: "181,387", classification: "FORWARD-SIGNAL", implication: "Cash-flow-hedge QoQ swing 14.50 exceeds full FY26 move 11.81; underwater hedges to reclassify to P&L = future margin pressure."}
  - {id: "A3-F13", check: "F13", line: "35", classification: "AMBIGUOUS", implication: "3h10m single-agenda board meeting; question undisclosed deliberations vs same-day Reg 30 SMP designation and reintroduced QIP optionality."}
  - {id: "A3-F14", check: "F14", line: "312,426", classification: "NEUTRAL-FACT", implication: "Intra-filing entity-name inconsistencies (Communication(s)/Inc.); cumulative governance/drafting data point."}
forward_signals: ["A3-F8", "A3-F9"]
ambiguous: ["A3-F2", "A3-F13"]
commitments: []
gate_a3: pass
blank_checks: []
```
