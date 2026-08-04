# STAGE 5: CONCALL ANALYSIS — AARTISURF (AARTI SURFACTANTS LIMITED)
## NO-CONCALL MODE — DEGRADED PROCEDURE

**Manifest flag:** `concalls_available: false`. No earnings call transcripts exist for
this company/run. Per the degraded procedure in prompts/05-concall-pipeline.md, this
stage substitutes:
1. AR FY2020-21 MD&A + Chairman's/MD's Message + Directors' Report (file labelled
   "Annual_Report_2022.pdf" but internally dated for FY ended 31 Mar 2021 — the
   Notice references the 3rd AGM, 10 Aug 2021, and Financial Year 2020-21. This
   document is **~5.3 years stale** relative to the 2026-08-04 run date and predates
   five subsequent fiscal years of company history.)
   Source: `runs/aartisurf-2026-08-04/inputs/annual-report/Annual_Report_2022.pdf`
2. 7th-AGM Investor Presentation, dated 23 Sep 2025, carrying FY2025 (year ended
   31 Mar 2025) headline financials.
   Source: `runs/aartisurf-2026-08-04/inputs/presentation/Investor_Presentation_1.pdf`
3. Screener annual/quarterly data sheet (FY2020-FY2026) for guidance-vs-actual
   cross-checks.
   Source: `runs/aartisurf-2026-08-04/inputs/screening/screener-Data_Sheet.csv`

There is a **~4-year documentary gap** (FY2021-FY2024) between the two narrative
sources; anything said in the FY2020-21 message that requires multi-year delivery
tracking can only be checked against the screener's numeric series, not against any
intervening management commentary (none was supplied). This gap itself is a data
point: no interim AR/annual commentary was provided to this stage to corroborate the
trajectory between the two narrative anchors.

---

## SECTION 1: GROWTH TRIGGERS & DRIVERS (from AR FY2020-21 + Inv. Pres. 2025)

### 1A. Triggers/drivers stated

| Trigger | Type | Timeframe | Confidence | Classification | Source |
|---|---|---|---|---|---|
| Hygiene/health segment demand to grow post-Covid | Volume | Near (FY22 outlook) | Planned | SECTORAL | AR FY2020-21 MD&A, "Opportunities and Outlook," p.11 |
| Rising FMCG disinfectant-segment demand | Volume | Near | Planned | SECTORAL | AR FY2020-21 MD&A p.11 |
| India's rising preference as "alternative supplier hub" (global structural driver) | Volume | Medium/Long | Aspirational | SECTORAL/REGULATORY-POLICY | AR FY2020-21 MD&A p.11 |
| Adding new customers, adding new products | Revenue | Near-Medium | Planned | VOLUME | MD's Message, "Business Outlook," p.7 |
| Cost-controlling measures to become "leaner and more agile" | Margin/Cost | Near (FY22) | Committed (tone) | COST | MD's Message p.7 |
| Capitalising on emerging opportunities via manufacturing capacity, product portfolio, R&D | Both | Medium | Planned | VOLUME/COST | AR FY2020-21 MD&A "Company Overview," p.10 |
| Global surfactants market growth: USD 42.1bn (2020) → USD 52.4bn (2025), 4.5% CAGR | SECTORAL | Long | Third-party cited (Markets and Markets Research), not a company commitment | SECTORAL | AR FY2020-21 MD&A "Global Surfactants Market," p.9 |
| Growing demand for bio-based/eco-friendly surfactants | Volume | Long | Aspirational | SECTORAL | AR FY2020-21 MD&A p.9-10 |
| Export diversification (30+ countries, Asia/Europe/Africa/Americas) | Revenue | Ongoing | Stated as existing footprint, not forward target | SECTORAL | Inv. Pres. slide 5-6 |

No numeric revenue target, margin band target, capex-with-timeline, capacity
addition figure, order book figure, commissioning date, debt-reduction target, or
formal return target appears anywhere in the AR FY2020-21 MD&A, MD's Message, or
Directors' Report sections read (pp.6-16 printed / PDF pages 6-19). This absence is
itself data: the FY2020-21 document is narrative/qualitative, not a KPI-anchored
guidance document. NOT FOUND for capex timeline, capacity addition figure, order
book, commissioning dates, debt-reduction target, formal ROE/ROCE target.

### 1B. Quantified guidance actually found

| Item | Number | Timeframe | Stated in |
|---|---|---|---|
| Final dividend recommended | ₹3.00 per equity share (cash outflow ₹2,27,53,431) | FY2020-21, payable on shareholder approval | AR FY2020-21 Directors' Report, "Dividend," p.13 |
| Sales CAGR claimed (retrospective, framed as a track-record marker, not forward guidance) | 14% CAGR in sales "over six years" | As of 2024 milestone | Inv. Pres. "Milestone" slide 4 |
| Credit ratings reaffirmed | CARE A- (Stable) long-term bank facilities; CARE BBB+ (Stable) long-term instruments | June 2025 (Care Edge Ratings) | Inv. Pres. slide 7 |

No forward revenue guidance, no forward margin-band guidance, no capex plan with
timeline, and no debt-reduction target appear in either source. This is a material
gap for a credibility-grading exercise: with almost no falsifiable forward numeric
commitment on record, the promise-vs-delivery tracker below is necessarily built
from qualitative-outlook-vs-actual-trend comparisons, which is a weaker evidentiary
base than a transcript-based quarter-over-quarter tracker would provide.

### 1C. Trigger evolution — not applicable in the transcript sense

There is only one narrative snapshot (FY2020-21) and one financial-summary snapshot
(Inv. Pres., Sep 2025, FY2025 numbers) — not three quarters of the same document
type. True quarter-over-quarter "strengthening/weakening/unchanged/dropped" tracking
is NOT POSSIBLE with these inputs. What can be checked is whether the FY2020-21
narrative's implied trajectory shows up in the FY2025 numbers 4+ years later:

- **Hygiene/FMCG demand thesis**: partially delivered — revenue did grow (₹465.77 cr
  FY21 → ₹659.09 cr FY25, screener), but margin did not follow (see 2A).
- **"Leaner and more agile," cost-controlling measures (FY22 outlook, MD's Message
  p.7)**: DROPPED/REVERSED by FY2025. EBITDA margin (standalone) fell from 10.70%
  (FY2024) to 7.56% (FY2025), a 29% relative decline (Inv. Pres. slide 6-7); PAT
  margin fell from 3.77% to 2.27% over the same year. Raw material cost as % of
  sales rose from 75.6% (FY2024: ₹445.83 cr / ₹589.86 cr) to 82.3% (FY2025: ₹542.61
  cr / ₹659.09 cr) per screener — the opposite direction from a "leaner" cost
  structure.
- **Export/global-diversification footprint touted in both documents** ("30+
  countries," Inv. Pres. slide 2 and 6): the underlying export **share** of revenue
  fell over the same period the footprint claim was repeated. AR FY2020-21
  Directors' Report (p.13) states FY2020-21 exports of ₹13,110 lakhs against
  standalone revenue of ₹46,577 lakhs = 28.2% export share — this is the same 28.2%
  cited in prior-stage context as the starting point. Inv. Pres. slide 6 shows the
  FY2025 geographical split at 20% international / 80% domestic. The "30+ countries"
  claim is repeated in both documents unchanged (breadth of footprint), while the
  substance (share of revenue from that footprint) contracted materially — a trigger
  that looks unchanged on the surface but has quietly weakened underneath. FLAG.

**Dropped/quietly-disappeared trigger**: the FY2020-21 emphasis on "efficient raw
material sourcing" as a named competitive advantage (AR MD&A, "Manufacturing
Capabilities," p.10) does not appear anywhere in the FY2025 Investor Presentation,
which drops all discussion of cost/input management and shows only headline
revenue/profit/ROE/ROCE bar charts. Given raw material cost ratio rose ~7 points of
sales over FY24-FY25, the silence on this topic in the later document (see Section
2D) is notable.

**Timeline slippage**: none can be identified in the classic sense (no dated
commitments existed to slip). The closest analogue is that the "leaner and more
agile" cost-efficiency posture promised for FY22 was never subsequently reasserted
or reported on, and margins moved the opposite way by FY2025.

---

## SECTION 2: MANAGEMENT CREDIBILITY CHECK (AR-guidance-vs-results basis)

### 2A. Promise vs delivery tracker (built from AR-guidance vs results-delivery, per degraded procedure)

| Promised in | Promise | Outcome | Explanation given |
|---|---|---|---|
| AR FY2020-21 Directors' Report, Dividend, p.13 | ₹3.00/share final dividend for FY2020-21 | ✅ Delivered — screener shows FY2021 dividend outflow of ₹2.27 cr, matching the AR's stated cash outflow of ₹2,27,53,431 (screener row "Dividend Amount," FY2021 column) | N/A — declared and consistent |
| MD's Message, "Business Outlook," p.7 (FY22 outlook: cost-controlling measures, "leaner and more agile") | Implicit margin/cost discipline going forward | ❌ Missed by FY2025 — EBITDA margin fell from 10.70% (FY2024) to 7.56% (FY2025); PAT margin fell from 3.77% to 2.27%; raw material cost/sales rose from 75.6% to 82.3% (screener; Inv. Pres. slide 6-7) | No explanation available — the FY2025 Investor Presentation gives no commentary on the margin decline; it is presented as a bare table/chart with no narrative (see 2D) |
| AR FY2020-21 MD&A, "Opportunities and Outlook," p.11 (positive long-term outlook, structural growth drivers, hygiene/FMCG demand) | Revenue growth to continue | Partial ✅ — standalone revenue grew from ₹465.77 cr (FY21) to ₹659.09 cr (FY25) to ₹859.13 cr (FY26, screener), i.e. top-line growth materialised, though FY2023→FY2024 saw a dip (₹601.29 cr → ₹589.86 cr) | Not addressed in either source document (no FY2023/FY2024 commentary supplied to this stage) |
| Inv. Pres. slide 2/6 ("30+ countries," "strong global footprint" — repeated, not a forward promise but an implied continuity claim) | Sustained/growing export diversification | ❌ Reversed — export share of revenue fell from 28.2% (FY2020-21, per AR Directors' Report exports of ₹13,110 lakhs / ₹46,577 lakhs revenue) to 20% (FY2025, per Inv. Pres. slide 6 geographical split) | Not addressed — no explanation for the export-share decline appears in either document |

**Tally: delivered 1 (dividend), partial 1 (revenue growth trajectory), missed 2
(cost/margin discipline, export-share sustenance).** This is the full set of
checkable promise-like statements identifiable across the two source documents; no
capex, capacity, debt, or formal return-target promises existed to check.

### 2B. Excuse pattern analysis

No excuse pattern can be characterized in the transcript sense (no analyst pressure,
no live Q&A exists in either source). What is observable: the FY2025 Investor
Presentation offers **zero narrative explanation** for the EBITDA margin
compression (10.70%→7.56%), the PAT margin compression (3.77%→2.27%), the ROE
collapse (11.50%→6.61%, Inv. Pres. slide 7), or the export-share decline
(28.2%→20%). It is a bare data deck — tables and bar charts with no accompanying
MD&A-style commentary, no "reasons for the decline" section, and no forward
statement about remediation. Classified as **silence** (per the 2B taxonomy: this
is neither external-blame nor honest-admission nor deflection — it is the complete
absence of any acknowledgement that a decline occurred). A genuinely transparent
deck would flag a near-30% EBITDA-margin decline explicitly; this one does not.

### 2C. Tone ratings (1-5, evidence-based; degraded-mode caveat: no analyst
interaction exists, so these ratings can only assess the written disclosure itself,
not live Q&A conduct)

| Attribute | Rating | Evidence |
|---|---|---|
| Transparency | 2/5 | FY2025 Inv. Pres. shows a near-30% EBITDA margin decline and a 43% ROE decline (11.50%→6.61%) with zero explanatory text (slides 6-8) |
| Specificity | 2/5 | AR FY2020-21 outlook language is generic ("positive," "structural growth drivers," "capitalise on opportunities") with no numeric targets; Inv. Pres. is numbers-only with no qualitative context |
| Consistency | 2/5 | "30+ countries" / global-footprint framing repeated unchanged across FY2020-21 AR and FY2025 Inv. Pres. even as the underlying export-revenue share fell by 8.2 points |
| Accountability | 1/5 | No acknowledgement anywhere in the FY2025 document of the margin/ROE decline versus FY2024, let alone versus the FY2020-21 cost-discipline framing |
| Defensiveness | N/A | Cannot be assessed — no analyst pressure exists in either source to react to |
| Over-promotion | 3/5 | Milestone slide highlights "14% CAGR in sales over six years" and credit-rating reaffirmations while the same deck's own tables show FY2025 margin and ROE both down sharply year-on-year — selective emphasis on the flattering metric |

### 2D. What they are NOT saying

- No commentary anywhere on the raw-material cost escalation (75.6%→82.3% of sales,
  FY2024→FY2025, screener) that is the arithmetic driver of the margin collapse.
  Given the AR FY2020-21 named "efficient raw material sourcing" as a competitive
  advantage (p.10), its complete disappearance from the FY2025 deck alongside the
  cost blowout is a likely-deliberate omission.
- No commentary on the export-share reversal (28.2%→20%) despite repeating the
  "30+ countries" footprint claim unchanged.
- No commentary on receivables/payables/working-capital dynamics. Screener shows
  "Other Liabilities" (a proxy including payables) rising from ₹104.99 cr (FY2024)
  to ₹134.15 cr (FY2025), +27.8%, well ahead of the 12% revenue growth, while cash
  from operating activity fell from ₹51.96 cr (FY2024) to ₹11.14 cr (FY2025) — a
  cash-conversion deterioration consistent with the FLAG-CASH raised in prior
  pipeline stages. Neither source document addresses this.
- No capex, capacity, or debt-reduction commentary at all in either document,
  despite Capital Work in Progress roughly tripling from ₹7.64 cr (FY2024) to
  ₹14.65 cr (FY2025) to ₹41.03 cr (FY2026, screener) — a capacity build-out is
  apparently underway with no public narrative accompanying it in the sources
  available to this stage.
- No discussion of customer concentration, competitor names, or pricing
  environment in the FY2025 Inv. Pres. (it is purely a financial-results deck).

### 2E. Repeated question tracker

**NOT APPLICABLE — no analyst Q&A source exists in no-concall mode.** There are no
transcripts, hence no repeated-question mechanism can be evaluated.
"NO REPEATED UNANSWERED QUESTIONS FOUND" (vacuously true — no questions were ever
posed in the sources available).

---

## SECTION 3: COMPETITIVE / INDUSTRY INTELLIGENCE (from AR + Inv. Pres. only)

### 3A. Competitor commentary

The AR FY2020-21 MD&A states: "Even though the industry is witnessing intensified
competition as new players continue to enter the market, your Company remains
focused on bolstering its competitive position..." (p.11). No competitor is named,
no market-share figure given. Credibility check: unverifiable from the sources
supplied; flagged for peer triangulation (see 4B).

### 3B. Industry/market intelligence

- Global surfactants market: USD 42.1bn (2020) → USD 52.4bn (2025E), 4.5% CAGR,
  sourced to Markets and Markets Research (AR FY2020-21 MD&A p.9). This is a
  third-party estimate reproduced by the company, not a management claim of
  proprietary insight, but management chose to cite it as the frame for its own
  growth thesis.
- India surfactants consumption CAGR cited at 9.6% (SLP), 8.8% (paints & coatings),
  8% (construction) through 2022 (AR MD&A p.10) — stale forecast window already
  passed as of this run date; no update available.
  regions" (AR MD&A p.9) — directional claim about developed markets leading demand for bio-based surfactants, no figures for India specifically.
- No raw-material (fatty alcohol, palm/oleochemical feedstock) price-trend
  commentary anywhere in either source, despite the RM-cost-ratio spike identified
  in Section 2D. NOT FOUND.

### 3C. Toughest questions

Not applicable — no Q&A exists in either source.

### 3D. Customer/order book signals

Inv. Pres. states "100+ Customers" (slide 2/3) as of FY2025, versus no comparable
customer-count figure disclosed in the AR FY2020-21. No concentration, win/loss, or
renewal data in either source. NOT FOUND.

---

## SECTION 4: KEY TAKEAWAYS & TRIGGERS SUMMARY

### 4A. Investment-ready trigger list (ranked by earnings impact, degraded-mode
evidentiary caveat applies to all entries — sourced from AR/Inv. Pres. only)

| Priority | Trigger | Type | Timeframe | Conviction | Confirms | Kills |
|---|---|---|---|---|---|---|
| 1 | Margin recovery toward FY2024 levels (EBITDA margin back above 9-10%) | Margin | Near-Medium | L | RM-cost ratio (currently 82.3% of sales) falls back toward 75-76% in a subsequent annual print | RM-cost ratio holds at/above 82% or rises further; no company commentary appears to explain the driver |
| 2 | Export-share recovery (currently 20%, down from 28.2%) | Volume/PRICE-MIX | Medium | L | International sales % rises in next disclosed geographical split | Export share continues to compress toward pure-domestic mix |
| 3 | Working-capital/cash-conversion normalisation (Cash from Ops fell to ₹11.14 cr FY2025 from ₹51.96 cr FY2024, screener shows a partial rebound to ₹76.65 cr in FY2026) | COST/liquidity | Near | M | FY2026 print (₹76.65 cr, screener) suggests some recovery already underway; needs confirmation via next disclosed statement | Payables/inventory stretch resumes without matching revenue growth |
| 4 | Capacity build-out (CWIP rising ₹7.64 cr→₹14.65 cr→₹41.03 cr, FY2024-FY2026, screener) | INORGANIC/VOLUME | Medium-Long | L | Any forthcoming disclosure naming the capex project, capacity addition, and commissioning date | Capex continues without any disclosed rationale or capacity-utilisation update |
| 5 | Structural hygiene/personal-care demand thesis (repeated across both documents) | SECTORAL | Long | M | Continued top-line growth (revenue already grew FY21→FY26 per screener) | Renewed revenue stagnation as seen FY2023→FY2024 |

### 4B. Questions for peer verification (formal handoff to stage 6)

The peers with available concalls are FCL (Fineotex Chemical), GALAXYSURF (Galaxy
Surfactants), and ROSSARI (Rossari Biotech).

1. **Raw-material cost trend**: AARTISURF's raw-material cost rose from 75.6% to
   82.3% of sales FY2024→FY2025 (screener), driving the EBITDA margin collapse
   (10.70%→7.56%, Inv. Pres.). Why: this is either an industry-wide fatty
   alcohol/oleochemical feedstock cost spike (in which case it is a sector risk) or
   an AARTISURF-specific pricing-power/contract-structure problem (in which case it
   is a company-specific red flag). Check peers: did FCL, GALAXYSURF, and ROSSARI
   report similar raw-material cost inflation and margin compression in FY2025
   concalls, or did they hold/expand margins over the same period?

2. **Industry growth rate cited**: AR FY2020-21 cites a global surfactants market
   CAGR of 4.5% (2020-2025, Markets and Markets Research, USD 42.1bn→USD 52.4bn)
   and India-specific consumption CAGRs of 8-9.6% for SLP/paints/construction
   end-uses through 2022. Why: these are the only industry growth figures on
   record for this company and are now stale (the India figures' forecast window
   already lapsed). Check peers: what growth rates do FCL, GALAXYSURF, and ROSSARI
   management cite currently for Indian specialty surfactants/personal-care-chemical
   demand, and do they corroborate or contradict AARTISURF's dated 2020-vintage
   figures?

3. **Export/China+1 dynamics**: AARTISURF's export share of revenue fell from
   28.2% (FY2020-21) to 20% (FY2025) even as it continues to advertise "30+
   countries" of export presence unchanged. Why: this could reflect a genuine
   industry-wide reversal of China+1/export tailwinds for Indian specialty
   chemicals, or an AARTISURF-specific loss of export customers/competitiveness.
   Check peers: have FCL, GALAXYSURF, or ROSSARI (all with meaningful export books)
   discussed a similar export-share decline, pricing pressure from Chinese
   competitors, or demand-side weakness in export markets over FY2024-FY2025?

4. **Market-share/competitive-intensity claim**: AR FY2020-21 states "the industry
   is witnessing intensified competition as new players continue to enter the
   market" (p.11) with no name or figure attached. Why: no market-share number
   exists anywhere in the sources for this stage, so this claim is entirely
   unverified. Check peers: do FCL, GALAXYSURF, or ROSSARI concalls corroborate new
   entrant pressure/capacity additions compressing industry-wide margins in
   specialty surfactants, consistent with what would explain AARTISURF's margin
   collapse as sector-wide rather than company-specific?

5. **Capex cycle**: AARTISURF's Capital Work in Progress rose from ₹7.64 cr
   (FY2024) to ₹14.65 cr (FY2025) to ₹41.03 cr (FY2026) per screener, with no
   accompanying disclosure of what is being built, timeline, or expected capacity
   addition in either source available to this stage. Why: an undisclosed,
   accelerating capex ramp with no public rationale is itself a gap that needs
   context. Check peers: are FCL, GALAXYSURF, or ROSSARI in a parallel
   capacity-expansion cycle right now (i.e., is this an industry-wide investment
   phase into which AARTISURF is spending), or does AARTISURF's ramp look
   out-of-cycle/idiosyncratic?

6. **Working-capital/cash-conversion stress**: AARTISURF's cash from operating
   activity fell sharply (₹51.96 cr FY2024 → ₹11.14 cr FY2025) alongside payables
   growing faster than revenue (+27.8% vs. +12%) and a receivables build, before a
   partial rebound in FY2026 (₹76.65 cr, screener) — consistent with the
   prior-stage FLAG-CASH. Why: this could be an industry-wide FMCG-customer
   payment-cycle stretch, or specific to AARTISURF's customer mix/credit terms.
   Check peers: have FCL, GALAXYSURF, or ROSSARI flagged similar receivable/payable
   stretch or cash-conversion deterioration with their FMCG customer base over the
   same period?

### 4C. Management quality verdict table

| Dimension | Assessment | Evidence |
|---|---|---|
| Promise specificity | Very low | No forward numeric commitments (revenue, margin, capex, capacity, debt, returns) found in either source document |
| Delivery on the one hard promise checkable (dividend) | Delivered | ₹3.00/share FY2020-21, matches screener dividend outflow |
| Delivery on qualitative cost/margin posture | Missed | EBITDA margin -29% (10.70%→7.56%), PAT margin -40% (3.77%→2.27%), RM cost ratio +6.7pts of sales, FY2024→FY2025 |
| Delivery on footprint/export narrative consistency | Missed | Export share fell 28.2%→20% while the "30+ countries" claim was repeated unchanged |
| Transparency on the decline | Very low | FY2025 Inv. Pres. presents the margin/ROE collapse with zero narrative explanation |
| Evidentiary base for this grade | Thin | Only one narrative AR (FY2020-21, ~5.3y stale) and one numbers-only deck (FY2025) exist; no interim commentary supplied to this stage |

**Overall grade: C.** Per the degraded-mode rule, the grade defaults to C and may
rise to B only on documented AR-guidance-vs-results delivery evidence; it never
reaches A in this mode. Here, the one genuinely delivered promise (the FY2020-21
dividend) is a trivial, low-conviction data point, while the two substantive
qualitative commitments that could be checked — cost/margin discipline ("leaner and
more agile") and sustained export diversification — were both **missed**, with
material, unexplained deterioration in both by FY2025. That is not evidence
sufficient to raise the grade to B; it holds at the default **C**.

### 4D. Red flags

| Flag | Severity |
|---|---|
| Zero narrative explanation in the FY2025 Investor Presentation for a ~29% EBITDA-margin decline and ~43% ROE decline versus FY2024 | High |
| Raw-material cost ratio rose 75.6%→82.3% of sales (FY2024→FY2025) with no company commentary on cause or mitigation anywhere in sources reviewed | High |
| Export share reversal (28.2%→20%) unaccompanied by any acknowledgement, while unchanged "30+ countries" messaging persists | Medium |
| Accelerating, unexplained capex/CWIP ramp (₹7.64 cr→₹41.03 cr, FY2024-FY2026) with no disclosed project, timeline, or capacity target in either source | Medium |
| Cash-conversion deterioration (Cash from Ops ₹51.96 cr→₹11.14 cr, FY2024→FY2025) coincident with payables outgrowing revenue — corroborates prior-stage FLAG-CASH | High (carried forward from prior stage) |
| No-concall mode itself: credibility grading here rests on a single, 5.3-year-stale narrative document and one numbers-only deck, not on any tested pattern of forward guidance across multiple periods | Structural (affects confidence in this stage's entire output) |

---

## Summary for downstream stages

Credibility grade C (default, no evidence sufficient to raise to B), no_concall_mode
true. The evidentiary base for this grade is unusually thin: one AR from FY2020-21
(effectively pre-listing-maturity, ~5.3 years stale) and one bare-numbers FY2025
investor deck, with a roughly four-year gap in between during which no company
commentary was supplied to this stage. Six peer-verification questions are handed to
stage 6, focused on whether the raw-material cost spike, export-share reversal,
competitive-intensity claim, capex ramp, and working-capital stress are
industry-wide phenomena (visible in FCL/GALAXYSURF/ROSSARI concalls) or specific to
AARTISURF.

```yaml
stage: B05-concall
company: "AARTISURF"
run_date: "2026-08-04"
model: claude-sonnet-5
status: complete
input_gaps:
  - "No earnings call transcripts available for this company (concalls_available: false in manifest)"
  - "AR used (Annual_Report_2022.pdf) is actually FY2020-21 (year ended 31 Mar 2021), ~5.3 years stale relative to run date"
  - "No interim AR/results commentary for FY2022-FY2024 was supplied to this stage; only two narrative snapshots exist (FY2020-21 AR, FY2025 Inv. Pres.), separated by a ~4-year documentary gap"
  - "No forward numeric guidance (revenue, margin band, capex timeline, capacity, order book, commissioning dates, debt reduction, return targets) found in either source"
  - "No raw-material price-trend, customer-concentration, competitor-name, or order-book commentary found in either source"
flags:
  - "no_concall_mode"
  - "AR-source is 5.3 years stale; degraded credibility evidence base"
  - "FLAG-CASH corroborated: cash from operating activity fell Rs51.96cr (FY2024) to Rs11.14cr (FY2025) while payables grew 27.8% vs 12% revenue growth"
quarters_analysed: []          # not applicable in no-concall mode; see credibility_basis
triggers:
  - {priority: 1, name: "Margin recovery toward FY2024 EBITDA-margin levels", type: "margin", timeframe: "near-medium", conviction: "L", confirm_signal: "raw-material cost ratio falls back toward 75-76% of sales in next annual print", kill_signal: "raw-material cost ratio holds at/above 82% or rises further with no explanation"}
  - {priority: 2, name: "Export-share recovery from 20% back toward historical 28.2%", type: "price-mix", timeframe: "medium", conviction: "L", confirm_signal: "international sales % rises in next disclosed geographical split", kill_signal: "export share continues compressing toward pure-domestic mix"}
  - {priority: 3, name: "Working-capital/cash-conversion normalisation", type: "cost", timeframe: "near", conviction: "M", confirm_signal: "cash from operating activity sustains the FY2026 rebound (Rs76.65cr per screener) in subsequent prints", kill_signal: "payables/inventory stretch resumes without matching revenue growth"}
  - {priority: 4, name: "Capacity build-out (CWIP ramp) delivering disclosed capacity addition", type: "inorganic", timeframe: "medium-long", conviction: "L", confirm_signal: "company discloses the capex project, timeline, and capacity target", kill_signal: "capex continues with no disclosed rationale or utilisation update"}
  - {priority: 5, name: "Structural hygiene/personal-care demand thesis continuing to support top-line growth", type: "sectoral", timeframe: "long", conviction: "M", confirm_signal: "continued revenue growth as seen FY2021-FY2026 per screener", kill_signal: "renewed revenue stagnation as seen FY2023 to FY2024"}
guidance:
  - {item: "Final dividend FY2020-21", number: "Rs3.00 per equity share (Rs2.2753 cr cash outflow)", timeframe: "FY2020-21", stated_in: "AR FY2020-21 Directors' Report, Dividend, p.13"}
  - {item: "Sales CAGR track-record claim (retrospective, not forward guidance)", number: "14% CAGR over six years", timeframe: "as of 2024 milestone", stated_in: "Investor Presentation, Milestone slide 4"}
  - {item: "Credit rating reaffirmation", number: "CARE A- (Stable) bank facilities; CARE BBB+ (Stable) instruments", timeframe: "June 2025", stated_in: "Investor Presentation slide 7"}
promise_delivery:
  delivered: 1
  partial: 1
  missed: 2
  rows:
    - {promised_in: "AR FY2020-21 Directors' Report p.13", promise: "Rs3.00/share final dividend for FY2020-21", outcome: "delivered", explanation: "screener dividend outflow Rs2.27cr FY2021 matches AR's stated Rs2,27,53,431"}
    - {promised_in: "MD's Message, Business Outlook, p.7 (FY22 outlook)", promise: "cost-controlling measures, become leaner and more agile", outcome: "missed", explanation: "no explanation given anywhere; EBITDA margin fell 10.70pct to 7.56pct and raw material cost ratio rose 75.6pct to 82.3pct of sales FY2024 to FY2025"}
    - {promised_in: "AR FY2020-21 MD&A, Opportunities and Outlook, p.11", promise: "positive long-term outlook, structural growth drivers sustain revenue growth", outcome: "partial", explanation: "revenue did grow FY2021 to FY2026 per screener, but with a dip FY2023 to FY2024 (Rs601.29cr to Rs589.86cr), unexplained in sources available"}
    - {promised_in: "Investor Presentation slides 2 and 6 (repeated footprint claim, not an explicit forward promise)", promise: "sustained global/export footprint across 30+ countries", outcome: "missed", explanation: "no explanation given; export share of revenue fell from 28.2pct (FY2020-21) to 20pct (FY2025) even as the footprint claim was repeated unchanged"}
excuse_pattern: "silence"      # FY2025 deck offers zero narrative on margin/ROE/export declines
repeated_evasions: []          # NO REPEATED UNANSWERED QUESTIONS FOUND - not applicable, no analyst Q&A source exists in no-concall mode
credibility_grade: "C"
credibility_basis: "Default C retained: the one delivered promise (FY2020-21 dividend) is trivial, while the two substantive qualitative commitments checkable (cost/margin discipline and sustained export diversification) were both missed with material unexplained deterioration by FY2025; evidentiary base is thin (one 5.3y-stale AR, one numbers-only FY2025 deck, ~4y documentary gap between them)."
peer_questions:
  - {question: "Did FCL, GALAXYSURF, and ROSSARI report similar raw-material cost inflation and margin compression in FY2025, matching AARTISURF's raw-material cost ratio rising 75.6pct to 82.3pct of sales and EBITDA margin falling 10.70pct to 7.56pct?", why: "Determines whether AARTISURF's margin collapse is an industry-wide feedstock cost shock or a company-specific pricing-power/contract problem", check_peers: ["FCL", "GALAXYSURF", "ROSSARI"]}
  - {question: "What growth rates do FCL, GALAXYSURF, and ROSSARI management currently cite for Indian specialty surfactants/personal-care-chemical demand, and do they corroborate AARTISURF's stale 2020-vintage figures (global surfactants 4.5pct CAGR 2020-2025; India SLP/paints/construction consumption 8-9.6pct CAGR through 2022)?", why: "AARTISURF's only industry growth figures on record are five-plus years old and their forecast window has already lapsed", check_peers: ["FCL", "GALAXYSURF", "ROSSARI"]}
  - {question: "Have FCL, GALAXYSURF, or ROSSARI discussed a similar export-share decline, Chinese competitive pricing pressure, or export-market demand weakness over FY2024-FY2025, matching AARTISURF's export share falling from 28.2pct to 20pct of revenue?", why: "Distinguishes an industry-wide China+1/export-tailwind reversal from an AARTISURF-specific loss of export customers or competitiveness", check_peers: ["FCL", "GALAXYSURF", "ROSSARI"]}
  - {question: "Do FCL, GALAXYSURF, or ROSSARI concalls corroborate new-entrant/capacity-driven competitive intensity compressing industry-wide specialty surfactant margins, consistent with AARTISURF's AR FY2020-21 claim that intensified competition from new entrants is underway?", why: "AARTISURF's competitive-intensity claim carries no name or figure and is otherwise entirely unverified from the sources available", check_peers: ["FCL", "GALAXYSURF", "ROSSARI"]}
  - {question: "Are FCL, GALAXYSURF, or ROSSARI in a parallel capacity-expansion cycle right now, i.e. is AARTISURF's accelerating Capital Work in Progress (Rs7.64cr to Rs14.65cr to Rs41.03cr, FY2024-FY2026) part of an industry-wide investment phase or an out-of-cycle, company-specific ramp?", why: "AARTISURF discloses no project name, timeline, or capacity target for this capex acceleration in either source available to this stage", check_peers: ["FCL", "GALAXYSURF", "ROSSARI"]}
  - {question: "Have FCL, GALAXYSURF, or ROSSARI flagged receivable/payable stretch or cash-conversion deterioration with their FMCG customer base over FY2024-FY2025, matching AARTISURF's operating cash flow falling from Rs51.96cr to Rs11.14cr while payables grew 27.8pct against 12pct revenue growth?", why: "Corroborates or isolates the prior-stage FLAG-CASH finding as industry-wide FMCG payment-cycle stretch versus AARTISURF-specific credit management", check_peers: ["FCL", "GALAXYSURF", "ROSSARI"]}
red_flags:
  - "Zero narrative explanation in FY2025 Investor Presentation for ~29pct EBITDA-margin decline and ~43pct ROE decline versus FY2024 (High)"
  - "Raw-material cost ratio rose 75.6pct to 82.3pct of sales FY2024 to FY2025 with no company commentary on cause or mitigation (High)"
  - "Export share reversal 28.2pct to 20pct unaccompanied by any acknowledgement, while unchanged 30+ countries messaging persists (Medium)"
  - "Accelerating, unexplained capex/CWIP ramp Rs7.64cr to Rs41.03cr FY2024-FY2026 with no disclosed project, timeline, or capacity target (Medium)"
  - "Cash-conversion deterioration (Cash from Ops Rs51.96cr to Rs11.14cr FY2024 to FY2025) coincident with payables outgrowing revenue, corroborating prior-stage FLAG-CASH (High, carried forward)"
  - "Structural: credibility grading rests on a single 5.3-year-stale narrative document and one numbers-only deck, with a ~4-year documentary gap between them (affects confidence in this entire stage's output)"
dropped_triggers:
  - "'Efficient raw material sourcing' named as a competitive advantage in AR FY2020-21 (p.10) does not appear anywhere in the FY2025 Investor Presentation, despite the raw-material cost ratio spiking over the same period"
timeline_slippages:
  - "No dated commitments existed in either source to slip in the classic sense; the closest analogue is the FY22-outlook 'leaner and more agile' cost-discipline posture (MD's Message p.7), never reasserted or reported on again, with margins moving the opposite direction by FY2025"
```
