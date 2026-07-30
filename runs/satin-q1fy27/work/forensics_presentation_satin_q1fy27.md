# A3 FORENSIC NOTES — SATIN Q1 FY27 — doctype: PRESENTATION (Investor/Earnings Deck)

Source document: `extract_presentation_satin_q1fy27.txt` (42 slides, unit = Rs Crores; OCR dividers 2,4,13,28,34,42).
Ledger: `ledger_presentation_satin_q1fy27.md` (A2, gate_a2 pass).
Thesis brief (weighed, NOT evidence): `thesis_brief_notion.md`.

**Ledger reconciliation: 100%.** Every A2 ledger row (Tables 1-8, ~240 line items across slide groups) was read verbatim at its cited line in the A1 extract before judging. No unread rows.

**Doctype scoping (company-authored deck).** Auditor / Board-outcome / statutory-notes checks have no source in a presentation and are marked N.A. explicitly: F4 (auditor Other Matters), F5 (Going Concern/EoM), F9 (OCI), F13 (Board outcome/AGM/director terms), F17 (concall silence). F3 (shell test needs per-subsidiary cost lines — not disclosed) and F12 (segment assets AND liabilities — not disclosed) are also N.A. F15 (entity-list diff) is N.A. because no prior-quarter ledger was supplied (A2 STRUCTURAL_GAP); within-document entity observations are recorded under F1 and the Commitment Register.

---

## FINDINGS TABLE

| id | check | ledger row ref | slide / line | short verbatim quote | classification | forward implication |
|---|---|---|---|---|---|---|
| A3-01 | F1 | T6 #1; T4h SGAL rows | s29/33, L907-937, L1054-1066 | "Satin Growth Alternatives Limited … Received license from SEBI for Category II AIF, targeting first close and first deployment in next quarter" | FORWARD-SIGNAL | Consolidated WOS with a standing template slot but ZERO financials (no AUM/net worth/fund size). A pre-deployment AIF = future capital call / first-close event next quarter; first quarter fund-size disclosure is the milestone A4 must pin. |
| A3-02 | F1 | T6 #2; T4b Active Clients | s16, L468-469 | "xx" (Active Clients, Q1FY27 and QoQ cells) | NEUTRAL-FACT | Literal "xx" template token in the company's own deck (Q1FY27=34, Q4FY26=34, i.e. ~0% QoQ). Unresolved-artifact = deck QC gap; harmless numerically but a governance/drafting data point. |
| A3-03 | F2 | T4k Profit rows s37/s38 | s37 L1183; s38 L1214 | consol PAT "123" vs standalone PAT "120"; Q4FY26 "162" vs "137" | AMBIGUOUS | Subsidiary earnings contribution to consolidated PAT collapsed QoQ: +Rs 25 Cr in Q4FY26 (162-137) to +Rs 3 Cr in Q1FY27 (123-120) — a ~15pp swing of standalone PAT, above the 5pp threshold. Rs 2,623 Cr of subsidiary AUM (SHFL 1,263 + SFL 1,360) is contributing ~Rs 3 Cr of PAT. A4 question: what one-off inflated Q4 subsidiary PAT / what dragged Q1 (SFL provisioning?). |
| A3-04 | F6 | T4a guidance; T4h; s20 | s6 L160-171; s5 L127-147; s20 L574-575; s32 L1034 | "20%-25% … Implies AUM of Rs18,200 - Rs18,900 Crores"; "Promoters will infuse Rs100 Crores"; "Go-live targeted for 30 September 2026" | FORWARD-SIGNAL | Dense dated management-commitment set (see Commitment Register). FY27 guidance is the single most catalyst-relevant slide for A4's monitorables. |
| A3-05 | F7 | T3 #6,#11,#25; s3 fn1 | s16 L473,498; s23 L716; s3 L109 | "Q1FY27 and Q4FY26 are not comparable due to cyclical nature of business"; "Credit cost looks inflated and ROA & ROE are suppressed due to management overlay" | AMBIGUOUS | Pre-emptive comparability hedges appear exactly where QoQ deteriorated (standalone PAT 137->120, ROA 4.31%->3.55%, ROE 17.91%->15.10%, NIM 15.85%->14.36%). "Revenue and NIM are adjusted for MTM gains and Forex Movement" removes forex volatility from every headline — unadjusted figures are never shown. A4 question: request unadjusted revenue/NIM and QoQ bridge. |
| A3-06 | F10 | T5; s3 bullet | s3 L104-105; s39 L1244 | "Promoters will infuse Rs100 Crores Equity Share Capital at ~17% premium to minimum issue price as per SEBI Regulations" | FORWARD-SIGNAL | Preferential equity issue pending (SEBI ICDR minimum-price basis) against 11.0 Cr shares outstanding = a near-term dilutive corporate action requiring EGM/board approval. No basic-vs-diluted EPS spread is disclosed in the deck. Track issue price, share count, timing. |
| A3-07 | F11 | T4d Net Worth; T4l | s21 L621; s39 L1244,L1251 | Net Worth "3,243"; "Book Value per share 270"; "Equity Shares Outstanding (Crores) 11.0" | AMBIGUOUS | Tie-out gap: 270 x 11.0 = Rs 2,970 Cr vs standalone net worth Rs 3,243 Cr = ~8% gap (>5% threshold). Market cap 2,716.5 / price 245.9 corroborates ~11.05 Cr shares. Candidate reconcilers: BVPS computed on a different (consolidated / intangible-adjusted) equity base, warrant/ESOP shares, or the pending Rs 100 Cr infusion. A4: reconcile BVPS base to statutory net worth. |
| A3-08 | F14 | T4i L1108/1143; T4j; T4b | s35 L1108; s36 L1143; s18 L507 | SCNL AUM shown as "13,312" (s18), "12,882" MFI Lending (s35), "12,856" (s36) | NEUTRAL-FACT | Three SCNL "AUM" bases across three slides, reconciled only by scattered footnotes ("+Rs456 Cr other MSME", "incl. BC 26"); states/UTs 30 (s36) vs group 32 (s26). Individually immaterial, cumulatively a drafting/definition-discipline data point (compounds the "xx" artifact). |
| A3-09 | F16 | T4c DELTA_OMITTED (24 rows) | s17 L479-491; s19 L544-556 | Header columns "YoY" and "QoQ" present, every ratio cell blank | AMBIGUOUS | Full-column omission of YoY/QoQ deltas across all 12 ratios on BOTH ratio slides forces manual computation and masks the QoQ step-downs: consol ROA 4.71%->3.30%, consol ROE 23.31%->16.75%, consol NIM 15.20%->13.21%, Gross Yield 23.28%->21.27%. A4: demand the QoQ delta table. |
| A3-10 | F16 | T4a; s5 KPI | s5 L127-129 | "Rs25,000 Crores (Earlier Target) … Revised AUM target for FY2030 … Rs32,000 Crores (Revised Target)" | FORWARD-SIGNAL | FY2030 AUM guidance reframed UP +28% (25,000 -> 32,000) same quarter QoQ profitability softened — an ambitious long-dated anchor set beside a soft near-term print. Pair with Non-MFI share "targeting 30% by 2030" (L140-141). A4 catalyst-timeline item. |
| A3-11 | F16 | T4e bullets; s20 | s24 L748-751; s20 L579 | "Recovery against write-offs Rs8 Crores during Q1FY27"; "GNPA further improved to 2.2% … as against 3.1% as on Mar'26" | CONFIRMATORY-NEGATIVE | GNPA improved 3.1%->2.2% QoQ but the deck discloses ONLY the favourable side (Rs 8 Cr recovery) and OMITS gross write-offs and any ARC sale volume for Q1FY27 — the exact laundering-vs-organic question in monitoring item #2 (FY26 write-offs ~Rs437 Cr + ARC). No Stage-1/2/3 asset split, so monitoring item #22 (Stage 2 %) is undisclosed. A4: request Q1FY27 gross write-offs, ARC sales, and Stage 2 book. |
| A3-12 | F16 | T4k DA Income; T4f | s38 L1198; s37 L1167; s20 L575 | DA Income standalone "92" (Q4FY26 "130"); "Secured DA sanction limit of Rs2,000 Crores from a PSU through its first ever digital-direct assignment" | AMBIGUOUS | DA income fell QoQ (standalone 130->92; consol 145->94) and SCNL off-book AUM is ~flat (3,314->3,277), consistent with Q4FY26's large DA (thesis Rs 1,256 Cr) being lumpy/timing. Deck discloses DA income but NOT Q1FY27 DA assignment VOLUME. New Rs 2,000 Cr PSU DA sanction signals more DA ahead. A4: DA volume this quarter, recurring run-rate, P&L dependence. |

---

## CHECKLIST SCORECARD (F1-F17, all marked)

| Check | Status | One-line basis |
|---|---|---|
| F1 ZERO-VALUE STANDING | **FINDING** | SGAL consolidated WOS with empty template slot (A3-01); literal "xx" Active-Clients token (A3-02). |
| F2 STANDALONE vs CONSOL | **FINDING** | Subsidiary PAT contribution collapsed +25 Cr (Q4FY26) -> +3 Cr (Q1FY27), ~15pp of standalone PAT, >5pp (A3-03). |
| F3 SHELL-ENTITY | **N.A.** | Deck gives no per-subsidiary Cost-of-Materials/Employee/Depreciation lines to compare; SHFL/SFL clearly operating, SGAL pre-operational (noted under F1). |
| F4 UNAUDITED CONTRIBUTION | **N.A.** | No auditor Other Matters in a presentation; results are "Un-audited" (L42) but no component-auditor disclosure. |
| F5 GOING CONCERN / EoM | **N.A.** | No auditor emphasis-of-matter paragraph in a deck. |
| F6 FORWARD-COMMITMENT MINING | **FINDING** | Dense dated commitments: FY27 guidance, Rs100 Cr infusion, Core Banking go-live 30-Sep-2026, SGAL first close, Rs2,000 Cr DA sanction (A3-04; Register below). |
| F7 HEDGE-PHRASE MINING | **FINDING** | "not comparable due to cyclical nature", "adjusted for MTM gains and Forex Movement", "ROA & ROE are suppressed due to management overlay" — pre-emptive cover over QoQ declines (A3-05). |
| F8 TAX FORENSICS | **PASS** | ETR consol 24.2% (39/161), standalone 24.1% (38/158); all periods 22-24% vs statutory 25.17%, trending up YoY from ~22%; no "earlier years" tax adjustment disclosed. Mild future-ETR normalisation risk noted, not finding-level. |
| F9 OCI FORENSICS | **N.A.** | No OCI / actuarial statement in the deck. |
| F10 SHARE COUNT / DILUTION | **FINDING** | Pending Rs100 Cr promoter preferential issue vs 11.0 Cr shares outstanding; no basic/diluted EPS spread disclosed (A3-06). |
| F11 RESERVES / NET-WORTH TIE-OUT | **FINDING** | BVPS 270 x 11.0 Cr = 2,970 vs net worth 3,243 = ~8% gap (>5%) (A3-07). |
| F12 SEGMENT FORENSICS | **N.A.** | No segment assets-AND-liabilities table; entity/product AUM only (covered under F2). |
| F13 BOARD OUTCOME | **N.A.** | No AGM notice / record date / director-term disclosure in a deck; the preferential-issue approval pathway is captured under F6/F10. |
| F14 NOTE-DRAFTING INCONSISTENCY | **FINDING** | SCNL AUM appears as 13,312 / 12,882 / 12,856 across slides 18/35/36; states 30 vs 32; footnote-reconciled but cumulatively a discipline point (A3-08). |
| F15 ENTITY-LIST DIFFS | **N.A.** | No prior-quarter ledger supplied (A2 STRUCTURAL_GAP); SGAL "Since Aug'25" and QTrino 68% (Jan'26) recorded under F1/Register, but a mechanical prior-quarter diff cannot be performed and is not estimated. |
| F16 DROPPED/REFRAMED DISCLOSURE | **FINDING** | YoY/QoQ delta columns blank across 24 ratios (A3-09); FY2030 target revised up (A3-10); gross write-offs/ARC/Stage-2 absent (A3-11); DA volume absent (A3-12). |
| F17 CONCALL SILENCE AUDIT | **N.A.** | No transcript in scope for this doctype; monitoring-checklist silences (write-offs, Stage 2, DA volume, promoter guarantees) folded into F16 findings for A4. |

Tally: 8 FINDING, 1 PASS, 8 N.A. — 17/17 marked, no blanks. GATE A3: pass.

---

## COMMITMENT REGISTER (F6)

| commitment | implied date | slide / line ref | status word |
|---|---|---|---|
| Consolidated AUM growth 20%-25% FY27 -> Rs18,200-18,900 Cr | FY27 (Mar-2027) | s6 L160-161 | guided |
| Standalone credit-cost target 3.0%-3.5% FY27 | FY27 | s6 L171 | guided |
| Standalone ROA target 3.5%-4.0% FY27 | FY27 | s6 L171 | guided |
| FY2030 AUM target revised to Rs32,000 Cr (from Rs25,000 Cr) | FY2030 | s5 L127-129 | revised/upgraded |
| Non-MFI portfolio share to 30% (from 19%) | 2030 | s5 L140-141 | targeting |
| Promoters to infuse Rs100 Cr equity at ~17% premium to min issue price | near-term (H1 FY27) | s3 L104 | announced / "will infuse" |
| SGAL AIF first close and first deployment | next quarter / Q2 FY27 | s5 L147; s33 L1066 | license received, targeting |
| Satin Technologies Core Banking go-live | 30 September 2026 | s32 L1027,L1034 | UAT complete -> underway |
| QTrino LMS/LOS portfolio expansion; SaaS MVP; FIPS certification | ongoing | s32 L1036-1041 | underway / in progress |
| Rs2,000 Cr DA sanction from a PSU (first digital-direct assignment) | drawdown forward | s20 L575 | secured, undrawn |
| Undrawn debt sanctions in hand ~Rs2,600 Cr | forward | s20 L574 | secured, undrawn |
| Branch-add operating efficiencies (392 branches added FY26) "visible in coming quarters" | H2 FY27 | s22 L672 | underway |
| Strategic entry into Kerala (June 2026) | executed Q1 FY27 | s20 L586 | completed |

---

## THESIS CROSS-CHECK NOTES (weighed against monitoring brief; not decisions — A4 owns the verdict)

**FY27 guidance (slide 6, FORWARD-SIGNAL).** Only FOUR numbers are guided: consol AUM growth 20-25% (Rs18,200-18,900 Cr), standalone credit cost 3.0-3.5%, standalone ROA 3.5-4.0%. Notably ABSENT: any consolidated ROE guidance (the thesis "single cleanest metric"), any GNPA, NIM, or consolidated ROA guidance. Selective guidance = AMBIGUOUS; A4 should convert the missing consol-ROE guide into a question.

**ROA/ROE sustainability read (slides 17, 19, 23; DELTA columns blank — A3-09).** Reported Q1FY27: consol ROA 3.30% / ROE 16.75% (L486,488); standalone ROA 3.55% / ROE 15.10% (L551,553). Both DOWN QoQ from Q4FY26 (consol ROA 4.71%, ROE 23.31%; standalone ROA 4.31%, ROE 17.91%). So the Q4 4.71% ROA did NOT repeat — the sustainability concern resolves toward "not sustained at 4.7%." BUT the company steers to ADJUSTED (ex-overlay) figures: adj ROA 4.02% consol / 4.34% standalone, and the management overlay GREW to Rs36 Cr (from Rs21 Cr Q4FY26, Rs8 Cr Q1FY26), mechanically suppressing reported ROA. Corroboration is internal and consistent: standalone ROA 3.55% and ROE 15.10% reappear on the slide-23 return-ratios chart (L704,L700). Net: run-rate ROA sits ~3.3-3.5% reported / ~4.0-4.3% adjusted — above the thesis "sustainable 2.5-3.0%" band, below the Q4 peak. AMBIGUOUS pending the QoQ bridge (A3-09).

**Asset quality (slide 24).** PAR 90 / GNPA 2.2% (Rs219 Cr) — high-confidence (corroborated L579, L747). Stage-3 coverage 85% vs 73% Mar'26 (L750). On-book provisions Rs252 Cr (2.5%) vs RBI-required Rs152 Cr, overlay Rs36 Cr (L748-749). CHART_LAYOUT_AMBIGUOUS on the PAR/NNPA multi-series charts (A2) — the Q1FY27 NNPA and mid-quarter values are NOT asserted. Laundering test (A3-11): only Rs8 Cr recovery-against-write-offs shown; gross write-offs and ARC volume OMITTED; Stage-2 bucket (#22) not disclosed. Standalone GNPA 2.2% is inside every thesis threshold (<=3.05 green), but the mechanism is unverifiable from the deck.

**Direct Assignment (A3-12).** DA income down QoQ (standalone 130->92; consol 145->94); off-book AUM ~flat (3,314->3,277); new Rs2,000 Cr PSU DA sanction. Consistent with Q4 DA being lumpy. DA assignment VOLUME for Q1FY27 not disclosed.

**Funding base (slide 25).** Foreign funding source 25.7%; ECB 21.5%; overseas/HSBC/Blue Orchard among top lenders. "Our Forex borrowings are 100% hedged" repeated 5x (L496,561,714,1188,1219) — but headline revenue/NIM are "adjusted for MTM gains and Forex Movement," so unadjusted forex-FV impact is excluded from every KPI (A3-05). Total debt Rs10,216 Cr (L780); marginal cost of borrowing 10.52%, -37bps YoY (L576); rating unchanged A (Stable)/A1 by ICRA (L790-791). CHART_LAYOUT_AMBIGUOUS on pie-slice-to-label mapping (A2) — lender/product percentages not asserted at slice level.

**Subsidiaries (slides 29-33).** SFL GNPA 3.5% (L991) — well inside thesis-broken trigger 5.0% and stop-loss 5.5%; SFL AUM Rs1,360 Cr, +134% YoY (582->1,360), CRAR 27.1%. SHFL GNPA 3.3%, AUM Rs1,263 Cr, CRAR 59.8%, A- rating. STL net worth Rs20 Cr, QTrino 68% stake, Core Banking go-live 30-Sep-2026. SGAL: ZERO metrics disclosed despite template slot (A3-01). Subsidiary PAT contribution to consol collapsed to ~Rs3 Cr (A3-03).

**Slide-level ambiguity flags respected (not asserted):** CHART_LAYOUT_AMBIGUOUS on slides 8,9,23,24,25,26,31,39 and the "68% stake" floating label on slide 29 (confirmed = STL's QTrino stake, L1029) — scrambled chart values are NOT treated as evidence per the NEVER-estimate rule.

---

```yaml
stage: A3-forensics
company: "SATIN"
quarter: "Q1FY27"
doctype: "presentation"
model: claude-opus-4-8
status: complete
forensics_path: "/home/user/inflection-pipeline/runs/satin-q1fy27/work/forensics_presentation_satin_q1fy27.md"
ledger_reconciled_pct: 100
checklist:
  F1: FINDING
  F2: FINDING
  F3: N.A.
  F4: N.A.
  F5: N.A.
  F6: FINDING
  F7: FINDING
  F8: PASS
  F9: N.A.
  F10: FINDING
  F11: FINDING
  F12: N.A.
  F13: N.A.
  F14: FINDING
  F15: N.A.
  F16: FINDING
  F17: N.A.
findings:
  - {id: "A3-01", check: "F1", line: "907-937 / 1054-1066 (s29,33)", classification: "FORWARD-SIGNAL", implication: "SGAL WOS consolidated with empty template slot; AIF first close/deployment due next quarter"}
  - {id: "A3-02", check: "F1", line: "468-469 (s16)", classification: "NEUTRAL-FACT", implication: "literal 'xx' Active-Clients token; deck QC/drafting gap"}
  - {id: "A3-03", check: "F2", line: "1183 (s37) / 1214 (s38)", classification: "AMBIGUOUS", implication: "subsidiary PAT contribution collapsed +25 Cr Q4FY26 -> +3 Cr Q1FY27, >5pp of standalone PAT"}
  - {id: "A3-04", check: "F6", line: "160-171 (s6); 104 (s3); 1034 (s32); 575 (s20)", classification: "FORWARD-SIGNAL", implication: "FY27 guidance + dated commitment set (see register)"}
  - {id: "A3-05", check: "F7", line: "473,498 (s16); 716 (s23); 109 (s3)", classification: "AMBIGUOUS", implication: "'not comparable' and 'MTM/forex adjusted' hedges cover QoQ declines; unadjusted KPIs never shown"}
  - {id: "A3-06", check: "F10", line: "104 (s3); 1244 (s39)", classification: "FORWARD-SIGNAL", implication: "pending Rs100 Cr promoter preferential issue vs 11.0 Cr shares; dilution/EGM event"}
  - {id: "A3-07", check: "F11", line: "621 (s21); 1244,1251 (s39)", classification: "AMBIGUOUS", implication: "BVPS 270 x 11.0 Cr = 2,970 vs net worth 3,243 = ~8% tie-out gap"}
  - {id: "A3-08", check: "F14", line: "1108,1143 (s35,36); 507 (s18)", classification: "NEUTRAL-FACT", implication: "SCNL AUM shown as 13,312/12,882/12,856 across slides; drafting-discipline point"}
  - {id: "A3-09", check: "F16", line: "479-491 (s17); 544-556 (s19)", classification: "AMBIGUOUS", implication: "YoY/QoQ delta columns blank across 24 ratios; masks QoQ ROA/ROE/NIM/yield step-downs"}
  - {id: "A3-10", check: "F16", line: "127-129 (s5)", classification: "FORWARD-SIGNAL", implication: "FY2030 AUM target revised up 25,000 -> 32,000 Cr amid soft QoQ print"}
  - {id: "A3-11", check: "F16", line: "748-751 (s24); 579 (s20)", classification: "CONFIRMATORY-NEGATIVE", implication: "GNPA 3.1%->2.2% but gross write-offs, ARC sales, and Stage-2 bucket omitted"}
  - {id: "A3-12", check: "F16", line: "1198 (s38); 1167 (s37); 575 (s20)", classification: "AMBIGUOUS", implication: "DA income down QoQ, off-book flat, DA volume undisclosed; new Rs2,000 Cr PSU DA sanction"}
forward_signals: ["A3-01", "A3-04", "A3-06", "A3-10"]
ambiguous: ["A3-03", "A3-05", "A3-07", "A3-09", "A3-12"]
commitments:
  - {commitment: "Consolidated AUM growth 20-25% FY27 (Rs18,200-18,900 Cr)", implied_date: "FY27", ref: "s6 L160-161", status_word: "guided"}
  - {commitment: "Standalone credit-cost target 3.0-3.5% FY27", implied_date: "FY27", ref: "s6 L171", status_word: "guided"}
  - {commitment: "Standalone ROA target 3.5-4.0% FY27", implied_date: "FY27", ref: "s6 L171", status_word: "guided"}
  - {commitment: "FY2030 AUM target revised to Rs32,000 Cr", implied_date: "FY2030", ref: "s5 L127-129", status_word: "revised"}
  - {commitment: "Non-MFI portfolio share to 30%", implied_date: "2030", ref: "s5 L140-141", status_word: "targeting"}
  - {commitment: "Promoters infuse Rs100 Cr equity at ~17% premium", implied_date: "H1 FY27", ref: "s3 L104", status_word: "announced"}
  - {commitment: "SGAL AIF first close and first deployment", implied_date: "Q2 FY27", ref: "s5 L147 / s33 L1066", status_word: "targeting"}
  - {commitment: "Satin Technologies Core Banking go-live", implied_date: "30-Sep-2026", ref: "s32 L1034", status_word: "underway"}
  - {commitment: "Rs2,000 Cr DA sanction from PSU (first digital DA)", implied_date: "forward", ref: "s20 L575", status_word: "secured"}
  - {commitment: "Undrawn debt sanctions ~Rs2,600 Cr in hand", implied_date: "forward", ref: "s20 L574", status_word: "secured"}
  - {commitment: "Branch-add operating efficiencies visible in coming quarters", implied_date: "H2 FY27", ref: "s22 L672", status_word: "underway"}
  - {commitment: "Strategic entry into Kerala", implied_date: "Jun-2026", ref: "s20 L586", status_word: "completed"}
gate_a3: pass
blank_checks: []
```
