MISSING MATE DOCUMENT (FRESHNESS FAIL, RESULTS to CONCALL): Q2 FY27 earnings-call transcript for GE Power India (call scheduled 16 Nov 2026, 3:30 pm IST, per BSE intimation of 6 Nov 2026). Expected source when filed: BSE scrip 532309 announcements, or the screener.in GVPIL documents page. Push it to inputs/concalls/ with `py collect_to_repo.py --push-again`.

VERDICT: PROCEED WITH CAVEATS

# GVPIL FTTCP gate recommendation, PHASE 1 LITE (run 2026-11-15)

This is the go/no-go for the FTTCP deliberation on the evidence record alone. It carries no investment decision, no entry range, no margin of safety price, no destination multiple and no Hurdle verdict. Those form in phase 3. The Mental Model is NOT SIGNED, so nothing here binds the deliberation.

## Verdict block

- Verdict: PROCEED WITH CAVEATS.
- Three caps bind it, each enough on its own:
  1. Freshness cap. The corpus freshness verdict is CORPUS GAPPED-FRESHNESS. The Q2 FY27 results (letter 13 Nov 2026) have no same quarter call transcript.
  2. Cash cap. The cash conversion determination is INDETERMINATE (flag block below). INDETERMINATE caps at PROCEED WITH CAVEATS and never resolves to PROCEED.
  3. Verifier MAJORs worth carrying. Verifier A logged 4 MAJOR, Verifier B 3 MAJOR and Verifier C 2 MAJOR findings. None changes a classification, and all are listed in verifier-summary.md.
- Rule 1 (REWORK) does not fire. Verifier A logged no CRITICAL finding. No verifier acceptance rate sits below 60% on a denominator of 4 or more. Overall confidence is 83.3. The three source fidelity rows touch context figures, not a verdict card or pillar input, and each was corrected at its source anchor before this file was written.
- Rule 2 (INSUFFICIENT EVIDENCE) does not fire. The annual report, the audited and two later quarterly results, the rating rationale and three earnings calls are all present, so the decision record is intact. The gaps are named below and each has a place to obtain it. Second reading: if the half year cash flow in the Q2 FY27 results cannot be read from any source before the deliberation, the cash question has no current data point, and the operator can treat that as INSUFFICIENT EVIDENCE on cash. The separating observation is whether a legible H1 FY27 cash flow statement exists (re-extract the results PDF, or the BSE XBRL filing).
- Partial stages, named: stage 8 promoter scan (B08, status partial: AGM vote tallies for Items 8 to 10, the filed shareholding pattern with pledge, proxy adviser reports, employee review sites and MCA or RoC searches not reached) and stage 9 market sizing (B09, status partial: realistic TAM NOT FOUND, BHEL FY26 spares and services bookings not found, the CEA R&M document not fetched, competitor revenue aggregation incomplete).
- Confidence: overall 83.3, overall_set_by peer_utilisation, band 75 to 89 (normal, note specifics). The valuation half of framework adherence is pending phase 3.
- Remediation cycles used: 0 of 1. Verifier runs: A 1, B 1, C 1, D 1. No open item from either cap.
- No stage returned status blocked.

## Transition posture

Not classified in phase 1. The posture reads three state variables from the signed Mental Model: the proof gate (Part B3), the ugliness class (Part B5) and the recognition gap, which resolves at stage 11. The model is unsigned and stage 11 has not run. For the operator at Halt 1, the evidence each variable will draw on is this. The proof gate question is whether core services intake growth and a margin above 11% excluding other income both hold after the one time items. The ugliness question is whether the profit and cash optics (other income above half of profit, the group deposit, the order book fall) are artifacts of the exit from FGD and new build or features of a parent captive structure.

## Flag blocks

```
⚠️ CASH CONVERSION FLAG: FY26 CFO INR M 4,693.6 consolidated (Rs 469.36 Cr) against PAT Rs 252.61 Cr, 1.86x (calc), up from CFO Rs 182.40 Cr in FY24. Direction on the numbers: improving. Quality: one time. Forward direction: not established.
Determination: INDETERMINATE.
Evidence:
- Receivable release. Receivables decrease INR M 5,136.5 inside FY26 CFO (AR26 consolidated cash flow p.215; standalone INR M 5,136.0, AR26 p.133). Gross receivables INR M 18,950.3 / 13,489.2 / 8,260.5 at Mar-24 / Mar-25 / Mar-26; net days 597 / 409 / 219 (calc, FY24 not like for like) (AR26 Notes 13, 25 p.156-157, p.164; B02 receivables_trend).
- Receivables composition. FY26 release tied to BHEL settlement cash INR M 3,430.6, a one time size (AR26 Notes 53-54; Results Q2 FY27 note 4; B02, B05). Aged above six months INR M 1,314.1 (15.9%) at Mar-26; retention INR M 4,751.7; allowance INR M 635.9 (B02 receivables_trend). About Rs 640 Cr of non-BHEL receivables (FGD retentions and running bills) carry no stated collection timeline (Q2 FY26 call p.15, Verifier B MINOR, B12b).
- Offsets building against cash. Customer advances INR M 677.9 against 1,764.0 and billing in excess INR M 3,399.9 against 4,420.4 (AR26 p.164); together down INR M 2,106.6. Inventory +69.9% on revenue +21.2%, about 71 against 46 days (calc) (AR26 Note 12 p.156; B02 rank 12).
- Where the cash went. INR M 4,500.0, 95.9% of FY26 CFO, moved to an unsecured demand ICD with LM Wind Power Blades (India), the GE Vernova cash pool header (AR26 Note 16 p.158; CARO iii(a) p.128; B03 FLAG-CASH).
- FY25 comparative. FY25 CFO re-presented up INR M 593.9 (3,196.5 to 3,790.4) when the Durgapur drain of INR M 349.5 moved to financing (B03 FLAG-CASH).
- Capex commissioning timeline. Not a cash driver: capex is INR M 21.3 (FY26) and INR M 30.3 (FY25) (AR26 p.215, B12a mandatory tier), and capex embedded growth is 0 (B07). The one named project is the Vadodara repair facility with Quality Profiles (INR 18 Cr plus INR 25 Cr committed); its 53 week licence fee free setup period ends about 25 May 2027 (Reg 30, 20 May 2026, Annexure A(e); B07).
- Rating agency, verbatim (ICRA rationale, 3 Mar 2026; quotes retrieved by stage 13 from inputs/rating/ICRA_Rationale_2026-03-03.txt, because no upstream stage quoted this passage):
  p.1: "the company's decision to exit from construction portion of the EPC business is expected to reduce execution risks, shorten project cycles and moderate working capital intensity."
  p.2: "the new orders are likely to be more profitable with a shorter working capital cycle given a much shorter average duration for order execution in the services business."
  p.2: "deterioration in the working capital cycle owing to elongation in the receivables period will remain a key downward trigger."
Why INDETERMINATE, not GROWTH-INDUCED or STRUCTURAL: revenue growth of 9.3% in H1 FY27 is too slow to explain a working capital build, and the FY26 figure is a release, not a build. ICRA's reading (short cycle services shorten the cycle) is a forecast, and the filed record has no period after the release yet. The Q2 FY27 trade receivables and days were not legible in the OCR of the results file (B05 input_gaps), so no H1 FY27 cash data point exists in this run.
Missing evidence that would decide it:
1. H1 FY27 statement of cash flows and balance sheet (receivables, inventory, contract liabilities) from Results_Q2FY27_30Sep2026.pdf, re-extracted, or the BSE XBRL filing for scrip 532309.
2. Receivables ageing by customer for the non-BHEL book (FY27 half year notes or AR27 Note 13).
3. Q2 FY27 call commentary on collections and the cash pool (call 16 Nov 2026).
Separating metric (not a GROWTH-INDUCED falsifier, since no such determination is made): H1 FY27 CFO excluding group deposit movements against H1 FY27 PAT. At or above PAT, with receivable days at or below 219 and inventory days at or below 71, points to the ICRA reading. Below PAT points to a working capital rebuild.
Verdict effect: caps at PROCEED WITH CAVEATS.
```

```
⚠️ GATE 0 FLAG (FLAG-GATE0): classification AVOID. Grand total 44 of 160; core 33 of 100; moat 11 of 60; moats confirmed 2 of 12; moat class MODERATE (B01).
Blocks: A 6, B 2, C 1, D 16, E 8 (B01).
Deal-breakers: (1) Block A 6 below 8, FY22 to FY24 losses; (2) Block B 2 below 8, FY19 to FY21 negative CFO and capex gaps; (8) PAT negative in the last 3 years, FY24 Rs -171.33 Cr (B01).
Verifier C recompute: Block B 0 (B2 on the 10 year window, 3 of 10 = 30%), core 31, grand 42; deal-breaker 4 also fires (cumulative CFO/PAT -1.92 below 0.50); AVOID holds under every reading (B12c F-G10, F-G42). Observation O-01: moat class MODERATE rests on FY26 spot ROCE 48.4% in M3; on the window median (11.5%) the class is THIN, 1 moat, moat score 6 (B12c).
Depressors and whether they are historical:
- Historical, legacy cleanup: FY22 to FY24 losses (FY24 PAT Rs -171.33 Cr; cumulative ten year PAT Rs -190.51 Cr) from the FGD and new build EPC legacy (B01).
- Historical, restructuring: the gas and hydro carve-outs (FY25) and the Durgapur demerger (sanctioned 1 Oct 2026, not yet effective) reset the perimeter; FY17 to FY24 rows are on the old perimeter, so the revenue CAGR compares different bases (B01 data_notes; B04).
- Not yet shown to be historical: the FY25 and FY26 recovery rests on one time items. The M2 score of 5 falls to 3 without the INR M 1,016.6 loss allowance credit (AR26 p.252); FY26 EBITDA 20.4% is 12.4% excluding the credit (AR26 p.214, p.252; B01 FLAG-EARNINGS-QUALITY).
Effect: none on the verdict. Gate 0 AVOID is a backward screen label, not an investment decision; it caps nothing.
```

```
PROMOTER: FLAG-PROMOTER rule NOT FIRED. B08 verdict CAUTION, below the CONCERN line that triggers the flag (scorecard clean 5, caution 5, red 0; deal_breakers none). B08 emitted a FLAG-PROMOTER entry carrying CAUTION; it is shown here in the flag format so it is not missed.
Verdict: CAUTION, classified STRUCTURE, not INTEGRITY (B08 analyst_note).
Top findings: [1] INR M 4,500.0 unsecured demand deposit to the promoter group cash pool header LM Wind (21.4% of assets, 106% of cash, calc); guarantee proposed only at the 14 Aug 2026 AGM; ceiling to rise to INR M 10,000 (AR26 Notice Items 8-10 p.312-319; Note 16 p.158; Note 36 p.180-182). [2] Group royalty INR M 435.7 in Note 36 against INR M 125.7 in the P&L line; INR M 310.0 gap unreconciled (FY25 gap 382.4 on the AR25 original basis, 393.0 against the re-presented line) (AR26 Note 33 p.168, Note 36 p.180; B12a MINOR row 7).
Further findings: KMP turnover in 2026 (WTD and CFO, company secretary, one senior manager); group sourced other income INR M 851.9 = 25.1% of profit before exceptional items; Directors' Report says no guarantee provided while Note 36 labels a received guarantee INR M 7,977.6 as issued; GST demand orders (INR M 319.5 penalty FY2018-21 under appeal; Odisha FY2020-21) (B08 adverse_findings).
Transition evidence: (1) promoter ended its exit and de-promoterisation plan on 25 Jul 2024 and holds 68.58%, flat for 12 quarters; (2) new CFO Rahul Rojal and CS Vipul Sharma appointed 19 Jun 2026, WTD Shrikar Thakur approved at the 14 Aug 2026 AGM; (3) internal audit to Ernst & Young LLP, Deloitte Haskins and Sells re-appointed, unmodified opinions; (4) independent director added May 2025, board 3 of 6 independent, ICRA upgrade to BBB+ (B08 transition_evidence).
Tripwires named by B08: guarantee covering the ICD in writing; ICD size above INR M 4,500; royalty reconciliation; permanent CFO tenure.
Verifier B adds (MAJOR, missed upstream): the BHEL settlement was a three party deal with the promoter's offshore Vernova entities; the group side was not disclosed when asked; INR 17 Cr gap between the INR 357 Cr receivable and the INR 340 Cr agreed (calc) (Q2 FY26 call p.9, p.14; B12b).
Stage status: B08 partial (vote tallies, proxy advisers, MCA/RoC not reached).
```

Other stage flags carried as caveats (each corrected value is the one shown):

| Flag | What it says | Anchor |
|---|---|---|
| Earnings quality | INR M 3,174.4 profit step up is 55.2% loss allowance swing (1,320.0) plus other income rise (433.5); reported 27.0% is on total income; FY26 margin excluding other income and the credit 12.4%; Q1 FY27 14.5%, Q2 FY27 9.8%, H1 12.2%; other income 59.0% of Q2 FY27 PBT before exceptional, 51.9% for H1 | AR26 p.132-133, p.167-168; Results Q2 FY27 p.3; B02, B04, B05; B12a MINOR row 5 |
| Orders (corrected) | RPO INR M 26,623 to 16,278 (-38.9%) is driven by the INR M 7,749 Jaypee FGD EP termination; like for like -13.8% (calc). The earlier derived book-to-bill 0.18 is withdrawn; use deck intake Rs 877 Cr. INR M 1,327 bridge gap unexplained | Results Q1 FY27 p.15; AR26 Note 27 p.166; Q4 FY26 deck p.6; B04 FLAG-ORDERS-CORRECTION |
| Guidance | 11% is the FY26 entity level normalised EBITDA including discontinued Durgapur, not an FY27 guide; CFO declined a range; 85% to 90% applies to "order in hand", not a named core backlog | Q4 FY26 call p.6-8, p.15; B04 FLAG-GUIDANCE; B05 |
| Demerger | Durgapur cost INR M 548.0 FY26 outside continuing P&L; INR M 247.0 internal billing not charged to continuing cost; JSW supply price after the demerger and the consideration NOT FOUND; NCLT sanction 1 Oct 2026, not effective at 30 Sep 2026 | AR26 Note 47 p.194-198; Results Q2 FY27 note 2; B02, B04 |
| Provisions | Note 26 FY26 warranty 185.0 and loss order 137.7 "slump sale" deductions repeat FY25 values; P&L effect NOT STATED, bound nil to INR M 299.2 on warranty | AR26 Note 26 p.164-165; B02 FLAG-PROVISION |
| CARO reconciliation | CARO vii(b) disputed dues INR M 8,022.1 against Note 39 contingent liabilities INR M 4,575.9; gap INR M 3,446.2 unreconciled | AR26 CARO p.129; Note 39 p.185; B03 |
| Disclosure | MD&A omits the JSW demerger, the ICD and customer names; attrition 8.7% (MD&A) against BRSR turnover 71.11% | AR26 MD&A p.90-93; BRSR p.51; B03 |
| Market size shift | Management market Rs 2,500 Cr (defined, Q3 FY26 call) to Rs 3,500-4,000 Cr (undefined, Q4 FY26 call); same Rs 734 Cr intake is 29.4% or 18.4% | Q3 FY26 call p.7, p.13; Q4 FY26 call p.8; B09 |
| Concentration | Top two customers 38.6% FY26 against 34.8% FY25; names NOT FOUND | AR26 Note 35 p.176 |

## Confidence delta (phase 1)

| Component | Value | Basis | Source |
|---|---|---|---|
| numerical_acceptance | 98 | 429 numbers checked; mandatory tier 139 of 139 (Gate 0 scorecard); 0 CRITICAL, 4 MAJOR, 4 MINOR | B12a |
| redflag_coverage | 86 | 14 material verifier flags, 12 caught (9 caught, 3 partially caught); strict caught only 64 | B12b |
| framework_adherence | 89.3 | Gate 0 and Emerging Moat only, 67 of 75 rules passed; valuation half PENDING PHASE 3 | B12c |
| peer_utilisation | 83.3 | 10 of 12 peer transcripts used substantively | B12d |
| overall | 83.3 | min of applicable components; overall_set_by peer_utilisation; not_applicable none | confidence.yaml |

Weakest component: peer utilisation at 83.3 (overall_set_by peer_utilisation). Two BHEL transcripts (Q1 FY22, Q4 FY22) are cited only, and every BHEL citation dates from 2021 to 2024, so no current read exists on the main OEM rival. The strict caught only red flag rate of 64 is the second soft spot.

## Contradicted claims

Peer stage contradicted list: none. No peer contradicts a company claim, and no peer names the company.

Nearest to a contradiction, for monitoring:
- Q2 FY27 margin fall. ISGEC margins rose in the July to September 2026 quarter (manufacturing EBIT 13.7%, projects 5.7%) while the company's margin excluding other income fell 4.7 points to 9.8%. Sector input costs explain the direction, not the size (ISGEC Q2 FY27 call, 5 Nov 2026, p.3-4, p.13; Results Q2 FY27 p.3). Verifier B notes that Power Mech's margin rise is the April to June quarter, so only ISGEC covers the same period.
- Margin basis. Power Mech O&M margin of 15% to 18% sits above the company's 10% to 12%, but Power Mech includes other income and its O&M is manpower based (Power Mech Q4 FY26 call p.18; Q1 FY27 call p.16-17).

Claims the filed record corrected (Step-1 web leads and management statements):
- "11% FY27 normalised margin guide": FY26 entity level actual including Durgapur; no FY27 range (Q4 FY26 call p.15).
- "Q2 FY27 other income 48% of PBT": 59.0% (Results Q2 FY27 p.3).
- "Royalty Rs 13.21 Cr": that is the AR25 P&L line (INR M 132.1); FY26 related party royalty is INR M 435.7 (AR26 Note 36 p.180).
- "Healthy order backlog" (MD&A): RPO -38.9%; like for like -13.8% after the termination add back (AR26 Note 27 p.166; Results Q1 FY27 p.15).
- "8 Sep 2026 order receipt": a GST demand order, not an order (Reg 30, 8 Sep 2026).
- "Durgapur average annual loss about Rs 27 Cr" (Jul 2026 deck p.7): filed discontinued loss before tax INR M 548.0 in FY26 and INR M 304.2 in H1 FY27 (Results Q2 FY27).
- Q4 FY26 revenue of Rs 316 Cr as clean delivery: the CFO told one analyst the BHEL reversal sat in cost (Q3 FY26 call p.9-10) and another to deduct about Rs 41 Cr from Q4 revenue (Q4 FY26 call p.16), giving about Rs 275 Cr underlying (calc). Unresolved.

## Monitorables and triggers

1. Listen to the Q2 FY27 call on 16 Nov 2026 and read its transcript on BSE. Note the reason given for the 9.8% margin, how Shoaiba is booked, what makes up the Rs 63 Cr of H1 other income, and any cash deployment plan. This closes the freshness gap and tests the margin base.
2. In the Q3 FY27 results (Feb 2027), compute margin excluding other income: PBT before exceptional items plus finance cost plus depreciation, less other income, over revenue from operations. Above 11% supports the services margin reading. A second quarter below 10% without a named mix reason breaks it.
3. In the same results, divide other income by PBT before exceptional items. Below 25% is healthy. Above 50% (H1 FY27 51.9%) means reported profit still rests on interest and group income, not on repairs.
4. In each quarterly press release and deck, check core services order growth and the oOEM share of core orders. Double digit YoY growth (Q2 FY27 +38%) and an oOEM share at or above 50% (FY26 43.6%) confirm the services engine. Intake below the prior year quarter, or an oOEM share falling further, kills it.
5. Track the order backlog (INR M 15,273 at Q2 FY27) and the services backlog (Rs 1,218 Cr at Mar 2026). Shoaiba should add about Rs 550 Cr once a contract is signed. A services backlog below Rs 1,124 Cr, or no Shoaiba entry by Q1 FY28, cuts revenue visibility.
6. In the H1 FY27 and FY27 cash flow statements, compare operating cash excluding group deposit movements with PAT. Cash at or above PAT, receivable days at or below 219 and inventory days at or below 71 resolve the INDETERMINATE cash flag toward the ICRA reading.
7. In the half year notes and exchange filings, check the group deposit: balance at or below INR M 4,500, a written GE Vernova guarantee covering 100% of it, its inclusion in the credit risk note, and the AGM vote tallies for Items 8 to 10. A balance rising toward INR M 10,000 with no cover, an unreconciled royalty gap, or a second CFO exit tests the STRUCTURE classification of the promoter read.
8. In exchange filings, watch for the Durgapur certified order filed with the RoC and the JSW supply terms. The discontinued loss (INR M 304.2 in H1 FY27) should stop. Material cost above 67% of revenue on the net of WIP basis (Q2 FY27 64.4%) signals the JSW supply price is eating the margin.

## Falsification line

The Q3 FY27 results (quarter ending 31 Dec 2026): margin excluding other income below 10% of revenue from operations for a second straight quarter after Q2 FY27's 9.8%, with no named mix reason. That print says the FY26 12.4% was not the base.

## Publish check

No publish candidate this analysis.
