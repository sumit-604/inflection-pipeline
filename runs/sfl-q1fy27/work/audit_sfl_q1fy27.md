# A5 ADVERSARY / COMPLETENESS AUDIT — SFL — Q1 FY27 (RE-AUDIT after A4 fix loop)

Company: Sheela Foam Limited (SFL) | Quarter: Q1 FY27 (ended 30 June 2026)
Auditor: A5 ADVERSARY (Opus 4.8) | Date: 2026-08-04
Review under audit: runs/sfl-q1fy27/work/review_sfl_q1fy27.md
Independence: fresh context. I re-derived every number from the A1 extracts and
re-ran the A2 enumeration with my own pass. I did NOT defer to A4's or A3's cites.

---

## PRIOR-LOOP ITEMS (confirm resolved, then re-audit whole review afresh)

1. **P-A3-12 mapping gap (was: in reconciliation list, no QfM row / no monitorable /
   no "reviewed, no finding" marker).** NOW RESOLVED. Review L37 explicitly reclassifies
   P-A3-12 as NEUTRAL-FACT and carries the marker: *"reviewed, no finding — no
   prior-quarter deck was supplied to diff against, so no reframe/drop can be confirmed
   and no management question is required."* It is intentionally absent from QfM/monitorables
   and logged as a downstream prior-deck-diff item. The four constituent slides named
   (slide 8 "1ST TIME EVER", slide 19 STAQO break-out, slide 38 Venti, slide 41 AI-led ads)
   match exactly the four POSSIBLE_NEW_OR_REFRAMED flags in ledger_presentation (p8, p19,
   p38, p41). Mapping is now consistent. PASS.

2. **Broken cite at review L219 (was: `R L235-236` should be `P L235-236`).** NOW RESOLVED.
   Review L219 reads: *"...mattress value +15% / foam value +26% (`P L235-236`, `PR L78-79`)."*
   Verified: presentation extract L235 = "Mattress volume grew by 6% and value grew by 15%",
   L236 = "Foam volume grew by 4% and value grew by 26%"; press-release L78-79 confirm.
   (The former `R L235-236` pointed at a debt-equity-ratio formula — genuinely wrong; now
   corrected to the presentation.) PASS.

I did NOT relax scrutiny on the rest. Full re-audit below.

---

## AUDIT 0 — DELIVERABLE-COMPLETENESS (hard gate)

PLAIN-LANGUAGE BRIEF present at review L473, all four labelled parts present, non-empty,
provenance-labelled:

| Part | Location | Present? | Content check |
|---|---|---|---|
| (1) Summary narrative | L475-477 | present | ~1 dense paragraph (>10 lines equiv.), real content, cites R/P/PR/DI lines |
| (2) SECTOR intelligence | L479-484 | present | 4 bullets, each provenance-tagged (this-quarter vs prior/analyst context) |
| (3) BUSINESS-MODEL intelligence | L486-492 | present | 5 bullets incl. ND-metrics-named-per-contract bullet |
| (4) COMPETITION intelligence | L494-499 | present | 4 bullets incl. peer-benchmark ND flagged per contract |

GATE: PASS. All four parts present and non-empty.

---

## AUDIT 1 — COVERAGE (independent re-enumeration vs A2 ledgers)

Fresh grep/sweep pass over each A1 extract, diffed against the ledgers.

| Category | A2 count | My fresh count | Orphan / mismatch | Status |
|---|---|---|---|---|
| Results: numbered notes | 19 | 19 (9 std L194-294 + 10 consol L556-679) | none | PASS |
| Results: consolidation entities | 11 | 11 (L375-407) | none | PASS |
| Results: signature blocks | 5 | 5 (L47, L110, L298, L456, L683 "Digitally signed") | none | PASS |
| Results: auditor paras | 11 | 11 (4 std L79-105 + 7 consol L341-448) | none | PASS |
| Results: line items | 138 | 138 (P&L + Reg-52 + segment + Security-Cover NIL) — P&L cells spot-reconciled cell-by-cell | none | PASS |
| Presentation: slides | 51 | 51 ([page N] markers 1-51) | none | PASS |
| Presentation: numbers | 505 | methodology reproduced; OCR-noise exclusions consistent; no undocumented data value found | none | PASS |
| Presentation: footnotes | 3 | 3 (L211 "*before Forex MTM"; L416 "*100% monetization"; L517 "*since inception") | none | PASS |

**A3-finding coverage (every ledger interpretive row cited in A4 OR marked "reviewed, no finding"):**

- R-A3-01..11 (all 11): each carried into a QfM row — Q4(R-A3-01), Q2(R-A3-02), Q15(R-A3-03),
  Q3(R-A3-04), Q7(R-A3-05), Q8(R-A3-06), Q9(R-A3-07), Q12(R-A3-08), Q11(R-A3-09), Q1(R-A3-10),
  Q5(R-A3-11). 11/11 mapped.
- P-A3-01..11 (11): Q6(P-A3-01,05), Q4(P-A3-02), Q14(P-A3-03), Q9(P-A3-04), Q5(P-A3-06),
  Q10(P-A3-07), Q2(P-A3-08,09), Q1(P-A3-10), Q13(P-A3-11). 11/11 mapped.
- P-A3-12: "reviewed, no finding" marker at L37 (NEUTRAL-FACT). Valid.

All 23 A3 findings accounted for. **Every FORWARD-SIGNAL / AMBIGUOUS finding has >=1 QfM row;
the sole NEUTRAL-FACT (P-A3-12) carries the reviewed-no-finding marker.**

No orphan ledger rows (present in ledger, absent from A4). No rows my fresh pass found that
the ledger lacks. COVERAGE: PASS.

---

## AUDIT 2 — ARITHMETIC (recomputed from raw A1 line cites; nothing deferred)

Core-EBITDA formula used = Rev − (TotExpenses − Finance − Depreciation), i.e. ex-other-income,
ex-exceptional. All source cells from results extract (R Lxxx).

**Standalone core EBITDA (ex-OI) + 10% test:**
| Period | Rev | TotExp−Fin−Dep | Core EBITDA | Margin | A4 | Match |
|---|---|---|---|---|---|---|
| Q1FY27 | 760.92 | 692.54 | 68.38 | 8.99% | 68.38 / 8.99% | PASS — <10% BREACH confirmed |
| Q1FY26 | 634.63 | 574.38 | 60.25 | 9.49% | 60.25 / 9.49% | PASS |
| Q4FY26 | 819.20 | 728.83 | 90.37 | 11.03% | 90.37 / 11.03% | PASS |
| FY26 | 2962.27 | 2664.67 | 297.60 | 10.05% | 297.60 / 10.05% | PASS |

**Consolidated core EBITDA (ex-OI) + 10% test:**
| Period | Rev | TotExp−Fin−Dep | Core EBITDA | Margin | A4 | Match |
|---|---|---|---|---|---|---|
| Q1FY27 | 1031.94 | 923.04 | 108.90 | 10.55% | 108.90 / 10.55% | PASS — >10%, <12% confirmed |
| Q1FY26 | 821.41 | 746.18 | 75.23 | 9.16% | 75.23 / 9.16% | PASS |
| Q4FY26 | 1050.06 | 933.44 | 116.62 | 11.11% | 116.62 / 11.11% | PASS |
| FY26 | 3820.84 | 3427.47 | 393.37 | 10.29% | 393.37 / 10.29% | PASS |

**Core PBT (ex-OI, ex-exc) = PBTbeforeExc − OI:** std 7.54 / 38.86 / 58.48 / 116.42 and
consol (0.06) / 57.20 / 60.14 / 119.64 — all recomputed, all PASS.

**S-vs-C PAT gap % (consol vs std, YAML sc_gap_pat_pct):**
Q1FY27 (62.34 vs 43.94)=+41.9%; Q4FY26 (91.77 vs 75.52)=+21.5%; Q1FY26 (6.55 vs 10.70)=−38.8%;
FY26 (160.85 vs 130.57)=+23.2%. All PASS.

**YoY depreciation delta:** std 29.91→17.24 = −12.67 (−42.4%); consol 46.12→33.88 = −12.24
(−26.5%). PASS.

**Key YoY/QoQ growth figures:**
| Metric | A4 | Recomputed | Source | Status |
|---|---|---|---|---|
| Std revenue YoY | +19.9% | 126.29/634.63=19.90% | R L145 | PASS |
| Consol revenue YoY | +25.6% | 210.53/821.41=25.63% | R L490 | PASS |
| Std core EBITDA YoY | +13.5% | 8.13/60.25=13.49% | R L145/160 | PASS |
| Consol core EBITDA YoY | +44.8% | 33.67/75.23=44.76% | R L490/504 | PASS |
| Std core margin YoY | −50 bps | 8.99−9.49 | derived | PASS (deck −51) |
| Consol core margin YoY | +139 bps | 10.55−9.16 | derived | PASS |
| Std PAT YoY | +310.7% | 33.24/10.70=310.7% | R L171 | PASS |
| Consol PAT YoY | +851.8% (~9.5x) | 55.79/6.55=851.8%; 62.34/6.55=9.52x | R L518 | PASS |
| Std finance YoY | −46.1% | −10.52/22.80 | R L157 | PASS |
| Consol reported PBT YoY | +722% | 69.91/9.68=722.2% | R L507 | PASS |
| Std revenue QoQ | −7.1% | −58.28/819.20 | R L145 | PASS |
| Consol revenue QoQ | −1.7% | −18.12/1050.06 | R L490 | PASS |

**PAT bridge — Standalone (Step 4a), reported ΔPAT = 43.94−10.70 = +33.24:**
GP +5.47 (COGS-derived: GP 253.34→258.81), Emp −0.91, OthExp +3.57 → CoreEBITDA Δ +8.13;
Dep +12.67; Fin +10.52; OI +5.28; Exceptional +6.26; Tax −9.62. Sum = 33.24. PASS (ties).
Recurring-core share 8.13/33.24=24%; non-recurring (OI+exc) 11.54/33.24=35%. PASS.

**PAT bridge — Consolidated (Step 4b), reported ΔPAT = 62.34−6.55 = +55.79:**
GP +51.94 (GP 329.75→381.69), Emp −9.50, OthExp −8.77 → CoreEBITDA Δ +33.67; Dep +12.24;
Fin +11.35; OI +6.39; Exceptional +6.26; Tax −15.51; JV +1.39. Sum = 55.79. PASS (ties).
Core-EBITDA share 33.67/55.79=60%; non-recurring 12.65/55.79=23%. PASS.

**Effective tax rate (Tax/PBT):** std 32.7/16.4/25.2/20.7%; consol 50.1/17.8/25.6/23.3%.
All recomputed, PASS.

**Reported EBITDA (PBT+D+Fin, incl exc):** std 68.60/122.25/88.27/345.85; consol
84.97/150.73/131.29/455.57. All PASS.

**Sub+JV block swing (QfM Q4 / L413):** consol PAT − std PAT = Q1FY26 −4.15 drag → Q1FY27
+18.40 contributor. PASS.

**Secondary claim checks:** exceptional 6.26/PBT 58.75 = 10.7% (Q6) PASS; QfM Q1 12.67/36.60=
34.6%≈35% PASS; QfM Q15 15.22/62.34=24.4% PASS; receivable days 91/2.72=33.5 vs 91/3.11=29.3
(+4.2d) PASS; FX OCI swing 24.55→−2.56 = ~₹27cr PASS; intl subs (Aus +30.4% rev, +600bps;
Spain +54.7% rev, +900bps; Staqo +71.4% rev, −320bps) PASS; geography Within-India +20.8%,
Outside-India +42.1% PASS; NCDs −66.7%, net worth std +6.0% / consol +8.5% PASS.

ARITHMETIC: PASS. No mismatch above rounding anywhere. Deck-vs-filing cross-checks
(68/9.0% std, 109/10.6% consol, 9.5x, +139bps) all tie to the filing-derived figures.

---

## AUDIT 3 — ADVERSARIAL READ (three most positive claims, strongest same-text bear counter)

**Positive claim 1 — "Consolidated core EBITDA +44.8% to 10.55%: real operating expansion"
(L206), the international engine carries the group.**
Bear counter (same extract): the entire consolidated beat rests on international subs whose
margins ~doubled in a single year (Australia 6.8%→12.8%, Spain 5.7%→14.7%, P L308/L328) — a
one-year step of that size is as consistent with cyclical demand + favourable FX as with
durable structural gain; the translation line swung −₹27cr YoY (R L533), proving the currency
exposure is live and reversible; and 9 of 11 subs (₹284.14cr rev / ₹15.22cr PAT, R L420) were
NOT reviewed by the principal auditor — so the engine driving the beat is also the least-assured
part of the print.
Survives? NO — already incorporated: QfM Q4 (durable vs cyclical/FX-aided), QfM Q9 (FX/hedging),
QfM Q15 (unreviewed component trend), Section-C + brief "model drift / internationally levered"
flags. No graft required.

**Positive claim 2 — "PAT ~9.5x / +851.8%" headline (L214, PR L73).**
Bear counter (same extract): the growth is off a depressed base (consol Q1FY26 core PBT ≈ breakeven,
−0.06) and is materially non-recurring — 35% std / 23% consol of the PAT rise is OI + a ₹6.26cr
land-sale exceptional + an unexplained 42% depreciation drop (R L158/L282), none operational.
Survives? NO — already incorporated: Step 2 diagnostics 3-4, Step 4 bridges, flag "≈35% of
standalone PAT rise non-recurring/unexplained." No graft required.

**Positive claim 3 — Deleveraging "GREEN / ON TRACK": NCDs −67%, finance cost −46% (L344, L366).**
Bear counter (same extract): NCDs are only one debt line; total borrowings, leases, cash and
therefore actual net debt are ND at Q1 (no balance sheet) — the "toward net cash" claim is not
confirmable this quarter; meanwhile debtors turnover fell YoY (3.11→2.72 std, R L219), a
working-capital drag that can consume the very cash the deleveraging narrative assumes, and the
finance-cost fall itself is part of the "not fully real" PBT flatter.
Survives? NO — already incorporated: net-debt/CFO named ND per house rule (Step 5), receivables
AMBER (monitor #5), finance-cost treated as recurring-but-flattering in the bridge, cash
conversion INDETERMINATE cap. No graft required.

ADVERSARIAL READ: no surviving bear counter requires grafting into A4. The review already
carries the symmetric bear side of each headline.

---

## VERDICT

**COMPLETE.**

- Deliverable gate: PASS (all four PLAIN-LANGUAGE BRIEF parts present, provenance-labelled).
- Coverage: PASS (fresh counts tie to A2; zero orphan rows; all 23 A3 findings mapped to QfM
  rows or a valid reviewed-no-finding marker).
- Arithmetic: PASS (every derived metric recomputed from raw line cites; no mismatch above
  rounding; both prior-loop mechanical defects — P-A3-12 mapping and the L219 R→P cite — confirmed
  fixed).
- Adversarial: PASS (three strongest bear counters all already incorporated; none survives
  un-grafted).

loop_back_to: none. Proceed to Notion save.

```yaml
stage: A5-adversary
company: "SFL"
quarter: "Q1 FY27"
model: claude-opus-4-8
status: complete
verdict: COMPLETE
plain_language_brief:
  narrative: present
  sector: present
  business_model: present
  competition: present
coverage:
  orphan_rows: []
  missing_from_ledger: []
arithmetic_mismatches: []
surviving_bear_counters: []
loop_back_to: ""
gap: ""
```
