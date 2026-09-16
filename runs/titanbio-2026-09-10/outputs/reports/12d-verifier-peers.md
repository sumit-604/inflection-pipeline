# VERIFIER D: PEER COVERAGE AUDIT
Company: TITANBIO | Run date: 2026-09-16 | Model: claude-sonnet-5
Inputs: 11 peer transcripts (ADVENZYMES x4, FERMENTA x4 [stale, Aug-2021 to Jun-2022],
VIDHIING x3), runs/titanbio-2026-09-10/outputs/reports/06-peers.md +
outputs/blocks/B06-peers.yaml, and the `peer_questions` list in
outputs/blocks/B05-concall.yaml.

Context note: Titan Biotech holds no earnings calls of its own. These 11 peer transcripts
are the only management voice on this industry anywhere in the corpus. A transcript cited
once in passing and counted as fully used is a more serious miss on this run than on a run
where the company's own calls exist, per the task brief. I read all 11 transcripts in full
before comparing against B06.

---

## PART 1: COVERAGE AUDIT PER PEER (transcript-instance level, 11 rows)

For every peer/call marked SUBSTANTIVE in B06's `peer_coverage_map`, I located the actual
citations in B06 Parts 1-2 and checked them against that specific transcript (not just
"somewhere in the 11-transcript set").

| # | Peer / call | B06 map's claimed contribution | Verified in THIS transcript? |
|---|---|---|---|
| 1 | ADVENZYMES Nov-13-2025 (Q2/H1 FY26) | 26% YoY growth quote, EFSA/registration timelines, tariff EBITDA quantification, inquiry-count drop, US market share | YES — all present and correctly quoted in this file. |
| 2 | ADVENZYMES Feb-04-2026 (Q3/9M FY26) | 2% YoY deceleration, "mixed" quarter, capacity utilisation 55-60%, R&D centre capex plan, **EFSA approval timelines** | Growth/utilisation/capex items YES. **EFSA approval timelines: NO — this transcript contains no EFSA content at all** (confirmed by full-text search). The "still waiting from 2014" EFSA quote B06 cites under Claim 4 to this call is actually in the **Aug-12-2026** transcript. |
| 3 | ADVENZYMES May-12-2026 (Q4/FY26) | FY26 full-year +17%, "highest-ever" revenue, **Nutrazyme/Wellfa disclosed revenue**, mix-vs-margin discussion | FY26 +17%/"highest-ever" YES, mix-vs-margin discussion YES. **Nutrazyme/Wellfa disclosed revenue: NO — "Nutrazyme" and "Wellfa" do not appear anywhere in this transcript.** That content is genuinely in the Nov-13-2025 transcript. |
| 4 | ADVENZYMES Aug-12-2026 (Q1 FY27) | Growth back to 2% YoY, "softer, muted start", utilisation 70-75%, Rs123cr capex breakdown, active pricing | YES — all present and correctly quoted. This is also the transcript that actually contains the "let's not get into the QoQ" quote and the "still waiting from 2014" EFSA quote that B06 mis-cites elsewhere as Feb-04-2026 (see Part 2). |
| 5 | FERMENTA Aug-17-2021 (Q1 FY22) | Structural: **formula-priced wool-grease contract**, near-100% human-side utilisation, capex-to-revenue rule of thumb | Utilisation and capex-to-revenue rule of thumb YES (both confirmed verbatim in this file). **Formula-priced contract: NO — this file has no "formula" pricing language.** That content ("formula based... we do not get hit by spot pricing") is in the Nov-17-2021 transcript. |
| 6 | FERMENTA Nov-17-2021 (Q2 FY22) | Animal-side utilisation ~35%, premix capex Rs 35cr, regulatory pathway discussion | YES — all confirmed verbatim. |
| 7 | FERMENTA Feb-16-2022 (Q3 FY22) | Vegan D3/K1 delay pattern, shareholder capital-allocation challenge (S.C. Gupta) | YES — "This is not that you can fool the shareholders every time" confirmed verbatim, correctly dated and attributed. |
| 8 | FERMENTA Jun-01-2022 (Q4/FY22) | Repeated timeline slippage ("target is over the next 2 quarters"), **key-account margin trade-off pattern** | Timeline-slippage quote YES (confirmed verbatim). **Key-account margin trade-off: NO — "key account" does not appear anywhere in this transcript.** That content is genuinely in the Nov-17-2021 transcript (already credited there under a different label). |
| 9 | VIDHIING Jun-12-2024 (Q4 FY24) | 4-10 year customer approval cycle, Dahej ramp-up baseline | YES — confirmed verbatim. (Separately: the Claim-2 text's attribution of the naphthalene-substitution answer to this call is right on the call, wrong on the speaker — see Part 2.) |
| 10 | VIDHIING Nov-13-2025 (Q2/H1 FY26) | -17.8% YoY revenue, sector-wide 30-35% utilisation commentary, approval-cycle restated, Dahej utilisation 65-70%, pricing power on tariff | YES — all confirmed verbatim. |
| 11 | VIDHIING May-14-2026 (Q4/FY26) | FY26 revenue flat/down (Rs380cr vs Rs382.30cr), CoatIcon adjacency, high-value mix target slippage 50%→5%, Rs100cr capex/18-month commissioning | YES — all confirmed verbatim (capex figure is actually Rs75-85cr per the transcript, see Part 2 for the exact-number note). |

**Result: 7 of 11 transcript rows are fully clean (contribution accurately sourced to that
specific call). 4 of 11 rows (#2, #3, #5, #8) contain at least one claimed "contribution"
that is not actually in the transcript it is credited to** — it is real content, correctly
quoted, but drawn from a *different call by the same peer company* and mis-slotted into
this row. None of the 11 rows is CITED-ONLY or UNUSED at the peer-company level: every
peer genuinely contributed verified, traceable material to the analysis. But the map's
per-call attribution, which the task brief asks me to check "honestly," fails for those 4
rows. Given no company-call transcript exists as an anchor discipline for Titan itself,
this precision matters more here than on an ordinary run.

Severity: each of these 4 is graded MAJOR (findings 1-4 below) — the underlying company-level
SUBSTANTIVE classification survives (each peer still cleared the bar on other, correctly-cited
material from the same call), so this is not a fabrication or an invented signal, but the
map's specific factual claim about what a given call contains is wrong, which is exactly the
"passing mention counted as used" risk the task brief warns is worse on a no-concall run.

---

## PART 2: CITATION-LEVEL SPOT CHECKS (quote-by-quote, beyond the coverage map)

Independent of the map, I checked whether direct quotes in B06 Parts 1 and 2 exist at the
call/speaker cited.

**Finding 5 (MAJOR) — wrong call date, ADVENZYMES "QoQ" quote (Claim 1, Part 2A).**
B06 quotes Mukund Kabra saying "let's not get into the QoQ... I would say some quarters here
and there," and cites it to the **Feb-04-2026** call. The quote is real but appears in the
**Aug-12-2026** transcript ("Nikhil ji, let's not get into the QoQ... Let's not get into the
QoQ. That's what I want to highlight out here.") The Feb-04-2026 call has a similar-in-spirit
but textually different line ("I would still like to see more certainties..."). The
underlying point (management resists characterising a trend quarter to quarter) is true and
independently supported elsewhere; the citation itself is wrong.

**Finding 6 (MAJOR) — wrong call date, ADVENZYMES EFSA "2014" quote (Claim 4, Part 1).**
B06 quotes "we are still waiting from 2014" on an EFSA filing and cites it to the
**Feb-04-2026** call. The quote is real but is in the **Aug-12-2026** transcript (Ketan
Chheda exchange). The Feb-04-2026 transcript contains no EFSA content whatsoever (confirmed
by full-text search across all four ADVENZYMES files). This is the same underlying
misattribution as Finding 2 (the "EFSA approval timelines" coverage-map contribution).

**Finding 7 (MAJOR) — wrong speaker, VIDHIING naphthalene-substitution quote (Claim 2).**
B06 attributes "Substitution of certain imported raw materials by domestically available raw
materials... some of the naphthalene-based raw materials we have started buying locally from
India" to **Mihir Manek, Jun-12-2024 call**. In the transcript this answer is given by
**Mitesh Manek** (CFO), not Mihir Manek (JMD) — Mihir Manek only asked the preceding
follow-up question. Call and content are correct; the speaker is wrong.

**Finding 8 (MAJOR) — wrong speaker, VIDHIING "inflationary trends... volatile freight
markets" quote (Claim 2).** B06 attributes this phrase to **Bipin Manek, May-14-2026 call**.
In the transcript it is said by **Mitesh Manek** in his financial-highlights section ("Financial
year 2025-'26 was a year characterized by significant external challenges, including tariff
pressures, geopolitical uncertainties, inflationary trends and volatile freight markets...").
Bipin Manek's own opening remarks on that call contain a different, correctly-attributed line
elsewhere in B06 ("a noticeable slowdown in demand..."), which may be the source of the
conflation.

**Finding 9 (MAJOR) — wrong speaker, VIDHIING "we have not reduced a penny" pricing-power
quote (Part 2B).** B06 attributes this to **Mihir Manek, Nov-13-2025 call**. In the transcript
it is **Mitesh Manek** who says "Just for your information, the whole tariff which was put on
India at 50%, we have not reduced a penny on our pricing to the US market. That is the kind of
bargaining power that we have. Sorry, not bargaining power, pricing power," answering Lala
Ram's question. Mihir Manek does not speak this line.

**Finding 10 (MAJOR) — two speakers/exchanges merged into one attribution (B06 YAML
`contradicted[1].quote_anchor`).** The YAML block credits "Mihir Manek, VIDHIING Q4FY26 call
(May-14-2026)" with both the 18-month commissioning detail and the Rs75-85cr capex /
Rs125-150cr revenue figures. In the transcript these come from two separate exchanges: the
18-month commissioning answer is given by Bipin Manek then confirmed by Mitesh Manek
(Gokul Maheshwari's question), while the Rs75-85cr/Rs125-150cr figures are given later by
Mihir Manek in response to Saket's question. The figures themselves are correct; the
single-speaker attribution is not.

None of findings 5-10 changes a verdict or invents a signal — in every case the quoted
words exist verbatim somewhere in the ADVENZYMES/VIDHIING transcript set and the substantive
point B06 draws from them is supported. But six citation-accuracy failures across two peers,
all in the direction of collapsing distinct calls/speakers into a single cited source, is a
pattern, not a one-off, and it directly touches the load-bearing question this run depends on
(these are the only management voices in the corpus).

---

## PART 3: DATA-INTEGRITY FLAG (not a B06 authorship error, but affects anchor reliability)

**Finding 11 (MINOR, flagged for operator, not charged against B06).** The exact same
Ravi-Purohit/Nutrazyme/Wellfa Q&A block (management roster mismatch: "Vasant Rathi" speaks,
though Vasant Rathi is not listed among the Nov-13-2025 call's stated management — only
Mukund Kabra, Beni Rauka, and Ronak Saraf are listed for that call) appears **verbatim,
including page markers, in both the Nov-13-2025 and Feb-04-2026 extracted transcript
files**. This is very likely a corpus-extraction artifact (duplicated page range across two
outputs), not a live transcript defect. B06's citation of the Nutrazyme/Wellfa quote to
Nov-13-2025 is defensible given what is in that extracted file, but the anomaly (a
non-attending speaker responding) should have been a flag on its own — worth a source-PDF
re-check before this quote is relied on further downstream. This also explains Finding 3
(the map's May-2026 row) and partially explains why an EFSA-adjacent quote could get
mis-slotted to Feb-2026 in Findings 2 and 6 — extraction contamination between calls appears
to be a real risk in this transcript set, and B06 did not surface it.

---

## PART 4: VERDICT-DISCIPLINE AUDIT (per claim)

| Claim | B06 verdict | # independent peer anchors | Discipline check |
|---|---|---|---|
| 1 — industry-wide demand re-acceleration | CONTRADICTED | 2 peers (ADVENZYMES, VIDHIING), multiple quarters each | PASS — genuinely 2+ independent peers, no verdict upgraded from silence. |
| 2 — raw-material/feedstock cost trend | PARTIALLY VERIFIED | 2 peers (ADVENZYMES, VIDHIING) + FERMENTA structural | PASS — correctly downgraded from VERIFIED because no peer names Titan's specific feedstock (peptone/protein). |
| 3 — freight gross-up practice | UNVERIFIABLE | 0 (explicit silence across all 11) | PASS — correctly left UNVERIFIABLE rather than inferring an answer from silence. |
| 4 — customer-qualification cycle | VERIFIED | 2 peers, anchor_count 4 | PASS — clears the ≥2-independent-peer bar for a VERIFIED verdict (Rule 4); no single-peer VERIFIED found anywhere in B06. |
| 5 — health-supplement adjacency timeline | PARTIALLY VERIFIED | 2 peers (ADVENZYMES, FERMENTA) | PASS — correctly distinguishes "delay is normal" (peer-confirmed) from "zero product-naming for 3 years" (not peer-confirmed), rather than over-crediting Titan. |
| 6 — capacity-utilisation/capex disclosure norm | CONTRADICTED | 3 peers (all) | PASS. |

**No claim in B06 rests on a single peer for a VERIFIED verdict. No verdict is upgraded from
silence.** This is the one area where B06's discipline is clean; the defects found above are
citation-accuracy problems, not verdict-inflation problems.

---

## PART 5: PEER_QUESTIONS COMPLETENESS CHECK

B05's `peer_questions` list has 6 items. All 6 map one-to-one onto B06 Part 1 Claims 1-6 and
each received an explicit verdict (CONTRADICTED / PARTIALLY VERIFIED / VERIFIED /
UNVERIFIABLE). No skipped claim. `claims_all_addressed: true` confirmed.

---

## PART 6: ATTRIBUTION DIRECTION CHECK

Checked that no peer statement is attributed to the subject company (Titan Biotech) and no
Titan claim is dressed up as a peer finding. Confirmed clean: every quote in B06 Parts 1-2 is
correctly framed as "[peer] said," and every Titan-side claim is clearly marked as Titan's own
(AR-sourced) statement being tested against peer evidence. `peer_mentions_of_company: []` is
also independently confirmed — none of the 11 transcripts mentions Titan Biotech, Peptech,
Titan Media, or any unmistakable description of the company, in any of the 11 calls.

---

## PART 7: UNUSED-BUT-RELEVANT SPOT READ

Two minor items found in the transcripts that bear on Titan's claim list but were not cited
by B06:
- VIDHIING May-14-2026 call (Mihir Manek): "There was also a survey very recently that 26 out
  of the 50 states are already in a recession in the US... this came out only about last
  month" — additional macro corroboration for Claim 1's "mixed-to-weak demand" finding.
  Not cited; the claim is already well-supported without it. MINOR, industry-context miss.
- VIDHIING Nov-13-2025 call: the "MAHA" political-risk narrative on synthetic-vs-natural food
  colors is a real, quantified risk (natural colors "increase the coloring budget... by at
  least 20 times") that is peer-specific and not obviously transferable to Titan's
  peptone/culture-media business. Correctly left out; noting it as considered-and-excluded
  rather than missed. Not a finding.

No directly claim-relevant peer statement was found unused.

---

## SUMMARY

- 11 of 11 transcripts genuinely contributed real, verifiable, traceable evidence somewhere
  in B06 — the "no-concall" bar (every transcript must earn its SUBSTANTIVE tag) is met at
  the peer-company level.
- Verdict discipline (Part 4) is clean: no single-peer VERIFIED, no verdict invented from
  silence, all 6 peer_questions addressed.
- The defect is concentrated in citation precision: 4 of 11 `peer_coverage_map` rows credit
  a call with content that is actually from a sibling call by the same peer, and 6 further
  quotes/figures in Parts 1-2 carry a wrong call-date or wrong-speaker attribution (Findings
  5-10). All are the same species of error — collapsing distinct calls or speakers from the
  same company into one citation — and none flips a verdict or fabricates a signal. Given
  that these 11 transcripts are the only management voice on this industry anywhere in the
  corpus, this pattern should be corrected before the citations are relied on further
  downstream (e.g., if Stage 11/FTTCP quotes these anchors directly).
- One likely corpus-extraction artifact (Finding 11) — duplicated Q&A block with a
  management-roster mismatch across two ADVENZYMES transcript files — should be checked
  against the source PDFs; it is not charged against B06 but explains part of the
  misattribution pattern.

```yaml
stage: B12d
company: "TITANBIO"
run_date: "2026-09-16"
model: claude-sonnet-5
status: complete
peers_audited: 11
substantive_confirmed: 11
substantive_unsupported: []
unused_but_relevant:
  - {peer: "VIDHIING", missed_item: "'26 of 50 US states in recession' macro color (Mihir Manek, May-14-2026 call) corroborating Claim 1 demand-weakness finding", anchor: "VIDHIING Q4/FY26 call, May-14-2026, Mihir Manek"}
claims_all_addressed: true
verdict_discipline_fails: []
findings:
  - {severity: "MAJOR", location: "B06 peer_coverage_map row: ADVENZYMES Feb-04-2026 (Q3/9M FY26)", claimed: "row credits this call with 'EFSA approval timelines'", source_truth: "Feb-04-2026 transcript contains no EFSA content at all; the EFSA/'2014' quote is in the Aug-12-2026 transcript", note: "coverage-map per-call attribution error, not a fabrication; peer overall still SUBSTANTIVE on other genuine content from this call"}
  - {severity: "MAJOR", location: "B06 peer_coverage_map row: ADVENZYMES May-12-2026 (Q4/FY26)", claimed: "row credits this call with 'Nutrazyme/Wellfa disclosed small revenue'", source_truth: "'Nutrazyme'/'Wellfa' do not appear anywhere in the May-12-2026 transcript; content is genuinely in the Nov-13-2025 transcript (also anomalously duplicated into the Feb-04-2026 file, see Finding 11)", note: "coverage-map per-call attribution error"}
  - {severity: "MAJOR", location: "B06 peer_coverage_map row: FERMENTA Aug-17-2021 (Q1 FY22)", claimed: "row credits this call with the 'formula-priced input contract'", source_truth: "no 'formula' pricing language in the Aug-17-2021 transcript; the formula-based wool-grease pricing quote is in the Nov-17-2021 transcript", note: "coverage-map per-call attribution error"}
  - {severity: "MAJOR", location: "B06 peer_coverage_map row: FERMENTA Jun-01-2022 (Q4/FY22)", claimed: "row credits this call with 'key-account margin trade-off pattern'", source_truth: "'key account' does not appear anywhere in the Jun-01-2022 transcript; content is genuinely in the Nov-17-2021 transcript", note: "coverage-map per-call attribution error"}
  - {severity: "MAJOR", location: "B06 report, Part 2A (cross-read on demand environment)", claimed: "'let's not get into the QoQ... some quarters here and there' quote cited to Mukund Kabra, Feb-04-2026 call", source_truth: "quote is verbatim in the Aug-12-2026 transcript, not the Feb-04-2026 transcript", note: "underlying point (management avoids QoQ characterisation) independently supported elsewhere; citation date is wrong"}
  - {severity: "MAJOR", location: "B06 report, Part 1 Claim 4", claimed: "'still waiting from 2014' EFSA quote cited to Mukund Kabra, Feb-04-2026 call", source_truth: "quote is verbatim in the Aug-12-2026 transcript; Feb-04-2026 transcript has no EFSA content", note: "same underlying misattribution as coverage-map finding 1 above"}
  - {severity: "MAJOR", location: "B06 report, Part 1 Claim 2", claimed: "naphthalene raw-material substitution quote attributed to Mihir Manek, Jun-12-2024 call", source_truth: "spoken by Mitesh Manek (CFO) in the transcript; Mihir Manek only asks the preceding question", note: "call and content correct, speaker wrong"}
  - {severity: "MAJOR", location: "B06 report, Part 1 Claim 2", claimed: "'inflationary trends and volatile freight markets' attributed to Bipin Manek, May-14-2026 call", source_truth: "spoken by Mitesh Manek in his financial-highlights section, not Bipin Manek", note: "call correct, speaker wrong"}
  - {severity: "MAJOR", location: "B06 report, Part 2B", claimed: "'we have not reduced a penny on our pricing' attributed to Mihir Manek, Nov-13-2025 call", source_truth: "spoken by Mitesh Manek answering Lala Ram's question, not Mihir Manek", note: "call correct, speaker wrong"}
  - {severity: "MAJOR", location: "B06-peers.yaml, contradicted[1].quote_anchor", claimed: "18-month commissioning + Rs75-85cr capex/Rs125-150cr revenue both attributed to 'Mihir Manek, May-14-2026 call' as one statement", source_truth: "18-month commissioning answered by Bipin Manek/Mitesh Manek in one exchange; Rs75-85cr/Rs125-150cr figures given by Mihir Manek in a separate, later exchange", note: "figures correct, two distinct speakers/exchanges merged into one attribution"}
  - {severity: "MINOR", location: "Corpus: ADVENZYMES-Concall_Nov_2025_Transcript.txt and ADVENZYMES-Concall_Feb_2026_Transcript.txt", claimed: "n/a - data integrity flag, not a B06 finding", source_truth: "identical Ravi Purohit/Nutrazyme/Wellfa Q&A block, including 'Vasant Rathi' speaking despite not being on the Nov-13-2025 call's stated management roster, appears verbatim in both extracted files", note: "likely extraction/page-duplication artifact; recommend re-checking against source PDFs before further downstream reliance; explains part of the misattribution pattern above"}
  - {severity: "MINOR", location: "B06 report, Part 1 Claim 1", claimed: "'mixed... some flat' quote attributed to 'Beni Rauka/Mukund Kabra, Feb-04-2026 call'", source_truth: "quote is solely Mukund Kabra's scripted opening remarks; Beni Rauka does not speak this line", note: "imprecise joint attribution, cosmetic"}
critical_count: 0
major_count: 10
minor_count: 2
acceptance_rate: 64
```
