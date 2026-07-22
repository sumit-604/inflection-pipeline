# A5 ADVERSARY / COMPLETENESS AUDIT — ADDENDUM (Reg 30 PRESS RELEASE) — Atlanta Electricals Ltd (ATLANTAELEC), Q1 FY27

Agent: A5 ADVERSARY | Model: claude-opus-4-8 | Date: 2026-07-22
Scope: audits `review_addendum_pressrelease_atlantaelec_q1fy27.md` (A4) against the press-release A1 extract, the press-release A2 ledger, and the verified filing spine (`extract_results_atlantaelec_q1fy27.txt`, page 6 CONSOLIDATED). Fresh context; all cites re-derived independently. Base review treated as already-COMPLETE cross-reference only.

Verdict headline: **INCOMPLETE — loop back to A4.** One arithmetic error above rounding in the addendum's own derived metric (QoQ PAT drop). Coverage and adversarial audits otherwise pass. Detail below.

---

## 1. COVERAGE AUDIT

Fresh enumeration of the extract (156 lines, 3 pages) reproduced independently and diffed against the A2 ledger (91 units).

| Category | A2 count | My fresh count | Orphan rows | Status |
|---|---|---|---|---|
| Cover-letter / Reg 30 transmittal (L16–35) | 9 | 9 | none | PASS |
| Highlights table cells (5 rows × 4 cols, L73–77) | 20 | 20 | none | PASS |
| Highlights footnote (*ex-OI, L78) | 1 | 1 | none | PASS |
| Headline banner claims (L63–65) | 5 | 5 | none | PASS |
| Performance-Overview sub-claims (L84–94) | 10 | 10 | none | PASS |
| Key-Business-Updates sub-claims (L97–118) | 18 | 18 | none | PASS |
| Mgmt-commentary restated figures (L120–132) | 6 | 6 | none | PASS |
| Forward-looking statements (L134–140) | 8 | 8 | none | PASS |
| About-section claims (L142–146) | 6 (Table 7) | 6 | none | PASS (see note) |
| Signature / footer / contact (L39–56, L150–156) | 8 | 8 | none | PASS |
| **Total** | **91** | **91** | **none** | **PASS** |

Structural cross-checks that confirmed the enumeration: 8 raw bullets (3 Performance-Overview + 5 Key-Business-Updates, `•` sweep on L84/88/91/97/101/105/109/115); 3 mgmt-commentary paragraphs (L123–126, L128–132, L134–140); single Reg 30 agenda item (L32–33), no AGM/dividend/director/auditor/ESOP/capital-raise resolution present (absence-swept, zero hits); 1 footnote only (no numbered notes section). My fresh pass finds **nothing the ledger lacks** and **no ledger row absent from the addendum**.

Row-level disposition of the substantive (non-boilerplate) rows in the addendum:
- Highlights table + footnote (2.1–2.6) → §1A tie table + EBITDA-definition note. Covered.
- Headline banner incl. ROUNDING_VARIANCE 3.5 (₹3,117 vs ₹3,116.63) → order-book value carried at 3,116.63 throughout; the 0.37cr headline rounding is immaterial and dispositioned under the blanket review statement. Covered.
- Inflow 972.42 (5.3) → N1 / §3 item 1 / §6. Covered.
- 220 kV >55% (5.6), 400 kV ~275cr (5.7) → N2/N3 / §3 item 2 / Q20. Covered.
- RRVPNL 291.68cr order + unit breakdown (4.7–4.10, 5.8–5.11 REPEAT_DISCLOSURE) → N4 / §4 / Q22. Covered.
- PGCIL / 400 kV / 765 kV status claims (5.12–5.14) → §3 item 2 / Q20. Covered.
- Scale-up / IDT / backward-integration status claims (5.16–5.18) + all 8 FLS (6.7–6.14) → A3-F6-1 (8 undated commitments) discharged into existing Q3/Q4/Q6/Q7 + monitorables. Covered.
- About cumulative supply 4,800+/1,16,000+ MVA (7.5–7.6, STALE_DATE) → N5. Covered.
- Cover-letter / signature / contact boilerplate → dispositioned as non-material transmittal context under the blanket "all 91 reviewed" statement (addendum L14).

**Coverage nit (non-fatal, no orphan created).** The addendum's §1 preamble narrative breakdown (L14) lists "5 About-section claims" and sums to 90, while it correctly declares the total as 91; the ledger itself carries the same 5-vs-6 About internal inconsistency (count-test row says 5 excluding qualitative 7.2; grand-total line L199 uses 6). Both agree on the affirmed total 91, and About row 7.2 (qualitative product list, L143–144) is dispositioned as boilerplate. No substantive ledger row is orphaned. Logged as an observation, not a coverage FAIL. All 9 A3 press-release findings (F6-1, F14-1/-2, F16-1…-6) are accounted for and mapped to Section-8/§4/Q19–Q22.

**COVERAGE AUDIT: PASS. No orphan rows; nothing missing from the ledger.**

---

## 2. ARITHMETIC AUDIT

Every press-release figure re-run against the verified page-6 CONSOLIDATED spine (SA figures shown where the addendum cites them).

| # | Metric | A4 / PR value | My recompute | Source line | Status |
|---|---|---|---|---|---|
| A | Revenue Q1FY27 | 466.33 | CON Rev 466.33 | extract_results L258 | TIE |
| B | EBITDA* Q1FY27 (ex-OI) | 77.10 | 466.33 − (405.07−5.71−10.13) = 466.33 − 389.23 = 77.10 | L258, L266–270 | TIE |
| C | EBITDA% Q1FY27 | 16.5% | 77.10/466.33 = 16.534% | — | TIE (rounds) |
| D | PAT Q1FY27 | 46.84 | CON Net Profit 46.84 | L284 | TIE |
| E | PAT% Q1FY27 | 10.0% | 46.84/466.33 = 10.045% | — | TIE (rounds) |
| F | Revenue Q1FY26 | 315.11 | CON 315.11 | L258 | TIE |
| G | EBITDA Q1FY26 | 48.78 | 315.11 − (275.55−6.87−2.35) = 315.11 − 266.33 = 48.78 | L258, L270 | TIE |
| H | EBITDA% Q1FY26 | 15.5% | 48.78/315.11 = 15.48% | — | TIE |
| I | PAT Q1FY26 | 31.14 | CON 31.14 | L284 | TIE |
| J | YoY Revenue | 48.0% | 466.33/315.11−1 = 47.99% | — | TIE |
| K | YoY EBITDA | 58.1% | 77.10/48.78−1 = 58.06% | — | TIE |
| L | YoY EBITDA margin | +105 bps | 16.534 − 15.48 = +105 bps | — | TIE |
| M | YoY PAT | 50.4% | 46.84/31.14−1 = 50.42% | — | TIE |
| N | YoY PAT margin | +16 bps | 10.045 − 9.88 = +16 bps | — | TIE |
| O | Col-4 "Q4FY25" Revenue 747.62 | = Q4FY26 CON | CON-Q4FY26 Rev 747.62 (SA = 747.43; PR uses CON) | L258 | TIE — value is Q4 **FY26** consol; header label wrong (addendum flags this correctly) |
| P | Col-4 EBITDA 149.56 / 20.0% | = Q4FY26 CON | 747.62 − (623.30−15.97−9.27) = 747.62 − 598.06 = 149.56; /747.62 = 20.005% | L258, L270 | TIE |
| Q | Col-4 PAT 102.19 / 13.7% | = Q4FY26 CON | CON-Q4FY26 Net Profit 102.19; /747.62 = 13.67% | L284 | TIE |
| R | SA Q1FY27 margin | 16.63% | 466.33 − (400.28−5.74−5.76) = 466.33 − 388.78 = 77.55; /466.33 = 16.63% | L258, L270 | TIE |
| S | Order-book roll-forward gap | ~117 | 3,116.63/1.25 = 2,493.30; 2,493.30 + 972.42 − 466.33 = 2,999.39; 3,116.63 − 2,999.39 = 117.24 | PR L97–98 vs L73 | TIE — gap real, correctly flagged to Q19 |
| T | 400 kV+reactors share of book | ~8.8% | 275/3,116.63 = 8.82% | PR L103–104, L97 | TIE |
| U | RRVPNL MVA total | 4,168 | 4×160 + 63×50 + 12×31.5 = 640+3,150+378 = 4,168; units 4+63+12 = 79 | PR L92–93 | TIE |
| V | Inflow vs green band | ~1.39x / ~40% above | 972.42/700 = 1.389 | PR L97–98 | TIE |
| W | QoQ EBITDA-margin step-down | −347 bps | 20.005% − 16.534% = 347.1 bps | §5 Q21 | TIE |
| **X** | **QoQ PAT drop (102.19→46.84)** | **−35%** | **(46.84 − 102.19)/102.19 = −55.35/102.19 = −54.2%** | **addendum §5 Q21 (L84)** | **FAIL** |

### FAIL X — QoQ PAT drop misstated by ~19 points
Addendum §5 Q21 (L84): *"…and −35% sequential PAT drop (102.19→46.84)…"*. The two numbers cited are the verified CON PAT for Q4 FY26 (102.19, spine L284) and Q1 FY27 (46.84, spine L284). The correct sequential drop is **−54.2%**, not −35%. Checked against every plausible alternative denominator so this is not a mislabelled metric: revenue QoQ = −37.6% (747.62→466.33), EBITDA QoQ = −48.5% (149.56→77.10), standalone PAT QoQ = −50.1% (106.30→53.09) — none is −35%. The figure as printed is a genuine arithmetic error (likely a −54% → −35% transposition). It is above any rounding tolerance and is A4's own derived metric.
- A4 value: −35%
- Recomputed: −54.2%
- Source line: addendum §5 Q21 (L84); inputs verified at extract_results L284.

This does not flow into the Notion Key-Notes handoff (L103 omits the percentage), and it does not alter the verdict logic (it sits inside a management question), but per A5 discipline any derived-metric mismatch above rounding is a FAIL that must be corrected before save. **Loop back to A4** to correct −35% → −54% (≈ −54.2%).

**ARITHMETIC AUDIT: FAIL (1 error, item X). All 22 other recomputations tie.**

---

## 3. ADVERSARIAL READ

The three most positive claims in the addendum, each with its strongest same-text bear counter, and whether the counter survives un-incorporated.

**Claim 1 — Q1 FY27 inflow ₹972.42 cr, ~40% above the ₹600–700 cr green band → Section-8 item 1 upgraded to fully GREEN (both legs).**
Bear counter (from PR L97–98, L73): the ₹972.42 inflow cannot be trusted as a clean "beat" because the order-book roll-forward does not close — 2,493.30 opening + 972.42 inflow − 466.33 revenue = 2,999.39 vs stated 3,116.63, a ~₹117 cr unreconciled delta — and the book's definition basis (gross/net of GST, executed vs pending) is undisclosed. Verdict: counter is VALID but **already grafted** — the addendum keeps item 1's residual "definition basis" open, raises Q19 on the exact ~117 gap, and does **not** let the inflow upgrade Decision Status or resolve any flag. No un-incorporated survivor.

**Claim 2 — RVPN (RRVPNL) appears as a ₹291.68 cr paying CUSTOMER → lowers modelled probability of a second-utility debarment (thesis trigger 2 de-risked).**
Bear counter (from PR L91–94, L105–108): a single order does not clear the live SBPDCL debarment; the order may carry conditional pre-qualification / type-test / PBG terms not yet met; RVPN sits on the cascade watch-list and one commercial order can mask an unrelated pending quality/pre-qual matter with RVPN or another utility. Verdict: VALID but **already grafted** — the addendum treats the RVPN positive as a probability re-weight only (explicitly "does NOT fire, clear, or alter any tripwire"), keeps the SBPDCL cascade tripwire ACTIVE, and raises Q22 on order terms and other-utility matters. No un-incorporated survivor.

**Claim 3 — EHV mix quantified for the first time: 400 kV+reactors ≈₹275 cr, 220 kV >55% of the book.**
Bear counter (from PR L103–104): these are ORDER-BOOK figures, not revenue; ₹275 cr is only ~8.8% of the book and confirms ~0% of *revenue*; Section-8 item 2's green trigger is a **revenue** share ≥10% by FY27 H2, which is not met and may be years away. Verdict: VALID but **already grafted** — the addendum explicitly refuses to flip item 2 to GREEN ("PARTIALLY QUANTIFIED (order-book level); REVENUE share still UNKNOWN"), and raises Q20 distinguishing book from revenue. No un-incorporated survivor.

Discipline confirmations the task flagged, all verified present in the addendum:
- Decision Status **UNCHANGED — WATCHLIST / BUY ON DIPS**, 8A-W branch; flag-not-decide preserved (L100–101). PASS.
- Verdict stays **PROCEED WITH FLAGS** (L95). PASS.
- SBPDCL silence treated as an **active** tripwire / confirmatory-negative across all three same-day docs (L57, L72, L98). PASS.
- Cash conversion still **INDETERMINATE**; no silent PROCEED; H1 FY27 CFS named as missing evidence (L98). PASS.
- Margin flag (first sub-17% qtr, item 3 AMBER) not resolved (L57, L98). PASS.
- **No thesis-broken trigger claimed fired**; trigger 2 explicitly NOT fired, only de-risked (L70, L99). PASS.
- Every press-release FORWARD-SIGNAL / AMBIGUOUS finding produced a management question: A3-F16-6→Q19, A3-F16-2→Q20, A3-F14-1+A3-F16-1→Q21, A3-F16-5→Q22; A3-F6-1 re-armed into existing Q3/Q4/Q6/Q7 (L78, Q19–Q22). PASS.

**ADVERSARIAL READ: PASS. No surviving un-incorporated bear counter; flag-not-decide integrity intact; the addendum does not overstate the good news.**

(Observation, out of addendum scope: the carried-forward base phrase "first sub-17% operating-margin quarter" sits against a Q1 FY26 CON margin of 15.48% (also sub-17%). This is inherited base-review content, already A5-COMPLETE and outside this addendum's revision surface; noted, not scored.)

---

## 4. VERDICT

**INCOMPLETE.** Coverage PASS (91/91, no orphan) and Adversarial PASS (all three bear counters already grafted; Decision Status, verdict, SBPDCL tripwire, and no-trigger-fired all intact). One arithmetic error fails the run: the QoQ PAT drop in §5 Q21 is stated as **−35%** when the cited figures 102.19→46.84 compute to **−54.2%**.

**Loop back to: A4.**
**Exact gap:** §5 Q21 (addendum L84) states "−35% sequential PAT drop (102.19→46.84)"; the correct value is −54.2% (verified CON PAT Q4 FY26 102.19 and Q1 FY27 46.84, extract_results L284). Correct −35% → −54% and re-emit; no other cell changes.

```yaml
stage: A5-adversary
company: "atlantaelec"
quarter: "q1fy27"
model: claude-opus-4-8
status: complete
verdict: INCOMPLETE
coverage:
  orphan_rows: []
  missing_from_ledger: []
arithmetic_mismatches:
  - {metric: "QoQ PAT drop (Q4FY26 102.19 -> Q1FY27 46.84)", a4_value: "-35%", recomputed: "-54.2%", source_line: "addendum sec5 Q21 (L84); inputs extract_results L284"}
surviving_bear_counters: []
loop_back_to: "A4"
gap: "Addendum sec5 Q21 (L84) states '-35% sequential PAT drop (102.19->46.84)'; correct QoQ PAT drop is -54.2% (CON PAT Q4FY26 102.19 -> Q1FY27 46.84, extract_results L284). Correct -35% to -54% and re-emit; all other cells tie and pass."
```
