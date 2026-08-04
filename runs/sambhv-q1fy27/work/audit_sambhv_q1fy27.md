# A5 ADVERSARY / COMPLETENESS AUDIT — Sambhv Steel Tubes Ltd (SAMBHV) — Q1 FY27

**Agent:** A5 ADVERSARY | **Model:** claude-opus-4-8
**Audit date:** 03-Aug-2026 (Role 4 pass) + 04-Aug-2026 (Role 5 MERGE-UPDATE)
**Under audit:** `review_sambhv_q1fy27.md` (A4, merged Section A + B + C)
**Re-derived from:** A1 extracts (results + presentation + concall) and A2 ledgers only. A3 reasoning not consulted; all A4 cites checked, not deferred to.

> **MERGE-UPDATE NOTE (04-Aug-2026):** The Role-4 pass (Section A = results + presentation) was audited previously and is RE-CONFIRMED below (Parts 1A/2A) — I independently re-derived the load-bearing Section A metrics and they still tie. This revision adds the NEW audit of the Role 5 (concall) content merged into Section B and the refreshed Section C / triggers / questions / position (Parts 1B/2B and the adversarial read). One audit, three audits complete (coverage, arithmetic, adversarial).

Fresh-context method: re-ran the concall enumeration by manual pass over `extract_concall_sambhv_q1fy27.txt` (184 lines) and diffed against `ledger_concall_sambhv_q1fy27.md`; recomputed each load-bearing concall claim from the transcript lines; re-derived Section A financials from the results-ledger ₹mn cells (÷10 to ₹Cr). Foot taken against clean-copy printed subtotals.

---

## 1. COVERAGE AUDIT

### 1A. Section A (results + presentation) — RE-CONFIRMED

| Category | A2 count | Fresh count | Anchor | Status |
|---|---|---|---|---|
| Agenda/meeting items | 7 | 7 | Board Outcome a–e + commenced/concluded | PASS |
| Annexure items (A8+B6) | 14 | 14 | Annexures A/B read in full | PASS |
| Notes / footnotes | 14 | 14 | 5 std + 5 consol numbered + 4 footnotes | PASS |
| Line items std (27) / consol (35) | 62 | 62 | every row matches ledger Tables 4/5 | PASS |
| Zero-standing | 6 | 6 | Excep-nil-std, NCI×3, share-of-investees, AnnexA nil | PASS |
| Auditor paragraphs | 10 | 10 | std 1-4 + consol 1-5 + Reg33(8) sub-para | PASS |
| Entities / signature blocks | 3 / 5 | 3 / 5 | reporting+holding+subsidiary; CS/MD/Auditor | PASS |
| Slides | 43 | 43 | 43 page markers | PASS |
| Slide atomic numbers | 1,111 | spot-verified | slides 8/13/15/33/34/39 tie exactly | PASS |

No orphan and no missing Section-A row. Filing silence on the warrant independently confirmed (grep `warrant|86,95,400|Anjaneya|convertible` in results extract = 0 hits, corroborating FIND-07). **Section A coverage: PASS.**

### 1B. Section B (concall) — NEW: fresh enumeration vs A2 concall ledger

| Category | A2 count | My fresh count | Basis of my count | Orphan / missing | Status |
|---|---|---|---|---|---|
| Participants | 20 | 20 | 4 mgmt present (Vikas Goyal MD, Anu Garg CFO, Vikas/Bikash Agrawal ED, Prachi Kothari) + 1 absent Chairman (Suresh Goyal, "सुरेश गोयल"=1 hit L33, third-person only) + 13 analysts + 2 call-flow | none | PASS |
| Turns | 143 | 143 | non-blank content lines L22–L181; turn table rows 1–143, last = L181 MOD sign-off | none | PASS |
| Questions | 52 (+1 no-response) | 52 substantive (+1 no-response) | Q1–Q54 labels less Q2/Q30 audibility = 52; Vidhi Shah 1st attempt = no-response (L142) | none | PASS |
| Mgmt numbers | 131 | 131 (spot-verified) | §4 rows cross-checked at L27/41/48/52/69/74/96/111/113/115/122/135/145/156/161/165/169; range lower-bounds + bare counts genuine, no double-count | none | PASS |
| Forward commitments | 14 | 14 | FC1–FC14 | none | PASS |
| Hedges | 7 | 7 | H1–H7 (L74/78/127/139/161/166/174) | none | PASS |

Concall count gate: PASS on all six. No fresh row absent from the ledger → **no FAIL to A2.** (The Q1–Q54 labels reaching 54 while the substantive count is 52 — Q2/Q30 audibility — is an internally documented A2 quirk, not an orphan.)

**A3 concall findings A3-01..A3-13 — cited in A4?**

| A3 | Substance | A4 location | Status |
|---|---|---|---|
| A3-01 | Fund-raise ₹400 Cr (L48) vs ₹100 Cr same turn | 5A, 8A overlay, 7A, 8E, Exch2, N2, monitorables | CITED |
| A3-02 | Open future raise "if required" (L78) | Q19, 8B(iii), 8E, N3 | CITED |
| A3-03 | FY29 WC ₹600 Cr (mgmt L115) vs ₹300 Cr (analyst, unconfirmed) | Step2 table, Step5 WC note, Q32/33, N4 | CITED |
| A3-04 | FY27 margin 12% then 6% same turn (L127) | Step2 diag, Q37, 6B, N5 | CITED |
| A3-05 | Peak GROSS debt 800-850 term + 200-300 WC end-2027, 7.5-8% (L41/42) | Exch3, 8C(e), 8B, N1 | CITED |
| A3-06 | ED/CSO name Vikas (call) vs Bikash (filing) | 0B, 5A, N12 | CITED |
| A3-07 | Chairman ABSENT on succession-opening call | 0B, 5B, 8C, VERDICT | CITED |
| A3-08 | Governance silence — pledge/FII-DII/guarantees/RPT/exceptional/OCI unraised | 3E, 5B, 8C(c), N14/N15 | CITED |
| A3-09 | Q2 dampener pre-warned (L161) | Step3 cross-note, 6A, 7A, 8C(b), N6 | CITED |
| A3-10 | MS price −3-5% (L74); post-safeguard "no vision" (L174) | Q17, Q53, 8C(b), N7 | CITED |
| A3-11 | Q2 realisation refused "I will go with them" (L139) | Q43, 4B, N8 | CITED |
| A3-12 | SS benefit war-contingent (L163) | Q17, 5A, N9 | CITED |
| A3-13 | Kesda Q4FY27 reaffirmed on-schedule (L43/87/127) | Q5, 6B, 8A, 8C(a), N10 | CITED |

All 13 concall A3 findings are cited → **no orphan → no FAIL to A3.** Material guidance numbers (revenue +10-15%, EBITDA/ton 7,500-8,500, FY28 rev ~4,500 Cr, peak debt 1,000-1,150 Cr, product realisations, capacity dates, PLI 13%, power savings) all appear in A4 Step 2 / 7A / monitorables.

**Coverage verdict: CLEAN.** No orphan rows, no missing rows, across all three docs.

---

## 2. ARITHMETIC AUDIT

### 2A. Section A (Role 4) — RE-CONFIRMED (independently re-derived)

| Metric | A4 value | My recompute | Status |
|---|---|---|---|
| Op EBITDA Q1FY27 (PBT+D+Fin−OI) | 95.178 | 76.875+12.530+10.721−4.948 = 95.178 | PASS |
| Op EBITDA margin Q1FY27 / Q1FY26 | 13.00% / 13.02% | 95.178/732.173=13.00% ; 72.710/558.629=13.02% (flat) | PASS |
| ETR Q1FY27 | 26.36% | 20.263/76.875 = 26.36% | PASS |
| Core PBT ex-OI YoY | +62.47% | 27.657/44.270 = +62.47% | PASS |
| Reported PAT YoY (std / consol) | +69.50% / +66.89% | 23.213/33.399=+69.50% ; 22.652/33.871=+66.88% | PASS (≤0.01pp rounding) |
| S-vs-C PAT gap Q1FY27 / Q4FY26 | −0.16% / −4.42% | −0.157% ; −4.416% | PASS |
| Sign-flip swing Q1FY26→Q4FY26 | 5.83 pp | 1.413−(−4.416)=5.83 pp | PASS |

Sign-flip driver re-verified: Q4FY26 consol PBT-before-exceptional (744.03 mn) is ABOVE standalone (742.35 mn); the −4.42% PAT discount is caused ENTIRELY by the ₹35.10 mn consol-only exceptional (L1435, nil standalone, no numbered note). **Section A ties to the cent. No mismatch above rounding.**

### 2B. Section B (concall) — NEW: the four flagged load-bearing claims

**(a) Q1-as-peak decomposition**

| Step | A4 value | My recompute | Status |
|---|---|---|---|
| FY27 revenue guide (+10-15% on 2,413) | 2,654–2,775 | 2,413×1.10=2,654.3 ; ×1.15=2,774.95 | MATCH |
| Q1 revenue annualised | 2,929 (+21.4%) | 732.173×4=2,928.7 ; +21.4% | MATCH |
| Implied Q2–Q4 avg revenue | 640.6–680.9/qtr | (2,654.3−732.2)/3=640.7 ; (2,775.0−732.2)/3=680.9 | MATCH — both < Q1 732 & Q4FY26 685 |
| FY27 op-EBITDA guide (+10-15% on 270 base) | 297–311 | 270×1.10=297 ; ×1.15=310.5 | MATCH |
| Q1 op-EBITDA annualised | 381 (+41%) | 95.178×4=380.7 ; +41.0% | MATCH |
| Implied Q2–Q4 avg op-EBITDA | 67.3–71.8/qtr | (297−95.2)/3=67.3 ; (310.5−95.2)/3=71.8 | MATCH — both < Q1 95.2 |

Confirmed: management's OWN +10-15% guidance mathematically forces Q2–Q4 quarterly revenue AND op-EBITDA below Q1 → Q1 is a self-guided peak. **A4 correct.**

**(b) Peak-leverage ratios** (gross debt 1,000–1,150 = 800–850 term + 200–300 WC, L41)

| Ratio | A4 value | My recompute | Status |
|---|---|---|---|
| vs FY26 EBITDA ~284 (trailing) | ~3.5–4.0x | 1,000/283.6=3.53x ; 1,150/283.6=4.05x | MATCH |
| vs guided FY28 EBITDA (4,500×13%=585) | ~1.7–2.0x | 1,000/585=1.71x ; 1,150/585=1.97x | MATCH |
| vs annualised Q1 reported EBITDA 400.5 | ~2.5–2.9x | 1,000/400.5=2.50x ; 1,150/400.5=2.87x | MATCH |

Trigger (e) is NET + 2 consecutive quarters; net figure ND → does not fire; A4 correctly names the net figure as the deciding monitorable. **A4 correct.**

**(c) Monitoring #13 — SS realisations**

| Series | Q1 actual (L111) | Threshold | Above? | Q2 guide (L113) | Q2 above? | Status |
|---|---|---|---|---|---|---|
| SS 200 | 1,40,000 | 1,15,000 | YES (+21.7%) | 1,30,000 | YES | GREEN |
| SS 300 | 2,10,000 | 1,75,000 | YES (+20.0%) | 2,00,000 | YES | GREEN |

Both clear the threshold in Q1 AND on the softer Q2 guide. **GREEN confirmed. A4 correct.**

**(d) EBITDA/ton Q1 vs FY27 guidance band**

| Figure | Value | vs guide top 8,500 | Status |
|---|---|---|---|
| Q1 incl. sponge (deck L207) | 9,355 | 8,500 = 9.2% below Q1 | guide BELOW Q1 |
| Q1 ex-sponge (L201 / L52) | 10,002 | 8,500 = 15% below; 7,500 = 25% below | guide BELOW Q1 |
| FY27 weighted-avg guide | 7,500–8,500 | entire band > 6,000 floor | trigger (b) de-risked FY27 |

Guidance sits 9–20% (incl.) below Q1 while staying above the ₹6,000 break line. **A4 correct.**

**Arithmetic verdict: NO MISMATCH above rounding on any load-bearing claim (Section A or B). No FAIL to A4.**

---

## 3. ADVERSARIAL READ

Three most positive claims in the merged review; strongest bear counter built from the SAME transcript; whether it survives UN-incorporated (and must be grafted).

**Positive claim 1 — Monitoring #13 GREEN (SS realisations 1,40,000 / 2,10,000 above thresholds; "single biggest watchlist upgrade").**
Bear counter (L113/L76/L163/L169): Q2 realisations are ALREADY guided DOWN across every product — SS200 1,40,000→1,30,000, SS300 2,10,000→2,00,000, MS 60,000→58,000, GP 75,000→72-73,000; 90% of SS output is 200-series (L76); the SS-price benefit is explicitly WAR-CONTINGENT ("competition returns once shipments resume", L163); SS EBITDA/ton has bottomed at ~₹10,000 (Q3FY26, L169) — realisations are demonstrably volatile.
Survives? **No — incorporated.** A4 carries it at 6B ("softening into Q2"), 8B, 7A, and A3-12/N9; and the softer Q2 guide still clears both thresholds (GREEN holds).

**Positive claim 2 — 3/3 gradeable commitments DELIVERED; credibility 100%; COMMITTED & CREDIBLE.**
Bear counter (L48/L115/L127/L52): single-call base; management self-selected which prior commitments to reference; the "beaten" ₹7-8k EBITDA/ton prior guidance is management's own recollection of its own prior call (L52), unauditable (no prior Role-5 log); and the same call carries three numeric self-contradictions — ₹400/100 Cr (L48), ₹600/300 Cr (L115/117), 12%/6% (L127).
Survives? **No — incorporated.** A4 caps at PROVISIONAL Grade B, invokes "never grade on one quarter", labels the base "thin one-call", flags all three self-contradictions, and appends the explicit OVERPROMISER-watch.

**Positive claim 3 — PLI ~13% of revenue till 2030 ("a real earnings tailwind").**
Bear counter (L94): a lone unquantified management assertion embedded in a JSL-comparison answer; NO filing corroboration, NO scheme/sanction named, NO base defined; "13% of revenue" is magnitude-implausible for total-company revenue (13% of guided FY28 ₹4,500 Cr = ₹585 Cr ≈ a full year's EBITDA) — far more likely 13% of incremental SS-coil revenue; it has not started.
Survives? **No (as a blocking survivor) — incorporated.** A4 logs PLI "not credited this pass", "do NOT upgrade on concall noise alone" (8D/8E), and 7C flags management-asserted regulatory items as UNVERIFIED. **Non-blocking refinement recommended:** A4's 5A/flags call PLI "a real earnings tailwind"; that adjective overstates an uncredited, uncorroborated, magnitude-implausible number — softening to "an unverified management assertion (implausible as 13% of TOTAL revenue; likely 13% of incremental SS revenue); verify against the PLI sanction" would be cleaner. Because A4 does not credit it and already flags it unverified, the counter does not survive as missing.

**Adversarial-read verdict:** the merged review is symmetric — every strongest bear counter constructible from the extracts is already carried. **No surviving unincorporated bear counter.** One optional, non-blocking wording refinement offered on PLI (Section B 5A/flags); substance already present.

---

## 4. VERDICT-CAP CONFIRMATION

Q1 cash conversion is INDETERMINATE (no Reg 33 Q1 cash-flow statement; the concall adds guidance, not a CFO statement — Step 5 / 8D). Per CLAUDE.md ("Never let INDETERMINATE cash conversion silently resolve to PROCEED") and the protocol house rule, the verdict is capped at PROCEED WITH CAVEATS with the missing evidence named (Q2FY27 half-year Reg 33 cash flow, ~Nov 2026). A4's verdict is **PROCEED WITH CAVEATS**, explicitly states it "cannot resolve to plain PROCEED (INDETERMINATE cash cap)", and preserves the human-decided escalation to PROCEED WITH FLAGS. **Cap correctly applied — plain PROCEED is foreclosed.**

---

## VERDICT

**COMPLETE.** Coverage clean across all three docs (Section A 115 rows + 43 slides re-confirmed; concall 20/143/52/131/14/7 re-enumerated; all 13 concall A3 findings A3-01..A3-13 cited; zero orphans, zero missing). Arithmetic clean (Section A Op EBITDA/margins/ETR/YoY-QoQ/both PAT bridges/S-vs-C sign flip re-derived to the cent; concall Q1-as-peak decomposition, peak-leverage 3.5-4.0x trailing / 1.7-2.0x forward, monitoring #13 GREEN, and EBITDA/ton guidance-below-Q1 all recomputed with no mismatch above rounding). Adversarial read clean (review symmetric; no surviving unincorporated bear counter). Cash INDETERMINATE cap correctly holds the verdict off plain PROCEED. No loop-back to A2, A3 or A4 required. Proceeds to Notion save.

```yaml
stage: A5-adversary
company: "SAMBHV"
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
