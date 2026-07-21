# A5 ADVERSARY / COMPLETENESS AUDIT — SOUTHWEST — Q1 FY27

Fresh context. Re-derived independently from A1 extracts and A2 ledgers only. A4's and A3's cites checked, not deferred to. All Rs Mn raw; conversion x0.1 to Rs Cr per A1 headers (results L8, presentation L8).

---

## AUDIT 1 — COVERAGE

Independent grep pass re-run over both extracts, diffed against the two A2 ledgers.

| Category | A2 count | My fresh count | Orphan rows | Status |
|---|---|---|---|---|
| Results: numbered notes | 0 | 0 (grep `^\s*[0-9]+\.\s` = 0; 4-page press release, not Reg 33) | — | PASS |
| Results: financial line items | 5 | 5 (results L86-90, grep confirmed) | — | PASS |
| Results: financial period cells | 20 | 20 (5 rows x 4 periods) | — | PASS |
| Results: Q1 highlight bullets | 13 | 13 (results L93-111, hand-swept) | — | PASS |
| Results: CMD commentary claims | 9 | 9 (results L115-148) | — | PASS |
| Results: JV/coal statements | 7 | 7 (cross-ref index over E/F/H) | — | PASS |
| Results: absent Reg-33 unit classes | 15 | 15 (K1-K15, each 0-hit grep) | — | PASS |
| Results: letterhead/cover/sig/about/safe-harbor/contact | 11 | 11 (A,B,C,H,I,J rows) | — | PASS |
| Presentation: slides | 40 | 40 (grep `\[page N\]` = 40) | — | PASS |
| Presentation: P&L line items (sl.33 + sl.35) | 32 | 32 (grep label-match = 32; 16+16) | — | PASS |
| Presentation: balance-sheet line items (sl.36) | 42 | 42 (22 assets + 20 equity/liab, hand-swept) | — | PASS |
| Presentation: capital-market table (sl.38) | 6 | 6 (L1199-1210) | — | PASS |
| Presentation: chart data points | 110 | 110 (8+8+6+11+25+6+12+32+2) | — | PASS |
| Presentation: footnotes | 7 | 7 (Table 7) | — | PASS |

**No row my fresh pass found is missing from either ledger. No count diverges from A2.** Gate A2 counts are reproducible and correct.

**Ledger-row → A4 disposition check** (every ledger row must be cited in A4 OR marked reviewed-no-finding). A4 preamble (review L9-19) asserts all 70 press-release rows and all 40 slides reviewed, and incorporates 25 A3 IDs. Spot-verified the flagged rows are individually dispositioned:
- `TITLE_LABEL_MISMATCH` (ledger B5/D0b, "Q on Q" vs "Y on Y") → A4 Step 3 F14-01 + Q14. Cited.
- E3 PBT% unreconciled → A4 Step 2 diagnostic ("PBT grows 8% to 19%"). Cited.
- F2 standalone claim ("on similar lines") → A4 First-Class Metric + Q4. Cited.
- Slide 6 Rs 307 cr HZL vs slide 32 Rs 3,070 Mn Rajasthan → A4 F16.2 double-count. Cited (A4 correctly raises "same order" concern despite ledger's "do not conflate" note — A4 is right to override).
- Slide 8 Ritolia caption/body `DISCLOSURE_INCONSISTENCY` → A4 F14.1 + Q15. Cited.
- Slide 37 `DATA_GAP` (no Q1 net-worth/D-E/ROE-ROCE) → A4 F16.1 + Q12. Cited.
- OCI `ZERO_STANDING` swing → A4 F9.1 + Q11. Cited.
- Current Tax Liability nil→56 Mn → A4 F1.2 + Q13. Cited.
- Held-for-sale asset → A4 F1.1. Cited.

**One immaterial row not individually dispositioned:** ledger J2 (results L157) flags a contact-phone digit-count mismatch (+91 124 423540 vs letterhead 4235402) "flagged for A3/A4." A4 does not name it. Judged an A1 extraction/truncation artifact, not a company-disclosure issue, and covered by A4's blanket "all 70 rows read." **Not an orphan FAIL** (immaterial, non-decision-relevant). Slide-9 map "14 states vs 8 States" cross-note similarly blanket-covered, immaterial.

**COVERAGE VERDICT: PASS.** No orphan rows, nothing missing from the ledgers.

---

## AUDIT 2 — ARITHMETIC

Every derived metric in A4's tables recomputed from raw slide-33/35/36 figures (Rs Mn). Representative and all load-bearing cells shown; all reconcile.

| Metric | A4 value | My recompute | Source line | Status |
|---|---|---|---|---|
| Total Income Q1FY27 (Rev+OI) | 62.1 | 61.7+0.4 = 62.1 | L1033,L1041 | OK |
| Op EBITDA margin Q1FY26 | 14.43% | 58/402 = 14.43% | L1035/33 | OK |
| Op EBITDA margin Q1FY27 | 24.15% | 149/617 = 24.15% | L1037/33 | OK |
| Reported EBITDA Q1FY27 (PBT+D+Fin) | 16.6 | 11.9+3.0+1.7 = 16.6 | L1051,43,45 | OK |
| Core Op PBT ex-OI Q1FY27 (PBT−OI) | 11.5 | 11.9−0.4 = 11.5 | L1051,41 | OK |
| Core Op PBT ex-OI ex-JV Q1FY27 | 10.2 | 10.6−0.4 = 10.2 | L1047,41 | OK |
| Effective Tax Rate Q1FY27 (Tax/PBT) | 21.8% | 26/119 = 21.85% | L1053/51 | OK |
| ETR pre-JV Q1FY27 (Tax/PBSJV) | 24.5% | 26/106 = 24.53% | L1053/47 | OK |
| Revenue YoY | +53.5% | (617−402)/402 = 53.48% | L1033 | OK |
| Op EBITDA YoY | +156.9% | (149−58)/58 = 156.9% | L1037 | OK |
| Op EBITDA margin bps YoY | +972 bps | 2415−1443 = 972 | L1039 | OK |
| Depreciation YoY | +42.9% | (30−21)/21 = 42.86% | L1043 | OK |
| Finance cost YoY | −15.0% | (17−20)/20 = −15.0% | L1045 | OK |
| Operating EBIT YoY | +221.6% | (11.9−3.7)/3.7 = 221.6% | der. L1037,43 | OK |
| Core Op PBT ex-OI YoY | +475% | (11.5−2.0)/2.0 = 475% | der. | OK |
| Core Op PBT ex-OI ex-JV YoY | +500% | (10.2−1.7)/1.7 = 500% | der. | OK |
| Reported PBT YoY | +283.9% | (119−31)/31 = 283.9% | L1051 | OK |
| PAT YoY | +287.5% | (93−24)/24 = 287.5% | L1055 | OK |
| PAT margin bps YoY | +910 bps | 1507−597 = 910 | L1057 | OK |
| EPS YoY | +287.3% | (3.06−0.79)/0.79 = 287.3% | L1063 | OK |
| PAT bridge: Op EBITDA delta | +9.1 | 14.9−5.8 = 9.1 | L1037 | OK |
| PAT bridge: = PBT change | +8.8 | 9.1−0.9+0.3−0.7+1.0 = 8.8; also 11.9−3.1 | L1051 | OK |
| PAT bridge: = reported PAT change | +6.9 | 8.8−1.9 = 6.9; also 9.3−2.4 | L1055 | OK |
| JV share of consolidated PAT | 14.0% | 13/93 = 13.98% | L1049/55 | OK |
| Receivable days FY25 (TR/Rev x365) | 154.5 | 763/1803 x365 = 154.5 | L1132/76 | OK |
| Receivable days FY26 | 175.0 | 1166/2430 x365 = 175.1 | L1132/76 | OK |
| Inventory days FY26 (Inv/TotExp) | 100.6 | 509/1847 x365 = 100.6 | L1129/78 | OK |
| Payable days FY26 (TP/TotExp) | 45.9 | 232/1847 x365 = 45.9 | L1133/78 | OK |
| Cash conv cycle FY26 | ~230 | 175.0+100.6−45.9 = 229.7 | der. | OK |
| Capex FY26 (PPE+CWIP) | 92.2 | 918+4 = 922 Mn | L1114-15 | OK |
| Cash & equiv FY25→FY26 | 19.4→1.3 (−93%) | 194→13 Mn, −93.3% | L1134 | OK |
| Gross borrowings FY26 (LT+ST) | 78.6 | 160+626 = 786 Mn | L1120/31 | OK |
| Net debt FY26 (gross−cash&equiv) | 77.3 | 78.6−1.3 = 77.3 | der. | OK |
| ROCE base (0.5xROCE+7.5) | 15.5x | 0.5x16+7.5 = 15.5 | L1170 (sl.37) | OK |

**Standalone-vs-consolidated PAT gap:** A4 records ND (both docs consolidated-only; results K5). Confirmed unrecoverable from today's extracts — correctly ND, not fabricated. JV-share-of-PAT (14.0%) is disclosed and A4 keeps it distinct from the S-vs-C gap. Correct handling.

**ARITHMETIC VERDICT: PASS.** Zero mismatches above rounding. Note (not a FAIL, no A4 table affected): the press-release body claim "PAT... more than 3.90 fold" (results L97) is a company overstatement — 93/24 = 3.875x — but A4 correctly used +287.5% throughout and did not import the 3.90 figure.

---

## AUDIT 3 — ADVERSARIAL READ

Three most positive A4 claims; strongest bear counter each, built only from the extracted text.

**Positive 1 — "Income-statement quality genuinely strong, PAT +287.5%, NOT treasury-led" (Step 2, Section C).**
Bear counter: growth is flattered by (a) an equity-accounted, possibly-unaudited JV (share of profit 3→13 Mn, now 14.0% of PAT) and (b) a low Q1FY26 margin base (14.43%), so the +972 bps is a base effect and margin is flat vs FY26 (23.99%).
Survives? **NO.** Refuted by the same extract: core PBT ex-OI **ex-JV** still +500% (10.2 vs 1.7), so JV is not propping the core; and A4 already states the margin matches full-FY26 (the low-base point is incorporated). Counter does not survive.

**Positive 2 — "Coal first-production target FY27-28 is EARLIER than the house FY29 tripwire" (Step 6, Section C).**
Bear counter: FY27-28 is an unverified management target in a promotional deck, and the enabling GR is "being finalised for its early submission" (L682) — not yet submitted; mining-plan approval and development all still pending.
Survives? **PARTIALLY, but already covered.** A4 carries the "binary GR-slip risk" (Step 6D), gates it (Q6) and monitorables it. The Section C phrasing states the positive without the "GR-not-yet-submitted" qualifier adjacent, but the substance is present elsewhere. Not a required graft.

**Positive 3 — "Order book at all-time high Rs 761 Cr, +31% QoQ" (Step 6, Section C, flags).**
Bear counter (built from extract): the order book grew only **Rs 180 Cr QoQ** (FY26 5,812 Mn → Q1FY27 7,613 Mn = +1,801 Mn, L535/542), yet the deck touts a "single largest order value of INR 3,070 Mn / Rs 307 Cr in Rajasthan" as this quarter's event (L1004). **A single Rs 307 Cr order exceeds the entire net QoQ book growth of Rs 180 Cr.** It therefore cannot be an incremental Q1 addition — it was already in the book (slide 6 "Journey So Far" 2024-25 records the Rs 307 crore Hindustan Zinc-subsidiary order, L151-155; HZL operates in Rajasthan), and Q1 merely "commences operations to execute" it. Cross-check reconciles: FY26 5,812 + this-quarter RIL CBM win 1,660 Mn (L1006) − ~62 Cr revenue burn ≈ 7,410, close to the 7,613 actual, WITHOUT the Rs 307 Cr being new. The "307 newly added" reading would instead require ~Rs 127 Cr of non-revenue book run-off in one quarter (on Rs 62 Cr revenue) — unevidenced and implausible.
Survives? **YES.** This is extract-supported and NOT stated in A4. It converts A4's hedged "Rajasthan order LIKELY equals the HZL award — double-count risk, unresolved, defer to management" into a near-resolved, arithmetic-backed finding: the touted Rs 307 Cr order is pre-booked, so crediting it as an incremental driver of the "all-time-high +31% QoQ" order book double-counts a previously-won order. This materially strengthens flag F16.2 and tempers the visibility-pillar positive. **Must be grafted into A4 before save.**

---

## VERDICT

**INCOMPLETE.** Loop back to **A4**.

- Coverage: PASS. Arithmetic: PASS (zero mismatches).
- Adversarial: one surviving bear counter (Positive 3) not present in A4.

**Exact gap:** A4 must graft the order-book arithmetic into the F16.2 double-count treatment (Step 6D, Section C caution, and the flags block): the QoQ order-book growth is only Rs 180 Cr (5,812→7,613 Mn), which is smaller than the single Rs 307 Cr / 3,070 Mn Rajasthan order the deck highlights; combined with slide 6 placing the Rs 307 crore HZL-subsidiary award in 2024-25, this is extract-level evidence that the Rs 307 Cr order is pre-booked and "commencing," NOT incremental Q1 intake. A4 should downgrade the "all-time-high order book" positive from an unqualified strength to one net of the pre-booked headline order, and state the double-count as extract-supported (near-resolved) rather than wholly deferred to the concall. Re-submit for A5 re-check after grafting.

---

```yaml
stage: A5-adversary
company: "SOUTHWEST"
quarter: "Q1 FY27"
model: claude-opus-4-8
status: complete
verdict: INCOMPLETE
coverage:
  orphan_rows: []
  missing_from_ledger: []
arithmetic_mismatches: []
surviving_bear_counters:
  - claim: "Order book at all-time high Rs 761 Cr, +31% QoQ (Step 6 / Section C positive)"
    counter: "Net QoQ order-book growth is only Rs 180 Cr (FY26 5,812 Mn -> Q1FY27 7,613 Mn), which is smaller than the single Rs 307 Cr / 3,070 Mn Rajasthan order the deck touts as this quarter's event. The order therefore is not incremental Q1 intake; slide 6 places the Rs 307 crore HZL-subsidiary award in 2024-25 and Q1 only 'commences operations' on it. This is extract-supported evidence the headline order is pre-booked, strengthening F16.2 double-count from 'defer to management' to near-resolved, and it tempers the all-time-high order-book positive."
    source_line: "presentation L535, L542, L546 (order book 5,812/7,613); L1004 (Rs 3,070 Mn Rajasthan); L151-155 (slide 6 Rs 307 crore HZL 2024-25); L1006 (RIL 1,660 Mn)"
loop_back_to: "A4"
gap: "A4 must graft the order-book arithmetic into its F16.2 double-count treatment: QoQ book growth (Rs 180 Cr) is less than the single Rs 307 Cr Rajasthan order the deck highlights, and slide 6 dates that Rs 307 crore HZL award to 2024-25 — so it is pre-booked, not incremental. Downgrade the all-time-high order-book positive to net-of-pre-booked-order and state the double-count as extract-supported rather than wholly deferred to the concall."
```
