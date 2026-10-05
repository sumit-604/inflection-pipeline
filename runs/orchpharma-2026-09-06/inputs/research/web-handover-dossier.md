# WEB HANDOVER DOSSIER — ORCHPHARMA (Orchid Pharma Ltd, BSE 524372)
## claude.ai live-verification layer, Halt 1 close-out

**Run:** `runs/orchpharma-2026-09-06/` | **Branch:** `claude/orchpharma-2026-09-06-runs-bx6lcr`
**Produced:** 28-Sep-2026 in the claude.ai project (Dhruva Research), from the Halt 1 stress-test and vertical deep dive of 21 to 28 Sep 2026.
**Inputs consumed:** Claude Code extractions (imports, CWIP, geography, cash flow and merger, Synmedic), Screener AI answers accepted only where cited and spot-checked, live web (issuing bodies, rating agencies, counterparties).

**Precedence rule.** Where this dossier conflicts with a corpus document, the corpus document wins UNLESS this dossier marks an explicit supersession with its evidence (Section 3). Evidence tiers: [FILED] filed document; [AGENCY] rating agency or regulator; [MGMT] management verbal; [COUNTERPARTY] a customer's, supplier's or rival's own disclosure; [SECONDARY] news, forum, aggregator; [INFERENCE] analyst arithmetic or deduction, always labelled.

---

## 0. INSTRUCTIONS FOR CLAUDE CODE

1. Commit this file to `runs/orchpharma-2026-09-06/inputs/research/web-handover-dossier.md` on branch `claude/orchpharma-2026-09-06-runs-bx6lcr`.
2. Add the TRACKER PROOF block in Section 10 to `companies/ORCHPHARMA.md`, replacing "TRACKER PROOF: PENDING". This satisfies the Role 5.5 tracker gate.
3. Apply correction 37 (Section 3) to the signed mental model text in `companies/ORCHPHARMA.md` if it is not already there.
4. Run outputs only on this branch. No framework edits. Open the PR the same day. Merge before any FTTCP session.
5. Do NOT start `/fttcp` until the operator says "run FTTCP".
6. Two extractions are requested before or during FTTCP Step 1 (not blockers, but the P/E card is provisional without them):
   - **X1.** Orchid Bio-Pharma Ltd: Orchid's percentage holding, any other equity holder, and whether any option, warrant or partner equity exists. Source: FY26 AR subsidiary list and Form AOC-1.
   - **X2.** Any management statement of peak revenue, EBITDA margin, or per-kg cost for the Jammu 7-ACA plant at full utilisation. Source: all concall transcripts FY24 to Q1 FY27, investor presentations. Quote-then-comment; NOT DISCLOSED where absent.
   - **X3.** Reconcile Q1 FY27 EBITDA margin: this dossier computes operating EBITDA 4.9% excluding other income; the 09b dossier carries ~8.2% "combined". State which lines each includes. Source: Q1 FY27 results filing.

---

## 1. ENTITY COUNT, HALT 1 RULING AND SIGNED MENTAL MODEL

### 1.1 Entity count: ONE

**Declared entities: 1 — Orchid Pharma Ltd (consolidated).**

- Dhanuka Laboratories Ltd merged INTO Orchid, appointed date 1-Apr-2024, effective 10-Jul-2026 [FILED]. It no longer exists as a separate entity. All history is on the restated combined basis.
- Orchid Bio-Pharma Ltd (OBPL, the Jammu 7-ACA project) is a subsidiary [FILED]. No listing, demerger, spin-off or outside equity is disclosed. It is scored as a CONVERTER SLICE inside the one entity (Amendment 17), not as a separate entity. Extraction X1 confirms the holding. **If X1 shows any outside equity holder or partner equity, the count becomes TWO and FTTCP runs per entity.**
- Synmedic (98% held, NOT consolidated, FY26 loss about Rs 13.2 cr) [FILED] is an investment, not an entity. It is carried as a governance tripwire and a cash leak line, not scored.
- Dormant US subsidiaries (qualified consolidated opinion) [FILED]: not operating entities. Carried in the governance tripwire.

Value slices inside the one entity (for SOTP inside a single pass):

| Slice | Archetype | Treatment |
|---|---|---|
| Core cephalosporin API, oral and sterile, incl. merged Dhanuka | CONVERTER economics (spread, price taker) | Core PE per Section 1B |
| Jammu 7-ACA (OBPL) | CONVERTER slice, stranded until COD | 0.5 x destination ROCE + 7.5, never core PE |
| Exblifep (enmetazobactam) | IP option | Amendment 18 option, resolved state at exit |
| Cefiderocol (GARDP) | Cost-plus contract | Earnings inside core once commissioned |
| PLI on 7-ACA | Time-bound cash inflow | Discrete, FY28-FY29 only |

### 1.2 Halt 1 ruling (operator, 28-Sep-2026)

- Mental model: SIGNED, with correction 37 applied.
- Halt 1: **PROCEED.** Claude web recommended SHALLOW WATCH (price ahead of proof; Gate 0 core 29 defaults to WATCHLIST). Operator changed it to PROCEED on 28-Sep-2026. The run proceeds to FTTCP and valuation for research; Gate 0 core below 60 still defaults any verdict to WATCHLIST.
- Promoter items ruled STRUCTURE concerns (Section 8).
- FLAG-CASH ruled split (Section 6).

### 1.3 Signed mental model (plain form)

**The business.** Orchid makes cephalosporin antibiotic APIs and sells them by the kilogram to formulators in India and abroad. It sets no prices. It buys its key inputs: GCLE for oral products from Otsuka Chemical (India), a related party, and 7-ACA for sterile products, mostly from China. It is building its own 7-ACA fermentation plant in Jammu. It owns one novel antibiotic (Exblifep) and a cost-plus manufacturing contract (cefiderocol for GARDP).

**Analogy.** A flour mill in a town of flour mills. It buys wheat from outside and sells flour at the price the neighbours set. It is building its own wheat farm with the same seeds foreign farms use, so the farm helps only if local land, power and a temporary subsidy make its wheat cheaper than imported wheat. It holds one patented recipe not yet sold in the biggest market. The bank wants instalments before the first harvest.

**Dominant variables (four).**
1. Core price spread (gross margin). Current: 31.5% FY26; about 33% Q4 FY26 and Q1 FY27 [FILED]. One point is about Rs 13 cr EBITDA a year [INFERENCE].
2. Jammu on time, on cost, and cheaper than Chinese 7-ACA. Current: COD guided Feb-Mar 2027, cost Rs 750 cr [MGMT].
3. Cash wall FY27-FY28. Current: principal about Rs 40 cr FY27, about Rs 130 cr a year from FY28 [FILED maturities plus INFERENCE].
4. Exblifep US partnering. Current: no partner; management's target expires 30-Sep-2026 [MGMT].

**Rejected as noise.** Quarterly revenue swings from inventory timing; other income; the hospital (AMS) division; the Russia deal headline dollar value; the "up to Rs 600 cr" PLI headline; price moves around the merger share listing.

**Model falsifier.** Material cost at or above 63.5% of sales four quarters after Jammu COD (about the Mar-2028 quarter). That would mean the plant bought no cost edge.

**Fragility.** FRAGILE. The cash wall arrives before the plant's proof.

**Competitive position.**
- Real: scale in cephalosporins (domestic share about 34% merged, 15-20% legacy Orchid [MGMT]); clean FDA inspection record, all VAI 2010, 2012, 2015, 2019, 2025 [AGENCY, FDA via ProPublica FEI 3003747558]; sterile pricing held (+17% FY26) while oral fell 13% [INFERENCE from FILED volumes]; long Otsuka GCLE supply relationship with about 100 days of credit [FILED] (also a single-source dependency).
- Emerging, unproven: own 7-ACA (one of two PLI applicants; see correction 37 on Aurobindo); Exblifep IP (US exclusivity to about 2034 [AGENCY]); GARDP credential.
- Not advantages: oral pricing (Covalent larger and integrated via group Pen-G [AGENCY]); regulated-market share falling 40% to about 30% of sales over three years [FILED]; rising debt; disclosure quality.

---

## 2. VERTICAL FINDINGS (verdicts with tiers)

### V1. Core API spread. Verdict: PRICE TAKER IN A PRICE WAR; STERILE HOLDS, ORAL FALLS.

- Revenue: FY26 restated combined Rs 1,233 cr against Rs 1,398 cr FY25 (−12%); legacy Orchid Rs 811 cr against Rs 922 cr (−12%) [FILED/MGMT]. Dhanuka about Rs 422-475 cr a year [INFERENCE from restated minus standalone].
- Geography: exports (rest of world) Rs 996 cr → Rs 796 cr (−20%); India +7% [FILED].
- Realisations FY26 [INFERENCE from FILED volume and value]: oral Rs 13,388/kg (FY25 Rs 15,356, −13%); sterile Rs 18,520/kg (FY25 Rs 15,883, +17%).
- Gross margin: 31.5% FY26; about 33% Q4 FY26 and Q1 FY27 [FILED].
- Operating cost structure [INFERENCE]: fixed costs about Rs 350 cr a year; breakeven about Rs 260 cr revenue a quarter; each Rs 100 cr revenue above that adds about Rs 33 cr EBITDA.
- FY26 operating EBITDA Rs 37.8 cr (3.1%) reported; about Rs 56 cr (4.6%) excluding Synmedic (Rs 13.2 cr loss plus Rs 5.4 cr impairment in other expenses) [FILED plus INFERENCE].
- Q1 FY27 operating EBITDA 4.9% excluding other income; consolidated PBT Rs 2.65 cr [FILED; see X3 for the 8.2% reconciliation].
- FY27 cases [INFERENCE]: base 7.3% on revenue Rs 1,360 cr at GM 33%; bear 3.9%; bull 10.4%. Management guides about 12% including other income, about 9% on a consolidated operating basis [MGMT plus INFERENCE].
- Market price: cefixime industrial price about $127.6/kg, flat; cefuroxime axetil about $96.1/kg, −9.3% over 90 days [SECONDARY, Pharmaoffer]. India makes about 90% of cefixime exports [SECONDARY]. The oral war is India against India.
- Rival: Covalent Laboratories (Virchow Group, Hyderabad), largest Indian maker of cefixime, axetil and cefdinir; FY25 operating income Rs 2,675.8 cr; OPBDITA margin 10.2% FY24, 9.8% FY25; bought Nectar Lifesciences' API, formulation and menthol businesses for Rs 1,290 cr (Nov-2025) with a Rs 700 cr term loan; debt/OPBDITA to about 3.5x by Mar-2027 from 0.2x; group company and vendor Virchow Petrochemicals commissioning domestic Pen-G [AGENCY, ICRA 31-Mar-2026, verified live 28-Sep-2026].
- Regulated-market share of sales 40% → 36% → 32% → about 30% [FILED].
- FDA: all VAI across five inspections [AGENCY]. Form 483 (fda.gov media/191891) observations contradict the company's "no data integrity" wording [AGENCY vs MGMT].

### V2. Jammu 7-ACA (OBPL). Verdict: ON A SLIPPED BUT LIVE SCHEDULE; EDGE IS LOCATION PLUS A TIME-BOUND SUBSIDY, NOT TECHNOLOGY.

- Capacity 1,000 t/yr 7-ACA [MGMT/FILED].
- Cost path Rs 489 cr → Rs 596 cr → Rs 600-700 cr → Rs 750 cr [FILED/MGMT]. Spent plus contracted about Rs 600 cr [MGMT].
- Schedule: monitoring agency original schedule land Jun-2024, plant and machinery Dec-2024 [FILED]. COD then Dec-2026 (AR) → Sep-2026 (Q3 FY26 call) → Mar-2027 (Q4 FY26, Q1 FY27 calls). Current guide Feb-Mar 2027 COD, 12-month ramp [MGMT]. Scale-up about 800x from pilot, "a little unpredictable" [MGMT].
- Land: 203.8 Kanal acquired, 176.65 Kanal registered; the rest was due Mar-2026 and was still pending in the Aug-2026 monitoring agency report [FILED]. About 3.4 acres unregistered [INFERENCE from the Kanal gap].
- Technical know-how budget Rs 10 cr, Rs 3.77 cr spent [FILED].
- OBPL FY26 financials [FILED]: capex Rs 193.8 cr; interest capitalised Rs 13.64 cr; guarantee commission to Orchid Rs 1.84 cr; loans HDFC sanctioned Rs 217.22 cr / drawn Rs 33.32 cr, maturity 31-May-2035; ICICI Rs 70 cr / Rs 70 cr, 1-Apr-2034; YES Bank Rs 160 cr / Rs 75 cr, 1-Apr-2034; current maturities Rs 28.79 cr; auditor Ashok Kumar Malhotra & Associates.
- Technology: the partner supplies technology "to even the Chinese manufacturers... economics should be similar" [MGMT, Q4 FY23 call, 11-May-2023]. Partner identity and country NOT DISCLOSED.
- Offtake plan: about 80% in-house (about 25% captive for own sterile APIs, about 50% into downstream non-sterile ceftriaxone for Aurobindo and others), about 20% sold outside [MGMT]. Regulated-market products need DMF/CEP source changes, so unregulated products benefit first [INFERENCE].
- PLI [AGENCY, DoP guidelines 29-Oct-2020 and DoP Annual Report 2025-26]:
  - Rates: 20% FY24-FY27, 15% FY28, 5% FY29.
  - 7-ACA ceiling per company: Rs 120 cr a year in years 1-4, Rs 90 cr FY28, Rs 30 cr FY29. "Up to Rs 600 cr" is the six-year scheme ceiling.
  - In-house consumption valued at the lower of the quoted price and actual cost.
  - 90% domestic value addition required; 80-90% earns 50% for 12 months only.
  - Full committed capacity installed before claiming; sale price fixed at the 2021 quote; unclaimed incentive lapses.
  - Orchid's reachable total about Rs 65 cr at most (FY28 about Rs 40 cr, FY29 about Rs 26 cr) [INFERENCE], subject to the 90% rule.
- Other 7-ACA applicant KAPL: cost +58%, offered for sale Nov-2024 [AGENCY, CARE; FILED, EOI].
- Aurobindo reported 7-ACA project about 2,000 t/yr [corpus 09b Correction 7.1; status NOT verified live]. See correction 37.
- Policy: DGFT minimum import price on Pen-G (Rs 2,216/kg), 6-APA and amoxicillin, 29-Jan-2026, exempting EOU, SEZ and Advance Authorisation imports [AGENCY]. It does not cover 7-ACA or GCLE. China MOF Announcement 2 of 2026 export-rebate cuts list no antibiotics or 7-ACA [SECONDARY copy]. Chinese 7-ACA prices get no policy lift.
- Consent to operate (JKPCC): status not found; the OCMMS portal was unavailable when checked. Expected before COD.

### V3. Cash and debt. Verdict: CORE CASH STRUCTURAL; DEBT SERVICE ARRIVES BEFORE JAMMU EARNS.

- Borrowings Rs 3,230 cr FY19 → Rs 135 cr FY24 → Rs 363 cr FY26 [FILED].
- FY26 consolidated CFO Rs 126 cr, of which Rs 85 cr came from inventory release [FILED]. Underlying CFO about 60% of operating EBITDA [INFERENCE].
- Receivables: about Rs 28 cr in an aged pocket, unprovided [FILED].
- Old payables about Rs 56.5 cr sit in dormant US subsidiaries [FILED].
- Debt service [FILED maturities plus INFERENCE]: FY27 principal about Rs 40 cr (OBPL current maturities Rs 28.79 cr plus cefiderocol loan from Nov-2026); FY28 onward about Rs 130 cr a year.
- Base FY27 EBITDA about Rs 100 cr → about Rs 60 cr CFO [INFERENCE]. FY28 service needs Jammu earnings, refinance or new equity.
- Otsuka credit: about 100 days on about Rs 231 cr FY25 purchases [FILED] = about Rs 60-67 cr of related-party supplier credit [INFERENCE]. A change in terms moves working capital by that amount.

### V4. Exblifep and cefiderocol. Verdict: OPTION NOT YET CASH; CONTRACT IS SMALL AND SAFE.

- Exblifep: FDA approval Feb-2024; GAIN exclusivity to about 2034 [AGENCY]. Europe licensed to Advanz; management gives growth rates only, refuses absolute sales [MGMT]. Russia: licensing and supply with Pharmasyntez, 7-Jul-2026, headline $178m over the deal life [FILED/SECONDARY]. US: no partner. Target "this quarter, coming quarter" (May-2026 call) expires 30-Sep-2026 [MGMT]. No US deal found on 28-Sep-2026; one secondary site reports a target of FY27 [SECONDARY].
- Enmetazobactam global rights: 100% bought back from Allecra [FILED].
- Cefiderocol: Shionogi-GARDP-CHAI licence; GARDP sublicence to Orchid. Economics cost plus 25% at PBT [MGMT, Q3 FY24 call 9-Feb-2024 and Q1 FY25 call 13-Aug-2024]. Commissioning Dec-2026; India launch Q3 FY28, needs a DCGI waiver; ex-India needs WHO prequalification [MGMT]. Debt service from Nov-2026 [FILED].

### V5. Merger and share count. Verdict: RECONCILED; OVERHANG EXTINGUISHED; FAIR TO SLIGHTLY FAVOURABLE FOR MINORITIES.

- Dhanuka Laboratories (69.84% holder) merged into Orchid; swap 161 Orchid shares per 5 DLL shares; 4,45,86,052 new shares allotted 1-Aug-2026 [FILED via stage 8].
- Share count [INFERENCE]: 5.07 cr pre-merger − 3.54 cr cancelled (DLL's own 69.84% holding) + 4.459 cr new = **about 5.99 cr**. This reconciles the Rs 5,717 cr manifest market cap (Correction 4 in the orchestrator file is resolved).
- Promoter about 74.5%, public about 25.5% [INFERENCE; matches reported holding].
- 14,300 zero-coupon OCDs (Rs 143 cr) held by DLL, convertible at par Rs 10 into up to 14.3 cr shares, redemption premium up to 16-18% IRR if unconverted [FILED FY25 AR]: **extinguished by the merger** (holder and issuer became one). Conversion was in practice blocked by the 25% minimum public shareholding rule.
- Minorities gave up about 4.7 points (about Rs 285 cr at about Rs 6,100 cr market cap) for removal of the OCD overhang and Rs 143 cr of promoter debt, plus a thin-margin business [INFERENCE].
- Dhanuka margin: FY23 PBT loss Rs 17.3 cr; FY24 about 6%; 9M FY25 about 8%; FY26 about 0 [INFERENCE from scheme financials]. CDSCO WC-0545 (21-Apr-2026) [AGENCY]; EU GMP 2016 [SECONDARY].
- Merger shares listed about 23-Sep-2026 [SECONDARY, unverified]. Lock-in NOT DISCLOSED.

---

## 3. EXPLICIT SUPERSESSIONS AND NUMBERED CORRECTIONS

Supersessions of corpus-derived views:

- **S1. Share count "does not reconcile" (orchestrator Correction 4).** SUPERSEDED: about 5.99 cr post-merger once DLL's 3.54 cr holding is cancelled. Per-share work may use 5.99 cr, subject to the post-allotment shareholding pattern.
- **S2. OCD overhang "up to 14.3 cr further shares" (orchestrator Correction 4, 02-notes-pass3).** SUPERSEDED: extinguished on merger.
- **S3. Per-kg realisations (09b line 150: oral ~Rs 1,536/kg, sterile ~Rs 1,588/kg FY25).** SUPERSEDED: off by 10x. FY25 oral Rs 15,356/kg, sterile Rs 15,883/kg; FY26 Rs 13,388 and Rs 18,520 [INFERENCE from FILED volume and value].
- **S4. "7-ACA PLI up to Rs 600 cr".** SUPERSEDED: Orchid can reach about Rs 65 cr in total at most (V2).
- **S5. Dhanuka FY26 EBITDA about −Rs 7 cr (claude.ai draft).** SUPERSEDED: erratic 0-8%, FY26 about zero (V5).
- **S6. Synmedic "independent" (Screener AI, uncited).** SUPERSEDED: Orchid holds 98% [FILED]; not consolidated.
- **S7. Debt service "from FY28".** SUPERSEDED: repayments start FY27, about Rs 40 cr (V3).

Numbered corrections logged in the claude.ai session (25 to 37):

| # | Correction |
|---|---|
| 25 | Dhanuka FY26 EBITDA: erratic 0-8%, not −Rs 7 cr |
| 26 | Half-year balance sheet carries no receivables ageing; a receivables/revenue proxy is used |
| 27 | Per-kg realisations were off by 10x (S3) |
| 28 | PLI value about Rs 65 cr max, not Rs 60-100 cr |
| 29 | Cefiderocol 25% at PBT is real [MGMT]; earlier "invented" call withdrawn |
| 30 | "Tech partner supplies Chinese makers" is management's own statement |
| 31 | Domestic share 15-20% legacy Orchid, 34% merged |
| 32 | Exblifep US deadline is 30-Sep-2026 (May call) |
| 33 | Repayments start FY27, about Rs 40 cr (S7) |
| 34 | Merger cancelled the OCDs; better for minorities than "full price" (S2) |
| 35 | Screener's uncited "Synmedic independent" accepted → reversed by 36 |
| 36 | Orchid holds 98% of Synmedic (S6) |
| 37 | "Orchid may be the only Indian 7-ACA maker" STRUCK. The corpus records a reported Aurobindo 7-ACA project of about 2,000 t/yr (09b Correction 7.1). Orchid is one of two PLI applicants, not necessarily the only domestic maker. Status of the Aurobindo project not verified live. |

Also: Covalent's Pen-G integration is through a group company (Virchow Petrochemicals), not Covalent itself [AGENCY].

---

## 4. PROMISE-VS-DELIVERY LEDGER

| Promise (when) | Outcome | Grade |
|---|---|---|
| Turnaround after IBC to profit | Profitable FY23 onward (PAT Rs 46 cr FY23, Rs 92 cr FY24, Rs 100 cr FY25) [SECONDARY, Screener data sheet of filed figures] | HIT |
| QIP Rs 392 cr (at about Rs 404) deployed into the 7-ACA project | Deployed; CWIP rising [FILED] | HIT |
| Out-license Exblifep beyond Europe | Russia signed 7-Jul-2026 [FILED] | HIT |
| Jammu plant and machinery by Dec-2024 (monitoring agency schedule) | COD now Feb-Mar 2027 | MISS |
| Jammu COD Dec-2026 (AR) → Sep-2026 (Q3 FY26) | Moved to Mar-2027 | MISS |
| Jammu cost Rs 489 cr | Rs 750 cr | MISS |
| Remaining Jammu land registered by Mar-2026 | Still pending Aug-2026 | MISS |
| Exblifep US partner "this quarter, coming quarter" (May-2026) | None announced by 28-Sep-2026 | PENDING, likely MISS (30-Sep) |
| FY27 EBITDA about 12% incl. other income (FY27 guide) | Q1 FY27 operating 4.9% | PENDING, tracking below |
| Cefiderocol commissioning Dec-2026 | Not yet due | PENDING |

**Credibility split (binding for deliberation).** Deals and the turnaround are DELIVERED. Timelines, capex cost and partner dates are MISSED repeatedly. Therefore: no Jammu revenue in a base case before the first commercial batch is printed; apply at least a two-quarter slip to management's COD in the base; no Exblifep US revenue in the base until a licence is signed; discount FY27 margin guidance by delivery (Rule B/E, trailing four quarters = Mixed to Poor).

---

## 5. SECOND-ORDER CHAINS (Rule F; five minimum)

- **Chain 1. A leveraged rival keeps oral prices down.** Covalent took debt to about 3.5x OPBDITA for Nectar [AGENCY]. [INFERENCE] A leveraged leader pushes volume to service debt, so cefixime and axetil prices stay under pressure through FY27-FY28. That is the window of Orchid's own debt service. Unsaid: management frames the oral fall as cyclical. Confirm or break: cefixime below about $120/kg; Covalent's next ICRA rationale.
- **Chain 2. Orchid's planned 7-ACA customer may become a 7-ACA maker.** About 50% of Jammu output is meant for downstream ceftriaxone sold to Aurobindo and others [MGMT]. Aurobindo has a reported 2,000 t/yr 7-ACA project [corpus]. [INFERENCE] If Aurobindo self-supplies, Orchid's largest downstream buyer turns into a competitor at the input. Unsaid: no named offtake contract. Confirm or break: Aurobindo filings on 7-ACA commissioning; any Orchid offtake agreement.
- **Chain 3. The subsidy is smaller and shorter than the headline.** PLI values captive use at the lower of the quote and actual cost, needs 90% local value, and ends FY29 [AGENCY]. [INFERENCE] After FY29, Jammu must beat Chinese 7-ACA on power, tax, freight and duty alone, with Chinese export rebates unchanged for antibiotics. Unsaid: whether the PLI claim assumes 90% local value is met. Confirm or break: first PLI disbursal in the DoP annual report.
- **Chain 4. The import price floor protects a rival's chain, not Orchid's.** MIP covers Pen-G, 6-APA and amoxicillin, not 7-ACA or GCLE, and exempts EOU and Advance Authorisation imports [AGENCY]. [INFERENCE] It helps domestic Pen-G makers (Covalent's group) and does nothing for Orchid's inputs. Confirm or break: any MIP extension to 7-ACA or cephalosporin intermediates.
- **Chain 5. Related-party supplier credit funds working capital.** Otsuka gives about 100 days of credit on about Rs 231-245 cr of purchases [FILED]; Manish Dhanuka has been an Otsuka India director since 2006 [FILED]. [INFERENCE] About Rs 60-67 cr of working capital rests on one related-party supplier's terms. Confirm or break: payables days to Otsuka in the FY26/FY27 related-party note.
- **Chain 6. Debt before revenue points to new equity.** FY28 service about Rs 130 cr against about Rs 60 cr underlying CFO [INFERENCE]. Promoter at about 74.5% is near the 75% cap, so a promoter-led rights issue has little room; a QIP or preferential is the likely route [INFERENCE]. Confirm or break: enabling resolutions at the 29-Sep-2026 AGM; Q4 FY27 funding commentary.
- **Chain 7. Thin float, new supply.** Mutual funds hold about 17% of the company, about two-thirds of the float [SECONDARY]; 4.46 cr merger shares became tradeable about 23-Sep with no disclosed lock-in [SECONDARY]. [INFERENCE] If any went to non-promoter holders, supply meets a float already owned by funds. Confirm or break: Sep-2026 shareholding pattern (about 21-Oct).

---

## 6. SECTION 6 GATE PRE-RULINGS (one entity: Orchid Pharma Ltd)

Drafts by claude.ai for the P/E base card. The operator rules on the card. Where a value is an operator input, it is marked OPERATOR INPUT with a reference frame.

| Input | Pre-ruling | Reasoning |
|---|---|---|
| Pillar 1 ROCE and route | ROCE below 10% → base PE 9x. Normalisation route: NONE for the core. | Audited ROCE never above 8.33% in FY22-FY25 [corpus B01], before the Jammu capex began drawing debt (Q3 FY26). The low ROCE predates the capex, so it is not a temporary capex trough. Trajectory smoothing needs hard evidence of recovery; none exists for the core. |
| Jammu slice (Amendment 17) | CONVERTER: 0.5 x destination ROCE + 7.5. Destination ROCE is an OPERATOR INPUT. | Reference frame: at 12% destination ROCE the converter PE is 13.5x; at 15%, 15x; at 20%, 17.5x. No filed or counterparty unit economics exist for Jammu (X2 requested). Ambiguous slices default to CONVERTER. |
| Pillar 2 cash band | Core: STRUCTURAL (operator ruling 28-Sep-2026). Band 1.00x (volatile), no growth offset. | CFO/PAT is not meaningful while PAT is near zero (FY26 PAT Rs 20.6 cr against CFO Rs 126 cr). CFO/EBITDA underlying is about 60% after removing the Rs 85 cr inventory release [INFERENCE]. Revenue fell 12% in FY26, so working capital is not growth-induced. No rating agency confirms persistent negative WC, so 0.65x is not triggered. Jammu and cefiderocol: capex-phase drag, not a WC flag; judged after COD. |
| Pillar 3 growth premium | +0x in base. Amendment 16: does NOT open in base; assessable in the bull path only. | Emerging Moat score 23 (MODEST) [corpus B07], below 25. Amendment 16 opens if projected ROCE crosses cost of capital; in the base, core ROCE does not cross it before Jammu proves cost. In the bull (Jammu cost edge proven, gross margin above 36%) it may. |
| Strategic premium | +0x on the core. Exblifep valued as an option (Amendment 18), not as a premium. | No documented pricing power; FDA record is a hygiene factor, not a franchise. Adding a premium AND an option would count the IP twice. |
| Sector cap row | Pharma / CDMO 38x. Not binding. | Any earned destination sits far below the cap. |
| Undiscovered Alpha | Not applicable. | Institutional holding well above 3% (mutual funds about 17%). |
| Earnings basis | OPERATOR DECISION. | Trailing EPS is depressed (FY26 PAT Rs 20.6 cr ≈ Rs 3.4/share on 5.99 cr) [INFERENCE] and distorted by Synmedic and merger restatement. One-year-forward EPS still precedes Jammu. The first year that reflects the thesis is FY29 (first full Jammu year after a slipped COD). Claude web notes that a forward FY29 basis discounted back is the only basis that tests the transition; trailing tests only the past. |
| Option: Exblifep US licence within hold (Amendment 18) | OPERATOR INPUT. Claude web draft: P(licence by FY28) 35%. | Reference frame: FDA-approved Feb-2024, no US partner in 31 months; management deadline missed or about to be; "advanced talks" reported repeatedly [SECONDARY]. Resolved states at exit: licensed (upfront plus milestones; Russia $178m headline as a size reference, US typically larger) or unlicensed (value near zero in the hold). |
| Option: PLI receipt | OPERATOR INPUT. Claude web draft: P(full claim met) 50%. | Maximum about Rs 65 cr total, FY28-FY29 only; depends on 90% local value and full capacity installed [AGENCY]. |
| Jammu mature revenue and margin | OPERATOR INPUT. NOT FOUND in anything claude.ai holds. | X2 extraction requested. Without it, Jammu value is provisional. Reference frame for the operator: 1,000 t/yr at a 7-ACA price that must first be sourced [NOT FOUND]; 80% in-house means most value shows as lower material cost in the core, not as separate revenue. The falsifier (material cost ≥ 63.5% of sales four quarters after COD) is the measurable test. |
| Amendment 18 option calendar | Exblifep: window to Q3 FY27 call (partner) and FY28 (first US milestone). PLI: FY28-FY29. Cefiderocol ex-India: WHO PQ, FY28 onward. | Within-hold options exit as resolved states. |
| Amendment 19 | FV path table and return-source classification required. Claude web expects DISCOUNT-CLOSER or HYBRID at best at current price, since the price already embeds Jammu success. | CMP about Rs 1,021 (28-Sep-2026) [SECONDARY, ScanX], market cap about Rs 6,100 cr on 5.99 cr shares, about 230x trailing PBT [INFERENCE]. For 25% CAGR over three years, the FY29 market cap must reach about Rs 11,900 cr; at 30x that needs about Rs 400 cr PAT against a best-ever Rs 100 cr (FY25) [INFERENCE]. Stage 11 fetches the live price. |

**Gate 0 default.** Core 29/100 [corpus stage 1]. Any verdict defaults to WATCHLIST regardless of narrative (Role 2 decision rules).

---

## 7. ENTREPRENEUR LEDGER

| Head | Evidence | Credited |
|---|---|---|
| (a) Built from what base | Bought out of IBC in 2020 (Rs 1,116 cr figure per stage 8; confirm whether plan value or lender haircut). Revenue Rs 450 cr FY21 → Rs 922 cr FY25 (about 20% CAGR); profit from FY23; borrowings Rs 3,230 cr FY19 → Rs 135 cr FY24 [FILED] | YES |
| (b) Capital raised vs deployed | QIP Rs 392 cr deployed into Jammu as stated [FILED]; capex overran Rs 489 → Rs 750 cr and is not yet earning | YES (deployed as promised; return not yet shown) |
| (c) Against-the-sector bets that worked | 7-ACA backward integration when the only other applicant (KAPL) failed; Exblifep rights bought back. Neither has worked yet | NOT CREDITED (pending) |
| (d) Skin in the game | About 74.5% promoter; pledge nil [SECONDARY, confirm from filed pattern]; restrained pay; no dividend; OCD overhang given up in the merger | YES |

Three of four heads evidenced. Per Part 2.6, CONCERN (structure) treats as TRUSTWORTHY for sizing, with the structure items as tripwires. Moot while Gate 0 core 29 defaults to WATCHLIST.

---

## 8. PROMOTER RULINGS (operator, 28-Sep-2026)

All three items are STRUCTURE concerns, not integrity findings.

- (a) 2023 minimum public shareholding breach: historic, cured. CLOSED, noted.
- (b) FDA wording gap: the company said there was no data integrity issue; the Form 483 records observations of that kind [AGENCY]. Tripwire on any repeat.
- (c) Synmedic: 98% held, Rs 22.9 cr put in during FY26, not consolidated, no reason given; family partners with negative capital; Arjun Dhanuka (whole-time director, uncapped bonus) runs it [FILED]. Tripwire. Escalates to an integrity review if funding continues without consolidation or explanation.

Other tripwires: consolidated opinion qualified again (dormant US subsidiaries); Rs 56.5 cr old payables in those subsidiaries; small audit firm at OBPL and at Dhanuka; any promoter pledge.

---

## 9. OPEN ITEMS

- Extractions X1, X2, X3 (Section 0).
- IR questions: Synmedic (why not consolidated, revenue, plan); unregistered land; Jammu product sequencing; FY27 debt funding; Q1 FY27 India/export split; succession; technology partner and country; whether the PLI claim assumes 90% local value; lock-in on merger shares.
- Live checks not yet done: Aurobindo 7-ACA project status; JKPCC consent to operate; promoter pledge from the filed shareholding pattern; the Aug-2026 transcript wording on the Exblifep US target.
- Watch dates: Exblifep deadline 30-Sep-2026; AGM 29-Sep-2026; Sep-2026 shareholding pattern about 21-Oct; Q2 FY27 results with half-year balance sheet about 14-Nov-2026; consent to operate by Jan-2027; cefiderocol commissioning Dec-2026; first 7-ACA batch Feb-Mar 2027.

---

## 10. TRACKER PROOF (paste into `companies/ORCHPHARMA.md`)

```
## TRACKER PROOF
- WRITTEN 2026-09-28 (Role 5.5, claude.ai), operator instruction "Yes, write the rows".
- COMPANIES MASTER row: Orchid Pharma (ORCHPHARMA) https://www.notion.so/3e9bb2b9d3ab81c89befecdec79e1c78
- DOWNSTREAM SIGNAL TRACKER rows (9), each linked to the master row:
  1. Exblifep US licence (Tier 1) https://www.notion.so/3e9bb2b9d3ab812492b5d1821a5ab593
  2. Core gross margin (Tier 1) https://www.notion.so/3e9bb2b9d3ab813db524e9de2f3f15cd
  3. Jammu 7-ACA build and COD (Tier 1) https://www.notion.so/3e9bb2b9d3ab811a9a15f55ae06203fc
  4. Material cost after Jammu COD, model falsifier (Tier 1) https://www.notion.so/3e9bb2b9d3ab815c8248f070cadc3c3c
  5. Cash and debt wall (Tier 1) https://www.notion.so/3e9bb2b9d3ab8178b86ad59b9780769e
  6. Shareholding and merger share supply (Tier 2) https://www.notion.so/3e9bb2b9d3ab8181bface656a3bb4ce8
  7. Cefiderocol start (Tier 2) https://www.notion.so/3e9bb2b9d3ab81c98211d6f067e9ed86
  8. Governance tripwires (Tier 2) https://www.notion.so/3e9bb2b9d3ab817eb4a6d707dfd69f8b
  9. Cefixime price and rival capacity (Tier 2) https://www.notion.so/3e9bb2b9d3ab817fa99bf5d6e4dc4ac1
- URL verification: BSE URLs not live-verified in session (stated in each row's Notes); ICRA URL verified live 28-Sep-2026.
```

---

## 11. LESSONS_ARCHIVE CLOSE-OUT (append; OPEN ACTION lines to LESSONS.md for OPEN rows)

| # | What went wrong or was corrected | Stage | File / rule | Status |
|---|---|---|---|---|
| 1 | Per-kg realisations computed 10x too low and carried into 09b | B04 | Sanity-check per-kg price against a market price reference | OPEN (prompt fix) |
| 2 | Share count flagged as unreconcilable; cancellation of the holding company's own shares was not modelled | Orchestrator / B08 | On any holding-company merger, model cancellation of the holder's shares before comparing counts | OPEN (prompt fix) |
| 3 | Uncited Screener AI claim (Synmedic independent) accepted, then reversed | claude.ai | Uncited Screener answers stay as questions; cited ones take the tier of the cited document after a spot check | CLOSED (rule adopted) |
| 4 | "Up to Rs 600 cr" PLI headline carried without the per-company, per-year ceiling | B05 | Read scheme guidelines for per-company caps before valuing any incentive | OPEN (prompt fix) |
| 5 | Scanned FY26 AR unreadable by Screener AI; only Claude Code OCR reads it | Collector | Flag scanned ARs at collection | OPEN |

*End of dossier. Where silent, the corpus governs.*
