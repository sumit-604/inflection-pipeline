# A3 FORENSIC NOTES: ADOR (Ador Welding Limited), Q2 FY27, doctype: results

Quarter ended 30-Sep-2026. Board outcome and Reg 33 results dated 21-Oct-2026.
Units: INR lakhs (x0.01 = Rs Crore). Line numbers refer to
runs/ador-q2fy27/extracted/ador-results-q2fy27-fulltext.md. R### IDs refer to
runs/ador-q2fy27/extracted/ador-results-q2fy27-structured.md.

Read mode: PRE-THESIS READ. This is the first quarterly run for the ticker. No prior-quarter
extract exists. There is no Notion checklist, no companies/ADOR.md and no spear. Every
quarter-over-quarter diff (F5 EoM diff, F7 "newly added" hedge test, F15 entity diff, F4 trend)
is NOT TESTABLE. NOT TESTABLE does not mean clean.

Inputs read: A1 structured (R001-R900, all 900 rows), A1 fulltext (678 lines, all), A2 ledger
(all sections). The source PDF and inputs/ were not opened.

---

## 0. LEDGER RECONCILIATION

| Ledger section | Rows / IDs accounted | Read at cited line | Result |
|---|---|---|---|
| 1. Notes (S notes 1-9, C notes 1-10, sub-notes 3a/3b/4a) | R393-R442, R857-R900 | lines 307-347, 631-677 | reconciled |
| 2. Line items (6 statements + 4 exceptional-table lines) | R043-R392, R474-R856, R398/R399/R863/R864 | lines 125-157, 186-236, 249-304, 440-481, 506-556, 573-628, 314-316, 641-642 | reconciled; 2 A1 cell defects, see below |
| 2b. Table metadata | 21 IDs | lines 119-123, 159, 180-183, 244-247, 435-438, 482, 500-503, 567-571 | reconciled |
| 3. Agenda items | R001-R023 | lines 19-61 | reconciled |
| 4. Auditor paragraphs | R024-R038, R443-R470, plus 2 no-ID paras | lines 65-110, 360-426 (paras at 373 and 392 confirmed) | reconciled |
| 5. Entities | 26 ENTITY rows | as cited | reconciled |
| 6. Cross-references (RESTATED sets) | 7 sets | as cited | reconciled; all restated amounts identical S vs C |
| 7. Missing from structured | M01 (line 24, symbol ADOR) | line 24 | confirmed present in fulltext; low materiality |

ids_in_structured 900, ids read 900, orphans 0. ledger_reconciled_pct = 100.

A1 data defects found during the read (loop to A1; neither changes a finding below):
- R083 (standalone Employee benefits, H1 FY26) carries 5,130. A1's own verification note at
  line 169 says: "5,737 verified by arithmetic to total expenses 51,091". A3 arithmetic agrees:
  28,790 + 5,212 - 1,440 + X + 147 + 944 + 2,792 + 8,909 = 51,091 gives X = 5,737. The
  consolidated figure 5,825 (line 448) also fits 5,737 (gap 88), not 5,130 (gap 695).
- R272 (standalone current Lease liabilities, 30-Sep-2026) carries 15. A1 note at line 237 says
  "Current lease liabilities 75 / 64". The current-liabilities column casts to 22,668 (line 235)
  only with 75. The consolidated figure is 75 (line 547).
- A2 flag A1_VALUE_CHECK on R744 is stale. Structured R744 already carries 11,119
  [OCR_CORRECTED, image-verified]. The consolidated current-liabilities column casts with 11,119.
- R893 / R895 OCR_GLYPH (27.50 / 210): confirmed as rupee-glyph reads of 7.50 / 10 (line 678,
  line 41, line 336). No conflict on the dividend amount.

Statement tie-outs run by A3 (all PASS unless noted): standalone and consolidated P&L total
expenses for all six columns; both balance sheets (both dates); both cash flows (op and
investing); Other equity roll-forward (F11). Consolidated non-current assets at 30-Sep-2026 cast
to 26,755 against a printed 26,753 (line 517), a 2-lakh casting difference.

---

## 1. FINDINGS TABLE

| id | check | ledger row ref | line | short verbatim quote | classification | forward implication |
|---|---|---|---|---|---|---|
| A3-01 | F1 | R097-R103, R528-R534 | 136, 451 | "Onerous cost and Liquidated Damages (refer note 4)   -   -   -   -   2,792   2,482" | FORWARD-SIGNAL | The line stays in the template while the turnkey project is still open 15 months past target. A non-dash cell in a later quarter means a further overrun/LD charge, or a reversal on a variation order (FY26 shows a 310 reversal: 2,792 H1 less 2,482 FY). Nil for H1 FY27 despite continued delay: either the LD cap is reached or adequacy has not been retested. |
| A3-02 | F1 | R303/R304, R357/R358, R400-R402 | 255, 285, 319 | "Impairment of Intercorporate deposit (ICD)   64   -" | FORWARD-SIGNAL | A standing-dash line activated. The FY26 ICD impairment on 3DFT (556) was booked as "exceptional" (line 319-320). In H1 FY27 a further 64 impairment sits in ordinary P&L, against 68 of new ICD to the subsidiary (line 285). The parent is funding 3DFT's cash burn and writing it off about one-for-one. Expect a recurring ~64 per half while 3DFT operates. The "exceptional" label on the FY26 amount does not describe a recurring pattern. |
| A3-03 | F1 | R622-R627, R634-R639, R646-R651 | 470, 473, 476 | "Non-controlling interest   -   =   =   =   a   -" | NEUTRAL-FACT | All NCI lines are dash in every period. 3DFT is wholly owned (line 636). This is a template line. It anticipates a partly owned subsidiary that does not exist today. A first non-dash NCI cell means a dilution of 3DFT or a new non-wholly-owned entity. |
| A3-04 | F2 | R160-R165, R591-R596, R458/R459 | 147, 462, 409 | "total net profit / (loss) after tax (before consolidation adjustments) of Rs. (49) lakhs and Rs. (64) lakhs" | AMBIGUOUS | C-minus-S PAT moved from -110 (-4.96% of standalone PAT, H1 FY26) to +51 (+0.94%, H1 FY27): a 5.90 pp swing, over the 5 pp threshold. Consolidated PAT exceeds standalone although the only subsidiary lost (64) in H1. Implied consolidation adjustments are +115. Elimination of the parent's 64 ICD impairment (line 255) explains part. A residual of about +51 has no explanation in the filing. Small in rupees; it is a reconciliation question for management. |
| A3-05 | F3 | R079-R081 vs R510-R512; R043-R045 vs R474-R476; R453-R457 | 133, 448, 125, 440, 407-409 | "Employee benefits expenses   3,273   3,098   2,900" vs "Employee benefits expense   3272   3,068   2,860" | FORWARD-SIGNAL | 3DFT employee cost (C minus S) went 40 (Q2 FY26) to 30 (Q1 FY27) to 1 (Q2 FY27). 3DFT revenue (C minus S) went 109 (Q2 FY26) to 56 (Q2 FY27), down 49% YoY; H1 239 to 137. Subsidiary employee provisions (C minus S, lines 541/553) went 28 at Mar-26 to 0 at Sep-26. Total assets are 299 (line 407). 3DFT is moving to a shell. It is not a shell yet: it still books revenue. Watch for wind-down, sale, strike-off or a further impairment of the remaining ICD and investment. The LRR carries no going-concern language. The other auditor's report is not reproduced, so a going-concern note at 3DFT level is NOT TESTABLE. |
| A3-06 | F6 | R410, R411, R413, R419, R871, R875, R880 | 326, 649, 330 | "commenced a turnkey project targeted for completion by June 2025" | FORWARD-SIGNAL | The target date lapsed 15 months before quarter end and about 16 months before the filing. The note repeats the lapsed date. It gives no revised date and no completion statement: "remains committed to its successful execution". The division is "erstwhile" (Flares & Process Equipment), so a discontinued line still carries an open contract. Provisions on record: 1,293 overrun plus 1,499 potential LD, less a 310 VO reversal (lines 328-329). Questions for management: current percent complete, revised completion date, LD cap as a percent of contract value (NOT DISCLOSED), and residual provision against exposure. |
| A3-07 | F7 | R405-R409, R866-R870 | 322, 325, 648 | "clarifications from the Government on other aspects of Labour Code, if any and would provide appropriate accounting effect on the basis of such developments, as needed in future" | FORWARD-SIGNAL | The FY26 exceptional charge of 275 rests on "draft Central Rules and FAQs" (line 322) and an "internal assessment". The note keeps the door open for a further charge when final Central/State rules are notified. The exceptional line (lines 141, 456) is the line that would carry it. Standalone employee cost rose 14.4% YoY in Q2 (3,272 vs 2,860, line 133). Part of the recurring Labour Code cost may already sit in the run-rate. The filing does not split it. |
| A3-08 | F7 | R413, R414, R416, R877 | 326-328, 649-651 | "encountered certain delays due to a combination of operational and external challenges ... to mitigate potential impacts" | AMBIGUOUS | The LD amount is provisioned as "potential liquidated damages". It is not stated as levied or settled. Two outcomes: a reversal if the customer waives or reduces LDs (upside, as the 310 VO showed), or crystallisation above the 1,499 provision if delays extend. The filing gives no way to separate the two. The newness of the hedge is NOT TESTABLE (no prior quarter). |
| A3-09 | F8 | R226/R227 vs R694/R695; R148-R153 vs R579-R584; R154-R159 vs R585-R590 | 195, 515, 145, 460, 461 | "(h) Deferred tax assets (net)   1,887   1,912" vs "(h) Deferred tax assets (net)   919   983" | AMBIGUOUS | The consolidated DTA is 968 below standalone at Sep-26 (929 at Mar-26), about half. The gap widened by 39. This equals the excess of consolidated over standalone deferred tax in H1 FY27 (81 vs 42). FY26: consolidated deferred tax +7 vs standalone (446), a 453 gap, so the consolidated FY26 ETR is 28.71% vs 25.60% standalone (+311 bps) and +354 bps over the 25.17% statutory rate. 3DFT's total assets are 299, so the gap must come from consolidation adjustments. [INFERENCE] The parent carries a DTA on its 3DFT investment/ICD provisions, and consolidation reverses it. If so, about 968 of the standalone 1,887 DTA depends on the tax deductibility of a subsidiary loss (possibly a capital loss). Ask management. |
| A3-10 | F10 | R192-R205, R307/R308, R773/R774 | 156-157, 257, 580 | "Equity settled shared based payments   118" (H1 FY27) vs "3" (H1 FY26), image-verified line 305 | FORWARD-SIGNAL | Paid-up capital is flat at 1,740 (174 lakh shares) in every period. The standalone basic-diluted spread widened from 0.00 (Q2 FY26: 14.72 / 14.72) to 0.06 (Q2 FY27: 15.33 / 15.27). The ESOP charge rose about 39 times. New dilutive grants exist. Implied potential shares are about 0.7 lakh (about 0.4%). A4 cross-checks against the ESOP scheme terms. |
| A3-11 | F12 | R274-R277, R270/R271, R343/R344, R232/R233, R246/R247, R375 | 229-230, 226, 276, 199, 207, 295 | "Total outstanding dues to creditors other than micro and small enterprises   11,052   17,384" | AMBIGUOUS | Note 7 (line 335) gives one segment, so the entity balance sheet is the segment balance sheet. Non-MSME payables fell 6,332 (-36%). MSME dues rose 1,503 (+78%, 1,922 to 3,425). Short-term borrowings rose from 27 to 2,771. Operating cash flow was (750) against PBT 7,241 (H1 FY26: +4,243). Inventories rose 2,527 and other current assets rose 1,805. Meanwhile the company held 11,948 in cash, bank balances and current investments. It paid a 4,003 dividend (line 294), and a 1,305 special dividend falls due by 20-Nov-2026. Reading 1: a one-off reset of supplier terms. Reading 2: a structural working-capital step-up on 23% revenue growth. H2 payables days and operating cash flow separate the two. The MSME increase also matters for tax: dues unpaid past the statutory window lose deductibility (s.43B(h)). Ask management. |
| A3-12 | F13 | R015-R019, R432-R438, R893-R897 | 41-43, 336, 661 | "declared a special interim dividend of % 7.50 per equity share ... to commemorate the 75th anniversary" | NEUTRAL-FACT | The dividend is labelled commemorative and one-off. It is not a signal of payout policy. The cash out is about 1,305 (7.50 x 174 lakh shares): record date 30-Oct-2026, payment on or before 20-Nov-2026. The letter carries no AR, AGM, director, auditor, ESOP or capital-raise item, so no Role 6 event is triggered. |
| A3-13 | F14 | R015 vs R432; R398 vs R400; R359-R362 vs R823-R826; R039; R412; R429 | 41 vs 336; 314 vs 319; 286-287 vs 608-609; 119; 326; 334; 311; 517 | "Fixed deposits matured   2,163   -" / "Fixed deposits placed   (14)   831" | NEUTRAL-FACT | Cumulative drafting list. (1) Letter says "interim dividend" (line 41); notes say "special interim dividend" (lines 336, 661). (2) The exceptional table says "investment in and intercorporate deposit" (line 314); note 3a says impairment "on the inter-corporate deposit (ICD)" only (line 319). (3) The consolidated CF H1 FY26 comparative shows FD matured "-" and placed 831 as an inflow. The standalone CF shows matured 831 and placed "-" (lines 286-287). Labels are swapped. (4) Title typo "Quater" (line 119). (5) "the Company erstwhile (Flares & Process Equipment)" is garbled (line 326). (6) "Impaitment" typo (line 334). (7) The standalone exceptional table lacks the "Quarter ended" header (line 311). (8) Consolidated non-current assets have a 2-lakh casting gap (line 517). Each item is immaterial. Together they are a governance data point on filing care. |
| A3-14 | F14 | R321/R322 vs R787/R788; R053 vs R484; R054 vs R485 | 264, 587, 126, 441 | "Interest income   (444)   (498)" vs "Interest income   (445)   (418)" | AMBIGUOUS | In the H1 FY26 comparative, consolidated CF interest income (498) exceeds standalone (418) by 80. Consolidated P&L other income (928) is 82 below standalone (1,010). Both cannot hold if 3DFT earns no interest. A1 verified the 498 by arithmetic to the operating profit of 3,625. The comparative is internally consistent but conflicts with the P&L direction. The reliability of the consolidated comparative column is a question. FY26 other income C minus S is -148 (interest on the ICD eliminated). H1 FY27 is +1. [INFERENCE] The parent stopped accruing interest on the 3DFT ICD after the impairment. |

---

## 2. CHECK WORKINGS

### F2. Standalone vs consolidated decomposition (INR lakhs; C minus S)

| Period | Revenue S / C / gap | Other income gap | EBITDA pre-exceptional S / C / gap | PAT S / C / gap | Gap % of S PAT |
|---|---|---|---|---|---|
| Q2 FY27 | 34,420 / 34,474 / +54 | +1 | 3,717 / 3,772 / +55 | 2,668 / 2,694 / +26 | +0.97% |
| Q1 FY27 | 30,863 / 30,946 / +83 | 0 | 3,532 / 3,571 / +39 | 2,735 / 2,760 / +25 | +0.91% |
| Q2 FY26 | 28,000 / 28,109 / +109 | -41 | 3,492 / 3,475 / -17 | 2,562 / 2,501 / -61 | -2.38% |
| H1 FY27 | 65,283 / 65,420 / +137 | +1 | 7,249 / 7,343 / +94 | 5,403 / 5,454 / +51 | +0.94% |
| H1 FY26 | 53,054 / 53,293 / +239 | -82 | 3,054 / 3,035 / -19 | 2,216 / 2,106 / -110 | -4.96% |
| FY26 | 1,13,545 / 114,001 / +456 | -148 | 12,146 / 12,126 / -20 | 8,280 / 8,198 / -82 | -0.99% |

EBITDA = PBT before exceptional + finance costs + D&A - other income (lines 134-140, 449-455).

Decomposition: no JV or associate. One subsidiary, 3DFT. H1 FY27: the revenue gap of 137 equals 3DFT's
reported H1 revenue of 137 (line 409), so revenue eliminations are nil. 3DFT PAT is (64) (line 409).
The implied net consolidation adjustment is +115. The identifiable part is elimination of the
parent's ICD impairment of 64 (line 255). The residual of about +51 is unexplained. FY26: the
standalone exceptional item is (831), the consolidated one (275) (lines 141, 456). The 556 impairment
of the 3DFT investment/ICD is eliminated. The PBT gap is +371 and the tax gap -453. Swing test:
H1 FY26 to H1 FY27 is 5.90 pp (FINDING A3-04). Q2 FY26 to Q2 FY27 is 3.35 pp.

### F3. Shell test (C minus S cost lines, Q2 FY27 / Q1 FY27 / Q2 FY26)
- Cost of materials: +29 / +17 / +46. Not identical.
- Purchases of stock-in-trade and inventory change: identical in every period (lines 130-131 vs 445-446).
- Employee benefits: +1 / +30 / +40. Near-identical in Q2 FY27.
- Depreciation: +3 / +2 / +3. Near-identical.
- Other expenses: -31 / -3 / +40. Consolidated is below standalone in Q2 FY27, so eliminations exceed 3DFT's own costs.
Verdict: 3DFT is not yet a shell but trends to one (A3-05). The LRR has no Going Concern EoM to reconcile.

### F4. Unaudited contribution ratio
3DFT was reviewed by another auditor, not by BSR (line 414). H1 FY27 loss (64) = 1.17% of
consolidated PAT 5,454. Q2 loss (49) = 1.82% of 2,694. Revenue 137 = 0.21% of consolidated
revenue. Assets 299 = 0.36%. All below the 10% threshold. The YoY trend is NOT TESTABLE (no prior
LRR). The other auditor is unnamed (A2 flag UNREVIEWED_ENTITY, noted).

### F8. Tax
| Period | Standalone ETR | Consolidated ETR | Standalone deferred tax |
|---|---|---|---|
| Q2 FY27 | 25.58% (917/3,585) | 25.95% (944/3,638) | +42 charge |
| Q1 FY27 | 25.19% (921/3,656) | 25.26% (933/3,693) | nil |
| Q2 FY26 | 25.26% (866/3,428) | 25.72% (866/3,367) | (26) credit |
| H1 FY27 | 25.38% (1,838/7,241) | 25.60% (1,877/7,331) | +42 charge |
| H1 FY26 | 25.46% (757/2,973) | 26.44% (757/2,863) | (474) credit |
| FY26 | 25.60% (2,849/11,129) | 28.71% (3,302/11,500) | (446) credit |

Standalone ETR stays within 45 bps of the 25.17% statutory rate. The H1 FY26 deferred credit (474) is
1,594 bps of PBT. [INFERENCE] It is the DTA on the non-deductible onerous/LD provision of 2,792; the
current tax of 1,231 is 41% of PBT. The Q2 FY27 charge of +42 is the first sign of reversal as the
provision is used. This is ETR-neutral (current tax falls as the deferred charge rises). There is no
"tax adjustments relating to earlier years" line in any column. The DTA tie works: standalone DTA moved
-25 = P&L charge 42 less OCI credit 17. Consolidated DTA moved -64 = 81 less 17. FINDING A3-09 is
the S-vs-C DTA gap.

### F9. OCI
Standalone remeasurement: Q2 FY27 (69); Q1 nil; Q2 FY26 (109); FY26 (75). Consolidated: Q2 FY27 (69);
FY26 (69). The single quarter does not exceed the full prior year. The consolidated figure EQUALS it
((69) vs (69)), which is at the threshold, not over it. The Q1 dash in both statements points to
actuarial valuation at half-year and year-end only. At the AR, A4/Role 6 can verify the
discount-rate assumption because the H1 loss equals the full prior year.

### F11. Net worth tie-out
- Standalone: 1,740 + 56,113 = 57,853 (line 214). Mar-26: 1,740 + 54,647 = 56,387. Tie.
- Consolidated: 1,740 + 55,222 = 56,962 (line 534). Mar-26: 1,740 + 53,705 = 55,445. Tie.
- Other equity roll-forward, standalone: 54,647 + TCI 5,351 - dividend 4,003 + SBP 118 = 56,113. Exact.
- Other equity roll-forward, consolidated: 53,705 + 5,402 - 4,003 + 118 = 55,222. Exact.
- Revaluation reserve Nil (lines 154, 478). No third-party net-worth figure is in context to reconcile.

### F12. Segment
One segment, "Welding & Related Products and Services" (line 335). No segment asset/liability table
exists. The entity balance sheet stands in for the segment. FINDING A3-11.

### F15. Entity list
Consolidation list = Parent + 3DFT. The LRR says "Subsidiary" (line 391); note 3 says "wholly owned
subsidiary" (line 636); standalone note 3a says "wholly owned subsidiary" (line 319). Consistent
within the document. The prior-quarter diff is NOT TESTABLE.

---

## 3. CHECKLIST SCORECARD

| Check | Status | Basis |
|---|---|---|
| F1 | FINDING | 29 zero-standing items reviewed. Onerous/LD line anticipates turnkey charges or reversals (A3-01). ICD-impairment line activated (A3-02). NCI lines are template (A3-03). Other dashes (Q1 deferred tax/OCI, FD, FX, inventory write-off, borrowings) are timing or treasury lines with no forward content. |
| F2 | FINDING | H1 PAT gap swung 5.90 pp of standalone PAT. Consolidated PAT exceeds standalone despite a sub loss; residual about +51 unexplained (A3-04). |
| F3 | FINDING | 3DFT cost lines converge on standalone (employee +1 in Q2) and revenue is halving. Trending to shell (A3-05). No GC EoM. |
| F4 | PASS | Other-auditor component = 1.17% of H1 consolidated PAT, below 10%. Trend NOT TESTABLE. |
| F5 | PASS | No EoM or Going Concern paragraph in either LRR (lines 94, 392, 418: "not modified"). Prior-quarter verbatim diff NOT TESTABLE. |
| F6 | FINDING | Turnkey June 2025 target repeated after it lapsed, with no new date (A3-06). Register below. |
| F7 | FINDING | Labour Codes open-ended true-up hedge (A3-07). Turnkey "potential" LD hedge (A3-08). Newness NOT TESTABLE. |
| F8 | FINDING | Standalone ETR near statutory. Consolidated DTA 968 below standalone; FY26 consolidated ETR +311 bps over standalone (A3-09). No prior-year tax line. |
| F9 | PASS | Q2 FY27 OCI (69) does not exceed FY26 ((75) standalone, (69) consolidated, equal). At threshold; verify assumptions at the AR. |
| F10 | FINDING | Paid-up flat at 1,740. Diluted spread widened 0.00 to 0.06; ESOP charge 118 vs 3 (A3-10). |
| F11 | PASS | Paid-up + other equity = total equity, both statements and dates. Roll-forward exact. No third-party figure in context. |
| F12 | FINDING | Single segment; entity BS as proxy. Payables down 36%, short-term debt up to 2,771, op CF negative (A3-11). |
| F13 | FINDING | Special commemorative interim dividend 7.50, record 30-Oct-2026, pay by 20-Nov-2026. No AR/AGM/director items (A3-12). |
| F14 | FINDING | Eight drafting items (A3-13) and a consolidated CF comparative that conflicts with the P&L (A3-14). LRR "limited review" matches note 1; no audit/review mismatch. |
| F15 | PASS | Parent + 3DFT, relationship consistent across LRR and notes. Prior diff NOT TESTABLE. |
| F16 | N.A. | Results filing; presentation-only check. |
| F17 | N.A. | Results filing; concall-only check. No Notion checklist exists. |

---

## 4. COMMITMENT REGISTER (F6)

| commitment | implied date | note / line ref | status word |
|---|---|---|---|
| Special interim dividend Rs 7.50 per share paid; record date 30-Oct-2026 | on or before 20-Nov-2026 | letter item c, lines 41-43; S note 8 line 336; C note 10 line 661 | initiated (declared) |
| Results uploaded to website; extract published in newspapers | after 21-Oct-2026, undated | lines 38-39 | initiated |
| Turnkey project (erstwhile Flares & Process Equipment) completion | June 2025 (LAPSED; no revised date) | S note 4 line 326; C note 5 line 649 | underway (delayed) |
| Pursue measures to optimise project overrun costs and delivery timelines | undated | S note 4 line 330; C note 5 line 653 | underway |
| Monitor final Labour Code Central/State Rules; book accounting effect "as needed in future" | undated (on final notification) | S note 3b line 325; C note 4a line 648 | initiated |
| BIS compounding 3,643 and court fine 34 | historic (order 15-Jun-2023) | S note 5 lines 331-332; C note 6 lines 654-655 | completed |
| Kuwait receivable recovery 1,412 "as final settlement" | historic (FY26) | S note 6 line 333; C note 7 line 656 | completed |

---

## 5. FOR A4 (management questions to draft)

FORWARD-SIGNAL: A3-01, A3-02, A3-05, A3-06, A3-07, A3-10.
AMBIGUOUS: A3-04, A3-08, A3-09, A3-11, A3-14.

```yaml
stage: A3-forensics
company: "ADOR"
quarter: "Q2 FY27"
doctype: "results"
model: "claude-opus-5-5"
status: complete
forensics_path: "runs/ador-q2fy27/work/forensics_ador_q2fy27_results.md"
ledger_reconciled_pct: 100
checklist:
  F1: FINDING
  F2: FINDING
  F3: FINDING
  F4: PASS
  F5: PASS
  F6: FINDING
  F7: FINDING
  F8: FINDING
  F9: PASS
  F10: FINDING
  F11: PASS
  F12: FINDING
  F13: FINDING
  F14: FINDING
  F15: PASS
  F16: N.A.
  F17: N.A.
findings:
  - {id: "A3-01", check: "F1", line: "136, 451", classification: "FORWARD-SIGNAL", implication: "Onerous/LD line kept while turnkey project is open 15 months past target; nil in H1 FY27 means LD cap reached or adequacy untested; next non-dash = further charge or VO reversal"}
  - {id: "A3-02", check: "F1", line: "255, 285, 319", classification: "FORWARD-SIGNAL", implication: "ICD impairment line activated: 64 impaired vs 68 new ICD to 3DFT in H1 FY27, in ordinary P&L; FY26 556 'exceptional' recurs at ~64 per half while 3DFT burns cash"}
  - {id: "A3-03", check: "F1", line: "470, 473, 476", classification: "NEUTRAL-FACT", implication: "NCI lines all dash; 3DFT wholly owned; first non-dash = dilution or new partly owned entity"}
  - {id: "A3-04", check: "F2", line: "147, 462, 409", classification: "AMBIGUOUS", implication: "C-S PAT gap swung -4.96% to +0.94% of standalone PAT (5.90 pp); consolidated PAT above standalone despite sub loss (64); implied adjustments +115, ICD impairment elimination 64, residual ~+51 unexplained"}
  - {id: "A3-05", check: "F3", line: "133, 448, 125, 440, 407-409", classification: "FORWARD-SIGNAL", implication: "3DFT employee cost 40 -> 30 -> 1, revenue 109 -> 56 YoY, employee provisions 28 -> 0; trending to shell; watch wind-down, sale, strike-off or further impairment; sub-level GC NOT TESTABLE"}
  - {id: "A3-06", check: "F6", line: "326, 649, 330", classification: "FORWARD-SIGNAL", implication: "Turnkey target June 2025 repeated ~16 months after lapse with no revised date; provisions 1,293 + 1,499 less 310 VO; ask percent complete, new date, LD cap, residual provision"}
  - {id: "A3-07", check: "F7", line: "322, 325, 648", classification: "FORWARD-SIGNAL", implication: "FY26 Labour Codes charge 275 rests on draft rules; note reserves a further accounting effect on final Central/State rules; exceptional line is the carrier"}
  - {id: "A3-08", check: "F7", line: "326-328, 649-651", classification: "AMBIGUOUS", implication: "LD provisioned as 'potential'; outcome is reversal (upside) or crystallisation above 1,499; filing gives no separator"}
  - {id: "A3-09", check: "F8", line: "195, 515, 145, 460, 461", classification: "AMBIGUOUS", implication: "Consolidated DTA 919 vs standalone 1,887 (gap 968, widened 39 = excess consolidated deferred tax H1); FY26 consolidated ETR 28.71% vs 25.60% standalone; about 968 of standalone DTA may depend on deductibility of 3DFT losses"}
  - {id: "A3-10", check: "F10", line: "156-157, 257, 580", classification: "FORWARD-SIGNAL", implication: "Paid-up flat 1,740; basic-diluted spread 0.00 -> 0.06; ESOP charge 118 vs 3; new grants, ~0.4% potential dilution; A4 cross-checks scheme"}
  - {id: "A3-11", check: "F12", line: "229-230, 226, 276, 199, 207, 295", classification: "AMBIGUOUS", implication: "Non-MSME payables -6,332 (-36%), MSME +1,503 (+78%), short-term debt 27 -> 2,771, op CF (750) vs PBT 7,241, while 11,948 treasury held and 4,003 + 1,305 dividends paid/due; one-off terms reset vs structural WC step-up; H2 op CF separates; s.43B(h) watch on MSME"}
  - {id: "A3-12", check: "F13", line: "41-43, 336, 661", classification: "NEUTRAL-FACT", implication: "Special commemorative interim dividend 7.50 (~1,305 cash), record 30-Oct-2026, pay by 20-Nov-2026; not a payout-policy signal; no AR/AGM/director items"}
  - {id: "A3-13", check: "F14", line: "41 vs 336; 314 vs 319; 286-287 vs 608-609; 119; 311; 326; 334; 517", classification: "NEUTRAL-FACT", implication: "Eight drafting inconsistencies (dividend label, ICD vs investment, swapped FD labels, typos, missing header, 2-lakh casting gap); cumulative governance data point"}
  - {id: "A3-14", check: "F14", line: "264, 587, 126, 441", classification: "AMBIGUOUS", implication: "H1 FY26 consolidated CF interest income 498 exceeds standalone 418 while consolidated other income is 82 below standalone; reliability of consolidated comparative column in question"}
forward_signals: ["A3-01", "A3-02", "A3-05", "A3-06", "A3-07", "A3-10"]
ambiguous: ["A3-04", "A3-08", "A3-09", "A3-11", "A3-14"]
commitments:
  - {commitment: "Special interim dividend Rs 7.50 per share, record date 30-Oct-2026", implied_date: "on or before 20-Nov-2026", ref: "lines 41-43, 336, 661", status_word: "initiated"}
  - {commitment: "Results uploaded to website and extract published in newspapers", implied_date: "undated, after 21-Oct-2026", ref: "lines 38-39", status_word: "initiated"}
  - {commitment: "Turnkey project (erstwhile Flares & Process Equipment) completion", implied_date: "June 2025 (lapsed; no revised date)", ref: "S note 4 line 326; C note 5 line 649", status_word: "underway"}
  - {commitment: "Optimise project overrun costs and delivery timelines", implied_date: "undated", ref: "S note 4 line 330; C note 5 line 653", status_word: "underway"}
  - {commitment: "Monitor final Labour Code rules; accounting effect as needed in future", implied_date: "undated (on final notification)", ref: "S note 3b line 325; C note 4a line 648", status_word: "initiated"}
  - {commitment: "BIS compounding 3,643 and court fine 34 paid", implied_date: "historic (order 15-Jun-2023)", ref: "S note 5 lines 331-332; C note 6 lines 654-655", status_word: "completed"}
  - {commitment: "Kuwait receivable recovery 1,412 as final settlement", implied_date: "historic (FY26)", ref: "S note 6 line 333; C note 7 line 656", status_word: "completed"}
gate_a3: pass
blank_checks: []
analyst_note: "Pre-thesis read. There is no prior quarter, so the F5, F15, F4-trend and F7-newness diffs are NOT TESTABLE, not clean. Two signals matter. First, cash: H1 PBT of 7,241 converted to operating cash of (750) because non-MSME payables fell 6,332. The company drew 2,700 of short-term debt while it held about 11,948 in cash, bank balances and current investments. It paid a 4,003 dividend, and 1,305 more is due. Reading one is a one-off reset of supplier terms. Reading two is a structural working-capital step-up from 23% revenue growth. H2 payables and operating cash flow separate them. Second, the turnkey note repeats a June 2025 target about 16 months after it lapsed, with no new date, and the onerous line is nil. So either the LD cap is reached or provision adequacy has not been retested. 3DFT is small (0.2% of revenue) but trends to a shell funded by parent ICDs that the parent impairs. A residual of about 51 in the consolidation and a 968 DTA gap need a management answer. A1 cell defects: R083 should read 5,737 and R272 should read 75, per A1's own notes. Neither changes a finding."
```
