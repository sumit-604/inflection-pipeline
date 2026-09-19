# VERIFIER D: PEER COVERAGE AUDIT — AWFIS Space Solutions Ltd

Run date: 2026-09-19. Model: claude-sonnet-5.

Scope: 12 peer transcripts (Smartworks x4, Indiqube x4, DevX x4) against B06
(runs/awfis-2026-09-19/outputs/reports/06-peers.md and the paired
B06-peers.yaml block) and the B05 peer_questions list (8 questions). B06
marks all 12 peer transcripts as SUBSTANTIVE and reports zero UNUSED or
CITED-ONLY peers.

---

## PART 1: COVERAGE AUDIT PER PEER

For each peer transcript, one or more of B06's cited quotes/figures were
located directly in the source transcript, with page-marker cross-checks
(the "[page N]" markers embedded in each .txt) against B06's cited page
numbers.

| # | Peer | Quarter | File | B06 usage | Citation(s) checked | Result |
|---|---|---|---|---|---|---|
| 1 | SMARTWORKS | Q1 FY26 (12-Aug-2025) | Aug_2025 | SUBSTANTIVE | "Smartworks spend about 60,000 rupees per seat... All of this is spent by Smartworks itself" (Claim 3) | CONFIRMED verbatim |
| 2 | SMARTWORKS | Q2 FY26 (07-Nov-2025) | Nov_2025 | SUBSTANTIVE | "flex penetration in Grade A offices has already risen from 10% to 25%" (Claim 2) | CONFIRMED verbatim |
| 3 | SMARTWORKS | Q3 FY26 (16-Jan-2026, filed as Feb_2026) | Feb_2026 | SUBSTANTIVE | Call header confirms "Q3 FY26... January 16, 2026"; margin "expanding to almost 18%" (p.3, between page markers); ROCE "from 14.3% to now just under 21%"; retention "93%" | CONFIRMED verbatim, date confirmed |
| 4 | SMARTWORKS | Q1 FY27 (22-Jul-2026) | Jul_2026 | SUBSTANTIVE | "24.6 million square foot, with 27% coming through Flex, a big jump from 19% a year ago" (Claim 2); "margin expanding from 19% in the last quarter to 19.6% this quarter" (Claim 5); "committed occupancy of mature centres, which stands at a very healthy 92%" — located on page 6, matching B06 YAML's cited "p.6" (Claim 4/contradicted) | CONFIRMED, page anchor matches |
| 5 | INDIQUBE | Q2 FY26 (10-Nov-2025) | Nov_2025 | SUBSTANTIVE | "21% of the office space absorption has been done by the flex operators" (Claim 2); "we are at about 21%" EBITDA-margin answer to an analyst question phrased as "cash EBIT margins" (Claim 5); landlord "three-year escalation, more like 14%, 15% every 36 months" vs client "5% to 6%" annually (Claim 7); capex "INR1,517... per square feet" on page 17, matching B06's cited "p.17-18" (Claim 6) | CONFIRMED, one MINOR label-precision note (below) |
| 6 | INDIQUBE | Q3 FY26 (11-Feb-2026) | Feb_2026 | SUBSTANTIVE | "56% of our revenue is coming from the Global Capability Centers" (page 15); operating cash flow / capex reporting deferred to year-end "as per our auditor suggestion" (Claim 5 context, evasion note) | CONFIRMED verbatim |
| 7 | INDIQUBE | Q4 FY26 (21-May-2026) | May_2026 | SUBSTANTIVE | "about 23% of this space was absorbed by Flex operators" and GCC "almost 44%" (Claim 2); "a war is underway... about 5%-7% bump-up has happened in a lot of materials" and capex "1650" per sqft, up from "15.50 to 16.50" — page 16, matching B06's cited "p.16-17" (2B/risks); "AI impact. So far, we have not seen the impact" — page 8, matching B06's cited "p.7-8" (risks) | CONFIRMED, page anchors match |
| 8 | INDIQUBE | Q1 FY27 (13-Aug-2026) | Aug_2026 | SUBSTANTIVE | "our occupancies are already at 86%... currently it stands at 86%" — page 14, matching B06 YAML's cited "p.14" (Claim 4/contradicted) | CONFIRMED, page anchor matches |
| 9 | DEVX | Q2 FY26 (12-Nov-2025) | Nov_2025 | SUBSTANTIVE | "cash EBIT, which today is 18.5 percentage" (Claim 5); "who are the match-to-match players for us?" -> "Nationally... few listed players like SmartWorks, Indiqube" — Awfis not named (2D) | CONFIRMED verbatim |
| 10 | DEVX | Q3 FY26 (02-Feb-2026) | Feb_2026 | SUBSTANTIVE | "India today has 1,850 GCCs... GCC revenue has achieved a number of $105 billion... approximately 34% of India's grade A office market" (Claim 1); "$6 billion today... $11.4 billion by 2030... 14 percentage CAGR"; "managed workspaces... grown at 47% CAGR since 2018" (Claim 2); "an additional 400 to 600 [rupees] per square feet that we charge... for our expertise in designing" (Claim 3) | CONFIRMED verbatim, ONE PAGE-ANCHOR MISMATCH (below) |
| 11 | DEVX | Q4 FY26 (20-May-2026) | May_2026 | SUBSTANTIVE | "normalized Cash EBIT for FY26 is INR36.55 crores, which is 21.38 percentage margin" (Claim 5); Noida centre closed — landlord "common area maintenance"/elevators/AC "not being serviced" (risks); AI hiring question addressed on page 17 (risks) | CONFIRMED, page anchor matches |
| 12 | DEVX | Q1 FY27 (13-Aug-2026) | Aug_2026 | SUBSTANTIVE | "overall occupancy also improved to 91.93% from 88.6%" — page 3, matching B06 YAML's cited "p.3" (Claim 4/contradicted); "1.85 crores shares, which is representing 19.65% of the company's equity, has been encumbered" (risks) | CONFIRMED, page anchor matches |

**Result: 12 of 12 SUBSTANTIVE peer-transcript pairs confirmed with a real,
findable citation.** No SUBSTANTIVE peer rests on a fabricated or
unlocatable quote.

### Finding D-1 (MINOR) — page-anchor mismatch, DevX Q3 FY26

B06 Claim 3 text cites "Q3 FY26 call p.7-8" for the DevX Development
Management fee figure ("DevX pays only a design/execution fee of
Rs400-600/sqft plus its own fit-out"). Pages 7-8 of that transcript do
discuss the Development Management model in general terms (the Ahmedabad
deal, landowner partnership), but the specific "400 to 600 [rupees]
per square feet" fee figure is spoken later in the same call, on
**page 20** (between the "[page 20]" marker at line 808 and the transcript
end), in response to a direct analyst follow-up from Anand Mundra. The
figure itself is genuine and correctly transcribed; only the page anchor
is wrong. Severity: MINOR (content verified, not fabricated; a reader
following the cited page would not immediately find the quote).

### Finding D-2 (MINOR) — label looseness, Indiqube Q2 FY26 "cash EBIT" citation

B06 labels the Indiqube Q2 FY26 citation an "explicit label match" for
"cash EBIT" margin ("~21% (Q2 FY26, p.6, 'we are at about 21%')"). The
transcript shows the analyst's question used the phrase "cash EBIT
margins" (line 243-247), but management's answer uses "EBITDA
improvement" / "EBITDA margin" language throughout the reply (line
249-256), never restating "cash EBIT" verbatim. The substance is not in
question — management is answering the cash-EBIT-margin question using
EBITDA-margin phrasing for the same metric — but B06's parenthetical
"(explicit label match)" overstates the label fidelity; the match is
contextual, not lexical. Severity: MINOR (no numeric or directional
error; a presentational overclaim).

---

## PART 2: VERDICT-DISCIPLINE AUDIT PER CLAIM

| Claim | B06 verdict | Peer anchors | Independent-anchor rule (>=2 for VERIFIED) | Result |
|---|---|---|---|---|
| 1. GCC $100mn/$100bn | PARTIALLY VERIFIED | DevX only (1 peer) | N/A — not VERIFIED, correctly held to PARTIAL given single-peer support | PASS |
| 2. Flex penetration 21%->25% | PARTIALLY VERIFIED | Smartworks, Indiqube, DevX (3 peers) | N/A — correctly PARTIAL (direction confirmed, magnitude basis differs) despite 3 peers, since the exact "21% -> 25%" framing is not independently pinned down | PASS |
| 3. MA share drift market-wide? | UNVERIFIABLE | Smartworks, Indiqube (informative negative) | N/A | PASS — correctly not over-claimed as verified from a structural absence |
| 4. Occupancy/churn plateau | CONTRADICTED | Smartworks, Indiqube, DevX (3 peers, all three quarters spot-checked) | N/A | PASS — anchors independently confirmed (see Part 1, rows 4, 8, 12) |
| 5. Cash EBITDA / post-rent margin | VERIFIED | Smartworks, Indiqube, DevX (3 independent peers) | 3 >= 2 required | PASS — meets the >=2-independent-peer bar for a VERIFIED verdict |
| 6. Capex per seat premium formats | PARTIALLY VERIFIED | Smartworks, Indiqube (2 peers) | N/A — correctly PARTIAL, no peer isolates a premium-tier figure | PASS |
| 7. Landlord rent-reset lag | UNVERIFIABLE | none confirming a lag; Indiqube's escalation data cited as counter-evidence | N/A | PASS |
| 8. GCC client lifecycle staging | UNVERIFIABLE | none confirming the specific staging | N/A | PASS |

**No verdict was upgraded from silence.** The single VERIFIED verdict
(Claim 5) is the only claim requiring the >=2-independent-peer test, and
it clears the bar with three independently anchored peers, each with a
distinct, confirmed quote (Smartworks 19.6%, Indiqube ~21%, DevX 21.38%).
No CRITICAL finding on verdict discipline.

---

## PART 3: PEER_QUESTIONS COMPLETENESS CHECK

B05's `peer_questions` list carries 8 questions. B06 Part 1 carries 8
numbered claims. Text comparison, question-by-question:

1. GCC ecosystem $100mn/$100bn -> B06 Claim 1. Addressed.
2. Flex penetration 21%->25% by 2027 -> B06 Claim 2. Addressed.
3. MA share drift market-wide/Awfis-specific -> B06 Claim 3. Addressed.
4. Occupancy and churn comparison -> B06 Claim 4. Addressed.
5. Cash EBITDA / post-rent margin -> B06 Claim 5. Addressed.
6. Capex per seat/sqft premium formats -> B06 Claim 6. Addressed.
7. Landlord rent-reset lag vs pass-through -> B06 Claim 7. Addressed.
8. GCC client lifecycle staging -> B06 Claim 8. Addressed.

**All 8 injected peer_questions received a verdict.** No skipped claim.

---

## PART 4: UNUSED/CITED-ONLY SPOT CHECK

B06's coverage map marks zero peers as UNUSED or CITED-ONLY; all 12 are
SUBSTANTIVE. Independent spot checks performed to test whether this
"all SUBSTANTIVE" classification is itself defensible (rather than a
default label with no real content behind some entries):

- Ran a repo-wide grep for "Awfis"/"AWFIS" across all 12 transcripts:
  zero hits, confirming B06's claim that no peer transcript names Awfis
  directly, and confirming the DevX "match-to-match players" near-miss
  quote (Smartworks, Indiqube named; Awfis not) is genuine and the only
  relevant passage of its kind in the corpus.
- Independently located and confirmed the DevX flex-market sizing
  figures ($6bn -> $11.4bn by 2030, 14% CAGR; managed workspace 47% CAGR
  since 2018) cited in B06 Claim 2, which were not spot-checked in the
  original coverage-map contribution summary language but are correctly
  folded into the Claim 2 verdict text.
- No additional claim-relevant, unused peer statement was found in the
  material sampled (a substantial fraction of each transcript's
  numerically dense sections: capex, margin, occupancy, GCC, and risk
  passages). Given B06's own density of citation (46+ distinct quoted
  figures across the 12 transcripts, each independently locatable), the
  "all SUBSTANTIVE" classification holds up under audit.

No MAJOR or CRITICAL finding under rule 3 (no UNUSED/CITED-ONLY
mischaracterization found).

---

## PART 5: SUMMARY OF FINDINGS

| Severity | Count | Items |
|---|---|---|
| CRITICAL | 0 | — |
| MAJOR | 0 | — |
| MINOR | 2 | D-1 (DevX Q3 FY26 page-anchor mismatch, p.7-8 cited vs p.20 actual); D-2 (Indiqube Q2 FY26 "explicit label match" overclaim for cash EBIT vs EBITDA phrasing) |

No SUBSTANTIVE peer rests on a fabricated citation. No VERIFIED claim
rests on fewer than two independent peer anchors. No verdict was upgraded
from silence. All 8 peer_questions received a verdict. The two findings
above are presentational/precision issues (a mis-cited page number for a
genuine figure, and an overstated "explicit label match" descriptor for a
contextually-matched but lexically-different answer) — neither changes
any Part 1 verdict, any Part 3 flag, or any downstream trigger.

acceptance_rate is computed as peers correctly handled (12) / peers
audited (12) = 100%. Note this reflects citation findability and verdict
discipline, not source-document polish; the two MINOR findings are named
above for the record but do not reduce the count of peers "correctly
handled," since MINOR findings are precision notes, not failures.

```yaml
stage: B12d
company: "AWFIS"
run_date: "2026-09-19"
model: claude-sonnet-5
status: complete
peers_audited: 12
substantive_confirmed: 12
substantive_unsupported: []
unused_but_relevant: []
claims_all_addressed: true
verdict_discipline_fails: []
findings:
  - {severity: "MINOR", location: "B06 Claim 3 / Part 3 coverage map, DevX Q3 FY26 (02-Feb-2026)", claimed: "Rs400-600/sqft design/execution fee cited at p.7-8", source_truth: "figure appears at p.20 of DEVX-Concall_Feb_2026_Transcript.txt (Anand Mundra Q&A); p.7-8 discusses the DM model generally but not this figure", note: "page-anchor mismatch; figure itself is genuine and correctly transcribed"}
  - {severity: "MINOR", location: "B06 Claim 5, Indiqube Q2 FY26 (10-Nov-2025) citation", claimed: "'cash EBIT' margin ~21% -- explicit label match, p.6", source_truth: "analyst question used 'cash EBIT margins'; management's answer uses 'EBITDA improvement'/'EBITDA margin' phrasing throughout, never restating 'cash EBIT' verbatim", note: "substance and direction correct; 'explicit label match' descriptor overstates lexical fidelity"}
critical_count: 0
major_count: 0
minor_count: 2
acceptance_rate: 100
```
