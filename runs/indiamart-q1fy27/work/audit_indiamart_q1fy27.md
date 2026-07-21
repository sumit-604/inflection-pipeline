# A5 ADVERSARY / COMPLETENESS RE-AUDIT — IndiaMART InterMESH (INDIAMART), Q1 FY27
# Loop 1 of 2 (re-audit of REVISED A4 review). Model: claude-opus-4-8. Date: 2026-07-21.
# Independence: every number below re-derived from the A1 extracts at cited line numbers; A4/A3 cites checked, not trusted.

## SCOPE
Re-audit of the revised A4 review after my prior INCOMPLETE (four gaps). Three audits re-run in full on the
whole document, plus explicit confirmation each prior gap is genuinely closed and a NEW-error sweep on the
rebuilt PAT bridges. Extracts: results (INR mn, x0.1 = Rs Cr), presentation (Rs Cr), press release (Rs Cr).

---

## 1. COVERAGE AUDIT (fresh enumeration diffed against the three A2 ledgers)

| Category | A2 count | My fresh count | Method | Orphan rows | Status |
|---|---|---|---|---|---|
| Results — notes | 14 | 14 | 5 consol (L415/419/423/425/428) + 6 standalone (L649/653/656/658/660/663) + 3 segment fn a/b/c (L402/405/408) | none | PASS |
| Results — entities (Annexure I) | 13 | 13 | grep "Private Limited" in results extract → rows 1-13, L273-300 | none | PASS |
| Results — line items | 65 | 65 (all P&L rows 5A/5B/5C spot-verified to source) | full read of both filings' tables | none | PASS |
| Results — auditor paras | 16 | 16 | 9 consol + 7 standalone report sections (L66-305 / L464-604) | none | PASS |
| Results — agenda / annexure / signatures | 2 / 8 / 5 | 2 / 8 / 5 | Board Outcome L17-32; Annexure B L690-726; 5 sig blocks | none | PASS |
| Presentation — slides | 69 | 69 | grep `^\[page N\]$` in deck extract = 69 | none | PASS |
| Presentation — numbers / footnotes / zero-standing | 462 / 58 / 1 | reconciled (material KPI rows spot-checked to source lines) | Table 4/5 cross-read; L1166 zero-standing confirmed | none | PASS |
| Press release — bullets / claims / table items / quote | 3 / 24 / 11 / 1 | 3 / 24 / 11 / 1 | Tables 1-4; 38 NOT_IN_FILING/reconciles flags present | none | PASS |

**Orphan-row test (ledger row present, absent from A4):** none found. A4's preamble (review L11) reads every A2
row verbatim and marks the immaterial remainder "reviewed, no finding"; every KPI_WATCH / flagged row (notes
table Step 0D, entities incl. MonotaRO exit, segment results, Annexure B lending WOS, Other-Matters a/b/c,
signature-timing, all 10 monitoring KPIs, OI-composition, dividend payable) is cited at its line. All A3 finding
IDs enumerated at review L18-20 are carried into the body.

**Reverse test (row my fresh pass found, ledger lacks):** none. My grep counts equal the ledger counts on every
count-tested category. No loop-back to A2.

COVERAGE VERDICT: **PASS** — no orphan rows, no missing enumeration.

---

## 2. ARITHMETIC AUDIT (recomputed from raw extract lines; x0.1 applied to results mn)

All Section 1A/1B cells re-derived from results L321-350 / L618-643 — every cell ties. Every 1C derived metric,
Step 2 YoY, Step 3 QoQ, Step 4 bridge, Step 5 cash, and the S-vs-C gaps recomputed.

| Metric | A4 value | My recompute | Source line(s) | Status |
|---|---|---|---|---|
| Consol Op EBITDA Q1FY27 (PBTbefassoc+D+FC−OI) | 146.5 | 246.3+6.4+0.5−106.7 = 146.5 | res L332/328/327/322 | PASS |
| Consol Op EBITDA margin Q1FY27 | 35.4% | 146.5/414.4 = 35.35% | res L321 | PASS |
| Standalone Op EBITDA Q1FY27 | 149.3 | 234.3+2.6+0.5−88.1 = 149.3 | res L628/625/624/619 | PASS |
| Standalone Op EBITDA margin Q1FY27 | 39.7% | 149.3/375.9 = 39.72% | res L618 | PASS |
| Consol core PBT ex-OI Q1FY27 | 125.0 | 231.7−106.7 = 125.0 | res L334/322 | PASS |
| Consol core PBT YoY | +12.1% | 125.0/111.5−1 = 12.11% | res | PASS |
| Standalone core PBT YoY | +12.1% | 146.2/130.4−1 = 12.12% | res | PASS |
| Consol ETR Q1FY27 | 25.7% | 59.5/231.7 = 25.68% | res L339/334 | PASS |
| Standalone ETR Q1FY27 | 24.8% | 58.2/234.3 = 24.84% | res L632/628 | PASS |
| Consol revenue YoY | +11.4% | 414.4/372.1−1 = 11.37% | res L321 | PASS |
| Standalone revenue YoY | +8.5% | 375.9/346.3−1 = 8.55% | res L618 | PASS |
| Consol PAT YoY | +12.2% | 172.2/153.5−1 = 12.18% | res L341 | PASS |
| Standalone PAT YoY | +6.1% | 176.1/166.0−1 = 6.08% | res L633 | PASS |
| **4A consol bridge total** | **+18.7** | +42.3−29.3+0.5+0.5+14.3−0.5−9.1 = +18.7 (=172.2−153.5) | res L321/326/329/328/327/322/333/339 | **PASS (additive, exact)** |
| — 4A ΔOp EBITDA subtotal | +13.0 | 42.3−29.3 = 13.0 (=146.5−133.5) | res | PASS |
| — 4A ΔPBT subtotal | +27.8 | 13.0+0.5+0.5+14.3−0.5 = 27.8 (=231.7−203.9) | res | PASS |
| **4B standalone bridge total** | **+10.1** | +29.6−15.0+0.9+0.3+3.7−9.4 = +10.1 (=176.1−166.0) | res L618/623/626/625/624/619/632 | **PASS (additive, exact)** |
| — 4B ΔOp EBITDA subtotal | +14.6 | 29.6−15.0 = 14.6 (=149.3−134.7) | res | PASS |
| — 4B ΔPBT subtotal | +19.5 | 14.6+0.9+0.3+3.7 = 19.5 (=234.3−214.8) | res | PASS |
| OI unrealized MTM Q1FY27 (consol) | ~Rs 96 Cr | deck L1169 Q1FY27 col = 96 | deck L1169 | PASS |
| OI realized (non-op income) Q1FY27 | ~Rs 16 Cr | deck L1162 Q1FY27 col = 16 | deck L1162 | PASS |
| Unrealized MTM as % of consol PBT | ~41% | 96/231.7 = 41.4% | res L334 | PASS |
| Unrealized MTM post-tax as % of consol PAT | ~41% | 96×(1−0.257)=71.3; 71.3/172.2 = 41.4% | res L341 | PASS |
| OI-delta reversion → consol PAT hit | ~Rs 10.6 Cr → +5% | 14.3×(1−0.257) = 10.6; new PAT 161.6 = +5.3% YoY | res | PASS |
| Enquiries YoY (deck series) | −16% | 26/31−1 = −16.1% | deck L2030-2034 | PASS |
| Enquiries YoY (printed label) | −11% | table L1004 "(11%)"; chart L2024 "(11)%" | deck | PASS (inconsistency real) |
| Active buyers YoY (document-cited) | −5% | table L1002 "41 41 (5%)" | deck L1002 | PASS |
| Rolling-12m CFO consol | 696 | 694−161+163 = 696 | deck L1907/L1160 | PASS |
| Rolling-12m PAT consol | stated 493.7 | 474.7−153.5+172.2 = **493.4** | res L341 | within-rounding (Δ0.3; ratio 1.41x unchanged) |
| Rolling CFO/PAT consol | ≈1.41x | 696/493.4 = 1.410x | — | PASS |
| Single-q CFO/PAT consol Q1FY27 | 0.95x | 163/172.2 = 0.947 | deck L1160 | PASS |
| Single-q CFO/PAT standalone Q1FY27 | 0.87x | 153/176.1 = 0.869 | deck L1971 | PASS |
| CFO QoQ consol | −44% | 163/290−1 = −43.8% | deck L1907 | PASS |
| S-vs-C PAT gap Q1FY27 | 2.2% | (176.1−172.2)/176.1 = 2.21% | res L341/633 | PASS |
| S-vs-C PAT gap Q1FY26 | 7.5% | (166.0−153.5)/166.0 = 7.53% | res | PASS |
| S-vs-C PAT gap Q4FY26 | 27.9% | (69.6−50.2)/69.6 = 27.87% | res | PASS |
| Acct-software segment result | −0.6→−2.7 | L381 (6)→(27) mn ×0.1 = −0.6→−2.7 | res L381 | PASS |
| Busy EBITDA margin | 16%→9% | deck L1566 "16% 9%" | deck L1566 | PASS |

**Arithmetic mismatches above rounding: NONE.** The only numeric quibble — rolling-12m PAT stated 493.7 vs
recomputed 493.4 — is a 0.3 Cr difference that leaves the reported ratio (1.41x) unchanged and sits within
rounding; not a FAIL, no loop-back.

ARITHMETIC VERDICT: **PASS**. Both rebuilt PAT bridges are fully additive and reconcile exactly to +18.7
(consol) and +10.1 (standalone); the prior over-count (~+25.3 / ~+16.1) is gone; no new error introduced.

---

## 3. PRIOR-GAP CLOSURE CONFIRMATION

- **Gap 1 (OI composition grafted into the verdict, not left open):** CLOSED. The ~Rs 96 Cr unrealized FV-gain
  (deck L1169, verified = 96) vs ~Rs 16 Cr realized (deck L1162, verified = 16; footnote L1175) is quantified in
  Step 2 diag 6 (review L174), Step 4 questions (L238-239), Combined-Verdict flag 8 (L472), Q9 (L397), and the
  monitorables. ~41% of consol PBT / ~41% post-tax of the "record" PAT and the reversibility (Q4FY26 consol OI
  −33.9, res L322; prior FV swings (18),(85),109,89 verified at L1169) are correctly stated. The 96+16=112 vs
  106.7 gap is honestly labelled a cash-gen-table-vs-P&L classification difference, not a forced reconciliation.
  PROCEED WITH FLAGS / HOLD explicitly re-affirmed after the ex-MTM stress.
- **Gap 2 (non-additive PAT bridges):** CLOSED. Rebuilt as additive line-item walks; both reconcile exactly.
- **Gap 3 (active-buyer −3%→−5% "2nd consecutive" phrasing):** CLOSED. Re-labelled everywhere (item 2 L304,
  Step 6D L334, Q3 L391, flag L554): −5% is document-cited (L1002); the −3% and the "2nd consecutive decline"
  framing are named as Notion Q4 FY26 prior-quarter memory, NOT this quarter's filings.
- **Gap 4 (enquiries −11% vs 31→26 −16%):** CLOSED. Both figures cited (printed −11% at L1004/L2024; series
  31→29→28→27→26 at L2030-2034 → −16.1%), the ~5pp inconsistency named as unreconciled, RED held on either, and
  a management question raised (Q21). Verified line by line.

---

## 4. ADVERSARIAL READ (three most positive claims; strongest bear counter from the SAME extract)

1. **Positive: "Standalone Op EBITDA margin 40%, highest of trailing 5 quarters, +80bps YoY, above band."**
   Bear counter (same text): part of the +14.6 Cr YoY standalone EBITDA gain is cost operating-leverage while
   demand-gen spend is held flat — Selling & Marketing −1% YoY at Rs 54 Cr (deck L1419), falling to 14% of revenue
   from 16% (L1421), even as active buyers −5% (L1002) and enquiries −11%/−16% (L1004/L2034), and D&A fell −26%
   (res L625). SURVIVES? **No (already covered).** The review's central "split" thesis (price/margin delivered,
   volume did not; growth realization-only on a shrinking base) plus the guidance-silence flag (Q20/F17-04)
   carries the substance; the S&M-flat nuance sharpens but adds no missing risk.
2. **Positive: "Core operating PBT +12.1% both bases — operations stronger than the headline."**
   Bear counter: core PBT outpaces +8.5% standalone revenue via cost restraint on a contracting-volume base, not a
   healthy growth engine; ARPU (+9%/+10%, L1014/L1016) is the sole load-bearing driver. SURVIVES? **No** —
   explicitly incorporated (Step 6D "FIRING but now load-bearing"; Step 8C realization-only resolver).
3. **Positive: "Rolling CFO/PAT ≈1.41x elite; net cash Rs 3,553 Cr; clean unmodified audit."**
   Bear counter: single-quarter CFO/PAT sub-unity (0.87-0.95x), consol CFO +2% vs PAT +12% (L1107), ~12.2% of
   consol PAT unaudited-by-BSR incl. a fully board-furnished MonotaRO stub (res L215-227), and a ~Rs 340 Cr
   dividend payable (deck L1142) will draw the treasury in Q2. SURVIVES? **No** — every element already flagged
   (Step 5 seasonality, F4-01 unaudited stub, F11-01 dividend draw).

**Surviving bear counters requiring graft into A4: NONE.** All strongest same-text counters are already
incorporated; the one incremental nuance (S&M held flat while the funnel contracts) refines an already-headlined
flag rather than adding a missing risk, and does not meet the bar for mandatory graft.

---

## VERDICT

**COMPLETE.** Coverage clean (no orphan rows; fresh counts equal the ledgers). Arithmetic clean (every derived
metric re-derived from raw lines; both rebuilt PAT bridges additive and exact to +18.7 / +10.1; no error above
rounding). All four prior gaps genuinely closed and no new error introduced by the revision. No surviving bear
counter needs grafting. Proceeds to Notion save.

```yaml
stage: A5-adversary
company: "INDIAMART"
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
