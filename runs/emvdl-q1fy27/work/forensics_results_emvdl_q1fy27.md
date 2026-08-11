# A3 FORENSIC NOTES — EMVDL Q1 FY27 (Doctype: RESULTS)

Company: Embassy Developments Limited (formerly Equinox India Developments Limited)
Quarter: Q1 FY27 (quarter ended June 30, 2026)
Source extract: runs/emvdl-q1fy27/work/extract_results_emvdl_q1fy27.txt
Reconciliation contract: runs/emvdl-q1fy27/work/ledger_results_emvdl_q1fy27.md
Model: claude-opus-4-8

Line numbers cite the A1 extract's embedded line numbers (same convention as the A2
ledger; real file line = embedded + 14). Unit: Rs millions unless stated (x0.1 -> Rs Cr).

Ledger reconciliation: 100%. Every A2 section (Board Outcome 4 agenda items + 2
sub-annexures; standalone 57/consolidated line items; 25 notes; 14 auditor paras; 184
entities; 7 zero_standing; signature blocks) was read verbatim at its cited line before
judging. Notes/auditor pages are OCR-garbled at source; legible text quoted, illegibility
flagged (not guessed).

---

## FINDINGS TABLE

| id | check | ledger row ref | line | short verbatim quote | classification | forward implication |
|---|---|---|---|---|---|---|
| A3-01 | F1 | Std/Cons Exceptional items (ZERO_STANDING); Note 9/12 | 432-434, 522-523 | "Exceptional items, net gain … -" (Q1FY27) vs "The share transfer was completed on April 16, 2026" (Rs 1,000.00m) | AMBIGUOUS | A Rs 1,000m subsidiary sale COMPLETED within Q1FY27 (16-Apr-2026) yet exceptional items = dash both S and C. Gain/loss either nil (book-value transfer) or routed through Other income (std +141.71 vs 67.89 PY). Ask mgmt where the disposal result landed. |
| A3-02 | F2 | Std L16 vs Cons L18 (PAT) | 442, 902 | std "(902.88)" vs cons "(2,344.02)" | FORWARD-SIGNAL | S-vs-C loss gap = Rs 1,441m in Q1FY27 (160% of standalone loss) vs 87% in Q1FY26 and 305% in Q4FY26 — swing far exceeds 5pp trigger. Consolidated loss increasingly rests on subsidiary losses; standalone is a near-dormant holdco (revenue 129.45 < employee cost 439.87). |
| A3-03 | F4 | Cons auditor Other Matters 5a/5b/5c + reliance (OTHER_AUDITOR_RELIANCE, UNAUDITED_MGMT_FURNISHED) | 606-624 | "total revenue of Rs. 1,645.39 million, total net profit/(loss) after tax of Rs. (627.36) million … reviewed by other auditors" / "furnished to us by the management" | FORWARD-SIGNAL | Rs 1,645.39m = 75.9% of consolidated revenue (2,167.54) and the (627.36)m loss = 26.8% of consolidated loss rest on entities NOT reviewed by the principal auditor (reports furnished by management, reliance sole). Well above 10% PAT trigger. SOUTHWEST-style: consolidated loss leans on other-auditor / mgmt-furnished numbers. No prior extract to trend. |
| A3-04 | F6 | Notes 7,11,12; Agenda B,C,D; AGM commitment | 69-70, 124-126, 513-515, 1028-1031 | "in the process of obtaining"; "voluntarily committed to exercise and convert all the Warrants within a period not exceeding 6 (six) months"; "shall be circulated to the shareholders" | FORWARD-SIGNAL | Multiple dated/dateable commitments: warrant conversion within 6m of allotment; NCLT amalgamation hearings 14-Aug-2026 (Mumbai) & 27-Aug-2026 (Delhi); AGM notice pending; SMP effective 1-Oct-2026. Feed Role 5 promise-vs-delivery tracker. See Commitment Register. |
| A3-05 | F7 | Cons Note 9 EEBPL/KIADB (LEGAL_CONTINGENCY); Agenda B | 1007-1009, 43-44 | "no coercive action shall be taken, continues to remain in force, and EEBPL continues to hold and retain possession of the Land pending fresh consideration of the matter on merits" | AMBIGUOUS | Consolidated-only note; land possession (Whitefield/KIADB) NOT resolved — Division Bench set aside the favourable order 15-Jun-2026, merits still open. Pre-emptive legal cover; possession could still be lost. Warrant/appointments carry procedural "subject to shareholder approval." Ask: quantum of EEBPL land at risk and carrying value. |
| A3-06 | F8 | Std L13-15 / Cons L13-15 (tax) | 438-440, 895-896 | "Current tax ( Including earlier year taxes)"; total tax charge "7.17" on pre-tax loss "(895.71)" | AMBIGUOUS | (a) Net tax CHARGE booked on pre-tax LOSSES both S (7.17) and C (2.89) in Q1FY27 — no DTA shield on current losses at parent (deferred tax flips to a 16.99 charge std). (b) Consolidated deferred tax persistently a CREDIT (Q1FY27 (9.04), Q4FY26 (221.02), FY26 (341.95)) building DTA on mounting losses — recoverability question if losses persist. (c) Earlier-year taxes bundled into current-tax line, non-zero, not isolable. |
| A3-07 | F9 | Cons OCI FX translation (OCR_GARBLED) | 907 | "Exchange difference in translation of foreign operations … [Q1FY27 value illegible]" | NEUTRAL-FACT | Actuarial (remeasurement) OCI is nil/dash this quarter — no swing to flag. BUT the Q1FY27 foreign-operations translation OCI value is OCR-garbled at source and cannot be confirmed (3 of 4 periods legible). Data gap; verify at Annual Report / source PDF, do not infer. |
| A3-08 | F10 | Std L20/21/22, Note 5, Agenda B (CAPITAL_RAISE) | 451, 454-455, 39, 487-491 | paid-up "2,730 50" (Q1FY26) -> "2,780 07"; EPS Basic "(0 65)" = Diluted "(0 65)"; "3,25,18,900 unlisted warrants" | FORWARD-SIGNAL | Basic=Diluted EPS (options/warrants anti-dilutive in loss year) masks a large overhang: 3,25,18,900 promoter warrants + 1,46,99,601 options + 48,04,041 PSUs outstanding. Paid-up rose 2,730.50->2,780.07 during FY26 (corporate action not explained in this filing's notes). Warrant conversion lifts promoter group 42.65%->43.96%. |
| A3-09 | F11 | Std L23 / Cons L30 Other equity (ZERO_STANDING) | 457, 923 | std other equity blank in quarter cols, FY26 "1,10,223.45"; cons FY26 "96,859.81" | NEUTRAL-FACT | Q1FY27 net worth cannot be tied out (other equity reported only at FY-end per format; blank all quarters). Consolidated reserves (96,859.81) sit Rs 13,363.64m BELOW standalone (110,223.45) at FY26 — accumulated subsidiary losses eroding consol net worth. Rs 362.62 Cr warrant money is a future credit to equity. No third-party (rating) number in context to reconcile the 5% test. |
| A3-10 | F13 | Agenda B/C/D + AGM (CAPITAL_RAISE, RELATED_PARTY) | 34-36, 96-98, 102-105 | "the Board has approved a fund raise … for repayment of shareholder debt"; "Mr. Neel Virwani, a member of the Promoter Group, as senior management personnel … w.e.f. October 1, 2026" | FORWARD-SIGNAL | Board outcome carries a capital-raising enabling resolution (Rs 362.62 Cr warrants to promoter, to AGM) AND induction of the Chairman's son / MD's brother (age 27) into senior management. Stated use "repayment of shareholder debt" = promoter converting related-party debt exposure into fresh promoter equity. Funding-round + succession signals; no AR/MD&A approval flagged (no imminent AR-drop event). |
| A3-11 | F14 | Std Note 5 vs Cons Note 5; std vs cons auditor sig; Cons Note 11 | 487, 953, 397, 645, 1021 | std "Employee Stock Option Scheme - 2015 (' ESOS 202j")" vs cons "Scheme - 2025"; "Membership No.: 09784" vs "097848"; "Equinox India Infraestate Limited (Transferee Company), a subsidiary of the Transferee Company" | NEUTRAL-FACT | Cumulative drafting/control inconsistencies: ESOS scheme year 2015 vs 2025 across S/C notes; auditor membership no. truncated 09784 vs 097848 (UDIN confirms 097848); self-referential entity description in the amalgamation note. Individually immaterial, together a governance/controls data point. |
| A3-12 | F15 | Entity #152; Note 7/8 strike-offs; Note 11 amalgamation; Note 9/12 SPA (ENTITY_CHANGE, SUBSEQUENT_EVENT, PENDING_APPROVAL) | 823-824, 518-520, 1021-1031, 522-523 | "Dev Property Development Limited (struck off on 26 May 2026)"; "strike off of three non-operational subsidiaries … one foreign subsidiary … struck off"; "Scheme of Amalgamation … for the merger of Spero Properties" | FORWARD-SIGNAL | In-period entity churn: #152 struck off 26-May-2026; 3 non-operational + 1 foreign subsidiary struck off in-quarter; one UNNAMED subsidiary sold via SPA (Rs 1,000m, completed 16-Apr-2026); Spero Properties (#160) pending amalgamation into Equinox India Infraestate (#26), NCLT hearings 14/27-Aug-2026. 184-entity list is baseline for next-quarter diff (no prior ledger supplied). Ask mgmt to name the sold subsidiary. |

---

## CHECKLIST SCORECARD (all 17)

| Check | Status | Basis (one line) |
|---|---|---|
| F1 | FINDING | Exceptional-items line zero in Q1FY27 despite Rs 1,000m subsidiary sale completing in-quarter (Note 9/12); disposal result location unexplained. |
| F2 | FINDING | S-vs-C loss gap swings 87% -> 305% -> 160% of standalone PAT across periods (>5pp); consolidated loss leans on subsidiary losses; parent near-dormant. |
| F3 | PASS | Cost lines differ materially S vs C (employee 439.87 vs 772.65; land cost 187.63 vs 2,054.65) — subsidiaries operate, not shells; dormant SPVs being struck off; no going-concern EoM present. |
| F4 | FINDING | 75.9% of consolidated revenue and 26.8% of consolidated loss rest on other-auditor / mgmt-furnished entities (Rs 1,645.39m / (627.36)m); >10% trigger. |
| F5 | PASS | No going-concern paragraph or EoM in either review report; both conclusions unmodified; Other Matters para is other-auditor reliance only, not a going-concern flag. No prior extract to diff. |
| F6 | FINDING | Multiple dated commitments mined (warrant 6-month conversion; NCLT hearings 14/27-Aug-2026; AGM notice; SMP w.e.f. 1-Oct-2026). See Commitment Register. |
| F7 | FINDING | Live legal hedge on EEBPL/KIADB land possession ("pending fresh consideration on merits") after Division Bench set aside favourable order 15-Jun-2026. |
| F8 | FINDING | Net tax charge on pre-tax losses (S & C) Q1FY27; persistent consolidated deferred-tax credits building DTA on losses; earlier-year taxes bundled, non-zero. |
| F9 | FINDING | Actuarial OCI nil this quarter (no swing), but Q1FY27 foreign-translation OCI value OCR-garbled/illegible — data gap flagged, not inferred. |
| F10 | FINDING | Basic=Diluted EPS masks 3.25cr warrants + 1.47cr options + 0.48cr PSUs overhang; paid-up rose 2,730.50->2,780.07 in FY26 (corporate action unexplained here). |
| F11 | FINDING | Q1FY27 net worth un-tie-outable (other equity blank in quarter cols); consolidated reserves Rs 13,363.64m below standalone at FY26 (subsidiary loss erosion). |
| F12 | PASS | Single reportable business segment / single geography per Note 4; no segment asset/liability split disclosed to trend. |
| F13 | FINDING | Board outcome carries capital-raise enabling resolution (Rs 362.62 Cr promoter warrants, repaying shareholder debt) + promoter-family SMP induction, both to AGM. |
| F14 | FINDING | ESOS year 2015 vs 2025 across S/C; auditor membership 09784 vs 097848; self-referential Transferee-Company description — cumulative controls signal. |
| F15 | FINDING | In-period entity changes: #152 struck off; 3+1 strike-offs; unnamed subsidiary sold (Rs 1,000m); Spero amalgamation pending NCLT. 184 = next-quarter baseline. |
| F16 | N.A. | Presentation-specific check; this is a results filing, not a deck. |
| F17 | N.A. | Concall-specific silence audit; no transcript in this doctype. |

Blank checks: none. GATE A3: PASS (all 17 marked exactly one status).

---

## COMMITMENT REGISTER (from F6)

| commitment | implied date | note/ref | status word |
|---|---|---|---|
| Preferential issue of 3,25,18,900 warrants up to INR 362.62 Cr to Embassy Property Developments Pvt Ltd (promoter group) | ensuing AGM approval | Agenda B / L34-44 | board-approved, pending shareholder |
| Promoter to exercise & convert ALL warrants within 6 months of allotment (vs 18m ICDR max) | <=6m post-allotment | Agenda B / L69-70, 205-206 | voluntarily committed |
| Appointment of Neel Virwani as SMP | w.e.f. 1-Oct-2026 (subject to AGM) | Agenda C / L96-98 | board-approved, pending shareholder |
| Re-appointment of Jitendra Virwani (Chairman, retires by rotation) | ensuing AGM | Agenda D / L102-105 | recommended |
| AGM notice circulation & exchange intimation | within prescribed timelines | L124-126 | pending |
| Rs 10,200m NCDs issued; Rs 9,200m applied to debt repayment | post Q1FY27 (subsequent event) | Note 7/6 / L513-515, 960-962 | completed |
| Scheme of Amalgamation (Spero -> Equinox India Infraestate); NCLT final hearings | 14-Aug-2026 (Mumbai), 27-Aug-2026 (Delhi) | Note 11 / L1028-1031 | underway ("in the process of obtaining") |
| SPA sale of subsidiary shares (Rs 1,000m) | completed 16-Apr-2026 | Note 9/12 / L522-523, 1033-1034 | completed |
| Strike-off of 3 non-operational + 1 foreign subsidiary | during Q1FY27 | Note 8/7 / L518-520, 966-968 | completed |

---

## CLASSIFICATION SUMMARY (for A4)
- FORWARD-SIGNAL: A3-02 (F2), A3-03 (F4), A3-04 (F6), A3-08 (F10), A3-10 (F13), A3-12 (F15)
- AMBIGUOUS -> A4 management questions: A3-01 (F1), A3-05 (F7), A3-06 (F8)
- NEUTRAL-FACT: A3-07 (F9), A3-09 (F11), A3-11 (F14)
- CONFIRMATORY-NEGATIVE: none isolated (no prior-quarter extract; deferred to next quarter's diff)

## MONITORING-CHECKLIST TIE-INS (pass-through, memory to weigh)
- Cost of debt: NCD Rs 10,200m at face Rs 0.10m each; coupon not stated in filing (verify vs 11% thesis note) — Note 7. Warrant raise Rs 362.62 Cr confirmed.
- Standalone vs consolidated PAT gap (SOUTHWEST test): CONFIRMED material and widening — A3-02 + A3-03 (76% of consol revenue on other-auditor/mgmt-furnished numbers).
- Legal contingencies: STPL CIRP dismissed/no longer under CIRP (Note 6/8); EEBPL/KIADB land possession unresolved (A3-05); Nashik SEZ not addressed in filing.
- Interest coverage / EBITDA margin: standalone finance cost 224.27 vs revenue 129.45 (uncovered); consolidated finance cost 1,185.68 — coverage remains deeply negative; verify against Red <1.2x tripwire.
- Promoter encumbrance/pledge: NOT disclosed in this filing (verify separately; warrant raise lifts promoter holding 42.65%->43.96%).
