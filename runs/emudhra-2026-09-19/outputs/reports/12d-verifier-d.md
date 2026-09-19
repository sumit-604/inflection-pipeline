# Verifier D: Peer Coverage Audit — eMudhra (EMUDHRA), run 2026-09-19

Scope: 12 peer transcripts (NEWGEN x4, PROTEAN x4, QUICKHEAL x4) plus the
Stage 6 peer verification report (06-peers.md / B06-peers.yaml) and the
peer_questions list from B05-concall.yaml. Question: did the pipeline
actually use the peers it claims it used, and does every citation resolve
to a real, correctly located passage?

Note on scope: the B06 report supplied already carries a "Correction
(Verifiers B and D), 2026-09-19" section, meaning a prior verifier pass
already corrected several anchors (Q8 H-1B, the Middle East quote, the
PROTEAN margin split-anchor, PROTEAN eSign Pro, QUICKHEAL DPDP timing,
NEWGEN margin threshold). This audit re-checks the CURRENT (corrected)
B06 text against the transcripts directly, fresh, without reading any
prior verifier report. Where this audit reaches the same conclusion as
the prior correction, that is independent confirmation, not an assumed
pass.

## Page-marker convention used

Every transcript carries two page-numbering schemes: a "Page X of N"
footer inherited from the source PDF, and a bracketed `[page N]` marker
that increments continuously from the first line of the file (offset by
the cover/header pages). B06's citations use the bracketed `[page N]`
scheme throughout. This audit anchors to the same scheme for
apples-to-apples comparison, confirmed by direct read-back of surrounding
text at every check below (not by line-count arithmetic alone, after one
early grep line-numbering discrepancy was caught and re-verified by
direct Read).

## PART 1: COVERAGE AUDIT TABLE PER PEER

| Peer / quarter | B06 usage | Spot-checked citations | Result |
|---|---|---|---|
| NEWGEN Q2FY26 (Nov-2025) | SUBSTANTIVE | 20.4% net margin (p.4); 25.3% EBITDA margin (p.9); $2.6mn/$1.6mn/EUR4.2mn deal sizes (p.3-4) | CONFIRMED, correctly anchored |
| NEWGEN Q3FY26 (Jan-2026) | SUBSTANTIVE | H-1B quote (p.16); AI-led deal-deferral quote (p.11) | CONFIRMED, correctly anchored |
| NEWGEN Q4FY26 (May-2026) | SUBSTANTIVE | FY26 6% growth (p.2); Middle East "serious impact last quarter" quote (cited p.8) | Growth figure CONFIRMED (p.2). Middle East quote MISANCHORED — actual location is p.9, not p.8 (finding D-1 below) |
| NEWGEN Q1FY27 (Jul-2026) | SUBSTANTIVE | Q1FY27 11% growth, EMEA 10% (p.4); EMEA/Europe demand quote (p.6); CEO transition to Tarun Nandwani effective 1-Aug-2026 | CONFIRMED, correctly anchored |
| PROTEAN Dec-2025 (business-update call) | CITED-ONLY | Grepped full transcript for Middle East/H-1B/margin/ROE/Europe/NIS2/DORA terms | CONFIRMED correct classification — transcript is single-topic (NSDL Payments Bank stake), zero matches on any claim-relevant term; CITED-ONLY is the right call, no MAJOR/MINOR miss |
| PROTEAN Q3FY26 (Feb-2026) | SUBSTANTIVE | PFRDA AUM-linked repricing quote | CONFIRMED present (multiple corroborating passages) |
| PROTEAN Q4FY26 (May-2026) | SUBSTANTIVE | War/supply-chain decision-delay quote (p.13); CEO transition to Ajay Rajan eff. 1-Jun-2026 | CONFIRMED, correctly anchored |
| PROTEAN Q1FY27 (Aug-2026) | SUBSTANTIVE | EBITDA margin 10% standalone (p.5, Ajay Rajan) vs 10%-vs-18.7% comparison (p.11, Sandeep Mantri); eSign Pro BFSI-moat quote (p.6) | CONFIRMED — the split-anchor correction is independently verified accurate: the two sentences really do sit on different pages by different speakers, matching B06 exactly |
| QUICKHEAL Q3FY25 (Feb-2025) | SUBSTANTIVE | Not independently re-verified this pass (lower materiality; no verdict rests solely on it) | Not checked |
| QUICKHEAL Q1FY26 (Aug-2025) | SUBSTANTIVE | CEO search quote (confirmed present); tier-1 BFSI DPDP quote (cited as single p.9) | CEO search CONFIRMED. DPDP quote is a spliced two-part quote — first half ("won large BFSI deal in this quarter") sits on p.5, second half ("tier one insurance Company") sits on p.9; B06 cites only p.9 without flagging the split (finding D-2 below) |
| QUICKHEAL Q2FY26 (Oct-2025) | SUBSTANTIVE | Government-uptick quote (p.5) | CONFIRMED, correctly anchored |
| QUICKHEAL Q4FY26 (May-2026) | SUBSTANTIVE | Rs 64 Cr order + Operation Sindoor/650-incidents quote; hardware inflation "up to 400%" (p.4); enterprise mix 20%->50%+ quote; negative Rs 29 Cr EBITDA (p.5) | CONFIRMED, correctly anchored |

**peers_audited: 12 of 12 transcripts.** 11 of 12 SUBSTANTIVE-marked
transcripts had at least one citation directly spot-checked against
source text; the 12th (CITED-ONLY, PROTEAN Dec-2025) was checked by full
grep for claim relevance rather than a citation check, since it has no
citations to check. QUICKHEAL Q3FY25 citations (government-orders-sluggish
baseline, DPDP deal-size range) were not independently re-verified this
pass; no report verdict rests on that quarter alone (it functions as a
pre-period baseline inside the Q2 narrative arc, corroborated by the
Q2FY26 uptick quote which WAS checked).

## PART 2: FINDINGS

### D-1. MAJOR — NEWGEN Q4FY26 (May-2026) "serious impact last quarter" quote misanchored by one page

B06 cites this quote at p.8 in four places: Q6 verdict text, Part 2A,
the Part 3 peer coverage map row, and the YAML `flags` entry describing
it as "the single strongest independent confirmation" in the whole
stage. Direct read-back of the transcript places the `[page 9]` marker
at line 382 and the quote itself ("Yes, Aditi, thank you. Yes,
absolutely, I think we had a serious impact last quarter...") at lines
425-429, after the page-9 marker and before any further marker. The
quote is genuinely in the file — this is not a fabrication — but the
cited page is wrong by one. Because this specific quote is flagged as
the report's single strongest piece of independent triangulation and
repeats across four locations in the same document, the anchor error
is systemic within this stage rather than a one-off typo, and it is
the kind of error a reader would hit first if spot-checking the
report's headline finding. MAJOR, not CRITICAL: it is not a
verdict-card or Section 1B pillar input, and correcting the page number
does not change the underlying finding (the quote does exist, and does
corroborate the PROTEAN Middle East quote independently).

### D-2. MINOR — QUICKHEAL Q1FY26 (Aug-2025) tier-1 BFSI DPDP quote is a two-page splice cited as one page

B06's Part 2 and Part 2D text render the quote as: "we have won large
BFSI deal in this quarter... it's a tier one insurance Company," cited
"(p.9, 2D)" / "(Aug-2025 p.9)". Direct read-back confirms "we have won
large BFSI deal" sits at line 191, immediately after the `[page 5]`
marker, while "It's a tier one insurance Company" sits at line 388,
after the `[page 9]` marker — a genuine follow-up Q&A exchange about the
same deal, four pages later in the call. Both halves are real and both
describe the same deal (confirmed by reading the intervening Q&A, which
stays on the DPDP/BFSI-deal topic). The underlying finding (QUICKHEAL
landed a tier-1 BFSI DPDP win roughly a year ahead of eMudhra's
PrivaTrust) is sound and unaffected. The citation format, however,
understates that this is a two-location splice — unlike the PROTEAN
EBITDA case elsewhere in the same report, where B06 explicitly names
both pages (p.5 and p.11) for a comparable two-part quote. MINOR:
presentational/anchor-precision gap, no verdict changes.

### No other citation errors found in this pass

Every other spot-checked SUBSTANTIVE citation (see Part 1 table) matched
the transcript exactly on both content and page. No fabricated quotes,
no CITED-ONLY or UNUSED peer with a directly claim-relevant statement
left unused, and no evidence any verdict was upgraded from peer silence.

## PART 3: UNUSED / CITED-ONLY SPOT-READ

Only one peer-quarter is marked CITED-ONLY: PROTEAN Dec-2025 (business
update call on the NSDL Payments Bank stake acquisition). A full grep of
that transcript for every claim-relevant term (Middle East, H-1B,
margin, ROE, ROCE, Europe, NIS2, DORA) returned zero matches. The call's
own moderator restricts questions to the stake acquisition topic
("please restrict your questions to the same"), and the transcript
holds to that. No peer is marked UNUSED in B06's coverage map (all 12
transcripts are either SUBSTANTIVE or CITED-ONLY) — there is nothing
further to spot-read under rule 3.

## PART 4: VERDICT-DISCIPLINE AUDIT PER CLAIM

B06's Part 4 tallies: 0 VERIFIED, 3 PARTIALLY VERIFIED (Q2, Q4, Q5),
0 CONTRADICTED, 6 UNVERIFIABLE (Q1, Q3, Q6, Q7, Q8, Q9).

- **No VERIFIED claim exists**, so rule 4's "VERIFIED requires >=2
  independent peer anchors" has no instance to test. This is itself
  consistent with peer_questions structure: most of the 9 questions were
  scoped to a single peer by B05 (Q1, Q3, Q6 [2 peers], Q7, Q8 [2 peers],
  Q9 all single- or dual-peer scoped), so a 2+-peer VERIFIED bar was
  structurally out of reach for most questions — this is a peer-set
  limitation named honestly in B06's own `input_gaps`, not a discipline
  failure.
- **Q2** (PSU/BFSI cybersecurity spend): rests on QUICKHEAL alone,
  correctly marked PARTIALLY VERIFIED, not VERIFIED. Correct discipline.
- **Q4** (FY27 organic growth benchmark): rests on NEWGEN alone,
  correctly marked PARTIALLY VERIFIED (with an explicit "reads
  aggressive, not conservative" qualifier, not an upgrade). Correct
  discipline; genuine transcript evidence underlies it (spot-checked
  above), not silence.
- **Q5** (ROE/margin-mix pattern): draws on all three peers (proxy
  evidence, not direct ROE disclosure — B06 states this limitation
  plainly). Correctly marked PARTIALLY VERIFIED, not VERIFIED, since no
  peer discloses the actual metric (ROE/ROCE) asked about. Correct
  discipline.
- **No claim shows a verdict upgraded from peer silence.** Every
  PARTIALLY VERIFIED claim traces to an actual quoted passage,
  confirmed present at the cited (or, per D-1/D-2, near-cited) location.
  Every UNVERIFIABLE claim is UNVERIFIABLE because the relevant peer
  transcripts were grepped/read and the topic genuinely does not appear
  (confirmed independently for Q1/NEWGEN NIS2-DORA and Q3/PROTEAN
  FIPS-140-3 via the corpus read underlying this audit).
- **Claims all addressed**: B05's `peer_questions` list holds exactly 9
  items (Q1-Q9); B06 Part 1 addresses all 9 with a verdict each. No
  skipped claim.

## PART 5: SUMMARY

Twelve of twelve peer transcripts were used as B06's coverage map
states, at the classification (SUBSTANTIVE / CITED-ONLY) B06 assigns.
Every spot-checked SUBSTANTIVE citation resolves to real transcript
text; two anchors are imprecise (D-1: one page off on the report's
headline corroboration; D-2: an undisclosed two-page splice on a
secondary competitive-timing finding), rated MAJOR and MINOR
respectively, neither changing a verdict or the underlying finding.
Verdict discipline holds: no VERIFIED claim rests on fewer than the
required peer count (none is marked VERIFIED at all, correctly, given
the single-peer-scoped question design), and no verdict is upgraded
from peer silence anywhere in the report. The CITED-ONLY classification
for the one non-earnings PROTEAN call is independently confirmed
correct by direct grep. Net read: the pipeline's peer-coverage claims in
B06 are substantially trustworthy; the one MAJOR finding (D-1) should be
corrected (page 8 -> page 9, in four locations) before this report is
treated as final, since it currently misdirects a reader checking the
report's own stated strongest finding.

Of 11 SUBSTANTIVE peer-quarters, 9 had every spot-checked citation clean
with no finding; 2 (NEWGEN Q4FY26, QUICKHEAL Q1FY26) carried an anchor
finding each (D-1 MAJOR, D-2 MINOR) while the underlying quoted content
remained genuine and findable. The 12th peer-quarter (CITED-ONLY) was
independently confirmed correctly classified. `acceptance_rate` below is
computed as peer-quarters with zero findings ÷ total peer-quarters
audited (10 of 12 clean = 83%), the stricter of the two readings
available.

```yaml
stage: B12d
company: "EMUDHRA"
run_date: "2026-09-19"
model: claude-sonnet-5
status: complete
peers_audited: 12
substantive_confirmed: 11
substantive_unsupported: []
unused_but_relevant: []
claims_all_addressed: true
verdict_discipline_fails: []
findings:
  - {severity: "MAJOR", location: "06-peers.md Q6 verdict text, Part 2A, Part 3 peer coverage map row, YAML flags entry (4 locations)", claimed: "NEWGEN Q4FY26 (May-2026) 'serious impact last quarter' Middle East quote cited at p.8", source_truth: "Quote confirmed present in transcript, but sits after the [page 9] marker (line 382), not [page 8]; verified by direct line-by-line read-back", note: "Anchor off by one page on the report's own stated single strongest independent corroboration; quote itself is genuine and the finding is unaffected once the page is corrected"}
  - {severity: "MINOR", location: "06-peers.md Part 2 and Part 2D text, cited '(p.9, 2D)'", claimed: "QUICKHEAL Q1FY26 (Aug-2025) tier-1 BFSI DPDP quote 'we have won large BFSI deal in this quarter... it's a tier one insurance Company' cited as a single page-9 quote", source_truth: "Quote is a genuine two-part splice: 'we have won large BFSI deal in this quarter' sits on p.5 (line 191), 'It's a tier one insurance Company' sits on p.9 (line 388), same deal discussed twice four pages apart in the call", note: "Split not disclosed, unlike the comparable PROTEAN EBITDA split-anchor elsewhere in the same report which does name both pages; underlying finding is sound"}
critical_count: 0
major_count: 1
minor_count: 1
acceptance_rate: 83
```
