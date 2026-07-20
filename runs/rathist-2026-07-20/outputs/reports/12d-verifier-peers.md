# Verifier D: Peer Coverage Audit — Rathi Steel & Power Ltd (RATHIST)

Run date: 2026-07-20 | Verifies: B06 (06-peers.md) against the two peer source documents and
B05's peer_questions[] list | Model: claude-sonnet-5

## SCOPE NOTE (read before the rest of this audit)

Only two peer documents were provided in `inputs/peer-concalls/`, and neither is an earnings-call
transcript:

- `202602120239_VRAJ_Iron_And_Steel_Limited.pdf` — a CARE Ratings credit rating press release for
  VRAJ Iron And Steel Limited (VISL), 7 pages, dated 26 Feb 2026, covering FY24/FY25 (audited) and
  9M FY26 (unaudited).
- `804f416c-ec0b-4aad-b2f1-d317fd004a58.pdf` — confirmed as **Scan Steels Ltd** (BSE 511672), a
  40-page Investor Presentation ("Corporate Presentation June'26"), filed under Reg. 30 to BSE on
  19.06.2026 per the cover letter on page 1.

B06 flagged this document-type mismatch prominently and correctly; this audit independently
confirms both identifications and the page-count/content characterization are accurate. The rest
of this audit assesses whether B06 extracted and represented these two documents' content
correctly, whether the peer_questions were all addressed, and whether verdict discipline was
honoured given only 2 peer sources were available (structurally below the protocol's implied
richer peer set).

---

## PART 1: SOURCE VERIFICATION — VRAJ CARE RATIONALE (7 pages, read in full)

All citations tested below were checked against the full 7-page document.

| B06 location | Claimed content | Cited anchor | Verified against source | Verdict |
|---|---|---|---|---|
| Q1 | "Company's sales volumes are expected to remain healthy in the near-to-medium-term considering steady demand from end-user industries" | p.1 | Exact quote, p.1 para 2 | MATCH |
| Q2 | "iron ore, coal, pig iron, dolomite and manganese ore... directly sourced from the domestic market, less than 10% of the total coal purchase is imported" | p.3 | Exact quote, p.3 "Profitability susceptible to input price volatility" | MATCH |
| Q2 | PBILDT margin 13.20% FY25 implies ~86.8% cost base | p.2 (computed) | 13.20% margin figure exact; 86.8% is B06's own arithmetic (100−13.20), correctly caveated as "of which RM share is not broken out" | MATCH, computation sound and honestly caveated |
| Q4 | VRAJ "does not mention hot charging or direct billet-charging anywhere" | whole document | Confirmed by full read — no such term appears anywhere in the 7 pages | MATCH |
| Q5 | 20-MW captive power (WHRB), 15 MWp solar plant; "leading to a better cost structure, positively impacting the company's profitability margins" | p.2 | Exact quote and figures, p.2 "Semi-integrated nature of operations and captive power plant" | MATCH |
| Q6 | Sponge iron CU "above 90% in FY25"; MS billet CU "improved to 84% in FY25... from 77% in FY24"; TMT CU "increased significantly to 67% in FY25 from 48% in FY24"; "In H1FY26, CU across all product segments witnessed further improvement" | p.2 | Exact quotes, p.2 "Satisfactory capacity utilisation" | MATCH |
| 2B | PBILDT margin 18.33% FY24 → 13.20% FY25, "largely due to a decline of ~10% in average selling prices across all product categories" | p.2 | Exact quote/figures, p.2 | MATCH |
| 2B | 9M FY26 PBDIT margin 9.11%, "primarily attributable to a decline in realisations across key products" | p.3 | Exact quote/figure, p.3 | MATCH |
| 2C | ~₹165cr sponge iron/MS billet/WHRB project; ~₹171cr FY25 IPO | p.2 | Both figures exact, p.2 | MATCH (figures) |
| 2C | "~₹49 crore, 15 MWp solar plant" **funded via** the ~₹171cr IPO | p.2, p.4 | **Solar plant figures (₹49cr cost) are exact, but the source explicitly states the solar plant was financed via ₹38cr term debt from HDFC Bank + ₹11cr internal accruals — NOT the IPO** (p.2: "financed through debt of ₹38 crore and ₹11 crore through internal accrual of the company"; repeated p.4) | **MISMATCH — see Finding 1 below** |
| 2E | Geographic concentration (majority customers within Chhattisgarh); customer concentration (top-5 ~32% FY25 revenue vs 37% FY24); group exposure ~15% of TNW via equity + corporate guarantee | p.3 | All exact quotes/figures, p.3 | MATCH |

**Finding 1 (MAJOR).** B06 Part 2C states: *"VRAJ funded a ~Rs 165 crore sponge iron/MS billet/WHRB
expansion plus a further ~Rs 49 crore, 15 MWp solar plant via a ~Rs 171 crore FY25 IPO (CARE
rationale, p.2, p.4)."* This is not what the source says. Per the CARE rationale (p.2): the ₹171cr
IPO proceeds were used to (a) repay ₹70cr of debt already drawn for the sponge iron/billet/WHRB
project and (b) fund ₹59.5cr of that project's remaining cost — i.e. the IPO substituted for debt
on part of the first project. The separate 15 MWp solar plant (₹49cr) was **explicitly and
exclusively** financed by a ₹38cr HDFC Bank term loan plus ₹11cr internal accruals; the source
states this twice, once on p.2 and again on p.4 ("commissioned a 15-MWp solar plant... incurring a
total cost of ₹49 crore funded through ₹38 crore term debt from HDFC Bank and ₹11 crore from
internal accruals"). B06's YAML compounds the error: `industry_cross_read.capex_cycle` states
*"VRAJ funded ~Rs214cr integration via IPO proceeds"* — summing 165+49=214 and attributing the
whole amount to the IPO, when a material share (₹38cr debt, ₹11cr accruals, plus the ~₹25cr cost
overrun on the first project which the source says was "funded from internal accrual") was not
equity-funded at all. This matters because it directly under-girds Part 5's cross-peer hypothesis
("producers who can tap equity markets... are scaling... an order of magnitude faster than
producers who cannot") — the hypothesis conflates VRAJ's IPO-and-debt-and-accrual-funded capex
with Scan Steels' genuinely 59%-equity-funded (₹500cr fresh raise) capex as if both are the same
"equity access" story, when VRAJ's is materially more debt/accrual-financed than represented. This
does not overturn the qualitative point that VRAJ raised equity (it did, via a real IPO) or that
Rathi has not, but it overstates the degree to which VRAJ's *specific* capex items were
equity-funded, and that overstatement is what feeds the stated hypothesis. Decision-relevance is
moderate: this is background/cross-read material rather than a verdict-card input, so it would not
flip the peer verdicts on Q1–Q6, but it is a genuine misreading of the source that should be
corrected before the hypothesis is carried into synthesis. **Severity: MAJOR** (wrong, but the
Q1–Q6 verdicts and the overall "complicates" narrative effect survive; only the Part 5 hypothesis
framing needs revision).

---

## PART 2: SOURCE VERIFICATION — SCAN STEELS INVESTOR PRESENTATION (40 pages, read in full)

| B06 location | Claimed content | Cited anchor | Verified against source | Verdict |
|---|---|---|---|---|
| Cover/identification | Company = Scan Steels Ltd, BSE 511672, Investor Presentation June'26, filed under Reg. 30, cover letter dated 19.06.2026 | p.1 | Cover letter confirms all details exactly, including "~₹850 Crores" project reference | MATCH |
| Methodological flag | "forward figures are management estimates, not guidance" | p.6 | Exact quote, p.6 Executive Summary | MATCH |
| Q2 | "IF melt + casting - charge ≈ 75% sponge + 25% scrap/pig iron" for MS Billet | p.9 | Exact quote, p.9 "Integrated Business Model" MS Billet column | MATCH |
| Q4/2C | Hot charging "Cost Reduction (already done): Hot charging at rolling mill" | p.25 | Exact quote, p.25 "How Scan Gets to Vision 2031" | MATCH |
| Q4 | "Hot Charging & Yield: 0.8pp" of FY26 baseline EBITDA margin (5.9%) | p.27 | Exact figures, p.27 "The Margin Stack" (0.8pp line item; 5.9% FY26 baseline) | MATCH |
| Q4 | Blended FY26 realization ~Rs 40,000-43,430/ton | p.24 | SHRISHTII TMT: cost ≈₹40,000 vs realization ₹43,430/T, p.24 "The Steel Cup" | MATCH |
| Q5 | Brand premium of Rs 1,500-2,000/ton over unbranded local product | p.12 | Exact figure and framing, p.12 "Brand-Led Pricing Power" | MATCH |
| Q6 | Sponge Iron 84%, MS Billets 81%, Rolled Products 82%, Captive Power 100% util, FY26 | p.7 | Exact figures, p.7 "FY26 Capacity & Production" | MATCH |
| 2A/Part1 Q1 | "~8-9% Annual Demand Growth," per-capita ~100kg vs world ~220kg+, National Steel Policy 300MT FY30 target | p.34 | Exact figures, p.34 "Demand Tailwinds" | MATCH |
| 2A | "Ministry of Steel - National Steel Policy 2017 · IBEF (FY26). Macro context only — not a Scan forecast" | p.34 | Exact footnote quote, p.34 | MATCH |
| 2C | ~₹850cr greenfield pellet/DRI/coal-washery/50MW power buildout | p.6, p.21, p.31 | ₹850 Cr Capex Estimated exactly matches p.21 "Theme 3" table and p.31 "Use of Proceeds"; p.6 references "~₹850 Crores" investment | MATCH |
| 2C | Equity raise "Rs 500 Cr" = 59% of funding, "priced at a premium to CMP" | p.31 | p.31: "Equity Raise ₹500 Cr 59%"; "Fresh equity raised in three staggered tranches at a premium to the prevailing market price" — B06 paraphrases "CMP" for "prevailing market price," a fair paraphrase | MATCH |
| 2C | Targeting ~4.9x revenue growth (Rs 838cr→Rs 4,133cr) and ~11.7x EBITDA growth (Rs 49cr→Rs 575cr) by FY31 | p.19, p.25, p.31 | Exact figures/multipliers, all three pages | MATCH |
| Q3/context | Bindals Sponge Industries acquisition, "under IBC since 2018" | p.23 | Exact quote, p.23 "Bindals Acquisition" | MATCH |
| 2E | Recurring mine and transporter strikes, ~45-day RM buffer stock | p.29 | p.29 "Working Capital" panel lists "Frequent mine strikes," "Transporter strikes" as recurring disruptions and "~45 days" procurement lead time driving the buffer; B06's framing ("requiring a ~45-day RM buffer stock") is a reasonable paraphrase of "critical buffer stock is held to avoid mill stoppage" against the ~45-day lead time | MATCH (paraphrase, faithful) |
| 2E | Monsoon-driven (Jun-Sep) RM moisture/supply risk | p.29 | Exact match, p.29 "Monsoon - high moisture ... Jun-Sep" | MATCH |
| 2E | Execution/dilution risk in Rs500cr equity-funded expansion | p.31 | Matches "FUNDING & DILUTION" panel, p.31 | MATCH |

No mismatches found in the Scan Steels citation set — every anchor checked resolves to the exact
page and, in most cases, a near-verbatim quote.

**Finding 2 (MINOR — completeness, not accuracy).** Several Scan Steels disclosures adjacent to
the peer_questions were not mined even though they could have added marginal color: p.22's
"Energy = 12-15% of TMT cost structure" and WHRS-vs-grid power cost benchmarks (₹2/kWh vs
₹6.80/kWh) were not tied into the Q5 (green power) discussion; p.15/16's working-capital and
valuation ratios (debtor days, P/E, ROCE, ROE) were not cross-referenced against Rathi's own
disclosed WC (~₹35cr on ~₹500cr turnover, per B05). None of these are directly responsive to any
of the six specific peer_questions, so this is scored as a minor industry-context gap only, not a
missed claim-relevant item under Rule 3.

**Finding 3 (MINOR — basis note, source-inherited not B06-introduced).** The YAML's
`industry_cross_read.pricing_inputs` field narrates VRAJ's margin as one continuous gradient,
"18.33%→13.20%→9.11% PBDIT," but the source itself uses two different margin definitions across
the period: PBILDT for FY24/FY25 (18.33%, 13.20%) and PBDIT for H1/9M FY26 (9.11%). CARE's own
document introduces this switch, not B06, and the two metrics are close enough in construction
(both pre-depreciation, pre-interest, pre-tax) that the directional read is not undermined, but
labeling them as a single unbroken series slightly overstates precision. Low materiality.

---

## PART 3: PEER-QUESTION COVERAGE CHECK (B05 peer_questions[] vs B06 Part 1)

| # | B05 peer_questions[] item (verbatim topic) | B06 Part 1 verdict | Addressed? |
|---|---|---|---|
| 0 | Domestic demand tracking Budget 2026/FTA/tariff-cut narrative | Q1 — PARTIALLY VERIFIED | Yes |
| 1 | RM/scrap sourcing, RM cost ratio ~75-80% of sales | Q2 — UNVERIFIABLE | Yes |
| 2 | Stainless-steel oversupply from IBC-acquired plants | Q3 — UNVERIFIABLE | Yes |
| 3 | Direct billet/hot-charging savings quantum + "first and only" claim | Q4 — CONTRADICTED | Yes |
| 4 | Green-steel/GreenPro institutional demand premium | Q5 — UNVERIFIABLE | Yes |
| 5 | Capacity-utilization disclosure volatility as industry-comparable | Q6 — CONTRADICTED | Yes |

All 6 items in B05's `peer_questions[]` received an explicit, anchored verdict in B06 Part 1, in
the same order. `claims_all_addressed: true`. No skipped claims — Rule 5 satisfied cleanly.

---

## PART 4: VERDICT-DISCIPLINE AUDIT (Rule 4)

| Claim | B06 verdict | Peer anchors used | Independent-anchor rule satisfied? |
|---|---|---|---|
| Q1 (demand macro) | PARTIALLY VERIFIED | VRAJ + Scan Steels (2 peers) | Yes — appropriately downgraded from VERIFIED since the *specific* triggers (Budget 2026, FTA, tariff cuts) are not named by either peer; only the generic infra-demand direction is corroborated by both. Correct discipline. |
| Q2 (RM cost ratio) | UNVERIFIABLE | Both peers checked, neither comparable | N/A — no verdict upgrade from silence. Correct. |
| Q3 (SS oversupply) | UNVERIFIABLE | Both peers checked, wrong sub-segment | N/A — correctly flagged as a coverage gap, not treated as silent confirmation. Correct. |
| Q4 (hot-charging "first and only") | CONTRADICTED | Scan Steels only (VRAJ silent — doesn't discuss hot charging) | Single-peer contradiction. The B12d rubric's explicit 2-peer-anchor rule is written for VERIFIED claims; it does not on its face require 2 independent contradicting peers. Given only 2 peer documents exist and one (VRAJ) has zero relevant disclosure, a single-source contradiction is the ceiling achievable with this peer set — B06 is transparent about this ("Peers silent: VRAJ does not mention hot charging..."). Not scored as a discipline fail, but flagged as a structural single-source limitation worth naming explicitly for synthesis (the contradiction is real and well-anchored, but rests on one peer, not two). |
| Q5 (green premium) | UNVERIFIABLE | Both peers checked, neither addresses demand-side premium | N/A — correctly not upgraded from silence, and B06 explicitly reasons through why the silence is "mildly informative" without overclaiming it as a verdict. Correct discipline. |
| Q6 (utilization volatility) | CONTRADICTED | VRAJ + Scan Steels (2 peers) | Two independent peer anchors, both showing cleaner/higher utilization than Rathi. Correct, well-supported. |

No claim marked VERIFIED rests on a single peer (there are zero VERIFIED claims in this report,
which is itself the correct, conservative outcome given a 2-document, non-transcript peer set).
No verdict was upgraded from silence — every UNVERIFIABLE stayed UNVERIFIABLE with the reasoning
shown. `verdict_discipline_fails: []`.

---

## PART 5: PEER-UTILISATION ASSESSMENT

peers_provided = 2. Both VRAJ and Scan Steels are marked SUBSTANTIVE in B06's coverage map, and
both classifications are earned: each peer's citations were checked exhaustively against the full
source document (7 pages for VRAJ, 40 pages for Scan Steels) and, with the single funding-source
exception in Finding 1, every citation resolves to real, accurately-quoted content at the stated
page. Peer utilisation = 2/2 = 100% substantively used, which is honest — neither document could
credibly be marked UNUSED given the volume of real, checkable evidence each contributed to Part 1
verdicts and Part 2 cross-reads.

The larger and more important coverage finding is not about whether the two provided peers were
used (they were, thoroughly) but about the structural inadequacy of the peer *set* itself: with
only 2 documents, neither a transcript, 3 of 6 peer_questions (Q2, Q3, Q5) were always going to be
unverifiable because neither carbon-steel producer addresses stainless steel, discloses a
comparable RM-cost ratio, or discusses institutional green-steel demand premiums. B06 names this
gap honestly and repeatedly rather than papering over it with a forced verdict — this is the
correct behavior under the framework's evidence-discipline rules.

---

## SUMMARY OF FINDINGS

| # | Severity | Location | Issue |
|---|---|---|---|
| 1 | MAJOR | B06 Part 2C / YAML `industry_cross_read.capex_cycle` | Mischaracterizes VRAJ's ₹49cr solar-plant capex as IPO-funded when the source states it was financed via ₹38cr term debt + ₹11cr internal accruals; compounds into an overstated "~Rs214cr via IPO proceeds" figure that feeds the Part 5 capital-market-access hypothesis |
| 2 | MINOR | B06 Part 2 (Scan Steels) | Some adjacent Scan Steels disclosures (energy cost %, WC/valuation ratios) not mined; not responsive to any of the 6 peer_questions, so a completeness gap only |
| 3 | MINOR | B06 YAML `industry_cross_read.pricing_inputs` | PBILDT (FY24/25) and PBDIT (9M FY26) margin figures narrated as one unbroken gradient; the basis switch is source-inherited, not introduced by B06, and doesn't change the direction of the finding |

No CRITICAL findings. No SUBSTANTIVE-but-unsupported peers. No unused-but-relevant claim-level
misses. All 6 peer_questions addressed. Verdict discipline honoured throughout, including the
correct, conservative decision to award zero full VERIFIED verdicts given the thin, non-transcript
peer set.

---

```yaml
stage: B12d
company: "RATHIST"
run_date: "2026-07-20"
model: claude-sonnet-5
status: complete
peers_audited: 2
substantive_confirmed: 2
substantive_unsupported: []
unused_but_relevant: []
claims_all_addressed: true
verdict_discipline_fails: []
findings:
  - {severity: "MAJOR", location: "B06 Part 2C / YAML industry_cross_read.capex_cycle", claimed: "VRAJ funded its ~Rs165cr sponge iron/MS billet/WHRB expansion plus a further ~Rs49cr, 15 MWp solar plant via a ~Rs171cr FY25 IPO (summed in YAML to ~Rs214cr 'via IPO proceeds')", source_truth: "CARE rationale p.2 and p.4 state the 15 MWp solar plant (Rs49cr) was financed via Rs38cr HDFC Bank term debt + Rs11cr internal accruals, unrelated to the IPO; the IPO's Rs171cr was used to repay Rs70cr of prior project debt and fund Rs59.5cr of the first project, not the solar plant", note: "Overstates VRAJ's equity-funded capex share; directly feeds the Part 5 capital-market-access cross-peer hypothesis, which should be revised before carrying into synthesis. Does not affect the Q1-Q6 verdicts.", source_fidelity: true}
  - {severity: "MINOR", location: "B06 Part 2 (Scan Steels cross-read)", claimed: "n/a - completeness gap", source_truth: "Scan Steels p.22 (energy = 12-15% of TMT cost structure, WHRS vs grid power cost) and p.15/16 (working capital, valuation ratios) not mined into the analysis", note: "Not responsive to any of the 6 peer_questions; industry-context miss only", source_fidelity: false}
  - {severity: "MINOR", location: "B06 YAML industry_cross_read.pricing_inputs", claimed: "18.33%->13.20%->9.11% PBDIT as one continuous margin series", source_truth: "Source uses PBILDT for FY24/FY25 and PBDIT for H1/9M FY26; basis switch is CARE's own, not introduced by B06", note: "Direction of finding unaffected; precision slightly overstated", source_fidelity: false}
critical_count: 0
major_count: 1
minor_count: 2
acceptance_rate: 100
```
