REWORK

# INDNIPPON gate recommendation (Phase 1 lite, run 2026-09-10)

Verdict: REWORK. Selection rule 1 fired. This verdict judges the pipeline, not the stock. It says the evidence pack is incomplete. It says nothing about whether India Nippon Electricals is a good or bad business. The run does not halt. The verdict is not a KILL.

Partial status, carried into this verdict block by rule: the promoter stage returned status partial, because WebSearch was unavailable for the whole session and SEBI, MCA, court and pledge searches were skipped. The market sizing stage returned status partial for the same reason, and the electric vehicle content per vehicle number stayed NOT FOUND. Both partial stages touch decision relevant questions.

Freshness: FRESHNESS PAIRS OK. The freshness cap and the first line rule do not apply. Corpus audit: CORPUS GAPPED. The shareholding pattern filing is absent, and the promoter pledge position is UNRESOLVED.

Phase 1 scope: this is the gate decision on evidence alone. No valuation ran. This file carries no investment decision, no entry range, no margin of safety price, no destination PE and no Hurdle verdict. Phase 3 forms the investment decision on a signed model.

## Why REWORK

Two triggers fired, and either one alone forces the verdict.

1. The red flag verifier's acceptance rate is 29%, below the 60% floor. It caught 7 of 24 independent red flag items that upstream stages should have found.
2. The overall phase 1 confidence is 29, below the 60 band floor.

The red flag verifier also raised two CRITICAL findings. They are verifier B findings, so the literal Verifier A CRITICAL clause does not fire. They are the substance behind the acceptance rate trigger.

The numbers verifier came back clean: 175 of 180 claims verified, zero CRITICAL. The peer verifier found all 12 peer transcripts used substantively. Every flag the concall and peer stages raised survived the red flag verifier's check. The problem is missing work, not wrong work.

## What the rework is

No stage reconciled the investor decks and the MD&A against the audited notes and the Regulation 33 results filing. The deck and narrative stage read the decks and the annual report narrative. The Gate 0, notes and annual report stages read the audited statements. No stage put the two side by side. Twelve red flag grade items sat in that seam until the red flag verifier did the operation itself.

Failing stages: stage 5 (deck commentary, run in no concall mode) and stage 6 (peers) did not perform the reconciliation. Stage 4 (business model) saw the deck ROCE series and accepted it as "directionally consistent" instead of testing it against the audited ratio note.

A rerun must fix the following, in this order:

1. Rebuild FY26 and FY25 EBITDA margin on the audited basis from the Reg 33 results filing and AR2026 Notes 29 and 35, and state whether foreign exchange gains sit in operating expenses or in other income.
2. Reconcile the deck ROCE (34.97%) to the audited Note 51 ROCE (17%) and name the capital employed definition behind each.
3. Reconcile every deck and MD&A headline figure to its audited source: net profit margin 13.7% against 10.40%; three FY26 revenue bases; three ROE figures; deck EPS 49.14 consolidated against AR EPS 49.18 standalone; three employee counts; working capital days 42 to 40 against 40 to 42 against 51.48.
4. Test the transition claim against the filed spend: R&D (Note 43), advertising and sales promotion (Note 37), segment reporting (single audited segment against unaudited deck mix).
5. Test the related party receivables: the Lucas Indian Service receivable stretch (Note 42).
6. Route the margin and ROCE figures to Verifier A for a source fidelity read, then rerun the red flag verifier on the reconciled pack.
7. Carry the Gate 0 correction (core 54, grand 73) and the two corrected peer citations into every downstream use.

## First live verification items (open cross verifier conflicts, carried unresolved)

These three items are open. This file does not adjudicate them. They are the first items for Halt 1 and live verification.

| # | Item | Position A | Position B | Status |
|---|---|---|---|---|
| a | FY26 audited basis EBITDA margin | Deck: 11.27% FY25 to 11.44% FY26 (Q4FY26 deck p.16) | Verifier B, CRITICAL: 11.11% FY25 to 11.10% FY26, flat to down; deck nets FX gains of Rs 3.72 Cr FY26 against Rs 1.02 Cr FY25 into operating expenses, while AR2026 Note 29 books them in other income (Reg 33 results filing 2026-08-07 p.4; AR2026 Note 29, Note 35) | OPEN. Not examined by Verifier A; its single re-invocation is spent. No phase 3 margin input may use FY26 until this is resolved. |
| b | FY26 ROCE | Deck: 34.97% (Q4FY26 deck p.19; Q1FY27 deck p.18) | Audited: 17% (AR2026 Note 51, PDF p.235). Verifier B, CRITICAL: 2.06 times gap on an undisclosed definition that appears to strip the Rs 531.5 Cr investment book from capital employed | OPEN. Definition undisclosed. The gap spans three rungs of the quality ladder. |
| c | Credibility grade | Stage 5 filed C (no concall default, not raised to B) | Verifier B would grade D, because the two headline quality metrics in the deck differ from the audited notes | UNRESOLVED. Both grades carried. The operator rules. |

## Phase 1 confidence delta

| Component | Value | Source block | Note |
|---|---|---|---|
| numerical_acceptance | 97.2% | B12a (re-invocation, 180 claims, 175 clean) | Zero CRITICAL. One false MAJOR withdrawn. |
| redflag_coverage | 29% | B12b (7 caught of 24) | Weakest. Forces REWORK on its own. |
| framework_adherence | 82% | B12c (phase 1 scope: Gate 0 23 of 29, EM 24 of 28) | Valuation audit pending phase 3. |
| peer_utilisation | 100% | B12d (12 of 12 substantive) | Two citation MAJORs, claims stand. |
| overall | 29 | min of the four | Band: BELOW 60, FORCED REWORK. |

Weakest component: red flag coverage at 29%. Every one of the 12 missed items comes from the deck against audited reconciliation that no stage performed.

## Flag blocks

```
⚠️ CASH CONVERSION FLAG: CFO/PAT fell to 0.36x in FY26 from 0.60x in FY25; deteriorating.
Determination: INDETERMINATE.
Evidence:
- CFO Rs 40.47 Cr against PAT Rs 111.26 Cr FY26; CFO Rs 49.40 Cr against PAT
  Rs 82.03 Cr FY25 (AR2026 standalone cash flow statement p.182, p.185-186;
  B03 FLAG-CASH).
- Receivables plus inventory absorbed Rs 54.17 Cr (AR2026 cash flow statement
  p.185-186; B03). Capex Rs 42.15 Cr, up 81.3%, no named project; FCF about
  minus Rs 1.7 Cr (B00 LB1; B07 FLAG-CASH-CONTRADICTS-G1).
- Rating agency quote: NONE EXISTS. The company is debt free with no rated
  facilities, so no rating rationale was issued (B00 input_gaps, rating/).
- Capex commissioning timeline: NOT FOUND. No project, capacity or
  commissioning date named in either AR or any deck (B03 input_gaps; B05
  peer question 9). Capital commitments rose to Rs 26.35 Cr from Rs 3.67 Cr
  (AR2026 Note 45; B12b MINOR).
- Receivables composition: near term overdue bucket (under 6 months) up
  152.4%, Rs 16.99 Cr to Rs 42.90 Cr, against 26.5% revenue growth; overdue
  share 15.3% FY24, 11.1% FY25, 22.3% FY26; not yet due share fell 88.9% to
  77.7% (AR2026 Note 13c p.208-209; FY25 AR p.211; B02 receivables_trend).
- Zero ECL recognised both years; the justification paragraph is new text in
  FY26, absent from the FY25 AR (AR2026 Note 13, 48(i) p.232-233; FY25 AR
  Note 46(i) p.233; B02 top_findings rank 2).
- Note 13c gives no split of overdue receivables by debtor (B02 red_flags;
  B02 questions_for_mgmt 1).
- Parent receivable: Lucas Indian Service receivable up 65.7%, Rs 10.89 Cr to
  Rs 18.05 Cr, on sales to it up 22.2%, about 80 to about 108 days (AR2026
  Note 42, PDF p.226-227; B12b MAJOR).
- Peer read: Varroc, on record, "there is no change [in] receivable days...
  it's a temporary increase" (VARROC Aug2026 concall, extraction page 16,
  printed page 15 of 18, as corrected by B12d); no peer reports an overdue
  build (B06 contradicted[0]; verified by B12d).
- Working capital days, three company figures: AR letter 42 to 40 (AR2026
  p.9); decks 40 to 42 (Q4FY26 deck p.19; Q1FY27 deck p.18); computed 51.48
  from 40.64 in FY24 (B01 data_notes; B12a MAJOR, classified COMPANY ANOMALY).
- Growth reading support: company states "Working capital requirements
  increased during the quarter, primarily due to strategic build-up of magnet
  inventory" (Q3FY26 deck p.14; B05 report). Raw material inventory up 40.8%,
  finished goods down 9.2%, no channel stuffing signal (AR2026 Note 12 p.208;
  B02 rank 6).
Why INDETERMINATE: the inventory half of the drag has a stated, dated
growth cause. The receivables half does not. The overdue SHARE doubled, not
only the rupee amount; the parent receivable stretched; the only peer asked
denied an industry effect; the zero ECL defence is new. That leans
structural on receivables. But without a debtor split, a timing slip by one
large OEM at year end and a broad collection problem produce the same Note
13c table.
Missing evidence that separates the two readings:
1. The debtor level split of the Rs 42.90 Cr overdue bucket: two large OEMs
   against the smaller tail (management disclosure; not in AR2026).
2. The Sep-2026 half year statement of assets and liabilities and half year
   cash flow in the Q2 FY27 Reg 33 results filing (BSE scrip 532240): do
   trade receivables fall back toward revenue growth, and does H1 CFO
   recover?
3. The FY27 AR Note 13c ageing table and any ECL booked.
Cap: INDETERMINATE caps the verdict at PROCEED WITH CAVEATS. It never
resolves to PROCEED. The REWORK verdict above is more severe and stands; this
cap binds any post rework verdict until the missing evidence is in hand.
Falsifying observation for a GROWTH-INDUCED reading, if later argued: FY27
CFO/PAT below 0.4x for a second consecutive year (B04 must_track_metrics red
flag), or a further rise in the overdue share above 22.3% in the FY27 Note 13c
table (B03 monitorables).
```

```
PROMOTER STATUS (not a mandatory FLAG-PROMOTER block: verdict is CAUTION, not
CONCERN or AVOID). Verdict: CAUTION. Stage status: PARTIAL (WebSearch
unavailable all session; SEBI, MCA, court and proxy advisor searches skipped)
(B08 status, searches_skipped).
Top findings: [1] Dual managing director interlock. Arvind Balaji is MD of
INEL and MD of Lucas TVS, INEL's largest investment at Rs 264.12 Cr, 32.2% of
net worth and the sole FY26 Key Audit Matter, valued at a flat 8x EV/EBITDA on
an undisclosed EBITDA, with INEL's ownership percentage undisclosed (AR2026
Note 47(f)-(g) p.228; Note 42.1 p.223; B08 adverse_findings). [2] MAHLE's
whole founding stake moved to Lucas Indian Service by inter se transfer on
26-Jun-2023 at an undisclosed price, promoter stake 50.80% to 70.32% (FY25 AR
Shareholding Pattern note p.8; B08). Also: apprentice stipend to TVS
Educational Society Rs 30.59 Cr FY26, up 26.7% (AR2026 Note 42.2 p.224;
figure confirmed by Verifier A re-read).
Pledge: UNRESOLVED. No primary shareholding pattern filing in the corpus; the
AR carries no pledge disclosure (B00; B08 pledge_trend).
Transition evidence: external CFO hire, Saravana Kumar M, from 01-Oct-2026
(Q1FY27 board outcome filing 07-Aug-2026, Annexures C-D); both independent
directors renewed for second terms, zero mid term exits (Change in
Directorate filing 31-Jul-2026; AGM outcome 30-Jul-2026) (B08
transition_evidence). Counterpoint: the outgoing CFO cessation is absent from
the Q1FY27 deck and the filing calls it both a resignation and a designation
change (results filing 2026-08-07 pp.1-2, 6-7; B12b MAJOR).
```

```
FLAG-GATE0: Classification AVERAGE. Core 54/100 (corrected from 56; A1 median
ROCE 13.68% re-scored 3 to 1 per the band table), grand 73/160 (from 75),
moat 19/60, moats_confirmed 5/12 (B01; B12c F-GATE0-01).
Depressors: Block B cash generation 5/20 (cumulative CFO/PAT 70.5% over ten
years; FY26 FCF negative; WC days up 10.8 over FY24-FY26) (B01 flags). Block A
7/20, driven by formula ROCE 11.4% to 15.0% FY24-FY26 on a capital base that
holds the Rs 531.5 Cr investment book; operating ROCE net of the book computed
at 21.9%, 26.4%, 30.5% (B01 data_notes). Block A below 8 now triggers the max
GOOD deal breaker, non binding at AVERAGE (B12c).
Historical or current: Block A depression is structural to the balance sheet
(treasury book), not a legacy cleanup. Block B depression is current, FY26.
AVERAGE caps nothing; it is recorded.
```

```
UA QUALIFIER (fact for phase 3, not a valuation): UA MULTIPLIER WITHHELD.
q1 listed 12 months or more: PASS. q2 Gate 0 core 60 or more OR EM 25 or more:
FAIL on both limbs (core 54; EM 24). q3 FII plus DII under 3%: PASS (FPI 0.41%
at 31-Mar-2026, AR2026 CG Report shareholder table) (ua-qualifier-check).
EM misses by one point. Treat as live at Halt 1, not settled.
```

## Transition decision matrix: posture not assigned

The Mental Model is unsigned and the recognition gap is a stage 11 output, so this file assigns no posture. The evidence informs two of the three state variables. Both stay open questions for Halt 1.

- Proof gate. The proof the transition needs is a measured rise in content per vehicle or a mix driven margin rise. The company discloses no product revenue split. The only quantitative margin support is the deck expansion from 11.27% to 11.44%, which Verifier B says disappears on the audited basis (item a above). R&D spend was flat and R&D capex fell 41.7% (AR2026 Note 43). The run found nothing that fires a proof gate. The Part B3 gate itself is not yet declared.
- Ugliness classification. The ugly optic is the cash break. ARTIFACT OF CLIMB fits the inventory half (declared magnet build). STRUCTURAL FEATURE fits the receivables half (overdue share doubled, parent receivable stretch, zero ECL with new defence text). This is the same question as the cash determination, and it is INDETERMINATE on current evidence.
- Recognition gap. Not informed. Stage 11 resolves it in phase 3.

## Contradicted claims

From the peer stage (priority monitoring items):

1. Claim that INEL's overdue receivables build is an industry wide OEM payment cycle effect. Contradicted by Varroc: "there is no change [in] receivable days... it's a temporary increase" (VARROC Aug2026 concall, extraction page 16, printed page 15 of 18). The peer stage notes Varroc's customer mix differs, so this removes the default benign reading. It does not prove a company specific cause.
2. Partially verified, weight as a contradiction on degree: INEL's Q1 FY27 comparator of 20% industry growth understates the 22% to 23% that Varroc (22.8%), Pricol (22%) and Minda Corp (23%) report for the same quarter (Aug2026 concalls of each), so the 35.5% against 20% gap overstates the edge.

Inside the company's own documents (found by the evidence stages and verifiers, carried for the same monitoring use):

3. Working capital days: AR letter 42 to 40 (AR2026 p.9) against decks 40 to 42 (Q4FY26 deck p.19; Q1FY27 deck p.18).
4. Customer dependence "progressively reduced" (AR2026 MD&A p.126) against two customer share 67.33% FY24 to 70.65% FY26 (Note 28e, both ARs).
5. Net profit margin 13.7% (AR2026 MD&A p.125) against audited net profit ratio 10.40% (AR2026 Note 51, PDF p.297).
6. "Constant sales promotion efforts" (all five decks p.7) against advertising and sales promotion down 30.8%, Rs 3.86 Cr to Rs 2.67 Cr (AR2026 Note 37, PDF p.220).
7. BorgWarner EFI ECU licensing slide repeated for five quarters (decks Aug-2025 to Aug-2026) against the AR's in house EFI controller development (AR2026 p.23 to 24). Verifier B grades this route confusion, PARTIAL rather than MISSED, because the same AR records EFI ECU nominations (AR2026 p.16).

## Monitorables and triggers

1. Watch the overdue receivables share in each half year balance sheet and in the FY27 Note 13c table. FY26 closed at 22.3% with zero credit loss provision (AR2026 Note 13c). A further rise, or a first provision booked, says the cash break is structural. This tests the ugliness classification.
2. Watch full year cash conversion. FY26 CFO/PAT was 0.36x (AR2026 cash flow statement). Recovery toward 0.7x supports a one year build; a second year below 0.4x says the business now needs more working capital per rupee of sales. Find it in the FY27 cash flow statement and the half year cash flow in the Q2 FY27 results filing.
3. Rebuild the operating margin from every Reg 33 results filing yourself: revenue minus total expenses, with other income and FX gains kept out. The audited basis read was 11.10% for FY26 (Reg 33 results filing 2026-08-07 p.4, per Verifier B, unverified by Verifier A). A rise on this basis is the only proof the mix shift is paying. Ignore the deck margin until item (a) is resolved.
4. Compare company revenue growth with SIAM two wheeler growth each quarter. FY26 was 26.5% against 36.1% (AR2026 p.118); Q1 FY27 was 35.5% against a peer reported 22% to 23%. Two quarters below SIAM growth would show the company losing share or content. Source: SIAM monthly release and the results filing.
5. Watch two customer concentration in Note 28e on the percentage basis. It was 67.33% in FY24 and 70.65% in FY26. A rise above 75%, or a third customer above 10%, deepens the single point of failure (AR2026 Note 28e; stage 4 must track metric).
6. Watch magnet exposure: any disclosed ferrite substitution percentage, any named alternate supplier, and material cost as a share of revenue in each results filing. Rare earth supply has been named as a live risk in five consecutive decks with no number attached (AR2026 p.125; decks Q1FY26 to Q1FY27). An unwarned material cost jump would hit both the magneto base and the new motor lines.
7. Watch the Lucas TVS and Lucas Indian Service links in the FY27 AR: the Note 47 valuation multiple (8x, flat two years; Rs 16.51 Cr of value per 0.5x move), any disclosure of INEL's ownership percentage, and the Lucas Indian Service receivable days (about 108 in FY26, AR2026 Note 42). These test governance and the book value of 32.2% of net worth.
8. Watch delivery on the product promises: the 3 kW motor controller commercial rollout due by end CY2026, the EFI ECU route, and R&D spend in Note 43 (Rs 28.77 Cr FY26, flat). Delivery with rising R&D supports the transition; another silent drop weakens it (AR2026 p.82, Note 43).

## Falsification line

The Q2 FY27 Reg 33 results filing, with its Sep-2026 half year statement of assets and liabilities and half year cash flow: trade receivables growing faster than revenue again, with half year CFO still below 0.4x of half year PAT, would do the most damage. It would make the cash break a second period running and push the ugliness classification toward STRUCTURAL.

## Gaps and where to close them

| Gap | Needed by | Where to obtain |
|---|---|---|
| Promoter pledge trend and FII/DII split | Promoter verdict, UA q3 recheck | BSE scrip 532240 quarterly shareholding pattern filings |
| Debtor split of the Rs 42.90 Cr overdue bucket | Cash determination | Management disclosure; operator ferried extraction prompt; not in AR2026 |
| INEL's ownership percentage of Lucas TVS; Lucas TVS EBITDA and net debt | Promoter verdict, SOTP | MCA filings of Lucas TVS Limited |
| Audited basis FY26 margin and ROCE definition | Phase 3 margin bridge, ladder rung | Verifier A read of Reg 33 filing p.4, AR2026 Notes 29, 35, 51 |
| EV content per vehicle for INEL's EV stack | Market sizing, forward basis | Live web (web search failed all session) |
| Product revenue split (ignition against electronics) | Proof gate, margin bridge | Not disclosed; management question |
| Capex project, capacity and commissioning dates | Cash determination | Not disclosed; management question, next AR |
| SEBI, MCA, court searches for promoter entities | Promoter verdict (partial) | Live web rerun of stage 8 |

## Publish check

No publish candidate this analysis.
