# Verifier D: Peer Coverage Audit — CEIGALL (Ceigall India Ltd)
Run date: 2026-09-06 | Model: claude-sonnet-5 | Stage audited: B06 (outputs/blocks/B06-peers.yaml, outputs/reports/06-peers.md)
Peer questions audited against: B05 Section 4B (outputs/reports/05-concall.md, 7 questions)

Scope: did B06 actually use the 12 peer transcripts it was given, are its SUBSTANTIVE
labels earned, are its verdicts (verified/partially_verified/contradicted/unverifiable)
correct against the transcript text, and are its citations real and correctly anchored.

Note on citation convention: every one of the 12 source .txt files carries its own header
instruction — "Page markers below are the PDF page numbers. Cite them as (filename, p.N)."
— i.e. the `===== [PAGE N] =====` markers are the mandated citation basis, not the
transcript's own internal printed "Page X of Y" footer (the two frequently differ by one,
since the footer numbering starts from a different reference point than the PDF page
count). All page checks below use the `[PAGE N]` marker as ground truth, per the files'
own stated convention.

---

## PART 1: COVERAGE AUDIT PER PEER

### HGINFRA (4 transcripts, all marked SUBSTANTIVE)

| Quarter | B06 contribution claim | Verified against transcript | Anchor accuracy |
|---|---|---|---|
| Q1 FY26 (Aug-2025) | HAM monetization EV/equity/debt (EV Rs3,584cr, equity Rs767cr, debt Rs2,200cr); HAM equity requirement Rs1,664cr; Ganga Expressway Rs43cr change-in-law margin item | Confirmed real, both figures found verbatim | EV figures p.5-6 correct. HAM equity Rs1,664cr p.6 correct. Ganga Expressway Rs43cr quote is real but appears at p.10, not the p.14 cited in Part 2 |
| Q2 FY26 (Nov-2025) | HAM equity requirement Rs1,709cr continuation; monetization EV repeat-disclosure | Confirmed real | p.6-7 cited, content at p.7 — acceptable (range citation) |
| Q3 FY26 (Feb-2026) | Monetization SPA-execution update; HAM equity Rs1,750cr; one-off margin denial exchange ("no additional exceptional item") | Confirmed real, quote verbatim | HAM equity Rs1,750cr p.6 correct. Margin-denial quote cited p.7, actually at p.8 |
| Q4 FY26 (May-2026) | Names "West Asian conflict"/"war situation" explicitly; NHAI-km deflection ("I'm not having a very exact number"); HAM equity Rs1,903cr | Confirmed real, all three quotes verbatim | "West Asian conflict" quote p.2 correct. NHAI deflection quote p.17-18 correct. HAM equity Rs1,903cr p.6 correct. BUT the "war situation... cannot guarantee anything" quote (used in Part 2B to resolve B05's open item) is cited at p.17 and is actually at p.11 — a materially wrong anchor, six pages off. The "temporarily increasing overall leverage" quote (Q1 section) is cited p.6 and is actually at p.5 |

Verdict: HGINFRA's SUBSTANTIVE label is earned — every quoted passage exists verbatim in
the named file, and the material used (HAM equity drift, EV disclosure, margin
transparency, the "war situation" resolution) is genuinely load-bearing. But two of its
four transcripts (Aug-2025, May-2026) carry page anchors that are wrong by 4-6 pages on
specific, checkable quotes. Finding severity: MAJOR (anchor, not content).

**Independent read, not surfaced by B06**: the May-2026 (Q4 FY26) call states, on the same
page as the correctly-cited HAM equity paragraph: "We have started the last year with
expected new order inflows of INR10,000 crores, but due to lukewarm bids pipeline, we
could secure only new orders of INR1,300 crores during the year" (HGINFRA-Concall_May_2026
_Transcript.txt, p.6). This is an 87% guidance miss by the largest of the three peers, in
the exact fiscal year Ceigall beat its own Rs5,000cr order-inflow guidance by 2.3x. B06's
industry_cross_read (2A) already flags that Ceigall's order-inflow beat "needs its own
explanation" against a soft-award year, but never cites this specific, dramatic
counter-example sitting on a page it otherwise quotes. This is directly relevant to the
same cross-read argument and was available. MAJOR miss (unused, directly relevant).

### KNRCON (4 transcripts, all marked SUBSTANTIVE)

| Quarter | B06 contribution claim | Verified | Anchor accuracy |
|---|---|---|---|
| Q1 FY26 (Aug-2025) | WC days 93→169 with named cause; HAM equity Rs990cr; monetization deflection on live deal | Confirmed real, all quotes verbatim | WC/debt figures p.5 correct. Deflection quote ("we'll let you know") p.20 correct. Irrigation/HAM debtor figures (Rs800cr/Rs1,200cr) cited p.8, actually at p.7 |
| Q2 FY26 (Nov-2025) | HAM equity Rs991cr exact tie-out; Cheyyur-Vandavasi bonus tracking | Confirmed real | Both p.4 and p.17 citations correct |
| Q3/9M FY26 (Feb-2026) | Proactive 1,448km/712km disclosure; WC recovery to 82 days | Confirmed real | Both p.3 and p.6 citations correct |
| Q4 FY26 (Jun-2026) | Full-year 3,100km, -22% YoY; West Asia/bitumen narrative; MoRTH price-cycle change | Confirmed real | p.3 and p.4 citations correct |

Verdict: KNRCON's SUBSTANTIVE label is fully earned across all four quarters, with the
strongest anchor accuracy of the three peers — only one minor (one-page) slip found.

### PNCINFRA (4 transcripts, all marked SUBSTANTIVE)

| Quarter | B06 contribution claim | Verified | Anchor accuracy |
|---|---|---|---|
| Q2 FY26 (Nov-2025) | 6,300km target unprompted; HAM equity Rs1,744cr; Rs5.3cr Mathura bonus; EV Rs630cr | Confirmed real, all quotes verbatim | 6,300km p.4 correct, HAM equity p.5 correct, Mathura bonus p.4 correct, EV Rs630cr p.10 correct (equity Rs114cr described loosely as "same exchange," actually one page earlier at p.9 — immaterial) |
| Q3 FY26 (Feb-2026) | 377km vs 504km; HAM equity reconciliation continuation; Hardoi bonus follow-up | Confirmed real | 377km/504km cited p.3, actually at p.4 (one page off). The HAM equity reconciliation (Rs1,744cr total / Rs1,110cr invested / Rs634cr remaining) is cited in the report as "p.13, 'Page 13 of 18' printed" — this is wrong on both counts: the figures actually appear at marker p.5 (printed footer "Page 4 of 18"), and marker p.13/p.14 (printed "Page 12-13") contains unrelated Q&A (canal-project execution, unbilled revenue, mining/solar FY27-28 targets). This is not an off-by-one slip; it is a specific, defended page claim that a direct check disproves. Hardoi bonus quote at p.15-16 range, close enough |
| Q4 FY26 (May-2026) | HAM equity Rs1,744cr→Rs1,623cr reconciled with reason; MSRDC Rs50cr+ bonus; West Asia narrative; diversification margin-pressure caution | Confirmed real, all quotes verbatim | Rs1,623cr reconciliation p.6 correct (matches both marker and printed footer here). MSRDC bonus p.14 correct. Vivad-se-Vishwas III Rs235cr settlement (used in Part 2E) p.6 correct. Diversification-margin-pressure quote cited p.9, actually at p.11 (two pages off) |
| Q1 FY27 (Aug-2026) | 107km disclosure; WC days 110 with driver | Confirmed real | 107km cited p.2, actually at p.3 (one page off). WC days 110 cited p.9-10, correct at p.9 |

Verdict: PNCINFRA's SUBSTANTIVE label is earned on content — nothing quoted is invented —
but it carries the single worst anchor error in the set (the Feb-2026 reconciliation
citation), plus three further one-to-two-page slips.

---

## PART 2: VERDICT-DISCIPLINE AUDIT PER CLAIM (B05's 7 peer questions)

All seven questions handed off in B05 Section 4B receive an explicit verdict in B06 Part 1
(Q1-Q7 map one-to-one). claims_all_addressed: TRUE, no skipped claim.

| # | Claim | B06 verdict | Independent check | Agree? |
|---|---|---|---|---|
| 1 | "Cash flow not a problem" narrative is sector-wide tone | CONTRADICTED | Confirmed: zero hits for "cash rich"/"comfortable cash"/"amazing" across all 12 transcripts; HGINFRA and KNRCON both name specific drivers instead (verified quotes real, though HGINFRA's is anchored p.6 vs actual p.5) | Agree |
| 2 | NHAI award-pace deflection is standard sector reticence | PARTIALLY VERIFIED | Confirmed: KNRCON and PNCINFRA volunteer exact figures unprompted every quarter (verified); HGINFRA deflects when pressed directly ("I'm not having a very exact number", verified verbatim, p.17-18 correct) | Agree |
| 3 | Non-disclosure of HAM sale price is industry-standard opacity | CONTRADICTED (price/consideration); UNVERIFIABLE (realised IRR) | Confirmed: HGINFRA (3 calls) and PNCINFRA both disclose hard EV/equity/debt figures on completed or near-complete deals; no peer states a realised IRR number | Agree |
| 4 | Unreconciled equity-commitment totals are company-specific | PARTIALLY VERIFIED | Confirmed: KNRCON and PNCINFRA reconcile arithmetically clean (verified the KNRCON Rs676→698cr / Rs314→292cr tie-out and PNCINFRA Rs1,744cr with stated scope change); HGINFRA shows a milder, unexplained drift (Rs1,664→1,709→1,750→1,903cr on an unchanged 11-project count, all four figures confirmed real at their respective pages) | Agree |
| 5 | Peers proactively disclose governance/compliance events | UNVERIFIABLE | Confirmed by independent grep: zero hits for fraud/IFC/auditor-resign/whistleblower/leadership-change terms across all 12 files. No comparable peer event exists to test against | Agree |
| 6 | Working-capital stretch is sector-wide vs company-specific | PARTIALLY VERIFIED | Confirmed: KNRCON's WC days swing 93→169→82 (verified, named cause at p.7, not the p.8 cited) and PNCINFRA's ~110 days (verified) both show volatility-with-attribution-and-recovery, unlike Ceigall's described one-directional drift | Agree |
| 7 | Folding bonus/royalty into headline margin is standard practice | CONTRADICTED | Confirmed: PNCINFRA (Mathura Rs5.3cr, Hardoi Rs14cr, MSRDC Rs50cr+, all verified verbatim), KNRCON (Cheyyur-Vandavasi, verified), and HGINFRA (Ganga Expressway Rs43cr, verified but anchored p.14 vs actual p.10) all name project, amount and timing every time | Agree |

**Verdict discipline check (rule 4):** B06's `verified` list is empty — no claim was marked
outright VERIFIED, so the ">=2 independent anchors for VERIFIED" rule has no instance to
fail. No claim was upgraded from a silent peer set to a positive verdict (the one place
this risk existed, Q5, was correctly left UNVERIFIABLE rather than inferred). No
verdict-discipline failure found.

**Contradicted-list cross-check:** all three CONTRADICTED entries (Q1, Q3, Q7) rest on 2-3
independent peer anchors each, consistent with the multi-peer evidence shown in Part 1
above; none rests on a single peer. No claim placed in "contradicted" that the transcript
evidence actually supports is found; all three read correctly as contradictions of the
tested claim.

---

## PART 3: MATERIAL PASSAGES NOT USED

1. **HGINFRA-Concall_May_2026_Transcript.txt, p.6** — FY26 order-inflow guidance of
   Rs10,000cr vs actual Rs1,300cr secured (an 87% miss), stated on the same page as the
   HAM-equity paragraph B06 already cites. Directly relevant to B06's own
   industry_cross_read note that Ceigall's order-inflow beat "needs its own explanation";
   this is the single most concrete counter-data-point available and was not used. MAJOR.

No other transcript passage bearing directly on the seven peer_questions was found
unused in the spot-reading performed for this audit. Industry/contextual material
(competitive silence on Ceigall, capex-cycle diversification, arbitration/dispute risk,
BOT-vs-HAM preference shift) was checked and is genuinely reflected in B06 Part 2.

---

## PART 4: PEER UTILISATION

peer_utilisation = 3 peers used substantively / 3 peers provided = **100%**
(transcript_utilisation = 12 substantively used / 12 provided, also confirmed).

I agree with B06's own count (peer_utilisation_summary: peers_provided 3, peers_used
_substantively 3). Every peer's SUBSTANTIVE label is earned on content: every quoted
passage checked was found verbatim in the named file, and the content used is genuinely
load-bearing for at least one Part 1 verdict or Part 2 cross-read finding — this audit
found no fabricated quote and no invented figure anywhere in the 12-transcript set.

The count should not be read as a clean bill of health on citation precision, however.
Of roughly 25-30 individual page anchors spot-checked across the three peers, 9 carry a
wrong page number against the `[PAGE N]` marker convention the source files themselves
specify: 5 are one-page slips (MINOR — the quote is on the immediately adjacent page),
and 4 are multi-page or actively-defended-and-wrong anchors (MAJOR — HGINFRA's "war
situation" quote cited 6 pages off, HGINFRA's Ganga Expressway quote cited 4 pages off,
PNCINFRA's diversification-margin quote cited 2 pages off, and PNCINFRA's Feb-2026 HAM
equity reconciliation cited with a specific, checkable "Page 13 of 18 printed" claim that
points to unrelated content). This is a real and recurring anchor-fidelity problem, even
though the underlying claims all survive re-verification by text search.

---

## FINDINGS

| # | Severity | Location (B06) | Issue | Correct anchor |
|---|---|---|---|---|
| 1 | MAJOR | Part 2B, "war situation" quote | HGINFRA-Concall_May_2026_Transcript.txt cited p.17; quote is real but located at p.11 (6 pages off) | p.11 |
| 2 | MAJOR | Part 1 Q1, Ganga Expressway margin quote | HGINFRA-Concall_Aug_2025_Transcript.txt cited p.14; quote is real but located at p.10 (4 pages off) | p.10 |
| 3 | MAJOR | Part 1 Q4, HAM equity reconciliation figures | PNCINFRA-Concall_Feb_2026_Transcript.txt cited "p.13, 'Page 13 of 18' printed"; figures (Rs1,744cr/Rs1,110cr/Rs634cr) are real but located at p.5 (printed "Page 4 of 18"); the cited page (marker 13/14, printed 12-13) contains unrelated content | p.5 |
| 4 | MAJOR | Part 1 Q4/Part 2C, diversification-margin quote | PNCINFRA-Concall_May_2026_Transcript.txt cited p.9; quote is real but located at p.11 (2 pages off) | p.11 |
| 5 | MAJOR | Not present in B06 | HGINFRA's FY26 order-inflow guidance miss (Rs10,000cr guided vs Rs1,300cr achieved) is directly relevant to B06's own cross-read on Ceigall's order-inflow beat and was not used, despite sitting on an already-cited page | HGINFRA-Concall_May_2026_Transcript.txt, p.6 |
| 6 | MINOR | Part 1 Q1, "temporarily increasing leverage" quote | HGINFRA-Concall_May_2026_Transcript.txt cited p.6; quote located at p.5 | p.5 |
| 7 | MINOR | Part 1 Q7, margin-denial quote | HGINFRA-Concall_Feb_2026_Transcript.txt cited p.7; quote located at p.8 | p.8 |
| 8 | MINOR | Part 1 Q6, irrigation/HAM debtor figures | KNRCON-Concall_Aug_2025_Transcript.txt cited p.8; figures located at p.7 | p.7 |
| 9 | MINOR | Part 1 Q2, 377km/504km quote | PNCINFRA-Concall_Feb_2026_Transcript.txt cited p.3; quote located at p.4 | p.4 |
| 10 | MINOR | Part 1 Q2, 107km quote | PNCINFRA-Concall_Aug_2026_Transcript.txt cited p.2; quote located at p.3 | p.3 |

No CRITICAL findings. No fabricated quote, no invented figure, no verdict-discipline
failure, no skipped claim.

---

```yaml
stage: B12d
company: "CEIGALL"
run_date: "2026-09-06"
model: claude-sonnet-5
status: complete
peers_audited: 3
substantive_confirmed: 3
substantive_unsupported: []
unused_but_relevant:
  - {peer: "HGINFRA", missed_item: "FY26 order-inflow guidance of Rs10,000cr vs only Rs1,300cr actually secured (87% miss), stated on the same page as HAM-equity content B06 already cites; directly relevant to B06's own cross-read flagging that Ceigall's FY26 order-inflow beat needs its own explanation in a soft-award year", anchor: "HGINFRA-Concall_May_2026_Transcript.txt, p.6"}
claims_all_addressed: true
verdict_discipline_fails: []
findings:
  - {severity: "MAJOR", location: "B06 Part 2B", claimed_anchor: "HGINFRA-Concall_May_2026_Transcript.txt, p.17", issue: "quote real, wrong page (actual p.11)", note: "war situation quote resolving B05 open item"}
  - {severity: "MAJOR", location: "B06 Part 1 Q1/Part 2C", claimed_anchor: "HGINFRA-Concall_Aug_2025_Transcript.txt, p.14", issue: "quote real, wrong page (actual p.10)", note: "Ganga Expressway Rs43cr margin item"}
  - {severity: "MAJOR", location: "B06 Part 1 Q4", claimed_anchor: "PNCINFRA-Concall_Feb_2026_Transcript.txt, p.13 (defended as printed page 13 of 18)", issue: "figures real, wrong page (actual p.5); cited page contains unrelated content", note: "HAM equity Rs1,744cr/Rs1,110cr/Rs634cr reconciliation"}
  - {severity: "MAJOR", location: "B06 Part 1 Q4/Part 2C", claimed_anchor: "PNCINFRA-Concall_May_2026_Transcript.txt, p.9", issue: "quote real, wrong page (actual p.11)", note: "diversification will pressure margins quote"}
  - {severity: "MAJOR", location: "B06 industry_cross_read 2A (omission)", claimed_anchor: "n/a - not used", issue: "HGINFRA's 87% FY26 order-inflow guidance miss (Rs10,000cr guided vs Rs1,300cr secured) not surfaced despite direct relevance and proximity to cited material", note: "HGINFRA-Concall_May_2026_Transcript.txt, p.6"}
  - {severity: "MINOR", location: "B06 Part 1 Q1", claimed_anchor: "HGINFRA-Concall_May_2026_Transcript.txt, p.6", issue: "quote real, wrong page (actual p.5)", note: "temporarily increasing overall leverage"}
  - {severity: "MINOR", location: "B06 Part 1 Q7", claimed_anchor: "HGINFRA-Concall_Feb_2026_Transcript.txt, p.7", issue: "quote real, wrong page (actual p.8)", note: "no additional exceptional item margin denial"}
  - {severity: "MINOR", location: "B06 Part 1 Q6", claimed_anchor: "KNRCON-Concall_Aug_2025_Transcript.txt, p.8", issue: "figures real, wrong page (actual p.7)", note: "irrigation/HAM debtor figures"}
  - {severity: "MINOR", location: "B06 Part 1 Q2", claimed_anchor: "PNCINFRA-Concall_Feb_2026_Transcript.txt, p.3", issue: "quote real, wrong page (actual p.4)", note: "377km vs 504km"}
  - {severity: "MINOR", location: "B06 Part 1 Q2", claimed_anchor: "PNCINFRA-Concall_Aug_2026_Transcript.txt, p.2", issue: "quote real, wrong page (actual p.3)", note: "107km awarded"}
critical_count: 0
major_count: 5
minor_count: 5
acceptance_rate: 100
