# A3 FORENSIC NOTES — GNG Electronics Limited (EBGNG) — Q1 FY27 — CONCALL

Source extract: `runs/ebgng-q1fy27/work/extract_concall_ebgng_q1fy27.txt` (113 lines, ASR transcript)
Ledger: `runs/ebgng-q1fy27/work/ledger_concall_ebgng_q1fy27.md` (61 turns, 26 questions, 79 mgmt numbers, 7 ZERO_STANDING)
Prior-quarter transcript: none (first post-listing concall). F17 run against the 8 pre-committed monitorables + the presentation/commitment register supplied in the task, not a QoQ transcript diff.

Ledger reconciliation: 100%. Every N1-N79, Z1-Z7, Q-1..Q-26 and turns 1-61 were read at their cited line in the extract before judging. No orphan ledger row.

Doctype note: this is a transcript. F6/F7/F17 are the primary checks. Most statement/balance-sheet checks are N.A. Two checks the task defaulted to N.A. (F1, F14) are marked FINDING here because the A2 ledger genuinely populates them under the SOUTHWEST convention (F1 = the 7 ZERO_STANDING claimed-zeros) and the transcript-internal-consistency reading (F14 = the CONTRADICTION / NUMBER_DISCREPANCY / AMBIGUOUS_FIGURE cross-cutting flags the task asked me to weigh). Marking them N.A. would leave those flags unhoused; the substance is surfaced with line cites below.

---

## FINDINGS TABLE

| id | check | ledger row | line/turn | verbatim quote (short) | classification | forward implication |
|----|-------|-----------|-----------|------------------------|----------------|---------------------|
| A3F-01 | F1 | Z3 / N67-68 | L98 / T34 | "There is no disruption at all in our UAE... we see no visible damage anywhere" (vs "500 missiles and 2,000 drones have been fired upon UAE") | AMBIGUOUS | UAE = 12% of revenue + refurb hub. Absolute "no disruption" claim against an active conflict is an un-hedged concentration risk. A4 Q on contingency / air-freight cost. |
| A3F-02 | F1 | Z4 / N66 | L94 / T32 | "I don't think there's any significant cause of concern" (re other expenses +68% YoY) | AMBIGUOUS | Opex growing ~2x revenue (32%) dismissed. Operating-leverage timing risk; ties to A3F-09. A4 Q. |
| A3F-03 | F1 | Z5 | L100 / T36 | "we don't have any fixed capital worth talking about... The business is working capital" | CONFIRMATORY-NEGATIVE | On-record confirmation the whole model is WC-absorptive. Explains net debt +Rs100cr QoQ (A3F-24); structural cash-flow drag. |
| A3F-04 | F1 | Z1 / Z2 | L67 / L73 | "we are actually facing negligible competition" / "finding negligible competition" | AMBIGUOUS | Repeated unfalsifiable moat/margin-durability claim underpinning the guidance raise. A4 Q on evidence. |
| A3F-05 | F6 | N45 / N46 | L73 / T15 | "revise our guidance from earlier 25% to 30%... net PAT level margin... 0.5 to 0.75 and 1%" | FORWARD-SIGNAL | Two-part guidance RAISE. Primary promise-tracker line for Role 5. |
| A3F-06 | F6 | N52 / N12 | L85, L35 | "it will continue to rise 5-10% every quarter"; "no meaningful relief... before end of 2027" | FORWARD-SIGNAL | Margin tailwind is management's own dated assumption (through end-2027). Falsifiable each quarter; margins partly ride it despite the "not memory dependent" caveat. |
| A3F-07 | F6 | N73 / N75 | L106 / T42 | "we are pegging our product around 30%... we can bring it from 30 to 50" | FORWARD-SIGNAL | Multi-year realization/margin lever, explicitly disclaimed as "not guidance." Track the 30%→35%→50% ratio as a margin proxy. |
| A3F-08 | F6 | N70 | L100 / T36 | "keep a good amount of 30-40 days of finished inventory" | FORWARD-SIGNAL | Only concrete WC target given. Test vs actual inventory days (Rs700cr on Rs412.5cr/qtr revenue ~ far above 30-40 days of COGS). A4 Q. |
| A3F-09 | F6 | — | L122 / T56 | "operating leverage will obviously kick in very soon" | AMBIGUOUS | Undated ("very soon") after admitting opex runs ahead of revenue "for the next couple of years" (L121-122). Self-contradicting horizon. A4 Q. |
| A3F-10 | F6 | — | L116 / T50 | "More goodness should be seen in the coming quarters... secure material at the old prices" | FORWARD-SIGNAL | Claims procurement immune to the +20-30% new-price inflation. Testable via COGS/procurement cost next 1-2 quarters. |
| A3F-11 | F6 / F7 | N72 | L104 / T40 | "our pie should increase and their share should be significant" (declined exact numbers) | AMBIGUOUS | Redington/Ingram/Supertron contribution promised-directional but unquantified over 12-18 months (Q-16). Open item A3-01/A3-11. A4 Q. |
| A3F-12 | F7 | N42 / N43 | L71 / T13 | "I want to refrain from giving any specific guidance in terms of what margin will come from the penetration in India" | AMBIGUOUS | CFO confirms 21% India / ~30% intl split but refuses to underwrite blended GM as India scales via Redington. Durability of 24.6% at volume unaddressed (A3-09). A4 Q. |
| A3F-13 | F7 | — | L100 / T36 | "Situation is very evolving and current situation demands that we take the call as demanded by situation" | AMBIGUOUS | Deflects the explicit ask for inventory-days / receivable-days / CCC / OCF targets (Q-14). Hedge substitutes for the monitorable. A4 Q. |
| A3F-14 | F7 | — | L87 / T27 | "never say never — we can engage with retailers" (B2C) | NEUTRAL-FACT | Optionality register item; B2C not on roadmap but not foreclosed. |
| A3F-15 | F8 | N65 | L94 / T32 | "between 10 to 12% for the full year on a consol basis" | FORWARD-SIGNAL | Guided FY27 ETR 10-12% vs Q1 print implied ETR ~19% and statutory 25.17%. Full-year guide ~40% below the Q1 run-rate — implies expected DTA/credits or a heavier low-tax step-down mix. Unexplained. A4 Q + promise-tracker. |
| A3F-16 | F14 | N7 / N51 | L35, L85 | "more than doubled" → "they have gone up by five times now" | NEUTRAL-FACT | MD self-corrects mid-call (transparency positive) but a headline data point moved 2x→5x. Data-quality flag; verify actual index. |
| A3F-17 | F14 | N64 | L90 / T30 | "about 1.5% better... On an overall basis 12%" (others ASP QoQ) | AMBIGUOUS | "12%" looks like the laptop YoY figure (N58) misattributed to others/QoQ. Reconcile against the filed results. A4/A5 data check. |
| A3F-18 | F14 | N79 | L70 / T12 | "your consolidated revenue fell almost 37%" (analyst; uncorrected) | NEUTRAL-FACT | Directly conflicts with +32% growth stated twice (L33, L56). Likely ASR/analyst error; management did NOT correct it on record. Silence-on-error noted. |
| A3F-19 | F17 | monitorable #7 | none (L24-129: 0 occurrences) | KKOC / related-party / Rs305 M tax demand — zero mention | CONFIRMATORY-NEGATIVE | Pre-committed governance monitorable went wholly unaddressed; no analyst raised it either. Sustained silence on a governance item. |
| A3F-20 | F17 | monitorables #1, #4 | L100 (deflect); L64 | OCF target deflected; WCL operating-vs-financing classification not mentioned | CONFIRMATORY-NEGATIVE | No cash-flow statement tabled. OCF ask deflected (A3F-13); WCL classification silent while net debt rose. Cash-conversion still unproven. |
| A3F-21 | F17 | monitorable #5 / A3-01,11 | L104 / T40 | distributor contribution "not correct for me to give exact numbers" | AMBIGUOUS | Redington channel revenue still unquantified this quarter. A4 Q. |
| A3F-22 | F17 | FND-04 | none (0 occurrences) | US step-down audit status / FZC-vs-US PAT split — not discussed | CONFIRMATORY-NEGATIVE | Unaudited US step-downs + the low guided ETR (A3F-15) compound: low-tax profit may sit in un-reviewed entities. A4/A5. |
| A3F-23 | F17 | FND-06 | none (0 occurrences) | Diluted-EPS > Basic-EPS Ind AS 33 anomaly — not raised/corrected | AMBIGUOUS | Standing anomaly neither corrected nor explained on the call. Carry to results-filing review. |
| A3F-24 | F17 / F8 | N39-41, N53-54 | L64, L89 | "net debt has increased by about 100 odd crores... to 406 crores" while WC "marginally gone down" and inventory Rs740→700cr | AMBIGUOUS (lean bear) | Net debt +35% QoQ NOT reconciled by a Rs40cr inventory fall and "marginally" lower WC. ~Rs100cr cash use unexplained without a CFS (receivables build? repayment timing?). Implies OCF still negative. A4 Q — the single most important reconciliation gap on the call. |

Findings: 24. FORWARD-SIGNAL: A3F-05, A3F-06, A3F-07, A3F-08, A3F-10, A3F-15. AMBIGUOUS: A3F-01, A3F-02, A3F-04, A3F-09, A3F-11, A3F-12, A3F-13, A3F-17, A3F-21, A3F-23, A3F-24. CONFIRMATORY-NEGATIVE: A3F-03, A3F-19, A3F-20, A3F-22. NEUTRAL-FACT: A3F-14, A3F-16, A3F-18.

---

## CHECKLIST SCORECARD (all 17; one status each)

| # | Status | One-line basis |
|---|--------|----------------|
| F1 | FINDING | 7 ZERO_STANDING claimed-zeros exist (SOUTHWEST convention); UAE "no disruption" (Z3), opex "no concern" (Z4), "no fixed capital" (Z5), "negligible competition" (Z1/Z2) surfaced — A3F-01..04. |
| F2 | N.A. | No standalone-vs-consolidated statements tabled on a concall; only a spoken India-21%/intl-~30% GM split (N42/N43), addressed under F17/A3F-12. |
| F3 | N.A. | No entity-level cost lines on a transcript; shell detection not possible. |
| F4 | N.A. | No auditor Other Matters / component-auditor disclosure in a transcript (US step-down audit status routed to F17/A3F-22). |
| F5 | N.A. | No auditor report or Going Concern / EoM paragraph in a transcript. |
| F6 | FINDING | Forward-commitment lexicon populated: guidance raise, ETR, memory-price path, refurb 30→50%, inventory-days, operating-leverage timing, procurement — A3F-05..11 + register below. |
| F7 | FINDING | Hedge lexicon populated: "refrain from giving specific guidance," "not correct... to give exact numbers," "situation is very evolving," "never say never" — A3F-11..14. |
| F8 | FINDING | Call carries tax numbers: guided FY27 ETR 10-12% consol (N65) vs Q1 implied ~19% and statutory 25.17% — A3F-15; also net-debt/leverage read A3F-24. |
| F9 | N.A. | No OCI / actuarial disclosure in a transcript. |
| F10 | N.A. | Call carries no share-count or basic/diluted-EPS numbers; dilution not computable here (EPS anomaly routed to F17/A3F-23). |
| F11 | N.A. | No balance sheet / reserves / net-worth tie-out in a transcript. |
| F12 | N.A. | No segment assets/liabilities tables; only spoken geo revenue mix (N32-37). |
| F13 | N.A. | Not a Board Outcome letter; no AR/AGM/director-term agenda items. |
| F14 | FINDING | Transcript-internal inconsistencies (the CONTRADICTION/NUMBER_DISCREPANCY/AMBIGUOUS_FIGURE flags): memory 2x→5x (N7/N51), others-ASP 12% misattribution (N64), analyst -37% uncorrected (N79) — A3F-16..18. |
| F15 | N.A. | No consolidation entity list in a transcript; ledger notes no ENTITY_CHANGE. |
| F16 | N.A. | Not an investor presentation; no prior deck to diff for dropped/reframed disclosures. |
| F17 | FINDING | Silence audit vs 8 monitorables + commitment register: KKOC/tax demand, WCL classification, OCF target, US step-down audit, EPS anomaly all unaddressed — A3F-19..24 + table below. |

Counts: FINDING = 6 (F1, F6, F7, F8, F14, F17); N.A. = 11; PASS = 0; blank = 0. GATE A3: PASS.

---

## F6 COMMITMENT REGISTER (promise-vs-delivery feed for A4/Role 5)

| commitment | implied date | turn / line | status word |
|------------|--------------|-------------|-------------|
| Revenue growth raised to 30% FY27 (from 25%) | by Mar-2027 | T15 / L73 | raised — underway |
| PAT margin raised to 0.75-1% FY27 (from 0.5%) | by Mar-2027 | T15 / L73 | raised — underway |
| Consolidated ETR 10-12% FY27 | FY27 | T32 / L94 | guided |
| Memory prices continue +5-10% every quarter | ongoing | T25 / L85 | in progress (external) |
| No meaningful memory-shortage relief before end-2027 | end-2027 | T3 / L35 | asserted |
| Refurb realization 30% → 35% → 50% of new | multi-year | T42 / L106 | intends |
| 30-40 days of finished inventory | ongoing | T36 / L100 | targeting |
| Operating leverage "will kick in very soon" | undated ("soon") | T56 / L122 | pending |
| Procurement at "old prices"; "more goodness in coming quarters" | next 1-2 quarters | T50 / L116 | underway |
| Distributor (Redington/Ingram/Supertron) share "should increase and be significant" | 12-18 months | T40 / L104 | underway — unquantified |
| Onboarding distributors across international markets | ongoing | T3 / L47 | underway |
| No procurement challenge for next couple of quarters | next 2 quarters | T52 / L118 | committed |
| Growth "will not slow down" | FY27 | T60 / L126 | committed |

---

## F17 SILENCE AUDIT

### A) The 8 pre-committed monitorables
| # | Monitorable | Status | Cite | Note |
|---|-------------|--------|------|------|
| 1 | OCF positive | NOT-DISCUSSED (deflected) | L100 | Asked (Q-14); MD answered "situation is very evolving," no OCF number/target. |
| 2 | WC / debtor days (~178 net WC days; debtor 40-45) | PARTIAL / NOT-QUANTIFIED | L64 | CFO: WC "absolutely similar... marginally gone down"; no debtor days, no net WC days. |
| 3 | Gross margin vs <17% falsification line | ADDRESSED (favorable) | L56, L71 | Consol GM 24.6%; India 21%; intl ~30%. Well clear of 17%. |
| 4 | WCL operating-vs-financing classification | NOT-DISCUSSED | L64 | Net debt discussed; WCL classification never raised. |
| 5 | Ingram / Supertron / Redington revenue contribution | NOT-QUANTIFIED | L104 | Rankings given (#1/#2/#5); MD "refrain from giving the exact contribution." |
| 6 | FY27 guidance delivery (~25% rev / ~50 bps margin) | ADDRESSED — RAISED | L73 | Revenue 25%→30%; PAT margin 0.5%→0.75-1%. |
| 7 | KKOC governance / RPT / Rs305 M tax demand | NOT-DISCUSSED | none (L24-129) | Zero mention by management or analysts. |
| 8 | Net debt / leverage (0.53x post-IPO; watch >1.5x) | ADDRESSED (unfavorable direction) | L64 | Net debt Rs406cr, +Rs100cr (+35%) QoQ; gearing not restated. See A3F-24 reconciliation gap. |

### B) Presentation / commitment register + open A3 findings
| Item | Addressed? | Cite |
|------|-----------|------|
| Redington partnership revenue contribution (A3-01/A3-11) | NO — not quantified | L104 |
| EB Elite Program enrolment / revenue / timeline (A3-02) | PARTIAL — launch named, no enrolment/revenue/timeline | L45 |
| FZC-vs-US step-down PAT split + plan to bring US step-downs under audit (FND-04) | NO | none |
| Consolidated ETR trajectory / FY27 tax guidance (FND-05/A3-05) | YES — 10-12% guided | L94 |
| Diluted-EPS > Basic-EPS Ind AS 33 anomaly (FND-06) | NO — not raised/corrected | none |
| Explicit FY27 numeric guidance (A3-04) | YES — 30% rev / 0.75-1% PAT margin | L73 |
| QoQ -36.7% revenue seasonality (A3-08) | PARTIAL — "low seasonality quarter," no numeric bridge | L124 |
| 24.6% gross-margin durability at volume (A3-09) | PARTIAL — split confirmed, blended GM not underwritten | L71 |
| Parent inventory build ~Rs75 Cr / WC absorption (FND-02) | YES — confirmed on record | L71 (N77/N78) |

Sustained-silence confirmatory-negatives (1 consecutive quarter each, being the first post-listing call): KKOC/Rs305 M tax demand (#7), WCL classification (#4), OCF target (#1), US step-down audit status (FND-04). Per Role 5 these become tripwires if silence persists next quarter.

---

## FLAGGED FOR A4 (convert to management questions / promise-tracker)
- FORWARD-SIGNAL: A3F-05 (guidance raise), A3F-06 (memory-price path/end-2027), A3F-07 (refurb 30→50%), A3F-08 (30-40 inventory days), A3F-10 (procurement at old prices), A3F-15 (ETR 10-12% vs ~19% Q1).
- AMBIGUOUS: A3F-01 (UAE no-disruption overclaim), A3F-02 (opex +68% dismissed), A3F-04 (negligible competition), A3F-09 (operating-leverage timing), A3F-11 (distributor share unquantified), A3F-12 (blended GM not underwritten), A3F-13 (WC/OCF targets deflected), A3F-17 (others-ASP 12% misattribution), A3F-21 (Redington contribution), A3F-23 (EPS anomaly), A3F-24 (net-debt +Rs100cr un-reconciled — highest priority).
