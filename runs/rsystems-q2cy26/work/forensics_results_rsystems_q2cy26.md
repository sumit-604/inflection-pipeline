# A3 FORENSIC NOTES — R Systems International Limited (RSYSTEMS) — Q2 CY2026 — DOCTYPE: results

Source extract: `runs/rsystems-q2cy26/work/extract_results_rsystems_q2cy26.txt` (1412 lines, 21 pages)
Ledger: `runs/rsystems-q2cy26/work/ledger_results_rsystems_q2cy26.md`
Unit: Rs. million (x0.1 -> Rs Cr). Prior-quarter extract: NOT PROVIDED (verbatim EoM/entity/line diffs against prior quarter could not be performed; flags below rest on in-document evidence only).
Ledger reconciliation: 100% — all 8 agenda items, 31 notes, 281 line items (10 tables), 6 zero-standing rows, 27 auditor paragraphs, 31 entities, 15 signature blocks read at their cited lines.

Reader context tested (not assumed): Novigo consolidated w.e.f. 13-Nov-2025; Velotio/Scaleworx amalgamated into parent; prior "standing software qualification"; OCRPS + Novigo CCPS dilution overhang; S-vs-C PAT gap as first-class metric; all 8 Board agenda items.

---

## FINDINGS TABLE

| id | check | ledger row ref | line | verbatim quote | classification | forward implication |
|----|-------|----------------|------|----------------|----------------|---------------------|
| F1-a | F1 | Consol P&L 10(b)/11(b) NCI + BS NCI | L161, L378 | "Non controlling interest" (blank all periods) vs "Non controlling interests 1,923.88 ... 1,923.88" | AMBIGUOUS | Rs 1,923.88m NCI is static across all six periods yet attracts ZERO P&L attribution — behaves like a fixed instrument (candidate: Novigo CCPS classified as equity NCI), not an operating minority. Ask nature/terms and 2028 conversion mechanics. |
| F2-a | F2 | Consol PAT L135 vs Standalone PAT L784 | L135, L784 | Consol "555.70"; Standalone "358.09" | FORWARD-SIGNAL | S-vs-C PAT gap swung from +4.0% of standalone (Q1: 654.14 vs 628.92) to +55.2% (Q2: 555.70 vs 358.09) — a 51pp swing (threshold 5pp). Subsidiary net contribution jumped from +25.22m to +197.61m. At FY25 the gap was NEGATIVE (-6.6%: 1,861.96 vs 1,994.52) — subsidiaries were dilutive. Relationship is inverting and volatile; Novigo ramp is now the swing factor but is not separately quantified. |
| F2-b | F2 | Finance costs L120/L770; ISCR L280/L938; DSCR L932 | L120, L280, L932 | Consol finance costs "94.77" (Q2) vs "21.41" (Q2CY25); standalone DSCR "5.43" | FORWARD-SIGNAL | Consolidation (Novigo debt, Rs 2,697.75m non-current borrowings L384) lifted finance costs ~4.4x YoY; interest service coverage HALVED (consol 25.39x->9.35x L280; standalone 21.17x->6.52x L938); standalone DSCR fell to 5.43x (L932) from 13.67x. Coverage still above monitoring floors (ISCR >6x, warning <5x) but trend break is sharp — leverage-driven earnings sensitivity rising. |
| F2-c | F2 | Standalone P&L L764/L765/L772/L784 | L784, L765, L772 | PAT "358.09" (Q2) vs "628.92" (Q1); Other income "12.54" vs "210.71"; Other expenses "569.27" vs "293.63" | AMBIGUOUS | Standalone Q2 PAT -43% QoQ despite revenue +6.9% (3,425.40 vs 3,203.41). Driven by (a) other-income collapse (Q1 carried Rs 140.60m intercompany dividend, Note 4 L859, tax-light, eliminated in consol — this also artificially compressed the Q1 S-vs-C gap) and (b) other expenses +94% QoQ (+275.64m), a bigger jump than consol's (+135m). Unexplained standalone cost spike — post-amalgamation reclassification? Concall question. |
| F4-a | F4 | Consol review report para 6 | L592-598 | "We did not review the interim financial information of 21 subsidiaries ... total net profit after tax of Rs. 114.58 million and Rs. 147.96 million" | AMBIGUOUS | Unreviewed component PAT = 114.58m = 20.6% of Q2 consolidated PAT (555.70); 6M 147.96m = 12.2%; unreviewed revenue 1,605.36m = 26.7% of consol revenue. Both above the 10% threshold. No prior ledger to trend the count (21) or %. Novigo entities presumably sit in this unreviewed bucket — reliance on component/other auditors is material. |
| F5-a | F5 | Consol review report (no EoM); Standalone audit report | L520(ledger), L626, L832 | "Our conclusion on the Statement is not modified in respect of this matter" | AMBIGUOUS | No Emphasis of Matter, no qualification, unmodified opinion in BOTH reports this quarter. The reader-context "standing technical software-related qualification" is NOT observable here. Cannot verbatim-diff (no prior extract). Its apparent absence is itself a status change to confirm — resolved, reclassified, or annual-report-only? |
| F6-a | F6 | Consol Note 6 / Standalone Note 7 | L231-232, L887-888 | "Such accumulated amount will be reclassified to the Statement of Profit and Loss" | FORWARD-SIGNAL | Rs 89.63m accumulated cash-flow-hedge LOSS in reserve is a dated future P&L drag, reclassifying as hedged forecast FX transactions land. Known earnings headwind for coming quarters. |
| F6-b | F6 | Agenda items 3, 3a-3e; postal ballot | L40-61, L63 | "The Postal Ballot Notice will be circulated separately to the shareholders" | NEUTRAL-FACT | Board approved and will circulate a postal ballot seeking shareholder approval for 3 ID appointments + 1 NED + NEID commission. Near-term dated commitment; content (record date, e-voting window, scrutinizer) not attached (circulated separately). |
| F8-a | F8 | Tax lines Consol L132-135 / Standalone L781-784 | L134, L135, L783 | Consol total tax "249.37" on PBT "805.07"; standalone "156.82" on "514.91" | AMBIGUOUS | Q2 ETR elevated: consol 30.98%, standalone 30.46% vs statutory 25.17%. Standalone ETR swung 20.24% (Q1, exempt-dividend-depressed) -> 30.46% (Q2). Persistent FY deferred-tax CREDITS (consol -74.21m, standalone -65.80m) = DTA build/utilisation -> future ETR step-up risk. Novigo overseas mix may structurally raise ETR and compress PAT margin. Ask sustainable tax rate. No "earlier-years" tax adjustment line present. |
| F9-a | F9 | Consol OCI L146-153 / Standalone L790-802; Note 6/7 | L146, L139, L231 | "Fair value changes on derivatives designated as cash flow hedge ... 90.79 ... (180.42)" | AMBIGUOUS | New cash-flow-hedge OCI line (designated w.e.f. 01-Jan-2026, no prior-year comparative): +90.79m (Q2), -180.42m (Q1), net -89.63m accumulated. Highly volatile. Separately, Q1 actuarial re-measurement gain +31.66m EXCEEDS the full FY25 figure (-10.40m) in magnitude — candidate discount-rate/assumption change to verify at Annual Report. |
| F10-a | F10 | Note 3 OCRPS; BS "Instruments entirely equity" L375/L1059; Note 7 RSU | L205-210, L375, L235 | "approved the allotment of 5,160,833 Optionally Convertible Redeemable Preference Shares ... Rs. 5.16 million ... disclosed as 'Instruments entirely equity in nature'" | FORWARD-SIGNAL | Paid-up capital drift (118.40->118.49) fully traced to RSU exercise (89,106 shares 6M, Note 7 L235) — clean. But OCRPS 5,160,833 (Re 1 each, valued Rs 2,407.00m) newly allotted this quarter; basic-vs-diluted spread ~4-5% (Q2 consol 4.69/4.49; standalone 3.02/2.89 L812-813). NOTE unit mismatch: filing states 5,160,833 = 5.16 MILLION OCRPS (Rs 5.16m to equity), whereas the Notion thesis cites "OCRPS 5.16 Cr shares" — A4 to reconcile the units before sizing the Nov-2027 dilution. |
| F12-a | F12 | Consol Segment L503/L510; note L522-524 | L510, L503, L522 | "disclosure relating to segment assets and liabilities has not been provided"; IT results "687.84" on revenue "5,437.01" | FORWARD-SIGNAL | Segment assets/liabilities withheld under Ind AS 108 interchangeable-use exemption (L522-524, L1212-1214) — equity-funded-build / capex-proxy detection impossible. IT-services segment margin compressed QoQ 16.16% (Q1: 841.72/5,208.13) -> 12.65% (Q2: 687.84/5,437.01) while revenue grew — consistent with lower-margin inorganic (Novigo) mix. Monitoring: Novigo margin uplift missed >40bps is a thesis-broken trigger; ask segment/Novigo margin bridge. |
| F13-a | F13 | Agenda 3a-3e | L42-61 | "Appointment of Mr. Pranav Damani (DIN: 11416778) as Non-Executive Non-Independent Director" | FORWARD-SIGNAL | Simultaneous refresh: 3 Independent Directors (Kekre, Sangeeta Kapil Jit Singh, Srikanth Balachandran), 5-year terms from 29-Jun-2026 -> to Jun-2031, spanning the OCRPS (Nov-2027) and CCPS (2028) windows; PLUS a new Non-Executive Non-Independent director (Damani, no term) — a likely investor/promoter nominee (Blackstone?). Three IDs at once + one non-independent seat is a governance event. A4: map Damani's affiliation and the trigger for the refresh. No AGM/AR/dividend resolution in this outcome. |
| F15-a | F15 | Entity list #27-31; Note 3 | L722-731, L198-210 | "Novigo Solutions Private Limited ('Novigo') (w.e.f 13 November, 2025) (subsidiary of the Parent)" | FORWARD-SIGNAL | 5 Novigo entities added w.e.f. 13-Nov-2025 (L722-731); Velotio + Scaleworx amalgamated INTO parent (effective 01-May-2026, comparatives restated, Note 3 L198-210/L837-858). Novigo (#27, L722) and RSCSL (#19, L696) are NON-wholly-owned -> candidate source of the Rs 1,923.88m NCI (links F1-a). CRITICAL SILENCE: Novigo revenue is NOT separately disclosed anywhere in the filing (monitoring item 3, ">Rs 55 Cr/quarter, silence = 3rd evasion flag") — the only Novigo-adjacent number is the 21-subsidiary aggregate (1,605.36m, L594). No prior extract to confirm Novigo already appeared last quarter. |

---

## CHECKLIST SCORECARD (all 17, exactly one status each)

| # | Status | One-line basis |
|---|--------|----------------|
| F1 | FINDING | 4 template zero-lines are benign (Debenture redemption reserve NA L286/L949, Inventory turnover NA L317/L991 — no debentures, services co), BUT NCI profit attribution is nil all periods (L161) against a live Rs 1,923.88m NCI on the balance sheet (L378) — anomalous. See F1-a. |
| F2 | FINDING | S-vs-C PAT gap swung 51pp (4.0% -> 55.2%) Q1->Q2; finance-cost surge halved coverage; standalone Q2 PAT -43% QoQ. See F2-a/b/c. YoY consol PAT decline (-26.7%) is largely a base effect from the Q2CY25 Rs 435.95m Noida property gain (Note 4/5 L212), not operational. |
| F3 | PASS | No shells. Consol employee cost 3,661.55 vs standalone 2,124.51 (subs ~1,537m), consol D&A 220.39 vs 138.32 — cost lines materially differ; subsidiaries clearly operational. No going-concern EoM on any entity. |
| F4 | FINDING | 21 subsidiaries unreviewed; PAT 114.58m = 20.6% of Q2 consol PAT (>10%). See F4-a. |
| F5 | FINDING | Both reports unmodified, no EoM / no qualification; prior "standing software qualification" not observable and un-diffable without prior extract; absence is a change to confirm. See F5-a. |
| F6 | FINDING | Commitments mined: hedge reserve "will be reclassified" (F6-a, forward P&L drag); postal ballot "will be circulated" + board-approved director appointments pending shareholder vote (F6-b). See Commitment Register. |
| F7 | PASS | No pre-emptive legal-cover hedge phrases newly added in notes — no "no assurance", "evaluating", "exploring", "in discussions", "endeavour"; no new revenue-lumpiness or customer-concentration hedge. Notes are factual. |
| F8 | FINDING | Q2 ETR elevated (consol 30.98%, standalone 30.46% vs 25.17%); intercompany-dividend-driven ETR volatility; persistent FY deferred-tax credits (DTA). See F8-a. No "earlier-years" tax adjustment line. |
| F9 | FINDING | New volatile cash-flow-hedge OCI (no prior comparative); Q1 actuarial +31.66m exceeds full FY25 (-10.40m) -> possible assumption change to verify at AR. See F9-a. |
| F10 | FINDING | Paid-up drift traced cleanly to RSU exercise, but OCRPS 5,160,833 newly allotted + ~4-5% basic/diluted spread = dilution overhang; Notion "5.16 Cr" vs filing "5.16 million" unit mismatch. See F10-a. |
| F11 | PASS | Net worth ties exactly: consol 118.49 + 5.16 + 10,859.03 = 10,982.68 = Reg 52(4) net worth (L287); standalone 118.49 + 5.16 + 9,227.46 = 9,351.11 = net worth (L950). No third-party number in doc to reconcile against; gap 0%. |
| F12 | FINDING | Segment assets/liabilities withheld (Ind AS 108 exemption L522); IT-services segment margin compressed QoQ 16.16% -> 12.65% while revenue grew. See F12-a. |
| F13 | FINDING | 3 IDs (terms to Jun-2031) + 1 NE non-independent director + NEID commission, via postal ballot — governance refresh spanning the dilution window. See F13-a. |
| F14 | PASS | Note-to-report descriptors match (consol Note 1 "limited review ... unmodified report" L193-194 <-> SRE 2410 review; standalone Note 1 "unmodified audit opinion" L832 <-> SA audit). Cross-references internally consistent (one-note offset from standalone's extra dividend note). Only discrepancies are OCR artifacts ("Naida", "14.29t1/21") — not drafting. |
| F15 | FINDING | 5 Novigo entities added w.e.f. 13-Nov-2025; Velotio/Scaleworx amalgamated into parent; Novigo & RSCSL non-wholly-owned; Novigo revenue not separately disclosed. See F15-a. |
| F16 | N.A. | Doctype is results, not a presentation/deck — no dropped/reframed slide disclosures, chart baselines, or order-book definitions to assess. |
| F17 | N.A. | Doctype is results, not a concall transcript — no turns to silence-audit. Monitoring items the filing structurally cannot answer are forwarded below as concall questions. |

Gate A3: PASS — every check carries exactly one status; every FINDING cites a line.

---

## COMMITMENT REGISTER (from F6)

| commitment | implied date | note/ref | status word |
|------------|--------------|----------|-------------|
| Postal Ballot Notice to be circulated to shareholders and filed with exchanges | Near-term (post 04-Aug-2026; before/around ~12-Aug concall) | Agenda 3, L63-65 | initiated |
| Appointment of 3 Independent Directors (5-yr terms from 29-Jun-2026) — shareholder approval | Postal ballot close (weeks) | Agenda 3a-3c, L42-47 | initiated (board-approved, pending vote) |
| Appointment of Pranav Damani as NE Non-Independent Director — shareholder approval | Postal ballot close | Agenda 3d, L58-59 | initiated |
| NEID commission remuneration — shareholder approval | Postal ballot close | Agenda 3e, L60-61 | initiated |
| Rs 89.63m accumulated cash-flow-hedge loss "will be reclassified" to P&L | As hedged forecast FX transactions affect P&L (coming quarters) | Note 6 L231-232 / Note 7 L887-888 | underway |
| OCRPS 5,160,833 allotted; Rs 5.16m transferred to "Instruments entirely equity in nature" | Completed this quarter (allotted); conversion/redemption overhang -> Nov-2027 | Note 3 L205-210 / L852-858 | completed (allotment) / pending (conversion) |
| Velotio + Scaleworx amalgamation into parent; comparatives restated | Effective 01-May-2026 (appointed date 01-Apr-2024) | Note 3 L198-210 / L837-858 | completed |

---

## MONITORING-CHECKLIST CROSS-REFERENCE (Step 5 triggers -> A4 concall questions)

Items the RESULTS filing CAN answer:
- Debtor turnover (item 7, floor 1.45x): consol 1.47x Q2 (L313), recovered from 1.35x in Q1 (a sub-1.4x trend-break breach last quarter). Standalone 1.71x (L986). Satisfied this quarter; flag the Q1 breach.
- Interest coverage (item 8, >6x, warning <5x): consol ISCR 9.35x (L280), standalone 6.52x (L938) — above floor but halved YoY; standalone DSCR 5.43x (L932) is the softest reading. See F2-b.
- Adjusted EBITDA margin (item 4, >=18.5%): filing operating margin (excl. D&A add-back) consol 14.73% (L318) / standalone 17.32% (L992); adding back D&A, consol reported-basis EBITDA margin ~18.4% Q2 — just below the 18.5% target, above the 17% STAGNANT floor. Definition of "adjusted" to confirm on call.

Items the filing CANNOT answer (silence -> forward to A4 as concall questions; F17 N.A. on results):
- Organic constant-currency revenue growth (item 1): only reported revenue given; consol +30.2% YoY (6,017.01 vs 4,620.15) but blends Novigo inorganic + restatement — organic/CC split not disclosed.
- TTM ACV bookings (item 2): not in filing.
- Novigo revenue >Rs 55 Cr/quarter (item 3): NOT separately disclosed (see F15-a) — potential 3rd evasion flag.
- USD/INR average (item 5), Fixed-price mix (item 6), Annualised ROCE (item 9): not in filing.
- THESIS-BROKEN watch: no KMP fraud and no material audit qualification found (F5); Novigo margin uplift not verifiable (F12-a); Blackstone/price signals N.A. to a results filing.

---

## RECONCILIATION NOTE
All 281 ledger line items across the 10 financial tables, all 31 notes, 8 agenda items, 6 zero-standing rows, 27 auditor paragraphs, 31 consolidated entities and 15 signature blocks were read at their cited lines in the extract and reconciled 100% against the A2 ledger. No unread rows. Prior-quarter extract absent -> F5 (EoM/qualification diff) and F15 (entity diff) rest on in-document dated evidence, flagged AMBIGUOUS where a cross-filing diff is required.
