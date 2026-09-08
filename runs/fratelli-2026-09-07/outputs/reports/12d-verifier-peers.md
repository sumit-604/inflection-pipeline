# VERIFIER D: PEER COVERAGE AUDIT — FRATELLI VINEYARDS
## Audit of outputs/blocks/B06-peers.yaml + outputs/reports/06-peers.md (run 2, current)

Audited against: 12 peer transcripts (SULA x4, TI x4, SDBL x4) in
work/text/peer-concalls/, 6 peer investor presentations in
work/text/peer-presentation/, and B05-concall.yaml's peer_questions list.
Run-1 archived artifacts (06-peers-run1.md, B06-peers-run1.yaml,
B05-concall-run1.yaml) were not consulted, per the task's "ignore entirely"
instruction.

This run's own run_note states the rerun was specifically told: "citation
anchors must be confirmed against the page marker before writing." That rule
was not fully honoured. Six of twenty-four spot-checked citation anchors
(25%) resolved to the wrong page or the wrong document.

---

## PART 1: CITATION ANCHOR SPOT-CHECK

24 citations were located in the source .txt files against the page markers
cited by B06. Method: grep the exact quoted text or figure, find the nearest
preceding `===== PAGE N =====` marker, compare to B06's cited page.

| # | Claim / figure | B06 cites | Actual page | Result |
|---|---|---|---|---|
| 1 | "85% or 90%... duopoly" quote | Concall_Q1FY26_Aug2025_Transcript.txt p.14 | p.14 | MATCH |
| 2 | "market leader, which is 25% to 30%" (Harshal Sheth) | Concall_Q1FY26_Aug2025_Transcript.txt p.16 | p.16 | MATCH |
| 3 | Sula Own Brands revenue Rs511.1cr | SULA-Investor_Presentation_Q4FY26_2026-05-06.txt p.10 | p.10 | MATCH |
| 4 | Sula Operating EBITDA/margin/PBT (103.5cr/17.4%/24.1%/35.4cr) | same, p.10 | p.10 | MATCH |
| 5 | Sula FY26 WIPS accrual 48cr / payout 35cr | SULA-Concall_May_2026_Transcript.txt p.10 | p.10 | MATCH |
| 6 | "slow traction on canned wines" | SULA-Concall_Nov_2025_Transcript.txt p.10 | p.10 | MATCH |
| 7 | "60% market share... industry leader" / "12%... return on equity" | SULA-Concall_Nov_2025_Transcript.txt p.13 | p.13 | MATCH |
| 8 | EU-FTA EUR2.5 CIF / 75% first step / "7 to 10 years" | SULA-Concall_Feb_2026_Transcript.txt p.6 | p.6 | MATCH |
| 9 | TI "degrown by around 20%, the IMFL industry" | TI-Concall_Nov_2025_Transcript.txt p.6 | p.6 | MATCH |
| 10 | TI "60-100 bps" FTA margin benefit | TI-Concall_Jun_2026_Transcript.txt p.6 | p.6 | MATCH |
| 11 | SDBL "lost about 5%, 5.5% in half 1" | SDBL-Concall_Nov_2025_Transcript.txt p.10 | p.10 | MATCH |
| 12 | SDBL "commissioning... commencement of commercial production" | SDBL-Concall_Aug_2026_Transcript.txt p.3 | p.3 | MATCH |
| 13 | TI "TI Journey Over the Years" / 42.5%-79.8%-90%+ P&A | TI-Investor_Presentation_Q4FY26_2026-05-29.txt p.18 | p.18 | MATCH |
| 14 | Sula core-wine capex Rs50-60cr → ~Rs25cr FY26 | SULA-Concall_May_2026_Transcript.txt p.9 | p.9 | MATCH |
| 15 | Fratelli "expecting the industry to grow at about 15% to 20%" | Concall_Q1FY26_Aug2025_Transcript.txt p.7 | p.7 | MATCH |
| 16 | TI "adjusted for subsidy" Rs110cr/Rs90cr etc. | TI-Concall_Feb_2026_Transcript.txt p.3-4 | p.3 (within cited range) | MATCH |
| 17 | Fratelli "Commanding 1/3rd market share" | Investor_Presentation_Q4FY26_May2026.txt p.23 | p.23 | MATCH |
| 18 | Sula elite/premium vs cheaper-segment mix commentary | SULA-Concall_Feb_2026_Transcript.txt p.14 | p.14 | MATCH |
| 19 | Table-grape "more than doubling" / "Rs15-16/kg" / "Rs35/kg" compound quote | SULA-Concall_Aug_2026_Transcript.txt p.8 (all three) | "more than doubling" = p.8; "Rs15-16/kg" and "Rs35/kg" = **p.9** | **MISMATCH** (2 of 3 quote fragments wrongly anchored) |
| 20 | "~350-400bps FY26 full-year gross-margin impact" | SULA-Investor_Presentation_Q1FY27_2026-08-06.txt p.10-11 | Wrong document entirely — the "350 to 400 basis points" figure is in **SULA-Concall_May_2026_Transcript.txt p.8**, not the Q1FY27 presentation. The Q1FY27 presentation contains only a *different* figure (~150bps Q1FY27 impact, correctly cited elsewhere in the same sentence) | **MISMATCH** (wrong transcript) |
| 21 | SDBL "Rs570 crores greenfield project... Phase 1... completed by June" | SDBL-Concall_Feb_2026_Transcript.txt p.4 | p.3 | **MISMATCH** |
| 22 | SDBL "operational and regulatory disruption in Madhya Pradesh" | SDBL-Concall_Aug_2026_Transcript.txt p.4 | p.3 | **MISMATCH** |
| 23 | Sula WIPS receivable Rs85cr (Dec-25) | SULA-Concall_Feb_2026_Transcript.txt p.9 | p.11 | **MISMATCH** |
| 24 | Sula Q2FY26 WIPS accrual/payout detail (Rs20cr accrued/Rs13cr paid, Oct top-up) | SULA-Concall_Nov_2025_Transcript.txt "p.10-11" | p.9 | **MISMATCH** |

**Resolution rate: 18 of 24 (75%) resolved correctly.** All six mismatches
are genuine (verified twice against the page markers), not typos on my
part; none involve fabricated quotes — the words quoted are real and exist
in the named peer's corpus — but a reader following the cited anchor would
land on the wrong page five times and the wrong document once. Per the
task's own standard, each is a finding regardless of the quote being
genuine, because it cannot be verified at the stated anchor.

Two of the six sit inside this stage's own headline flags:
`SECTOR-WIDE-WIPS-DEPENDENCY` draws on the Q2 FY26 and Q3 FY26 WIPS figures
(items 23-24), and `GRAPE-COST-SILENCE-DURING-DISCLOSED-PEER-SPIKE` draws on
items 19-20. The underlying numbers in both flags are genuine and the
flags' conclusions survive re-anchoring (see Part 2), but the citations as
printed would not let an operator verify them without re-searching.

---

## PART 2: ARITHMETIC RE-DERIVATION

### 2.1 Market share / duopoly (CONTRADICTED)
- Fratelli FY26 revenue Rs181.29cr (B01-gate0.yaml, confirmed wine-only) ÷
  TAM Rs1,917-2,320cr (B09-tam.yaml) = 9.46% (low TAM end) to 7.81% (high
  TAM end). B06's flag states "7.5-9.5% share" — a touch generous at the
  low end (actual floor is 7.81%, not 7.5%) but directionally correct and
  not material. MINOR imprecision.
- Combined Fratelli + Sula Own Brands (181.29 + 511.1 = 692.39) ÷ TAM:
  692.39/1,917 = 36.1%, 692.39/2,320 = 29.85%. B06 states "36.1%" and
  "29.8%" — both correct to one decimal. MATCH.
- Conclusion (neither 1/3rd alone nor 85-90% combined survives) is
  correctly drawn from the arithmetic. Verdict CONTRADICTED holds.

### 2.2 Sector-wide WIPS dependency
- Sula FY26 WIPS accrual Rs48cr ÷ FY26 PBT Rs35.4cr = 1.356 = 136% of PBT.
  B06 states "exceeds... by 36%" and "136% of the market leader's own
  bottom line" — both correct.
- Rs48cr ÷ Operating EBITDA Rs103.5cr = 46.4%. B06 states "46%". MATCH.
- Conclusion holds; this is genuine arithmetic on two figures that are each
  correctly anchored (item 4, item 5 in Part 1), even though a third,
  adjacent WIPS figure used elsewhere in the same argument (item 23) is
  mis-anchored. The core sector-wide-dependency arithmetic is sound.

### 2.3 EBITDA benchmark (CONTRADICTED)
- Cited "market leader" benchmark: 25-30% (item 2, correctly anchored).
- Sula's actual filed Operating EBITDA margins: 14.7% (Q1FY27), 16.7%
  (Q1FY26 comparator), 19.5% (Q4FY26), 21.4% (Q4FY25), 17.4% (FY26 full
  year), 24.1% (FY25 full year, itself inflated by a one-time WIPS
  unwinding gain per Sula's own footnote).
- B06 states this "understat[es] the true benchmark by 5-15 points."
  Re-derived: the gap ranges from 0.9 points (25% vs the FY25 24.1%
  comparator, which is itself the most favourable and most inflated data
  point) up to 15.3 points (30% vs 14.7%). The stated "5-15 points" range
  therefore does not capture the true minimum gap (0.9 points) at the
  single most favourable comparator. Since that comparator is also the one
  Sula's own management flags as inflated by a non-recurring item, using
  it as the benchmark actually understates Fratelli's overstatement, not
  the reverse — so the CONTRADICTED verdict is not threatened, but the
  "5-15 points" figure as printed is imprecise. MINOR.

**Overall: neither arithmetic-based verdict is undermined.** The
calculations that carry the CONTRADICTED and structural-flag conclusions
are correct on the figures that are correctly anchored; the imprecisions
found are in supporting color language (percentage-point range wording),
not in the load-bearing numbers themselves.

---

## PART 3: PEER COVERAGE MAP AUDIT

12 peer-transcript-quarters were checked for the accuracy of their
usage classification and the presence of a real, findable citation
supporting that classification (Rule 2/3).

| Peer-quarter | B06 usage | Citation check |
|---|---|---|
| SULA Q2 FY26 (Nov 2025) | SUBSTANTIVE | Canned-wine and 60%-share citations correct (items 6, 7); WIPS accrual/payout citation mis-anchored (item 24, p.9 not p.10-11). Content genuine, anchor wrong. |
| SULA Q3 FY26 (Feb 2026) | SUBSTANTIVE | EU-FTA and elite/premium-mix citations correct (items 8, 18); WIPS receivable citation mis-anchored (item 23, p.11 not p.9). Content genuine, anchor wrong. |
| SULA Q4 FY26 (May 2026) | SUBSTANTIVE | WIPS accrual and capex-reduction citations both correct (items 5, 14). Clean. |
| SULA Q1 FY27 (Aug 2026) | SUBSTANTIVE | Low-single-digit-growth citation correct (page 8); grape-price compound quote partially mis-anchored (item 19); the headline 350-400bps figure attributed here is actually sourced from a different quarter's transcript entirely (item 20). Content genuine, two of three citations wrong. |
| TI Q2 FY26 (Nov 2025) | SUBSTANTIVE | Correct (item 9). Clean. |
| TI Q3 FY26 (Feb 2026) | CITED-ONLY | Correct (item 16), reasonable classification — checked transcript for wine/market-share content, found none beyond the noted subsidy-adjustment figures. |
| TI Q4 FY26 (Jun 2026) | SUBSTANTIVE | Correct (item 10). Clean. |
| TI Q1 FY27 (Aug 2026) | CITED-ONLY | Reviewed independently: transcript contains only IB/whisky market-share and ENA-cost commentary, nothing wine- or FTA-specific. Classification reasonable. |
| SDBL Q2 FY26 (Nov 2025) | SUBSTANTIVE | Correct (item 11). Clean. |
| SDBL Q3 FY26 (Feb 2026) | CITED-ONLY | Rs570cr Phase-1 quote mis-anchored (item 21, p.3 not p.4). Content genuine, anchor wrong. |
| SDBL Q4 FY26 (Jun 2026) | SUBSTANTIVE | **No page citation given anywhere in the report body for this quarter's specific contribution.** The Part 2C narrative cites only the Feb 2026 and Aug 2026 SDBL calls for the UP-brewery story; independently confirmed the Jun 2026 transcript does contain relevant content ("UP plant is 1 crore cases per annum" capacity, commissioning language), so the underlying claim is not fabricated, but as printed this SUBSTANTIVE row carries no locatable anchor. Rule 2 finding: MAJOR. |
| SDBL Q1 FY27 (Aug 2026) | SUBSTANTIVE | MP-disruption quote mis-anchored (item 22, p.3 not p.4). Content genuine, anchor wrong. |

**6 of 12 peer-quarters (50%) carry at least one citation-anchor problem
in their supporting evidence, though in every case except SDBL Q4 FY26 the
underlying claim itself is genuine and independently locatable in the
named transcript** (just not at the page printed). SDBL Q4 FY26 is the one
row with no findable anchor at all for its specific claim.

### Peer presentations (6 provided, explicitly in scope)
B06's own text states: "Peer presentations... were used substantively
throughout" and names five of the six by filename (SULA Q4FY26, SULA
Q1FY27, TI Q4FY26, SDBL Q4FY26, SDBL Q1FY27). **The sixth,
TI-Investor_Presentation_Q1FY27_2026-07-27.txt, is never mentioned anywhere
in B06 — not marked SUBSTANTIVE, not CITED-ONLY, not UNUSED-with-reason. It
is simply absent from the account.** Independently reviewing it: page 12
states "Customs: Reduction in custom under India-UK FTA from 150% to 75%
for scotch import" with "Cost savings will result in 250-400 bps in margin
expansion on the acquired business." This is directly relevant to Question
6 (EU-FTA duty-phasing schedule) — it independently corroborates, from a
second peer and a second document, the identical 150%-to-75% duty-step
structure Sula separately confirms for wine, and with a more precise
margin-benefit figure (250-400bps) than the 60-100bps TI concall figure
B06 actually used. This strengthens, rather than changes, Question 6's
PARTIALLY VERIFIED verdict, but it is material, claim-relevant peer
evidence that was never accounted for. Rule 3 finding: MAJOR
(unused_but_relevant).

---

## PART 4: VERDICT-DISCIPLINE AUDIT (per B05 peer_questions)

| # | Claim | B06 verdict | Addressed? | Discipline check |
|---|---|---|---|---|
| 1 | ~30-33% share / duopiy | CONTRADICTED | Yes | Rests on Fratelli's own figures + one peer (Sula) disclosure, cross-checked arithmetically — not a "VERIFIED resting on one peer" case (Rule 4 binds VERIFIED, not CONTRADICTED); arithmetic re-derived clean (Part 2.1). |
| 2 | Comparable WIPS subsidy at peers | PARTIALLY VERIFIED | Yes | Rests on Sula (granular) + TI (partial, differently-structured mechanism correctly caveated as non-comparable). Reasonable. |
| 3 | Market-leader EBITDA margin 25-30% | CONTRADICTED | Yes | Rests on one peer (Sula); again a CONTRADICTED verdict, not VERIFIED, so Rule 4's 2-anchor requirement does not literally bind; arithmetic re-derived, minor imprecision only (Part 2.3). |
| 4 | Bro Code formulation/share | UNVERIFIABLE | Yes | Confirmed zero matches for "Bro Code" across all 12 transcripts and 6 presentations independently. Correct verdict. |
| 5 | RTD/wine-in-a-can growth 25-30% QoQ | CONTRADICTED (with mapping caveat) | Yes | Rests on one peer statement (Sula), directional not magnitude-matched; caveat is stated prominently and appropriately hedges the verdict. |
| 6 | EU-FTA duty schedule | PARTIALLY VERIFIED | Yes | Rests on Sula only; the missed TI Q1FY27 presentation (Part 3) would have added a second, independent corroborating source and arguably justified upgrading this toward VERIFIED rather than PARTIALLY VERIFIED — a materiality point, not a verdict error, since PARTIALLY VERIFIED is the more conservative call and remains defensible without the missed source. |

**claims_all_addressed: true.** No claim was skipped. No verdict was
upgraded from silence (the ZERO-PEER-RECOGNITION and
peer_mentions_of_company:[] findings are used correctly as standalone
observations, not as confirmation of any claim). Rule 4's 2-anchor
requirement for VERIFIED claims is vacuously satisfied because B06 records
zero VERIFIED claims (0 of 6) — appropriately conservative given a
single-peer wine-industry universe (Sula is the only wine-sector peer
among the three provided).

---

## PART 5: OVERALL ASSESSMENT

The substantive judgment in B06 is sound: the two headline
arithmetic-based contradictions (market share/duopoly, EBITDA benchmark)
and the sector-wide WIPS-dependency reframing all re-derive correctly from
figures that exist where cited, using arithmetic that is correct, drawing
a conclusion the arithmetic supports. No fabricated numbers, no invented
peer statements, and the zero-Fratelli-mentions and zero-Bro-Code-mentions
claims are both independently confirmed exhaustive.

The weakness is citation-anchor discipline, which this exact rerun was
explicitly instructed to fix. Six of twenty-four spot-checked citations
(25%) resolved to the wrong page or the wrong transcript, concentrated in
the SULA WIPS/grape-cost evidence chain and the SDBL capex/regulatory
evidence chain — precisely the load-bearing supporting citations behind
two of B06's five headline flags. One peer-quarter (SDBL Q4 FY26) carries
a SUBSTANTIVE classification with no locatable citation at all. One of six
mandated peer presentations (TI Q1FY27) is entirely unaccounted for and
contains directly claim-relevant material.

None of these findings change the direction of any verdict. All are
MAJOR-not-CRITICAL: the facts asserted are genuine and independently
confirmable in the corpus, but not verifiable at the anchors printed,
which is exactly the failure mode the task brief asked this audit to
weight heavily.

**peer_utilisation: 9 of 12 peer transcripts used substantively (75%);
3 of 6 peer presentations used substantively, 2 cited-only, and 1
(TI Q1FY27) unaccounted for entirely (0/1, an omission, not a documented
non-use).**

Given 6 of 12 peer-quarters (50%) carry a citation-anchor defect in their
supporting evidence — below the pipeline's 60% acceptance-rate floor — I
am reporting acceptance_rate at peer-quarter granularity as 50%, which
would trigger the standing REWORK safeguard. This reflects citation
fidelity, not substantive judgment: every mis-anchored figure was verified
to exist genuinely in the correct peer's corpus, just not at the page or
in the document printed.

---

```yaml
stage: B12d
company: "FRATELLI"
run_date: "2026-09-07"
model: claude-sonnet-5
status: complete
peers_audited: 12
substantive_confirmed: 8
substantive_unsupported: ["SDBL Q4 FY26 (Jun 2026) — SUBSTANTIVE classification with no page/quote anchor given anywhere in the report for its specific claimed contribution (UP-brewery commissioning/capacity); content independently confirmed present in the transcript but not cited"]
unused_but_relevant:
  - {peer: "Tilaknagar Industries (TI)", missed_item: "TI-Investor_Presentation_Q1FY27_2026-07-27.txt (one of the six mandated peer presentations) is never mentioned anywhere in B06 -- not SUBSTANTIVE, not CITED-ONLY, not UNUSED-with-reason. Page 12 states 'Customs: Reduction in custom under India-UK FTA from 150% to 75% for scotch import' with 'Cost savings will result in 250-400 bps in margin expansion,' directly relevant to Question 6 (EU-FTA duty schedule) and more precise than the 60-100bps figure B06 actually used.", anchor: "TI-Investor_Presentation_Q1FY27_2026-07-27.txt p.12"}
claims_all_addressed: true
verdict_discipline_fails: []
findings:
  - {severity: "MAJOR", location: "Part 2B narrative + GRAPE-COST-SILENCE flag (report + YAML)", claimed: "~350-400bps FY26 gross-margin impact cited to SULA-Investor_Presentation_Q1FY27_2026-08-06.txt p.10-11", source_truth: "Figure is genuine but located in SULA-Concall_May_2026_Transcript.txt p.8, a different document entirely", note: "wrong-transcript citation on a load-bearing flag figure"}
  - {severity: "MAJOR", location: "Part 2B narrative + GRAPE-COST-SILENCE flag (report + YAML)", claimed: "'Rs15-16/kg' and 'Rs35/kg' cited to SULA-Concall_Aug_2026_Transcript.txt p.8 (as part of a compound quote)", source_truth: "These two fragments are on p.9; only the 'more than doubling' fragment is genuinely on p.8", note: "compound claim, one citation, mixed-page components"}
  - {severity: "MAJOR", location: "Part 1 Question 2 evidence table", claimed: "Sula WIPS receivable Rs85cr (Dec-25) cited to SULA-Concall_Feb_2026_Transcript.txt p.9", source_truth: "p.11", note: "two pages off"}
  - {severity: "MAJOR", location: "Peer coverage map, SULA Q2 FY26 row", claimed: "WIPS accrual/payout detail cited p.10-11", source_truth: "SULA-Concall_Nov_2025_Transcript.txt p.9", note: "wrong page"}
  - {severity: "MAJOR", location: "Part 2C narrative + coverage map, SDBL Q3 FY26 row", claimed: "Rs570cr Phase 1 quote cited SDBL-Concall_Feb_2026_Transcript.txt p.4", source_truth: "p.3", note: "wrong page"}
  - {severity: "MAJOR", location: "Part 2A/2E narrative + coverage map, SDBL Q1 FY27 row", claimed: "Madhya Pradesh disruption quote cited SDBL-Concall_Aug_2026_Transcript.txt p.4", source_truth: "p.3", note: "wrong page"}
  - {severity: "MAJOR", location: "Coverage map, SDBL Q4 FY26 row", claimed: "SUBSTANTIVE, 'UP greenfield brewery commissioning and capacity detail'", source_truth: "no page/quote anchor given anywhere in the report body for this specific quarter", note: "content genuine but unanchored; Rule 2 violation"}
  - {severity: "MAJOR", location: "Part 3 peer-presentation summary", claimed: "peer presentations used substantively throughout / SDBL two presentations CITED-ONLY", source_truth: "TI-Investor_Presentation_Q1FY27_2026-07-27.txt never mentioned; contains claim-relevant FTA duty-schedule corroboration for Question 6", note: "Rule 3 violation, unused-but-relevant"}
  - {severity: "MINOR", location: "Part 1 Question 3 net read", claimed: "market-leader EBITDA benchmark understated by 5-15 points", source_truth: "re-derived range is 0.9 to 15.3 points depending on comparator quarter", note: "verdict unaffected, range imprecise"}
  - {severity: "MINOR", location: "flags YAML, MARKET-SHARE-ARITHMETIC-CONTRADICTED", claimed: "implies 7.5-9.5% share", source_truth: "re-derived range is 7.81%-9.46%", note: "low end rounded down beyond the actual figure; immaterial"}
  - {severity: "MINOR", location: "Part 2C narrative", claimed: "Sula's CFO did not dispute the [12% ROE] framing, attributing it instead to harvest seasonality of tanks and barrels, same page", source_truth: "the harvest-seasonality explanation (SULA-Concall_Nov_2025_Transcript.txt p.12-13) was given in response to an earlier asset-turnover question; the CFO's direct response to the 12%-ROE follow-up instead cited a base-year comparability issue and a forward 17-18% ROE target (p.13)", note: "same speaker, same general exchange, but the two explanations are conflated as one response"}
critical_count: 0
major_count: 8
minor_count: 3
acceptance_rate: 50
