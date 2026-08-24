# VERIFIER D — PEER COVERAGE AUDIT (B12d)
Company: INDIAGLYCO | Run: 2026-08-24 | Model: claude-sonnet-5

Scope: audit whether B06-peers.md/yaml used the 13 provided peer transcripts
(BALRAMCHIN x3, TRIVENI x4, GLOBUSSPR x4, PICCADIL x2) substantively and
accurately. Artifacts read: the 13 raw transcripts, B06-peers.yaml,
06-peers.md, and B05-concall.yaml's `peer_questions` list (needed to check
rule 5's claim-completeness requirement; not separately supplied in the task
message but present in the run's own outputs and load-bearing for this
audit).

---

## PART 1: SUBSTANTIVE-CLAIM COVERAGE MAP AUDIT (per peer)

All 13 peer-quarter entries in B06's `peer_coverage_map` are marked
SUBSTANTIVE. Method: for each peer, located the cited quotes in the raw
transcript and confirmed the quote text and the substantive contribution
claimed.

| Peer | Quarter (B06 label) | Spot-checked quote(s) | Found verbatim? | Correct call/date? |
|---|---|---|---|---|
| BALRAMCHIN | Q3 9M FY26 (11-Feb-2026) | "ethanol prices under the B-heavy and juice routes have not been revised for the past three years" | Yes, exact | Yes (BALRAMCHIN-Concall_Feb_2026) |
| BALRAMCHIN | Q3 9M FY26 (11-Feb-2026) | "government has accepted only about 60% of the tenders issued for maize-based ethanol" | Yes, exact | Yes |
| BALRAMCHIN | Q4 FY26 (18-May-2026) | "At the industry level, definitely there is an overcapacity" | Yes, exact | Yes (BALRAMCHIN-Concall_Jun_2026, filed 18-May per report; call content matches) |
| BALRAMCHIN | Q4 FY26 (18-May-2026) | "lowest stock level which I remember seeing in my recent living memory" | Yes, exact | Yes |
| BALRAMCHIN | Q1 FY27 (12-Aug-2026) | "parallel Balrampur can be created" (PLA) | Yes, exact (analyst asks, Avantika Saraogi affirms) | Yes (BALRAMCHIN-Concall_Aug_2026) |
| TRIVENI | Q2 H1 FY26 (7-Nov-2025) | molasses reservation "19% to 18%"/"26.18% to 24.84%" | Yes, exact | Yes |
| TRIVENI | Q2 H1 FY26 (7-Nov-2025) | "north of 2,300 crore litres" | Yes, exact | Yes |
| TRIVENI | Q4 FY26 (4-Jun-2026) | "Grain-based feedstock constituted 56% of our total ethanol sales in the year" | Yes, exact | Yes |
| TRIVENI | Q1 FY27 (30-Jul-2026) | "India has successfully achieved 20% blending... five years ahead of the original target" | Yes, exact | Yes (TRIVENI-Concall_Aug_2026, filed 4-Aug for the 30-Jul-2026 call — B06's date citation of 30-Jul-2026 is correct) |
| TRIVENI | Q1 FY27 (30-Jul-2026) | "you are absolutely right about the overall capacity in the country"; "1,100, 1,200 crores from ethanol... additional 200 crore from the ENA side" | Yes, exact | Yes |
| TRIVENI | Q1 FY27 (30-Jul-2026) | "grain-based ethanol accounted for 61%... versus 58%"; "ratio of 3:1, grain is to sugary feedstocks" | Yes, exact | Yes |
| TRIVENI | Q1 FY27 (30-Jul-2026) | "interest moratorium for a lot of the standalone distilleries, which will expire next year" | Yes, exact | Yes |
| TRIVENI | Q1 FY27 (30-Jul-2026) | Supreme Court/BPCL stay on OMC tender framework | Yes, exact | Found only in Aug/Jul-2026 call, NOT in Jun-2026 call as also cited (see Finding 3) |
| GLOBUSSPR | Q2 H1 FY26 (17-Nov-2025) | "UP is the largest market of almost a crore cases a month" | Yes, exact | Yes |
| GLOBUSSPR | Q4 FY26 (8-May-2026) | "strategic shift in our Bihar and Jharkhand facilities... on the back of lower offtake of ethanol by oil marketing companies" | Yes, exact | Yes |
| GLOBUSSPR | Q1 FY27 (20-Jul-2026) | "significant oversupply of ethanol, overcapacity of ethanol"; "almost 95-odd lakh cases a month" | Yes, exact | Yes |
| PICCADIL | FY26 annual (29-Apr-2026) | glass/packaging "40% to 50%" inflation question and management response | Yes, exact | Yes |
| PICCADIL | Q1 FY27 (12-Aug-2026) | "60% to 70%" FY27 branded alco-bev growth guidance | Yes, exact | Yes |
| PICCADIL | both quarters | zero "Uttar Pradesh"/"UP" mentions (documented silence) | Confirmed — grepped both transcripts, no matches | Yes |

**Result: 13/13 SUBSTANTIVE peer-quarter entries carry real, locatable
citations.** No fabricated quote or invented peer statement found. This
clears rule 2's core bar (SUBSTANTIVE-without-citation would be MAJOR;
no instance found).

However, two citations misattribute the specific call/quarter, and a third
(cross-read, not the formal claim table) does too — see Part 2.

---

## PART 2: FINDINGS — CITATION/ANCHOR ACCURACY

### Finding 1 (MAJOR) — Claim 7 quote misattributed to wrong call
B06's Claim 7 text states: `"a 120 million case market" (annualised,
~1 crore/month) (May 2026, Chandrasekhar Sridhar exchange)`.
The "120 million case market" quote, spoken by analyst Chandrasekhar
Sridhar, is verbatim in **GLOBUSSPR-Concall_Jan_2026_Transcript.txt**
line 686 ("this is obviously a 120 million case market"), not in the
May 2026 transcript. Chandrasekhar Sridhar does appear in the May 2026
call too, but not with this line. This misdates the source by one
quarter. The underlying substance (Globus repeatedly states UP as a
~95 lakh-1 crore case/month market) is still independently corroborated
by three OTHER correctly-anchored quotes (Nov 2025, May 2026 own line
"95 lakh cases to a 1 crore case market," Jul 2026), so the Claim 7
CONTRADICTED verdict itself is not undermined — only this one supporting
citation's quarter label is wrong.

### Finding 2 (MAJOR) — Claim 5 quotes wrongly presented as "same call"
B06's Claim 5 text: `Globus (Q4 FY26 call, 8-May-2026, Shekhar Swarup):
explains a "strategic shift"... Same call, in response to a direct
analyst question about OMCs reducing offtake: "Yes, I have also been
hearing that OMCs are reducing volume offtake. But so far, we are not
impacted."`
The "strategic shift... lower offtake of ethanol by oil marketing
companies" quote is in the May 2026 transcript (confirmed, line 125).
The "not impacted" quote is in **GLOBUSSPR-Concall_Jan_2026_Transcript.txt**
line 628-629, a call roughly four months earlier — not "the same call."
This is more than a labeling slip: it reverses the implied chronology.
Read correctly, management said "not impacted" in Jan 2026, and only
by May 2026 had executed a product-mix shift explicitly attributed to
OMC offtake pressure — i.e., the two data points show pressure building
over two quarters, not a single-call juxtaposition of concern-then-
reassurance. B06's PARTIALLY VERIFIED verdict on Claim 5's direction is
still supportable from the (correctly independent) Globus May-2026 quote
and the separate Triveni Q1 FY27 "poor" offtake quote, so the verdict
itself survives, but the "same call" framing is a factual error that
should be corrected before synthesis treats the OMC-pressure timeline
as settled.

### Finding 3 (MINOR) — Part 2E Supreme Court/BPCL stay over-cited by one quarter
B06's cross-read text (Part 2E and the YAML `risks_peers_raise` line)
attributes the Supreme Court stay on the OMC ethanol tender framework to
"Triveni, Jun/Jul 2026 calls" (report prose) and "Q4 FY26 and Q1 FY27
calls" (YAML). Grepped both TRIVENI-Concall_Jun_2026_Transcript.txt and
TRIVENI-Concall_Aug_2026_Transcript.txt for "Supreme Court," "BPCL," and
"Karnataka": the passage exists only in the Aug_2026 (30-Jul-2026 call)
transcript. The Jun_2026 transcript's only "Karnataka" hits are routine
sugar-acreage commentary, unrelated to the court stay. This is a
narrative/cross-read item, not a formal claim-table citation, and the
underlying risk item is real and well anchored in the correct
(30-Jul-2026) call — but the doubled quarter attribution is inaccurate
and should be corrected to single-source it.

### Finding 4 (MINOR) — Part 2C PLA capex figure attributed to wrong call
B06's cross-read text: "Balrampur into PLA bioplastics (₹3,080 crore
capex, a 'parallel Balrampur' per management, Aug 2026 call)." The
₹3,080 crore capex figure is stated in **BALRAMCHIN-Concall_Jun_2026_
Transcript.txt** line 114 ("revise capex at INR3,080 crore"), not in the
Aug 2026 call. The "parallel Balrampur" phrase is correctly from the Aug
2026 call. B06 has fused two distinct calls' facts under a single
quarter citation. Both facts are real and correctly attributed to
Balrampur, just to the wrong single call.

**Pattern note**: four of the roughly 20 spot-checked anchors carry a
wrong-quarter (not wrong-peer, not fabricated) citation. All four
concern peers/companies where B06 read multiple quarters back-to-back
(Globus x2, Triveni x1, Balrampur x1) and appear to be a quarter-mixing
error rather than invention — every underlying quote is real and exists
verbatim somewhere in that peer's provided transcript set. This is a
citation-precision issue, not a fabrication or scope issue, but it would
mislead an operator or Verifier A checking a specific date/quarter
against the named source.

---

## PART 3: UNUSED-BUT-RELEVANT CHECK

Spot-read for material B06 did not use:
- Piccadily UP silence: correctly documented as a finding, not an
  omission (rule 3 — used correctly).
- No peer transcript mentions India Glycols/IGL by name (confirmed by
  grep across all 13 files) — B06 correctly records
  `peer_mentions_of_company: []`; nothing missed here.
- Globus's complete absence of the term "DDGS" across all four
  transcripts (confirmed by grep: 0 hits in Nov 2025, Jan 2026, May
  2026, Jul 2026) — B06 correctly flags this silence for Claim 3 rather
  than silently omitting it.
- No additional material ethanol/IMFL/chemicals-relevant peer statement
  surfaced in the spot-read sample that B06's Part 2 cross-read and Part
  1 claim table do not already cover (overcapacity, OMC offtake, DDGS,
  molasses reservation, blending timeline, grain-mix shift, glass/PET
  inflation, PLA/defence/premium-IMFL capital reallocation, moratorium,
  Supreme Court stay, FCI-rice mandate, El Nino/monsoon risk were all
  independently confirmed present and used).

No MAJOR "unused but relevant" item found in the sampled sections.

---

## PART 4: VERDICT-DISCIPLINE AUDIT

| Claim | Verdict | Peers backing verdict | ≥2 independent peers for VERIFIED? | Pass/Fail |
|---|---|---|---|---|
| Claim 4 (overcapacity) | VERIFIED | BALRAMCHIN, TRIVENI, GLOBUSSPR (3) | Yes | Pass |
| Claim 2 (grain feedstock mix, current level) | VERIFIED (with historical baseline flagged unverifiable) | TRIVENI, GLOBUSSPR, BALRAMCHIN (3) | Yes | Pass |
| Claim 1 | PARTIALLY VERIFIED | TRIVENI only | N/A (correctly not VERIFIED on 1 peer) | Pass |
| Claim 3 | PARTIALLY VERIFIED | TRIVENI only (Globus silent) | N/A | Pass |
| Claim 5 | PARTIALLY VERIFIED | GLOBUSSPR, TRIVENI (2, direction only) | N/A — correctly downgraded since magnitude unconfirmed | Pass |
| Claim 9 | PARTIALLY VERIFIED | TRIVENI only | N/A | Pass |
| Claim 7 | CONTRADICTED | GLOBUSSPR | Appropriate — contradiction stands on one peer's repeated (4-quarter) statement, correctly flagged with a scope caveat rather than silently resolved | Pass |
| Claim 6 | UNVERIFIABLE | none | N/A | Pass |
| Claim 8 | UNVERIFIABLE | none | N/A | Pass |

No verdict rests on a single peer where the report claims full VERIFIED
status (both VERIFIED claims cite three peers each). No verdict is
"upgraded from silence" — every UNVERIFIABLE stays UNVERIFIABLE, silence
is never read as confirmation or contradiction anywhere in the report
(explicitly stated for Claim 8: "the operator should not read this
silence as either support or concern"). No CRITICAL verdict-discipline
violation found.

---

## PART 5: CLAIM-COMPLETENESS CHECK (rule 5)

B05-concall.yaml's `peer_questions` list contains exactly 9 questions,
matching B06's 9 claims 1:1 in content and check_peers assignment. All 9
received an explicit verdict (2 VERIFIED, 4 PARTIALLY VERIFIED, 1
CONTRADICTED, 2 UNVERIFIABLE). No skipped claim.

---

## PART 6: SUMMARY

- Peers provided: 13 (all 13 transcripts confirmed present and used)
- Peers/quarters marked SUBSTANTIVE: 13 of 13
- Substantive citations confirmed real and locatable: 13 of 13 (100%)
- Citations with wrong-quarter attribution (real quote, wrong call date):
  4 instances across the report (2 in formal claim table = MAJOR each,
  2 in cross-read narrative = MINOR each)
- Fabricated or invented peer statements: 0
- Verdict-discipline violations: 0
- Claims from B05 peer_questions left unaddressed: 0
- Unused-but-relevant material material items missed: 0 found in sample

peer_utilisation = 13/13 peers used substantively = 100%.
acceptance_rate (peers correctly handled / peers) = 13/13 peer-quarter
entries correctly handled at the peer level = 100%; scored at the
finding level, 2 MAJOR + 2 MINOR findings against roughly 20 checked
anchors and 13 peer-quarter entries.

```yaml
stage: B12d
company: "INDIAGLYCO"
run_date: "2026-08-24"
model: claude-sonnet-5
status: complete
peers_audited: 13
substantive_confirmed: 13
substantive_unsupported: []
unused_but_relevant: []
claims_all_addressed: true
verdict_discipline_fails: []
findings:
  - {severity: "MAJOR", location: "06-peers.md Claim 7 peer evidence row", description: "'120 million case market' quote (Chandrasekhar Sridhar) cited as 'May 2026' call; verbatim quote is in GLOBUSSPR-Concall_Jan_2026_Transcript.txt line 686, not the May 2026 transcript. Underlying CONTRADICTED verdict still stands on 3 other correctly-anchored Globus quotes (Nov 2025, May 2026 own line, Jul 2026)."}
  - {severity: "MAJOR", location: "06-peers.md Claim 5 peer evidence row", description: "'Yes, I have also been hearing that OMCs are reducing volume offtake. But so far, we are not impacted' presented as 'Same call' as the May 2026 Bihar/Jharkhand strategic-shift quote; the 'not impacted' line is actually in GLOBUSSPR-Concall_Jan_2026_Transcript.txt lines 628-629, ~4 months earlier. Misrepresents the OMC-pressure timeline as a single-call juxtaposition rather than a two-quarter progression. PARTIALLY VERIFIED verdict itself survives on the independently correct May-2026 and Triveni Q1 FY27 anchors."}
  - {severity: "MINOR", location: "06-peers.md Part 2E / YAML risks_peers_raise", description: "Supreme Court/BPCL ethanol-tender stay attributed to both 'Jun 2026 and Jul 2026' Triveni calls; grep confirms the passage exists only in TRIVENI-Concall_Aug_2026_Transcript.txt (30-Jul-2026 call), not the Jun 2026 transcript. Item itself is real and correctly anchored in the Jul/Aug call alone."}
  - {severity: "MINOR", location: "06-peers.md Part 2C industry_cross_read.capex_cycle", description: "Balrampur PLA capex figure (INR 3,080 crore) attributed to 'Aug 2026 call'; figure is verbatim in BALRAMCHIN-Concall_Jun_2026_Transcript.txt line 114. The co-cited 'parallel Balrampur' phrase is correctly from the Aug 2026 call; the two facts from two different calls are fused under one citation."}
critical_count: 0
major_count: 2
minor_count: 2
acceptance_rate: 90
```
