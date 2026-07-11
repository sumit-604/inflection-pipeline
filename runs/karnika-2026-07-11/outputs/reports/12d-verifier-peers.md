# Verifier D: Peer Coverage Audit — Karnika Industries Ltd (KARNIKA)
Run date: 2026-07-11 | Model: claude-sonnet-5 | Stage: B12d
Fresh-context audit of Stage 6 (B06-peers) against the 12 raw peer transcripts and the B05 peer_questions list. No other verifier output consulted.

## Scope and method
Read all 12 peer transcripts directly. Given budget, achieved deep page-level verification on 10 of 12 (all 4 SPAL calls, all 4 MonteCarlo calls, 3 of 4 Cantabil calls — Cantabil Q2 FY26/Nov-2025 and SPAL Q2 FY26/Nov-2025 were not independently re-read in this pass; their B06 coverage-map entries are noted as unverified-by-me below, not disputed). For every SUBSTANTIVE citation checked, I located the actual page in the source PDF (using the PDF's own printed page-footer numbering, e.g. "Page 5 of 19") and compared it against the page B06 cited.

## PART 1: Coverage audit table (peer x quarter)

| Peer | Quarter | B06 usage | My check | Result |
|---|---|---|---|---|
| CANTABIL | Q1 FY26 (Aug 6 2025) | SUBSTANTIVE | Read in full | Confirmed. "we did not notice any change in the raw material prices as such... we did not see any change in the price as much in the quarter for last many months" (Shivendra Nigam) — verbatim, correctly located. |
| CANTABIL | Q2 FY26/H1 (Nov 4 2025) | SUBSTANTIVE | Not re-read this pass | Unverified by me — not disputed, flagged as an audit gap. |
| CANTABIL | Q3 FY26/9M (Feb 6 2026) | SUBSTANTIVE | Read in full | Content confirmed, page anchor wrong (see Finding 2). |
| CANTABIL | Q4/FY26 (May 19 2026) | SUBSTANTIVE | Read in full | Content partly confirmed, one fabricated figure and two anchor errors (see Findings 1, 2, 3). |
| MONTECARLO | Q1 FY26 (Aug 7 2025) | SUBSTANTIVE | Read in full | Confirmed. "cotton is 50% of our business" (Viraj Parekh, analyst — not management, see note under Finding 4) is accurately reflected. |
| MONTECARLO | Q2 FY26/H1 (Nov 13 2025) | SUBSTANTIVE | Read in full | Content confirmed, page anchor wrong (see Finding 2). |
| MONTECARLO | Q3 FY26/9M (Jan 29 2026) | CITED-ONLY | Read pages 1-5 of 17 | Classification reasonable on what I read — routine labour-code/inventory/guidance Q&A, no decisive new evidence found or missed. |
| MONTECARLO | Q4/FY26 (May 19 2026) | SUBSTANTIVE | Read in full (16 pages) | Content confirmed, one anchor cites a page that does not exist in the source (see Finding 3). |
| SPAL | Q1 FY26 (Aug 18 2025) | SUBSTANTIVE | Read in full | Confirmed. Babywear moat quote (p.3), tariff cost-sharing "one fourth" (p.6-7), Tamil Nadu wage hike (p.7) — all verbatim, all correctly page-anchored. |
| SPAL | Q2 FY26/H1 (Nov 17 2025) | SUBSTANTIVE | Not re-read this pass | Unverified by me — not disputed, flagged as an audit gap. |
| SPAL | Q3 FY26/9M (Feb 13 2026) | SUBSTANTIVE | Read in full | Confirmed. "Q3 was soft for the sector" (p.2), US-tariff-pause-easing narrative (p.2-3) — verbatim, correctly anchored. |
| SPAL | Q4/FY26 (May 22 2026) | SUBSTANTIVE | Read in full | Confirmed. Cotton price INR75,000→70,000 + yarn +5% (p.10), Strait of Hormuz (p.2), standalone EBITDA margin 16.5%/16.7% and consolidated 13.8%/13.5% (p.5), Bangladesh EU-LDC 2029 (p.10) — all verbatim, all correctly page-anchored. |

**Pattern observed:** every SPAL citation I checked was both content-accurate and page-accurate. Every CANTABIL and MONTECARLO citation I checked was content-accurate, but four of them cited the wrong page (off by 1-5 pages), and one cited a page number that does not exist in the source document at all.

## PART 2: Findings

### Finding 1 — MAJOR — fabricated/misattributed figure under CANTABIL's name
**Location:** 06-peers.md, Claim 7 / Part 2A; B06-peers.yaml `contradicted[1]`. Anchor claimed: "CANTABIL, Q3 FY26 call Feb 6 2026 p.10... Q4 FY26 revenue +36% YoY (May 19, 2026 call, p.3)".
B06 states Cantabil's Q4 FY26 revenue grew "+36% YoY," sourced to Cantabil's own May 19, 2026 call. Cantabil's actual May 2026 transcript (page footer "Page 3 of 19"): "Revenue from operations for Q4 FY26 grew by 15% to INR253.5 crores as compared to INR219.8 crores in Q4 FY25." No 36% figure appears anywhere in Cantabil's Q4/FY26 disclosure for this metric. The 36% figure is Monte Carlo's own Q4 FY26 revenue growth: "the company reported revenue of around INR280 crores, reflecting a strong year-on-year growth of 36%" (Sandeep Jain, MonteCarlo May 19, 2026 call, footer "Page 2 of 16"). This looks like a peer data mix-up: Monte Carlo's number was attributed to Cantabil. It does not exist in Cantabil's transcript at any page. Under Verifier D rule 2, a SUBSTANTIVE claim without a real, findable citation in that peer's own transcript is MAJOR. The underlying Claim 7 verdict (CONTRADICTED — demand/discounting resilient, not weak) still stands on other genuine evidence (Cantabil's real SSG 6.3% and GST-momentum quote, Monte Carlo's real discount-percentage data), so the verdict itself is not overturned, but this specific number should be struck and corrected — it currently misstates Cantabil's own Q4 growth by more than 2x.

### Finding 2 — MINOR (pattern, 3 instances) — page-anchor drift on otherwise-accurate CANTABIL/MONTECARLO citations
Quotes are verbatim and correctly attributed to the right speaker and call in every case; only the printed page number cited is wrong:
- CANTABIL Q4/FY26 CFO quote "some input material has seen some hike" (Claim 2): B06 cites p.10; actual location is p.5 (footer "Page 5 of 19", Tarun Sharma Q&A).
- CANTABIL Q4/FY26 gross-margin data "60.4% FY26 vs 56.2% FY24" (Claim 6): B06 bundles this under "p.3" alongside the EBITDA-margin figure; the gross-margin figure is actually on p.9 (footer "Page 9 of 19", Swapnil Gupta Q&A). The EBITDA-margin figure (31% vs 28.4%) is correctly on p.3.
- CANTABIL Q3 FY26 GST-momentum quote "the momentum is definitely there... it looks like long term" (Claim 7, Part 2A): B06 cites p.10; actual location is p.6 (footer "Page 6 of 20", Harshit Q&A).
- MONTECARLO Q2 FY26 "we dropped that idea... margin accretion is only 3% to 4%" (Claim 3): B06 cites p.10; actual location is p.9 (footer "Page 9 of 13", Raman KV Q&A).
None of these change the substance of the claims — the data is real and correctly used — but the anchors as written would not resolve on a page-by-page check, which is a real (if minor) verification-quality gap.

### Finding 3 — MAJOR — cited page does not exist in the source document
**Location:** 06-peers.md, Claim 5. Anchor claimed: "Monte Carlo, Q4 FY26 call (May 19, 2026, p.18-19)".
Monte Carlo's May 19, 2026 transcript is 16 pages long in total (final page footer reads "Page 16 of 16"). Pages 18-19 do not exist in this document. The quote B06 attributes to this location — Sandeep Jain framing Zara and Shein as long-standing competitors ("Zara is here in last, I think, 10, 12 years, they came in around 2009 and Shein came in around 2014, '15. So we have been competing with them") — is real and accurately characterized, but it is actually on page 14 (footer "Page 14 of 16"). An anchor pointing to a page range outside the document's actual length is functionally unfindable and should be graded the same as "ANCHOR NOT FOUND" even though the content itself checks out on manual search. This is the most serious of the anchor errors found because it is not just imprecise, it is impossible.

### Finding 4 — MINOR — attribution nuance on the "cotton = 50%" baseline
**Location:** B06-peers.yaml peer_coverage_map, MONTECARLO Q1 FY26 row: "Cotton 50% of business baseline, no cost complaint at year start."
The "cotton is 50% of our business" figure in the Aug 7, 2025 call is stated by the analyst (Viraj Parekh) as a premise within his question, not independently disclosed by Monte Carlo management (management does not contest or restate it, but also does not originate it). This is a minor sourcing nuance, not a fabrication — the figure is on the record either way — but B06's characterization implies it is a company disclosure when it is technically an analyst-stated fact left unchallenged by management.

### Finding 5 — no issues found — verdict discipline
Checked the ≥2-independent-peer-anchor rule (rule 4) against all VERIFIED/PARTIALLY VERIFIED/CONTRADICTED claims:
- Claim 2 (VERIFIED, cotton/yarn shock): 4 anchors across 3 peers (SPAL, MonteCarlo, Cantabil) — passes.
- Claim 6 (CONTRADICTED, sector margins expanded): 3 independently-anchored peer EBITDA-margin figures, all confirmed accurate on their own pages — passes.
- Claim 7 (CONTRADICTED, demand resilient): nominally 2 peers (Cantabil, MonteCarlo). After removing the flawed 36% figure (Finding 1), Cantabil still contributes 2 genuine anchors (SSG 6.3%, GST-momentum quote), so the claim retains ≥2 independent peer anchors and the verdict survives — but the specific unsupported number inside it should be corrected.
No claim was found upgraded from silence (rule 4's CRITICAL trigger) — the three UNVERIFIABLE claims (1, 4, 5) are correctly left unresolved rather than pushed toward a verdict the peer set cannot support.

### Finding 6 — no issues found — claim coverage
All 5 claims from B05's `peer_questions` list (kids-apparel TAM/CAGR, cotton/yarn shock, "no true integrated peer," Kidcity footprint, Zara/H&M/DMart negotiations) received an explicit verdict in B06 Part 1 (Claims 1-5). B06 additionally raised two unprompted claims (6, 7) from its own cross-read, which is permitted and disclosed as such, not substituted for the assigned list. `claims_all_addressed: true`.

### Finding 7 — no issues found — UNUSED classification and peer_mentions_of_company
No peer transcript I read mentions Karnika, Kidcity, HopScotch, or Spencer's by name — consistent with B06's `peer_mentions_of_company: []`. I found no peer-quarter that should have been marked UNUSED (all 12 contribute at least a genuine timeline or cost-shock data point), and no claim-relevant peer statement left completely unused in the material I checked (e.g. SPAL's Tamil Nadu wage-hike and tariff cost-sharing detail, Bangladesh EU-LDC detail, and Monte Carlo's discount/return data are all captured in B06 Part 2E).

## PART 3: peer_utilisation

Treating each of the 12 peer-quarter transcripts as the unit (matching B06's own peer_coverage_map granularity): 11 SUBSTANTIVE + 1 CITED-ONLY + 0 UNUSED.

**peer_utilisation = 11/12 = 91.7%** (peers used substantively ÷ peers provided, B06's own classification, which I found largely supportable on independent read).

Of the 11 SUBSTANTIVE entries, 2 peer-quarters carry a MAJOR anchor/attribution problem (CANTABIL Q4/FY26 — fabricated 36% figure; MONTECARLO Q4/FY26 — nonexistent page anchor) and 2 more carry MINOR anchor-only drift (CANTABIL Q3 FY26; MONTECARLO Q2 FY26), all four of which were nonetheless genuinely and substantively used in the underlying analysis. **Peer-quarters correctly handled (no MAJOR issue): 10/12 = 83.3%.**

## Overall assessment
B06 read all 12 provided transcripts and used the content in them honestly and substantively — no evidence of fabricated quotes, invented peer statements, or claims stretched beyond what a peer actually said. The single most consequential problem is Finding 1: a real number (Monte Carlo's 36% Q4 revenue growth) was attributed to the wrong company (Cantabil), inflating the apparent strength of Cantabil's specific Q4 data point inside an already-correct CONTRADICTED verdict. Finding 3 (a citation to a nonexistent page range) is a citation-hygiene failure serious enough to be MAJOR on its own terms even though the underlying quote, once located, checks out. The recurring MINOR page-drift pattern (Finding 2) affects only CANTABIL and MONTECARLO citations, not SPAL, and never changes the substance of a claim — but it means a spot-check reader following B06's stated page numbers would not find several of its quotes where claimed. None of these issues flip a verdict or invalidate the stage's central finding (Claim 6: peers held/expanded margins while Karnika's compressed sharply), which remains well-supported on independently-confirmed data.

```yaml
stage: B12d
company: "KARNIKA"
run_date: "2026-07-11"
model: claude-sonnet-5
status: complete
peers_audited: 12
substantive_confirmed: 9
substantive_unsupported:
  - "CANTABIL (Q4/FY26, May 19 2026 call): Claim 7 cites 'Q4 FY26 revenue +36% YoY' at p.3 of Cantabil's own call; Cantabil's transcript actually shows +15% YoY at that page. The 36% figure belongs to MONTECARLO's Q4 FY26 revenue growth, not Cantabil's — apparent peer data mix-up."
  - "MONTECARLO (Q4/FY26, May 19 2026 call): Claim 5 cites the Zara/Shein-as-competitors quote at 'p.18-19'; the transcript is only 16 pages long, so this page range does not exist. The quote is real and accurate but is actually on p.14."
unused_but_relevant: []
claims_all_addressed: true
verdict_discipline_fails: []
findings:
  - {severity: "MAJOR", location: "06-peers.md Claim 7 / B06-peers.yaml contradicted[1]; peer+quarter: CANTABIL Q4/FY26 (May 19 2026)", claimed: "Cantabil Q4 FY26 revenue +36% YoY, cited to Cantabil's own May 2026 call p.3", source_truth: "Cantabil's May 2026 call p.3 states Q4 FY26 revenue grew 15% YoY (INR253.5cr vs INR219.8cr); 36% is Monte Carlo's own Q4 FY26 revenue growth figure from the same call cycle", note: "Peer data mix-up; underlying CONTRADICTED verdict on Claim 7 survives on Cantabil's other genuine anchors (SSG 6.3%, GST quote) plus Monte Carlo's real discount data, but this specific figure should be struck/corrected"}
  - {severity: "MAJOR", location: "06-peers.md Claim 5; peer+quarter: MONTECARLO Q4/FY26 (May 19 2026)", claimed: "Zara/Shein competitor quote cited at p.18-19", source_truth: "Transcript is 16 pages total; quote is actually on p.14", note: "Cited page range does not exist in the source document; content itself is accurate once located, but the anchor as written is unfindable"}
  - {severity: "MINOR", location: "06-peers.md Claim 2; peer+quarter: CANTABIL Q4/FY26 (May 19 2026)", claimed: "CFO quote 'some input material has seen some hike' cited at p.10", source_truth: "Actual location p.5 (Tarun Sharma Q&A)", note: "Quote verbatim-accurate, page wrong"}
  - {severity: "MINOR", location: "06-peers.md Claim 6; peer+quarter: CANTABIL Q4/FY26 (May 19 2026)", claimed: "Gross margin 60.4% FY26 vs 56.2% FY24 bundled under p.3", source_truth: "Actual location p.9 (Swapnil Gupta Q&A); EBITDA margin figure at p.3 is correctly anchored", note: "Two distinct data points from different pages bundled under one citation"}
  - {severity: "MINOR", location: "06-peers.md Part 2A / Claim 7; peer+quarter: CANTABIL Q3 FY26 (Feb 6 2026)", claimed: "GST-momentum quote cited at p.10", source_truth: "Actual location p.6 (Harshit Q&A)", note: "Quote verbatim-accurate, page wrong"}
  - {severity: "MINOR", location: "06-peers.md Claim 3; peer+quarter: MONTECARLO Q2 FY26 (Nov 13 2025)", claimed: "'We dropped that idea' quote cited at p.10", source_truth: "Actual location p.9 (Raman KV Q&A)", note: "Quote verbatim-accurate, page wrong"}
critical_count: 0
major_count: 2
minor_count: 4
acceptance_rate: 83
```
