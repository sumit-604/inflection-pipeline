# A3 FORENSIC NOTES — Park Medi World Limited (PARKHOSPS) — Q1 FY27 — Doctype: results

Agent: A3 (Forensic Notes) | Model: claude-opus-4-8
Source extract: extract_results_parkhosps_q1fy27.txt (712 lines incl. header, 15 pages)
Ledger: ledger_results_parkhosps_q1fy27.md (GATE A2 pass)
Prior-quarter extract: NONE (first quarterly run; F5 EoM diff and F15 entity diff assessed on face)
Ledger reconciliation: 100% (all 8 categories / 141 counted rows read at cited lines before judging)
Unit: Rs Millions (x0.1 to Cr). Columns: Q1 FY27 | Q4 FY26 | Q1 FY26 | FY26 (full year).

Doctype applicability: F1–F15 apply; **F16 and F17 are N.A.** (results filing, no deck, no transcript).

---

## FINDINGS TABLE

| id | check | ledger row ref | line | verbatim quote | classification | forward implication |
|----|-------|----------------|------|----------------|----------------|---------------------|
| A3-01 | F1 | §3 / §2A r13 / §2B r13 | 178, 431, 501 | "IV Exceptional items  -  -  -  -" | FORWARD-SIGNAL | Exceptional-items line stands nil in all four periods of both statements even though a subsidiary (Devina Derma, 55% sold for Rs 0.60mn, line 501) was divested in-quarter and Rs 2,840mn of acquisitions are announced (V3 Rs 1,770mn + Mehar Rs 1,070mn). The disposal gain/loss location is unexplained; template line anticipates future acquisition gains / impairments / profit-on-sale and is likely to populate as M&A closes. Asymmetry: standalone "Income tax relating to previous years" is nil all periods (line 183) while the identical consolidated line is populated (line 436). |
| A3-02 | F2 | §2A vs §2B (r1,2,12; PBT) | 165-179, 418-432 | standalone "Profit/(Loss) before exceptional items and tax (I-II)  17.11 ... 60.93" | FORWARD-SIGNAL | Standalone PBT collapsed 72% YoY (60.93→17.11) while consolidated PBT rose 28% (818.99→1,050.84); S-vs-C gap widened by far more than 5pp of standalone PAT (=FINDING trigger). Standalone core is loss-making: revenue 335.32 − expenses 364.89 = (29.57) operating loss, lifted to +17.11 PBT only by Other income 46.68 (line 166), which by itself exceeds PBT. Parent earnings are effectively interest on unutilised IPO cash; as that cash deploys into V3/Mehar the prop shrinks. Standalone employee +143%, professional fees +219%, depreciation +191% = Panchkula greenfield ramp drag ahead of revenue; finance cost fell 32.98→8.60 (IPO deleveraging). A4 question: composition of the Rs 46.68mn standalone other income. |
| A3-03 | F4 | §5B para 7 | 342-353 | "The interim financial results of 2 subsidiaries have been reviewed by the Management of the Company" | AMBIGUOUS | Rs 743.68mn PAT (717.68 other-auditor + 26.00 management) = **83.9% of consolidated PAT (885.93)** not reviewed by the principal auditor; of which Rs 26.00mn (2.9% of PAT) across 2 subsidiaries is reviewed by **no auditor at all**. Both clear the 10%-of-PAT threshold. A4 question: identity and control status of the 2 management-reviewed subsidiaries; concentration of assurance risk. |
| A3-04 | F5 | §5A para 5 / §5B para 5 | 133-138, 320-326 | "the corresponding quarter ended June 30, 2025 ... which were not subject to limited review" | NEUTRAL-FACT | Going Concern **NOT FOUND** in either report (confirmed absent, not silently omitted). No prior-quarter extract available to verbatim-diff EoM. On face: EoM-type paragraph confirms Q1 FY26 comparatives were never reviewed and Q4 FY26 are balancing figures — so the standalone YoY collapse in A3-02 is measured against an unreviewed base. Baseline capture for future QoQ diffing. |
| A3-05 | F6 | §1A n3/n4/n8, §1B n4, §4 i2/i3, §8 | 223-231, 264, 490, 618-654 | "the proposed capacity addition is to be completed by November 2026" | FORWARD-SIGNAL | Dense dated commitment stack — see Commitment Register. Near-term milestones: Palam Vihar +100 beds by Nov 2026; Mohali +150 beds; Mehar completion Dec 3 2026; V3 remaining 20% by Apr 30 2030; "~1,500 beds ... 46% capacity addition" in 12 months; "~5,800 beds by March 2028". First-quarter capture (no prior status-transitions to compare); feeds Role 5 promise-vs-delivery and FTTCP catalyst timeline. |
| A3-06 | F8 | §2B r16/r17, §2A r16 | 435, 436, 182 | consolidated "Deferred tax charge/(benefit)  (93.40)  68.25" | FORWARD-SIGNAL | Consolidated deferred-tax **sign flip**: Rs 93.40mn benefit Q1 FY27 vs Rs 68.25mn charge Q4 FY26 — a Rs 161.65mn QoQ swing — cut consolidated ETR to 15.7% (vs 25.7% Q4; statutory 25.17%), a **~889 bps shield ≈ Rs 93mn of reported PAT**; ex-benefit PAT ~Rs 792mn vs reported 885.93. Persistent-credit pattern = DTA/carryforward = future ETR step-up (PAT headwind). "Income tax relating to previous years" non-zero (2.67) (line 436) independently trips the FINDING rule. Standalone booked opposite-sign deferred **charge** 2.83 on 36.6% ETR — S/C sign divergence. A4 question: driver of the Rs 93.40mn deferred benefit (acquisition-related DTA?). |
| A3-07 | F9 | §2B r20 | 441 | consolidated "Remeasurement of employee defined benefit plans  (7.76)  4.15" | AMBIGUOUS | Consolidated actuarial remeasurement swung to (7.76) loss from +4.15 — an Rs 11.91mn QoQ reversal and sign flip ≈ 92% of the entire FY26 movement (12.88) in a single quarter. Below the strict "exceeds full prior year" bright line (7.76 < 12.88) but close enough to flag as a probable discount-rate / plan-asset assumption change. Verify assumptions at the Annual Report. A4 question. |
| A3-08 | F13 | §4 i2/i3, §7C, §1C | 62-72, 259, 532, 584 | "Variation in the objects of the Initial Public Offer Proceeds ... subject to approval of the Shareholders by way of Postal Ballot" | FORWARD-SIGNAL | Postal-ballot notice incoming to vary IPO objects while only Rs 648.32mn IPO proceeds remain pending (lines 259/532) against Rs 2,840mn of announced acquisitions (V3 1,770 + Mehar 1,070) — variation likely reallocates the medical-equipment / NCR-capex heads and/or signals external-funding need. Trigger-#4 check: Mehar Rs 107 Cr / 150 beds = **Rs 0.71 Cr/bed**; V3 Rs 177 Cr / 330 beds = **Rs 0.54 Cr/bed** — both **below** the Rs 1.0 Cr/bed thesis-broken threshold, so that trigger does NOT trip. No AR/AGM/director-term item in this board outcome (no Role 6 AR event scheduled). A4 question: scope of the IPO object variation. |
| A3-09 | F14 | §5A sig, §1A/§1B n5, §1C, §6 | 147, 234, 497, 255, 529, 389-395 | standalone review report "Membership Number:" [blank] vs consolidated "Membership Number: 080475" | CONFIRMATORY-NEGATIVE | Same partner (P.C. Agiwal), same date, membership number printed on the consolidated report (line 365) but blank on the standalone (line 147). Plus entity-name inconsistencies: "Healplus" (234) vs "Heal Plus" (497) same CIN; "Ratangiri" (255/397) vs "Ratnagiri" (529); "Heathcare"/"Helathcare" typos (389/390/395); consolidated IPO table drops the "Total" subtotal row present standalone (257 vs 519-532). Individually immaterial; cumulatively a drafting-quality / control-environment data point corroborating the standing governance flag (IT audit-trail not enabled). |
| A3-10 | F15 | §6 r20, §6A | 233-234, 396-401 | Healplus "incorporated a wholly owned subsidiary ... on May 20, 2026" (absent from 23-row list) | AMBIGUOUS | No prior-quarter extract to diff. On face: (1) Healplus/Heal Plus, incorporated 20-May-2026 (before 30-Jun period end) as a step-down subsidiary, is **omitted** from the Annexure-I consolidation list; the note explains no financial impact (not commenced ops) but not the list omission — A4 question. (2) Devina Derma exit 5-Jun-2026 (55% for Rs 0.60mn, line 401) reconciles arithmetically with review para 7 (23 = 1 parent + 22 subs; para 7 covers 21; residual = Devina). Entity list is a moving target under heavy M&A; establishes the QoQ-diff baseline. |

---

## CHECKLIST SCORECARD (all 17)

| # | Status | One-line basis |
|---|--------|----------------|
| F1 | **FINDING** | Exceptional-items nil all periods (l.178/431) through a divestment quarter and ahead of Rs 2,840mn M&A; disposal-result location unexplained → A3-01. |
| F2 | **FINDING** | Standalone PBT −72% YoY vs consolidated +28%; parent core loss-making, propped by other income > PBT (l.166) → A3-02. |
| F3 | PASS | Cost lines diverge massively S vs C (employee 87.54 vs 924.07; materials 54.19 vs 771.24) — subsidiaries are the operating entities, no shell pattern; no Going Concern to pair. |
| F4 | **FINDING** | 83.9% of consolidated PAT rests on other/management review; Rs 26.00mn PAT (2 subs) reviewed by no auditor (l.351) → A3-03. |
| F5 | **FINDING** | Going Concern absent (both reports); no prior to diff; EoM-type para confirms Q1 FY26 comparatives unreviewed (l.137) → A3-04. |
| F6 | **FINDING** | Dense dated commitment stack across notes 3/4/8, consol note 4, board items, press release → A3-05 + Commitment Register. |
| F7 | PASS | Notes carry no new risk hedges (revenue lumpiness / concentration / impairment); only a routine procedural "subject to shareholder approval" in the board letter (l.69), outside the notes proper. |
| F8 | **FINDING** | Consolidated deferred-tax sign flip (93.40 benefit vs 68.25 charge), ~889 bps ETR shield; prior-year tax credit (2.67) non-zero (l.435/436) → A3-06. |
| F9 | **FINDING** | Consolidated actuarial remeasurement (7.76), Rs 11.91mn QoQ reversal ≈ 92% of full FY26 move in one quarter — probable assumption change (l.441) → A3-07. |
| F10 | PASS | Paid-up 768.80→863.86 traces to IPO (Dec 2025 prospectus, l.68); EPS basic = diluted in all periods (l.195-196/460-461) — no dilutive instruments. |
| F11 | PASS | Other Equity populated annual-column only per interim convention (l.193/458); no third-party net-worth figure in the filing to reconcile against — nothing to gap. |
| F12 | PASS | Single reportable segment "Healthcare Service", one geography (Ind AS 108, l.506); no segment asset/liability disaggregation exists to test for build/unwind. |
| F13 | **FINDING** | IPO object variation → postal ballot; announced M&A (Rs 2,840mn) exceeds pending IPO funds (Rs 648mn); trigger-#4 not tripped (l.68) → A3-08. |
| F14 | **FINDING** | Blank membership number on standalone review report + entity-name/subtotal-row inconsistencies (l.147 etc.) → A3-09. |
| F15 | **FINDING** | Healplus incorporated 20-May but omitted from entity list; Devina Derma exit 5-Jun; no prior to diff (l.233/401) → A3-10. |
| F16 | **N.A.** | Presentation-specific; this is a results filing, no deck. |
| F17 | **N.A.** | Concall-specific silence audit; no transcript in scope. |

Tally: 10 FINDING, 5 PASS, 2 N.A. = 17. No blanks. **GATE A3: pass.**

---

## COMMITMENT REGISTER (F6)

| # | commitment | implied date | note/ref | status word |
|---|-----------|--------------|----------|-------------|
| 1 | Panchkula 350-bed multi-super-specialty hospital launched | 10 Apr 2026 (done) | std note 3 / consol note 3 (l.223/486) | completed |
| 2 | Palam Vihar / "Park Hospital Platinum" +100 beds (Umkal), ~Rs 250mn internal accruals | by Nov 2026 | std note 4 (l.228-231) | underway (proposed) |
| 3 | RGS Healthcare Mohali expansion 350→500 beds (+150), ~Rs 400mn internal accruals | no date given | consol note 4 (l.490) | proposed |
| 4 | Healplus / Heal Plus Medical Services incorporated (WOS of Park Medicenters) | 20 May 2026 incorporated; ops not commenced | notes 5 (l.233/497) | initiated (pending commencement) |
| 5 | V3 Healthcare (Rudrapur, 330 beds) — 80% acquired, hospital launched; remaining 20% pending; ~Rs 1,770mn | 80% done 31 Jul 2026; launch 2 Aug 2026; 20% by 30 Apr 2030 | notes 8/9 (l.264/537) | completed (80%) / pending (20%) |
| 6 | Mehar Hospital-Zirakpur (Mehar Mediserve LLP) 100% cash, Rs 107 Cr, 150+ beds | completion 3 Dec 2026; commissioning Nov 2026 | board item 2 / Annexure-II (l.62/584/618) | underway (agreement executed) |
| 7 | IPO object variation — postal ballot notice to be sent | "in due course" | board item 3 (l.68-72) | proposed |
| 8 | Narela, Delhi 200-bed commissioning | over balance of FY27 | press release (l.652) | underway |
| 9 | ~1,500 beds / 46% capacity addition; total ~5,800 beds | ~1,500 within 12 months; ~5,800 by Mar 2028 | press release (l.654/673) | in process |

Status-transition note: no prior-quarter extract exists, so no initiated→underway→completed transitions can be confirmed this run; register is the baseline for the Role 5 promise-vs-delivery tracker.

---

## FOR A4 (questions to generate)

FORWARD-SIGNAL → A3-01, A3-02, A3-05, A3-06, A3-08.
AMBIGUOUS → A3-03, A3-07, A3-10.
Highest-priority management questions: (a) composition of Rs 46.68mn standalone other income and whether standalone core is structurally loss-making [A3-02]; (b) driver of the Rs 93.40mn consolidated deferred-tax benefit and normalized go-forward ETR [A3-06]; (c) identity/controls of the 2 management-only-reviewed subsidiaries [A3-03]; (d) funding path for Rs 2,840mn M&A vs Rs 648mn pending IPO funds and the IPO object-variation scope [A3-08]; (e) why Healplus is omitted from the consolidation entity list despite pre-period-end incorporation [A3-10].

```yaml
stage: A3-forensics
company: "PARKHOSPS"
quarter: "Q1 FY27"
doctype: "results"
model: claude-opus-4-8
status: complete
forensics_path: "/home/user/inflection-pipeline/runs/parkhosps-q1fy27/work/forensics_results_parkhosps_q1fy27.md"
ledger_reconciled_pct: 100
checklist:
  F1: FINDING
  F2: FINDING
  F3: PASS
  F4: FINDING
  F5: FINDING
  F6: FINDING
  F7: PASS
  F8: FINDING
  F9: FINDING
  F10: PASS
  F11: PASS
  F12: PASS
  F13: FINDING
  F14: FINDING
  F15: FINDING
  F16: N.A.
  F17: N.A.
findings:
  - {id: "A3-01", check: "F1", line: "178/431/501", classification: "FORWARD-SIGNAL", implication: "Exceptional line nil through a divestment quarter and ahead of Rs 2,840mn M&A; disposal-result location unexplained; line likely to populate as acquisitions close"}
  - {id: "A3-02", check: "F2", line: "165-179/418-432", classification: "FORWARD-SIGNAL", implication: "Standalone PBT -72% YoY vs consolidated +28%; parent core loss-making, rescued by other income 46.68 > PBT 17.11; prop shrinks as IPO cash deploys"}
  - {id: "A3-03", check: "F4", line: "342-353", classification: "AMBIGUOUS", implication: "83.9% of consolidated PAT not principal-auditor-reviewed; Rs 26.00mn PAT (2 subs) reviewed by no auditor; above 10% threshold"}
  - {id: "A3-04", check: "F5", line: "133-138", classification: "NEUTRAL-FACT", implication: "Going concern absent both reports; Q1 FY26 comparatives never reviewed, so YoY collapse measured against unreviewed base; QoQ diff baseline"}
  - {id: "A3-05", check: "F6", line: "223-231/264/490/618-654", classification: "FORWARD-SIGNAL", implication: "Dense dated commitment stack (beds/acquisitions/postal ballot); feeds Role 5 promise-vs-delivery and FTTCP timeline"}
  - {id: "A3-06", check: "F8", line: "435-436/182", classification: "FORWARD-SIGNAL", implication: "Consolidated deferred-tax sign flip; ~889 bps ETR shield ~Rs 93mn PAT; ETR normalization is a future PAT headwind; prior-year tax credit non-zero"}
  - {id: "A3-07", check: "F9", line: "441", classification: "AMBIGUOUS", implication: "Actuarial remeasurement (7.76) QoQ reversal ~92% of full FY26 move; probable discount-rate/plan-asset assumption change; verify at AR"}
  - {id: "A3-08", check: "F13", line: "62-72", classification: "FORWARD-SIGNAL", implication: "IPO object variation via postal ballot; Rs 2,840mn M&A vs Rs 648mn pending IPO funds signals reallocation/external funding; trigger-#4 not tripped"}
  - {id: "A3-09", check: "F14", line: "147/234/497/255/529", classification: "CONFIRMATORY-NEGATIVE", implication: "Blank membership number on standalone report + entity-name/subtotal inconsistencies; drafting/control-environment data point"}
  - {id: "A3-10", check: "F15", line: "233-234/396-401", classification: "AMBIGUOUS", implication: "Healplus omitted from entity list despite pre-period-end incorporation; Devina Derma exit reconciles; entity-list QoQ baseline"}
forward_signals: ["A3-01", "A3-02", "A3-05", "A3-06", "A3-08"]
ambiguous: ["A3-03", "A3-07", "A3-10"]
commitments:
  - {commitment: "Panchkula 350-bed hospital launched", implied_date: "2026-04-10", ref: "std/consol note 3 (l.223/486)", status_word: "completed"}
  - {commitment: "Palam Vihar Park Platinum +100 beds, ~Rs 250mn", implied_date: "2026-11", ref: "std note 4 (l.228)", status_word: "underway"}
  - {commitment: "RGS Mohali expansion 350->500 beds, ~Rs 400mn", implied_date: "none stated", ref: "consol note 4 (l.490)", status_word: "proposed"}
  - {commitment: "Healplus/Heal Plus WOS incorporated", implied_date: "2026-05-20", ref: "notes 5 (l.233/497)", status_word: "initiated"}
  - {commitment: "V3 Healthcare Rudrapur 80% acquired; 20% pending; ~Rs 1,770mn", implied_date: "2026-07-31 (80%); 2030-04-30 (20%)", ref: "notes 8/9 (l.264/537)", status_word: "completed-80/pending-20"}
  - {commitment: "Mehar Hospital-Zirakpur 100% cash Rs 107 Cr", implied_date: "2026-12-03", ref: "board item 2 / Annexure-II (l.62/584)", status_word: "underway"}
  - {commitment: "IPO object variation postal-ballot notice", implied_date: "in due course", ref: "board item 3 (l.68)", status_word: "proposed"}
  - {commitment: "Narela Delhi 200-bed commissioning", implied_date: "FY27", ref: "press release (l.652)", status_word: "underway"}
  - {commitment: "~1,500 beds / ~5,800 total capacity", implied_date: "~12 months / by 2028-03", ref: "press release (l.654/673)", status_word: "in-process"}
gate_a3: pass
blank_checks: []
```
