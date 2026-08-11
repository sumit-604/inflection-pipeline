# A3 FORENSIC NOTES — NephroPlus (Nephrocare Health Services Ltd), Q1FY27 — doctype: results (PRESS RELEASE companion)

Source extract: `runs/nephroplus-q1fy27/work/extract_pressrelease_nephroplus_q1fy27.txt`
Ledger reconciled: `runs/nephroplus-q1fy27/work/ledger_pressrelease_nephroplus_q1fy27.md`
Ledger rows read verbatim at cited line before judging: 44 / 44 = 100%.
Line references (L#) are the A1 embedded extraction line numbers, matching the ledger convention.

Doctype note: this is a press-release companion, not a Reg 33 statutory statement. It carries a curated
consolidated highlights table + operational table + three management quotes + footnotes + safe-harbour.
It has no auditor report, no going-concern/EoM, no board outcome, no balance sheet, no tax/OCI/segment
tables, and no formal consolidation entity list. Those statutory-apparatus checks are marked N.A. with a
one-line reason. The high-value checks that DO bite here are F2 (standalone-vs-consolidated coverage),
F6/F7 (forward-signal and hedge language in the quotes), F14 (inconsistency vs the statutory apparatus /
drafting), and F17 (silence audit vs the Notion monitoring checklist). F17 is run against the management
narrative surface per the prompt's own injected-input tie (checklist supplied "for F17 silence audit") and
the task injection naming silence / promise-vs-delivery as high value; it is NOT marked N.A.

---

## FINDINGS TABLE

| id | check | ledger row | line | verbatim quote | classification | forward implication |
|----|-------|-----------|------|----------------|----------------|---------------------|
| F2-1 | F2 | T7 (STANDALONE_NOT_IN_EXTRACT) | L18-20 | "Unaudited Standalone and Consolidated financial results of the Company for the quarter ended June 30, 2026" | AMBIGUOUS | Cover letter certifies BOTH standalone and consolidated are enclosed, but no standalone table exists anywhere in the 4 pages. S-vs-C decomposition (India standalone vs JV/international drag) is impossible from this doc. The one number that would localise the JV loss (Rs 3.6 cr, N2) and Saudi expenses is exactly what is withheld. A4 to request the standalone highlights. |
| F6-1 | F6 | Q2 (CEO quote) | L112-114 | "the NephroPlus Dialysis Index, a composite health score ... which can be aggregated at the Clinic, Cluster, Zone, and Country levels over the next few quarters" | FORWARD-SIGNAL | Dateable management commitment (~2-4 quarters). Feeds Role 5 promise-vs-delivery tracker and FTTCP catalyst timeline; check for the aggregated index disclosure by Q3-Q4 FY27. |
| F6-2 | F6 | Q1 (Chairman quote) | L96-97 | "We will continue to invest in identifying and understanding new geographies" | FORWARD-SIGNAL | Ongoing/underway commitment to further international M&A/partnership capex; signals continued deployment (ties to CFO "capital ... deployed with discipline", L126). |
| F7-1 | F7 | Q1 (Chairman quote) | L95-96 | "we are also exploring entry into new countries via strategic acquisitions or long-term partnerships with payors" | AMBIGUOUS | "exploring" is a pre-emptive hedge — new-country entry is early-stage, no near-term commitment. Notably softer than the prior-quarter posture on KSA ("expected shortly"). Lean bear: next-country pipeline is not yet a dated catalyst. A4 question. |
| F14-1 | F14 | N3 vs N1 (INCONSISTENT_DEFINITION) | L83 vs L53 | N3: "EBITDA adjusted for Saudi expenses and ESOP expenses" vs N1: "EBITDA adjusted for ESOP expenses of Rs. 1.3 crores ..." | AMBIGUOUS | Same "*" marker, same Adj. EBITDA metric, two different definitions. The narrative footnote reveals "Saudi expenses" are stripped OUT of headline Adj. EBITDA while the table footnote does not — implying KSA is a pre-revenue cost drag excluded from the 23.1% margin, quantum undisclosed. If Saudi expenses were add-back material, reported margin flatters the true consolidated economics. A4 to size Saudi expense adjustment and reconcile the two definitions. |
| F14-2 | F14 | M14/M15/M17 (ROUNDING_VARIANCE) | L102-104 | "Revenue grew 23.7% year-on-year to ₹282 crore, and EBITDA grew 30.7% YoY to ₹65 crore ... we crossed 10,30,000 treatments" | NEUTRAL-FACT | CEO quote rounds ₹281.8→₹282, ₹65.1→₹65, 10,31,084→10,30,000. Immaterial individually; cumulatively a drafting-precision note, not a discrepancy of substance. Also MARGIN_DELTA_OMITTED (L49/L52): table YoY/QoQ margin-delta cells blank while bullets carry +120bps/+220bps — asymmetry, not contradiction. |
| F17-1 | F17 | M28 + N3 vs monitoring item 7 (KSA) | L132-133 & L83 | Footprint "India, Nepal, the Philippines, Uzbekistan, and Saudi Arabia" (L132-133) and "Saudi expenses" (L83) — but NO statement of KSA license received or first revenue anywhere | AMBIGUOUS | The single cleanest Q1 FY27 metric to watch (KSA license received + first revenue) is NOT explicitly confirmed. The doc DOES touch Saudi twice (named in footprint; expenses being incurred and adjusted out) yet stays silent on the license/first-revenue confirmation — a selective silence on the key catalyst that prior quarter flagged "expected shortly." Saudi cost is being incurred (setup underway) but revenue unconfirmed. Per Role 5, silence on a watched catalyst is a confirmatory concern. A4 to ask directly: is the KSA license received and has first revenue been booked? |

---

## CHECKLIST SCORECARD (all 17 — no blanks)

| Check | Status | One-line basis |
|-------|--------|----------------|
| F1  ZERO-VALUE STANDING LINES | PASS | Ledger zero_standing = 0; both curated highlights tables (L47-52, L62-64) carry no nil/dash/zero line item across any period. Nothing standing at zero to interrogate. |
| F2  STANDALONE vs CONSOLIDATED | FINDING | F2-1: standalone certified as enclosed (T7, L18-20) but absent; decomposition impossible, JV/Saudi drag not isolable. |
| F3  SHELL-ENTITY DETECTION | N.A. | Requires standalone-vs-consolidated cost lines (materials, employee, depreciation); press release carries no cost-line breakdown and no standalone table. |
| F4  UNAUDITED CONTRIBUTION RATIO | N.A. | Requires auditor's Other Matters paragraph (component/JV auditors); no auditor report in a press release (ledger auditor_paras = 0). |
| F5  GOING CONCERN / EoM SCOPE | N.A. | No auditor report, hence no going-concern/Emphasis-of-Matter paragraph to verbatim-diff. |
| F6  FORWARD-COMMITMENT MINING | FINDING | F6-1 ("over the next few quarters" index aggregation) + F6-2 ("will continue to invest in ... new geographies"); dated/dateable commitments in the quotes. |
| F7  HEDGE PHRASE MINING | FINDING | F7-1: "exploring" new-country entry — pre-emptive hedge signalling early-stage, uncommitted expansion pipeline. |
| F8  TAX FORENSICS | N.A. | No PBT/tax split, no ETR, no deferred-tax line; press release reports Adj. PAT only. |
| F9  OCI FORENSICS | N.A. | No OCI / actuarial line in a press-release highlights table. |
| F10 SHARE COUNT & DILUTION | N.A. | No paid-up capital and no basic/diluted EPS disclosed. (ESOP expense trend Rs 2.3→1.3 cr YoY is captured in footnotes N1/N2 but gives no share count to run a dilution spread.) |
| F11 RESERVES / NET WORTH TIE-OUT | N.A. | No balance sheet, no other-equity/paid-up figures to reconcile. |
| F12 SEGMENT FORENSICS | N.A. | No segment assets/liabilities tables; geography footprint (L132-133) is narrative, not segment financials. |
| F13 BOARD OUTCOME | N.A. | Press release, not the Board Outcome letter (ledger agenda_items = 0); no AR/AGM/record-date/director-term content. |
| F14 NOTE DRAFTING INCONSISTENCIES | FINDING | F14-1 (INCONSISTENT_DEFINITION, N3 vs N1 — Saudi+ESOP vs ESOP-only) + F14-2 (ROUNDING_VARIANCE; MARGIN_DELTA_OMITTED). |
| F15 ENTITY LIST DIFFS | N.A. | No formal consolidation entity list with relationship type (ledger entities = 0); 5-country footprint is a narrative operating claim, not a subsidiary/JV/associate list, and no prior-quarter list to diff. |
| F16 PRESENTATION DROPPED/REFRAMED | N.A. | Not a presentation deck (no charts/axes/order-book); no prior-quarter press release supplied (PRIOR_EXTRACT_PATH not provided) for a cross-deck disclosure diff. |
| F17 SILENCE AUDIT | FINDING | F17-1: KSA license + first revenue (the single cleanest watched metric) not confirmed despite Saudi named in footprint and Saudi expenses incurred; plus balance-sheet/cash/ownership watch-items structurally absent (see table below). |

---

## COMMITMENT REGISTER (from F6/F7)

| commitment | implied date | note/quote ref | status word |
|-----------|--------------|----------------|-------------|
| Dialysis Index aggregated at Clinic/Cluster/Zone/Country levels | "over the next few quarters" (~by Q3-Q4 FY27) | Q2 / L112-114 | underway |
| Continue to invest in identifying/understanding new geographies | ongoing, undated | Q1 / L96-97 | underway |
| Explore entry into new countries via acquisitions / payor partnerships | undated, early-stage | Q1 / L95-96 | exploring (hedge) |
| Scale into higher price-point international markets, preserving margin discipline | undated intent | Q3 / L121-123 | intends |
| NIDA (International Dialysis Academy) launched in India + Philippines | achieved Q1FY27 | Q2 / L107-110 | completed |
| NephroPlus Dialysis Index launched | achieved Q1FY27 | Q2 / L112 | completed |
| Capital deployed with discipline, "on track" for long-term value creation | ongoing, undated | Q3 / L126-128 | underway |

---

## F17 SILENCE AUDIT — monitoring-checklist items NOT addressed in the press release

| # | Monitoring item | Addressed? | Note |
|---|-----------------|-----------|------|
| 1 | Revenue growth YoY | YES | 23.7% (L47) — GREEN (>15%). |
| 2 | Adj. EBITDA margin | YES | 23.1% (L49) — GREEN (>22%), but see F14-1: Saudi expenses stripped out. |
| 3 | International revenue mix | NO | No geographic revenue split disclosed anywhere. |
| 4 | Pre-tax ROCE | NO | No capital-employed / return metric. |
| 5 | CFO/PAT ratio | NO | No cash-flow statement in press release. |
| 6 | Net cash position | NO | No balance sheet. |
| 7 | KSA license + first revenue | NO (selective) | Saudi named in footprint + Saudi expenses incurred, but license/first-revenue NOT confirmed — F17-1. Highest-value silence. |
| 8 | Receivable days | NO | No working-capital disclosure. |
| 9 | Promoter pledge | NO | No shareholding/pledge disclosure. |
| 10 | Captive hospital renewal rate | NO | Not mentioned. |
| 11 | Clinics added rolling 12m | PARTIAL | 550 clinics now (L104/L131), 50-clinic Philippines milestone (L105); net YoY add count not given. |
| 12 | Goodwill as % net worth | NO | No balance sheet. |
| 13 | Promise vs delivery (guidance) | PARTIAL | Prior "KSA expected shortly" not explicitly closed out — see F17-1. |
| 14 | Promoter/PE shareholding change | NO | Not mentioned (Dec-26 IPO lockup overhang unaddressed). |
| 15-18 | Bed count / utilisation / treatments-per-clinic | PARTIAL | Treatments 10,31,084 (L62) and 550 clinics allow inference; not stated directly. |

Interpretation: most balance-sheet / cash / ownership silences are STRUCTURALLY EXPECTED of a press release and are NOT per se red flags — the statutory filing will carry them. The one silence that is conspicuous and material is item 7 (KSA), because the document elects to mention Saudi twice yet withholds the license/first-revenue confirmation that the thesis explicitly nominated as the single cleanest Q1 FY27 metric. That selective omission is the forward signal, promoted to F17-1 and flagged for A4.

---

## FLAGGED FOR A4 (convert to management questions)

- FORWARD-SIGNAL: F6-1 (Dialysis Index aggregation "over the next few quarters" — dated milestone to track).
- AMBIGUOUS: F2-1 (request standalone highlights; where do the Rs 3.6 cr JV loss and Saudi expenses sit?),
  F7-1 (is any new-country entry beyond "exploring" — named target, indicative timeline?),
  F14-1 (size the "Saudi expenses" add-back; reconcile the two Adj. EBITDA definitions; is KSA pre-revenue?),
  F17-1 (is the KSA license received and has first revenue been booked in Q1 FY27?).

---

```yaml
stage: A3-forensics
company: "nephroplus"
quarter: "q1fy27"
doctype: "results (press-release companion)"
model: claude-opus-4-8
status: complete
forensics_path: "/home/user/inflection-pipeline/runs/nephroplus-q1fy27/work/forensics_pressrelease_nephroplus_q1fy27.md"
ledger_reconciled_pct: 100
checklist:
  F1: PASS
  F2: FINDING
  F3: N.A.
  F4: N.A.
  F5: N.A.
  F6: FINDING
  F7: FINDING
  F8: N.A.
  F9: N.A.
  F10: N.A.
  F11: N.A.
  F12: N.A.
  F13: N.A.
  F14: FINDING
  F15: N.A.
  F16: N.A.
  F17: FINDING
findings:
  - {id: "F2-1", check: "F2", line: "L18-20", classification: "AMBIGUOUS", implication: "Standalone certified as enclosed but absent; JV/Saudi drag not isolable — request standalone"}
  - {id: "F6-1", check: "F6", line: "L112-114", classification: "FORWARD-SIGNAL", implication: "Dialysis Index aggregation over next few quarters — dated milestone for promise-vs-delivery tracker"}
  - {id: "F6-2", check: "F6", line: "L96-97", classification: "FORWARD-SIGNAL", implication: "Ongoing commitment to further international investment/capex"}
  - {id: "F7-1", check: "F7", line: "L95-96", classification: "AMBIGUOUS", implication: "'exploring' new-country entry — early-stage, softer than prior KSA posture; no dated catalyst yet"}
  - {id: "F14-1", check: "F14", line: "L83 vs L53", classification: "AMBIGUOUS", implication: "Two Adj. EBITDA definitions; Saudi expenses stripped from headline margin — KSA pre-revenue cost drag, quantum undisclosed"}
  - {id: "F14-2", check: "F14", line: "L102-104", classification: "NEUTRAL-FACT", implication: "CEO rounding variance vs table; margin-delta cells omitted from table — drafting, not substance"}
  - {id: "F17-1", check: "F17", line: "L132-133 & L83", classification: "AMBIGUOUS", implication: "KSA license+first revenue (single cleanest watched metric) unconfirmed despite Saudi in footprint and Saudi expenses incurred — selective silence"}
forward_signals: ["F6-1", "F6-2"]
ambiguous: ["F2-1", "F7-1", "F14-1", "F17-1"]
commitments:
  - {commitment: "Dialysis Index aggregated at Clinic/Cluster/Zone/Country levels", implied_date: "over the next few quarters (~Q3-Q4 FY27)", ref: "Q2/L112-114", status_word: "underway"}
  - {commitment: "Continue to invest in identifying/understanding new geographies", implied_date: "ongoing/undated", ref: "Q1/L96-97", status_word: "underway"}
  - {commitment: "Explore entry into new countries via acquisitions/payor partnerships", implied_date: "undated/early-stage", ref: "Q1/L95-96", status_word: "exploring"}
  - {commitment: "Scale into higher price-point international markets, preserving margin discipline", implied_date: "undated intent", ref: "Q3/L121-123", status_word: "intends"}
  - {commitment: "NIDA International Dialysis Academy launched (India+Philippines)", implied_date: "achieved Q1FY27", ref: "Q2/L107-110", status_word: "completed"}
  - {commitment: "NephroPlus Dialysis Index launched", implied_date: "achieved Q1FY27", ref: "Q2/L112", status_word: "completed"}
  - {commitment: "Capital deployed with discipline, on track for long-term value creation", implied_date: "ongoing/undated", ref: "Q3/L126-128", status_word: "underway"}
gate_a3: pass
blank_checks: []
```
