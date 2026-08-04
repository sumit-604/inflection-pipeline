# A5 ADVERSARY / COMPLETENESS AUDIT — R SYSTEMS INTERNATIONAL (RSYSTEMS) Q2 CY2026
Model: claude-opus-4-8 | Fresh context: A4 review + A1 extracts (results, presentation) + A2 ledgers only.
Unit convention re-derived independently: filing in Rs Millions; Rs Cr = mn x 0.1. All my figures computed from mn.

---

## AUDIT 0 — DELIVERABLE-COMPLETENESS (hard gate, run first)

The A4 review carries a Section F "PLAIN-LANGUAGE BRIEF" with all four labelled parts present and non-empty:

| Part | Heading present | Location | Content real (not placeholder) | Status |
|---|---|---|---|---|
| 1. Summary narrative (10-20 lines) | yes | review L559-560 | yes — full ~18-line narrative | PRESENT |
| 2. SECTOR intelligence | yes | review L562-567 | yes — industry, tailwind, FX, vertical mix, gaps | PRESENT |
| 3. BUSINESS-MODEL intelligence | yes | review L569-573 | yes — revenue engine, unit economics, model drift, balance sheet | PRESENT |
| 4. COMPETITION intelligence | yes | review L575-579 | yes — where it wins/loses, risk-to-watch, peer cross-check | PRESENT |

**Gate 0 result: PASS.** No missing or empty brief part.

---

## AUDIT 1 — COVERAGE (independent re-enumeration vs A2 ledgers)

Fresh grep/sweep over both extracts, diffed against the two ledgers.

| Category | A2 count | My fresh count | Orphan rows (in ledger, absent from A4) | Rows I found ledger lacks | Status |
|---|---|---|---|---|---|
| agenda_items (results) | 8 | 8 (3 top-level L36/38/40 + 5 sub 3a-3e L42-60) | none | none | MATCH |
| notes (results) | 31 | 31 (consol main 9 + consol ratio-notes 3 + SA main 10 + SA ratio-notes 3 + 6 unnumbered) | none | none | MATCH |
| line_items (results, 10 tables) | 281 | 281 (146 consol side + 135 SA side; per-table verified) | none | none | MATCH |
| zero_standing (results) | 6 | 6 (2 NCI attrib rows, 2 Debenture-RR, 2 Inventory-turnover NA) | none | none | MATCH |
| auditor_paras (results) | 27 | 27 (10 consol review L549-645 + 17 SA audit L1247-1407) | none | none | MATCH |
| entities (results) | 31 | 31 (L660-731, ends "31. Novigo Solutions B.V.") | none | none | MATCH |
| signature_blocks (results) | 15 | 15 (reconciled at ledger detail; OCR-garbled MD blocks confirmed) | none | none | MATCH |
| presentation gated rows | 189 (18 cats) | 189 | none | none | MATCH |
| presentation zero_standing | 1 (Assets held for sale L385) | 1 | none | none | MATCH |
| concall turns/slides | 0 / 0 | 0 / 0 (no transcript supplied; concall ~12 Aug 2026 not held) | n/a | n/a | MATCH |

Ledger-flagged items are all addressed by A4: NCI zero-standing → Q7 ("static Rs 192.39 Cr NCI, zero P&L attribution"); Novigo ENTITY_CHANGE (#27-31) → Step 5N + Q11; Velotio/Scaleworx amalgamation → Note-3 restatement handling (Step 0D, 5S); OCRPS "Instrument entirely equity" line → Step 0C + Q6. The blanket "all reviewed at cited lines" (review L16-21) covers the trivial nil ratios (Debenture-RR, Inventory-turnover, Assets-held-for-sale).

**Coverage result: PASS.** orphan_rows = none; missing_from_ledger = none. No loop-back to A2 or A3 on coverage.

---

## AUDIT 2 — ARITHMETIC (recomputed from raw mn; do NOT trust A4's cites)

### 2a. Reproductions that CHECK OUT (representative; all reconcile within rounding)

| Metric | A4 value | My recompute (from mn) | Source lines | Status |
|---|---|---|---|---|
| Revenue YoY Q2 | +30.2% | 6017.01/4620.15−1 = +30.23% | L115 | OK |
| Op EBITDA Q2 CY26 | 110.66 | (805.07+220.39+94.77−13.68)/10 = 110.66 | L130/121/120/116 | OK |
| Op EBITDA margin Q2 CY26 | 18.39% | 110.66/601.70 = 18.39% | — | OK |
| Op EBITDA margin +bps YoY | +320 bps | 18.39%−15.19% = 320 bps | — | OK |
| Core PBT ex-OI Q2 CY26 | 79.14 | (805.07−13.68)/10 = 79.14 | L130/116 | OK |
| Core PBT ex-OI YoY | +51.6% | 79.14/52.22−1 = +51.55% | — | OK |
| Finance cost YoY Q2 | +342.7% | 94.77/21.41−1 = +342.7% | L120 | OK |
| Reported PAT YoY Q2 | −26.7% | 555.70/758.54−1 = −26.74% | L135 | OK |
| ETR Q2 CY26 consol | 30.98% | 249.37/805.07 = 30.98% | L134/130 | OK |
| PAT bridge total | −20.28 | Σ(+41.01−1.37−6.20−7.34−2.23−42.55−1.61) = −20.29 | L275-292 | OK (rounding) |
| Non-recurring swing | −42.55 | (−16.17−409.36)/10 = −42.55 | L286 | OK |
| Adj PAT YoY Q2 | +35.4% | 628.74/464.38−1 = +35.4% | L296 | OK |
| CFO/PAT H1 CY26 | 1.35x | 1632.58/1209.84 = 1.35x | L448/135 | OK |
| CFO/PAT ex-receivables | ~0.93x | (1632.58−511.92)/1209.84 = 0.93x | L448/442 | OK |
| Capex H1 CY26 | 15.07 | (130.31+20.39)/10 = 15.07 | L450/451 | OK |
| Net cash excl lease | +63.12 | 333.97−270.85 = 63.12 | L363+364 / L384+392 | OK |
| Net debt incl lease | +35.36 | 270.85+98.48−333.97 = 35.36 | L385/393 | OK |
| S-vs-C gap Q2 CY26 | +19.76 / +55.2% | (555.70−358.09)/10 = 19.76; /35.809 = 55.2% | L135/784 | OK |
| S-vs-C gap swing Q1→Q2 | +51 pp | 55.2−4.0 = 51.2 pp | — | OK |
| SA other-exp QoQ | +94% / +27.56 | 569.27/293.63−1 = +93.9%; Δ 27.56 Cr | L772 | OK |
| SA Op EBITDA margin Q2 | 21.36% | 73.16/342.54 = 21.36% | L779/771/770/765 | OK |
| Consol ISCR / SA ISCR / SA DSCR | 9.35 / 6.52 / 5.43 | L280 / L938 / L932 verbatim | — | OK |
| Utilisation blended YoY | −151 bps | 81.13−82.64 = −151 bps | L483 | OK |
| IT-seg margin QoQ | 16.16→12.65% (−351 bps) | 841.72/5208.13; 687.84/5437.01 | L510/503 | OK |
| Unreviewed subs % of PAT | 20.6% | 114.58/555.70 = 20.6% | L595/135 | OK |
| USD/INR implied | ~94.7 | 6017.01/63.56 = 94.66 | L273 | OK |
| OCRPS share count | 5,160,833 = 5.16 mn | Note 3 L205 verbatim; face value Rs 5.16 mn to equity; valued Rs 2,407.00 mn | L205-210 | OK |

### 2b. MISMATCHES ABOVE ROUNDING — FAIL (loop to A4)

**FAIL-1 — Reported EBITDA H1 CY25 (Step 1C consol table, review L123-124).**
- A4 value: Reported EBITDA H1 CY25 = **174.99**; margin = **19.35%**.
- Recomputed (A4's own definition PBT + D + FC): 1559.11 + 304.44 + 36.31 = 1899.86 mn = **189.99 Cr**; margin = 189.99/904.48 = **21.00%**.
- Source lines: PBT L124/130 (1559.11), D&A L121 (304.44), Finance costs L120 (36.31), Revenue L115 (9044.80).
- Discrepancy: **14.99 Cr (~8%)** on the value; **165 bps** on the margin. Cross-check: A4's own Operating EBITDA H1 CY25 (140.74) + Other Income (49.25) = 189.99, confirming 174.99 is wrong. The other five columns of this row (117.17 / 120.73 / 112.02 / 232.76) all reproduce correctly — only the H1 CY25 column is in error.
- Materiality: this is the row A4 explicitly de-emphasises (asterisked as NOIDA-inflated; operating EBITDA is the anchor), so no thesis conclusion turns on it. But it is a derived metric in an A4 table and the mismatch is far above rounding. **FAIL → A4.**

**FAIL-2 — Working-capital change H1 CY26 (Step 5 table + mandatory answer, review L234, L250).**
- A4 value: H1 CY26 WC change = **"+Rs 23.61 net"** (a release); mandatory answer states **"No drag — WC released cash this half."**
- Recomputed net WC movement (consol CF): Operating profit before WC 2248.17 → Cash generated from operations 2065.14 = **−183.03 mn = −18.30 Cr (a USE, not a release).** Line detail: receivables +511.92, other assets −475.83, provisions −175.28, payables −43.84 = −183.03 mn.
- Source lines: L440 (2248.17), L442-445 (WC lines), L446 (2065.14).
- Discrepancy: A4 shows a +23.61 Cr release; the filing shows a −18.30 Cr use — **wrong sign and magnitude (~42 Cr apart).** The receivables release (+51.19 Cr, correctly cited) is substantially offset by an unexplained "other assets" build of Rs 47.58 Cr (475.83 mn) plus a provisions decrease of Rs 17.53 Cr. **FAIL → A4.**
- Consequence: the CFO/PAT 1.35x metric itself is correct and the STRUCTURAL/FIRING classification can survive on non-cash addbacks (D&A 43.55, ESOP 12.65, interest 19.07), but A4's supporting claim "WC released cash / no drag" is contradicted by the cash flow statement and must be corrected. (See surviving bear counter #2 below.)

*(H1 CY25 WC change A4 −66.31 vs my −66.35 mn-summed = within rounding, not flagged.)*

---

## AUDIT 3 — ADVERSARIAL READ (three most-positive claims + strongest bear counter)

**Positive claim 1 — "Core operating PBT +51.6% YoY; the −26.7% reported-PAT print is a base-effect illusion."** (Step 2, L157/165/170)
- Bear counter (from same text): the +51.6% core PBT and +30.2% revenue are undecomposed — Novigo is in the Q2 CY26 base but not the Q2 CY25 base (consolidated 13-Nov-2025, L722), and INR growth exceeds US$ growth by 12.5 pp (FX). Organic constant-currency growth is disclosed nowhere (L163). So "core operations grew >50%" is inorganic + FX-levered, and below the core line the same Novigo drives D&A +39.1% and finance +342.7% that turn the print negative.
- Survives? **Already incorporated** — A4 flags organic-undetermined (Flag 3), Novigo-blended (Step 5N), and the D&A/finance drag (Step 4). No graft required.

**Positive claim 2 — "Cash conversion STRUCTURAL / FIRING at 1.35x, above the top band; no WC drag."** (Step 5, L231/249-250)
- Bear counter (from same text): the 1.35x rests on non-cash addbacks plus a Rs 51.19 Cr trade-receivables release that is **offset by a Rs 47.58 Cr build in "other assets" and a Rs 17.53 Cr provisions drawdown**, so net working capital was a **Rs 18.30 Cr use**, not a release. Ex the receivables timing item, CFO/PAT is ~0.93x. The H1 CY25 comparison base (0.52x) was itself depressed, exaggerating the +0.83x "improvement."
- Survives? **YES, and it is NOT incorporated** — A4 asserts the opposite ("WC released cash this half; no drag") on the strength of the mis-signed +23.61 figure (FAIL-2). **Must be grafted into A4:** correct the WC-change sign, note the offsetting other-assets build, and qualify "no drag." This ties to FAIL-2.

**Positive claim 3 — "Operating EBITDA margin expanded +320 bps YoY; margin genuinely expanded (management adj. EBITDA 20.1%)."** (Step 2, L152/164)
- Bear counter (from same text): the CFO attributes the margin to "improved utilisation," yet blended utilisation FELL 151 bps YoY (82.64% → 81.13%, L483); the gain is mix/leverage, and the IT-services segment margin actually compressed QoQ 16.16% → 12.65% (L510/503) as revenue grew — consistent with lower-margin inorganic (Novigo) mix diluting the segment even as the adjusted headline holds.
- Survives? **Already incorporated** — A4 flags the utilisation contradiction (Flag 5, Step 7 7A) and the IT-seg compression (F12-a, Q2). No graft required.

**Net adversarial finding:** one surviving counter (claim 2, cash/working-capital) is NOT in A4 and contradicts an A4 assertion; it must be grafted. It is the same defect as FAIL-2.

---

## OTHER FAVOURABLE-RESOLUTION / STEP-5-MONITOR SPOT CHECKS

- **OCRPS unit correction is itself CORRECT.** Filing Note 3 (L205-210, L852-858): "5,160,833 OCRPS of face value Re. 1 each ... valued at Rs. 2,407.00 million ... Rs. 5.16 million transferred to Instruments entirely equity in nature." 5,160,833 = 5.16 **million** shares (not 5.16 crore); Reg 52(4) ratio row (d) confirms "Outstanding redeemable preference shares (Rs. in million) 5.16" (L283/L944). A4's correction of the Notion "5.16 Cr" (a ~100x overstatement) and its ~4.4% dilution sizing (5.16/118.49) are both right. No fault.
- **Monitors marked answered vs unanswered:** A4 does NOT over-claim resolution. Items 1 (organic CC), 2 (ACV), 3 (Novigo revenue), 6 (fixed-price mix), 9 (ROCE) are all left UNKNOWN/RED/silence — correct, the filing genuinely does not answer them. Item 4 (adj EBITDA margin GREEN 20.07%/20.10%), item 5 (USD/INR), item 7 (debtor turnover 1.47x) and item 8 (coverage) are answered by the filing and reproduce. No monitor is falsely marked answered.
- **NCI zero-P&L-attribution catch is valid:** consol P&L attributes nil profit to NCI in every period (L159-161) while the balance sheet carries Rs 192.39 Cr NCI equity (L378) — A4 correctly routes this to Q7 rather than resolving it favourably.

---

## VERDICT

**INCOMPLETE.**

- Gate 0 (deliverable): PASS.
- Audit 1 (coverage): PASS — no orphan rows, no missing enumeration.
- Audit 2 (arithmetic): **FAIL x2** — (FAIL-1) Reported EBITDA H1 CY25 stated 174.99 / 19.35% vs correct 189.99 / 21.00%; (FAIL-2) H1 CY26 working-capital change stated "+23.61 release / no drag" vs correct −18.30 Cr use.
- Audit 3 (adversarial): one surviving bear counter (cash/working-capital) not incorporated; must be grafted (same defect as FAIL-2).

**loop_back_to: A4.**

**Gap:** A4 must (1) correct Reported EBITDA H1 CY25 to 189.99 Cr and its margin to 21.00% (Step 1C consol table); (2) correct the H1 CY26 net working-capital change from "+Rs 23.61 net / WC released cash / no drag" to a net USE of ~Rs 18.30 Cr, disclose the offsetting Rs 47.58 Cr "other assets" build against the Rs 51.19 Cr receivables release, and graft the surviving bear counter that the 1.35x cash conversion rests on non-cash addbacks plus a receivables timing item rather than a genuine WC release. Only after these corrections may the review proceed to Notion save.

**Output written to:** `/home/user/inflection-pipeline/runs/rsystems-q2cy26/work/audit_rsystems_q2cy26.md`

```yaml
stage: A5-adversary
company: "RSYSTEMS"
quarter: "Q2CY2026"
model: claude-opus-4-8
status: complete
verdict: INCOMPLETE
plain_language_brief:
  narrative: present
  sector: present
  business_model: present
  competition: present
coverage:
  orphan_rows: []
  missing_from_ledger: []
arithmetic_mismatches:
  - {metric: "Reported EBITDA H1 CY25 (Step 1C consol)", a4_value: "174.99 Cr (margin 19.35%)", recomputed: "189.99 Cr (margin 21.00%)", source_line: "L124/130 PBT 1559.11 + L121 D&A 304.44 + L120 FC 36.31; Rev L115 9044.80"}
  - {metric: "Working-capital change H1 CY26 (Step 5)", a4_value: "+23.61 Cr net release / 'no drag, WC released cash'", recomputed: "-18.30 Cr net use (2065.14 - 2248.17)", source_line: "L440 2248.17; L442-445; L446 2065.14"}
surviving_bear_counters:
  - {claim: "Cash conversion STRUCTURAL/FIRING at 1.35x with no working-capital drag (Step 5)", counter: "Net WC was a Rs 18.30 Cr USE; the Rs 51.19 Cr receivables release is offset by a Rs 47.58 Cr other-assets build and Rs 17.53 Cr provisions drawdown; ex the receivables timing item CFO/PAT is ~0.93x and the H1 CY25 base (0.52x) was depressed", source_line: "L440/442/443/444/446/448"}
loop_back_to: "A4"
gap: "A4 arithmetic: (1) Reported EBITDA H1 CY25 174.99/19.35% must be 189.99/21.00%; (2) H1 CY26 WC change +23.61 release must be -18.30 use, disclose offsetting Rs 47.58 Cr other-assets build vs Rs 51.19 Cr receivables release, and graft the surviving cash-conversion bear counter."
```
