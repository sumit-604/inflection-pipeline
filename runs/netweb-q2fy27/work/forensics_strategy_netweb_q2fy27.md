# A3 FORENSIC NOTES: NETWEB q2fy27, doctype presentation (strategy), 28-slide strategy deck

Agent: A3 forensic notes | model: claude-opus-5-5 | run date 2026-10-28
Inputs read: A1 structured (R001-R336), A1 fulltext (765 lines, all pages), A2 ledger (336 rows), Notion checklist excerpt (memory, not evidence).
Not read: source PDF, inputs/. Prior-quarter fulltext: not available (no prior NETWEB run folder). Every "vs prior quarter" test is marked not assessable.
Arithmetic marked [A3 arithmetic] is computed only from deck numbers. It is not a filed figure.

## 0. LEDGER RECONCILIATION (336 of 336 rows read at cited line)

All 336 ledger rows were read in the structured file and checked at their cited fulltext line. Values match the text layer for every row. Exceptions follow. None of them changes a value.

| Row(s) | Issue | Resolution |
|---|---|---|
| R018, R023, R029, R030, R050, R120, R166, R170 | Value sits one or two lines off the cited line (60+ at l147; 22 at l143; "23 states/204" at l181; 12,000 at l179; 204 at l266; 40+ at l489; 32.4% at l628; 23.9% at l632) | Line offset only. Values confirmed. |
| R121 | Navin Lodha "25+ years" cited at l489. It sits at l496, beside Bagla's 25+ | Line corrected to l496. Value confirmed. |
| R020/R021 (UNRECONCILED_PAIR) | l149-151: "03 ... Supercomputers listed 17 / times in the world's top 500 / supercomputers" | One claim: 3 systems, 17 list appearances in total. Not a conflict. Closed as NEUTRAL. |
| R312 (FOOTNOTE_TRUNCATED) | l643 ends "less `Other income'" | Same text as the first clause of p28 note 1 (l729). Only the margin clause is missing on p21, and p28 carries it. Definition complete by cross-reference. |
| R089/R090 (LAYOUT_ORDER_MAPPING) | R089 gives 74.2% to AI software FY26-FY30P | 96.8 to 342.9 over 4 years = 37.2% [A3 arithmetic]. That matches R090 (37.2%, l318), not R089. A1's label fails the arithmetic. See F14-f. |
| R166/R167, R170/R171 (LAYOUT_ORDER_MAPPING) | FY24/FY25 ROCE and ROE order | Fails the column and equity cross-check. Left AMBIGUOUS. See F11-b. |
| R050, R055-R058, R062-R064 (AMBIGUOUS_MAPPING) | p9 small-line values and mix shares | Left AMBIGUOUS as directed. One candidate tie-out is in F12-a, and it is labelled as a candidate. |
| R103-R114 (AMBIGUOUS_MAPPING) | p18 repeat-revenue and concentration values | Left AMBIGUOUS as directed. See F16-b. |
| R306/R307 (FOOTNOTE_UNRESOLVED) | l479 character-interleaved | Left UNRESOLVED. A candidate de-interleave is given in F16-b as a question only. |
| R024 (GARBLED) | l131-135 left-margin digits "12 / 3 / 4 / 65" | Unresolved. Probably layout decoration. Immaterial. |
| R014/R016 vs R097/R098 (DATE_MISMATCH) | 30 Sep vs 30 Jun | Left AMBIGUOUS. See F14-a. |
| R022 vs R123 (FOUNDING_YEAR_CONFLICT) | 1999 vs 1996 | See F14-b. |

ledger_reconciled_pct: 100 (336/336).

## 1. FINDINGS TABLE

| id | check | ledger row ref | line / slide | short verbatim quote | classification | forward implication |
|---|---|---|---|---|---|---|
| F6-a | F6 | R258 | l663-664, slide 22 | "Commenced R&D of / quantum simulators and" | FORWARD-SIGNAL | A new R&D line is open (quantum, plus physical AI at R256/R257). The deck gives no spend, date or revenue path. Watch for an R&D cost step-up with no revenue offset. A4: spend, headcount, first deliverable date. |
| F6-b | F6 | R176-R178, R260, R261, R314-R318 | l686, l689, l692, l699-700, slide 23 | "111,518 Mn" / "6,525 Mn" / "26,290 Mn" / "formal purchase order or contract is / yet to be issued or accepted" | FORWARD-SIGNAL | The order book of 26,290 Mn covers about 7.4 months of the H1 run-rate (42,860 Mn annualised) [A3 arithmetic]. The pipeline is 2.6x the run-rate. The deck gives no conversion rate, execution dates or L1 ageing. H2 revenue depends on conversion that the deck does not evidence. A4: L1 ageing, expected PO dates, share of order book billable in H2 FY27. |
| F6-c | F6 | R249-R259 | l709, slide 23 | "well positioned to deliver medium to long-term sustainable growth" | NEUTRAL-FACT | The deck holds no dated company commitment. The only lexicon hit with content is "Commenced". The "will be" hits are p3 boilerplate (l98, l100, l116). The deck adds nothing dated to the Role 5 promise tracker. Undated strategy intents are logged in the register. |
| F10-a | F10 | R013, R173, R232, R327, R332 | l140, l748-749, l764, l179-182 | "annualized PAT for / September'26 divided by average of September'26 & March'26 `Total Equity'" | FORWARD-SIGNAL | ROE of 31.4% averages pre-QIP Mar-26 equity (about 7,371 Mn) with post-QIP Sep-26 equity (about 20,909 Mn) [A3 arithmetic]. On Sep-26 equity alone, annualised H1 PAT of 4,440 Mn gives about 21% [A3 arithmetic]. ROE and ROCE headlines will compress mechanically in coming periods unless PAT scales with the 12,000 Mn raise. The deck states the raise (l179-182) with no share count, price or use of proceeds. Dilution check goes to A4. |
| F11-a | F11 | R011, R160, R161, R164, R165, R232, R322, R323 | l630, l634, l632, l736, l179-180 | "(0.01) (0.02)" vs FY26 "(0.44)"; "Free Cash is calculated as `Cash and cash equivalents' and non-lien cash" | AMBIGUOUS | Net cash was about 1,253 Mn at Mar-26 (0.44 x 2,848). At Sep-26 it was about 100-210 Mn (0.02 x 6,460 annualised; 0.01 x ~20,900 equity) [A3 arithmetic]. That is after a 12,000 Mn raise. So about 13,000 Mn of "Free Cash" was used or reclassified in H1. Two readings. (a) Working capital consumed it, and/or gross borrowings rose. (b) Unspent proceeds sit in instruments that the Free Cash definition excludes (liened deposits, investments). The deck cannot separate them. Lean bear. A4: gross borrowings at 30-Sep, where unspent QIP proceeds sit, and Free Cash plus investments. |
| F11-b | F11 | R166, R167, R170, R171 | l626, l628, l630, l632, l640 | "38.5%   ...   37.5%  38.6%" (l626) / "32.4%" (l628) | AMBIGUOUS | A1 reads ROCE 32.4%, 38.5%, 37.5%, 38.6% and ROE 23.9%, 29.4%, 32.9%, 31.4%: a smooth climb. Two checks fail that order. (1) Columns: 32.4% sits at the FY25 tick (col 75) and 38.5% sits left of the FY24 tick. (2) Equity implied by the net-debt ratios (Mar-24 ~4,229; Mar-25 ~5,232; Mar-26 ~7,371 Mn) gives FY25 ROE of about 24%, not 29.4%. FY26 ties at 32.7% vs 32.9% shown [A3 arithmetic]. The chart may show an FY25 return dip that the extraction smooths away. Not resolved. A4: confirm FY24/FY25 ROCE and ROE. |
| F12-a | F12 | R047-R058, R062-R064 | l250, l261, l263, l265, l268 | "1.0% 2.65%" / "498 568" / "Software services, spares and others" | AMBIGUOUS | A proxy: product-line revenue. The deck shows no segment assets or liabilities. Labels stay AMBIGUOUS. A candidate tie-out: the H1 FY27 residual after HPC, Private Cloud and AI is 1,057 Mn, and 204 + 285 + 568 = 1,057 exactly [A3 arithmetic]. That would make software/services 568 Mn = 2.65% of H1 revenue, against 1,232 Mn in FY26 (annualised H1 1,136, down). If confirmed, Notion checklist #5 is below even its red line (flat at 4%). The stickiness line would then be shrinking while AI hardware is 59.9% of H1 (l257). A4: confirm the software/services value and share per period. |
| F14-a | F14 | R014, R016, R097, R098, R267, R284 | l146, l428, l442 | "As of 3T0toh bSeept'26   128  R&D Team Strength" vs "*As of 30th June 2026" | AMBIGUOUS | The same 128 R&D staff and 18 patents carry two as-of dates. The p5 date string is interleaved with a hidden "To be" fragment (see F14-g). The p16 date is clean. Either R&D headcount did not change across a quarter of 2x+ revenue growth, or p5 re-dated a stale figure. A4: R&D headcount at 30-Sep-26. |
| F14-b | F14 | R022, R123, R185, R268, R096 | l143, l488, l19, l378 | "Established in 1999" vs "Founded Netweb Technologies in 1996"; "26 Years of Domain" | NEUTRAL-FACT | The CIN (l19, "...HR1999PLC...") supports 1999 as the incorporation year. 1996 is probably a predecessor date. "26 Years" fits neither date at Oct-2026 (27 years from 1999; 30 from 1996) [A3 arithmetic]. It reads as a carry-over from a 2025 deck. Part of a pattern of unrefreshed text (F14-a, F14-g). |
| F14-c | F14 | R326, R329-R332, R180 | l744-745, l756, l764 | "for September'26 quarter as multiplied by 183 days" vs "multiplying the relevant H1 FY27 ... by 2" | NEUTRAL-FACT | Notes 8 and 11-13 say "quarter" but use 183 days, a half-year. Note 14 says H1 x 2. The ratios are H1-based. Drafting error only. Any WC-day figure quoted elsewhere on this basis is half-year-based. |
| F14-d | F14 | R035-R058, R136-R139 | l251, l256, l265, l261, l263, l574 | "11,490" vs p9 offering values | AMBIGUOUS | Across the four periods, the 12 small-line p9 values (HPS, data centre, software) total 5,768 Mn. The residual that p21 operating income implies is 5,825 Mn: a 57 Mn shortfall under any mapping [A3 arithmetic]. FY24 and H1 FY27 tie exactly, and FY26 ties within 1 Mn, under layout order. So the gap sits in FY25: the six lines total 11,432 vs 11,490. Small (0.5%), but the two slides disagree. A4: FY25 offering split. |
| F14-e | F14 | R230, R313, R308-R312, R319-R332, R139, R006 | l73, l105, l558, l642-643, l729-764 | "OR ITS SUBSIDIARY (TOGETHER"; "Operating Income (INR Mns)" | NEUTRAL-FACT | The deck never says whether its figures are consolidated or standalone, though the disclaimer names a subsidiary. The same 21,430 Mn is labelled "Revenue from Operations" (p5) and "Operating Income" (p21). p21 notes 1-4 number differently from p28 notes 1-14 (ROCE is note 1 on p21, note 10 on p28). The p21 notes give only the full-year method, though the H1 column is annualised. Each is minor. Together they are a governance data point. |
| F14-f | F14 | R089, R090, R091-R094 | l318, l320, l324 | "37.2%#  ...  119.6%-137.8%#" / "74.2%#" / "0.07  0.24  4.00-5.50" | NEUTRAL-FACT | Third-party (1Lattice) market data. The DC-capacity CAGRs do not tie to the GW values printed beside them: 0.07 to 0.24 is about 85% (shown 74.2%), and 0.24 to 4.00-5.50 is about 102-119% (shown 119.6-137.8%) [A3 arithmetic]. The A1 label for R089 is corrected in section 0. Market sizing only, so no thesis input changes. |
| F14-g | F14 | R024, R014, R267 | l131, l146, l248, l328, l343, l356 | "FiTnoanbceial"; "3T0toh bSeept'26"; "oTffoeribnges"; "tThoe nbeext" | NEUTRAL-FACT | The text layer shows a hidden "To be" fragment interleaved on slides 5, 9, 12 and 13. On slide 5 it overlays the "H1 FY27 Financial Metrics" header and the as-of date. This is probably a leftover placeholder layer. It lowers the weight of the p5 date in F14-a. A separate stray "c" layer appears on slides 13-14 (l349, l387). Immaterial. |
| F16-a | F16 | R320, R324-R326, R329-R331 | l732, l740-762, slide 28 | "11. Receivable Days" / "12. Inventory Days" / "7. Net Current Assets" | AMBIGUOUS | Annexure II defines PBT margin, Net Fixed Assets, Net Current Assets, GFA turnover and receivable, inventory and payable days. None of these appear on any of the 28 slides. The definitions have no slide that uses them, which suggests the template once showed these metrics or a companion deck does. A prior deck is not available, so a true drop is not assessable. The omission falls in the quarter where Notion memory records inventory rising from 805 to 1,931 Cr. Lean bear. A4: where are the WC days for 30-Sep-26, and why are they not in this deck? |
| F16-b | F16 | R103-R116, R306, R307 | l456, l459-465, l469-473, l479 | "reflecting limited customer / concentration" beside 12 unmapped values 50.3%-94.4% | AMBIGUOUS | The slide frames concentration through top-10 pool churn ("25 Customers featured in the top 10 customer pool"), not revenue share. That is a reframe. The 8 concentration values (whatever their mapping) run from 50.3% up to 85.2%. The asterisk footnote that defines the measure is garbled (l479). A candidate de-interleave (unverified) reads "As a % of revenue from operations excludes other operating revenue" plus a "CAGR FY20-FY24" note with no visible marker, which would be a stale carry-over. Notion checklist #6 red is "top 10 sustained above 70%". The headline read on Notion (85.2/76.5) is memory, not evidence here. A4: top-10 and top-5 share for each period, and the footnote text. |
| F16-c | F16 | R099-R102, R119 | l458, l475 | "New Customers 171  147  131  49" / "498 New customers onboarded from FY24 to H1FY27" | FORWARD-SIGNAL | The four values sum to 498, so they are the four periods (FY24, FY25, FY26, H1 FY27 in layout order). Onboarding falls each year: 171, 147, 131, then 49 in H1 (about 98 annualised) [A3 arithmetic]. New-customer acquisition is slowing while revenue concentrates in AI systems. This points to rising dependence on a few large orders. A4: why the onboarding is falling, and the H2 outlook. |
| F16-d | F16 | R316, R317, R318, R314 | l687-691, l704-707, l711 | "Confirmed purchase orders received from customers that are pending execution/ billing"; "#Pipeline excludes L1, L1 excludes Order Book" | AMBIGUOUS | The funnel tiers are clearly exclusive. The order book basis (gross or net of GST) is not stated. The pipeline is open-ended ("active business opportunities under pursuit"). Without a prior deck, a definition change is not assessable. A4: GST basis, and whether the NIC Blackwell order sits inside the 26,290 Mn. |
| F17-a | F17 | R322-R332, R011, R165, R232 | slide 28 notes; l179-182 | Notion #2 "CCC / WC days ... Q PPT" vs deck notes 11-13 with no figures shown | AMBIGUOUS | Silence audit run on the deck, as the orchestrator directed. Checklist #1 (CFO/PAT), #2 (CCC/WC days; the checklist names "Q PPT" as the source), inventory build, H2 CFO path, QIP use of proceeds and finance cost: no figure in this deck. 1 quarter of silence (this deck; prior not assessable). Not yet CONFIRMATORY-NEGATIVE. Test on the transcript (due about 2-Nov per Notion). |
| F17-b | F17 | R196, R201, R234, R254, R186, R230 | l171-177, l667, l73 | "Received order for India's government-owned on-prem AI cloud facility for National Informatics Centre (NIC)" / "Maintain a chip-agnostic design / philosophy" | AMBIGUOUS | Checklist #3 (Blackwell order executed by H2 FY27): the deck states the order but gives no value, delivery status or date. #9 (new sovereign order of Rs 500 Cr or more): no new rupee value disclosed. Thesis-broken #4 (Rubin): no mention of Rubin. The new strategy line "chip-agnostic" sits beside the NVIDIA OEM claim at l138-139. Taiwan WOS (Notion memory): not mentioned, and the disclaimer still says one "SUBSIDIARY" (l73). 1 quarter of silence each. A4: NIC order value and delivery schedule, Rubin inclusion, and what "chip-agnostic" means for the NVIDIA OEM status. |

## 2. CHECKLIST SCORECARD

| Check | Status | Basis |
|---|---|---|
| F1 Zero-value standing items | N.A. | The ledger has 0 ZERO_STANDING rows. The deck has no statement templates. |
| F2 Standalone vs consolidated | N.A. | The deck shows a single, unlabelled basis, with no S-vs-C pair. Basis silence is logged in F14-e. |
| F3 Shell-entity detection | N.A. | No standalone or consolidated cost lines. |
| F4 Unaudited contribution ratio | N.A. | No auditor report in a strategy deck. |
| F5 Going concern / EoM tracking | N.A. | No EoM paragraph, and no prior extract. |
| F6 Forward-commitment phrase mining | FINDING | Lexicon hit "Commenced" (l663). "will be" hits are boilerplate only. The funnel is pending conversion. No dated commitment (F6-a, b, c). |
| F7 Hedge phrase mining | PASS | Hits: "subject to change" (l93, l107, l111) and "assurance given" (l86). All are p3 safe-harbour boilerplate. No body-slide hedge on lumpiness or concentration. |
| F8 Tax forensics | N.A. | No tax lines. |
| F9 OCI forensics | N.A. | No OCI lines. |
| F10 Share count and dilution | FINDING | The 12,000 Mn raise is disclosed with no share count or EPS. Return ratios use a blended pre/post-QIP base (F10-a). |
| F11 Reserves / net worth tie-out | FINDING | Equity implied by the deck ratios ties for FY26 and H1. Net cash nearly gone after the raise (F11-a). The FY24/FY25 ROE and ROCE order fails the tie-out (F11-b). |
| F12 Segment forensics | FINDING | Proxy: product-line revenue. No segment assets or liabilities. Candidate shrinking software/services line (F12-a, AMBIGUOUS). |
| F13 Board outcome beyond results | N.A. | The cover letter is a deck intimation, not a board outcome. The board slide (p19) carries no term dates. |
| F14 Drafting inconsistencies | FINDING | Seven items (F14-a to g). Each is minor. Together they are a governance data point. |
| F15 Entity list diffs | N.A. | No consolidation list, and no prior extract. Taiwan WOS silence is logged under F17-b. |
| F16 Dropped / reframed disclosures | FINDING | Defined metrics never shown, concentration reframe, onboarding decline, funnel definition gaps (F16-a to d). Prior-deck drops are not assessable. |
| F17 Silence audit | FINDING | Run on the deck against the Notion checklist, as the orchestrator directed. The protocol treats F17 as concall-specific. Silence count is 1 quarter (F17-a, b). |

## 3. COMMITMENT REGISTER (F6)

| commitment | implied date | ref | status word |
|---|---|---|---|
| Quantum simulator / emulator R&D; engage National Quantum Mission ecosystem | none stated | l663-679, slide 22, R258 | initiated ("Commenced") |
| Physical AI R&D across hardware, agentic and interface layers; defence priority | none stated | l663-675, slide 22, R256, R257 | intent (no status word) |
| Convert L1 6,525 Mn to POs | none stated | l689, l695-700, slide 23, R177, R261 | pending ("yet to be issued or accepted") |
| Execute order book 26,290 Mn | none stated (about 7.4 months at H1 run-rate [A3 arithmetic]) | l692, l704-707, slide 23, R178, R317 | pending ("pending execution/ billing") |
| NIC on-prem AI cloud (Blackwell, IndiaAI Mission) | not stated in deck; Notion memory says H2 FY27 | l171-177, slide 6, R234 | received (execution status not stated) |
| Foundational LLM infrastructure, over 5,000 GPUs | not stated (order dated 2025) | l157-160, slide 6, R235 | received (delivery status not stated) |
| CERT-IN sovereign compute facility, 650+ units | 2026 | l164-167, slide 6, R233 | completed ("Built") |
| First capital raise since listing, 12,000 Mn | 2026 | l179-182, slide 6, R232 | completed ("Successfully raised") |
| Tier-II and DC-park push with edge/compact HCI, backed by 22 offices | none stated | l672-673, slide 22, R252 | intent |
| Tyrone Skylus indigenous private cloud to colos, CSPs, enterprises | none stated | l662-666, slide 22, R251 | intent |
| Chip-agnostic design; sovereign AI appliances and recipes | none stated | l667-674, slide 22, R254, R255 | intent |
| NSM 2.0 alignment; liquid cooling and low-footprint designs for exascale | NSM 2.0 target CY28 (policy, third party) | l661-669, l347-349, R249, R250, R246 | intent |

## 4. NOTES FOR A4
- AMBIGUOUS chart mappings (p9, p18, ROCE/ROE order) are not resolved here. The arithmetic tie-outs are candidates for management confirmation. They are not readings.
- Notion figures cited in F11-a, F16-a and F17 are memory to weigh. They are not anchored evidence from this document.

```yaml
stage: A3-forensics
company: "NETWEB"
quarter: "q2fy27"
doctype: "presentation (strategy)"
model: "claude-opus-5-5"
status: complete
forensics_path: "C:/Users/SUMIT SHARMA/repos/inflection-pipeline/.claude/worktrees/qr-netweb-q2fy27-a60c5c/runs/netweb-q2fy27/work/forensics_strategy_netweb_q2fy27.md"
ledger_reconciled_pct: 100
checklist:
  F1: N.A.
  F2: N.A.
  F3: N.A.
  F4: N.A.
  F5: N.A.
  F6: FINDING
  F7: PASS
  F8: N.A.
  F9: N.A.
  F10: FINDING
  F11: FINDING
  F12: FINDING
  F13: N.A.
  F14: FINDING
  F15: N.A.
  F16: FINDING
  F17: FINDING
findings:
  - {id: "F6-a", check: "F6", line: "l663-664 slide 22", classification: "FORWARD-SIGNAL", implication: "Quantum and physical AI R&D opened with no spend, date or revenue path; R&D cost step-up risk"}
  - {id: "F6-b", check: "F6", line: "l686, l689, l692, l699-700 slide 23", classification: "FORWARD-SIGNAL", implication: "Order book 26,290 Mn = ~7.4 months of H1 run-rate; L1 6,525 Mn unconverted; no conversion rate or dates"}
  - {id: "F6-c", check: "F6", line: "l709 slide 23", classification: "NEUTRAL-FACT", implication: "No dated company commitment in the deck; nothing new for the promise tracker"}
  - {id: "F10-a", check: "F10", line: "l140, l748-749, l764, l179-182", classification: "FORWARD-SIGNAL", implication: "ROE 31.4% on blended pre/post-QIP equity; ~21% on Sep-26 equity alone [A3 arithmetic]; returns compress unless PAT scales"}
  - {id: "F11-a", check: "F11", line: "l630, l634, l736, l179-180", classification: "AMBIGUOUS", implication: "Net cash ~1,253 Mn (Mar-26) to ~100-210 Mn (Sep-26) despite 12,000 Mn raise [A3 arithmetic]; WC or borrowings vs proceeds held outside Free Cash"}
  - {id: "F11-b", check: "F11", line: "l626, l628, l630, l632, l640", classification: "AMBIGUOUS", implication: "FY24/FY25 ROCE and ROE order fails column and implied-equity checks; chart may show an FY25 return dip"}
  - {id: "F12-a", check: "F12", line: "l250, l261, l263, l265, l268", classification: "AMBIGUOUS", implication: "Candidate: software/services 568 Mn = 2.65% of H1 vs 1,232 Mn FY26; below Notion #5 red line if confirmed"}
  - {id: "F14-a", check: "F14", line: "l146, l428, l442", classification: "AMBIGUOUS", implication: "128 R&D staff / 18 patents dated 30-Sep on p5 vs 30-Jun on p16; flat headcount or stale p5"}
  - {id: "F14-b", check: "F14", line: "l143, l488, l19, l378", classification: "NEUTRAL-FACT", implication: "1999 (CIN) vs 1996 founding; '26 Years' fits neither; unrefreshed text"}
  - {id: "F14-c", check: "F14", line: "l744-745, l756, l764", classification: "NEUTRAL-FACT", implication: "Notes say 'quarter' but use 183 days and H1 x2; ratios are H1-based"}
  - {id: "F14-d", check: "F14", line: "l251, l256, l265, l574", classification: "AMBIGUOUS", implication: "p9 offering values fall 57 Mn short of p21 operating income across periods, located in FY25 (11,432 vs 11,490) [A3 arithmetic]"}
  - {id: "F14-e", check: "F14", line: "l73, l558, l642-643", classification: "NEUTRAL-FACT", implication: "Basis (consolidated/standalone) unstated; revenue labels differ; dual note numbering"}
  - {id: "F14-f", check: "F14", line: "l318, l320, l324", classification: "NEUTRAL-FACT", implication: "1Lattice DC-capacity CAGRs do not tie to printed GW values; A1 R089 label corrected"}
  - {id: "F14-g", check: "F14", line: "l131, l146, l248, l328, l343, l356", classification: "NEUTRAL-FACT", implication: "Hidden 'To be' fragment on slides 5, 9, 12, 13, including the p5 as-of date"}
  - {id: "F16-a", check: "F16", line: "l732, l740-762 slide 28", classification: "AMBIGUOUS", implication: "WC days, NCA, NFA, GFA turnover defined but never shown, in the quarter of the inventory build"}
  - {id: "F16-b", check: "F16", line: "l456, l459-465, l469-473, l479", classification: "AMBIGUOUS", implication: "Concentration reframed as pool churn ('limited customer concentration') beside unmapped 50.3-94.4% values; footnote garbled"}
  - {id: "F16-c", check: "F16", line: "l458, l475", classification: "FORWARD-SIGNAL", implication: "New customers 171/147/131/49 (sum 498) declining; ~98 annualised in H1 [A3 arithmetic]"}
  - {id: "F16-d", check: "F16", line: "l687-691, l704-707, l711", classification: "AMBIGUOUS", implication: "Order book GST basis unstated; pipeline open-ended; NIC order inclusion unknown"}
  - {id: "F17-a", check: "F17", line: "slide 28 notes 11-13; l179-182", classification: "AMBIGUOUS", implication: "Silent on CFO/PAT, WC days, inventory, QIP use, finance cost; 1 quarter (deck)"}
  - {id: "F17-b", check: "F17", line: "l171-177, l667, l73", classification: "AMBIGUOUS", implication: "NIC Blackwell order no value or schedule; no Rubin; new 'chip-agnostic' line; Taiwan WOS absent; 1 quarter"}
forward_signals: ["F6-a", "F6-b", "F10-a", "F16-c"]
ambiguous: ["F11-a", "F11-b", "F12-a", "F14-a", "F14-d", "F16-a", "F16-b", "F16-d", "F17-a", "F17-b"]
commitments:
  - {commitment: "Quantum simulator/emulator R&D; NQM engagement", implied_date: "none stated", ref: "l663-679 R258", status_word: "initiated"}
  - {commitment: "Physical AI R&D, defence priority", implied_date: "none stated", ref: "l663-675 R256 R257", status_word: "intent"}
  - {commitment: "Convert L1 6,525 Mn to POs", implied_date: "none stated", ref: "l689 l695-700 R177 R261", status_word: "pending"}
  - {commitment: "Execute order book 26,290 Mn", implied_date: "none stated", ref: "l692 l704-707 R178 R317", status_word: "pending"}
  - {commitment: "NIC on-prem AI cloud, Blackwell, IndiaAI Mission", implied_date: "not stated in deck", ref: "l171-177 R234", status_word: "received"}
  - {commitment: "Foundational LLM infra, over 5,000 GPUs", implied_date: "not stated (order 2025)", ref: "l157-160 R235", status_word: "received"}
  - {commitment: "CERT-IN sovereign compute facility", implied_date: "2026", ref: "l164-167 R233", status_word: "completed"}
  - {commitment: "Capital raise 12,000 Mn", implied_date: "2026", ref: "l179-182 R232", status_word: "completed"}
  - {commitment: "Tier-II/DC-park push with edge HCI, 22 offices", implied_date: "none stated", ref: "l672-673 R252", status_word: "intent"}
  - {commitment: "Tyrone Skylus indigenous private cloud", implied_date: "none stated", ref: "l662-666 R251", status_word: "intent"}
  - {commitment: "Chip-agnostic design; sovereign AI appliances", implied_date: "none stated", ref: "l667-674 R254 R255", status_word: "intent"}
  - {commitment: "NSM 2.0 alignment; exascale liquid cooling", implied_date: "CY28 (policy target)", ref: "l661-669 l347-349 R249 R250 R246", status_word: "intent"}
gate_a3: pass
blank_checks: []
analyst_note: "Strategy deck, no statements, so most balance-sheet checks are N.A. The weight sits in the deck's own ratios. First, net cash fell to about 100-210 Mn at Sep-26 from about 1,253 Mn at Mar-26, despite a 12,000 Mn raise (F11-a). That fits Notion memory of negative H1 CFO and the inventory build. The question is whether unspent proceeds sit outside 'Free Cash' or borrowings rose. Second, the ROE headline averages pre- and post-QIP equity. On Sep-26 equity alone, ROE is about 21% (F10-a). Third, the FY24/FY25 ROCE and ROE order from A1 fails the column and equity cross-checks (F11-b). Fourth, the deck defines WC days but shows none (F16-a). It reframes concentration as pool churn (F16-b). New-customer onboarding falls every year (F16-c). Candidate software share is 2.65% (F12-a). Mappings flagged AMBIGUOUS are not resolved. The arithmetic tie-outs are candidates for A4 to put to management, not readings. F17 was run on the deck at the orchestrator's direction, so the silence counts are one quarter only."
```
