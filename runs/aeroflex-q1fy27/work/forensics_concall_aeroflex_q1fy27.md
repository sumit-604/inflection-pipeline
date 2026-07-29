# A3 FORENSIC NOTES — Aeroflex Industries Limited (AEROFLEX), Q1 FY27, DOCTYPE: CONCALL

Agent: A3 FORENSIC NOTES | Model: claude-opus-4-8 | Date: 2026-07-29
Source A1 extract: `runs/aeroflex-q1fy27/work/extract_concall_aeroflex_q1fy27.txt` (turns T00-T17)
Source A2 ledger: `runs/aeroflex-q1fy27/work/ledger_concall_aeroflex_q1fy27.md`
Companions read: `review_aeroflex_q1fy27.md`, `_notion_thesis_snapshot.md`, `extract_results_*`, `extract_presentation_*` (P&L baselines cited from the A4 review, which reconciled deck-to-filing to the paise).

**Ledger reconciliation: 100%.** Every A2 ledger section (Participants 1, Speaker-turns 2, Questions 3, mgmt_numbers 4 with all per-turn tables T01-T17, Forward-commitments/Hedges 5, Consolidated flags 6) was read verbatim and cross-read against the transcript turn it cites. A2 gate was PASS (turns 14/14, questions 55/55, mgmt_numbers 120/120, participants 15/15); no re-sweep required. All 15 A2 flags carried into the checks below.

This is a **concall**. Per doctype applicability (prompt lines 128-131), F6/F7/F17 apply; F16 applies to the guidance/disclosure-reframing content the call carries versus the deck/prior call; balance-sheet, auditor, tax, OCI, share-count, segment, board-outcome and entity-list checks (F1-F5, F8-F13, F15) are N.A. on a transcript and are marked so with a one-line basis. F14 (drafting/number inconsistencies) is run against the call-vs-deck number integrity the injected priorities require.

---

## FINDINGS TABLE

| id | check | ledger row ref | line/turn | short verbatim quote | classification | forward implication |
|---|---|---|---|---|---|---|
| CC-F6-01 | F6 | Sec5 fwd-commit #2 | T10 | "it may come anywhere between October to November... it depends on our machine supplier because from where we are facing certain delays from their end" | FORWARD-SIGNAL | The 15,000-skid milestone (Notion: Q3, 60% util on 15k by ~Mar-27) is now supplier-dependent; slip risk to the FY28 optimum-utilisation and ROCE-recovery path. |
| CC-F6-02 | F6 | Sec5 fwd-commit #4 | T08 | "in this financial year we'll definitely have business coming in from an international market" | FORWARD-SIGNAL | New unquantified FY27 commitment; design "slightly different," still "in talks... to develop," customer identity withheld — a promise now trackable but un-evidenced. |
| CC-F6-03 | F6 | Sec5 fwd-commit #3 | T07, T12 | "the product is already almost towards the end of completion. Should be commercialized by... the end of this quarter or... the start of next quarter" | FORWARD-SIGNAL | Fire-hose assembly (international-only, 23-26% margin band [T12]) is a near-dated FY27 revenue catalyst; realisation quantum declined [T07] so size is untestable. |
| CC-F6-04 | F6 | Sec4 T10/T13; Sec5 #5 | T09, T10, T13 | "these are mostly the cost related to... setting up of the plant... the employees cost has increased because of the ramp up in in manpower" | FORWARD-SIGNAL | Rs 48 Cr skid + Rs 54 Cr hose capex confirmed [T09]; QoQ +~300 bps opex de-leverage framed as expansion-related and absorbable "next few quarters" — a management claim, untested until H1 CFO. Advances the Notion capex-absorption / ROCE-denominator concern. |
| CC-F7-01 | F7 | Sec5 hedges #1,3,7,8,9,10; flag GUIDANCE reframing | T07, T08, T11, T13, T14 | "I will not be able to share the exact margin details on public forum"; "I would want everyone to look at our business not from a quarteronquarter basis" | AMBIGUOUS | Systematic deflection on skid margin, customer names, Q2 numbers, international quantum, own-vs-sourced split, all on a "public forum" / "annual not quarterly" basis. Guarded-selective archetype; direction uncertain (competitive sensitivity vs concealment) — lean bear, generate question. |
| CC-F7-02 | F7 | Sec2 T11; Sec4 T11 | T08, T11 | "it is not our customer the end customer who is ultimately setting up the data center. It is the customer of our customer" | FORWARD-SIGNAL | Skid revenue runs through a single intermediary customer; forward visibility only ~2 months tentative dispatch + a Q3 project template; names proprietary [T08]. Thin, concentrated, low-visibility order book into a capacity build. |
| CC-F14-01 | F14 | Sec4 T01 row8; flag DECK_MISMATCH_CANDIDATE | T01 | "Our stood at 33 12 crores which is up by 116%... margins expanding by 468 basis points... to 23.04%" | NEUTRAL-FACT | Spoken EBITDA 33.12 Cr ties to neither deck figure (consol 33.49 / standalone 33.03) and is internally inconsistent with the spoken 23.04% margin, which on consol rev 145.38 implies 33.49. Deck 33.49 governs; treat 33.12 as a spoken/transcription slip, not a restated number. |
| CC-F14-02 | F14 | Sec4 T11 row5, T08 row1, T09 row1; flag TRANSCRIPTION_AMBIGUOUS | T08, T09, T11 | "the number the volume was 140 [1,040]. It is mentioned on the in the presentation also" | NEUTRAL-FACT | Skid volume "140" reconciles to deck 1,040; skid-capacity base "2,000" reconciles to 6,000 (recurs 3x). All reconcilable to the deck/filing; no unreconciled number. |
| CC-F16-01 | F16 | Sec6 flag GUIDANCE_SOFTENED; Sec5 hedge #4 | T07 | "I would... talk about this at the end of the year because... quarter on quarter things change... but we work on a yearly basis" | AMBIGUOUS | Prior guidance (25% SFN-share-of-revenue by year-end) neither reaffirmed nor withdrawn, explicitly deferred — despite the analyst noting Q1 is already ~22% without full capacity. Softening of a stated target = bear-leaning ambiguity. |
| CC-F16-02 | F16 | Sec4 T06 row1; Sec3 T06 | T06, T08 | "technically... the price has not declined because the value per skid assembly... depends on the design... it's not the right way to see as the price per skid assembly" | AMBIGUOUS | Reframes the declining-ASP metric the prior review flagged (A3-F07 open). Plausible (tailor-made Rs 1-5 lakh/skid, costed individually) and margin-neutral by assertion, but unverifiable without volume-by-design mix and the exact skid margin, which was declined [T08]. PARTIALLY resolves A3-F07. |
| CC-F17-01 | F17 | Notion 3 red silences; Sec6 | T00-T17 (absent) | (no turn — zero mentions of ROCE, contingent IT/GST demand, or US M&A/QIP anywhere in T00-T17) | CONFIRMATORY-NEGATIVE | All three Notion "red silences" persist: ROCE trajectory, GST/IT contingent tax, and the US M&A pillar (dropped ~Rs 400 Cr US QIP) were neither asked nor volunteered. Sustained silence on the deteriorating ROCE metric is a confirmatory negative (2nd consecutive call). |
| CC-F17-02 | F17 | review Step 8.5 Q1-Q14 | T11 (declined) | "Q2 delivery schedule we have but I will not be able to share it right now. So probably you can take it on a onetoone basis" | CONFIRMATORY-NEGATIVE | 10 of the 14 prior-review management questions went unanswered on the call; the Q2 skid-unit ask (the single cleanest next-quarter metric, review 8C) was explicitly declined to a one-to-one channel. |
| CC-F17-03 | F17 | Sec1 row2, Sec6 flag MGMT_ABSENCE | T01-T17 | "No CFO / other named executive spoke on the recorded transcript... MD Asad Daud answered ALL 14 analyst turns personally" (ledger Sec1) | AMBIGUOUS | Single-voice call; CFO also absent from Q4 FY26 per Notion = 2nd consecutive quarter with no finance-officer voice. On a capex/cash-conversion-sensitive name with untestable Q1 cash flow, a persistent CFO absence is a governance/credibility signal, not a neutral fact. |

---

## CHECKLIST SCORECARD (all 17; one status each — GATE A3)

| Check | Status | One-line basis |
|---|---|---|
| F1 Zero-value standing line items | N.A. | No balance-sheet template / line items on a concall transcript. |
| F2 Standalone vs consolidated decomposition | N.A. | S-vs-C decomposition needs filed statements; call gives consol headline only (EBITDA integrity handled under F14). |
| F3 Shell-entity detection | N.A. | Requires standalone-vs-consol cost-line comparison from filed statements; not in a transcript. |
| F4 Unaudited contribution ratio | N.A. | Auditor Other-Matters paragraph is a filing artifact; not present on a concall. |
| F5 Going concern / EoM scope | N.A. | No EoM / going-concern language exists in a transcript. |
| F6 Forward-commitment phrase mining | **FINDING** | Dated commitments extracted; 15k timing slipped to supplier-dependent Oct-Nov and new intl/fire-hose/capex-absorption commitments (CC-F6-01..04). Register below. |
| F7 Hedge phrase mining | **FINDING** | Pervasive "public forum"/"proprietary"/"difficult to give a number"/"annual not quarterly" deflection; single-customer concentration disclosure (CC-F7-01, CC-F7-02). |
| F8 Tax forensics | N.A. | No tax lines / ETR / deferred-tax detail on the call (ETR step-up handled in results forensics A3-F8). |
| F9 OCI forensics | N.A. | No OCI / actuarial content on a concall. |
| F10 Share count and dilution | N.A. | No paid-up capital / EPS-spread content on the call. |
| F11 Reserves and net worth tie-out | N.A. | No equity / reserves figures on the call. |
| F12 Segment forensics | N.A. | Single-segment company; no segment asset/liability tables on a transcript. |
| F13 Board outcome beyond results | N.A. | No board agenda / AGM / director-term content on the call. |
| F14 Note drafting / number inconsistencies | **FINDING** | Spoken EBITDA 33.12 Cr ties to neither deck figure and contradicts own 23.04% margin; volume "140"/base "2,000" slips reconciled (CC-F14-01, CC-F14-02). |
| F15 Entity list diffs | N.A. | Consolidation-list diff needs filed entity lists; not on a transcript. |
| F16 Dropped / reframed / softened disclosures | **FINDING** | 25% SFN-share target softened/deferred vs prior call; skid-ASP metric reframed as non-meaningful (CC-F16-01, CC-F16-02). |
| F17 Silence audit | **FINDING** | Three red silences persist; 10/14 prior questions unanswered; Q2 units declined; CFO absent 2nd straight call (CC-F17-01..03). |

Applicable checks run: F6, F7, F14, F16, F17. No blank checks. **GATE A3: PASS.**

---

## COMMITMENT REGISTER (from F6)

| # | Commitment | Implied date | Turn ref | Status word |
|---|---|---|---|---|
| 1 | Flexible-hose capacity 16.5/17.5 → 20 Mn m | Q3 FY27 | T01, T09 | underway (reaffirmed twice) |
| 2 | Skid capacity 9,000 → 15,000 units p.a. | "October to November" (Q3 FY27) | T01, T08, T09, T10 | underway — **slipped/hedged** (machine-supplier delays) |
| 3 | Fire-hose assembly commercialisation, international-only | end-Q2 / start-Q3 FY27 | T07, T12 | underway (near completion; 23-26% margin) |
| 4 | International skid revenue booked | within FY27 | T08 | initiated / in development (design differs, customer withheld) |
| 5 | Skid capex Rs 48 Cr + hose capex Rs 54 Cr, remaining spend | completes FY27 | T09 | underway |
| 6 | Skid optimal utilisation ~80% | full-year FY28 | T09 | guided (future) |
| 7 | Q4 exit run-rate ~750 skids/month at 60-65% util on 15,000 base | Q4 FY27 | T10, T11 | reaffirmed intact (analyst-sourced number, MD-confirmed) |
| 8 | Company blended EBITDA margin 25% | "next few years" | T05, T09 | aspirational / reaffirmed (unquantified) |
| 9 | Metal / miniature bellows sales uptake | "next two quarters" | T05 | initiated |
| 10 | Hyd-Air capex plan | "announce as soon as it is finalized" | T05 | not initiated (under discussion) |
| 11 | 25% SFN-share-of-revenue | year-end FY27 | T07 | **softened / deferred** (see CC-F16-01) |
| 12 | Capacity expansion beyond 15,000 skids | undated | T08 | under discussion — "too early to comment" |

---

## SUBSECTION — THREE RED SILENCES: ANSWER-STATUS

Screened the whole transcript (T00-T17). For each, whether management VOLUNTEERED, was ASKED, and the outcome.

| Red silence | Volunteered? | Asked by analyst? | Outcome | Status |
|---|---|---|---|---|
| **ROCE trajectory** (Notion tripwire ROCE<18%; 6-yr decline to 20.4%) | No | No | Zero mentions of ROCE, ROE, or returns-on-capital anywhere in the call. Nearest-adjacent (T09 margin-accretion, T14 "judge by our gross margins") never touches capital returns. | **UNANSWERED — silence persists (CONFIRMATORY-NEGATIVE).** 2nd consecutive call. |
| **GST / IT contingent tax** (IT Rs 41.76 Cr, GST Rs 8.56 Cr) | No | No | No mention of any tax demand, litigation, appeal, or contingent liability. West-Asia "logistics cost" [T13] is unrelated. | **UNANSWERED — silence persists (CONFIRMATORY-NEGATIVE).** |
| **US M&A pillar** (dropped ~Rs 400 Cr US QIP / acquisition) | No | No | International expansion is discussed only as organic skid supply [T08]; no M&A, acquisition, QIP, or US capital-raise reference. | **UNANSWERED — silence persists (CONFIRMATORY-NEGATIVE).** |

All three persist untouched. Per Role 5, sustained silence on the deteriorating ROCE metric and the two governance/contingent items is itself a confirmatory-negative signal, captured as CC-F17-01.

---

## SUBSECTION — PROMISE vs DELIVERY / GUIDANCE TRAJECTORY

| Promise (source) | Q1 FY27 status on the call | Verdict |
|---|---|---|
| (a) 25% SFN share-of-revenue by year-end | Deferred: "I would talk about this at the end of the year... we work on a yearly basis" [T07], despite Q1 already ~22-23% ([T01] 23%; analyst [T07] 22%) without full capacity utilisation | **SOFTENED** (CC-F16-01) |
| (b) Q4 exit run-rate ~750 skids/month at 60-65% util on 15,000 | "as of now the way things are planning up we feel that that is intact" [T10] | **ON-TRACK / reaffirmed** (analyst-sourced number, MD-confirmed) |
| (c) 15,000 capacity by Q3 (Notion 60% util on 15k by ~Mar-27) | "an expected Q3... anywhere between October to November... depends on our machine supplier... facing certain delays" [T10]; "start of Q3" [T08] | **SLIPPED / hedged** (supplier-dependent) (CC-F6-01) |
| (d) 25% company EBITDA margin "next few years" | Reiterated twice, aspirational, unquantified: "the target for the company overall is to achieve an... margin of 25% in the next few years and we are right now on track" [T05, T09] | **ASPIRATIONAL / on-track (claimed)** |
| FY27 rev growth ~35% (Q4 guide) | Q1 consol +72.4% YoY [T01] — front-loaded, well ahead | **ON-TRACK / ahead** |
| FY27 EBITDA margin ~23% (Q4 guide) | Q1 23.04% consol [T01] | **DELIVERED / at guide** |
| Skids 20-22% of revenue (Q4 guide) | Q1 ~22-23% [T01] | **AT / top-of-band (slightly above)** |

Net: headline P&L delivered at/above guide; the two forward-looking soft spots are the deferred 25%-SFN-share target and the supplier-dependent 15k-capacity timing.

---

## SUBSECTION — PRIOR-REVIEW OPEN-QUESTION RESOLUTION (review Step 8.5, Q1-Q14)

| # | Prior question (abridged) | On-call outcome | Turn | Status |
|---|---|---|---|---|
| 1 | Firm customer visibility behind 9k/15k capacity | Capacity sized on customer projections; ~2-month tentative dispatch + Q3 project template; no named/committed program count, no order cover | T08, T11 | **PARTIAL** |
| 2 | Skid ASP: mix vs discounting vs scale; where it settles | Driver answered — tailor-made per floor design, Rs 1-5 lakh/skid, not discounting, margin-neutral (assertion); "where ASP settles" not given | T06, T08 | **PARTIAL** (see CC-F16-02) |
| 3 | Q2 FY27 skid-unit expectation + FY27 exit utilisation | Q2 units explicitly declined ("one-to-one basis") [T11]; exit util 60-65%/750-per-month reaffirmed [T10], FY28 80% [T09] | T10, T11 | **PARTIAL** |
| 4 | ROCE definition reconciliation (deck 20.4% vs MD&A 28.43%) | Not addressed | — | **UNANSWERED** (red silence) |
| 5 | When ROCE/ROE inflect back up post-capex | Not addressed | — | **UNANSWERED** (red silence) |
| 6 | Hyd-Air Q1 loss seasonal/deteriorating; diminution provision | Only Hyd-Air's role discussed (internal-use components, not SFN; ~7 Cr rev [T05]); the loss and any diminution provision not addressed | T05, T15 | **UNANSWERED** (loss/impairment) |
| 7 | Deployment schedule for Rs 10.38 Cr idle GCP proceeds | Not addressed | — | **UNANSWERED** |
| 8 | Zero-OCI actuarial treatment | Not addressed | — | **UNANSWERED** |
| 9 | Sustainable FY27 ETR after step-up to 27.4% | Not addressed | — | **UNANSWERED** |
| 10 | Assemblies growth 36.96% (MD) vs 33.60% (chart) | Not addressed (T01 qualitative "even faster"; T05 gave margin bands, not growth) | T01, T05 | **UNANSWERED** |
| 11 | Product-mix chart not footing to 100% (75%/101%) | Not addressed | — | **UNANSWERED** |
| 12 | Tax-auditor split / statutory bandwidth / Italica FY27 RPT cap | Not addressed | — | **UNANSWERED** |
| 13 | Contingent IT Rs 41.76 Cr + GST Rs 8.56 Cr status | Not addressed | — | **UNANSWERED** (red silence — GST/IT) |
| 14 | How skid YoY comparatives presented given ~nil base | Continued voluntary volume (1,040) + value (32.4 Cr) disclosure [T11]; no explicit comparative-framing commitment | T11 | **PARTIAL** |

Tally: **0 fully ANSWERED, 4 PARTIAL (Q1, Q2, Q3, Q14), 10 UNANSWERED.** The call answered the operational demand-visibility and ASP-mechanics questions only in part and left every governance / returns / cash / contingent-tax question untouched — a broad confirmatory-negative consistent with CC-F17-01/02.

---

## SUPPLEMENTARY FORENSIC READS (injected priorities 1, 4, 7, 8, 9)

**1. Management participation (CC-F17-03).** MD Asad Daud answered all 14 analyst turns; no CFO or second executive voice on the recorded transcript (ledger MGMT_ABSENCE). CFO also absent Q4 FY26 per Notion — 2nd consecutive call. On a name whose live concerns are cash conversion, capex absorption and an unresolved ROCE definition, a persistent finance-officer silence is a governance/credibility flag, classified AMBIGUOUS and passed to A4.

**4. Skid-ASP explanation (CC-F16-02, resolves prior A3-F07 PARTIALLY).** MD's design-driven, tailor-made, per-floor costing rationale (Rs 1-5 lakh/skid) is internally coherent and, if true, means the falling reported ASP is a mix artifact rather than discounting or margin compression. It is **credible but unverifiable**: no volume-by-design mix is disclosed, and the exact skid margin was declined [T08] ("blended... same level as the company average"). It therefore only partially closes the prior open question; the "where does ASP settle / is the anchor customer being discounted" leg remains open and is retained as an A4 question.

**7. New disclosures materially reshaping the picture.** Thesis-material new numbers first surfaced on this call (not in deck/filing): ~40 skids per 1 MW liquid-cooled load [T14] (lets analysts translate the 9 GW India pipeline into a revenue proxy — a genuine sizing input); peak hose+assembly revenue 650-675 Cr at 65-66% util / 70% assembly mix [T05] (a core-business ceiling); skid capex Rs 48 Cr and hose capex Rs 54 Cr [T09] (the capex envelope A4 flagged as ND); product-margin bands (hose 16-20%, assemblies 22-26%, fire-hose 23-26% [T05, T12]); Senior plc & Parker Hannifin named as international skid competitors [T04]; West-Asia logistics cost spike as a partial QoQ margin driver [T13]. Non-thesis-moving: Hyd-Air ~7 Cr and metal bellows ~3 Cr this quarter [T05], Hyd-Air internal-use-only [T15].

**8. Deflection pattern / archetype (CC-F7-01).** MD declines specifics on a "public forum" basis for skid margin [T08], customer names [T08], Q2 numbers [T11], international quantum [T08], fire-hose realisation [T07] and own-vs-sourced value split [T14], and twice reframes to "judge us annually not quarterly" [T07, T13]. Archetype reads **guarded-selective on competitive/forward specifics but candid-operational on the core disclosed metrics** (voluntary skid volume 1,040, ASP mechanics, capex 48/54 Cr, margin bands). Not evasive across the board, but the guarded items cluster precisely on the thesis-sensitive unknowns (customer, margin, cash) — hence AMBIGUOUS, lean-bear.

**9. Capex-absorption cross-read (CC-F6-04).** The call worsens, not eases, the Notion capex-absorption / ROCE-denominator concern in the near term: Rs 48 Cr + Rs 54 Cr capex confirmed [T09]; QoQ opex de-leverage of ~+300 bps (employee + other) driven by Pune/Taloja/Chakan facility ramp and West-Asia logistics [T10, T13]; management asserts absorption "in the next few quarters" as Bellows scales [T10] — a claim with no cash-flow evidence (Q1 has no mandated cash-flow statement; first FY27 CFO/PAT read at H1 ~Oct-26). Classified FORWARD-SIGNAL for A4.

---

```yaml
stage: A3-forensics
company: "AEROFLEX"
quarter: "Q1 FY27"
doctype: "concall"
model: claude-opus-4-8
status: complete
forensics_path: "runs/aeroflex-q1fy27/work/forensics_concall_aeroflex_q1fy27.md"
ledger_reconciled_pct: 100
checklist:
  F1: N.A.
  F2: N.A.
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
  F16: FINDING
  F17: FINDING
findings:
  - {id: "CC-F6-01", check: "F6", line: "T10", classification: "FORWARD-SIGNAL", implication: "15,000-skid milestone now supplier-dependent Oct-Nov; slip risk to util/ROCE-recovery path"}
  - {id: "CC-F6-02", check: "F6", line: "T08", classification: "FORWARD-SIGNAL", implication: "New unquantified FY27 international-skid revenue commitment; design differs, customer withheld"}
  - {id: "CC-F6-03", check: "F6", line: "T07", classification: "FORWARD-SIGNAL", implication: "Fire-hose assembly near-dated FY27 catalyst (intl-only, 23-26% margin); size declined"}
  - {id: "CC-F6-04", check: "F6", line: "T09", classification: "FORWARD-SIGNAL", implication: "Rs 48Cr+Rs 54Cr capex + ~300bps opex de-leverage; absorption a claim, untested until H1 CFO; advances capex-absorption/ROCE concern"}
  - {id: "CC-F7-01", check: "F7", line: "T08", classification: "AMBIGUOUS", implication: "Systematic public-forum deflection on margin/customer/Q2/quantum; guarded-selective, lean-bear"}
  - {id: "CC-F7-02", check: "F7", line: "T11", classification: "FORWARD-SIGNAL", implication: "Single intermediary customer, ~2-month visibility, names withheld; concentrated thin order book into a capacity build"}
  - {id: "CC-F14-01", check: "F14", line: "T01", classification: "NEUTRAL-FACT", implication: "Spoken EBITDA 33.12 ties to neither deck figure and contradicts own 23.04% margin (implies 33.49); deck 33.49 governs"}
  - {id: "CC-F14-02", check: "F14", line: "T11", classification: "NEUTRAL-FACT", implication: "Volume 140->1,040 and base 2,000->6,000 transcription slips reconcile to deck; no unreconciled number"}
  - {id: "CC-F16-01", check: "F16", line: "T07", classification: "AMBIGUOUS", implication: "25% SFN-share year-end target deferred, not reaffirmed, despite Q1 ~22-23%; softening of a stated target"}
  - {id: "CC-F16-02", check: "F16", line: "T06", classification: "AMBIGUOUS", implication: "Skid-ASP reframed as non-meaningful/margin-neutral; credible but unverifiable (skid margin declined); partially resolves A3-F07"}
  - {id: "CC-F17-01", check: "F17", line: "T00-T17 (absent)", classification: "CONFIRMATORY-NEGATIVE", implication: "All three red silences (ROCE, GST/IT tax, US M&A) neither asked nor volunteered; 2nd consecutive call"}
  - {id: "CC-F17-02", check: "F17", line: "T11", classification: "CONFIRMATORY-NEGATIVE", implication: "10 of 14 prior questions unanswered; Q2 skid units explicitly declined to one-to-one channel"}
  - {id: "CC-F17-03", check: "F17", line: "T01-T17", classification: "AMBIGUOUS", implication: "No CFO/second voice, 2nd consecutive quarter; governance/credibility signal on a cash-sensitive name"}
forward_signals: ["CC-F6-01","CC-F6-02","CC-F6-03","CC-F6-04","CC-F7-02"]
ambiguous: ["CC-F7-01","CC-F16-01","CC-F16-02","CC-F17-03"]
commitments:
  - {commitment: "Flexible-hose capacity to 20 Mn m", implied_date: "Q3 FY27", ref: "T01,T09", status_word: "underway"}
  - {commitment: "Skid capacity 9,000->15,000 units p.a.", implied_date: "Oct-Nov (Q3 FY27)", ref: "T01,T08,T09,T10", status_word: "slipped"}
  - {commitment: "Fire-hose assembly commercialisation (intl-only)", implied_date: "end-Q2/start-Q3 FY27", ref: "T07,T12", status_word: "underway"}
  - {commitment: "International skid revenue booked", implied_date: "within FY27", ref: "T08", status_word: "initiated"}
  - {commitment: "Skid capex Rs 48 Cr + hose capex Rs 54 Cr remaining", implied_date: "completes FY27", ref: "T09", status_word: "underway"}
  - {commitment: "Skid optimal utilisation ~80%", implied_date: "full-year FY28", ref: "T09", status_word: "guided"}
  - {commitment: "Q4 exit ~750 skids/month at 60-65% util on 15,000", implied_date: "Q4 FY27", ref: "T10,T11", status_word: "reaffirmed"}
  - {commitment: "Company blended EBITDA margin 25%", implied_date: "next few years", ref: "T05,T09", status_word: "aspirational"}
  - {commitment: "Metal/miniature bellows sales uptake", implied_date: "next two quarters", ref: "T05", status_word: "initiated"}
  - {commitment: "Hyd-Air capex plan", implied_date: "when finalized", ref: "T05", status_word: "under-discussion"}
  - {commitment: "25% SFN-share-of-revenue", implied_date: "year-end FY27", ref: "T07", status_word: "softened"}
  - {commitment: "Capacity expansion beyond 15,000 skids", implied_date: "undated", ref: "T08", status_word: "under-discussion"}
gate_a3: pass
blank_checks: []
```
