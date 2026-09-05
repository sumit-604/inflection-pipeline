# VERIFIER D: PEER COVERAGE AUDIT — KABRAEXTRU

**Model:** claude-sonnet-5 | **Run date:** 2026-09-05 | **Audits:** outputs/reports/06-peers.md and outputs/blocks/B06-peers.yaml against the 5 raw peer transcripts and the 9 peer_questions in B05-concall.yaml.

Method: every citation B06 marks against a SUBSTANTIVE peer was located in the raw transcript text (page-marked "===== PAGE n =====" per the task's PDF-page convention) and checked for wording accuracy and correct page anchor. All 5 transcripts and the WINDMACHIN screening CSV were read in full.

---

## PART 1: COVERAGE AUDIT TABLE PER PEER

| Peer / call | B06 usage | Citations checked | Result |
|---|---|---|---|
| RAJOOENG Q4 FY23 (16-May-2023) | SUBSTANTIVE | FY23 revenue Rs159.79 Cr, p.3 | CONFIRMED verbatim at cited page |
| RAJOOENG Q2 FY24 (6-Nov-2023) | SUBSTANTIVE | CAGR quote p.3; "raw material prices have gone up" p.7; "back-to-back procurement" p.9 | First two CONFIRMED at cited page. Third: quote is real and correctly transcribed but sits on PDF page 10, not p.9 (MINOR anchor drift) |
| RAJOOENG Q4 FY24 (18-Apr-2024) | SUBSTANTIVE | Global CAGR p.2; FY24 revenue Rs197.35 Cr p.5; 80%/60% market share p.7; "Windsor machines and carbon extrusion" p.8; 45% FY24 export share p.11 | First three CONFIRMED at cited page. "Windsor machines and carbon extrusion" is real and correctly quoted but sits on PDF page 9, not p.8 (MINOR anchor drift). 45% export figure is real but sits on PDF page 12, not p.11 (MINOR anchor drift) |
| RAJOOENG Q2 FY25 (22-Oct-2024, filename mislabeled Nov_2025) | SUBSTANTIVE | H1 FY25 revenue p.3-4; order book Rs200+ Cr / Rs1,000 Cr pipeline p.13/15; 33% PVC market share / 55-60% blown films market share p.9-10; "domestic is not really encouraging margin"/73% export p.11 | Revenue and order-book/pipeline citations CONFIRMED at cited pages. The two market-share quotes are real and correctly transcribed but sit on PDF pages 11 and 12 respectively, not p.9-10 (MINOR anchor drift, compounding across three citations in this one call). The "domestic is not really encouraging margin" quote is real but sits on PDF page 12, not p.11 (MINOR anchor drift) |
| HBLENGINE FY25 AGM (25-Sep-2025) | SUBSTANTIVE | Lithium-cell/Navy quote p.4; Rs200 Cr investment/profit-from-year-one p.4; electric truck 55/35-ton pivot p.15-16; Kavach Rs3,000 Cr p.2; Rs4,500 Cr FY30 target p.3; conglomerate-discount quote p.5; "no margin" nickel-cadmium quote p.17 | All CONFIRMED at cited page. One quote-wording issue: B06 renders "everybody can import cells" where the transcript literally reads "everybody can import sales" (likely an upstream transcription artifact) — substance intact, wording not verbatim (MINOR) |
| WINDMACHIN | UNUSED (no transcript) | n/a | B06 correctly flags the missing transcript and correctly identifies its materiality (RAJOOENG names "Windsor machines" as one of only two domestic competitors it tracks, Apr-2024 p.9). But B06 never mentions or uses the WINDMACHIN screening CSV that IS in corpus (`inputs/screening/WINDMACHIN-Data_Sheet.csv`), which is the only peer data source in this run that actually reaches KABRAEXTRU's FY26 window (see Part 2) |

**Coverage summary:** 5 of 5 provided transcripts were genuinely read and genuinely used; no SUBSTANTIVE marking is unsupported by a real citation. Every citation checked corresponds to a real, correctly-quoted (with one minor wording exception) statement in the named transcript. The defect found is anchor precision (page number), not fabrication or invention: nine citations were verified as exact-page matches; five citations across three calls carry a 1-2 PDF-page drift from their stated anchor, all traceable to the correct call and locatable within a few pages.

---

## PART 2: THE WINDMACHIN GAP — WHAT B06 MISSED

B06's single biggest analytical constraint, stated up front and repeated in nearly every claim row, is that no transcript in this corpus reaches KABRAEXTRU's FY26 window (year ended 31-Mar-2026): the four RAJOOENG calls stop at 22-Oct-2024, roughly 17 months short; HBLENGINE is a segment mismatch. Every CONTRADICTED verdict is explicitly capped to "framing plausibility as of the closest observable peer window," never the FY26 figures themselves.

`inputs/screening/WINDMACHIN-Data_Sheet.csv` was available in this run's corpus and was never mentioned by B06, even to explain why it was out of scope. It is not a concall (B06's stated remit is peer concall verification), but it is the only peer data source in this run that has data points reaching INTO the FY26 window:

- Annual Sales: Rs327.60 Cr (FY25, year ended 2025-03-31) -> Rs566.52 Cr (FY26, year ended 2026-03-31), a +72.9% YoY jump, while Net Profit stayed negative (FY25: -25.27 Cr; FY26: -4.43 Cr).
- Quarterly Sales reach through Q1 FY27 (quarter ended 2026-06-30): Rs146.21 Cr, versus Rs69.60 Cr in the equivalent quarter a year earlier (2025-06-30) — again a large increase.
- Cash from Investing Activity: -Rs348.74 Cr (FY25) and -Rs121.67 Cr (FY26), alongside an equity-capital increase (Rs12.99 Cr to Rs16.90 Cr to Rs17.70 Cr) and an Investments line that spikes to Rs343.11 Cr in FY25 before dropping to Rs42.0 Cr in FY26 — consistent with a large one-off capital raise/investment event, not necessarily organic capex, so this data needs a caveat and does not straightforwardly read as "industry tailwind."

This matters directly to three of the nine peer_questions:
- Claim 1 (JJM framing for the 13.2% extrusion decline) and Claim 5 (export weakness): Windsor's FY26 top-line surge, whatever its cause, is one more data point (however ambiguous) that a same-sector peer was not seeing an unambiguous FY26 industry-wide contraction — precisely the test RAJOOENG's stale data could not perform, and precisely the test this CSV can partially perform.
- Claim 6 (capex cycle): Windsor's sustained heavy investing outflow through FY26 (-Rs121.67 Cr) sits alongside KABRAEXTRU's near-halved capex, reinforcing (with the same peer-set-of-one caveat B06 already applies to RAJOOENG) the "lone contractor vs. active peer" pattern B06 built entirely on RAJOOENG.

This is not a case of B06 needing to run a full financial-statement peer analysis (that is genuinely out of a concall-verification stage's remit, and the M&A-like ambiguity in the numbers means this data cannot simply be read as clean confirmation). But given that B06's own framing repeatedly leans on "no peer data reaches FY26" as the load-bearing limitation of the whole report, a one-line acknowledgment that a FY26-reaching (if ambiguous, and non-transcript) data point existed and was not usable/reliable for concall-style verification would have been the honest, defensible move. Its complete absence — not even a footnote — is a coverage gap. **Severity: MAJOR** (directly claim-relevant peer data left unused, bearing on three of nine claims and on the report's central limitation).

---

## PART 3: VERDICT-DISCIPLINE AUDIT PER CLAIM

| # | Claim | B06 verdict | Peers anchored | Discipline check |
|---|---|---|---|---|
| 1 | JJM/infra external-blame framing | CONTRADICTED (framing) / UNVERIFIABLE (FY26 magnitude) | RAJOOENG (4 calls) | Grounded in real, affirmative peer evidence (accelerating revenue, no JJM mention across 4 calls), not silence. Explicitly scoped to framing plausibility only. PASS |
| 2 | Global extrusion CAGR | PARTIALLY VERIFIED | RAJOOENG (2 calls, same company) | Correctly NOT labeled VERIFIED despite two data points, because both come from a single peer — rule 4's 2-independent-peer bar for full VERIFIED is respected by not awarding VERIFIED here. PASS |
| 3 | ~40% market share dropped | UNVERIFIABLE | RAJOOENG | No peer statement addresses KABRAEXTRU's share directly; correctly left unverifiable rather than stretched into a verdict from the "carbon extrusion" inference, which B06 itself flags as tentative. PASS |
| 4 | RM cost trend / pass-through | UNVERIFIABLE (with peer signal noted) | RAJOOENG | Correctly UNVERIFIABLE for the FY25-26 window itself; the "net read" is explicitly labeled a lean, not a proof. PASS |
| 5 | Export weakness sector-wide? | CONTRADICTED (framing) / UNVERIFIABLE (FY26 magnitude) | RAJOOENG | Same structure as Claim 1: real affirmative trend evidence (export share rising to 73-74%), correctly scoped. PASS |
| 6 | Capex cycle / capacity signal | CONTRADICTED (direction) | RAJOOENG | Real evidence (continuous capacity expansion across 4 calls); B06 itself flags the "only one directly comparable peer" limitation and declines to call it industry-wide. This is the claim where the missed WINDMACHIN CSV data (Part 2) would have mattered most. PASS on discipline, but see Part 2 gap |
| 7 | HBL EV-OEM credit quality | UNVERIFIABLE — segment mismatch | HBLENGINE | Genuine mismatch, correctly explained (Navy-only lithium-ion vs. mass 2W/3W EV), not a question-asking gap. PASS |
| 8 | HBL lithium-ion pack margin/utilisation | UNVERIFIABLE — segment mismatch | HBLENGINE | Same as above; structural commentary correctly labeled as context, not a substitute answer. PASS |
| 9 | HBL EV battery market-size figure | UNVERIFIABLE — no figure cited | HBLENGINE | Confirmed: no such figure appears anywhere in the transcript. PASS |

**Rule 4 checks:**
- Zero claims are marked VERIFIED, so the "VERIFIED needs >=2 independent peer anchors" trigger never fires. No violation.
- No verdict is an upgrade from silence: every CONTRADICTED verdict rests on affirmative, correctly-quoted peer statements describing a contrary trend, not an absence of peer commentary. No CRITICAL finding here.
- All three CONTRADICTED verdicts are careful, in both the report prose and the YAML `quote_anchor` fields, to scope themselves to "framing plausibility as of the closest observable peer window" rather than a direct test of the FY26 figures. This is the correct discipline given the 17-18 month data gap, and it is applied consistently, not just in the summary section.
- One presentational observation (MINOR): the verdict label "CONTRADICTED" by itself, if lifted out of context by a downstream synthesis stage without its accompanying caveat, could read as a stronger, FY26-figure-level contradiction than the evidence supports. The caveat is present everywhere in this report (STALENESS NOTICE, per-claim Verdict field, Part 4 summary, and the YAML `analyst_note`), so this is a labeling-clarity suggestion, not a discipline failure.

**Rule 5 check (all peer_questions addressed):** All nine questions in B05-concall.yaml's `peer_questions` list map one-to-one onto B06's nine claims and all nine received explicit verdicts (0 VERIFIED / 1 PARTIALLY VERIFIED / 3 CONTRADICTED / 5 UNVERIFIABLE = 9). None were skipped. PASS.

---

## PART 4: FINDINGS SUMMARY

| Severity | Finding |
|---|---|
| MAJOR | WINDMACHIN screening CSV (the only peer data source in corpus reaching KABRAEXTRU's FY26 window) was never mentioned or used, despite bearing directly on Claims 1, 5, and 6 and on the report's own central staleness limitation. See Part 2. |
| MINOR | "Back-to-back procurement" quote (Claim 4), cited RAJOOENG Q2 FY24 p.9, actually sits on PDF page 10. Quote is real and accurately transcribed. |
| MINOR | "Windsor machines and carbon extrusion" quote (Claim 3, Part 2D), cited RAJOOENG Q4 FY24 p.8, actually sits on PDF page 9. Quote is real and accurately transcribed. |
| MINOR | 45% FY24 export-share figure (Claim 5), cited RAJOOENG Q4 FY24 p.11, actually sits on PDF page 12. |
| MINOR | 33% PVC market-share quote and 55-60% blown-films market-share quote (Claim 3), both cited RAJOOENG Q2 FY25 p.9-10, actually sit on PDF pages 11 and 12 respectively. |
| MINOR | "Domestic is not really encouraging margin" / 73% export quote (Claim 1 net read), cited RAJOOENG Q2 FY25 p.11, actually sits on PDF page 12. |
| MINOR | HBLENGINE p.17 quote rendered as "everybody can import cells"; transcript literally reads "everybody can import sales." Substance intact, wording not verbatim. |
| MINOR | The "CONTRADICTED" verdict label, standing alone outside its caveat, risks being read downstream as a stronger claim than the evidence supports (it is fully caveated in context; this is a labeling-clarity note, not a discipline failure). |

No CRITICAL findings. All SUBSTANTIVE markings are supported by real, locatable citations. All nine claims received a verdict. Verdict discipline (2-peer rule for VERIFIED, no upgrade from silence) is respected throughout.

---

## PART 5: ACCEPTANCE RATE

Peers audited (coverage-map rows): 6 (4 RAJOOENG calls + HBLENGINE + WINDMACHIN).
Correctly handled: 5 (all SUBSTANTIVE peers — citations real and substantively accurate, anchor-page drift is a precision defect, not a fabrication or misuse).
Not correctly handled: 1 (WINDMACHIN — correctly flagged as UNUSED for the transcript gap, but its available screening-CSV data going completely unacknowledged is a material coverage miss).

Acceptance rate = 5 / 6 = 83%.

```yaml
stage: B12d
company: "KABRAEXTRU"
run_date: "2026-09-05"
model: claude-sonnet-5
status: complete
peers_audited: 6
substantive_confirmed: 5
substantive_unsupported: []
unused_but_relevant:
  - {peer: "WINDMACHIN", missed_item: "Screening CSV (inputs/screening/WINDMACHIN-Data_Sheet.csv) shows FY26 sales +72.9% YoY (Rs566.52 Cr vs Rs327.6 Cr FY25) with quarterly data reaching Q1 FY27 (quarter ended Jun-2026) -- the only peer data source in this corpus that actually reaches KABRAEXTRU's FY26 window, which every RAJOOENG transcript misses by ~17 months. Net profit stayed negative and an equity-capital/investments spike suggests the growth may be M&A-driven rather than organic, so it is not clean confirmation, but B06 never mentions the CSV exists, even to caveat it out of scope. Directly bears on Claims 1, 5, and 6 and on the report's own central staleness limitation.", anchor: "inputs/screening/WINDMACHIN-Data_Sheet.csv, rows 10-11 (FY26 column) and rows 27-28 (quarterly columns through 2026-06-30)"}
claims_all_addressed: true
verdict_discipline_fails: []
findings:
  - {severity: "MAJOR", location: "Part 3 coverage map / WINDMACHIN row", claimed: "WINDMACHIN listed UNUSED, no transcript in corpus", note: "True but incomplete: the WINDMACHIN screening CSV in corpus reaches KABRAEXTRU's FY26 window and was never mentioned, unlike every RAJOOENG transcript which stops 17 months short; a material, available, claim-relevant data source went unacknowledged"}
  - {severity: "MINOR", location: "Claim 4, RAJOOENG Q2 FY24 back-to-back procurement quote", claimed: "cited p.9", note: "quote is real and accurately transcribed but sits on PDF page 10"}
  - {severity: "MINOR", location: "Claim 3 / Part 2D, RAJOOENG Q4 FY24 'Windsor machines and carbon extrusion' quote", claimed: "cited p.8", note: "quote is real and accurately transcribed but sits on PDF page 9"}
  - {severity: "MINOR", location: "Claim 5, RAJOOENG Q4 FY24 45% FY24 export share", claimed: "cited p.11", note: "figure is real but sits on PDF page 12"}
  - {severity: "MINOR", location: "Claim 3, RAJOOENG Q2 FY25 33% PVC / 55-60% blown-films market share quotes", claimed: "cited p.9-10", note: "quotes are real and accurately transcribed but sit on PDF pages 11 and 12 respectively"}
  - {severity: "MINOR", location: "Claim 1 net read, RAJOOENG Q2 FY25 'domestic is not really encouraging margin' / 73% export quote", claimed: "cited p.11", note: "quote is real but sits on PDF page 12"}
  - {severity: "MINOR", location: "Claim 8, HBLENGINE p.17 nickel-cadmium quote", claimed: "'everybody can import cells'", note: "transcript literally reads 'everybody can import sales'; substance intact, wording not verbatim"}
  - {severity: "MINOR", location: "Part 4 Triangulation Summary, CONTRADICTED verdict labels", claimed: "CONTRADICTED", note: "label alone (outside its caveat) risks reading stronger than the framing-only scope the report consistently states; presentational note, not a discipline failure"}
critical_count: 0
major_count: 1
minor_count: 7
acceptance_rate: 83
```
