# Verifier D: Peer Coverage Audit — N R Agarwal Industries Ltd (NRAIL)
Run date: 2026-07-22 | Model: claude-sonnet-5 | Emits: B12d

## Scope
Audited: Stage 6 peer verification report (`06-peers.md`) against the 8 peer transcripts it
draws on (JKPAPER x4: May-2022, Aug-2022, May-2023, May-2024; KUANTUM x4: Aug-2025,
Nov-2025, Feb-2026, May-2026) and against the 6 peer_questions injected by B05
(`B05-concall.yaml`). I read all 8 transcripts independently and checked B06's page-anchored
quotes against the actual source text, then audited coverage-map SUBSTANTIVE claims for a
real, findable citation, and audited verdict discipline (2-peer rule for VERIFIED, no
upgrade-from-silence).

Context noted per the task brief and confirmed on read: the peer set has a genuine
fibre/product mismatch (JKPAPER virgin-fibre packaging board; KUANTUM wood+agro
writing/printing, explicitly not paperboard) and a vintage split (JKPAPER FY22-FY24,
KUANTUM FY26). B06 treats this mismatch as informative rather than papering over it —
that framing is honest and correctly applied throughout the report.

## Coverage audit per peer (8 transcripts)

| Peer / Quarter | B06 usage | Verified? |
|---|---|---|
| JKPAPER Q4 FY22 (filed "May_2022") | SUBSTANTIVE | **Not supported** — no page-anchored quote to this file anywhere in Part 1 or Part 2; only a general, unanchored coverage-map characterization. See Finding 1. |
| JKPAPER Q1 FY23 (2-Aug-2022) | SUBSTANTIVE | Confirmed. Multiple quotes checked against source and matched exactly (100% virgin-fibre statement p.9; coated-paper import-dependency p.5-6; India-growth/demand link p.10-11; Rs2,000cr Gujarat capex p.8). |
| JKPAPER Q4 FY23 (19-May-2023) | SUBSTANTIVE | Confirmed content exists in this call, but one specific figure (33.1% FY23 EBITDA margin) is cross-attributed to the wrong call elsewhere in the report — see Finding 2. |
| JKPAPER Q4 FY24 (21-May-2024) | SUBSTANTIVE | Confirmed. The consolidation-narrative rejection quote (p.12), antidumping filing status (p.7-8), corrugated-packaging acquisitions (p.5), BCTMP ROI comment (p.6) all checked and matched exactly. |
| KUANTUM Q1 FY26 (11-Aug-2025) | SUBSTANTIVE | Confirmed for the DGTR probe (p.3) and 3-4% imported-pulp share (p.9) citations. One contribution line in the coverage map ("wheat-straw/wood cost baseline") is not actually supported by this specific transcript — see Finding 5. |
| KUANTUM Q2/H1 FY26 (10-Nov-2025) | SUBSTANTIVE | Confirmed. "Not in the paperboard segment at all" (p.7), GST inverted-duty explanation (p.3), Rs1,300/ton cost increase (p.4), import-substitution language (p.16), India 5-6% CAGR (p.16), 2012-13 analyst aside (p.10) all checked and matched exactly. |
| KUANTUM Q3 FY26 (9-Feb-2026) | SUBSTANTIVE | Confirmed. "Wider paper industry is expanding..." (p.5), Ruchira as sole named W&P entrant (p.14-15), 6% CAGR/education demand (p.14), anti-involution skepticism (p.16-17) all checked and matched exactly. |
| KUANTUM Q4 FY26/FY26 (29-May-2026) | SUBSTANTIVE | Confirmed. "Paperboards is an entirely different segment" (p.5), MIP-for-paperboard extension (p.5-6), West Asia trade-diversion risk (p.2), notebook exit 22%→7-8% (p.11 and p.17) all checked and matched exactly, with two page-citation imprecisions — see Findings 3 and 4. |

**Substantive-confirmed: 7 of 8.** One peer-quarter (JKPAPER May_2022 file) is marked
SUBSTANTIVE in the coverage map without a locatable, page-anchored citation anywhere in
Parts 1-2 of the report, which fails the audit bar in rule 2.

## Verdict-discipline audit (6 claims from B05 peer_questions)

All 6 questions in B05's `peer_questions` list (Q1 realization, Q2 waste-paper cost, Q3
import-substitution, Q4 consolidation, Q5 capex cycle, Q6 GDP-demand link) received a
verdict in B06 Part 1. No skipped claims — `claims_all_addressed: true` is correct.

- **Q5 (VERIFIED)** is the only VERIFIED claim in the set and it rests on two independent
  peers (JKPAPER + KUANTUM) plus three peers named within KUANTUM's own testimony (West
  Coast, Andhra Paper, Ruchira), with 5 anchors total — satisfies the 2-peer rule. No
  discipline failure.
- **Q3 and Q4 (CONTRADICTED)** each rest on a single peer (JKPAPER). This is correct
  under the rubric — the 2-peer bar applies to VERIFIED, not to CONTRADICTED — and I
  independently confirmed both underlying quotes exist exactly as cited (Q3: p.5-6 of the
  Aug-2022 call; Q4: p.12 of the May-2024 call, the "smaller mill closing down... not the
  dumping" quote from A.S. Mehta).
- **Q1 and Q6 (PARTIALLY VERIFIED)** are correctly downgraded from VERIFIED given the
  vintage gap (Q1) and the paperboard-specific gap for KUANTUM's corroboration (Q6) — this
  is the report correctly applying its own stated discipline rather than inflating
  confidence.
- **Q2 (UNVERIFIABLE)** is the honest and correct call — neither peer sources
  recovered/waste paper, so the claim genuinely cannot be triangulated from this set. No
  verdict is upgraded from peer silence anywhere in the report; I found no instance of a
  claim marked VERIFIED or PARTIALLY VERIFIED where the peer evidence was actually silent.

**No verdict-discipline failures found.**

## Findings

| # | Severity | Location | Detail |
|---|---|---|---|
| 1 | MAJOR | Part 3 Peer Coverage Map, row 1 / YAML `peer_coverage_map[0]` | JKPAPER Q4 FY22 ("May_2022" file) is marked SUBSTANTIVE, but no quote from this file is page-anchored anywhere in Part 1 or Part 2 of the report — it exists only as a general, unanchored coverage-map summary ("Pre-downturn baseline... no major capex announcement industry-wide at that time"). On independent read, that characterization itself overstates the source: the actual line is A.S. Mehta describing JK Paper's *own* post-2000cr-capex pause ("I don't think it is expected from us to invest further in the capacity immediately... At this point of time in the paper there is no major expansion") — a company-specific statement, not an industry-wide one. Per rule 2, SUBSTANTIVE without a real, findable citation is MAJOR. |
| 2 | MAJOR | Part 1, Q1 evidence row | The "33.1% FY23 EBITDA margin" figure is cited under "(Q4 FY24 call, 21-May-2024, p.2, A.S. Mehta)" alongside genuine Q4 FY24 quotes ("sharp drop in the prices..."; "wood cost... 30%-35%"). On independent read, page 2 of the Q4 FY24 (May-2024) call contains the 26-27% FY24 figure and the "22-23 was the outlier year" framing, but not the number "33.1%". That figure is stated verbatim in the *Q4 FY23* call (19-May-2023), page 2 ("the EBITDA margin- fourth quarter was around 29.8% and full year 33.1%"). The number itself is genuine and exists in the peer set, but it is cross-attributed to the wrong call/date. |
| 3 | MINOR | Part 2E / YAML `risks_peers_raise` | The "anti-dumping/anti-subsidy/MIP... 1.5-2+ years after filing" quote is cited to "(Kuantum, Q4 FY26 call, 29-May-2026, p.9-10)". On independent read, the exact quote ("it will normally take about 1.5 to 2 years for it to start getting implemented") appears on page 8 of that transcript, not p.9-10. |
| 4 | MINOR | Stage-specific flags / YAML `flags` | The notebook-segment-exit figures ("~22% to ~7-8%") are cited to "Kuantum... Q4 FY26 call p.13, 17". On independent read, the first statement of this figure ("about 22% was going into this sector... We are already down to about 7% to 8%") is on page 11, not page 13; the second citation (p.17, the follow-up restating the same figures) is correct as cited. |
| 5 | MINOR | Part 3 Peer Coverage Map, KUANTUM Q1 FY26 row | The coverage-map contribution line for the Aug-2025 (Q1 FY26) call lists "wheat-straw/wood cost baseline" as a contribution of that specific transcript. On independent read, this call discusses wood pulp pricing and the 3-4% imported-pulp share but does not mention "wheat straw" at all; wheat straw first appears as a topic in the Q2/H1 FY26 (Nov-2025) call, which is separately and correctly cited elsewhere in the report. Not fabricated — the content exists and is used correctly elsewhere — but misattributed to this specific row. |

No CRITICAL findings. No fabricated quotes, no invented peer statements, and no verdict
upgraded from peer silence were found anywhere in the 8-transcript, 6-claim, 8-peer-row
audit. The overwhelming majority of B06's ~30+ page-anchored citations that I independently
checked against source (JKPAPER 100%-virgin-fibre statement, coated-board import-dependency
framing, consolidation-rejection quote, capex figures; KUANTUM's "not in paperboard"
statements across three separate calls, GST inverted-duty mechanics, DGTR/MIP timeline,
West Asia trade-diversion risk, capex-race naming of five peers) matched the source
transcripts exactly, including page number, speaker, and wording. The peer-mismatch framing
(vintage gap, fibre/product gap) that the report leads with is accurate and is applied
consistently rather than selectively — B06 does not quietly let KUANTUM's non-paperboard
disclaimers count as affirmative paperboard evidence, and it says so explicitly in Part 3.

## Coverage note
I read all 8 transcripts in full and checked essentially every page-anchored quote in B06
Parts 1 and 2 against source (all six claim rows, all five cross-read items, the five
stage-specific flags). I did not attempt to independently re-derive every unquoted
background/contextual sentence in the coverage-map "contribution" column beyond spot-checks,
since those are summaries rather than sourced assertions.

```yaml
stage: B12d
company: "NRAIL"
run_date: "2026-07-22"
model: claude-sonnet-5
status: complete
peers_audited: 8
substantive_confirmed: 7
substantive_unsupported: ["JKPAPER Q4 FY22 (filed \"May_2022\" transcript) — marked SUBSTANTIVE with no page-anchored citation in Part 1/2"]
unused_but_relevant: []
claims_all_addressed: true
verdict_discipline_fails: []
findings:
  - {severity: "MAJOR", location: "Part 3 Peer Coverage Map / YAML peer_coverage_map[0]", claimed: "JKPAPER Q4 FY22 (May_2022) marked SUBSTANTIVE, contribution described as pre-downturn baseline incl. 'no major capex announcement industry-wide at that time'", source_truth: "No page-anchored quote from this file appears in Part 1/2; the closest source line is JK Paper's own statement about pausing its own further capex post its Rs2,000cr expansion, not an industry-wide observation", note: "SUBSTANTIVE without a real, findable citation; coverage-map summary also overstates a company-specific remark as industry-wide"}
  - {severity: "MAJOR", location: "Part 1, Q1 evidence row", claimed: "EBITDA margin falling from 33.1% (FY23) cited to Q4 FY24 call (21-May-2024), p.2", source_truth: "33.1% figure appears verbatim in the Q4 FY23 call (19-May-2023), p.2 ('full year 33.1%'); Q4 FY24 call p.2 contains the 26-27% figure and outlier-year framing but not '33.1%'", note: "Genuine number, wrong call/date attribution -- cross-call misattribution of a specific sourced figure"}
  - {severity: "MINOR", location: "Part 2E / YAML risks_peers_raise", claimed: "'1.5-2+ years' MIP/antidumping timeline cited to Kuantum Q4 FY26 call p.9-10", source_truth: "Exact quote ('about 1.5 to 2 years for it to start getting implemented') is on p.8 of that transcript", note: "Page-citation imprecision, quote itself is accurate"}
  - {severity: "MINOR", location: "Stage-specific flags / YAML flags", claimed: "Notebook segment exit ~22% to ~7-8% cited to Kuantum Q4 FY26 call p.13, 17", source_truth: "First statement of the figure is on p.11, not p.13; p.17 citation (restatement) is correct", note: "Page-citation imprecision, figures themselves are accurate"}
  - {severity: "MINOR", location: "Part 3 Peer Coverage Map, KUANTUM Q1 FY26 row", claimed: "Contribution listed as including 'wheat-straw/wood cost baseline'", source_truth: "This transcript (11-Aug-2025) does not mention wheat straw; wheat straw first appears in the Q2/H1 FY26 (10-Nov-2025) call, correctly cited elsewhere", note: "Content is not fabricated -- exists and is correctly cited under a different call -- but misattributed in this row"}
critical_count: 0
major_count: 2
minor_count: 3
acceptance_rate: 88   # 7 of 8 peer-transcripts correctly handled (real, verified citations) ÷ 8 audited
```
