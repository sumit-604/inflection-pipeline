MISSING MATE DOCUMENT (freshness pair 1, results to concall): KPL Q2 FY27 concall transcript, call held 13 Nov 2026. Expected source: BSE/NSE filing or the screener Concalls row. Not published as of 2026-11-16; BSE and screener carry the deck and audio only. Re-collect after about 20 Nov 2026.

**Verdict: PROCEED WITH CAVEATS**

Phase 1 lite. This is the FTTCP gate decision on evidence alone. No valuation has run. The investment decision forms in phase 3.

## Why this verdict

The selection rules run in order.

1. REWORK does not fire. Verifier A found no CRITICAL and no source fidelity finding. The lowest acceptance rate is 63% on 19 items, above the 60% floor. Overall confidence is 63, above 60.
2. INSUFFICIENT EVIDENCE does not fire. The annual report, three results filings, the H1 FY27 cash flow, the full ICRA rationale and two concalls are all in the corpus. The open gaps are items the company has never filed: receivables ageing by customer and country, and the split of revenue between its own and partner registrations. A missing filing would cap the gate. A missing disclosure is a question for management and a caveat here.
3. FLAG-CASH is active. Its determination is INDETERMINATE, so the verdict caps at PROCEED WITH CAVEATS instead of PROCEED WITH FLAGS.
4. The freshness cap applies on its own. The corpus is CORPUS GAPPED-FRESHNESS, so the verdict can be no better than PROCEED WITH CAVEATS whatever the flag count.
5. Confidence sits in the 60 to 74 band, set by redflag coverage. The band downgrades a PROCEED one level. The verdict already sits at PROCEED WITH CAVEATS under two hard caps, so the band changes nothing. The band does not push the verdict into INSUFFICIENT EVIDENCE, which needs its own grounds.

Three separate rules land on the same verdict. Removing any one of them leaves it in place.

Transition posture: NOT CLASSIFIED. The Mental Model is unsigned. The proof gate read belongs to FTTCP and the recognition gap to stage 11, and neither has run.

## Flag blocks

```
⚠️ CASH CONVERSION FLAG: CFO/PAT fell from 1.32 in FY25 to 0.25 in FY26, then rose to 0.50 in H1 FY27.
Receivables rose in rupees in both periods. The annual ratio is deteriorating; the half year ratio is
improving; the rupee balance is still rising.
Determination: INDETERMINATE.
Evidence:
- Rating agency, verbatim (ICRA rationale dated 7 May 2026, PDF page 2, text layer as extracted):
  "The rating s, however, are constrained by KPL's high working capital intensity of operations , with
  an NWC/OI 2 of 50.2% in FY2025. The elevated working capital intensity is partly on account of
  increased debtors due to the company's growth phase in several semi-regulated markets and a higher
  inventory holding on account of a greater number of stock-keeping units (SKUs)."
  (inputs/rating/ICRA_rationale_2026-05-07_via_BSE_20260508.pdf, p.2; the "2" is footnote 2, NWC/OI)
- Rating agency, verbatim (same document, PDF page 3):
  "Being in a growth phase in several semi -regulated markets, KPL offers a relatively longer payment
  period to its customers, resulting in a high debtor cycle. Moreover, it also needs to maintain a n
  increased inventory owing to a greater number of SKUs relative to its scale. This has resulted in a
  sustained elevated working capital intensity over the last few years with an NWC/OI of 53% in FY2024
  and FY2025." (ICRA p.3; B04 Section 2A)
  The rationale gives FY2025 NWC/OI as 50.2% on p.2 and 53% on p.3. It rests on FY2025 and 9M FY2026
  data, so it predates the FY26 year end receivables rise (ICRA p.2-3).
- Cash flow: FY26 CFO 1,658.62 vs PAT 6,734.60 INR lakh = 24.6%; CFO/EBITDA 14.0%; FCF -3,235.42 lakh
  after capex 4,894.04 lakh (AR FY26 CFS p.190-191; B02 top_findings 1; B03 flags). FY25 like for like
  CFO/PAT 85.3% after removing 1,876.75 lakh of short term borrowing booked in FY25 CFO (derived; B02).
  Screener basis FY26 CFO Rs 17.06 Cr vs PAT Rs 67.35 Cr (screener Data Sheet; B01 block_b_trend).
  H1 FY27 CFO 2,756.79 lakh = 50.4% of PAT 5,464.85 lakh (Q2 FY27 results p.14-15, p.18; B05 FLAG-CASH).
- Receivables composition: 28,005.24 INR lakh at 31 Mar 2026, +81.5% vs revenue +35.9%; 203.2 days on
  year end revenue (derived); 69.0% of current assets; over 6 months 3,030.29 lakh; over 2 years
  564.29 lakh; nil ECL or doubtful provision; at least 1,166.32 lakh of FY25 balances overdue by more
  than a year left the ledger with no disclosed route (AR Note 9 p.211-212; Note 39 p.236; B02 ranks
  2-4). Unhedged FX receivables 15,599.05 lakh = 55.7% of receivables (AR Note 37 p.229; B02 rank 5).
  33,503.65 lakh at 30 Sep 2026, up 5,498.41 lakh in H1 (Q2 FY27 results p.14, p.18; B01 data_notes).
  Middle East debtors Rs 60-70 Cr claimed on the 19 May 2026 call; no filing gives the amount (B05
  promise_delivery row "Middle East debtors"). Customer and country ageing NOT FOUND (B03 input_gaps).
- Supplier funding: payables 5,579.34 to 10,168.66 INR lakh (+82.3%); CFO would be -2,930.69 lakh
  without the payables rise (AR Note 20 p.219-220; B02 rank 7).
- Capex commissioning timeline: FY26 capex cash 4,894.04 lakh, 2.0x FY25 (B02 rank 11). H1 FY27 capex
  3,850.49 lakh vs CFO 2,756.79 lakh; net borrowing +1,578.18 lakh (Q2 FY27 results p.18; B05 FLAG-CASH).
  Gross borrowings Rs 130 Cr to Rs 146 Cr (B07 FLAG-CAPEX-FUNDING). Unit 6 hormones: construction 100%
  per deck; CWIP Rs 17 Cr at Mar 2026 and Rs 33 Cr at Sep 2026; manufacturing licence expected Nov 2026;
  WHO-GMP Jun-Jul 2027 (Q2 deck p.15; Aug call p.8; B07 FLAG-CWIP-HORMONE; B05 trigger 7). Oncology
  expansion due June 2027 (Q2 deck p.5; B05 timeline_slippages).
- Peer benchmark: KPL 178 debtor days vs Caplin 117-136, Senores NWC 90-104, Lincoln 89-101 (stale)
  (CAPLIPOINT Q4 FY26 p.9, p.13-14; SENORES Q3 FY26 p.16; LINCOLN Q4 FY24 p.17; B06 contradicted).
- Ten year record: cumulative FCF proxy Rs -2.52 Cr; receivables Rs 22.61 Cr (FY17) to Rs 280.05 Cr
  (FY26) (screener Data Sheet; B01 analyst_note).
Two readings:
- GROWTH-INDUCED: credit extended to win new semi regulated markets (ICRA p.2-3); H1 CFO/PAT doubled
  to 50.4%; inventory fell Rs 78 Cr to Rs 74 Cr (Q2 deck p.8; B07 G2).
- STRUCTURAL: receivables outran revenue 2.3 to 1 in FY26; ICRA calls the intensity "sustained" over
  "the last few years"; six negative FCF proxy years of ten (B01 deal_breakers); peers collect in
  90-136 days; H1 receivables still rose Rs 55 Cr.
Separating observation: receivables ageing by customer and country, with the Middle East amount.
INDETERMINATE: verdict caps at PROCEED WITH CAVEATS. Missing evidence and where to get it:
  (1) receivables ageing by customer and country: management answer; AR FY27 Note 9;
  (2) Middle East debtor amount, age and provision: Q2 FY27 transcript once posted; management;
  (3) ECL policy and expected loss rate: first B S R & Co. LLP audit, AR FY27;
  (4) the FY27 cash flow statement: FY27 audited results on BSE, about May 2027.
Resolving metric: FY27 CFO/PAT and receivables at 31 Mar 2027 (FY27 audited results). At or above 60%
with receivables below Rs 335 Cr reads GROWTH-INDUCED. Below 35% with receivables above Rs 350 Cr reads
STRUCTURAL (B03 monitorables; B05 trigger 4; B07 optionality_register).
```

```
FLAG-GATE0: Gate 0 GOOD by deal-breaker override. Grand total 80/160; core 61/100; moat 19/60 (B01).
Blocks: A 13, B 4, C 17, D 15, E 12. Moats confirmed 3 of 12, MODERATE (B01).
Deal-breaker #2: Block B 4 < 8 caps the class at GOOD. Years driving it: FY26 CFO Rs 17.06 Cr vs PAT
Rs 67.35 Cr; FCF proxy negative in FY17, FY18, FY20, FY22, FY23, FY26; receivable days 84 to 203 from
FY17 to FY26 (screener Data Sheet; B01 deal_breakers).
Historical depressor? NO. The weak cash years run from FY17 to FY26 and include the latest year. The
record shows no post IPO rebase, legacy cleanup or restructuring behind them (B01 analyst_note).
Knife edge: core 61 sits one point above the 60 line. Three routes reach AVERAGE:
- strict ROCE reading (no TA - CL data for 3+ years): Block A 4, core 52 (B12c C-G03, MAJOR);
- GST items outside the E4 total: E4 1, core 59 (B12c C-G53);
- B1 headroom of Rs 2.02 Cr of CFO: core 59 (B12c F-2, F-4).
Upside gap: promoter holding three years ago NOT FOUND, so E2 scored 0; resolving it within 1pp would
add 3 to Block E (B01 input_gaps).
This flag caps nothing. Role 2 sizing handles the override.
```

FLAG-PROMOTER: not active. The promoter verdict is CAUTION, and the flag fires only on CONCERN or AVOID. The promoter stage is partial and recorded two deal breakers. Both sit under Open items below.

## Confidence delta (phase 1)

| Component | Value | Basis |
|---|---|---|
| numerical_acceptance | 99 | B12a: 390 checked; 55 of 55 mandatory; 0 CRITICAL, 0 MAJOR, 3 MINOR; no source fidelity finding |
| redflag_coverage | 63 | B12b: 12 of 19 MATERIAL items fully caught, 6 partly caught, 1 missed |
| framework_adherence | 86 | B12c phase 1 scope (Gate 0 + Emerging Moat): 69 of 80 rules passed; valuation half pending phase 3 |
| peer_utilisation | 90 | B12d: 9 of 10 peer transcripts used substantively; 1 cited only (stale) |
| overall | 63 | min of applicable components; set by redflag_coverage; band 60-74 |

Weakest component: redflag coverage. The concall and peer stages fully caught 12 of 19 material items. They missed one MAJOR: management's FY29 Rs 1,000 Cr target includes hormones and biologics, with a downside of Rs 800 to 850 Cr without them.

## Contradicted claims

From the peer stage:

1. Management framed 150 to 180 receivable days as normal and blamed the Gulf disruption. Peers contradict both. Caplin ran 136 days at Mar 2026, 125 days excluding FX, and its management said "100 to 130 days even is probably still okay" (CAPLIPOINT Q4 FY26 p.9, p.13-14). Senores ran 90 to 94 net working capital days (SENORES Q3 FY26 p.16). No peer says a 2026 Gulf disruption lengthened its own receivables. This item tests the cash determination.

The red flag verifier found two more that the peer stage left out or understated:

2. "Very less competition" in LATAM, against Caplin and Senores both entering Mexico (KPL Aug 2026 call p.5; CAPLIPOINT Nov 2025 p.5, p.10; CAPLIPOINT May 2026 p.6; CAPLIPOINT Aug 2026 p.3; SENORES Jul 2026 call p.12).
3. The Q4 FY26 gross margin dip blamed on the war, against the same call's "not much increase... API prices" and a Caplin COGS rise under 2% (KPL May 2026 call p.15, p.17-18; KPL Aug 2026 call p.11; CAPLIPOINT May 2026 p.16).

Contradictions inside the company's own filed record, carried as priority monitoring:

4. Domestic turnover was 50.3% of FY26 revenue, against management's "India about 5%" (AR FY26 p.154; May 2026 call p.20).
5. The Q2 deck names KPMG as auditor. The 12 Nov 2026 filing appoints B S R & Co. LLP (Q2 deck p.11; Q2 FY27 results p.19-23).
6. The filed Q2 commentary states PAT of Rs 50 Cr vs Rs 25 Cr. Those are EBITDA values. Filed consolidated PAT is 2,902.62 INR lakh vs 1,411.57 lakh (Q2 FY27 results p.3 vs p.16).
7. The board report says no conflicted related party deal took place. Note 40 shows two director interested counterparties, with a Kaler return of 262.75 INR lakh above a sale of 121.48 lakh (Board report p.41-42; AR Note 40 p.238-239).
8. The MD&A claims a natural FX hedge. USD payables cover 1.1% of USD receivables (AR p.94; AR Note 37 p.229, derived).

## Monitorables and triggers

1. Read the FY27 audited cash flow statement on BSE, about May 2027. FY27 CFO/PAT at or above 60%, with receivables below Rs 335 Cr, supports the growth reading. Below 35%, with receivables above Rs 350 Cr, supports the structural reading. This settles the cash flag.
2. Read Note 9 in the FY27 annual report. Look for the first expected credit loss provision and for an over one year bucket above 1,566.38 INR lakh, which is adverse. This tests whether reported profit is cash profit.
3. Track the auditor change on BSE. Members must approve B S R & Co. LLP by about 12 Feb 2027. Any qualification, emphasis of matter, or provisioning change in its first audit that cuts FY27 PAT tests governance and earnings quality together.
4. Read the Q3 FY27 results in Feb 2027. Revenue at or above Rs 176 Cr and effective tax at or below 25% keep the Rs 720 Cr revenue and Rs 122 Cr PAT guides alive. Revenue below Q2's Rs 181 Cr without an explanation, or tax above 28%, breaks them.
5. Watch gross margin in the Q3 and Q4 FY27 results. Holding at or above 52% (Q2 52.1%) supports the margin climb. A fall back under 48% says the Q2 jump was a one quarter event.
6. Ask management for revenue and EBITDA by registration holder, and for a top five customer and country table. Watch the next concall and the FY27 annual report. Any single name above 20% is a red flag. This is the one disclosure that tests the margin engine.
7. Pull MCA records for Kaler Biopharmachem and Iair Infocom, and read the half year related party filing. Any repeat sale return, or a promoter link to the owners, tests the related party risk.
8. Track the dated pipeline steps through Reg 30 filings and CDSCO and CTRI records. The Unit 6 licence is due Nov 2026, with a kill past Q4 FY27. The EPO trial should start by Nov-Dec 2026, with a kill if there is no start by Mar 2027. The oncology expansion is due June 2027. These test the execution record that has slipped on every dated milestone so far.

Falsification line: the Q3 FY27 results (Feb 2027) show revenue below Q2's Rs 181 Cr with no explanation. The FY27 guide needs Q4 above Rs 200 Cr, and the credibility grade rests on beaten sales guides.

## Open items the operator must see

Stages partial or blocked:

- Promoter stage: PARTIAL. MCA master data for Kaler Biopharmachem and Iair Infocom is PENDING LIVE VERIFICATION. Kaler's directors (the MD, DIN 00462656, and Deepak Bansal, a 9.24% public holder) rest on aggregator data only. Not searched or not found: eCourts, High Court and NCLT records; the SEBI enforcement database; proxy advisor reports; SCORES counts; CRISIL's current rating status and the reason for non cooperation; the status of independent director Prashanth Vellanki; the three year promoter pledge trend. Source: MCA21, court portals, SEBI, CRISIL, BSE shareholding history. Claude web closes these in live verification.
- Promoter stage deal breakers, recorded under a CAUTION verdict: (1) statutory auditor resignation within three years, Vijay Mehra & Co., 12 Nov 2026, reason "Due to Pre-occupation in other assignments" (BSE Reg 30 outcome, ANN 20261112-4a20fb35 p.1-2, 19-23); (2) two independent directors exited before their terms ended within three years, Kiran Kumar Verma on 26 Jul 2025 and Kartik Kapur on 2 Jun 2026 (AR p.64; ANN 20260602-5daf24b4 p.1, 4-5).
- No stage is blocked. Every other phase 1 stage is complete.

Verifier C forward flags:

- F-1 (stage 11, Pillar 3): the emerging moat score already credits R1, A4, E1 and H2 for items that also sit in the 12 month catalysts (Unit 6 licence, EPO, Pembrolizumab, BE dossiers, EU approvals). No second credit as catalyst proximity.
- F-2 (Halt 1): Gate 0 core is 61 against a line of 60. Three downside routes reach AVERAGE: the strict ROCE reading (52), E4 composition (59), and B1 headroom of Rs 2.02 Cr of CFO (59).
- F-3 (operator ruling candidate): prompts/07 Section 5 has no rule for mixed tier multipliers. On this name it decides NONE (10.3; recompute 11.6 to 11.9) against MODEST (12.4 to 13.4).
- F-4 (Verifier A pointers): B1 headroom Rs 2.02 Cr; C1 0.11pp under 20%; D1 0.07x over 1.0x; Note 34 sum 36.56 vs 36.98; fixed asset turnover 3.23x (Gate 0, net block 155.57) vs 3.35x (emerging moat, 150).

Other open items:

- The concall stage grades credibility B. The red flag verifier reads C and corrects the promise tally to 9 delivered, 6 partial, 5 missed and 2 open. The operator rules on the grade at Halt 1.
- Revenue and margin by registration holder are NOT FOUND in the AR, three decks, the results and the ICRA rationale. The web brief carries the 28-32% and 24-26% EBITDA bands, unanchored.
- The company secretary resignation claim has no filing behind it. The incumbent signed the 9 Nov and 14 Nov 2026 filings. The Q2 transcript would settle it.
- GST contingent liabilities of 3,697.75 INR lakh, 11.2% of net worth, carry no provision. Writs CWP-12033-2026 and CWP-34165-2024 are pending (AR Note 34 p.226-227).
- The shareholding folder holds the BSE summary only. The FII and DII breakdown is missing, so the institutional absence qualifier for the UA multiplier is unevidenced. Source: the full BSE shareholding pattern, Sep 2026.
- The screener Profit & Loss, Quarters, Balance Sheet and Cash Flow sheets are empty for KPL and all three peers. Open Financials.xlsx once, save it, and run --push-again.
- Peer transcripts are 10 of 12. Caplin has no Q2 FY27 call yet. Lincoln has no call after Feb 2026, plus one stale May 2024 call.
- Verifier A could not check the web market figures against filed sources (IMARC, EMR, Pharmexcil, RBI and others). Several came from search snippets with the pages unopened.
- The Mental Model Declaration is NOT SIGNED. The Halt 1 decision is pending. Nothing after Halt 1 runs until both are done.

## Publish check

No publish candidate this analysis.
