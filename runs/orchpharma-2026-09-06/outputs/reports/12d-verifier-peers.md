# VERIFIER D: PEER COVERAGE AUDIT — Orchid Pharma Ltd (ORCHPHARMA)
Run date: 2026-09-06 | Model: claude-sonnet-5 | Emits B12d

Independent audit of Stage 6 (B06-peers) against the 11 raw peer transcripts and
the B05 peer_questions list. I read all 11 transcripts myself from the clean
text extracts (`work/text/peer-concalls__*.txt`) and checked B06's citations
against them page by page.

## Mechanical framing carried into this audit

None of the three peers (NEULANDLAB, GRANULES, KOPRAN) manufactures
cephalosporins or 7-ACA. Questions 3, 4, 6, 8 in the peer_questions list ask
about cephalosporin/7-ACA-specific facts that this peer set is structurally
unable to answer. That is a peer-SELECTION limit (the corpus given to Stage 6
contains no cephalosporin producer), not a peer-UTILISATION failure by Stage 6.
I score B06 on whether it used what these three peers actually said, not on
whether cephalosporin-specific facts got confirmed — they cannot be, by this
corpus.

The three KOPRAN transcripts predate April 2025 (Nov 2024, Feb 2025, Mar 2025);
NEULANDLAB and GRANULES run Nov 2025 through Aug 2026. B06 flags this staleness
consistently and correctly throughout — confirmed.

## PART 1: COVERAGE AUDIT TABLE, PER PEER-QUARTER ENTRY

11 entries in B06's Part 3 coverage map. For each: B06's classification,
whether the cited content is real and findable, and any material gap.

| # | Peer / quarter | B06 usage | Citation spot-checked | Verdict |
|---|---|---|---|---|
| 1 | NEULANDLAB Q2 FY26 (Nov 2025) | SUBSTANTIVE | "63.7% jump... Rs. 516 crores" — found verbatim, Abhijit Majumdar, PDF p.3 (exact match to B06's "p.3") | CONFIRMED |
| 2 | NEULANDLAB Q3 FY26 (Feb 2026) | SUBSTANTIVE | "11.4% YoY... INR447.8 crores" — found verbatim, Abhijit Majumdar, PDF p.3 (B06 cites "p.2"; B06's page number matches the transcript's own internal footer "Page 2 of 18", one page behind the PDF page marker) | CONFIRMED, anchor off-by-one (MINOR, see Finding 2) |
| 3 | NEULANDLAB Q4 FY26/FY26 (May 2026) | SUBSTANTIVE | "134.9%... 37.1%... INR2053.1 crores versus INR1,497.3 crores" — found verbatim, PDF p.3 (matches B06's "p.3" exactly) | CONFIRMED |
| 4 | NEULANDLAB Q1 FY27 (Aug 2026) | SUBSTANTIVE | "growth of 16.3%" — found verbatim, PDF p.3 (matches B06's "p.3" exactly) | CONFIRMED |
| 5 | GRANULES Q2 FY26 (Nov 2025) | SUBSTANTIVE | "Rs. 12,970 million... Rs. 9,666 million... growth of 34%," plus the Gagillapur voluntary-pause context — found verbatim, Mukesh Surana, PDF p.6 (B06 cites "p.5", one page behind the internal footer "Page 5 of 14") | CONFIRMED, anchor off-by-one (MINOR) |
| 6 | GRANULES Q3 FY26 (Jan 2026) | SUBSTANTIVE | "price erosion also in paracetamol... inventory... volumes are building back up" — found verbatim, Priyanka Chigurupati, PDF p.13 (B06 cites "p.12", internal footer) | CONFIRMED, anchor off-by-one (MINOR) |
| 7 | GRANULES Q4 FY26/FY26 (May 2026) | SUBSTANTIVE | "crossed the landmark number of INR50,000 million... 6 straight quarters of sequential growth" (exact match, PDF p.6 = B06's "p.6"); "no price increases we wish we had... raw material prices have gone up" (K.P. Chigurupati, PDF p.8, B06 cites "p.7"); DCDA "Chinese competition, they started reducing prices drastically" (K.P. Chigurupati, PDF p.8, matches B06's "p.8" exactly) | CONFIRMED, one of three citations off-by-one (MINOR) |
| 8 | GRANULES Q1 FY27 (Jul 2026) | SUBSTANTIVE | "Revenue grew 22%... EBITDA... up 37%... PBT before exceptional items grew 41%" — found verbatim, PDF p.6 (B06 cites "p.5-6", range partially matches); West Asia input-cost line found verbatim, PDF p.6 (B06 cites "p.5") | CONFIRMED, anchor off-by-one on West Asia cite (MINOR) |
| 9 | KOPRAN Q2 FY25 (Nov 2024) | SUBSTANTIVE, STALE | "Penems prices have... gone down by about 25%" — found verbatim, Sanjay Dosi, PDF p.6 (B06 cites "p.5-6", range covers it) | CONFIRMED |
| 10 | KOPRAN Q3 FY25 (Feb 2025) | SUBSTANTIVE, STALE | "gradual recovery in the API business" (PDF p.3, B06 cites "p.2-3" — covers it) and "Chinese bringing down prices" (PDF p.4, matches B06's "p.4" exactly) both confirmed. BUT: the same call, same Surendra Somani answer B06 already quotes for Q4 (on fermentation-based KSMs), explicitly says: *"antibiotics, China, antibiotics are based on fermentation-based raw material, whether it is Penicillins or **Cephalosporins** or others, Tetracycline, Azithromycin, these are all fermentation based. India still has a long way to go. Maybe it will be more like a 5, 7 year time cycle"* (KOPRAN-Concall_Feb_2025_Transcript.pdf, p.7-8, Surendra Somani). This is a direct, named "Cephalosporins" mention inside a passage B06 already cites, and B06 did not surface it. | MATERIAL GAP — see Finding 1 (MAJOR) |
| 11 | KOPRAN merger-scheme investor meet (Mar 2025) | UNUSED | Full transcript read: entirely about the Kopran Laboratories-into-Kopran-Limited diagnostics merger (swap ratio, diagnostics segment economics, Aurobindo/Abbott/Siemens as diagnostics competitors). No API pricing, China, demand, or capacity content anywhere in the transcript. | CONFIRMED — UNUSED classification is correct; nothing was missed here |

**Summary: 10 of 11 entries correctly and completely handled. 1 of 11
(KOPRAN Q3 FY25 / Feb 2025) has a real, material coverage gap — Finding 1
below.**

## PART 2: FINDINGS

### Finding 1 (MAJOR) — B06's "no peer mentions cephalosporin" claim is factually wrong

B06's Q3 net read states: *"No peer transcript in the corpus mentions 7-ACA,
cephalosporin key starting materials, or per-kg cephalosporin intermediate
pricing at any point."* B06's Q4 net read states: *"All three peers silent on
7-ACA specifically"* and the reading note at the top of the report states
cephalosporin/7-ACA claims "have no direct peer analogue in any of the 11
transcripts."

This is inaccurate. KOPRAN-Concall_Feb_2025_Transcript.pdf, p.7-8 (the exact
page range B06 already cites for a different point in the Q4 section),
Surendra Somani explicitly names "Cephalosporins" as one of the
fermentation-based antibiotic raw materials China dominates, and states India
is "5, 7 year[s]" from self-sufficiency in fermentation-based KSMs generally.
This is not a 7-ACA-specific statement (7-ACA itself is never named in this
corpus — that narrower claim in B06 stands), but it is a direct, named
cephalosporin mention that bears on both:
- Q3 (7-ACA/cephalosporin KSM pricing and Chinese supplier dominance): weak
  corroboration that China dominates cephalosporin-family fermentation KSMs,
  consistent in kind with Orchid's claim, from a source B06 already had open.
- Q4 (falsification test on "nobody else is building" capacity in India): this
  passage is arguably the single most relevant sentence in the entire peer
  corpus to the falsification test — a peer management team's own estimate
  that India is 5-7 years from fermentation-based KSM (which covers
  cephalosporin precursors) self-sufficiency, which would, if credited,
  mildly support Orchid's "nobody else is building yet" claim rather than
  leave it fully untestable.

Correcting this would not flip either verdict — Q3 and Q4 would still likely
read UNVERIFIABLE given the statement is about the broader fermentation-KSM
category, not 7-ACA by name — but B06's absolute claim ("no peer transcript...
at any point," "all three peers silent," "no direct peer analogue... at all")
is not true of this corpus, and the passage sits inside a section B06 had
already opened and partially quoted. This is a completeness failure, not a
fabrication: MAJOR per the rubric ("wrong but decision likely survives").

### Finding 2 (MINOR, systemic) — inconsistent page-anchor convention

B06's page citations mix two different numbering schemes without flagging
either: sometimes they match the PDF's own page marker exactly (e.g.
NEULANDLAB Nov 2025 "p.3" for the 63.7% figure, NEULANDLAB May 2026 "p.3" for
37.1%, NEULANDLAB Aug 2026 "p.3" for 16.3%, GRANULES May 2026 "p.8" for the
DCDA China quote — all exact PDF-page matches); other times they match the
transcript's own internal running-footer page number, which runs one page
behind the PDF marker because each transcript PDF opens with an unnumbered
BSE/NSE cover letter (e.g. NEULANDLAB Feb 2026 "p.2" for the 11.4% figure is
actually PDF p.3; GRANULES Nov 2025 "p.5" for the 34% figure is actually PDF
p.6; GRANULES Jan 2026 "p.12" for the paracetamol quote is actually PDF p.13;
GRANULES Jul 2026 "p.5" for the West Asia line is actually PDF p.6). Every
citation checked was still correctly locatable within one page of the stated
number, and the quoted content and speaker attribution were correct in every
case. This is an anchor-precision defect, not a sourcing failure: MINOR.

### Finding 3 (MINOR-to-MAJOR, precision) — 2E inventory-days claim conflates two different disclosed metrics

B06's Part 2E / risks_peers_raise line states Neuland's "inventory days
rising from ~94 to ~145-155 days across FY26." Checked against the transcripts:
- "155 days" and "145 days" are the CFO's standard quarterly "working capital
  days of sales" disclosure (Q2 FY26 call: "working capital for the quarter
  was at 155 days of sales," NEULANDLAB-Concall_Nov_2025_Transcript.pdf p.3-4;
  Q3 FY26 call: "working capital for the quarter stood at 145 days of sales,"
  NEULANDLAB-Concall_Feb_2026_Transcript.pdf p.3) — this metric actually
  DECREASED (155 to 145) across the two quarters, not rose.
- "94 days" (FY25) to "124 days" (Q3 FY26, per-sales-basis) is a DIFFERENT,
  narrower "inventory holding period on current sales basis" metric the CFO
  gives only in the Aanchal Jalan Q&A exchange (NEULANDLAB-Concall_Feb_2026_Transcript.pdf,
  p.8-9), where a separate "inventory day total days" figure of 145 is also
  given in the same answer.
B06's single sentence blends the (declining) quarterly working-capital-days
disclosure with the (rising) inventory-days-to-sales figure into one
apparent trend line, which is not what either individual metric shows. The
underlying finding — analysts are actively pressing Neuland on
inventory-versus-profit correlation, and that scrutiny is a genuine, real,
well-quoted exchange (confirmed verbatim, including the "94... to 124... it
was 149... then 123... and it's 124" sequence) — is accurate and the
Aanchal Jalan quote itself is not misrepresented elsewhere in the report.
Only the compressed numeric summary line is imprecise enough to mislead a
reader who does not open the transcript. Graded MAJOR because this line feeds
directly into a named risk carried forward for Orchid's own balance-sheet
read, and a misdirected trend (rising vs. falling) on a specific metric is a
different claim than what the source supports, but note the qualitative
finding underneath it survives cleanly.

## PART 3: VERDICT-DISCIPLINE AUDIT (against B05 peer_questions, 8 claims)

| Q | Verdict in B06 | Peers behind it | Discipline check |
|---|---|---|---|
| 1 | CONTRADICTED (breadth only) | NEULANDLAB + GRANULES (2 independent) | PASS — ≥2 peers, revenue figures independently confirmed for both |
| 2 | UNVERIFIABLE | KOPRAN (stale) only has affirmative content; current peers silent | PASS — correctly not upgraded past UNVERIFIABLE despite Kopran's vivid FY25 account, staleness caveat applied consistently |
| 3 | UNVERIFIABLE | none | PASS — correctly not fabricated; confirmed no 7-ACA $/kg or supplier-count figure anywhere in corpus |
| 4 | UNVERIFIABLE (falsification test, absence treated as weak, not proof) | KOPRAN (Aurobindo penicillin, fermentation-KSM timeline) | PASS on verdict; INCOMPLETE on evidence base — see Finding 1 |
| 5 | UNVERIFIABLE | none (confirmed: zero "Russia"/"CIS" hits in all 8 current-peer transcripts) | PASS |
| 6 | UNVERIFIABLE | none (confirmed: zero "Ceftazidime"/"Avibactam" hits anywhere in corpus) | PASS |
| 7 | PARTIALLY VERIFIED | GRANULES only (1 peer) | PASS — correctly NOT marked VERIFIED given single-peer support; PARTIALLY VERIFIED is the right tier per rule 4 |
| 8 | UNVERIFIABLE | none | PASS |

No claim in the peer_questions list was skipped: all 8 received a verdict.
No VERIFIED claim rests on a single peer (there are zero full VERIFIED
verdicts in this report at all — appropriately conservative given the
corpus). No verdict was upgraded from silence; every CONTRADICTED or
PARTIALLY VERIFIED verdict is backed by an affirmative, checkable quote, not
by absence alone.

**claims_all_addressed: true.**

## PART 4: OVERALL ASSESSMENT

B06 is a well-anchored, honestly-scoped report. Every substantive citation I
checked (14 spot-checked quotes across all 11 transcripts, covering every
peer-quarter entry) was real, correctly attributed to the named speaker, and
accurately quoted — no fabricated or misattributed citation was found
anywhere in this report. The UNUSED classification of the Kopran merger-scheme
call is correct and the report's own staleness and no-cephalosporin-peer
caveats are, with one exception, honestly and consistently applied throughout.
The one real gap (Finding 1) is a completeness miss inside a passage the
report had already opened, not an invented or unsupported claim, and it does
not change any of the report's eight verdicts. The page-anchor convention
(Finding 2) is a systemic but non-material precision defect that a future run
should standardize (always cite the PDF's own page marker, never the
transcript's internal running-footer number).

```yaml
stage: B12d
company: "ORCHPHARMA"
run_date: "2026-09-06"
model: claude-sonnet-5
status: complete
peers_audited: 11
substantive_confirmed: 10
substantive_unsupported: []
unused_but_relevant: []
claims_all_addressed: true
verdict_discipline_fails: []
findings:
  - {severity: "MAJOR", location: "B06 Part 1 Q3 net read; Q4 net read; reading note", claimed: "No peer transcript in the corpus mentions 7-ACA, cephalosporin key starting materials... at any point / All three peers silent on 7-ACA specifically / no direct peer analogue in any of the 11 transcripts", source_truth: "KOPRAN-Concall_Feb_2025_Transcript.pdf, p.7-8, Surendra Somani names \"Cephalosporins\" explicitly inside the same fermentation-KSM passage B06 already cites for Q4, inside a call B06 marks SUBSTANTIVE", note: "Completeness miss, not fabrication; does not flip either UNVERIFIABLE verdict but the absolute 'no mention anywhere' framing is factually wrong"}
  - {severity: "MINOR", location: "B06 Part 1, multiple citations (Q1 NEULANDLAB Feb 2026 p.2, GRANULES Nov 2025 p.5, GRANULES Jan 2026 p.12, GRANULES May 2026 p.7, GRANULES Jul 2026 p.5)", claimed: "page numbers per B06's own anchors", source_truth: "each is one PDF page behind the actual PDF page marker (matches the transcript's internal running-footer number instead); content and speaker confirmed correct at the true page in every case", note: "Systemic anchor-convention inconsistency, all content independently confirmed present and accurately quoted"}
  - {severity: "MAJOR", location: "B06 Part 2E / risks_peers_raise, working-capital line", claimed: "inventory days rising from ~94 to ~145-155 days across FY26", source_truth: "94->124 days is a distinct 'inventory days to sales' metric (rising); 155->145 days is the separate quarterly 'working capital days of sales' disclosure (falling); B06 conflates the two into one apparently-rising range", note: "Underlying qualitative finding (analyst scrutiny on inventory-vs-PAT correlation) is accurately quoted elsewhere in the same section and not in dispute"}
critical_count: 0
major_count: 2
minor_count: 1
acceptance_rate: 91   # 10 of 11 peer-quarter entries correctly and completely handled
```
