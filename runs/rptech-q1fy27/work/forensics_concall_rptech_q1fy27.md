# A3 FORENSIC NOTES — RPTECH (Rashi Peripherals) Q1 FY27 — doctype: CONCALL

Source extract: `extract_concall_rptech_q1fy27.txt` (217 lines, ASR auto-transcription, no page structure).
Ledger reconciled: `ledger_concall_rptech_q1fy27.md` — all 8 sections / every row read at its cited source line. Reconciled 100%.
Filed-results anchors used for Role 5 arithmetic-consistency: Consolidated Rev 5,101.85 Cr / Op EBITDA 155.28 Cr (3.04%) / PBT ~139 / PAT 104.57 (2.05%) / EPS 15.25; Standalone Rev 4,832.22 / PAT 97.15 / PBT ~130; FY26 base Rev 15,827, PAT 282.

Doctype rule applied: on a concall F6/F7/F17 carry the load; balance-sheet checks (F2-F5, F8-F16) are mostly N.A. and are marked so with a one-line basis. Every one of F1-F17 carries exactly one status. No blanks (GATE A3 pass).

---

## LEDGER RECONCILIATION (100%)

Read verbatim at cited lines: Section 1 (19 participants), Section 2 (103 turns), Section 3 (33 questions), Section 4A/4B/4C (110 mgmt numbers), Section 5 (19 forward-commitments), Section 6 (15 hedges), Section 7 (2 zero-standing), Section 8 (flags). No row unread. A2's count-test gate (participants 19, turns 103, questions 33, numbers 110, zero-standing 2, forward 19, hedges 15) accepted; A2 deliberately did NOT resolve any ASR conflict — that reconciliation is done below.

---

## ROLE 5 ARITHMETIC RECONCILIATION (spoken vs filed) — the three flagged conflicts

**(1) EBITDA: MD "155 Cr / 50% growth / (implied 3.04%)" vs CFO "173 Cr / 55% growth / 3.38% margin" — GENUINE DEFINITIONAL CONFLICT, NOT an ASR error.**
- Filing Op EBITDA = 155.28 Cr, margin 3.04%. Kapil's "155 crores" (line 15) matches the filing exactly → operating EBITDA.
- CFO's "173 crores" with "AITA margins at 3.38%" (line 17): 173 / 5,101.85 = 3.39% ≈ the 3.38% he himself quoted. The number and its margin are INTERNALLY CONSISTENT, so 173 is not a mis-transcription of 155 — the CFO is quoting a broader EBITDA (~18 Cr of other income added: 173 − 155 ≈ 18). Two different EBITDA definitions were presented on the same call by MD and CFO with no reconciliation.
- Forensic weight: the filing shows operating margin CONTRACTED ~24 bps YoY. The CFO's 3.38% (other-income-inclusive) obscures that contraction; the "operating leverage is visible… absolute margin grows" narrative (line 15) rests on the higher figure. → FINDING F17-02 (AMBIGUOUS).

**(2) Standalone PAT "97 crores" vs "INR 197 in PAT" — ASR ERROR.** Filing standalone PAT = 97.15 Cr. "97" (line 17, 2.01% margin: 97/4,832 = 2.01% ✓) is correct; the summary "INR 197 in PAT" (line 17) is a genuine ASR mis-transcription of 97. No genuine conflict. Not a finding, resolved.

**(3) Consol revenue "5,12 crores" vs "5,100 crores" — ASR ERROR.** Filing 5,101.85 Cr. Both intend ~5,102; "5,12" is an ASR garble of "5,102". YoY: MD 61.9% (line 15) = filing exactly; CFO "62% rounded off" consistent. Not a finding, resolved.

**Consistent spoken figures (confirm the filing):** Consol PAT 105 ≈ 104.57; Consol PBT 139 ≈ ~139; EPS 15.25 = filing; Standalone Rev 4,832 = 4,832.22; Standalone growth 58% = filing; Standalone PBT 130 ≈ ~130. WC days 56, inventory days 55, debtor days 41, creditor days 40, net debt 1,285 — spoken only, not in the anchor set, carried as UNVERIFIED per A1.

**Filed forensic facts that got ZERO airtime on the call** (feed F17): Q1 inventory build ~₹651 Cr standalone (~5x YoY); consolidated purchases ~₹5,604 Cr EXCEEDED revenue (5,102); write-off provision roughly doubled; net DTA exhausted / ETR up ~+163 bps; operating margin contracted ~24 bps. VDA 67% (₹368.5 Cr) and the Restar JV are POST-period and correctly flagged by mgmt as "coming in Q2 financials" (line 43) — no misstatement there.

---

## FINDINGS TABLE

| id | check | ledger row ref | line / turn | short verbatim quote | classification | forward implication |
|---|---|---|---|---|---|---|
| F1-01 | F1 | Sec7 row1 / Sec4C n/a | line 109 / turn 50 | "currently refurbished business is none but yes… fingers crossed at this moment" | FORWARD-SIGNAL | Repeatedly asked (Qs 10,16); mgmt hedges launch with "fingers crossed" (again line 113). A launch is being contemplated but undated → A4 question on refurbished entry timing/capex. |
| F1-02 | F1 | Sec7 row2 | line 101 / turn 46 | "we don't have a single Japanese manufacturer as a customer" | NEUTRAL-FACT | Stated as the strategic rationale for the Restar JV (zero-base = the whitespace the JV monetises). Confirmatory of JV logic, not a red flag. |
| F6-01 | F6 | Sec5 (19 rows) | see Commitment Register | "In Q2 we will have our numbers much more presentable… numbers are also going to come back reporting… with the quarter 2 financials" (line 43) | FORWARD-SIGNAL | 15 dateable commitments (register below). Priority tripwires for Q2: VDA + JV consolidation, Q2 ~60% growth, $100m JV revenue in 3 yrs, 50+ engineers in 2 yrs. Feeds Role 5 promise-vs-delivery tracker. |
| F7-01 | F7 | Sec6 (15 rows) | lines 53,109,113,185,199 | "orange alert… we track it on a weekly basis" (l.53); "premature" (l.185,199); "fingers crossed" (l.109,113) | AMBIGUOUS | Hedge density clusters on (a) H2 supply/volume risk, (b) refurbished launch, (c) JV investment quantum & margin. Each hedge = pre-emptive cover on a metric mgmt expects to move → A4 questions. |
| F17-01 | F17 | Sec4B (WC-days block) | line 15 / line 17 | "disciplined working capital staying tight at around 56 days"; net debt "1,285 cr" (l.133) | CONFIRMATORY-NEGATIVE | BINDING GATE = Pillar-2 CASH CONVERSION. Management gave NO CFO / operating-cash / free-cash figure anywhere on the call — only working-capital DAYS and net debt. With a ~5x inventory build and purchases > revenue (filing), operating cash flow is almost certainly deeply negative; days-framing substitutes for the cash number on the exact metric the thesis gates on. Silence on the gate = confirmatory negative. |
| F17-02 | F17 | Sec4A #6 vs Sec4B #22/#23 | line 15 vs line 17 | MD "EITA growing 50% to 155 crores"; CFO "AITA grew 55% to INR 173 crores and AITA margins at 3.38%" | AMBIGUOUS | Two EBITDA definitions un-reconciled on one call; the 3.38% (other-income-inclusive) masks the ~24 bps operating-margin CONTRACTION shown in the filing. Hype-vs-substance gap → A4: ask for operating EBITDA bridge and other-income quantum. |
| F17-03 | F17 | Sec4C #66 | line 57 / turn 24 | "roughly about 5% uh business has come from the new Dell commercial business" | CONFIRMATORY-NEGATIVE | Notion checklist expects Dell DOUBLE-DIGIT share; ~5% is below threshold. Addressed but under-delivers vs monitoring bar. When asked the FY27 Dell target (Q8) mgmt said "above the target… that's what I can say" (l.61) — declined a number. |
| F17-04 | F17 | (not in ledger — silence) | n/a | — no quote (absence) | CONFIRMATORY-NEGATIVE | Promoter PLEDGE (checklist: 0%) and promoter HOLDING % (checklist ≥63%) were NOT addressed. Also unaddressed: write-off provision doubling, net DTA exhaustion / ETR +163 bps, consolidated purchases exceeding revenue (all real filing facts). Sustained silence on deteriorating/adverse items. |
| F17-05 | F17 | Sec4C (inventory) | line 71 / turn 31 | "yes, inventory is high but it is not a very big concern… the days of inventory are marginally going down" | AMBIGUOUS | Filing shows ~5x YoY standalone inventory build (~₹651 Cr). Management reframes an absolute 5x build as a POSITIVE ("means July-Aug-Sept sales will be good", l.71) via a days ratio that flatters on a +62% revenue base. Days metric masks the absolute cash lock-up → A4: absolute inventory ₹ and cash impact. |
| F17-06 | F17 | Sec3 Q13/Sec4C #73-74 | line 93 / turn 42 | "Q2 also similar trend will be there. The only correction… speed of the price increase. Price increase speed should be half" | FORWARD-SIGNAL | Explicit Q2 FY27 guidance: ~60% YoY growth but price-driven tailwind decelerating to "half" speed. Sets the deceleration tripwire — if Q2 misses ~60% or price contribution < ~15-17%, thesis WC/margin math cracks. Dated: Q2 FY27 (Sept qtr). |
| F17-07 | F17 | Sec4C #55-57,#59,#70-71 | line 39 / turn 15 | growth bridge: "30 35%… price… 5 to 10%… new… 20 25%… quantity… 10% business is accounted for improved market share" | AMBIGUOUS | Bridge sums to ~65-80% at range tops vs stated 60-62% total growth; the "10% market share" appears to double-count within the 20-25% volume line. Over-attributed decomposition → A4: reconcile the growth bridge to 60-62%. |

---

## CHECKLIST SCORECARD (all 17)

| Check | Status | One-line basis |
|---|---|---|
| F1 ZERO-VALUE STANDING ITEMS | FINDING | 2 spoken nil disclosures (Sec7): refurbished revenue = none + "fingers crossed" (l.109); zero Japanese-mfr customers (l.101). |
| F2 STANDALONE vs CONSOL DECOMP | N.A. | Concall, single period, no period trend possible. One-period gap is clean: subsidiary rev ~269.6 Cr (5.3% of consol), subsidiary PAT ~7.4 Cr (7.1% of consol PAT) — within tolerance, nothing to trend. |
| F3 SHELL-ENTITY DETECTION | N.A. | No standalone-vs-consol cost-line detail in a transcript. (Note: mgmt referenced a subsidiary acquired last-year-Q1 affecting GP/other-expenses geography, l.131 — not shell evidence.) |
| F4 UNAUDITED CONTRIBUTION RATIO | N.A. | No auditor Other-Matters paragraph in a concall. |
| F5 GOING CONCERN / EoM SCOPE | N.A. | No audit EoM language in a concall. |
| F6 FORWARD-COMMITMENT MINING | FINDING | 19 forward-commitment phrases (Sec5) → 15 dateable commitments in the register. |
| F7 HEDGE PHRASE MINING | FINDING | 15 hedges (Sec6) clustering on H2 supply risk, refurbished launch, JV quantum/margin. |
| F8 TAX FORENSICS | N.A. | No ETR / deferred-tax discussion in the transcript. NOTE: filing's net-DTA exhaustion / ETR +163 bps went entirely unmentioned → carried in F17-04. |
| F9 OCI FORENSICS | N.A. | No OCI / actuarial disclosure in a concall. |
| F10 SHARE COUNT & DILUTION | N.A. | Only diluted EPS 15.25 given (matches filing); no share count or basic-vs-diluted spread. |
| F11 RESERVES / NET WORTH TIE-OUT | N.A. | No equity build in a transcript; ROE 19.8% and net debt 1,285 alone insufficient. |
| F12 SEGMENT FORENSICS | N.A. | No segment assets/liabilities in a transcript (only qualitative consumer/commercial/semicon commentary). |
| F13 BOARD OUTCOME | N.A. | No AR/AGM/board-resolution/director-term content in a concall. |
| F14 NOTE-DRAFTING INCONSISTENCIES | N.A. | Name/entity inconsistencies present (UNAT vs Monarch Capital; CEO Rajes/Rajesh; CFO spellings; JV stake 74/"60 26") but these are ASR transcription artifacts per A1, not audited-note drafting. |
| F15 ENTITY LIST DIFFS | N.A. | No consolidation list to diff in a transcript. NEW entities announced (VDA Info Solutions 67%; JV "Rashi Restar Semiconductor Solutions Pvt Ltd", step-down subsidiary) are POST-period and captured as F6 commitments; expect the consolidation list to change in Q2. |
| F16 PRESENTATION-SPECIFIC | N.A. | Doctype is concall, not a slide deck. |
| F17 CONCALL SILENCE AUDIT | FINDING | Binding-gate CFO/cash silence + 6 unaddressed adverse items + Dell below checklist bar + margin-definition masking. See "What Was NOT Discussed" below. |

---

## COMMITMENT REGISTER (from F6 — Section 5)

| # | Commitment | Implied date | Ref (turn/line) | Status word |
|---|---|---|---|---|
| 1 | VDA numbers "much more presentable"; update on acquisition direction | Q2 FY27 results (~Nov 2026) | 17 / 43 | underway |
| 2 | JV numbers to "come back reporting… with the quarter 2 financials" | Q2 FY27 results | 17 / 43 | initiated |
| 3 | JV incorporated as "Rashi Restar Semiconductor Solutions Pvt Ltd" (step-down subsidiary; Restar to take 26%) | announced now; close post-period | 46 / 101 | initiated |
| 4 | "we will get all the products and solutions… distributed by Restar" (subject to OEM contracts) | post JV close | 46 / 101 | underway |
| 5 | "we will get access to all the Japanese manufacturers in India" / "we will get Japanese customers" | post JV close | 46 / 101 | initiated |
| 6 | "we will send them [design engineers] to Tokyo" + "50 plus local engineering hires over next two years" | by ~FY28-29 | 3 / 15; 46 / 101 | initiated |
| 7 | Two new branches Udaipur & "Doule" (Dhule?) opened | this quarter | 3 / 15 | completed |
| 8 | Large-deal pipeline "will continue to be there for next three quarters at least" | through Q4 FY27 | 55 / 119 | underway |
| 9 | Large deals "we can always take it in [JAS] quarter itself and you will see some of them" | Q2 FY27 (JAS) | 57 / 123 | initiated |
| 10 | VDA "value creation… in next 2 to 3 years" | FY29-30 | 20 / 49 | initiated |
| 11 | VDA-JV integration for data-center bidding "a little few quarters away" | ~FY27-28 | 73 / 155 | initiated |
| 12 | JV "revenue of more than 100 million US dollars… in next 3 years maximum" | by ~FY30 | 89 / 187; 95 / 199 | initiated |
| 13 | Q2 guidance: "similar trend" ~60% YoY growth; price-increase speed "should be half" | Q2 FY27 | 42 / 93 | guidance (underway) |
| 14 | Restar 26% stake investment amount — deferred to FMV/SPA, "premature" to quantify | on SPA execution | 88 / 185 | not-quantified |
| 15 | Refurbished business launch — "fingers crossed", no timeline given | undated | 50 / 109; 52 / 113 | not-initiated |

Status-transition note (for the Q2 promise-vs-delivery tracker): items 1, 2, 3, 13 are the hard Q2 milestones — each carries an explicit "Q2 financials" or "Q2 growth" hook and will either transition initiated→underway→reported or slip. Item 15 (refurbished) is a standing non-commitment; item 14 (JV consideration) is a standing "premature" deferral — both to be re-tested for a status change next quarter.

---

## F17 — "WHAT WAS NOT DISCUSSED" TABLE (silence audit vs F6 + Notion checklist)

| Item (checklist / filing fact) | Addressed on call? | Consecutive-quarter silence* | Note |
|---|---|---|---|
| CFO / operating cash flow / free cash (BINDING GATE — Pillar 2 cash conversion) | NO — only WC/inventory/debtor DAYS + net debt given | ≥1 (this call) | Highest-priority silence; days-framing substitutes for the gate metric amid ~5x inventory build. |
| CFO/PAT ratio | NO | ≥1 | Cannot be computed from anything given; not volunteered. |
| Promoter pledge (target 0%) | NO | ≥1 | Not mentioned. |
| Promoter holding % (target ≥63%) | NO | ≥1 | Only VDA-founder staged stake mentioned (l.15), not Rashi promoter holding. |
| Write-off / provision (filing: roughly doubled) | NO | ≥1 | Adverse filing fact absent from commentary. |
| Net DTA exhaustion / ETR +163 bps (filing) | NO | ≥1 | Tax narrative entirely absent. |
| Consolidated purchases > revenue (~₹5,604 Cr vs 5,102) | NO | ≥1 | Not surfaced; ties to inventory build and cash silence. |
| Operating-margin contraction ~24 bps YoY | NO — reframed as expansion via 3.38% incl. other income | ≥1 | See F17-02. |
| Dell double-digit share (checklist) | ADDRESSED but ~5% (below bar) + declined FY27 number | — | See F17-03. |
| WC days ≤58 | ADDRESSED: 56 (meets) | — | Spoken only, unverified. |
| Debtor days ≤50 | ADDRESSED: 41 (meets) | — | ASR unit-word missing, per A2 flag. |
| EBITDA margin ≥2.7% | ADDRESSED: 3.38% (incl. other income) / 3.04% operating (both meet) | — | Definitional caveat F17-02. |
| Semicon >50% YoY | ADDRESSED: +70% YoY (meets), clarified l.89 | — | Initial "70% of last year's revenue" phrasing mis-heard by an analyst, self-corrected. |
| Net D/E ≤0.5x | ADDRESSED: "around 0.5" (borderline); would go "2x" if large AI-infra deals pursued | — | Forward tripwire per thesis-broken trigger (D/E >1.0x two quarters). |
| ROCE >17% | ADDRESSED: ROC ~19.5% / ROE 19.8% annualised (claim meets) | — | Annualised claim; unverified. |

*Consecutive-quarter silence marked ≥1 because no prior-quarter concall extract was provided to A3; A4 should extend the counter using the run history.

---

## CLASSIFICATION SUMMARY

- FORWARD-SIGNAL (flag to A4 → management questions): F1-01, F6-01, F17-06.
- AMBIGUOUS (flag to A4 → management questions): F7-01, F17-02, F17-05, F17-07.
- CONFIRMATORY-NEGATIVE: F17-01, F17-03, F17-04.
- NEUTRAL-FACT: F1-02.

Single most decision-relevant item: **F17-01 — total silence on cash flow / CFO on the exact pillar (cash conversion) the position gates on, delivered alongside a ~5x inventory build and purchases exceeding revenue.** Per the binding gate, INDETERMINATE cash conversion cannot resolve to PROCEED; this caps the review at PROCEED WITH CAVEATS with the missing evidence (Q1 FY27 operating cash flow) named.

---

```yaml
stage: A3-forensics
company: "RPTECH"
quarter: "Q1FY27"
doctype: "concall"
model: claude-opus-4-8
status: complete
forensics_path: "/home/user/inflection-pipeline/runs/rptech-q1fy27/work/forensics_concall_rptech_q1fy27.md"
ledger_reconciled_pct: 100
checklist:
  F1: FINDING
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
  F14: N.A.
  F15: N.A.
  F16: N.A.
  F17: FINDING
findings:
  - {id: "F1-01", check: "F1", line: "109 / turn 50", classification: "FORWARD-SIGNAL", implication: "Refurbished revenue = none, hedged 'fingers crossed'; launch contemplated, undated -> A4 question."}
  - {id: "F1-02", check: "F1", line: "101 / turn 46", classification: "NEUTRAL-FACT", implication: "Zero Japanese-mfr customers = stated rationale for Restar JV."}
  - {id: "F6-01", check: "F6", line: "43 / turn 17 (+Sec5 19 rows)", classification: "FORWARD-SIGNAL", implication: "15 dateable commitments; Q2 milestones = VDA+JV consolidation, ~60% growth, $100m JV/3yr."}
  - {id: "F7-01", check: "F7", line: "53,109,113,185,199", classification: "AMBIGUOUS", implication: "Hedges cluster on H2 supply risk, refurbished launch, JV quantum/margin -> A4 questions."}
  - {id: "F17-01", check: "F17", line: "15 / 17 / 133", classification: "CONFIRMATORY-NEGATIVE", implication: "No CFO/operating-cash figure on the binding cash-conversion gate; only WC days + net debt amid ~5x inventory build; caps at PROCEED WITH CAVEATS."}
  - {id: "F17-02", check: "F17", line: "15 vs 17", classification: "AMBIGUOUS", implication: "155 Cr operating EBITDA (filing) vs CFO 173 Cr/3.38% (incl other income) masks ~24bps operating-margin contraction -> A4 EBITDA bridge."}
  - {id: "F17-03", check: "F17", line: "57 / turn 24 (+61)", classification: "CONFIRMATORY-NEGATIVE", implication: "Dell ~5% below checklist double-digit bar; declined FY27 Dell number."}
  - {id: "F17-04", check: "F17", line: "n/a (absence)", classification: "CONFIRMATORY-NEGATIVE", implication: "Silent on promoter pledge, promoter holding, write-off doubling, DTA exhaustion/ETR +163bps, purchases>revenue."}
  - {id: "F17-05", check: "F17", line: "71 / turn 31", classification: "AMBIGUOUS", implication: "~5x absolute inventory build reframed as strength via days ratio on +62% base -> A4 absolute inventory/cash impact."}
  - {id: "F17-06", check: "F17", line: "93 / turn 42", classification: "FORWARD-SIGNAL", implication: "Explicit Q2 FY27 guidance ~60% growth, price contribution 'half' speed; deceleration tripwire."}
  - {id: "F17-07", check: "F17", line: "39 / turn 15", classification: "AMBIGUOUS", implication: "Growth bridge sums ~65-80% vs 60-62% stated; 10% market share likely double-counts volume -> A4 reconcile."}
forward_signals: ["F1-01", "F6-01", "F17-06"]
ambiguous: ["F7-01", "F17-02", "F17-05", "F17-07"]
commitments:
  - {commitment: "VDA numbers presentable + direction update", implied_date: "Q2 FY27 results", ref: "17/43", status_word: "underway"}
  - {commitment: "JV numbers into Q2 financials reporting", implied_date: "Q2 FY27 results", ref: "17/43", status_word: "initiated"}
  - {commitment: "JV 'Rashi Restar Semiconductor Solutions Pvt Ltd' formed; Restar 26%", implied_date: "post-period close", ref: "46/101", status_word: "initiated"}
  - {commitment: "Access to Restar-distributed products/solutions", implied_date: "post JV close", ref: "46/101", status_word: "underway"}
  - {commitment: "Access to Japanese manufacturers/customers in India", implied_date: "post JV close", ref: "46/101", status_word: "initiated"}
  - {commitment: "50+ local engineering hires + Tokyo training", implied_date: "by ~FY28-29", ref: "3/15;46/101", status_word: "initiated"}
  - {commitment: "Two branches Udaipur & Dhule opened", implied_date: "this quarter", ref: "3/15", status_word: "completed"}
  - {commitment: "Large-deal pipeline for next 3 quarters at least", implied_date: "through Q4 FY27", ref: "55/119", status_word: "underway"}
  - {commitment: "Take large deals in JAS quarter 'you will see some'", implied_date: "Q2 FY27", ref: "57/123", status_word: "initiated"}
  - {commitment: "VDA value creation in 2-3 years", implied_date: "FY29-30", ref: "20/49", status_word: "initiated"}
  - {commitment: "VDA-JV integrated data-center bidding 'few quarters away'", implied_date: "~FY27-28", ref: "73/155", status_word: "initiated"}
  - {commitment: "JV revenue >$100m in 3 years", implied_date: "by ~FY30", ref: "89/187;95/199", status_word: "initiated"}
  - {commitment: "Q2 ~60% growth, price-increase speed 'half'", implied_date: "Q2 FY27", ref: "42/93", status_word: "underway"}
  - {commitment: "Restar 26% stake consideration (FMV/SPA, 'premature')", implied_date: "on SPA execution", ref: "88/185", status_word: "not-quantified"}
  - {commitment: "Refurbished business launch ('fingers crossed')", implied_date: "undated", ref: "50/109;52/113", status_word: "not-initiated"}
gate_a3: pass
blank_checks: []
```
