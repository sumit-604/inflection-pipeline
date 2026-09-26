# Stage 6 — Peer Concall Verification, Trident Lifeline Ltd (TLL), 2026-09-26
# REWORK ROUND (run 2). Superseded run-1 report:
# outputs/superseded/06-peers-run1-superseded.md

Peers: Caplin Point Laboratories (CAPLIPOINT, registration-led LatAm/RoW
injectable+OSD exporter), Senores Pharmaceuticals (SENORES, recently
listed, US/emerging-market registrations plus acquired plants and CDMO),
Innova Captab (INNOVACAP, contract manufacturer transitioning into an
owned-plant, branded-generics group). All 12 transcripts confirmed on
page 1 against the manifest (issuer, quarter, call date); no mislabelled
file found. TLL files no transcripts (B05, NO-CONCALL MODE); this stage
is the run's only source of independent, peer-disclosed evidence.

## REWORK RESOLUTION (this round's mandate)

Three items from the gate-recommendation rework list (item 19) and the
run-1 Verifier D audit (12d, Findings 1-2-3), each re-read at source this
round:

**(a) SENORES Jan-2026, lines 1310-1315 — ACCEPTED, corrected.**
Re-read at source. SENORES-Concall_Jan_2026_Transcript.txt lines 1310-1315
records analyst Maitri Seth asking receivable/payable days directly, and
CFO Deval Shah answering: "I think net versus capital cycle is around 90
days, 94 days" (line 1315). Run-1 mischaracterised this transcript as
containing "no decisively quantified figure" and tagged it CITED-ONLY.
That characterisation was wrong; the quote is decisive, quantified, and
directly on-topic for Q1. Corrected below: SENORES Jan-2026 is now
SUBSTANTIVE, and Q1's CONTRADICTED verdict rests on two independent,
quantified peer anchors (CAPLIPOINT's 117-136 day band, SENORES' 90-94
day cycle) rather than one.

**(b) Coverage count arithmetic — ACCEPTED, corrected.**
Run-1's Part 3 closing line said "ten of twelve" SUBSTANTIVE against a
table that itself listed eleven SUBSTANTIVE rows and one CITED-ONLY row
(12 total); the prose undercounted by one even before resolution (a).
With (a) now reclassifying the twelfth row, the corrected count is twelve
of twelve SUBSTANTIVE, zero CITED-ONLY, zero UNUSED. See Part 3 below.

**(c) INNOVACAP 65-70% utilisation quote, call attribution — ACCEPTED,
prose fix (no anchor change).** Re-read at source. The 65-70%
utilisation/4-5 year ramp quote at lines 712-714 is in
INNOVACAP-Concall_Nov_2025_Transcript.txt (confirmed verbatim, lines
710-716), not the Aug-2026 call. The B06-peers.yaml `quote_anchor` field
already named the Nov-2025 file correctly in run 1; the defect was in
the Part 1/Q2 report prose, which named the Nov-2025 call explicitly for
an earlier point in the same paragraph, then cited "lines 712-714"
without re-stating which call, reading ambiguously as if carried forward
from the Aug-2026 sentence just before it. Fixed below: every occurrence
of the 65-70% quote in this report now states "INNOVACAP Nov-2025 call"
inline, no shared-paragraph ambiguity.

Nothing else in the run-1 report is disturbed; items outside (a)-(c) were
not re-checked per instruction.

---

## PART 1: CLAIM-BY-CLAIM VERIFICATION

### Q1. Debtor days / receivable-ageing for RoW distributors (Africa/LatAm/CIS), 208 days (TLL FY26) vs sector norm

| Field | Content |
|---|---|
| Claim | TLL's debtor days rose 116 (FY25) to 208 (FY26); B05/LBF1 asks whether this is sector-standard credit terms for these geographies or company-specific |
| Verdict | CONTRADICTED (peer evidence points to sector norm well below 208 days) |
| Peer evidence | CAPLIPOINT (a RoW/LatAm/Africa/CIS registration-led exporter, the closest comparable) discloses receivable days repeatedly and specifically: 117-118 days (CAPLIPOINT-Concall_Nov_2025_Transcript.txt, line 469, "receivables are at 117 days, I think it's 118 days as of March"); 121 days (CAPLIPOINT-Concall_Feb_2026_Transcript.txt, line 466, "Receivable stands at 121 days as against 118 days"); the CFO himself frames 120 days as the internal benchmark ("we've been promising 120 as a benchmark", line 468); 136 days in the May-2026 call, with management EXPLICITLY naming and quantifying the two causes of the jump (CAPLIPOINT-Concall_May_2026_Transcript.txt, lines 617-633): ~11 days from a non-cash FX/FCTR revaluation add-back ("but for this, my receivables would have been 125 days"), and the rest from a large, named, one-off government tender in Salvador whose collection was expected by Q2. By Aug-2026, receivables were up again (+INR46 Cr q/q) but again named and dated to a specific cause (government supplies, expected collection Q3 FY27). **SENORES gives a SECOND, independent, quantified anchor** (added this round, see Rework Resolution (a)): in its Jan-2026 call, CFO Deval Shah states directly, in answer to an analyst's receivable/payable-days question, "I think net versus capital cycle is around 90 days, 94 days" (SENORES-Concall_Jan_2026_Transcript.txt, lines 1310-1315). This is a second registration-led exporter peer, independent of CAPLIPOINT, giving a specific working-capital-cycle figure roughly half of TLL's 208 days. SENORES separately (Nov-2025 call) shows a smaller receivables jump (INR25 Cr to INR45 Cr standalone) attributed to consolidation effects, described as "well under control" (lines 1009-1013). |
| Peers silent | INNOVACAP does not disclose receivable days in isolation; it discloses a combined "working capital cycle" (Jammu-inflated) instead, so it is a partial rather than a silent data point (see Part 2A). |
| Net read | Two independent peers now anchor this verdict. CAPLIPOINT (same RoW/registration-led export model) runs receivable days in the 117-136 day band across four quarters, with every material deviation from its ~120-day internal benchmark individually named, quantified, and time-bound (FX revaluation, one named tender, one named government-supply delay). SENORES, a second and separate registration-led exporter, independently reports a 90-94 day working-capital cycle in its Jan-2026 call. TLL's 208 days sits well outside either peer's band and, per B02/B03/B05, carries no comparable line-by-line explanation in its own filings. Two peers, not one, now argue AGAINST the "sector-standard credit term" reading in LBF1: the two closest peers' bands (90-94 days and 117-136 days) sit at roughly half or less of TLL's 208 days, which strengthens the reading that the 208-day figure is company-specific deterioration (or a company-specific disclosure gap) rather than a common RoW-distributor credit norm. |

### Q2. Injectable-plant ramp timeline and margin profile vs TLL Parenterals' claimed 90% peak utilisation / 27% steady-state EBITDA margin (undated, no revenue booked)

| Field | Content |
|---|---|
| Claim | TLL Parenterals: 90% peak utilisation, 27% steady-state EBITDA margin, "revenue contribution expected from FY27 onwards", peak undated; facility carries zero booked revenue as of the Q1 FY27 results (this run date) |
| Verdict | CONTRADICTED on the pace and shape of the claim (not on directional plausibility of eventual margin) |
| Peer evidence | INNOVACAP's Jammu facility (comparable transition case: a new owned-plant complex including injectables, general formulation and cephalosporin) gives the most detailed ramp data of any peer in this set: (1) even reaching EBITDA BREAKEVEN, not peak margin, took multiple quarters after commissioning — "nearing the EBITDA breakeven" (INNOVACAP Nov-2025 call, line 771) to "we have already hit break even, actually positive in this quarter" (INNOVACAP Aug-2026 call, lines 1001-1003), i.e. roughly 3-4 quarters just to cross zero; (2) management's own long-run UTILISATION ceiling for the facility is 65-70%, reached only after 4-5 YEARS of ramp — **stated in the INNOVACAP Nov-2025 call, not the Aug-2026 call** (corrected this round, see Rework Resolution (c)): "Jammu... normally our CDMO manufacturing capabilities peaked out at a capacity utilisation of say, 65% to 70%. So going by the full potential of our Jammu plant is down the year from 4 to 5 years, we should be estimating to reach a 65% to 70% capacity utilization" (INNOVACAP-Concall_Nov_2025_Transcript.txt, lines 710-716) — well below TLL's claimed 90% peak; (3) margin only converges to the base-business level ("in line with the base business margin profile") AFTER the ramp clears breakeven (INNOVACAP Aug-2026 call, lines 992-996), i.e. the 27% steady-state figure TLL cites is, on this peer's evidence, a multi-year-out number, not a near-term one. CAPLIPOINT's own injectable-expansion commentary (May-2026 call) is more bullish in tone but still frames its steady-state economics as a multi-year, multi-phase build ("first phase... took 10-12 years already", Aug-2026 call line 462; "In the next two-to-three years, we will have 17 injectable lines", May-2026 line 117) with no single-quarter utilisation or margin figure offered for a newly commissioned line. SENORES, the peer with the most directly comparable pre-revenue posture, in fact SCALED BACK its own sterile-injectable ambition mid-plan: "we have scaled down little bit on the sterile injectable side of the business and utilized the proceeds towards expanding our capacities on oral solid" and pushed the injectable project "to later half of this year" as "a small pilot project with the reduced cost" (Aug-2026 call, lines 755-781), with ~INR100 Cr of IPO proceeds still unutilised on that line. |
| Peers silent | No peer discloses a single-quarter utilisation or margin figure for a facility at the exact stage TLL Parenterals is at (commissioned, pre-revenue). |
| Net read | Two of three relevant peers give evidence that undercuts, rather than supports, TLL's claimed pace and ceiling: INNOVACAP's own comparable facility (per its Nov-2025 call) caps out at 65-70% utilisation after 4-5 years (TLL claims 90% "peak," undated) and needed several quarters merely to reach zero EBITDA (TLL has not yet booked any revenue and already claims a 27% steady-state margin); SENORES actively de-risked and shrank its own sterile-injectable ambition rather than push through it. This is the run's single strongest peer-sourced caution on LBF3: the claimed numbers sit well ahead of what comparable owned-plant injectable ramps have actually delivered in this peer set, in both ceiling and speed. |

### Q3. EBITDA-margin uplift actually realised transitioning from loan-licence/CMO to owned-plant manufacturing, and over what timeframe

| Field | Content |
|---|---|
| Claim | TLL's central thesis: transition from asset-light exporter (loan-licence, third-party manufacturing) to an owned-plant, multi-vertical group should re-rate margins |
| Verdict | PARTIALLY VERIFIED (directionally supportive, but INNOVACAP's own numbers show a slow, single-digit-to-low-double-digit uplift, not a step change, and explicitly volume/mix-driven more than manufacturing-model-driven) |
| Peer evidence | INNOVACAP is the direct comparable (pure-play CMO historically, now building Jammu as an owned facility spanning CDMO and its own Branded Generics). Its own CFO frames the margin gain from operating leverage as incremental and gradual: "on a [material] basis, material margin is like 30% to 33%. But once the performance of the business... optimized and given a better territory, then it results in a better EBITDA margin. Because like electricity or workman cost, all are the constant... from the operational degrees, we are getting benefit. Better price realization is the second one." (Nov-2025 call, lines 590-597). Crucially, INNOVACAP's own third-party (pure CMO) volume growth is described as modest and largely mix-driven, not manufacturing-model-driven: "our volume growth is around 6% to 10%. Rest is all change in product/sales mix" (line 607), and API pricing was a headwind year-on-year ("we are even losing on the price front," line 627), meaning realised margin gains this period were NOT primarily an owned-plant story. INNOVACAP also does not (yet) disclose the CDMO vs Branded Generics revenue/margin split separately, having only just reclassified its segments from 1-Apr-2025 (Nov-2025 call, lines 843-847), which limits how cleanly the uplift can be isolated even by its own analysts. |
| Peers silent | CAPLIPOINT does not frame its own history in loan-licence-to-owned-plant terms (it has always run its own facilities); it is not a clean comparable for this specific question. |
| Net read | The one peer that has actually made a comparable transition (INNOVACAP) describes the margin uplift as real but gradual, driven as much by better territory/price realisation and product mix as by the ownership change itself, and explicitly not yet cleanly separable in its own disclosure. This tempers, without falsifying, TLL's thesis: the direction is corroborated, the magnitude and speed TLL's decks imply (peak margins of 24-30% across four new subsidiaries, undated) are not corroborated by the nearest comparable's actual delivered numbers. |

### Q4. New product registrations per year and pipeline-to-revenue conversion share within 1.5-3 years

| Field | Content |
|---|---|
| Claim | TLL: 300-400 additional registrations/year, 1.5-3 year gestation to revenue, registration pipeline "intrinsic value" ~Rs 80 Cr |
| Verdict | UNVERIFIABLE (no peer discloses a comparable annual registration count or a conversion-rate percentage) |
| Peer evidence | CAPLIPOINT discloses absolute registration STOCK, not an annual flow rate: "Today, we have 500 to 600 products actually in most of the geographies" registered (Nov-2025 call, line 1102), and market-specific detail ("Mexico. We have already filed 35+ products. We have 20 approvals along with our partners," May-2026 call, line 338), but no peer states a single "X registrations added per year" figure or a percentage-conversion rate comparable to TLL's own 1.5-3 year gestation claim. SENORES discloses a large registration BACKLOG ("we have another 942 products that are under registration... can be approved in next two to three years," Aug-2026 call, lines 1242-1246), which is at least directionally consistent with TLL's stated 1.5-3 year gestation window, but again gives no annual flow rate or conversion percentage. |
| Peers silent | INNOVACAP does not discuss registration counts or pace in any of the four calls; its growth commentary is capacity- and mix-led, not registration-led. |
| Net read | The peer set corroborates the EXISTENCE of a multi-year registration-to-revenue gestation window broadly in the 2-3 year range (SENORES) and confirms that large registration stocks (500-600+ products) are achievable at scale (CAPLIPOINT) for this business model, but no peer discloses the specific annual-flow or conversion-rate numbers needed to sanity-check TLL's 300-400/year claim or its self-assessed Rs 80 Cr "intrinsic value." This verdict cannot be upgraded past UNVERIFIABLE without inferring from silence, which the protocol disallows. |

### Q5. IV cannula / infusion set device pricing trends and competitive intensity in RoW markets, last four quarters

| Field | Content |
|---|---|
| Claim | Tests Trident Mediquip's device-margin claims (24% steady-state EBITDA) against independent pricing evidence |
| Verdict | UNVERIFIABLE |
| Peer evidence | None. No peer in this set (CAPLIPOINT, SENORES, INNOVACAP) is a device manufacturer; none of the 12 transcripts mentions IV cannulas, infusion sets, or medical-device pricing at all. A targeted search across all 12 files for "IV cannula," "infusion set," and "cannula" returned zero matches. |
| Peers silent | All three peers, on this specific topic; this was flagged in B05 as a partial cross-check only, and the peer set delivers nothing at all, not even adjacent evidence. |
| Net read | This question cannot be answered from this peer set. It requires a device-sector peer (e.g. a syringe/IV-set manufacturer), which none of the three chosen peers is. No inference is drawn from the silence; it is a structural gap in peer selection for this specific claim, not evidence either way on Trident Mediquip's device economics. |

### Q6. Industry growth-rate citations (pharma export CAGR, nutraceutical CAGR) vs TLL's AR's Frost & Sullivan / IBEF figures

| Field | Content |
|---|---|
| Claim | Tests whether TLL's AR macro citations (global pharma CAGR ~7.1% 2024-2030; India pharma exports ~USD 31.1 Bn FY26) match what comparable exporters cite themselves |
| Verdict | UNVERIFIABLE (no peer cites a directly comparable macro industry CAGR figure; peers instead cite company-specific growth targets) |
| Peer evidence | No peer transcript in this set cites the Frost & Sullivan or IBEF pharma-export or nutraceutical figures TLL's AR uses, or any comparable macro industry CAGR. What peers cite instead are COMPANY-level growth targets: SENORES targets "25%-30%" sustainable CAGR company-wide post-FY27 (Nov-2025 call, lines 609-615) and "about 30-odd percent CAGR over the next three to five years" specifically on its CDMO-CMO side (line 928); INNOVACAP frames its own multi-year target as "20% plus growth... INR1,000 crores plus" over 3 years (Nov-2025 call, lines 470-472) and reiterates "this 20% plus CAGR" as an ongoing company target (Aug-2026 call, line 754). |
| Peers silent | All three peers are silent on the specific secondary-source macro figures (Frost & Sullivan, IBEF) TLL's AR names; none engage with third-party market-sizing data on these calls at all, which is itself a mild pattern (see Part 2A). |
| Net read | The peer set gives no basis to confirm or contradict TLL's cited macro figures, because peers do not discuss macro market sizing on their own calls; they discuss their own targeted growth rates instead (20-30% company CAGR ranges), which is a different kind of number from TLL's cited 7.1% global industry CAGR and cannot be used as a proxy. UNVERIFIABLE stands; this is a genuine gap, not one resolvable by analogy. |

---

## PART 2: UNPROMPTED CROSS-READ

### 2A. DEMAND ENVIRONMENT
The peer set shows a demand picture that is real but SLOWER and more receivables-strained than TLL's own framing implies. CAPLIPOINT flags a specific, government-tender-driven receivables spike in two consecutive quarters (Salvador tender, May-2026; unnamed government supplies, Aug-2026), i.e. demand exists but converts to cash slowly and lumpily, consistent with, not contradicting, the general "semi-regulated market credit risk" backdrop TLL's own risk sections gesture at generically. INNOVACAP's Jammu facility ramp is explicitly seasonal ("quarter one, there is a seasonal impact... from Q2 onwards the normal healthy season start picking up," Aug-2026 call, lines 416-420) rather than a straight-line ramp, a nuance TLL's decks do not surface for its own subsidiaries. No peer describes an industry-wide demand boom; growth is company-specific execution (new lines, new registrations, tender wins), not a rising tide. This complicates, rather than supports, a reading of TLL's growth as riding a sector-wide wave.

### 2B. PRICING AND INPUT COSTS
INNOVACAP is explicit that API input prices were a YEAR-ON-YEAR HEADWIND even as they stabilised quarter-on-quarter ("year-on-year, if you see, then there is a negative on the prices... We are even losing on the price front," Nov-2025 call, line 623-627). This directly complicates any assumption that margin improvement in this peer group is priced-in or automatic; INNOVACAP's own margin gains in the period came from operating leverage and mix, explicitly NOT from favourable input costs. TLL's own decks do not discuss input-cost trends for its formulation business at all (B05 finding); this peer evidence is a genuine addition the main company's own disclosure does not carry.

### 2C. CAPEX CYCLE
This is an INDUSTRY-WIDE CAPACITY RACE, not a lone expander. CAPLIPOINT is mid-build on a large multi-line injectable expansion (targeting 17 lines within two-to-three years, repeated across three of its four calls) explicitly framed against a competitor with "close to 30 lines" (Aug-2026 call, lines 534-536, "the largest capacity of injectables in India... close to 30 lines"). SENORES is simultaneously expanding oral-solid capacity in the US and India while deliberately SHRINKING its injectable capex plan. INNOVACAP is mid-ramp on its own new Jammu complex (injectables, general, cephalosporin) and is still years from full utilisation. TLL, with its five new subsidiaries (TNS, Mediquip, Parenterals, Wellness, Elements) and cephalosporin ("TLL Cefa") facility "planning underway" (B05), is one more entrant into a sector where every peer in this set is simultaneously building capacity. The situation this describes is a CAPACITY RACE across the semi-regulated-to-regulated pharma export space, with capital intensity, ramp risk, and utilisation ceilings (65-70% even for a well-run peer facility after years, per INNOVACAP's Nov-2025 call) as the shared risk, not a TLL-specific one. This is a genuinely useful sector-level finding TLL's own decks, which frame its capex as a unique strategic pivot, do not surface.

### 2D. COMPETITIVE MENTIONS
No peer names or unmistakably describes Trident Lifeline, TLL, or any of its subsidiaries (TNS Pharma, Trident Mediquip, TLL Parenterals, TLL Wellness, TLL Elements) in any of the 12 transcripts. A targeted search across all files for "Trident" and "Lifeline" returned zero matches. TLL is not a large enough or visible enough player in this space to draw peer-analyst or peer-management attention on these calls. This absence is itself informative (Part 1 rules: silence may be noted when informative): it is consistent with TLL's small scale relative to these three, exchange-listed BSE SME peers on the main board, rather than with any adverse or favourable signal.

### 2E. RISKS PEERS DISCUSS THAT TLL DOES NOT
- **Utilisation ceilings below 100% even at scale and after years of ramp**: INNOVACAP names a 65-70% long-run utilisation ceiling for its own comparable owned-plant facility, achieved only after 4-5 years (Nov-2025 call, lines 710-716). TLL's decks name 80-90% "peak utilisation" figures for four different pre-revenue or barely-scaled subsidiaries with no ramp timeline attached. This gap (ceiling and speed) is a risk TLL's own disclosure never names.
- **Scaling back a stated capex plan mid-course**: SENORES explicitly de-scoped its own sterile-injectable ambition, reallocating IPO proceeds to oral solids, and frames the change as a considered risk-management decision requiring shareholder approval (Aug-2026 call, lines 755-781). TLL's decks show no equivalent optionality language anywhere in the four decks' subsidiary sections; every subsidiary target is presented as a fixed peak-revenue number with no stated fallback or de-scoping path.
- **Input-cost headwinds as a stated, quantified risk to margin**: INNOVACAP names API price deflation as an active year-on-year drag on margin (lines 623-627). TLL's AR/decks discuss margin bridges without naming input-cost trend as a risk factor at all (B05 2D finding, carried forward).
- **Seasonality in ramp-up pacing**: INNOVACAP explicitly attributes slower Q1 ramp to seasonality, expecting healthier ramp from Q2 (Aug-2026 call, lines 416-420). TLL's Parenterals/Wellness FY27 revenue-contribution claim carries no seasonality caveat.
- **A named, specific, dominant competitor scale reference**: CAPLIPOINT names an unnamed but specific competitor with "close to 30 lines" of injectable capacity as a scale benchmark for its own ambitions (Aug-2026 call, lines 534-536). TLL's decks never benchmark its own injectable ambitions (TLL Parenterals, Rs 200 Cr peak) against any named or scaled competitor capacity, leaving the claim's competitive plausibility untested in its own materials.

---

## PART 3: PEER COVERAGE MAP

| Peer | Quarter | Used how | Key contribution |
|---|---|---|---|
| CAPLIPOINT | Q2 FY26 (Nov-2025, call 06-Nov-2025) | SUBSTANTIVE | Baseline receivable days (117-118 days), registration stock (500-600 products), first competitive-scale reference (implicit, elaborated later) |
| CAPLIPOINT | Q3 FY26 (Feb-2026, call 05-Feb-2026) | SUBSTANTIVE | Receivable-days trend (121 days), injectable pipeline detail, oncology facility ramp commentary |
| CAPLIPOINT | Q4 FY26 (May-2026) | SUBSTANTIVE | Receivable-days spike explicitly explained and quantified (FX/FCTR + named Salvador tender), Mexico registration detail, injectable capacity build plan (17 lines) |
| CAPLIPOINT | Q1 FY27 (Aug-2026, call 12-Aug-2026) | SUBSTANTIVE | Second receivables spike (government supplies, quantified and dated), named competitor capacity scale ("close to 30 lines"), long injectable-build history (10-12 years phase 1) |
| SENORES | Q2 FY26 (Nov-2025, call 06-Nov-2025) | SUBSTANTIVE | Company CAGR targets (25-30%), receivables/consolidation commentary, working-capital-cycle target (80-90 days) |
| SENORES | Q3 FY26 (Jan-2026, call, filed 27-Jan-2026) | **SUBSTANTIVE (corrected this round; was CITED-ONLY in run 1)** | **90-94 day net working-capital cycle, stated directly by CFO Deval Shah in answer to an analyst's receivable/payable-days question (lines 1310-1315); a second, independent, quantified peer anchor for the Q1 debtor-days CONTRADICTED verdict** |
| SENORES | Q4 FY26 (May-2026, call 19-May-2026) | SUBSTANTIVE | Working-capital cycle ex-Apnar (104 days), Apnar US-shipment ramp detail |
| SENORES | Q1 FY27 (Aug-2026, call 03-Aug-2026, filed as "July 27, 2026" transcript header) | SUBSTANTIVE | Sterile-injectable capex de-scoping (the single most consequential peer finding for Q2), registration backlog (942 products), Apnar commercialisation detail (6 products, 30 million units) |
| INNOVACAP | Q2 FY26 (Nov-2025, call 10-Nov-2025) | SUBSTANTIVE | Jammu ramp/breakeven detail, CMO margin-uplift mechanics, API pricing headwind, volume growth quantified (6-10%), utilisation ceiling 65-70% over 4-5 years (lines 710-716) |
| INNOVACAP | Q3 FY26 (Feb-2026, call, filed 2026) | SUBSTANTIVE | Jammu "nearing break-even at EBITDA level," Jammu revenue in the quarter (Rs 89 Cr), "very nascent stage of ramping up" |
| INNOVACAP | Q4 FY26 (May-2026, call 08-May-2026) | SUBSTANTIVE | Jammu ex-facility EBITDA margin back-calculation (~18%), 3-4 year ramp horizon, EBITDA-vs-revenue growth guidance |
| INNOVACAP | Q1 FY27 (Aug-2026, call 12-Aug-2026) | SUBSTANTIVE | Margin convergence to base business only post-breakeven, breakeven itself only just reached this quarter; working-capital normalisation commentary |

**Twelve of twelve transcripts are SUBSTANTIVE (corrected this round: run 1 said "ten of twelve" against a table of eleven, both undercounts; the SENORES Jan-2026 reclassification in this round brings the true count to twelve). Zero are CITED-ONLY. Zero are UNUSED.** No peer transcript failed the page-1 issuer/quarter check.

---

## PART 4: TRIANGULATION SUMMARY

- **Claims verified**: 0 of 6 fully VERIFIED (two-or-more-peer corroboration bar not cleared by any single question; the peer set is informative but partial on every question).
- **Claims partially verified**: 1 of 6 (Q3, loan-licence-to-owned-plant margin uplift: directionally corroborated, magnitude/speed not).
- **Claims contradicted**: 2 of 6 (Q1, debtor days; Q2, injectable ramp pace/ceiling). These go to synthesis as priority items. **Q1 now rests on two independent peer anchors (CAPLIPOINT, SENORES), corrected this round; it was single-peer in run 1.**
- **Claims unverifiable**: 3 of 6 (Q4, registration pace/conversion; Q5, device pricing; Q6, macro-CAGR citation match).
- **The single most consequential contradiction**: Q2, the injectable-plant ramp claim. INNOVACAP's own comparable owned-plant facility (per its Nov-2025 call) caps out at 65-70% utilisation after 4-5 years and needed several quarters merely to reach EBITDA breakeven; TLL Parenterals claims 90% peak utilisation and a 27% steady-state EBITDA margin for a facility that has booked zero revenue to date. The gap in both ceiling (90% vs 65-70%) and pace (undated peak vs a peer's explicit multi-year path) is the largest and most testable divergence this stage finds, and it sits directly on LBF3, the run's top verification priority.
- **The single strongest independent confirmation**: none of the six questions clears the VERIFIED bar (two-or-more-peer corroboration). The closest to a genuine confirmation is Q1's directional read, now on a stronger footing than in run 1: CAPLIPOINT's disciplined ~117-136 day receivable band and SENORES' independently-stated 90-94 day cycle, taken together, corroborate (by contrast) that TLL's undisclosed, unexplained 208-day figure is atypical for this business model, which is itself a form of confirmation of the LBF1 concern, not of TLL's own framing.
- **Overall**: the peer set COMPLICATES the main company's narrative more than it supports it. On the two questions where peers gave the most concrete, comparable evidence (debtor days and injectable-plant ramp), the peer evidence sits below or slower than what TLL claims for itself, not above or faster; on the registrations and macro-citation questions, the peer set is simply silent rather than corroborating; and on the loan-licence-to-owned-plant thesis, the nearest comparable (INNOVACAP) confirms the direction but at a materially slower, more mix-driven pace than TLL's deck-stated peak-revenue and margin figures imply. No peer evidence in this set supports TLL's claimed pace or scale on any of the falsifiable questions; the strongest peer evidence available argues for treating TLL's Parenterals and receivables claims as upper-bound aspirations, consistent with B05's own independent conclusion that the AR, not the promotional deck, is this management's more reliable register.

---

## PART 5: CROSS-PEER HYPOTHESIS

**Hypothesis**: the three peers are bifurcating along a SPEED-VS-BREADTH axis in how they deploy capital into owned manufacturing, and the axis correlates with how much registration/distribution infrastructure they already had built out before committing capex — which, if it holds, argues TLL's decision to build FIVE new subsidiaries simultaneously (rather than sequencing capex behind an already-proven registration/distribution base, as CAPLIPOINT did before its injectable build, or scaling back capex when early signals were soft, as SENORES did) sits at the higher-risk end of a pattern this peer set reveals but none of the three peers states explicitly.

Specifically: CAPLIPOINT, which already had ~500-600 registered products and a mature RoW distribution network before its current injectable expansion, is pushing FAST and BROAD on capex (17 lines targeted in 2-3 years) because the demand-side registration base was already proven; INNOVACAP, which had an established CMO client base before Jammu, is pushing capex more cautiously and is explicit about a 4-5 year ceiling-reaching timeline; SENORES, the most recently listed and with the least mature RoW distribution base of the three, is the one peer that ACTIVELY SCALED BACK its owned-manufacturing capex plan (sterile injectables) once early execution signals were soft, redirecting capital to a lower-risk, already-proven oral-solid capacity instead. The pattern across all three, none of whom states it this way, is that CAPEX AMBITION SCALES WITH PROVEN DEMAND-SIDE INFRASTRUCTURE, not the reverse: the peer with the most mature registration/distribution base builds fastest and broadest, and the peer with the least mature base is the one that pulled back. TLL's decks show it building five new owned-plant subsidiaries (oral solids, devices, injectables, wellness, "Elements") simultaneously, on a registration base that this run's own evidence (B05) shows is still gestating (1.5-3 year conversion) and a distribution base concentrated in four countries (Ghana, Venezuela, Kenya, Cambodia, ~60% of registered+in-process products). If the peer pattern generalises, TLL's simultaneous multi-vertical capex commitment is closer to SENORES' position (less mature demand-side base) than to CAPLIPOINT's (mature base, hence fast/broad capex justified), which would argue for a SENORES-style contingency (scale back, sequence, or pilot) rather than the "triple in three years, five subsidiaries at once" framing TLL's Aug-2026 deck presents. This is inferable only from comparing all three peers' capex posture against their respective demand-side maturity; no single peer states this trade-off, and TLL's own materials do not address it at all.

---

## INPUT GAPS CARRIED FORWARD

- No peer covers the medical-device (IV cannula/infusion set) segment; Q5 structurally unanswerable from this peer set (peer-selection gap, not a corpus gap).
- No peer cites the specific Frost & Sullivan / IBEF macro figures TLL's AR uses; peers discuss company-level CAGR targets instead, a different kind of number (Q6).
- Carried from B00/B05: TLL itself files no transcripts (NO-CONCALL MODE); this stage is the run's only source of forward-looking, non-company-authored evidence, which raises the weight this stage's findings should carry relative to a normal run.
- (Run-1 gap "SENORES Q3 FY26 (Jan-2026) transcript is CITED-ONLY" is RESOLVED this round; see Rework Resolution (a). No longer carried forward.)
