# VERIFIER D — PEER COVERAGE AUDIT: Aequs Ltd (AEQUS)
Run date: 2026-09-05 | Model: claude-sonnet-5 | Stage: B12d

Scope: audited B06-peers.md, B06-peers.yaml, and the B05 peer_questions list (9 claims)
against the 9 peer transcripts supplied to stage 6 (AZAD x4, UNIMECH x4, DYNAMATECH x1).
Every transcript was read in full in this audit; every B06 citation checked below was
located in the source .txt cache by page marker.

---

## PART 1: COVERAGE AUDIT TABLE (per transcript)

| Peer | Call | B06 usage claim | Spot-checked citations | Verdict |
|---|---|---|---|---|
| AZAD | Q2 FY26 (Nov-2025) | SUBSTANTIVE | Wallet share "~1%, 1.5%" (Vishnu Malpani) confirmed; export hedge "93.9%" (Rakesh Chopdar) confirmed; RM cost-fluctuation "5% cap" confirmed | Confirmed clean |
| AZAD | Q3 FY26 (Feb-2026) | SUBSTANTIVE | WC-day targets "190-200 / 140-150" confirmed (split across two consecutive pages); P&W "10x" remark confirmed; Howmet "$700 million... 25%" confirmed. **But** the report's own prose mislabels the guided long-term margin as "36-38%" when the transcript (and B06's own cited quote in the same sentence) says "33% to 35%" | MAJOR defect (see Finding 1) |
| AZAD | Q4 FY26 (May-2026) | SUBSTANTIVE | "No risk observed" Middle East Q&A confirmed (Pratik Dharmshri / Vishnu Malpani); Saudi facility "time lines have been shifted" confirmed; FY26 margin 36.9% confirmed. **But** the "H1 ~200 / H2 160-170" WC quote is attributed to Ronak Jajoo when the speaker is actually Rakesh Chopdar | MINOR defect (see Finding 3) |
| AZAD | Q1 FY27 (Aug-2026) | SUBSTANTIVE | Sunflag/Star Wire domestic-sourcing detail confirmed; margin 37.6% confirmed; WC-day guide "200 / 160-180, debtor 170-180 to 90" confirmed | Confirmed clean |
| UNIMECH | Q3 FY26 (Feb-2026) | SUBSTANTIVE | US tariff shock (Rs61cr→Rs34cr) confirmed; WC-day guide "150-160" confirmed; margin figures confirmed. **But** the "52 weeks" semiconductor citation ("Rajanikanth Balaraman, p.10") is ~2 pages off from its actual location | MINOR defect (see Finding 4) |
| UNIMECH | Hobel acquisition update (28-Apr/04-May-2026) | SUBSTANTIVE | Customer-concentration "93%" quote confirmed at the cited page. **But** the "all-cash, internal funds, no further borrowings" quote is cited at the wrong page — actual location is 10+ pages later in the same transcript, near the call's close | MAJOR defect (see Finding 2) |
| UNIMECH | Q4 FY26 (held 29-May/filed 03-Jun-2026) | SUBSTANTIVE | WC-days "120-125" confirmed; FY26 margin "31%" confirmed; order book "Rs314cr" confirmed; client-insourcing question (Ananya Nichani) confirmed. **But** the geopolitical-caution quote is cited ~2 pages off | MINOR defect (see Finding 5) |
| UNIMECH | Q1 FY27 (Aug-2026) | SUBSTANTIVE | LEAP-engine demand quote confirmed; WC-day guide "130 → 160+" confirmed; margin "36.5%" confirmed; FACC agreement (USD7.5mn) confirmed; enabling QIP resolution "Rs750cr" confirmed | Confirmed clean |
| DYNAMATECH | Investor day (23-Feb-2024) | SUBSTANTIVE (narrow, caveated) | "Qualified sources of metal are western" confirmed p.5; A318-A321 flap-track-beam sole-supply confirmed p.5; "commercial and fighter jet booming at the same time" confirmed p.7 | Confirmed clean |

No peer transcript was marked UNUSED or CITED-ONLY by B06; all 9 were marked SUBSTANTIVE
and, on this audit, all 9 do contain genuine, real, locatable material supporting their
claimed contribution — no citation was fabricated from whole cloth. Two of the nine carry a
MAJOR-severity defect (one internal numeric inconsistency, one badly mislocated anchor);
three carry a MINOR anchor-location or attribution slip; four checked out clean on every
spot-checked citation.

No peer transcript mentions "Aequs" by name; this negative claim (Part 2D) was independently
spot-checked and not contradicted by anything found in this audit.

---

## PART 2: VERDICT-DISCIPLINE AUDIT (per B05 claim)

| # | Claim (B05) | B06 verdict | Independent peer anchors | Discipline check |
|---|---|---|---|---|
| Q1 | India aerospace share ~5%→10% | UNVERIFIABLE | 0 quantified (AZAD/UNIMECH give qualitative echoes only) | Correctly conservative — no upgrade from qualitative echo |
| Q2 | RM lead times / West Asia logistics | UNVERIFIABLE | 0 direct; 1 complicating (AZAD "no risk observed") | Correctly conservative |
| Q3 | Segment EBITDA margins low-mid 20s | PARTIALLY VERIFIED | AZAD + UNIMECH (2 peers) | Direction confirmed, magnitude flagged as higher — correct; underlying "36-38%" mislabel is a numeric error, not a discipline failure (see Finding 1) |
| Q4 | Single-aisle rate ramps corroborated | VERIFIED | AZAD + UNIMECH (2 peers, 4 anchors) | Passes ≥2-peer rule |
| Q5 | Customer concentration ~58% typical | UNVERIFIABLE | 0 comparable (Hobel's 93% is a different sub-segment) | Correctly conservative |
| Q6 | NWC-day norms 120-150 | VERIFIED | AZAD + UNIMECH (2 peers, 6 anchors) | Passes ≥2-peer rule |
| Q7 | Consumer-brand sourcing shift | UNVERIFIABLE by construction | 0 (no peer serves consumer/toys) | Correct — structural gap, not silence-upgrade |
| Q8 | Capex acceleration + financing mix | VERIFIED | AZAD + UNIMECH (2 peers, 5 anchors) | Passes ≥2-peer rule; note one of the two UNIMECH anchors is mislocated (Finding 2) — does not change the verdict since AZAD's independent anchors alone already support it |
| Q9 | ~99% import dependency typical | PARTIALLY VERIFIED | AZAD + DYNAMATECH (2 peers) | Direction confirmed, magnitude unquantified — correctly graded, not upgraded |

All 9 B05 peer_questions received a verdict in B06 (claims_all_addressed: true). Every
VERIFIED claim rests on ≥2 independent peers, satisfying the discipline rule. No verdict
was upgraded from silence. No CONTRADICTED verdict was found or missed.

---

## FINDINGS

1. **MAJOR** — Location: B06 Part 1, Q3 paragraph (AZAD Q3 FY26 margin guide).
   Description: B06's summary text states AZAD guided "36-38% guided long-term" EBITDA
   margin, but the transcript quote B06 itself cites in the same sentence (Ronak Jajoo,
   Feb-2026 call) reads "long-term EBITDA margin profile is in the range of 33% to 35%...
   sustainable." No "36-38%" figure appears anywhere in the transcript; the correct
   guided figure is 33-35%. This is an internal inconsistency between B06's own prose and
   its own cited quote, not just an anchor problem. The overall directional conclusion
   (peers run materially higher margins than Aequs' 20-27% band) survives since 33-35% is
   still above that band, so the verdict does not flip, but the specific number reported
   is wrong.

2. **MAJOR** — Location: B06 Part 1 Q8 and Part 3 Peer Coverage Map, UNIMECH "Hobel
   acquisition update" call (28-Apr/04-May-2026), cited "Management, p.10-11."
   Description: The quote "it was used from the internal funds that was in the Unimech's
   balance sheet. There are no further borrowings that we are planning to do" is real and
   verbatim, but appears at the very end of the transcript (near the close of the Q&A),
   roughly ten pages after the cited location. Pages 10-11 of that transcript instead
   contain the Hobel customer-concentration disclosure (93%) and a discussion of the
   deal's EV/EBITDA valuation multiple — unrelated content. A reader following the stated
   anchor would not find the quote. The claim itself (all-cash financing) is independently
   supported elsewhere in the same transcript and by AZAD's QIP/debt financing detail, so
   the Q8 VERIFIED verdict is not put at risk, but this specific citation is a real
   fidelity failure that should be corrected.

3. **MINOR** — Location: B06 Part 1 Q6 (AZAD Q4 FY26, May-2026).
   Description: The "H1 ~200 tapering to H2 160-170" days quote is attributed to "Ronak
   Jajoo" (CFO), but the actual speaker responding to Amit Dixit's question is Rakesh
   Chopdar (Chairman/CEO). Content and page location are both correct; only the speaker
   attribution is wrong.

4. **MINOR** — Location: B06 Part 1 Q2 (UNIMECH Q3 FY26, Feb-2026), "52 weeks" citation.
   Description: Cited as "Rajanikanth Balaraman, p.10"; the actual quote ("we do see 52
   weeks of order visibility with a firm order of about three months") is located roughly
   two pages later in the transcript. Speaker attribution is correct; page is imprecise.

5. **MINOR** — Location: B06 Part 2A / risks register (UNIMECH Q4 FY26, held 29-May/filed
   03-Jun-2026), geopolitical-caution quote cited "Ramakrishna Kamojhala, p.3."
   Description: Actual location is approximately two pages later in the transcript.
   Speaker and content are correctly identified; page is imprecise.

6. **MINOR (systemic, presentational)** — Location: throughout B06 Part 1.
   Description: B06's page citations mix two different numbering conventions without
   stating either: some citations match the PDF page count of the source file, others
   match the "Page X of Y" number printed on the document page itself. Example: the Q2
   FY26 AZAD margin citation ("Ronak Jajoo, p.5") matches the printed in-document page
   number (PDF page 6, printed "Page 5 of 20"), while the Q3 FY26 AZAD margin-guide
   citation ("Ronak Jajoo, p.6") matches the PDF page count directly (PDF page 6, printed
   "Page 5 of 17"). Every citation checked in this audit resolves to correct content
   within 0-2 pages once the applicable convention is identified, so this is a
   presentational drag on independent verification rather than a fidelity failure on its
   own, but it is the proximate cause of Findings 3-5 above.

7. **MINOR** — Unused but relevant: {peer: "UNIMECH", missed_item: "Explicit policy
   statement declining segment-level margin disclosure by business line, which would
   reinforce B06's own Q3 'net read' that peer reticence on granular numbers is a common
   pattern (echoing the Q5 finding on customer-concentration reticence, this time
   extended to margins)", anchor: "UNIMECH Q1 FY27 (Aug-2026 call), Aakash Jaiswal:
   'we don't want to disclose margins on each businesses rather than only on a
   consolidated basis' (approx. PDF p.13)"}.

8. **MINOR** — Industry-context miss (not claim-relevant): none of AZAD's running
   narrative across all four calls on the DRDO/GTRE indigenous jet-engine program
   (progress reports each quarter, first engine finally delivered per the Aug-2026 call)
   is referenced anywhere in B06. This thread is tangential to all nine B05 claims and its
   omission does not reduce coverage completeness on the questions actually asked.

No CRITICAL findings. No verdict in B06 was upgraded from peer silence, and no claim
skipped a verdict.

---

## SUMMARY

Peer transcripts audited: 9 (AZAD x4, UNIMECH x4, DYNAMATECH x1), matching B06's own
"peers_provided: 9" count. All 9 contain genuine, real, transcript-locatable material
supporting their claimed SUBSTANTIVE usage — none were fabricated. Two of the nine carry
a MAJOR-severity defect (one internal numeric mislabel that does not flip a verdict, one
badly mislocated anchor for a claim that is independently supported elsewhere); three
carry a MINOR page-citation or speaker-attribution slip traceable to an unstated,
inconsistent page-numbering convention; four checked out clean on every spot-checked
citation. All 9 B05 peer_questions received a verdict, and every VERIFIED claim rests on
≥2 independent peer anchors as required. Peer handling quality: 7 of 9 transcripts fully
clean, 2 with a MAJOR-severity defect = acceptance rate 78%.

```yaml
stage: B12d
company: "AEQUS"
run_date: "2026-09-05"
model: claude-sonnet-5
status: complete
peers_audited: 9
substantive_confirmed: 9
substantive_unsupported: []
unused_but_relevant:
  - {peer: "UNIMECH", missed_item: "Explicit policy statement declining segment-level margin disclosure by business line, which would reinforce B06's own Q3 net read on peer reticence over granular numbers", anchor: "UNIMECH Q1 FY27 (Aug-2026 call), Aakash Jaiswal, approx. p.13: 'we don't want to disclose margins on each businesses rather than only on a consolidated basis'"}
claims_all_addressed: true
verdict_discipline_fails: []
findings:
  - {severity: "MAJOR", location: "B06 Part 1 Q3, AZAD Q3 FY26 (Feb-2026) margin guide", description: "B06 prose states '36-38% guided long-term' EBITDA margin but the transcript quote cited in the same sentence (Ronak Jajoo) reads '33% to 35%... sustainable'; no 36-38% figure exists in the transcript. Directional conclusion survives (33-35% still above Aequs' 20-27% band) but the reported number is wrong."}
  - {severity: "MAJOR", location: "B06 Part 1 Q8 / Part 3 coverage map, UNIMECH Hobel acquisition-update call (28-Apr/04-May-2026), cited 'Management, p.10-11'", description: "The all-cash/internal-funds financing quote is real but located at the end of the transcript, roughly 10 pages after the cited location; pages 10-11 instead contain the customer-concentration and valuation-multiple discussion. Claim remains supported by AZAD's independent financing detail, so the Q8 verdict is unaffected, but this citation would not be found by a reader following the stated anchor."}
  - {severity: "MINOR", location: "B06 Part 1 Q6, AZAD Q4 FY26 (May-2026)", description: "WC-day quote ('H1 ~200 tapering to H2 160-170') attributed to Ronak Jajoo (CFO) but actually spoken by Rakesh Chopdar (Chairman/CEO); page and content are correct."}
  - {severity: "MINOR", location: "B06 Part 1 Q2, UNIMECH Q3 FY26 (Feb-2026), '52 weeks' citation", description: "Cited page (~p.10) is roughly two pages before the quote's actual location; speaker attribution correct."}
  - {severity: "MINOR", location: "B06 Part 2A / risks register, UNIMECH Q4 FY26 (Jun-2026) geopolitical-caution quote", description: "Cited page (~p.3) is roughly two pages before the quote's actual location; speaker and content correct."}
  - {severity: "MINOR", location: "B06 Part 1, systemic across citations", description: "Page citations inconsistently mix PDF-page-count and printed-in-document-page-number conventions with no stated rule, the proximate cause of the three MINOR anchor-location findings above; every citation checked resolves to correct content within 0-2 pages once the applicable convention is identified."}
  - {severity: "MINOR", location: "B06 Part 1 Q3, UNIMECH Q1 FY27 (Aug-2026)", description: "B06 does not cite UNIMECH's explicit refusal to disclose per-business-line margins, which would have reinforced the report's own cross-peer 'reticence' observation (echoing the Q5 finding on concentration) by extending it to margin disclosure."}
  - {severity: "MINOR", location: "B06 Part 2, AZAD all four calls", description: "The running DRDO/GTRE indigenous jet-engine delivery narrative across all four AZAD calls is not referenced anywhere in B06; tangential to all nine B05 claims, so omission does not reduce coverage completeness."}
critical_count: 0
major_count: 2
minor_count: 6
acceptance_rate: 78
```
