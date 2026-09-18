# Verifier D: Peer Coverage Audit — TruAlt Bioenergy (TRUALT)
Run date: 2026-09-18. Inputs: 12 peer transcripts (GULPOLY x4, BALRAMCHIN x4,
TRIVENI x4) in inputs/peer-concalls/; B06 peer verification report
(outputs/reports/06-peers.md); B05 peer_questions list
(outputs/blocks/B05-concall.yaml). Question: did the pipeline actually USE
the peers it claims it used?

Method: for every peer-quarter marked SUBSTANTIVE in B06's Part 3 coverage
map, I located the exact quote B06 cites, confirmed it exists verbatim in
the named transcript, and checked its stated page anchor against the
transcript's own `[page N]` markers. For the two CITED-ONLY rows I spot-read
the full transcript for claim-relevant material B06 did not use. I then
audited verdict discipline (independent-anchor count per VERIFIED claim) and
confirmed every B05 peer_question received a verdict.

## Coverage audit table (SUBSTANTIVE rows)

| Peer-quarter | B06 claimed anchor | Quote located at | Status |
|---|---|---|---|
| GULPOLY Nov_2025 | p.8, "not our target audience at all" | p.8 (between [page 8]/[page 9] markers) | MATCH |
| GULPOLY Nov_2025 | p.3, Rs 5.34cr PLI | p.3 (between [page 3]/[page 4]) | MATCH |
| GULPOLY Feb_2026 | p.6, "lower allocation than what it was applied for" | p.6 | MATCH |
| GULPOLY Feb_2026 | p.10, "adjusted EBITDA per litre... was Rs. 9" | p.10 (between [page 10]/[page 11]) | MATCH |
| GULPOLY May_2026 | p.8, "about INR 10 to INR 11 on average" | p.8 | MATCH |
| GULPOLY May_2026 | p.8, PLI "about INR 30 crores per annum" | p.8 | MATCH |
| GULPOLY May_2026 | p.6, FCI "400 million tonnes" abundance quote | p.7 | ANCHOR OFF BY 1 (finding 1) |
| GULPOLY May_2026 | p.13, applied 23cr L / received 18cr L (78%) | p.14 | ANCHOR OFF BY 1 (finding 2) |
| GULPOLY Aug_2026 | p.6-7, ethanol revenue Rs426cr / EBITDA Rs81cr | p.6 | MATCH (figures genuine; see finding 8 on B06's derived "19%") |
| GULPOLY Aug_2026 | (Part 4 prose) guided EBITDA margin "10-11%" | p.5 and p.7 ("10 to 11%" / "10% to 11%") | MATCH |
| BALRAMCHIN Feb_2026 | p.10-11, tendered 5cr L / received 3.15cr L (63%) | p.10 | MATCH |
| BALRAMCHIN Feb_2026 | p.10-11, national "~60% of tenders" accepted | p.10 | MATCH |
| BALRAMCHIN Jun_2026 | p.11, "FY26 production 27cr L / nameplate 34-35cr L"; Vivek Saraogi "At the industry level, definitely there is an overcapacity" | p.10; quote spoken by Pramod Patwari, not Vivek Saraogi | ANCHOR OFF BY 1 + SPEAKER MISATTRIBUTION (finding 6) |
| TRIVENI Nov_2025 | p.5, Cycle 1 "1,048 crore litres against 1,050 crore" | p.5 | MATCH |
| TRIVENI Nov_2025 | p.5-6, "country's production is north of 2,300 crore" | p.6 | MATCH (within cited range) |
| TRIVENI Nov_2025 | p.5, FCI ethanol price "Rs 58.5 to Rs 60.32" | p.6 | ANCHOR OFF BY 1 (finding 3) |
| TRIVENI Nov_2025 | p.10, maize EBITDA "Rs 11 or Rs 12 a litre" | p.10 | MATCH |
| TRIVENI Nov_2025 | p.2, term loans ~Rs310cr / ~Rs160cr subvention | p.3 | ANCHOR OFF BY 1 (finding 4) |
| TRIVENI Feb_2026 | p.11-12, "robust double-digit contribution, higher than C-heavy" | p.11 | MATCH |
| TRIVENI Feb_2026 | p.16, "the massive overcapacity that exists in the nation" | p.8 | ANCHOR WRONG BY 8 PAGES (finding 5) |
| TRIVENI Jun_2026 | p.17-18, "huge disappointment... haven't even had R2" | p.18 | MATCH (within cited range) |
| TRIVENI Aug_2026 | p.6-7, Supreme Court stay / BPCL challenge to Karnataka HC ruling | p.6 | MATCH — the run's single most consequential peer finding, confirmed accurate and precisely anchored |
| TRIVENI Aug_2026 | p.10-11, capacity ~2,000cr L vs offtake; standalone-distillery solvency risk | p.10 | MATCH |
| TRIVENI Aug_2026 | p.12-13, margin "maintained" via DDGS realisation increase | p.12 | MATCH |

10 of 10 SUBSTANTIVE peer-quarter rows have real, locatable, accurately
quoted citations. None is fabricated or invented. Six citations across four
different transcripts carry a page-anchor error (five off-by-one, one off
by eight pages), and one quote is misattributed to the wrong speaker. The
run's headline finding (TRIVENI's Supreme Court/BPCL disclosure, Q1FY27,
the item B06 calls its strongest independent confirmation) is anchored
exactly and verified word for word.

## CITED-ONLY rows: spot-read for missed material

- **BALRAMCHIN "May 2026" (filed 30-Apr-2026, PLA/capital-raise special
  call).** Confirmed silent-period framing: line 50-51 of the transcript,
  "currently in a silent period... refrain from asking questions related to
  the quarterly business performance." No ethanol allocation, private-OMC,
  or margin content anywhere in the file. B06's CITED-ONLY classification
  and its use of this call solely for capex-cycle context (Part 2C) is
  accurate; nothing claim-relevant was left unused.
- **BALRAMCHIN Aug_2026 (Q1 FY27).** Spot-read of the Q&A (lines 100-320):
  content is next-season C-heavy/grain volume planning, distillery margin
  resilience from feedstock mix (B-heavy plus maize, "hardly any sale...
  juice-based ethanol, that is the reason margins are at a good level"),
  and PLA. No mention of Jio-bp/Nayara/Reliance, no new allocation-shock
  language, no PBT-percentage disclosure. B06's characterisation ("no new
  allocation-shock or private-OMC content") matches; no missed material
  found against the claim list.

No peer-quarter in this run is marked UNUSED; all 12 transcripts appear in
B06's coverage map as either SUBSTANTIVE or CITED-ONLY.

## Verdict-discipline audit

| Q | B06 verdict | Independent peer anchors | Discipline check |
|---|---|---|---|
| Q1 (allocation hit rate) | PARTIALLY VERIFIED | 3 (GULPOLY, BALRAMCHIN, TRIVENI) | OK |
| Q2 (private-OMC reneging) | UNVERIFIABLE | 0 (silence) | OK — no verdict upgraded from silence |
| Q3 (maize margin compression) | CONTRADICTED | 2 (GULPOLY, TRIVENI) | OK |
| Q4 (balanced demand-supply) | CONTRADICTED (framing) | 3 (TRIVENI, BALRAMCHIN, GULPOLY context) | OK |
| Q5 (government-scheme dependency) | PARTIALLY VERIFIED (qualitative only) | 3 (GULPOLY, BALRAMCHIN, TRIVENI) | OK |
| Q6 (FCI-rice realisation price) | VERIFIED (price point) | **1** (TRIVENI only — GULPOLY confirms the mandate mechanics, not the litre price) | **FAIL — rule 4** |

**Finding 7 (MAJOR, rule 4).** Q6's price-point sub-claim is marked VERIFIED
but rests on a single peer anchor (TRIVENI's Rs 58.5→60.32/litre quote).
GULPOLY's Feb_2026 and Nov_2025 transcripts confirm the 40% FCI-rice mandate
and its raw-material pricing (Rs 24-25/kg) but never quote a separate
FCI-ethanol litre realisation figure — B06's own Part 1 text says so
explicitly ("does not separately quote an FCI-ethanol litre price"). Per
Verifier D rule 4, a VERIFIED verdict resting on one peer should read
PARTIALLY VERIFIED. The availability-constraint half of the same Q6 row
(CONTRADICTED, two peers — TRIVENI via the 40% mandate context and GULPOLY's
explicit abundance statement) is correctly disciplined; only the
price-point half over-states its own evidentiary base.

**claims_all_addressed: true.** All six peer_questions in B05's
peer_questions list (allocation hit rate, private-OMC reneging, maize
margin, demand-supply balance, government-scheme PBT dependency, FCI-rice
realisation/availability) received a verdict in B06 Part 1, Q1 through Q6,
in the same order and with the same check_peers lists honoured.

## Findings

| # | Severity | Location | Claimed | Source truth | Note |
|---|---|---|---|---|---|
| 1 | MINOR | B06 Q6 peer evidence, GULPOLY May_2026 FCI-abundance quote | "p.6" | p.7 | One-page anchor drift; quote itself verbatim and genuine |
| 2 | MINOR | B06 Q1 peer evidence, GULPOLY May_2026 own bid-vs-award | "p.13" | p.14 | One-page anchor drift; figures (23cr applied, 18cr received, 78%) confirmed exact |
| 3 | MINOR | B06 Q6 peer evidence, TRIVENI Nov_2025 FCI-ethanol price | "p.5" | p.6 | One-page anchor drift; quote verbatim and genuine, near-exact match to TruAlt's claimed range |
| 4 | MINOR | B06 Q5 peer evidence, TRIVENI Nov_2025 term loans/subvention | "p.2" | p.3 | One-page anchor drift |
| 5 | MAJOR | B06 Q4 peer evidence, TRIVENI Feb_2026 "massive overcapacity" | "p.16" | p.8 | Anchor wrong by 8 pages; not findable at the cited location (only via full-transcript search); content is genuine and the only occurrence of the phrase in the file |
| 6 | MINOR | B06 Q4/Part 2C, BALRAMCHIN Jun_2026 overcapacity quote | attributed to "Vivek Saraogi"; "p.11" | spoken by Pramod Patwari; located p.10 | Speaker misattribution plus one-page anchor drift; production/nameplate figures (27cr/34-35cr L) confirmed exact |
| 7 | MAJOR | B06 Part 4/Q6 verdict | "VERIFIED (price point)" | rests on 1 peer anchor (TRIVENI); GULPOLY does not corroborate the litre price | Rule 4: VERIFIED on one peer should read PARTIALLY VERIFIED |
| 8 | MINOR | B06 Q3 peer evidence, GULPOLY Aug_2026 Q1FY27 margin | B06 computes "19% margin for the quarter" (Rs81cr / Rs426cr) | management's own stated figure in the transcript is "EBITDA margin of 18%" | Arithmetic (81/426=19.0%) is correct but diverges from the company's own stated round figure; does not change the substantive contradiction (margin held well above the 10-11% full-year guide either way) |

No CRITICAL findings. No fabricated citation, no invented peer statement,
no verdict upgraded from silence to VERIFIED/CONTRADICTED without evidence.

## Summary

The pipeline genuinely read and used the peer transcripts it claims to have
used. Every SUBSTANTIVE citation checked is a real quote from the named
file; the run's most consequential single finding (TRIVENI's Supreme
Court/BPCL disclosure) is anchored with precision. The defects found are
citation-hygiene issues, not coverage or fabrication failures: five
one-page anchor drifts, one eight-page anchor miss, one speaker
misattribution, one derived-vs-stated figure divergence, and one verdict
(Q6 price point) that should be downgraded from VERIFIED to PARTIALLY
VERIFIED under the single-peer rule. None of these would flip the run's
substantive conclusions (the margin-compression contradiction, the
demand-supply framing contradiction, or the Supreme Court/BPCL
confirmation all stand as B06 states them).

acceptance_rate basis: 11 of 12 peer-quarter rows handled without a MAJOR
finding (the one MAJOR row is TRIVENI Feb_2026, on the anchor-location
failure only — its content is genuine) = 92%. The Q6 verdict-discipline
MAJOR finding is a cross-cutting claim-level issue, not peer-row-specific,
and does not itself subtract from this peer-row denominator.

```yaml
stage: B12d
company: "TRUALT"
run_date: "2026-09-18"
model: claude-sonnet-5
status: complete
peers_audited: 12
substantive_confirmed: 10
substantive_unsupported: []
unused_but_relevant: []
claims_all_addressed: true
verdict_discipline_fails:
  - {claim: "Q6 FCI-rice ethanol realisation price point", verdict_given: "VERIFIED", basis: "1 independent peer anchor (TRIVENI only; GULPOLY confirms mandate mechanics, not the litre price)", should_be: "PARTIALLY VERIFIED"}
findings:
  - {severity: "MINOR", location: "B06 Q6, GULPOLY-Concall_May_2026_Transcript.pdf FCI-abundance quote", claimed_anchor: "p.6", source_truth_anchor: "p.7", note: "one-page anchor drift; quote verbatim and genuine"}
  - {severity: "MINOR", location: "B06 Q1, GULPOLY-Concall_May_2026_Transcript.pdf own bid-vs-award", claimed_anchor: "p.13", source_truth_anchor: "p.14", note: "one-page anchor drift; 23cr applied / 18cr received / 78% figures confirmed exact"}
  - {severity: "MINOR", location: "B06 Q6, TRIVENI-Concall_Nov_2025_Transcript.pdf FCI-ethanol price quote", claimed_anchor: "p.5", source_truth_anchor: "p.6", note: "one-page anchor drift; quote verbatim, near-exact match to TruAlt claimed range"}
  - {severity: "MINOR", location: "B06 Q5, TRIVENI-Concall_Nov_2025_Transcript.pdf term-loan subvention", claimed_anchor: "p.2", source_truth_anchor: "p.3", note: "one-page anchor drift"}
  - {severity: "MAJOR", location: "B06 Q4, TRIVENI-Concall_Feb_2026_Transcript.pdf massive-overcapacity quote", claimed_anchor: "p.16", source_truth_anchor: "p.8", note: "anchor wrong by 8 pages, not findable at cited location; content genuine, only occurrence in file"}
  - {severity: "MINOR", location: "B06 Q4/Part 2C, BALRAMCHIN-Concall_Jun_2026_Transcript.pdf overcapacity quote", claimed_anchor: "p.11, attributed to Vivek Saraogi", source_truth_anchor: "p.10, spoken by Pramod Patwari", note: "speaker misattribution plus one-page anchor drift; 27cr/34-35cr L production figures confirmed exact"}
  - {severity: "MAJOR", location: "B06 Part 4, Q6 verdict", claimed_anchor: "n/a (verdict discipline)", source_truth_anchor: "n/a", note: "VERIFIED price-point verdict rests on a single peer anchor (TRIVENI); rule 4 requires PARTIALLY VERIFIED"}
  - {severity: "MINOR", location: "B06 Q3, GULPOLY-Concall_Aug_2026_Transcript.pdf Q1FY27 margin", claimed_anchor: "computed 19% (Rs81cr/Rs426cr)", source_truth_anchor: "management states 18% in the transcript", note: "arithmetic correct but diverges from company's own stated figure; does not change the substantive contradiction"}
critical_count: 0
major_count: 2
minor_count: 6
acceptance_rate: 92
```
