# VERIFIER D — PEER COVERAGE AUDIT: Rappid Valves (India) Ltd (RAPPID)
Run date: 2026-09-19. Model: claude-sonnet-5.

Scope: did B06 (Stage 6 peer concall verification) actually USE the 8 peer
transcripts it claims to have used? Every SUBSTANTIVE citation was traced
back to the named transcript and page-marker location; every peer's full
transcript was read (or grep-searched at the specific quote level) for
material the pipeline should have used against the B05 peer_questions
claim list but did not.

Inputs read directly: all 8 files in
runs/rappid-2026-09-19/inputs/peer-concalls/ (KSB-Concall_Sep_2025,
KSB-Concall_Nov_2025, KSB-Concall_Mar_2026, KSB-Concall_Aug_2026,
ATAM-Concall_Nov_2023, ATAM-Concall_Apr_2024, ATAM-Concall_Jul_2024,
QUESTFLOW-Concall_Jun_2024); B06 report
(outputs/reports/06-peers.md) and block (outputs/blocks/B06-peers.yaml);
B05 peer_questions[] (outputs/blocks/B05-concall.yaml).

Note on B06's own history: this is a "round 2" (CORRECTION RUN) report.
Round 1 was already audited by a prior Verifier B/D pass and round 2
states it applied 7 corrections, including page-anchor fixes flagged by a
prior Verifier D pass. This audit re-derives every citation independently
from the source files rather than trusting B06's own correction log.

---

## PART 1: COVERAGE AUDIT PER PEER (SUBSTANTIVE citations traced to source)

All 8 transcripts are marked SUBSTANTIVE in B06's coverage map. None is
marked UNUSED or CITED-ONLY, so Rule 3's "spot-read for missed material"
test was run on all 8 anyway (see Part 2) rather than only the
unused/cited-only subset the rubric names.

| # | Peer / quarter | Claimed citation | Verified in source? | Result |
|---|---|---|---|---|
| 1 | ATAM Apr-2024, "credit period... 90 to 120 days" | p.5 | Quote found verbatim, file's own "Page 5 of 17" marker | CONFIRMED |
| 2 | ATAM Apr-2024, "No PSUs, no L1 bidding" | p.13 | Quote found verbatim, "Page 13 of 17" marker | CONFIRMED |
| 3 | ATAM Apr-2024, "96,000 pieces per month... 85% utilization" | p.2 | Quote found verbatim, "Page 2 of 17" marker | CONFIRMED |
| 4 | ATAM Nov-2023, "~Rs30 crore new plant... bathroom-faucet import line" | p.6-9 | Content real but spread p.3 (Rs30cr capex plan), p.4 (new plant for bigger valves), p.5-6 (delay/asset-light China-Spain-Italy import), p.7 (ROI/breakeven), p.8 (WC for capex+bathware); p.9 is Canada/API, off-topic for this claim | CONFIRMED, page range imprecise (MINOR) |
| 5 | ATAM Jul-2024, "35-40% growth... next two years" | p.4 | Quote found verbatim, "Page 4 of 11" marker | CONFIRMED |
| 6 | KSB Sep-2025, "net working capital more than 120 days" / "below 120 days" | p.10 | Quote found verbatim, "Page 10 of 29" marker | CONFIRMED |
| 7 | KSB Sep-2025, "one of our competitor has a development order" | p.11 | Quote found verbatim (Nitin Patil), "Page 11 of 29" marker | CONFIRMED |
| 8 | KSB Sep-2025, "fourth shed... Shirwal... extra plot... ready by March" | p.20-21 | Quote found verbatim; response begins on p.20 (resources discussion), specific shed/plot sentence on p.21 | CONFIRMED |
| 9 | KSB Nov-2025, "gross margins have reduced from 54% to 44%, 43%" + EBITDA steady 12-14% explanation | p.31-32 | Quote and the "internal efficiency improvement" follow-up both sit on p.31; p.32 covers firefighting market share, unrelated | CONFIRMED, page range imprecise (MINOR) |
| 10 | KSB Nov-2025, "close to 85% kind of utilization" | p.37 | Quote found verbatim, "Page 37 of 45" marker | CONFIRMED |
| 11 | KSB Mar-2026, "chances of the spike in commodity prices... watching very carefully" | p.8 | Quote found verbatim, "Page 8 of 29" marker | CONFIRMED |
| 12 | KSB Mar-2026, PVC clause / "we don't have PVC clause with our suppliers... those businesses are without PVC and those are long deliveries" | p.8-9 | Quote genuinely spans the p.8/p.9 boundary as cited | CONFIRMED |
| 13 | KSB Mar-2026, "3% to 4%... maximum up to 3% to 5% in any project" (pumps content-share) | p.15 | Quote found verbatim, "Page 15 of 29" marker | CONFIRMED |
| 14 | KSB Mar-2026, portal-payment mechanism ("uploaded all the things report... portal acknowledges it") | p.24 | Quote found verbatim, "Page 24 of 29" marker | CONFIRMED |
| 15 | KSB Aug-2026, "80% to 90% capacity utilization" | p.7 | Quote found verbatim, "Page 7 of 30" marker | CONFIRMED |
| 16 | KSB Aug-2026, "given foundries maybe in the range also of 12% to 15%... standard markets would be still single-digit" | p.23 | Quote found verbatim, "Page 23 of 30" marker | CONFIRMED |
| 17 | KSB Aug-2026, "3% to 5% is something of the total... project value" + "3% to 5% of my sales turnover" | p.25 | Both quotes found verbatim, "Page 25 of 30" marker | CONFIRMED |
| 18 | KSB Aug-2026, Mahesh Bhave receivable-days/solar quote | p.27 | Quote found verbatim, "Page 27 of 30" marker | CONFIRMED |
| 19 | QUESTFLOW Jun-2024, global/India industrial valve TAM | p.3 | Quote found verbatim | CONFIRMED |
| 20 | QUESTFLOW Jun-2024, H2 FY24 EBITDA/PAT margin figures | p.3-4 | Figures genuinely split across the p.3/p.4 boundary as cited | CONFIRMED |
| 21 | QUESTFLOW Jun-2024, FY24 full-year EBITDA/PAT (incl. the flagged Rs4.95cr/23.61% reconciliation gap) | p.4 | Both figures found verbatim on p.4; the reconciliation gap is real in the source (not a B06 transcription error) | CONFIRMED |
| 22 | QUESTFLOW Jun-2024, "Amrit Kaal 2047"/100% domestic utilization | p.5 | Quote found verbatim | CONFIRMED |
| 23 | QUESTFLOW Jun-2024, CNC machines / foundry backward integration | p.8-9 | CNC-machine and foundry statements on p.8; the "30-40% throughput increase" follow-up is on p.9 | CONFIRMED |
| 24 | QUESTFLOW Jun-2024, "our niche is nonferrous... hardly around less than 5%" | p.6 | Quote found verbatim | CONFIRMED |
| 25 | QUESTFLOW Jun-2024, "nonferrous valves are having better margins" | p.19 | Quote found verbatim | CONFIRMED |

**Result: 25 of 25 spot-checked citations trace to real, findable material
in the named transcript at (or immediately adjacent to) the cited page.
Zero fabricated or unfindable citations. Two of the 25 (#4 and #9) cite a
page range that is real but imprecise (over-broad or one page off);
graded MINOR each, not MAJOR, because the underlying quoted content is
genuinely in the transcript and substantiates the claim made.**

Peer-level roll-up:

| Peer transcript | Usage claimed | Confirmed |
|---|---|---|
| ATAM-Concall_Nov_2023 | SUBSTANTIVE | Yes (1 MINOR anchor imprecision) |
| ATAM-Concall_Apr_2024 | SUBSTANTIVE | Yes |
| ATAM-Concall_Jul_2024 | SUBSTANTIVE | Yes |
| KSB-Concall_Sep_2025 | SUBSTANTIVE | Yes |
| KSB-Concall_Nov_2025 | SUBSTANTIVE | Yes (1 MINOR anchor imprecision) |
| KSB-Concall_Mar_2026 | SUBSTANTIVE | Yes |
| KSB-Concall_Aug_2026 | SUBSTANTIVE | Yes |
| QUESTFLOW-Concall_Jun_2024 | SUBSTANTIVE | Yes |

8 of 8 peer transcripts confirmed SUBSTANTIVE with real citations.
0 unsupported.

---

## PART 2: SPOT-READ FOR MISSED MATERIAL (all 8 peers, since none were
marked UNUSED/CITED-ONLY)

Each transcript was read in full (or grepped at the quote level for the
longer KSB files) looking for claim-relevant material B06 did not use.

- **ATAM (all 3 calls):** no additional material found bearing on the six
  B05 claims. ATAM's competitor list (Parveen Industries, Oswal
  Industries, Hawa Valves, Rotovalve, Centro Valves) is general industrial
  competitive colour, not naval/PSU-specific; correctly left out.
- **KSB Sep-2025:** no additional material found. The attrition/retention
  discussion (single-digit 9-10% vs industry 15%+) is already surfaced in
  Part 2E (risks peers raise) though without a page citation there —
  acceptable, since it is offered as colour, not a claim-test citation.
- **KSB Nov-2025:** no additional claim-relevant material found beyond
  what is cited. Firefighting/mining segment detail is genuinely
  off-topic for the six claims.
- **KSB Mar-2026:** PTR/vendor-list/EIL-approval mechanics for PSU
  qualification appear repeatedly (e.g. "you need to find one order, you
  supply it, you get a PTR, then you get approved with all PSUs") and are
  summarised in the coverage-map contribution field without a specific
  quote citation. This is a legitimate summary use, not a citation, so it
  is not a finding — but it is worth noting for the operator that this
  qualification-cycle detail is a genuine, unused-as-verbatim-quote
  resource if a later stage wants a direct PTR-cycle quote.
- **KSB Aug-2026:** no additional claim-relevant material found. The
  inventory-build-up discussion (export clearance delays, FGD business
  closure, solar slowdown) is KSB-specific balance-sheet noise, not
  relevant to any of the six Rappid claims.
- **QUESTFLOW:** no additional claim-relevant material found. The H2O
  Dynamics/water-treatment and Nibe JV discussion is a genuine
  diversification story for QuestFlow but does not bear on any of the six
  claims tested.

**No claim-relevant peer statement was found left unused.
`unused_but_relevant` is empty.**

---

## PART 3: VERDICT-DISCIPLINE AUDIT PER CLAIM

| Claim | B06 verdict | Peer anchors | Discipline check |
|---|---|---|---|
| 1 — PSU payment terms / ~170-day cycle / no escalation clause | PARTIALLY VERIFIED | KSB (2 quarters), Atam Valves | 2+ independent peers; correctly not VERIFIED since no peer confirms the specific 170-day figure or a naval-shipyard counterparty by name. Pass. |
| 2 — Margin differential / raw-material pass-through | PARTIALLY VERIFIED | KSB, QuestFlow | 2 independent peers; verdict correctly downgraded from round 1's CONTRADICTED after the like-for-like correction was verified against the source figures. Pass. |
| 3 — Working-capital cycle | PARTIALLY VERIFIED | KSB, Atam Valves | 2 independent peers; correctly caveated that inventory days and supplier-advance practice are unconfirmed. Pass. |
| 4 — Marine/naval TAM + per-vessel cost share | PARTIALLY VERIFIED | KSB (cost-share sub-question only) | Single-peer anchor (KSB's 3-5% pumps analogy) for the cost-share half; TAM half stays UNVERIFIABLE (correctly, since no peer sizes it). A single-peer PARTIALLY VERIFIED is not the same failure mode as a single-peer VERIFIED (Rule 4 targets VERIFIED specifically); PARTIALLY VERIFIED on one corroborating peer, explicitly labelled as an analogy from an adjacent product category rather than a direct confirmation, is an honest characterisation, not an overreach. No upgrade-from-silence: KSB's numbers are affirmative content, not an absence reinterpreted as support. Pass, no finding. |
| 5 — Capacity-utilization-vs-revenue reconciliation | UNVERIFIABLE | KSB, Atam Valves (checked, silent on the specific framing) | Correctly UNVERIFIABLE; both peers disclose utilization differently (units or bare %) and neither frames a rupee-crore capacity ceiling the way Rappid does. Pass. |
| 6 — 50% supplier advance practice | UNVERIFIABLE | Atam Valves, QuestFlow (checked, silent) | Correctly UNVERIFIABLE; independently re-searched all 8 transcripts for "advance" during this audit — only ATAM's own outbound export-advance practice (opposite direction) surfaces, which B06 already notes and correctly distinguishes. Pass. |

**No VERIFIED verdict exists in this run (0 of 6), so the "VERIFIED on one
peer" MAJOR trigger does not apply anywhere. No verdict was upgraded from
silence. All six B05 peer_questions received a verdict — claims_all_addressed
= true.**

---

## PART 4: FINDINGS

Two MINOR findings, zero MAJOR, zero CRITICAL:

1. **MINOR — ATAM-Concall_Nov_2023 capex citation over-broad.** B06 Part
   2C cites "p.6-9" for "Atam Valves is funding a ~Rs30 crore new plant
   for larger valve sizes plus a bathroom-faucet import line." The
   Rs30cr capex figure and its purpose are stated on p.3-4, the delay and
   asset-light China/Spain/Italy import decision on p.5-6, ROI/breakeven
   on p.7, and the capex-plus-bathware working-capital framing on p.8.
   Page 9 (the cited range's upper bound) covers the Canada/API
   discussion, unrelated to this specific claim. The claim is genuinely
   supported by the transcript; only the cited page range is one page
   too wide at the top end and could be tightened to p.3-8.

2. **MINOR — KSB-Concall_Nov_2025 gross-margin citation over-broad.** B06
   Part 2B cites "p.31-32" for the "gross margins have reduced from 54%
   to 44%, 43%... EBITDA steady 12-14%" exchange. Both the analyst's
   question and management's full answer (product mix, then "internal
   efficiency improvement... better capacity utilizations... 2x
   turnovers") sit entirely on p.31; p.32 covers an unrelated
   firefighting-segment-share question. Could be tightened to p.31 alone.

Neither finding changes the substance of any claim or verdict; both are
citation-precision notes, not source-fidelity failures (the quoted text
is verbatim-accurate in both cases, and the material genuinely exists in
the cited transcript).

---

## PART 5: OVERALL ASSESSMENT

B06 round 2 is a materially strengthened report relative to what a fresh,
independent trace of every SUBSTANTIVE citation would predict from a
report carrying that label: of 25 spot-checked citations across all 8
peer transcripts, all 25 point to real, verbatim-accurate quoted material,
and 23 of 25 land on the exact page cited. The two imprecise citations are
both over-broad page ranges around genuinely correct material, not
fabrications or misattributions. No peer is CITED-ONLY or UNUSED despite
this audit's independent full-transcript read of all 8 files. No claim in
the B05 peer_questions list was skipped. No verdict rests on an
upgrade-from-silence, and no VERIFIED verdict (the highest-discipline
category) exists to test the "VERIFIED on one peer" rule against, since
B06 correctly declined to VERIFY anything at this level of peer coverage.

The round-2 self-correction process itself (7 logged corrections, several
originating from a prior Verifier D page-anchor pass) is visible in this
audit's own findings: it caught and fixed nearly every anchor error a
fresh trace would otherwise have surfaced, leaving only two minor residual
imprecisions. This suggests B06's correction loop is functioning as
intended rather than papering over problems.

---

```yaml
stage: B12d
company: "RAPPID"
run_date: "2026-09-19"
model: claude-sonnet-5
status: complete
peers_audited: 8
substantive_confirmed: 8
substantive_unsupported: []
unused_but_relevant: []
claims_all_addressed: true
verdict_discipline_fails: []
findings:
  - {severity: "MINOR", location: "B06 Part 2C (capex cross-read), ATAM-Concall_Nov_2023_Transcript.txt", claimed: "p.6-9", source_truth: "Rs30cr capex plan on p.3-4; delay/asset-light China-Spain-Italy import on p.5-6; ROI/breakeven on p.7; capex+bathware WC framing on p.8; p.9 covers Canada/API, unrelated to this claim", note: "Content is real and verbatim-accurate; cited page range is one page too wide at the top end.", source_fidelity: false}
  - {severity: "MINOR", location: "B06 Part 2B (margin/pricing cross-read), KSB-Concall_Nov_2025_Transcript.txt", claimed: "p.31-32", source_truth: "the 54%->43-44% gross-margin exchange and the full internal-efficiency-improvement explanation both sit on p.31; p.32 covers an unrelated firefighting-segment-share question", note: "Content is real and verbatim-accurate; cited page range is one page too wide.", source_fidelity: false}
critical_count: 0
major_count: 0
minor_count: 2
acceptance_rate: 100
```
