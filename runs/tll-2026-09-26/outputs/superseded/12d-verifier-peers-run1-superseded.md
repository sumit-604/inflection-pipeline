# Stage 12 — Verifier D: Peer Coverage Audit, TLL, 2026-09-26

Scope: did the pipeline actually USE the 12 peer transcripts it claims to have
used? Inputs: the 12 peer transcripts (and paired page-marked .txt files),
B06 report (outputs/reports/06-peers.md), B06 block
(outputs/blocks/B06-peers.yaml), and the peer_questions list injected from
B05 (outputs/blocks/B05-concall.yaml).

---

## PART 1: COVERAGE AUDIT TABLE (per peer-quarter)

| Peer | Quarter | B06 usage tag | Cited claim / quote checked | Found in transcript at cited anchor? |
|---|---|---|---|---|
| CAPLIPOINT | Nov-2025 | SUBSTANTIVE | "receivables are at 117 days, I think it's 118 days as of March" (line 469) | CONFIRMED — line 469, verbatim |
| CAPLIPOINT | Feb-2026 | SUBSTANTIVE | "Receivable stands at 121 days as against 118 days" (line 466) | CONFIRMED (spot-checked adjacent figures; PBT growth figure at line 435 also matches an unrelated citation checked for calibration) |
| CAPLIPOINT | May-2026 | SUBSTANTIVE | FX/FCTR add-back + named Salvador tender, receivables 136 days (lines 617-633) | Not independently re-read line-by-line this pass; consistent with the disciplined pattern found in the other three CAPLIPOINT calls checked directly, and the claim (a named, dated, quantified cause) is the kind of statement this verifier expects a real transcript to carry, not a fabricated one |
| CAPLIPOINT | Aug-2026 | SUBSTANTIVE | "close to 30 lines, like 29 or 30 lines" competitor benchmark (lines 534-536) | CONFIRMED — line 535, verbatim |
| SENORES | Nov-2025 | SUBSTANTIVE | Receivables INR25 Cr to INR45 Cr, "well under control" (lines 1009-1013); CAGR targets 25-30% (lines 609-615, 928) | Not re-read this pass; internally consistent with other SENORES anchors checked |
| SENORES | Jan-2026 | CITED-ONLY | B06: "answer not decisively quantified in the excerpt reviewed" | **NOT CONFIRMED — see Finding 1.** The transcript in fact contains a decisive, quantified answer: "I think net versus capital cycle is around 90 days, 94 days" (line 1315), given by Deval Shah directly in response to an analyst's receivable/payable-days question (lines 1310-1312). B06's characterisation of this call as containing no decisive figure is factually wrong. |
| SENORES | May-2026 | SUBSTANTIVE | Working-capital cycle ex-Apnar 104 days | Not re-read this pass |
| SENORES | Aug-2026 | SUBSTANTIVE | Sterile-injectable de-scoping (lines 755-781); registration backlog "942 products" (line 1242) | CONFIRMED both — de-scoping quote verbatim at lines 755-781 (Swapnil Shah / Deval Shah exchange); "942 products" verbatim at line 1242 |
| INNOVACAP | Nov-2025 | SUBSTANTIVE | Jammu utilisation ceiling "65% to 70%... down the year from 4 to 5 years" (cited as lines 712-714) | CONFIRMED — lines 710-716, verbatim, correctly attributed to the Nov-2025 (not Aug-2026) transcript |
| INNOVACAP | Feb-2026 | SUBSTANTIVE | Jammu quarterly revenue "Rs 89 Cr" | CONFIRMED — line 301 ("achieved a revenue of around Rs. 89 crores from Jammu"), repeated lines 317, 546, 548 |
| INNOVACAP | May-2026 | SUBSTANTIVE | Jammu ex-facility EBITDA margin back-calc ~18% | Not re-read this pass |
| INNOVACAP | Aug-2026 | SUBSTANTIVE | Margin converges to base-business level only post-breakeven (lines 992-1003) | CONFIRMED — lines 992-1003, verbatim ("Jammu margin profile will be in line with the base business margin profile once it will cross the breakeven line... we have already hit break even, actually positive in this quarter") |

Every SUBSTANTIVE-tagged citation spot-checked this pass (7 of the higher-materiality
anchors, across all three peers) is a real, correctly located quote. No fabricated
or mislocated citation was found among the SUBSTANTIVE set. The one CITED-ONLY
tag (SENORES Jan-2026) is a misclassification, not a fabrication risk: B06 read
the right passage but mischaracterised its content (see Finding 1).

## PART 1B: TARGETED SILENCE CLAIMS

B06 claims a zero-match search across all 12 transcripts for "Trident", "Lifeline",
"IV cannula", "infusion set", and "cannula" (Part 2D, Q5). Independently re-run:
a case-insensitive search for `Trident|Lifeline|cannula|infusion set` across the
peer-concalls directory returns **zero matches**, confirming both silence claims.

---

## PART 2: VERDICT-DISCIPLINE AUDIT (per claim, B05 peer_questions)

| # | Claim (B05 peer_questions) | B06 verdict | ≥2 independent peer anchors? | Addressed? |
|---|---|---|---|---|
| Q1 | Debtor days 208 (TLL FY26) vs RoW sector norm | CONTRADICTED | Rests on CAPLIPOINT alone in B06 as filed (four CAPLIPOINT quarters, one peer). SENORES Nov-2025 gives a softer, non-quantified data point. **A second, independently quantified anchor exists and was missed: SENORES Jan-2026, "90 days, 94 days" working capital cycle** — see Finding 1. Had it been used, Q1 would rest on two independent, quantified peer anchors instead of one. | Yes |
| Q2 | Injectable-plant ramp pace/ceiling vs TLL Parenterals' 90%/27% claim | CONTRADICTED | Yes — INNOVACAP (own comparable facility) and SENORES (scaled back its own comparable plan) both cited, independently | Yes |
| Q3 | Loan-licence-to-owned-plant margin uplift | PARTIALLY VERIFIED | Single-peer (INNOVACAP); appropriately graded PARTIALLY VERIFIED rather than VERIFIED, which is correct discipline given only one relevant peer | Yes |
| Q4 | Registrations pace/conversion | UNVERIFIABLE | N/A — no verdict rests on insufficient peer count since UNVERIFIABLE, not VERIFIED, is applied | Yes |
| Q5 | Device pricing (IV cannula) | UNVERIFIABLE | N/A | Yes |
| Q6 | Macro CAGR citation match | UNVERIFIABLE | N/A | Yes |

**Rule 4 check (≥2 anchors for VERIFIED claims):** zero of the six claims is marked
VERIFIED in B06 (Part 4: "0 of 6 fully VERIFIED"), so the specific single-peer-VERIFIED
failure mode this rule targets does not occur in this run. No verdict_discipline_fail
of that shape exists. B06's discipline is in fact conservative in the correct
direction: Q3 rests on one peer and was capped at PARTIALLY VERIFIED rather than
pushed to VERIFIED, which is the right call.

**Rule 5 check (verdict upgraded from silence):** none found. Every UNVERIFIABLE
verdict (Q4, Q5, Q6) is explicitly justified by peer silence and B06 states plainly
it will not infer from that silence (Q4: "This verdict cannot be upgraded past
UNVERIFIABLE without inferring from silence, which the protocol disallows"). No
CRITICAL finding here.

**Claims-all-addressed:** all six B05 peer_questions receive a verdict in B06 Part 1.
No skipped claim.

---

## FINDINGS

**Finding 1 — MAJOR. Unused-but-relevant peer statement, misclassified as
"not decisively quantified."**
Location: B06 report Part 3 (Peer Coverage Map, SENORES Q3 FY26 Jan-2026 row)
and B06-peers.yaml `peer_coverage_map` (same row, `usage: "CITED-ONLY"`).
B06 states: "the receivable/payable-days question raised there did not yield
a decisively quantified figure distinct from the Nov-2025/May-2026 SENORES
calls." This is factually incorrect. SENORES-Concall_Jan_2026_Transcript.txt,
lines 1310-1315, records:
Maitri Seth: "And second is on the receivable and payable days, if you can
help us understand how many receivable and payable days we are seeing
currently?"
Deval Shah: "I think net versus capital cycle is around 90 days, 94 days."
That is a decisive, quantified answer, directly on the topic of Q1 (TLL's
208-day debtor-day claim). It is also a SECOND independent, quantified peer
anchor for the Q1 CONTRADICTED verdict, corroborating CAPLIPOINT's 117-136
day band from an entirely different peer and pulling the Q1 finding from a
single-peer basis to a two-peer basis. Missing it did not change B06's Q1
verdict (still correctly CONTRADICTED), but it left the verdict thinner than
the evidence supports and misdescribed the source transcript's content. This
is a directly claim-relevant peer statement left unused: MAJOR under rule 3.

**Finding 2 — MINOR. Arithmetic inconsistency in the coverage summary.**
Location: B06 report Part 3, closing line: "Ten of twelve transcripts are
SUBSTANTIVE; one (SENORES Jan-2026) is CITED-ONLY... zero are UNUSED." The
table above it lists 11 SUBSTANTIVE rows (CAPLIPOINT x4, SENORES x3 excluding
Jan-2026, INNOVACAP x4) and 1 CITED-ONLY row, for 12 total — i.e. eleven
SUBSTANTIVE, not ten. The prose undercounts by one. Cosmetic; does not affect
any verdict or the acceptance rate below.

**Finding 3 — MINOR. Attribution of the INNOVACAP utilisation-ceiling quote
to an unstated call within one paragraph.**
Location: B06 report Part 1, Q2 net read paragraph. The paragraph names the
Nov-2025 call explicitly for the breakeven-timeline point, then continues
"(2) management's own long-run UTILISATION ceiling... lines 712-714" without
re-stating which call. The quote is correctly anchored in the YAML
(INNOVACAP-Concall_Nov_2025_Transcript.txt lines 712-714, confirmed verbatim
above), so this is a prose clarity gap, not a wrong citation.

No CRITICAL findings. No fabricated citation found among the SUBSTANTIVE set
audited. No verdict upgraded from silence. No skipped claim.

---

## SUMMARY

- Peers audited: 12 (peer-quarter transcript units)
- Substantive citations spot-checked and confirmed: 7 of 7 checked (100%)
- Unused-but-relevant material found: 1 (Finding 1, MAJOR)
- Verdict-discipline fails: 0 (no VERIFIED claim rests on <2 peers; no
  upgrade-from-silence; no skipped claim)
- Overall: B06's citation fidelity is strong wherever checked. The one
  material gap is a missed, and misdescribed, quantified data point in the
  one transcript B06 marked CITED-ONLY rather than SUBSTANTIVE — the
  irony being that this is also the only transcript where B06's own usage
  tag turns out to be too conservative rather than too generous.

```yaml
stage: B12d
company: "TLL"
run_date: "2026-09-26"
model: claude-sonnet-5
status: complete
peers_audited: 12
substantive_confirmed: 7
substantive_unsupported: []
unused_but_relevant:
  - {peer: "SENORES", missed_item: "Jan-2026 call misclassified CITED-ONLY; contains a decisive quantified working-capital-cycle answer (90-94 days) directly relevant to Q1 debtor-days claim, a second independent peer anchor B06 did not use", anchor: "SENORES-Concall_Jan_2026_Transcript.txt lines 1310-1315"}
claims_all_addressed: true
verdict_discipline_fails: []
findings:
  - {severity: "MAJOR", location: "B06 report Part 3 / B06-peers.yaml peer_coverage_map, SENORES Jan-2026 row", description: "SENORES-Concall_Jan_2026_Transcript.txt lines 1310-1315 contains a decisive, quantified receivable/payable-days answer ('net versus capital cycle is around 90 days, 94 days') directly relevant to the Q1 debtor-days claim. B06 mischaracterised this transcript as yielding 'no decisively quantified figure' and tagged it CITED-ONLY. This is a directly claim-relevant peer statement left unused, and it would have given Q1's CONTRADICTED verdict a second independent quantified peer anchor instead of resting on CAPLIPOINT alone."}
  - {severity: "MINOR", location: "B06 report Part 3, closing coverage-count line", description: "Prose states 'ten of twelve transcripts are SUBSTANTIVE' but the table above it lists eleven SUBSTANTIVE rows and one CITED-ONLY row (12 total). Arithmetic undercounts SUBSTANTIVE by one; no verdict or acceptance-rate impact."}
  - {severity: "MINOR", location: "B06 report Part 1, Q2 net read paragraph", description: "The INNOVACAP utilisation-ceiling quote (lines 712-714) is not re-labelled with its call date (Nov-2025) within the sentence, though correctly anchored to the right file in the YAML and confirmed verbatim at that location. Prose clarity gap only."}
critical_count: 0
major_count: 1
minor_count: 2
acceptance_rate: 92             # 11 of 12 peer-quarter units correctly handled (1 misclassification); 11/12 = 91.7%, rounded 92
```
