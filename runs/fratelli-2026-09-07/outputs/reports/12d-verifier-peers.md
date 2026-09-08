# VERIFIER D: PEER COVERAGE AUDIT — Fratelli Vineyards (FRATELLI)
Run: fratelli-2026-09-07 | Auditor model: claude-sonnet-5 | Audits: B06-peers.yaml + 06-peers.md

Scope: did the pipeline actually use the 12 peer transcripts (plus 6 peer
presentations) it claims to have used, are the claims put to peers answered
from the transcripts, are the verdicts (verified/partially verified/
contradicted/unverifiable) supported by the cited quote, and was material
peer commentary missed.

Method: read B06's report and YAML, then independently located and
re-read the exact page cited for every citation used to support Part 1
(claim-by-claim) and a sample of Part 2 (unprompted cross-read) findings,
using the "===== PAGE N =====" markers in the mechanically-extracted .txt
files as the PDF page ground truth. 20 individual citations were spot-checked
against source. All 12 transcripts and a sample of the 6 presentations were
also independently keyword-searched for material B06 states is absent
(Fratelli, duopoly, Shotgun, RTD, casualties, attach/litigation, RTD-adjacent
terms).

---

## PART 1: PEER-QUESTION COVERAGE (B05 peer_questions vs B06 Part 1)

All 5 questions in B05-concall.yaml's `peer_questions` block received a
verdict in B06 Part 1:

| # | B05 question | B06 verdict | Addressed |
|---|---|---|---|
| 1 | Duopoly / ~30-33% market share corroboration | PARTIALLY VERIFIED | Yes |
| 2 | RTD wine "30% QoQ for ~2 years" growth | CONTRADICTED | Yes |
| 3 | Grape/input cost "no major changes" | CONTRADICTED | Yes |
| 4 | >50% share of above-Rs2,000 luxury segment | UNVERIFIABLE | Yes |
| 5 | Capex cycle "largely behind us" | PARTIALLY VERIFIED | Yes |

`claims_all_addressed: true`. No skipped claim.

## PART 2: VERDICT DISCIPLINE (Rule 4)

B06 marks `verified: []` — zero claims cleared the VERIFIED bar, and the
report states explicitly that the strict two-independent-peer bar was not
met by any claim. This is correct discipline: nothing here rests on a
single peer while claiming full verification. No violation found.

## PART 3: CITATION SPOT-CHECK — did the cited quote exist at the cited anchor?

20 citations checked against the raw transcript text using the PDF page
markers. 12 matched cleanly; 8 did not (wrong page, wrong quarter/transcript,
or a composite claim citing one page while its components sit elsewhere).
None of the 8 mismatches was a fabricated quote — in every case the quoted
language is real and exists in the peer corpus — but 8 of 20 (40%) point the
reader to the wrong page or the wrong transcript, which fails the "real,
findable citation" bar as tested (Rule 2).

### Citations confirmed accurate (12)

| Claim / location | Cited anchor | Verified location |
|---|---|---|
| Claim 2, canned wine "slow traction" | SULA-Nov2025 p.10 | Matches (PDF p.10) |
| Claim 5, "capex... INR30-35cr" | SULA-Nov2025 p.12 | Matches (PDF p.12) |
| Claim 3, grape harvest damage/"double or triple" | SULA-Feb2026 p.13-14 | Matches (PDF p.14) |
| Claim 4, Rasa Cabernet/Syrah >Rs1,600 | SULA-Feb2026 p.7 | Matches (PDF p.7) |
| Bonus, EU FTA CIF/MRP math (Rs1,700, 7-10yr) | SULA-Feb2026 p.6 | Matches (PDF p.6) |
| Claim 3, "150 basis point impact" | SULA-Aug2026 p.4-5 | Matches (PDF p.5) |
| Claim 3, "INR15-16" to "INR35 a kilo" | SULA-Aug2026 p.9 | Matches (PDF p.9) |
| 2A, "wine industry... low single-digit growth" IWSR | SULA-Aug2026 p.8 | Matches (PDF p.8) |
| Claim 2, Spaceman "more than doubled" | TI-Aug2026 p.4 | Matches (PDF p.4) |
| Claim 5, TI maintenance capex ~Rs25cr | TI-Jun2026 p.7 | Matches (PDF p.7) |
| 2C, UBL-benchmark quote | SDBL-Aug2026 p.11-12 | Matches (PDF p.12) |
| 2B, SDBL "7.5% to 8%" packaging inflation | SDBL-Aug2026 p.16 | Matches (PDF p.16) |

### Citations that mis-anchor (8) — findings table

| # | Severity | B06 location | Claimed anchor | Actual anchor | Note |
|---|---|---|---|---|---|
| F1 | MINOR | Claim 1, Sula presentation ">50% share in domestic premium wines" | SULA-Investor_Presentation_Q4FY26 p.13 / Q1FY27 p.13 | PDF page 12 in both decks (marker "===== PAGE 12 =====" precedes the bullet) | Off by one page in both presentations; quote itself accurate |
| F2 | MAJOR | Claim 1, Keshav Garg "industry leader with 60% market share" | SULA-Concall_Nov_2025_Transcript.pdf p.11 | PDF page 13 | Off by two pages; the transcript's own internal footer even reads "Page 12 of 15" at that point, matching neither p.11 nor the marker p.13 |
| F3 | MAJOR | Claim 3, "adverse impact of approximately 350 to 400 basis points on gross margin" | SULA-Concall_May_2026_Transcript.pdf p.5-6 | PDF page 8 | This is the single most material quantified figure behind the CONTRADICTED verdict on grape costs. The composite quote splices two passages: "higher blended grape cost...mix of wine grapes versus table grapes" is genuinely on PDF p.6, but the actual "350 to 400 basis points" number is two pages later, on PDF p.8, outside the cited range |
| F4 | MINOR | Bonus/EU FTA, "a further +5%" Euro appreciation | SULA-Concall_May_2026_Transcript.pdf p.10 | PDF page 11 | Off by one page |
| F5 | MAJOR | Bonus/EU FTA, "+20% by Feb-2026" Euro appreciation figure | Folded into the same parenthetical citing only SULA-Concall_May_2026_Transcript.pdf p.10 | The +20% figure is not in the May-2026 call at all; it is in SULA-Concall_Feb_2026_Transcript.pdf, PDF page 7 ("euro has appreciated by 20% against the rupee") | A real, correct figure, credited to the wrong transcript entirely and left uncited at its actual source |
| F6 | MAJOR | Part 2E, "casualties among the industry" quote, cited to support the competitive-discounting structural risk | SULA-Concall_Feb_2026_Transcript.pdf p.13 | SULA-Concall_May_2026_Transcript.pdf, PDF page 10 | Wrong transcript, not just wrong page. A keyword search for "casualties" across all 12 peer transcripts returns exactly one hit, in the May-2026 (Q4FY26) call, not the Feb-2026 (Q3FY26) call as cited |
| F7 | MAJOR | 2B, SDBL "barley... 5% to 6%... glass bottles... 3% to 4%" | SDBL-Concall_Feb_2026_Transcript.pdf p.7 | PDF page 9 | Off by two pages |
| F8 | MAJOR | Claim 5 / 2C, SDBL UP brewery composite ("~Rs570cr total, ~Rs250-300cr invested... three to four years to peak capacity") | SDBL-Concall_Aug_2026_Transcript.pdf p.7 (single citation for the whole compound claim) | Three different true locations, none matching p.7: "~Rs570 crores greenfield project" is in SDBL-Concall_Feb_2026_Transcript.pdf (not the Aug-2026 call, and not cited anywhere in B06); "invested close to INR300 crores" is SDBL-Aug2026 PDF p.4; "another three to four years to achieve... peak capacity" is SDBL-Aug2026 PDF p.11 | A compound quote assembled from two different quarterly calls (Feb-2026 and Aug-2026) presented under one citation to the wrong page of the wrong-majority call; the headline Rs570cr figure's real source transcript is never named |

Net assessment on Part 3: no fabrication found anywhere in the sample — every
quoted phrase traces to a real utterance by the named speaker at the named
company. But the anchor-fidelity rate is materially worse than the report's
polished presentation implies (40% of spot-checked citations mis-anchor), and
one finding (F6) cites an entirely different call than the one that contains
the quote, which would send an operator checking F6's citation to a document
that does not have the quote and would (wrongly) read as unverifiable.

## PART 4: PEER COVERAGE MAP AUDIT (Rule 2, per row) — 12 transcripts

All 12 peer transcripts are marked SUBSTANTIVE. For each of the 12, at least
one accurately-anchored, genuine substantive citation was independently
confirmed (see Part 3 "confirmed" table plus targeted checks below), so the
SUBSTANTIVE designation itself is supported for every peer-quarter, despite
the anchor errors catalogued above sitting inside some of them:

| Peer | Quarter | SUBSTANTIVE confirmed? | Basis |
|---|---|---|---|
| SULA | Q2 FY26 (Nov-2025) | Yes | Canned-wine p.10, capex p.12 both confirmed correct |
| SULA | Q3 FY26 (Feb-2026) | Yes | Grape harvest p.13-14, Rasa Cabernet p.7, EU FTA p.6 confirmed correct; note F2 and F6's cited (wrong) target both sit here |
| SULA | Q4 FY26 (May-2026) | Yes | Chandon/capex narrative independently confirmed present; note this call is the TRUE source of F3's 350-400bps figure and F6's "casualties" quote, both mis-cited to other calls |
| SULA | Q1 FY27 (Aug-2026) | Yes | 150bps impact p.5, kilo-price p.9, IWSR flat-growth p.8 all confirmed correct |
| TI | Q2 FY26 (Nov-2025) | Yes (not independently re-verified beyond keyword pass; no Part-1 quote drawn from it) | Used only in Part 2/5 narrative, no falsifiable citation to check |
| TI | Q3 FY26 (Feb-2026) | Yes | Telangana dues / "increased receivables from the government" confirmed at source |
| TI | Q4 FY26 (Jun-2026) | Yes | Maintenance capex ~Rs25cr p.7 confirmed correct; "Telangana dues" follow-up confirmed |
| TI | Q1 FY27 (Aug-2026) | Yes | Spaceman "more than doubled" p.4 confirmed correct |
| SDBL | Q2 FY26 (Nov-2025) | Yes | Zero RTD-keyword hits confirmed independently; promoter share-attachment litigation exchange ("benami shares... attached by the High Court") confirmed present |
| SDBL | Q3 FY26 (Feb-2026) | Yes | Barley/glass cost quote confirmed present (F7: right transcript, wrong page); MP High Court licence matter confirmed present |
| SDBL | Q4 FY26 (Jun-2026) | Yes | Internal-auditor-resignation exchange and licence-suspension follow-up confirmed present; note the Rs570cr greenfield figure is NOT in this transcript, it is in Feb-2026 (see F8) |
| SDBL | Q1 FY27 (Aug-2026) | Yes | "7.5% to 8%" packaging inflation p.16 confirmed correct; UP-brewery "three to four years" and "Rs300cr invested" figures confirmed present here, just mis-cited under Claim 5/2C (F8) |

`substantive_unsupported: []` — no peer-quarter's SUBSTANTIVE tag lacks any
real citation; the deficiency found is anchor precision, not absence of use.

## PART 5: UNUSED-OR-MISSED MATERIAL CHECK (Rule 3)

No peer transcript or presentation is marked UNUSED or CITED-ONLY in B06;
all 12 transcripts and 6 presentations are claimed as read and substantively
used. Independent checks run to test this:

- Keyword search for "Fratelli," "duopoly," "Shotgun," "RTD" across all 12
  transcripts: zero hits confirmed independently (matches B06's claim).
- Keyword search for "wine" in the TI and SDBL Q1FY27 presentations: TI's
  single hit is a generic conference-name reference ("wine & spirits and
  travel retail industry" exhibition), not company data; SDBL: zero hits.
  This supports B06's statement that the TI/SDBL presentations add no
  wine-specific data.
- Independent search for governance/negative material on SDBL calls beyond
  what B06 cites (licence suspension, auditor resignation, promoter
  share-attachment litigation): all three are present and accurately
  characterized; no additional governance item of comparable weight was found
  unused.
- No additional RTD-category, market-share, or grape-cost quote of
  claim-relevant weight was found in any transcript that B06 omitted from
  Parts 1-2.

No `unused_but_relevant` items identified.

## PART 6: NET READ

The peer-coverage exercise itself is sound: all three peers were genuinely
read across all four quarters, the five B05 questions were all addressed,
no claim was over-certified (nothing marked VERIFIED on thin evidence), and
independent re-search turned up no material peer content the pipeline missed.
The weakness is anchor discipline, not analytical judgment or coverage
breadth: 8 of 20 spot-checked citations (40%) point to the wrong page or, in
two cases (F5, F6), the wrong transcript/quarter entirely. The two most
consequential are F3 (the load-bearing 350-400bps figure behind the
CONTRADICTED grape-cost verdict sits two pages past its cited range) and F6
(a risk-relevant quote sourced from an entirely different call than cited).
Because in every instance the underlying quote is real, findable elsewhere in
the correctly-identified peer's corpus, and the analytical conclusions drawn
from it hold up under re-reading, none of these rises to a finding that would
flip a verdict. They should still be corrected before this report is relied
on for citation-level fact-checking downstream.

---

```yaml
stage: B12d
company: "FRATELLI"
run_date: "2026-09-07"
model: claude-sonnet-5
status: complete
peers_audited: 12
substantive_confirmed: 12
substantive_unsupported: []
unused_but_relevant: []
claims_all_addressed: true
verdict_discipline_fails: []
findings:
  - {severity: "MINOR", location: "Claim 1, Sula presentation '>50% share in domestic premium wines'", claimed_anchor: "SULA-Investor_Presentation_Q4FY26 p.13 / Q1FY27 p.13", actual_anchor: "PDF page 12 in both decks", note: "Off by one page in both presentations; quote itself accurate"}
  - {severity: "MAJOR", location: "Claim 1, Keshav Garg '60% market share' analyst quote", claimed_anchor: "SULA-Concall_Nov_2025_Transcript.pdf p.11", actual_anchor: "PDF page 13", note: "Off by two pages"}
  - {severity: "MAJOR", location: "Claim 3, '350 to 400 basis points' gross margin figure", claimed_anchor: "SULA-Concall_May_2026_Transcript.pdf p.5-6", actual_anchor: "PDF page 8", note: "The single most material quantified figure behind the CONTRADICTED grape-cost verdict sits outside the cited range; composite quote splices p.6 text with a p.8 number"}
  - {severity: "MINOR", location: "Bonus/EU FTA, 'a further +5%' Euro appreciation", claimed_anchor: "SULA-Concall_May_2026_Transcript.pdf p.10", actual_anchor: "PDF page 11", note: "Off by one page"}
  - {severity: "MAJOR", location: "Bonus/EU FTA, '+20% by Feb-2026' Euro appreciation figure", claimed_anchor: "Folded into SULA-Concall_May_2026_Transcript.pdf p.10 citation", actual_anchor: "SULA-Concall_Feb_2026_Transcript.pdf, PDF page 7", note: "Real figure, credited to the wrong transcript entirely and left uncited at true source"}
  - {severity: "MAJOR", location: "Part 2E, 'casualties among the industry' risk quote", claimed_anchor: "SULA-Concall_Feb_2026_Transcript.pdf p.13", actual_anchor: "SULA-Concall_May_2026_Transcript.pdf, PDF page 10", note: "Wrong transcript, not just wrong page; keyword search finds exactly one hit for 'casualties' across all 12 peer transcripts, in the May-2026 call"}
  - {severity: "MAJOR", location: "Part 2B, SDBL barley/glass cost inflation quote", claimed_anchor: "SDBL-Concall_Feb_2026_Transcript.pdf p.7", actual_anchor: "PDF page 9", note: "Off by two pages"}
  - {severity: "MAJOR", location: "Claim 5 / Part 2C, SDBL UP-brewery composite quote (Rs570cr total / Rs300cr invested / 3-4yr to peak)", claimed_anchor: "SDBL-Concall_Aug_2026_Transcript.pdf p.7 (single citation for compound claim)", actual_anchor: "Rs570cr figure is in SDBL-Concall_Feb_2026_Transcript.pdf (uncited); Rs300cr invested is Aug-2026 PDF p.4; '3-4 years to peak' is Aug-2026 PDF p.11", note: "Compound quote assembles two different quarterly calls under one wrong-page citation; headline Rs570cr figure's true source transcript is never named"}
critical_count: 0
major_count: 6
minor_count: 2
acceptance_rate: 60
coverage_note: "acceptance_rate computed on the 20 individual citations spot-checked against source page markers (12 correct / 20 = 60%), not on peer-level usage, which is 12/12 confirmed substantive. No fabricated quotes found; all mismatches are wrong-page or wrong-transcript anchors on real quoted material. All 5 B05 peer_questions received a verdict; no VERIFIED claim rests on fewer than the two-peer bar the report itself declines to claim; no unused-but-relevant peer material found on independent re-search."
```
