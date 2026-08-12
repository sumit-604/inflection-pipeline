# A3 FORENSIC NOTES — KRN Heat Exchanger and Refrigeration Limited — Q1 FY27 — doctype: RESULTS

Source spine: `runs/krn-q1fy27/work/extract_results_krn_q1fy27.txt` (unit = Lakhs; Rs Cr = Lakhs x0.01).
Ledger contract: `runs/krn-q1fy27/work/ledger_results_krn_q1fy27.md` (A2). Notion context weighed, not anchored.

**Ledger reconciliation: 100%.** Every A2 row read at its cited line in the A1 extract before judging:
all 63 P&L line items (C, D), 51 ZERO_STANDING rows, 36 segment rows (H1, I1), 22 export-country rows
(H2, I2), 18 notes (E, G), 16 auditor-para elements (J, K), 3 agenda items (A), 2 entities (L), 8
annexure sub-rows (M1, M2), 5 signature blocks (B). No unread row. All four A2 `FIGURE_MISMATCH`
flags, `UNAUDITED_SUBSIDIARY_RELIANCE`, `INCOMPLETE_SIGNATURE` x2, and `HEADER_MISCOUNT` carried
forward and dispositioned below.

> **A5 loop-1 update (GATE A5):** F14 now enumerates **four** discrete drafting-control instances.
> The fourth — standalone segment-note pre-exceptional FY26 (9,191.08, L564) vs standalone P&L
> pre-exceptional FY26 (9,111.66, L434), a 79.42-Lakh / Rs 0.79 Cr gap — is A2's fourth
> `FIGURE_MISMATCH`; previously folded into F14 prose, now a distinct sub-finding. No other finding changed.

---

## FINDINGS TABLE

| id | check | ledger row ref | line(s) | verbatim quote | classification | forward implication |
|----|-------|----------------|---------|----------------|----------------|---------------------|
| **F1** | F1 | C-5 / D-5, FY26 col | 122, 425 (FY26 21,165.88) | "Purchase of Stock-in-trade … 921.46 … 3,375.03 … 21,165.88" | AMBIGUOUS | Trading line blank in Q1FY26, Rs 211.66 Cr in FY26, still live Q1FY27. Standalone Rs 33.75 Cr **exceeds** consol Rs 9.21 Cr → Rs 24.54 Cr is intra-group (parent buying its own subsidiary's output to on-sell). Nature unexplained = open governance Q2. |
| **F2** | F2 | C-1/D-1, C-19/D-19, C-26 | 117, 420, 139, 442, 150 | "a) Owner of the company 3,289.56" vs standalone "Profit for the period 1,866.84" | FORWARD-SIGNAL | S-vs-C revenue gap swung from **−11.2%** (Q4FY26: consol 17,947.98 < SA 20,206.18) to **+38.7%** (Q1FY27: 25,231.70 vs 18,197.15). Subsidiary PAT swung from **−326** lakhs (Q1FY26 loss) to **+1,422.72** (43.2% of group PAT). Neemrana subsidiary is now the profit engine and is beginning to book external revenue. Swing >>5pp. |
| **F4** | F4 | LRR Other Matters | 382–388 | "2 subsidiaries, whose unaudited interim financial results reflect total income of ₹ 16,718.73 Lakhs, total profit after tax of ₹ 1,422.72 Lakhs" | FORWARD-SIGNAL | **43.2%** of consolidated PAT (1,422.72 / 3,289.56) and 65.5% of group total income rest on numbers **not reviewed** by the principal auditor — management-furnished. YoY jump from negative contribution to 43% = separate finding. |
| **F6** | F6 | F2/F5 footnote (note 8) | 234–236, 524–526 | "remaining amount is oP: 14,317.77 Lakhs is unutilized and parked in FDs and Bonds" | FORWARD-SIGNAL | Company-level QIP table reads "Nil" unutilized, but at subsidiary level **Rs 143.18 Cr of Rs 235.26 Cr is undeployed**, parked in FDs/Bonds. Future working-capital / capex deployment pending; masks a large idle balance behind a "Nil" company-level line. |
| **F8** | F8 | C-17 / D-17, C-16/D-16 | 137, 440, 136, 439 | "Income Tax (Short/Excess provision) … 302.65" (consol) vs "(302.65)" (standalone) | AMBIGUOUS | Non-zero prior-year tax adjustment (Rs 3.03 Cr) → F8 trigger. **Sign flips** consol +302.65 vs standalone (302.65). Q1FY27 consol ETR 22.29% vs statutory 25.17% (~288bps shield). Standalone runs **persistent deferred-tax credits** (Q1FY27 (4.23), FY26 (58.90)) = DTA/carryforward, future ETR step-up risk. |
| **F9** | F9 | C-20 | 142 | "Remeasurements of defined benefit plans … 19.18" | AMBIGUOUS | Single-quarter consol OCI remeasurement **+19.18** exceeds the full prior year FY26 (−14.26) and flips sign → actuarial-assumption change (discount rate / plan assets). Immaterial in Rs (Rs 0.19 Cr); verify assumptions at Annual Report. |
| **F12** | F12 | H1-13..18, H1-7 | 285–291, 275, 561, 571–577 | "Segment Liabilities Overseas 10,851.33 … Segment Asset Overseas 8,102.18" (Overseas result row blank) | AMBIGUOUS | Consol overseas segment carries **liabilities (10,851.33) > assets (8,102.18)** — net negative position; and "Segment Results — Overseas" is **blank in every period**. Overseas profitability is never disclosed while overseas revenue is Rs 52–99 Cr. Concall question on overseas margin + the liability overhang. |
| **F13** | F13 | Agenda 2 & 3 / M1, M2 | 53–64, 667, 699 | "Appointment of M/s. R S Chauhan & Associates … Cost Auditor" / "M/s. Sharma Shankar & Co. … Internal Auditor" | AMBIGUOUS | **Both** cost auditor and internal auditor appointed in the **same** 29-minute meeting (15:30–15:59, line 79–80), Reg 30 field reads "appointment" not "reappointment". No AR approval / AGM notice / dividend / director / capital-raise item (absent by sweep, line 74–76). Verify whether predecessors were replaced — relevant to the MONITOR promoter verdict. |
| **F14** | F14 | C-19 vs C-26/C-32; C-13/D-13; C-17/D-17; I1-10 vs D-12 | 139 vs 150/160; 132 vs 435; 137 vs 440; **564 vs 434** | "Profit for the period (Vil-VIII) 3,269.56" vs "a) Owner of the company 3,289.56"; **"Profit/(loss) Before Exceptional Items & Tax … 9,191.08" (segment) vs "Profit Before Prior Period and Exceptional Item … 9,111.66" (P&L)** | CONFIRMATORY-NEGATIVE | **Four** discrete drafting-control instances (see scorecard). Cumulatively a control-weakness pattern; individually the PAT typo alone is decision-relevant (understates headline consol PAT), the fourth (Rs 0.79 Cr segment-vs-P&L) is immaterial in rupees but a genuine flagged instance. |

---

## F14 SUB-FINDING ENUMERATION (four instances)

| # | instance | line cites | magnitude | note |
|---|----------|-----------|-----------|------|
| F14-1 | Consol "Profit for the period" 3,269.56 vs "Owner of the company" / "Net Profit after Tax & NCI" 3,289.56 | 139 vs 150 & 160 | Rs 0.20 Cr (20 Lakh) | **Keying typo**: PBT 4,233.08 − tax 943.52 = 3,289.56, and EPS 5.20 × 632.57L wtd shares = 3,289.56 — both prove 3,289.56 is correct and line 139 understates. Decision-relevant (headline PAT). |
| F14-2 | Prior Period / Exceptional Item FY26: consol **+39.71** vs standalone **(39.71)** | 132 (& seg 279) vs 435 (& seg 565) | Rs 0.40 Cr (39.71 Lakh), sign | Sign inconsistency across statements for the same-nature item. |
| F14-3 | Income Tax (Short/Excess provision) FY26: consol **302.65** vs standalone **(302.65)** | 137 vs 440 | Rs 3.03 Cr (302.65 Lakh), sign | Presentation sign flip (both function as credits); overlaps F8. |
| F14-4 | Standalone **segment-note** pre-exceptional FY26 **9,191.08** vs standalone **P&L** pre-exceptional FY26 **9,111.66** | **564 vs 434** | **Rs 0.79 Cr (79.42 Lakh)** | Segment note overstates pre-exceptional profit by 79.42 (= 2×39.71), i.e. double-counts the 39.71 exceptional relative to the P&L; both still reconcile down to PBT 9,151.37 (L566 = L436). **Immaterial in rupees but a genuine flagged drafting-control instance** — this is A2's fourth `FIGURE_MISMATCH`, now dispositioned. |

---

## CHECKLIST SCORECARD (all 17; exactly one status each)

| # | status | basis |
|---|--------|-------|
| F1 | **FINDING** | ZERO_STANDING "Purchase of Stock-in-trade" (122/425) blank Q1FY26 → Rs 211.66 Cr FY26 → still live Q1FY27; standalone > consol proves intra-group trading. Other zero-standing rows benign (NCI blank = wholly owned; exceptional-item line 132 template; investor-complaints Nil; quarterly Other Equity/segment-BS undisclosed = standard). |
| F2 | **FINDING** | S-vs-C gap decomposed every period; revenue gap swings −11.2%→+38.7%, PAT gap −20.8%→+76.2% of standalone PAT — both far exceed the 5pp threshold. |
| F3 | **PASS** | Not shells: consol vs standalone cost lines diverge materially — CoM 16,441 vs 11,162, Employee 1,819 vs 446, Depn 646.76 vs 71.84. Subsidiary (Neemrana plant) has real workforce and fixed assets. No going-concern EoM on any entity. |
| F4 | **FINDING** | Rs 14,22.72 lakhs (43.2% of consol PAT) unaudited/management-furnished (382–388); YoY jump from a loss = second leg. Above 10% trigger. |
| F5 | **PASS** | No Emphasis-of-Matter and no Going-Concern paragraph in either LRR (consol 344–354; standalone 617–625) — absent by sweep. Consistent with Notion's prior-quarter "UNMODIFIED, no EoM." No prior extract supplied for verbatim diff; nothing to track. |
| F6 | **FINDING** | Forward-commitment mining: QIP "completed" (213), IPO proceeds "fully utilised" (210), and the live commitment — Rs 143.18 Cr QIP proceeds "unutilized and parked in FDs and Bonds" (234–236) pending deployment. Register below. |
| F7 | **PASS** | Hedge-lexicon sweep of both note blocks: only boilerplate — "subject to limited review" (193/486, factual) and the standing regroup/restate note (184/477). No **newly added** hedge on revenue lumpiness or customer concentration. |
| F8 | **FINDING** | Non-zero prior-year tax adjustment 302.65 (137/440) with consol/standalone sign flip; ETR shield ~288bps vs 25.17%; standalone persistent deferred-tax credits. |
| F9 | **FINDING** | Consol single-quarter OCI remeasurement 19.18 (142) exceeds full FY26 (14.26) with sign flip = assumption change; low materiality, flagged for AR verification. |
| F10 | **PASS** | Paid-up 6,215.66 → 6,545.85 (+330.19 lakhs = 33,01,900 sh) traces cleanly to the QIP 33,01,886-share allotment (216). Basic = Diluted in both statements (5.20; 2.95) — no dilutive-instrument spread. |
| F11 | **PASS** | FY26 net worth ties: consol Other Equity 51,183.82 + paid-up 6,215.66 = Rs 573.99 Cr; standalone 50,452.30 + 6,215.66 = Rs 566.68 Cr. Q1 Other Equity not disclosed (standard). No third-party net-worth figure inside the filing to reconcile against; no >5% gap detectable. |
| F12 | **FINDING** | Overseas segment liabilities (10,851.33) > assets (8,102.18); overseas segment result blank every period; quarterly segment BS not disclosed so accretion rate not trendable. |
| F13 | **FINDING** | Cost + internal auditor both freshly appointed same meeting; no AR/AGM/dividend/director/capital-raise item. Low severity, verify replacement vs reappointment. |
| F14 | **FINDING** | **Four** drafting-control instances (see enumeration table): F14-1 headline PAT keying typo (139 vs 150; arithmetic + EPS confirm 3,289.56); F14-2 prior-period-item sign flip (132 vs 435); F14-3 income-tax short/excess sign flip (137 vs 440); **F14-4 standalone segment-vs-P&L pre-exceptional FY26 gap of Rs 0.79 Cr (9,191.08 L564 vs 9,111.66 L434)**. Also duplicate/mislabelled OCI sub-heading (consol 141 & 144 both "will not be reclassified"). |
| F15 | **PASS** | Two subsidiaries — KRN HVAC Products Pvt Ltd, Thermotech Research Laboratory Pvt Ltd (367–368) — internally consistent with Notes 7/8 and the LRR entity list; all-blank NCI confirms both wholly owned. `NO_PRIOR_LEDGER`: add/delete/rename diff not runnable this cycle; carried as a limitation. |
| F16 | **N.A.** | Doctype = results filing, not a presentation. No slides, baselines, or order-book definitions to diff. |
| F17 | **N.A.** | Doctype = results filing, not a transcript. Silence audit deferred to the concall document; monitorables tested where the filing permits are noted below for A4. |

No blank checks. GATE A3 = pass.

---

## COMMITMENT REGISTER (F6)

| commitment | implied date | note/ref | status word |
|------------|--------------|----------|-------------|
| QIP of 33,01,886 sh at Rs 1,060 (Rs 350 Cr gross) allotted | 01-Jun-2026 | Note 8, line 213–219 | completed |
| IPO net proceeds Rs 311.12 Cr fully utilised (Neemrana subsidiary plant + GCP) | as at 30-Jun-2026 | Note 7, line 208–210 | completed |
| QIP proceeds Rs 235.26 Cr into subsidiary WC — **only Rs 92.08 Cr utilised; Rs 143.18 Cr undeployed, parked in FDs/Bonds** | ongoing / undated | Note 8 footnote, line 234–236 | underway |
| Cost Auditor FY26-27 (R S Chauhan & Associates, FRN 003517) | FY 2026-27, appointed 12-Aug-2026 | Agenda 2 / M1, line 53–57, 667–672 | completed (board-approved) |
| Internal Auditor FY26-27 (Sharma Shankar & Co., FRN 019317C) | FY 2026-27, appointed 12-Aug-2026 | Agenda 3 / M2, line 59–64, 699–704 | completed (board-approved) |

---

## MONITORABLES TESTED WHERE THE FILING PERMITS (for A4; not a checklist verdict)

- **Revenue YoY**: consol Q1FY27 Rs 252.32 Cr vs Q1FY26 Rs 115.28 Cr = **+118.9%** (green >35%); standalone Rs 181.97 Cr vs Rs 114.40 Cr = **+59.1%** (green). Caveat: consol growth is inflated by the subsidiary ramp and intra-group trading (F1/F2).
- **Q1 revenue thresholds**: consol Rs 252.32 Cr clears bull (>=185); standalone Rs 181.97 Cr sits **between** bull (185) and bear (165) — flag which entity the threshold references (A4 to resolve).
- **Export mix**: consol overseas Rs 52.38 Cr / Rs 252.32 Cr = **20.8%** (green >10%); standalone 15.0%. Standalone exports (8 countries) are a strict subset of consol (14) — Brazil/Nepal/Netherlands/Norway/Sri Lanka/UK served only via the subsidiary.
- **CFO/PAT**: **not testable** — quarterly results carry no cash-flow statement. Silence to be logged at the concall/AR (SOFT-TRIM revenue leg partially green; cash leg undisclosed).
- **Data-centre / DC customer disclosure**: **absent** — segmentation is geographic only (India/Overseas); no product/customer segment, no DC mention. Notion 24-Jul-26 Rs 43.11 Cr subsidiary order not referenced in this filing.
- **Daikin / promoter share-sale / Purchase of Stock-in-trade Rs 211.66 Cr**: no new disclosure on Daikin or promoter sale; the stock-in-trade line persists (F1) with intra-group signature — carries governance Q2 forward.

---

## DISPOSITION OF A2 CARRY-FORWARD FLAGS

- `FIGURE_MISMATCH` (i) PAT 3,269.56 vs 3,289.56 → **resolved**: 3,289.56 is correct (PBT−tax and EPS both confirm); line 139 is a keying typo → F14-1.
- `FIGURE_MISMATCH` (ii) prior-period-item sign flip → F14-2.
- `FIGURE_MISMATCH` (iii) tax short/excess sign flip → F8 / F14-3.
- `FIGURE_MISMATCH` (iv) standalone segment pre-exceptional 9,191.08 (L564) vs P&L 9,111.66 (L434), Rs 0.79 Cr / 79.42 Lakh → **F14-4** (dispositioned per A5 loop-1; segment note double-counts the 39.71 exceptional; both reconcile to PBT 9,151.37). Immaterial in rupees, genuine drafting-control instance.
- `UNAUDITED_SUBSIDIARY_RELIANCE` → F4 (43.2% of PAT).
- `INCOMPLETE_SIGNATURE` x2 (458–459, 533–534): unnamed "For and on behalf of Board of Directors" blocks on both P&L pages — OCR/stamp-only, no extractable signatory. CS (88–94) and both auditor blocks (393–403, 637–647) are named with distinct UDINs; no UDIN reuse. Recorded as a NEUTRAL-FACT drafting/OCR gap, not escalated (named signatures exist elsewhere in the filing).
- `HEADER_MISCOUNT` (header 708 vs body 735): confirmed — page 13 content ends line 735; does not affect any line cite. NEUTRAL-FACT.
- `NO_PRIOR_LEDGER`: limits F5 verbatim EoM diff and F15 entity diff; both carried as stated limitations, not manufactured findings.

---

```yaml
stage: A3-forensics
company: "KRN"
quarter: "Q1 FY27"
doctype: "results"
model: claude-opus-4-8
status: complete
forensics_path: "runs/krn-q1fy27/work/forensics_krn_q1fy27.md"
ledger_reconciled_pct: 100
checklist:
  F1: FINDING
  F2: FINDING
  F3: PASS
  F4: FINDING
  F5: PASS
  F6: FINDING
  F7: PASS
  F8: FINDING
  F9: FINDING
  F10: PASS
  F11: PASS
  F12: FINDING
  F13: FINDING
  F14: FINDING
  F15: PASS
  F16: N.A.
  F17: N.A.
findings:
  - {id: "F1", check: "F1", line: "122,425,FY26 21165.88", classification: "AMBIGUOUS", implication: "Purchase of Stock-in-trade trading line emerged FY26 (Rs 211.66 Cr), persists Q1FY27; standalone > consol = intra-group; nature unexplained (governance Q2)"}
  - {id: "F2", check: "F2", line: "117,420,139,442,150", classification: "FORWARD-SIGNAL", implication: "S-vs-C revenue gap swung -11.2% to +38.7%; subsidiary PAT -326 to +1423 lakhs = 43% of group PAT; Neemrana subsidiary now profit engine"}
  - {id: "F4", check: "F4", line: "382-388", classification: "FORWARD-SIGNAL", implication: "43.2% of consolidated PAT unaudited/management-furnished; YoY jump from a loss"}
  - {id: "F6", check: "F6", line: "234-236", classification: "FORWARD-SIGNAL", implication: "Rs 143.18 Cr QIP proceeds undeployed, parked in FDs/Bonds behind a company-level Nil; future WC/capex deployment pending"}
  - {id: "F8", check: "F8", line: "137,440", classification: "AMBIGUOUS", implication: "Prior-year tax adj 302.65 non-zero with consol/standalone sign flip; ETR 22.3% vs 25.17% ~288bps; standalone persistent DT credits = future ETR step-up risk"}
  - {id: "F9", check: "F9", line: "142", classification: "AMBIGUOUS", implication: "Single-quarter OCI remeasurement 19.18 > full FY26 14.26 with sign flip = actuarial assumption change; verify at AR"}
  - {id: "F12", check: "F12", line: "285-291,275", classification: "AMBIGUOUS", implication: "Overseas segment liabilities > assets and overseas result never disclosed; concall Q on overseas profitability"}
  - {id: "F13", check: "F13", line: "53-64,667,699", classification: "AMBIGUOUS", implication: "Cost + internal auditor both freshly appointed same meeting; verify replacement vs reappointment; no AR/AGM/dividend item"}
  - {id: "F14", check: "F14", line: "139-vs-150; 132-vs-435; 137-vs-440; 564-vs-434", classification: "CONFIRMATORY-NEGATIVE", implication: "FOUR drafting-control instances: F14-1 headline PAT keying typo (true 3289.56 via PBT-tax and EPS, 20 Lakh); F14-2 prior-period-item sign flip (39.71); F14-3 income-tax short/excess sign flip (302.65); F14-4 standalone segment-vs-P&L pre-exceptional FY26 gap Rs 0.79 Cr (9191.08 L564 vs 9111.66 L434, 79.42 Lakh, immaterial but genuine). Instance count = four."}
forward_signals: ["F2", "F4", "F6"]
ambiguous: ["F1", "F8", "F9", "F12", "F13"]
commitments:
  - {commitment: "QIP 33,01,886 sh at Rs 1,060 (Rs 350 Cr) allotted", implied_date: "2026-06-01", ref: "note8/line213-219", status_word: "completed"}
  - {commitment: "IPO net proceeds Rs 311.12 Cr fully utilised (subsidiary plant + GCP)", implied_date: "2026-06-30", ref: "note7/line208-210", status_word: "completed"}
  - {commitment: "QIP Rs 235.26 Cr into subsidiary WC; Rs 143.18 Cr undeployed in FDs/Bonds", implied_date: "ongoing", ref: "note8-footnote/line234-236", status_word: "underway"}
  - {commitment: "Cost Auditor FY26-27 (R S Chauhan & Associates)", implied_date: "2026-08-12", ref: "agenda2/line53-57", status_word: "completed"}
  - {commitment: "Internal Auditor FY26-27 (Sharma Shankar & Co.)", implied_date: "2026-08-12", ref: "agenda3/line59-64", status_word: "completed"}
gate_a3: pass
blank_checks: []
```
