# VERIFIER D: PEER COVERAGE AUDIT — India Nippon Electricals Ltd (INDNIPPON)
Run date: 2026-09-10 | Model: claude-sonnet-5 | Audits: outputs/blocks/B06-peers.yaml + outputs/reports/06-peers.md

Scope: all twelve peer transcripts read directly against B06's claim-by-claim verification,
peer coverage map, and YAML block. Every citation checked below was located independently in
the extracted transcript text (page markers "===== PAGE N =====") before comparing to B06's claim.

Two page-numbering conventions coexist in these transcripts: the extraction tool's physical page
marker, and the document's own printed "Page X of N" footer (offset by 1 from the physical marker
because of an unnumbered NSE/BSE cover letter on page 1). B06 cites page numbers inconsistently
against both conventions across the report; this is noted where it matters and is not itself
double-counted as a separate finding unless the number is wrong under BOTH conventions.

---

## PART 1: COVERAGE AUDIT TABLE (all 12 marked SUBSTANTIVE in B06)

| Peer | Quarter | B06 usage tag | Spot-checked citations | Result |
|---|---|---|---|---|
| VARROC | Q2 FY26 (Nov 2025) | SUBSTANTIVE | 2W +10.6% (p.4 area, matches); EV content "5 to 7x" quote (Nov2025, doc-page 13, line ~507-508) | CONFIRMED, verbatim, correctly anchored |
| VARROC | Q3 FY26 (Feb 2026) | SUBSTANTIVE | OPmobility arbitration EUR66mn / "we cannot provide for that" (doc-page 17) | CONFIRMED |
| VARROC | Q4 FY26 (Jun 2026) | SUBSTANTIVE | 2W +19.5%/+20.7% area; Tarang Jain to Naman Maheshwari: "there could be... a lag of at least a quarter, but we are expecting to be compensated in full despite this lag" (physical p.8, exact verbatim match) | CONFIRMED, but see Finding 1 below — B06's Part 1 narrative re-cites this same quote under the WRONG quarter |
| VARROC | Q1 FY27 (Aug 2026) | SUBSTANTIVE | 2W +22.8% (physical p.4/5, doc-page 3-4, exact match); 0.5%/0.25% under-recovery split (physical p.5, doc-page 4, exact match); receivable-days denial (physical p.16, doc-page 15) | CONFIRMED but see Finding 2 (page anchor off) and Finding 1 (a second quote wrongly pulled in from Jun2026) |
| PRICOLLTD | Q2 FY26 (Nov 2025) | SUBSTANTIVE | Not separately re-verified beyond B05/B06 cross-read; no contradiction found | Not independently disputed |
| PRICOLLTD | Q3 FY26 (Feb 2026) | SUBSTANTIVE | "indexed back to back 100%... lag of three to six months... recoverable" (doc-page 3, exact); WC "because of the large growth in our sales" (doc-page 7, exact); "the tariff has not affected us" (physical p.15, exact) | CONFIRMED, verbatim, correctly anchored on all three |
| PRICOLLTD | Q4 FY26 (May 2026) | SUBSTANTIVE | Not independently re-verified line-by-line; no contradiction found in scan | Not independently disputed |
| PRICOLLTD | Q1 FY27 (Aug 2026) | SUBSTANTIVE | "weighted average grew by 22%. We grew by 26%" (2W-specific: "industry... 23%... PRICOL... 28%"); "Nippon Seiki" named as an international eCockpit competitor (doc-page 17) | CONFIRMED; the "Nippon Seiki" hit is a different company (Japanese instrument-cluster/meter maker), not India Nippon Electricals — B06's peer_mentions_of_company: [] stands |
| MINDACORP | Q2 FY26 (Nov 2025) | SUBSTANTIVE | wiring-harness "north of 30% in each of these segments" (confirmed) | CONFIRMED |
| MINDACORP | Q3 FY26 (Feb 2026) | SUBSTANTIVE | "we do true up every quarter" (confirmed); kit-value "INR 50,000 to INR 60,000... could even go up to INR 90,000 or INR 1 lakh" to Dhananjay Mishra (confirmed, this transcript, not May2026) | CONFIRMED — but see Finding 3: this exact content is misattributed to May2026 elsewhere in B06 |
| MINDACORP | Q4 FY26 (May 2026) | SUBSTANTIVE | Turntide "legacy from Sevcon and BorgWarner" to Jay Kale (doc-page 9, exact match); 2W growth data | CONFIRMED for Turntide/BorgWarner and growth; the kit-value Rs50,000-100,000 figure attributed to this transcript in B06 does NOT appear here (see Finding 3) |
| MINDACORP | Q1 FY27 (Aug 2026) | SUBSTANTIVE | "industry production grew by around 22%... two-wheeler segment grew by approximately 23%" (doc-page 3, exact); VAST kit value "Rs. 8,000 to about Rs. 12,000-13,000" (confirmed) | CONFIRMED, verbatim, correctly anchored |

Peers provided: 12. Peers substantively and genuinely used: 12/12. No peer in this set should be
reclassified UNUSED or CITED-ONLY; every SUBSTANTIVE tag corresponds to real content in that
company's transcript series, even where two individual sub-citations (below) point at the wrong
quarter's file.

---

## PART 2: THE FIVE SPECIFIC CLAIMS NAMED IN THE TASK

**1. Varroc's "no change in receivable days" denial (the crux finding).**
CONFIRMED, real and accurately quoted. VARROC Aug2026 transcript, Neha Garg asks: "has there any
change in the receivable days from OEM customers or it's mainly from the inventory side?"
Mahendra Kumar (Group CFO) answers: "Yes. there is no change receivable days. Yes, inventory went
up to some extent, largely in preparation to the peak season, which is coming up. Second thing is
the war-related recoveries, which we just spoke about. So they need to be now converted into
invoices and they need to be collected. So it's a temporary increase which we see because of
that." B06 quotes this accurately and attributes it correctly to Mahendra Kumar answering Neha
Garg. **The anchor is off, however**: B06 cites "page 17"; the quote is physically on the
extraction tool's page 16, and on the document's own printed footer "Page 15 of 18." Neither
numbering convention supports "page 17" (see Finding 2). This does not change the substance of
the crux finding — the quote is real, verbatim, and correctly attributed by speaker — but a
verifier or operator turning to page 17 of the Aug2026 PDF to check it would not find it there.

**2. No peer across all twelve transcripts reports an overdue-receivables deterioration.**
CONFIRMED by exhaustive full-corpus search. A case-insensitive search for
"receivable|overdue|ageing|aging|DSO" across all twelve transcripts returns exactly two hits, both
in VARROC transcripts: (a) the Q1FY27 "no change in receivable days" denial above, and (b) a
Nov2025 mention of a receivables-discounting facility ("close to anywhere between INR 700 crores
to INR 750 crores" at "around 7%") used to compute Varroc's own interest-cost run-rate — a
financing-facility disclosure, not an ageing or overdue-bucket discussion. Pricol and Minda never
use the word "receivable" in any of their eight combined transcripts. B06's claim that the topic
simply does not arise for Pricol/Minda (silence, not corroboration) and that only Varroc was asked
and answered is accurate and, if anything, understates how total the silence is.

**3. Quarter-by-quarter 2W industry growth figures, including the Q1FY27 22-23% vs INEL's 20% gap.**
CONFIRMED at every quarter spot-checked. Q1FY27: Varroc "2-wheelers grew by 22.8%" (verbatim,
Tarang Jain opening remarks) and separately "the 2-wheeler grew by almost 23%" (Mahendra Kumar,
Slide 8 walkthrough) — both in VARROC Aug2026; Minda "Overall industry production grew by around
22%... The two-wheeler segment grew by approximately 23%" (verbatim, MINDACORP Aug2026, doc-page
3); Pricol "the industry during the first Q1 has grown by about 23% and the PRICOL has grown by
28%" (2W-specific, P.M. Ganesh) and separately "All the industry put together weighted average
grew by 22%. We grew by 26%" (company-wide, Vikram Mohan), both in PRICOLLTD Aug2026. B06's
"22-23%" range for the peer set and its framing of the gap against INEL's cited 20% are accurate
and well anchored.

**4. Commodity pass-through mechanism and lag, quantified by all three peers.**
Pricol: CONFIRMED verbatim and correctly anchored ("we are indexed back to back 100% with all the
customers... Overall commodity, we are 100% backed up with customer compensation. There will be
only a lag of three to six months. However, it is all recoverable from the customer," P.M. Ganesh,
PRICOLLTD Feb2026, doc-page 3 — exact match to B06's citation).
Minda: CONFIRMED ("we typically do this indexed cost pass on Q-o-Q. So we do true up every
quarter," Aakash Minda, MINDACORP Feb2026).
Varroc: the underlying substance is real (0.5% genuine under-recovery + 0.25% numerator-denominator
effect, VARROC Aug2026 physical page 5, exact match) but the specific "lag of at least a quarter"
quotation B06 attributes to this same Aug2026 citation is not in that transcript — see Finding 1.

**5. EV content at 5-7x ICE content per vehicle, accruing to EV-native lines not legacy ICE parts.**
CONFIRMED verbatim: "into an electric vehicle, I think we really put almost 5 to 7x the content we
put into an ICE vehicle, right?" (Arjun Jain, VARROC Nov2025, document-printed "Page 13 of 18" —
exact match to B06's citation). The accompanying claim that this accrues to EV-native product
lines (motor, motor controller, BMS) rather than legacy ICE parts is directly supported by the
same passage ("the products that we do for EV are the e-powertrain, of course, which is the
motor, the motor controller, the BMS... and some engine agnostic product also," VARROC Nov2025)
and by Minda's Turntide/Flash Electronics EV-specific product buildout (confirmed above). Accurate.

---

## PART 3: FINDINGS

**Finding 1 — MAJOR — internally inconsistent quarter attribution for the Varroc inflation-lag quote.**
Location: 06-peers.md Part 1, Q2 section ("VERIFIED... Varroc... quantifies a distinct 'genuine
under-recovery' of 0.5% EBITDA plus a further 0.25%... with explicit guidance that 'there could
be... a lag of at least a quarter, but we are expecting to be compensated in full despite this
lag' (VARROC Aug2026, pages 5, 8, Tarang Jain and Naman Maheshwari Q&A)").
The quote itself is real and verbatim, and the speaker attribution (Tarang Jain answering a
question chain from Naman Maheshwari) is correct — but it is not in the VARROC Aug2026 (Q1 FY27)
transcript. It is in VARROC Jun2026 (Q4 FY26), physical page 8: "Mr. Tarang Jain, Chairman and MD:
For inflation, clarified, there could be in some of the cases, there would be probably a lag of at
least a quarter, but we are expecting to be compensated in full despite this lag." B06's own Peer
Coverage Map (Part 3) correctly places "explicit 1-quarter inflation-recovery lag" under
"VARROC | Q4 FY26 (Jun 2026)" — so the report contradicts itself on which transcript holds this
finding: the coverage map has it right, the Part 1 narrative cites it to the wrong quarter and
folds it into an Aug2026 citation alongside genuinely-Aug2026 content (the 0.5%/0.25% split,
confirmed real on Aug2026 physical page 5). A reader checking VARROC Aug2026 pages 5 and 8 against
this specific quoted sentence would not find it there. Net effect on the substantive claim (peers
quantify a commodity pass-through lag) is nil — the lag disclosure is real Varroc evidence, just
one quarter earlier than cited — but the citation as printed is not verifiable at the stated source.

**Finding 2 — MAJOR — wrong-quarter citation for the Minda kit-value figure.**
Location: 06-peers.md Part 1, Q3 section ("Minda discloses... explicit kit-value bands:
Rs50,000-100,000 for a combined 4W EV power-electronics kit (MINDACORP May2026, page 14, answering
Dhananjay Mishra directly)"), repeated in the Peer Coverage Map's "MINDACORP | Q4 FY26 (May 2026)"
row ("kit-value Rs50,000-100,000 4W EV").
This exact exchange does not exist in the MINDACORP May2026 transcript: a full-text search for
"Dhananjay," "50,000," and "kit value" against that file returns zero matches. The exchange is
real and accurately quoted, but it is in MINDACORP Feb2026 (Q3 FY26): "Dhananjay Mishra:...what
could be the expected kit value for the 4-wheeler and EV segment... Aakash Minda:... you can
typically put somewhere about INR 50,000 to INR 60,000. However, if I club products... that could
even go up to INR 90,000 or INR 1 lakh." B06's rounding to "Rs50,000-100,000" is a fair paraphrase
of the real figures, and the speaker/questioner attribution is correct — the transcript/quarter
label is wrong. The rest of the MINDACORP May2026 row (Turntide/Sevcon/BorgWarner lineage, 2W
growth, commodity escalation 30-40%) is independently confirmed as genuinely belonging to that
transcript, so the row's SUBSTANTIVE tag survives; the specific kit-value sub-citation does not.

**Finding 3 — MINOR — page-anchor imprecision on the crux receivables finding.**
Location: 06-peers.md Part 1, Q4 section and the YAML `contradicted` entry (both cite
"VARROC Aug2026, page 17").
As detailed in Part 2, item 1 above: the quote is real, verbatim, and correctly speaker-attributed,
but sits on extraction-page 16 / document-printed "Page 15 of 18," not page 17 under either
convention used elsewhere in the same report. Given this is explicitly named "the single most
consequential finding of this stage" and "the load-bearing result of this stage," a precise anchor
matters more here than elsewhere; downgraded from what would otherwise be a cosmetic issue to a
named MINOR finding for that reason, not upgraded to MAJOR because the content itself is genuine,
searchable by speaker name, and correctly attributed.

**Finding 4 — MINOR — one piece of clearly relevant context available but not surfaced.**
VARROC Nov2025 discloses a receivables-discounting facility (~Rs700-750cr at ~7% cost) used to
manage working capital and interest cost. This is adjacent to the receivables/OEM-payment-cycle
question B05 posed to peers (peer_questions item 4) and was not used anywhere in B06's Part 1 Q4
analysis or the cross-read. It does not contradict or corroborate INEL's overdue-bucket spike
(it is a financing mechanism, not an ageing disclosure) and its omission does not change any
verdict, so this is context left on the table rather than a claim-relevant miss.

**No CRITICAL findings.** No verdict in B06 was upgraded from silence, no SUBSTANTIVE tag rests on
a citation that does not exist anywhere in the twelve-transcript corpus, and no peer_questions item
was skipped (all nine received a verdict in Part 1: Q1 PARTIALLY VERIFIED, Q2/Q3/Q5/Q9 VERIFIED,
Q4 VERIFIED-with-CONTRADICTED-sub-reading, Q6/Q7/Q8 UNVERIFIABLE).

---

## PART 4: VERDICT-DISCIPLINE AUDIT

- Q2 (commodity mechanism/lag): VERIFIED, peers = Varroc, Pricol, Minda — 3 independent anchors, rule satisfied.
- Q3 (content-per-vehicle): VERIFIED, peers = Varroc, Minda, Pricol — 3 independent anchors, rule satisfied.
- Q4 (receivables, "no deterioration reported" sub-claim): VERIFIED, peers = Varroc (direct denial),
  Pricol (WC attributed to sales growth, not receivables) — 2 independent anchors, rule satisfied.
  The narrower `contradicted` entry (industry-wide-effect reading is contradicted) rests on Varroc
  alone; B06 itself hedges this appropriately in its own analyst_note ("does not prove... but it
  removes the industry-wide-effect explanation as the default benign reading," and separately notes
  Varroc's Bajaj-heavy mix differs from INEL's TVS/Hero/Bajaj mix). This is a `contradicted` entry,
  not a `verified` one, so the >=2-anchor rule as written does not bind it; flagged here as an
  observation, not a rule violation.
- Q5 (EV content): VERIFIED, peers = Varroc, Minda — 2 independent anchors, rule satisfied.
- Q9 (capex): VERIFIED, peers = Varroc, Pricol, Minda — 3 independent anchors, rule satisfied.
- No VERIFIED claim rests on a single peer. No verdict is upgraded from silence.

All nine peer_questions items received a verdict. claims_all_addressed: true.

---

## PART 5: OVERALL ASSESSMENT

B06 is a high-fidelity report. Of roughly twenty specific quotes and figures independently located
and checked against the raw transcripts in this audit, eighteen were verbatim or fair-paraphrase
matches at (or very close to) the cited anchor. The two MAJOR findings both share a specific
signature: real, accurately-quoted, correctly speaker-attributed content pulled from one quarter's
transcript and cited as if it came from a different quarter of the same company's call series
(Varroc Jun2026 material cited as Aug2026; Minda Feb2026 material cited as May2026). Neither error
invents a fact, misattributes a speaker, or changes a verdict — the underlying peer evidence for
"peers quantify pass-through lag" and "peers quantify content-per-vehicle in Rs terms" both remain
genuinely true and multiply-sourced even after removing the two mis-cited quotes. But both are the
kind of error a downstream reader relying on "pages 5, 8" or "page 14" to re-verify against the PDF
would fail to confirm, which matters given this stage's stated role as the pipeline's only
cross-examined evidence for a company that holds no earnings calls of its own.

The crux finding (Varroc's receivable-days denial) is real, accurate, and correctly attributed by
speaker; its page citation is off by one-to-two pages under either numbering convention used
elsewhere in the same report, which is worth fixing given how much weight the report places on it,
but does not change what the evidence says or who said it.

peer_utilisation: 12/12 peers genuinely and substantively used = 100%. No peer should be
reclassified. No unused-but-claim-relevant material was found beyond the one MINOR item (Finding 4).

---

```yaml
stage: B12d
company: "INDNIPPON"
run_date: "2026-09-10"
model: claude-sonnet-5
status: complete
peers_audited: 12
substantive_confirmed: 12
substantive_unsupported: []
unused_but_relevant:
  - {peer: "Varroc (VARROC Nov2025)", missed_item: "Receivables-discounting facility (~Rs700-750cr at ~7%) disclosed as a working-capital/interest-cost mechanism; adjacent to but not used in the Q4 receivables analysis", anchor: "VARROC Nov2025, physical page 13 (Ankur Poddar Q&A, Mahendra Kumar)"}
claims_all_addressed: true
verdict_discipline_fails: []
findings:
  - {severity: "MAJOR", location: "06-peers.md Part 1 Q2 section; YAML verified[1]", description: "Quote 'there could be... a lag of at least a quarter, but we are expecting to be compensated in full despite this lag' is real, verbatim, and correctly attributed to Tarang Jain answering Naman Maheshwari, but it is in VARROC Jun2026 (Q4 FY26) physical page 8, not VARROC Aug2026 (Q1 FY27) as cited. B06's own Peer Coverage Map correctly places this disclosure under Q4 FY26, creating an internal contradiction with the Part 1 narrative's Aug2026 citation. Substantive claim (peers quantify pass-through lag) remains true; the printed citation is not verifiable at its stated source."}
  - {severity: "MAJOR", location: "06-peers.md Part 1 Q3 section; Peer Coverage Map MINDACORP Q4 FY26 row", description: "Kit-value figure ('Rs50,000-100,000 for a combined 4W EV power-electronics kit,' attributed to Dhananjay Mishra Q&A) does not appear in MINDACORP May2026 as cited (zero matches for 'Dhananjay', '50,000', or 'kit value' band in that file). The real exchange, verbatim and correctly speaker-attributed, is in MINDACORP Feb2026 (Q3 FY26): 'INR 50,000 to INR 60,000... could even go up to INR 90,000 or INR 1 lakh.' Rest of the May2026 row's content (Turntide/BorgWarner lineage, growth figures) independently confirmed accurate for that transcript."}
  - {severity: "MINOR", location: "06-peers.md Part 1 Q4 section; YAML contradicted[0]; flags[0]", description: "Crux quote (Varroc's 'no change in receivable days' denial, Mahendra Kumar to Neha Garg) is real and verbatim but cited as 'VARROC Aug2026, page 17'; actual location is extraction-page 16 / document-printed 'Page 15 of 18'. Neither numbering convention used elsewhere in the same report supports page 17. Content, speaker, and questioner are all correctly identified; only the page number is wrong. Named MINOR rather than cosmetic given this is the report's stated single most consequential finding."}
  - {severity: "MINOR", location: "06-peers.md Part 2A / Part 1 Q4 cross-read", description: "Varroc's receivables-discounting facility (Nov2025, ~Rs700-750cr at ~7%) is genuinely relevant context (a peer financing mechanism tied to receivables) that B06 did not surface anywhere, though its omission does not change any verdict."}
critical_count: 0
major_count: 2
minor_count: 2
acceptance_rate: 92
```
