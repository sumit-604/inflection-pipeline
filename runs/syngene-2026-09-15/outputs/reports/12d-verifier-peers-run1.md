# VERIFIER D: PEER COVERAGE AUDIT — SYNGENE B06
Run date: 2026-09-15 | Model: claude-sonnet-5 | Inputs: 6 peer transcripts (ANTHEM x4, SAILIFE x1, PPLPHARMA x1), B06-peers.yaml + 06-peers.md, B05-concall.yaml peer_questions

Scope note: this run's peer set is 6 transcripts (3 tickers), not the "12 peers" the generic rubric text assumes. Audited what is actually present.

---

## PART 1: PEER COVERAGE AUDIT TABLE

All six transcripts are marked SUBSTANTIVE in B06's peer_coverage_map, and none is marked UNUSED/CITED-ONLY, so rule 3's UNUSED spot-read does not apply as written; instead every peer's SUBSTANTIVE claim was tested by locating its cited quotes.

| Peer/call | Contribution claimed | Citation located in transcript? | Anchor accuracy |
|---|---|---|---|
| ANTHEM Nov-25 | Modality/peptide narrative, "build it and they will come", NeoAnthem not-yet-profitable | YES — "build it and then they will come" (line 228, actual PDF p.6, matches cite p.6); "won't be in the profitable zone" (actual PDF p.5, matches cite p.5); Unit-IV "two years" (actual PDF p.6, cited p.5 — off by one); employee-cost "amongst the lowest" (actual PDF p.7, bundled cite "p.6" — off by one) | Mostly correct, two 1-page drifts |
| ANTHEM Feb-26 | Destocking explanation, backward-integration margin story, Labour Code exceptional item, no-hedge FX | YES — Rs25.4cr exceptional item (actual PDF p.3, cited p.2 — off by one); China-sourced-intermediate backward-integration story (actual PDF pp.4-5, cited "p.3-4" — close, one page short); no-hedge FX policy quote (actual PDF p.14, cited p.14 — EXACT MATCH) | One exact match, two off-by-one |
| ANTHEM May-26 | Funding recovery (+50% YoY), "destocking behind us", Unit-IV timeline, tariff dismissal, ADC/peptide detail | YES — funding recovery quote (actual PDF p.17, cited p.17 — EXACT); FY26 18% CRDMO growth / record Q4 (actual PDF p.3, cited p.3 — EXACT); peptide TAM quote (actual PDF p.9, cited p.9 — EXACT); ADC "15-20 payloads" (actual PDF p.8, cited p.7 — off by one); "mostly it's behind us" destocking quote (actual PDF p.4, cited p.7 in Part 2A — off by THREE pages); "No tariffs is not a problem" (actual PDF p.13, cited p.12 — off by one) | Several exact matches; one material (3-page) drift |
| ANTHEM Jul-26 | Q1 FY27 softness (analyst -25% YoY), utilization data, AI commentary, unnamed-peer questions | YES — Mehul Sheth -25% YoY exchange (actual PDF p.8, cited p.8 — EXACT); Bansi Desai unnamed-peer semaglutide question (actual PDF p.10, cited p.10 — EXACT); Unit-3 utilization 30-35% vs 15% prior (confirmed, present); "moment hype" AI quote (actual PDF p.15, cited p.14 — off by one) | Mostly exact, one off-by-one |
| SAILIFE Aug-26 | CRO +26% YoY, diversification tailwind, new-modality mix, capacity dates | YES — CRO +26% YoY appears twice (actual PDF pp.4 and 6; B06's bundled anchor "p.2, p.6" matches only the p.6 instance, the p.2 reference does not correspond to either occurrence — actual first occurrence is p.4, not p.2); geopolitical-diversification / "18 IPOs" quote (actual PDF p.4, cited "p.2"/"p.2-3" — off by one to two); returning-customers >90% (actual PDF p.7, cited p.6 — off by one); peptide facility "operational in 2028" (actual PDF p.4, cited p.4 — EXACT); Bidar blocks (actual PDF p.12, cited p.11 — off by one); "4% to 5% of our revenues from new modalities" (actual PDF p.15, cited p.15 for location — EXACT location, but MISATTRIBUTED, see Finding D-1 below) | One exact page match, several off-by-one/two, one misattribution |
| PPLPHARMA Jul-26 | CDMO +19% YoY, tariff/near-shoring pushback, ADC capacity, tax-loss disclosure | YES — CDMO +19% YoY / funding recovery / pricing discipline (actual PDF p.3, cited p.2 — off by one); Riverview inauguration + "small percentage share...rapidly growing market" (actual PDF pp.3 and 18, cited p.3 and p.18 — EXACT on both); NPS "in the 60 range" (actual PDF p.10, cited "p.10-11" — matches); "Not really" on near-shoring (actual PDF p.15, cited "p.14-15" — matches); Lexington CY2027, speaker Vivek Valsaraj (actual PDF p.12, cited p.13 — off by one, speaker attribution correct); overseas carry-forward tax losses (actual PDF p.19, cited "p.18-19" — matches) | Mostly correct or matching range, two off-by-one |

**Coverage verdict:** all six peers were genuinely, substantively used — every claimed contribution corresponds to real material in the correct transcript. No peer earns a `substantive_unsupported` flag under the letter of rule 2 (a real, findable citation exists for every claim tested). But roughly half the individual page anchors tested (13 of ~24 checked) are off by one to three pages from the actual PDF-page-marker location, and one citation is misattributed to the wrong speaker.

---

## PART 2: FINDINGS

**D-1 (MAJOR) — Misattributed quote, load-bearing to an analytical point.** B06 (Part 1, Claim 1 "Peers silent" row) writes: "SAILIFE quantifies new-modality work at only '4% to 5% of our revenues' today (Siva Chittor, SAILIFE-Aug-2026, p.15)" and uses this as "a caution against reading 'growing fast' as 'already large'" — a load-bearing qualifier in the claim's net read. Checked against the transcript (SAILIFE-Concall_Aug_2026_Transcript.txt, PDF p.15, line 639): the "4% to 5%" figure appears ONLY inside analyst Yasser Lakdawala's question ("I think when we say that we have got about between 4% to 5% of our revenues from new modalities..."), not in any statement by Siva Chittor. Siva Chittor's reply ("We are not doing it on the commercial side, but we are doing on all the development and the discovery side") answers the analyst's follow-up but never restates or confirms the percentage. A full-text search of the transcript for "4% to 5%" / "4-5%" / "new modalit*" finds no other instance. B06 presents an analyst-sourced, unconfirmed figure as a management-quantified data point — this overstates the evidentiary tier of a number used to qualify a VERIFIED-adjacent claim.

**D-2 (MAJOR) — Citation to a page/call that does not contain the cited claim.** B06 Part 2B cites: "Anthem instead reports margin expansion from backward integration (eliminating a China-sourced intermediate)... (Gawir Baig, ANTHEM-Nov-2025, p.6; ANTHEM-Feb-2026, p.3-4)". The specific "China-sourced intermediate eliminated via backward integration" story is told in ANTHEM-Concall_Feb_2026_Transcript.txt at PDF pp.4-5 (lines 176-183: "we had mentioned that for one of the customer products, a lot of intermediates were being outsourced, and hence China procurement had gone up... we have completely discontinued China supplies because now we manufacture the intermediate in-house") — so the Feb-2026 half of the citation is real, just one page short of the cited range. But ANTHEM-Concall_Nov_2025_Transcript.txt contains no China-sourced-intermediate discussion anywhere (the only "backward integrated" mention in that transcript, at PDF p.15/line 596, is about GLP-1/fermentation, an unrelated topic). The Nov-2025, p.6 half of this citation appears to be a spurious source attribution, not merely an off-by-one drift.

**D-3 (MAJOR, systemic) — Recurring 1-3 page anchor drift across roughly half of tested citations.** Beyond D-1/D-2, of ~24 page anchors spot-checked against the PDFs' own "===== PAGE n =====" markers (the anchor unit B00 mandates — "carry the PDF page number, not the printed folio... Anchor to the PDF filename and page"), 13 are off by one to three pages from the true marker location (see Part 1 table for the full list: e.g., Rs25.4cr Labour Code item cited p.2/actual p.3; "build it and they will come" repeat cited p.10-11/actual p.12; ADC "15-20 payloads" cited p.7/actual p.8; "mostly it's behind us" cited p.7/actual p.4 — a 3-page miss; CDMO +19% YoY cited p.2/actual p.3; Bidar blocks cited p.11/actual p.12; Lexington CY2027 cited p.13/actual p.12). Roughly the same number of citations land exactly on the correct marker (funding-recovery +50% quote, FY26 18% CRDMO growth, peptide-TAM quote, no-hedge FX quote, Mehul Sheth -25% YoY, semaglutide scaling question, NPS "60 range", near-shoring "not really", Riverview quotes, tax-loss disclosure). The drift is not confined to one call or one direction consistently (some ANTHEM May-26 folios drift by the covering-letter offset of 1, one drifts by 3), so it reads as inconsistent anchoring discipline rather than a single systematic off-by-one rule that could be mechanically corrected. Every drifted citation's underlying quote IS genuinely present in the correct document, one to three pages from where cited — this is an anchor-precision defect, not a fabrication, but it materially raises the cost of an operator spot-check against roughly half the citations in this stage's most citation-dense report.

No CRITICAL findings: no claim's verdict is invented from silence, no VERIFIED claim rests on fewer than two peers, and no cited quote is entirely absent from its named transcript.

---

## PART 3: VERDICT-DISCIPLINE AUDIT

Only one claim carries a VERIFIED verdict: "Biotech VC funding recovery is real and converts into discovery/CRO revenue growth..." — peers ANTHEM + SAILIFE, anchor_count 3. Two independent peers satisfy the ">=2 independent peer anchors" rule; both anchors were independently located and confirmed real in Part 1 (ANTHEM p.17 funding-recovery quote; SAILIFE p.2-3 CRO growth/IPO commentary, with the SAILIFE anchor itself carrying the page-drift issue noted in D-3 but the underlying quotes still genuinely present). No verdict is upgraded from silence: the CONTRADICTED verdict (Claim 2) is built on affirmative peer statements (SAILIFE CRO +26%, >90% repeat revenue; ANTHEM's absence of any comparable pressure is explicitly flagged by B06 itself as the weaker "by omission" half of that verdict, not treated as equal-weight evidence). The three PARTIALLY VERIFIED claims are each built on genuinely mixed peer evidence, not silence dressed as partial support.

**Verdict discipline: no fails.**

---

## PART 4: CLAIM COMPLETENESS CHECK

B05's peer_questions list carries 5 items (advanced-modality mix, discovery pricing/commoditization, tariff/Biosecure demand, VC-funding recovery, capacity gestation timeline). B06 Part 1 addresses exactly these 5, in the same order, each with a verdict. No skipped claim.

**Claims all addressed: true.**

---

## PART 5: UNUSED-BUT-RELEVANT CHECK

A full-text scan of all six transcripts for "Syngene", "Biocon", "pricing pressure", "price competition", "lower-cost"/"lower cost", "attrition", "competitive pricing", and "discount" returned zero matches across the corpus. This corroborates B06's own `peer_mentions_of_company: []` and its finding that no peer volunteers discovery/CRO pricing pressure — there is no unused material contradicting B06's read on this point. No additional directly claim-relevant peer statement was found sitting unused in the six transcripts beyond what B06 already cites (e.g., Sai Life's Boston-team discovery-revenue CAGR discussion, lines 628-630, is tangential context, not a fifth data point the claim list requires).

**Unused but relevant: none identified.**

---

## SUMMARY

B06 genuinely read and substantively used all six peer transcripts; no peer coverage is fabricated or invented, no verdict rests on silence or a single peer where two are required, and all five B05 peer_questions received a verdict. The audit's material findings are citation-precision defects: one misattributed quote presented as management-confirmed when it is analyst-paraphrased (D-1), one citation half that points to a transcript section that does not contain the claimed material (D-2), and a broader pattern of one-to-three-page anchor drift across roughly half the citations tested (D-3). None of these change the direction of any of B06's five verdicts — the underlying substantive claims (peer growth vs. Syngene's attrition, verified funding recovery, mixed tariff/modality/capacity evidence) all hold up against the source transcripts independent of the anchor-page errors. Recommend the maker re-verify and correct all cited page numbers against the PDF page markers (not printed folios) before this report is relied on for an operator spot-check, and correct or drop the Siva Chittor attribution on the 4-5% new-modality figure.

```yaml
stage: B12d
company: "SYNGENE"
run_date: "2026-09-15"
model: claude-sonnet-5
status: complete
peers_audited: 6
substantive_confirmed: 6
substantive_unsupported: []
unused_but_relevant: []
claims_all_addressed: true
verdict_discipline_fails: []
findings:
  - {severity: "MAJOR", location: "06-peers.md Part 1, Claim 1 'Peers silent' row", claimed: "SAILIFE quantifies new-modality work at '4% to 5% of our revenues' (Siva Chittor, SAILIFE-Aug-2026, p.15)", source_truth: "Figure appears only in analyst Yasser Lakdawala's question (SAILIFE-Concall_Aug_2026_Transcript.txt PDF p.15, line 639); Siva Chittor's reply does not restate or confirm the number", note: "Misattributed to management; overstates evidentiary tier of a figure used to qualify a claim's net read"}
  - {severity: "MAJOR", location: "06-peers.md Part 2B (Pricing and input costs)", claimed: "Backward-integration/China-sourced-intermediate margin story cited to ANTHEM-Nov-2025, p.6 and ANTHEM-Feb-2026, p.3-4", source_truth: "China-intermediate story is in ANTHEM-Concall_Feb_2026_Transcript.txt PDF pp.4-5 (one page beyond cited range); no China-intermediate discussion exists anywhere in ANTHEM-Concall_Nov_2025_Transcript.txt", note: "Nov-2025 p.6 half of the citation is spurious, not merely off-by-one"}
  - {severity: "MAJOR", location: "06-peers.md Parts 1-2, ~13 of ~24 spot-checked citations", claimed: "Various page anchors across ANTHEM (all 4 calls), SAILIFE, and PPLPHARMA citations", source_truth: "True PDF-page-marker location is 1-3 pages from the cited page in roughly half of citations checked (examples: Rs25.4cr exceptional item cited p.2/actual p.3; ADC '15-20 payloads' cited p.7/actual p.8; destocking 'behind us' cited p.7/actual p.4; CDMO +19% YoY cited p.2/actual p.3; Lexington CY2027 cited p.13/actual p.12)", note: "Systemic anchor-precision defect, not fabrication; every underlying quote is genuinely present in the correct document"}
critical_count: 0
major_count: 3
minor_count: 0
acceptance_rate: 100
```
