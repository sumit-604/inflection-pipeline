# A5 ADVERSARY / COMPLETENESS AUDIT — Atlanta Electricals Ltd (ATLANTAELEC) — Q1 FY27

Agent: A5 ADVERSARY | Model: claude-opus-4-8 | Date: 2026-07-21
Independence: fresh context. Inputs seen = A4 review + A1 extracts (results, presentation) + A2 ledgers (results, presentation). A3 forensic reasoning NOT seen — every number below re-derived from the A1 extract line numbers, not deferred to A4/A3 cites.
Scope confirmation: two documents (results filing + investor presentation); no concall transcript filed this quarter → Role 5 legitimately absent. Verified A4 states this (review L3, L5, L428, verdict block) and fabricates no concall content.

---

## AUDIT 1 — COVERAGE (fresh grep re-enumeration vs A2 ledgers, then ledger-vs-A4)

### 1A. Fresh count vs A2 ledger

| Category | A2 count | My fresh count | Method | Orphan / missing | Status |
|---|---|---|---|---|---|
| Results — pages | 9 | 9 | `grep ^\[page N\]` = 9 | none | PASS |
| Results — FS notes (numbered) | 5 | 5 | manual L304–311 | none | PASS |
| Results — notes incl. unnumbered footnote | 6 | 6 | +Details of Unutilized Funds L417–420 | none | PASS |
| Results — line items (FS 24 + IPO 5) | 29 | 29 | manual sweep FS table L258–301 (24) + IPO table L394–413 (5) | none | PASS |
| Results — zero-standing | 8 | 8 | FS L275/282/288/296/298 (5) + IPO rows 1,2,3 during-qtr (3) | none | PASS |
| Results — agenda items | 2 | 2 | Board letter L52, L60 | none | PASS |
| Results — auditor paras (13 numbered + 9 unnumbered) | 22 | 22 | `grep ^[0-9]+\.` numbered spine = 18 total (5 notes + 4 SA-LRR + 6 CON-LRR + 3 IPO-cert); of which 13 are auditor paras; +9 unnumbered IPO narrative (manual) | none | PASS |
| Results — entities | 3 | 3 | CON-LRR para 4 L209–212 | none | PASS |
| Presentation — slides | 30 | 30 | `grep ^\[page N\]` = 30 | none | PASS |
| Presentation — metrics (M-rows) | 148 | 148 | `grep ^\| M[0-9]+ \|` = 148 | none | PASS |
| Presentation — footnotes / people / milestones | 11 / 17 / 10 | 11 / 17 / 10 | `grep ^\| (F/P/T)[0-9]+ \|` = 38 = 11+17+10 | none | PASS |
| Presentation — disclosure units | 186 | 186 | 148+11+17+10 | none | PASS |

Every A2 grep count reproduces on my independent pass. No row my fresh pass found is absent from a ledger (nothing to loop back to A2). No orphan created by enumeration.

### 1B. Ledger rows → cited in A4 or reviewed-no-finding

A4's Ledger-Reconciliation Preamble (review L12–16) claims all rows reviewed at cited line numbers. Spot-verified the material spine:
- All 24 FS line items carried in A4 Step 1A/1B for BOTH standalone and consolidated (review L60–106). Confirmed against source L258–301.
- Zero-standing / non-operational rows: the operational zero-standing line (Exceptional, L275) is carried explicitly through Steps 1–4. The balance-sheet-style zero rows (Paid-up Capital L296, Other Equity L298) and OCI rows (L288–294) are legitimately outside the P&L Step 1 table; paid-up capital 15.38 is nonetheless used in Step 0C (share-count derivation). Not dropped — accounted for. No FAIL.
- Both standalone and consolidated carried throughout: Step 1A/1B, 1C (both), Step 2A/2B, Step 3 (both margins), Step 4A CON / 4B SA. Confirmed.
- Entity list (3 subs) → Step 0D / A3-F09 / Q16. IPO table + row-4 inconsistency → Step 0D / Q10. Balancing-figure Note 4 → Step 0D + Step 3 QoQ caution.
- Presentation: every material M-row that carries a forensic signal is cited (see Audit-3 forward-signal map). Immaterial extraction-quality flags (M76/M109/M110/M112/M114/M115 LAYOUT_AMBIGUOUS market-size charts; M77 [TBU] placeholders; F8 orphaned VDP footnote; M117 wallet-share; T9 GETCO Rs 298 Cr milestone) are not financially material to the results review; treated reviewed-no-finding. No material orphan.

Observation (not a FAIL): A4's incorporation list (review L19) names A3-F05, A3-F06, A3-F08, F1-1, F14-2 which are not separately quoted in the body. On my independent re-derivation from the extracts, every forensically-material item maps to a Step and/or a question (Audit 3); the plausible identities of these IDs (clean-opinion PASS; IPO-deployment monitorable; balancing-figure QoQ caution; signing-partner/cert-date non-flags) are all substantively addressed or are resolved PASS findings that require no management question. No uncovered forward-signal exists on independent derivation → no loop-back to A3 warranted.

**COVERAGE VERDICT: PASS.** No orphan rows, no rows missing from ledger.

---

## AUDIT 2 — ARITHMETIC (recomputed from A1 extract line numbers; ₹ Cr)

Source anchors: FS table L258 (Rev), L259 (OI), L266–269 (opex), L272 (PBT pre-exc), L275 (exceptional), L277 (PBT), L280–282 (tax), L284 (PAT), L301 (EPS). IPO table L394–413.

| Metric | A4 value | My recompute | Source lines | Status |
|---|---|---|---|---|
| Revenue YoY (SA/CON) | +48.0% | 466.33/315.11−1 = +48.02% | L258 | MATCH |
| SA Op EBITDA Q1FY27 | 77.55 | 70.44+5.76+5.74−4.39 = 77.55 | L272,268,267,259 | MATCH |
| SA Op EBITDA margin | 16.63% | 77.55/466.33 = 16.63% | L258 | MATCH |
| SA Op EBITDA YoY | +59.0% | 77.55/48.78−1 = +58.98% | L272 etc | MATCH |
| SA margin bps YoY | +115 bps | 16.63−15.48 | — | MATCH |
| CON Op EBITDA Q1FY27 | 77.10 | 63.58+10.13+5.71−2.32 = 77.10 | L272,268,267,259 | MATCH |
| CON Op EBITDA margin | 16.53% | 77.10/466.33 = 16.53% | L258 | MATCH |
| CON Op EBITDA YoY | +58.1% | 77.10/48.78−1 = +58.06% | — | MATCH |
| CON margin bps YoY | +105 bps | 16.53−15.48 | — | MATCH |
| SA PAT YoY | +70.5% | 53.09/31.14−1 = +70.49% | L284 | MATCH |
| CON PAT YoY | +50.4% | 46.84/31.14−1 = +50.42% | L284 | MATCH |
| SA EPS YoY | +58.6% | 6.90/4.35−1 = +58.62% | L301 | MATCH |
| CON EPS YoY | +40.0% | 6.09/4.35−1 = +40.00% | L301 | MATCH |
| SA Core PBT ex-OI YoY | +67.0% | (70.44−4.39)/(41.97−2.41)−1 = 66.05/39.56−1 = +66.96% | L277,259 | MATCH |
| CON Core PBT ex-OI YoY | +54.9% | 61.26/39.56−1 = +54.85% | L277,259 | MATCH |
| CON reported PBT YoY | +51.5% | 63.58/41.97−1 = +51.49% (deck prints 51.4%) | L272 | MATCH |
| SA ETR Q1FY27 | 24.63% | (17.00+0.35)/70.44 = 17.35/70.44 = 24.63% | L280–282,277 | MATCH |
| CON ETR Q1FY27 | 26.33% | (17.00−0.26)/63.58 = 16.74/63.58 = 26.33% | L280–282,277 | MATCH |
| Q1FY26 ETR | 25.80% | 10.83/41.97 = 25.80% | L280–284 | MATCH |
| SA D&A YoY | +145.1% | 5.76/2.35−1 = +145.1% | L268 | MATCH |
| CON D&A YoY | +331.1% | 10.13/2.35−1 = +331.1% | L268 | MATCH |
| SA finance cost YoY | −16.4% | 5.74/6.87−1 = −16.4% | L267 | MATCH |
| CON EBIT YoY | +44.2% | 66.97/46.43−1 = +44.2% (66.97=77.10−10.13) | L268 | MATCH |
| SA-vs-CON PAT gap Q1FY27 | 11.8% | (53.09−46.84)/53.09 = 6.25/53.09 = 11.77% | L284 | MATCH |
| S-vs-C gap Q4FY26 | 3.9% | (106.30−102.19)/106.30 = 3.87% | L284 | MATCH |
| S-vs-C gap Q1FY26 | 0.0% | (31.14−31.14)/31.14 = 0 | L284 | MATCH |
| QoQ revenue (SA) | −37.6% | 466.33/747.43−1 = −37.62% | L258 | MATCH |
| CON margin QoQ | −347 bps | 16.53−20.00; Q4 CON Op EBITDA 131.87+9.27+15.97−7.55=149.56, /747.62=20.00% | L272,268,267,259 | MATCH |
| SA margin QoQ | −322 bps | 16.63−19.85; Q4 SA Op EBITDA 136.50+5.37+16.04−9.53=148.38, /747.43=19.85% | L272 etc | MATCH |
| CON PAT bridge ΔPAT | +15.70 | 46.84−31.14 = 15.70; volume 151.22×15.48%=23.41 + margin 1.05%×466.33=4.90 = ΔEBITDA 28.32; −D&A 7.78 +FC 1.16 −OI 0.09 = ΔPBT 21.61; −tax 5.91 = 15.70 | L258–284 | MATCH |
| SA PAT bridge ΔPAT | +21.95 | 53.09−31.14 = 21.95; ΔEBITDA 28.77 −D&A 3.41 +FC 1.13 +OI 1.98 = ΔPBT 28.47; −tax 6.52 = 21.95 | L258–284 | MATCH |
| FY26 SA Op EBITDA margin | 18.73% | 346.82/1,851.32 = 18.73% (346.82=294.09+15.88+56.73−19.88) | L272,268,267,259,258 | MATCH |
| FY26 CON Op EBITDA margin | 18.60% | 344.45/1,851.52 = 18.60% (344.45=277.42+26.12+56.56−15.65) | same | MATCH |
| Deck FY26 EBITDA 344.44 "incl OI" | actually excl OI (ties CON 344.45) | incl-OI would be 344.45+15.65=360.10 ≠ 344.44 → deck footnote mislabels; excl-OI correct | deck L890/846; L272 etc | MATCH (F16-1 confirmed) |
| Implied shares Q1FY26/Q1FY27 | 7.16 / 7.69 Cr (+7.5%) | 31.14/4.35=7.16; 53.09/6.90=7.69; +7.4%; paid-up 15.38/2=7.69 | L284,301,296 | MATCH |
| IPO deployment | 99.5% | 398.09/400.00 = 99.52% | L413 | MATCH |
| IPO row-4 footing | needs 23.94, source prints 21.31 | 21.31+2.63=23.94; total-at-30Jun 79.12+210+85.03+23.94=398.09 (matches printed total); with printed 21.31 total would be 395.46 ≠ 398.09 | L410–413 | MATCH (A3-F07 confirmed in source) |

Every derived metric in A4's tables reproduces from the raw extract within rounding. **NO ARITHMETIC MISMATCH.**

House-rule / verdict-consistency checks:
- INDETERMINATE cash conversion (no mandated interim CFS; Reg 33 half-yearly): A4 caps at PROCEED WITH CAVEATS and names the missing evidence (H1 FY27 CFS/BS, ~Oct–Nov 2026) — review L263, L268, L437. It does NOT silently resolve to PROCEED. Escalation to PROCEED WITH FLAGS is driven by additional forensic flags; FLAGS is more cautionary than CAVEATS, so the "caps at CAVEATS" ceiling (no cleaner-than-CAVEATS) is respected. Consistent with CLAUDE.md NEVER rule.
- No exit PE used from outside Section 1B; no fair-value recompute triggered (Step 7 held pending ROCE reconciliation). Consistent.
- Decision Status WATCHLIST → 8A-W non-held branch, no trim/exit mechanics. Consistent.
- Thesis-broken triggers: margin 16.53% CON above the 15% exit line; single sub-17% quarter trips only the Section-8 item-3 amber (1 of 2), not the exit trigger. Correctly distinguished (review L312–314).
- Role 5 concall N.A. stated, not fabricated.

**ARITHMETIC VERDICT: PASS.**

---

## AUDIT 3 — ADVERSARIAL READ (three most-positive claims; strongest bear from the SAME extract)

**Positive claim 1 (review L424, L171, Step 4):** "Growth is real and clean — core operating PBT +54.9% CON / +67.0% SA, essentially 100% recurring, not an Other-Income artefact."
Bear counter from same text: consolidated PAT growth (+50.4%, L284) trails standalone (+70.5%) and the S-vs-C PAT gap widened 0% → 3.9% → 11.8% because the three subsidiaries booked Rs NIL revenue and a Rs (4.40) Cr net loss (CON-LRR para 6, L223–227) while CON D&A quadrupled to 10.13 vs SA 5.76 (L268). The group is carrying pre-commissioning burn; "operating leverage" is also cushioned by a one-time IPO-deleverage finance-cost fall (+1.16 in the CON bridge). Survives on the extract — BUT already fully incorporated by A4 (S-vs-C gap flag, D&A drag Step 4, Q2, item-6 UNKNOWN). No graft required.

**Positive claim 2 (review L141, L157, L170):** "Operating margin EXPANDED +115 bps SA / +105 bps CON YoY."
Bear counter from same text: the expansion is only against a weak Q1FY26 base (15.48%); sequentially margin COLLAPSED −347 bps QoQ (CON 20.00% → 16.53%, deck M42 L274) and Q1FY27 is the FIRST sub-17% quarter, directionally aligned with the flagged Voltamp −500 bps sector shock. The YoY optic hides the live compression signal. Survives — BUT A4 already renders this "dual-signed" (Step 2 diagnostic 2, Step 3, item-3 amber, Step 8C). No graft required.

**Positive claim 3 (review L295, L336, L425):** "Order book +25% QoQ to Rs 3,116.63 cr — strong revenue visibility; thesis INTACT."
Bear counter from same text: the order-book figure is undefined (gross/net of GST, executed/pending) and gross Q1 inflow is undisclosed (item-1 inflow leg UNKNOWN), so +25% could be one lumpy award; the "visibility" coexists with unquantified 400 kV share (item 2), blended 98.28% utilization masking plant-level Vadod ~39% / Trafo ~15% (deck M104), and total SBPDCL-debarment silence in both documents (selective disclosure). Survives — BUT A4 already carries all three (Q15 / item-1 UNKNOWN; Q14 / item-6 masked; Q18 / item-8 silence). No graft required.

Forward-signal / AMBIGUOUS coverage check (independently derived from the extracts; every item must yield ≥1 management question):

| Forward/ambiguous item (extract) | Q# |
|---|---|
| Sub-17% margin, −347 bps QoQ (L272 / deck L274) | Q1 |
| Subsidiary NIL rev + Rs (4.40) loss (L223–227) | Q2 |
| Atlanta Trafo "turnaround in a quarter" (deck L542) | Q3 |
| 765 kV tie-up "active discussions" unsigned (deck L541) | Q4 |
| 400 kV share unquantified / "development" (deck L185) | Q5 |
| IDT facility "commissioning" (deck L183) | Q6 |
| Backward integration, no capex figure (deck L792) | Q7 |
| CON D&A quadrupled (L268) | Q8 |
| CON deferred-tax credit / subsidiary DTA (L281) | Q9 |
| IPO row-4 arithmetic (L410–413) | Q10 |
| RoCE 39.11 / 21.71 / 47 conflict + D/E 0.97 (deck M57/M123/M125) | Q11 |
| Share-count / EPS lag (L301) | Q12 |
| EBITDA definition mismatch (deck F2 vs F11) | Q13 |
| Blended 98.28% masks plant-level (deck M104) | Q14 |
| Order-book definition / inflow (deck M22/M30) | Q15 |
| Atlanta Trafo rename + acquisition-date Apr-2025 vs 2024 cluster (L211 / deck M56/T9) | Q16 |
| Labour Codes exceptional FY27 exposure (L275) | Q17 |
| SBPDCL silence (both docs) | Q18 |

Every independently-derivable forward-signal/ambiguous item produces at least one management question. No surviving bear counter is un-incorporated.

**ADVERSARIAL VERDICT: PASS.** All three strongest bear counters survive on the extract but are already present in A4's symmetric bull-bear treatment; none needs grafting.

---

## VERDICT

**COMPLETE.** Coverage PASS (fresh grep reproduces every A2 count; no orphan; no ledger gap; both standalone and consolidated carried throughout; zero-value lines not dropped; Role 5 correctly N.A. and not fabricated). Arithmetic PASS (every derived metric re-computed from extract line numbers within rounding, including YoY/QoQ, margins, ETR, S-vs-C PAT gap, PAT bridges, and the IPO row-4 footing). Adversarial PASS (three strongest bear counters survive but are already incorporated; every forward-signal has a management question; the INDETERMINATE cash-conversion cap is applied correctly per house rule). No loop-back to A2, A3, or A4. Proceeds to Notion save.

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
