# Verifier D: Peer Coverage Audit — BIRLACABLE (2026-08-20)

Scope: 12 peer transcripts (HFCL x4, PARACABLES x4, STLTECH x4) against B06-peers.md and
B06-peers.yaml. Checked whether every peer marked SUBSTANTIVE has real, findable citations,
whether the coverage map's classification is honest, whether the peer_questions list was fully
addressed, and whether verdict discipline (>=2 independent anchors for VERIFIED claims) holds.

## Method

Spot-checked ~28 quoted anchors across all 12 transcripts (at least 2 per transcript, weighted
toward the claims with the largest downstream weight: Claim 1 OFC revival, Claim 3 copper/LAN
contradiction, Claim 4 export pricing, and the Part 2E risk list). Quotes were located by
grep against the raw extracted transcript text and checked against B06's cited page number
where a page number was given. Quarter-confirmation table cross-checked on one file
(HFCL Oct 2025 cover letter) as a sanity check.

## Coverage audit per peer

| Peer / quarter | Usage claimed | Citation located in transcript | Verdict |
|---|---|---|---|
| HFCL Q2 FY26 (Oct 2025) | SUBSTANTIVE | "strong revival... hyperscalers and data center operators" (p.3, exact) confirmed; West Bengal BharatNet circle quote (p.5, exact) confirmed; Punjab/BSNL "no complaints" quote located but on printed p.17, B06 cites p.18 | Confirmed, MINOR page-anchor slip |
| HFCL Q3 FY26 (Feb 2026) | SUBSTANTIVE | INR964->INR1,055/fkm realization quote confirmed verbatim; 100,000-router order + INR700-800cr quote confirmed verbatim | Confirmed |
| HFCL Q4 FY26 (May 2026) | SUBSTANTIVE | EBITDA margin 4.93%->23.25%/18.47% figures confirmed verbatim; "BharatNet kind of EPC project, where there is profitability" quote confirmed verbatim, BUT the preceding "warranty period" loss the quote is spliced onto is explicitly the Army's NFS network in the transcript, not BharatNet | Confirmed as quote; MAJOR misreading of what the quote supports (see findings) |
| HFCL Q1 FY27 (Jul 2026) | SUBSTANTIVE | $18-28/fkm realization range confirmed verbatim; 35% Chinese-fiber duty quote confirmed; EBITDA margin 4.93%->23.25% (Q1 FY26 to Q1 FY27, restated) confirmed; "INR13,100 crore order intake, 1.7x prior FY booking" quote NOT found anywhere in this transcript — located instead verbatim in STLTECH Jul 2026 | Confirmed except one fabricated attribution — CRITICAL/MAJOR (see findings) |
| PARACABLES Q2 FY25 (Nov 2024) | SUBSTANTIVE | "peers... approximately 65 days" question and "market leaders... channel financing" answer confirmed verbatim | Confirmed |
| PARACABLES Q3 FY25 (Feb 2025) | SUBSTANTIVE | "very lax... not particularly competitive" OFC quote confirmed verbatim, p.16 matches | Confirmed |
| PARACABLES Q4 FY25 (May 2025) | SUBSTANTIVE | 155->101 working-capital-day and 86->47 debtor-day figures confirmed verbatim, p.3 | Confirmed |
| PARACABLES Q4 FY26 (May 2026) | SUBSTANTIVE | 10%->25%->50% tariff progression and Supreme Court/IEEPA relief quote confirmed verbatim; Narmadapuram INR300cr spend / INR1,200cr FY29 revenue target confirmed verbatim | Confirmed |
| STLTECH Q2 FY26 (Nov 2025) | SUBSTANTIVE | "US market continues to be strong and quite robust" confirmed; $96.5m US litigation exchange confirmed; copper-to-fiber "emerging trend" quote confirmed verbatim but on printed p.15, B06 cites p.13-14 | Confirmed, MINOR page-anchor slip |
| STLTECH Q3 FY26 (Jan 2026) | SUBSTANTIVE | CRU "4% year-on-year" 2025 upgrade quote confirmed verbatim; Invenia J&K BharatNet package quote confirmed verbatim; North America 25%->36% confirmed | Confirmed |
| STLTECH Q4 FY26 (May 2026) | SUBSTANTIVE | Copper segment "moderated to 19%... higher LME prices" quote confirmed verbatim on printed p.8 (matches B06's p.8 citation exactly); CRU 6.8% 2026 upgrade + "not a cyclical uptick" quote confirmed verbatim | Confirmed, this is the single most consequential citation in the report and it is clean |
| STLTECH Q1 FY27 (Jul 2026) | SUBSTANTIVE | Order book INR18,618cr / 2.4x confirmed verbatim; PAT margin 10% / 3.5x confirmed verbatim; separately, this file is also the true source of the INR13,100cr / 1.7x order-intake figure misattributed to HFCL above | Confirmed, and this file is more heavily used than the coverage map implies once the misattributed line is corrected |

12 of 12 peer-quarter entries have a real, findable primary citation. All are genuinely
SUBSTANTIVE — no CITED-ONLY or UNUSED reclassification is warranted. The "all 12 contributed
materially" claim in Part 3 is honest.

## Findings

1. **Misattributed data point (HFCL Q1 FY27 entry).** B06 Claim 1 states: "HFCL, Q1 FY27 call
   (Jul 22, 2026): ... Q1 order intake INR13,100 crore, 1.7x the whole of the prior fiscal
   year's booking, anchored by a $1.1bn multiyear hyperscaler deal." This sentence does not
   exist in the HFCL Jul 2026 transcript (grepped for "13,100," "1.7x," "intake," "booking" —
   zero matches). It is a near-verbatim match for STL Technologies' own Jul 2026 transcript:
   "we secured orders worth INR13,100 crores, which is 1.7x the total order wins of INR7,687
   crores... anchored by a landmark multiyear $1.1 billion deal with a global hyperscaler."
   HFCL's Jul 2026 call does separately report a real INR26,665cr all-time-high order book and
   its own $1.1bn hyperscaler order (line ~834, "the INR1.1 billion order that we got from a
   hyperscaler"), so the two companies' hyperscaler deals are genuinely parallel facts — but the
   specific quarterly-intake figure and its "1.7x" multiple belong to STL, not HFCL, and B06
   presents it as an HFCL number. This is a real cross-company data contamination inside a
   SUBSTANTIVE citation, not a paraphrase error.
2. **Conflated causal mechanic (HFCL Q4 FY26 entry, feeds Part 2E and analyst_note).** B06
   reads the HFCL Q4 FY26 quote "we have started executing BharatNet kind of EPC project, where
   there is profitability" as evidence that "BharatNet-linked EPC work ran at a loss through a
   'warranty period' before AMC conversion brought profitability." In the transcript, the
   warranty-period loss is explicitly attributed to a different customer/project — the Army's
   NFS network ("EPC business loss was majorly due to this Army's network which we constructed,
   and it was undergoing warranty period... Now, AMC contract is shortly to be signed with
   Army... Moreover, now we have started executing BharatNet kind of EPC project, where there is
   profitability"). The BharatNet EPC line is described as profitable from the outset, not as
   the loss-making leg going through a warranty-to-AMC transition. B06's "EPC/government-contract
   execution lag" risk item in Part 2E and its repetition in the analyst_note ("template risk for
   BCL's own BharatNet exposure") therefore rest on an HFCL mechanic that is not actually about
   BharatNet. This is a material misreading that could mislead stage-13 synthesis into treating a
   generic government-EPC warranty pattern (Army NFS) as a BharatNet-specific precedent.
3. **Page-anchor imprecision, HFCL Q2 FY26 Punjab/BSNL quote.** B06 cites "p.18"; the quote
   ("we are doing Punjab execution for BharatNet... BSNL has acknowledged to me personally that
   they have no complaints") sits under the transcript's own "Page 17 of 21" header. Quote
   content is accurate; page number is off by one.
4. **Page-anchor imprecision, STL Q2 FY26 copper-to-fiber quote.** B06 cites "p.13-14"; the
   quote ("there is also an emerging trend of some of the copper that is required within data
   centers is moving to fiber") sits under the transcript's own "Page 15 of 18" header. Quote
   content is accurate; page number is off by roughly two.
5. **Verdict discipline holds.** Both VERIFIED claims (Claim 1, Claim 4) rest on >=2
   independent peers with real, checkable anchors (HFCL + STL in both cases); no VERIFIED claim
   rests on a single peer. No verdict is upgraded from silence — CONTRADICTED (Claim 3) and
   PARTIALLY VERIFIED (Claims 2, 5) verdicts are conservatively drawn and the "unverifiable"
   items (BharatNet disbursement pace, 47% concentration comparability) are correctly left
   unresolved rather than forced to a verdict.
6. **peer_questions coverage is complete.** All 5 questions in B05.peer_questions map 1:1 to
   B06 Part 1 Claims 1-5 and each received a verdict (VERIFIED / PARTIALLY VERIFIED /
   CONTRADICTED). No skipped claim.
7. **Quarter-confirmation table spot check clean.** HFCL Oct 2025 cover letter confirms Q2
   FY26 / call referenced Oct 17, 2025, matching B06's table exactly.
8. **No unused-but-relevant material found on spot read.** Checked HFCL's OFC capacity
   expansion (42.36 million fkm, used in Part 2C) and STL's QIP/US-capex figures (used in Part
   2C) — both correctly captured. No peer statement bearing materially on BCL's five claims was
   found unused in the sampled passages; this is a sampled check, not an exhaustive one, given
   report scope constraints.

## Verdict-discipline audit per claim

| Claim | Verdict | Independent peer anchors | Discipline check |
|---|---|---|---|
| 1 — OFC demand/pricing revival | VERIFIED | HFCL (4 calls) + STL (4 calls), >=2 | PASS |
| 2 — BharatNet order inflow | PARTIALLY VERIFIED | HFCL, STL, Paramount | PASS (not over-claimed to VERIFIED) |
| 3 — Copper/LAN growth engine | CONTRADICTED | STL only (HFCL silent) | Single-peer contradiction; correctly not force-fit to a >=2-peer VERIFIED-style claim, but the load-bearing contradiction rests on one peer's data — worth naming as a dependency, not a verdict-discipline violation since the rule as written governs VERIFIED, not CONTRADICTED |
| 4 — Export/NA record pricing | VERIFIED | HFCL + STL, >=2 | PASS |
| 5 — Operating cycle/concentration | PARTIALLY VERIFIED | HFCL, Paramount | PASS (47% concentration correctly left unverifiable) |

## Peer utilisation

12 of 12 provided peers/quarters were used substantively with real, locatable citations
(peer_utilisation = 100%, before adjusting for the two anchor-quality findings above, which
affect anchor precision, not usage classification).

```yaml
stage: B12d
company: "BIRLACABLE"
run_date: "2026-08-20"
model: claude-sonnet-5
status: complete
peers_audited: 12
substantive_confirmed: 12
substantive_unsupported: []
unused_but_relevant: []
claims_all_addressed: true
verdict_discipline_fails: []
findings:
  - {severity: "MAJOR", location: "06-peers.md Part 1 Claim 1, HFCL Q1 FY27 evidence bullet + B06-peers.yaml peer_coverage_map HFCL Q1 FY27", description: "Quote 'Q1 order intake INR13,100 crore, 1.7x the whole of the prior fiscal year's booking' is attributed to HFCL's Jul 2026 call but does not appear in that transcript; it is verbatim from STL Technologies' Jul 2026 transcript ('we secured orders worth INR13,100 crores, which is 1.7x the total order wins of INR7,687 crores... anchored by a landmark multiyear $1.1 billion deal'). Cross-company data contamination inside a SUBSTANTIVE citation."}
  - {severity: "MAJOR", location: "06-peers.md Part 1 Claim 2 + Part 2E risks_peers_raise + analyst_note", description: "The HFCL Q4 FY26 'warranty period' EPC-loss-to-AMC-profit mechanic is attributed to BharatNet, but the transcript states the loss was 'majorly due to this Army's network' (NFS), a different government contract; the BharatNet EPC line quoted immediately after is described as already profitable. B06's Part 2E risk item and analyst_note both carry this mislabeled mechanic forward as a 'template risk for BCL's own BharatNet exposure.'"}
  - {severity: "MINOR", location: "06-peers.md Part 1 Claim 2, HFCL Q2 FY26 Punjab/BSNL quote", description: "Cited as p.18; quote sits under the transcript's own 'Page 17 of 21' header. Quote text itself is accurate."}
  - {severity: "MINOR", location: "06-peers.md Part 1 Claim 3, STL Q2 FY26 copper-to-fiber quote", description: "Cited as p.13-14; quote sits under the transcript's own 'Page 15 of 18' header. Quote text itself is accurate."}
critical_count: 0
major_count: 2
minor_count: 2
acceptance_rate: 83   # 10 of 12 peers correctly and cleanly handled (no finding attached); 2 carry a MAJOR finding each
peer_utilisation: 100   # % of the 12 provided peer-quarters used substantively (real, locatable citation for each)
```
