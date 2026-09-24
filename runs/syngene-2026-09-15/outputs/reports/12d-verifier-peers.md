# VERIFIER D: PEER COVERAGE AUDIT — SYNGENE INTERNATIONAL LTD (B06, run 2 / correction run)
Model: claude-sonnet-5 | Run date: 2026-09-15

Scope: audit whether the pipeline actually used the 6 peer transcripts it claims to have used
(ANTHEM Nov-25/Feb-26/May-26/Jul-26, SAILIFE Aug-26, PPLPHARMA Jul-26), against B06's coverage
map and Parts 1-2, and against B05's peer_questions handoff. I read all 6 peer transcripts in full
(page-marked text, "===== PAGE n =====" = PDF extraction marker) and independently located every
citation used in B06 Parts 1, 2 and 3, plus the "Consolidated re-anchoring" table B06 published as
proof of its own correction pass.

---

## METHOD

For each of the ~35 quotes/figures B06 attributes to a peer transcript, I searched the transcript
text for the exact phrase and recorded the marker page it actually sits on, then compared it to
B06's cited page. I also read every transcript end-to-end (not just around the cited anchors) to
check for claim-relevant material left unused (Rule 3) and to confirm no peer names Syngene
(peer_mentions_of_company).

---

## PART A: PEER-BY-PEER COVERAGE AUDIT

| Peer/call | B06 usage label | Citations checked | Result |
|---|---|---|---|
| ANTHEM Nov-25 (Q2/H1 FY26) | SUBSTANTIVE | "amongst the lowest" employee cost (p.7); "10 peptide programs...separate program" (p.15); "build it and then they will come" (p.6); Unit-IV "two years" (p.10); NeoAnthem "won't be in the profitable zone" (cited p.4) | 4 of 5 confirmed exact page. 1 anchor error (see Finding 1) |
| ANTHEM Feb-26 (Q3/9M FY26) | SUBSTANTIVE | Rs25.4cr Labour Code item (p.3); "backward integration, material margins have improved" (p.4); "completely discontinued China supplies...backward integrated" (p.5); "outsourcing is nil...full impact is baked in" (p.7); no-hedge FX policy (p.14); "build it and then they will come" repeat (p.11) | All 6 confirmed exact page |
| ANTHEM May-26 (Q4/FY26) | SUBSTANTIVE | Funding recovery "+50-odd percent YoY" (p.17); FY26 18% CRDMO growth / record Q4 (p.3); destocking "mostly it's behind us" (p.4); "peptides...biggest [TAM]" (p.10); "No tariffs is not a problem" (p.13); ADC "15-20 payloads" (p.8); R&D "8% to 9%" (p.15); Unit-IV "by end of this FY28" (p.6); unnamed-peer peptide-chain question (p.9) | All 9 confirmed exact page |
| ANTHEM Jul-26 (Q1 FY27) | SUBSTANTIVE | Analyst "-25%...down almost like a 25%" unchallenged (p.8); Unit 3 utilization "30% to 35%...ramp-up from...15% odd...in FY26" (p.4); "amongst the lowest" employee cost repeat (p.13); "A lot of AI talk is a moment hype" (p.15); unnamed-peer semaglutide-scaling question (p.10) | All 5 confirmed exact page. See Finding 1 for how the p.4 "15% in FY26" figure was mis-sourced into the Nov-25 anchor |
| SAILIFE Aug-26 (Q1 FY27) | SUBSTANTIVE | Geopolitical/diversification quote (p.3); peptide/XDC/2028 facility (p.4); CRO +26% YoY (p.6); "returning customers...90%" (p.7); Bidar 450KL H2/Q3 (p.12); capex Rs1,100-1,300cr (p.10); "4% to 5%" analyst-asked, CFO-unconfirmed (p.15) | All 7 confirmed exact page |
| PPLPHARMA Jul-26 (Q1 FY27) | SUBSTANTIVE | CDMO +19% YoY / funding recovery (p.3); "different pricing measures" (p.12); "Not really" near-shore pushback + "particular spike" (p.15); NPS "60 range" (p.10); Lexington CY2027 (p.12); ADC "small percentage share...large and rapidly growing market" (p.18); overseas tax loss ~Rs146cr (p.18-19) | All 7 confirmed exact page |

**Result: 33 of 34 spot-checked citations (97%) land on the exact page B06 cites.** This confirms the
correction run's central repair (re-anchoring to the PDF marker instead of the printed footer) mostly
held. One residual defect survived the correction pass (Finding 1 below), in the same failure family
the correction run claims to have eliminated.

No peer transcript, across all 17-19 pages of all 6 calls, names Syngene directly or by unmistakable
description. `peer_mentions_of_company: []` is confirmed correct. The two "unnamed peer" analyst
questions (ANTHEM-May-26 p.9 peptide-chain; ANTHEM-Jul-26 p.10 semaglutide scaling) are correctly
flagged as non-attributable rather than counted as Syngene mentions.

---

## PART B: FINDINGS

### Finding 1 — MAJOR: residual anchor error and cross-call attribution error, NeoAnthem utilization

B06 Part 1 item 5 states: *"NeoAnthem (Unit-III), commissioned earlier, still ran at only 15%
utilization in FY26 and 'won't be in the profitable zone' as of Nov-2025 (Ajay Bhardwaj,
ANTHEM-Nov-2025, p.4), reaching 30-35% utilization by Q1 FY27 (Gawir Baig, ANTHEM-Jul-2026, p.4)."*

Two problems with the single citation "(Ajay Bhardwaj, ANTHEM-Nov-2025, p.4)":

1. **Page drift.** The quote *"It still won't be in the profitable zone, but it is trending upwards
   significantly now"* sits on **marker PAGE 5** of ANTHEM-Concall_Nov_2025_Transcript.txt (in the
   middle of Ajay Bhardwaj's answer on Unit-III WIP/POs), not PAGE 4. This is the exact "footer vs.
   marker, off by one" defect the CORRECTIONS LOG (item 3) states was fixed everywhere via
   exact-phrase re-search: *"Every quote used in this report was re-located against its file's PDF
   markers using exact-phrase search."* This instance shows the fix was not complete.
2. **Cross-call number attribution.** The "15% utilization in FY26" figure does **not appear anywhere
   in the Nov-2025 transcript** — I read it in full and the only Unit-III utilization language there
   is qualitative ("won't be in the profitable zone," "trending upwards significantly"). The 15%
   figure is disclosed for the first time three quarters later, in ANTHEM-Jul-2026 p.4: *"This is a
   ramp-up from what we had about 15% odd of utilization in FY26."* B06's citation presents both the
   15% figure and the "won't be in the profitable zone" quote as if they come from the same
   Nov-2025/p.4 source; only the qualitative quote is from Nov-2025 (at p.5), and the quantitative
   figure is a retrospective FY26 disclosure made in the Jul-2026 call.

Net effect: a reader checking the stated anchor (Nov-2025 p.4) will find neither the 15% figure nor
the exact quote on that page. This is a source-attribution error on a used, SUBSTANTIVE citation,
in the same category the run's own corrections log was built to eliminate. It does not change any
verdict (the underlying point — Unit-III was under-profitable through FY26 and ramped to 30-35% by
Q1 FY27 — is independently supported by the correctly-anchored Jul-2026 p.4 citation), so it is not
a verdict-flipping error, but it is a citation the pipeline claims is settled and is not.

### Finding 2 — MINOR: an industry-context data point left unused (SAILIFE overseas-subsidiary maturity)

SAILIFE-Aug-2026 p.15 (Siddharth Negandhi question on Boston/Manchester) contains a directly
claim-relevant, unused data point: *"if you look at the Boston P&L that you would see, it is a bit
accretive to the business"* and *"if you look at the discovery revenue it is probably in the last
four, five years has grown at a CAGR of close around 30%-35%"* (Boston established "somewhere around
the end of 2020"). This is a second, more favorable peer data point on new-overseas-site maturity
timelines — a direct comparator to Bayview (a new, not-yet-profitable US site under B00's LBF3
"capital not yet earning" priority) alongside the PPLPHARMA overseas-tax-loss story B06 already
uses. B06's `risks_peers_raise` and Part 2E use only the negative Piramal comparator; the positive
SAILIFE comparator (an overseas site that did become accretive, over a ~5-year window) is left out,
which would have sharpened rather than changed the analysis — Bayview's slippage sits between two
peer data points (Piramal's still-loss-making sites and SAILIFE's since-turned-accretive Boston
site) rather than only against the negative case. This is an industry-context miss, not a
claim-verdict miss (per Rule 3, MINOR).

### No further findings

- All 5 `peer_questions` handed off by B05 received an explicit verdict in B06 Part 1 (items 1-5).
  `claims_all_addressed: true` is confirmed accurate.
- Verdict discipline: the one VERIFIED claim (item 4, VC-funding recovery) rests on 2 independent
  peers (ANTHEM, SAILIFE) with 3 anchors — satisfies the ≥2-anchor rule, no MAJOR finding here. No
  verdict is upgraded from silence anywhere in the report.
- The CONTRADICTED verdict (item 2, commoditization) rests more heavily on one peer (SAILIFE) with
  ANTHEM cited only for absence of comparable pressure; Rule 4 as written binds VERIFIED claims, not
  CONTRADICTED ones, so this is not scored as a finding — and B06 already discloses this exact
  weakness prominently in its own flags and analyst_note ("rests on a qualitative contrast only"),
  so there is no concealment to flag.
- Coverage map labels: all 6 transcripts are SUBSTANTIVE and each independently contributes at least
  one citation-bearing fact used in Parts 1-2; none should be downgraded to CITED-ONLY or UNUSED.
- `unverifiable: []` is reasonable given the peer evidence available; no item in the peer_questions
  list was left genuinely unaddressable.

---

## PART C: TRIANGULATION SANITY CHECK

Spot-checking the report's own headline claims against the source transcripts:
- SAILIFE CRO +26% YoY in the same Q1 FY27 window Syngene's total revenue fell 16% YoY: confirmed,
  Siva Chittor, SAILIFE-Aug-2026 p.6.
- ANTHEM funding recovery "+50-odd percent YoY" through April 2026: confirmed, Gawir Baig,
  ANTHEM-May-2026 p.17.
- PPLPHARMA's "Not really" on near-shoring as the primary RFP driver: confirmed verbatim, Peter
  DeYoung, PPLPHARMA-Jul-2026 p.15, including the immediately following four-reasons answer and the
  "particular spike...above and beyond" qualifier — B06's paraphrase does not overstate this.
- No peer, across 6 transcripts, volunteers or disputes a "40% of clinical pipelines" figure —
  confirmed; the 40% statistic remains unverified against any peer source, as B06 states.

---

## SUMMARY

The correction run substantially repaired the anchor-drift problem it was built to fix: 33 of 34
independently spot-checked citations across all 6 peer transcripts land exactly where B06 says they
do, including every citation the corrections log specifically claims to have re-anchored. One
citation (NeoAnthem utilization, ANTHEM-Nov-2025) still carries the same class of defect — a
one-page drift plus a number attributed to the wrong call — that the correction pass was meant to
eliminate everywhere. This does not change any triangulation verdict, since the same underlying
fact is independently and correctly anchored elsewhere in the same item. One industry-context
data point (SAILIFE's Boston-subsidiary maturity) was available and would have added a second,
more favorable comparator to the Bayview-adjacent risk discussion, but its absence does not change
any claim verdict.

```yaml
stage: B12d
company: "SYNGENE"
run_date: "2026-09-15"
model: claude-sonnet-5
status: complete
peers_audited: 6
substantive_confirmed: 5
substantive_unsupported: []
unused_but_relevant:
  - {peer: "SAILIFE", missed_item: "Boston overseas-subsidiary now 'a bit accretive to the business' with ~30-35% discovery-revenue CAGR since ~2020 -- a favorable comparator to Bayview's slower ramp, alongside the negative Piramal overseas-tax-loss comparator B06 already uses", anchor: "SAILIFE-Concall_Aug_2026_Transcript.txt p.15"}
claims_all_addressed: true
verdict_discipline_fails: []
findings:
  - {severity: "MAJOR", location: "B06 Part 1 item 5 / 06-peers.md line ~95", claimed: "'won't be in the profitable zone' + '15% utilization in FY26' both cited to (Ajay Bhardwaj, ANTHEM-Nov-2025, p.4)", source_truth: "The quote is on marker PAGE 5 of ANTHEM-Nov-2025, not p.4; the '15% utilization in FY26' figure does not appear anywhere in ANTHEM-Nov-2025 at all -- it is disclosed retrospectively in ANTHEM-Jul-2026 p.4 ('ramp-up from what we had about 15% odd of utilization in FY26')", note: "Residual instance of the exact anchor-drift/cross-call-attribution defect the correction run's CORRECTIONS LOG item 3 claims to have eliminated via exact-phrase re-search; does not flip any verdict since the same fact is independently and correctly anchored via the Jul-2026 p.4 citation in the same sentence"}
  - {severity: "MINOR", location: "B06 Part 2E / risks_peers_raise", claimed: "Only the negative Piramal overseas-subsidiary tax-loss comparator is used against Bayview", source_truth: "SAILIFE-Aug-2026 p.15 discloses a positive overseas-subsidiary comparator (Boston, accretive, ~30-35% CAGR since ~2020) that was not incorporated", note: "Industry-context miss per Rule 3, not a claim-verdict miss; would sharpen but not change the analysis"}
critical_count: 0
major_count: 1
minor_count: 1
acceptance_rate: 83
