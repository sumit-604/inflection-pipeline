=== FILE: gate-recommendation.md ===

PROCEED WITH CAVEATS

# CAPILLARY gate recommendation (phase 1, evidence only)

This is the FTTCP go or no go call on the evidence. It is not the investment decision. No BUY, WATCHLIST or AVOID call is made here. No entry range, margin of safety price, destination PE or Hurdle verdict is set. Those form in phase 3.

Operator choice pending: Verifier B reports red flag coverage on two bases. The rubric basis (70) gives the verdict above. The strict basis (40) sits below the 60% line and would force REWORK under rule 1. This file does not pick between them. See "Verdict rule trace".

## Verdict rule trace

- Rule 1 (REWORK): not triggered on the rubric basis. Verifier A found 0 CRITICAL findings and 0 source fidelity findings (41 of 41 figures clean). Acceptance rates: A 100, B 70, C 86.7, D 92. Overall confidence is 70, above 60.
- Rule 1, strict basis: Verifier B's strict count (only partial catches the pipeline flagged as a concern) is 4 of 10 material items, 40%. That is below 60% and would force REWORK. REWORK would judge the analysis, not the company. The failing stage would be stage 5 (concall), with scoped fixes to stage 6 (peers). A rerun must fix: the organic growth row (23% includes about 6% currency, so about 17% organic), the healthcare customer contradiction, the aiRA sizing regression, the SessionM USD 35 m to USD 32 m restatement, the SessionM price adjustment framed as a positive, the Kognitiv churn indemnity read as acquired book churn, the gross margin contradiction, the new order value base exclusion, and the unsupported "build it yourself risk not named" claim in stage 6. Three of the six partial catches (organic growth, SessionM price, Kognitiv indemnity) were recorded neutrally or as positives. The operator decides which basis governs.
- Rule 2 (INSUFFICIENT EVIDENCE): not triggered. The FY26 annual report, three results filings, three concalls, the draft prospectus, four investor decks and 38 exchange filings are present. Gate 0 ran on screening data and audited results. The gaps named below are partial and leave the decision record intact. Freshness verdict is FRESHNESS PAIRS OK, so no freshness cap applies.
- Rule 3 (PROCEED WITH FLAGS): FLAG-CASH is active. Its determination is INDETERMINATE, which caps the verdict at PROCEED WITH CAVEATS. FLAG-PROMOTER is not triggered: the promoter verdict is CAUTION, not CONCERN or AVOID.
- Rule 4: overall confidence 70 sits in the 60 to 74 band, which downgrades a PROCEED family verdict one level. The verifiers also logged 16 MAJOR findings worth carrying. A clean PROCEED would fall to PROCEED WITH CAVEATS on either ground.

The INDETERMINATE cash cap and the 60 to 74 band converge on PROCEED WITH CAVEATS. Verdict rule applied: 3 (cash cap), reinforced by rule 4.

## Transition posture (provisional, phase 1)

The Mental Model is not signed. The three state variables below are the run's evidence read, not the signed values.

- PROOF GATE: NOT FIRED. The margin climb rests on organic EBITDA margin near 23% in Q1 FY27 (management figure). FY26 operating EBITDA margin was 12.64% and ROCE never cleared 10%. The organic growth rate under the FY27 guide is unresolved (17% claimed, about 11% analyst reading, 3 to 6% from plan arithmetic).
- UGLINESS: ARTIFACT-OF-CLIMB on current evidence. Low ROCE tracks four historical loss years, a doubled post IPO equity base and acquisition goodwill, not falling unit economics. Subscription gross margin rose from 66.4% to 67.2% in FY26 (AR p.99). The STRUCTURAL reading would need the acquired books to bleed. Inorganic net retention of 94% and the Kognitiv churn indemnity are the first signs to watch on that side.
- RECOGNITION GAP: UNRESOLVED. Stage 11 sets it in phase 3.

Posture on current evidence: RESEARCH / WATCH until the proof gate fires. If phase 3 finds the target state already priced, the posture moves to PRICED NARRATIVE (TRAP), where the climb can fail and the multiple can compress together.

## Confidence delta (phase 1)

| Component | Score | Source | Note |
|---|---|---|---|
| numerical_acceptance | 100 | B12a | 41 of 41 checked clean; material universe 47; 0 CRITICAL, 0 source fidelity findings |
| redflag_coverage | 70 (rubric) / 40 (strict) | B12b | 7 of 10 material flags counting 6 partials as caught; strict basis counts 3 of the 6 partials, 4 of 10. 3 MAJOR missed |
| framework_adherence | 86.7 | B12c | phase 1 portion only: Gate 0 44 rules + Emerging Moat 31 rules, 65 pass; valuation half pending phase 3 |
| peer_utilisation | 100 | B12d | 12 of 12 peer transcripts used substantively; Verifier D acceptance 92 (one MAJOR paraphrase finding on NEWGEN) |
| overall | 70 | min of four, set by redflag_coverage | band 60 to 74: PROCEED verdicts downgrade one level |

Weakest component: red flag coverage. The concall stage missed three MAJOR items and misread six more. The misses all point the same way: management figures that moved between calls without comment.

## Active flags

### FLAG-CASH (active)

```
⚠️ CASH CONVERSION FLAG: Working capital days worsened from 24.0 (FY23) to 52.8 (FY26) while FY26 operating cash flow improved.
Determination: INDETERMINATE.
Evidence:
- Multi year trend: WC days 24.0 (FY23) to 52.8 (FY26), driven by payable days falling 66.6 to 37.0 over FY23 to FY26 (B01 Block B4; B12c F-G2).
- Mechanism corrected by Verifier C (F-G2, MAJOR). Stage 1 wrote that FY26 CFO "leans on payable-days compression (66.6 to 37.0 days) rather than receivable discipline". Verifier C: 66.6 to 37.0 is the FY23 to FY26 move, and a payable days fall consumes cash. In FY26 receivable days fell 98.3 to 89.8 and payable days rose 30.9 to 37.0, and both helped FY26 CFO. The multi year deterioration stands. The corrected reading governs; the stage reading is retained here for the record.
- CFO Rs -46.20 Cr (FY25) to Rs +149.91 Cr (FY26) (AR Consolidated Cash Flow p.193; B12a MATCH). The Rs 24.96 Cr Kognitiv churn indemnity is stripped from CFO and its receipt sits in investing activities (B03 LBF4).
- FY26 working capital release Rs 43.71 Cr: trade payables +Rs 24.72 Cr and other liabilities +Rs 22.80 Cr, "most likely deferred/unearned revenue growth" (B03 LBF4). The deferred revenue reading is not confirmed from the note.
- Receivables composition: consolidated trade receivables +12.2% against revenue +22.8%; credit impaired receivables down 65.3%, Rs 12.83 Cr to Rs 4.45 Cr; unbilled revenue Rs 27.45 Cr to Rs 26.24 Cr (B02, Note 8 p.222-223). Standalone unbilled +126.5% is intercompany and nets out on consolidation (B02 finding 10).
- OCF to adjusted EBITDA about 140% in FY26 (Rs 150 Cr / Rs 107 Cr). Management reason: "we bill and collect money upfront in a healthy growing business" (Q4 FY26 call, Anant, [p10] L409-412). Verifier B rates the stage 5 "missed / never reconciled" reading OVERSTATED (B12b).
- Capitalised internally generated software Rs 36.62 Cr, about 34% of consolidated EBITDA, 3 year amortisation, a Key Audit Matter (B02 finding 9; AR Note 4 p.219, KAM p.178-179). FY26 capex Rs 39.37 Cr; FCF Rs 110.54 Cr (B12a MATCH, AR p.193).
- SessionM: USD 20 m headline price trued up to about Rs 17 Cr net, with an adjustment of about USD 18 m unexplained on the call; management says the entities are debt free (Q1 FY27 call [p22] L907-921). Verifier B infers assumed customer prepayments or deferred revenue as a likely candidate [INFERENCE] (B12b item 5).
- Rating agency quote: none exists. The FY26 AR states the company "has neither obtained nor revised any credit rating" (B00 input_gaps).
If INDETERMINATE: verdict caps at PROCEED WITH CAVEATS.
Missing evidence:
1. The FY26 AR note behind "other liabilities" (+Rs 22.80 Cr), split into contract liabilities (deferred revenue) and other items, FY25 against FY26. Held in the corpus; a Claude Code extraction request closes it.
2. The trade receivables ageing schedule, AR FY26 Note 8.
3. The cause of the payable days fall, 66.6 (FY23) to 37.0 (FY26): payables composition from UDRHP-I p.394 and AR Note 18 p.230.
4. The SessionM purchase price allocation, including any assumed deferred revenue: Q2 FY27 results notes (BSE, due around Nov 2026).
Two readings: (A) GROWTH-INDUCED. Payables normalised from loss year levels once IPO cash arrived, and the FY26 liability build is upfront billing. (B) The FY26 CFO leans on a liability build that slows with bookings, and acquired prepayments flatter acquisition quarters.
Separating observation: the contract liabilities line FY25 against FY26, then the H1 FY27 balance sheet.
Falsifier to attach if the operator resolves it GROWTH-INDUCED: receivable days above 98 (the FY25 level) or WC days above 52.8 in the H1 FY27 balance sheet (Q2 FY27 results, BSE).
```

Guard: INDETERMINATE cash never resolves silently to PROCEED. It caps this verdict at PROCEED WITH CAVEATS.

### FLAG-GATE0 (active, informational)

```
Gate 0 score: 66/160 per Verifier C recompute (stage 68/160); Core 51/100; moat 15/60, 3 moats, MODERATE (stage: 17/60, 4 moats, STRONG); classification AVERAGE under both readings (B01; B12c F-G1).
Depressors are historical: PAT negative FY21 to FY24 (FY24 Rs -56.99 Cr); median ROCE -1.83% on FY23 to FY26; cumulative CFO/PAT distorted by the loss years (cumulative PAT Rs -202.71 Cr against cumulative CFO Rs +189.14 Cr) (B01 deal_breakers).
Open operator ruling (B12c O4): keying the data confidence band to the four balance sheet years instead of six P&L years would trigger the LIMITED downgrade, AVERAGE to AVOID. Stage 1 keyed to six years, the literal reading.
Recurring reading of D2 (B12c O1): strip the Rs 24.96 Cr one time gain from EBIT and interest cover falls 10.36x to 5.79x, core 51 to 50; AVERAGE unchanged.
```

FLAG-GATE0 caps nothing. Position sizing in Role 2 handles it.

### Promoter treatment

FLAG-PROMOTER verdict line block: not triggered. The promoter verdict is CAUTION (5 clean, 5 caution, 0 red), with no deal breaker. The legal and regulatory record of both promoters is clean, and pledge is 0% across all three filed quarters.

CAUTION items, surfaced as caveats:
- The promoter holding company, CTIPL, sold 4.14% (3,292,428 shares) on 10 Aug 2026, 48.92% to 44.78%, to fund Peak XV's exit. The company discloses that other PE investors hold over 30% of CTIPL and may exit the same way (company clarification 25 Aug 2026).
- Institutions voted 55.9% against the Feb 2026 postal ballot extending ESOP 2021 to subsidiary staff. It passed on promoter and retail votes (voting results filed 13 Mar 2026).
- The Head of Finance resigned on 29 May 2026 and the Head of Corporate Development on 27 Jul 2026. Both fall inside the window around the fraud disclosure and the forensic audit. No source establishes a causal link.
- The chairperson holds 12 audit and stakeholder committee positions in other companies, at or above the LODR Reg 26(1) ceiling depending on the count method. It is not verified against the regulator registry.
- A promoter group company, Gowthami Agro Industries, received an information notice from an Andhra Pradesh SIT on the 2019 liquor policy. No chargesheet link was found.

Transition evidence: Kotak Mahindra Mutual Fund crossed 5% on 14 Aug 2026. The Audit Committee started the KPMG forensic audit within 25 days of the fraud, without a regulator mandate. The company issued specific clarifications on the ESOP pricing and the CTIPL sale. Peeyush Ranjan joined as independent director on 7 May 2025.

### Other flags carried from the stages

- FLAG-DISCLOSURE-GAP: the contingent liabilities note promises a claims description and gives none; the >10% customer sentence in Note 36(iii) is incomplete; no capital commitments note; hedging policy stated with no forward notional (AR Notes 31/34, 36(iii), 34(2)).
- FLAG-RPT: 75.7% of standalone revenue comes from the Singapore subsidiary; the FY26 transfer pricing study was still open at sign off (AR Notes 20/32, p.155-168).
- FLAG-GOVERNANCE-COMMITTEE: the chairperson committee count above.
- Emerging moat flags: FY26 concentration undisclosed under the strongest customer row; the acquisition rollup row fails the sacrifice test; the execution row capped by the cash conversion question.

## Verifier corrections carried

- Gate 0: 66/160, moat class MODERATE (Verifier C). The stage scored 68/160, STRONG. Classification AVERAGE under both.
- Emerging moat score: 21.9 before rescoring (Verifier C). The stage scored 24.0. Band MODEST under both. The customer ecosystem row falls 4.0 to 2.8, since the documented Fortune 50 deal is a new customer win (Q4 FY26 call L195-198, L755). The execution row falls 3.0 to 2.1, since it double credited the acquisition margins. The sacrifice test still has to run on each claimed moat, aiRA's usage pricing first.
- R&D spend: disclosed at Rs 121.2 Cr including ESOP (AR FY26 p.41, Directors' Report, technology absorption item iv). Stages 1 and 7 said no R&D disclosure existed. The M6 Gate 0 score stays 0. The A4 and F1 emerging moat rows need a rescore on the disclosed figure. Crossing 25 would need F1 at the top grade on documented evidence, which a spend line cannot carry.
- FLAG-CASH mechanism: see the flag block. Verifier C's reading governs.
- Concall record (Verifier B): three MAJOR items missed (healthcare customer contradiction, SessionM USD 35 m to USD 32 m, gross margin 69 to 70% against above 75%). Direction errors in the concall stage: the Q1 FY27 margin softness row is "delivered, better than guided" but margin fell from about 19% to 17% as guided; the OCF/EBITDA row scored a norm as a missed promise; SessionM "ahead of schedule" rests on two months of cash, not EBITDA. Promise delivery spot checks: 5 checked, 3 confirmed, 2 wrong. Verifier B grades credibility B minus to C plus against the stage's B.
- Peer record: the claim that Capillary never named the build it yourself AI risk is NOT SUPPORTED. Analysts raised it and management answered on the Q1 FY27 call ([p17-18] L694-717; [p21] L888-906). Verifier D found one NEWGEN paraphrase that reverses who wins; the Q6 verdict holds.

## Load bearing facts: what the run found

- LBF1, guidance decomposition. FY27 guide Rs 1,000 to 1,050 Cr (Q4 FY26 call), later "will definitely beat" Rs 1,065 Cr revenue and Rs 172 Cr EBITDA (Q1 FY27 call). Plan split: organic about Rs 673 Cr, acquired about Rs 390 Cr (Q1 FY27 [p11] L464-469). Organic growth is UNRESOLVED: 17% claimed, which may already include about 6% currency; about 11% on an analyst's Q1 arithmetic; 3 to 6% from the plan split [INFERENCE]. SessionM consideration USD 20.00 m, signed 24 Feb 2026, completed 1 May 2026 (AR Note 44 p.259). Net price about Rs 17 Cr after a true up the call did not explain. The acquired base moved from USD 35 m (Q4 call) to USD 32 m ARR (Q1 call). The "profitable within two months" claim rests on Rs 5 to 6 Cr of cash in two months, not EBITDA. The purchase price allocation and goodwill are NOT FOUND in the corpus; the Q2 FY27 notes should carry them. Template: Kognitiv goodwill was 62% of consideration (AR Note 39 p.254).
- LBF2, governance and earnings quality. (a) EUR 3.0 m cyber banking fraud at a Czech subsidiary (Reg 30, 6 Jul 2026), KPMG forensic audit (31 Jul 2026), Rs 33.39 Cr exceptional loss in Q1 FY27 (Q1 FY27 results). Insurance recovery has no amount or date ("we don't have clarity", Q1 call). The auditor's FY26 IFC report already named an audit trail and backup location exception (AR Annexure II p.184-185). (b) Company memory's "FY26 other income Rs 39 Cr" is corrected: the P&L other income line is Rs 13.73 Cr, and screener's Rs 38.69 Cr adds the separately reported Rs 24.96 Cr Kognitiv churn indemnity (AR p.190, Note 28 p.235). Q1 FY27 screener other income of Rs -27.68 Cr is consistent with the fraud exceptional. (c) CTIPL sale confirmed at 4.14% on 10 Aug 2026, 48.92% to 44.78%; PE holders keep over 30% of CTIPL.
- LBF3, concentration and retention. FY26 top 10 share is NOT FOUND; Note 36(iii) is incomplete. FY26 net retention: 110% blended, 114% organic, 94% inorganic (AR MD&A p.80). USA 55.6% of FY26 revenue (AR Note 22). Q1 FY27 net retention 111%, or 116% excluding one large healthcare customer that did not grow. Q3 FY26 had described a large healthcare payer adding 50% more members. Whether these are the same account is unresolved.
- LBF4, cash conversion. CFO Rs -46 Cr to Rs 150 Cr confirmed (AR p.193). Debtor days 98.3 (FY25) and 89.8 (FY26). Capitalised development Rs 36.62 Cr. Goodwill Rs 309.58 Cr and other intangibles Rs 138.56 Cr at FY26 end (AR p.85). The run did not reproduce company memory's "fixed assets Rs 301 Cr to Rs 460 Cr" as stated. The deferred revenue share of the FY26 liability build is not confirmed. IPO cash: Rs 323.24 Cr of fixed deposits sit outside the company's own "Total Fund" definition (AR Note 38 p.253).

## Contradicted claims (priority monitoring)

The peer stage recorded no contradicted claims. Priority items in their place:
- Unverifiable in all 12 peer transcripts: loyalty software is under 10% of loyalty spend; 110% plus net retention is top decile.
- Soft peer contradiction on demand: Capillary says it is "not seeing" the new business slowdown (Q3 FY26 [p12] L518-520), while NEWGEN reports "elongated decision cycles" and deferred large deals (NEWGEN Jan 2026 call L136-138, L222-223). The segments differ.
- Management figures contradicted across Capillary's own calls: aiRA sizing, SessionM base, platform gross margin, organic growth (see Verifier corrections).

## Monitorables and triggers

1. Organic revenue growth at constant currency for H1 FY27, in the Q2 FY27 results and call (about Nov 2026). Sustained growth below 15% is the red flag line. Near 11% confirms the analyst reading over management's 17%. This tests whether the organic engine or the acquisitions carry the FY27 guide.
2. Organic net retention, reported and excluding the healthcare account, in the quarterly deck. At or above 114% for two more quarters confirms. Below 105% kills the expansion trigger. Ask management to name whether the flat Q1 account is the payer described in Q3. Also watch for any FY27 top 10 disclosure or a Reg 30 non renewal.
3. SessionM and Kognitiv delivery. The Q2 FY27 notes should show the SessionM purchase price allocation and name the roughly USD 18 m adjustment. SessionM margin stalling below 15% by Q4 FY27 kills the margin ramp. Kognitiv's first customer was due live on 1 Sep 2026, with full migration by Sep 2027; a slip past that tests the acquisition playbook.
4. Operating EBITDA margin with exceptional items stripped and tax normalised, from the quarterly results. It must rise from 12.64% (FY26) toward management's 25 to 30% steady state. ROCE above 10% for two straight periods clears the Gate 0 deal breaker. This tests the margin climb itself.
5. Cash conversion in the H1 FY27 balance sheet: receivable days against 89.8, WC days against 52.8, and the contract liabilities line. Receivable days above 98 or WC days above 52.8 would argue against the benign cash reading.
6. The KPMG forensic report, the insurance recovery against the Rs 33.4 Cr loss, and closure of the auditor's audit trail exception. These come by Reg 30 filing, expected in H2 FY27. Adverse findings or new control lapses test the governance side of the thesis.
7. Further sales by CTIPL or its PE holders, from SAST Reg 29 filings and the quarterly shareholding pattern. A second block sale without warning tests the float overhang the company has already disclosed.
8. aiRA revenue in rupees, on a consistent basis each quarter, against the 5 to 10% of FY27 revenue target. Paying customers still under 10 of 150 plus through FY27 kills the aiRA option.

## Falsification line

H1 FY27 organic revenue growth at constant currency below 15%, printed with the Q2 FY27 results. That print would confirm the acquisitions, not the platform, carry the FY27 guide.

## Corpus verdict

CORPUS GAPPED, freshness pairs OK. Gaps and where to get them:
- Final RHP / Prospectus (Nov 2025): capillarytech.com returned HTTP 403 to scripted download. The operator can push it by hand. UDRHP-I (Jun 2025) is held.
- FII / DII split: the BSE Reg 31 summary lacks it. Get the full shareholding pattern from BSE or NSE.
- FY26 top 10 customer share: not disclosed by the company. Ask management; watch the FY27 AR.
- SessionM purchase price allocation: Q2 FY27 results notes (BSE).
- Credit rating: none exists (AR FY26). Not a collection gap.
- Screener P&L, balance sheet, cash flow and quarters sheets exported empty; Data_Sheet and the filings were used instead.

## Publish check

No publish candidate this analysis.
