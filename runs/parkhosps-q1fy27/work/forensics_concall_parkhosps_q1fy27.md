# FORENSIC NOTES — Park Medi World Limited (PARKHOSPS) — Q1 FY27 — CONCALL

Agent: A3 FORENSIC NOTES | Model: claude-opus-4-8
Inputs reconciled: A1 extract (87 lines, GATE A1 pass) + A2 ledger (GATE A2 pass).
Ledger reconciliation: 100% — every ledger row (16 participants, 87 turns, 29
questions, 199 mgmt numbers, 34 forward phrases, 6 hedges) read at its cited
extract line before judging.
Citation convention: "turn N" = extract line N (A1/A2 verified 1:1). Quotes are
verbatim from the extract, garbles preserved.
Doctype note: concall. F6/F7/F17 apply in full. Balance-sheet/auditor checks
are N.A. EXCEPT where management spoke a number a check bites on (F8 tax
attribution; F10 promoter dilution). Conservative bias: uncertain direction ->
lean bear, raise an A4 question.

---

## 1. FINDINGS TABLE

| id | check | ledger ref | line/turn | verbatim quote (trimmed) | classification | forward implication |
|----|-------|-----------|-----------|--------------------------|----------------|---------------------|
| FN-01 | F6 | §4 #76-82 | turn 7 (L24) | "we are expecting a top line of 2080 crores... VA of 530 crores and a P of 360 crores... revenue growth is 24%... AITA growth 25%... fat growth staggering at 32%" | FORWARD-SIGNAL | First hard FY27 P&L guidance; the sole anchor for the 25% CAGR thesis. Feeds Role 5 promise-vs-delivery. |
| FN-02 | F6 | §4 #79; F8 context | turn 7 (L24) vs turn 4 (L21) | PAT guidance "P of 360 crores" (+32%) vs Q1 PAT "89 crores" | AMBIGUOUS | ARITHMETIC-CONSISTENCY: Q1 PAT Rs 89cr x4 = Rs 356cr ~ Rs 360cr guidance, but Q1 PAT is ETR-flattered (15.7%). Normalising ETR to 25.17% cuts Q1 PAT to ~Rs 79cr -> ~Rs 316cr annualised. The +32% PAT guidance leans on the tax benefit persisting OR strong H2 acceleration. A4 question. |
| FN-03 | F6 | §4 #20-22,142-144; §5 #2,4,26,27 | turns 2,42 | "end financial year 27 with 4740 beds... 5740 bed capacity by financial year 28" (turn 2) / "6740 by end of FI28" (turn 42) | FORWARD-SIGNAL | Bed roadmap is the capex/growth engine; FY28 endpoint self-contradicts (5,740 vs 6,740) — see FN-18. |
| FN-04 | F6 | §4 #103-108; §5 #16 | turn 10 (L27) | "first year we... generate 100 K of revenue... about 20 22 KES and a pack of about 12 13 K... next year... 140 K... beta around 35 36 crores" | FORWARD-SIGNAL | Rudrapur standalone ramp (a Notion monitorable). Units garbled ("K"/"KES") — Role 5 must resolve against deck. |
| FN-05 | F6 | §4 #116-117; §5 #19 | turn 10 (L27) | "first year of operations... revenue of about roughly FI28 705 crores with an AIA of about 2526 person" | AMBIGUOUS | Zirakpur FY28 revenue: spoken "705 crores" is a NUMBER_GARBLE vs the ~Rs 70-75cr scale of a 150-bed first-year asset. A4/Role 5 must resolve; do not carry 705 forward. |
| FN-06 | F6 | §4 #93,184,185; §5 #31 | turns 9,62,63 | "ARPO... 10 to 12%... this trend we believe will continue" / "10 to 12% for upcoming 2 years... correct? Yes" | FORWARD-SIGNAL | Dated 2-year ARPOB growth commitment; the volume/price bridge under the 24% revenue guide. |
| FN-07 | F6 | §4 #72,73,182,183; §5 #31 | turns 4,61 | "guided towards 7030 split over the next 12 to 18 months" (turn 4) / "next 12 to 15 months it will be 7030" (turn 61) | FORWARD-SIGNAL | Payer-mix graduation dated commitment; window self-varies 12-18 vs 12-15 months. |
| FN-08 | F6 | §4 #91,99,129; §5 #15 | turns 8,9,30 | "we remain study on the beta margin of 26 to 27% the current year" / "AITA of 26.5 to 27% will hold for complete financial year" | FORWARD-SIGNAL | Full-year EBITDA-margin floor commitment; tripwire is <22% for 2 quarters. |
| FN-09 | F6 | §4 #131-133; §5 #23,24 | turn 35 | "right now also we are at around 18%... increase of 150 200 basis coming... in the next 12 to 18 months" | FORWARD-SIGNAL | Dated ROCE improvement claim; the only ROCE anchor given. |
| FN-10 | F6 | §4 #53,124-128; §5 #5 | turns 3,21,26,28 | "we continue to expect the fuller impact to be visible from Q2" / "7 to 7.5% benefit flowing into FI27" | FORWARD-SIGNAL | CGHS uplift dated to Q2 full-impact; but see FN-13 (routed to capex, not margin). |
| FN-11 | F6 | §4 #43,44,49 | turn 3 (L20) | "full year FI27 occupancy to moderate from the FI26 figures of 64%" | FORWARD-SIGNAL | Management pre-warns FY27 occupancy below 64%; occupancy is a live monitorable (Q1 already 56% network). |
| FN-12 | F7 | §6 #2,3,4 | turn 51 (L68) | "too early to comment on that... we are evaluating now opportunities... I cannot specify exact timeline right now" | AMBIGUOUS | Triple hedge on promoter-dilution timing; equity raise explicitly tied to an unspecified acquisition. A4 question on dilution mechanism/timing. |
| FN-13 | F7 | §4 #124-130; §6 (context) | turns 26,28,30 | "it will not directly translate into I beta because... this opportunity of rate revision we'll also be utilizing in upgrading our equipment and capex" | FORWARD-SIGNAL | CONFIRMATORY that the CGHS uplift is NOT a margin tailwind — diverted to capex/equipment. Softens the EBITDA-margin bull case despite the 7-7.5% headline. |
| FN-14 | F7 | §6 #1 | turn 9 (L26) | "we can't see any challenge in terms of achieving the numbers... we are expecting that we will overachieve" | AMBIGUOUS | Overconfidence hedge against an occupancy-drag question; conservative read = downside not stress-tested. A4 question. |
| FN-15 | F7 | §6 #5,6 | turn 55 (L72) | "very difficult to actually project or predict any percentage... it's very difficult to say" | AMBIGUOUS | Refusal to commit a long-term case-mix target; contrast with the specific 2-year ARPOB commit (FN-06). |
| FN-16 | F8 | §4 #62-64 | turn 4 (L21) | "pat margin expansion was largely on account of reduction in interest outgo following the substantial repayment of term debt" | CONFIRMATORY-NEGATIVE | The +220bps PAT-margin bridge credits ONLY interest reduction and is silent on the Rs 93.40mn consolidated deferred-tax benefit / ETR fall to 15.7% from 20.0% that actually flattered the +35% PAT. Single most material silence (see F17 #1). |
| FN-17 | F10 | §4 #156-161; §6 #2-4 | turn 51 (L68) | "3-year regulatory timeline which lapse phase in December 2028... approximately 8% equity that we have to divest... would be the right time for us to raise this equity capital" | FORWARD-SIGNAL | Forward dilution: ~8% promoter divestment by Dec-2028, delivered via an acquisition-linked equity raise. Future share-count expansion; A4 to size dilution vs entry zone. |
| FN-18 | F14 | §4 #22/#144, #74/#145/#152, #5/#137, #4/#102 | turns 2/42, 4/43/46, 2/42, 2/10 | "5740 bed capacity by financial year 28" vs "6740 by end of FI28"; "37 lakhs per bed" vs "around 34 lakh" vs "36 lakhs"; "22nd August 2026" vs "2nd of August"; "331 NH accredited" vs "all 330 beds" | NEUTRAL-FACT (governance data-quality) | Four unreconciled internal inconsistencies in one call (FY28 bed endpoint off by 1,000; capex/bed spread 34-37 lakh; Rudrapur commissioning date off by 20 days; Rudrapur bed count 330/331). Cumulatively a disclosure-precision flag; Role 5 must not carry any single value forward unverified. |
| FN-19 | F14 | §1 row 5 (MGMT_ABSENCE) | participants §1 | "grep for 'Ajit Gupta'/'Chairman' = 0 hits" | AMBIGUOUS | Chairman Dr. Ajit Gupta absent across all 87 turns on a quarter with two acquisitions (Rudrapur ~Rs 177cr, Zirakpur) and a bed-guidance change (5,040->4,740). Governance signal; A4 question. |
| FN-20 | F17 | silence #1 | turn 4 (L21) | (deferred-tax benefit NOT DISCUSSED) — cf. "reduction in interest outgo" | CONFIRMATORY-NEGATIVE | Deferred-tax benefit / low ETR omitted entirely; management gave an alternative causal story. Adjudicated as sustained silence on a material, earnings-flattering item. |
| FN-21 | F17 | silence #2 | (whole call) | (subsidiary-audit / assurance scope NOT DISCUSSED) | AMBIGUOUS | 83.9% of consolidated PAT sits outside the principal auditor's limited review (Rs 26mn reviewed); scope never raised. A4 question. |
| FN-22 | F17 | silence #3 | turn 2 (L19), turn 4 (L21) | "funded largely through internal acrals and IP proceeds without recourse to our fresh debs" / "fully funded... without recourse to any material such debt" | CONFIRMATORY-NEGATIVE | "Fully funded" asserted while the Rs 648mn IPO proceeds sitting idle at zero yield, the medical-equipment object 84% behind FY26 schedule, and the Board object-variation postal ballot are all left undisclosed. The framing masks a deployment problem. |
| FN-23 | F17 | silence #4 | turn 3 (L20), turns 9/62 | "Network occupancy for the quarter stood at 56% compared to 68%" | FORWARD-SIGNAL | Network occupancy decline WAS disclosed (56% vs 68%, ~-1,200bps) and ARPOB GROWTH given (10-12%), but ABSOLUTE ARPOB and the same-store vs new-bed occupancy split were NOT quantified. Partial disclosure; A4 to demand the mature-asset occupancy and ARPOB level. |
| FN-24 | F17 | silence #5 | (whole call) | (standalone parent economics NOT DISCUSSED) | AMBIGUOUS | Standalone parent core is loss-making (standalone = 1.22% of consol PAT); no standalone figure spoken. Expected silence, logged for consecutive-quarter tracking. |

---

## 2. CHECKLIST SCORECARD (all 17 — exactly one status each)

| # | Status | One-line basis |
|---|--------|----------------|
| F1 | N.A. | No balance-sheet template line items in a transcript. Rhetorical ZERO_STANDING claims ("no EBITDA loss" turn 8, "no concern" turn 45, "zero patient grievances" turn 83) are assurance-hedges, adjudicated under F7/F17, not template zero-lines. |
| F2 | N.A. | No standalone-vs-consolidated split spoken; only consolidated figures given. Standalone core (F17 #5) is a silence item, logged under FN-24. |
| F3 | N.A. | No entity-level cost lines (materials/employee/depreciation) in a transcript; shell detection needs the filing. |
| F4 | N.A. | No auditor "Other Matters" in a transcript. The 83.9% unaudited-PAT ratio is a silence item, logged under FN-21 (F17). |
| F5 | N.A. | No auditor EoM/Going-Concern paragraph in a transcript; first concall for the ticker, so no prior-quarter verbatim diff possible. |
| F6 | FINDING | 34 forward phrases + full new FY27 P&L and asset-level guidance registered (FN-01 to FN-11); see Commitment Register. |
| F7 | FINDING | 6 lexicon hedges + the CGHS-not-into-EBITDA diversion mined (FN-12 to FN-15); promoter-dilution triple hedge and overconfidence hedge flagged for A4. |
| F8 | FINDING | Management spoke PAT (+35%) and PAT-margin (+220bps) and attributed the bridge solely to interest reduction, omitting the Rs 93.40mn deferred-tax benefit / ETR 15.7% (FN-16). Check bites. |
| F9 | N.A. | No OCI / actuarial gain-loss discussion on the call. |
| F10 | FINDING | Management discussed the promoter-holding reduction to 75% (~8% divest by Dec-2028) via an acquisition-linked equity raise (FN-17). Check bites. |
| F11 | N.A. | Only a single aggregate net-worth figure spoken (Rs 2,100cr, turn 4 #68); no paid-up/other-equity components and no third-party number in the transcript to tie out against. |
| F12 | N.A. | No segment asset/liability tables in a transcript. |
| F13 | N.A. | Board "approved the result... yesterday" (turn 2) is the only board outcome spoken; no AR/AGM/record-date/director-term or enabling-resolution disclosure on the call. The Board object-variation postal ballot was NOT mentioned -> logged under FN-22 (F17). |
| F14 | FINDING | Four unreconciled internal inconsistencies (FN-18) plus the Chairman's full-call absence (FN-19). |
| F15 | N.A. | No consolidation entity list in a transcript; first concall, no prior list to diff. |
| F16 | N.A. | Doctype is concall, not a presentation; dropped/reframed-disclosure check applies to the deck (ARPOB-absent-from-deck cross-referenced under FN-23). |
| F17 | FINDING | Silence audit run against 5 same-quarter findings + Notion monitorables; deferred-tax silence (FN-20) and "fully funded" framing (FN-22) adjudicated CONFIRMATORY-NEGATIVE. |

Blank checks: none. GATE A3: PASS.

---

## 3. COMMITMENT REGISTER (from F6)

| commitment | implied date | ref (turn) | status word |
|------------|--------------|------------|-------------|
| FY27 revenue ~Rs 2,080cr / EBITDA ~Rs 530cr / PAT ~Rs 360cr (growth 24/25/32%) | FY27 (by Mar-2027) | turn 7 | expecting |
| Bed capacity 4,740 by end FY27 | Mar-2027 | turns 2, 42 | expect / laid out |
| Bed capacity 5,740 [stated] / 6,740 [restated] by end FY28 | Mar-2028 | turns 2, 4, 42 | will add (INCONSISTENT endpoint) |
| 450 beds (Narela/Palam-Platinum/Zirakpur) commissioning | Nov-Dec 2026 (Q3 FY27) | turns 2, 42 | scheduled / on track |
| Rudrapur commissioned | 22-Aug-2026 [op] / 2-Aug-2026 [Q&A] | turns 2, 42 | commissioned (DATE INCONSISTENT) |
| Rudrapur FY27 revenue ~Rs 100cr / EBITDA ~Rs 20-22cr / PAT ~Rs 12-13cr; FY28 rev ~Rs 140cr | FY27 / FY28 | turn 10 | feel / will ramp |
| Zirakpur (Mahair) FY28 first-year revenue [spoken "705cr" garble; ~Rs 70-75cr scale] | FY28 | turn 10 | intend commencing Nov-2026 |
| Rudrapur incremental capex not more than Rs 10-12cr | FY27 | turn 18 | expecting |
| ARPOB growth 10-12% p.a. | next 2 years (thru FY28) | turns 9, 62, 63 | believe will continue |
| Payer mix to 70:30 | next 12-18 months [also stated 12-15] | turns 4, 61 | guided towards |
| EBITDA margin held 26-27% | full FY27 | turns 8, 9, 30 | remain steady / will hold |
| Full-year FY27 occupancy to moderate below FY26 64% | FY27 | turn 3 | expect |
| CGHS 7-7.5% benefit, full impact | from Q2 FY27 | turns 3, 21, 26 | continue to expect |
| CGHS benefit routed to equipment/capex, NOT directly to EBITDA | ongoing | turns 26, 28 | will be utilizing |
| ROCE ~18% today, +150-200bps improvement | next 12-18 months | turn 35 | believe |
| Four additional hospitals to obtain NABH accreditation | current FY27 | turn 3 | planning to |
| Receivable days to trend to 125-130 (medium-term) | medium-term | turn 4 | continue to expect |
| Total planned capex Rs 767cr -> 2,130 beds at ~Rs 36 lakh/bed | FY27+FY28 | turns 46, 48 | plan to do |
| Promoter stake to 75% (~8% divest) via acquisition-linked equity raise | by Dec-2028 | turn 51 | evaluating / too early |

---

## 4. WHAT WAS NOT DISCUSSED (F17 SILENCE AUDIT)

Consecutive-quarter silence count: this is the FIRST concall for PARKHOSPS, so every silence below is quarter 1 of 1 (baseline). Sustained-silence escalation applies from Q2 FY27 onward.

| # | Item (same-quarter finding / monitorable) | Addressed? | Evidence / cite | Classification | Q-silence count |
|---|-------------------------------------------|-----------|-----------------|----------------|-----------------|
| 1 | DEFERRED-TAX BENEFIT (Rs 93.40mn; ETR 15.7% vs 20.0%) that flattered +35% PAT | NOT DISCUSSED (actively re-attributed) | turn 4 L21: "pat margin expansion was largely on account of reduction in interest outgo" — no tax/ETR mention anywhere | CONFIRMATORY-NEGATIVE | 1 |
| 2 | UNAUDITED CONTRIBUTION — 83.9% of consol PAT outside principal auditor's limited review | NOT DISCUSSED | no assurance/subsidiary-audit-scope reference in any of 87 turns | AMBIGUOUS -> A4 | 1 |
| 3 | IPO PROCEEDS — Rs 648mn idle at zero yield; equipment object 84% behind; object-variation postal ballot | NOT DISCUSSED (contradicted by "fully funded" framing) | turn 2 L19 / turn 4 L21: "fully funded... without recourse to any material such debt" | CONFIRMATORY-NEGATIVE | 1 |
| 4 | ABSOLUTE ARPOB level + same-store vs new-bed occupancy split | PARTIAL — network occupancy 56% vs 68% given (turn 3) and ARPOB GROWTH 10-12% given (turn 62); ABSOLUTE ARPOB and same-store split NOT given | turn 3 L20; turn 62 L79 | FORWARD-SIGNAL -> A4 | 1 |
| 5 | STANDALONE parent core loss-making (standalone = 1.22% of consol PAT) | NOT DISCUSSED (expected) | no standalone figure spoken | AMBIGUOUS -> A4 | 1 |
| M1 | FY27 FCF inflection (Notion monitorable) | NOT DISCUSSED | debt/FD spoken (turns 4) but no FCF statement | AMBIGUOUS -> A4 | 1 |
| M2 | Rudrapur standalone economics (monitorable) | ADDRESSED | turn 10 L27: "100 K of revenue... 20 22 KES... 12 13 K" (units garbled) | NEUTRAL-FACT | 0 |
| M3 | Platinum / Park Platinum ARPOB (monitorable) | NOT DISCUSSED (extension size given, no ARPOB) | turn 2 L19: "100 bed extension... park platinum" | AMBIGUOUS -> A4 | 1 |
| M4 | Debtor days (tripwire >175 for 2Q; guided 125-130) | ADDRESSED | turn 4 L21: "trend towards our medium-term target of 125 to 130 days" | NEUTRAL-FACT | 0 |
| M5 | EBITDA margin (tripwire <22% for 2Q; guided 26-27) | ADDRESSED | turns 8/9/30: "26 to 27%" held | NEUTRAL-FACT | 0 |
| M6 | Promoter remuneration >30% PAT (tripwire) | NOT DISCUSSED | no promoter-remuneration figure spoken | AMBIGUOUS -> A4 | 1 |
| M7 | Acquisition cost/bed >Rs 1.0cr (tripwire; Rudrapur 0.54, Mehar 0.71) | ADDRESSED (indirectly) | turn 42 L59: "54 lakh per capex... around 70 lakh"; turn 46: blended "36 lakhs" | NEUTRAL-FACT (within tripwire) | 0 |

---

## 5. ANALYST NOTES FOR A4 (routing)

- FORWARD-SIGNAL findings (feed the promise-vs-delivery tracker and catalyst
  timeline): FN-01, FN-03, FN-04, FN-06, FN-07, FN-08, FN-09, FN-10, FN-11,
  FN-13, FN-17, FN-23.
- AMBIGUOUS findings (convert to management questions): FN-02 (PAT guidance vs
  tax-flattered run-rate), FN-05 (Zirakpur 705 garble), FN-12 (dilution timing),
  FN-14 (overconfidence vs occupancy drag), FN-15 (case-mix refusal), FN-19
  (Chairman absence), FN-21 (audit scope), FN-24 (standalone core).
- CONFIRMATORY-NEGATIVE (Role 5 escalation): FN-16 / FN-20 (deferred-tax
  silence + re-attribution), FN-22 ("fully funded" masking idle IPO proceeds).
- Single most important adjudication: the deferred-tax benefit is not merely
  unmentioned; management supplied a competing causal explanation (interest
  outgo) for the same margin movement. Treat as the priority A4 question.

---

```yaml
stage: A3-forensics
company: "PARKHOSPS"
quarter: "Q1 FY27"
doctype: "concall"
model: claude-opus-4-8
status: complete
forensics_path: "/home/user/inflection-pipeline/runs/parkhosps-q1fy27/work/forensics_concall_parkhosps_q1fy27.md"
ledger_reconciled_pct: 100
checklist:
  F1: N.A.
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
  F16: N.A.
  F17: FINDING
findings:
  - {id: "FN-01", check: "F6", line: "turn 7 (L24)", classification: "FORWARD-SIGNAL", implication: "FY27 guidance rev 2080/EBITDA 530/PAT 360cr, growth 24/25/32%"}
  - {id: "FN-02", check: "F6", line: "turn 7 (L24) vs turn 4 (L21)", classification: "AMBIGUOUS", implication: "PAT 360 guide leans on tax-flattered Q1 (ETR 15.7%); ETR-normalised annualised ~316cr"}
  - {id: "FN-03", check: "F6", line: "turns 2,42", classification: "FORWARD-SIGNAL", implication: "Bed roadmap 4740 FY27, 5740/6740 FY28 (endpoint self-contradicts)"}
  - {id: "FN-04", check: "F6", line: "turn 10 (L27)", classification: "FORWARD-SIGNAL", implication: "Rudrapur FY27 rev ~100/EBITDA 20-22/PAT 12-13; FY28 ~140 (units garbled)"}
  - {id: "FN-05", check: "F6", line: "turn 10 (L27)", classification: "AMBIGUOUS", implication: "Zirakpur FY28 rev spoken '705cr' garble vs ~70-75cr scale"}
  - {id: "FN-06", check: "F6", line: "turns 9,62,63", classification: "FORWARD-SIGNAL", implication: "ARPOB growth 10-12% for 2 years"}
  - {id: "FN-07", check: "F6", line: "turns 4,61", classification: "FORWARD-SIGNAL", implication: "Payer mix to 70:30 in 12-18 (also 12-15) months"}
  - {id: "FN-08", check: "F6", line: "turns 8,9,30", classification: "FORWARD-SIGNAL", implication: "EBITDA margin held 26-27% full FY27"}
  - {id: "FN-09", check: "F6", line: "turn 35", classification: "FORWARD-SIGNAL", implication: "ROCE ~18% +150-200bps in 12-18 months"}
  - {id: "FN-10", check: "F6", line: "turns 3,21,26", classification: "FORWARD-SIGNAL", implication: "CGHS 7-7.5% full impact from Q2 FY27"}
  - {id: "FN-11", check: "F6", line: "turn 3 (L20)", classification: "FORWARD-SIGNAL", implication: "FY27 occupancy pre-warned below FY26 64%"}
  - {id: "FN-12", check: "F7", line: "turn 51 (L68)", classification: "AMBIGUOUS", implication: "Triple hedge on promoter-dilution timing; raise tied to unspecified acquisition"}
  - {id: "FN-13", check: "F7", line: "turns 26,28,30", classification: "FORWARD-SIGNAL", implication: "CGHS uplift diverted to capex/equipment, NOT EBITDA margin"}
  - {id: "FN-14", check: "F7", line: "turn 9 (L26)", classification: "AMBIGUOUS", implication: "Overconfidence hedge vs occupancy-drag question, downside untested"}
  - {id: "FN-15", check: "F7", line: "turn 55 (L72)", classification: "AMBIGUOUS", implication: "Refuses long-term case-mix target vs specific ARPOB commit"}
  - {id: "FN-16", check: "F8", line: "turn 4 (L21)", classification: "CONFIRMATORY-NEGATIVE", implication: "+220bps PAT-margin credited to interest only; silent on Rs 93.4mn deferred-tax / ETR 15.7%"}
  - {id: "FN-17", check: "F10", line: "turn 51 (L68)", classification: "FORWARD-SIGNAL", implication: "~8% promoter divestment by Dec-2028 via acquisition-linked equity raise = future dilution"}
  - {id: "FN-18", check: "F14", line: "turns 2/42, 4/43/46, 2/10", classification: "NEUTRAL-FACT", implication: "Four internal inconsistencies: 5740 vs 6740 beds; 34/36/37 lakh capex/bed; 2 vs 22 Aug; 330 vs 331 beds"}
  - {id: "FN-19", check: "F14", line: "participants row 5", classification: "AMBIGUOUS", implication: "Chairman Dr. Ajit Gupta absent across all 87 turns on a 2-acquisition quarter"}
  - {id: "FN-20", check: "F17", line: "turn 4 (L21)", classification: "CONFIRMATORY-NEGATIVE", implication: "Deferred-tax benefit not disclosed; competing causal story supplied"}
  - {id: "FN-21", check: "F17", line: "whole call", classification: "AMBIGUOUS", implication: "83.9% unaudited PAT scope never raised"}
  - {id: "FN-22", check: "F17", line: "turns 2,4 (L19,L21)", classification: "CONFIRMATORY-NEGATIVE", implication: "'Fully funded' framing masks Rs 648mn idle IPO proceeds, equipment delay, object-variation ballot"}
  - {id: "FN-23", check: "F17", line: "turns 3,62", classification: "FORWARD-SIGNAL", implication: "Absolute ARPOB + same-store vs new-bed occupancy split not quantified"}
  - {id: "FN-24", check: "F17", line: "whole call", classification: "AMBIGUOUS", implication: "Standalone parent core loss-making not discussed"}
forward_signals: ["FN-01","FN-03","FN-04","FN-06","FN-07","FN-08","FN-09","FN-10","FN-11","FN-13","FN-17","FN-23"]
ambiguous: ["FN-02","FN-05","FN-12","FN-14","FN-15","FN-19","FN-21","FN-24"]
commitments:
  - {commitment: "FY27 rev ~2080 / EBITDA ~530 / PAT ~360 cr (24/25/32%)", implied_date: "FY27", ref: "turn 7", status_word: "expecting"}
  - {commitment: "Bed capacity 4740 by end FY27", implied_date: "Mar-2027", ref: "turns 2,42", status_word: "expect"}
  - {commitment: "Bed capacity 5740[/6740] by end FY28", implied_date: "Mar-2028", ref: "turns 2,42", status_word: "will-add-inconsistent"}
  - {commitment: "450 beds commissioning (Narela/Platinum/Zirakpur)", implied_date: "Nov-Dec-2026", ref: "turns 2,42", status_word: "scheduled"}
  - {commitment: "Rudrapur commissioned", implied_date: "Aug-2026", ref: "turns 2,42", status_word: "completed-date-inconsistent"}
  - {commitment: "Rudrapur FY27 rev ~100/EBITDA 20-22/PAT 12-13cr; FY28 ~140cr", implied_date: "FY27-FY28", ref: "turn 10", status_word: "expect"}
  - {commitment: "Zirakpur FY28 first-year revenue (~70-75cr; '705' garble)", implied_date: "FY28", ref: "turn 10", status_word: "intend"}
  - {commitment: "ARPOB growth 10-12% p.a.", implied_date: "next 2 years", ref: "turns 9,62,63", status_word: "believe-continue"}
  - {commitment: "Payer mix to 70:30", implied_date: "12-18 months", ref: "turns 4,61", status_word: "guided"}
  - {commitment: "EBITDA margin held 26-27%", implied_date: "full FY27", ref: "turns 8,9,30", status_word: "will-hold"}
  - {commitment: "FY27 occupancy to moderate below FY26 64%", implied_date: "FY27", ref: "turn 3", status_word: "expect"}
  - {commitment: "CGHS 7-7.5% full impact (routed to capex not margin)", implied_date: "from Q2 FY27", ref: "turns 3,26,28", status_word: "continue-to-expect"}
  - {commitment: "ROCE ~18% +150-200bps", implied_date: "12-18 months", ref: "turn 35", status_word: "believe"}
  - {commitment: "Receivable days to 125-130", implied_date: "medium-term", ref: "turn 4", status_word: "expect"}
  - {commitment: "Total capex 767cr -> 2130 beds at ~36 lakh/bed", implied_date: "FY27-FY28", ref: "turns 46,48", status_word: "plan"}
  - {commitment: "Promoter stake to 75% (~8% divest) via acquisition-linked equity raise", implied_date: "by Dec-2028", ref: "turn 51", status_word: "evaluating"}
  - {commitment: "Four hospitals to obtain NABH accreditation", implied_date: "FY27", ref: "turn 3", status_word: "planning"}
gate_a3: pass
blank_checks: []
```
