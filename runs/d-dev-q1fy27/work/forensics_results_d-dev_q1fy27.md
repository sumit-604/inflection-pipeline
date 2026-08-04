# A3 FORENSIC NOTES — DEE Development Engineers Ltd (D-DEV / DEEDEV / BSE 544198)
**doctype = results** | Quarter: Q1 FY27 (quarter ended 30 June 2026) | Source: DOC1_board_outcome_full_results.pdf (17 pp, Rs. Lakhs, x0.01 to Cr)
Model: claude-opus-4-8 | A1 extract and A2 ledger reconciled 100% (every ledger row read at its cited line).
Units note: figures below are Rs. Lakhs as printed; Cr conversion = Lakhs x0.01. Original figures preserved.

---

## FINDINGS TABLE

| id | check | ledger row ref | line | verbatim quote | classification | forward implication |
|----|-------|----------------|------|----------------|----------------|---------------------|
| A3-01 | F2 | §3/§7 lines IX; §6 para 8 | 310 / 562 / 495-498 | "total net profit after tax of Rs. 555.96 lacs" | FORWARD-SIGNAL | Consol PAT 1,608.30 vs SA 1,052.31 = gap 555.99 lacs; ~100% of the consolidated uplift is subsidiary PAT (555.96). S-vs-C PAT gap swung 84.1%→36.5%→52.8% of SA PAT across Q1FY26/Q4FY26/Q1FY27 (>5pt = trigger). Consol growth (+22.4% YoY) lags standalone (+47.4%): the subsidiary engine (incl. Heavy Fab) is decelerating relative to the parent. |
| A3-02 | F2/F12 | §7 EBITDA build | 541,549,550,554 | "Profit before exceptional items and tax 2,005.43" | FORWARD-SIGNAL | Consol operating EBITDA ≈ 4,974.61 lacs / rev 29,446.22 = **16.9%**; SA ≈ 16.2%. Below the **>19% FY27 guidance** (Notion watch item 1). No margin inflection this quarter. |
| A3-03 | F4 | §6 para 8-9 | 495-506 | "in respect of 5 subsidiaries ... reviewed by their respective independent auditors" | AMBIGUOUS | 555.96 / 1,608.30 = **34.6% of consolidated PAT** rests on numbers reviewed by component auditors, not the principal auditor S.R. Batliboi. Above 10% threshold. No prior-period disclosure available to trend (NO_PRIOR_LEDGER). |
| A3-04 | F5 | §6 para 5-7; §9 Note 5 | 462-468 / 486-494 / 652-665 | "management is unable to assess the consequential impact of the above uncertainties on the carrying value of above assets amounting to Rs 5,082.67 lakhs" | CONFIRMATORY-NEGATIVE | Consolidated **qualification RETAINED** (Malwa Power, Rs.5,082.67 lacs, impairment not assessed) and PSPCL EoM RETAINED, both unchanged in amount vs prior description. **Thesis trigger 1 (qualification not removed by Q3 FY27)** is NOT yet cured — 2 quarters left. Note 5 narrative has **WIDENED**: new "operational viability ... uncertainty over its future cash flows" and "evaluation of strategic alternatives" language (see A3-05). |
| A3-05 | F7 | §9 Note 5 | 662 / 665 | "adversely impacted the operational viability of MPPL and created uncertainty over its future cash flows ... Pending final outcome of the appeal before APTEL and evaluation of strategic alternatives" | FORWARD-SIGNAL | Newly added going-concern-flavoured hedge on a subsidiary. "Strategic alternatives" is a euphemism candidate for divestment/closure/write-down. Foreshadows a possible impairment or exit of Malwa Power. |
| A3-06 | F6 | Item 2 / Annexure B | 719-720 / 41-50 | "To meet future fund-raising requirements / growth plans of the Company" | FORWARD-SIGNAL | Authorised capital raised Rs.85→95 Cr expressly to enable future fund-raising. Equity funding round foreshadowed. |
| A3-07 | F6/F13 | Item 6 / Annexure E | 88-101 / 787-804 | "in the event of default to convert the whole or part of the outstanding loan into Equity Shares" | FORWARD-SIGNAL | Board pre-authorised Sec 62(3) conversion of a **Rs.2,000 Cr Bank of India consortium loan into equity on Event of Default**. Distress/covenant signal; ties to ND/EBITDA >3x thesis trigger and to future dilution. |
| A3-08 | F8 | §7 tax rows | 557-561 | "Profit before tax 2,005.43 ... Total tax expense 397.13" | FORWARD-SIGNAL | Consol ETR **19.8%** vs statutory 25.17% (~537 bps shield). Incremental tax on subsidiary PBT (591.30) is only 35.31 = **5.97% effective** — subsidiary profits (Thailand / MPPL-offset) lightly taxed. Future ETR step-up risk as shields normalise. |
| A3-09 | F10 | §3/§7 row XII/XV | 317 / 584 | "Paid up share capital ... 6,926.34" (30-06-2026, unchanged from 31-03-2026) | AMBIGUOUS | Paid-up capital at 30-06-2026 is **unchanged** at 6,926.34 lacs (6,92,63,400 sh) despite the Jun-26 ₹300 Cr preferential (59,76,096 sh → 7,52,39,438 post-issue per Notion). Allotment evidently closed post-quarter-end, yet **NO subsequent-events note discloses a ₹300 Cr capital raise** (Notes 1-7 both statements). ~8.6% dilution pending; EPS here is pre-issue. Combined with A3-06 (authorised-cap hike) and A3-07 (loan conversion), a multi-track dilution pipeline. |
| A3-10 | F12 | §8 Heavy fabrication | 600 / 608 / 619 | "Heavy fabrication ... 1,534.93 ... 367.66 ... 4,781.58" | CONFIRMATORY-NEGATIVE | Heavy Fab revenue **+3.7% YoY** (1,534.93 vs 1,480.06), result **-7.2% YoY** (367.66 vs 396.03), -23.4% QoQ. Far below the 20% bar in **thesis trigger 4 (Heavy Fab <20% YoY for two consecutive quarters)** — this is quarter 1 of that count. Segment assets **+28.8% YoY** (4,781.58 vs 3,713.21) with liabilities +45% QoQ = capacity/WC build ahead of revenue (Ganeko Solar ₹64 Cr order executes Jan-2027). |
| A3-11 | F12 | §8 Power division | 607 / 624 | "Power division (120.86)" | AMBIGUOUS | Consol Power segment result negative (-120.86) with liabilities +57% YoY (3,018.87 vs 1,926.07) and it houses impaired Malwa. Loss-making segment with rising liabilities. |
| A3-12 | F13 | Item 3 | 52-59 | "Ms. Shikha Bansal, WTD, from Rs. 38.49 Lakhs to Rs. 1.38 Crore per annum i.e. increase of Rs. 1 Cr" | AMBIGUOUS | Promoter-group WTD remuneration +259% w.e.f. 01.04.2026, pending members' special resolution. Governance data point during a period of qualified audit and negative CFO. |
| A3-13 | F13 | Item 5 / Annexure D | 80-86 / 761-778 | "Ms. Ashvika Bansal, relative of a director, as CSR Head ... Rs. 2,40,000 per month ... currently pursuing a BA" | AMBIGUOUS | Promoter relative (undergraduate, volunteer since 2021) appointed CSR Head at Rs.28.8 L p.a. under Sec 188 RPT. Related-party appointment. |
| A3-14 | F13 | Item 4 / Annexure C | 61-68 / 730-739 | "Ms. Shikha Bansal ... shall take on the office premises ... and further rent out ... to Atul Krishan Bansal (AKB) Foundation ... subject to completion of ownership transfer in her name" | AMBIGUOUS | Promoter WTD interposed as landlord between company premises and a promoter-group foundation (itself a consolidated "Subsidiary"). Small value (Rs.70k/mo) but structurally a related-party web. |
| A3-15 | F13 | Item 10 | 122-128 | "to approve Notice, Annual Report for FY 2025-26, Board's Report" | FORWARD-SIGNAL | 37th AGM convening + full FY25-26 Annual Report imminent (weeks) → **schedule Role 6 AR Deep Dive**; enabling resolutions (capital, remuneration, loan-conversion) all route through this AGM. |
| A3-16 | F14 | §5 / §9 sig blocks; cover | 405 / 687 / 159 | "Date: 2026.08.04 10:49:58" (CMD) vs "concluded at 10:52 A.M." | AMBIGUOUS | `SIG_BEFORE_CONCLUSION`: CMD digitally signed standalone (10:49:58) and consolidated (10:50:53) results **before** the stated board conclusion (10:52 A.M.). Both auditor signatures post-date conclusion (10:59:41 / 11:01:33). Control/sequencing anomaly. |
| A3-17 | F14 | headers / entity table | 360 / 630 / 452-459 | "Notes to the Statement of Uudited Standalone Financials Results" | NEUTRAL-FACT | Drafting inconsistencies: header typos (lines 360, 630), "Relationship" column populated only for rows 1 and 4 of the 6-entity table (455,456,458,459 blank), line-item reordering (finance/depreciation swap SA vs consol). Individually immaterial; cumulatively a controls data point alongside A3-16. |

---

## CHECKLIST SCORECARD (all 17, one status each)

| Check | Status | Basis (one line) |
|-------|--------|------------------|
| F1 ZERO-VALUE STANDING | **PASS** | All 7 ZERO_STANDING rows explained benignly — SA 304/307/318, Consol 556/559/578/585 (see per-row assessment below). |
| F2 STANDALONE vs CONSOLIDATED | **FINDING** | A3-01/A3-02: PAT gap = ~100% subsidiary PAT; gap swung >5pt YoY; consol EBITDA 16.9% below 19% guidance (lines 310/562/495-498). |
| F3 SHELL-ENTITY DETECTION | **PASS** | Cost lines differ materially SA vs consol (materials 10,081.63 vs 10,944.03; employees 3,289.88 vs 4,442.22; depr 1,103.25 vs 1,500.77 — lines 293/545, 296/548, 298/549); subsidiaries have real operations; no shells. Malwa viability handled at F5/F7. |
| F4 UNAUDITED CONTRIBUTION | **FINDING** | A3-03: 34.6% of consol PAT via component-auditor-reviewed subsidiaries (lines 495-498). |
| F5 GOING CONCERN / EoM SCOPE | **FINDING** | A3-04: qualification + EoM RETAINED (unchanged Rs.5,082.67 lacs); Note 5 narrative WIDENED to viability/strategic-alternatives (lines 462-468, 486-494, 652-665). |
| F6 FORWARD-COMMITMENT PHRASES | **FINDING** | A3-06/A3-07/A3-15: capital-raise, loan-conversion, AGM/AR commitments (lines 719, 88-101, 122-128, 665). See Commitment Register. |
| F7 HEDGE PHRASE MINING | **FINDING** | A3-05: newly added MPPL "operational viability ... uncertainty over its future cash flows" + "strategic alternatives" hedge (lines 662, 665). |
| F8 TAX FORENSICS | **FINDING** | A3-08: consol ETR 19.8% vs 25.17%; ~6% effective on subsidiary PBT = future step-up risk (lines 557-561). Earlier-year tax adjustment nil this quarter (307/559 dash) but non-zero in FY26 comparatives (-156.90 SA / -151.50 consol). |
| F9 OCI FORENSICS | **PASS** | Remeasurement Q1FY27 69.20 (SA & consol) < FY26 totals (242.73 / 270.73); FX translation -56.76 < FY26 528.03 (lines 313-315, 565-569). No single-quarter swing exceeding prior year; no assumption-change flag. |
| F10 SHARE COUNT / DILUTION | **FINDING** | A3-09: paid-up unchanged 6,926.34 lacs despite ₹300 Cr Jun-26 preferential; no subsequent-events note; dilution pipeline (lines 317/584, 88-101, 697-723). Basic/diluted spread negligible (1.52/1.52 SA; 2.33/2.32 consol, lines 320-321/587-588). |
| F11 RESERVES / NET WORTH TIE-OUT | **PASS** | Consol other equity 82,112.20 + paid-up 6,926.34 = 89,038.54 lacs = ₹890.39 Cr, ties to Notion equity ₹890.4 Cr (<5% gap). Lines 585, 584. Preferential ₹293 Cr net is post-period (reconciles with A3-09). |
| F12 SEGMENT FORENSICS | **FINDING** | A3-10/A3-11: Heavy Fab +3.7% YoY rev / -7.2% result / +28.8% assets; Power loss-making with rising liabilities (lines 600,608,619,607,624). |
| F13 BOARD OUTCOME BEYOND RESULTS | **FINDING** | A3-07/A3-12/A3-13/A3-14/A3-15: loan-conversion-on-default enabler, capital-raise enabler, promoter remuneration +259%, promoter-relative CSR head, promoter RPT, AR imminent (lines 41-130). |
| F14 NOTE DRAFTING INCONSISTENCIES | **FINDING** | A3-16/A3-17: SIG_BEFORE_CONCLUSION + header typos + incomplete entity-relationship column (lines 405/687/159, 360/630, 452-459). |
| F15 ENTITY LIST DIFFS | **N.A.** | NO_PRIOR_LEDGER — no prior-quarter extract supplied; diff not computable. Baseline recorded: 6 entities (lines 454-459), incl. Atul Krishan Bansal Foundation consolidated as "Subsidiary Company" — carry forward for next-quarter diff. |
| F16 PRESENTATION-SPECIFIC | **N.A.** | Doctype = results; no presentation deck in scope. |
| F17 CONCALL SILENCE AUDIT | **N.A.** | Doctype = results; no transcript. Note: order-book items (BHEL conversion, HRSG additions — Notion watch 4/5) carry no disclosure in a results filing; defer to concall/press-release agents. |

**Status line: 4 PASS (F1, F3, F9, F11) / 10 FINDING (F2, F4, F5, F6, F7, F8, F10, F12, F13, F14) / 3 N.A. (F15, F16, F17). Total 17. No blanks.**

### F1 per-row ZERO_STANDING assessment (7 rows)
- SA line 304 / Consol line 556 — Exceptional items "Impact of Labour Codes": nil in Q1FY27 & Q1FY26; the (227.41) past-service-cost charge was a one-time Q4FY26 event (Labour Codes notified 21 Nov 2025, Notes 5/6). Ongoing incremental cost now flows through employee benefits, not exceptional. Benign template + timing.
- SA line 307 / Consol line 559 — "Adjustment of tax related to earlier years": nil current quarter; anticipates prior-period tax true-ups (non-zero only in FY26 columns). Benign (see F8).
- SA line 318 / Consol line 585 — "Other equity": dash in all interim columns, populated only at year-end (81,780.51 / 82,112.20) — standard interim-filing convention. Benign.
- Consol line 578 — OCI attributable to Non-controlling interest: nil all four periods — NCI holders bear no OCI component. Benign.

---

## COMMITMENT REGISTER (from F6)

| Commitment | Implied date | Note / item ref | Status word |
|------------|--------------|-----------------|-------------|
| Increase authorised capital Rs.85→95 Cr "to meet future fund-raising requirements / growth plans" | ensuing 37th AGM (~Sep 2026) | Item 2 (l.41-50); Annexure B (l.719) | board approved / pending members |
| Enable Sec 62(3) conversion of Rs.2,000 Cr BoI consortium loan into equity on Event of Default | on default; SR at general meeting | Item 6 (l.88-101); Annexure E (l.787-804) | board approved / pending members |
| Increase Shikha Bansal (WTD) remuneration to Rs.1.38 Cr p.a. w.e.f. 01.04.2026 | AGM special resolution | Item 3 (l.52-59) | board approved / pending members |
| RPT office-premises rent (Shikha Bansal → AKB Foundation) | "subject to completion of ownership transfer ... and execution of rent agreement" | Item 4 (l.61-68); Annexure C (l.730-739) | approved / pending completion |
| Convene 37th AGM; approve Annual Report FY25-26 & Board's Report | within weeks (AGM ~Sep 2026) | Item 10 (l.122-128) | authorised / underway → Role 6 AR Deep Dive |
| MPPL "evaluation of strategic alternatives" | pending APTEL final outcome | Consol Note 5 (l.665) | underway |
| Rejoinder before APTEL seeking substitution of interim with final tariff | filed 21 Jun 2026 | Consol Note 5 (l.659) | completed / filed |

---

## THESIS / NOTION TIE-BACK (for A4)
- **Watch 1 (EBITDA margin → >19%)**: A3-02 — Q1FY27 consol ~16.9%, SA ~16.2%; no inflection. Below guidance.
- **Watch 2 (Heavy Fab scaling)**: A3-10 — +3.7% YoY revenue; **thesis-broken trigger 4 clock started (quarter 1 of 2 at <20%)**.
- **Watch 3 (working capital normalisation)**: A3-11 and segment liabilities (Heavy Fab +45% QoQ, Power +57% YoY) — no full balance sheet in a results filing; AMBIGUOUS → concall question.
- **Watch 4/5 (BHEL conversion, HRSG additions)**: absent from this doctype; F17 N.A. — defer to press release / concall.
- **Trigger 1 (qualification removal by Q3 FY27)**: A3-04 — NOT cured this quarter; widened. Two quarters remain.
- **Trigger 2 (ND/EBITDA >3x)**: A3-07 loan-conversion-on-default + A3-09 ₹293 Cr net raise for debt repayment are the offsetting forces; no ND figure in this filing.
- **Trigger 5 (governance-event repeat)**: A3-16 SIG_BEFORE_CONCLUSION + A3-12/13/14 related-party cluster are the governance items to weigh against the prior Q3 FY26 EBITDA-misclassification event.

---

```yaml
stage: A3-forensics
company: "D-DEV"
quarter: "Q1FY27"
doctype: "results"
model: claude-opus-4-8
status: complete
forensics_path: "/home/user/inflection-pipeline/runs/d-dev-q1fy27/work/forensics_results_d-dev_q1fy27.md"
ledger_reconciled_pct: 100
checklist:
  F1: PASS
  F2: FINDING
  F3: PASS
  F4: FINDING
  F5: FINDING
  F6: FINDING
  F7: FINDING
  F8: FINDING
  F9: PASS
  F10: FINDING
  F11: PASS
  F12: FINDING
  F13: FINDING
  F14: FINDING
  F15: N.A.
  F16: N.A.
  F17: N.A.
findings:
  - {id: "A3-01", check: "F2", line: "310/562/495-498", classification: "FORWARD-SIGNAL", implication: "Consol PAT uplift ~100% subsidiary; S-vs-C gap swung 84%->53% YoY; consol growth lags standalone"}
  - {id: "A3-02", check: "F2", line: "541/549/550/554", classification: "FORWARD-SIGNAL", implication: "Consol EBITDA ~16.9% below >19% FY27 guidance"}
  - {id: "A3-03", check: "F4", line: "495-506", classification: "AMBIGUOUS", implication: "34.6% of consol PAT reviewed by component auditors, not principal auditor"}
  - {id: "A3-04", check: "F5", line: "462-468/486-494/652-665", classification: "CONFIRMATORY-NEGATIVE", implication: "Qualification+EoM retained, Note 5 widened; thesis trigger 1 not cured"}
  - {id: "A3-05", check: "F7", line: "662/665", classification: "FORWARD-SIGNAL", implication: "New MPPL viability/strategic-alternatives hedge foreshadows impairment/exit"}
  - {id: "A3-06", check: "F6", line: "719-720/41-50", classification: "FORWARD-SIGNAL", implication: "Authorised capital hike for future fund-raising -> equity round"}
  - {id: "A3-07", check: "F6/F13", line: "88-101/787-804", classification: "FORWARD-SIGNAL", implication: "Sec 62(3) loan-to-equity conversion on default of Rs.2,000 Cr BoI loan = distress/dilution signal"}
  - {id: "A3-08", check: "F8", line: "557-561", classification: "FORWARD-SIGNAL", implication: "Consol ETR 19.8% vs 25.17%; subsidiary PBT taxed ~6% = future ETR step-up risk"}
  - {id: "A3-09", check: "F10", line: "317/584/88-101/697-723", classification: "AMBIGUOUS", implication: "Paid-up unchanged despite Rs.300 Cr preferential; no subsequent-events note; ~8.6% dilution pending"}
  - {id: "A3-10", check: "F12", line: "600/608/619", classification: "CONFIRMATORY-NEGATIVE", implication: "Heavy Fab +3.7% YoY rev / -7.2% result; assets +28.8% = build ahead of revenue; trigger 4 clock started"}
  - {id: "A3-11", check: "F12", line: "607/624", classification: "AMBIGUOUS", implication: "Power segment loss-making with liabilities +57% YoY; houses impaired Malwa"}
  - {id: "A3-12", check: "F13", line: "52-59", classification: "AMBIGUOUS", implication: "Promoter WTD remuneration +259% amid qualified audit / weak CFO"}
  - {id: "A3-13", check: "F13", line: "80-86/761-778", classification: "AMBIGUOUS", implication: "Promoter relative (undergraduate) appointed CSR Head at Rs.28.8 L, Sec 188 RPT"}
  - {id: "A3-14", check: "F13", line: "61-68/730-739", classification: "AMBIGUOUS", implication: "Promoter WTD interposed as landlord between company premises and promoter foundation"}
  - {id: "A3-15", check: "F13", line: "122-128", classification: "FORWARD-SIGNAL", implication: "Full FY25-26 Annual Report imminent -> schedule Role 6 AR Deep Dive"}
  - {id: "A3-16", check: "F14", line: "405/687/159", classification: "AMBIGUOUS", implication: "SIG_BEFORE_CONCLUSION: CMD signed results before stated board conclusion time"}
  - {id: "A3-17", check: "F14", line: "360/630/452-459", classification: "NEUTRAL-FACT", implication: "Header typos + incomplete entity-relationship column + line-item reordering = controls data point"}
forward_signals: ["A3-01", "A3-02", "A3-05", "A3-06", "A3-07", "A3-08", "A3-15"]
ambiguous: ["A3-03", "A3-09", "A3-11", "A3-12", "A3-13", "A3-14", "A3-16"]
commitments:
  - {commitment: "Increase authorised capital Rs.85->95 Cr for future fund-raising", implied_date: "37th AGM ~Sep 2026", ref: "Item 2 l.41-50 / Annexure B l.719", status_word: "board approved / pending members"}
  - {commitment: "Sec 62(3) conversion of Rs.2,000 Cr BoI consortium loan to equity on default", implied_date: "on Event of Default; SR at general meeting", ref: "Item 6 l.88-101 / Annexure E l.787-804", status_word: "board approved / pending members"}
  - {commitment: "Increase Shikha Bansal WTD remuneration to Rs.1.38 Cr p.a.", implied_date: "AGM special resolution; effect 01.04.2026", ref: "Item 3 l.52-59", status_word: "board approved / pending members"}
  - {commitment: "RPT office-premises rent Shikha Bansal -> AKB Foundation", implied_date: "on ownership transfer + deed execution", ref: "Item 4 l.61-68 / Annexure C l.730-739", status_word: "approved / pending completion"}
  - {commitment: "Convene 37th AGM; approve Annual Report FY25-26 and Board's Report", implied_date: "within weeks (~Sep 2026)", ref: "Item 10 l.122-128", status_word: "authorised / underway"}
  - {commitment: "MPPL evaluation of strategic alternatives", implied_date: "pending APTEL final outcome", ref: "Consol Note 5 l.665", status_word: "underway"}
  - {commitment: "Rejoinder before APTEL to substitute interim with final tariff", implied_date: "filed 21 Jun 2026", ref: "Consol Note 5 l.659", status_word: "completed / filed"}
gate_a3: pass
blank_checks: []
```
