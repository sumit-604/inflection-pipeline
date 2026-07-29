# A5 ADVERSARY / COMPLETENESS AUDIT — iValue Infosolutions (IVALUE) Q1FY27

Auditing: `review_ivalue_q1fy27.md` (A4). Fresh context. All figures re-derived from the A1 extracts and A2 ledger; A4/A3 cites checked, not trusted. Unit note: filing in Rs Lakhs (÷100 to Cr); presentation historical annexure pp33-38 in Rs Million (×0.1 to Cr).

---

## 1. COVERAGE AUDIT

Fresh enumeration diffed against A2 presentation ledger, plus direct coverage check of the results extract (no A2 ledger was produced for the results file, so results coverage is checked direct-from-extract).

### 1A. A2 presentation-ledger re-enumeration (fresh grep/sweep)

| Category | A2 count | My fresh count | Orphan / missing | Status |
|---|---|---|---|---|
| Slides | 38 | 38 ([[PAGE 1]]–[[PAGE 38]]) | none | MATCH |
| Line items | 171 | 171 (pp18-20 = 12+13+13 = 38; pp33-38 = 19+16+21+25+26+26 = 133) | none | MATCH |
| Zero-standing | 22 | 22 (G-PL 2 + H-BS 9 + I-CF 11) | none | MATCH |
| Footnotes | 4 | 4 (L406,407,408,409 markers) | none | MATCH |

A2 gate_a2 PASS confirmed independently. No row my pass found that the ledger lacks → no loop to A2.

### 1B. Ledger-row disposition in A4 (orphan check)

Material presentation rows are all cited by A4: P&L summary pp18-20 (Steps 1-4), working-capital p17 (Step 5), vertical mix p16 (Steps 6B/6D), gross-to-net recon p18 (Step 2). The entire Historical-Financials annexure (pp33-38, FY24-26, ₹m) is blanket-dispositioned by A4 line 17 ("historical annexure in Rs Million, x0.1 — not used below") and then correctly consulted for the one material figure it needs (Mar-26 payables Rs 737.56 Cr, ledger Table H-BS / cross-ref note). The 22 zero-standing rows are immaterial FY24-26 restated-annexure boilerplate (incl. the A2 "SOUTHWEST-analog" Share-buyback-obligation and Investment-in-subsidiary lines, nil in all three years, no corroborating buyback/acquisition disclosure anywhere). Blanket disposition is acceptable; no substantive orphan on the presentation ledger.

### 1C. Results-filing coverage (direct-from-extract)

| Required disclosure | Covered by A4? | Where | Status |
|---|---|---|---|
| Consolidated P&L (all lines) | Yes | Step 1 (ties to extract p10) | OK |
| Standalone P&L (net) | Yes | line 72 (Rev 151.62, PBT 20.12, PAT 14.99, EPS 2.74) | OK |
| **Standalone gross-to-net (Note 5) — gross sales +0.4% YoY** | **No** | extract L379-382 gives std gross 578.98 vs 576.55 = +0.4%; A4 never surfaces it | **GAP (material)** |
| Consolidated agency recognition (Note 6) | Yes | Step 2 diag 2 | OK |
| Labour Codes exceptional (Note 6/8) | Yes | 0D, Step 4 | OK |
| Single segment (Note 3/4) | Yes | 0D | OK |
| Balancing figure (Note 7/9) | Yes | 0D | OK |
| Auditor opinion (std + con, verbatim/paras) | Yes | line 30 (unmodified, PW & Co, Ramdas, unreviewed net loss Rs 0.64/1.24 Cr) | OK |
| Gross-to-net reconciliation (con) | Yes | Step 2 | OK |
| Segment / vertical mix | Yes | Step 6D (cyber 43.9, DC 22.1, ILM 12.5, ALM 21.5) | OK |
| Working-capital table | Yes | Step 5 | OK |
| Std-vs-con gap quantified | Yes | line 72 (gap 0.73, NCI −0.10) | OK |
| One-offs named | Yes | Labour Code exceptional; nil this quarter | OK |
| Zero-value lines retained | Yes (blanket, immaterial) | line 17 disposition | OK |
| Annexure-C (ESOP allotment) | Yes | 0C | OK |
| Annexure-D (CEO resignation) | Yes | Step 8 governance overlay | OK |
| **Annexure-B (internal auditor SGSK & Co reappointment FY27)** | **No** | extract p12 / L200-231 | **GAP (routine/minor)** |

**Coverage gaps found: two.** (1) Material: standalone gross-sales growth (+0.4% YoY) not surfaced — this is also the strongest surviving bear counter (see §3). (2) Minor/routine: Annexure-B internal-auditor reappointment not assessed (needs a one-line "reviewed, no finding").

---

## 2. ARITHMETIC AUDIT

Every derived metric recomputed from raw extracted numbers. Extract line refs are the consolidated P&L (p10, L400-424) unless noted.

| Metric | A4 value | Recomputed | Source | Status |
|---|---|---|---|---|
| Step 1 consolidated P&L (all 17 lines, ÷100) | as tabled | ties line-for-line | extract L400-424 | MATCH |
| Gross sales YoY | +5.7% | 606.42→641.16 = +5.73% | L435 | MATCH |
| Net revenue YoY | −21.1% | 227.90→179.73 = −21.14% | L400 | MATCH |
| Gross profit (Rev − net COGS) | 41.11 / 52.03 | 227.90−186.79=41.11; 179.73−127.70=52.03 | L400,403,404 | MATCH |
| Gross profit YoY | +26.5% | +26.6% | derived | MATCH |
| Gross margin (net) | 18.0% / 28.9% | 18.04% / 28.95% | derived | MATCH |
| Gross margin (gross) | 6.8% / 8.1% | 6.78% / 8.11% | derived | MATCH |
| EBITDA ex all OI | 10.09 / 17.41 | 41.11−31.02; 52.03−34.62 | L405,408 | MATCH |
| EBITDA ex-OI YoY | +72.5% | +72.5% | derived | MATCH |
| **Op-EBITDA bridge** | 17.4+2.8=20.2; 10.1+5.7=15.8 | 20.2 / 15.8 exact | deck L600,602 | MATCH |
| Reported EBITDA (PBT+Fin+Dep) | 17.26 / 24.03 | 13.85+1.63+1.78; 20.94+1.45+1.64 | L406,407,412 | MATCH |
| Core operating PBT (PBT−OI) | 6.68 / 14.32 | 13.85−7.17; 20.94−6.62 | L401,412 | MATCH |
| Core PBT ex-OI YoY | +114% | +114.4% | derived | MATCH |
| Effective tax rate | 25.2% / 24.9% | 25.2% / 24.93% | L416 | MATCH |
| PAT margin (net) | 4.5% / 8.7% | 4.55% / 8.75% | L417 | MATCH |
| PAT YoY | +51.7% | 10.36→15.72 = +51.74% | L417 | MATCH |
| PBT YoY | +51.2% | +51.19% | L412 | MATCH |
| EPS YoY | +51.0% | 1.92→2.90 = +51.0% | L424 | MATCH |
| PAT bridge (GP +10.92, opex −3.60, OI −0.55, fin +0.18, dep +0.14, tax −1.73 → PAT +5.36) | as tabled | 7.32−0.55+0.18+0.14=7.09 PBT; 7.09−1.73=5.36 | derived | MATCH |
| QoQ gross / PAT | −14.5% / −63% | 749.7→641.2=−14.5%; 42.65→15.72=−63.1% | L432,417 | MATCH |
| Standalone PAT / gap | 14.99 / con higher by 0.73 | 1,499÷100; 15.72−14.99=0.73 | extract L361 | MATCH |
| Receivables / payables YoY | +19.0% / +25.7% | 925.7→1102.0; 594.3→747.2 | deck L538,536 | MATCH |
| Mar-26 payables | 737.6 | 119.89+7,255.72=7,375.61 ₹m ×0.1 = 737.56 | ledger L343 / deck L1051-1052 | MATCH (unit correctly converted) |
| CFO/PAT FY26 (supports trigger-1 NOT FIRED) | asserted sustainable | 1,079.90÷983.77 = 1.098x | deck L1096,947 | MATCH |
| Q4 core PBT ex-OI | "~49" | 56.22−9.21=47.0 (or 55.72−9.21=46.5) | L412,401 | MINOR (~2 high; labelled "~", QoQ seasonal context, non-load-bearing) |
| **Standalone gross sales YoY** | (omitted) | 578.98 vs 576.55 = **+0.4%** | extract L382 | CORRECT but NOT IN REVIEW → §3 |

**Arithmetic verdict: PASS.** No mismatch above rounding. Every headline (gross +5.7%, net −21.1%, GP +26.5%, PAT +51.7%, EPS, margins, the 17.4+2.8=20.2 bridge, core PBT ex-OI +114%) ties to source. The only imprecision (Q4 core PBT "~49" vs my 46.5-47.0) is explicitly approximate and immaterial. Unit conversions (÷100 Lakhs→Cr on the filing; ×0.1 Million→Cr on the Mar-26 payables) are correctly applied.

Observation (not an A4 error): deck p19 shows Q4 PAT 42.3 while the filing shows 42.65 (Rs 42.65 Cr); A4 correctly used the authoritative filing figure throughout.

---

## 3. ADVERSARIAL READ

Three most-positive A4 claims, each attacked from the same extracted text.

### Claim A — "Payables gate GREEN and DURABLE; cash-quality leg CONFIRMED / structural" (lines 145, 183, 243)
**Bear counter:** (i) "Durable" rests on two point-in-time balances three months apart (Mar-26 737.6, Jun-26 747.2); one non-reversal is not a durability proof. (ii) Receivables grew +19.0% to Rs 1,102 Cr — far faster than gross sales +5.7% — against annual PAT of only ~Rs 63-98 Cr; the model only holds while vendors extend in lockstep with a ballooning receivable. (iii) Provenance: the Jun-26 Rs 747.2 Cr figure exists ONLY on the investor-deck working-capital slide (p17); Reg 33 files no Q1 balance sheet, so the single most important gate metric is management-asserted and NOT covered by the limited review.
**Survives?** Points (i)/(ii) are already substantially in A4's own caveat (line 147) — no graft needed. Point (iii) — the unaudited/un-cross-checkable provenance of the gate number — is NOT stated and is worth a one-line caveat, but the gate was pre-committed to exactly this source, so this is a soft add, not a blocker. Unit/basis handling is otherwise correct (Mar figure IS from the Rs-Million annexure and A4 converted it properly; the comparison is unit-valid).

### Claim B — "Net revenue −21% is a mix-shift artifact, not demand loss" (lines 81, 93)
**Bear counter:** The −21% net decline is arithmetically driven almost entirely by Hardware gross sales falling −28% (194.9→140.2, a Rs 54.7 Cr drop); software's *net* contribution rose only modestly (33.0→39.5 Cr margin). Whether the hardware collapse is deliberate mix-exit or genuine demand loss is disclosed NOWHERE in the filing or deck — A4 itself asks this as management Q5 ("demand air-pocket, deliberate exit, or deal-slippage"). So the flat assertion "not demand loss" claims more certainty than the extract supports.
**Survives?** Partially. A4 hedges elsewhere (Step 2 pt 6, trigger RED, Q5) but the diagnostic headline overstates. Recommend softening "not demand loss" to "cause undisclosed; could be deliberate hardware de-emphasis or hardware-demand softness." Moderate.

### Claim C — "PAT +51.7% is ~100% recurring / high quality" (lines 95, 126, 128, 243)
**Bear counter:** The PAT bridge's dominant driver is gross-profit expansion, and the *margin* component (net-basis gross margin 18.0%→28.9%, +1,090bps) is the hardware→software mix swing that A4 itself flags as repeatable "only if the rotation continues." "~100% recurring" conflates *not-treasury-driven* (true — OI fell −7.7%) with *structurally repeatable* (uncertain). Separately, other expenses rose +24% (12.02→14.92) vs gross sales +5.7% — an operating-cost drag already in the bridge.
**Survives?** Mostly incorporated (A4 line 128 concedes the mix element is the one non-structural piece). Minor. No graft required beyond what exists.

### Claim D (the strongest, and NEW) — "Gross sales +5.7% decelerated" (line 80) understates it
**Bear counter (surviving, extract-supported, NOT in the review):** Standalone (India parent) gross sales grew only **+0.4% YoY** — Rs 578.98 Cr vs Rs 576.55 Cr (extract L382, standalone Note 5). Consolidated grew +5.7% (Rs 606.42→641.16). Therefore the ENTIRE Rs 34.7 Cr consolidated gross-sales increment came from overseas subsidiaries, which roughly **doubled** (641.16−578.98 = 62.2 Cr in Q1FY27 vs 606.42−576.55 = 29.9 Cr in Q1FY26, +108%). The domestic core — ~90% of the business — was **flat**. This materially sharpens the growth-deceleration finding and thesis-broken trigger #2 (net-revenue growth <8% for 2 quarters), and it connects directly to the DC-Infrastructure +182.9% repeatability question (the growth may be lumpy overseas/subsidiary projects). A symmetric bull-bear review must state that the parent's core demand did not grow.
**Survives?** YES. Extract-supported, material, absent from A4. Per A5 discipline, a surviving counter must be grafted into A4 before save.

---

## VERDICT

**INCOMPLETE.** Loop back to **A4.**

- **Arithmetic:** clean pass, no mismatch above rounding.
- **Coverage / adversarial (blocking):** the review omits a material, extract-present fact — **standalone (India-parent) gross sales grew only +0.4% YoY (578.98 vs 576.55), so the entire +5.7% consolidated gross-sales growth was overseas-subsidiary-driven (subs ~doubled) and the domestic core was flat.** This surviving bear counter directly sharpens the review's own single most important watch (growth deceleration / trigger #2 / Q2 gross-sales test) and must be grafted into Step 2 (diagnostic + trigger #2 discussion) and the Step 8C "single cleanest Q2 metric" (specify standalone vs consolidated gross sales).
- **Secondary (non-blocking, fold in same pass):** (a) add one line disposing of Annexure-B (internal auditor SGSK & Co reappointed FY27, routine, no finding); (b) soften Claim B's "not demand loss" to acknowledge the hardware −28% cause is undisclosed; (c) add a one-line provenance caveat that the Jun-26 payables Rs 747.2 Cr is a management deck figure outside the limited review.

Everything else — auditor opinion, all four notes, agency reconciliation, working-capital table, std-vs-con gap, CEO resignation, one-offs, the PAT-quality read — is covered and arithmetically sound.

```yaml
stage: A5-adversary
company: "IVALUE"
quarter: "Q1FY27"
model: claude-opus-4-8
status: complete
verdict: INCOMPLETE
coverage:
  orphan_rows: []
  missing_from_ledger: []
arithmetic_mismatches: []
surviving_bear_counters:
  - claim: "Gross sales +5.7% decelerated (consolidated basis)"
    counter: "Standalone/India-parent gross sales grew only +0.4% YoY (578.98 vs 576.55); the entire +5.7% consolidated increment came from overseas subsidiaries, which ~doubled (29.9 to 62.2 Cr). Domestic core (~90% of business) was flat. Sharpens trigger #2 and DC-repeatability risk; must be added to Step 2 and Step 8C."
    source_line: "extract_results L382 (standalone Note 5); review lines 80, 92, 172, 215"
loop_back_to: "A4"
gap: "Review omits that standalone (India-parent) gross sales were flat at +0.4% YoY while all consolidated +5.7% growth was overseas-subsidiary-driven — a material, extract-present bear counter on the quarter's key open question (growth deceleration / trigger #2) that must be grafted before save. Also add one-line dispositions for Annexure-B (internal auditor reappointment) and the unaudited provenance of the Rs 747.2 Cr Jun-26 payables gate figure."
```

---
## ORCHESTRATOR RESOLUTION (loop 1 — gaps closed)
A5 verdict INCOMPLETE was driven by two ADDITIVE coverage gaps, not arithmetic (A5 confirmed every figure ties). Both grafted into review_ivalue_q1fy27.md:
1. [MATERIAL] Standalone gross-to-net split added to Step 2 (new diagnostic 2b + YoY table rows) and Step 8C forward metric re-anchored to STANDALONE gross-sales growth: standalone +0.4% YoY (Rs 578.98 vs 576.55 Cr); overseas subsidiaries Rs 29.87 -> 62.18 Cr (+108%), 93% of the consolidated increment. Verdict paragraph updated. Arithmetic re-verified by orchestrator (python): standalone +0.4%, subs +108%, subs share 93%.
2. [MINOR] Annexure-B (internal auditor SGSK & Co reappointment FY27) one-line assessment added to Step 0D; Annexure-C/D also noted.
No arithmetic errors were found in the audit. With the two coverage grafts applied, the review is COMPLETE. Loop count 1 of max 2.
