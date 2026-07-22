# A5 ADVERSARY AUDIT — ADDENDUM (Reg 30 PRESS RELEASE) — Atlanta Electricals Ltd (ATLANTAELEC), Q1 FY27 — RE-AUDIT (loop 2 of 2)

Agent: A5 ADVERSARY | Model: claude-opus-4-8 | Date: 2026-07-22
Scope: RE-AUDIT (loop 2 of max 2) of `review_addendum_pressrelease_atlantaelec_q1fy27.md` after A4 corrected the single arithmetic error flagged in loop 1.
Fresh context: I re-derived from the A1 press-release extract, the A1 filing extract (verified spine, page-6 CONSOLIDATED block), and the A2 press-release ledger. I did not defer to A4's or A3's cites.

Prior INCOMPLETE gap (loop 1): addendum Q21 stated the sequential PAT drop as "−35%"; correct value 46.84/102.19 − 1 = −54.16%. This re-audit confirms the correction, then re-runs all three audits to confirm no regression.

---

## 0. FIX VERIFICATION (the single loop-1 gap)

| Location | Loop-1 value | Loop-2 value now on file | Correct value | Status |
|---|---|---|---|---|
| §5 Q21 prose (review L84) | "−35% sequential PAT drop (102.19→46.84)" | "**−54% sequential PAT drop (102.19→46.84)**" | 46.84/102.19 − 1 = −54.16% → −54% | **FIXED, CORRECT** |
| YAML Q21 (review L151) | (no %) | "PAT 102.19->46.84" (no % asserted) | consistent | OK |

No stray "−35%" token remains anywhere in the addendum. The −347 bps EBITDA-margin QoQ figure sitting beside it in the same sentence, and the 102.19→46.84 endpoints, are unchanged and independently re-verified below. Fix accepted.

---

## 1. COVERAGE AUDIT (fresh grep + line-by-line sweep vs A2 ledger)

Re-enumerated the press-release extract (156 lines, 3 pages) independently.

| Category | A2 ledger count | My fresh count | Orphan rows | Status |
|---|---|---|---|---|
| Cover-letter / Reg 30 transmittal (L16–35) | 9 | 9 | none | OK |
| Financial-highlights cells (L73–77, 5 rows × 4 cols) | 20 | 20 | none | OK |
| EBITDA footnote (L78) | 1 | 1 | none | OK |
| Headline banner claims (L63–65) | 5 | 5 | none | OK |
| Performance-Overview sub-claims (L84–94) | 10 | 10 | none | OK |
| Key-Business-Updates sub-claims (L97–118) | 18 | 18 | none | OK |
| Mgmt-commentary restated figures (L120–132) | 6 | 6 | none | OK |
| Forward-looking statements (L134–140) | 8 | 8 | none | OK |
| About-section rows (L142–146) | 6 rows (7.1–7.6) | 6 | none | OK (see note) |
| Signature/footer/contact (L39–56, L150–156) | 8 | 8 | none | OK |
| **TOTAL** | **91** | **91** | **none** | **PASS** |

Fresh cross-checks that reproduced the ledger: 8 raw bullets (3 Performance-Overview at L84/L88/L91 + 5 Key-Business-Updates at L97/L101/L105/L109/L115); 5 table rows × 4 period columns = 20 cells (L73–77); 1 asterisk footnote (L78); 3 management paragraphs (blank-line delimited L123–126 / L128–132 / L134–140). All reconcile.

Orphan check (every ledger row cited in A4 OR marked reviewed-no-finding): PASS. A4 states all 91 rows reviewed at cited line numbers (review L14). Material rows are explicitly cited: highlights cells → §1A; RRVPNL order (4.7–4.10 / 5.8–5.11) → N4/§4; order book + inflow (5.1–5.3) → §3 item 1 / Q19; EHV split (5.6–5.7) → N2/N3/§3 item 2 / Q20; 400/765 kV status + IDT + backward-integration (5.13/5.14/5.16/5.17/5.18) + FLS (6.7–6.14) → A3-F6-1 discharged into existing Q3/Q4/Q6/Q7 + monitorables; About cumulative (7.5/7.6) → N5. Boilerplate rows (cover letter, product range 7.1, facilities 7.3, 30-years 7.4, signature/contact) are covered by the blanket reviewed-no-finding statement. No orphan.

Missing-from-ledger check (rows my fresh pass found that the ledger lacks): none. PASS.

NOTE (immaterial, not a FAIL, unchanged from loop 1): A4's prose in review L14 describes "5 About-section claims," and the A2 COUNT TEST reports `about_section_claims: 5` (excluding qualitative row 7.2), so A4's L14 prose components sum to 90 while correctly asserting the 91 total; the ledger's own grand-total row-enumeration counts Table 7 as 6 rows (7.1–7.6) to reach 91. This is a cosmetic prose/count-test inconsistency internal to A2/A4; it creates no orphan row (7.2 is boilerplate product-list, reviewed-no-finding) and did not gate loop 1. Logged as observation only. Coverage verdict PASS.

---

## 2. ARITHMETIC AUDIT (recomputed from raw filing-spine numbers)

Raw inputs from `extract_results_atlantaelec_q1fy27.txt`, CON block: L258 (Revenue), L267 (Finance Cost), L268 (Depreciation), L270 (Total Expenses), L284 (Net Profit). EBITDA ex-OI = Revenue from Operations − (Total Expenses − Depreciation − Finance Cost).

| Metric | A4 / press-release value | My recompute | Source lines | Status |
|---|---|---|---|---|
| CON Q1FY27 Revenue tie | 466.33 | 466.33 | filing L258 = PR L73 | EXACT |
| CON Q4FY26 Revenue (under "Q4FY25" hdr) | 747.62 | 747.62 | filing L258 = PR L73 | EXACT (label wrong, value right) |
| CON Q1FY26 Revenue | 315.11 | 315.11 | filing L258 = PR L73 | EXACT |
| CON Q1FY27 EBITDA ex-OI | 77.10 / 16.5% | 466.33−(405.07−10.13−5.71)=77.10; 77.10/466.33=16.53% | filing L258,270,268,267 | EXACT (rounds) |
| CON Q4FY26 EBITDA ex-OI | 149.56 / 20.0% | 747.62−(623.30−9.27−15.97)=149.56; /747.62=20.00% | filing L258,270,268,267 | EXACT |
| CON Q1FY26 EBITDA ex-OI | 48.78 / 15.5% | 315.11−(275.55−2.35−6.87)=48.78; /315.11=15.48% | filing L258,270,268,267 | EXACT (rounds) |
| SA Q1FY27 EBITDA margin | 16.63% | 466.33−(400.28−5.76−5.74)=77.55; /466.33=16.63% | filing L258,270,268,267 | EXACT |
| CON Q1FY27 PAT / margin | 46.84 / 10.0% | 46.84; 46.84/466.33=10.04% | filing L284 | EXACT |
| CON Q4FY26 PAT / margin | 102.19 / 13.7% | 102.19; /747.62=13.67% | filing L284 | EXACT |
| CON Q1FY26 PAT / margin | 31.14 / 9.9% | 31.14; /315.11=9.88% | filing L284 | EXACT |
| YoY Revenue | 48.0% | 466.33/315.11−1=47.99% | PR L73 | EXACT |
| YoY EBITDA | 58.1% | 77.10/48.78−1=58.06% | PR L74 | EXACT |
| YoY PAT | 50.4% | 46.84/31.14−1=50.42% | PR L76 | EXACT |
| YoY EBITDA-margin bps | +105 bps | 16.53−15.48=+1.05% | PR L75 | EXACT |
| YoY PAT-margin bps | +16 bps | 10.04−9.88=+0.16% | PR L77 | EXACT |
| **QoQ PAT (Q21 — the fix)** | **−54%** | **46.84/102.19−1=−54.16%** | filing L284 | **EXACT — FIX CONFIRMED** |
| QoQ EBITDA-margin (Q21 / §3 item 3) | −347 bps | 16.5336−20.0048=−3.4712% | filing L258,270,268,267 | EXACT (−347.1 bps) |
| OB roll-forward gap (Q19) | ~117 cr | 3,116.63/1.25=2,493.30; +972.42−466.33=2,999.39; 3,116.63−2,999.39=117.24 | PR L97–98 | EXACT (~117) |
| 400 kV share of book (N3/Q20) | ~8.8% | 275/3,116.63=8.82% | PR L103–104 | EXACT |
| RRVPNL MVA total (N4) | 4,168 MVA | 4×160+63×50+12×31.5=640+3,150+378=4,168 | PR L92–93 | EXACT |
| RRVPNL unit total (N4) | 79 units | 4+63+12=79 | PR L92–93 | EXACT |
| Inflow vs green-band top (§3 item 1 / §6) | ~40% above / 1.39x | 972.42/700=1.389 | PR L97–98 | EXACT |

No mismatch above rounding anywhere. Every derived metric re-derives from the verified spine. The CON-vs-SA PAT gap (46.84 vs 53.09, −6.25, driven by higher CON depreciation 10.13 vs SA 5.76 and subsidiary PAT of −4.40 per filing L225/L268/L284) is spine-consistent and undisturbed by the addendum. ARITHMETIC PASS.

---

## 3. ADVERSARIAL READ (three most positive claims, strongest bear counter from same text)

| # | A4's positive claim | Strongest bear counter (from the extract) | Survives? | Already grafted in A4? |
|---|---|---|---|---|
| 1 | Order inflow ₹972.42 cr, ~40% above the ₹600–700 cr green band → item 1 fully GREEN (review §3 item 1, PR L97–98) | Closing book does not tie: 2,493.30 + 972.42 − 466.33 = 2,999.39 vs stated 3,116.63, a ~₹117 cr unreconciled delta; order-book definition (gross/net of GST, executed/pending) undisclosed — so "green-band-beating inflow" rests on numbers that do not foot | Valid, but ALREADY grafted: §3 item 1 residual, Q19 (L82), flag "order-book roll-forward ~117cr unreconciled", monitorable (b) | YES — no new graft |
| 2 | RVPN (cascade-watch utility) is a ₹291.68 cr paying CUSTOMER → lowers 2nd-utility-debarment probability (review §4, PR L91–94) | SBPDCL / South Bihar debarment silent across all three same-day documents; RVPN and SBPDCL are separate utilities, so one order cannot down-weight the live SBPDCL cascade; RVPN order terms (type-test/PBG, pending pre-qual) undisclosed, possibly conditional | Valid, but ALREADY grafted: §4 ("No comfort is taken from the RVPN positive on the SBPDCL question"), item 8 UNKNOWN, tripwire ACTIVE, Q22 (L85) | YES — no new graft |
| 3 | EHV quantified first time: 400 kV+reactors ≈₹275 cr (≈8.8% of book), 220 kV >55% → item 2 partially quantified (review §3 item 2, PR L103–104) | These are ORDER-BOOK figures; item 2 is a REVENUE metric (≥10% revenue share by FY27 H2), not met; "nearly ₹275 cr" is approximate/possibly-gross; no 400 kV deliveries confirmed; item does not flip GREEN | Valid, but ALREADY grafted: §3 item 2 ("REVENUE share still UNKNOWN"), Q20 (L83), monitorable (a) | YES — no new graft |

Additional bear angle checked: headline touts YoY +48%/+58%/+50%/+105 bps while the sole non-YoY column is a mislabelled "Q4FY25" and no QoQ P&L column appears, masking −37.6% QoQ revenue, −54% QoQ PAT, −347 bps QoQ margin into the first sub-17% margin quarter. Already grafted (§3 item 3 AMBER, Q21, flags). No surviving bear counter requires new incorporation into A4.

---

## 4. CROSS-CHECK OF TASK CONFIRMATIONS

- Q21 now reads −54% (not −35%): CONFIRMED (review L84).
- Highlights table ties to verified spine: CONFIRMED (§2, all EXACT).
- "Q4FY25"-labelled column equals verified Q4 FY26 CON figures: CONFIRMED (747.62 / 149.56 / 20.0% / 102.19 / 13.7% all = filing Q4 FY26 CON; header label wrong, values right; A4 flags cosmetic).
- Order-book roll-forward ~117 gap recomputes: CONFIRMED (117.24).
- 400 kV ~275cr = ~8.8% of 3,116.63: CONFIRMED (8.82%).
- No Decision Status upgrade: CONFIRMED (WATCHLIST / BUY ON DIPS unchanged; review L8/L101, YAML decision_status_changed:false).
- SBPDCL still an active tripwire: CONFIRMED (review §4, YAML signals).
- Verdict stays PROCEED WITH FLAGS: CONFIRMED (review §6, YAML protocol_verdict).

No regression introduced by the Q21 correction. The fix was surgical: only the single token changed; all surrounding figures (−347 bps, the 102.19→46.84 endpoints, and the YAML) remain internally consistent.

---

## VERDICT

**COMPLETE.** The loop-1 arithmetic gap (Q21 −35% → −54%) is corrected and independently confirmed at −54.16%. Coverage re-enumeration reproduces the A2 ledger at 91/91 with zero orphan and zero missing rows. Every derived metric re-derives from the verified filing spine with no mismatch above rounding. All three most-positive claims already carry their surviving bear counters in the review, so no counter requires new grafting. No FAIL, no loop-back. This addendum may proceed to Notion save.

```yaml
stage: A5-adversary
company: "atlantaelec"
quarter: "q1fy27"
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
