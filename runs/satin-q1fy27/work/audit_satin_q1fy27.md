# A5 ADVERSARY / COMPLETENESS AUDIT — SATIN CREDITCARE (NSE: SATIN) — Q1 FY27
## RE-AUDIT v2 (dated 2026-07-30) — target: REVISED A4 merged review

Fresh context. Inputs seen: revised A4 review, the three A1 extracts, the three A2
ledgers. A3 forensics files are NOT in my context by design; where the task asks me to
confirm "every A3 finding produces a question", I verify against the finding-IDs A4
itself carries and their mapping to Step 8.5 rows. Every number below is re-derived from
the raw extract lines; I do not defer to A4's or A3's cites.

Scope of this re-audit pass (per task): (a) confirm the prior-pass BLOCKING gap — the
client-base / over-indebtedness counter — is now discharged across diagnostics, Bear
column, monitorables, and a Questions-for-Management row; (b) confirm the Reg 52(4)
consolidated sector-ratio absence is handled honestly and NOT substituted with
standalone; (c) confirm the A3-F6-01 discharge and Reg 52(4) OCR wording are corrected;
(d) full coverage, arithmetic, and adversarial re-run on the merits.

---

## 1. COVERAGE AUDIT

Fresh grep pass vs A2 ledger counts.

| Category | A2 count | My fresh count | Method | Orphan / missing | Status |
|---|---|---|---|---|---|
| Results: statement blocks | 2 | 2 | `grep "Notes to the unaudited"` = 2 (std+consol) | none | PASS |
| Results: notes (16+16) | 32 | 32 | 2 note-sets, 16 each; spot-verified Notes 4,5,6,7,8,9,10,13,14,15,16 both sides | none | PASS |
| Results: Reg 52(4) std sector ratios | 5 (populated) | 5 | ln 403-407 a)GNPA 2.18 b)NNPA 0.33 c)PCR 84.66 d)CRAR 26.74 e)LCR 134.89 | none | PASS |
| Results: Reg 52(4) consol sector ratios | flagged ABSENT | ABSENT (confirmed) | ln 782: table terminates row 18; no GNPA/NNPA/PCR/CRAR/LCR rows; 400-DPI repair confirms | none | PASS (see 1.1) |
| Press release: disclosure units | 112 | reconciled (44+19+2+10+6+20+11) | bullets/table-rows/footnotes/headings/pages/prose/absent-standard | none | PASS |
| Presentation: slides | 42 | 42 | `grep "^\[page "` = 42 | none | PASS |
| Presentation: ratio-slide rows (17/19) | 24 | 24 | ln 480-491 / 545-556 all present, YoY/QoQ cells blank (DELTA_OMITTED) | none | PASS |
| Presentation: client-base series (s22) | present | present | ln 641-660: New-clients 1.9/2.5/2.2/1.6/1.5; AUM/LO 1.08→1.39; AUM/branch 6.8→7.4 | none | PASS |
| Presentation: ₹61,000 JLG ticket (s36) | present | present | ln 1147 "₹61,000 (JLG)" | none | PASS |

**Orphan-row check (ledger rows absent from A4):** none. Every material ledger block is
either cited or explicitly carried as ND / reviewed-no-finding in A4: full P&L (1L.a/b),
all comparability notes (0D table), Reg 52(4) both statements, DA loan-transfer note
(A3-F1-02/Q2), segment note, auditor paras (0D), warrants/ESOP (0C), funding & lender
mix (5.a/monitorables), geography (5.b), subsidiaries (5.b/Q5/Q10), guidance (6B/6D),
shareholding & price (6D/8B), the "xx" active-clients artifact + states 30-vs-32 (Q12),
SGAL zero-financials (Q10/flags), absent-standard PR disclosures (NNPA/PAR buckets →
ND / monitorables). No orphan.

**Missing-from-ledger check (rows my fresh pass found, ledger lacks):** none.

### 1.1 Consolidated Reg 52(4) sector-ratio absence — handled honestly
CONFIRMED CLEAN. Three independent checks:
1. Extract ln 782 states the consolidated Reg 52(4) table genuinely terminates at row 18
   (Net profit margin 16.04%); no GNPA/NNPA/PCR/CRAR/LCR/Tier/ECL row exists; the earlier
   garbled "ECL" fragment was seal-stamp OCR noise, not a data row. This is an absence in
   the SOURCE, not an OCR artifact.
2. A4 carries consol GNPA/NNPA/PCR/CRAR/LCR as `ND` in every table that touches them
   (1L.d note ln 239; 2.a has no consol GNPA row; 5.b line "Consol GNPA/NNPA/PCR/CRAR/LCR
   = ND"). No standalone analogue is substituted for any absent consol cell — verified
   cell by cell.
3. The 400-DPI repair is genuine and legible in the extract: Net worth 2,94,361.98 L =
   Rs 2,943.62 Cr (ln 769), NPAT 12,264.56 L = Rs 122.65 Cr (ln 770), EPS 11.15/11.15
   (ln 771-772), NP-margin 16.04% (ln 781). A4's preamble item 1 describes exactly this.
   The OCR wording is CORRECTED from the prior pass (repair scope limited to the legible
   rows; sector ratios explicitly NOT claimed repaired, flagged genuinely absent). PASS.

### 1.2 One non-blocking observation (not a FAIL, no loop-back)
The A2 results ledger enumerated consolidated Note 14 as 19 rows (7.14.1–7.14.19),
including 7.14.19 "sector-specific ratios" as a placeholder for an expected-but-absent
row (correctly flagged OCR_DROPPED_LINE / re-verify). The 400-DPI repair now confirms
that row is genuinely absent, so the consolidated table has 18 rows, and the A2
line-item total of 144 technically includes one confirmed-absent placeholder (true
present-row count 143). This is OVER-inclusion with a flag, not omission: no evidence is
lost and A4 treats the row as ND with no substitution. Enumerate-with-flag rather than
drop is the correct A2 discipline. Recorded for the record; it does not gate the verdict
and requires no A2 loop-back.

---

## 2. ARITHMETIC AUDIT

All raws re-read from extract_results (Lakhs, x0.01 = Cr) and extract_presentation.
No figure below is untied to a cited line. No mismatch above rounding.

| Metric | A4 value | Recomputed | Source line(s) | Status |
|---|---|---|---|---|
| Lakhs→Cr: II std | 632.03 | 63,202.99 L ×0.01 = 632.03 | res ln 175 | OK |
| Lakhs→Cr: PBT std | 157.96 | 15,795.61 L = 157.96 | res ln 195 | OK |
| Lakhs→Cr: PAT std | 120.29 | 12,028.68 L = 120.29 | res ln 203 | OK |
| Lakhs→Cr: PAT consol | 122.65 | 12,264.56 L = 122.65 | res ln 609/770 | OK |
| Lakhs→Cr: tax std / consol | 37.67 / 38.55 | 3,766.93 / 3,855.11 L | res ln 201 / 608 | OK |
| Lakhs→Cr: consol net worth | 2,943.62 | 2,94,361.98 L = 2,943.62 | res ln 769 | OK |
| NII std (II − int cost) | 363.14 | 632.03 − 268.89 = 363.14 | res ln 175/187 | OK |
| PPOP std (PBT+impair) | 258.11 | 157.96 + 100.15 = 258.11 | res ln 195/189 | OK |
| PPOP std Q1FY26 | 189.26 | 54.63 + 134.64 = 189.265 → 189.26 (Lakhs-precise) | res ln 195/189 | OK |
| ETR std / consol | ~24% | 37.67/157.96 = 23.85%; 38.55/161.20 = 23.91% | res ln 201/195, 608/603 | OK |
| Deferred-tax credit std/consol | 4.72 / 7.45 | (472.20)/(744.80) L | res ln 200 / 607 | OK |
| YoY consol PAT | +171.9% | (122.65/45.10)−1 = +171.95% | res | OK |
| YoY consol PBT | +177.6% | (161.20/58.08)−1 = +177.55% | res | OK |
| YoY consol AUM | +27.5% | (15,935/12,499)−1 = +27.49% | PR 66 | OK |
| YoY std AUM | +21.5% | (13,312/10,956)−1 = +21.50% | PR 97 | OK |
| YoY std PAT | +182.4% | (120.29/42.60)−1 = +182.37% | res | OK |
| YoY consol total income | +8.0% | (764.75/707.84)−1 = +8.04% | res ln 593 | OK |
| YoY consol impairment | −25.7% | (106.12/142.88)−1 = −25.73% | res ln 598 | OK |
| Std GNPA YoY | −156 bps | 3.74% − 2.18% = 156 bps | PR 161 / ln 403 | OK |
| S-vs-C PAT gap Q1FY27 | +2.36 (+1.96%) | 122.65−120.29 = 2.36; /120.29 = 1.96% | res ln 203/609 | OK |
| S-vs-C PAT gap Q4FY26 | +25.10 (+18.33%) | 162.05−136.95 = 25.10; /136.95 = 18.33% | deck/res | OK |
| S-vs-C PAT gap Q1FY26 | +2.50 (+5.86%) | 45.10−42.60 = 2.50; /42.60 = 5.87% | res | OK (rounding) |
| S-vs-C PAT gap FY26 | +30.13 (+9.97%) | 332.21−302.08 = 30.13; /302.08 = 9.97% | res | OK |
| Sub gap QoQ swing | −16.4 pp | 18.33% − 1.96% = 16.37 pp | deck/res | OK |
| Sub PATs vs uplift | 6.4 > 2.36 | 1.5+4.9 = 6.4; drag ≈ 6.4−2.36 = 4.04 | PR 179/189 | OK |
| Consol ROA step-down QoQ | 4.71→3.30 (−141 bps) | −141 bps | s17/L486 | OK |
| Consol ROE step-down QoQ | 23.31→16.75 (−656 bps) | −656 bps | s17/L488 | OK |
| Consol NIM step-down QoQ | 15.20→13.21 (−199 bps) | −199 bps | s17/L482 | OK |
| Std ROA/ROE/NIM step-down | 4.31→3.55 / 17.91→15.10 / 15.85→14.36 | −76 / −281 / −149 bps | s19/L551,553,547 | OK |
| Overlay QoQ (fresh charge) | 21→36 = +15 | Rs 36 (Q1) − Rs 21 (Q4) = Rs 15 | s17-note2/L495 | OK |
| Overlay 3-pt trend | 8 / 21 / 36 | L495: ₹36 Q1FY27, ₹21 Q4FY26, ₹8 Q1FY26 | s17/L495 | OK |
| Treasury effect on PPOP YoY | ≈ +Rs 1 Cr | FV swing −89.54 (57.11 loss vs 32.43 gain) + FX swing +90.61 (62.43 credit vs 28.18 charge) = +1.07 | res ln 178/188 | OK |
| Escalation ROE annualised | 16.7% | 122.65×4 / 2,943.62 = 16.67% (≈ deck 16.75%) | res ln 609/769 | OK |
| EPS std / consol basic=diluted | 10.94 / 11.15 | ln 222-223 / 635-636; warrants excluded pending allotment | res | OK |
| Off-book implied | ~3,270 (~25%) | on-book 219/2.18% = 10,046; 13,312−10,046 = 3,266; deck off-book 3,277 | PR 161 / s35/L1103 | OK |
| On-book provision % | 2.51% | 252/10,035 = 2.51% | PR 163 | OK |
| Consol-vs-std net worth gap | Rs 275 Cr / 8.55% | 3,218.93 − 2,943.62 = 275.31; /3,218.93 = 8.55% | res ln 389/769 | OK |
| Active clients YoY | ~+3% | consol 34/33 = +3.0%; std 33/32 = +3.1% | s16/L467, s18/L534, PR 90 | OK |
| New-client adds trend | 2.5→2.2→1.6→1.5; 1.5 vs 1.9 YoY | ln 641-645: Q1FY26 1.9 / Q2 2.5 / Q3 2.2 / Q4 1.6 / Q1FY27 1.5 | s22/L642-645 | OK |
| AUM per loan officer | 1.08 → 1.39 | ln 658-660: Q1FY26 1.08, Q1FY27 1.39 | s22/L658-660 | OK |
| ~₹61,000 JLG ticket | ~Rs 61,000 | ln 1147 "₹61,000 (JLG)" | s36/L1147 | OK |

**Newly-grafted client-base / over-indebtedness figures — all tie to cited lines:**
active clients +3% YoY vs AUM +21.5% std / +27.5% consol (verified); new adds 2.5→1.5
lakh peak-to-current and 1.5 vs 1.9 YoY (ln 641-645, endpoints corroborated, chart
flagged CHART_LAYOUT_AMBIGUOUS but endpoints high-confidence); AUM/loan-officer 1.08→1.39
(ln 658-660); ~Rs 61,000 ticket (ln 1147). No arithmetic mismatch. No untied figure.

Zero arithmetic mismatches above rounding.

---

## 3. ADVERSARIAL READ — three most positive claims, strongest bear counters

**Claim 1 — "All three escalation conditions met (PAT ≥110, std GNPA ≤3.05, consol ROE
≥16); escalate toward BUY."**
Strongest bear counter (same text): the ROE clears the 16% floor by only 75 bps on a
single-quarter-annualised basis that fell from 23.31% (Q4), the +172% PAT is largely a
Q1FY26 trough base effect (impairment −25.7% off a 4.52% loan-loss quarter), and the
GNPA that anchors condition 2 is unverifiable (no write-off/ECL/ARC walk; ~25% of AUM
off-book). SURVIVES — but ALREADY GRAFTED: 6C caveats (i)/(ii), the Bear paragraph, the
INDETERMINATE cap, and the flag "clears 16% floor by only 75 bps and is overlay-flattered
to 20.39%." No new graft required.

**Claim 2 — "PPOP grew +33%/+36% on genuine operating leverage; treasury nets ~Rs 1 Cr."**
Strongest bear counter: PPOP sits above the impairment add-back and includes the volatile
Rs 62.43 Cr FX finance-cost credit; strip it and PPOP is flattered. Test from the raws:
FV YoY swing = −89.54 Cr (57.11 loss vs 32.43 gain) inside revenue; FX YoY swing = +90.61
Cr (62.43 credit vs 28.18 charge) inside finance cost; net effect on PPOP = +1.07 Cr.
The counter does NOT survive: the two treasury items genuinely offset within PPOP to ~Rs 1
Cr YoY, so YoY PPOP growth is not FX-flattered. A4 states exactly this and flags "counter
does NOT survive." The residual FX reversal risk (a next-quarter, not this-quarter, PPOP
issue) is separately carried (FND-04, tripwire #9, Q8). Correctly handled.

**Claim 3 — "AUM +27.5% consol beats the 20-25% guide."**
Strongest bear counter: the growth is ticket-led on a near-static borrower base — active
clients +3% while AUM +21.5%/+27.5%, new-client adds falling every quarter since the Q2
FY26 peak (2.5→1.5 lakh), AUM/loan-officer up 1.08→1.39 at a ~Rs 61,000 ticket — a
recognised MFI over-indebtedness precursor that a clean 2.18% GNPA does not yet reflect.
SURVIVES — and this is the prior pass's BLOCKING gap. It is now DISCHARGED in the revised
review across all four required surfaces:
- Diagnostics: Step 2 "Growth-quality diagnostic (grafted counter…)" (ln 309-322) and
  Step 5L "Growth quality / borrower-base divergence" mandatory-lender answer (ln 464-473).
- Bear column: Symmetric Bear paragraph (ln 719-723).
- Monitorables: register row "Client-base growth vs AUM growth divergence…" (ln 690) and
  the YAML monitorables entry.
- Questions for Management: Q13 (ln 656), with a bull/bear answer pair and from-finding
  "A5-graft-client-base / A3-11". Also surfaced as a standalone FLAG in the verdict and
  YAML flags.
No un-incorporated surviving counter remains.

**Interpretation-integrity checks (no AMBIGUOUS/FORWARD-SIGNAL silently upgraded to fact):**
- SFL GNPA 3.5% labelled "deck-only, not in filing" everywhere it appears (5.b, 6B#5, 6C).
- Q2/Q3 FY26 mid-quarter ratios carry the "~ CHART_LAYOUT_AMBIGUOUS, endpoints
  corroborated" caveat (Step 3, 5-qtr table).
- Consol sector ratios held ND, not asserted.
- GNPA-improvement mechanism held INDETERMINATE, never asserted organic; Asset-Quality
  Multiplier explicitly NOT upgraded on unverified GNPA (HOLD at Sound).
- Every A3 finding-ID A4 carries (FND-01..10; A3-F1-01, F1-02, F2-01, F2-02, F6-01,
  F10-01, F14-01, F16-01, F16-02; A3-01..12) maps to at least one Step 8.5 question
  (union check across Q1-Q13 from_finding_id lists = complete; A3-F6-01 appears in Q6/Q11
  and is additionally discharged in the Monitorables register preamble ln 677-680, so it
  is no longer a silent drop — CORRECTED from prior pass).
- Escalation/trigger treated as a FLAG, not a Decision Status change: Step 8 (ln 613-615),
  6C (ln 570), verdict (ln 752-753) all state "A4 FLAGS; the human decides; Decision Status
  is NOT changed." Consistent.
- Verdict PROCEED WITH CAVEATS sits inside the PROCEED set and is correctly capped by the
  INDETERMINATE asset-quality mechanism per house rule (INDETERMINATE cannot silently
  resolve to PROCEED); the four missing-evidence items are named. Consistent.

---

## 4. VERDICT

**COMPLETE.**

The revised A4 review passes all three audits on the merits:
- COVERAGE: fresh grep reconciles to every A2 count (slides 42, note-sets 2, std sector
  ratios 5, consol sector ratios genuinely absent, client-base series present). No orphan
  row, nothing missing from any ledger. The consolidated Reg 52(4) sector-ratio absence is
  handled honestly (ND, source-absent, 400-DPI-repair scope correct, no standalone
  substitution). One non-blocking over-inclusion (consol Note-14 phantom row 19) is
  transparently flagged and loses no evidence — no loop-back.
- ARITHMETIC: every headline, YoY/QoQ walk, the S-vs-C PAT gap, ROA/ROE/NIM step-downs,
  the Rs 15 Cr fresh-overlay effect, ETR, EPS, Lakhs→Cr conversions, and the newly-grafted
  client-base figures re-derive from cited raws with zero mismatch above rounding. The
  ~Rs 1 Cr net-treasury-on-PPOP claim independently checks out (+1.07 Cr).
- ADVERSARIAL: the prior BLOCKING gap (client-base / over-indebtedness counter) is now
  discharged across diagnostics, Bear column, monitorables, and Q13; the A3-F6-01 discharge
  and the Reg 52(4) OCR wording are corrected; no AMBIGUOUS/FORWARD-SIGNAL finding is
  upgraded to fact; the escalation is a FLAG not a status change; the verdict is within the
  PROCEED set and consistent with the INDETERMINATE asset-quality cap.

No loop-back to A2, A3, or A4. Proceeds to Notion save.

```yaml
stage: A5-adversary
company: "SATIN"
quarter: "Q1FY27"
model: claude-opus-4-8
status: complete
verdict: COMPLETE
coverage:
  orphan_rows: []
  missing_from_ledger: []
arithmetic_mismatches: []
surviving_bear_counters:
  - {claim: "AUM +27.5% consol beats guide", counter: "Ticket-led growth on near-static borrower base: active clients +3% vs AUM +21.5%/+27.5%, new adds 2.5->1.5 lakh, AUM/LO 1.08->1.39 at ~Rs 61,000 ticket = MFI over-indebtedness early warning", source_line: "s16/L467,s18/L534,s22/L642-645,s22/L658-660,s36/L1147", status: "already grafted in revised A4 (Step2 diagnostics, Step5L, Bear, monitorable L690, Q13)"}
  - {claim: "All 3 escalation conditions met -> escalate", counter: "ROE clears 16% floor by only 75bps off 23.31% Q4; +172% PAT is Q1FY26 trough base effect; GNPA unverifiable, ~25% off-book", source_line: "s17/L488;res ln403,609", status: "already grafted (6C caveats, Bear, INDETERMINATE cap)"}
loop_back_to: ""
gap: ""
```
