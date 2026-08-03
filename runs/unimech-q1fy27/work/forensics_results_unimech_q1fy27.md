# A3 FORENSIC NOTES — UNIMECH Q1 FY27 (Doctype: RESULTS, Reg 33 primary filing)

Company: Unimech Aerospace and Manufacturing Limited (UNIMECH)
Quarter: Q1 FY27 (quarter ended June 30, 2026)
Source extract: `extract_results_unimech_q1fy27.txt` (655 lines, 11 pages)
Ledger: `ledger_results_unimech_q1fy27.md` — 100% of rows read at cited lines (21 notes, 75 line items, 3 zero_standing, 4 agenda, 11 auditor paras, 6 entities, 3 annexure, 3 signatures).
Unit convention: INR lakhs (x0.01 = Rs Cr).
Prior-quarter filing: NONE (fresh company; no companies/UNIMECH.md, no Notion page). Prior-period comparisons use the filing's own Q4 FY26 / Q1 FY26 / FY26 columns. F5 and F17 marked N.A. where a true prior-quarter artifact would be required.

Reading convention below: figures quoted as Q1FY27 / Q4FY26 / Q1FY26 / FY26.

---

## FINDINGS TABLE

| id | check | ledger row ref | line | short verbatim quote | classification | forward implication |
|----|-------|----------------|------|----------------------|----------------|---------------------|
| FND-01 | F1 | §5 zero_standing 1-3; §8b para 7 | 439-441 | "financial results of subsidiary which are not subject to review, whose financial results reflect total revenue of Rs. Nil, total net profit/(loss) after tax of Rs. Nil" | FORWARD-SIGNAL | A freshly consolidated subsidiary (implicates Uniflux Renewable Energy, incorporated Apr 27 2026, green-energy EPC) is pre-revenue at quarter-end. The Nil template line anticipates future revenue/PAT accretion once it and the Hobel units scale; the management-furnished carve-out will grow with them. |
| FND-02 | F2 | §3 rows 207/208/233; §4 rows 487/488/514 | 207,208,233 / 487,488,514 | standalone "Revenue from operations 459.06" vs consolidated "10,762.04"; standalone "Other income 978.32" vs consolidated "732.85" | AMBIGUOUS | Standalone is now ~4.3% of consolidated revenue and ~7.9% of consolidated PAT; standalone operating revenue FELL YoY (1,170.55 -> 459.06, -61%) while consolidated ROSE (6,298.85 -> 10,762.04, +71%). Standalone other income (978.32) exceeds both standalone revenue AND consolidated other income (732.85), so standalone PAT is propped by >=245 lakh of intra-group income that eliminates on consolidation. Direction of the parent-level revenue collapse is unexplained -> A4 question. |
| FND-04 | F6 | §6 items 2-4; §1 notes 5-10; §2 notes 6-11 | 50,64,80,281-302,584-605 | "the Board has approved to raise further capital ... aggregate consideration not exceeding 750,00,00,000"; "acquisition was completed on April 27, 2026"; AR "will be submitted to exchanges as soon as ... sent to the Shareholders" | FORWARD-SIGNAL | Dense dated/dateable commitment set: Rs 750 Cr QIP (AGM approval Aug 28 2026), Rs 5 Cr Dheya top-up, Rs 45,000 lakh Hobel acquisition already CLOSED, Uniflux incorporated, IPO proceeds fully deployed. Feeds Role 5 promise-vs-delivery tracker and FTTCP catalyst timeline. See Commitment Register. |
| FND-05 | F8 | §3 rows 228/229/230; §4 rows 506/507/508 | 228,229,230 / 506,507,508 | standalone "Deferred tax (credit)/charge (293.53)"; "Adjustments for current tax of prior period ... 43.42" (FY26) | AMBIGUOUS | Large deferred-tax CREDITS in 3 of 4 periods (Q1FY27 -293.53 std / -299.98 consol) shield the ETR; standalone current tax 373.41 EXCEEDS standalone PBT 300.03 (124%), fully offset by the deferred credit — persistent DTA/timing reversal implies future ETR step-up. Non-zero prior-period tax adjustments booked (std 43.42 / consol 35.52 in FY26; -4.49 both in Q4FY26) = per-F8 FINDING trigger. |
| FND-06 | F10 | §4 row 547; §1 note 7; §6 item 2 | 290,547,296 | "compulsorily convertible debentures (CCDs)"; consolidated "Diluted (INR) 5.47" vs Basic "5.48"; "raise funds aggregating up to INR 75,000 lakhs through a Qualified Institutions Placement" | FORWARD-SIGNAL | Paid-up capital unchanged (2,542.84 all periods) but a three-way forward dilution pipeline exists: existing basic-vs-diluted spread (ESOP-type instruments), CCDs issued in the Hobel consideration (compulsory future equity), and an approved Rs 750 Cr QIP. Share count is set to rise; model dilution before per-share targets. |
| FND-07 | F13 | §6 items 2,3,4 | 50,64,80,87 | "Subject to the approval of the Shareholders at the ensuing Annual General Meeting ... QIP"; "10th Annual General Meeting ... August 28, 2026"; "Annual Report for the financial year 2025-26 will be submitted to exchanges" | FORWARD-SIGNAL | Board outcome beyond the results carries (a) a capital-raising ENABLING resolution (Rs 750 Cr QIP special resolution at AGM) = funding round imminent; (b) Dheya further-investment approval; (c) AGM Aug 28 2026 + full FY2025-26 Annual Report dropping within weeks -> schedule a Role 6 AR Deep Dive event. |
| FND-08 | F14 | §4 rows 521,531,534; §3 row 239 | 239,521,531,534 | consolidated index "11" printed twice (line 531 "Other comprehensive loss ... attributable to" and line 534 "Total comprehensive income attributable to"); OCI "Income tax effect on above item (0.90) / 0.31 / 1.37 / (1.52)" identical in standalone AND consolidated | AMBIGUOUS | The OCI income-tax-effect row is byte-identical across standalone (remeasurement gain 3.57) and consolidated (remeasurement loss -8.36) despite different actuarial bases — the consolidated tax effect on subsidiary plans appears not separately computed. Plus a duplicated line index "11" (source numbering defect) and entity-name drift (Inc./Inc, Co./Co, "Private Limited"/"limited"). Individually immaterial, cumulatively a governance/close-process data point -> A4 question on the OCI tax effect. |
| FND-09 | F15 | §9 entities 3,4,5; §1 notes 6,7; §2 notes 7,8 | 391,394,398,569-571,284,287,587,590 | "*w.e.f. April 27, 2026"; "total investment of INR 45,000 lakhs ... structured through a combination of equity, debt, and compulsorily convertible debentures" | FORWARD-SIGNAL | Three entities added to consolidation this quarter, all effective Apr 27 2026: Uniflux Renewable Energy (new incorporation, green-energy EPC), Hobel Bellows Private Limited (step-down of Innomech) and Hobel Bellows Co. (step-down of Hobel Bellows Pvt). First-ever NCI appears (line 530, -0.05). Rs 45,000 lakh acquisition adds debt + CCDs to the balance sheet; integration, leverage and NCI trajectory are the new watch items. |

---

## CHECKLIST SCORECARD (all 17; PASS / FINDING / N.A.)

| Check | Status | One-line basis |
|-------|--------|----------------|
| F1 ZERO-VALUE STANDING | FINDING | Auditor para 7 (l.439-441): unreviewed subsidiary revenue/PAT/TCI all Rs Nil — pre-revenue freshly consolidated entity (Uniflux implicated). FND-01. |
| F2 STANDALONE vs CONSOLIDATED | FINDING | S-vs-C PAT gap widened from ~116% of standalone PAT (Q1FY26) to ~1,165% (Q1FY27); standalone revenue -61% YoY while consolidated +71%; standalone other income > consolidated other income. FND-02. |
| F3 SHELL-ENTITY DETECTION | PASS | Cost lines differ materially standalone vs consolidated (materials 108.08 vs 2,694.74; employees 377.71 vs 1,624.65) — operating subsidiaries are real, not shells. The single Nil subsidiary is a fresh Apr-27 incorporation (pre-revenue), not a balance-sheet-cleanup shell; no going-concern EoM anywhere. |
| F4 UNAUDITED CONTRIBUTION RATIO | PASS | Other Matters: associate net loss Rs 13.80 lakh relies on OTHER auditor (l.416); subsidiary Nil is management-furnished (l.439). Truly management-unaudited PAT = Nil (0%); other-auditor reliance = 13.80/2,786.36 = 0.5% of consolidated PAT. Well below the 10% trigger. |
| F5 GOING CONCERN / EoM SCOPE | N.A. | No going-concern or Emphasis-of-Matter paragraph in either report (standalone clean; consolidated has two Other Matters, neither an EoM). No prior-quarter filing to verbatim-diff against — a true QoQ EoM diff is not possible for this fresh company. |
| F6 FORWARD-COMMITMENT MINING | FINDING | Lexicon hits at l.52/53/78/81/88/288/290/296/300/590/653: QIP, Dheya top-up, Hobel "completed", AGM, AR filing, IPO utilisation. See Commitment Register. FND-04. |
| F7 HEDGE PHRASE MINING | PASS | Only "subject to" hits (l.52 QIP shareholder approval; l.72 Dheya "such terms and conditions as may be mutually agreed"; l.439 auditor "not subject to review") — all transaction/approval conditionality, boilerplate. No NEW hedge about revenue lumpiness or customer concentration inside the notes. |
| F8 TAX FORENSICS | FINDING | Persistent deferred-tax credits (Q1FY27 -293.53 std / -299.98 consol) shield ETR; standalone current tax 373.41 > standalone PBT 300.03; non-zero prior-period tax adjustments in FY26 (43.42 std / 35.52 consol) and Q4FY26 (-4.49). FND-05. |
| F9 OCI FORENSICS | PASS | Remeasurement swings within bounds: consolidated Q1FY27 -8.36 does NOT exceed full FY26 -41.60; standalone Q1FY27 +3.57 within FY26 +6.05. No single-quarter swing exceeding prior year = no evident assumption change. (Standalone/consolidated sign divergence and the identical tax-effect row are captured under F14.) |
| F10 SHARE COUNT AND DILUTION | FINDING | Paid-up flat at 2,542.84 (508.57 lakh shares, FV Rs 5), but basic-vs-diluted spread present (consol 5.48 vs 5.47) alongside CCDs (l.290) and an approved Rs 750 Cr QIP (l.296) = material forward dilution pipeline. FND-06. |
| F11 RESERVES / NET WORTH TIE-OUT | PASS | Other equity + paid-up ties internally: standalone FY26 52,565.56 + 2,542.84 = 55,108.40 lakh (Rs 551.08 Cr); consolidated 71,196.17 + 2,542.84 = 73,739.01 lakh (Rs 737.39 Cr). Other-equity populated only at FY-end (ANNUAL_ONLY_LINE); no third-party number (rating/slide) in this filing to reconcile against. |
| F12 SEGMENT FORENSICS | N.A. | Single reportable segment per Ind AS 108 (std note 2 l.273; consol note 3 l.575) — no segment asset/liability or segment revenue/results tables disclosed, so no segment trend to run. |
| F13 BOARD OUTCOME BEYOND RESULTS | FINDING | Agenda items 2-4 (l.50/64/80): QIP enabling resolution (Rs 750 Cr), Dheya further investment (Rs 5 Cr), 10th AGM Aug 28 2026 + FY2025-26 Annual Report incoming -> Role 6 AR Deep Dive. FND-07. |
| F14 NOTE DRAFTING INCONSISTENCIES | FINDING | Duplicated consolidated line index "11" (l.531 and l.534); OCI income-tax-effect row identical across standalone and consolidated despite different remeasurement bases (l.239 vs l.521); entity-name drift (Inc./Inc, Co./Co, "Private Limited"/"limited"). FND-08. |
| F15 ENTITY LIST DIFFS | FINDING | Three additions to consolidation w.e.f. Apr 27 2026: Uniflux Renewable Energy (new incorporation), Hobel Bellows Private Limited and Hobel Bellows Co. (acquired, Rs 45,000 lakh, equity/debt/CCDs); first NCI appears. FND-09. |
| F16 PRESENTATION-SPECIFIC | N.A. | Doctype = results filing, not an investor presentation. No deck, chart baselines or order-book definitions to diff. |
| F17 CONCALL SILENCE AUDIT | N.A. | Doctype = results filing, no transcript. Monitoring checklist = NONE (fresh company). No call to audit for silence. |

Blank checks: none. GATE A3 = pass.

---

## COMMITMENT REGISTER (from F6 — feeds Role 5 promise-vs-delivery and FTTCP catalyst timeline)

| # | Commitment | Implied date | Note / agenda ref | Status word |
|---|-----------|--------------|-------------------|-------------|
| 1 | QIP up to Rs 750 Cr (INR 75,000 lakhs), equity and/or convertibles, one or more tranches | Shareholder approval at AGM Aug 28 2026; issuance thereafter | agenda item 2 (l.50); std note 9 (l.296); consol note 10 (l.598); Annexure-II (l.643-655) | board approved (subject to shareholder approval) |
| 2 | Further investment in Dheya Engineering Technologies (Associate) up to Rs 5 Cr (INR 500 lakhs) via subscription and/or secondary purchase | Open; Reg 30 details "will be submitted post completion" | agenda item 3 (l.64); std note 10 (l.300); consol note 11 (l.603) | board approved |
| 3 | 10th Annual General Meeting via VC/OAVM | August 28, 2026, 11:00 AM IST | agenda item 4 (l.80-81) | will be held (scheduled) |
| 4 | AGM Notice + full FY2025-26 Annual Report to exchanges | "as soon as ... sent to the Shareholders" (weeks) | l.87-89 | pending / underway |
| 5 | Reg 30 additional information on the Dheya investment | "post completion of the Investment" | l.76-78 | to be submitted |
| 6 | Hobel Bellows Pvt Ltd + Hobel Bellows Co. acquisition, 100% stake, Rs 45,000 lakh via equity/debt/CCDs | Completed April 27, 2026 | std note 7 (l.287-291); consol note 8 (l.590-594) | completed |
| 7 | Uniflux Renewable Energy Pvt Ltd incorporated for green/renewable/clean-energy EPC projects | Incorporated April 27, 2026; pre-revenue at quarter-end | std note 6 (l.284-286); consol note 7 (l.587-589) | initiated (incorporated) |
| 8 | IPO net proceeds (Rs 23,091.10 lakhs) fully utilised per approved limits; Rs 162 lakh of expenses paid post quarter-end, Rs 58 lakh reclassified to general corporate purposes | Utilised as at June 30 2026; balance actions subsequent to quarter-end | std note 5 (l.281-283); consol note 6 (l.584-586) | completed |

---

## ADDITIONAL FORENSIC OBSERVATIONS (context for A4, not separate GATE checks)

- Consolidated finance costs spiked to 1,125.23 in Q4FY26 (73% of the full-year 1,538.81) versus 193.76 in Q1FY27 and 114.61 in Q1FY26 (l.497). Q4FY26 is a balancing/audited quarter (note 5, l.582); the spike may be a year-end true-up or acquisition-financing accrual. Worth an A4 question given the Rs 45,000 lakh debt/CCD-funded Hobel deal.
- Standalone PAT collapsed to 220.15 (Q1FY27) from 886.20 (Q1FY26) while consolidated PAT rose to 2,786.36 from 1,912.43 — reinforces FND-02: the parent is trending toward a holding-company profile with earnings concentrated in Innomech / Hobel subsidiaries.
- First non-controlling interest appears this quarter (-0.05, l.530/536), consistent with the CCD-structured Hobel acquisition and Uniflux formation; NCI trajectory is a new balance-sheet watch item.

---

```yaml
stage: A3-forensics
company: "UNIMECH"
quarter: "Q1 FY27"
doctype: "results"
model: claude-opus-4-8
status: complete
forensics_path: "/home/user/inflection-pipeline/runs/unimech-q1fy27/work/forensics_results_unimech_q1fy27.md"
ledger_reconciled_pct: 100
checklist:
  F1: FINDING
  F2: FINDING
  F3: PASS
  F4: PASS
  F5: N.A.
  F6: FINDING
  F7: PASS
  F8: FINDING
  F9: PASS
  F10: FINDING
  F11: PASS
  F12: N.A.
  F13: FINDING
  F14: FINDING
  F15: FINDING
  F16: N.A.
  F17: N.A.
findings:
  - {id: "FND-01", check: "F1", line: "439-441", classification: "FORWARD-SIGNAL", implication: "Pre-revenue freshly consolidated subsidiary (Uniflux implicated); Nil line anticipates future revenue accretion."}
  - {id: "FND-02", check: "F2", line: "207,208,233,487,488,514", classification: "AMBIGUOUS", implication: "Standalone hollowing vs consolidated growth; standalone other income props parent PAT and exceeds consolidated other income; parent revenue collapse unexplained."}
  - {id: "FND-04", check: "F6", line: "50,64,80,281,287,296,300", classification: "FORWARD-SIGNAL", implication: "Dense dated commitment set: Rs 750 Cr QIP, Rs 5 Cr Dheya, Rs 45,000 lakh Hobel close, Uniflux, IPO utilisation."}
  - {id: "FND-05", check: "F8", line: "228,229,230,506,507,508", classification: "AMBIGUOUS", implication: "Persistent deferred-tax credits shield ETR (current tax exceeds standalone PBT); prior-period tax adjustments non-zero; future ETR step-up risk."}
  - {id: "FND-06", check: "F10", line: "290,296,547", classification: "FORWARD-SIGNAL", implication: "Forward dilution pipeline: existing diluted spread + CCDs in Hobel consideration + Rs 750 Cr QIP; share count set to rise."}
  - {id: "FND-07", check: "F13", line: "50,64,80,87", classification: "FORWARD-SIGNAL", implication: "QIP enabling resolution + Dheya investment + AGM Aug 28 2026 and FY2025-26 Annual Report incoming (schedule Role 6 AR Deep Dive)."}
  - {id: "FND-08", check: "F14", line: "239,521,531,534", classification: "AMBIGUOUS", implication: "OCI income-tax-effect row identical across standalone and consolidated despite different bases; duplicated line index 11; entity-name drift."}
  - {id: "FND-09", check: "F15", line: "391,394,398,569,570,571", classification: "FORWARD-SIGNAL", implication: "Three entities added to consolidation w.e.f. Apr 27 2026 (Uniflux + Hobel x2); Rs 45,000 lakh debt/CCD-funded; first NCI appears."}
forward_signals: ["FND-01", "FND-04", "FND-06", "FND-07", "FND-09"]
ambiguous: ["FND-02", "FND-05", "FND-08"]
commitments:
  - {commitment: "QIP up to Rs 750 Cr (INR 75,000 lakhs)", implied_date: "AGM 2026-08-28 approval, tranches thereafter", ref: "agenda item 2 l.50 / std note 9 l.296 / consol note 10 l.598", status_word: "board approved"}
  - {commitment: "Further investment in Dheya (Associate) up to Rs 5 Cr", implied_date: "open; Reg 30 post completion", ref: "agenda item 3 l.64 / std note 10 l.300 / consol note 11 l.603", status_word: "board approved"}
  - {commitment: "10th AGM via VC/OAVM", implied_date: "2026-08-28", ref: "agenda item 4 l.80-81", status_word: "scheduled"}
  - {commitment: "AGM Notice + FY2025-26 Annual Report to exchanges", implied_date: "within weeks", ref: "l.87-89", status_word: "underway"}
  - {commitment: "Reg 30 details on Dheya investment", implied_date: "post completion", ref: "l.76-78", status_word: "to be submitted"}
  - {commitment: "Hobel Bellows acquisition Rs 45,000 lakh (equity/debt/CCDs)", implied_date: "2026-04-27", ref: "std note 7 l.287 / consol note 8 l.590", status_word: "completed"}
  - {commitment: "Uniflux Renewable Energy incorporation (green-energy EPC)", implied_date: "2026-04-27", ref: "std note 6 l.284 / consol note 7 l.587", status_word: "initiated"}
  - {commitment: "IPO net proceeds fully utilised; Rs 58 lakh reclassified", implied_date: "as at 2026-06-30", ref: "std note 5 l.281 / consol note 6 l.584", status_word: "completed"}
gate_a3: pass
blank_checks: []
```
