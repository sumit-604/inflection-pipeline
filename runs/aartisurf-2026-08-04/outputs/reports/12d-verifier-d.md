# B12d — Verifier D: Peer Coverage Audit of B06 (AARTISURF)
Run date: 2026-08-04 | Model: claude-sonnet-5 | Stage: verifier-d-peers

## Correction to prior run

The prior invocation of this stage reported the 12 peer transcript PDFs as missing and
returned a CRITICAL blocker. That was a look-up error, not a real artifact gap. This run
read all 12 PDFs directly by absolute path (each required page-range chunking due to a
20-page-per-request tool limit; every page of every file was read). All 12 files exist,
are valid, and are readable. No `ls`/`grep` was used on the PDFs. This report replaces the
prior CRITICAL finding with the actual source-fidelity audit that finding said could not be
performed.

Scope read: B06 (`06-peers.md`), the injected B05 peer_questions (Q1-Q6), and all 12 peer
transcripts (FCL x4, GALAXYSURF x4, ROSSARI x4).

---

## 1. Coverage map audit (B06 Part 3)

| Peer / Call | B06 classification | Audit finding |
|---|---|---|
| FCL Dec 2025 (Q2 FY26) | UNUSED | CONFIRMED. Call content is exclusively Q&A on the CrudeChem Technologies (US oilfield chemicals) acquisition — no India textile/hygiene demand, margin, export, or competition content bearing on Q1-Q6. UNUSED is correct. |
| FCL Feb 2026 (Q3/9M FY26) | SUBSTANTIVE | CONFIRMED. Export share "48% in quarter 3... from 25% last quarter" located. Gross margin "36%... Earlier, it was 38%" and the tariff-discounting quote ("margin pressures we got in India in the textiles because many companies, we had to support them in the times of tariff") located verbatim, correctly attributed to Sanjay Tibrewala (CFO). Hygiene-segment stabilization language located. |
| FCL May 2026 (Q4/FY26) | SUBSTANTIVE | CONFIRMED. WC "79 days... at par with the industry" located verbatim. OCF one-time-accounting-treatment quote ("that entry will not be there... Actually, till now also it's positive only") located verbatim. "Indian textile export grew 2.1% year-on-year in FY '26" and "one of the worst year of the decade for the textile companies" both located (B06's "worst years" plural is an immaterial paraphrase of the transcript's singular "worst year"). |
| FCL Jul 2026 (Q1 FY27) | SUBSTANTIVE | CONFIRMED, with one basis-anchor issue (Finding 2 below). Gross margin "35.42%... successfully pass on higher raw material costs" and WC "72 days" located verbatim. Texas capacity "80,000 MTPA to 1,48,000 MTPA... total capacity has expanded to 2,68,000 MTPA" located verbatim. |
| GALAXYSURF Aug 2025 (Q1 FY26) | SUBSTANTIVE | CONFIRMED. India volume "3% on volume terms," EBITDA/MT "maintained... INR20,000... versus INR20,200," Egypt/AMET backward-integration language, and capex guidance "INR120 crores to INR150 crores... not planning anything significant" all located verbatim. |
| GALAXYSURF Nov 2025 (Q2 FY26) | SUBSTANTIVE | CONFIRMED, with one anchor misattribution (Finding 1 below). H1 EBITDA "declined by 5% year-on-year at INR251 crores vis-a-vis INR265 crores" located verbatim. AMET erosion from "aggressive local players who are backward integrated" located. The China cost-arbitrage quote located verbatim and correctly attributed to the Divyansh Gupta exchange. CWIP "around INR260 crores as of FY '25... 1.5 years back" located verbatim. |
| GALAXYSURF Feb 2026 (Q3 FY26) | SUBSTANTIVE | CONFIRMED, one minor rounding note. The "2% to 4%... underlying volume growth" quote located verbatim. US tariff "reduced from 50% to 18%" located verbatim. The transcript states AMET volumes are "down 35% from our peak quarterly volumes" (a single figure); B06 renders this as "down roughly 30-35% from peak" — a minor softening of a precise number, not a direction or magnitude error. |
| GALAXYSURF May 2026 (Q4 FY26) | SUBSTANTIVE | CONFIRMED. EBITDA/MT "INR20,114... versus INR21,715 per metric ton in Q4 FY '25" located verbatim. India volumes "grew 8% year-on-year... 3% growth in performance and more than 27% growth in specialty" located verbatim. AMET "declining 15% year-on-year in Q4" located verbatim. |
| ROSSARI Oct 2025 (Q2 FY26) | SUBSTANTIVE | CONFIRMED. WC "102 days compared to 95 days in March," negative OCF, and Ketan Sablok's confirming quote ("a little stretch on the working capital... that led to this negative cash flow") all located verbatim. Margin "12.3%... compared to 13.2% in Q2 last year" located verbatim. |
| ROSSARI Jan 2026 (Q3 FY26) | SUBSTANTIVE | CONFIRMED, with one anchor-precision issue (Finding 3 below). EBITDA margin "11.8%" located verbatim. Soft-domestic-demand language located. China-as-phenol-supplier context located ("phenol is available from various sources including Thailand, Malaysia, India and China"). WC "improved sequentially in Q3 with better collection" located verbatim. |
| ROSSARI May 2026 (Q4/FY26) | SUBSTANTIVE | CONFIRMED. The Rs.192cr rephasing quote ("we internally have decided to rephase our earlier CAPEX spend, which was announced in April of Rs. 192 crore across Rossari, Unitop and Tristar"), the March RM "25% to 30%" cost quote, the Fineotex Q&A (Madhur Rathi asking / Sunil Chari answering — word for word, including "I cannot comment because I do not know their portfolio"), and the BASF/Dow/Lubrizol/Syensqo/Evonik/Chinese-competitor quote were all located verbatim and correctly attributed. FY27 capex guidance "Rs.50 crore to Rs.75 crore" located verbatim. |
| ROSSARI Jul 2026 (Q1 FY27) | SUBSTANTIVE | CONFIRMED. Margin "11.6%... compared to 12.5% in the corresponding quarter last year" located verbatim. Sunil Chari's RM/freight volatility quote ("a lot of volatility in buying our raw materials and in freight costs... this is causing us some degree of margin loss for us") located verbatim. "Slowed down on all the CAPEX spends" quote located verbatim. |

peers_provided confirmed: 12 of 12, all read in full.

---

## 2. Findings (anchor-precision issues; none change any verdict or the decision)

**Finding 1 — MINOR.** B06's Q5/Part 1 net-read attributes the "~INR480cr cumulative capex
over the prior 3 years" figure to the GALAXYSURF Nov 2025 call. The figure is real and
correctly quoted in substance, but it is actually stated in the GALAXYSURF **May 2026** call
("if I zoom out and look at it, we have done capex in last 3 years of roughly INR480 crores"
— Arun Prasath/K. Natarajan exchange). The Nov 2025 call correctly supports the adjacent
CWIP figure (~INR260cr) on its own. Correct number, correct peer, wrong call/date anchor.
Does not change the Q5 finding (Galaxy's capex wave winding down), which is independently
supported by the Aug 2025 call's maintenance-capex guidance and the Nov 2025 CWIP figure.

**Finding 2 — MINOR.** B06's Q1 discussion states "FCL (Jul 2026 call, Q1 FY27): gross
margin actually IMPROVED to 35.42% vs ~33% in Q1 FY26; EBITDA margin improved to 15.70% vs
13.93%," framing both comparisons as YoY (Q1 FY27 vs Q1 FY26). The gross-margin comparison
(33%) is confirmed YoY in the transcript ("last year 33%"). However, the 13.93% EBITDA
figure is introduced in the transcript as "the last quarter" — i.e., a QoQ comparison
against Q4 FY26 ("it's like 15.7 now and the last quarter was 13.93%" — Sanjay Tibrewala,
responding to Sunil Jain) — not a YoY comparison against Q1 FY26. The number is correctly
sourced from the transcript; the period basis implied by B06's sentence structure is not.
This is the same class of QoQ/YoY basis trap Verifier A is separately tasked to catch;
flagged here because it touches a peer citation. Does not change the Q1 net read (FCL is
already treated as a non-corroborating/contradicting data point on raw-material inflation).

**Finding 3 — MINOR.** B06's Q5 discussion states "ROSSARI (Jan 2026 call): was still in an
active capex cycle at this point... and a ~Rs192cr capex plan across Rossari/Unitop/Tristar
on the books." The Rs.192cr figure itself is explicitly stated in the ROSSARI Oct 2025
transcript ("our total planned capital outlay of Rs. 192 crore") and referenced again in the
May 2026 transcript as the plan "announced in April" that was subsequently rephased. The Jan
2026 transcript, as read, does not re-state the specific "Rs.192 crore" figure — it
describes ongoing phased capex generically. The inference that the plan was "still in force"
as of Jan 2026 is reasonable and correct (no rephasing had yet been announced), but the
specific rupee figure is not independently re-anchored in the Jan 2026 call itself. Does not
change the Q5 finding, which rests primarily and correctly on the Oct 2025 announcement and
the May 2026 rephasing (both directly quoted and dated in their own right).

No CRITICAL or MAJOR findings. No SUBSTANTIVE row lacked a real, locatable citation. No
verdict rests on a single peer where B06 called it more than PARTIALLY VERIFIED (see below).
No verdict was upgraded from peer silence.

---

## 3. Verdict-discipline audit (per claim, Q1-Q6)

| Claim | B06 verdict | Peers actually supporting | Discipline check |
|---|---|---|---|
| Q1 (RM inflation/margin compression) | PARTIALLY VERIFIED | Galaxy (2 calls) + Rossari (2 calls) corroborate direction; FCL contradicts/complicates | PASS — rests on 2+ independent peers; correctly not escalated to VERIFIED given the magnitude gap vs AARTISURF's figures |
| Q2 (demand growth currency) | CONTRADICTED | Galaxy (3 calls) + Rossari (4 calls) | PASS — 2 independent peers, multiple quarters each, both directly quoted |
| Q3 (export/China pressure) | PARTIALLY VERIFIED | FCL + Galaxy + Rossari | PASS — 3 peers; correctly held at PARTIALLY VERIFIED since no peer quantifies the specific FMCG/personal-care export-share magnitude AARTISURF reports |
| Q4 (new-entrant competition) | PARTIALLY VERIFIED | Galaxy only (4 calls); Rossari/FCL explicitly non-corroborating | PASS — B06 correctly holds this at PARTIALLY VERIFIED (not VERIFIED) precisely because only one peer corroborates, and in an adjacent market (AMET, not India domestic). Correct handling of single-peer evidence. |
| Q5 (capex cycle) | CONTRADICTED | Galaxy (2 calls) + Rossari (3 calls) | PASS — 2 independent peers, each with dated, quoted, specific capex pull-backs |
| Q6 (cash-conversion stretch) | PARTIALLY VERIFIED | Rossari only (1 call); Galaxy silent; FCL a false positive explicitly explained away | PASS — B06 correctly holds this at PARTIALLY VERIFIED given single-peer support, and separately flags Galaxy's silence as itself informative rather than treating it as corroboration. Correct handling. |

All six injected peer_questions (Q1-Q6) received an explicit verdict. No claim skipped. No
claim verdict rests on peer silence being read as confirmation.

---

## 4. Unused/cited-only peer spot-read

FCL Dec 2025 is the only UNUSED entry in B06's coverage map. Spot-read confirms the call is
exclusively CrudeChem-acquisition Q&A (integration timeline, US oilfield-chemicals capacity
ramp, deal financing) with no discussion of India textile/hygiene demand, margins, export
share, or competition. Nothing claim-relevant was left on the table in this call; UNUSED is
the correct classification. No CITED-ONLY rows exist in B06's map — every used peer-call is
marked SUBSTANTIVE with contributions actually traceable into Part 1 and Part 2 of B06.

No additional material peer evidence surfaced in the full read of all 12 transcripts that
B06 failed to use. Minor additional color exists in the transcripts (e.g., FCL Jul 2026's
aside that blended margins "one year back" were around 18% on a pre-CrudeChem base; ROSSARI
Jan 2026's aside on multi-year ROCE stagnation near 13%) but neither bears materially on any
of Q1-Q6 or on the Part 2 cross-read themes, so their omission from B06 is not a coverage
failure.

---

## 5. Overall assessment

B06's peer verification report is well-anchored against the source transcripts. Every
SUBSTANTIVE citation checked was locatable in its named transcript, in most cases as a
verbatim or near-verbatim quote with correct speaker attribution (Ketan Sablok, Sunil Chari,
Edward Menezes for Rossari; K. Natarajan for Galaxy; Sanjay Tibrewala for FCL, and analyst
names Madhur Rathi, Divyansh Gupta, Sunil Jain all correctly matched to their questions). The
UNUSED classification for FCL Dec 2025 is correct — the transcript genuinely contains no
relevant content. Verdict discipline is sound throughout: no claim is escalated beyond what
its peer-evidence count supports, single-peer-supported claims (Q4, Q6) are correctly capped
at PARTIALLY VERIFIED rather than VERIFIED, and Part 4's "0 of 6 fully verified" summary is
an honest characterization of a genuinely mixed, partial-corroboration peer read.

The three findings above are citation-anchor imprecisions — a correct figure attributed to
the wrong call-date (Finding 1), a QoQ figure implicitly framed alongside a YoY comparison
(Finding 2), and one figure's specific rupee anchor sourced from an adjacent call rather than
the cited one (Finding 3) — none of which change the substance of any Q1-Q6 finding or the
thesis-relevant conclusions (the Q2 demand-currency contradiction and the Q5 capex-cycle
contradiction, both independently well-supported apart from these three imprecisions).

```yaml
stage: B12d
company: "AARTISURF"
run_date: "2026-08-04"
model: claude-sonnet-5
status: complete
peers_audited: 12
substantive_confirmed: 11
substantive_unsupported: []
unused_but_relevant: []
claims_all_addressed: true
verdict_discipline_fails: []
findings:
  - {severity: "MINOR", location: "B06 Part 1 Q5 net read / Part 3 coverage map, GALAXYSURF Nov 2025 row", claimed: "cumulative ~INR480cr capex over prior 3 years, attributed to the Nov 2025 call", source_truth: "figure is stated in the GALAXYSURF May 2026 call (\"we have done capex in last 3 years of roughly INR480 crores\"), not the Nov 2025 call; Nov 2025 correctly supports the adjacent ~INR260cr CWIP figure", note: "correct number, correct peer, wrong call/date anchor; does not change the Q5 finding"}
  - {severity: "MINOR", location: "B06 Part 1 Q1, FCL Jul 2026 row", claimed: "EBITDA margin improved to 15.70% vs 13.93%, framed alongside a Q1 FY26 YoY gross-margin comparison", source_truth: "13.93% is introduced in the transcript as \"the last quarter\" (QoQ vs Q4 FY26: \"it's like 15.7 now and the last quarter was 13.93%\"), not a Q1 FY26 YoY figure", note: "number correctly sourced from transcript; period basis implied by B06's sentence structure is QoQ not YoY; does not change the Q1 net read"}
  - {severity: "MINOR", location: "B06 Part 1 Q5, ROSSARI Jan 2026 row", claimed: "active Rs192cr capex plan still in force, attributed to the Jan 2026 call", source_truth: "Rs192cr figure is explicitly stated in the Oct 2025 transcript and referenced again in the May 2026 transcript (\"announced in April of Rs. 192 crore\"); the Jan 2026 transcript describes ongoing phased capex generically without restating the specific figure", note: "inference (\"still in force\") is correct and reasonable; specific rupee anchor not independently re-confirmed in the Jan 2026 call itself; does not change the Q5 finding"}
critical_count: 0
major_count: 0
minor_count: 3
acceptance_rate: 92
```
