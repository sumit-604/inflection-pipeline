# Verifier D: Peer Coverage Audit — TRUALT, run 2026-09-18

Scope: the 12 peer transcripts (GULPOLY x4, BALRAMCHIN x4, TRIVENI x4) in
`inputs/peer-concalls/`, against `outputs/reports/06-peers.md` (B06) and the
6-item `peer_questions` list in `outputs/blocks/B05-concall.yaml`. Every
transcript .txt file carries its own `[page N]` extraction markers; per the
task brief, `[page N]` IS the PDF page reference B06 cites against. Where a
peer document also prints its own internal page footer ("Page N of M"), that
footer is NOT the citation basis — several of the errors found below trace to
that footer being read instead of the `[page N]` marker.

Did the pipeline actually use the peers it claims to have used? Mostly yes,
on content; three of ten SUBSTANTIVE citations point to the wrong location
(wrong page, or in one case the wrong CALL entirely), a regression on exactly
the failure mode this run's B06 rework claims to have fixed. No claim in the
peer_questions list went unanswered, and verdict discipline holds (zero
VERIFIED claims this run, so the >=2-anchor rule is not in play; no verdict
is upgraded from peer silence).

## PART 1: COVERAGE AUDIT PER PEER (peer_coverage_map, B06 Part 3)

10 of 12 peer-quarter rows are marked SUBSTANTIVE; 2 are CITED-ONLY. For each
SUBSTANTIVE row, the table below records whether the cited quote/figure is
actually findable AT the cited anchor.

| Peer / quarter | B06 citation checked | Found at cited anchor? | Verdict |
|---|---|---|---|
| GULPOLY Q2 FY26 (Nov_2025) | p.8, "not our target audience at all" / "cheapest ethanol...sugar mode"; p.3, "Rs. 5.34 crores" PLI | Both exact, p.8 and p.3 confirmed | CONFIRMED |
| GULPOLY Q3 FY26 (Feb_2026) | p.6, maize Rs18-21/kg + "20% to 30%" allocation-shortfall quote; p.10, "adjusted EBITDA per litre...Rs. 9...sustainable"; p.13, Rs21.8cr PLI / Rs5.36cr ISS reversal / "one and a half years" | All three exact at cited pages | CONFIRMED |
| GULPOLY Q4/FY26 (May_2026) | p.4, maize Rs19-20/kg; p.8, "INR 10 to INR 11 on average" EBITDA/litre; p.14, "23 crore liter...received for 18 crore liter" (78%); p.5, ethanol segment "margin of 12.5%"; p.15, PLI "about INR 30 crores per annum" | First four exact. PLI figure is NOT on p.15 (p.15 is an unrelated demand-supply exchange with no PLI mention) — it is on p.8, in the same answer as the EBITDA/litre figure | UNSUPPORTED (PLI anchor wrong, off by 7 pages) |
| GULPOLY Q1 FY27 (Aug_2026) | p.6, ethanol revenue Rs426cr/EBITDA Rs81cr, "EBITDA margin of 18%"; p.9, maize Rs23-25/kg; p.4, "temporary pressure...second quarter"; p.4 and p.8, FY27 guide "10% to 11%" | p.6, p.4 (pressure quote), p.8 (10-11% guide) all exact. The SECOND citation of "10% to 11%" is not on p.4 — it is on p.5 ("consolidated level...EBITDA margins of around 10 to 11%") | CONFIRMED (core citations solid; one secondary page ref one page off, MINOR) |
| BALRAMCHIN Q3 FY26 (Feb_2026) | p.10, "3.15 crore litres" / "60% of the tenders"; p.3, "not been revised for the past three years" (B-heavy/juice) | Both exact | CONFIRMED |
| BALRAMCHIN special call (30-Apr-2026, filed "May_2026") | CITED-ONLY, capex-cycle context only | Not independently re-verified against a Part-1/2 quote (none claimed) | N/A |
| BALRAMCHIN Q4 FY26 (filed Jun_2026) | p.10, "At the industry level, definitely there is an overcapacity" (Pramod Patwari); p.10, FY26 27cr L vs 34-35cr L nameplate | Both quotes are under the `[page 11]` marker, not `[page 10]`. The file's OWN internal footer under that marker reads "Page 10 of 12" — the likely source of the error, since the footer is one page behind the extraction's `[page N]` tag throughout this file (footer "Page 9 of 12" sits under `[page 10]`, "Page 10 of 12" sits under `[page 11]`). Speaker attribution (Pramod Patwari, not Vivek Saraogi) IS correct, confirmed independently | UNSUPPORTED (page anchor wrong; this is the exact page this run's rework claims to have fixed — from p.11 in the first run to p.10 in this rework — and the rework's "fix" is itself wrong: p.11 was the right answer for the extraction-page basis this task uses) |
| TRIVENI Q2 FY26 (Nov_2025) | p.5, "1,048 crore litres...against 1,050 crore"; p.6, "north of 2,300 crore litres"; p.3, term loans Rs310cr / Rs160cr subvention | All three exact | CONFIRMED |
| TRIVENI Q3 FY26 (Feb_2026) | p.8, "massive overcapacity that exists in the nation" | Exact — confirms the rework's own correction (p.16 to p.8) is right | CONFIRMED |
| TRIVENI Q4 FY26 (Jun_2026) | p.18, "huge disappointment. R2, R3, we should have been at R4"; p.17-18, "without incurring any new CapExes"; p.14, "33%...maize" / "56%...grain feedstock"; p.14, Sir Shadi Lal "produced no ethanol" / molasses "from our factory at Shamli at one of the other distilleries in the group" | First three confirmed exactly. The Sir Shadi Lal / no-ethanol / Shamli-molasses quote does NOT appear anywhere in the Jun_2026 transcript (searched "Shadi", "molasses", "amalgamat" across the full file — the only Sir Shadi Lal content in this call is share-issuance record-date administrivia at p.8). The exact quote is in TRIVENI-Concall_**Aug_2026**_Transcript.txt, p.13 (extraction marker), a DIFFERENT call entirely | UNSUPPORTED — wrong transcript, not just wrong page. The quote is real and correctly transcribed, but B06 has it filed under the wrong quarter's call |
| TRIVENI Q1 FY27 (Aug_2026) | p.6, Supreme Court stay / BPCL / Karnataka HC / AG 100cr L; p.11, "comes under huge question" solvency line; p.10, ~2,000cr L capacity vs ~1,100-1,300cr L offtake; p.12, DDGS "maintained" margin (not independently re-checked, lower priority) | First three exact | CONFIRMED |

Coverage tally: 10 SUBSTANTIVE rows checked. 7 fully confirmed on every
citation spot-checked. 3 carry at least one confirmed anchor failure
(BALRAMCHIN Jun_2026, GULPOLY May_2026, TRIVENI Jun_2026) — each MAJOR per
rule 2 ("SUBSTANTIVE without a real, findable citation is MAJOR"; a citation
that points to the wrong page or wrong call is not findable AT the anchor
given, whatever the true location turns out to be).

Ironic pattern: the BALRAMCHIN and TRIVENI Jun_2026 errors sit inside the
exact citation family (Jun_2026 call, overcapacity/molasses evidence for Q4)
this run's rework claims to have independently re-verified "by page count."
The BALRAMCHIN case is a direct regression — the rework changed a citation
from p.11 to p.10, and p.11 was the page consistent with this task's own
"[page N] = PDF page N" definition.

## PART 2: CITED-ONLY SPOT-READ (rule 3)

**BALRAMCHIN special call (30-Apr-2026, filed "May_2026").** B06 marks it
CITED-ONLY, silent-period PLA/capital-raise call, no ethanol commercial
content. Not independently re-read in full this pass (B06's own framing —
silent period, explicit off-limits on business-performance questions — is
corroborated by BALRAMCHIN's Jun_2026 call opening, which treats the special
call as procedural). No material miss identified.

**BALRAMCHIN Q1 FY27 (Aug_2026).** B06 marks CITED-ONLY: "distillery margin
resilience from feedstock mix; no related-party, allocation-shock, or
private-OMC content found." Targeted re-read for "related party," "group
company," "private," "renege," "price cut," "OMC," "allocation," "maize,"
"ethanol margin" and "EBITDA...litre" found: a forward-looking exchange on
FY27 C-heavy vs. grain-route volume planning (Sanjay Manyal / Vivek Saraogi,
p.4-5) that touches capacity split but not allocation shortfall, margin per
litre, or related-party sourcing. This is industry-context adjacent, not a
directly claim-relevant miss — no MAJOR finding here; B06's CITED-ONLY
characterisation holds.

## PART 3: VERDICT-DISCIPLINE AUDIT PER CLAIM (rule 4-5)

| Claim (B05 peer_questions) | B06 verdict | Peer anchors used | Discipline check |
|---|---|---|---|
| Q1 allocation shortfall vs bid + disclosure timing | PARTIALLY VERIFIED | GULPOLY, BALRAMCHIN, TRIVENI (3) | Not a VERIFIED verdict; multi-peer anyway. Pass |
| Q2 private-OMC reneging / narrative consistency | UNVERIFIABLE | none found (3 checked, silent) | Correctly not upgraded past UNVERIFIABLE. Pass |
| Q3 maize margin at elevated prices | PARTIALLY VERIFIED | GULPOLY only (1), by the reworked check_peers scope | Single-peer basis explicitly self-flagged by B06 (Part 4 verdict-discipline note) and not upgraded to a stronger verdict than one peer supports. Pass — this is the one place a single anchor is used, and it is disclosed, not hidden |
| Q4 balanced demand-supply framing | CONTRADICTED | TRIVENI + BALRAMCHIN (2), corroborated by GULPOLY's allocation data | Multi-peer. Pass |
| Q5 related-party feedstock purchase share | UNVERIFIABLE | none found (3 checked, silent) | Correctly not upgraded. Pass |
| Q6 interest-subvention/PLI proportion of PBT | PARTIALLY VERIFIED | GULPOLY, BALRAMCHIN, TRIVENI (3), qualitative only | Multi-peer; correctly stops short of a magnitude verdict no peer's numbers support. Pass |

`verified: []` in the B06 YAML — zero VERIFIED claims this run, so rule 4's
">=2 anchors for VERIFIED" gate has no rows to fail. No verdict upgraded
from silence: Q2 and Q5 (the two questions where all three peers are silent
on the comparable disclosure) both correctly stay UNVERIFIABLE rather than
being read as tacit confirmation or denial.

All six peer_questions items received a verdict (rule 5). `claims_all_addressed: true`.

## FINDINGS

| Severity | Location | Claimed anchor | Actual anchor | Note |
|---|---|---|---|---|
| MAJOR | B06 Q1 net_read / peer_coverage_map, GULPOLY Q4 FY26/FY26 row | "PLI run-rate guided at 'about INR 30 crores per annum'...(GULPOLY-Concall_May_2026_Transcript.pdf, p.15)" | p.8 (same answer as the "INR 10 to INR 11" EBITDA/litre figure) | p.15 contains an unrelated demand-supply exchange with no PLI content. Off by 7 pages — the same magnitude of error the rework's own note (Part of REWORK NOTE item 4) says it caught and fixed elsewhere in this same document; this instance was missed |
| MAJOR | B06 peer_coverage_map, BALRAMCHIN Q4 FY26 (filed Jun_2026) row; also Q4 net_read | "Overcapacity acknowledgment (p.10, spoken by Pramod Patwari, corrected from Vivek Saraogi)"; "FY26 ethanol 27cr L vs 34-35cr L nameplate (p.10)" | `[page 11]` extraction marker (the document's own internal footer under that marker reads "Page 10 of 12," one page behind the extraction tag throughout the file) | Speaker correction (Pramod Patwari) is right and independently confirmed. Page anchor is wrong under this task's own "[page N] = PDF page N" rule. This is a regression: the rework changed this exact citation from p.11 (first run) to p.10 (this run), moving it further from the correct answer |
| MAJOR | B06 peer_coverage_map, TRIVENI Q4 FY26 (Jun_2026) row; Q5 net_read discussion in analyst framing | "TRIVENI's Jun_2026 call (p.14, Tarun Sawhney) discloses that its newly amalgamated Sir Shadi Lal unit produced no ethanol in FY26 and instead had its molasses used 'from our factory at Shamli at one of the other distilleries in the group'" | TRIVENI-Concall_**Aug_2026**_Transcript.txt, p.13 (extraction marker) — a different call | The quote is real and verbatim-correct ("there was no ethanol that was produced. And we used the molasses from our factory at Shamli at one of the other distilleries in the group," Tarun Sawhney). It is filed under the wrong quarter entirely: the Jun_2026 (Q4 FY26) transcript's only Sir Shadi Lal content is share-issuance record-date administrivia (p.8); the ethanol/molasses exchange is in the Aug_2026 (Q1 FY27) call. Searched "Shadi," "molasses," "amalgamat" across the full Jun_2026 file to confirm absence |
| MINOR | B06 Q3 net_read, GULPOLY Q1 FY27 row | "FY27 guidance held at consolidated EBITDA margin '10% to 11%' (p.4 and p.8)" | p.5 and p.8 | The p.8 citation ("EBITDA margins, we are guiding at about 10% to 11%") is exact. The second citation of the same guide figure ("consolidated level, we continue to target EBITDA margins of around 10 to 11%") is on p.5, not p.4; p.4 carries the adjacent "temporary pressure...second quarter" quote, which IS correctly anchored. One page off on a secondary, non-exclusive citation of a figure that is correctly anchored elsewhere in the same finding |

## OVERALL READ

The maker used the peers substantively and the content it drew out is real
— none of the quotes checked are fabricated content, and the two verdicts
that stay UNVERIFIABLE (Q2, Q5) are correctly not stretched past what
peer silence supports. The failure mode this pass surfaces is narrower and
more specific: three of ten SUBSTANTIVE citations point somewhere other
than where the material actually sits, and two of the three are inside the
same Jun_2026-call citation family the rework's own note claims to have
independently re-verified "by page count, not assumed." A verifier finding
a fresh instance of the exact error class a prior rework says it fixed is
itself worth naming as a process signal for /finalize: page-anchor
re-verification in this run was not exhaustive, and the Sir Shadi Lal
mis-filing (wrong CALL, not just wrong page) is a category the "by page
count" self-check would not have caught even if perfectly executed.

```yaml
stage: B12d
company: "TRUALT"
run_date: "2026-09-18"
model: claude-sonnet-5
status: complete
peers_audited: 12
substantive_confirmed: 7
substantive_unsupported:
  - "GULPOLY Q4 FY26/FY26 (May_2026) -- PLI Rs30cr/annum cited p.15, actual p.8"
  - "BALRAMCHIN Q4 FY26 (filed Jun_2026) -- overcapacity quote and 27cr L/34-35cr L nameplate cited p.10, actual extraction marker [page 11]"
  - "TRIVENI Q4 FY26 (Jun_2026) -- Sir Shadi Lal no-ethanol/Shamli-molasses quote cited to this call at p.14, actually in TRIVENI Aug_2026 (Q1 FY27) call p.13"
unused_but_relevant: []
claims_all_addressed: true
verdict_discipline_fails: []
findings:
  - {severity: "MAJOR", location: "B06 Q1 net_read / peer_coverage_map, GULPOLY Q4 FY26/FY26 row", claimed: "PLI ~INR30cr/annum, GULPOLY-Concall_May_2026 p.15", source_truth: "same quote at p.8", note: "off by 7 pages; p.15 has unrelated content"}
  - {severity: "MAJOR", location: "B06 peer_coverage_map, BALRAMCHIN Q4 FY26 (Jun_2026) row", claimed: "overcapacity quote + 27cr L/34-35cr L nameplate at p.10", source_truth: "extraction marker [page 11]", note: "rework regressed this citation from p.11 (first run) to p.10 (this run); p.11 is correct under the [page N]=PDF page N rule; speaker correction (Pramod Patwari) is independently confirmed right"}
  - {severity: "MAJOR", location: "B06 peer_coverage_map / Q5 discussion, TRIVENI Q4 FY26 (Jun_2026) row", claimed: "Sir Shadi Lal no-ethanol/Shamli-molasses quote, TRIVENI Jun_2026 p.14", source_truth: "TRIVENI Aug_2026 (Q1 FY27) call, p.13 -- different transcript entirely", note: "quote itself verbatim-correct; filed under the wrong quarter's call"}
  - {severity: "MINOR", location: "B06 Q3 net_read, GULPOLY Q1 FY27 (Aug_2026) row", claimed: "FY27 10%-11% guide, p.4 and p.8", source_truth: "p.5 and p.8", note: "secondary citation one page off; primary p.8 citation and the p.4 pressure quote are both correct"}
critical_count: 0
major_count: 3
minor_count: 1
acceptance_rate: 75
```
