# STAGE 12D — VERIFIER D: PEER COVERAGE AUDIT
Company: RAPPID | Run date: 2026-09-19 | Model: claude-sonnet-5

Scope: did B06 actually USE the 8 peer transcripts provided (KSB x4,
Atam Valves x3, Quest Flow Controls/Meson Valves India Ltd x1), and does
every claim in B05's peer_questions carry a real verdict on real evidence?
Note: the task brief and prompt text reference "12 peer transcripts";
only 8 exist in inputs/peer-concalls/ for this run (B06 itself documents
Marine Electricals as dropped for no filed transcript and no pure-play
marine-valve peer existing). This audit covers the 8 actually supplied,
matching what B06 had to work with.

---

## PART 1: COVERAGE AUDIT PER PEER (Rule 2)

Every peer B06 marks SUBSTANTIVE was checked: locate the cited quote,
confirm it exists in that peer's own transcript file.

| Peer / quarter | B06 usage | Citation checked | Found in transcript? | Note |
|---|---|---|---|---|
| ATAM Apr-2024 | SUBSTANTIVE | "90 to 120 days" credit period; "No PSUs, no L1 bidding"; "put on hold" MSME quote; 96,000 pcs/month at 85% | YES, all four, verbatim | Page anchors off (see Part 2) |
| ATAM Nov-2023 | SUBSTANTIVE | Rs30cr bathware capex; PAT target "12% to 13%" | YES, both, verbatim | — |
| ATAM Jul-2024 | SUBSTANTIVE | Q1 "EBITDA margins were 13%"; 35-40% two-year growth guidance | YES, both, verbatim | — |
| KSB Sep-2025 (Q2 CY25) | SUBSTANTIVE | "net working capital more than 120 days"; competitor "development order"; Sinnar/Shirwal capex; attrition 9-10% vs industry >15% | YES, all four, verbatim | Two page anchors wrong (see Part 2), one materially so |
| KSB Nov-2025 (Q3 CY25) | SUBSTANTIVE | Gross margin "54% to 44%, 43%" vs EBITDA "12% to 14%"; "close to 85% kind of utilization" | YES, both, verbatim | One page anchor off by 2 |
| KSB Mar-2026 (Q4 CY25) | SUBSTANTIVE | "payment becomes receivable only after you have uploaded..." portal mechanism | YES, verbatim | — |
| KSB Aug-2026 (Q2 CY26) | SUBSTANTIVE | "given foundries maybe in the range also of 12% to 15%... single-digit"; "already at 80% to 90%"; Mahesh Bhave receivable/solar/state-government answer; PTR/GeM/EIL mechanics | YES, all four, verbatim | Three page anchors off (see Part 2) |
| Quest Flow Controls (Meson Valves India Ltd), Jun-2024 | SUBSTANTIVE | EBITDA 24.96%/23.61%, PAT 14.85%/14.3%; India/global valve TAM figures ($80.4bn->$99.8bn, $2.6bn->$3.7bn); "almost 100%" utilization / Amrit Kaal 2047 domestic-shipbuilding language; CIN/BSE-code naming clarification | YES, all, verbatim, including the CIN (U29299GA2016PLC012972) and BSE code (543982) B06 uses for the naming note | Source transcript carries **no page markers at all** — every "p.X" citation to this peer is a number that does not exist in the source (see Part 2) |

**Result: 8 of 8 peers correctly classified SUBSTANTIVE. Zero UNUSED or
CITED-ONLY peers in B06 to test under Rule 3, so no findings arise there**
(spot-read below covers the residual "was there material B06 should have
used and did not" question independently of that binary).

---

## PART 2: ANCHOR-PRECISION FINDINGS (page numbers, not content)

Every content match above is a genuine, verbatim quote correctly
attributed to the right speaker in the right transcript. The problem
found is narrower and specific to page numbers:

**KSB and ATAM files carry literal "Page N of M" markers printed in the
text.** Checking B06's cited page against the actual marker position:

| # | File | B06 quote (short) | B06 cited page | Actual page (by file's own marker) | Off by |
|---|---|---|---|---|---|
| 1 | ATAM-Apr-2024 | "90 to 120 days" credit period | p.6 | p.5 | 1 |
| 2 | ATAM-Apr-2024 | "No PSUs, no L1 bidding" | p.14 | p.13 | 1 |
| 3 | KSB-Sep-2025 | "net working capital more than 120 days?" | p.11 | p.10 | 1 |
| 4 | KSB-Sep-2025 | "one of our competitors has a development order" | p.16 | p.11 | **5** |
| 5 | KSB-Aug-2026 | "given foundries...12% to 15%...single-digit" | p.24 | p.23 | 1 |
| 6 | KSB-Aug-2026 | "already at 80% to 90% capacity utilization" | p.9 | p.7 | 2 |
| 7 | KSB-Aug-2026 | Mahesh Bhave receivable/solar/state-government answer | p.29-30 | p.27 | 2-3 |
| 8 | KSB-Nov-2025 | "close to 85% kind of utilization" | p.39 | p.37 | 2 |

Finding #4 checked specifically for a possible duplicate/second mention
near the cited page 16 (KSB-Sep-2025, lines 906-935): that page discusses
Navy/marine qualification, BP&CL, and vertical turbine pumps, not the
competitor development-order exchange, which sits five pages earlier
(line 646, page 11, speaker Nitin Patil, confirmed correct on content and
speaker). This is not a rounding slip; the cited page holds unrelated
content.

**Quest Flow Controls (Meson Valves India Ltd) — systemic anchor
problem.** The source file QUESTFLOW-Concall_Jun_2024_Transcript.txt
contains zero instances of any "Page N of M" string. B06 nonetheless
cites this peer at "p.3-4," "p.3," "p.6," "p.7-8" throughout Parts 1, 2
and the YAML block. Every one of these page numbers is unverifiable
against the source because the source carries no page numbering
mechanism at all. The underlying quotes are genuine and located by
full-text search (confirmed above), so this is not a fabricated
finding — but the specific page anchor on every Quest Flow citation is
a number invented for a document that does not print one. Quest Flow is
the single most consequential peer in this report (it drives the sole
FLAG-MARGIN-CONTRADICTION and the Part 5 cross-peer hypothesis), which
raises this from a cosmetic slip to a MAJOR finding: the report's most
load-bearing peer evidence carries no verifiable page anchor anywhere.

**Severity assignment.** Findings 1, 2, 3, 5, 6, 7, 8 are MINOR: content
is correct, speaker is correct, the quote is genuinely in the file, only
the page label is off by 1-3. Finding 4 (5-page displacement on a
material claim, KSB's own nuclear-competitor risk) and the Quest Flow
systemic non-anchor are MAJOR: neither changes what was found, but both
mean an operator or Claude web trying to jump straight to the cited page
would land on the wrong content (Quest Flow: no page numbers to jump to
at all; KSB #4: five pages into an unrelated Navy/marine discussion).

None of this changes B06's coverage classification (all 8 peers remain
correctly SUBSTANTIVE) or its verdict-per-claim table; it is an
anchor-precision defect layered on top of otherwise accurate content.

---

## PART 3: SPOT-READ FOR MISSED MATERIAL (Rule 3, exercised as due
diligence even though no peer is UNUSED/CITED-ONLY)

Searched all 8 transcripts independently for terms tied to the six
claims that B06 marked "peers silent" on, to test whether B06's silence
calls are accurate rather than a missed reading:

- "escalation" — zero hits across all 8 files. Confirms B06's Claim 1
  "no peer... any price-escalation clause" call.
- "per vessel" / "vessel cost" — zero hits. Confirms Claim 4's framing
  that no peer isolates a per-vessel valve cost share.
- "advance" — hits found, but all in the opposite direction from
  Rappid's claim (paying a supplier 50% advance): ATAM's own export
  sales are collected "on an advanced basis" (customer pays ATAM first),
  and KSB receives customer milestone advances on nuclear pump orders
  (KSB-Concall_Sep_2025_Transcript.txt, line 1501-1503; KSB-Concall_Nov_
  2025_Transcript.txt, line 1849). Neither describes a buyer paying a
  raw-material supplier in advance, so these do not contradict B06's
  Claim 6 UNVERIFIABLE call; they are a different transaction direction
  and immaterial to the specific claim tested. Correctly not cited.

No unused-but-relevant material found. B06's "peers silent" calls hold up
under independent search.

---

## PART 4: VERDICT-DISCIPLINE AUDIT (Rule 4)

B06 marks **zero** claims VERIFIED (verified: [] in the block). The
"any VERIFIED resting on one peer is MAJOR" and "any verdict upgraded
from silence is CRITICAL" tests therefore have no VERIFIED row to test
against. Checked the two PARTIALLY VERIFIED and one CONTRADICTED verdict
for the same discipline in spirit:

- Claim 1 (PSU payment terms) — PARTIALLY VERIFIED, rests on 2 peers
  (KSB + Atam Valves), both independently confirmed above. Correctly not
  over-claimed as VERIFIED given no peer names Mazagon Dock/GRSE/Cochin
  Shipyard/HSL or a naval-specific 170-day figure.
- Claim 3 (working-capital cycle) — PARTIALLY VERIFIED, same 2-peer
  basis, same discipline held.
- Claim 2 (12% margin-ceiling framing) — CONTRADICTED, resting on one
  peer (Quest Flow Controls) as the contradicting evidence, with KSB's
  imperfect-pass-through data used as a *separate*, non-contradicting
  corroboration of a different (narrower) sub-claim. This is methodologically
  sound: a CONTRADICTED verdict needs one clean counter-example, not two;
  the "any VERIFIED resting on one peer is MAJOR" rule binds VERIFIED
  claims, not CONTRADICTED ones, and is not violated here. No downgrade
  warranted.

No verdict-discipline failures found.

---

## PART 5: CLAIM-COVERAGE CHECK (Rule 5)

B05's injected `peer_questions[]` contains 6 questions. B06 Part 1
addresses all 6 in order (Claims 1-6), each with a stated verdict
(PARTIALLY VERIFIED x2, CONTRADICTED x1, UNVERIFIABLE x3). No skipped
claim found.

---

## PART 6: FINDINGS TABLE

| Severity | Location | Finding |
|---|---|---|
| MAJOR | B06 all Quest Flow Controls citations (Part 1 Claims 2/4, Part 2A/2B/2C, Part 5, YAML flags/contradicted) | Every page anchor cited for this peer ("p.3-4," "p.3," "p.6," "p.7-8") references a page-numbering system the source transcript does not contain (zero "Page N of M" markers in QUESTFLOW-Concall_Jun_2024_Transcript.txt). Content of every checked quote is verbatim-accurate; only the anchor is unverifiable. Material because Quest Flow is the sole basis for the report's one FLAG and its central cross-peer hypothesis. |
| MAJOR | B06 Part 2D, "KSB-Concall_Sep_2025_Transcript.txt, p.16, Nitin Patil" | Cited page (p.16, lines ~906-935) discusses Navy-qualification/BP&CL/turbine-pump content, not the "development order" exchange. Correct location is p.11 (line 646). Content and speaker attribution are otherwise accurate. |
| MINOR | ATAM-Concall_Apr_2024_Transcript.txt, B06 Claim 1, "p.6" | Actual page 5 (off by 1). |
| MINOR | ATAM-Concall_Apr_2024_Transcript.txt, B06 Claim 1, "p.14" | Actual page 13 (off by 1). |
| MINOR | KSB-Concall_Sep_2025_Transcript.txt, B06 Claim 1, "p.11" | Actual page 10 (off by 1). |
| MINOR | KSB-Concall_Aug_2026_Transcript.txt, B06 Claim 2 / 2B, "p.24" | Actual page 23 (off by 1). |
| MINOR | KSB-Concall_Aug_2026_Transcript.txt, B06 Claim 5, "p.9" | Actual page 7 (off by 2). |
| MINOR | KSB-Concall_Aug_2026_Transcript.txt, B06 Claim 1, "p.29-30" | Actual page 27 (off by 2-3). |
| MINOR | KSB-Concall_Nov_2025_Transcript.txt, B06 Claim 5, "p.39" | Actual page 37 (off by 2). |

Critical: 0. Major: 2. Minor: 7.

---

## PART 7: OVERALL

Peer coverage itself is genuinely strong: 8 of 8 provided transcripts
were read and used substantively, every SUBSTANTIVE citation checked
resolves to a real, verbatim quote from the correct speaker, the
"peers silent" calls hold up under independent re-search, all 6 injected
peer questions received a verdict, and verdict discipline (no VERIFIED
claim over-relying on one peer, no upgrade from silence) is intact. The
finding set is entirely about anchor precision, not fabrication or
missed coverage: eight page-number mismatches, two material enough
(5-page displacement onto unrelated content; and a peer with no page
numbering at all standing behind the report's single flag) to name as
MAJOR rather than cosmetic. Recommend the page anchors on the two MAJOR
items be corrected before this report is relied on for a live citation
jump, and that Quest Flow citations be re-anchored to paragraph or
speaker-turn markers since no page numbers exist in that source file.

```yaml
stage: B12d
company: "RAPPID"
run_date: "2026-09-19"
model: claude-sonnet-5
status: complete
peers_audited: 8
substantive_confirmed: 8
substantive_unsupported: []
unused_but_relevant: []
claims_all_addressed: true
verdict_discipline_fails: []
findings:
  - {severity: "MAJOR", location: "B06 Quest Flow Controls citations (Claims 2/4, Part 2A-2C, Part 5, YAML)", claimed: "page anchors p.3-4 / p.3 / p.6 / p.7-8", source_truth: "QUESTFLOW-Concall_Jun_2024_Transcript.txt contains zero page markers; quoted content itself is verbatim-accurate", note: "most consequential peer (sole basis for the report's one FLAG) has unverifiable anchors throughout; content not disputed"}
  - {severity: "MAJOR", location: "B06 Part 2D, KSB-Concall_Sep_2025_Transcript.txt citation", claimed: "p.16", source_truth: "p.11 (line 646); p.16 (lines 906-935) covers unrelated Navy/BP&CL/turbine-pump content", note: "5-page displacement; quote and speaker (Nitin Patil) otherwise correct"}
  - {severity: "MINOR", location: "B06 Claim 1, ATAM-Concall_Apr_2024_Transcript.txt", claimed: "p.6", source_truth: "p.5", note: "off by 1 page, content verbatim-correct"}
  - {severity: "MINOR", location: "B06 Claim 1, ATAM-Concall_Apr_2024_Transcript.txt", claimed: "p.14", source_truth: "p.13", note: "off by 1 page, content verbatim-correct"}
  - {severity: "MINOR", location: "B06 Claim 1, KSB-Concall_Sep_2025_Transcript.txt", claimed: "p.11", source_truth: "p.10", note: "off by 1 page, content verbatim-correct"}
  - {severity: "MINOR", location: "B06 Claim 2 / 2B, KSB-Concall_Aug_2026_Transcript.txt", claimed: "p.24", source_truth: "p.23", note: "off by 1 page, content verbatim-correct"}
  - {severity: "MINOR", location: "B06 Claim 5, KSB-Concall_Aug_2026_Transcript.txt", claimed: "p.9", source_truth: "p.7", note: "off by 2 pages, content verbatim-correct"}
  - {severity: "MINOR", location: "B06 Claim 1, KSB-Concall_Aug_2026_Transcript.txt", claimed: "p.29-30", source_truth: "p.27", note: "off by 2-3 pages, content verbatim-correct"}
  - {severity: "MINOR", location: "B06 Claim 5, KSB-Concall_Nov_2025_Transcript.txt", claimed: "p.39", source_truth: "p.37", note: "off by 2 pages, content verbatim-correct"}
critical_count: 0
major_count: 2
minor_count: 7
acceptance_rate: 100
```
