# Verifier summary, Yasho Industries (Phase 1 Lite)

Four Phase 1 verifiers: A (numbers), B (red flag coverage), C (framework, Gate 0 and emerging moat portion), D (peer utilisation). Verifier C's valuation half is deferred to Phase 3 and did not run. Findings below are sorted CRITICAL, then MAJOR, then MINOR, each with a location anchor and the verifier's one line note.

## Confidence delta and acceptance rates

| Component | Verifier | Acceptance / coverage |
|---|---|---|
| Numerical acceptance | A (B12a) | 85.7 |
| Red flag coverage | B (B12b) | 85 (fully caught 62; 8 of 13) |
| Framework adherence, gate0 + emoat | C (B12c) | 100 |
| Peer utilisation | D (B12d) | 90.9 |
| Overall (min of four) | | 85 |

Band: 75 to 89 normal; note specifics; no verdict downgrade.

Severity totals across all four verifiers: 0 CRITICAL, 4 MAJOR, 10 MINOR.

Source fidelity: 0 failures. No Verifier A finding carries source_fidelity true. Verifier A's initial CRITICAL on the MNC advance figure was re-graded to MAJOR after the orchestrator's severity semantics sanity check: the pipeline faithfully captured a company disclosure inconsistency (Rs 51.4 Cr MD&A vs Rs 29.52 Cr audited notes vs Rs 98.12 Cr presentation) and sourced all three figures correctly, so source_fidelity is false. A company's own inconsistency is not a pipeline fidelity failure. No REWORK.

## Verifier A, numbers (B12a). 28 figures checked, acceptance 85.7

| Severity | Location | Note |
|---|---|---|
| MAJOR | B02 Finding 1; B03 Phase 4; B07 Section 1A | MNC customer advances inconsistent within company disclosure: Rs 29.52 Cr audited Note 19/24/48, Rs 51.4 Cr MD&A p.30, Rs 98.12 Cr Q1FY27 presentation. All three sourced correctly and flagged by the pipeline. Company disclosure gap for Halt 1, not fabrication. Re-graded from initial CRITICAL; source_fidelity false. |
| MINOR | B02 Finding 6 | Drawing power variance Rs 31.7 to 52.7 Cr/quarter verified against Note 46 p.154. Individual quarterly lakhs not isolable in the PDF extract; sourcing and calculation confirmed. Data retrieval limitation, not report error. |
| MINOR | B02 Finding 8 | 43.2% on demand share = Rs 23,386.05L / Rs 54,094.07L verified from Note 41E p.148. Component lines not isolable in extract; calculation accurate. |
| MINOR | B06 Peers; B05 Concall | Raw material inflation 10 to 15% sourced correctly to the Q1FY27 transcript. Peer evidence (NOCIL aniline +70-73%, Camlin Fine phenol +76%) contradicts the magnitude on same chemistry comparables. Verification finding for Halt 1, not a fidelity error. |

Coverage note: 24 of 28 figures verified clean. All Gate 0 Block A to E inputs and all Q1FY27 presentation figures verified clean. Zero fabrication or misreading.

## Verifier B, red flag coverage (B12b). 13 independent flags, fully caught 8 (62), coverage 85

| Severity | Location | Note |
|---|---|---|
| MAJOR | B05 2D/2E utilisation + 2A tracker | MISSED: "we have shut Vapi" (Q1 FY27 p15) vs "Vapi 95-98%" (p11) unreconciled; the ramp is a Pakhajan only story. Material to the operating leverage and margin thesis. |
| MAJOR | B05 2A tracker + 2C | MISSED: WC beat 190 to 143 days presented as a clean quality beat; management's own "genuine supply issue... inventory base came down" admission (partly involuntary) unrecorded. Inverts a headline positive. |
| MAJOR | B05 4B Q6 asset turn | Under-weighted: Yasho's own asset turn assumption fell from 4:1 (Q3 FY26) to 2.5x (Q1 FY27) while the FY28 target rose; peers imply ~1x. Own number downgrade not flagged as a red flag. |
| MINOR | B05 4D red flags | Plant utilisation evasion graded LOW-MEDIUM; a 2+ quarter evasion of the load bearing operating variable should grade higher. |
| MINOR | B05 2A promise tracker | WC "160-175 by March MISSED (190)": promise was INVENTORY days (Q3 ~170, in band); 190 is working capital days. Basis mismatch, overstated miss in the conservative direction. |
| MINOR | B05 2C / analyst note | Scripted "confident to sustain" margin softens to "can't promise / try our best" in Q&A; script vs Q&A softening not isolated. |

Credibility grade: concur (B). The two misses and the under-weighted utilisation evasion press Transparency to the low end of B, not below.

## Verifier C, framework, Gate 0 and emerging moat (B12c). Rules checked 65, fails 0, acceptance 100

Gate 0: 36 rules checked, 0 fails. Emerging moat: 29 rules checked, 0 fails. Valuation portion: 0 rules checked, deferred to Phase 3. Gate 0 AVOID re-derived and confirmed.

| Severity | Location | Note |
|---|---|---|
| MINOR | B01 Block F / M3 | M3 uses FY26 latest ROCE (11.34%); pairing median ROCE (12.87%) with the FAT tier would give M3=1 and grand total 45 to 46. No effect on moats present (3, MODERATE) or classification (AVOID). Latest ROCE pairing internally consistent; advisory only. |
| MINOR | B01 confidence / YAML flags | The "5 to 6 years lower confidence, may not have seen full cycle" note is in the dashboard prose but not in the YAML flags array. Cosmetic; the flags slot is scoped to FLAG-GATE0, which is present. |

## Verifier D, peer utilisation (B12d). 11 peer calls audited, acceptance 100

10 of 11 calls substantive, all 3 peer entities correctly handled, 1 call correctly downgraded to CITED-ONLY, zero fabricated or unsupported SUBSTANTIVE citations.

| Severity | Location | Note |
|---|---|---|
| MINOR | B06 Q6 verdict + contradicted array | CONTRADICTED (asset turn ~1.0-1.1x vs 2.5-4x) rests on a single peer (NOCIL), a computed inference not a peer stated ratio. Hedged correctly in prose ("directional rather than definitive"), but the bare CONTRADICTED label risks equal weight with the 2 peer VERIFIED finding. source_fidelity true (label weight, not a number existence failure; not a REWORK trigger). |
| MINOR | B06 Q4 verdict + contradicted array | CONTRADICTED (EU FTA timeline) rests on a single peer (NOCIL Feb 2026), a direct dated verbatim quote, correctly anchored. Single peer basis noted for completeness; lower risk than Q6. |
