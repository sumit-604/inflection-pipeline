# VERIFIER D: PEER COVERAGE AUDIT — SHARE INDIA SECURITIES (SHAREINDIA)
Run date: 2026-09-19. Model: claude-sonnet-5. Inputs: 12 peer transcripts
(SMC Global x4, Choice International x4, Angel One x4), B06 peer
verification report + block, B05 peer_questions list.

Scope per instructions: did the pipeline actually USE the peers it claims
to have used? Content-accuracy of quotes and page-anchor precision are
checked to the extent needed to answer that question; this is not a
line-by-line numerical audit (Verifier A's remit).

---

## PART 1: COVERAGE AUDIT PER PEER-QUARTER

12 of 12 peer-quarters are accounted for in B06's Part 3 coverage map: 11
SUBSTANTIVE, 1 CITED-ONLY (SMC Global Q2 FY26), 0 UNUSED.

| Peer / Quarter | B06 usage | Citation located in transcript? | Content match | Anchor accuracy |
|---|---|---|---|---|
| SMCGLOBAL Q2 FY26 (2025-11-07) | CITED-ONLY | Yes — "average daily turnover in the derivative segment declined sequentially" (line 93-94) | Exact | Roughly correct (p.2/3 boundary, ambiguous marker convention) |
| SMCGLOBAL Q3 FY26 (2026-02-09) | SUBSTANTIVE | Yes — "around 4% share from commodity... increasing towards 10%" (line 205-208) | Exact | Cited p.4; actual location is p.6 by the "Page N of 8" footer convention — MINOR anchor drift |
| SMCGLOBAL Q4 FY26 (2026-05-08) | SUBSTANTIVE | Yes — RBI-circular Q&A ("minimal impact... negligible impact... no impact", line 397-405) confirmed at p.11, matches citation exactly | Exact | Correct |
| SMCGLOBAL Q4 FY26 (2026-05-08), NCD/RBI-intent quote | SUBSTANTIVE (2B) | Yes — but located in a Q&A answer (Himanshu Gupta responding to a direct question on "strategic intent behind diversifying toward NCD", line 342-350, actual page 10) | Exact quote text | Cited as "SMCGLOBAL-2026-05-08, p.2" and framed as "opening remarks" — actual location is p.10, Q&A, answering a narrower NCD-strategy question, not a proactive RBI-curb disclosure. **MAJOR**: mischaracterizes both anchor and voluntariness/context of the disclosure |
| SMCGLOBAL Q1 FY27 (2026-07-31) | SUBSTANTIVE | Yes — "a relatively stable operating environment" (line 84), matches p.3 as cited | Exact | Correct |
| CHOICEIN Q2 FY26 (2025-10-24) | SUBSTANTIVE | Yes — NNPA 2.79% (line 109), segment splits | Exact | Correct |
| CHOICEIN Q3 FY26 (2026-02-11) | SUBSTANTIVE | Yes — per-branch capex "INR 3,00,000 to INR 5,00,000" (line 277) | Exact | Correct (p.5) |
| CHOICEIN Q4 FY26 (2026-04-28) | SUBSTANTIVE | Yes — "segment contributed 59% to total revenue" (line 87) | Exact | Correct (p.2) |
| CHOICEIN Q1 FY27 (2026-08-17) | SUBSTANTIVE | Yes — "800 branches over the next three to four years" (line 487); "210 to 220... 300 to 350" (line 496-498) | Exact | 800-branch quote cited p.13, actual location p.12 by bracket-marker convention — MINOR anchor drift. The 210-350 branch figure is correctly on p.13. |
| ANGELONE Q2 FY26 (2025-10-23) | SUBSTANTIVE | Yes — "different companies are built very differently" (line 109, p.11-12 as cited — correct); expiry-sensitivity question (line 113, p.12-13 boundary, close to cited p.13) | Exact | Correct |
| ANGELONE Q3 FY26 (2026-01-21) | SUBSTANTIVE | Yes — "early signs of recovery... 4.9 million... 6.2 million" and "highest ever order and ADTO... higher by 21% and 43%" (line 220-232, p.4-5 as cited — correct); MTF pricing exchange (Dipanjan Ghosh / Kenghe / Majumdar, line 687-714) | Exact | MTF-pricing citation given as p.17-18; the file carries two overlapping page-marking conventions (bracket "[page N]" vs "Page N of 19" footer) that disagree by roughly one page in this section — MINOR, not a hard mismatch given the ambiguity is in the source extraction itself |
| ANGELONE Q4 FY26 (2026-04-22) | SUBSTANTIVE | Yes — "limited operational impact... intraday credit availability... bank guarantees... diversified" (line 297-302), dated 22-Apr-2026, before Share India's own 20-May-2026 Q4 call — confirmed | Exact | Cited p.6; actual location p.7 by footer convention — MINOR anchor drift |
| ANGELONE Q1 FY27 (2026-07-21) | SUBSTANTIVE | Yes — "second order impact... spillover effect" (line 364/477) and "not seeing any kind of a liquidity issue... transient" (line 503), cited p.11-12 — correct; PAT +102.1% YoY (line 206) — correct; restricted-basket / Zerodha customer-attrition quote (line 1017-1033) | Exact | Second-order-impact and PAT citations correct. Restricted-basket quote cited p.19-20; actual location is p.24 by the "Page N of 25" footer convention — a larger drift than the others (~4-5 pages), still MINOR since the quote is real, exact, and directly attributable, just mis-paginated |

**No fabricated or non-existent citation was found.** Every quote checked
(15+ spot checks across all three peer companies) exists verbatim, or
functionally verbatim, at the peer transcript and speaker named. The one
MAJOR finding is a context/anchor mischaracterization, not an invented
quote: the NCD-diversification quote used in Part 2B (pricing/funding
cross-read) is presented as spontaneous "opening remarks" proactively
tying NCD diversification to the RBI capital-markets curb, when it is
actually the CFO's answer to a direct, narrower analyst question about
NCD strategic intent, ten pages later in the call than cited. This does
not touch any Part 1 verdict (it sits in Part 2's cross-read colour, not
in the five claim verdicts), but it overstates how proactively SMC Global
volunteered the RBI-driven funding-diversification parallel.

Page-anchor drift (1-5 pages, all in the MINOR band) recurs across
several citations. The likely mechanical cause: the source transcripts
carry two different page-marking conventions that do not always agree
(an injected "[page N]" bracket tag versus a "Page N of Y" printed
footer), and B06 appears to have mixed the two inconsistently. This is
worth flagging to the operator as a corpus-extraction hygiene issue, not
as evidence the pipeline invented or misused peer material.

---

## PART 2: CITED-ONLY / UNUSED SPOT-READ

SMC Global's Q2 FY26 call (2025-11-07, 9 pages) is the sole CITED-ONLY
peer-quarter. Full read confirms B06's single use (the "declining
sequentially" derivatives ADTO line) is accurate and is the call's most
claim-relevant content. One additional, moderately relevant item was not
picked up: this same call discloses NBFC GNPA 3.6% / NNPA 2.5% (line
313-314) — an earlier, more claim-relevant data point for B06's Part 2E
finding that peers proactively quantify asset-quality metrics that Share
India never discloses for its own lending book. B06 makes that point
using the SMC Global Q1 FY27 and Choice International Q2 FY26 calls
instead, so the substance already reaches downstream stages; the miss is
an additional corroborating data point, not the point itself. Graded
MINOR (industry-context miss, not claim-relevant miss per rule 3).

No peer-quarter is marked UNUSED, so rule 3's "directly claim-relevant
peer statement left unused" test does not otherwise apply.

---

## PART 3: VERDICT-DISCIPLINE AUDIT

| Claim (B06 Part 1) | Verdict | Peers cited | Independent anchor count | Discipline check |
|---|---|---|---|---|
| Q1: ADTO recovery industry-wide, commodity-driven | VERIFIED | ANGELONE, SMCGLOBAL | 2 | Passes (>=2 independent peers) |
| Q2: RBI intraday curb + bank-guarantee mitigation (mechanism; magnitude unconfirmed) | VERIFIED (mechanism only) | ANGELONE (x2 calls), SMCGLOBAL | 3, across 2 peer companies | Passes; correctly left the Rs 40,000-50,000 Cr magnitude UNVERIFIABLE rather than upgrading it on the strength of the mechanism confirmation |
| Q3: MTF pricing pressure (direction only) | PARTIALLY VERIFIED | ANGELONE only | 1 | Correctly NOT marked VERIFIED given single-peer support — matches rule 4 |
| Q4: Prop-vs-client split (LBF1) | UNVERIFIABLE | SMCGLOBAL, CHOICEIN (silent) | 0 | Correctly left unresolved; peer silence is not treated as corroboration in either direction — no verdict-upgraded-from-silence violation |
| Q5: SEBI algo-vendor circular | UNVERIFIABLE | all three (silent) | 0 | Same — correctly unresolved |

No VERIFIED verdict rests on a single peer. No verdict is upgraded from
silence. `verdict_discipline_fails: []`.

All 5 questions in B05's `peer_questions` list receive an explicit
verdict in B06 Part 1 (Questions 1-5 map one-to-one). `claims_all_addressed: true`.

---

## PART 4: SUMMARY

- 12 of 12 peer-quarters accounted for; 11 SUBSTANTIVE citations are
  genuine and locatable, 1 CITED-ONLY use is accurate and adequate.
- 0 fabricated citations, 0 verdict-discipline failures, 0 skipped
  peer_questions claims.
- 1 MAJOR finding: a Part 2B citation (SMCGLOBAL-2026-05-08 NCD quote)
  mischaracterizes an analyst-prompted Q&A answer as proactive "opening
  remarks" and cites the wrong page (p.2 vs actual p.10). Recommend the
  operator/Role-2 downstream stages treat this specific data point as
  "confirmed under direct questioning about NCD strategy", not as an
  unprompted RBI-curb disclosure; it does not change any Part 1 verdict.
- 5 MINOR findings: recurring 1-5 page anchor drift on otherwise
  accurately quoted citations (SMCGLOBAL-2026-02-09, ANGELONE-2026-04-22,
  ANGELONE-2026-01-21, ANGELONE-2026-07-21, CHOICEIN-2026-08-17), plus one
  industry-context item (SMC Q2 FY26 GNPA/NNPA) that could have
  additionally corroborated an existing Part 2E point but was not fatal
  to it.
- Net assessment: B06 genuinely read and used the peer corpus it claims
  to have used. The pipeline did not invent peer support, did not
  overstate verdict strength, and did not let peer silence quietly become
  corroboration on the run's central open question (LBF1). Anchor
  precision needs tightening (page-marking convention discipline), but
  this is a hygiene finding, not a fidelity failure.
