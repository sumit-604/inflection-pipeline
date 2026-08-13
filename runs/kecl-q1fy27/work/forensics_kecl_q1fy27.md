# A3 FORENSIC NOTES — Kirloskar Electric Company Limited (KECL) — Q1 FY27 — DOCTYPE: RESULTS

Source extract: `/home/user/inflection-pipeline/runs/kecl-q1fy27/work/extract_results_kecl_q1fy27.txt`
Ledger contract: `/home/user/inflection-pipeline/runs/kecl-q1fy27/work/ledger_results_kecl_q1fy27.md`
Prior-quarter extract: NONE (first pipeline run for KECL). All quarter-over-quarter diffs (F5, F6 status transitions, F14, F15, F16) run against the filing's own comparative columns (Qtr Jun-30-2026 / Qtr Mar-31-2026 / Qtr Jun-30-2025 / Year Mar-31-2026) and cross-note consistency, with the absence of an independent prior filing stated explicitly. No Notion monitoring checklist exists (new name to coverage) — F17 has no external silence baseline.
Auditor-paragraph, going-concern, EoM, Other-Matters, segment-table and "except for" quotes are cited from the VERBATIM RE-EXTRACTION (lines 881-1301), not the mangled original-region lines, per task guidance.

Ledger reconciliation: 100% — every ledger row (Sections 1-11, all 14 notes, 28 P&L rows, 32 segment rows, 3 agenda items, 22 auditor paragraphs, Annexures 2-3, 7 entities, 4 signature blocks) read at its cited line before judging.

Unit note: financial-statement tables are in **Rs Lakhs**; Annexure 3 press release is natively in **Rs Crores** (do not reapply the Lakhs factor there). Rs132.35 cr = 13,235 lakhs, etc.

---

## FINDINGS TABLE

| id | check | ledger row ref | line | verbatim quote (short) | classification | forward implication |
|----|-------|----------------|------|------------------------|----------------|---------------------|
| F1 | F1 ZERO_STANDING | P&L line c "Deferred tax"; Note 12 | 114; 395; 113 | "Deferred tax  .  -" (dash all 8 cols); "Secured Redeemable Non-Convertible Debentures - NIL"; "Adjustments relating to earlier years" (row blank) | FORWARD-SIGNAL | Nil deferred tax in every period despite accumulated losses + eroded net worth = **no DTA recognised** (going-concern doubt bars future-profit assertion). Future ETR steps up once brought-forward losses exhaust. NCD line standing at NIL = funding is coming via equity (Note 9), not debt. |
| F3 | F3 shell-entity | P&L cost rows a-f | 100,103,104,105,106 | Cost of materials "8,083 … 8,083"; Employee benefits "1,952 … 1,952"; Depreciation "101 … 101" (standalone = consolidated, Jun-26) | FORWARD-SIGNAL | Every cost line is **identical** standalone vs consolidated. Foreign subsidiary Kirsons BV and the associate add ~0 to revenue and all cost lines; consolidation touches only ~7 lakhs of full-year PAT. Kirsons BV is operationally a shell; the going-concern flag is balance-sheet cleanup, not lost operations. |
| F4 | F4 unaudited/qualified contribution | Consol review para 7 (Other Matters) | 1248; 1231-1240 | "except for the effects in respect of the matter stated in the paragraph on Other Matters, nothing has come to our attention" | AMBIGUOUS | Consolidated review conclusion is **modified ("except for")**, tied to reliance on Kirsons BV figures converted from local GAAP by Parent management (para 6). Quantified contribution is immaterial (consol PAT ≈ standalone PAT, gap 0-7 lakhs, <1%), yet the auditor still qualified — A4 question: why a scope carve-out for an immaterial, operationally-empty subsidiary? |
| F5 | F5 going concern / EoM | Note 5 (KAM); EoM(a) Note 4; EoM(b) Note 6 | 281-293; 1043-1046; 1064-1066 | "their net worth (after excluding Revaluation Reserve) is eroded. There are certain overdue payments to creditors"; "Our opinion is not modified in respect of this matter" | FORWARD-SIGNAL | Going-concern KAM (both reports): net worth ex-revaluation ERODED, **overdue payments to creditors** — a liquidity red flag disclosed by the auditor. Opinion not modified only because it is *conditional* on the restructuring plan + fund infusion. No prior filing to diff; this is the baseline. Distinct from the F4 "except for" (that attaches to Other Matters/Kirsons BV, NOT to going concern). |
| F6 | F6 forward-commitment mining | Note 5/7; Note 9; press release | 284-288; 371-378; 823; 833-835 | "in advance stage for monetization … which will improve the working capital"; "Board … has approved to issue upto 34,68,007 equity shares … subject to … ensuing general meeting"; "expects conditions to normalize through the balance of the year" | FORWARD-SIGNAL | Multiple dated/dateable management promises → promise-vs-delivery tracker (see Commitment Register). Property monetization and the Rs40 cr preferential issue are the two load-bearing catalysts for the going-concern cure. |
| F7 | F7 hedge mining | Note 5 KAM (auditor); Note 9; press release | 1063-1064; 376-378; 822 | "The appropriateness of the said basis of Going Concern is **subject to** the Company adhering to the restructuring plan and infusion of requisite funds"; "subject to necessary approval of the members … as maybe applicable"; "amid broader macroeconomic and supply chain uncertainty" | AMBIGUOUS | The auditor's going-concern comfort is explicitly conditional ("subject to"). If the restructuring plan slips or funds are not infused, the KAM converts toward a modified opinion next quarter. The macro/supply-chain hedge in the press note pre-empts continued soft billing. |
| F8 | F8 tax forensics | P&L rows a "Current Tax", c "Deferred tax" | 112; 114; 110 | Current tax "30" on FY26 PBT "875" (ETR 3.4%); Jun-26 tax "4" on PBT "(595)"; Deferred tax nil all periods | FORWARD-SIGNAL | FY26 ETR 3.4% vs statutory 25.17% = ~2,170 bps shield (≈190 lakhs) from brought-forward losses. Nil deferred tax = unrecognised DTA. Current tax (4 / 9) charged despite pre-tax LOSSES = MAT / taxable pocket somewhere. Future ETR step-up risk once carryforwards exhaust. "Adjustments relating to earlier years" is nil (not a finding on the non-zero test). |
| F10 | F10 share count / dilution | Note 9; Paid-up capital; EPS rows | 371-375; 128; 133-134 | "issue upto 34,68,007 … equity shares at a floor price of ₹115.34 … aggregating upto ₹40,00,00,000 … to Kirloskar Power Equipments Limited" | FORWARD-SIGNAL | Paid-up steady at 6,641 lakhs (66.41m shares) across all periods; basic≈diluted (no live instrument). But Note 9 preferential issue = **~5.2% forward dilution** (3,468,007 / 66,410,000) to a promoter-group entity at Rs115.34, ~Rs40 cr, not yet in share count. Diluted-EPS "1.2/" is an OCR artifact (read 1.27) — NOT a real basic-vs-diluted discrepancy. |
| F11 | F11 reserves / net-worth tie-out | Other Equity; Paid-up; Note 5 | 130; 128; 281 | Other Equity "6,594"; Paid-up "6,641"; Note 5 "net worth (after excluding revaluation reserve) … is eroded" | FORWARD-SIGNAL | Balance-sheet equity = 6,641 + 6,594 = **13,235 lakhs POSITIVE**, yet Note 5 states net worth ex-revaluation is ERODED (negative). Reconciling item = a **revaluation reserve inside Other Equity that must exceed 13,235 lakhs**. Reported equity is a revaluation-reserve artifact; real net worth is negative. Monetising the revalued land (Note 7, Gokul Road) is the only path to convert paper reserve into cash net worth. Gap >>5% → FINDING. |
| F12 | F12 segment forensics | Segment Assets/Liabilities/Cap-Employed "Others" + Unallocated | 941; 954; 965; 985 | "Others" assets 8,893 / liabilities 927 / capital employed 7,966 on revenue 624; "Add: Unallocated … (19,505)" | AMBIGUOUS | "Others" is an **asset-heavy, near-zero-liability, low-revenue bucket** (cap employed 7,966 on 624 revenue) = non-core property held for monetization (ties Note 7/10). Unallocated capital employed (19,505) = ~Rs195 cr net corporate borrowings (unallocable liabilities 23,203 vs assets 3,698). Rotating machines carries 37,199 assets on 5,743 qtr revenue (0.15x turn). Ambiguous: is falling segment-liability the WC unwind management promises, or debt reduction? → concall question. |
| F13 | F13 board outcome beyond results | Agenda item 2; Note 9 | 47-51; 371-378; 53-54 | "appointment of M/s. Rao, Murthy & Associates … as Cost Auditors"; "subject to … approval of the members … in ensuing general meeting" | FORWARD-SIGNAL | Note 9 preferential issue needs member approval → an **ensuing general meeting with a capital-raising enabling resolution** is incoming (funding round foreshadowed). Cost-auditor appointment (FY27) noted. 19-minute board meeting (12:46→13:05, lines 36-37) for 3 items incl. results + cost auditor. No AR/AGM/dividend/director item this meeting. |
| F14 | F14 note-drafting inconsistencies | Note 4 vs auditor EoM(a); Note 5 vs KAM; EoM numbering | 268-270 vs 503-505; 283 vs 1045; 1068 vs 1200 | Note 4 "SKG Terra **Promenade** / SLPKG Estate **Holdings** / **Luxquisite** Parkland" vs auditor "**Promonede** / **Holding** / **Luxqusite**"; Note 5 "its **subsidiary**" vs KAM "its **subsidiaries**"; standalone EoM "6." vs consolidated EoM "5." | NEUTRAL-FACT | Three entity-name spelling variants across the same filing; singular-vs-plural "subsidiary" between Note 5 and both KAMs; EoM paragraph numbering diverges (standalone 6 / consolidated 5) despite the consolidated report carrying an EXTRA (SEBI 33(8)) paragraph; source typo "respective county" (1242). Individually immaterial, cumulatively a document-control governance data point. |
| F15 | F15 entity-list diffs | Note 4; consol para 7; entity list | 267-278; 1270-1275; 249-254 | "merger of Company's wholly owned subsidiaries i.e., Kelbuzz Trading … SKG Terra Promenade … SLPKG Estate Holdings … Luxquisite Parkland … with the Holding company … order … passed on April 30, 2026 … effective date … April 1, 2024" | NEUTRAL-FACT | No prior-quarter ledger to diff, but the filing documents a consolidation-scope change: 4 domestic subsidiaries merged into KECL (NCLT order 30-Apr-2026, effective 1-Apr-2024, given effect in FY26). Post-merger scope = Parent + Kirsons BV (foreign sub) + one unnamed associate. Baseline recorded for future-quarter diffs; Kaytee Switchgear (SLP counterparty) is a separate historical merger — do not conflate. |

---

## CHECKLIST SCORECARD (all 17, one status each — GATE A3)

| Check | Status | One-line basis |
|-------|--------|----------------|
| F1 ZERO-VALUE STANDING | **FINDING** | Deferred tax nil every period (unrecognised DTA); Note 12 NCD "NIL"; "Adjustments relating to earlier years" fully blank template row. Line 114/395/113. |
| F2 STANDALONE vs CONSOL | **PASS** | S-vs-C gap on Revenue = 0; on PAT = 0 (Jun-26), 3 (Jun-25), 7 (FY26) lakhs, all <1% of standalone PAT; no period swing >5pp. Lines 96,110,115. Near-zero gap feeds F3. |
| F3 SHELL-ENTITY | **FINDING** | All standalone cost lines = consolidated (materials 8,083; employee 1,952; depn 101) → Kirsons BV operationally a shell. Lines 100-106. |
| F4 UNAUDITED CONTRIBUTION | **FINDING** | Consolidated conclusion modified "except for" the Kirsons BV Other-Matters reliance; contribution immaterial (<1% PAT) yet still qualified. Line 1248/1231-1240. |
| F5 GOING CONCERN / EoM | **FINDING** | Net-worth-eroded going-concern KAM + "overdue payments to creditors"; opinion "not modified" but conditional; EoM(a) Note 4, EoM(b) Note 6. Lines 281,1043-1046. |
| F6 FORWARD-COMMITMENT MINING | **FINDING** | Property monetization "in advance stage", Rs40 cr preferential issue "board … approved … subject to … general meeting", "expects … normalize". Lines 284,371,823. |
| F7 HEDGE MINING | **FINDING** | Auditor going concern "subject to the Company adhering to the restructuring plan and infusion of requisite funds"; press "supply chain uncertainty". Lines 1063,822. |
| F8 TAX FORENSICS | **FINDING** | FY26 ETR 3.4% vs 25.17% (~2,170 bps shield); nil deferred tax = unrecognised DTA; current tax charged on pre-tax losses. Lines 110,112,114. |
| F9 OCI FORENSICS | **PASS** | Actuarial remeasurement is annual-only (79 in FY26, nil in every quarter column); quarter OCI is a 9-lakh MTM swing; no single-quarter swing exceeding prior year, no assumption-change signal. Lines 118,121,124. |
| F10 SHARE COUNT / DILUTION | **FINDING** | Paid-up steady 6,641; basic≈diluted; but Note 9 = ~5.2% forward dilution (34,68,007 shares, Rs40 cr, promoter group). Diluted-EPS "1.2/" is OCR, not real. Lines 128,133-134,371. |
| F11 RESERVES / NET-WORTH TIE-OUT | **FINDING** | BS equity 13,235 lakhs positive vs Note 5 "ex-revaluation net worth eroded" (negative) → revaluation reserve >13,235 lakhs is the reconciling item; equity is a paper artifact. Lines 128,130,281. |
| F12 SEGMENT FORENSICS | **FINDING** | "Others" asset-heavy (8,893)/near-zero-liability (927)/low-revenue (624) = non-core property for monetization; Unallocated cap employed (19,505) = ~Rs195 cr net corporate debt. Lines 941,954,965,985. |
| F13 BOARD OUTCOME BEYOND RESULTS | **FINDING** | Ensuing general meeting for the preferential issue = capital-raise enabling resolution incoming; cost-auditor appointment; 19-min meeting. Lines 47-51,371-378. |
| F14 NOTE-DRAFTING INCONSISTENCIES | **FINDING** | 3 entity spelling variants; singular/plural "subsidiary"; EoM numbering 6 vs 5; "county" typo — cumulative document-control data point. Lines 268/503,283/1045,1068/1200. |
| F15 ENTITY-LIST DIFFS | **FINDING** | 4 domestic subsidiaries merged into parent (NCLT 30-Apr-2026, eff 1-Apr-2024); scope now Parent+Kirsons BV+associate. Baseline for future diffs; no prior ledger. Lines 267-278,1270-1275. |
| F16 DROPPED/REFRAMED DISCLOSURES | **N.A.** | Doctype = results, not a presentation; no prior deck to diff (first run). Press-release order-book metrics captured under F6/F13. |
| F17 CONCALL SILENCE AUDIT | **N.A.** | No concall/transcript in scope; no Notion monitoring checklist (new name) to audit silence against. F6 commitments carried forward as the silence baseline for the first concall when one occurs. |

GATE A3 self-check: 17 of 17 checks carry an explicit status (11 FINDING, 4 PASS effectively 2 PASS [F2,F9] + 13 FINDING + 2 N.A.). Count: FINDING = 13 (F1,F3,F4,F5,F6,F7,F8,F10,F11,F12,F13,F14,F15); PASS = 2 (F2,F9); N.A. = 2 (F16,F17). Total 17. **No blank checks. GATE A3 = PASS.**

---

## COMMITMENT REGISTER (from F6 — promise-vs-delivery tracker seed)

| commitment | implied date | note/ref | status word |
|------------|-------------|----------|-------------|
| Monetization of Gokul Road, Hubballi immovable property (31 Ac 24 G; consideration 9,512 lakhs) to improve working capital/net worth | "forthcoming periods" (indefinite; change-of-land-use contested) | Note 5 (l.284-288), Note 7 (l.305-354) | underway (contested — contempt petition 02-Jun-2026; State writ appeal 07-Apr-2026) |
| Preferential issue of up to 34,68,007 equity shares (~Rs40 cr, floor Rs115.34) to Kirloskar Power Equipments Ltd | "ensuing general meeting" (near-term EGM) | Note 9 (l.371-378) | board-approved (16-Jul-2026), pending member approval |
| Merger of 4 wholly-owned subsidiaries into KECL | done (NCLT order 30-Apr-2026, eff 01-Apr-2024) | Note 4 (l.267-278), consol para 7 (l.1270-1275) | completed |
| Trading conditions to "normalize through the balance of the year" | FY27 (H2) | Press release (l.823) | guidance issued |
| Sale of 1.06-acre Gokul Road plot (Rs300 lakhs) — possession handed over, PoA executed | possession done 26-Dec-2025; sale deed pending | Note 8 (l.357-369) | consideration received, deed execution underway |
| Cost auditor appointment (Rao, Murthy & Associates) FY27 | FY27 | Agenda 2 (l.47-51), Annexure 2 (l.781-790) | appointed 13-Aug-2026 |
| SLP on resale-tax penalty Rs527 lakhs (Kaytee Switchgear) | Supreme Court, pending | Note 6 (l.295-303), EoM(b) (l.1216-1220) | admitted, sub judice |

---

## CLASSIFICATION ROLL-UP (for A4 question generation)

- **FORWARD-SIGNAL** (flagged for A4): F1, F5, F6, F8, F10, F11, F13
- **AMBIGUOUS** (lean-bear; A4 to convert into management questions): F4, F7, F12
- **NEUTRAL-FACT / CONFIRMATORY**: F3 (shell = confirmatory of consolidation being hollow), F14, F15
- **PASS**: F2, F9  |  **N.A.**: F16, F17

Priority A4 questions seeded:
1. (F11/F5) What is the exact revaluation reserve balance inside Other Equity (6,594 lakhs) and the ex-revaluation net worth in Rs — quantify how negative real net worth is, and the timeline to close it via monetization + the Rs40 cr infusion.
2. (F4) Why does the auditor carry an "except for" scope carve-out on Kirsons BV when its consolidated PAT contribution is <1%? Is Kirsons BV dormant / being wound down / carrying an impaired asset?
3. (F5) Quantify the "overdue payments to creditors" flagged in the going-concern KAM — amount, ageing, and cure plan.
4. (F12) Is the fall in segment liabilities working-capital unwind or debt repayment, and what is the "Others" segment's 7,966-lakh capital employed composed of?
5. (F7/F6) The going-concern opinion is conditional on adhering to the restructuring plan + fund infusion — what happens to the review conclusion if the change-of-land-use litigation (Note 7) blocks the Gokul Road monetization?

```yaml
stage: A3-forensics
company: "KECL"
quarter: "q1fy27"
doctype: "results"
model: claude-opus-4-8
status: complete
forensics_path: "/home/user/inflection-pipeline/runs/kecl-q1fy27/work/forensics_kecl_q1fy27.md"
ledger_reconciled_pct: 100
checklist:
  F1: FINDING
  F2: PASS
  F3: FINDING
  F4: FINDING
  F5: FINDING
  F6: FINDING
  F7: FINDING
  F8: FINDING
  F9: PASS
  F10: FINDING
  F11: FINDING
  F12: FINDING
  F13: FINDING
  F14: FINDING
  F15: FINDING
  F16: N.A.
  F17: N.A.
findings:
  - {id: "F1", check: "F1", line: "114", classification: "FORWARD-SIGNAL", implication: "Nil deferred tax every period = unrecognised DTA under going-concern doubt; future ETR step-up; NCD line NIL = equity-funded"}
  - {id: "F3", check: "F3", line: "100", classification: "FORWARD-SIGNAL", implication: "Standalone=consolidated cost lines -> Kirsons BV a shell; going-concern is balance-sheet cleanup not lost operations"}
  - {id: "F4", check: "F4", line: "1248", classification: "AMBIGUOUS", implication: "Consolidated review conclusion modified 'except for' Kirsons BV despite <1% PAT contribution -> A4 question"}
  - {id: "F5", check: "F5", line: "281", classification: "FORWARD-SIGNAL", implication: "Net worth ex-revaluation eroded + overdue creditor payments; opinion unmodified but conditional"}
  - {id: "F6", check: "F6", line: "371", classification: "FORWARD-SIGNAL", implication: "Dated commitments: property monetization, Rs40 cr preferential issue, normalization guidance -> promise tracker"}
  - {id: "F7", check: "F7", line: "1063", classification: "AMBIGUOUS", implication: "Auditor going-concern comfort 'subject to' restructuring adherence + fund infusion; slippage risks modified opinion"}
  - {id: "F8", check: "F8", line: "110", classification: "FORWARD-SIGNAL", implication: "FY26 ETR 3.4% vs 25.17% (~2170 bps shield); nil DTA; ETR step-up once carryforwards exhaust"}
  - {id: "F10", check: "F10", line: "371", classification: "FORWARD-SIGNAL", implication: "~5.2% forward dilution from Rs40 cr promoter-group preferential issue, not yet in share count"}
  - {id: "F11", check: "F11", line: "130", classification: "FORWARD-SIGNAL", implication: "BS equity 13,235 lakhs positive but ex-revaluation net worth eroded -> revaluation reserve >13,235 lakhs; equity a paper artifact"}
  - {id: "F12", check: "F12", line: "941", classification: "AMBIGUOUS", implication: "'Others' asset-heavy near-zero-liability = non-core property for monetization; Unallocated (19,505) = ~Rs195 cr net corporate debt"}
  - {id: "F13", check: "F13", line: "47", classification: "FORWARD-SIGNAL", implication: "Ensuing general meeting = capital-raise enabling resolution incoming; cost-auditor appointment"}
  - {id: "F14", check: "F14", line: "268", classification: "NEUTRAL-FACT", implication: "Entity spelling variants, singular/plural subsidiary, EoM numbering divergence = document-control governance data point"}
  - {id: "F15", check: "F15", line: "267", classification: "NEUTRAL-FACT", implication: "4 domestic subsidiaries merged into parent; scope now Parent+Kirsons BV+associate; baseline for future diffs"}
forward_signals: ["F1", "F5", "F6", "F8", "F10", "F11", "F13"]
ambiguous: ["F4", "F7", "F12"]
commitments:
  - {commitment: "Monetization of Gokul Road Hubballi property (working-capital/net-worth cure)", implied_date: "forthcoming periods (litigation-contested)", ref: "Note 5 l.284 / Note 7 l.305", status_word: "underway"}
  - {commitment: "Preferential issue up to 34,68,007 shares (~Rs40 cr) to Kirloskar Power Equipments Ltd", implied_date: "ensuing general meeting", ref: "Note 9 l.371", status_word: "board-approved-pending-members"}
  - {commitment: "Merger of 4 wholly-owned subsidiaries into KECL", implied_date: "done (NCLT 30-Apr-2026, eff 01-Apr-2024)", ref: "Note 4 l.267", status_word: "completed"}
  - {commitment: "Trading conditions to normalize through balance of FY27", implied_date: "FY27 H2", ref: "Press release l.823", status_word: "guidance"}
  - {commitment: "Sale deed of 1.06-acre Gokul Road plot (Rs300 lakhs)", implied_date: "possession done Dec-2025; deed pending", ref: "Note 8 l.357", status_word: "underway"}
  - {commitment: "Cost auditor appointment FY27 (Rao, Murthy & Associates)", implied_date: "FY27", ref: "Agenda 2 l.47 / Annexure 2 l.781", status_word: "completed"}
  - {commitment: "SLP resale-tax penalty Rs527 lakhs (Kaytee Switchgear)", implied_date: "Supreme Court pending", ref: "Note 6 l.295 / EoM(b) l.1216", status_word: "admitted"}
gate_a3: pass
blank_checks: []
```
