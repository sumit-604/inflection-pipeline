# STAGE 12d — VERIFIER D: PEER COVERAGE AUDIT
TAAL Tech Ltd (TAALTECH) | Run date 2026-09-10

Scope: audit whether the pipeline's peer verification stage (B06,
`outputs/reports/06-peers.md`) actually used the 11 peer transcripts it
claims to have used, whether its quotes and figures are correctly
anchored, and whether all six handed-over peer_questions (from B05)
received a real, worked verdict. I read the 11 raw transcripts myself
and compared them against B06's citations. I hold no view on TAAL Tech
itself; findings below are confined to B06's handling of the peer
evidence.

---

## 0. FILE IDENTITY CHECK

I confirmed each transcript's company, quarter, and call type from its
own first two pages against B06's own confirmation table. All 11 match
what B06 claims:

| File | Confirmed | B06 claim | Match |
|---|---|---|---|
| TATAELXSI-Concall_Jan_2026 | Q3 FY26 call, held 13-Jan-2026 | same | YES |
| TATAELXSI-Concall_Apr_2026 | Q4 FY26 call, held 21-Apr-2026 | same | YES |
| TATAELXSI-Concall_Jul_2026 | Q1 FY27 call, held 14-Jul-2026 | same | YES |
| CYIENT-Concall_Apr_2026 | Q4 FY26 results call, 23-Apr-2026 | same | YES |
| CYIENT-Concall_Jun_2026 | "Acquisition of TAO Digital" special call, 01-Jun-2026 | same, NOT a quarterly call | YES |
| CYIENT-Concall_Jun_2026_2 | "Semiconductor Strategic Financing Transaction and Growth Roadmap" (Cyient Semiconductors), 26-May-2026, filed 01-Jun-2026 | same | YES |
| CYIENT-Concall_Aug_2026 | Q1 FY27 results call, held 23-Jul-2026, filed 30-Jul-2026 | same | YES |
| ONWARDTEC-Concall_Oct_2025 | Q2 FY26 call, held 17-Oct-2025 | same | YES |
| ONWARDTEC-Concall_Jan_2026 | Q3 FY26 call, held 16-Jan-2026 | same | YES |
| ONWARDTEC-Concall_May_2026 | Q4 FY26 call, held 05-May-2026 | same | YES |
| ONWARDTEC-Concall_Jul_2026 | Q1 FY27 call, held 16-Jul-2026 | same | YES |

B06 correctly identifies the two Cyient special calls as non-quarterly
(M&A and financing calls respectively) rather than treating them as
missing quarterly coverage. This part of B06's own methodology note is
accurate.

---

## 1. UTILISATION — WAS EACH TRANSCRIPT ACTUALLY MINED?

B06's coverage map (Part 3) claims 9 SUBSTANTIVE, 1 CITED-ONLY, 1 UNUSED.
I spot-read every file and traced the specific citations back to their
source text.

| Peer file | B06 marking | My check | Verdict |
|---|---|---|---|
| TATAELXSI Jan 2026 | SUBSTANTIVE | 3.2% QoQ CC / "volume-led" (p.3, confirmed marker PAGE 3), "headwinds are still there" / "Times are still tough" (p.6-7, confirmed spans marker PAGE 6-7), "pent-up demand" framing (real quote, but see §2 anchor note) | Confirmed substantive, real citations |
| TATAELXSI Apr 2026 | SUBSTANTIVE | 0.9% QoQ CC, Healthcare -13.1%, 73% utilisation, 27% PBT aspiration, "not seeing irrationality," APAC/US wins, Terumo ODC — all confirmed present in transcript (page anchors imprecise in several places, §2) | Confirmed substantive |
| TATAELXSI Jul 2026 | SUBSTANTIVE | 1.3% QoQ / 6.5% YoY CC, Rs1,000cr milestone, Chapter 11 provisioning, "just above 75%" utilisation, Sky (Europe) "30% to 70% efficiencies," "a little moderated" Europe — all confirmed present | Confirmed substantive |
| CYIENT Apr 2026 | SUBSTANTIVE | -2.4% QoQ CC DET degrowth, "downward variance," Strategic Units -12.4% QoQ, West Asia deferral, price-increase quote, FCF/PAT 163%, T&M +13.2% YoY — all confirmed present | Confirmed substantive |
| CYIENT Jun 2026 (TAO Digital) | CITED-ONLY | Confirmed: this call is M&A strategy content only (deal terms, TAO capabilities, TAM reframe). No quarterly demand/margin/DSO data exists in it, matching B06's own characterisation. Used once, for the AI/TAM figure in Q6 and Part 5 — but that one figure is itself inflated, see §2 finding 1 | CITED-ONLY classification correct; the one citation drawn from it is inaccurate |
| CYIENT Jun 2026_2 (Semiconductor financing) | UNUSED | Confirmed: entirely about Cyient Semiconductors' external funding round, valuation methodology, and product roadmap. No ER&D services demand/margin/DSO/concentration content. One tangential item not used: an explicit "AI data center power" TAM/thesis passage (pp.3-4) that would have reinforced B06's own Part 5 cross-peer hypothesis about AI-infrastructure-adjacent demand — see §3 | UNUSED classification is justified; one MINOR miss |
| CYIENT Aug 2026 | SUBSTANTIVE | -0.5% QoQ CC DET degrowth, Strategic Units -8.2% QoQ, T&M +14.8% YoY, FCF/PAT 80.5% "consistent with prior years," "some slowness in awarding of discretionary projects" — all confirmed present | Confirmed substantive |
| ONWARDTEC Oct 2025 | SUBSTANTIVE | DSO 73 days ("includes both billed and unbilled"), headcount 2,525 flat with revenue Rs100cr->Rs500cr, India Rs500/hr vs export $18/hr, "speed I've never seen before" — all confirmed present. This file ALSO contains the source of a quote B06 misattributes to a different call, see §2 finding 2 | Confirmed substantive, but see misattribution finding |
| ONWARDTEC Jan 2026 | SUBSTANTIVE | DSO 70 days improving — confirmed present. BUT: the "our peers... somewhere around in the range of 20%" analyst quote B06 attributes to this call (p.11) does NOT appear anywhere in this transcript — see §2 finding 2 | Partially unsupported: one cited quote is not in this file |
| ONWARDTEC May 2026 | SUBSTANTIVE | Top-25 concentration 88% (both the standalone mention and the 80%->88% growth comparison), "sweet spot" / 250->75->50 customer pruning, "90% to 95% of profits" analyst-education quote — all confirmed present | Confirmed substantive |
| ONWARDTEC Jul 2026 | SUBSTANTIVE | Rs33cr NA power-management ODC win, 87% concentration (implied by continuity), 11.5% YoY revenue growth — all confirmed present | Confirmed substantive |

**Result: 9 of 11 files are genuinely mined with real, locatable
citations. The CITED-ONLY and UNUSED classifications are both
defensible on the evidence.** The one structural problem is not a
missing-use problem, it is a quote-fidelity problem inside two of the
SUBSTANTIVE/CITED-ONLY files: see §2.

---

## 2. QUOTE FIDELITY — FINDINGS

### FINDING 1 (MAJOR): TAM figure inflated beyond what either source says
B06 states, in Q6 and again in Part 5: "Cyient's TAO Digital acquisition
is explicitly framed as AI SCOPE EXPANSION: moving from a $100 billion
ER&D outsourcing TAM to a **$2-3 trillion** lifecycle-engineering TAM
enabled by AI adoption work (CYIENT TAO Digital call, p.3-4; Q1 FY27
call, p.5)."

Neither cited source supports "$2-3 trillion":
- TAO Digital call (CYIENT-Concall_Jun_2026, marker PAGE 4): "It drives
  a shift from a narrow view of a $100 billion TAM that is ER&D
  outsourcing to an estimated **$2 trillion** market in just the
  industries we play in" — a single figure, not a range, and not "$3
  trillion" at either end.
- Q1 FY27 call (CYIENT-Concall_Aug_2026, marker PAGE 5): "ER&D
  outsourcing today is a market of roughly $80 to $100 billion. Across
  the full product lifecycle, the opportunity in front of us is close
  to **20 times that**" — 20x of $80-100bn is $1.6-2.0 trillion, again
  not "$2-3 trillion."
No occurrence of "trillion" appears anywhere near a "3" in either
transcript. This is a real inflation of Cyient's own stated market-size
claim by up to 50% at the top end, embedded in the cross-peer AI
hypothesis in Part 5 (a section the report itself flags as inferential,
but the underlying figure it inflates from is not inferential — it is
misquoted).

### FINDING 2 (MAJOR): Analyst margin-benchmark quote attributed to the wrong quarter
In "THE MARGIN BENCHMARK" section, B06 writes: "An analyst on the Q3
FY26 call directly benchmarked Onward against 'our peers, I believe
[who] are somewhere around in the range of 20%' (Q3 FY26 call, p.11) —
management did not dispute the 20% peer figure, only its own trajectory
toward it."

I searched all four Onward transcripts for this quote. It does not
appear in ONWARDTEC-Concall_Jan_2026 (the actual Q3 FY26 call) at all —
that file's only "peer" mention (line 678) is about demand pockets, not
margin. The quote is real, but it is in
**ONWARDTEC-Concall_Oct_2025 (Q2 FY26 call), marker PAGE 10** (internal
"Page 9 of 12"): "would it be safe to say that the H1 margin is
currently sitting at 13.5% roughly... Can you see a path to 15% by
FY '27 because our peers, I believe, are somewhere around in the range
of 20%?" This is a genuine wrong-quarter misattribution: a real,
material analyst quote sourced to the wrong call, one quarter off from
where it actually was said. Correct anchor: ONWARDTEC Q2 FY26 call
(Oct 2025), marker PAGE 10.

### FINDING 3 (MINOR): Systemic page-anchor imprecision, mixed PDF-marker vs. internal-page conventions
Every transcript carries two page-numbering systems: the extraction's
own "===== PAGE N =====" marker (starting at the BSE/NSE cover letter,
page 1) and the transcript's internal printed header ("Page X of Y",
which starts one page later, since page 1 of the internal numbering is
the cover letter's marker page 2). B06's citations mix both conventions
inconsistently, sometimes within the same paragraph, producing citations
that are off by one page (occasionally two) from the stated marker
convention this run uses for anchors. Confirmed examples, content
verified accurate in every case, only the page number is imprecise:
- TATAELXSI Apr 2026: "0.9% QoQ" and "Healthcare de-grew 13.1%" cited as
  p.2 — actual location is marker PAGE 3 (internal "Page 2 of 17").
  "High-single digit exit... geopolitical and all the war" cited as
  p.6 — actual location is marker PAGE 7 (internal "Page 6 of 17").
- TATAELXSI Jan 2026: the "pent-up demand" characterisation is folded
  into a "(TATAELXSI Q3 FY26 call, p.3)" citation shared with the 3.2%
  growth quote; the 3.2% quote is genuinely on marker PAGE 3, but "pent
  -up demand" itself is said on marker PAGE 9, six pages later.
- CYIENT Apr 2026: the price-increase quote ("existing customers have
  also backed us on price increases") and the "downward variance / 2.4%
  degrowth" quote are cited as p.5 — actual location is marker PAGE 6
  (internal "Page 5 of 14"). The Strategic Units -12.4% / West Asia
  deferral material is cited as p.5 — actual location is marker PAGE 6
  -7 (internal "Page 5-6 of 14").
None of these affect the substance of any claim; every quote checked is
genuinely present in the named file. This is an anchor-precision defect,
not a fabrication, but it means a reader following B06's page citations
literally will occasionally land one page short.

### FINDING 4 (MINOR): A paraphrase presented with quotation marks as if verbatim
B06 writes, for TATAELXSI Q1 FY27: "Europe automotive described as 'a
little moderated,' Germany 'soft'." "A little moderated" is a genuine
verbatim quote (marker PAGE 13: "Europe is a little moderated right
now"). The word "soft" in quotation marks is not: I searched the entire
Q1 FY27 transcript and the word "soft" does not appear anywhere as an
isolated word. What management actually said, twice, is "softness in
Germany" (marker PAGE 5 and marker PAGE 11) — a noun, not the adjective
B06 quotes. The substance (Germany is weak) is accurately conveyed; the
quotation marks around "soft" misrepresent a paraphrase as a direct
quote.

---

## 3. MISSED EVIDENCE

Reading CYIENT-Concall_Jun_2026_2 (the UNUSED semiconductor financing
call) against the six peer_questions, one passage stands out as
relevant to B06's own Part 5 cross-peer hypothesis (that real demand
strength in this window clusters around AI/data-center capex
beneficiaries) but was not cited: management states the share of power
consumption going to data centers is "going up from 2% in 2025 to 8% in
2030" and frames the entire Rs300cr fundraise around "AI scale" power
demand (marker PAGE 4). This would have been a fourth, independent data
point for the Part 5 hypothesis, from the same company (Cyient) but a
different business line. This is an industry-context miss, not a
directly claim-relevant one (the six peer_questions are about ER&D
services demand/margin/DSO/concentration/account-wins/AI-effect-on-
services, and this call is about a separate semiconductor products
subsidiary) — MINOR per the rubric's own severity split.

I found no other material passage across the 11 transcripts, read
against the six questions, that B06 should have used and did not. The
UNUSED and CITED-ONLY classifications are both substantively correct.

---

## 4. QUESTION COVERAGE — ALL SIX PEER_QUESTIONS

Checked against B05's `peer_questions[]` list verbatim:

| # | B05 question | B06 verdict delivered | Worked or restated? |
|---|---|---|---|
| 1 | ER&D demand conditions FY26/Q1FY27, Plant Eng/A&C/Aerospace | CONTRADICTED, with quarter-by-quarter figures from all three peers and an explicit aerospace exception carved out | WORKED — extensive extraction, not a restatement |
| 2 | Pricing power / utilisation / billing-rate improvement | PARTIALLY VERIFIED, with utilisation %, bill-rate $/hr, and one explicit price-increase disclosure | WORKED |
| 3 | Billing-cycle / DSO / unbilled-revenue trends | CONTRADICTED, with DSO day-counts and FCF/PAT % figures | WORKED |
| 4 | Client concentration levels, industry-wide | VERIFIED, with top-25 %, customer-count pruning numbers, and a named analyst-education quote | WORKED |
| 5 | Named large account win / ramp NA or Europe | VERIFIED (disclosure-norm framing), with five separate named deals across all three peers | WORKED |
| 6 | AI's effect on ER&D scope/pricing/headcount | VERIFIED, cross-peer multi-quarter, though the TAM figure used to illustrate it is inflated (Finding 1) | WORKED, but the supporting figure needs correction |

All six questions received a genuinely worked, evidenced verdict; none
was left unanswered while appearing addressed. No skipped claim (which
would be MAJOR under rule 5).

---

## 5. VERDICT DISCIPLINE

Checked every VERIFIED verdict for the ≥2-independent-peer-anchor bar:
- Q4 (concentration): VERIFIED — anchored on Onward (numeric), Tata
  Elxsi (qualitative strategy language), Cyient (qualitative account-
  dependency language). 3 peers. Passes.
- Q5 (account-win disclosure norm): VERIFIED — anchored on all three
  peers with five separate named deals. Passes.
- Q6 (AI effect): VERIFIED — anchored on all three peers across eight
  quarterly calls plus the TAO Digital call. Passes, though see Finding
  1 on the one figure used to illustrate it.
No VERIFIED verdict in this report rests on a single peer. No verdict
was upgraded from silence (peer silence is correctly reported as
"peers silent: none" or named explicitly where a peer stopped
disclosing, e.g. Onward's DSO disappearing from Q4/Q1 disclosure —
correctly flagged as a disclosure-quality finding, not misread as
confirmation of anything). `verdict_discipline_fails: []`.

---

## 6. INFERENCE-LINE CHECK

B06 is consistently careful to frame peer evidence as evidence about the
peer or the sector, not as evidence about TAAL Tech's own filed numbers.
The margin-benchmark and working-capital-benchmark conclusions ("reads
as a TAAL Tech condition," "genuinely anomalous against the best
comparable evidence") are explicitly hedged with caveats about business-
model mismatch and the absence of a precise control, and are framed as
sharpening existing B01/B02/B04 flags rather than asserting new facts
about TAAL Tech. I found no place where a peer statement is used as if
it directly evidences a TAAL Tech number. No inference-line violation
found.

---

## SUMMARY

Peer utilisation is genuinely high: 9 of 11 transcripts substantively
mined with real, checkable citations; the 2 remaining files are
correctly classified as CITED-ONLY and UNUSED on the actual content.
All six handed-over questions were actually worked, not restated, and
verdict discipline (≥2 anchors, no upgrade-from-silence) holds
throughout. The defects that exist are quote-fidelity defects inside an
otherwise sound piece of work: one inflated TAM figure (MAJOR), one
quote sourced to the wrong quarter's call (MAJOR), a recurring page-
anchor imprecision from mixing two numbering conventions (MINOR), one
paraphrase dressed as a verbatim quote (MINOR), and one industry-context
passage in the UNUSED file that would have reinforced the report's own
cross-peer hypothesis (MINOR).

---

```yaml
stage: B12d
company: "TAALTECH"
run_date: "2026-09-10"
model: claude-sonnet-5
status: complete
peers_audited: 11
substantive_confirmed: 9
substantive_unsupported: []
unused_but_relevant:
  - {peer: "CYIENT-Concall_Jun_2026_2 (Semiconductor Strategic Financing, 26-May-2026)", missed_item: "AI/data-center power demand share rising 2% (2025) to 8% (2030), framing the entire fundraise around AI-infrastructure capex", anchor: "CYIENT-Concall_Jun_2026_2, marker PAGE 4"}
claims_all_addressed: true
verdict_discipline_fails: []
findings:
  - {severity: "MAJOR", location: "B06 Q6 and Part 5 cross-peer hypothesis", description: "B06 states Cyient's TAO Digital deal reframes ER&D TAM to '$2-3 trillion,' citing CYIENT TAO Digital call p.3-4 and CYIENT Q1 FY27 call p.5. Neither transcript supports this: the TAO Digital call states an estimated '$2 trillion market' (marker PAGE 4, singular figure, not a range), and the Q1 FY27 call implies roughly $1.6-2.0 trillion ('20 times' an $80-100bn base, marker PAGE 5). No source states $3 trillion at either end."}
  - {severity: "MAJOR", location: "B06 THE MARGIN BENCHMARK section", description: "B06 attributes the analyst quote 'our peers, I believe, are somewhere around in the range of 20%' to the ONWARDTEC Q3 FY26 call (Jan 2026 transcript), p.11. This quote does not appear anywhere in that transcript. It is genuinely said in the ONWARDTEC Q2 FY26 call (Oct 2025 transcript), marker PAGE 10 ('...Can you see a path to 15% by FY'27 because our peers, I believe, are somewhere around in the range of 20%?'). Wrong-quarter misattribution of a real, material quote."}
  - {severity: "MINOR", location: "Multiple B06 citations, TATAELXSI Apr 2026 and Jan 2026, CYIENT Apr 2026", description: "B06 mixes the extraction's PDF-marker page numbering with the transcripts' internal printed 'Page X of Y' numbering inconsistently within the same report, producing citations off by one (occasionally two) pages from the stated marker convention. Confirmed instances: TATAELXSI Apr 2026 '0.9% QoQ'/'Healthcare -13.1%' cited p.2 vs actual marker PAGE 3; 'high-single digit exit' cited p.6 vs actual marker PAGE 7; TATAELXSI Jan 2026 'pent-up demand' folded into a p.3 citation vs actual marker PAGE 9; CYIENT Apr 2026 price-increase and 'downward variance/2.4%' quotes cited p.5 vs actual marker PAGE 6, Strategic Units -12.4%/West Asia material cited p.5 vs actual marker PAGE 6-7. Every quote content itself is genuine and present in the named file."}
  - {severity: "MINOR", location: "B06 Q1 sector demand section, TATAELXSI Q1 FY27 quote", description: "B06 places the word 'soft' in quotation marks as a direct Tata Elxsi quote describing Germany. The word 'soft' does not appear anywhere in the TATAELXSI Jul 2026 transcript; management says 'softness in Germany' (noun form) twice, at marker PAGE 5 and marker PAGE 11. Substance accurate, quotation-mark precision is not."}
  - {severity: "MINOR", location: "B06 Part 3 coverage map, CYIENT-Concall_Jun_2026_2 row", description: "The UNUSED classification is justified on content, but the file contains an AI/data-center power-demand market-sizing passage (marker PAGE 4) that would have reinforced B06's own Part 5 cross-peer hypothesis about AI-infrastructure-adjacent demand clustering; an industry-context item left on the table, not a claim-relevant one."}
critical_count: 0
major_count: 2
minor_count: 3
acceptance_rate: 82
```
