# A5 ADVERSARY / COMPLETENESS AUDIT — Balaji Amines Limited (BALAMINES), Q1 FY27

**Second-pass (loop-2) audit.** The review under audit was re-emitted after a prior A5 loop
that grafted two counters (A5-C1, A5-C2). Per instruction this pass re-derives independently
from the A1 extracts and A2 ledgers, does not defer to A4's or A3's cites, and re-checks
whether the two prior counters are now incorporated with correct line cites. Fresh grep/sweep
enumeration was diffed against both ledgers; every derived metric was recomputed from raw
Lakhs (results, x0.01 -> Cr) and Crores (press). Concall/deck absence is disclosed in the
review's flags and is NOT treated as a failure.

Unit note: results filing values are Lakhs; I converted to Cr for every recompute. Press
release is already Cr. Review line cites (L###) reference the results extract unless prefixed
"press".

---

## AUDIT 1 — COVERAGE

Fresh enumeration (independent grep + manual sweep of each extract) vs the A2 ledgers, then
each ledger row checked for citation-or-reviewed-no-finding in A4.

| Category | A2 count | My fresh count | Orphan rows (in ledger, absent from A4) | Status |
|---|---|---|---|---|
| Results — agenda items (L49/51/53-55) | 3 | 3 | none (results approval + review-report note-taking cited Step 0; board timing L57 used in A3-03 flag) | PASS |
| Results — numbered notes (L291-304) | 5 | 5 | none (all 5 in Step 0D table) | PASS |
| Results — line-items (logical) | 102 | 102 (106 physical − 4 wraps: L111-112/134-135/173-174/202-203) | none (all P&L/segment rows in Steps 1A-1E, 2E, 4A, 5) | PASS |
| Results — zero-standing cells | 13 | 13 (SA: 119,129,130,131,132,136; CO: 181,194,195,196,197,204; SEG: 247) | none (exceptionals-nil cited L54; OCI/other-equity reviewed-no-finding, immaterial/BS-only) | PASS |
| Results — auditor paras | 9 | 9 (SA 4 + CO 5, incl. Other-Matter L417) | none (unmodified opinion + Other-Matter both in Step 0D / A3-04) | PASS |
| Results — entities | 2 | 2 (BAL parent; BSC subsidiary L301/L398) | none (Note 3, S-vs-C gap Step 1E) | PASS |
| Results — signature blocks | 3 | 3 (CS Kothadiya; SA auditor L367-374; CO auditor L430-436) | none (auditor timestamp in A3-03/Step 8.5-Q8) | PASS |
| Press — pages | 5 | 5 | none | PASS |
| Press — highlight-table cells | 48 | 48 (8 metrics × 6 cols) | none (Steps 1C/1D cross-checks; Cash PAT at Step 5/F11-02) | PASS |
| Press — segment volumes | 3 | 3 (L98-100; sum 21,586.60 ≈ 21,587) | none (Step 5A new-disclosure) | PASS |
| Press — diluted-EPS figures | 2 | 2 (L108-109; 23.13 / 19.99) | none (Q7 / F10-01) | PASS |
| Press — mgmt/forward statements | 32 | 32 (sentence-level over the 9 spans) | none (Section B Steps 1-2; F6/F7/F16 findings) | PASS |
| Press — footnotes/disclaimers | 2 | 2 (Cash-PAT def L84; Safe Harbor L208-216) | none (F11-02; safe-harbour Step 0D-B) | PASS |
| Press — admin identifiers | 14 | 14 | none (IR contact / [NS1] artefact F14-01 cited) | PASS |

**Rows my fresh pass found that the ledger lacks:** none.
**Orphan rows (ledger row not cited and not marked reviewed-no-finding in A4):** none.

COVERAGE VERDICT: **PASS.** No orphan rows; nothing missing from either ledger. The 15 A3
findings and both A5 grafted counters map cleanly onto enumerated ledger rows.

---

## AUDIT 2 — ARITHMETIC

Every derived metric recomputed from raw extracted numbers. All ties within rounding.

| Metric | A4 value | My recompute | Source line(s) | Status |
|---|---|---|---|---|
| SA Op EBITDA Q1FY27 (PBT+D+FC−OI) | 103.46 | 97.82+11.54+0.27−6.17 = 103.46 | L120/114/115/107 | PASS |
| SA Op EBITDA margin Q1FY27 | 24.47% | 103.46/422.74 = 24.47% | L106 | PASS |
| SA Op EBITDA margin YoY | +679 bps | 24.47%−17.68% = 6.79pp | L106 (both yrs) | PASS |
| SA reported EBITDA Q1FY27 | 109.63 | 97.82+11.54+0.27 = 109.63 | — | PASS |
| SA ETR Q1FY27 / Q1FY26 | 26.25% / 23.96% | 25.68/97.82 ; 12.54/52.34 | L125/120 | PASS |
| SA revenue YoY | +32.4% | 422.74/319.38−1 = 32.36% | L106 | PASS |
| SA PAT YoY | +81.3% | 72.14/39.80−1 = 81.3% | L126 | PASS |
| SA core PBT ex-OI YoY | +103.3% | 91.65/45.07−1 = 103.3% | L120/107 | PASS |
| CO Op EBITDA Q1FY27 | 115.87 | 106.20+13.78+1.41−5.52 = 115.87 | L182/176/177/169 | PASS |
| CO Op EBITDA margin Q1FY27 / YoY | 25.41% / +1,015 bps | 115.87/455.93 ; −15.26% = 10.15pp | L168 | PASS |
| CO reported EBITDA Q1FY27 | 121.40 | 106.20+13.78+1.41 = 121.39 | — | PASS (rounds 121.40) |
| CO revenue YoY | +27.2% | 455.93/358.34−1 = 27.23% | L168 | PASS |
| CO PAT total YoY / owners YoY | +113.9% / +97.2% | 78.12/36.53−1 ; 74.94/38.00−1 | L188/190 | PASS |
| CO ETR Q1FY27 / Q1FY26 | 26.45% / 25.48% | 28.09/106.20 ; 12.49/49.01 | L187/182 | PASS |
| CO core PBT ex-OI YoY | +151.7% | 100.68/39.99−1 = 151.7% | L182/169 | PASS |
| S-vs-C PAT gap Q1FY27 (Cr / %SA) | +5.98 / +8.28% | 78.12−72.14 ; 5.98/72.14 = 8.29% | L188/126 | PASS |
| S-vs-C PAT gap Q1FY26 | −3.27 / −8.22% | 36.53−39.80 ; /39.80 | L188/126 | PASS |
| S-vs-C YoY swing | ~16.5pp | −8.22 → +8.28 = 16.50pp | — | PASS |
| BSC-attributable volume proxy | 2,723 → 968 MT | 27,570−24,847 ; 21,587−20,619 | press L82 | PASS |
| BSC proxy volume YoY | ~−64% | 968/2,723−1 = −64.4% | press L82 | PASS |
| CO volume YoY / QoQ | −21.7% / −21.0% | 21,587/27,570−1 ; /27,341−1 | press L82 | PASS |
| SA volume YoY / QoQ | −17.0% / −18.8% | 20,619/24,847−1 ; /25,394−1 | press L82 | PASS |
| CO realization Q1FY27 / Q1FY26 (L/MT) | 2.11 / 1.30 | 45,592.56L/21,587 ; 35,834.12L/27,570 | L168 / press L82 | PASS |
| CO realization YoY | ~+62% | 2.11/1.30−1 = 62.3% | — | PASS |
| Amines seg revenue YoY | +26.7% | 452.89/357.37−1 | L233 | PASS |
| Hotel seg revenue YoY | −22.2% | 7.99/10.27−1 | L234 | PASS |
| Hotel seg PBIT (result b/int&tax) YoY | −59.0% | 1.60/3.90−1 | L241 | PASS |
| Hotel seg PBT YoY | −59.9% | 1.54/3.84−1 | L251 | PASS |
| CO PBT change decomposition | +59.32 / −2.30 / +0.17 = +57.19 | Amines 104.09−44.77; Hotel 1.54−3.84; Unalloc 0.57−0.40; sum ties to 106.20−49.01 | L250/251/252/182 | PASS |
| CO PAT bridge closes | +41.59 | GP+56.62 −emp5.35 +oth9.92 +dep0.19 −fin0.68 −OI3.50 −tax15.60 = +41.59 | L168-188 | PASS |
| SA PAT bridge closes | +32.34 | GP+46.84 −emp5.08 +oth5.23 −dep0.48 +fin0.07 −OI1.10 −tax13.14 = +32.34 | L106-126 | PASS |
| CO gross margin Q1FY26 → Q1FY27 | 40.8% → 44.5% (+370bps) | 146.33/358.34 ; 202.95/455.93 | L168/172/173 | PASS |
| CO other-exp/rev QoY | 19.86% → 13.43% (−640bps) | 71.16/358.34 ; 61.24/455.93 | L178/168 | PASS |
| Seg liabilities QoQ (total / Amines) | −153.39 / −164.06 Cr | 437.43−590.82 ; 289.59−453.64 | L264/261 | PASS |
| Seg assets QoQ (total / Amines) | −75.31 / −76.39 Cr | 2,667.23−2,742.54 ; 2,577.31−2,653.71 | L259/256 | PASS |
| ROCE proxy (indicative) | ~19% | (107.62×4=430.5)/(2,667.23−437.43=2,229.80) = 19.3% | L243/259/264 | PASS |
| Press "Total Revenue" = Total Income | CO 461 = 461.45 ; SA 429 = 428.91 | L170 ; L108 | — | PASS |
| Diluted EPS basis (press 23.13 = consol) | 23.13 consol vs 22.27 SA | L206 vs L138 | — | PASS |
| Reported-EBITDA press cross-check | SA 64/94/110 ; CO 64/102/121 | 63.74/94.49/109.63 ; 63.71/101.99/121.40 | — | PASS |

ARITHMETIC VERDICT: **PASS.** No mismatch above rounding. Every table (1C, 1D, 1E, 2A, 2B,
2D, 2E, 3, 4A, 4B, 5, 7) ties to the raw extract. Both PAT bridges close exactly; the segment
PBT decomposition sums to the consolidated +57.19 Cr; the S-vs-C gap and BSC volume proxy
reproduce. (Sole rounding note: CO reported EBITDA 121.39 vs stated 121.40, and S-vs-C
Q1FY27 8.29% vs stated 8.28% — both within rounding, not a FAIL.)

---

## AUDIT 3 — ADVERSARIAL READ (three most positive claims + strongest bear counter)

**Claim 1 (Section C L605): "Strong headline — consol revenue +27.2% YoY, op EBITDA margin
+1,015 bps to 25.41%, PAT owners +97.2%, EPS +97.2%."**
Strongest bear counter from the same text: the entire top-line and margin lift is
realization-led on a −21.7% YoY / −21.0% QoQ consolidated volume decline (press L82);
consolidated realization rose ~+62% (L168 vs press L82). A price/mix spike of unproven
durability, not volume-led compounding. **Counter is SUPPORTED but already incorporated** —
Step 2D (central analytical tension), Step 3C, and flag #2 (earnings-durability) carry it with
the correct L82/L168 cites. Not surviving.

**Claim 2 (Step 4C L319 / Section C L606): "Earnings quality clean — ~100%+ recurring, zero
exceptionals, other income declined (not inflating PAT), ETR near statutory."**
Strongest bear counter from the same text: a large slice of the "recurring" operating gain is a
−640 bps drop in the other-expenses/revenue ratio (consol 71.16 → 61.24 Cr, L178) achieved on
a shrinking tonnage base — variable power/fuel/freight fall mechanically with volume and may
reverse when volume recovers; and the gain is concentrated in one segment. **Counter is
SUPPORTED but already incorporated** — Step 2D final bullet ("durability of a −640 bps
other-expense-ratio move on a shrinking tonnage base is a legitimate question"), Step 2E, and
the Step 4C caveat explicitly discount the sustainability. Not surviving.

**Claim 3 (Section C L608): "Sole subsidiary BSC turned profit-accretive (S-vs-C PAT gap
−8.22% → +8.28%, NCI −1.47 → +3.18 Cr)."**
Strongest bear counter from the same text: BSC's ~+597.53 L PAT swing came on a ~−64%
attributable-volume proxy (2,723 → 968 MT, press L82); it is a realization/margin recovery, not
a proven volume-led growth vector. **Counter is SUPPORTED but already incorporated** — this is
A5-C1, grafted at Step 1E, Step 6D, Step 8, Q3, Section B 7A, Section C, and flag #3, all with
correct L82/L126/L188/L190/L191 cites.

**Prior-loop counter re-verification:**
- **A5-C1 (BSC not a proven growth vector):** incorporated with correct cites — Step 1E derives
  2,723 → 968 MT from press L82 (consol−standalone), ties the +597.53 L PAT swing to L188−L126,
  and reframes it as a monitorable. Correct.
- **A5-C2 (print not broad-based; Hotel decline):** incorporated with correct cites — new Step 2E
  uses Hotel revenue L234 (10.27→7.99, −22.2%), segment result L241 (−59.0%), segment PBT L251
  (1.54 vs 3.84, −59.9%), and Amines +59.32 Cr PBT from L250; ~100%+ of the +57.19 Cr group PBT
  growth attributed to one segment. Correct. Also carried in Step 4A attribution, Q9, Section B
  5B/7A, Section C, and flag #4.

**Search for a NEW surviving counter (independent):** I stress-tested four further positive
threads — (a) "deleveraging" from the −153.4 Cr QoQ segment-liability fall, (b) flat
depreciation despite DME commissioning read as clean, (c) OI-normalisation carries no downside,
(d) owners-EPS +97.2%. Each already carries its offsetting bear read in the review: (a) held
AMBIGUOUS (WC-unwind vs debt paydown, A3-02/Step 5, not asserted as positive); (b) flagged as a
forward depreciation headwind and an open question (Step 2C-Q5, 3C, 4C-Q3, Q4); (c) stated
symmetrically (OI already near a low); (d) owners PAT grew SLOWER than total (97.2% vs 113.9%)
and the review says so, so no hidden NCI inflation. **No new un-incorporated surviving bear
counter found.**

ADVERSARIAL VERDICT: **PASS.** All three top-positive claims have their strongest text-supported
bear counter already grafted with correct line cites; no positive claim carries an
un-incorporated surviving counter.

---

## HOUSE-RULE CROSS-CHECK (non-blocking, confirmed consistent)

- Cash conversion **INDETERMINATE** (no Q1 cash-flow statement; Reg 33 half-yearly) is not
  silently resolved to PROCEED; the four missing-evidence items are named (Step 5, flag #5). The
  verdict is PROCEED WITH FLAGS, which surfaces the cap prominently rather than upgrading past
  it — consistent with CLAUDE.md.
- No exit PE / valuation authority invoked (new coverage; deferred to FTTCP/Role 1).
- No STOP verdict asserted; only flags propagate. New-coverage 8A-W branch applied; no position
  action taken. Consistent.

---

## VERDICT

**COMPLETE.** Coverage is clean (no orphan rows, nothing missing from either ledger),
arithmetic ties throughout (no mismatch above rounding), and all three most-positive claims
have their strongest bear counter already incorporated with correct line cites — including the
two prior-loop counters A5-C1 and A5-C2, which are correctly grafted. No new surviving bear
counter. This review proceeds to Notion save.

```yaml
stage: A5-adversary
company: "BALAMINES"
quarter: "Q1 FY27"
model: claude-opus-4-8
status: complete
verdict: COMPLETE
coverage:
  orphan_rows: []
  missing_from_ledger: []
arithmetic_mismatches: []
surviving_bear_counters: []
loop_back_to: ""
gap: ""
```
