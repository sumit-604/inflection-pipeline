# VERIFIER D: PEER COVERAGE AUDIT — KISSHT (OnEMI Technology Solutions Ltd)

Run date: 2026-09-19. Scope: did the pipeline actually USE the 12 peer
transcript files (11 effective calls — POONAWALLA-Concall_Jan_2026_Transcript.pdf
and its _2 cover-letter duplicate are the same 16-Jan-2026 call, counted once)
it claims it used in B06? Inputs read: all 12 peer transcript .txt files in
R\inputs\peer-concalls\, B06 report (outputs/reports/06-peers.md), and the
peer_questions block from B05 (outputs/blocks/B05-concall.yaml).

Method: for every SUBSTANTIVE citation in B06 Parts 1–2, I located the
[page N] marker cited, confirmed the quoted text exists verbatim (or as a
faithful paraphrase) at that marker, and checked page-tag boundaries against
the actual line ranges in each .txt file (I grepped every `[page N]` tag per
file to build exact line-range maps rather than trusting my own page count).
I read all 12 files in full or near-full (some in targeted excerpts once the
page-map was built) and ran a corpus-wide grep for FLDG/DLG/first-loss to
independently test B06's zero-match claim on Claim 3.

---

## PART 1: COVERAGE AUDIT PER PEER (11 effective transcripts)

| Peer / quarter | B06 classification | Citation located? | Notes |
|---|---|---|---|
| SBICARD Oct-2025 (Q2 FY26) | CITED-ONLY | N/A — no substantive quote claimed | Read in full. Confirmed no DPD write-off figure, no FCNR mention, no Kissht/Bajaj/Chola naming, no capital-raise or divergence-narrative discussion anywhere in the transcript. CITED-ONLY is the correct call; nothing claim-relevant was left on the table. |
| SBICARD Feb-2026 (Q3 FY26) | SUBSTANTIVE | YES | "the benefit from repo rate cuts on our floating book has been mostly absorbed. The cost of funds is expected to remain stable at current levels from here onwards" — verified verbatim at p.5 (line-range 143–183 in the .txt page-map). "we are the single largest pure-play [credit card issuers]" verified verbatim at p.20 (line-range 723–762). Both citations exact. |
| SBICARD May-2026 (Q4 FY26) | CITED-ONLY | YES (context figure) | "The cost of funds during Q4 was 6.4%, lower by 82 basis points Y-o-Y" verified verbatim, correctly used only as a trend data-point, not over-claimed as SUBSTANTIVE. |
| SBICARD Jul-2026 (Q1 FY27) | SUBSTANTIVE | YES | Anand Dama's "we've been hearing that, particularly in Southern India... Any stress which you see over there?" and his follow-up "whatever check that we have done with multiple lenders and collection agencies... 300 to 400 basis points, bucket delinquency has gone up" both verified verbatim at p.15 (line-range 561–601). Salila Pande's "no cohort where we see this kind of stress... even for the IT sector, we did a separate analysis" also verified at p.15, same exchange. "we expect cost of funds to trend higher in line with the market rates" verified verbatim at p.5 (line-range 146–175). Geopolitical/Middle-East monitoring language verified at p.7 (line-range 228–271), matching the Part 2E citation. All four citations from this call check out exactly. |
| POONAWALLA Jan-2026 (Q3 FY26, incl. _2 duplicate) | SUBSTANTIVE | YES | Sanjay Miranka's "unsecured is 180 DPD. Vehicle secured is 365 DPD and even loan against property is 730 DPD, which actually is case-by-case basis across the industry" verified verbatim at p.16 (line-range 613–649). Abhijit Tibrewal's "this has nothing to do with any accelerated write-offs... These are all business-as-usual credit costs" verified verbatim at p.19 (line-range 733–739) — B06 cites this without naming the analyst, which is accurate (it does not misattribute the question to Chintan Shah as an early skim might suggest; Chintan Shah asked the immediately preceding question at p.15–16, Tibrewal asked this one). Cost-of-borrowing decline (8.04%→7.65%, NCD mix 7%→27%→30-33%, "cumulative repo cuts of 125 basis points since February") verified at p.3–5. |
| POONAWALLA May-2026 (Q4 FY26) | SUBSTANTIVE | YES | Pre-raise CRAR "16.83%... Tier 1 capital is at 15.90%" and post-raise "20.74%" both verified verbatim at p.14 (line-range 549–593). Jay Betai's ALM-gap question and Sanjay Miranka's "it gets bridged. With the capital raise, it has been bridged" verified verbatim at p.19 (line-range 764–805), one line above the [page 20] tag — an acceptable close anchor for a citation given by B06 as "p.19–20". |
| POONAWALLA Jul-2026 (Q1 FY27) | SUBSTANTIVE | YES, with one MINOR mischaracterization | Cost of borrowing "7.72% versus 7.63% in the previous quarter" (+9bps QoQ) verified verbatim at p.12 (Sunil Samdani's financial highlights, line-range 477–519) — note this specific pair of numbers is NOT on the page(s) B06 cites for this claim (B06 gives no page for the raw figures themselves inside the Claim-4 paragraph, only narrative page cites; not a hard miscite, see Finding D-1 below for the related characterization issue). Abhijit Tibrewal's question naming "bond yields... geopolitical environment" is verified verbatim at p.16 (line-range 651–695). Arvind Kapil's actual reply ("I wouldn't be too worried... I wouldn't be too worried on the net trade-off") and Sanjay Miranka's later reply ("there can be a small uptick here and there... we will more than be able to offset this impact") are verified verbatim at p.16–17 and p.19 respectively — see Finding D-1: B06 attributes the "geopolitical environment" framing to management when it originates in the analyst's question. |
| UGROCAP Nov-2025 (Q2 FY26) | SUBSTANTIVE | YES | "the current market is a little bit stressed in terms of customers being a little bit of over-leveraged" verified verbatim at p.6 (line-range 211–249). "micro and small SMEs... adjacent to microfinance" and "stopped doing loans less than INR7.5 lakh ticket size" (floor raised from Rs 5 lakh) verified verbatim at p.7 (line-range 250–289) — the combined "p.6-7" citation is exact. Shachindra Nath's "almost at every point of time when we reach roughly around 18% of capital adequacy, we need to raise more capital... every 1 year, 1.5 years" verified verbatim at p.9 (line-range 329–369). CRAR 25.4% verified at p.4 (line-range 129–169), and the Rs 550 Cr preferential + Rs 380 Cr rights-issue figures verified at p.9 — the compound "(p.4, p.9)" citation is exact. |
| UGROCAP Feb-2026 (Q3 FY26) | SUBSTANTIVE | YES, with one MINOR page drift | "the quality of ROA would improve dramatically... spread income, NPV values get recognized... that would convert to more interest-led income" is real and verified verbatim, but sits one page later than cited: the .txt page-map places it at p.10 (line-range 385–426), not p.9 as B06 states. The broader ROA-quality discussion (co-lending's declining share of the 4% ROA target) does continue on to p.12–13, so the compound citation "p.9, p.13-14" is off by one page on its first leg but the underlying claim is genuinely supported in this transcript. |
| UGROCAP Apr-2026 (Q4 FY26) | SUBSTANTIVE | YES | "The move from 2.2% to 2.5% GNPA is a denominator effect as the non-focus book runs down; it is essentially not a deterioration in the incremental portfolio" verified verbatim at p.6 (line-range 212–251) — exact match to B06's citation. |
| UGROCAP Aug-2026 (Q1 FY27) | SUBSTANTIVE | YES, with one MINOR mis-citation | "portfolio yield rose to 18.1%. Now this was up 63 bps quarter-over-quarter" verified verbatim at p.7 (line-range 263–304), matching B06's "p.7" citation for the 2B pricing point exactly. "Income from co-lending and direct assignment is now about 14% of total income as against 24% in Q4'FY26" is also on p.7, NOT on p.4 or p.9 as B06's Claim-3 citation states. The separate "4% in the end of the next 12 quarters or now 11 quarters" target IS correctly on p.9 (line-range 329–369, Shachindra Nath). So the compound citation "(p.4, p.9)" correctly anchors the 11-12-quarter target but mis-anchors the 24%→14% figure, which belongs on p.7 (see Finding D-2). "competitive intensity, large lenders" verified verbatim at p.18 (line-range 725–767), matching the Part 2D citation exactly. |

10 of 11 effective peer transcripts SUBSTANTIVE, 1 CITED-ONLY, 0 UNUSED —
matches B06's own count exactly.

---

## PART 2: INDEPENDENT ZERO-MATCH CHECK (Claim 3, FLDG/DLG)

B06 asserts "a systematic search of all 11 transcripts for 'FLDG', 'DLG',
and 'first loss' returns ZERO matches in any peer transcript." I ran a
case-insensitive regex search for `FLDG|DLG|first loss|first-loss` across
all 12 files in the peer-concalls directory independently (not trusting
B06's own search) and got zero matches in every file. This claim is
CONFIRMED — not merely asserted but independently reproduced.

---

## PART 3: VERDICT-DISCIPLINE AUDIT

Six claims handed off from B05's peer_questions list; all six received a
verdict in B06 (claims_all_addressed: true — no skipped claim).

| Claim | B06 verdict | Peer anchors used | Discipline check |
|---|---|---|---|
| 1. Divergence-beneath-calm-surface | PARTIALLY VERIFIED | SBICARD Jul-26 (independent, adjacent axis) + UGROCAP Nov-25 (independent, adjacent axis); POONAWALLA silent | 2 independent peers, correctly NOT upgraded to full VERIFIED since axis/magnitude differ from Kissht's own claim. Correct discipline. |
| 2. DPD write-off trigger extension | PARTIALLY VERIFIED | 1 peer only (POONAWALLA, 180 DPD); SBICARD/UGROCAP silent on any figure | Only ONE peer discloses a comparable figure. B06 correctly does NOT call this VERIFIED (it explicitly notes "Only one of three peers discloses a number at all") — this is the correct discipline call under rule 4 (a verdict resting on one peer must not be VERIFIED), and B06 already downgrades it to PARTIALLY VERIFIED rather than over-claiming. No violation. |
| 3. FLDG/DLG peer benchmark | UNVERIFIABLE | 0 peers (independently confirmed zero-match, Part 2 above) | Correctly UNVERIFIABLE, not silently resolved either way. |
| 4. Cost-of-borrowing tailwind | CONTRADICTED | SBICARD Jul-26 + POONAWALLA Jul-26, both same quarter | 2 independent peers, both genuinely reporting flat-to-rising cost of borrowing for the same quarter Kissht claimed easing. Correctly graded CONTRADICTED, not silently softened. See Finding D-1 for a characterization nuance within this claim's supporting narrative. |
| 5. Competitive naming | UNVERIFIABLE | 0 peers name Kissht/Bajaj/Chola | Correctly UNVERIFIABLE. |
| 6. Capital-raise precedent | CONTRADICTED | POONAWALLA May-26 + UGROCAP Nov-25, both with numeric rationale | 2 independent peers, correctly graded CONTRADICTED as a precedent (both peers gave numeric triggers Kissht's raise lacks). |

No VERIFIED verdict rests on fewer than two peers (none reach full VERIFIED
at all, so this failure mode cannot occur here). No verdict is upgraded
from silence — the two UNVERIFIABLE claims are left as such rather than
being read as either confirmation or refutation. Verdict discipline is
sound across all six claims.

---

## PART 4: FINDINGS

**D-1 (MINOR).** Claim 4's narrative states Poonawalla's rising Q1 FY27
cost of borrowing is something "management (Arvind Kapil, Sanjay Miranka)
attributes to bond-yield and 'geopolitical environment' pressure." On the
transcript, the "geopolitical environment" phrase is introduced by analyst
Abhijit Tibrewal inside his question (p.16: "given the geopolitical
environment"), not volunteered by management. Arvind Kapil's actual reply
neither confirms nor engages that specific framing ("I wouldn't be too
worried... I think we could be very comfortably NIM accretive"), and Sanjay
Miranka's later reply (p.19) is measured ("there can be a small uptick here
and there... we will more than be able to offset this impact"), not an
attribution to geopolitical pressure. The underlying fact the claim rests
on — cost of borrowing rose 7.63%→7.72% QoQ, no FCNR(B)-style easing cited —
is correct and independently verified; only the framing of WHO named
geopolitical pressure as the cause is imprecise. This does not change the
CONTRADICTED verdict or its materiality to Stage 11's margin bridge, so it
is MINOR, not MAJOR.

**D-2 (MINOR).** Claim 3's UGROCAP Aug-2026 citation "(p.4, p.9)" for "from
24% of total income in Q4 FY26 to 14% in Q1 FY27" mis-anchors the 24%→14%
figure, which is actually on p.7 (Shilpa Bhatter's financial highlights),
not p.4 or p.9. The separate "4% within 11-12 quarters" target figure in
the same sentence IS correctly anchored to p.9. Both figures are genuinely
in the transcript and correctly quoted; only the page number for one of the
two figures is wrong. Claim 3 is UNVERIFIABLE regardless (this is
background cross-read material, not load-bearing for that verdict), so
this is MINOR.

**D-3 (MINOR).** Claim 3 (Part 1) / 2E's UGROCAP Feb-2026 citation "p.9,
p.13-14" for the realised-vs-unrealised ROA-quality framing places the
specific "NPV values... interest-led income" quote one page later than
cited: it sits at p.10 by the file's own [page N] markers, not p.9. The
quote itself is real and accurately paraphrased; only the page number is
off by one, likely a boundary-counting slip rather than a fabricated
anchor.

No CRITICAL or MAJOR findings. No fabricated quotes, no invented peer
statements, no SUBSTANTIVE claim lacking a real citation, and no peer
material that should have been used but was missed (the single CITED-ONLY
transcript, SBICARD Oct-2025, was read in full and contains nothing
claim-relevant that B06 left out).

---

## PART 5: SUMMARY

B06 used the peer corpus honestly and with real citations in essentially
every case audited. Of roughly 20 distinct quoted or paraphrased anchors
checked against the underlying .txt page-marker maps, 17 were exact, and 3
carried a MINOR page-number or attribution imprecision that does not change
any claim's verdict or any coverage-map classification. The zero-match
claim on FLDG/DLG (Claim 3) was independently reproduced by a fresh corpus
grep rather than merely trusted. Verdict discipline (two-peer bar for
VERIFIED, no upgrade from silence, all six handed-off claims addressed) is
sound throughout.

```yaml
stage: B12d
company: "KISSHT"
run_date: "2026-09-19"
model: claude-sonnet-5
status: complete
peers_audited: 11
substantive_confirmed: 10
substantive_unsupported: []
unused_but_relevant: []
claims_all_addressed: true
verdict_discipline_fails: []
findings:
  - {severity: "MINOR", location: "B06 Claim 4 narrative", claimed: "management (Arvind Kapil, Sanjay Miranka) attributes rising cost of borrowing to bond-yield and 'geopolitical environment' pressure", source_truth: "the 'geopolitical environment' phrase originates in analyst Abhijit Tibrewal's question (POONAWALLA-Concall_Jul_2026_Transcript.txt p.16); management's actual replies (p.16-17, p.19) are measured and do not adopt that framing explicitly", note: "underlying number and CONTRADICTED direction are correct and independently verified; only the attribution of who named the cause is imprecise"}
  - {severity: "MINOR", location: "B06 Claim 3, UGROCAP Aug-2026 citation", claimed: "24% of total income in Q4 FY26 to 14% in Q1 FY27 — UGROCAP-Concall_Aug_2026_Transcript.txt p.4, p.9", source_truth: "the 24%->14% figure is on p.7 (Shilpa Bhatter's financial highlights); only the separate '4% within 11-12 quarters' target is on p.9; p.4 contains neither number", note: "figures are real and correctly quoted; page anchor for one of the two figures is wrong; Claim 3 remains UNVERIFIABLE regardless"}
  - {severity: "MINOR", location: "B06 Part 2E, UGROCAP Feb-2026 citation", claimed: "realised-vs-unrealised ROA quality framing — UGROCAP-Concall_Feb_2026 p.9, p.13-14", source_truth: "the specific 'NPV values / interest-led income' quote sits at p.10 by the file's [page N] markers, one page later than cited; broader discussion does continue to p.12-13", note: "quote is real and accurately paraphrased; page number off by one"}
critical_count: 0
major_count: 0
minor_count: 3
acceptance_rate: 100
```
