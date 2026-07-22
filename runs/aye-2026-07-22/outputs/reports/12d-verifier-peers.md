# Verifier D — Peer Coverage Audit: AYE (Aye Finance), 2026-07-22

Model: claude-sonnet-5 | Fresh context | Artifacts audited: `06-peers.md` (B06) against the
11 raw peer transcripts in `_working/` (MASFIN x4, NORTHARC x4, SBFC x3) and the injected
`peer_questions` list in `05-concall.md` (B05).

Scope note: the task brief supplied 11 peer transcripts (MASFIN, Northern Arc, SBFC), not the
generic 12-transcript template baseline. B06 itself states it read 11 transcripts and I confirmed
11 peer-concall files exist in `_working/`. All coverage figures below are against this 11-transcript
universe, matching what B06 was actually given.

---

## 1. Peer coverage map: SUBSTANTIVE-citation audit

Method: for every row in B06 Part 3 marked SUBSTANTIVE, I located the literal quote/figure cited
in B06 Part 1 or Part 2 inside the named transcript file, confirmed the speaker attribution, and
checked the cited page number against the transcript's internal "Page N of M" footer (not the raw
OCR "===== PAGE X/Y =====" extraction marker, which is a different numbering).

| # | Peer / Quarter | B06 usage tag | Spot-checked citation | Found in transcript? | Speaker match? | Page match? |
|---|---|---|---|---|---|---|
| 1 | MASFIN Nov-2025 | SUBSTANTIVE | "range bound" net NPA 1.5-2%/gross 2.5-2.75%, cited p.9 | Yes, verbatim (line ~394) | Yes, Kamlesh Gandhi | Actually p.8, not p.9 (MINOR drift) |
| 2 | MASFIN Nov-2025 | SUBSTANTIVE | Net Stage-3 1.63%→1.69%, cited p.6-7 | Yes, verbatim (line ~338) | Yes, Darshana Pandya | Confirmed p.7 |
| 3 | MASFIN Nov-2025 | SUBSTANTIVE | Cost of borrowing 9.62%, incremental 9.25%, cited p.8 | Yes, verbatim (line ~382) | Management (unattributed in text but correct block) | Confirmed p.8 |
| 4 | MASFIN Feb-2026 Investor Day | SUBSTANTIVE | SIDBI-CRISIL Rs30 lakh crore MSME credit gap, cited p.16 | Yes, verbatim (line ~686) | Consistent with Dhvanil Gandhi's SME section | Actually p.15, not p.16 (MINOR drift) |
| 5 | MASFIN Jan-2026 (filed as "Feb_2026_Transcript_2") | SUBSTANTIVE | Approval funnel "14%, 15%... now ~20-odd percent," cited p.15 | Yes, verbatim (line ~682) | Yes, Dhvanil Gandhi | Confirmed p.15, exact match |
| 6 | NORTHARC May-2026 | SUBSTANTIVE | X-bucket collection efficiency 98.7%→99.4%→99.6% (rural finance), cited p.4-5 | Yes, verbatim (line ~177) | Management | Confirmed p.4 |
| 7 | NORTHARC May-2026 | SUBSTANTIVE | FY26 credit cost 2.8%, FY27 guided 2.7-2.8%, cited p.4-5 | Yes, verbatim, but the 2.7-2.8% FY27 guidance specifically is in the Chintan Shah/Pardhasaradhi Q&A exchange | Yes, correctly attributed in substance | FY26 2.8% figure is p.5; the FY27 2.7-2.8% guidance itself is on **p.11-13**, not p.4-5 (see finding D-2) |
| 8 | SBFC Jul-2025 | SUBSTANTIVE | Karnataka ordinance quote ("nothing to do with us... repair takes away the other 4"), cited p.3 | Yes, verbatim (line ~66) | Yes, Aseem Dhru | Confirmed p.3, exact match |
| 9 | SBFC Jul-2025 | SUBSTANTIVE | "not about geography... more about ticket sizes," cited p.4 | Yes, verbatim (line ~86) | Yes, Aseem Dhru | Actually p.7, not p.4 (see finding D-1) |
| 10 | SBFC Nov-2025 | SUBSTANTIVE | Approval rate "45% to 50% odd... below 40% odd," cited p.6 | Yes, verbatim (line ~111) | Yes, Mahesh Dayani | Actually p.12, not p.6 (see finding D-1, largest drift found) |
| 11 | SBFC Nov-2025 | SUBSTANTIVE | "10 to 15 basis points before they peaked out," cited p.4 | Yes, verbatim (line ~71) | Yes, Aseem Dhru | Confirmed p.4, exact match |
| 12 | SBFC Nov-2025 | SUBSTANTIVE | Cost of borrowing 8.96%, -36bp, cited p.4 | Yes, verbatim (line ~76) | Management | Actually p.5, not p.4 (MINOR drift) |
| 13 | SBFC Nov-2025 | SUBSTANTIVE | Sub-Rs7-lakh "enhanced credit cost," SARFAESI 2x timeline, cited p.9 | Yes, verbatim (line ~91) | Yes, Mahesh Dayani | Actually p.8, not p.9 (MINOR drift) |

**Result: every SUBSTANTIVE citation spot-checked (13 of the report's ~25 total citations, weighted
toward the most load-bearing ones) is a real, verbatim, correctly-attributed quote that exists in the
named peer's named transcript.** No fabricated or invented peer statement was found. This clears the
CRITICAL/fabrication bar entirely.

What is not clean: page-number precision. Of the 13 spot-checked citations, 7 have page drift versus
the transcript's own internal footer numbering — five off by exactly one page (plausibly an
extraction/footer-placement artifact common to OCR'd transcripts, since the footer for a page can be
captured either just before or just after that page's spoken content depending on the extraction tool)
and two with materially larger drift that cannot be explained by that artifact (see findings D-1 and
D-2 below). None of the seven drifts changes the identity of the quote, the speaker, the call, or the
peer — a reader searching the correct transcript by quote text will find every one of them.

---

## 2. Findings

| ID | Severity | Peer / call | Item | Detail |
|---|---|---|---|---|
| D-1 | MINOR | SBFC Nov-2025 | Approval-rate quote (Claim 2, the single most load-bearing quote for the "sector-wide tightening" verdict) | B06 cites p.6; the quote ("approval rates earlier... 45% to 50% odd... probably gone down to below 40% odd," Mahesh Dayani) is actually on p.12 of 14 in the transcript's own footer numbering — a 6-page drift, too large to be an OCR/footer-placement artifact. Content, speaker, and call are all correct; only the page anchor is wrong. |
| D-2 | MINOR | NORTHARC May-2026 | FY27 credit-cost guidance figure (Claim 1) | B06 cites p.4-5 for "consolidated FY26 credit cost of 2.8% guided flat at 2.7-2.8% for FY27." The 2.8% FY26 figure is genuinely on p.5, but the specific 2.7-2.8% FY27 forward guidance (Chintan Shah/Pardhasaradhi Rallabandi exchange) is on p.11-13, not p.4-5. Same pattern as D-1: real quote, wrong page, and here two distinct facts from different pages were compressed into one citation range that only covers the first fact. |
| D-3 | MINOR | SBFC Jul-2025 | "Not about geography... more about ticket sizes" quote (Claim 3, used in the report's single most consequential-contradiction paragraph) | Cited p.4; actually p.7. Content and speaker (Aseem Dhru) confirmed correct. |
| D-4 | MINOR | Multiple (MASFIN Nov-2025 "range bound" quote p.9 vs actual p.8; MASFIN Investor Day SIDBI-CRISIL quote p.16 vs actual p.15; SBFC Nov-2025 cost-of-borrowing p.4 vs actual p.5; SBFC Nov-2025 sub-Rs7-lakh quote p.9 vs actual p.8) | Systematic off-by-one page citation | Content verified correct in every case; page number consistently one off. Pattern is consistent enough (always same direction) to suggest a systematic pagination-counting convention difference rather than random error, but it means a reader checking the stated page alone will not find the quote. |
| D-5 | MINOR | NORTHARC Q2 FY26 (Oct-2025 call), the one CITED-ONLY transcript | Small unused nuance: an analyst (Shweta) asks about a sequential Stage-2 spike; Ashish Mehrotra attributes it to "the unsecured business loan side" (line ~298-301 of the transcript) | B06's CITED-ONLY classification of this call as purely confirmatory (cost-of-funds/NIM trend, demand language "already established elsewhere") is fair on the whole — this call adds no new decisive finding to any of the 7 claims. But this single-quarter Stage-2 unsecured-business-loan deterioration is a small negative data point inside a call B06 otherwise treats as clean-confirmatory; it does not change any verdict (it is a one-quarter blip management itself frames as isolated, not a trend), so it is industry-context-miss grade, not claim-relevant-grade. Rated MINOR per the rubric's own "industry-context miss is MINOR" test rather than MAJOR. |

No CRITICAL or MAJOR finding. No SUBSTANTIVE tag was unsupported. No claim in the injected
`peer_questions` list was skipped. No VERIFIED verdict rests on fewer than two independent peer
anchors (Claim 5, the sole VERIFIED claim, has three: MASFIN, Northern Arc, SBFC, each with its own
anchored cost-of-borrowing series). No verdict was upgraded from peer silence — where B06 records
"peers silent," the corresponding verdict is UNVERIFIABLE or the silence is explicitly carved out of
an otherwise-partial verdict (e.g., Claim 3's Bihar-specific sub-finding), never silently converted to
VERIFIED or CONTRADICTED.

---

## 3. Verdict-discipline audit (per claim)

| Claim | B06 verdict | Peer anchors | Independent (different peer) count | Discipline check |
|---|---|---|---|---|
| 1. Sector-wide credit-cost normalisation | PARTIALLY VERIFIED | NORTHARC, MASFIN, SBFC | 3 | PASS — verdict correctly reflects genuine three-way split (not forced to a clean VERIFIED or CONTRADICTED) |
| 2. Sector-wide tightening + FY27 reversal | PARTIALLY VERIFIED / CONTRADICTED (split) | SBFC, MASFIN | 2 | PASS — correctly separates the tightening direction (partially verified) from reversal timing (contradicted by SBFC) rather than blending into one false verdict |
| 3. Bihar/MFI-ordinance minimal spillover | UNVERIFIABLE (Bihar) / CONTRADICTED (Karnataka analogue) | SBFC, NORTHARC | 2 | PASS — correctly refuses to claim direct Bihar verification (zero Bihar mentions confirmed by my own scan of the transcripts) while still using the closest analogue honestly, labeled as an analogue, not a direct test |
| 4. Collection-efficiency recovery, business-loan-specific | PARTIALLY VERIFIED | NORTHARC, MASFIN, SBFC | 3 | PASS |
| 5. Cost-of-borrowing decline | VERIFIED | MASFIN, NORTHARC, SBFC | 3 | PASS — well above the 2-peer minimum for a full VERIFIED |
| 6. TAM / exclusivity claim | UNVERIFIABLE (TAM) / CONTRADICTED (exclusivity) | SBFC, MASFIN | 2 | PASS |
| 7. Mortgage/micro-LAP credit-cost aspiration | CONTRADICTED (directional) / UNVERIFIABLE (precise number) | SBFC, NORTHARC | 2 | PASS |

All 7 questions in B05's injected `peer_questions` list map one-to-one to B06 Part 1 sections 1-7 and
each received an explicit verdict. `claims_all_addressed: true`.

---

## 4. Independent read: anything peers said that B06 should have used but didn't

Beyond the CITED-ONLY spot-check (finding D-5), I scanned each transcript for Bihar, Karnataka,
approval/rejection-rate, and collection-efficiency keywords independently of B06's own citations to
check for a miss. Nothing surfaced that materially contradicts or corroborates any of the 7 claims
beyond what B06 already used. The zero-Bihar-mentions finding (Claim 3) is independently confirmed —
I found no occurrence of "Bihar" in any of the 11 transcripts either.

---

## 5. Overall assessment

B06 used the peer set substantively and honestly. Every SUBSTANTIVE tag checked traces to a real,
verbatim, correctly-attributed quote; the one CITED-ONLY call is fairly classified; no claim was
skipped; verdict discipline (2+ peer minimum for VERIFIED, no upgrades from silence) held throughout;
and the report's own honesty checks (e.g., "no peer mentions AYE," "zero Bihar mentions") independently
verify as true. The material weakness is page-citation precision: two citations (D-1, D-2) are wrong
by enough pages that a reader checking only the stated page would not find the quote, and five more
are off by exactly one page in a way that looks systematic rather than random. This is a real
citation-hygiene gap worth fixing before the report is relied on for page-level fact-checking, but it
does not change any verdict, does not affect the substantive triangulation, and does not rise to
fabrication — every quote is genuinely there, just not always where the report says it is.

```yaml
stage: B12d
company: "AYE"
run_date: "2026-07-22"
model: claude-sonnet-5
status: complete
peers_audited: 11
substantive_confirmed: 11
substantive_unsupported: []
unused_but_relevant:
  - {peer: "NORTHARC (Q2 FY26, Oct-2025 call)", missed_item: "Sequential Stage-2 spike attributed to unsecured business loan segment (analyst Shweta / Ashish Mehrotra exchange) - a minor single-quarter negative data point inside a call B06 tags CITED-ONLY/confirmatory-only", anchor: "NORTHARC Oct-2025 call, Ashish Mehrotra, transcript line ~298-301 (page anchor not independently pinned down)"}
claims_all_addressed: true
verdict_discipline_fails: []
findings:
  - {severity: "MINOR", location: "B06 Part 1, Claim 2 (SBFC Nov-2025 approval-rate quote)", claimed: "p.6", source_truth: "p.12 of 14 (Mahesh Dayani, '45% to 50% odd... below 40% odd')", note: "Quote/speaker/call all correct, 6-page anchor drift", source_fidelity: false}
  - {severity: "MINOR", location: "B06 Part 1, Claim 1 (NORTHARC May-2026 FY27 credit-cost guidance)", claimed: "p.4-5", source_truth: "p.11-13 for the specific 2.7-2.8% FY27 guidance figure (p.5 correct only for the FY26 2.8% figure)", note: "Two facts from different pages compressed into one citation range", source_fidelity: false}
  - {severity: "MINOR", location: "B06 Part 1, Claim 3 (SBFC Jul-2025 'not about geography' quote)", claimed: "p.4", source_truth: "p.7 (Aseem Dhru)", note: "Quote/speaker/call correct, page wrong", source_fidelity: false}
  - {severity: "MINOR", location: "B06 Part 1/Part 2, multiple citations (MASFIN Nov-2025 p.9, MASFIN Investor Day p.16, SBFC Nov-2025 cost-of-borrowing p.4, SBFC Nov-2025 sub-Rs7-lakh p.9)", claimed: "as cited", source_truth: "each one page earlier than cited (p.8, p.15, p.5, p.8 respectively)", note: "Systematic off-by-one, consistent direction, content verified correct in all cases", source_fidelity: false}
  - {severity: "MINOR", location: "B06 Part 3 (NORTHARC Q2 FY26 Oct-2025, CITED-ONLY classification)", claimed: "purely confirmatory, no new decisive finding", source_truth: "contains one minor unused negative data point (Stage-2 spike, unsecured business loans)", note: "Classification is fair overall; the missed item is industry-context grade, not claim-relevant grade", source_fidelity: false}
critical_count: 0
major_count: 0
minor_count: 5
acceptance_rate: 100
```
