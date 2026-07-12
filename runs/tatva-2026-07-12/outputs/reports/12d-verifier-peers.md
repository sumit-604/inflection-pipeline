# VERIFIER D: PEER COVERAGE — TATVA (2026-07-12)
Fresh-context audit of B06 (Stage 6, Peer Concall Verification) against the 15 raw peer
transcripts and B05's peer_questions claim list. Model: claude-sonnet-5.

## 0. Claim-list completeness check (B05.peer_questions vs B06 Part 1)

B05.peer_questions carries 7 items. B06 Part 1 carries 7 numbered claims in the same order,
each with a verdict (CONTRADICTED / PARTIALLY VERIFIED / UNVERIFIABLE), matching B05's
designated check_peers list for each. Verified 1:1 by text comparison of the "Claim (verbatim)"
lines in B06 against B05's `question` field.

| # | B05 question (short) | check_peers (B05) | B06 verdict | Addressed? |
|---|---|---|---|---|
| 1 | Destocking-to-restocking recovery narrative | ACUTAAS, CAMLINFINE, CLEAN, NEOGEN | CONTRADICTED | Yes |
| 2 | ~30-40% RM cost spike, amines/ammonia, Iran conflict | CAMLINFINE, CLEAN | PARTIALLY VERIFIED | Yes |
| 3 | Euro 7 / SDA tailwind, market-share vs Sarchem | ACUTAAS, CLEAN | UNVERIFIABLE | Yes |
| 4 | "Sole India supplier" hybrid-battery electrolytes, +1,378% YoY | NEOGEN | CONTRADICTED (exclusivity); UNVERIFIABLE (magnitude) | Yes |
| 5 | Jolva greenfield slippage vs industry EPC pattern | CLEAN, ACUTAAS | PARTIALLY VERIFIED | Yes |
| 6 | Semiconductor 8-9yr qualification cycle, INR2,000cr range | ACUTAAS, CLEAN | PARTIALLY VERIFIED | Yes |
| 7 | SRF crop-protection caution vs peer agro order books | CAMLINFINE, ACUTAAS | UNVERIFIABLE | Yes |

Note: for Claim 2, B05 designated only CAMLINFINE and CLEAN as check_peers, but B06's Part 1
evidence section for Claim 2 also cites NEOGEN as a second independent corroborating peer (not
on the original designated list). This is additive, not a scope violation — NEOGEN's RM-cost
commentary is genuinely on-topic and strengthens rather than dilutes the triangulation. Not
flagged as an issue.

**claims_all_addressed: true.** No skipped claim.

## 1. Coverage audit table — SUBSTANTIVE peer citations (B06 Part 3 coverage map)

All 15 of 15 peer-quarter transcripts are marked SUBSTANTIVE in B06 (none UNUSED, none
CITED-ONLY). Per rubric rule 2, each SUBSTANTIVE entry's citation was checked against the
underlying transcript. Spot-check method: grepped the exact or near-exact quoted language from
B06 Parts 1-2 against the specific transcript file cited, confirmed speaker attribution and
surrounding context.

| Peer | Quarter | B06 usage | Citation checked | Found in cited transcript? | Verdict |
|---|---|---|---|---|---|
| ACUTAAS | Q1 FY26 (Aug 2025) | SUBSTANTIVE | Abhishek Patel: BFC semiconductor demand "soft" from end customer | YES, verbatim, correct speaker/quarter (line ~453) | Confirmed |
| ACUTAAS | Q2 FY26 (Oct 2025) | SUBSTANTIVE | "groundbreaking ceremony took place last month...capex activities are now underway" | YES, verbatim (line ~157) | Confirmed |
| ACUTAAS | Q3 FY26 (Feb 2026) | SUBSTANTIVE | Guidance raised 25%->30% "based on the strength of our current order book"; "not disclosing anywhere for future businesses"; capex "started almost 4 months back...by end of this calendar" | YES, all three verbatim/near-verbatim, correct quarter | Confirmed. One imprecision: B06 attributes the INR42.1cr figure to "Baba Fine Chemicals" specifically ("Baba Fine Chemicals (BFC...) generating INR42.1 crore in the Q3 FY26 segment"); the transcript actually reports INR42.1cr as the **Specialty Chemicals segment** total, of which BFC's "commodity chemical sub-segment" is a described contributor via "recovery," not the segment's sole constituent. Segment-vs-subsegment conflation. **MINOR.** |
| CAMLINFINE | Q1 FY26 (Aug 2025) | SUBSTANTIVE | "sluggish demand," channel stocks clear "in the next few months" | YES, verbatim, correct quarter | Confirmed |
| CAMLINFINE | Q2 FY26 (Nov 2025) | SUBSTANTIVE | Clearance pushed to Q4; "are we seeing a delay on that? Yes, I think so" | YES, verbatim (analyst asks the delay question, management confirms "by Q4... in the US and Q1 in Europe") | Confirmed |
| CAMLINFINE | Q3 FY26 (Feb 2026) | SUBSTANTIVE | Channel stocks "being liquidated" | YES, verbatim, correct quarter | Confirmed |
| CAMLINFINE | Q4 FY26 (May 2026) | SUBSTANTIVE | Phenol INR85->INR150+/kg (Santosh Parab); caustic "literally doubled up...after the war situation"; ~20% quarterly sales impacted by shipment delays; cash-burn reduction | YES, all verbatim, correct speaker/quarter | Confirmed |
| CLEAN | Q1 FY26 (Jul 2025) | SUBSTANTIVE | "numbness or a slower in demand" (Siddharth Sikchi) | YES, verbatim, correct quarter | Confirmed |
| CLEAN | Q2 FY26 (Nov 2025) | SUBSTANTIVE | "Not Q3 for sure"; phenol price rise from US restrictions | YES, both verbatim, correct quarter | Confirmed |
| CLEAN | Q3 FY26 (Feb 2026) | SUBSTANTIVE | "3, 4 quarters out" recovery framing; agchem "postponed, not lost"; "oil prices...at low point"/"raw material play is not playing out"; **China hydroquinone competitive-pricing pressure** | First three: YES, verbatim, correct quarter. Fourth: **NOT FOUND in this transcript.** See finding below. | **MAJOR — see Finding D-1** |
| CLEAN | Q4 FY26 (May 2026) | SUBSTANTIVE | Performance Chemical 2 delay quote (60-day + 15-day, "quarter delay"); "less than a quarter delay...at the project costs anticipated"; "challenging global environment and geopolitical uncertainties" | YES, verbatim (minor: B06's second quote drops "beyond -- I mean," a disfluency, immaterial); correct quarter | Confirmed. Note: the "calibrate our prices...keep our market share within China as a market" quote (Sanjesh Jain / Siddharth Sikchi exchange) actually belongs to **this** call (May 2026), not Q3 FY26 as B06 cites it in Part 2B/2E — see Finding D-1. |
| NEOGEN | Q1 FY26 (Aug 2025) | SUBSTANTIVE | Baseline Ionics revenue INR5.4cr Q1 FY26 vs INR11.95cr prior FY | YES, verbatim, correct quarter | Confirmed |
| NEOGEN | Q2 FY26 (Nov 2025) | SUBSTANTIVE | Morita/NML JV announcement; "despite global economic headwinds, our commitment to volume growth" | YES, both verbatim, correct quarter | Confirmed |
| NEOGEN | Q3 FY26 (Feb 2026) | SUBSTANTIVE | "a period of steady recovery," "demand resilience in Pharma, Flavors and Fragrances"; "India electrolyte demand is still developing"; customer "had enough inventory so we had to skip" | YES, all verbatim, correct quarter | Confirmed |
| NEOGEN | Q4 FY26 (May 2026) | SUBSTANTIVE | "persistent overcapacity, pricing volatility, and subdued demand"; bromine "pause in the war"/Dead Sea Bromine; Pakhajan H1/H2 FY27 targets; "India's first non-FEOC compliant" (Morita); Ionics INR13cr Q4 / INR36cr FY26; INR161cr preferential allotment; INR1,330cr total debt / INR1,295cr net debt | YES, all verbatim, correct quarter | Confirmed |

**substantive_confirmed: 15 of 15** peer-quarter entries carry at least one genuine, correctly
located citation supporting their SUBSTANTIVE designation — the coverage map's headline claim
("all 15 SUBSTANTIVE, none padding") holds. One entry (CLEAN Q3 FY26) carries one additional
item whose citation is misattributed to the wrong call date; the entry's SUBSTANTIVE status is
still earned by its other three correctly-cited items.

**substantive_unsupported: none** (no peer-quarter's SUBSTANTIVE label rests on a citation that
cannot be found anywhere in the 15-file set — see Finding D-1 nuance: the content itself is real
and findable, just at the wrong transcript).

### Finding D-1 (MAJOR): China hydroquinone pricing quote misdated by one full quarter, repeated 4x

B06 quotes: *"forcing CLEAN to 'calibrate our prices... to keep our market share within China as
a market' (CLEAN Feb 2026 call)"* — cited as Q3 FY26 in Part 2B, again in Part 2E, again in the
peer coverage map row for CLEAN Q3 FY26, and again in the YAML `risks_peers_raise` block.

Grepped "calibrate" across all 15 transcripts: the phrase exists in exactly one file —
`CLEAN-Concall_May_2026_Transcript.txt` (Q4 FY26), not `CLEAN-Concall_Feb_2026_Transcript.txt`
(Q3 FY26). Full quote, correctly transcribed: *"So in view of this, we have to calibrate our
prices in a manner that we are able to balance all the positions and still keep our market share
within China as a market"* (Siddharth Sikchi, in response to Sanjesh Jain, CLEAN May 2026 call,
in a discussion of hydroquinone prices rising post-"West Asia" conflict).

The CLEAN Feb 2026 (Q3 FY26) transcript does contain adjacent, related material — Siddharth
Sikchi there says the company has "no choice but to lower our prices of MEHQ to compete with
these emerging players of hydroquinone-derived MEHQ in China" — but this is a different quote,
in a different quarter, about a different (declining, not conflict-driven) pricing dynamic. B06
either conflated the two calls or mis-transcribed the call date when copying the quote forward.

This is not a fabrication — the underlying claim (Chinese hydroquinone competitive pricing
capping Indian realizations) is real and independently supported by transcript evidence — but
the anchor as printed (call, and by extension the quarter placed in the coverage map row) is
wrong, and the error is systematic (appears identically in 4 separate locations in the report,
suggesting the quote was cut once and pasted forward without re-verifying its source call).
Anyone tracing this specific citation back to "CLEAN Q3 FY26 / Feb 2026" as instructed by the
report would not find it there. **Severity: MAJOR** (per rubric rule 2: citation for a claimed
SUBSTANTIVE contribution does not exist at the stated location; content is recoverable elsewhere
in the dataset, which keeps this short of fabrication, but the specific anchor as printed is
false in 4 places).

## 2. UNUSED / CITED-ONLY peer spot-read (rubric rule 3)

B06 reports zero peers as UNUSED or CITED-ONLY — all 15 are SUBSTANTIVE. This audit independently
spot-read for claim-relevant material the pipeline might have left on the table regardless of its
own labeling:

- Grepped "Euro 7"/"Euro7"/"SDA"/"Sarchem"/"catalytic converter"/word-bounded "urea"/"SCR" across
  all 15 transcripts (case-insensitive, word-bounded to avoid false positives from substrings like
  "measure," "treasury," "obscure"): **zero genuine matches**. Confirms B06's Claim 3 UNVERIFIABLE
  call is accurate — this is not an omission, the peer set genuinely contains nothing on this
  topic.
- Grepped "crop protection"/"agrochemical"/"agro-chem"/"pesticide"/"SRF" across CAMLINFINE and
  ACUTAAS (Claim 7's designated peers): **zero matches**. Confirms Claim 7 UNVERIFIABLE is
  accurate for the designated peer pair.
- Read NEOGEN's own capex-delay commentary (Pakhajan/Dahej "slight delay," approval timeline
  push-outs, Feb 2026 and May 2026 calls) — this is thematically adjacent to Claim 5 (industry-wide
  greenfield slippage) but NEOGEN was not on B05's designated check_peers list for that claim
  (only CLEAN, ACUTAAS were designated). This is a B05 scoping choice, not a B06 coverage gap, and
  NEOGEN's capex program is already discussed in Part 2C's cross-read in a different (leverage/
  capacity-race) framing. Not flagged as MAJOR; noting as a MINOR observation only — a slightly
  broader read of Claim 5 could have cited NEOGEN's own commissioning delays as a third data point
  for "industry-wide EPC slippage is real," which would have strengthened rather than changed the
  PARTIALLY VERIFIED verdict.

**unused_but_relevant:** one MINOR item (NEOGEN capex-delay commentary, off-list for Claim 5 but
thematically relevant); no MAJOR omissions found.

## 3. Verdict-discipline audit (rubric rule 4)

| Claim | B06 verdict | Peers backing it | >=2 independent anchors? | Discipline check |
|---|---|---|---|---|
| 1. Destocking-to-restocking | CONTRADICTED | CLEAN, NEOGEN (both explicit, repeated) | Yes | Clean — not a VERIFIED claim, but well past the 2-anchor bar anyway |
| 2. RM cost spike | PARTIALLY VERIFIED | CAMLINFINE, NEOGEN | Yes | Clean; correctly downgraded from full VERIFIED because chemistry category (amine/ammonia) doesn't match either peer's actual inputs — appropriate hedge, not an overclaim |
| 3. Euro7/SDA tailwind | UNVERIFIABLE | none (confirmed by this audit's independent grep) | N/A | Correct — verdict matches genuine silence, not "upgraded from silence" |
| 4. Sole India supplier / +1,378% | CONTRADICTED (exclusivity) / UNVERIFIABLE (magnitude) | NEOGEN only | No — single peer | Rubric rule 4 as written governs VERIFIED claims specifically; this is CONTRADICTED, not VERIFIED, so it is not a literal rule violation. Flagged for completeness: a CONTRADICTED verdict resting on one peer is thinner evidence than a 2-peer CONTRADICTED, but B06's own prose appropriately hedges ("read literally and narrowly... technically unverifiable... read as intended... direct evidence to the contrary... should be treated as unverified-to-contradicted rather than accepted at face value") — the report does not overstate confidence here. No severity assigned; the sole peer's evidence is itself sound (checked above). |
| 5. Jolva slippage | PARTIALLY VERIFIED | CLEAN, ACUTAAS | Yes (one confirms a milder version of the pattern, one shows a comparable initiative with zero slippage — genuinely mixed, correctly reported as "partial") | Clean |
| 6. Semiconductor 8-9yr / INR2,000cr | PARTIALLY VERIFIED | ACUTAAS only (CLEAN silent, correctly noted) | No — single peer, but verdict is PARTIALLY VERIFIED not VERIFIED, and B06 explicitly notes the single-peer limitation and non-comparability caveat | Clean — no overclaim |
| 7. SRF crop-protection caution | UNVERIFIABLE | none (confirmed) | N/A | Correct — genuine silence, not upgraded |

**No claim in this report is marked (fully) VERIFIED.** `verified: []` in B06's YAML is accurate
— zero claims reached the "VERIFIED, full standard" bar, so rubric rule 4's core trigger (a
VERIFIED claim rests on one peer) never fires. No CRITICAL "verdict upgraded from silence" found:
both UNVERIFIABLE calls (Claims 3, 7) are genuinely unaddressed by any peer, confirmed by
independent grep, not silently resolved to a directional verdict.

**verdict_discipline_fails: none rise to MAJOR or CRITICAL.** (Minor observational note only, on
Claim 4's single-peer basis, already self-hedged in the report text.)

## 4. Other checks

- **Quarter-mapping table (B06 header):** spot-checked 4 of 15 filename-to-quarter mappings
  against transcript content (dates/quarter labels appearing in the transcripts themselves) —
  ACUTAAS Feb 2026 transcript is dated "January 28, 2026" internally (matches "Q3 FY26" call-date
  row showing 28-Jan-2026); CLEAN Feb 2026 transcript dated "January 31, 2026" (matches). No
  mismatches found in the sample checked.
- **"No peer mentions Tatva" claim:** independently re-grepped "Tatva" case-insensitive across all
  15 files — zero hits, confirming B06's claim.
- **Numeric spot-checks embedded in citations** (phenol INR85->150/kg, caustic "doubled,"
  NEOGEN Ionics INR13cr/INR36cr, INR161cr preferential allotment, INR1,330cr total debt, ACUTAAS
  guidance 25%->30%, Indichem KRW30bn) — all confirmed verbatim against source in the checks above.

## Summary

Coverage claims in B06 are substantially accurate: 15 of 15 peer-quarter transcripts genuinely
contributed real, findable evidence, all 7 of B05's peer_questions received a verdict, and no
VERIFIED claim rests on insufficient anchoring (because no claim was marked VERIFIED at all —
the report is appropriately conservative throughout, using PARTIALLY VERIFIED / CONTRADICTED /
UNVERIFIABLE rather than overclaiming). The one substantive defect found is a real, repeated
(4x) citation error: a genuine and correctly-transcribed quote about Chinese hydroquinone
competitive pricing is dated to the wrong call (Feb 2026 instead of its actual source, May 2026),
which would mislead anyone tracing that specific anchor back to source. This does not change any
of the seven claim verdicts (the underlying finding is independently true and recoverable
elsewhere in the dataset) but it is a real accuracy defect in source citation, hence MAJOR rather
than MINOR.

acceptance_rate = 14 of 15 peer-quarter entries handled with zero defect / 15 = 93%. (The 15th,
CLEAN Q3 FY26, is "correctly handled" on 3 of its 4 cited items and mishandled on the 4th; scored
as a partial/flagged entry rather than a clean pass.)

```yaml
stage: B12d
company: "TATVA"
run_date: "2026-07-12"
model: claude-sonnet-5
status: complete
peers_audited: 15
substantive_confirmed: 15
substantive_unsupported: []
unused_but_relevant:
  - {peer: "NEOGEN", missed_item: "NEOGEN's own Pakhajan/Dahej commissioning-approval delays (Feb 2026, May 2026 calls) are thematically relevant third-peer corroboration for Claim 5 (industry-wide greenfield/EPC slippage) but NEOGEN was not on B05's designated check_peers list for that claim, so B06 did not cite it there; already covered in a different framing (leverage/capacity-race) in Part 2C. MINOR, not a coverage failure attributable to B06.", anchor: "NEOGEN Feb 2026 call, e.g. 'why this repeated delay in the approvals'; NEOGEN May 2026 call, 'slight delay in terms of commissioning of the project'"}
claims_all_addressed: true
verdict_discipline_fails: []
findings:
  - {severity: "MAJOR", location: "B06 Part 2B, Part 2E, Peer Coverage Map (CLEAN Q3 FY26 row), YAML risks_peers_raise (repeated 4x)", claimed: "Quote 'calibrate our prices... to keep our market share within China as a market' attributed to CLEAN Feb 2026 (Q3 FY26) call", source_truth: "Quote is verbatim-accurate but occurs only in CLEAN-Concall_May_2026_Transcript.txt (Q4 FY26), not the Feb 2026 transcript; Feb 2026 transcript contains a different, related but distinct quote ('no choice but to lower our prices of MEHQ...') on the same general topic", note: "Content is real and independently supported elsewhere; the specific anchor as printed is wrong in all 4 locations it appears, a systematic copy-forward error rather than a one-off typo. Does not change any of the 7 claim verdicts."
  - {severity: "MINOR", location: "B06 Part 1, Claim 6 evidence section", claimed: "Baba Fine Chemicals (BFC) generating INR42.1 crore in the Q3 FY26 segment", source_truth: "INR42.1cr is the total 'Specialty Chemicals segment' revenue (ACUTAAS Feb 2026 call), of which BFC's 'commodity chemical sub-segment' is a described contributor via recovery, not the segment's sole or exact figure", note: "Segment-vs-subsegment conflation; figure is anchored to a real number, just mislabeled in scope"}
critical_count: 0
major_count: 1
minor_count: 2
acceptance_rate: 93
```
