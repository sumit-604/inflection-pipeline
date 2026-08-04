# A3 FORENSIC NOTES — Park Medi World Limited (PARKHOSPS) | Q1 FY27 | doctype: PRESENTATION

Source extract: `extract_presentation_parkhosps_q1fy27.txt` (26 pages, unit Rs Millions, x0.1 to Cr; OCR pages 7/16/20/23)
Source ledger: `ledger_presentation_parkhosps_q1fy27.md` (GATE A2 pass; 26 slides, 341 number rows, 14 footnotes)
Prior-quarter deck: NONE supplied — F16 dropped/reframed disclosures assessed "no prior deck to diff"; instead axis starts / chart baselines / softened language judged on their face.

Ledger reconciliation: 100%. Every Section-1 slide row, all 341 Section-2 number rows (incl. 115 CHART_AXIS_ARTIFACT + 125 CHART_DATA_LABEL), the Section-3 dropped-slide note, and all 14 Section-4 footnotes were read at their cited lines before judging. The one `ZERO_STANDING` flag (L414/L506) and the one `PARTIAL_OWNERSHIP` flag (L409/L533) were both worked.

Conservative bias applied: where a chart-artifact value could not be trusted as a free-standing data point (per A2's caveat), it was verified against the labelled P&L (slide 24) or the labelled build chart (slide 18) rather than read off the scrambled chart page.

---

## FINDINGS TABLE

| id | check | ledger row ref | line/slide | verbatim quote | classification | forward implication |
|---|---|---|---|---|---|---|
| A1 | F1 | Sec4 ZERO_STANDING (row L414); Sec2 #143 | slide 10 / L506 | "(Rudrapur was commissioned on 2nd Aug'26 and had nil contribution in Q1 FY'27)" | FORWARD-SIGNAL | Q2 FY27 is the first quarter to carry any Rudrapur P&L. The 65%/69%/77% acquisition-contribution donuts on slide 10 exclude the 330-bed 12th acquisition; next quarter's mix and a first minority-interest line (only 80% owned) both step-change. |
| A2 | F6 | Sec2 #35-37, #216-239; Sec1 slide 17/18 | slides 5/17/18 / L174-175, L763-812 | "we expect to exit FY'27 at 4,740 beds and, adding a further 1,000 beds through FY'28, to reach 5,740 beds by March 2028" | FORWARD-SIGNAL | Dense dated bed/commissioning roadmap (see Commitment Register). Each dated line is a promise-vs-delivery checkpoint for Role 5; several land in Q2/Q3 FY27 (Zirakpur Nov'26, Palam Vihar Nov'26, Narela Dec'26). |
| A3 | F7 | Sec2 #37, #242-246; Sec1 slide 19 | slides 5/19 / L175-176, L843-844, L854 | "funded largely through internal accruals and IPO proceeds, without recourse to any material fresh debt" | AMBIGUOUS | Funding of a 2,130-bed (+59%) build is hedged three ways — "largely," "material," and an explicit equity backstop ("future equity raise if required," "capacity to raise capital for unidentified acquisitions"). Pre-emptive cover for a possible dilution / debt-drawdown next year. A4 question. |
| A4 | F8 | Sec2 #316-318 (slide 24 P&L) | slide 24 / L1025-1026 | "Tax  165  164  1%  266  -38%" (vs PBT "1,051  819  28%  1,034") | FORWARD-SIGNAL | Effective tax rate collapsed to 15.7% (Q1FY27) from 20.0% (Q1FY26) and 25.7% (Q4FY26) against 25.17% statutory — tax flat +1% YoY while PBT +28%. The +35% PAT headline is flattered by a low ETR and a -35% finance-cost drop; EBITDA grew only 20%. ETR normalisation is a future earnings headwind. (See note below on injected-input deviation.) |
| A5 | F10 | Sec2 #320, #326; Sec1 slide 19 | slides 24/25/19 / L1029, L1046, L852-854 | "EPS (INR)  2.05  1.70  20%  1.78  15%" | FORWARD-SIGNAL | PAT +35% YoY but EPS only +20% — implied share count rose ~385m (655/1.70) to ~432m (886/2.05, = 431,930,864 disclosed), i.e. the Dec-2025 IPO diluted EPS growth by ~12%. Only a single (basic) EPS shown, no diluted line. Slide 19 flags further dilution headroom "up to regulatory threshold (~75%)" from 82.9% promoter holding. Forward EPS dilution risk. |
| A6 | F14 | Sec4 PARTIAL_OWNERSHIP (row L409); Sec2 #29, #161 | slides 5/10 / L167 vs L533 | slide 5: "acquire 100% of 'The Medicity Hospital'" — slide 10 fn: "consideration paid for 80% ownership is INR 1,416 mn … Remaining 20% to be acquired by FY'30" | AMBIGUOUS | Chairman letter frames Rudrapur as a 100% acquisition; slide-10 footnote reveals a staged 80%-now / 20%-by-FY30 structure. Inconsistent framing conceals (a) a deferred cash outflow to FY30 and (b) a minority-interest deduction against consolidated PAT until then. A4 question on put/call terms and price of the 20%. |
| A7 | F16 | Sec2 #77 (L304), #103 (L387), #94 (L361) | slide 6 / L304, L387, L361 | secondary occupancy axis runs "110.0%" (L304) down to "-10.0%" (L387) | AMBIGUOUS | Occupancy secondary axis is scaled -10% to 110% — including impossible negative-occupancy territory stretches the plot so the 67.8%→62.5%→55.6% path (a 12.2pp YoY / 6.9pp QoQ fall) occupies a small vertical fraction and reads shallow. Axis choice flatters the single worst operating metric in the deck. |
| A8 | F16 | Sec2 #76 (L303), #81(L320); Sec1 slide 6 | slide 6 / L303, L310, L331, L339 | "Occupancy has moderated due to addition of significant capacity" | FORWARD-SIGNAL | "Moderated" softens a 12.2pp YoY decline and attributes it wholly to the denominator (new beds), implying no same-store weakness. Unverifiable without ARPOB / same-store occupancy — which the deck does not give. Occupancy at 55.6% on 3,960 beds means ~1,760 beds are empty; Q2 ramp of Agra/Panchkula/Rudrapur is the swing factor. |
| A9 | F16 | Sec1 slide 19 (L830, L848) | slide 19 / L830, L848 | "higher patient volumes & ARPOB" (L830); "Improving ARPOB, case mix and overall efficiency" (L848) | AMBIGUOUS | ARPOB is named twice as a growth/quality driver but is never quantified anywhere in the 26 slides — no level, no delta, no Platinum figure. A key metric on the Notion monitorable list (Platinum ARPOB delta vs ₹29,725) is asserted-improving but undisclosed. A4 question: disclose ARPOB and same-store occupancy. |

---

## CHECKLIST SCORECARD (all 17)

| Check | Status | One-line basis |
|---|---|---|
| F1  ZERO-VALUE STANDING ITEMS | **FINDING** (A1) | One ZERO_STANDING row: Rudrapur nil Q1 contribution (L506); first contribution + minority line arrive Q2FY27. |
| F2  STANDALONE vs CONSOLIDATED | **N.A.** | Deck carries only a consolidated P&L (slide 24); no standalone column to decompose. |
| F3  SHELL-ENTITY DETECTION | **N.A.** | No standalone-vs-consolidated cost lines in a presentation. |
| F4  UNAUDITED CONTRIBUTION | **N.A.** | No auditor Other-Matters paragraph; deck is management-prepared, "not independently verified" (L112). |
| F5  GOING CONCERN / EoM | **N.A.** | No auditor EoM / going-concern paragraph in a deck. |
| F6  FORWARD-COMMITMENT MINING | **FINDING** (A2) | Rich dated bed/commissioning/capex commitment set — see Commitment Register. |
| F7  HEDGE PHRASE MINING | **FINDING** (A3) | Funding hedges: "largely," "material," "if required," "unidentified acquisitions" around a +59% bed build (L175-176, L843-844, L854). |
| F8  TAX FORENSICS | **FINDING** (A4) | Slide-24 P&L carries Tax + PBT; ETR fell to 15.7% vs 25.17% statutory (tax +1% YoY, PBT +28%). Deviation from injected N.A. guidance justified below. |
| F9  OCI FORENSICS | **N.A.** | No OCI / actuarial disclosure in the deck. |
| F10 SHARE COUNT & DILUTION | **FINDING** (A5) | PAT +35% vs EPS +20% = ~12% IPO dilution; single basic EPS; explicit further dilution headroom to ~75% (L852-854, L1029, L1046). |
| F11 RESERVES / NET WORTH | **N.A.** | No balance sheet / net-worth figure and no third-party (rating) net-worth to tie out. |
| F12 SEGMENT FORENSICS | **N.A.** | No segment assets/liabilities tables in the deck. |
| F13 BOARD OUTCOME BEYOND RESULTS | **N.A.** | No AR/Board's-Report/AGM-notice/record-date/director-term content; board-approved Palam Vihar expansion captured under F6. |
| F14 NOTE-DRAFTING INCONSISTENCIES | **FINDING** (A6) | "acquire 100%" (L167) vs footnote "80% ownership … Remaining 20% … by FY'30" (L533). |
| F15 ENTITY-LIST DIFFS | **N.A.** | No consolidation entity list and no prior deck to diff. |
| F16 DROPPED / REFRAMED DISCLOSURES | **FINDING** (A7, A8, A9) | Occupancy axis -10%/110% flatters the drop; "moderated" softening; ARPOB named but never quantified. |
| F17 CONCALL SILENCE AUDIT | **N.A.** | Document is a presentation, not a transcript. |

Blank checks: none. **GATE A3: PASS.**

---

## COMMITMENT REGISTER (from F6)

| # | Commitment | Implied date | Ref (line) | Status word |
|---|---|---|---|---|
| C1 | Panchkula 350-bed super-speciality hospital commissioned | 10 Apr 2026 (done) | L756 | completed |
| C2 | Rudrapur (The Medicity, 330 beds) commissioned / launched | 2 Aug 2026 (done) | L169, L765-767 | completed |
| C3 | Rudrapur remaining 20% ownership to be acquired | by FY'30 | L533 | intends (deferred) |
| C4 | Palam Vihar / Park Platinum +100 beds (225→325), operate as Park Platinum | Nov 2026 | L759-760, L797 | board-approved / underway |
| C5 | Narela, Delhi 200-bed hospital (insolvency-acquired) | Dec 2026 | L171, L811-812 | on track / underway |
| C6 | Zirakpur (Mehar Hospital) 150-bed acquisition + launch | Nov 2026 | L172, L763-765, L792 | signed agreement / expected |
| C7 | Mohali expansion +150 (350→500) | Sep 2027 | L762-763 ("ongoing 150 bed expansion"), L788 | underway |
| C8 | Ambala expansion +200 (250→450) | Oct 2027 | L794 | planned |
| C9 | Rohtak greenfield 250 beds | Jan 2028 | L791 | planned |
| C10 | Gorakhpur acquisition (O&M) 400 beds | Apr 2027 | L810 | planned |
| C11 | Exit FY'27 at 4,740 beds | Mar 2027 (FY27-end) | L174-175 | expect / underway |
| C12 | Reach 5,740 beds (further +1,000 in FY28) | Mar 2028 | L175 | expect |
| C13 | CY2026 capacity additions of 1,490 beds (+46% over CY25 base 3,250) | CY2026 | L173-174 | will |
| C14 | Bed capacity +c.59% FY26-28, funded largely via internal accruals + IPO proceeds, no material fresh debt | FY28 | L175-176, L829, L841-842 | expect (hedged — see A3) |
| C15 | Panchkula NABH accreditation | in process | L446 | undergoing |
| C16 | Labs in 4 additional hospitals for NABL accreditation | planned | L447 | being planned |

Milestone-transition note for Role 5: C1, C2 have moved to **completed** this deck (Panchkula 10-Apr, Rudrapur 2-Aug). C4/C5/C6 all fall due within the next two quarters and become the first promise-vs-delivery tests. C3 (20% Rudrapur) and C14 (funding source) are the ones to watch for slippage or a switch to fresh debt/equity.

---

## Note on F8 injected-input deviation
The launching task listed F8 among "most balance-sheet checks … N.A." F8 (tax forensics) is a P&L check, and slide 24 carries a full consolidated P&L with explicit Tax (165/164/266) and PBT (1,051/819/1,034) lines. Marking a computable, materially anomalous ETR (15.7% vs 25.17% statutory) as N.A. would suppress exactly the forward signal A3 exists to surface. Per the conservative-bias rule and the "any numbers the deck carries" doctrine, F8 is run and marked FINDING with the computation shown. Flagged here for A4/operator visibility.

## Cross-checks worth noting (not standalone findings)
- Monitoring triggers not breached this deck: EBITDA margin 26.5% (>22% floor); no promoter-remuneration or debtor-days data in the deck (not disclosable from a P&L-only presentation) — carry forward to results/AR.
- Acquisition price/bed: Rudrapur 1,416mn / 330 beds = ~4.3mn/bed at 80% (5.4mn/bed grossed to 100% at 1,770mn valuation); Zirakpur ~107cr / 150 beds ≈ 7.1mn/bed. Both above the Notion "acquisition >Rs 1.0 Cr/bed" trigger — flagged for A4 (per-bed consideration well above the tripwire, though these are super-speciality assets).
- Slide 10 claims "11 Hospitals Successfully Acquired & Integrated" and folds Rudrapur's 1,416mn into the ₹9,991mn cumulative — yet Rudrapur had nil Q1 contribution and commissioned only 2-Aug; "integrated" is forward-leaning for the 11th. Minor; noted under A1/A6.

---

```yaml
stage: A3-forensics
company: "PARKHOSPS"
quarter: "Q1 FY27"
doctype: "presentation"
model: claude-opus-4-8
status: complete
forensics_path: "/home/user/inflection-pipeline/runs/parkhosps-q1fy27/work/forensics_presentation_parkhosps_q1fy27.md"
ledger_reconciled_pct: 100
checklist:
  F1: FINDING
  F2: N.A.
  F3: N.A.
  F4: N.A.
  F5: N.A.
  F6: FINDING
  F7: FINDING
  F8: FINDING
  F9: N.A.
  F10: FINDING
  F11: N.A.
  F12: N.A.
  F13: N.A.
  F14: FINDING
  F15: N.A.
  F16: FINDING
  F17: N.A.
findings:
  - {id: "A1", check: "F1", line: "L506 (slide 10)", classification: "FORWARD-SIGNAL", implication: "Rudrapur nil Q1; first P&L contribution + minority line hit Q2FY27; slide-10 acquisition donuts exclude the 12th asset"}
  - {id: "A2", check: "F6", line: "L174-175, L763-812 (slides 5/17/18)", classification: "FORWARD-SIGNAL", implication: "Dated bed/commissioning roadmap to 4,740 (FY27) and 5,740 (FY28); Q2/Q3 milestones become promise-vs-delivery tests"}
  - {id: "A3", check: "F7", line: "L175-176, L843-844, L854 (slides 5/19)", classification: "AMBIGUOUS", implication: "Funding of +59% build hedged; explicit equity backstop signals possible dilution or fresh debt next year"}
  - {id: "A4", check: "F8", line: "L1025-1026 (slide 24)", classification: "FORWARD-SIGNAL", implication: "ETR 15.7% vs 25.17% statutory; +35% PAT flattered by low tax + -35% finance cost; ETR normalisation is a future headwind"}
  - {id: "A5", check: "F10", line: "L1029, L1046, L852-854 (slides 24/25/19)", classification: "FORWARD-SIGNAL", implication: "PAT +35% vs EPS +20% = ~12% IPO dilution; further dilution headroom to ~75% flagged"}
  - {id: "A6", check: "F14", line: "L167 vs L533 (slides 5/10)", classification: "AMBIGUOUS", implication: "'100%' framing vs 80%-now/20%-by-FY30 reality; deferred cash outflow + interim minority interest concealed"}
  - {id: "A7", check: "F16", line: "L304/L387/L361 (slide 6)", classification: "AMBIGUOUS", implication: "Occupancy axis -10% to 110% flatters the 67.8%->55.6% decline visually"}
  - {id: "A8", check: "F16", line: "L303/L310/L331/L339 (slide 6)", classification: "FORWARD-SIGNAL", implication: "'moderated … addition of significant capacity' softens 12.2pp YoY drop; ~1,760 empty beds; Q2 ramp is the swing"}
  - {id: "A9", check: "F16", line: "L830/L848 (slide 19)", classification: "AMBIGUOUS", implication: "ARPOB touted as improving but never quantified; Platinum ARPOB vs Rs29,725 monitorable unverifiable"}
forward_signals: ["A1", "A2", "A4", "A5", "A8"]
ambiguous: ["A3", "A6", "A7", "A9"]
commitments:
  - {commitment: "Panchkula 350-bed hospital commissioned", implied_date: "2026-04-10", ref: "L756", status_word: "completed"}
  - {commitment: "Rudrapur 330-bed commissioned/launched", implied_date: "2026-08-02", ref: "L169/L765-767", status_word: "completed"}
  - {commitment: "Rudrapur remaining 20% ownership acquired", implied_date: "by FY30", ref: "L533", status_word: "intends"}
  - {commitment: "Palam Vihar/Park Platinum +100 beds (225->325)", implied_date: "2026-11", ref: "L759-760/L797", status_word: "board-approved/underway"}
  - {commitment: "Narela Delhi 200-bed hospital", implied_date: "2026-12", ref: "L171/L811-812", status_word: "on-track/underway"}
  - {commitment: "Zirakpur (Mehar) 150-bed acquisition+launch", implied_date: "2026-11", ref: "L172/L763-765/L792", status_word: "signed/expected"}
  - {commitment: "Mohali expansion +150 (350->500)", implied_date: "2027-09", ref: "L762-763/L788", status_word: "underway"}
  - {commitment: "Ambala expansion +200 (250->450)", implied_date: "2027-10", ref: "L794", status_word: "planned"}
  - {commitment: "Rohtak greenfield 250 beds", implied_date: "2028-01", ref: "L791", status_word: "planned"}
  - {commitment: "Gorakhpur acquisition O&M 400 beds", implied_date: "2027-04", ref: "L810", status_word: "planned"}
  - {commitment: "Exit FY27 at 4,740 beds", implied_date: "2027-03", ref: "L174-175", status_word: "expect"}
  - {commitment: "Reach 5,740 beds", implied_date: "2028-03", ref: "L175", status_word: "expect"}
  - {commitment: "CY2026 capacity additions 1,490 beds", implied_date: "CY2026", ref: "L173-174", status_word: "will"}
  - {commitment: "+c.59% beds FY26-28 funded via accruals/IPO, no material fresh debt", implied_date: "FY28", ref: "L175-176/L829/L841-842", status_word: "expect"}
  - {commitment: "Panchkula NABH accreditation", implied_date: "in-process", ref: "L446", status_word: "undergoing"}
  - {commitment: "Labs in 4 hospitals NABL accreditation", implied_date: "planned", ref: "L447", status_word: "being-planned"}
gate_a3: pass
blank_checks: []
```
