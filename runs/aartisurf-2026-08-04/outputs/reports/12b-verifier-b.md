# B12b — VERIFIER B: RED-FLAG AUDIT (AARTISURF)

Model: claude-opus-4-8 | Run date: 2026-08-04 | Mode: NO-CONCALL (company) + 12 peer transcripts

## Scope and method

No main-company transcripts exist (`concalls_available: false`). Per the degradation rule I
audited B05 against the company's WRITTEN communication (AR FY2020-21 =
`Annual_Report_2022.pdf`, read pp.3-16 printed; and the Sep-2025 investor deck
`Investor_Presentation_1.pdf`, read all 9 slides). Separately I read all **12 peer transcripts
myself, fresh** and audited B06:

- GALAXYSURF: Aug 2025, Nov 2025, Feb 2026, May 2026 (all 4, full)
- ROSSARI: Oct 2025, Jan 2026, "May 2026" (dated 28 Apr 2026), Jul 2026 (all 4, full)
- FCL: Dec 2025, Feb 2026, May 2026, Jul 2026 (all 4, full)

Tooling note: peer PDFs are binary/non-greppable and the directory is not directly listable
with the tools available; filenames were recovered from the pipeline's own naming convention
(`TICKER-Concall_MMM_YYYY_Transcript.pdf`) and every one of the 12 opened successfully.

---

## PART 1 — INDEPENDENT RED-FLAG LIST (from raw sources alone)

### Company written communication (AR FY2020-21 + Sep-2025 deck)

- **IC-1** Margin/return de-rating FY2024→FY2025 shown but not explained. Standalone EBITDA
  margin 10.70%→7.56% (-29%), PAT margin 3.77%→2.27% (-40%), ROE 11.50→6.61, ROCE 17.43→11.54.
  Deck slides 6-7; no causal narrative anywhere.
- **IC-2** "Efficient Raw Material Sourcing," a named Key Competitive Advantage in AR FY2020-21
  (p.10), is absent from the deck's competitive-advantage slide (slide 3) — dropped precisely as
  the RM-cost ratio blew out.
- **IC-3** Export share fell 28.2% (AR Directors' Report p.13: exports ₹13,110 L / revenue
  ₹46,577 L) to 20% (deck slide 5 geo split) while the "30+ countries" footprint claim (slide 2)
  is repeated unchanged.
- **IC-4** Deck slide 7 is headlined **"Financial Performance and Rating Upgrade,"** but the
  ratings table on that same slide shows both ratings (CARE A- Stable; CARE BBB+ Stable) as
  **"Reaffirmed,"** not upgraded. Mislabeling a reaffirmation as an "upgrade" is a small but
  genuine over-promotion. **B05 did not flag this.**
- **IC-5** Deck leads (Milestone slide 4) with a flattering retrospective "14% sales CAGR over
  six years" while the same deck's tables show profit and every return ratio down sharply —
  selective emphasis.
- **IC-6** The AR used as the credibility baseline is the exceptional Covid-hygiene **peak** year:
  RoNW 25.14% (AR p.11, celebrated as "Continues to enjoy high return on net worth"), EPS ₹28.53
  off a ₹2.76 base. Benchmarked to that AR's own headline metric, returns collapsed to ~6.6% ROE
  by FY25 — a larger de-rating than the FY24→FY25 window B05 emphasizes.

### Peer transcripts (items relevant to AARTISURF)

- **IP-1** Capex counter-cycle: Galaxy at maintenance-only spend ("not planning anything
  significant," Aug 2025) and Rossari rephasing a formal ₹192cr plan down to ₹50-75cr (28 Apr
  2026, Sablok) and "slowed down on all the CAPEX spends" (Jul 2026) — both retreating while
  AARTISURF's CWIP accelerates.
- **IP-2** Current India demand is soft: Galaxy "2% to 4%... underlying volume growth" (Feb 2026,
  verbatim), Rossari repeatedly "soft/muted" — contradicting AARTISURF's stale 8-9.6% figures.
- **IP-3** Reformulation risk to AARTISURF's own chemistry: Galaxy (Nov 2025) describes FMCG
  customers reformulating **away from oleochemical/fatty-alcohol surfactants toward petrochemical
  alternatives** amid high feedstock. AARTISURF is an oleochemical/fatty-alcohol surfactant
  producer, so this is a VOLUME/demand risk to its product line, not only a margin risk.
- **IP-4** All three peers are rotating away from India-domestic commodity surfactants toward
  higher-value adjacencies (Rossari→pharma/aroma; FCL→US oilfield via CrudeChem; Galaxy defending
  Specialty/prestige). AARTISURF is a lone, sub-scale, undiversified expander in a segment
  better-capitalized peers are exiting.
- **IP-5** No peer names AARTISURF across 12 calls, even where an analyst raised Fineotex
  unprompted (Rossari 28 Apr 2026, Madhur Rathi).
- **IP-6** RM/feedstock inflation is real and sector-wide (Galaxy, Rossari) but an order smaller
  than AARTISURF's 29% relative EBITDA-margin collapse.
- **IP-7** Export/tariff pressure is real (Galaxy US tariff 3-5% of FY25 EBITDA; FCL "worst year
  of the decade," Indian textile exports +2.1% FY26) but no peer quantifies a surfactant
  export-share drop of AARTISURF's magnitude.
- **IP-8** Cash-conversion stretch corroborated by Rossari only (Oct 2025, one quarter,
  self-correcting); Galaxy — the closest peer — is silent.

---

## PART 2 — COMPARISON TO PIPELINE (B05 / B06)

| # | Item | Verdict vs pipeline |
|---|---|---|
| IC-1 | Unexplained margin/ROE de-rating | CAUGHT (B05 4D red flags; but see F-1 overstatement) |
| IC-2 | Dropped "efficient RM sourcing" advantage | CAUGHT (B05 §1C/2D/dropped_triggers) |
| IC-3 | Export share 28.2%→20% vs "30+ countries" | CAUGHT (B05 §1C/2A/2C) |
| IC-4 | "Rating Upgrade" title vs "Reaffirmed" reality | **MISSED** (minor) |
| IC-5 | Cherry-picked 14% CAGR vs falling returns | CAUGHT (B05 §2C over-promotion) |
| IC-6 | FY21-peak baseline understates return collapse | PARTIALLY CAUGHT (B05 benchmarks FY24, not the FY21 AR it uses) |
| IP-1 | Counter-cyclical capex | CAUGHT (B06 Q5 — flagged most consequential) |
| IP-2 | Stale demand-growth claim | CAUGHT (B06 Q2 — CONTRADICTED) |
| IP-3 | Reformulation-away-from-oleochemical demand risk | PARTIALLY CAUGHT (surfaced as Galaxy margin story, not connected to AARTISURF volume) |
| IP-4 | Peers exiting the segment AARTISURF is entering | CAUGHT (B06 Part 5) |
| IP-5 | AARTISURF unmentioned by peers | CAUGHT (B06 2D) |
| IP-6 | RM inflation real, magnitude smaller | CAUGHT (B06 Q1) |
| IP-7 | Export/tariff real, magnitude unquantified | CAUGHT (B06 Q3) |
| IP-8 | Cash stretch, single-peer/transient | CAUGHT (B06 Q6, appropriately partial) |

**Tally: 14 independent flags — 11 CAUGHT, 2 PARTIALLY CAUGHT, 1 MISSED.**

### Pipeline flags I did NOT find independently — support test

Every substantive B06 verdict is transcript-supported; I re-verified the load-bearing quotes
verbatim across all 12 calls (Galaxy 2-4% India volume; tariff 50→18%; AMET -30/-35% from peak;
CWIP ₹260cr; China cost-arbitrage quote; Rossari ₹192cr→₹50-75cr rephase; EBITDA 11.3/11.6/11.8/
12.3%; Fineotex-competitor Q&A; BASF/Dow/Chinese landscape; FCL gross margin 35.42% vs 33%,
EBITDA 15.70% vs 13.93%, WC 72 days, Texas 80k→148k→268k, export share 48% from 25%, "rolling
back" textile discounts, Indian textile export +2.1% to ₹3.16tn, "worst year of the decade," WC
79 days; FCL Dec = 100% CrudeChem, correctly UNUSED). **No B06 flag is NOT SUPPORTED or
OVERSTATED on substance.** Two imprecisions only (F-4, F-5). B05's AR/deck citations all verify
verbatim (dividend ₹3.00 / ₹2,27,53,431 p.13; "leaner and more agile" p.7; competitive-intensity
p.11; global 4.5% CAGR p.9; India 9.6/8.8/8% p.10; export 28.2%). One B05 overstatement (F-1).

---

## PART 3 — PROMISE-DELIVERY SPOT CHECKS (5 checked, 5 confirmed)

| Promise (source verified verbatim) | Outcome direction | Confirmed? |
|---|---|---|
| ₹3.00/share final dividend, ₹2,27,53,431 outflow (AR Directors' Report p.13) | Delivered | ✓ |
| "cost controlling measures to become a leaner and more agile organisation" (MD's Message p.7) | Missed (EBITDA margin 10.70→7.56) | ✓ |
| "long term outlook... continues to be positive," structural growth (MD&A p.11) | Partial (revenue grew, margins fell) | ✓ |
| "30+ countries" footprint repeated (deck slide 2) | Missed (export share 28.2→20) | ✓ |
| "industry is witnessing intensified competition as new players... enter" (MD&A p.11) | Handed to peers (partially corroborated) | ✓ |

All five earlier-source promises actually exist at the cited anchors, and each later outcome
direction is correct. Promise table is well-anchored.

---

## PART 4 — CONSOLIDATED FINDINGS (all MINOR; no CRITICAL, no MAJOR)

- **F-1 (MINOR, B05 overstatement).** B05 §2B calls the deck "the complete absence of any
  acknowledgement that a decline occurred." Overstated: deck slide 6 discloses the declines with
  explicit negative YoY columns (-29% EBITDA margin, -40% PAT margin, -33% PAT) and slide 7 shows
  FY2025 bars markedly below FY2024 for EBITDA/PAT/ROCE/ROE. What is absent is **causal
  narrative**, not acknowledgement. Core red flag (no explanation of causes) stands; the wording
  overstates it. Does not change the C grade.
- **F-2 (MINOR, B05 miss).** IC-4: slide 7 titled "…and Rating Upgrade" while both ratings are
  "Reaffirmed." Small over-promotion B05 did not surface.
- **F-3 (MINOR, B05 under-weight).** IC-6: credibility baseline is the FY21 Covid peak (RoNW
  25.14%); the multi-year return collapse to ~6.6% ROE is larger than the FY24→FY25 framing.
- **F-4 (MINOR, B06 misattribution).** B06 Q3/2E attributes the "₹5cr phenol / delayed Chinese
  shipment" hit to the Rossari "May 2026" call; the ₹5cr figure is actually stated in the Rossari
  **Jul 2026** call (Sunil Chari, re Q4). Substance correct, sourcing off by one call.
- **F-5 (MINOR, B06 unverified figure + date label).** B06 Q5 cites Galaxy's "cumulative ~₹480cr
  over the prior 3 years (Nov 2025 call)"; I confirmed CWIP ~₹260cr but could not independently
  locate ₹480cr in the pages read (defer existence-of-number to Verifier A). Separately, B06
  labels the Rossari Q4/FY26 call "May 2026"; the transcript is dated **28 Apr 2026** (follows the
  filename). Neither affects a verdict.
- **F-6 (MINOR, B06 under-connect).** IP-3: the oleochemical→petrochemical reformulation
  substitution (Galaxy) is surfaced as Galaxy's own margin story under Q1 but not extended as an
  AARTISURF-specific **volume/demand** risk, which is the more thesis-relevant read given
  AARTISURF's fatty-alcohol chemistry.

## Credibility grade

**Concur with C.** B05's degraded-mode C is well-supported: one trivial delivered promise
(dividend) against two missed qualitative commitments with material unexplained deterioration.
If anything, the peer cross-read (a lone, sub-scale, undiversified, name-unrecognized
counter-cyclical expander in a segment three better-capitalized peers are exiting) makes the
qualitative picture modestly worse than a bare C, but the thin evidence base and no-concall
floor make C the right call. No basis to grade higher.

## Bottom line

Both B05 and B06 are accurate and thorough. Independent reading corroborated every load-bearing
citation. No fabricated or decision-changing missed signal; no repeated multi-quarter evasion
(none can exist in no-concall mode). Findings are six MINOR items — one genuine missed company
red flag (rating "upgrade" vs "reaffirmed"), one B05 overstatement, and four small B06/B05
imprecisions.

```yaml
stage: B12b
company: "AARTISURF"
run_date: "2026-08-04"
model: claude-opus-4-8
status: complete
independent_flags_found: 14
caught: 11
partially_caught: 2
missed:
  - {severity: "MINOR", item: "Deck slide 7 headlined 'Financial Performance and Rating Upgrade' while both CARE ratings (A- / BBB+ Stable) are shown as 'Reaffirmed', not upgraded — over-promotion B05 did not flag", anchor: "Investor_Presentation_1.pdf slide 7"}
pipeline_flags_not_supported: []
promise_delivery_spot_checks: {checked: 5, confirmed: 5, wrong: 0}
credibility_grade_concur: "concur — C; peer cross-read (lone counter-cyclical undiversified expander) arguably worse, but thin evidence base and no-concall floor keep it at C"
findings:
  - {severity: "MINOR", location: "B05 §2B", claim: "'complete absence of any acknowledgement that a decline occurred'", assessment: "OVERSTATED — deck discloses declines numerically (slide 6 negative YoY columns; slide 7 comparative bars); absent is causal narrative, not acknowledgement", anchor: "Investor_Presentation_1.pdf slides 6-7"}
  - {severity: "MINOR", location: "B05 §2C/4D", claim: "deck offers no acknowledgement / over-promotion set", assessment: "MISSED — 'Rating Upgrade' slide title vs 'Reaffirmed' ratings", anchor: "Investor_Presentation_1.pdf slide 7"}
  - {severity: "MINOR", location: "B05 §4C credibility_basis", claim: "delivery benchmarked to FY24", assessment: "PARTIALLY CAUGHT — FY21 AR baseline (RoNW 25.14%) implies a larger multi-year return collapse to ~6.6% ROE", anchor: "Annual_Report_2022.pdf p.11; deck slide 7"}
  - {severity: "MINOR", location: "B06 Q3/2E", claim: "'May 2026 call... Rs5cr hit from delayed Chinese phenol shipments'", assessment: "MISATTRIBUTED — Rs5cr phenol figure is stated in ROSSARI Jul 2026 call (re Q4), not the Apr/May call; substance correct", anchor: "ROSSARI-Concall_Jul_2026 p.13"}
  - {severity: "MINOR", location: "B06 Q5", claim: "Galaxy 'cumulative ~INR480cr over prior 3 years (Nov 2025)' and Rossari 'May 2026' call", assessment: "INR480cr not independently locatable (CWIP ~INR260cr confirmed; defer to Verifier A); Rossari Q4 call actually dated 28 Apr 2026", anchor: "GALAXYSURF-Concall_Nov_2025; ROSSARI-Concall_May_2026 (dated 28 Apr 2026)"}
  - {severity: "MINOR", location: "B06 Q1/2B", claim: "reformulation away from oleochemical surfactants", assessment: "PARTIALLY CAUGHT — surfaced as Galaxy margin story, not connected as an AARTISURF-specific volume/demand risk given its fatty-alcohol chemistry", anchor: "GALAXYSURF-Concall_Nov_2025 pp.3-9"}
critical_count: 0
major_count: 0
minor_count: 6
acceptance_rate: 79            # caught (11) / independent flags found (14)
```
