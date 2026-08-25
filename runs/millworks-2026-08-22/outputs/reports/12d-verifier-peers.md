# B12d — Verifier D: Peer Coverage Audit
Millworks Technologies Limited (MILLWORKS) | Run: millworks-2026-08-22 | Model: claude-sonnet-5

Scope: audit B06 (Stage 6 Peer Concall Verification) against the 7 peer transcripts
provided (4 Unimech, 1 Apsis Aerocom, 2 Airfloa Rail). No separate B05 peer_questions
artifact was supplied to this audit; B06's own Part 1 (7 numbered items) is treated as
the claim list, consistent with B06's own statement that it worked from an injected
peer_questions list rather than verbatim B05 claim text.

---

## PART 1: FILE IDENTITY CHECK (predicate to citation audit)

Before auditing citations, the actual call identity of each PDF was verified from its
cover letter and title page, since B06's Part 3 labels quarters by call date, not by
the filename convention given to this audit.

| File (as provided) | Actual call identity (from PDF cover page) |
|---|---|
| UNIMECH-Concall_Feb_2026_Transcript.pdf | Q3 FY26 Earnings Call, Feb 13, 2026 |
| UNIMECH-Concall_May_2026_Transcript.pdf | Acquisition Update Call, Apr 28, 2026 (filed May 4) |
| UNIMECH-Concall_Jun_2026_Transcript.pdf | **Q4 FY26 Earnings Call, May 29, 2026** (filed Jun 3) |
| UNIMECH-Concall_Aug_2026_Transcript.pdf | Q1 FY27 Earnings Call, Aug 4, 2026 |
| APSISAERO-Concall_Jun_2026_Transcript.pdf | H2 & FY26 Earnings Call, Jun 5, 2026 |
| 544516-Concall_Nov_2025_Transcript.pdf | H1 FY26 Results Call, Nov 18, 2025 |
| 544516-Concall_Jun_2026_Transcript.pdf | H2 FY26 & FY26 full year, Jun 3, 2026 |

Finding: the transcript containing Unimech's actual Q4 FY26 earnings call (working
capital days, capex deferral, Rs.9.6cr FX loss, AS9100 timeline, Dheya update) is the
file named "Jun_2026" in this run's inputs, not "May_2026." B06's Part 3 coverage map
labels this content's source row as "Q4 FY26 (May 2026 call)," which misidentifies
the physical file. The genuinely separate "May_2026" file is the April 28 Acquisition
Update call. See Finding 2 below for the consequence of this mislabeling.

---

## PART 2: PER-PEER COVERAGE AUDIT (B06 Part 3 rows)

| Peer / row | B06 label | Actual file | Content spot-checked | Verdict |
|---|---|---|---|---|
| UNIMECH Q3 FY26 | Feb 2026 call | Feb file (correct) | "not much competitors in India" (p.10); MTAR named (p.10); Dheya stake "30% from 16%" (p.8); Q3 revenue Rs.34cr, WC 150-160 days guidance (p.6) | Confirmed, correctly anchored |
| UNIMECH Acquisition update | Apr 2026 call, published May 2026 | May file (correct) | Hobel utilisation "50% to 60%... 85%-90%" (p.15 of 20); Rs.450cr EV, "6x to 7x EBITDA" (p.7); succession-exit seller motive (p.9) | Confirmed, correctly anchored |
| UNIMECH Q4 FY26 | **"May 2026 call"** | **Jun file** (mislabeled — see Finding 1/Part 1) | WC days "120 to 125... 150 to 160" (p.6); Rs.9.6cr exchange loss (p.6); "no major core business CAPEX requirement during FY27" (p.6); AS9100 "six to nine months," aerospace "2-3 years" (p.10); Dheya 30% stake detail (p.8) — all confirmed at cited pages | Content confirmed; **filename/quarter label wrong in Part 3** |
| UNIMECH Q1 FY27 | Aug 2026 call | Aug file (correct) | Order book Rs.280cr (p.4); WC 130 days trending 160+ (p.6); 58% utilisation (p.6); Rs.750cr QIP, "minimum public shareholding... due in the next 18 months" (p.17) | Confirmed, correctly anchored |
| APSISAERO H2 & FY26 | Jun 2026 call | Apsis file (correct) | Order book Rs.40.5cr, "1.32 times" FY26 revenue (p.5); Unit 1 "completely utilised" (p.8); IPO-then-machines sequence (p.9); receivables 45 days, 18.38%→13.14% (p.5); customer concentration 52%→35% (p.5); EBITDA 49%→37%, RM/FX driver quote (p.4); pipeline "100 crore," ~30% conversion (p.12) | Confirmed, correctly anchored |
| AIRFLOA H1 FY26 | Nov 2025 call | Airfloa Nov file (correct) | Order book Rs.455cr, defence ~Rs.65cr (p.5); "Rs.200-250cr this year... December of next year" (p.5) | Confirmed, correctly anchored |
| AIRFLOA H2 FY26 & FY26 | Jun 2026 call | Airfloa Jun file (correct) | Order book Rs.486.9cr, bid pipeline Rs.1,200cr, bid-win ratio 20-25% (p.3); trade receivables Rs.214cr (p.4-5); WC cycle "90-95 days... 60 to 70 days" (p.5); aluminium >80%, stainless steel 60-65% (p.9); competitors Kineco/Hindustan Fiberglass/DTL/Vibgyor/Universal Engineers/Tata/Fainsa (p.9-10); channel-partner model (p.13); China EUC delay (p.19); Rs.26,000cr refurbishment programme sanctioned (p.15) | Confirmed, correctly anchored |

7 of 7 rows are genuinely SUBSTANTIVE: every peer contributed real, page-locatable
citations that were not invented. No peer transcript was cited-only or left unused.
This part of B06's self-assessment ("all seven transcripts contributed a citation
that materially informed at least one verdict") holds up under independent re-read.

---

## PART 3: FINDINGS

### Finding 1 — MAJOR — Quote misattributed to wrong subject (Claim 3, Dheya evidence)
Location: B06 Part 1, Claim 3 ("investee/related-party top-customer structure"),
evidence sentence: *"management explicitly states Dheya revenue has not yet entered
the P&L ('No, not this year,' UNIMECH, Q4 FY26 call, p.13)."*

The actual transcript (Jun_2026 file = true Q4 FY26 call, p.12-13): analyst Ananya
Nichani asks **"And there was no JV revenue in this year, right?"** — referring to the
**Kanoo-Unimech Saudi JV**, not Dheya Technologies. Management's "No, not this year..."
answer is followed by "the Kanoo Unimech JV will take some time to operationalize."
Dheya is not the subject of this exchange anywhere on p.12-13. B06 has taken a real,
correctly-paged quote and attached it to the wrong company/topic. The broader claim
that "no revenue percentage from Dheya is disclosed in any of the four Unimech calls"
is independently true (no percentage is stated anywhere in the four transcripts), but
the specific supporting citation for "Dheya revenue not in P&L" does not say what B06
says it says. This affects the evidentiary weight for Claim 3, which currently reads
PARTIALLY VERIFIED partly on the strength of a misattributed quote.

### Finding 2 — MAJOR — File mislabeling produces an inflated double-citation (Claim 1)
Location: B06 Part 1, Claim 1, evidence sentence citing *"Hobel Bellows carries 'an
overall 12-month visibility' (UNIMECH, May 2026 Q&A, p.14; UNIMECH, Q4 FY26 call, p.14
[Garvit Goyal Q&A])."*

Both citations point to the identical passage — Aakash Jaiswal's answer to Garvit
Goyal on order-execution timelines ("PO to PO," "12 to 18 months" for nuclear,
"overall 12-month visibility" for Hobel) — which appears once, on p.14 of the Jun_2026
file (the true Q4 FY26 call). "UNIMECH, May 2026 Q&A" and "UNIMECH, Q4 FY26 call" are
not two different sources; they are two different (and in the first case, wrong)
labels for the same file and the same Q&A exchange. This traces to the same root
cause as Finding 1/Part 1's file-identity confusion (the true Q4 FY26 call sits in the
file named "Jun_2026," while the file named "May_2026" is a different call entirely).
The practical effect is that a single citation is dressed up to look like two
independent anchors within one evidence sentence. It does not change Claim 1's verdict
(already the more conservative PARTIALLY VERIFIED), but it is a citation-hygiene
failure the verdict-discipline rule (Rule 4) is meant to catch, and it would matter
more if reused on a claim marked fully VERIFIED.

### Finding 3 — MINOR — Small page-offset citations (Apsis)
Location: B06 Part 1, Claim 7, quote *"we cannot take very big orders, because most of
the time that becomes an execution issue"* cited as (APSISAERO, Jun 2026, p.12-13).
Actual location: Apsis document page 11 (footer "Page 11 of 19"). Off by one page;
content is genuine and correctly attributed to the right speaker and topic. Similarly
the "100 crore" pipeline / "~30% conversion" figures cited at p.12-13 are confirmed at
document p.12, a one-page variance. Cosmetic; does not affect any verdict.

---

## PART 4: VERDICT-DISCIPLINE AUDIT (Rule 4)

| Claim | B06 verdict | Independent peer anchors confirmed | Discipline check |
|---|---|---|---|
| 1. Order-to-revenue conversion pace | PARTIALLY VERIFIED | 3 (Unimech, Apsis, Airfloa) | OK — appropriately hedged despite 3 anchors, since Millworks' own order-book vintage is unknown |
| 2. Elongated receivables / testing delays | UNVERIFIABLE (contrast informative) | 3 peers show 45-160 day range, none support the mechanism | OK — correctly avoids over-claiming a mechanism no peer states |
| 3. Investee-top-customer structure (Dheya) | PARTIALLY VERIFIED | 1 (Unimech) | OK in principle (single peer, appropriately not marked VERIFIED), but rests partly on the misattributed quote in Finding 1 |
| 4. Utilisation threshold for capex / funding sequencing | **VERIFIED** | 3 independent peers (Unimech-Hobel, Apsis, Airfloa), all confirmed on independent re-read | OK — genuinely 3-peer corroboration; VERIFIED is earned, not a Rule-4 violation |
| 5. Railways capex cycle → order inflow (Airfloa only) | PARTIALLY VERIFIED (single peer, flagged as such) | 1 (Airfloa, the only rail peer asked) | OK — explicitly caveated as single-peer in the verdict text itself |
| 6. RM pass-through / FX hedging practice | PARTIALLY VERIFIED | 2 (Unimech, Apsis) | OK |
| 7. Sector capacity crunch vs company-specific share gain | PARTIALLY VERIFIED | 3 peers (qualitative pattern, not a direct quote match) | OK — verdict correctly notes no peer uses the exact framing |

No verdict is upgraded from silence. No VERIFIED verdict rests on a single peer.
Claim 4 is the only VERIFIED verdict and its three-peer support is independently
confirmed as real. Verdict discipline overall: sound, aside from Finding 1's effect on
Claim 3's evidentiary basis (verdict level itself — PARTIALLY VERIFIED — remains
appropriate even after discounting the bad citation).

---

## PART 5: CLAIMS COVERAGE

All 7 items in B06's Part 1 (the peer_questions items worked from) received an
explicit verdict (VERIFIED / PARTIALLY VERIFIED / UNVERIFIABLE) — none skipped. No
independent B05_PEER_QUESTIONS artifact was supplied to this audit to cross-check
whether the 7-item list itself is complete against what B05 or the operator originally
asked; this audit can only confirm internal completeness (every item B06 says it was
asked, it answered).

## PART 6: UNUSED-BUT-RELEVANT SCAN

Spot reads across all 7 transcripts did not surface material, claim-relevant peer
disclosures that B06 left out. Adjacent items not pulled into B06 (Apsis's RM
inflation being scoped to "US and European markets" specifically; Airfloa's
retender-on-thin-margin discipline) are industry-context color, not directly
responsive to Millworks' four open items (receivables, investee-customer, capex
discipline, RM/FX), and are MINOR-grade at most — not flagged as findings.

---

## SUMMARY

B06's factual base is sound: every cited figure and quote checked against source
independently re-verified to correct pages in the correct documents, across all 7
transcripts. The defects found are citation-hygiene problems from a mixed-up
correspondence between two of the four Unimech files (the true Q4 FY26 call physically
sits in the file named "Jun_2026," not "May_2026") — not fabrication and not a wrong
underlying fact. That mislabeling produced one misattributed quote (Finding 1, Dheya
vs. Saudi JV) and one inflated double-citation (Finding 2). Both are MAJOR under this
audit's rubric because they touch claim evidence directly, but neither changes a
verdict: Claim 3 remains correctly PARTIALLY VERIFIED and Claim 1 remains correctly
PARTIALLY VERIFIED even with the bad citation discounted.

```yaml
stage: B12d
company: "MILLWORKS"
run_date: "2026-08-22"
model: claude-sonnet-5
status: complete
peers_audited: 7
substantive_confirmed: 7
substantive_unsupported: []
unused_but_relevant: []
claims_all_addressed: true
verdict_discipline_fails: []
findings:
  - {severity: "MAJOR", location: "B06 Part 1, Claim 3 (investee/related-party top-customer), evidence citation 'No, not this year, UNIMECH Q4 FY26 call, p.13'", description: "Quote misattributed: the actual passage (Jun_2026 file, true Q4 FY26 call, p.12-13) is management confirming no revenue yet from the Kanoo-Unimech Saudi JV, not from Dheya Technologies. The broader claim that Dheya revenue percentage is undisclosed is independently true, but this specific supporting citation does not say what B06 says it says."}
  - {severity: "MAJOR", location: "B06 Part 1, Claim 1, evidence citation 'UNIMECH, May 2026 Q&A, p.14; UNIMECH, Q4 FY26 call, p.14 [Garvit Goyal Q&A]'", description: "Same single quote (Hobel '12-month visibility', Garvit Goyal Q&A, p.14 of the Jun_2026 file which is the true Q4 FY26 call) is cited twice under two different call labels, presenting one source as two independent anchors. Root cause: B06's Part 3 mislabels the physical file containing the true Q4 FY26 call as 'May 2026 call' when it is actually the file named Jun_2026 in this run's inputs; the true May_2026 file is the separate April 28 Acquisition Update call."}
  - {severity: "MINOR", location: "B06 Part 1, Claim 7, quote 'we cannot take very big orders...execution issue' cited as APSISAERO Jun 2026 p.12-13", description: "Quote is genuine and correctly attributed to the right speaker/topic but sits on document page 11, a one-page citation offset. Cosmetic only."}
critical_count: 0
major_count: 2
minor_count: 1
acceptance_rate: 71
```
