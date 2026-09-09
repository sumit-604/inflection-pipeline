# STAGE 6: PEER CONCALL VERIFICATION — RUN 2
Forbes Precision Tools & Machine Parts Ltd (TOTEM) | Run: totem-2026-09-09 | Run date: 2026-09-09

## RUN 2 NOTE
This is a full rewrite, not a patch, issued after four verifier findings against Run 1. Every finding was
checked against the transcript text before being adopted. One did not hold on independent re-reading; the
correction is flagged where it occurs (Q1 FY26/FY27 fiscal-label item, item 3 in the brief). All page citations
below were re-derived from the [PAGE n of N] markers in work/text/, not carried over from Run 1.

Sources read directly for this stage (page markers checked against every citation):
- work/text/peer-concalls__KENNAMET-Concall_Mar_2023_Transcript.txt (call 07-Mar-2023, 30 pages)
- work/text/peer-concalls__KENNAMET-Concall_May_2023_Transcript.txt (call 22-May-2023, 16 pages)
- work/text/peer-concalls__KENNAMET-Concall_Jun_2023_Transcript.txt (call 09-Jun-2023, 22 pages)
- work/text/peer-concalls__KENNAMET-Concall_Mar_2024_Transcript.txt (call 11-Mar-2024, 42 pages, newest in corpus)
- work/text/peer-concalls__WENDT-Concall_Jul_2026_Transcript.txt (file misnamed by data source; meeting date on
  page 1 of the transcript is 21-07-2025; anchored throughout as WENDT AGM, meeting 21-Jul-2025, 25 pages)
- work/text/annual-report__Annual_Report_2025.txt (TOTEM FY24-25 AR, subject-side anchor for the contradiction
  finding, PDF p.19)
- outputs/blocks/B05-concall.yaml (the six peer_questions and the claims under test)
- BIRLA PRECISION: zero transcripts in corpus. Never inferred, never cited.

## FISCAL-LABEL NOTE (carried forward correctly, restated once for clarity)
Two different "Q1" labels exist in this run and must stay separate:
- The WENDT transcript itself is WENDT's own Q1 FY26 call (April-June 2025), because its AGM meeting date is
  21-Jul-2025 and it reports results for the quarter ended 30-Jun-2025.
- TOTEM's own April-June 2026 quarter (the one compared in the screening CSVs against Kennametal's and Wendt's
  same-quarter growth) is TOTEM's Q1 FY27, one full year later than the WENDT transcript's own quarter.
These are never the same quarter. Every reference below to "WENDT's Q1" means WENDT's Q1 FY26 (Apr-Jun 2025)
call content; every reference to "TOTEM's Q1" means TOTEM's Q1 FY27 (Apr-Jun 2026), which no transcript in this
corpus covers directly — it is only reachable through the CSV cross-check (see below).

═══════════════════════════════════════════════════════════════
PART 1: CLAIM-BY-CLAIM VERIFICATION (the six B05 peer_questions)
═══════════════════════════════════════════════════════════════

### Q1. Is cutting-tool demand from automotive/aerospace/defence/railway customers in India accelerating
through FY25-FY26, or is TOTEM's 7.8-7.9% FY26 growth company-specific?

| Field | Content |
|---|---|
| Claim | TOTEM's FY26 domestic revenue growth of 7.8-7.9% rests entirely on internal capacity investment narrative, with no industry benchmark cited by TOTEM itself |
| Verdict | **PARTIALLY VERIFIED** |
| Peer evidence | KENNAMETAL, May-2023 call, Suresh Reddy, p.3-4: "hard metals are growing at around 9%... domestic market is strong, stable" (own-industry consumable/cutting-tool segment growth). KENNAMETAL, Mar-2024 call, Vijaykrishnan Venkatesan, p.28: "industry grew at probably 10% and 11%... [Kennametal's own] domestic [hard metal growth is] mid-single digit to a high single digit... 6 to 7% growth... because of the new tool consumption and then the volume growth", after an export headwind (-15-16%) diluted the total reported number. KENNAMETAL, Jun-2023, Vijaykrishnan, p.5-6: general robustness — "private sector capex expansion staying the course... robustness in the order book" (structural, not FY26-dated). WENDT AGM, meeting 21-Jul-2025, Bhagya Chandra Rao, p.3: domestic sales +7% "on account of higher demand from user industries like auto, auto ancillaries, bearing steel, cutting tools, resellers"; Ninad Gadgil, p.10: "Domestic Super Abrasives business grow close to about 9%"; p.11: Q1 FY26 (Apr-Jun 2025) domestic super abrasives grew a further 11% |
| Peers silent | Neither peer speaks to defence or railway demand specifically at any quantified level; both speak only to automotive/auto-ancillary/general engineering |
| Net read | Both peers show domestic demand growth in a 6-11% band across FY23-FY26 (peer fiscal years, not TOTEM's), which brackets TOTEM's own 7.8-7.9% FY26 domestic growth. This is directional corroboration that India cutting-tool/precision-tooling demand is genuinely growing at a mid-to-high single-digit clip industry-wide, not a TOTEM-specific artifact — but it stops short of full verification because none of the peer figures are drawn from TOTEM's own FY26 window (Kennametal's newest data is 2.5 years stale; Wendt's is one year adjacent). TOTEM's number reads as roughly in line with the sector, not standout outperformance and not underperformance either. |

### Q2. What is the HSS-versus-carbide demand and pricing mix trend industry-wide?

| Field | Content |
|---|---|
| Claim | TOTEM spans both HSS (Drills, Taps) and Solid Carbide with zero segment split disclosed; a peer mix-shift read would reframe which TOTEM growth story is riding a tailwind |
| Verdict | **PARTIALLY VERIFIED** |
| Peer evidence | KENNAMETAL, Mar-2023 call, Vijaykrishnan Venkatesan, p.7: draws the product-category line explicitly — "I am talking only tungsten carbide, not high-speed steel, not the taps" — confirming Kennametal's own core hard-metal business is carbide-centric, with HSS/taps treated as a separate, smaller category it does not lead in. Same call, p.11: on the shift from single-point (largely HSS/lathe) tooling to CNC-driven machining — "over the years... people have been migrating to CNC machines, right?... The whole industry itself is migrated... this technology migrates in the country, more and more automation comes in" — a structural, multi-decade migration away from manual/single-point tooling toward CNC-compatible (predominantly carbide) tooling, driven by productivity, accuracy, and rising labour cost |
| Peers silent | WENDT does not manufacture HSS or carbide round-tool cutting tools itself (its business is super-abrasives, grinding machines, and precision components); it has no comparable HSS-versus-carbide commentary |
| Net read | One peer, structurally credible: the CNC migration finding corroborates that TOTEM's Drills segment (explicitly CNC-capacity-led per its own AR) sits on a real secular tailwind. It also raises a genuine, unresolved question TOTEM's own AR never addresses: if the industry is migrating toward carbide/CNC broadly, is TOTEM's HSS Drills product itself vulnerable to substitution at the higher end of its own customer base, even as the CNC-driven VOLUME story holds? No peer or TOTEM disclosure answers that follow-on question; magnitude of the mix shift is not quantified anywhere in the corpus. |

### Q3. How are cutting-tool distributors/channel partners behaving on inventory through 2025-2026,
stocking up or destocking?

| Field | Content |
|---|---|
| Claim | TOTEM's own inventory built 76.7% in FY26 with zero management explanation; peer channel commentary is the closest external read available |
| Verdict | **UNVERIFIABLE** |
| Peer evidence | KENNAMETAL, Mar-2023 call, p.17 (Suresh Reddy / Vijaykrishnan, responding to Amit Sham Nadekar): inventory commentary exists but is about KENNAMETAL'S OWN book, not channel/distributor behaviour, and the stated cause is COVID-era safety stocking plus a facility-move transition ("we had to ensure that container movements... it was a huge crisis. So, we increased the safe inventory levels"), not demand signal. KENNAMETAL, May-2023 call, p.4-5 (Suresh Reddy): similar own-book "inventory correction" tied to the same facility move, explicitly not channel-driven. WENDT AGM, p.19 and p.23 (shareholder query and Mukesh Kumar Hamirwasia's answer): trade receivables rose Rs52cr to Rs65cr and DSO 80 to 101 days in FY24-25, attributed to machine-tool installation/commissioning timing, collected in Q1 — a receivables story, not an inventory-stocking one |
| Peers silent | Neither peer's channel PARTNERS' own stocking behaviour is discussed by either company at any point in any of the five transcripts. Both peers only speak to their own factory-gate inventory |
| Net read | This question cannot be answered from the corpus. The only inventory commentary available is 2+ years stale, describes each peer's OWN book (not distributor behaviour), and is driven by a one-off supply-chain/facility event rather than a demand read. This must stay UNVERIFIABLE, not upgraded on plausibility: TOTEM's 76.7% inventory build remains unexplained by any independent evidence this run can reach. |

### Q4. What do peers say about US/Mexico tariff impact on Indian cutting-tool exports, widening or
stabilising into 2026?

| Field | Content |
|---|---|
| Claim | TOTEM blames a specific, dated external cause (US/Mexico tariffs) for its FY26 export reversal; peer corroboration tests whether this is industry-wide or company-specific |
| Verdict | **UNVERIFIABLE** |
| Peer evidence | WENDT AGM, p.20 (Yashpal Chopra, shareholder): asks directly — "does Trump's those policies of tariffs and all that have any kind of effect on our company's performance that I would like to find out." Management's consolidated answer session (Bhagya Chandra Rao, pp.21-23) works through every other queued topic (video-conference AGM format, physical annual report, gifts, bonus, stock split, CUMI merger speculation, CEO transition, quarterly investor meet request, TAM, market share, ESG rating, capex, receivables/DSO) but never returns to the tariff question — it goes unanswered on the record. KENNAMETAL's four calls all pre-date the 2025 US/Mexico tariff action entirely; their own export-weakness commentary (Jun-2023, Vijaykrishnan, p.9: "the recovery post lockdowns in China... has been little slower"; Mar-2024, p.6: "exports... little bit of a struggle... driven because of softening of demand in the developed countries and China") names China and European softness, never tariffs, because the period predates the event |
| Peers silent | Both peers are structurally unable to speak to a 2025-dated tariff shock with any currency; WENDT is the one peer inside the right calendar window and its own shareholder asked the exact question, but the transcript records no answer |
| Net read | This is not silence-as-corroboration; it is a genuine gap. The one place in the entire five-transcript corpus where a tariff-specific answer could have been recorded went unanswered. TOTEM's tariff attribution for its FY26 export reversal cannot be checked against any peer evidence in this run, in either direction. |

### Q5. What capex-to-margin payback timeline do peers describe for their own capacity expansions?

| Field | Content |
|---|---|
| Claim | TOTEM's Drills capacity-to-margin claim has no stated payback timeline anywhere in three annual reports |
| Verdict | **PARTIALLY VERIFIED** |
| Peer evidence | KENNAMETAL, Jun-2023 call, Vijaykrishnan Venkatesan, p.5: "for the consumable side, we get a drag impact [as] capacity expansion happens with a face lag of 12 to 15 months. Once the machines are installed and the capacity expansion [occurs]..." — repeated in the same call, p.10, to Jainis Ketan Chheda: "long lead time of sale matures between one [to two] years... capital cycle being approved to installation it's 12 to 15 months, right." WENDT AGM, p.18-19 (Rahul Kumar Paliwal, shareholder, asking directly about the Capex jump from Rs11cr to Rs60cr, +420%): "given the current revenue growth rate of this 3, 4 or 5%, how do you justify this massive capital deployment... what kind of expected ROE timeline". Management's answer (Mukesh Kumar Hamirwasia, p.23) explains WHAT the capex was for (Rs35cr brand acquisition, "something for the future... export market in newer geographies") but gives no timeline, no ROE figure, and no payback period at all |
| Peers silent | Neither peer gives a payback figure specific to a NAMED capacity project (both figures are general statements about the category, not TOTEM-comparable per-project numbers) |
| Net read | One peer (Kennametal) supplies an explicit, twice-repeated benchmark: roughly 12-15 months between capacity coming online and volume showing up in reported consumable demand. The other peer (Wendt), asked the identical question by its own shareholder, gave no answer at all — which means TOTEM's own disclosure gap (zero payback timeline across three annual reports) is not a TOTEM-specific opacity; it appears to be a sector-wide reticence on this exact metric, at least among the two peers with transcripts. Applying Kennametal's 12-15 month benchmark: TOTEM's Drills CNC capacity, delivered per the FY26 AR (Annexure IV), showing up as a margin step-change in Q1 FY27, sits inside a plausible window under this peer's own stated lag, not a suspiciously fast one. |

### Q6. How much of steel/carbide raw-material cost inflation could peers pass through to customers
in 2023-2025?

| Field | Content |
|---|---|
| Claim | TOTEM's own pass-through language weakened from "successfully passed on" (FY24 AR) to "trying to pass on as much as possible" (FY26 AR) while materials cost/revenue rose 517bp |
| Verdict | **PARTIALLY VERIFIED** (single peer in scope per B05's check_peers list) |
| Peer evidence | KENNAMETAL, Jun-2023 call, Suresh Reddy, p.15: "wherever possible we try to pass on through the pricing increases, the cost of materials plus also working on modernisation of the facilities to bring in productivity" — hedged language ("wherever possible"), not an unqualified success claim. KENNAMETAL, Mar-2024 call, Suresh Reddy K V, p.19: tungsten prices fell 8-9% over the prior year and stabilised; "when there is a price escalation, we do revise our pricing to ensure that we mitigate some of the rise in prices... whenever there is a price drop, the customers do come back to ask for a price reductions" — pass-through runs BOTH ways, i.e. customers claw back on price falls too. Vijaykrishnan, same page: "it's not that one will edge out the other because everybody buys at the same price" (raw-material pricing is transparent market-wide, no single player can sustain a durable pass-through edge) |
| Peers silent | N/A — Kennametal is the only peer in scope for this question per B05 |
| Net read | Kennametal's own pass-through language is hedged in the identical register TOTEM's own weakened ("successfully" -> "trying... as much as possible"). This corroborates a reading that full raw-material pass-through is a structurally imperfect, competitively-constrained mechanism across this industry, not a TOTEM-specific pricing-power failure — though only one peer's evidence exists to support this, so it stays PARTIALLY VERIFIED rather than VERIFIED. |

═══════════════════════════════════════════════════════════════
PART 2: UNPROMPTED CROSS-READ
═══════════════════════════════════════════════════════════════

## 2A DEMAND ENVIRONMENT — including the one contradiction this run found

Kennametal's own domestic hard-metal/consumable growth runs mid-to-high single digit across FY23-FY24 calls
(9% May-2023 p.3-4; 6-7% net of export drag, 10-11% gross industry Mar-2024 p.28), with its CNC/machine-tools
segment showing far higher and more volatile domestic growth (46% cited Mar-2024 p.6). Wendt's most current
window (FY24-25 results plus Q1 FY26, meeting 21-Jul-2025) shows domestic Super Abrasives accelerating from
+9% (FY24-25, p.10) to +11% (Q1 FY26/Apr-Jun 2025, p.11), driven by the same end-customer set TOTEM cites
(auto, auto-ancillary, cutting tools, p.3) — directionally consistent with TOTEM's own domestic growth story.

**The contradiction.** TOTEM's own FY24-25 annual report (work/text/annual-report__Annual_Report_2025.txt,
PDF p.19, Precision Tools business section) states: "The business has also seen an improving trend in the
export business performance." In the SAME fiscal year (Apr-2024 to Mar-2025), Wendt's AGM (meeting
21-Jul-2025, reporting Wendt's own FY24-25 results, PDF p.3 of the transcript) states: "Exports were at
Rs 43.63 crores during the year, lower by 12% over the previous year due to reduced offtake from key
customers from a few countries." Both companies report on the identical April 2024-March 2025 fiscal window
(both use an April-March year). Wendt's stated cause (customer-specific offtake reduction) is different from
the tariff cause TOTEM names for its LATER FY25-26 reversal (Q1 FY27's peer_question), so this is not evidence
that TOTEM's later tariff claim is false. What it does contradict, directly and in the same period, is TOTEM's
own claim that its export business was on an "improving trend" during FY24-25 — a close peer in the same
broad manufacturing-export environment reports the opposite direction, in the same twelve months, for a
different but adjacent reason. This finding was available in Run 1 (quoted in this section) but was not
carried into the triangulation tally; it is carried here. **Verdict on this specific claim: CONTRADICTED.**

## 2B PRICING AND INPUT COSTS

Covered substantively under Q6 above. No peer contradicts TOTEM's margin narrative on raw-material
pass-through; if anything Kennametal's own hedged pass-through language and description of a fully
transparent, symmetric tungsten-pricing market corroborates that TOTEM's softening claim reflects a
sector-wide dynamic, not unique mismanagement.

## 2C CAPEX CYCLE — industry-wide capacity race, not a lone expander

Both peers with transcripts are ALSO expanding capacity in overlapping windows: Kennametal describes ongoing
modular capacity additions tied to demand ("we have room to continue to support the Indian growth story...
we just add machines," Jun-2023, Vijaykrishnan, p.12) across all four of its calls; Wendt's FY24-25 capex
jumped to Rs58.29cr from Rs11.15cr the prior year (+422%, p.4/p.10), split between new capacity and the
Rs35.08cr Wendt-brand acquisition. **This is an industry-wide capacity race, not a single company (TOTEM)
making a lone bet** — TOTEM's own Drills CNC and Austempering-furnace investments sit inside a sector-wide
pattern rather than standing apart from it. One cautionary parallel worth flagging forward: Wendt's own
capex spike was immediately followed by its worst quarter on record (Q1 FY26, Apr-Jun 2025: PBT -34%,
p.6/p.11, "due to lower order... sales from steel products and the amortisation of Wendt brand"). This
capex-then-worse-quarter pattern at a close peer is the direct evidentiary basis for the Part 5 hypothesis
below and bears on how TOTEM's own Q1 FY27 margin jump should be read.

## 2D COMPETITIVE MENTIONS

Neither peer names or unmistakably describes TOTEM/Forbes Precision Tools anywhere across all five
transcripts. This is a genuine, checked silence, not an absence of search: Kennametal names its addressable
Indian machine-tool market at roughly Rs20,000cr against its own ~Rs150cr base (Mar-2024, p.6); Wendt's own
scale is ~Rs212cr (p.11). TOTEM (~Rs290cr FY26 revenue per B03) is sub-scale relative to both, and operates
below the radar of either company's institutional-analyst conversations.

## 2E RISKS PEERS DISCUSS THAT TOTEM DOES NOT

- **Named, quantified import-competition intensity in a specific product slice.** Kennametal, Mar-2024,
  Neeraj Prakash / Vijaykrishnan, p.20-21: "we did see... a significant increase in competitive intensity
  because of products being pushed from one country into India" on roughly 1.5% of revenue. TOTEM's AR names
  "competition" only in undifferentiated boilerplate, never a quantified import-competition risk.
- **Leadership transition disclosed with a name and a date, in real time.** WENDT AGM, p.7: CEO Ninad Gadgil
  "will be stepping down from the Board effective 15th September 2025." TOTEM's own two HR-leadership exits
  inside roughly eight months are disclosed only through terse Regulation 30 filings, never narrated or dated
  with the same directness in the AR itself.
- **Receivables/DSO deterioration interrogated on the record and explained.** WENDT AGM, p.19 (shareholder
  question) and p.23 (Mukesh Kumar Hamirwasia's answer): receivables Rs52cr to Rs65cr, DSO 80 to 101 days,
  explained as installation/commissioning-linked and "collected in Q1." TOTEM's own 76.7% inventory build gets
  no equivalent forced explanation anywhere in this corpus, because no Q&A forum exists for TOTEM at all.
- **One-time costs named and reconciled against reported PBT.** WENDT AGM, p.4: "one-time expenses of
  Rs.1.77 crore related to the tech transfer agreement with 3M and the new company formation in Germany.
  Without these expenses, the Company would have made PBT of Rs.5146 lakhs" — an explicit ex-items
  reconciliation. TOTEM names its Labour Codes Rs5.90cr one-time cost in a Note but never walks an
  ex-items PBT reconciliation in its own MD&A narrative anywhere in three annual reports.

═══════════════════════════════════════════════════════════════
PART 3: PEER COVERAGE MAP
═══════════════════════════════════════════════════════════════

| Peer | Quarter/Meeting | Used how | Key contribution |
|---|---|---|---|
| KENNAMETAL INDIA | Call dated 07-Mar-2023 | SUBSTANTIVE | HSS-vs-carbide product-category distinction (p.7); structural HSS/single-point-to-CNC migration finding (p.11); distributor channel mix, ~70% of business (p.4); own-book inventory build tied to COVID safety stocking and facility move, not demand (p.17) |
| KENNAMETAL INDIA | Call dated 22-May-2023 | SUBSTANTIVE | Domestic hard-metal (consumable) growth ~9% (p.3-4); China-driven MSG machine-order weakness quantified (~25% QoQ degrowth, p.3); own-book inventory correction, facility-transition-linked, explicitly not channel-driven (p.4-5, p.10-11) |
| KENNAMETAL INDIA | Call dated 09-Jun-2023 | SUBSTANTIVE | Explicit capex-to-consumable-demand lag, "12 to 15 months," stated twice (p.5, p.10); imported-machine-tool surge, "crazy high... broken the record of 2018-2019" (p.7), corroborating the India capex upcycle with stronger evidence available at the Mar-2024 call, cited here per the coverage gap this run closes; hedged raw-material pass-through language, "wherever possible" (p.15); capacity investment described as demand-led, not speculative (p.12) |
| KENNAMETAL INDIA | Call dated 11-Mar-2024, newest in corpus (2.5yr stale vs run date) | SUBSTANTIVE | "Sequential improvement in our PBT" over four quarters (p.7); domestic CNC machine growth of 46% cited (p.6); domestic hard-metal growth mid-to-high single digit (6-7% net, 10-11% gross industry) after a -15-16% export drag (p.28-29); tungsten price stabilisation and symmetric, transparent pass-through commentary (p.19) |
| WENDT INDIA | AGM, meeting 21-Jul-2025 (transcript file misnamed "Jul_2026" by the data source; reports Wendt's own FY24-25 results plus Q1 FY26/Apr-Jun 2025) | SUBSTANTIVE | FY24-25 export decline -12% (p.3), directly contradicting TOTEM's own FY24-25 AR claim of an "improving trend" in exports (see Part 2A); CEO departure named and dated (p.7); Q1 FY26 PBT -34% immediately following a capex spike (p.6, p.11); capex +422% with no ROE/payback timeline disclosed even under direct shareholder questioning (p.18-19, p.23); a shareholder's US/Mexico tariff question asked and left unanswered on the record (p.20) |
| BIRLA PRECISION | N/A | UNUSED | Zero transcripts in corpus; never inferred, no position taken on its behalf |

═══════════════════════════════════════════════════════════════
PART 4: TRIANGULATION SUMMARY
═══════════════════════════════════════════════════════════════

- **Claims verified (two-peer bar met): 0 of 6.**
- **Claims partially verified: 4 of 6** (Q1 industry growth rate, Q2 HSS-carbide migration, Q5 capex payback
  timeline, Q6 raw-material pass-through).
- **Claims unverifiable: 2 of 6** (Q3 distributor/channel inventory behaviour 2025-26, Q4 US/Mexico tariff
  impact — the corpus genuinely cannot reach either, for different reasons: Q3 has no peer channel-level
  evidence at all; Q4 has one peer inside the right window whose own shareholder asked the exact question and
  received no recorded answer).
- **Claims contradicted: 1** (from Part 2A, unprompted cross-read, not one of the six injected B05 questions):
  TOTEM's FY24-25 AR claim of an "improving trend in the export business performance" is directly contradicted,
  in the same fiscal year, by Wendt's own reported -12% export decline. This is a priority item for synthesis.

**The single most consequential contradiction.** TOTEM's FY24-25 AR export claim and Wendt's FY24-25 export
result point in opposite directions in the identical twelve months. This does not prove TOTEM's claim was
knowingly false — Wendt's cause (customer-specific offtake loss) differs from what a general "improving trend"
would need to be wrong about — but it removes the one piece of independent corroboration a reader might have
assumed existed for TOTEM's own export narrative in that year, and it sits inside a corpus (see B05) that
already flags TOTEM's export commentary as reversing hard one cycle later.

**The single strongest independent confirmation.** The industry-wide capacity race (Part 2C): both peers with
transcripts are expanding capacity in overlapping windows, on demand-led (not speculative) terms, which
corroborates that TOTEM's own Drills-capacity growth trigger sits inside a genuine sector tailwind rather than
being a company-specific bet running against the grain.

**Overall: the peer set complicates more than it either supports or undercuts TOTEM's narrative.** It
corroborates the structural growth story (domestic demand growing mid-to-high single digit sector-wide, a real
HSS-to-carbide/CNC migration, an industry-wide capacity race, and a raw-material pass-through squeeze that
looks sector-wide rather than TOTEM-specific). But it delivers one direct, dated contradiction on the single
most checkable claim available (the export trend), and it goes silent on precisely the two questions the run
most needed answered because they are current-period (channel destocking, tariff trajectory) — not because
peers deny them, but because the corpus cannot reach them: Kennametal's newest call is 2.5 years stale, and
Wendt's one current-period call left the tariff question on the table, unanswered, on its own AGM record.

═══════════════════════════════════════════════════════════════
PART 5: CROSS-PEER HYPOTHESIS
═══════════════════════════════════════════════════════════════

**Hypothesis: in this precision-tooling sector, the capex/machine-tool segment behaves as a leading but
noisy indicator that systematically overshoots in both directions around a capacity cycle, while the
consumable segment is the true stabiliser — meaning a post-capex margin jump should be treated as
provisional for longer than one quarter before being read as a structural step-change.**

No single peer states this. It emerges only by placing two separate peer facts side by side. First,
Kennametal's own machine-tools (MSG) segment swings far harder than its hard-metals consumable segment:
domestic CNC machine growth of 46% (Mar-2024, p.6) against hard-metal consumable growth of 6-11% across the
same set of calls; a ~25% QoQ MSG degrowth from China order weakness in one quarter (May-2023, p.3) against a
stable 9% hard-metal growth in the same period. Second, Wendt's own capex spike (Rs11cr to Rs58cr, +422%,
FY24-25) was immediately followed by its single worst quarter on record — Q1 FY26 PBT down 34% — while its
consumable-adjacent Super Abrasives segment kept growing (+11% domestic, same quarter). In both peers,
independently, the capex/machine-adjacent line item is the volatile one and the consumable/recurring line is
the stable one, and in Wendt's case a capex spike coincided directly with the worst quarter, not the best one.
TOTEM's own Q1 FY27 margin jump (16.1% to 22.9%) follows directly from its own capex delivery (Drills CNC
capacity, confirmed in the FY26 AR). The peer pattern suggests this kind of post-capex margin move is, in this
specific sector, more often a transient re-basing that takes several quarters to settle than an immediate new
structural plateau — Kennametal's own language for its comparable episode was "sequential improvement" over
FOUR quarters (Mar-2024, p.7), not a one-quarter jump. This is testable: if TOTEM's Q2-Q4 FY27 margin holds
inside a narrowing band around the Q1 FY27 level (consistent with Kennametal's own multi-quarter settling
pattern), the hypothesis is supported; if it whipsaws back toward the FY26 16-18% band and then re-climbs
gradually, or overshoots further before settling, that also fits; a single-quarter flat-line at exactly 22.9%
with no further movement would be the pattern this hypothesis predicts is least likely.

═══════════════════════════════════════════════════════════════
VERIFIER-FINDING DISPOSITION (audit trail for this run)
═══════════════════════════════════════════════════════════════

1. **MAJOR, red-flag verifier — export contradiction. HOLDS.** Confirmed on direct read: WENDT AGM p.3 states
   FY24-25 exports "lower by 12% over the previous year due to reduced offtake from key customers"; TOTEM's
   FY24-25 AR, PDF p.19, states an "improving trend in the export business performance" for the same period.
   Adopted; now carried into Part 2A, Part 4, and the contradicted[] YAML list.

2. **MAJOR, peer-coverage verifier — citation defect, Q1 FY26 machine-tools/PBT quote. HOLDS, with one
   correction to the verifier's own page number.** The qualitative sentence ("decrease in profit is due to
   lower order... sales from steel products and the amortisation of Wendt brand") is confirmed spoken by
   Bhagya Chandra Rao (Chairman), on transcript p.6, not Ninad Gadgil at p.19 as Run 1 had it. The -18%
   (machine tools/EBITDA) and -34% (PBT) figures together are confirmed spoken by Ninad Gadgil — but on direct
   re-read against the page markers, this run finds them on **transcript p.11**, not p.10 as the verifier's
   finding stated. The verifier is another analyst, not an authority, per this run's brief; p.11 is what the
   page-marker text supports and is used throughout this report and the citations above.

3. **MINOR citation defects. Both HOLD, both fixed.** The CEO-departure quote (Ninad Gadgil stepping down
   15-Sep-2025) is confirmed at transcript p.7, not p.2. The Kennametal Mar-2024 "sequential improvement in
   our PBT" quote (Vijaykrishnan Venkatesan) is confirmed at transcript p.7, not p.5-6.

4. **MINOR, fiscal-label error. HOLDS, fixed.** "Q1 FY26" language for TOTEM's own April-June 2026 quarter is
   replaced throughout with "Q1 FY27" (see Fiscal-Label Note above), while the WENDT transcript's own quarter
   (Apr-Jun 2025) is correctly labelled WENDT's Q1 FY26 throughout.

5. **Unused-but-relevant item — Kennametal Jun-2023 "crazy high" import-machine-surge quote. Adopted.** Cited
   in the Part 3 coverage map for the Jun-2023 call and referenced in Part 2C's capex-cycle discussion,
   corroborating the same directional point Run 1 made from the stronger Mar-2024 evidence; no conclusion
   changes, coverage is simply now complete.

═══════════════════════════════════════════════════════════════
END OF STAGE 6 REPORT
═══════════════════════════════════════════════════════════════
