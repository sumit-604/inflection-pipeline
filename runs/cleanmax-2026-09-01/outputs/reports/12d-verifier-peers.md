# VERIFIER D: PEER COVERAGE AUDIT
Company: CLEANMAX | Run date: 2026-09-01 | Model: claude-sonnet-5

Scope: did the pipeline actually use the 19 peer transcripts it claims to have used
(KPIGREEN x4, ORIANA x3, ACMESOLAR x4, ADANIGREEN x4, JSWENERGY x4)? Audited against
B06 (06-peers.md) Parts 1-3 and the B05 peer_questions list (6 claims). NTPCGREEN has
screening data only, no concall transcript, so it is out of scope for this audit and
correctly absent from B06's peer set.

---

## PART A: PER-PEER COVERAGE AUDIT (Rule 2 - SUBSTANTIVE citation check)

19 transcripts, 14 marked SUBSTANTIVE, 5 marked CITED-ONLY, 0 marked UNUSED.

| Peer / call | B06 label | Citation checked | Result |
|---|---|---|---|
| KPIGREEN Q1 FY27 (Aug 2026) | SUBSTANTIVE | "geopolitical conditions" framing; 16% actual vs 20-30% expected growth | CONFIRMED (lines 152-153, 387-390, and "geopolitical" used repeatedly lines 322-1010) |
| KPIGREEN Q4 FY26 (May 2026) | SUBSTANTIVE | Khavda revenue-recognition delay, unenergised GSECL substation | CONFIRMED (lines 620-648) |
| KPIGREEN Q3 FY26 (Feb 2026) | SUBSTANTIVE | CPP-vs-IPP margin split; 24-month RFQ-to-execution data-centre lag | CONFIRMED. IPP 85-90% vs CPP figures: transcript gives "18% to 20%" (line 571) and, in an analyst's framing, "20% or 22%" (line 564) for CPP margin in different sub-contexts — B06's compressed "18-22%" is a reasonable rounding of both figures but is not a single verbatim number (MINOR imprecision). 24-month RFQ lag confirmed verbatim (lines 1522-1524). |
| KPIGREEN Q2 FY26 (Nov 2025) | SUBSTANTIVE | Data-centre/life-sciences JV, 2-3 year horizon, no revenue yet | CONFIRMED (lines 1085-1116, "2 to 3 years") |
| ORIANA Q4 FY26 (Jun 2026) | SUBSTANTIVE | ALMM1/ALMM2 31-Aug-2025 cutover front-loading; commodity/currency cost shock figures | CONFIRMED, high fidelity. "We have been aggressive there... we knew this was going to be tough after this scenario" verbatim (lines 566-572); ALMM1/2 cutover date confirmed (lines 561-565); silver +130-180%, copper +30-40%, steel +25-30%, aluminium +30-40%, polysilicon ~30%/glass 30-35%, crude +88% (Apr'25-Mar'26), INR 84.5->95 all confirmed verbatim (lines 168-181) |
| ORIANA Q2 FY26 (Dec 2025) | SUBSTANTIVE | "curtailment is a utility-scale problem, not C&I" framing | CONFIRMED verbatim: "specifically for utility-scale projects... we are largely into the C&I segment" (lines 845-847) |
| ORIANA Q1 FY26 (Jun 2025) | CITED-ONLY | General C&I long-term PPA/margin commentary | CONFIRMED as general/non-decisive; spot-read found no curtailment, GNA/TGNA, data-centre or market-share content that should have been elevated to SUBSTANTIVE |
| ACMESOLAR Q1 FY27 (Aug 2026) | SUBSTANTIVE | Curtailment ~1% of revenue; TGNA commissioning caution; 91% ex-BESS margin | CONFIRMED verbatim on all three (lines 657-660, 938-939, 1242) |
| ACMESOLAR Q4 FY26 (May 2026) | SUBSTANTIVE | 88-89% EBITDA margin (seasonally softer quarter) | CONFIRMED ("87%... in the range of 88%, 89%", line 275) |
| ACMESOLAR Q3 FY26 (Feb 2026) | SUBSTANTIVE | TRAS-Down/GNA mechanism; 91.5% vs 89.6% margin; 20.6% cash ROE | CONFIRMED verbatim, all three figures exact (lines 598-601, 208-210) |
| ACMESOLAR Q2 FY26 (Nov 2025) | SUBSTANTIVE | ALMM/module-cost-gap direction; **Sikar curtailment loss of Rs17.5 Cr**; 89% margin | ALMM direction and 89% margin CONFIRMED (lines 225-228, 288-299). **Sikar Rs17.5 Cr figure NOT FOUND in this transcript** (targeted search for "17.5" and "curtailment loss" returns zero matches). The figure actually appears in the **Feb 2026 (Q3 FY26)** transcript instead (line 159: "one-time curtailment loss of about 17.5 crores in our 300 megawatt Sikar project"). This is a wrong-transcript citation — MAJOR. |
| ADANIGREEN Q1 FY27 (Jul 2026) | SUBSTANTIVE | Khavda curtailment 5-7% of EBITDA | CONFIRMED verbatim (lines 156-157) |
| ADANIGREEN Q3 FY26 (Jan 2026) | CITED-ONLY | "14% of countrywide capacity addition" — different metric from CleanMax's C&I share claim | CONFIRMED correctly distinguished (lines 68-69). However, this call also contains a substantive curtailment Q&A (why curtailment appeared this quarter vs last, resolution via grid augmentation, lines 197-233) that B06 did not use — see Part B. |
| ADANIGREEN Q4 FY26 (Apr 2026, transcript 2) | SUBSTANTIVE | Khavda curtailment CUF impact 2.5-3% | CONFIRMED verbatim: "because of curtailment about 2.5% to 3% of CUF impact" (lines 1061-1063) |
| ADANIGREEN Q4 FY26 (Apr 2026, transcript 1) | CITED-ONLY | General Khavda progress, battery-capacity commentary | CONFIRMED as general/non-decisive; spot-read for curtailment/GNA/TGNA/data-centre/market-share terms returns no hits |
| JSWENERGY Q1 FY27 (Jul 2026) | SUBSTANTIVE | 400 MW ex-O2 Power Rajasthan TGNA, connectivity slipping to Sept/Oct; 69 MU curtailment | CONFIRMED verbatim, both items (lines 586-589, 730) |
| JSWENERGY Q4 FY26 (May 2026) | CITED-ONLY | Merchant-tariff premium ~20% over exchange price | CONFIRMED as stated (line 136: "approximately 20% plus premium"). But this call also contains directly claim-relevant curtailment content B06 did not use — see Part B, rated MAJOR. |
| JSWENERGY Q3 FY26 (Jan 2026) | CITED-ONLY | Same merchant-premium theme | CONFIRMED as stated (line 190: "20% premium to the average exchange prices"). Also contains a GNA/TGNA curtailment exchange not used — see Part B, rated MINOR (redundant with Oct2025 citation already used). |
| JSWENERGY Q2 FY26 (Oct 2025) | SUBSTANTIVE | Explicit GNA-vs-TGNA revenue-protection framework | CONFIRMED verbatim, this is the clearest statement of the mechanism in the corpus (lines 465-522) |

**Substantive citations checked: 14. Confirmed clean: 13. Wrong-transcript citation: 1 (ACMESOLAR Nov 2025 / Sikar Rs17.5 Cr).**

---

## PART B: UNUSED-BUT-RELEVANT AUDIT (Rule 3 - CITED-ONLY spot-read)

Spot-read of all 5 CITED-ONLY transcripts for claim-relevant material B06 should have used.

1. **JSWENERGY Q4 FY26 (May 2026) — MAJOR.** B06 labels this call CITED-ONLY for the
   merchant-premium theme only. It also contains a directly Claim-6-relevant, quantified
   curtailment disclosure the pipeline did not use: "about 160 million units were curtailed
   for us but a significant portion of this 160 MUs is under permanent recovery. So, we are
   getting the tariff for the same, thus not impacting our revenue. Only a small portion of
   this curtailment has resulted in a revenue loss of around ₹16 crores during the quarter and
   approximately ₹50 crores during the year gone by" (lines 232-240). This is a third
   independent, Rs-Cr-quantified confirmation of the GNA revenue-protection mechanism B06
   calls "the single most consequential finding" of the stage, and it gives a real-world
   Rs-Cr scale comparator (₹16-50 Cr) against which CleanMax's disclosed ~₹170 Cr full-year
   Bikaner impact can be sense-checked. Leaving it out of Part 1's Claim 6 analysis is a
   material coverage gap.

2. **JSWENERGY Q3 FY26 (Jan 2026) — MINOR.** Also CITED-ONLY for merchant premium only.
   Contains a further GNA-vs-TGNA exchange ("there are 2 types of curtailment... against the
   G&A... temporary grid connected -- connectivity gets curtailed wherein there is a financial
   impact. So our portion is significantly small," lines 861-874) that reinforces the same
   mechanism already established via the Oct 2025 JSW call and the Feb 2026 ACME call. Relevant
   but largely redundant with citations already in use — an industry-context miss rather than a
   new decisive data point.

3. **ADANIGREEN Q3 FY26 (Jan 2026) — MINOR.** CITED-ONLY for the "14%" capacity-addition
   figure only. Also contains a curtailment Q&A (why curtailment appeared this quarter vs
   last, resolving with grid augmentation, lines 197-233) reinforcing the industry-wide
   curtailment direction already well corroborated by three other peers in B06. Redundant,
   not decisive — MINOR.

4. **ORIANA Q1 FY26 (Jun 2025) and ADANIGREEN Q4 FY26 (Apr 2026, transcript 1) — no issue.**
   Targeted spot-reads for curtailment / GNA / TGNA / data-centre / market-share / hyperscaler
   language returned no hits in either transcript. CITED-ONLY is the correct label for both.

No transcript was left fully UNUSED; B06's Part 3 table accounts for all 19.

---

## PART C: VERDICT-DISCIPLINE AUDIT (Rules 4-5)

**Rule 4 — VERIFIED claims need ≥2 independent peer anchors.** B06 issues zero full
VERIFIED verdicts across its 6 claims (0 VERIFIED / 4 PARTIALLY VERIFIED / near-3-way split
on the rest, per B06's own Part 4 tally). No claim was upgraded to VERIFIED on single-peer
evidence, so the hard trigger in Rule 4 does not fire anywhere in this report. One
observation worth carrying forward: within Claim 4, the 89-91% utility-scale EBITDA-margin
corroboration rests on ACME Solar alone across three quarters (Aug 2026 / Feb 2026 / May 2026)
— technically one peer entity, not two independent peers, even though it is three separate
calls. B06 correctly kept this at PARTIALLY VERIFIED rather than promoting it to VERIFIED,
which is the right discipline call given Rule 4's independence requirement; flagged here as
an observation, not a rule violation.

**"Verdict upgraded from silence" (CRITICAL trigger) check.** Reviewed all 6 claim verdicts
for any case where peer silence was read as confirmation. None found — e.g., Claim 4's "superior
cash ROE" half is explicitly flagged as un-checkable rather than assumed true; Claims 1, 2, 5
are left UNVERIFIABLE rather than quietly passed. No CRITICAL findings under this rule.

**Rule 5 — every B05 peer_questions item gets a verdict.** B05's peer_questions list contains
exactly 6 items (market share, green-PPA TAM, module-cost gap/ALMM2, C&I tariff premium/margin,
hyperscaler conversion ratio, Bikaner curtailment). B06 Part 1 addresses all 6, one-to-one, as
Claims 1 through 6. No skipped claim. **claims_all_addressed: true.**

---

## PART D: SEVERITY SUMMARY

| # | Finding | Severity | Location |
|---|---|---|---|
| 1 | ACMESOLAR Q2 FY26 (Nov 2025) row cites a Sikar Rs17.5 Cr curtailment-loss figure that does not appear in that transcript; the figure is actually from the Q3 FY26 (Feb 2026) transcript | MAJOR | B06 Part 3, ACMESOLAR row 4; source: ACMESOLAR-Concall_Feb_2026_Transcript.txt line 159 |
| 2 | JSWENERGY Q4 FY26 (May 2026): 160 MU curtailment / ₹16-50 Cr revenue-loss disclosure, directly relevant to Claim 6's GNA-protection mechanism, left unused | MAJOR | JSWENERGY-Concall_May_2026_Transcript.txt lines 232-240 |
| 3 | JSWENERGY Q3 FY26 (Jan 2026): GNA/TGNA curtailment exchange left unused (redundant with existing citations) | MINOR | JSWENERGY-Concall_Jan_2026_Transcript.txt lines 861-880 |
| 4 | ADANIGREEN Q3 FY26 (Jan 2026): curtailment Q&A left unused (redundant with existing citations) | MINOR | ADANIGREEN-Concall_Jan_2026_Transcript.txt lines 197-233 |
| 5 | KPIGREEN Q3 FY26 (Feb 2026): "18-22%" CPP margin compresses two distinct figures (18-20% management answer; 20-22% analyst framing) from the same call into one range | MINOR | KPIGREEN-Concall_Feb_2026_Transcript.txt lines 564, 571 |

CRITICAL: 0. MAJOR: 2. MINOR: 3.

---

## PART E: COVERAGE ARITHMETIC

- Peers/transcripts audited: 19 of 19 (all rows in B06 Part 3)
- Rows with a clean, fully-confirmed citation set: 15 of 19
- Rows with an issue: 4 of 19 (1 wrong-transcript citation; 3 unused-but-relevant misses)
- acceptance_rate = 15/19 = 78.9%, rounded to 79%

The 79% rate sits above the 60% REWORK floor. B06's overall shape (14 SUBSTANTIVE peers
genuinely used, disciplined non-upgrading of PARTIALLY VERIFIED claims, all 6 injected
questions addressed) is sound; the defects found are a real, correctable citation error and
two missed-but-not-decisive curtailment data points, not a pattern of fabrication or
verdict inflation.

---

```yaml
stage: B12d
company: "CLEANMAX"
run_date: "2026-09-01"
model: claude-sonnet-5
status: complete
peers_audited: 19
substantive_confirmed: 13
substantive_unsupported:
  - "ACMESOLAR Q2 FY26 (Nov 2025): Sikar Rs17.5 Cr curtailment-loss citation not found in this transcript; figure actually appears in ACMESOLAR Q3 FY26 (Feb 2026) transcript, line 159"
unused_but_relevant:
  - {peer: "JSWENERGY Q4 FY26 (May 2026)", missed_item: "160 MU curtailed, ~Rs16 Cr quarterly / ~Rs50 Cr annual revenue loss with most under GNA permanent-recovery protection - a third, Rs-Cr-quantified confirmation of the GNA revenue-protection mechanism central to Claim 6, and a real-world scale comparator to CleanMax's ~Rs170 Cr Bikaner impact", anchor: "JSWENERGY-Concall_May_2026_Transcript.txt, lines 232-240"}
  - {peer: "JSWENERGY Q3 FY26 (Jan 2026)", missed_item: "GNA-vs-TGNA curtailment exchange ('our portion is significantly small') reinforcing Claim 6 mechanism; redundant with Oct2025/Feb2026 citations already used", anchor: "JSWENERGY-Concall_Jan_2026_Transcript.txt, lines 861-880"}
  - {peer: "ADANIGREEN Q3 FY26 (Jan 2026)", missed_item: "Curtailment Q&A reinforcing industry-wide curtailment direction for Claim 6; redundant with Jul2026/Apr2026 citations already used", anchor: "ADANIGREEN-Concall_Jan_2026_Transcript.txt, lines 197-233"}
claims_all_addressed: true
verdict_discipline_fails: []
findings:
  - {severity: "MAJOR", location: "B06 Part 3, ACMESOLAR Q2 FY26 (Nov 2025) row", claimed: "Sikar (Rajasthan) curtailment loss of Rs17.5 Cr, cited to Nov 2025 transcript", source_truth: "Figure appears in ACMESOLAR Feb 2026 (Q3 FY26) transcript line 159, not in Nov 2025 transcript (zero matches for '17.5' or 'curtailment loss')", note: "Wrong-transcript citation; underlying fact is true but misattributed to the wrong call"}
  - {severity: "MAJOR", location: "B06 Part 3, JSWENERGY Q4 FY26 (May 2026) row", claimed: "CITED-ONLY, merchant-tariff premium only", source_truth: "Transcript also contains 160 MU curtailment / Rs16-50 Cr revenue-loss GNA-protection disclosure directly relevant to Claim 6", note: "Directly claim-relevant peer statement left unused"}
  - {severity: "MINOR", location: "B06 Part 3, JSWENERGY Q3 FY26 (Jan 2026) row", claimed: "CITED-ONLY, merchant-tariff premium only", source_truth: "Transcript also contains a GNA/TGNA curtailment exchange, redundant with citations already in use", note: "Industry-context miss, not decisive"}
  - {severity: "MINOR", location: "B06 Part 3, ADANIGREEN Q3 FY26 (Jan 2026) row", claimed: "CITED-ONLY, 14% capacity-addition figure only", source_truth: "Transcript also contains curtailment Q&A, redundant with citations already in use", note: "Industry-context miss, not decisive"}
  - {severity: "MINOR", location: "B06 Part 1, Claim 4 evidence (KPIGREEN Feb 2026)", claimed: "KPI Green CPP EBITDA margin 18-22%", source_truth: "Transcript gives 18-20% (management direct answer, line 571) and 20-22% (analyst-framed figure, line 564)", note: "Compressed range is a reasonable rounding, not a single verbatim figure"}
critical_count: 0
major_count: 2
minor_count: 3
acceptance_rate: 79
```
