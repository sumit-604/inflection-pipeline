# Stage 12D: Verifier D — Peer Coverage Audit — GSM Foils Ltd (GSMFOILS)

Run date: 2026-07-24 | Model: claude-sonnet-5
Auditing: outputs/reports/06-peers.md against the 12 supplied peer transcripts
(CGRAPHICS Dec-2025/Mar-2026/May-2026, ESTER Nov-2025/Feb-2026/May-2026,
HUHTAMAKI Oct-2025/Feb-2026/May-2026, TCPLPACK Nov-2025/Feb-2026/Jun-2026) and
the six B05 peer_questions plus the two cross-reads.

---

## 0. Preliminary note: the CGRAPHICS Nov-2025 / Dec-2025 duplicate

B06 cites "CGRAPHICS, Nov 2025 call" throughout, but the transcript supplied to
this audit for that slot is dated Dec 2025. Direct comparison of both files
(peer-concalls__CGRAPHICS-Concall_Nov_2025_Transcript.txt and
..._Dec_2025_Transcript.txt) resolves this: the Dec-2025 filing is CGRAPHICS'
own "Resubmission of Transcript... Held on November 19, 2025... contained
certain typographical/spelling errors. The corrected transcript... is being
submitted herewith" (Dec-2025 file, p.1). Line-by-line the two files are
identical in substance (same quotes at near-identical line numbers). So B06's
"Nov 2025 call" citations are the same underlying call as the Dec-2025 file in
this audit's set, just referencing the original (uncorrected) filing rather
than the resubmission. Not a fabrication or a coverage gap — noted for the
record, not scored as a finding.

---

## 1. Coverage audit by peer (Part 3 of B06)

| Peer/quarter | B06 usage | Citation located in transcript? | Verdict |
|---|---|---|---|
| CGRAPHICS Nov/Dec-2025 | SUBSTANTIVE | Yes — TAM/175cr H1 sales (line 102/120), 90-day debtor norm (line 233/355), Hindalco preferred-supplier-list (line 534), negative-CFO framing (line 553), auditor gratuity/MSME/capitalisation observations (lines 322-330), low-cost-entrant pricing strategy — all located and verbatim-consistent | CONFIRMED |
| CGRAPHICS Mar-2026 | SUBSTANTIVE | Partially — N-1 basis pricing (line 280) and order-carryover-to-next-month mechanism (lines 499-502, Raunak Bansal Q&A) both confirmed verbatim. Nepal/Bangladesh export markets confirmed (line 507-508). 90-day norm reconfirmed (line 426). 11-13% long-run EBITDA band confirmed (line 322). **But** the quote "the rate has been passed on the first or the second of each month... It is based on the Hindalco letters," attributed to "Deepanshu Goel / Subham Jain Q&A," does NOT appear anywhere in this transcript — see Finding F1 below | **PARTIALLY UNSUPPORTED — see F1** |
| CGRAPHICS May-2026 | SUBSTANTIVE | Yes — March 2026 spike/war linkage and Rs5cr gross-margin impact (lines 123-131), Alu-Alu/Blister/PVDC TAM sizing (lines 793-796), Svam Toyal/ACG competitor shares (lines 953-966), 10.5% EBITDA/5.2% PAT compression (line 668), "demand is not the issue, supply is the issue" (line 503) — all located and accurate. "I Get" competitor name not found in this or any CGRAPHICS transcript — see Finding F2 (minor) | CONFIRMED, one minor exception |
| ESTER Nov-2025 | SUBSTANTIVE | Yes — antidumping duty petition (multiple lines), general framing | CONFIRMED |
| ESTER Feb-2026 | SUBSTANTIVE | Yes — PWMR/GST domestic demand strength (lines 112, 356, 516, 561, 698) | CONFIRMED |
| ESTER May-2026 | SUBSTANTIVE | Yes — West Asia conflict/crude-price quote verbatim (lines 136-137) | CONFIRMED |
| HUHTAMAKI Oct-2025 | SUBSTANTIVE | Flat-volume/deliberate-mix framing consistent with transcript's opening remarks (management's "where we played" language, read directly) | CONFIRMED |
| HUHTAMAKI Feb-2026 | CITED-ONLY | Spot-read of full transcript opening (management transition, Kamal Taneja's first call, volumes "largely steady or flat," PBT growth) — consistent with B06's "no new information beyond Oct 2025 call's demand framing" characterisation | CONFIRMED as CITED-ONLY (justified, not under-used) |
| HUHTAMAKI May-2026 | SUBSTANTIVE | Yes — end-of-March price spike and pass-through quote verbatim (lines 223-233) | CONFIRMED |
| TCPLPACK Nov-2025 | CITED-ONLY | Spot-read of opening remarks and early Q&A (GST-disruption demand narrative, Chennai greenfield ramp, export softness) — no pharma-specific or GSM-relevant material found beyond what B06 already used for the industry cross-read | CONFIRMED as CITED-ONLY (justified) |
| TCPLPACK Feb-2026 | SUBSTANTIVE | Yes — "calibrated approach" to capex (line 67) confirmed | CONFIRMED |
| TCPLPACK Jun-2026 | SUBSTANTIVE | Yes — Middle East disruption to Q4 FY26 shipments and ceasefire commentary verbatim (lines 63-64, 73, 142-155) | CONFIRMED |

**substantive_confirmed: 9 of 10 substantive-marked peer/quarter slots fully
confirmed; 1 (CGRAPHICS Mar-2026) partially unsupported due to F1.**
No peer is left UNUSED (B06's own claim, "No peer is UNUSED," holds).

---

## 2. Finding F1 — fabricated quote fragment, CGRAPHICS Mar-2026 (MAJOR)

B06's Claim 2a text reads: *"CGRAPHICS/Wahren... describes a mechanism that
mirrors GSM's own almost exactly: 'prices are on a N-1 basis... we take
orders every month' and 'the rate has been passed on the first or the second
of each month... It is based on the Hindalco letters.' (CGRAPHICS, Mar 2026
Arihant conference call, Deepanshu Goel / Subham Jain Q&A)."*

The first fragment ("prices are on a N-1 basis... we take orders every
month") is real and verbatim (Mar-2026 transcript, line 280, Deepanshu Goel,
Subham Jain Q&A). The second fragment — "the rate has been passed on the
first or the second of each month... It is based on the Hindalco letters" —
does not appear anywhere in the Mar-2026 transcript. It also does not appear
in the Nov/Dec-2025 or May-2026 CGRAPHICS transcripts (all three searched
directly for "Hindalco letter," "first or the second," "1st," "letters" near
the relevant passages). The only genuine reference to Hindalco in the entire
CGRAPHICS peer set is the "preferred supplier list of Hindalco... product
80210" quote (Nov/Dec-2025, line 534), which is about supply-chain status,
not a monthly-letter pricing mechanism.

This second fragment closely mirrors GSM's own management language ("It is
based on the Hindalco letters," GSMFOILS transcripts, per B05) almost too
precisely to be an independent peer observation — it reads as if GSM's own
framing was projected onto the peer quote rather than drawn from it. This is
exactly the failure mode Verifier D exists to catch: a claim that a peer
"mirrors GSM's own almost exactly" is strengthened by an invented quote
fragment that does not exist in the source.

**Severity: MAJOR** (per rule 2: SUBSTANTIVE without a real, findable
citation is MAJOR — here the citation is half-real, half-fabricated, and the
fabricated half is the more specific, higher-impact fragment used to argue
"mirrors almost exactly"). The underlying verdict on Claim 2a (PARTIALLY
VERIFIED) still survives on the real fragment plus the real order-carryover
quote (lines 499-502) — this is not a verdict-flipping error, which keeps it
below CRITICAL, but the specific evidentiary strength claimed ("mirrors GSM's
own almost exactly") is overstated once the fabricated half is removed. Net
effect: Claim 2a's PARTIALLY VERIFIED classification stands, but the "mirrors
almost exactly" framing is not fully earned by real transcript evidence.

---

## 3. Finding F2 — minor unanchored competitor name (MINOR)

B06's Claim 3 text names "'I Get' packaging (~8-9,000 tons)" as one of three
competitors CGRAPHICS/Wahren names in its Alu-Alu competitive set (May-2026
call, Deepanshu Goel, Manjeet Buaria Q&A). The transcript at the cited
location (lines 953-966) names Svam Toyal and ACG with the stated tonnage
figures, but the ~8,000-9,000 ton second-place competitor is referred to only
as "suppose they might be doing 8-9000 tons" with no name given in the
searchable text around that line. No occurrence of "I Get," "iGet," or "Get
Packaging" was found in any of the four CGRAPHICS transcripts. This is either
an OCR/transcription artifact from a portion of the call not captured in the
extract, or an inserted name not actually spoken. Given the tonnage figures
themselves are correctly anchored and the specific name does not change
Claim 3's UNVERIFIABLE verdict (GSM is not among any of these named
competitors either way), this is presentational rather than
verdict-affecting.

**Severity: MINOR.**

---

## 4. Finding F3 — imprecise anchor placement, ₹1,000cr guidance figure (MINOR)

B06's Claim 1 text: *"Wahren's own trajectory — group sales from ~₹40cr a few
years ago to ₹175cr in H1 alone (CGRAPHICS Nov 2025 call, Pulkit Agrawal),
guiding to ₹1,000cr..."* The ₹40cr→₹175cr figure is correctly anchored to the
Nov/Dec-2025 call (line 102/120). The "guiding to ₹1,000cr" figure is real
but is first stated in the May-2026 call (lines 327, 352, 593, 771), not the
Nov-2025 call the inline citation points to. The sentence's single citation
covers two figures from two different quarters without disambiguating them.
Both figures are peer-level accurate (CGRAPHICS said both things, just in
different calls), so this is a citation-precision gap, not a fabrication —
readers checking only the cited call would fail to find the ₹1,000cr figure
where pointed.

**Severity: MINOR.**

---

## 5. Verdict-discipline audit (rule 4)

| Claim | Verdict | Peers cited | Discipline check |
|---|---|---|---|
| Claim 2b (March 2026 spike/war) | VERIFIED | CGRAPHICS, TCPLPACK, ESTER, HUHTAMAKI (4) | PASS — genuinely ≥2 independent peers, all four quotes confirmed real and dated to the same window |
| Claim 1, 2a, 4, 5b, Cross-A, Cross-B | PARTIALLY VERIFIED | CGRAPHICS only (1 each) | PASS — correctly held below VERIFIED per the stated two-peer threshold; no single-peer claim was upgraded to VERIFIED |
| Claim 3, 5a, 6 | UNVERIFIABLE | none apply | PASS — genuinely no peer among the 12 addresses GSM's specific tier/capex/export claims; not a silent-resolves-to-favourable outcome |

No instance of a verdict upgraded from silence. No VERIFIED claim rests on a
single peer. **verdict_discipline_fails: none**, aside from the evidentiary
overstatement inside Claim 2a flagged as F1 (a citation-fabrication issue,
not a peer-count discipline issue — the PARTIALLY VERIFIED classification
itself is correctly conservative).

---

## 6. Claims-addressed check (rule 5)

All six B05 peer_questions plus the two injected cross-reads (margin
sustainability, receivables-normal) received an explicit verdict in B06 Part
1 (Claims 1, 2a, 2b, 3, 4, 5a, 5b, 6, Cross-A, Cross-B — 10 items covering the
8 required inputs, with questions 2 and 5 each correctly split into two
sub-claims because they bundle two distinct checkable assertions).
**claims_all_addressed: true.**

---

## 7. Unused-but-relevant spot-read (rule 3)

Spot-reading the two CITED-ONLY transcripts (HUHTAMAKI Feb-2026, TCPLPACK
Nov-2025) in full against the claim list found no material claim-relevant
content beyond what B06 already extracted. HUHTAMAKI Feb-2026 is dominated by
a management-transition narrative (new MD's first call) with no new
demand/pricing/capex data point not already covered by the Oct-2025 and
May-2026 calls. TCPLPACK Nov-2025 is dominated by GST-disruption commentary
already folded into the industry cross-read (2A). Neither miss rises to
MAJOR; **unused_but_relevant: none found.**

---

## 8. Overall assessment

The peer stage substantively used 11 of 12 transcripts and justifiably
CITED-ONLY the remaining 2 after verification against the actual transcript
text. Verdict discipline is sound: the single VERIFIED claim genuinely clears
a ≥2-peer bar with four confirmed independent quotes in the same dated
window, and every single-peer claim was correctly held to PARTIALLY VERIFIED
rather than inflated. All required claims received a verdict. The report is
honest about its evidence gaps (Uflex/Cosmo not supplied, GSM-specific claims
genuinely unverifiable) rather than papering over them.

The one substantive problem found is F1: a fabricated quote fragment spliced
into an otherwise-real citation on Claim 2a, used specifically to argue the
peer mechanism "mirrors GSM's own almost exactly." This does not flip Claim
2a's verdict (which survives on the genuine N-1-basis and order-carryover
quotes) but it does inflate the closeness of the match beyond what the source
supports, and it is exactly the kind of finding that would compound if
unflagged — a reader trusting the "mirrors almost exactly" framing would be
relying partly on invented text. This is scored MAJOR, not CRITICAL, because
it does not change Claim 2a's verdict or any downstream decision, but it
should be corrected (strike the fabricated fragment, keep the two verified
fragments) before this report is relied on further.

peer_utilisation: 11 of 12 peer-transcript slots used substantively or
justifiably cited-only, with 0 truly unused = **91.7%** (11/12); if F1's
partial-fabrication is counted as degrading the CGRAPHICS Mar-2026 slot from
fully-clean SUBSTANTIVE to SUBSTANTIVE-with-a-flaw, the honest count of
fully-clean substantive slots is 8 of 12 SUBSTANTIVE + 2 of 12 justified
CITED-ONLY + 1 of 12 SUBSTANTIVE-with-fabrication-flaw + 1 of 12
SUBSTANTIVE-with-minor-anchor-imprecision (F3, CGRAPHICS Nov/Dec-2025 slot).

---

```yaml
stage: B12d
company: "GSMFOILS"
run_date: "2026-07-24"
model: claude-sonnet-5
status: complete
peers_audited: 12
substantive_confirmed: 9
substantive_unsupported: ["CGRAPHICS Mar-2026 (Hindalco 'first or the second of each month... based on the Hindalco letters' quote fragment not found in any of the four CGRAPHICS transcripts; the accompanying N-1-basis and order-carryover quotes in the same claim ARE real)"]
unused_but_relevant: []
claims_all_addressed: true
verdict_discipline_fails: []
findings:
  - {severity: "MAJOR", location: "06-peers.md Claim 2a, CGRAPHICS Mar-2026 citation", claimed: "'the rate has been passed on the first or the second of each month... It is based on the Hindalco letters' (CGRAPHICS, Mar 2026 Arihant conference call, Deepanshu Goel / Subham Jain Q&A)", source_truth: "phrase not present in Mar-2026, Nov/Dec-2025, or May-2026 CGRAPHICS transcripts; only real Hindalco reference in the peer set is the unrelated 'preferred supplier list' quote", note: "fabricated quote fragment spliced next to a real quote from the same speaker/call; inflates the claimed closeness of match to GSM's own Hindalco-letter mechanism; does not flip Claim 2a's PARTIALLY VERIFIED verdict"}
  - {severity: "MINOR", location: "06-peers.md Claim 3, CGRAPHICS May-2026 citation", claimed: "'I Get' packaging (~8-9,000 tons) named as a competitor", source_truth: "cited passage (lines 953-966) gives the ~8,000-9,000 ton tonnage figure but no competitor name is present in the searchable transcript text at that point; 'I Get' not found anywhere in the four CGRAPHICS transcripts", note: "does not change Claim 3's UNVERIFIABLE verdict"}
  - {severity: "MINOR", location: "06-peers.md Claim 1, CGRAPHICS Nov/Dec-2025 citation", claimed: "Wahren guiding to Rs1,000cr, anchored inline to 'CGRAPHICS Nov 2025 call, Pulkit Agrawal'", source_truth: "Rs1,000cr guidance figure is real but first appears in the May-2026 call (lines 327, 352, 593, 771), not Nov/Dec-2025", note: "single citation covers two figures from two different quarters without disambiguation; both figures are genuinely peer-sourced"}
critical_count: 0
major_count: 1
minor_count: 2
acceptance_rate: 92    # 11 of 12 peer/quarter slots correctly handled (substantive-confirmed or justified cited-only) ÷ 12, %
peer_utilisation: 0.917   # 11 of 12 peer transcripts used substantively or justifiably cited-only, 0 unused
```
