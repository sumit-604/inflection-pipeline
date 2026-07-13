# Verifier D: Peer Coverage Audit — Prizor Viztech Ltd (PRIZOR)
Run date: 2026-07-12 | Fresh-context audit of Stage 6 (06-peers.md) against the 11 peer
transcripts in the text cache. No other pipeline output was consulted.

## Scope note
The task brief for this run supplied 3 peers with usable transcripts (CP Plus, 4 calls;
OSEL Devices, 3 calls; Sahasra, 4 calls = 11 transcripts) plus a 4th nominated peer
(D-Link India) with screener CSVs only, no transcript in the cache. This matches Stage 6's
own scope note exactly. No B05 peer-questions artifact was provided as an input to this
verification run, so "claims_all_addressed" is assessed against the 7 questions Stage 6
itself states it was answering (Part 1, Q1-Q7), not against an external source-of-truth
list. This is a limitation of the audit's evidence base, noted rather than penalized.

---

## PART A: PEER COVERAGE CLASSIFICATION AUDIT

| Peer | Stage 6 classification | Verified against transcripts | Verdict |
|---|---|---|---|
| CP Plus / Aditya Infotech (CPPLUS) | SUBSTANTIVE | Confirmed. Every material figure spot-checked below is a real, locatable quote/number in the 4 transcripts (STQC/BIS delisting language, market share 20.8%→31.4%→39%→45.4%, EBITDA/PAT margin series across all 4 quarters, capex figures, multi-SoC vendor list, Orient Cables MoU, CCC concession). Citation density and accuracy are high. | PASS — genuinely substantive, not decorative |
| OSEL Devices (OSELDEVICE) | SUBSTANTIVE | Core figures confirmed (short-term debt INR48cr→INR98cr, INR41cr in mutual funds, INR60cr working capital, "15% to 20% EBITDA margins" blended-context quote, JNPA/JNPT SEZ land, cash-flow-statement reclassification of short-term borrowings). One citation inside this peer's coverage is misattributed — see Finding below. | PASS with one MAJOR sourcing defect |
| Sahasra Electronic Solutions (SAHASRA) | SUBSTANTIVE | Core figures confirmed (DDR/memory shortage quote correctly attributed to Varun Manwani in the Nov 2025 call; standalone PAT 15.49% vs 9.13% prior year; negative CFO two years running with FY2028 turnaround guidance, confirmed via Paras Chheda Q&A; SMT line count and ATMP capex figures; Ravi Gupta guidance-credibility challenge, content and quote verbatim-accurate). Call-date labeling for the guidance-credibility quote is inconsistent between Stage 6's scope note (labels the file "Jun 2025") and its body text (labels the same call "May 2025 call") — both are technically correct (filing date vs. call date: the transcript itself is dated "2nd June 2025" covering a call "held on 30th May 2025") but the inconsistency is not resolved anywhere in the report. | PASS, minor labeling inconsistency only |
| D-Link India | UNUSED | Confirmed no transcript exists in the `_textcache` directory (only 11 peer transcript files present, none for D-Link); Stage 6's stated reason (no transcript, not lack of relevance) is accurate and appropriately caveated. | PASS — correct classification, correctly reasoned |

**peer_utilisation = peers used substantively ÷ peers provided = 3 ÷ 4 = 75%.**
Stage 6's own YAML states `peers_provided: 4` and lists 3 peers as SUBSTANTIVE + 1 as
UNUSED in `peer_coverage_map` — this is consistent with the 75% figure; Stage 6 does not
compute or state the ratio explicitly but nothing in its counts contradicts it.

---

## PART B: CITATION SPOT-CHECKS (materiality-ordered)

### B1. The central contradiction (Q5): Prizor's claimed 21-23% EBITDA / 14% PAT vs. CP Plus actual margins
This is the single most consequential claim in the report and was checked exhaustively
against all 4 CP Plus transcripts:

| Quarter | Stage 6 claim | Transcript source | Match |
|---|---|---|---|
| Q1 FY26 (Aug 2025 call) | EBITDA 8.7%, PAT 4.4% | "EBITDA margin stood at 8.7%... PAT margin stood at 4.4%" (line 246-249) | EXACT |
| Q2 FY26 (Nov 2025 call) | EBITDA 12.0%, PAT ~7.5% | "seen a 12% EBITDA last quarter, 7.5% PAT already" (line 390) | EXACT |
| Q3 FY26 (Feb 2026 call) | EBITDA 12.6%, adj. PAT 8.43% (INR96cr/INR1,139.1cr) | "revenue grew 37.3%... to INR1,139.1 crores... basis points to 12.6%... Adjusted PAT stood at INR96 crores" (line 127-132); 96/1139.1 = 8.43% | EXACT |
| Q4 FY26 (Jun 2026 call) | EBITDA 18.0%, adj. PAT 11.89% (INR169.1cr/INR1,422cr); FY26 full year EBITDA 13.7%, PAT 8.72% (INR368cr/INR4,220.8cr); "new normal" 14-15% EBITDA / 8.5-9.5% PAT guidance | "margins improving by 800 basis points to 18%... Adjusted PAT stood at INR169.1 crores... revenue grew... to INR4,220.8 crores... margins expanding by 540 basis points to 13.7%... Adjusted PAT rose to INR368 crores" (line 184-193); "14%-15% should be the new normal for this business" (line 548-555); one-off low-cost-inventory benefit "now exhausted" independently confirmed (line 229, 286) | EXACT |

Every number in this claim, including the derived percentages (169.1/1422, 368/4220.8), is
a real and correctly transcribed figure. The contradiction verdict is fully supported by
the transcripts as cited. This is the strongest-anchored section of the entire report.

### B2. STQC/BIS-ER displacement (Q1, Q4)
- "BIS has taken off all the old R-numbers of all the brands that were registered who are
  not STQC qualified... that's a grey market, which might be miniscule" — verbatim match,
  Aug 2025 call, Aditya Khemka, line 489-496.
- Market share trajectory 20.8% (FY25, line 105 Aug 2025 call) → 31.4% (Nov 2025 call, line
  142) → >39% (Feb 2026 call, line 122) → 45.4% (Jun 2026 call, line 91) — all four figures
  confirmed exactly as cited, including the "nearly 36%" pre-IPO projection and ~25% CP
  Plus brand share at IPO (Jun 2026 call, line 82-91).
- "Chinese players completely out... trusted supply chain clause" — confirmed as a
  faithful paraphrase combining the analyst's question and Aditya Khemka's answer (Feb
  2026 call, line 539-542); not a fabricated quote, but stitched from two speakers, which
  should ideally be flagged as a compound citation. MINOR.

### B3. Component costs / capex (Q3, Q6)
- Sahasra's memory-shortage quote ("with the growth in AI and extreme demand from the AI
  segment...") correctly attributed to Varun Manwani, Nov 2025 call, in an unbroken
  speaker block (line 221-242). Confirmed accurate.
- CP Plus multi-SoC vendor list (Realtek, Innofusion, Novatek, Ambarella, Qualcomm,
  Augentix) confirmed split across Feb 2026 (5 of 6 named) and Jun 2026 (all 6 named)
  calls — Stage 6 does not distinguish which quarter first names which vendor, a
  presentational simplification, not an error. MINOR.
- CP Plus INR200cr/2-year capex guidance (Aug 2025 call, line 592) and Orient Cables MoU
  (Feb 2026 call, line 178) both confirmed verbatim.
- Sahasra 28-32% semiconductor EBITDA margin guidance confirmed present but in the Nov
  2024 call (line 595, 659, 781), not dated anywhere in Stage 6's Q5 "Peers silent" cell —
  a missing anchor date for an otherwise accurate figure. MINOR.

### B4. Working capital / short-term debt (Q7) — sourcing defect
Stage 6, Q7 row: *"an investor (Mahesh Attal, May 2025 call) directly challenged this as
'extreme capital allocation,' raising debt while sitting on unutilized cash."*

This is checked and found **misattributed on both axes**:
- The "extreme capital allocation" phrase and the INR48cr→INR98cr / INR41cr / INR60cr
  figures it responds to are **in the same paragraph, same call** — the Nov 2025 OSEL
  transcript (line 175-192) — not a separate "May 2025 call."
- The speaker who says "this is a good extreme capital allocation strategy" is **Vivek
  Patel** (line 175-184), not Mahesh Attal. Mahesh Attal is a real questioner in OSEL's May
  2025 call (confirmed, line 386-527) but his questions there concern short-term loans/
  advances (~INR38.98cr) and the Philips mobile ramp, not the "extreme capital allocation"
  language or the 48→98cr figures.

The underlying substance (OSEL's short-term debt scaling pattern, used correctly for the
PARTIALLY VERIFIED Q7 verdict) is accurate and well-supported elsewhere in the same
paragraph. But the specific citation — wrong speaker, wrong quarter, presented as if it
were a separate corroborating data point from an earlier call — is a genuine sourcing
error, not merely a rounding or labeling quirk. **MAJOR** (rule 2: SUBSTANTIVE peer
coverage requires the citation to be real and findable as stated; this one is real in
substance but wrongly attributed, which would mislead anyone trying to re-verify it at the
stated location).

### B5. Sahasra CFO / FY2028 guidance (Q7, 2E)
"negative for two consecutive years... does not expect operating cash flow to turn
positive until 'the end of FY2028'" — confirmed via Paras Chheda's repeated follow-up
questions in the Jun 2026 call (line 759-808). Accurate.

### B6. OSEL cash-flow reclassification / "NSE compliance query" (2E)
Stage 6: *"OSEL had to restate/reclassify its cash flow statement after an NSE compliance
query on short-term-borrowing classification (Jun 2026 call)."*

The reclassification itself is confirmed (Ravi Mishra: "the reclassification has happened
to correct the erroneous reporting earlier," line 367-370; also raised independently by
analyst Pratiti Khara re: the September cash-flow statement, line 79-86, and by Kailash
Shah re: FY25 regrouping, line 347-355). However, **no transcript passage attributes the
correction's origin to an "NSE compliance query."** The correction is shown as
analyst-driven (multiple analysts independently flagged the same misclassification across
two calls) — a governance-relevant fact in its own right — but the specific causal claim
that NSE (the exchange) raised a compliance query is not supported anywhere in the
transcript text as cited. This reads as either an inference presented as fact or an import
from an outside source not in the audited cache. **MINOR** (the underlying governance
point — repeat cash-flow-statement errors requiring correction — stands on its own
transcript evidence without the NSE framing; the embellishment doesn't change the
substantive conclusion but is unanchored as stated).

---

## PART C: VERDICT-DISCIPLINE AUDIT

| Claim | Stage 6 verdict | Peers cited | Discipline check |
|---|---|---|---|
| Q3 component costs/backward integration | VERIFIED | CP Plus, Sahasra (2 independent) | PASS — 2 peers, correctly VERIFIED |
| Q6 capex cycle | VERIFIED | CP Plus, Sahasra, OSEL (3 independent) | PASS — 3 peers, correctly VERIFIED |
| Q1 STQC displacement | PARTIALLY VERIFIED | CP Plus only | PASS — correctly capped, single-peer basis explicitly stated |
| Q2 market CAGR | PARTIALLY VERIFIED | CP Plus only, magnitude gap flagged | PASS — correctly capped; the global $35.9bn figure is separately and correctly carried to `unverifiable` |
| Q4 STQC-driven share gains | PARTIALLY VERIFIED | CP Plus only | PASS — correctly capped |
| Q7 working-capital pattern | PARTIALLY VERIFIED | OSEL, Sahasra, CP Plus (3 peers) but capped on magnitude, not peer count | PASS — capping rationale (Prizor's ~11.5x increase not comparable to OSEL's ~2x) is a judgment call, correctly reasoned, not a discipline violation |
| Q5 margin claim | CONTRADICTED | CP Plus (single peer, but a contradiction, not a VERIFIED claim — the 2-peer rule applies to VERIFIED upgrades, not to CONTRADICTED findings) | PASS — no discipline issue; a single strong disconfirming peer is sufficient to contradict, and Stage 6 does not claim more than it has |

No VERIFIED claim rests on a single peer. No verdict is upgraded from silence — every
PARTIALLY VERIFIED claim correctly states single-peer status as the reason for the cap.
**Zero verdict-discipline violations found.**

---

## PART D: CLAIM COVERAGE

All 7 questions Stage 6 states it set out to answer (Q1-Q7) received an explicit verdict
in Part 1 and are carried through consistently into Part 4's triangulation summary (2
verified + 4 partially verified + 1 contradicted = 7, reconciles). No skipped claim
identified. (Caveat: this is checked against Stage 6's own stated question list, not an
independently-supplied B05 peer-questions artifact, which was not provided to this
verification run — see Scope note above.)

---

## FINDINGS TABLE

| Severity | Item | Location | Detail |
|---|---|---|---|
| MAJOR | Misattributed citation | Q7 row, "an investor (Mahesh Attal, May 2025 call)" | Quote and figures are real but from Vivek Patel in the Nov 2025 call (same call already correctly cited two sentences earlier for the associated numbers), not Mahesh Attal in a separate May 2025 call. |
| MINOR | Unanchored causal claim | Part 2E, "after an NSE compliance query" | The cash-flow reclassification is transcript-confirmed; the specific NSE-compliance-query origin is not supported by any passage in the audited transcripts. |
| MINOR | Compound/stitched quote presented as continuous | Q1 row, "Chinese players completely out... trusted supply chain clause" | Combines an analyst's question and management's answer without indicating the compound structure; substance is accurate. |
| MINOR | Call-date labeling inconsistency | Scope note vs. body text, Sahasra "Jun 2025"/"May 2025" and CP Plus "Jun 2026"/"May 2026" | Both labels are individually correct (cache filename/filing date vs. actual call date) but used inconsistently across the report without reconciliation; could confuse a reader cross-checking against the file cache. |
| MINOR | Missing quarter anchor | Q5 "Peers silent" cell, Sahasra 28-32% EBITDA guidance | Figure confirmed accurate (Nov 2024 call) but no call date given in the report. |
| MINOR | JNPT vs. JNPA naming | Q6 row, OSEL SEZ land parcel | Transcript uses "JNPA" (current name); report uses "JNPT" (older name for the same entity). Immaterial. |

**Overall:** the report's central and most consequential finding — the Q5 margin
contradiction — is exhaustively and exactly anchored across all four CP Plus quarters,
with every number independently reproducible from the transcripts. Peer classification
(3 SUBSTANTIVE, 1 UNUSED for a documented data-availability reason) is accurate. Verdict
discipline (VERIFIED requires 2+ peers, PARTIALLY VERIFIED capped on single-peer or
magnitude grounds) is applied correctly throughout with zero violations found. The one
MAJOR finding is a real sourcing defect (wrong speaker/quarter for an otherwise accurate
and substantively-used quote) that does not change any verdict or the report's central
contradiction, but should be corrected before the citation is relied on for further
scrutiny. All four peer classifications (3 SUBSTANTIVE, 1 UNUSED) are correct at the
handling level, so acceptance_rate is scored on peer-handling correctness with the MAJOR
citation defect reported separately in findings.

```yaml
stage: B12d
company: "PRIZOR"
run_date: "2026-07-12"
model: claude-sonnet-5
status: complete
peers_audited: 4
substantive_confirmed: 3
substantive_unsupported: []
unused_but_relevant: []
claims_all_addressed: true
verdict_discipline_fails: []
findings:
  - {severity: "MAJOR", location: "06-peers.md Part 1, Q7 row", claimed: "an investor (Mahesh Attal, May 2025 call) directly challenged this as 'extreme capital allocation'", source_truth: "Quote is from Vivek Patel in the OSEL Nov 2025 call (line 175-184), the same call already cited for the associated INR48cr/98cr/41cr/60cr figures; Mahesh Attal's real questions in the May 2025 call concern unrelated short-term loans/advances (~INR38.98cr)", note: "Wrong speaker and wrong quarter for an otherwise real, substantively-used quote; does not change the Q7 verdict but is a genuine sourcing defect"}
  - {severity: "MINOR", location: "06-peers.md Part 2E", claimed: "OSEL had to restate/reclassify its cash flow statement after an NSE compliance query on short-term-borrowing classification", source_truth: "OSEL Jun 2026 transcript confirms the reclassification (Ravi Mishra, line 367-370) and shows it was raised independently by analysts Pratiti Khara and Kailash Shah; no passage attributes the origin to an NSE compliance query", note: "Underlying governance point stands on transcript evidence alone; the NSE-query framing is unanchored as stated"}
  - {severity: "MINOR", location: "06-peers.md Part 1, Q1 row", claimed: "'Chinese players completely out... post April 1st 2026... trusted supply chain clause' (Q&A)", source_truth: "Compound of Prateek Chaudhary's question ('Chinese players are completely out, right?... post April 1st, 2026?') and Aditya Khemka's answer ('trusted supply chain clause... they don't qualify')", note: "Faithful in substance; presented as a single continuous quote without flagging the two-speaker composition"}
  - {severity: "MINOR", location: "06-peers.md scope note vs. Q7/2E body text", claimed: "Sahasra call labeled 'Jun 2025' in scope note, 'May 2025 call' in body text; CP Plus call labeled 'Jun 2026' in cache/scope references, 'May 2026 call' in body text", source_truth: "Both labels are individually correct: cache filenames follow the SEBI filing date (2nd Jun 2025 / 3rd Jun 2026), body-text labels follow the actual call date (30th May 2025 / 28th May 2026)", note: "Internally reconcilable but never reconciled in the report; could confuse a reader cross-referencing the file cache"}
  - {severity: "MINOR", location: "06-peers.md Part 1, Q5 'Peers silent' cell", claimed: "Sahasra EBITDA guidance 28-32% at points", source_truth: "Confirmed present in the Nov 2024 call (line 595, 659, 781); no call date given", note: "Figure accurate; missing granular anchor"}
  - {severity: "MINOR", location: "06-peers.md Part 1, Q6 row", claimed: "OSEL... JNPT SEZ land parcel", source_truth: "OSEL Jun 2026 transcript uses 'JNPA' (current name of the port authority), not 'JNPT'", note: "Same entity, older/newer name variant; immaterial"}
critical_count: 0
major_count: 1
minor_count: 5
acceptance_rate: 100
```
