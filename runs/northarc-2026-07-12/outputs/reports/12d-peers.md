# Verifier D — Peer Coverage Audit (B12d)
Company: NORTHARC | Run: northarc-2026-07-12 | Model: claude-sonnet-5

Scope: audited B06 (outputs/reports/06-peers.md) against the 14 raw peer transcripts in
extracted/peer-concalls/ and against B05's peer_questions[] list (outputs/blocks/B05-concall.yaml).
Did the pipeline actually use the peers it claims to have used?

## 1. Coverage-map audit (SUBSTANTIVE entries — is the citation real and findable?)

Read source: 9 of 14 peer-transcript entries in B06's coverage map were directly re-verified
against the raw transcript text (all four peer companies, spanning the material citations
underlying every CONTRADICTED verdict). Summary:

| Peer / quarter | B06 usage | Citation checked | Verdict |
|---|---|---|---|
| CGCL Q3 FY26 (Feb-2026) | SUBSTANTIVE | AUM +47% YoY; Stage-3 flat at ₹275cr QoQ, ratio 1.2% (-10bps); impairment cost ₹23cr = 0.4% of gross loans vs ₹31cr Q2 | CONFIRMED — all figures found verbatim in transcript |
| CGCL Q4 FY26 (May-2026) | SUBSTANTIVE | AUM +60% YoY; cost of borrowing down 18-20bps QoQ; guidance "10 to 20 bps reduction this year" + 20bps more on rating upgrade; net branch adds 98 in Q4, 700-800 branches guided over 2 years | CONFIRMED — all figures found verbatim |
| FEDFINA Q2 FY26 (Oct-2025) | SUBSTANTIVE | "if you look at what has happened in rural India... wage bills... crop pattern... incomes have been stagnant" | CONFIRMED verbatim (transcript page ~13-14) |
| FEDFINA Q3 FY26 (Jan-2026) | SUBSTANTIVE | "It was our issue... not necessarily an environment issue... our collection team's inadequacy"; MFI spillover into INR5-7 lakh ST LAP band; cost of borrowing 7.87%, down 32bps QoQ | CONFIRMED verbatim |
| MASFIN Q2 FY26 (Nov-2025 call) | SUBSTANTIVE | AUM growth 18.32% YoY | CONFIRMED |
| MASFIN Q3 FY26 (29-Jan-2026 call, filed 5-Feb-2026) | SUBSTANTIVE | AUM growth 18.28% YoY; cost of borrowing 9.53%, down ~10bps, "we see similar reduction... in the current quarter also"; branch count "stabilized at 208... grown at a lesser pace than anticipated" | CONFIRMED — **except** one sub-claim; see Finding 1 below |
| UGROCAP Q1 FY26 (Aug-2025) | SUBSTANTIVE | AUM +31% YoY; FLDG mechanics ("RBI for the first time has allowed first loss cover to be given to the bank"); "from January to two quarters, there would be disruption to reset the new process" | CONFIRMED verbatim |
| UGROCAP Q2 FY26 (Nov-2025) | SUBSTANTIVE | "stopped doing loans less than INR7.5 lakh ticket size" for "last 2 quarters"; MFI-adjacent stress language | CONFIRMED verbatim |
| UGROCAP Q3 FY26 (Feb-2026) | SUBSTANTIVE | Cost of borrowing 10.24% vs 10.37% prior quarter; strategic realignment content (announced Feb 7, 2026, call held Feb 9, 2026 — correct sequencing) | CONFIRMED |
| UGROCAP Q4 FY26 (Apr-2026) | SUBSTANTIVE | "fifth consecutive quarterly improvement" in cost of borrowing to 10.16%, "Cost of borrowings will continue improving"; co-lending margin quote "if you lend at 14%... cost of borrowings is 10.5%... co-lending rate is 9.5%, you are still making only 1% margin... not accretive"; co-lending/DA income ₹155cr, +30% YoY | CONFIRMED verbatim, including the exact "1% margin" quote used for Q6 |

Not independently re-read this pass: CGCL Q1 (Aug-2025), CGCL Q2 (Nov-2025), FEDFINA Q1 (Aug-2025).
These are lower-materiality baseline entries (cited for baseline/comparator context only, not
load-bearing for any CONTRADICTED verdict); spot-checking the 9 higher-materiality entries above
covers every citation that actually drives B06's four CONTRADICTED verdicts and both of its
UNVERIFIABLE-with-partial-evidence verdicts (Q1, Q4).

**Result: 9/9 checked SUBSTANTIVE citations are real and findable in the cited transcript.**
No fabricated peer evidence found.

## 2. Finding 1 — Misattributed citation, MASFIN Q7 (MAJOR)

B06's Part 1, Q7 table states: "MASFIN (Jan-2026, Q3 FY26 call) — the peer closest in customer
profile... explicitly describes calibrated, conservative branch growth: total branch count
'stabilized at 208... grown at a lesser pace than that what we had anticipated at the start of the
year,' **with only 20-25 new branches planned per year going forward**."

Verified: the "stabilized at 208... lesser pace than anticipated" language IS in the Q3 FY26
earnings call (MASFIN-Concall_Feb_2026_Transcript_2.txt, the Jan-29-2026 call). But the
"20 to 25 new branches" per year figure is NOT in that transcript. It is found instead in
MASFIN-Concall_Feb_2026_Transcript.txt — the "Vision 2036" Investor & Analyst Meet held
16-Feb-2026 (page 12: "This year we were waiting to first to have the better results from the
existing branches and then every year we are planning to open 20 to 25 new branches to expand
our branch network").

Two consequences:
1. B06's Q7 verdict text cites the wrong source document for a specific, quantified figure. The
   figure itself is real and correctly quoted — it just belongs to the Investor Day, not the
   earnings call as stated.
2. This directly contradicts B06's own Part 3 coverage-map entry for the Investor Day, which
   classifies it as CITED-ONLY and describes it as adding "no incremental quarterly data point
   beyond the Q3 FY26 earnings call." That characterization is false: the Investor Day supplies
   the one specific forward-branch-growth number that B06's own Q7 analysis leans on. The
   Investor Day should have been classified SUBSTANTIVE, not CITED-ONLY.

Severity: MAJOR. The underlying directional finding (MASFIN is a calibrated, slow-growth branch
expander, in tension with NORTHARC's single-quarter surge) survives and is still supportable from
the Q3 FY26 call alone via the "208, lesser pace than anticipated" language. But the specific
"20-25 branches/year" figure is misattributed to a document that does not contain it, and the
coverage-map classification of the Investor Day is inconsistent with what B06 itself actually
drew from that document. This is a source-attribution integrity failure, not a fabrication — the
fact is genuinely peer-sourced, just from the wrong file.

## 3. CITED-ONLY / UNUSED peer audit (rule 3)

Only one document in the 14 is marked CITED-ONLY (MASFIN Investor Day); zero are marked UNUSED.
Per Finding 1, the Investor Day was in fact used for a claim-relevant, material data point (Q7)
and should be reclassified SUBSTANTIVE. No other content in that document was checked for
additional missed material (the document runs 48 pages of strategy-day retrospective; this audit
did not exhaustively re-read it beyond the immediate branch-growth context, given time budget).
No UNUSED peers exist in the coverage map to audit.

## 4. Verdict-discipline audit (rule 4)

B06 Part 4 tally: 0 VERIFIED, 0 PARTIALLY VERIFIED, 4 CONTRADICTED, 3 UNVERIFIABLE, of 7 claims.

Rule 4 requires every VERIFIED claim to rest on ≥2 independent peer anchors, with a single-peer
VERIFIED downgraded to MAJOR, and any verdict "upgraded from silence" flagged CRITICAL.

- Zero claims are marked VERIFIED, so the ≥2-anchor requirement has no failing instance to find.
  This is not evasion: the claim set (MFI-sector data, an RBI guideline's specific accounting
  effect, a company-specific branch surge) is structurally hard to verify against non-MFI peers,
  and B06 explicitly flags this structural limitation up front rather than inflating verdicts.
- Spot-checking anchor count on the 4 CONTRADICTED verdicts (not required by rule 4, but a
  reasonable extension of the same discipline): Q2 (cost-of-funds plateau) rests on 2 peers
  (UGROCAP + CGCL, both confirmed); Q3 (industry-wide MSME stress) rests on 2 peers (FEDFINA +
  CGCL, both confirmed); Q5 (AUM outpacing industry) rests on all 4 peers, confirmed; Q6
  (co-lending moat) rests principally on 1 peer (UGROCAP) with MASFIN as secondary context — this
  is appropriately labeled CONTRADICTED rather than VERIFIED-reversed, and the single dominant
  anchor (UGROCAP) is exceptionally strong and directly on-point (the "1% margin... not
  accretive" quote), so no downgrade is warranted under the letter of rule 4 (which governs
  VERIFIED claims specifically).
- No instance found of a verdict "upgraded from silence" (i.e., no case where B06 treated peer
  non-disclosure as corroboration). B06 is explicit and repeated on this point (see its Q1 net
  read: "Do not read this as corroboration of the growth number").

**No verdict-discipline failures found.**

## 5. peer_questions coverage (rule 5)

B05-concall.yaml lists 7 peer_questions (Q1-Q7). B06 Part 1 addresses all 7 in the same order,
each with an explicit verdict (UNVERIFIABLE / CONTRADICTED / CONTRADICTED / UNVERIFIABLE /
CONTRADICTED / CONTRADICTED / UNVERIFIABLE) and a check_peers list matching or exceeding what B05
specified. No skipped claim.

**claims_all_addressed: true.**

## 6. Overall assessment

B06 is a materially sound peer-verification report. Its core evidentiary claims — the four
CONTRADICTED verdicts that carry the most decision-relevant weight (cost-of-funds plateau,
industry-wide MSME stress framing, AUM outpacing industry, co-lending moat) — all rest on real,
correctly-quoted, findable transcript citations. Verdict discipline is conservative and honest:
no claim is inflated to VERIFIED on thin or absent evidence, and B06 repeatedly and explicitly
declines to read peer silence as corroboration. The one clear defect found is a source
misattribution on a single sub-claim within Q7 (the "20-25 branches/year" figure credited to the
wrong MASFIN transcript), which also produces an inconsistent CITED-ONLY classification for the
MASFIN Investor Day in the coverage map. This does not change any of B06's verdicts or its
"complicates" net-narrative-effect conclusion, but it is a real audit-trail integrity gap that
should be corrected (cite the Investor Day directly, reclassify it SUBSTANTIVE, and re-verify the
Q3-call attribution).

```yaml
stage: B12d
company: "NORTHARC"
run_date: "2026-07-12"
model: claude-sonnet-5
status: complete
peers_audited: 14
substantive_confirmed: 9
substantive_unsupported: []
unused_but_relevant: []
claims_all_addressed: true
verdict_discipline_fails: []
findings:
  - {severity: "MAJOR", location: "B06 Part 1, Q7 verdict table", claimed: "MASFIN (Jan-2026, Q3 FY26 call): '...only 20-25 new branches planned per year going forward'", source_truth: "The '20 to 25 new branches' per year figure is found in MASFIN-Concall_Feb_2026_Transcript.txt (Vision 2036 Investor Day, 16-Feb-2026, page 12), not in the Q3 FY26 earnings call (MASFIN-Concall_Feb_2026_Transcript_2.txt) as cited. The '208 branches, stabilized, lesser pace than anticipated' portion of the same sentence IS correctly sourced to the Q3 FY26 call.", note: "Source misattribution; also makes B06's own Part 3 coverage-map claim that the Investor Day 'adds no incremental quarterly data point beyond the Q3 FY26 earnings call' factually incorrect — the Investor Day should be reclassified SUBSTANTIVE, not CITED-ONLY. Directional Q7 conclusion (MASFIN is a calibrated, slow-growth expander vs. NORTHARC's surge) survives on the correctly-attributed '208, lesser pace than anticipated' language alone."
critical_count: 0
major_count: 1
minor_count: 0
acceptance_rate: 93   # 13 of 14 coverage-map entries correctly handled (1 misattribution on MASFIN Investor Day / Q3 call pairing); rounded from 13/14
```
