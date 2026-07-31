# A3 FORENSIC NOTES — Black Rose Industries Ltd (BLACKROSE), Q1 FY27 (quarter ended 30 June 2026), doctype: RESULTS

Source extract: `/home/user/inflection-pipeline/runs/blackrose-q1fy27/work/extract_results_blackrose_q1fy27.txt` (523 lines, 8 pages, Lakhs, x0.01 to Rs Cr)
Ledger contract: `/home/user/inflection-pipeline/runs/blackrose-q1fy27/work/ledger_results_blackrose_q1fy27.md`
Prior-quarter extract: NOT AVAILABLE (first quarterly-pipeline run for this ticker). F5 and F15 diffs are done against the filing's own text and the Notion monitoring context, not a verbatim prior-quarter diff. This limitation is stated inline where it bites.
Ledger reconciliation: 100% — every ledger row (all sections 1-9, all 68 line items, 13 notes, 12 auditor paras, 5 ZERO_STANDING in-statement flags, 8 annexure items, 4 agenda items, 1 entity, 5 signature blocks) was read at its cited line before judging.

---

## FINDINGS TABLE

| id | check | ledger row ref | line | verbatim quote (short) | classification | forward implication |
|----|-------|----------------|------|------------------------|----------------|---------------------|
| A3-01 | F1 | §7 row 6 / §8 rows 6,12b | 268, 448, 458 | "Exceptional items — [dash]" ; "Tax expense of discontinued operations [blank]" | FORWARD-SIGNAL | Exceptional line stands empty while a foreign-subsidiary winding-up is board-approved. On completion (~12 mo) a disposal gain/loss and FCTR (foreign-currency translation reserve) recycle can land here or in discontinued ops. Blank tax on the discontinued loss = no tax shield taken on the foreign loss. |
| A3-02 | F3 | §7 rows 4a-4f vs §8 rows 4a-4f; §5 para 6 | 258-264 vs 439-444; 389-391 | consolidated "Cost of materials consumed 2,033.96" = standalone 2,033.96 (all cost lines identical) ; sub "total revenue of Rs. 0.00 lakhs" | CONFIRMATORY-NEGATIVE | Sole subsidiary (B.R. Chemicals Japan) is a non-operating shell: zero revenue, near-zero cost, only a Rs 1.72 L loss. Consolidation adds nothing operationally. Confirms the winding-up is balance-sheet cleanup, not a live business exit. |
| A3-03 | F6 | §1 item 4; §3 Sr 3; §8 note 5 | 57-64, 130-133, 495-498 | "The voluntary winding up process is expected to be completed in 12 months, subject to receipt of regulatory approvals" | FORWARD-SIGNAL | Dated management commitments (see Commitment Register). Status has advanced 30-Jan-2025 (discontinue) -> 14-Aug-2025 (initiate closure) -> 31-Jul-2026 (board approved winding-up). This is a milestone confirmation, not boilerplate; feeds Role 5 promise-vs-delivery tracker. |
| A3-04 | F7 | §1 item 4; §3 Sr 3 | 58-59, 130-133, 397 | "not expected to have any material impact on the consolidated financial performance" ; "subject to receipt of regulatory approvals and completion of statutory formalities" | AMBIGUOUS | Two pre-emptive hedges: (1) timing hedge — 12-month completion can slip; (2) impact hedge — "not expected to have any material impact" is management pre-cover against winding-up costs and FCTR recycling. Generate a management question on quantified winding-up cost and reserve recycle. |
| A3-05 | F8 | §7 rows 8a,8b | 271-272 | "Income Tax (including earlier year adjustments) 455.03" ; "Deferred Tax (81.73)" | AMBIGUOUS | Net ETR 26.40% (373.30/1,413.95) sits above the 25.17% statutory rate, but composition is odd: current tax alone is 32.18% of PBT while a large deferred CREDIT of Rs 81.73 L (a 578 bps shield) pulls it back. The line label bundles "earlier year adjustments." Question: is an earlier-year tax charge buried in the 32% current rate, and does the deferred credit reverse (ETR step-up risk)? |
| A3-06 | F9 | §7 row 10i | 275 | "Items that will not be reclassified to profit or loss (net of Tax) 4.14" | AMBIGUOUS | Single-quarter OCI of Rs 4.14 L exceeds the entire FY26 net OCI of Rs 0.04 L (line 275, col 6). Per F9 a single-quarter swing beating the full prior year signals an actuarial assumption change (discount rate / plan assets). Small in rupees but mechanically a flag; verify assumptions at the Annual Report. |
| A3-07 | F12 | §7 note 4 / §8 note 4 | 298-299, 490-491 | "business activity falls within a single primary business segment viz. 'Chemicals'. Hence, there are no separate reportable segments" | FORWARD-SIGNAL | The filing reports ONE segment. The Notion BINARY MASTER GATE (manufacturing rev >=15% YoY, manufacturing margin >=20%) and the acrylonitrile margin tripwire CANNOT be verified from this document — no manufacturing/distribution split, no segment assets/liabilities. Gate is unresolvable on the filing alone; requires concall/segment data. |
| A3-08 | F13 | §1 item 2; §7 note 3 | 46-50, 295-296 | "Declaration of payment of Interim Dividend of Rs. 2 per equity (i.e. 200%...)" ; Record Date 6 Aug 2026 | FORWARD-SIGNAL | Interim dividend Rs 2 on 5.10 Cr shares = ~Rs 10.2 Cr cash outflow, against FY26 CFO of Rs 44.58 Cr that Notion flags as substantially one-time (Red Sea inventory unwind), not run-rate. Cash deployment vs weak cash-conversion is a bear tension; question the sustainable payout basis. |
| A3-09 | F13 | §1 items 1,3 (absence) | 52-55 | "The Notice of 36th Annual General Meeting... to be held on Wednesday, 9th September, 2026" | NEUTRAL-FACT | AGM 9-Sep-2026; full AR drops within weeks -> schedule a Role 6 AR Deep Dive. Notably ABSENT this filing: AR/Board's-Report approval, any director appointment/re-appointment (no term-date signal against the PAM-Solid commissioning window), auditor item, and any capital-raising enabling resolution. |
| A3-10 | F14 | §8 note 5 vs §8 row 12a; §5 para 6 | 499-500 vs 457; 390-391 | note 5: "for the period ended 30 June 2025... Loss: Rs. 1.72 lakhs" | AMBIGUOUS | Drafting inconsistency: note 5 labels the discontinued-ops summary "period ended 30 June 2025" but the Rs 1.72 L loss it carries is the Q1 FY27 figure — line 457 shows discontinued loss of (1.72) for 30-06-2026 and (5.27) for 30-06-2025, and auditor para 6 assigns the 1.72 loss to "the quarter ended 30th June, 2026." The note period label appears stale/copy-pasted. |
| A3-11 | F14 | §1 item 4; §5 para 4; §8 note 5 | 57, 369, 495 | "B.R. Chemicals Co. Limited" (l.57) vs "B.R. Chemicals Co. Limited Gapan" (l.369) vs "BR Chemicals Co. Ltd" (l.495) | NEUTRAL-FACT | Entity-name variants across tables (B.R. vs BR; "Gapan" OCR of Japan; "Japan" dropped at l.62). Individually immaterial; cumulatively a note-drafting/governance data point on the same winding-up entity. |
| A3-12 | F15 | §6 entity; §1 item 4; §5 para 4; §8 note 5 | 57-64, 368-369, 495-498 | "Upon completion of the winding up, B.R. Chemicals Co. Limited shall cease to be a subsidiary" | FORWARD-SIGNAL | The SOLE consolidation entity is exiting: board approved winding-up this quarter (the new step vs the prior discontinued-ops classification). On completion, consolidated collapses to standalone-only and FCTR recycles to P&L. No prior-quarter extract to verbatim-diff; the change is evidenced within this filing's own text. |

---

## CHECKLIST SCORECARD (all 17; exactly one status each)

| Check | Status | One-line basis |
|-------|--------|----------------|
| F1 ZERO-VALUE STANDING | FINDING | Exceptional-items line (268/448) and discontinued-ops tax line (458) stand empty while a foreign-sub winding-up is approved — a live vessel for a future disposal gain/loss & FCTR recycle (A3-01). |
| F2 STANDALONE vs CONSOLIDATED | PASS | S-vs-C PAT gap is only the discontinued Japan loss: 1.72 L (0.165% of standalone PAT) in Q1FY27 vs 5.27 L (1.24%) in Q1FY26 — narrowed ~1.1pp, under the 5pp threshold. Every operating line identical. |
| F3 SHELL-ENTITY DETECTION | FINDING | Identical cost of materials/employee/depreciation lines standalone vs consolidated; sub revenue Rs 0.00 L — sole subsidiary is a non-operating shell (A3-02). |
| F4 UNAUDITED CONTRIBUTION | PASS | Unreviewed foreign-sub result (net loss 1.72 L, TCI loss 0.57 L, para 6 l.389-391) is 0.17% of consolidated PAT — far below the 10% threshold; management-furnished but immaterial. |
| F5 GOING CONCERN / EoM | PASS | No Emphasis of Matter and no Going Concern paragraph in either the standalone (l.215-221) or consolidated (l.379-385) report; only an Other-Matters reliance para. No prior-quarter extract to diff — noted; nothing to track. |
| F6 FORWARD-COMMITMENT MINING | FINDING | Multiple dated commitments: winding-up "expected to be completed in 12 months" (l.130-131), "shall cease to be a subsidiary" (l.62), AGM "to be held on... 9th September, 2026" (l.52), dividend record date (A3-03; register below). |
| F7 HEDGE PHRASE MINING | FINDING | "not expected to have any material impact" (l.58-59) and "subject to receipt of regulatory approvals" (l.132) — pre-emptive cover on winding-up cost and timing (A3-04). |
| F8 TAX FORENSICS | FINDING | ETR 26.40% net but current tax 32.18% of PBT offset by a Rs 81.73 L deferred credit (578 bps shield); label bundles "earlier year adjustments" (A3-05). |
| F9 OCI FORENSICS | FINDING | Q1FY27 OCI 4.14 L exceeds full FY26 net OCI 0.04 L — mechanical assumption-change flag; verify actuarial assumptions at AR (A3-06). |
| F10 SHARE COUNT & DILUTION | PASS | Paid-up capital flat at 510.00 L (Re 1 FV) across all four periods (l.278/466); Basic = Diluted EPS every period (l.281-282/470-474) — no dilutive instruments, no corporate action. |
| F11 RESERVES / NET WORTH TIE-OUT | PASS | Consol Other Equity 16,433.61 L less standalone 16,418.02 L = 15.59 L, cleanly matching Annexure A sub net worth "Rs. 15.58 Lakhs" (l.123). Internal tie-out clean; no third-party number in extract to reconcile against. |
| F12 SEGMENT FORENSICS | FINDING | Single-segment "Chemicals" reporting (l.298-299/490-491) means NO manufacturing/distribution split or segment assets/liabilities — the thesis BINARY MASTER GATE is unverifiable from the filing (A3-07). |
| F13 BOARD OUTCOME | FINDING | Interim dividend Rs 2 (~Rs 10.2 Cr) vs one-time-heavy CFO (A3-08); AGM 9-Sep-2026 -> AR deep-dive; conspicuous absence of AR approval, director re-appointments, capital-raise resolutions (A3-09). |
| F14 NOTE DRAFTING INCONSISTENCIES | FINDING | Note 5 dates the discontinued-ops summary "period ended 30 June 2025" but carries the Q1FY27 1.72 L loss (A3-10); entity-name variants B.R./BR Chemicals (A3-11). |
| F15 ENTITY LIST DIFFS | FINDING | Sole consolidation entity (B.R. Chemicals Japan) winding-up approved this quarter; will cease to be a subsidiary on completion (A3-12). No prior-quarter diff available; evidenced in-filing. |
| F16 DROPPED/REFRAMED DISCLOSURES | N.A. | Presentation-specific check; this is a results filing. |
| F17 CONCALL SILENCE AUDIT | N.A. | Concall-specific check; no transcript in this doctype. Notion checklist items unaddressable here are surfaced via F12/F13/F15 above. |

---

## COMMITMENT REGISTER (from F6)

| commitment | implied date | note/ref | status word |
|------------|--------------|----------|-------------|
| Voluntary winding-up of B.R. Chemicals Co. Ltd, Japan completed | ~12 months (~Jul 2027), subject to regulatory approvals | Annexure A Sr 3, l.130-133 | underway (board-approved this meeting) |
| B.R. Chemicals shall cease to be a subsidiary | upon winding-up completion (~Jul 2027) | Board letter item 4, l.62 | initiated |
| Closure / sale / transfer of 100% shareholding — steps initiated | since 14 Aug 2025 board decision (cont. of 30 Jan 2025) | Consol note 5, l.495-498 | initiated -> board-approved (status advanced) |
| Interim dividend Rs 2/share payment | Record Date 6 Aug 2026 | Note 3, l.295-296 & letter item 2, l.46-50 | board approved / to be paid |
| 36th AGM via VC/OAVM | 9 September 2026, 02:00 p.m. IST | Board letter item 3, l.52-55 | to be held |

Milestone note for Role 5: the winding-up has progressed across three quarters (30-Jan-2025 discontinue -> 14-Aug-2025 initiate closure -> 31-Jul-2026 board approves winding-up). Treat the 31-Jul-2026 approval as a confirmed status transition, not boilerplate.

---

## ANALYST HANDOFF NOTES (context for A4, not forensic findings)

- Total revenue Q1FY27 9,013.66 L vs Q1FY26 6,088.95 L (+48.0% YoY) but -14.0% QoQ vs Q4FY26 10,477.89 L. Because the filing is single-segment, this blend cannot be split into manufacturing vs distribution — the +48% cannot be attributed to the >=15% manufacturing-growth gate (see A3-07).
- Other expenses spiked to 1,292.71 L (Q1FY27) from 667.04 L (Q1FY26, +93.8%) and 826.13 L (Q4FY26, +56.5%) — a material cost swing worth a management question (freight/export/tariff drag per Notion export-collapse and REACH/KKDIK context). Not a formal F1-F15 line item; surfaced for A4.
- Cost of materials +19.4% YoY and purchase of stock-in-trade +34.0% YoY are directionally consistent with the acrylonitrile +33-50% spike tripwire, but single-segment reporting prevents isolating the manufacturing margin.

---

```yaml
stage: A3-forensics
company: "BLACKROSE"
quarter: "Q1 FY27"
doctype: "results"
model: claude-opus-4-8
status: complete
forensics_path: "/home/user/inflection-pipeline/runs/blackrose-q1fy27/work/forensics_blackrose_q1fy27.md"
ledger_reconciled_pct: 100
checklist:
  F1: FINDING
  F2: PASS
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
  - {id: "A3-01", check: "F1", line: "268/448/458", classification: "FORWARD-SIGNAL", implication: "Empty exceptional/discontinued-tax lines are a vessel for a future disposal gain-loss and FCTR recycle when the Japan sub winding-up completes."}
  - {id: "A3-02", check: "F3", line: "258-264 vs 439-444; 389-391", classification: "CONFIRMATORY-NEGATIVE", implication: "Sole subsidiary is a non-operating shell (zero revenue, identical cost lines); consolidation adds nothing operationally."}
  - {id: "A3-03", check: "F6", line: "57-64/130-133/495-498", classification: "FORWARD-SIGNAL", implication: "Dated winding-up and AGM/dividend commitments; winding-up status advanced to board-approved, a milestone for Role 5 tracking."}
  - {id: "A3-04", check: "F7", line: "58-59/132/397", classification: "AMBIGUOUS", implication: "Hedges on winding-up timing and impact pre-cover for possible costs and reserve recycle; quantify at concall."}
  - {id: "A3-05", check: "F8", line: "271-272", classification: "AMBIGUOUS", implication: "Current tax 32.2% vs 25.17% statutory offset by Rs 81.73L deferred credit (578bps shield); possible earlier-year adjustment and ETR step-up risk."}
  - {id: "A3-06", check: "F9", line: "275", classification: "AMBIGUOUS", implication: "Single-quarter OCI 4.14L exceeds full FY26 OCI 0.04L; likely actuarial assumption change to verify at Annual Report."}
  - {id: "A3-07", check: "F12", line: "298-299/490-491", classification: "FORWARD-SIGNAL", implication: "Single-segment reporting hides manufacturing/distribution split; BINARY MASTER GATE and margin tripwire unverifiable from filing."}
  - {id: "A3-08", check: "F13", line: "46-50/295-296", classification: "FORWARD-SIGNAL", implication: "Rs 2 interim dividend (~Rs 10.2Cr) deployed against one-time-heavy FY26 CFO; sustainable payout basis in question."}
  - {id: "A3-09", check: "F13", line: "52-55", classification: "NEUTRAL-FACT", implication: "AGM 9-Sep-2026 signals imminent AR (schedule Role 6 deep dive); absence of director/AR/capital-raise resolutions is notable."}
  - {id: "A3-10", check: "F14", line: "499-500 vs 457; 390-391", classification: "AMBIGUOUS", implication: "Note 5 mislabels the Q1FY27 discontinued loss as period ended 30 June 2025; clarify which period the figures pertain to."}
  - {id: "A3-11", check: "F14", line: "57/369/495", classification: "NEUTRAL-FACT", implication: "Entity-name variants (B.R./BR Chemicals, Gapan) are a cumulative drafting/governance data point."}
  - {id: "A3-12", check: "F15", line: "57-64/368-369/495-498", classification: "FORWARD-SIGNAL", implication: "Sole consolidation entity exiting; on completion consolidated collapses to standalone and FCTR recycles to P&L."}
forward_signals: ["A3-01", "A3-03", "A3-07", "A3-08", "A3-12"]
ambiguous: ["A3-04", "A3-05", "A3-06", "A3-10"]
commitments:
  - {commitment: "Voluntary winding-up of B.R. Chemicals Co. Ltd, Japan completed", implied_date: "~12 months (~Jul 2027), subject to regulatory approvals", ref: "Annexure A Sr 3, l.130-133", status_word: "underway"}
  - {commitment: "B.R. Chemicals shall cease to be a subsidiary", implied_date: "on winding-up completion (~Jul 2027)", ref: "Board letter item 4, l.62", status_word: "initiated"}
  - {commitment: "Closure/sale/transfer of 100% shareholding steps", implied_date: "since 14 Aug 2025 board decision", ref: "Consol note 5, l.495-498", status_word: "initiated"}
  - {commitment: "Interim dividend Rs 2/share payment", implied_date: "Record Date 6 Aug 2026", ref: "Note 3, l.295-296", status_word: "approved"}
  - {commitment: "36th AGM via VC/OAVM", implied_date: "9 September 2026", ref: "Board letter item 3, l.52-55", status_word: "to be held"}
gate_a3: pass
blank_checks: []
```
