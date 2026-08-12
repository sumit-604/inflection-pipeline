# A3 FORENSIC NOTES — NephroPlus (Nephrocare Health Services Ltd) — Q1 FY27 — DOCTYPE: CONCALL

Source extract: `extract_concall_nephroplus_q1fy27.txt` (126 source lines; transcript source-line
numbering used throughout, i.e. "line 12" = transcript source line 12 = file line 26).
Ledger: `ledger_concall_nephroplus_q1fy27.md`. Ledger reconciliation: 100% — every one of the
17 participant rows, 103 turn rows, 36 question rows, 81 mgmt-number rows and 18 forward/hedge
rows was read at its cited line in the extract before judging.

Call: IIFL Capital host. Management present & speaking: Vikram Vuppala (CMD, 13 turns), Rohit
Singh (Group CEO, 17), Prashant Goenka (Group CFO, 14). Kamal D Shah (Co-founder) introduced
3x, ZERO attributed turns — `SILENT_PARTICIPANT` (governance neutral-fact; CMD present so no
MGMT_ABSENCE). Spoken figures Rs Cr x1.

Doctype applicability: F6/F7/F17 are the core concall checks. F2-F5, F9-F13 are
statutory/balance-sheet apparatus absent from a transcript → N.A. with one-line reason. F1, F8,
F14, F15, F16 are run because the transcript verbally carries their subject matter (near-nil
standing items, tax rates, internal number inconsistencies, a new entity incorporation, and a
reframed/non-GAAP disclosure).

---

## FILING CROSS-CHECK (management numbers vs the filed results — the filing is the anchor)

| Mgmt claim (line) | Spoken | Filed anchor | Verdict |
|---|---|---|---|
| Revenue (l.10/12) | Rs 282 Cr, +23.7% | Rs 281.75 Cr | MATCH (rounding) |
| Adj EBITDA (l.12) | Rs 65.1 Cr, +31% | non-GAAP (ex-ESOP, ex-Saudi JV) | mgmt-defined, not a filed line — see F16 |
| Adj EBITDA margin (l.12) | 23.1% vs 21.9% | — | improvement stated as +120bps (l.10) AND +125bps (l.27) — see F14.1 |
| Adj PAT (l.12) | Rs 37 Cr, +41.7%, 13.1% margin | Reported PAT Rs 31.97 Cr, +34.9% (NEVER spoken) | NON-GAAP reframing — see F16.1 |
| Guests (l.10/12) | 38,262, +13% | matches | MATCH |
| Treatments (l.10/12) | 10.3 lakh, +13.3% | matches | MATCH |
| RPT (l.12) | Rs 2,733, +9.2%, prior "253" | prior ~Rs 2,503 | "253" = dropped-digit transcription — see F14.2 |
| Clinics (l.8/10) | 550 (26 added: 19 India + 7 PH) | matches | MATCH |
| Intl mix (l.10/40) | ~45% (30% 18m ago) | matches | MATCH |
| Utilisation (l.75/119) | 74% | matches | MATCH |
| Forex (l.45) | Rs 20 lakh favourable | matches | MATCH — see F1.2 |
| Capex (l.12/47) | Rs 44 Cr (vs Rs 43 Cr PY) | matches | MATCH |
| IPO fresh-issue util (l.12) | "68% which is about 27 cr" | garbled but internally consistent (~Rs 27 Cr / 68%) | recorded verbatim, low materiality |
| Tax (l.49) | ~20% this qtr | — | below 25.17% statutory — see F8.1 |
| AR days (l.22) | 121 → 101 (20-day improvement) | matches | MATCH |
| KSA JV loss (l.61/79) | "three odd cr" | filing Rs 3.57 Cr | MATCH (rounds to 3.57) |

---

## FINDINGS TABLE

| id | check | ledger row | line/turn | verbatim quote | classification | forward implication |
|---|---|---|---|---|---|---|
| F1.1 | F1 | mgmt r63 (ZERO_STANDING) | l.58 / turn 44 | "in the last 3 months we have hardly given any new machines... Of course it's a one-time benefit you get when you bring a new technology" | FORWARD-SIGNAL | Sequential depreciation dip is explicitly one-time; dep and the margin tailwind it created do not repeat — model a dep step-up next 1-2 quarters. |
| F1.2 | F1 | mgmt r54 (ZERO_STANDING) | l.45 / turn 32 | "We only saw 20 lakhs favorable outcome due to the forex. currencies were largely flat" | NEUTRAL-FACT | +23.7% growth is operational, not FX-aided; no currency cushion (or drag) embedded this quarter. |
| F6.1 | F6 | fwd r1 | l.12 / turn 5 | "we... maintain our medium-term growth guidance of 15 to 20% over the next 3 to 5 years" | FORWARD-SIGNAL | NEW explicit numeric guidance (did not exist in prior review). Becomes the promise-vs-delivery anchor (monitoring 13). |
| F6.2 | F6 | fwd r4/r5 | l.40/47 / turns 28,32 | "to add a new international market every 12 to 18 months" | FORWARD-SIGNAL | Datable market-entry cadence; slippage past 18m = the tripwire. |
| F6.3 | F6 | fwd r6/r7 | l.47 / turn 32 | "40 to 50 clinics in India every year. 10 to 15 clinics in Philippines every year" | FORWARD-SIGNAL | Quantified rollout pace = capex proxy in absence of capex guidance (see F7.2). |
| F6.4 | F6 | fwd r3 | l.10 / turn 4 | "The first batch will begin training in the third quarter" | FORWARD-SIGNAL | Dated Q3 FY27 milestone (NIDA nurse academy); check delivery next call. |
| F6.5 | F6 | fwd r2/r9/r10 | l.10/60/62 / turns 4,46,48 | "couple of months" / "3 to four quarters away" / "one to two quarters or probably longer" | AMBIGUOUS | Three non-reconcilable Saudi tender horizons in one call. A4 question: which is the base case for tender clarity? |
| F6.6 | F6 | fwd r16/r17 | l.110/117 / turns 91,97 | "in the next 5 to 10 years we'll be in 10 to 15 countries" | FORWARD-SIGNAL | Long-dated ambition (from 5 countries); standalone model to overtake in-hospital in 5-10 yrs. |
| F6.7 | F6 | mgmt r (l.35) | l.35 / turn 23 | "in consumables we have various levers be it even contract manufacturing of low complexity consumables" | FORWARD-SIGNAL | Vertical-integration signal; a future COGS lever and possible capex/inventory line. |
| F6.8 | F6 | mgmt r7 vs fwd r1 | l.10 vs 12 | delivered "23.7%" vs guides "15 to 20%" | AMBIGUOUS | Guidance is set BELOW current run-rate. A4 question: sandbag, or signalling deceleration as India lumpy-pricing base normalises? |
| F7.1 | F7 | hedge r11 | l.62 / turn 48 | "we are not giving any guidance on the loss assumptions for the Saudi" | AMBIGUOUS | KSA loss run-rate (~Rs 3.57 Cr/qtr equity-method) undisclosed; monitoring 7. |
| F7.2 | F7 | hedge r8 | l.47 / turn 32 | "we typically don't give guidance on the capex front" | AMBIGUOUS | No capex number; only strategic clinic-count. Forces capex to be inferred from F6.3. |
| F7.3 | F7 | hedge r15 | l.40 / turn 28 | "one should not expect that same cagr number to continue forever" | FORWARD-SIGNAL | ~11% RPT CAGR is not a run-rate; realization tailwind (lumpy CGHS +35% / Philippines +55-60%) fades — RPT growth decelerates. |
| F7.4 | F7 | hedge r12/r13 | l.90/117 / turns 73,97 | "We don't provide unit economics at a country level" | AMBIGUOUS | Country-level ROCE/margin opaque; direct feed to F17 silence. |
| F7.5 | F7 | fwd r2 (tail) | l.10 / turn 4 | "these timelines are not fully within our control" | AMBIGUOUS | Pre-emptive cover on Saudi tender slippage — read as expect-delay. |
| F8.1 | F8 | mgmt r56/57/58 | l.49 / turn 36 | "20 the current number probably reflects a good proxy... India and Philippines... 25%. Uzbekistan... So is at 0% tax rate" | FORWARD-SIGNAL | ETR 20% sits below 25.17% statutory purely on Uzbekistan's 0% (conditional on healthcare >90% of its revenue). Mix shift or breach of that condition steps ETR up toward 25% — a future EPS headwind. |
| F14.1 | F14 | mgmt r9 vs r39 | l.10 vs 27 / turns 4,16 | "120 basis point" (Rohit) vs "125 basis point" (Prashant) | AMBIGUOUS | Same margin-improvement metric quoted two ways on one call. A4 question: which reconciles to the filed 23.1% vs 21.9% (=+120bps)? |
| F14.2 | F14 | mgmt r26 | l.12 / turn 5 | "2733... compared to 253 rupees... representing a growth of 9.2%" | NEUTRAL-FACT | Adjudicated: 2733 / 1.092 = Rs 2,503, so "253" is a dropped-digit transcription of ~Rs 2,503; the 9.2% claim is internally consistent. Transcription noise, not a real discrepancy. |
| F14.3 | F14 | mgmt r49 vs r76 | l.38 vs 110 / turns 26,91 | "21 22%" vs "the organized market is 20%" | NEUTRAL-FACT | Organized-share rounding, immaterial; both ~20-22%. |
| F14.4 | F14 | mgmt r5 vs r13 | l.8 vs 10 / turns 3,4 | "550 clinics across 370 cities" vs "357 cities" | NEUTRAL-FACT | City-count transcription inconsistency (370 vs 357); immaterial. |
| F15.1 | F15 | fwd (l.10/64) | l.10/64 / turns 4,50 | "we incorporated our subsidy in Kazakhstan" / "we have registered a company there but we are still exploring" | FORWARD-SIGNAL | New legal entity = vehicle for the next international market (~$75 price point). Consolidation-scope change; watch for first-loss recognition. |
| F15.2 | F15 | mgmt (l.10) | l.10 / turn 4 | "we also let go two clinics under the Utrakhan PPP that were value dilutive" | NEUTRAL-FACT | NEW disclosure: return discipline. Small negative on gross clinic count (net-of-exits); positive governance read. |
| F16.1 | F16 | mgmt r20/22/23 | l.12 / turn 5 | "adjusted path after adding back ESOP expense in Saudi J expense stood at rupes 37 cr... growth of 41.7%" | AMBIGUOUS | Non-GAAP adjusted PAT (+41.7%) headlined; reported GAAP PAT (Rs 31.97 Cr, +34.9%) is NEVER spoken on the call. Favourable reframing — the ~7pt gap between adjusted and reported growth is the A4 question. |
| F17.1 | F17 | monitoring 15-17 | l.117 / turn 97 | "we do not want to mention country by country details and go into the micro" | CONFIRMATORY-NEGATIVE | Refuses country patient/revenue splits AND same-store-style disclosure (l.117/119/120). Monitoring items 15-17 (bed count / utilisation / treatments per clinic by country) are unanswerable from disclosure by design. |
| F17.2 | F17 | monitoring 10 | whole call | [not raised by any analyst; not addressed by mgmt] | CONFIRMATORY-NEGATIVE | Captive/hospital-partner contract renewal rate (>95% monitoring threshold) never mentioned. Sustained silence on a monitoring metric = per Role 5, treat as a soft negative until confirmed. |
| F17.3 | F17 | monitoring 7 | l.62 / turn 48 | "we are not giving any guidance on the loss assumptions for the Saudi" | AMBIGUOUS | KSA revenue/loss trajectory (monitoring 7) declined despite 5 separate Saudi questions across 2 analysts (Q16/17/23/24/25) — the most-pressed, least-answered topic of the call. |

---

## CHECKLIST SCORECARD (all 17; PASS / FINDING / N.A.)

| # | Check | Status | Basis (one line) |
|---|---|---|---|
| F1 | Zero-value standing items | FINDING | 4 ZERO_STANDING ledger rows; the near-zero machine deployment (l.58) is an explicit one-time depreciation benefit → F1.1. |
| F2 | Standalone vs consolidated | N.A. | No S-vs-C statements/tables in a transcript. |
| F3 | Shell-entity detection | N.A. | No standalone-vs-consolidated cost lines to compare. |
| F4 | Unaudited contribution ratio | N.A. | No auditor "Other Matters" para in a concall (KSA JV loss cross-check handled via F8/F17). |
| F5 | Going concern / EoM scope | N.A. | No auditor EoM paragraph in a transcript. |
| F6 | Forward-commitment mining | FINDING | 8 dated/dateable commitments incl. NEW 15-20% guidance and Q3 NIDA milestone; see Commitment Register. |
| F7 | Hedge phrase mining | FINDING | 5 hedges/refusals (capex, Saudi loss, country economics, RPT-not-repeatable, "not within our control"). |
| F8 | Tax forensics | FINDING | ETR 20% < 25.17% statutory, sustained only by Uzbekistan 0% (conditional) → normalisation-up risk (F8.1). |
| F9 | OCI forensics | N.A. | No OCI / actuarial disclosure in a transcript. |
| F10 | Share count & dilution | N.A. | No paid-up capital / basic-vs-diluted EPS on the call (ESOP exists as an add-back only; no share count). |
| F11 | Reserves / net worth tie-out | N.A. | No balance-sheet equity figures spoken. |
| F12 | Segment forensics | N.A. | No segment asset/liability tables; country splits explicitly declined (captured as F17.1). |
| F13 | Board outcome beyond results | N.A. | No board/AGM/AR-approval outcome in a transcript. |
| F14 | Drafting / number inconsistencies | FINDING | 120bps vs 125bps same-call margin inconsistency (F14.1); RPT "253" adjudicated as transcription (F14.2); city-count and share-% rounding noise. |
| F15 | Entity list diffs | FINDING | Kazakhstan subsidiary newly incorporated (F15.1); 2 Uttarakhand PPP clinics let go (F15.2). |
| F16 | Dropped / reframed disclosures | FINDING | Non-GAAP adjusted PAT headlined; reported GAAP PAT (Rs 31.97 Cr / +34.9%) never spoken (F16.1). |
| F17 | Silence audit | FINDING | Country splits, same-store, country unit economics, captive-renewal rate, Saudi loss all declined/absent (F17.1-3). |

Blank checks: none. GATE A3: pass.

---

## COMMITMENT REGISTER (F6)

| Commitment | Implied date | Line / turn | Status word |
|---|---|---|---|
| Revenue growth 15-20% p.a. | Next 3-5 yrs (≈FY30-32) | l.12 / turn 5 | reiterated (NEW numeric) |
| New international market added | Every 12-18 months (rolling) | l.40/47 | ongoing |
| 40-50 India clinics per year | Annual | l.47 / turn 32 | ongoing |
| 10-15 Philippines clinics per year | Annual | l.47 / turn 32 | ongoing |
| NIDA first nurse-training batch | Q3 FY27 | l.10 / turn 4 | scheduled |
| Saudi formal MoH tender process begins | "couple of months" (~Q3 FY27) | l.10 / turn 4 | underway (RFI response submitted) |
| Saudi clear visibility / first benefits | 3-4 quarters (~Q1 FY28) | l.60 / turn 46 | underway (investment phase) |
| Saudi first Riyadh clinic operational | July 2026 | l.10 / turn 4 | completed |
| Saudi home-dialysis operations | This quarter | l.10 / turn 4 | completed |
| Tamil Nadu PPP contract signed | This quarter | l.10 / turn 4 | completed |
| Kazakhstan subsidiary incorporated | This quarter (ops model TBD, ~$75) | l.10/64 / turns 4,50 | completed (entity) / exploring (ops) |
| Operate in 10-15 countries | Next 5-10 yrs | l.117 / turn 97 | intends |
| Standalone clinics overtake in-hospital (India) | Next 5-10 yrs | l.110 / turn 91 | intends |

---

## "WHAT WAS NOT DISCUSSED" — silence table (F17)

| Item | Monitoring ref | Line of refusal / silence | Consecutive-qtr silence | Read |
|---|---|---|---|---|
| Country-by-country patient/revenue split | 15-17 | declined l.117 | ongoing (structural refusal) | AMBIGUOUS/negative — same-store impossible from disclosure |
| Same-store / same-center growth | 15-17 | deflected l.117/119/120 | ongoing | reframed to "network utilisation 74% + guest count" instead |
| Country-level unit economics per bed | (thesis) | declined l.90 | ongoing | consolidated P&L only |
| Saudi JV loss run-rate / KSA revenue | 7 | declined l.62 | pressed 5x, declined each | CONFIRMATORY-NEGATIVE on visibility |
| Numeric capex guidance | (thesis) | declined l.47 | ongoing | infer from clinic-count only |
| Captive/hospital-partner renewal rate >95% | 10 | never raised, never addressed | silent this qtr | CONFIRMATORY-NEGATIVE — re-ask next call |
| Per-center Philippines acquisition goodwill | (thesis) | declined l.20 ("competitive information") | ongoing | goodwill/permit cost opaque |
| Kamal D Shah (Co-founder) participation | governance | 0 turns (introduced 3x) | — | SILENT_PARTICIPANT, neutral-fact |

---

## NOTE FOR A4 (question generation)
FORWARD-SIGNAL and AMBIGUOUS findings flagged below are the raw material for management
questions. Highest-value: F6.5 (Saudi timeline is quoted three irreconcilable ways), F6.8
(15-20% guidance sits below the 23.7% delivered — clarify sandbag vs decel), F8.1 (ETR
normalisation as Uzbekistan 0% condition erodes), F14.1 (120 vs 125 bps — which is filed),
F16.1 (reported PAT +34.9% vs adjusted +41.7% — why is reported never spoken), and F17.2/F17.3
(captive-renewal silence + Saudi loss non-guidance under 5x questioning).

```yaml
stage: A3-forensics
company: "nephroplus"
quarter: "q1fy27"
doctype: "concall"
model: claude-opus-4-8
status: complete
forensics_path: "/home/user/inflection-pipeline/runs/nephroplus-q1fy27/work/forensics_concall_nephroplus_q1fy27.md"
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
  F10: N.A.
  F11: N.A.
  F12: N.A.
  F13: N.A.
  F14: FINDING
  F15: FINDING
  F16: FINDING
  F17: FINDING
findings:
  - {id: "F1.1", check: "F1", line: "l.58/turn44", classification: "FORWARD-SIGNAL", implication: "Near-zero machine deployment is an explicit one-time depreciation benefit; dep steps up next quarters."}
  - {id: "F1.2", check: "F1", line: "l.45/turn32", classification: "NEUTRAL-FACT", implication: "Rs 20 lakh forex only; +23.7% growth is operational, no FX cushion."}
  - {id: "F6.1", check: "F6", line: "l.12/turn5", classification: "FORWARD-SIGNAL", implication: "NEW 15-20% medium-term guidance; promise-vs-delivery anchor."}
  - {id: "F6.2", check: "F6", line: "l.40/47", classification: "FORWARD-SIGNAL", implication: "New international market every 12-18 months; slippage = tripwire."}
  - {id: "F6.3", check: "F6", line: "l.47/turn32", classification: "FORWARD-SIGNAL", implication: "40-50 India + 10-15 Philippines clinics/yr; capex proxy."}
  - {id: "F6.4", check: "F6", line: "l.10/turn4", classification: "FORWARD-SIGNAL", implication: "NIDA first training batch Q3 FY27; dated milestone."}
  - {id: "F6.5", check: "F6", line: "l.10/60/62", classification: "AMBIGUOUS", implication: "Three irreconcilable Saudi tender timelines; clarify base case."}
  - {id: "F6.6", check: "F6", line: "l.110/117", classification: "FORWARD-SIGNAL", implication: "10-15 countries and standalone-model shift over 5-10 yrs."}
  - {id: "F6.7", check: "F6", line: "l.35/turn23", classification: "FORWARD-SIGNAL", implication: "Contract manufacturing of low-complexity consumables = vertical-integration/COGS lever."}
  - {id: "F6.8", check: "F6", line: "l.10-vs-12", classification: "AMBIGUOUS", implication: "Guidance 15-20% set below delivered 23.7%; sandbag vs deceleration."}
  - {id: "F7.1", check: "F7", line: "l.62/turn48", classification: "AMBIGUOUS", implication: "Saudi loss run-rate undisclosed; monitoring 7."}
  - {id: "F7.2", check: "F7", line: "l.47/turn32", classification: "AMBIGUOUS", implication: "Capex guidance declined; capex only inferable from clinic count."}
  - {id: "F7.3", check: "F7", line: "l.40/turn28", classification: "FORWARD-SIGNAL", implication: "RPT ~11% CAGR not repeatable; realization tailwind fades."}
  - {id: "F7.4", check: "F7", line: "l.90/117", classification: "AMBIGUOUS", implication: "Country-level unit economics declined; feeds silence audit."}
  - {id: "F7.5", check: "F7", line: "l.10/turn4", classification: "AMBIGUOUS", implication: "'timelines not fully within our control' = pre-emptive Saudi-delay cover."}
  - {id: "F8.1", check: "F8", line: "l.49/turn36", classification: "FORWARD-SIGNAL", implication: "ETR 20% below 25.17% statutory only via Uzbekistan 0% (conditional); normalisation-up risk."}
  - {id: "F14.1", check: "F14", line: "l.10-vs-27", classification: "AMBIGUOUS", implication: "120bps (Rohit) vs 125bps (Prashant) same-call margin inconsistency; reconcile to filing."}
  - {id: "F14.2", check: "F14", line: "l.12/turn5", classification: "NEUTRAL-FACT", implication: "RPT prior 'Rs 253' adjudicated as dropped-digit for ~Rs 2,503; 9.2% growth internally consistent."}
  - {id: "F14.3", check: "F14", line: "l.38-vs-110", classification: "NEUTRAL-FACT", implication: "Organized-share 21-22% vs 20% rounding; immaterial."}
  - {id: "F14.4", check: "F14", line: "l.8-vs-10", classification: "NEUTRAL-FACT", implication: "City count 370 vs 357 transcription noise; immaterial."}
  - {id: "F15.1", check: "F15", line: "l.10/64", classification: "FORWARD-SIGNAL", implication: "Kazakhstan subsidiary newly incorporated; next-market vehicle, consolidation-scope change."}
  - {id: "F15.2", check: "F15", line: "l.10/turn4", classification: "NEUTRAL-FACT", implication: "Two Uttarakhand PPP clinics let go (value-dilutive); return discipline, small clinic-count negative."}
  - {id: "F16.1", check: "F16", line: "l.12/turn5", classification: "AMBIGUOUS", implication: "Adjusted PAT +41.7% headlined; reported GAAP PAT Rs 31.97Cr/+34.9% never spoken — favourable reframing."}
  - {id: "F17.1", check: "F17", line: "l.117/turn97", classification: "CONFIRMATORY-NEGATIVE", implication: "Country splits and same-store growth declined; monitoring 15-17 unanswerable by design."}
  - {id: "F17.2", check: "F17", line: "whole-call", classification: "CONFIRMATORY-NEGATIVE", implication: "Captive-hospital renewal rate (>95% monitor 10) never discussed; sustained silence."}
  - {id: "F17.3", check: "F17", line: "l.62/turn48", classification: "AMBIGUOUS", implication: "Saudi loss/revenue declined despite 5x questioning; most-pressed least-answered topic."}
forward_signals: ["F1.1", "F6.1", "F6.2", "F6.3", "F6.4", "F6.6", "F6.7", "F7.3", "F8.1", "F15.1"]
ambiguous: ["F6.5", "F6.8", "F7.1", "F7.2", "F7.4", "F7.5", "F14.1", "F16.1", "F17.3"]
commitments:
  - {commitment: "Revenue growth 15-20% p.a.", implied_date: "next 3-5 yrs", ref: "l.12/turn5", status_word: "reiterated"}
  - {commitment: "New international market every 12-18 months", implied_date: "rolling", ref: "l.40/47", status_word: "ongoing"}
  - {commitment: "40-50 India clinics/yr", implied_date: "annual", ref: "l.47/turn32", status_word: "ongoing"}
  - {commitment: "10-15 Philippines clinics/yr", implied_date: "annual", ref: "l.47/turn32", status_word: "ongoing"}
  - {commitment: "NIDA first nurse-training batch", implied_date: "Q3 FY27", ref: "l.10/turn4", status_word: "scheduled"}
  - {commitment: "Saudi MoH formal tender process begins", implied_date: "~Q3 FY27 (couple of months)", ref: "l.10/turn4", status_word: "underway"}
  - {commitment: "Saudi clear visibility/first benefits", implied_date: "3-4 quarters (~Q1 FY28)", ref: "l.60/turn46", status_word: "underway"}
  - {commitment: "Saudi first Riyadh clinic operational", implied_date: "July 2026", ref: "l.10/turn4", status_word: "completed"}
  - {commitment: "Saudi home-dialysis operations", implied_date: "this quarter", ref: "l.10/turn4", status_word: "completed"}
  - {commitment: "Tamil Nadu PPP contract signed", implied_date: "this quarter", ref: "l.10/turn4", status_word: "completed"}
  - {commitment: "Kazakhstan subsidiary incorporated", implied_date: "this quarter (ops TBD)", ref: "l.10/64", status_word: "completed"}
  - {commitment: "Operate in 10-15 countries", implied_date: "next 5-10 yrs", ref: "l.117/turn97", status_word: "intends"}
  - {commitment: "Standalone clinics overtake in-hospital (India)", implied_date: "next 5-10 yrs", ref: "l.110/turn91", status_word: "intends"}
gate_a3: pass
blank_checks: []
```
