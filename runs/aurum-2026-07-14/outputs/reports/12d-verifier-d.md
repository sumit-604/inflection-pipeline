# VERIFIER D — PEER COVERAGE AUDIT (B12d)
AURUM | run_date 2026-07-14 | Model: claude-sonnet-5
Scope: B06 peer report (outputs/reports/06-peers.md) + B06 block (outputs/blocks/B06-peers.yaml), audited directly against the 14 raw peer transcripts (CARTRADE x4, RATEGAIN x2, ZAGGLE x4, NAZARA x4) and against B05's peer_questions list (outputs/blocks/B05-concall.yaml).

Fresh, independent read. No other verifier's output consulted.

---

## PART 1: PEER-QUESTION COMPLETENESS CHECK

B05.peer_questions lists exactly 9 claims with a `check_peers` list per claim. B06 Part 1 addresses all 9, in the same order, with the same wording, and restricts its evidence search to the peers B05 specified for each claim (e.g. Claim 4 and Claim 9 correctly restricted to ZAGGLE/RATEGAIN/NAZARA, not CARTRADE; Claim 8 correctly restricted to CARTRADE only). No skipped claims. **claims_all_addressed: true.**

---

## PART 2: SUBSTANTIVE-CITATION SPOT CHECK

For every peer/quarter B06 marks SUBSTANTIVE, I located the cited quote directly in the named transcript. Results:

| # | B06 citation | Transcript located | Verdict |
|---|---|---|---|
| 1 | CARTRADE Q1 FY26 (Aug-2025, Vinay Sanghi): "TAM is almost limitless... growth completely dependent on what we can execute" | CARTRADE-Aug-2025, line 598-599, verbatim, correct speaker | CONFIRMED |
| 2 | RATEGAIN Q2 FY26 (Nov-2025, Bhanu Chopra): "$7 billion" addressable market | RATEGAIN-Nov-2025, line 271-273, verbatim, correct speaker | CONFIRMED |
| 3 | ZAGGLE Q2 FY25 baseline (Nov-2024, Avinash Godkhindi): "INR79,000 crores" fleet TAM | ZAGGLE-Nov-2025_Transcript_2 (correctly the Nov-2024 Q2 FY25 call per B06's own input_gaps note), line 202/555, verbatim | CONFIRMED |
| 4 | RATEGAIN Q2 FY26 (Nov-2025, Bhanu Chopra): NRR "110 to 100," cross-sell "not been as optimal," "farmers" hires | RATEGAIN-Nov-2025, line 463-487, verbatim | CONFIRMED |
| 5 | ZAGGLE cross-sell 16% (IPO) -> 20% (Sep-2024) -> 21% (Sep-2025), Q2 FY26 call Nov-2025, Avinash Godkhindi | ZAGGLE-Nov-2025 (Q2 FY26 call), line 323-324 and 727-731: "our cross-sell percentage around IPO was about 16%... upped it to about 21%"; analyst cites "20% in September 2024... now we are just at 21%" | CONFIRMED — all three data points sourced from the SAME Nov-2025 call as management's own retrospective recap, consistent with how B06's Part 1 text cites it |
| 6 | RATEGAIN Q3 FY26 (Feb-2026, Bhanu Chopra): "up to 300% increase in ancillary revenue, 75% improvement in NPS, automation of up to 80% of guests queries" | RATEGAIN-Feb-2026, line 107-108, verbatim, correct speaker | CONFIRMED |
| 7 | ZAGGLE Q3 FY26 (Feb-2026, Raj Narayanam): dev cycle "75 to 80 days" to "under 30 days" | ZAGGLE-Feb-2026, line 741-742, verbatim | CONFIRMED |
| 8 | NAZARA Q2 FY26 (Nov-2025): "WCC4... completely coded in AI using Claude" | NAZARA-Nov-2025, line 443-444, verbatim ("WCC 4," minor spacing only) | CONFIRMED |
| 9 | CARTRADE counter-cyclicality: "whether the industry is down... our growth rates have been maintained" (Q3 FY26 Jan-2026) and "institutional [business] is not necessarily cyclical... repossession side and the retail side will keep growing" (Q4 FY26 May-2026) | CARTRADE-Feb-2026 line 337 and CARTRADE-May-2026 line 326-327 | CONFIRMED |
| 10 | CARTRADE Q4 FY26 (May-2026, Vinay Sanghi): ROE ~10% "because of the cash balance," "if the cash balance didn't exist, the ROE would be much higher" | CARTRADE-May-2026, line 678-682, verbatim | CONFIRMED |
| 11 | CARTRADE "declining a live acquisition (CarDekho) after diligence," INR1,244cr cash | CARTRADE-May-2026 line 112 (cash figure exact); CARTRADE-Feb-2026 line 296-311 (CarDekho) | CONFIRMED, with a note: transcript language is "put it on hold," not an outright "decline" — B06's word choice ("declining") is a fair but slightly stronger paraphrase than management's own framing. MINOR. |
| 12 | RATEGAIN Q3 FY26 (Feb-2026, Rohan Mittal): "$5 million to $6 million" GTM investment, "roughly 4% of our EBITDA at that time" | RATEGAIN-Feb-2026, line 400-402, verbatim, correct speaker | CONFIRMED |
| 13 | RATEGAIN Q3 FY26 (Feb-2026, Rohan Mittal): "$12 million in annualized cost savings... within 100 days of the Sojern deal" | RATEGAIN-Feb-2026: figure is "$12 million in annualized integration synergies" (line 188, Bhanu Chopra's closing remarks) and "$12 million in annualized cost savings in Phase 1" (line 245, Rohan Mittal) — but the transcript states the window as "first 90 days" (line 188 and again line 250, "our area of focus during the first 90 days"), never "100 days" | **MISMATCH** — B06 states 100 days; transcript says 90 days, twice, in two different speakers' remarks. The $12M figure itself and its EBITDA-base framing are accurate; only the day count is wrong. |
| 14 | ZAGGLE Q4 FY26 (May-2026, Avinash Godkhindi): "INR30 crores in H1 to INR56 crores in H2 FY26" capitalized tech/AI spend | ZAGGLE-May-2026, line 362 (partial match, "crores in H1 to INR56 crores in H2 FY26" — the "30" is cut at the top of the extract but clearly the intended figure given the paired framing) | CONFIRMED (reasonable, minor extract-boundary artifact, not B06's error) |
| 15 | NAZARA Sportskeeda "21-38%" revenue loss to Google Core update, "3+ quarters to recover" | NAZARA-Aug-2025 line 190 (21% YoY drop, Q1 FY26, tied to March-2025 Google Core update); NAZARA-May-2026 line 239 (38% FY26 decline, same underlying Google Core issue per line 241 "because of the Google Core issue... highlighted in the past calls"); NAZARA-Nov-2025 line 518-525 (PFN comparable took "3 quarters," Sportskeeda "two quarters... so another couple of updates") | CONFIRMED — legitimate synthesis across three calls tracking the same event's cumulative impact, not fabricated |
| 16 | ZAGGLE OCF: "H1 FY26 OCF of -INR19cr, later -INR33-34cr" | ZAGGLE-Nov-2025 line 353-363: "-INR19 crore" is stated as OCF **before taxes** for H1 FY26; the "INR 33 crore" figure in the same passage is explicitly a **year-on-year delta** ("if you look at your H1 last year versus this year, there is a sharp dip of almost like INR 33 crore"), not a second, later, worse absolute OCF reading. The actual later data point (ZAGGLE-May-2026, line 259-262) shows OCF **improving** to "minus INR6 crores," the opposite direction from what "later -INR33-34cr" implies. | **MISMATCH / MISLEADING** — B06 conflates a YoY delta with a sequential absolute OCF figure and asserts a trend (further deterioration) that the transcripts do not support; the actual later trend is improvement. |
| 17 | ZAGGLE "no-credit-risk governance stance, repeatedly stated" | ZAGGLE-Nov-2025, lines 517-519, 753-754, 770-771 (three separate instances); ZAGGLE-May-2026, line 442 | CONFIRMED, "repeatedly" is accurate |
| 18 | RATEGAIN Skift Travel Health Index citation | RATEGAIN-Nov-2025, line 150, verbatim | CONFIRMED |
| 19 | CARTRADE AI-moat "four levels of data" framing (Q2 FY26, cited as CITED-ONLY precursor) | CARTRADE-Nov-2025, line 524-528 and 545-547, verbatim | CONFIRMED — B06's CITED-ONLY classification for this transcript (precursor material, no new decisive evidence versus the fuller Q3 answer) is a fair characterization |

**16 of 19 spot-checked citations fully confirmed verbatim in the stated transcript with correct speaker and quarter. Two numeric/directional errors found** (RATEGAIN 90-vs-100-days; ZAGGLE OCF delta-vs-absolute conflation), one minor word-choice gloss (CarDekho "declining" vs "put on hold").

---

## PART 3: COVERAGE-MAP ACCURACY CHECK (Part 3 of B06, "contribution" column)

One material misattribution found. B06's peer_coverage_map row for **ZAGGLE Q2 FY25 baseline (Nov-2024 call)** states its contribution is: "Source of the Rs79,000cr fleet-TAM figure (Claim 1) **and the earliest cross-sell % baseline (16% at IPO) used in the Claim 3 trend line**."

I searched the full Nov-2024 baseline transcript (ZAGGLE-Concall_Nov_2025_Transcript_2.txt — B06 itself notes in input_gaps that this file is mislabeled and is actually the Nov-2024/Q2 FY25 call) for any cross-sell percentage disclosure. None exists; the only "16%" figure in that transcript is an unrelated EBITDA-margin aspiration exchange (Deepak Poddar: "earlier... 15%, 16% is what we might look at... over the medium to long term," referring to margin targets, not cross-sell). The actual "16% at IPO" cross-sell figure is disclosed entirely within the **Nov-2025 (Q2 FY26) call** as management's own retrospective recap (confirmed above, Part 2 item 5) — the same call already correctly credited elsewhere in the coverage map for the 21% figure.

So the Q2 FY25 baseline transcript is genuinely SUBSTANTIVE (it does supply the real Rs79,000cr fleet-TAM figure), but the second half of its stated "contribution" — being the source of the 16% cross-sell baseline — is not supported by that transcript. The correct source for all three cross-sell data points (16%, 20%, 21%) is the single Nov-2025 call. This is exactly the class of "SUBSTANTIVE without a real, findable citation" the audit is designed to catch, though it is contained to one data point within an otherwise-real citation.

Note: B06's Part 1 narrative text (Claim 3 discussion) does NOT repeat this error — it correctly attributes the full 16%->20%->21% trend line to the Nov-2025 call. The misattribution is confined to the Part 3 coverage-map table's "contribution" description.

---

## PART 4: UNUSED / CITED-ONLY PEER SPOT-READ

B06 marks CARTRADE Q2 FY26 (Oct/Nov-2025), NAZARA Q1 FY26 (Aug-2025), and NAZARA Q3 FY26 (Feb-2026) as CITED-ONLY. I keyword-scanned all three for TAM/billion/counter-cyclicality/market-share/valuation-multiple/private-company content that could bear on any of the 9 claims:

- **CARTRADE Q2 FY26**: only repeats the "TAM has expanded dramatically... limitless TAM" line already sourced from Q1 FY26 (line 849-853) — a repeat, not new decisive evidence, consistent with B06's characterization. The AI/proprietary-data "four levels of data" framing genuinely does first appear here (confirmed above) and is correctly flagged as a precursor.
- **NAZARA Q1 FY26 (Aug-2025)**: no TAM dollar figure, no counter-cyclicality claim, no valuation-multiple discussion found. "Market share" mentions are all about PokerBaazi's gaming segment, unrelated to any of the 9 claims.
- **NAZARA Q3 FY26 (Feb-2026)**: no TAM, billion, counter-cyclicality, market-share, or valuation content found at all beyond one unrelated "market share" mention (line 463, skill-based real-money-gaming context).

I also checked whether RATEGAIN or ZAGGLE (not in B05's check_peers list for Claims 5 and 6) contain material B06 should have surfaced anyway: no Bangalore/Pune/IT-hiring-slowdown content in either (RATEGAIN's one "hiring" hit is about GTM sales-team hiring, unrelated); no public-vs-private valuation-gap language in either. B06's restriction to the B05-specified peer subset for these two claims does not appear to have missed anything material.

**No unused-but-relevant findings of MAJOR weight identified.** The CITED-ONLY classifications are defensible; B06 tried the right transcripts.

---

## PART 5: VERDICT DISCIPLINE AUDIT

| Claim | Verdict | Peers cited | Discipline check |
|---|---|---|---|
| 1 (TAM $10bn) | UNVERIFIABLE | 4 checked, all silent on India PropTech specifically | Correct — genuine silence, not upgraded |
| 2 (Rs38,000cr TAM) | UNVERIFIABLE | 1 checked (CARTRADE), no split disclosed | Correct |
| 3 (cross-sell magnitude) | PARTIALLY VERIFIED | ZAGGLE + RATEGAIN (2 independent peers) | Correct — 2-peer bar met for partial (direction+magnitude split across 2 peers), no VERIFIED overreach |
| 4 (AI-moat specificity) | CONTRADICTED | RATEGAIN + ZAGGLE (2 independent peers) | Correct discipline — 2 peers cited |
| 5 (IT-hiring bifurcation) | UNVERIFIABLE | 2 checked, both silent | Correct |
| 6 (valuation gap) | UNVERIFIABLE | 2 checked, neither on-point | Correct |
| 7 (counter-cyclicality) | PARTIALLY VERIFIED | CARTRADE only (1 peer) | Correct — single-peer correctly kept at PARTIALLY VERIFIED, not upgraded to VERIFIED, per rule 4 |
| 8 (market-share displacement) | UNVERIFIABLE | 1 checked, silent | Correct |
| 9 (AI capex specificity) | CONTRADICTED | RATEGAIN + ZAGGLE (2 independent peers) | Correct discipline — 2 peers cited |

No VERIFIED verdicts issued (0 of 9), so the "VERIFIED resting on one peer" failure mode cannot occur here — B06 is if anything conservative, never crossing the 2-peer bar into a full VERIFIED even where two peers converge (it could arguably have called Claim 4 or Claim 9 "VERIFIED [that peers show more specificity]" given 2 independent peer confirmations of the same direction, but instead used the arguably more conservative CONTRADICTED label for the underlying Aurum claim, which is a defensible construction). No verdict is upgraded from silence — every UNVERIFIABLE is explicitly grounded in "no peer evidence either way," not treated as corroborating or contradicting. **No verdict-discipline failures found.**

---

## PART 6: FINDINGS

| Severity | Location | Description |
|---|---|---|
| MAJOR | B06-peers.yaml, `peer_coverage_map` row for ZAGGLE Q2 FY25 baseline (Nov-2024 call); 06-peers.md Part 3 table | Coverage-map "contribution" description claims this transcript is the source of "the earliest cross-sell % baseline (16% at IPO)." No cross-sell percentage of any kind appears in that transcript. The real source of all three cross-sell data points (16% IPO, 20% Sep-2024, 21% Sep-2025) is the Nov-2025 (Q2 FY26) call, which is already separately and correctly credited elsewhere in the same table. Part 1's Claim 3 narrative text does not repeat this error. |
| MAJOR | 06-peers.md, Claim 9 discussion (Part 1) | "$12 million in annualized cost savings... within 100 days of the Sojern deal" — transcript states "first 90 days" twice (RATEGAIN-Feb-2026, lines 188 and 250), never 100. The $12M figure and its EBITDA-base context are accurate; only the day count is wrong. |
| MAJOR | 06-peers.md Part 2E and B06-peers.yaml `risks_peers_raise` | "H1 FY26 OCF of -INR19cr, later -INR33-34cr" mischaracterizes the source: the "-33/34cr" figure in the transcript (ZAGGLE-Nov-2025, line 353-363) is explicitly a year-on-year delta ("H1 last year versus this year... a sharp dip of almost like INR 33 crore"), not a second, later, worse absolute OCF reading, and the actual next data point available (ZAGGLE-May-2026, line 259-262) shows OCF improving to -INR6cr, the opposite of the implied further-deterioration trend. The underlying point (ZAGGLE analysts press OCF-vs-PAT divergence every quarter, unlike Aurum's silent record) remains valid and well-supported independent of this specific figure. |
| MINOR | 06-peers.md, Part 2C / Claim 6 discussion | CARTRADE's CarDekho decision is described as "declining a live acquisition... after diligence"; management's own language is "put it on hold," a softer framing than "declining." Directionally consistent, minor overstatement. |
| MINOR | 06-peers.md Part 3 | "WCC4" spacing vs. transcript's "WCC 4" — cosmetic, not substantive. |

---

## PART 7: OVERALL ASSESSMENT

B06 used the four provided peer companies substantively and honestly. All four peers legitimately earn the SUBSTANTIVE tag in the aggregated company-level rating — each supplies at least one real, verbatim, correctly attributed citation feeding a Part 1 verdict or a Part 2 cross-read finding, confirmed directly against the raw transcripts in the large majority of spot checks (16 of 19 fully clean). The CITED-ONLY calls for three specific quarter-transcripts are defensible: targeted re-scans of those three transcripts turned up no missed material bearing on any of the 9 claims. The high UNVERIFIABLE count (5 of 9) is not a shortcut — for each of those five, B06 checked the peers B05 specified, found genuine silence (business-model mismatch, not a search failure), and said so plainly rather than papering over the gap. Verdict discipline (single-peer capped at PARTIALLY VERIFIED, no VERIFIED-from-silence, no VERIFIED at all in this run) is sound and, if anything, conservative.

Against that, three MAJOR-severity numeric/attribution errors were found on close verification: a coverage-map misattribution (cross-sell baseline wrongly credited to the wrong transcript, though the correct transcript is cited elsewhere in the same table), a day-count error (90 vs 100 days) in an otherwise-accurate quote, and a delta-vs-absolute conflation in the OCF risk-flagging paragraph that actually overstates the deterioration narrative relative to what the fuller transcript record shows (OCF was improving by the most recent call, not worsening). None of these three changes any of the 9 claim verdicts or the net_narrative_effect characterization — the underlying substance of each claim (cross-sell magnitude gap, RateGain integration-synergy specificity, ZAGGLE's OCF scrutiny asymmetry with Aurum) survives independent of the specific erroneous number. They are precision failures on a background of otherwise strong, verbatim-checkable sourcing discipline, not fabrication or invented evidence.

```yaml
stage: B12d
company: "AURUM"
run_date: "2026-07-14"
model: claude-sonnet-5
status: complete
peers_audited: 4
substantive_confirmed: 4
substantive_unsupported: []
unused_but_relevant: []
claims_all_addressed: true
verdict_discipline_fails: []
findings:
  - {severity: "MAJOR", location: "B06-peers.yaml peer_coverage_map (ZAGGLE Q2 FY25 baseline row); 06-peers.md Part 3", description: "Coverage map credits the Nov-2024 baseline transcript as source of the '16% at IPO' cross-sell figure; no cross-sell percentage appears in that transcript. All three cross-sell data points (16/20/21%) actually come from the Nov-2025 Q2 FY26 call, already correctly credited elsewhere in the same table. Part 1 narrative text does not repeat the error."}
  - {severity: "MAJOR", location: "06-peers.md Claim 9 discussion", description: "States RATEGAIN's $12M annualized cost savings were achieved 'within 100 days of the Sojern deal'; transcript states 'first 90 days' twice (lines 188, 250 of Feb-2026 call). Figure and EBITDA-base context otherwise accurate."}
  - {severity: "MAJOR", location: "06-peers.md Part 2E; B06-peers.yaml risks_peers_raise", description: "'H1 FY26 OCF of -INR19cr, later -INR33-34cr' conflates a stated year-on-year OCF delta (~INR33cr) with a second, later, worse absolute OCF reading; the actual subsequent data point (May-2026 call) shows OCF improving to -INR6cr, contrary to the implied further-deterioration trend. Underlying point about ZAGGLE's OCF scrutiny vs Aurum's silence remains valid independent of this figure."}
  - {severity: "MINOR", location: "06-peers.md Part 2C / Claim 6", description: "CARTRADE's CarDekho decision described as 'declining' the deal; management's own language was 'put it on hold' -- softer framing, directionally consistent."}
  - {severity: "MINOR", location: "06-peers.md Part 3", description: "'WCC4' vs transcript's 'WCC 4' -- cosmetic spacing only."}
critical_count: 0
major_count: 3
minor_count: 2
acceptance_rate: 84   # 16 of 19 spot-checked citations fully clean; all 4 peers correctly handled at the coverage-classification level; peers correctly handled 4/4 = 100%, citation-level spot-check clean rate 16/19 = 84%; reported figure is the citation-level rate as the more conservative/informative measure
peer_utilisation: 1.0   # 4 of 4 provided peers used substantively per the rubric's definition (contributed >=1 real, verbatim, correctly-sourced citation to a Part 1 verdict or Part 2 finding); 3 of 19 spot-checked individual citations had numeric/attribution defects, not full fabrications

```
