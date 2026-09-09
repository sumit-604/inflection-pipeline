# REWORK

TOTEM (Forbes Precision Tools and Machine Parts Ltd, BSE 544186)
Run: runs/totem-2026-09-09 | Phase 1 gate recommendation | 2026-09-09
Verdict rule applied: rule 1 (confidence delta forces REWORK).

PHASE 1 SCOPE NOTE. Stages 10 and 11 did not run. There is no valuation, no
destination PE, no Hurdle verdict, no entry zone, no fair value and no BUY,
WATCHLIST or AVOID call in this file. This is a go or no go on the evidence
pack alone.

## What REWORK means here

REWORK judges the ANALYSIS, not the business. Nothing in this pack halts on
company quality, and the framework has no halt for company quality.

The numbers are sound. Verifier A checked 87 material figures across all nine
stage reports against the sources and found zero mismatches, zero missing
anchors and zero source fidelity failures. Every figure in this pack traces to
a filing.

What is incomplete is the reading of management communication at stage 5 and
the peer verdict discipline built on top of it at stage 6. Verifier B read the
same filings independently and found 47 red flag grade items. It judged that
stages 5 and 6 caught 15 outright and partially caught 8, with one CRITICAL
miss and five claims the reports make that the sources do not support.

Three verifier cycles ran where the pipeline specifies one. Stage 5 and stage 6
were each rewritten twice against the findings. Verifier B's found item count
went 19, then 33, then 47, while the catch count went 4, then 16, then 15. The
ratio fell because the denominator grew, not because the work degraded. That
pattern is itself evidence about this company's disclosure quality.

## The rework list

The rework list is already written. It is the `missed[]` and
`pipeline_flags_not_supported[]` arrays in
`runs/totem-2026-09-09/outputs/blocks/B12b.yaml`, and the `findings[]` array in
`runs/totem-2026-09-09/outputs/blocks/B12d.yaml`. A rerun works those lists.

The five NOT SUPPORTED items come first, because they are claims the pack
currently makes that the sources do not carry.

**NS-1 (MAJOR) — 05-concall.md, pledge and dividend chain.** The report calls
Reading A, a share transfer after the record date, the more likely reading, and
states Shapoorji Pallonji and Company collected Rs 1,871.86 lakh. AR2026 note
30 p.108 states the dividend paid as Rs 1,798.36 lakh to Shapoorji Pallonji and
Company and Rs 106.50 lakh to Forbes Campbell. Rs 106.50 lakh at Rs 5 a share
is 2,130,000 shares, against 665,592 held at 31-Mar-2025, so the 1,470,000
share transfer completed BEFORE the 02-May-2025 record date. Reading B is
confirmed and Reading A is excluded. The report quotes the resolving figure
without recognising it.

**NS-2 (MAJOR) — 05-concall.md, the correction section.** The report uses the
Wendt AGM line "Commodity prices stayed largely stable" as the nearest in
window peer datapoint against TOTEM's FY26 abnormal commodity claim. WENDT p.3
places that sentence inside the Chairman's calendar 2024 global economy scene
setter. It covers CY2024, which is TOTEM's FY25 and not FY26, and it is a
global macro remark, not a carbide or steel price statement. Stage 5 states it
did not read the transcript. Wrong period, wrong subject, unread, and used to
support a HIGH flag.

**NS-3 (MAJOR) — 06-peers.md Part 5 and 05-concall.md trigger 1.** The reports
claim the Q1 FY27 margin jump follows directly from the company's own capex
delivery, confirmed in the FY26 annual report. Nothing in the corpus links
them. The Q1 FY27 filing carries four boilerplate notes, no commentary, no
segment data and no utilisation data. Three untested alternatives exist: Q1
FY26 was FY26's trough quarter, headcount fell 61 during FY26, and other
expenses fell 5% in absolute terms on revenue up 29% under a bare regrouping
note.

**NS-4 (MAJOR) — 05-concall.md ruling on the commodity claim.** The report
rules that the FY26 abnormal commodity prices sentence does not survive the
three year CIF series, at plus 1.23% for FY26 against FY24. That is overstated.
CIF is an import value, price times quantity. In the same year raw material
inventory nearly tripled, from Rs 738.71 lakh to Rs 1,993.71 lakh at note 8
p.92, and consumption rose 25.3%. A flat value against FY24 is consistent with
higher prices on lower volumes. The series REMOVES support; it cannot refute.
The correct ruling is UNEVIDENCED, not refuted. Stage 5 promotes it to a HIGH
flag and a hard delivery tracker fail.

**NS-5 (MAJOR) — 06-peers.md Part 2D.** The report sizes TOTEM at about
Rs 290 cr FY26 revenue. AR2026 p.70 states revenue from operations
Rs 25,101.13 lakh, that is Rs 251.0 cr, and total income Rs 25,473.95 lakh,
that is Rs 254.7 cr. Rs 290 cr appears in no source read, and it is used to
size TOTEM against peers. Verifier A is the binding authority on whether a
number exists in a source and did not check this cell, so the item stands open,
not cleared.

Two MINOR NOT SUPPORTED items follow. NS-6: stage 5 says three HR leadership
transitions in about nine months while stage 6 says two exits inside roughly
eight months, from the same two exits and one appointment in the same corpus.
NS-7: the stage 5 working capital row cites debtor days still low and debtor
days worsening 108% in the same cell, and never states that FY26 debtor days
IMPROVED to 46 at AR2026 p.26.

Beyond those seven, the rerun must work the one CRITICAL miss and the 18 MAJOR
misses in B12b, and the five MAJOR findings in B12d, of which the largest are
the unverdicted market share peer question, the Kennametal 250 to 300 basis
point market share gain quoted only for its refusal clause, and a quote
attributed to a 22 page transcript at p.27 to 28.

## Transition posture

NOT CLASSIFIABLE in phase 1. The recognition gap variable resolves at stage 11,
which has not run. The proof gate and the ugliness classification are not
carried forward here without it.

## Phase 1 confidence delta

| Component | Score | Source | Note |
|---|---|---|---|
| Numerical acceptance | 100 | B12a (verifier A, cycle 3) | 87 numbers checked, zero mismatch, zero source fidelity findings, zero CRITICAL |
| Red flag coverage | 32 | B12b (verifier B, cycle 3) | 47 found, 15 caught, 8 partial, 1 CRITICAL miss, 5 NOT SUPPORTED |
| Framework adherence | 90.2 | B12c (verifier C, cycle 2, governing) | 83 of 92 rule checks passed, zero CRITICAL, Gate 0 and Emerging Moat scope only |
| Peer utilisation | 65 | B12d (verifier D, cycle 3) | citation fidelity about 28 of 30 clean, coverage and verdict discipline gapped |
| **Overall** | **32** | confidence.yaml | below 60, forced REWORK |

Weakest component: red flag coverage at 32. It governs the verdict. The
valuation adherence half of verifier C is deferred to phase 3 because B10 and
B11 do not exist.

## FLAG-PROMOTER

**Verdict: CONCERN.** Deal breaker fired: promoter pledge above 40%.

Top findings.
1. 94.4% of the 73.85% promoter holding is pledged, which is 100% of Shapoorji
   Pallonji and Company's own 69.71% direct stake. 35,967,172 shares, unchanged
   across the Jun-2025, Mar-2026 and Jun-2026 filings. The pledgee is Catalyst
   Trusteeship Limited, the same trustee used for the SP Group's Afcons
   Infrastructure pledges. Forbes Campbell's 4.14% stayed unpledged throughout.
   (B08; shareholding__SHP_30Jun2026.txt / 31Mar2026.txt / 30Jun2025.txt,
   Table II)
2. The promoter group is in a live, currently downgraded refinancing crisis.
   CareEdge cut the Goswami Infratech NCD to B+ in May 2026 and the repayment
   deadline slipped from April to June 2026. (B08, media reported tier)

Supporting findings on the record. The pledge is absent from all three annual
reports, FY24, FY25 and FY26, though it was named as a risk factor in the
June 2024 Information Memorandum p.16. A SEBI adjudication order fined
Shapoorji Pallonji and Company Rs 7 lakh for LODR non compliance on its own
NCDs on 30-Aug-2023. Disputed tax exposure of about Rs 172 cr and three
operational creditor NCLT petitions were pending against the promoter as of
mid 2024. MD remuneration rose 74.7%, from Rs 265.52 lakh to Rs 464.00 lakh,
against the Board's Report's own stated average 7.5% KMP increase, in a year
PAT rose 0.1%. (B08; Information Memorandum 2024 p.16, p.90, p.152, p.153;
AR2026 note 30 and Annexure II)

The operating company is clean. TOTEM extends no loans, no inter corporate
deposits and no guarantees to the promoter group. The auditor record is clean
with an unmodified opinion and unmodified IFC. The Secretarial Compliance
Report is clean. The only material promoter cash flow is the Rs 19.05 cr FY26
dividend. (B02 findings 7 and 10; B03)

Transition evidence, as B08 records it: PARTIAL. The SP Group is deleveraging
at group level through the SWREL stake divestment, the Afcons Infrastructure
2024 IPO monetisation and a planned Tata Sons stake monetisation after listing.
There is no reduction in the TOTEM specific pledge to date; it is stable at
94.4% through June 2026.

## FLAG-CASH

**Determination: INDETERMINATE.**

Operating cash flow fell from Rs 51.32 cr to Rs 27.55 cr in FY26, a 46% fall,
on an inventory build from Rs 31.93 cr to Rs 56.42 cr, up 76.7%. The quick
ratio fell from 1.43 to 0.99, below 1.0 for the first time. CFO to PAT fell
from 1.79x to 0.96x. Receivables improved modestly over the same year, from
about 49 days to about 46 days on the company's own average balance basis, so
this is an inventory story and not a collections story. (B02 findings 1 and 2,
note 8 PDF p.92, cash flow statement PDF p.71, note 33.2; B03 phase 3B)

Why it cannot be settled. The annual report gives no inventory ageing, no write
down and no movement in the obsolescence provision, even though the company's
own policy at note 2B(v) names obsolescence a critical judgement. The auditor's
sole Key Audit Matter is revenue recognition, not inventory. Stock pre built
for the drill ramp and stock that did not sell are indistinguishable from these
filings.

The one external support offered for the raw material half was withdrawn. The
60.2% rise in CIF imports is a rebound off a depressed FY25; on the three year
series FY26 sits only 1.2% above FY24 (Rs 2,885.65 lakh FY24, Rs 1,823.74 lakh
FY25, Rs 2,921.18 lakh FY26). Verifier B adds that an import value is price
times quantity, so the series removes support without refuting the price claim
either way (B12b NS-4). The correct standing is UNEVIDENCED.

Rating agency verbatim quote on working capital: NOT FOUND. The `rating/` input
folder is empty. No rating rationale exists in this corpus. The IVR BBB/Stable
rating referenced at AR2026 p.54 was assigned 05-Dec-2024 and has gone
unreviewed for about 17 months (B12b, MINOR).

Missing evidence, named. First, the inventory ageing and net realisable value
disclosure, expected in the FY27 annual report at the note 8 equivalent.
Second, a credit rating rationale with working capital commentary, obtainable
from the rating agency's published rationale. Neither exists in this corpus.

Rule applied. Under the CLAUDE.md rule and the orchestrator's FLAG-CASH rule,
INDETERMINATE never silently resolves to PROCEED and caps at PROCEED WITH
CAVEATS with the missing evidence named. That cap is not what governs here.
REWORK is more severe and stands on its own grounds under verdict rule 1.

## Contradicted claims

One claim reached CONTRADICTED at the peer stage. It is the priority monitoring
item.

| Subject claim | Contradicting peer | Anchor |
|---|---|---|
| TOTEM AR FY25: "improving trend in the export business performance" | WENDT INDIA | WENDT AGM, meeting 21-Jul-2025, p.3: "Exports were at Rs 43.63 crores during the year, lower by 12% over the previous year due to reduced offtake from key customers from a few countries". Subject side anchor: annual-report__Annual_Report_2025.txt p.19. Kept at CONTRADICTED on a stated asymmetric bar rationale. |

Two claims stay UNVERIFIABLE: distributor and channel inventory behaviour in
2025 and 2026, and the US and Mexico tariff impact on Indian cutting tool
exports. Both peers were checked; the tariff question was asked by a Wendt
shareholder on the record and never answered (WENDT p.20 to 22).

Verifier D flags the CONTRADICTED verdict as incompletely defended. It rests on
one peer with a company specific cause, and TOTEM's own FOB series already
establishes the same direction more directly. The direction holds; the
attribution to a peer is the part that needs rework.

Verifier B raises a second, harder contradiction that stages 5 and 6 did not
grade. The FY26 MD&A calls exports a "stable trend" while FOB exports fell
15.9%, from Rs 3,791.05 lakh to Rs 3,189.46 lakh, and the FY25 report called
the same direction "improving". Two consecutive periods stating the export
direction backwards, disclosed correctly only in the section 134(3)(m)
annexure. That is the single CRITICAL miss (AR2026 p.25 against p.42; AR2025
p.19 against p.33; AR2024 p.29).

## Monitorables

Eight items, deduplicated across stages 3, 4, 7 and 9.

1. Operating margin in the Q2 FY27 results, due about November 2026. It must
   hold above 20% for a second consecutive quarter. Q1 FY27 was 22.9% against
   16.1% a year earlier and 16.4% for FY26 as a whole. This is the one number
   that separates a capacity gain from a soft base.
2. Inventory ageing or net realisable value disclosure in the FY27 annual
   report, at the note 8 equivalent. Any ageing table or write down at all. It
   is the only disclosure that can settle whether the Rs 56.4 cr inventory is
   ramp stock or dead stock.
3. Operating cash flow and inventory days in the FY27 annual report. CFO back
   at or above PAT, and inventory moving back toward the FY25 level of
   Rs 31.9 cr. Tests whether the FY26 build was deliberate and temporary.
4. Promoter pledge percentage in the September and December 2026 quarterly
   shareholding filings. Any move off 94.4%. A rise is a hard flag, a fall is
   the first real deleveraging signal on this specific block.
5. FOB export earnings in the FY27 annual report, Annexure IV forex earnings.
   It must clear the FY24 baseline of Rs 3,834.10 lakh. A third consecutive
   year below that level kills the export recovery trigger.
6. Raw material cost as a share of sales in the quarterly results. The healthy
   band is 32% to 35%; above 37% for two straight quarters is the margin
   failure signal. Q1 FY27 net material cost was 36.1% against 32.2% for FY26.
7. Kennametal India quarterly results on BSE, read beside TOTEM's own. If
   Kennametal keeps growing at its June 2026 pace while TOTEM slows, the growth
   was the cycle and not share gain.
8. MD remuneration against the stated average KMP increase in the FY27 annual
   report, note 30 against Annexure II. A reconciliation, or a repeat of the
   same unexplained gap, tests whether the FY26 disclosure defect was an
   isolated error.

## Falsification line

Q2 FY27 operating margin printing back near 16% on revenue growth in single
digits. That single print removes the only delivered leg of the transition
claim and confirms Q1 FY27 as a soft base artifact.

## Publish check

No publish candidate this analysis.
