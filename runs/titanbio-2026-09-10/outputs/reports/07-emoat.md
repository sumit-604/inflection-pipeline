# STAGE 7: EMERGING MOAT SCAN — Titan Biotech Ltd (TITANBIO)
## CORRECTION RUN (supersedes the 2026-09-16 original in place)

Run date: 2026-09-16 (correction pass) | Model: claude-sonnet-5
Taxonomy note: this is the Emerging Competitive Advantages scan (22 categories
+ R1). It is NOT FTTCP. FTTCP is a separate, later synthesis inside valuation.

---

## CORRECTION LOG

Nine findings were tested against this stage's own rubric, the corrected
Stage 1 (Gate 0) output, and the underlying filings. Nothing was accepted on
trust; each was independently re-derived before acceptance or rejection.

**FINDING 1 (upstream input, category G2). CONFIRMED, corrected.**
Stage 1's corrected WC-days series (130.85 FY23, 135.39 FY24, 150.05 FY25,
127.67 FY26 adjusted) is a net decrease of only 3.18 days across four years
(130.85 − 127.67), non-monotonic — it rose 19.2 days from FY23 to FY25 before
easing — and Stage 1 itself now calls the trend "stable," stating explicitly
that no working-capital release occurred. That does not meet the category's
own test (a genuine multi-year declining trajectory): a 2.4% net change
inside a path that gave back most of a prior rise is noise, not a trend.
Independently, AR FY26's MD&A Key Financial Ratios table (p.103, a
company-disclosed ratio unaffected by Stage 1's payable-days computation)
shows Inventory Turnover improving 1.85x to 2.21x (+19.46%) and Trade
Receivables Turnover improving 8.35x to 9.90x (+18.56%) — genuine, documented,
single-year facts. But the same table shows Trade Payables Turnover Ratio
collapsing 25.52x to 17.26x (-32.37%), and the AR's own Note 45 variance
disclosure states this is "mainly due to a substantial increase in average
trade payables compared with the growth in purchases" (AR FY26 p.153
standalone / p.196 consolidated, variance note (g)). The one day-count
improvement that did occur (FY25's 150.05 down to FY26's 127.67) is therefore
a payables-stretch event — the pattern this category is meant to screen OUT,
not customer advances rising or a prepaid/subscription shift. Verdict: the
corrected series does not evidence a working-capital improvement trajectory.
**G2 rescored 0, removed from active_categories.** Arithmetic: prior raw 1
(LM) x 1.0 documented = 1.0; corrected raw 0 = 0.0. em_score recomputed:
0.5 (B2) + 1.5 (E2) + 0.0 (G2, was 1.0) = **2.0, down from 3.0.**
Classification band unaffected (<12, NO MEANINGFUL EMERGING MOAT / NONE).

**FINDING 2 (Section 6D combined_assessment). CONFIRMED, corrected.**
The prior label ("GOOD+ (backward) / NO MEANINGFUL EMERGING MOAT (forward) —
GOOD, NOT TRANSITIONING") is not one of the prompt's eight permitted labels
(EXCEPTIONAL, EXCELLENT+, HIGH POTENTIAL, GOOD+, GOOD, TURNAROUND, AVERAGE,
AVOID); it is a coined compound. Re-read prompts/07-emerging-moat-pipeline.md
Section 6D in full: it names the eight labels and gives qualitative guidance
for two cells only (a GOOD/AVERAGE backward score paired with an EXPANSION
forward score is "exactly the transition setup this operation hunts";
HIGH POTENTIAL/TURNAROUND rows need full reasoning). It does NOT supply a
complete state-to-label mapping table. That gap is real and is named here
rather than silently bridged. Using the corrected Gate 0 inputs
(classification GOOD, core 79/100, moat 14/60 MODERATE, grand total 93/160)
against the corrected em_classification (NONE, 2.0/92 — no EXPANSION or even
STRENGTHENING signal): the prompt ties elevation above the backward label
specifically to a forward EXPANSION signal, which does not exist here.
Nothing in the prompt supports moving off the backward label in either
direction (GOOD is not weak enough to invoke TURNAROUND/AVOID either).
**Corrected to GOOD** — one of the eight permitted labels, equal to the
(corrected) backward classification alone.

**FINDING 3 (active_categories). CONFIRMED, corrected.**
The field's own definition ("only Strong/Moderate rows") and the body's own
count ("Count with Strong/Moderate evidence: 1 (E2)") both exclude G2
(graded Weak), yet the YAML listed both E2 and G2 — the body was already
right, the block was not. Combined with Finding 1's rescoring of G2 to
None, active_categories now correctly contains only E2.

**FINDING 4 (optionality register scope). CONFIRMED, corrected.**
Two prior rows (FVTPL portfolio composition/related-party linkage; Peptech
PAT reconciliation) are verification items already carried in B01's own
FLAG-ASSOCIATE-RECON and input_gaps, not forward advantages — the register
is defined for advantages scored 0 or resting only on claim/inference
evidence, not for balance-sheet reconciliation questions. Both moved to this
stage's input_gaps. B2 (qualification lock-in), which rests only on 🔍
industry-structural inference and was never registered, is added.

**FINDING 5 (block schema conformance). CONFIRMED, corrected.**
Re-checked the prompt's block schema: the field list is stage, company,
run_date, model, status, input_gaps, flags, em_score, em_classification,
active_categories, evidence_mix, completionist_recount, catalysts_12m,
capex_embedded_growth_pct, optionality_register, combined_assessment,
combined_reasoning, top_moat_risks, analyst_note. data_years and fy_range
are not present. Both removed; the data-window fact (3 annual reports,
FY2024-FY2026, plus Q1FY27 for corroboration) is stated in prose only.

**FINDING 6 (evidence_mix counts). CONFIRMED, corrected.**
The prior {documented: 2, claim: 1, inference: 1} counted only the two
scored-active rows on an undisclosed basis. Corrected basis, stated
explicitly: one item per category, at the primary evidence tier assigned in
the Section 3 summary table, excluding categories marked NO EVIDENCE FOUND
with no evidence of any kind. On this basis: documented (📄) = 5 categories
(E2, G2, A3, F2, G1 — matching the five the body anchors documented evidence
in); claim (🎙️) = 0 (no one of the 22 category rows scores purely on a
management claim; the health-supplement claim is a Section 1A/F2 narrative
fact, not a category row); inference (🔍) = 1 (B2). Corrected:
{documented: 5, claim: 0, inference: 1}.

**FINDING 7 (catalysts_12m evidence taxonomy). CONFIRMED, corrected.**
Two rows carried "DOCUMENTED (pending)" for events that have not occurred
(AR FY27 naming the health-supplement product; AR FY27 disclosing FVTPL
portfolio composition). Corrected label: "SCHEDULED, NOT YET DOCUMENTED" —
plain that the event is an announced/expected filing date, not evidence that
exists today.

**FINDING 8 (Section 3 recount prose). CONFIRMED, corrected.**
The recount sentence read "...2 categories carry documented ADVERSE evidence
(A3, F2, G1 — three categories)", an internal contradiction against its own
parenthetical and against the block, which correctly said three. Corrected
to state three consistently, and folded into the Finding-1 rewrite of the
same paragraph (G2 is now a fourth, separately-labelled non-qualifying
category, not a fourth "adverse" one).

**FINDING 9 (Section 2C fixed-asset-turnover basis). CONFIRMED, corrected.**
Section 2C used 206.19/51.34 = 4.02x, both standalone reported figures (the
206.19 numerator carries the ~Rs 5.84 cr freight gross-up per B01's
FLAG-REVENUE-BASIS). Gate 0's own M3 test (01-gate0.md, "M3 Capital
Efficiency": FAT = Sales/Net Block = 200.35/61.61 = 3.25x) uses 200.35, the
like-for-like (ex-gross-up) figure B01 established as the basis for "all
growth/margin scores in this scorecard," over 61.61, the consolidated net
block (screener-data). Reconciled: adopted Gate 0's 3.25x for cross-stage
consistency, applied to the only capex figure disclosed (Rs 1.73 cr CWIP,
standalone, Note 2(b) p.124 — no consolidated CWIP breakdown exists in the
corpus; a minor entity-basis mismatch, noted not resolved). Implied
incremental revenue = 1.73 x 3.2517 = Rs 5.63 cr. As % of like-for-like
current revenue (200.35 cr, the ratio's own numerator basis): 5.63/200.35 =
2.8%. (Applying the same ratio against the reported revenue base of 206.19
cr instead gives 5.63/206.19 = 2.7% — the two bases differ by 0.1pp,
immaterial.) **capex_embedded_growth_pct corrected 3.4 → 2.8.** The
conclusion is UNAFFECTED: both 3.4% and the corrected 2.7-2.8% are trivial
against a multi-year re-rating case and both read as evidence AGAINST a
capacity-led emerging moat.

**Unchanged, carried forward exactly as before (not questioned by this audit
and not contradicted by any recomputation):** the 22-category scan
structure and scope, the E2 export finding (both the fact and its
inference-capped strength), the identification of A3/F2/G1 as documented-
adverse categories, the absent-certification finding at B2, the I1/I2 scores
(both 0 by design), Sections 1, 2A, 2B, 2D, Section 4 in full, and every
anchor not named above.

---

Inputs consumed: B01-gate0 (corrected 2026-09-16 pass: core 79/100, moat
14/60 MODERATE, grand total 93/160, classification GOOD), B05-concall
(NO-CONCALL MODE, credibility grade C, promise-delivery 3/1/3), AR
FY2024/FY2025/FY2026 (full text), Q1FY27 unaudited results (13-Aug-2026),
FY26 audited results (30-May-2026), Q2/Q3 FY26 results, 8 Reg 30
announcements. No investor presentation exists (company publishes none). No
concall transcripts exist for this company. Data window: 3 annual reports
(FY2024-FY2026), plus the Q1FY27 results filing for corroboration; per
Finding 5 this window is stated here in prose only, not as a block field.

---

## SECTION 1: FUTURE PRODUCT & REVENUE STREAM ANALYSIS

### 1A New products/services in pipeline

| Product/service | Status | Evidence type | Expected launch | Revenue potential | How different from current portfolio |
|---|---|---|---|---|---|
| Health supplement segment products | CONCEPT (3 years running) | 🎙️ MANAGEMENT CLAIM | Not stated, no date given in any of 3 ARs | Not stated | Would move from B2B biological ingredients to a consumer/nutraceutical-adjacent line |

No other product in pipeline is disclosed anywhere in the three annual reports.
The identical sentence "the Company is developing product[s] for [in] health
supplement[s]" appears in AR FY2024 (Directors' Report, Future Plans, "The
Company is developing product for health supplement"), AR FY2025 (Directors'
Report, Future Plans, verbatim identical sentence), and AR FY2026 (Directors'
Report item 8, Future Plans, expanded wording but same substance: "the Company
is developing products in the health supplement segment to diversify its
product portfolio and address the growing demand for wellness and nutrition
products"). Zero product name, zero launch date, zero revenue figure across
three annual cycles. This is a 🎙️ claim with a documented THREE-YEAR non-
delivery record (B05 promise_delivery row 4: "missed... no product, launch, or
revenue evidence after 3 annual reports").

Company memory (runs/titanbio-2026-09-10/step1-business-brief.md, weighed not
anchored) names collagen-peptide brands "Titagen, Unstergen, OXIBIL" sourced
from the company website. These names do NOT appear anywhere in the extracted
text of AR FY2024, FY2025 or FY2026 (checked by direct search). NOT FOUND in
the filed evidence base this stage is restricted to; carried to the
Optionality Register as a verification item, not scored.

### 1B Diversification direction

- Product: health supplement claim, CONCEPT stage, no evidence of committed
  capital (🎙️, see 1A).
- Customer: no evidence of new customer-segment entry beyond the existing five
  named end-markets (Pharmaceuticals, Nutraceutical, Food & Beverages,
  Bio-technology & Fermentation, Cosmetic, Veterinary & Animal Feed — AR FY26
  Note 1.1, p.117), which are stated identically across all three years. NO
  EVIDENCE FOUND of expansion beyond this set.
- Geographic: export revenue growth outpacing domestic. Overseas revenue
  Rs 8,033.20 lakh (FY26) vs Rs 5,390.28 lakh (FY25), +49.0% (AR FY26, Note 38
  Segment Reporting, p.141-142). Domestic Rs 12,585.83 lakh vs Rs 10,254.80
  lakh, +22.7%. 📄 DOCUMENTED (audited segment note). This is the single
  strongest fact in the entire scan; scored under Family E (E2) below, not
  double-counted here.
- Channel: no evidence of a new channel (direct, distributor, e-commerce).
  NO EVIDENCE FOUND.
- Vertical integration: capital deployed into two ASSOCIATE companies (Peptech
  Biosciences Ltd, 36.87%, and Titan Media Ltd, 48.44%), both promoter-family-
  controlled entities, not third-party or organic TBL diversification (AR FY26
  Note 5, AOC-1 Annexure). Peptech's investment moved from partly-paid to
  fully-paid in FY26 (Rs 1,102.52 lakh partly-paid FY25 → Rs 1,230.01 lakh
  fully-paid FY26, AR FY26 Note 5, p.127), meaning cash left TBL to fund a
  related-party call, not a TBL product line. 📄 DOCUMENTED as a capital flow;
  🔍 ANALYST INFERENCE that this is related-party diversification rather than
  company-level product diversification. Not scored as a moat (it is capital
  deployed outside the listed entity's own operations); flagged for Halt 1
  reconciliation per the existing B01/B05 associate-gap flags.

### 1C Revenue mix shift table

| | Current % (FY26) | Expected % in 3 years | Margin direction | Profitability impact |
|---|---|---|---|---|
| Domestic | 61.0% | NOT FOUND — no forward mix guidance in any filing | NOT FOUND | NOT FOUND |
| Overseas | 39.0% | NOT FOUND | NOT FOUND | NOT FOUND |
| Health supplement (new) | 0% | NOT FOUND — no product named after 3 years, cannot project a mix share | n/a | n/a |

The company discloses one reportable business segment (Ind AS 108, AR FY26
p.100) and gives no product-wise revenue split. No forward revenue-mix
guidance exists in any filing reviewed. This table cannot be built beyond the
domestic/overseas split; all forward cells are NOT FOUND, not estimated.

---

## SECTION 2: CAPACITY & CAPEX PIPELINE

### 2A Capex programme table

| Project | Rs Cr | Funding source | Status | Expected commissioning | Capacity addition | % over current |
|---|---|---|---|---|---|---|
| "Projects in progress" (CWIP, undescribed) | Rs 1.73 cr (172.73 lakh, standalone, AR FY26 Note 2(b), p.124) | Internal accruals (near debt-free, debt-equity 0.03) | In progress, no description | NOT FOUND — no commissioning date disclosed | NOT FOUND — no capacity figure disclosed for any of the four plants, any year | NOT FOUND |

No named capex project exists in any of the three annual reports. No capital
commitment note (estimated amount of contracts remaining to be executed on
capital account) is disclosed at all in AR FY2026 — searched and absent. The
CWIP ageing table shows Rs 170.46 lakh of the Rs 172.73 lakh closing balance
is "less than 1 year" old (AR FY26 p.124), i.e. routine, small, rolling
maintenance-level spend, not a named expansion project.

Gross PPE additions have DECLINED for three consecutive years (standalone,
Rs lakh): FY2024 Rs 1,948.49 → FY2025 Rs 936.88 → FY2026 Rs 740.08 (AR FY24
Note 2(a) p.120 comparative; AR FY25 Note 2(a) p.160 comparative; AR FY26 Note
2(a) p.124). 📄 DOCUMENTED. Over the same three years the quoted-debt FVTPL
investment portfolio grew from a negligible base to Rs 813.10 lakh (FY25) to
Rs 3,328.78 lakh (FY26) (AR FY26 Note 5, p.127). 📄 DOCUMENTED. The MD&A's
"build capacity and capabilities for future business growth" sentence describing
the investing outflow (AR FY26 p.104) is reused near-verbatim from AR FY24 and
AR FY25 even as the underlying spend shifted from plant to securities. This is
the capital-allocation fact the F2 test below turns on.

### 2B Utilisation trajectory per facility

NO EVIDENCE FOUND. The company discloses four manufacturing facilities by
address (AR FY26 Note 1.1, p.117: Bhiwadi Unit I, Chopanki Units II and III,
Kaharani SP-238) but publishes no installed capacity, output volume, or
utilisation percentage for any facility in any of the three years. Gate 0's
finding stands: no capacity, line description or commissioning date is
disclosed anywhere for any of the four plants.

### 2C Growth embedded in capex (CORRECTED, Finding 9 of this pass)

Total capex under execution (CWIP, undescribed) = Rs 1.73 cr (standalone,
Note 2(b), p.124 — no consolidated CWIP breakdown exists in the corpus).

Fixed-asset turnover basis reconciled: the prior version of this section used
206.19/51.34 = 4.02x, both standalone REPORTED figures, where the 206.19
numerator carries a ~Rs 5.84 cr freight gross-up not present in the FY25
comparator (B01 FLAG-REVENUE-BASIS). Gate 0's own M3 test uses 200.35/61.61 =
3.25x, where 200.35 is B01's like-for-like (ex-gross-up) revenue figure — the
basis B01 establishes for "all growth/margin scores in this scorecard" — over
61.61, the consolidated net block (screener-data). Adopting Gate 0's 3.25x for
cross-stage consistency (noting, not resolving, the minor entity-basis
mismatch between the standalone CWIP numerator and the consolidated turnover
ratio, since no consolidated CWIP figure exists):

Implied incremental revenue = Rs 1.73 cr × 3.2517 ≈ Rs 5.63 cr.
As % of like-for-like current revenue (Rs 200.35 cr, the ratio's own
numerator basis): 5.63 / 200.35 ≈ **2.8%**.
(Applying the same 3.25x ratio against the reported revenue base of Rs 206.19
cr instead gives 5.63 / 206.19 ≈ 2.7% — the two bases differ by 0.1pp,
immaterial to the conclusion.)

**capex_embedded_growth_pct ≈ 2.8%** (corrected from 3.4%; the prior figure
used a freight-gross-up-inflated turnover ratio). The conclusion is
UNAFFECTED: this is still a trivial number precisely because there is no
committed expansion programme to size, and it should still be read as
evidence AGAINST an emerging capacity-led moat, not for one. If the
FY26/Q1FY27 growth (31.8% and 27.2% YoY respectively) continues, it is
running off existing capacity and mix, not a funded expansion.

### 2D New geography or market entries

NO EVIDENCE FOUND of a named new-country entry, new distributor appointment,
or new international certification in any of the three annual reports. The
export growth (Section 1B, Family E2 below) is aggregate and undifferentiated
by country; no filing names a specific new export market opened in FY24-FY26.

---

## SECTION 3: THE 22-CATEGORY SCAN

### FAMILY A — PRODUCT & TECHNOLOGY

**A1 — Rare manufacturing capability.** No global manufacturer count, no
qualification timeline, no long-lead equipment, no stated regulatory approval
timeline is disclosed anywhere in the AR text (searched for "capacity",
"MTPA", "qualification", none found tied to a specific claim). 🔍 ANALYST
INFERENCE only: fermentation-based peptone/culture-media manufacturing has a
small global producer set (peer set includes Advanced Enzyme Technologies,
Fermenta Biotech per B00/B01 peer selection; HiMedia is a known unlisted
competitor), but Titan's own filings make no rarity claim and give no count.
**NO EVIDENCE FOUND** at the documented tier.

**A2 — Patent and IP pipeline.** Zero patent mentions anywhere in three
annual reports (searched "patent", no matches). R&D spend is Rs 27.47 lakh in
FY26 (0.13% of turnover) against Rs 17.63 lakh in FY25 (0.11%) (AR FY26,
Annexure 2, Technology Absorption, p.81) — both entirely revenue (recurring),
zero capital R&D in either year. **NO EVIDENCE FOUND.**

**A3 — Process innovation.** No yield disclosure, no unit-cost-vs-quality
data by product. The only "process" disclosures are generic energy-efficiency
steps (VFDs, LED lighting, waste-heat recovery) with an explicit statement
that "the Company has not incurred any capital expenditure towards energy
conservation equipment" during the year (AR FY26, Annexure 2, p.80-81). Stage
4's finding that gross material margin was flat FY25→FY26 (48.3%→48.1% cost
ratio) despite 31.8% reported revenue growth is direct evidence AGAINST
process-driven margin improvement: no operating leverage showed up on the
cost-of-goods line. **NO EVIDENCE FOUND** for a positive process-innovation
moat; adverse evidence noted.

**A4 — Product platform / modular architecture.** No SKU count, no launch
frequency data, no shared-architecture language. **NO EVIDENCE FOUND.**

### FAMILY B — SUPPLY CHAIN

**B1 — Backward integration and RM security.** No captive raw-material
source, no disclosed multi-year supply agreement, no captive power (only a
diesel generator for backup, AR FY26 Annexure 2, p.80-81 — explicitly NOT a
captive power plant). Raw-material cost ratio has not declined (flat at
~48%, Stage 4 finding), so there is no RM% trend evidence of backward
integration working either. **NO EVIDENCE FOUND.**

**B2 — Qualification lock-in.** This is the category the injected context
flags as worth testing properly given the regulated-customer base (pharma,
biotech fermentation, diagnostics, nutraceutical). Searched explicitly for
cGMP, ISO, NABL, WHO-GMP, USFDA, USP/Ph.Eur/BP pharmacopoeia compliance,
halal/kosher certification: **zero matches in any of the three annual
reports.** For a company selling B2B biological ingredients into pharma and
diagnostic supply chains, the complete absence of any quality-certification
disclosure is itself a notable finding, not merely a gap. No sole-source
language, no customer-funded tooling, no disclosed multi-year post-
qualification agreement exists in the text. The structural argument in the
injected context (long customer-qualification cycles create switching costs)
remains **🔍 ANALYST INFERENCE from industry structure**, not evidence from
Titan's own filings — Titan's filings do not make this case for themselves.
**NO EVIDENCE FOUND at the documented tier; the absence of certification
disclosure for this customer base is flagged as a gap, not assumed to hide a
moat.**

**B3 — Supply chain network effect.** No platform, no hub-and-spoke, no
aggregation-of-fragmented-supply language. **NO EVIDENCE FOUND.**

### FAMILY C — CUSTOMER

**C1 — Customer ecosystem / embedded relationships.** No cross-sell metric,
no wallet-share data, no ERP/workflow integration with customers (the
Microsoft Navision ERP disclosed is internal accounting software, AR FY26
Directors' Report p.72, not a customer-facing system), no AMC revenue, no
co-development disclosure. "Long-term relationships... deeper customer
relationships" (MD&A Threats section, AR FY26 p.100) is 🎙️ boilerplate with
no supporting metric. **NO EVIDENCE FOUND.**

**C2 — Customer concentration improving.** No top-5/10 customer disclosure
exists in any filing (confirmed absent per B01 input_gaps M5/M7/M8). The
export-growth fact is a geographic-diversification signal but is scored once,
under E2 below, per the CLAUDE.md rule against crediting one improvement
through two mechanisms. **NO EVIDENCE FOUND** at C2 specifically (no
customer-count or concentration-ratio data exists to test).

### FAMILY D — DATA & DIGITAL

**D1 — Proprietary data asset.** No mention of any accumulated dataset, ML
model, or replicability claim. **NO EVIDENCE FOUND.**

**D2 — Digital platform.** No customer-facing digital platform, no
transaction-volume or digital-revenue disclosure. **NO EVIDENCE FOUND.**

### FAMILY E — GEOGRAPHIC & ACCESS

**E1 — Geographic first-mover.** No first-license, first-plant-logistics,
land-bank, or "peers have not entered" claim anywhere. **NO EVIDENCE FOUND.**

**E2 — China+1 beneficiary.** Export revenue Rs 8,033.20 lakh FY26 vs
Rs 5,390.28 lakh FY25, +49.0% YoY, now 38.96% of total revenue vs domestic
+22.7% (AR FY26, Note 38 Segment Reporting, p.141-142; consistent figure
appears in Directors' Report Annexure 2, p.81: "exported goods of Rs 8,033.20
Lakhs during the year"). This is 📄 DOCUMENTED, audited, and consistent across
two independent notes in the same filing. Export growth outpacing domestic in
a regulated-customer B2B ingredient business is the fact the injected context
asked to be tested properly, not assumed either way. Tested: the filings give
**zero causal narrative** for the export acceleration — no named new
customer, no new country, no new certification, no explicit "supply-chain
shift" or China+1 language anywhere in three annual reports (B05's
peer_questions register notes the same gap: "Titan gives no demand narrative
of its own"). So the FACT of accelerating export growth is hard evidence; the
INTERPRETATION that it reflects qualification stickiness or a structural
China+1 tailwind is **🔍 ANALYST INFERENCE**, unconfirmed by the company's own
disclosure. **Strength: Moderate** (real, audited, accelerating, two-year
trend visible against FY25's Rs 5,390.28 lakh base) but **evidence-mix capped**
because the forward-durability story is inference, not documented cause. This
is the strongest single entry in the 22-category scan.

**Note on scope discipline:** the Q1FY27 revenue re-acceleration (+27.2% YoY,
OPM 21%, the best quarterly margin in eight quarters, per the 13-Aug-2026
results filing) is consistent with the export-led story continuing but is not
itself independently attributed to exports in the filing (domestic/export
split is not given at the quarterly cadence); it corroborates the FY26 trend
without adding a new documented fact.

### FAMILY F — TALENT & ORGANISATIONAL

**F1 — Talent density.** R&D headcount not disclosed. No PhD or specialist
count. No ESOP-to-technical-staff scheme found (only a generic reference to
"ESOP" inside the remuneration-policy scope list, AR FY26 p.53, and a
"stock options" cross-reference to the Board's Report with no scheme detail
located in the extracted text). All executive management (Managing Directors
Naresh Kumar Singla and Suresh Chand Singla, Whole-time Directors Raja Singla,
Udit Singla, Shivom Singla) are members of the same promoter family (AR FY26
Board composition, p.11; Reg 30, 27-Sep-2025, Annexure-B). **NO EVIDENCE
FOUND** for a talent-density moat.

**F2 — Execution moat.** This is the category the injected context and B05
substitute record most directly target. Cross-referencing the capex-
completion evidence (Section 2A above) against the B05 promise-delivery
record: 📄 DOCUMENTED adverse findings —
(i) the "build capacity and capabilities for future business growth" sentence
was carried unchanged across AR FY24 and AR FY25 into AR FY26, even as FY26
gross PPE additions fell to a three-year low (Rs 740.08 lakh) and 77% of the
Rs 32.55 cr consolidated investing outflow went into a quoted-debt FVTPL
portfolio (AR FY26 Note 5, p.127 vs Note 2(a) p.124; MD&A p.104);
(ii) the health-supplement product claim has zero delivery evidence after
three consecutive annual reports (Section 1A);
(iii) B05's cross-annual-report promise tracker: 3 delivered (all mechanical
— two dividends, one share split), 1 partial, 3 missed, credibility grade C.
There is no positive execution-moat evidence to set against this: revenue per
employee did improve (standalone revenue Rs 206.19 cr / 527 employees ≈
Rs 39.1 lakh/employee FY26 vs Rs 156.45 cr / ~458 employees ≈ Rs 34.2
lakh/employee FY25, employees per AR FY26 MD&A p.103 headcount +15.09%), but
this single ratio does not offset two documented, three-year, undelivered
substantive claims. **Scored as adverse: an execution deficit is documented,
not an execution moat.** This is not "NO EVIDENCE FOUND" — evidence exists and
it cuts against a moat forming here.

### FAMILY G — FINANCIAL & STRUCTURAL

**G1 — War chest.** Debt-equity 0.03, near debt-free (B01 core finding),
finance cost low and stable (Rs 91.39 lakh FY26 vs Rs 80.18 lakh FY25, AR FY26
MD&A p.101). But the "war chest funding future capacity" pattern the category
tests for is specifically ABSENT: capex is declining (Section 2A) while the
cash is going into a quoted-debt FVTPL portfolio whose own return fell from
7.04% to 3.64% (AR FY26 MD&A Key Ratios table, p.103, Return on Investment
line). This is a balance sheet accumulating cash with a shrinking, not
growing, capex programme — the opposite of a war chest positioned to fund
expansion. No undrawn credit line disclosure, no rating action (no rating
exists at all, per B01/company memory). **NO EVIDENCE FOUND for a positive
G1 moat; the FVTPL buildup is flagged as evidence against reinvestment
capacity, consistent with B01's analyst_note, not credited as a war chest.**

**G2 — WC improvement trajectory (CORRECTED, Finding 1 of this pass).**
B01's corrected WC-days series (130.85 FY23, 135.39 FY24, 150.05 FY25, 127.67
FY26 adjusted; corrected from a lakh-to-crore unit error, B01 CORRECTION LOG
item 1) is a net decrease of only 3.18 days across four years (130.85 −
127.67), non-monotonic — it ROSE 19.2 days from FY23 to FY25 before easing —
and B01's own corrected block_b_trend now reads "stable," explicitly stating
"no working-capital release occurred." This is not a WC-days improvement
trajectory; it is noise inside a range that has run above 45 days (the
negative-WC/float moat threshold) in all four years.
FCF still grew from Rs 18.11 cr (FY23) to Rs 22.99 cr (FY26) — a fact the
correction does not touch. Inventory turnover improved 1.85x to 2.21x
(+19.46%) and trade receivables turnover improved 8.35x to 9.90x (+18.56%),
both 📄 DOCUMENTED (AR FY26 MD&A Key Financial Ratios table, p.103), genuine
single-year facts unaffected by the payable-days computation (they are
company-disclosed ratios, not stage-computed). But the SAME table shows Trade
Payables Turnover Ratio collapsing 25.52x to 17.26x (-32.37%), and the AR's
own Note 45 variance disclosure states this is "mainly due to a substantial
increase in average trade payables compared with the growth in purchases"
(AR FY26 p.153 standalone / p.196 consolidated, variance note (g)). The one
day-count improvement that did occur (FY25's 150.05 down to FY26's 127.67) is
therefore a payables-stretch event — the pattern this category is meant to
screen OUT (customer advances rising or a prepaid/subscription shift would
count; leaning harder on suppliers does not) — not a structural change.
**Re-scored: NONE, not Weak.** The genuine turnover-ratio gains are real but
are single-year data points, not a "trajectory" (the category's own word),
and the metric that would establish a trajectory (WC days) is flat across the
window once corrected. G2 leaves the active list; carried instead as a
documented, non-qualifying finding alongside A3/F2/G1 in the completionist
recount below.

### FAMILY H — ECOSYSTEM & EXTERNAL

**H1 — Industry consolidation beneficiary.** No competitor-exit,
compliance-cost regulation, anti-dumping, or bolt-on-acquisition language
anywhere in the AR. **NO EVIDENCE FOUND.**

**H2 — Strategic partnerships.** The two associate holdings (Peptech
Biosciences 36.87%, Titan Media 48.44%) are promoter-family-controlled
entities (common directors across both, AR FY26 Board of Directors "Other
Directorships" columns, p.15-17), not third-party JVs with a global leader,
not exclusivity or inbound-licensing arrangements. Does not fit the H2 test
as written. **NO EVIDENCE FOUND.**

**H3 — ESG moat.** No renewables percentage disclosed, no rating, no SBTi, no
ZLD. The only energy-related disclosure is the generic VFD/LED/waste-heat
list (AR FY26 Annexure 2, p.80) with an explicit statement of zero capex
towards energy conservation equipment in the year. **NO EVIDENCE FOUND**; the
zero-capex admission is a documented absence, not merely a gap.

### FAMILY I — STRUCTURAL ASYMMETRIES

**I1 — Talent asymmetry.** Part (a) (unusual-capability class) not evidenced:
no named inventors (no patents exist to name inventors on), no ex-DRDO/
ex-HAL/global-major staff concentration disclosed, no remuneration-annexure
line showing a technical hire paid above sector norm — the highest-paid
individuals are the promoter-family Managing Directors and Whole-time
Directors. Part (b) (competitor cannot match pay without breaking its
economics) is therefore moot. **Score 0. NO EVIDENCE FOUND**, as expected for
most companies per the framework's design.

**I2 — Cannibalization barrier.** Applying the test to the one moat claim
that survived Section 3 (E2, export growth): what would the best-resourced
competitor have to destroy in its own business to copy Titan's export growth?
Nothing specific is named or namable from the filings — no pricing regime, no
channel, no internal cost structure, no product line a competitor would need
to cannibalize is evidenced. The honest answer is "nothing must be
destroyed," which per the rubric is an execution lead, not a configuration
barrier, and execution leads close. **Score 0. NO EVIDENCE FOUND.**

### Section 3 summary table

| # | Category | Evidence? | Type | Strength | Time to materialise |
|---|---|---|---|---|---|
| A1 | Rare manufacturing capability | No | — | None | — |
| A2 | Patent/IP pipeline | No | — | None | — |
| A3 | Process innovation | Adverse (flat margin) | 📄 | None | — |
| A4 | Product platform | No | — | None | — |
| B1 | Backward integration | No | — | None | — |
| B2 | Qualification lock-in | No (documented tier); 🔍 structural inference only | 🔍 | Weak | Unknown |
| B3 | Supply chain network effect | No | — | None | — |
| C1 | Customer ecosystem | No | — | None | — |
| C2 | Customer concentration improving | No | — | None | — |
| D1 | Proprietary data asset | No | — | None | — |
| D2 | Digital platform | No | — | None | — |
| E1 | Geographic first-mover | No | — | None | — |
| E2 | China+1 beneficiary | Yes (growth fact); cause uninferred | 📄 (fact) / 🔍 (cause) | Moderate | 0-12m, ongoing |
| F1 | Talent density | No | — | None | — |
| F2 | Execution moat | Adverse (documented non-delivery) | 📄 | None (deficit, not moat) | — |
| G1 | War chest | Adverse (capex declining, treasury rising) | 📄 | None | — |
| G2 | WC improvement trajectory | Documented facts exist (turnover ratios); no genuine multi-year trajectory once WC-days corrected — net -3.18 days over 4 years, non-monotonic, "stable" per B01 (CORRECTED, was Weak) | 📄 (non-qualifying) | None | — |
| H1 | Industry consolidation beneficiary | No | — | None | — |
| H2 | Strategic partnerships | No (related-party only) | — | None | — |
| H3 | ESG moat | No (zero capex admitted) | — | None | — |
| I1 | Talent asymmetry | No | — | None | — |
| I2 | Cannibalization barrier | No | — | None | — |
| R1 | Regulatory/policy tailwind | No (see Section 4) | — | None | — |

**Count with Strong/Moderate evidence: 1** (E2, Moderate). No category scores
Strong.

**Completionist guard check (CORRECTED, Findings 1 and 8):** 📄 recount
performed: documented evidence exists in 5 categories (E2, G2, A3, F2, G1 —
the same five this report's body anchors documented evidence in). Of these,
only E2 scores as an active moat (Moderate); G2, A3, F2 and G1 carry
documented evidence that is neutral-to-adverse to a moat claim, not blank
absence, and none scores above 0 — 3 of these 4 (A3, F2, G1) are actively
ADVERSE, and 1 (G2, corrected this pass from a prior Weak score) is
non-qualifying, not adverse, because it lacks a genuine trajectory rather
than pointing the wrong way. One further category (B2) carries evidence at
the 🔍 inference tier only. Total categories carrying any evidence = 6 (E2,
G2, A3, F2, G1, B2), at the top edge of the 3-6 realistic base rate but still
inside it, and no over-crediting of 🎙️ claims as 📄 documented occurred
anywhere in the recount.

---

## SECTION 4: REGULATORY & POLICY TAILWINDS (R1)

**4A Regulatory approvals in pipeline.** NO EVIDENCE FOUND. No pending
regulatory application, no body named, no unlock event described.

**4B Government policy tailwinds.** The only government-linked item found is
a routine export-incentive accounting policy: "Export Incentive: under
various scheme[s] notified by government has been recognized on the basis of
credits afforded in the passbook or amount received" (AR FY26 Note 1.2, p.115
and p.136 comparative). This is a standard RoDTEP/duty-drawback-type
mechanism available to all Indian exporters, not company-specific, not
disclosed with an amount, duration, or enrolment status, and shared equally
by every exporting peer. No PLI scheme, import-substitution measure,
procurement preference, or sector scheme is named anywhere in the AR.
**NO EVIDENCE FOUND for a differential policy tailwind.**

**4C Regulatory moat assessment.** Neither active nor emerging. No time-to-
kick-in estimate applies because no qualifying tailwind exists in the filed
record. **R1 scores 0.**

---

## SECTION 5: EMERGING MOAT SCORECARD

Raw score = likelihood × impact (HH=4, HM/MH=3, HL/MM/LH=2, ML/LM=1, LL=1, no
evidence=0), then × evidence-quality multiplier (📄 1.0x, 🎙️ 0.7x, 🔍 0.5x).

| # | Category | Likelihood/Impact | Raw | Evidence type | Multiplier | Adjusted |
|---|---|---|---|---|---|---|
| A1 | Rare manufacturing capability | — | 0 | — | — | 0.0 |
| A2 | Patent/IP pipeline | — | 0 | — | — | 0.0 |
| A3 | Process innovation | — | 0 | — | — | 0.0 |
| A4 | Product platform | — | 0 | — | — | 0.0 |
| B1 | Backward integration | — | 0 | — | — | 0.0 |
| B2 | Qualification lock-in | LL | 1 | 🔍 | 0.5 | 0.5 |
| B3 | Supply chain network effect | — | 0 | — | — | 0.0 |
| C1 | Customer ecosystem | — | 0 | — | — | 0.0 |
| C2 | Customer concentration improving | — | 0 | — | — | 0.0 |
| D1 | Proprietary data asset | — | 0 | — | — | 0.0 |
| D2 | Digital platform | — | 0 | — | — | 0.0 |
| E1 | Geographic first-mover | — | 0 | — | — | 0.0 |
| E2 | China+1 beneficiary | MH (fact confirmed, cause uninferred) | 3 | 📄/🔍 blend, graded 🔍 for the moat claim (durable cause unproven) | 0.5 | 1.5 |
| F1 | Talent density | — | 0 | — | — | 0.0 |
| F2 | Execution moat | — (adverse, scored 0 per rubric) | 0 | 📄 (adverse) | — | 0.0 |
| G1 | War chest | — (adverse, scored 0 per rubric) | 0 | 📄 (adverse) | — | 0.0 |
| G2 | WC improvement trajectory | — (CORRECTED: no genuine trajectory, Finding 1) | 0 | 📄 (non-qualifying) | — | 0.0 |
| H1 | Industry consolidation beneficiary | — | 0 | — | — | 0.0 |
| H2 | Strategic partnerships | — | 0 | — | — | 0.0 |
| H3 | ESG moat | — | 0 | — | — | 0.0 |
| I1 | Talent asymmetry | — | 0 (by design) | — | — | 0.0 |
| I2 | Cannibalization barrier | — | 0 (by design) | — | — | 0.0 |
| R1 | Regulatory/policy tailwind | — | 0 | — | — | 0.0 |

**Adjusted total: 2.0** (out of a ceiling of 92, I1/I2 included). Corrected
this pass (Finding 1): G2's WC-improvement claim rested on a WC-days swing
Stage 1 has since corrected from a lakh-to-crore unit error; the corrected
series shows no genuine trajectory, so G2's prior 1.0 contribution is
removed (0.5 B2 + 1.5 E2 + 0.0 G2 = 2.0, down from 3.0).
**I1/I2 contribution: 0.0** (unchanged) — no threshold crossing occurs via
I1/I2 for this name; both score 0 on the standard evidence bar, as the
framework expects for most companies. Nothing here needs flagging for the
operator's 10-15-scan I1/I2 review checkpoint.

**Classification: <12 → NO MEANINGFUL EMERGING MOAT.** (Unaffected by the
correction; both 2.0 and the prior 3.0 sit far inside this band.)

This result is not a disclosure artefact to be second-guessed upward. Where
Gate 0's corrected 14/60 MODERATE existing-moat score was substantially a
function of missing disclosure (six of twelve tests scored 0 on absent data,
not adverse findings), this Emerging Moat scan found active, documented
ADVERSE evidence in three categories (A3 process innovation, F2 execution
moat, G1 war chest), and — corrected this pass — a fourth category, G2,
whose apparent WC-days improvement dissolves under the corrected unit
calculation into a flat, non-qualifying trend, on top of the near-total
absence of forward evidence elsewhere. The one Moderate-strength item (E2
export growth) is real and worth watching, but a single category at
Moderate strength, evidence-capped by an unproven causal story, does not
clear even the 12-point MODEST band on its own.

---

## OPTIONALITY REGISTER (revised scope, Finding 4 of this pass)

| Optionality (one line) | Converting 📄 evidence | Where it first appears | Conversion window |
| --- | --- | --- | --- |
| Health supplement product launch | A named product, launch date, and disclosed revenue line | AR FY27 Future Plans / a Reg 30 product-launch filing | Overdue 3 years already; realistic window unknown, watch AR FY27 (due ~Sep 2027) |
| Export growth (E2) reflects genuine customer-qualification stickiness rather than a lumpy/restocking order pattern | A filing names a specific new export customer, country, or certification tied to the export line, or Q2/Q3 FY27 sustains high-single-digit-plus like-for-like growth ex freight gross-up | Results filings (quarterly) or AR FY27 MD&A | 2-4 quarters (by Q3/Q4 FY27) |
| Titagen/Unstergen/OXIBIL collagen-peptide brands (named only on the company website per company memory, absent from all three filed annual reports) | The brand names appear in a filed AR, results filing, or Reg 30 announcement with a revenue or volume figure attached | AR FY27, or an interim results filing | Unknown; needs Halt-1 verification of whether these are even current products |
| Committed forward capex programme (any named project, capacity figure, or commissioning date) | A capital-commitment note or Reg 30 capex announcement | AR FY27 Note (capital commitments) or a Reg 30 filing | Unknown; none exists today after 3 years of review |
| Customer-qualification lock-in (B2) exists structurally in a pharma/biotech/diagnostic supply chain but rests only on industry inference, not Titan's own disclosure (added this pass, Finding 4) | AR or exchange filing names a specific certification (cGMP/ISO/NABL/WHO-GMP/USFDA/pharmacopoeia) held by Titan, or discloses sole-source/multi-year post-qualification customer language | AR FY27 Annexure 2 (Technology Absorption) or a customer-contract disclosure | Unknown; zero certification disclosure in 3 years reviewed, no near-term trigger identified |

Registered options are watched, never scored. Two rows previously carried
here (FVTPL portfolio composition/related-party linkage; Peptech
PAT-reconciliation gap) are verification items, not forward advantages, and
are moved to input_gaps this pass (Finding 4) — both remain tracked, via
B01's FLAG-ASSOCIATE-RECON and this stage's input_gaps list below. None of
the above converted to 📄 documented status within the evidence reviewed.

---

## SECTION 6: TIMELINE, RISKS & COMBINED ASSESSMENT

### 6A Moat evolution timeline

- **Next 12m:** Watch whether FY27 quarterly like-for-like growth (ex freight
  gross-up) sustains above high-single digits (B05 trigger 1) — the only
  near-term signal that would keep E2 alive as a real, not lumpy, trend. Watch
  whether AR FY27 finally names the health-supplement product or drops the
  claim.
- **12-24m:** AR FY27 (~Sep 2027) is the key milestone: it will show whether
  gross PPE additions keep declining (confirming the execution deficit) or
  reverse (a genuine change), and whether the FVTPL portfolio composition is
  disclosed for the first time.
- **24-36m:** If export growth continues to outpace domestic for two more
  years with a named customer/country/certification attached, E2 could
  mature from Moderate/inference-capped to Strong/documented. Absent that
  naming, it stays a fact without a moat story.
- **3-5yr:** No category in this scan currently points to a 3-5 year
  structural moat outcome; the scan would need to be re-run once (if ever) a
  named capex project, a certification, or a product launch enters the filed
  record.

### 6B Risks to each top-scoring emerging moat

- **E2 (export growth, the only Moderate-strength item, and now the only
  category scoring above zero):** Early warning signs the trend is lumpy
  rather than structural — a single-quarter export order pattern, a
  reversion to FY25's flat/declining pattern once the FY26 base effect laps
  (B05 trigger 1, kill signal), or a freight-gross-up base-effect distortion
  masking real deceleration. The filings give no demand narrative to lean on
  if growth reverses.

**Note on G2 (removed from scoring, Finding 1 of this pass):** the corrected
WC-days series shows no genuine multi-year improvement (net -3.18 days over
four years, non-monotonic, Stage 1's own "stable" read). The single-year
inventory/receivables turnover gains are real and documented, but the one
day-count improvement they coincide with (FY25 to FY26) is a documented
payables-stretch event (Trade Payables Turnover Ratio 25.52x to 17.26x, AR
FY26 Note 45 variance note (g)), a pattern that tends to reverse, not a
structural change. G2 carries no forward risk discussion here because it no
longer scores; watch only whether FY27's turnover ratios hold up against a
normalising payables cycle.

### 6C Combined Gate 0 + Emerging Moat table (CORRECTED)

| | Score | Classification |
|---|---|---|
| Gate 0 core score | 79/100 | — |
| Gate 0 existing moat count | 2 confirmed, moat_score 14/60 | MODERATE |
| Gate 0 grand total | 93/160 | GOOD |
| Emerging Moat adjusted score | 2.0 / 92 | NO MEANINGFUL EMERGING MOAT |

### 6D Combined classification (CORRECTED, Finding 2 of this pass)

The prompt names eight labels (EXCEPTIONAL, EXCELLENT+, HIGH POTENTIAL,
GOOD+, GOOD, TURNAROUND, AVERAGE, AVOID) but does not supply a complete
state-to-label mapping table; it gives qualitative guidance for two cells
only — a GOOD/AVERAGE backward score paired with an EXPANSION forward score
is "exactly the transition setup this operation hunts," and HIGH
POTENTIAL/TURNAROUND rows need full reasoning. That gap is named here rather
than bridged silently.

Applying the corrected Gate 0 inputs (core 79/100, moat 14/60 MODERATE,
grand total 93/160, classification GOOD) against the corrected Emerging Moat
score (2.0/92, classification NONE — no EXPANSION or even STRENGTHENING
signal): the prompt ties any elevation above the backward label specifically
to a forward EXPANSION signal, which does not exist here. Nothing in the
prompt supports moving off the backward classification in either direction —
GOOD is not itself weak enough to invoke the TURNAROUND/AVOID branch either.

**Combined assessment: GOOD.** Titan Biotech clears Gate 0 on core financial
quality (clean balance sheet, positive FCF, four-year data window, no deal
breakers), but its corrected classification sits at GOOD, not GOOD+ — the
working-capital-days unit error that had been the swing factor between the
two bands is now fixed, and it fixes toward the weaker reading. The evidence
built in Stages 4-7 stacks the same direction as before on the transition
question: pricing power WEAK (Stage 4), moat 14/60 MODERATE with much of
that thinness a disclosure gap rather than a decisive pass (Gate 0),
credibility grade C on the two claims that would evidence a forward story
(Stage 5/B05), and a corrected 2.0/92 Emerging Moat score with three
categories (A3, F2, G1) showing documented ADVERSE evidence (declining
capex, a contradicted capacity claim, treasury drift) and a fourth (G2)
showing documented evidence that does not rise to a genuine multi-year
improvement once the payable-days error is corrected. The one live forward
signal (export growth, E2) is real but unexplained by the company's own
disclosure and evidence-capped as a result. This is not a company caught
mid-climb on the Quality Ladder with the market not yet noticing; on the
corrected filed record, it is a company sitting where it has sat for three
years, on a slightly lower backward rung than previously read, with one
financial metric (exports) moving in a direction that could matter later if
a filing ever explains why.

### 6E Final output card

**Moat evolution map (existing → emerging per family):**
- Family A (Product/Tech): none existing (Gate 0), none emerging (this scan)
- Family B (Supply Chain): none existing, B2 unconfirmed structural inference only
- Family C (Customer): none existing, none emerging
- Family D (Data/Digital): none existing, none emerging
- Family E (Geographic): none existing, E2 export growth Moderate/inference-capped — the one live item
- Family F (Talent/Org): none existing, F2 shows a documented execution deficit, not a moat
- Family G (Financial/Structural): existing balance-sheet cleanliness (Gate 0 core), G1 shows adverse reinvestment signal; G2 shows genuine single-year turnover-ratio gains (inventory, receivables) but no multi-year WC-days trajectory once the payable-days unit error is corrected — the one FY25-to-FY26 day-count improvement that did occur is a documented payables-stretch event, not a structural change; scored None, not Weak (corrected this pass)
- Family H (Ecosystem/External): none existing, none emerging
- Family I (Structural asymmetries): none, by design for this company

**Catalysts to watch in the next 12 months:**
1. Q2/Q3 FY27 like-for-like (ex freight) growth sustaining above high-single
   digits — confirms or kills the E2 story (B05 trigger 1).
2. AR FY27 either naming the health-supplement product for the first time or
   repeating the identical claim a fourth year running (B05 kill signal).
3. AR FY27 Note 5 disclosing FVTPL portfolio composition and any
   related-party linkage (B05 trigger 3).

**Biggest risk to the emerging moats:** there is effectively one emerging
moat candidate in this entire scan (E2, export growth), and its own filings
give no causal explanation for it. If FY27 shows the export line decelerate
or revert to FY25's flat pattern, the Emerging Moat picture for this company
collapses to zero live categories, not merely a lower score.

---

```yaml
stage: B07-emoat
company: "TITANBIO"
run_date: "2026-09-16"
model: claude-sonnet-5
status: complete
input_gaps:
  - "No capital-commitment note (contracts remaining to be executed on capital account) disclosed in AR FY2026; no named capex project, capacity figure, or commissioning date exists for any of the four plants in any of the three annual reports"
  - "No quality/manufacturing certification (cGMP, ISO, NABL, WHO-GMP, USFDA, pharmacopoeia compliance) disclosed anywhere despite a pharma/biotech/diagnostic customer base; B2 qualification-lock-in cannot be tested beyond structural industry inference"
  - "Titagen/Unstergen/OXIBIL collagen-peptide brand names (from company memory / website) do not appear in any of the three filed annual reports; cannot be verified as current, revenue-generating products from the filed evidence base"
  - "No top-5/10 customer disclosure exists in any filing; C2 customer-concentration-improving cannot be tested"
  - "No R&D headcount, PhD count, or ESOP-to-technical-staff scheme detail disclosed; F1 talent density cannot be tested beyond the immaterial R&D spend figure"
  - "FVTPL quoted-debt portfolio composition (issuer names) and any related-party linkage is undisclosed (AR FY26 Note 5, p.127) -- a verification item for Halt 1, cross-references B01's FLAG-ASSOCIATE-RECON; moved here this pass from the optionality register, where it did not belong (Finding 4)"
  - "Peptech Biosciences associate PAT-reconciliation gap (Rs 415.03 lakh, per B01 FLAG-ASSOCIATE-RECON) is a verification item for Halt 1, not a forward optionality; moved here this pass from the optionality register (Finding 4)"
flags:
  - {type: FLAG-CAPEX-CLAIM-CONTRADICTED, reason: "MD&A 'build capacity and capabilities for future business growth' sentence reused near-verbatim AR FY24 to AR FY26 while gross PPE additions fell three years running (Rs 1,948.49 lakh FY24 to Rs 936.88 lakh FY25 to Rs 740.08 lakh FY26, AR FY24/FY25/FY26 Note 2(a)) and 77% of the FY26 investing outflow went into a quoted-debt FVTPL portfolio (AR FY26 Note 5, p.127) whose own return fell from 7.04% to 3.64% (AR FY26 MD&A Key Ratios, p.103)."}
  - {type: FLAG-HEALTH-SUPPLEMENT-STALE, reason: "Identical or near-identical 'developing product for health supplement' claim repeated in AR FY2024, AR FY2025 and AR FY2026 Directors' Reports with zero product name, launch date, or revenue evidence in any year."}
  - {type: FLAG-NO-CAUSAL-EXPORT-STORY, reason: "Export revenue +49.0% FY26 (AR FY26 Note 38, p.141-142) is the scan's one Moderate-strength item, but no filing names a customer, country, or certification driving it; durability unproven from the filed record."}
em_score: 2
em_classification: "NONE"
active_categories:
  - {id: "E2", name: "China+1 beneficiary (export growth)", strength: "Moderate", evidence_type: "documented fact / inference on cause", time_to_materialise: "0-12m, ongoing"}
evidence_mix: {documented: 5, claim: 0, inference: 1}
completionist_recount: "recount performed at the 22-category level, one item per category at its primary evidence tier, excluding NO EVIDENCE FOUND categories (basis stated per Finding 6 of the correction log): documented (E2, G2, A3, F2, G1) = 5 categories, of which only E2 scores as an active moat (Moderate) and 3 (A3, F2, G1) carry documented ADVERSE evidence while 1 (G2, corrected this pass) is documented but non-qualifying, not adverse; inference (B2) = 1 category; claim = 0 categories (no category row rests solely on a management claim). Total categories with any evidence = 6, at the top edge of the 3-6 realistic base rate, no over-crediting of management claims as documented."
catalysts_12m:
  - {catalyst: "Q2/Q3 FY27 like-for-like revenue growth (ex freight gross-up) vs high-single-digit bar", window: "0-9m", evidence_type: "MGMT CLAIM pending confirmation", anchor: "B05 trigger 1; results filings"}
  - {catalyst: "AR FY27 names health-supplement product or repeats claim a 4th year", window: "~12m (AR FY27 due ~Sep 2027)", evidence_type: "SCHEDULED, NOT YET DOCUMENTED", anchor: "AR FY24/FY25/FY26 Directors' Report Future Plans"}
  - {catalyst: "AR FY27 discloses FVTPL portfolio composition / related-party linkage", window: "~12m", evidence_type: "SCHEDULED, NOT YET DOCUMENTED", anchor: "AR FY26 Note 5, p.127"}
capex_embedded_growth_pct: 2.8
optionality_register:
  - {optionality: "Health supplement product launch", converting_evidence: "Named product, launch date, disclosed revenue", first_appears: "AR FY27 or a Reg 30 product filing", window: "Overdue 3 years; window unknown"}
  - {optionality: "Export growth (E2) proven structural, not lumpy/restocking", converting_evidence: "A filing names a specific new customer/country/certification, or growth sustains 2-4 quarters ex freight gross-up", first_appears: "Quarterly results or AR FY27 MD&A", window: "2-4 quarters"}
  - {optionality: "Titagen/Unstergen/OXIBIL brands confirmed as filed, revenue-generating products", converting_evidence: "Brand names appear in a filed AR or results filing with a figure attached", first_appears: "AR FY27 or interim results", window: "Unknown; needs Halt-1 verification"}
  - {optionality: "Named forward capex project with capacity/commissioning date", converting_evidence: "A capital-commitment note or Reg 30 capex announcement", first_appears: "AR FY27 or Reg 30 filing", window: "Unknown; none disclosed in 3 years reviewed"}
  - {optionality: "Customer-qualification lock-in (B2) confirmed by Titan's own disclosure, not only industry inference", converting_evidence: "AR or exchange filing names a specific certification (cGMP/ISO/NABL/WHO-GMP/USFDA/pharmacopoeia) or discloses sole-source/multi-year post-qualification customer language", first_appears: "AR FY27 Annexure 2 or a customer-contract disclosure", window: "Unknown; zero certification disclosure in 3 years reviewed"}
combined_assessment: "GOOD"
combined_reasoning: "Gate 0's corrected GOOD score (core 79/100, moat 14/60 MODERATE, grand total 93/160) pairs with a corrected 2.0/92 Emerging Moat score with three categories (A3, F2, G1) carrying documented adverse evidence and no genuine multi-year WC-improvement trajectory once the payable-days unit error is fixed (G2 now scores 0); no forward EXPANSION signal exists to elevate the backward classification, so GOOD stands unmodified as the combined assessment (one of the prompt's eight labels; the prompt supplies no full mapping table for this cell, a gap named rather than bridged)."
top_moat_risks:
  - "E2 export growth is the scan's only live category and has no causal explanation in the company's own filings; a reversion to FY25's flat pattern once the FY26 base laps would zero out the scan entirely"
  - "The capex-claim contradiction (F2/G1) is a credibility problem, not just an absence: management restated an unchanged sentence over a year in which the underlying spend pattern changed materially"
  - "Health-supplement claim has run three full annual cycles with zero delivery evidence; treating it as pending optionality rather than a dead claim requires AR FY27 to break the pattern"
  - "G2 (WC-days) no longer scores after Stage 1's unit-error correction; the only genuine year-on-year gains (inventory/receivables turnover) coincide with a documented payables stretch (AR FY26 Note 45 variance note (g)), a pattern that carries its own reversal risk"
analyst_note: "This correction pass fixes an upstream unit error (B01's payable-days lakh-to-crore conversion) that had inflated the appearance of a working-capital release. The corrected WC-days series (130.85 to 135.39 to 150.05 to 127.67, a net -3.18-day change over four years) is stable, not improving; G2 now scores 0 and leaves the active list, cutting em_score from 3.0 to 2.0. Gate 0's own corrected numbers (core 79/100, moat 14/60 MODERATE, grand total 93/160, classification GOOD) replace the pre-correction GOOD+ inputs throughout Section 6. The combined_assessment field is corrected from a coined compound label to GOOD, the closest of the prompt's eight labels: no forward expansion signal exists to elevate a GOOD backward score, and the prompt itself supplies no full mapping table for this cell, a gap named rather than bridged. The one live emerging-moat category remains E2 (export growth), real but causally unexplained by the company's own filings. Recommend Halt 1 still prioritise the optionality register (capex-claim contradiction, Titagen/Unstergen/OXIBIL brand-name gap, and now also B2 qualification-lock-in) over the export story, which the filings already evidence as far as they go."
```
