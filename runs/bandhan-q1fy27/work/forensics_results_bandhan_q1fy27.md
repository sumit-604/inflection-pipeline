# A3 FORENSIC NOTES — BANDHAN Q1FY27 — Doctype: results (Reg 30 Board Outcome + Reg 33 Unaudited Financials, standalone-only + Limited Review Report + Press Release)

Source extract: extract_results_bandhan_q1fy27.txt (735 lines, 13 pages).
Ledger: ledger_results_bandhan_q1fy27.md. Reconciliation: 100% — all 112 line
items, 16 notes, 4 agenda items, 6 auditor paras, 1 entity, and all 18
ZERO_STANDING rows read verbatim at their cited lines before judging.

Unit convention (per A1 header, carried into every calc below): Reg 33 tables
pages 4-8 in **Lakhs** (x0.01 -> Cr); Press Release pages 11-13 already in
**Rs crore**. UNIT_MIX respected; no double-conversion.

Doctype scope: this is a STANDALONE-only filing (Note 14, line 527: "The Bank
does not have any Subsidiary, Associate or Joint venture"). Consequently the
consolidation-family checks (F2 S-vs-C, F3 shell, F4 unaudited component
contribution, F15 entity-list diff) are N.A. and stated as such with the line
that makes them N.A. F16/F17 are N.A. by doctype (results, not deck/concall).

---

## FINDINGS TABLE

| id | check | ledger row ref | line | verbatim quote | classification | forward implication |
|----|-------|----------------|------|----------------|----------------|---------------------|
| F1-1 | F1 | §5 6(iii), lines 397-401 (ZERO_STANDING SR line) | 401 / 397-400 | "Investment made in Security Receipts (SR's) ... -" ; "Excess provisions reversed to Profit and Loss Account ... 535.98" | NEUTRAL-FACT | ARC sale was full-cash (sale consideration 11,948.98 > NBV 11,413.00 lakh), zero SRs retained = no residual SR risk carried forward; but Rs 5.36 Cr excess-provision write-back lifted Q1 P&L non-recurringly. |
| F6-1 | F6 | §1 items 1-4, lines 41-118 | 60, 67-78, 96-98, 111, 115-117 | "shall re-open 48 hours after this declaration"; "has approved the appointment of Mr. Vi nay Jain, as the (Interim) CFO ... effective September 26, 2026, till March 31, 2027"; "extension ... up to September 30, 2026"; "12th AGM ... will be held on Monday, August 24, 2026"; "Record Date ... fixed as Monday, August 17, 2026" | FORWARD-SIGNAL | Dense dated-commitment cluster: CFO handover 25/26-Sep, CIV interim to 30-Sep, AGM 24-Aug, dividend record date 17-Aug. Feeds Role 5 promise tracker + FTTCP timeline. |
| F7-1 | F7 | §2 Note 10, lines 495-503 | 503 / 499-501 | "The Bank continues to monitor the notification and implementation of rules by the Government under the Labour Codes." | FORWARD-SIGNAL | Pre-emptive hedge on a live cost line: Rs 6,082.72 lakh (Rs 60.83 Cr) additional gratuity already booked to Employee Cost in Q1; rules not yet finalised => further employee-cost accretion is signalled for coming quarters. |
| F11-1 | F11 | §2 Note 8, lines 434-439 | 438 | "the Bank has transferred z 21,567.42 lakhs from the Investment Fluctuation Reserve (IFR) to Balance in Profit and Loss Account" | FORWARD-SIGNAL | Rs 215.67 Cr reserve release supports CRAR/distributable reserves; yet CRAR still fell 114 bps YoY (19.08% -> 18.15%, line 215). Capital is being consumed faster than headline shows; ties to monitoring item #3 (25-Jun-26 Capital Plan). |
| F12-1 | F12 | §4 row 2c, line 263 | 263 | "Wholesale Banking (7,711.03)" | FORWARD-SIGNAL | AS-17 Wholesale Banking segment PBT = **Rs -77.11 Cr** Q1FY27 vs Rs -42.20 Cr Q1FY26 (loss widened ~83% YoY); FY26 full-year -Rs 237.96 Cr. Annualises to ~Rs 308 Cr against TRIPWIRE #2 (>Rs 400 Cr FY27). Not breached, but trajectory is toward it. |
| F12-2 | F12 | §4 row 3c, line 271 | 271 | "Wholesale Banking 42,09,080.59 ... 29,79,835.27" | FORWARD-SIGNAL | Wholesale segment assets +41% YoY (Rs 29,798 Cr -> Rs 42,091 Cr) inside a structurally loss-making segment = RWA/capital consumption with no segment profit; external funding / capital-raise pressure ahead. |
| F12-3 | F12 | §4 row 4c, line 279 | 279 | "Wholesale Banking 6,66,537.89 ... 8,18,337.13" | AMBIGUOUS | Wholesale segment liabilities fell Rs 8,18,337 -> Rs 6,66,538 lakh (-18.5% QoQ) while wholesale assets rose => funding gap now carried by other segments' deposits/equity. WC-unwind vs deliberate deleverage unclear -> A4 concall question. |
| F13-1 | F13 | §1 item 2, lines 63-78 | 64-67, 78 | "resignation of Mr. Rajeev Mantri ... last working day being September 25, 2026 ... appointment of Mr. Vi nay Jain, as the (Interim) CFO" | FORWARD-SIGNAL | Monitoring item #1 (replacement CFO) only PARTIALLY met: interim, fixed short term to 31-Mar-2027, no permanent CFO. 2nd CFO in 3 years / 5th CXO exit in 24 months (Notion). Governance instability persists. |
| F13-2 | F13 | §1 item 3, lines 92-98 | 96-98 | "extension of the term of appointment of Mr. Prakash E as the CIV ... on an interim basis, up to September 30, 2026 or till the date new CIV joins" | AMBIGUOUS | Chief of Internal Vigilance still interim ~8 months (since 24-Feb-26), no permanent vigilance head at a bank with prior asset-quality history -> controls-continuity question for A4. |
| F13-3 | F13 | §1 item 4, lines 109-118 | 111, 115-116 | "12th AGM ... August 24, 2026"; "Record Date for the purpose of Dividend ... August 17, 2026" | FORWARD-SIGNAL | AGM + dividend record date => full Annual Report drops within weeks (schedule Role 6 AR Deep Dive) and dividend / special resolutions incoming. |
| F14-1 | F14 | §2 Note 1 (line 334) vs §8 Para 5 (line 614) | 336-337 vs 614-616 | Note 1: "for the quarter ended June 30, 2025 were **reviewed** by the then ... joint statutory auditors"; Auditor Para 5: "corresponding quarter ended June 30, 2025 were **jointly audited** ... issued an **unmodified opinion**" | AMBIGUOUS | Note-vs-auditor drafting inconsistency (review vs audit) on the comparative period; compounded by AUDITOR_CHANGE (Singhi & Co. -> V. Singhi & Associates) and EOM_UNLABELED (paras 5-6 function as Other Matters, unheaded). Individually immaterial, cumulatively a governance data point -> A4 clarification. |

---

## TRIPWIRE & MONITORING RECONCILIATION (per task message)

ACTIVE TRIPWIRES:
1. Credit cost >2.5% two consecutive quarters FY27 — **NOT touched.** Provisions
   (other than tax) Q1FY27 = 68,258.61 lakh (Rs 682.59 Cr; press release line 691
   "Rs.683 crore, lower 40% YoY"). Annualised on advances Rs 1,55,555 Cr =
   ~1.76%. Q1FY26 provisions were Rs 1,146.9 Cr; sharp YoY relief. PASS.
2. Wholesale segment loss >Rs 400 Cr FY27 — **TOUCHED (monitoring).** Q1 = Rs
   -77.11 Cr (line 263), annualises ~Rs 308 Cr; loss widened YoY. See F12-1.
3. Fresh RBI / forensic action — **NOT touched.** No enforcement/forensic item in
   this filing. (CIV still interim, F13-2, but no external action disclosed.)
4. CASA <27% — **NOT touched.** CASA ratio "above 29%" (line 663), CASA Rs 48,479
   Cr (+15.8% YoY, line 718). ~2 pts of headroom only; watch.

MONITORING CHECKLIST:
1. Replacement CFO announcement — **advanced, partial** (interim only; F13-1).
2. Q1 FY27 full results — **delivered** (this filing; PAT Rs 502 Cr, +35% YoY).
3. 25-Jun-26 Capital Plan board outcome — not in this filing; CRAR -114 bps YoY
   and IFR release (F11-1) make the Capital Plan retrieval more urgent.
4. Axis Bank disclosure on Mantri — external, absent here (F17 N.A. for results).

AS-17 Wholesale Banking segment PBT (explicitly requested): **Rs -77.11 Cr**
(line 263, (7,711.03) lakh), captured as F12-1.

---

## CHECKLIST SCORECARD (all 17, exactly one status each)

| Check | Status | One-line basis |
|-------|--------|----------------|
| F1 ZERO-VALUE STANDING | FINDING | All 18 ZERO_STANDING rows read; template-anticipation lines confirm no exceptional/extraordinary items (lines 192, 202) and no project-finance resolution stress (9 nil PF rows). SR-investment nil (line 401) + full-cash ARC sale surfaced as F1-1. |
| F2 STANDALONE vs CONSOLIDATED | N.A. | No consolidated results; Note 14 (line 527) — no subsidiary/associate/JV. Nothing to decompose. |
| F3 SHELL-ENTITY DETECTION | N.A. | No subsidiaries to test for shells (Note 14, line 527). |
| F4 UNAUDITED CONTRIBUTION RATIO | N.A. | Single-entity bank; no JV/associate/component-auditor reliance in the review report (paras 1-6, lines 561-624). Zero unaudited PAT contribution. |
| F5 GOING CONCERN / EoM SCOPE | PASS | GOING_CONCERN_ABSENT is standard for a bank limited-review; no operational EoM, no new entity/amount. Unlabeled paras 5-6 concern comparatives not operations (routed to F14). No prior extract supplied, so no verbatim regression possible; nothing new operational to flag. |
| F6 FORWARD-COMMITMENT MINING | FINDING | Dated commitment cluster (CFO effective 26-Sep, CIV to 30-Sep, AGM 24-Aug, dividend record date 17-Aug, trading window reopen +48h). See F6-1 and Commitment Register. |
| F7 HEDGE PHRASE MINING | FINDING | Note 10 "continues to monitor" Labour Codes (line 503) = pre-emptive cost hedge with a live gratuity accrual. F7-1. |
| F8 TAX FORENSICS | PASS | ETR Q1FY27 = 17,384.88/67,551.75 = 25.7% ~ statutory 25.17%; Q4FY26 30.1%, Q1FY26 28.7%, FY26 29.4%. No "tax adjustments relating to earlier years" line; Reg 33 bank format carries no deferred-tax split. Nothing anomalous. |
| F9 OCI FORENSICS | N.A. | AS-based bank filing (AS 25 interim); no OCI / actuarial-through-OCI line item. Gratuity flows through Employee Cost (P&L), not OCI (Note 10). |
| F10 SHARE COUNT & DILUTION | PASS | Paid-up 1,61,107.80 lakh Q1FY27 vs 1,61,097.23 Q4FY26; +10.57 lakh reconciles exactly to Note 4 ESOP allotment of 1,05,686 shares (line 350-351). Basic-vs-diluted EPS spread <=1 paisa (3.11/3.11; 3.32/3.31) — immaterial. |
| F11 RESERVES & NET WORTH | FINDING | Net worth ties within ~1.3% (paid-up + reserves 25,25,632 lakh vs segment capital+reserves 25,57,490 lakh FY26, reconciler = ESOP-outstanding). The IFR->P&L transfer of Rs 215.67 Cr (Note 8, line 438) is a non-recurring reserve release supporting CRAR while CRAR still fell 114 bps YoY. F11-1. |
| F12 SEGMENT FORENSICS | FINDING | Wholesale segment loss Rs -77.11 Cr and widening (F12-1); wholesale assets +41% YoY in a loss segment (F12-2); wholesale liabilities -18.5% QoQ (F12-3); Other Banking Ops assets grow with zero liabilities (line 280, equity-funded, minor). |
| F13 BOARD OUTCOME BEYOND RESULTS | FINDING | Interim CFO / 2nd CFO in 3 yrs (F13-1); interim CIV extended (F13-2); AGM + dividend record date => AR imminent (F13-3). |
| F14 NOTE DRAFTING INCONSISTENCIES | FINDING | Note 1 says Q1FY26 "reviewed"; auditor Para 5 says "jointly audited"/"unmodified opinion" — review-vs-audit inconsistency; plus AUDITOR_CHANGE name shift and EOM_UNLABELED. F14-1. |
| F15 ENTITY LIST DIFFS | N.A. | Single standalone entity (entities count = 1, Note 14 line 527); no consolidation list to diff. |
| F16 PRESENTATION-SPECIFIC | N.A. | Doctype = results; Earnings Update Presentation submitted separately (line 55), not in this extract. |
| F17 CONCALL SILENCE AUDIT | N.A. | Doctype = results; no transcript in this extract. |

Blank checks: none. GATE A3 = pass.

---

## COMMITMENT REGISTER (from F6)

| commitment | implied date | note/turn ref | status word |
|------------|--------------|---------------|-------------|
| Trading window reopens ~48h after results declaration | ~23-Jul-2026 | line 60 | scheduled |
| Rajeev Mantri (CFO/KMP) last working day | 25-Sep-2026 | line 66 | approved/pending |
| Vinay Jain interim CFO & KMP effective, term to 31-Mar-2027 | 26-Sep-2026 | line 67-78 | board-approved |
| Prakash E interim CIV term extended | to 30-Sep-2026 | line 96-98 | board-approved |
| New (permanent) CIV to join ("till the date new CIV joins") | open | line 97 | underway/unfilled |
| 12th AGM via VC/OAVM | 24-Aug-2026 | line 111 | scheduled |
| Dividend record date fixed | 17-Aug-2026 | line 115-116 | fixed |
| Dividend, if declared at AGM, paid within 30 days | <=23-Sep-2026 (contingent) | line 116-118 | contingent |
| Earnings Update Presentation "being submitted separately" | on/around 21-Jul-2026 | line 55 | underway |
| IFR-to-P&L transfer Rs 215.67 Cr executed (CRAR) | done (Q1FY27) | line 438 | completed |
| Additional gratuity liability recognised under Labour Codes | done Q1 (Rs 60.83 Cr); ongoing monitoring | line 500-503 | underway |

---

## RECONCILIATION STATEMENT
All A2 ledger flags addressed: 18 ZERO_STANDING (F1 + F12), AUDITOR_CHANGE
(F14-1), UNIT_MIX (respected throughout), EOM_UNLABELED (F14-1),
GOING_CONCERN_ABSENT (F5, benign for a bank review), KMP_CHANGE (F13-1),
INCOMPLETE_DISCLOSURE rows (RoA/NNPA blanks — extraction-artifact per ledger
§3 note, no forensic content), UNREVIEWED_DISCLOSURE (Pillar 3/LCR, Note 5 /
Para 1 — carve-out is standard, no PAT impact). ledger_reconciled_pct = 100.
