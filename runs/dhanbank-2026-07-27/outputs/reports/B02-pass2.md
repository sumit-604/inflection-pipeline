# STAGE 2 — NOTES TO FINANCIAL STATEMENTS, PASS 2 (WHAT WAS MISSED)
Company: Dhanlaxmi Bank Ltd (DHANBANK) | Run date: 2026-07-27 | Source: FY2024-25 Annual Report (standalone financials)
Basis: re-read of Schedule 1 through Schedule 18 (Notes to Accounts) and Pillar III Basel disclosures against Pass 1
(B02-pass1.md), with the source PDF's raw "₹ in '000" tables re-parsed digit-by-digit to resolve Pass 1's flagged
unit/decimal questions. All new findings below are additional to Pass 1; items fully covered in Pass 1 are not repeated.

---

## HEADLINE RESOLUTION — THE PASS-1 FLAGGED 10x "DISCREPANCY" (ORCHESTRATOR TASK ITEM)

**Resolved: there is no real discrepancy between Schedule 2 and Pillar III DF-11. Pass 1's own conversion of the
Schedule 2 "Balance in Profit and Loss Account" line was wrong — the correct figure is ₹(711.25) Cr, not ₹(71.12) Cr,
and it matches Pillar III DF-11 exactly.**

Attempted the instructed step first: tried to read PDF pages ~149-150 visually via the Read tool's `pages` parameter
on `runs/dhanbank-2026-07-27/inputs/annual-report/Annual_Report.pdf`. The tool returned an error — `pdftoppm is not
installed` (poppler-utils missing in this environment) — so no PDF page can be rendered as an image here. Fell back to
a digit-level re-parse of the text cache plus an exact arithmetic cross-check against the Bank's own disclosed
subtotals, which is a stronger form of verification than a visual read would have been (it ties to the rupee, not
just "looks right").

**What the source actually says (Schedule 2, PDF p.80-81, raw table stated "₹ in '000"):**
"V BALANCE IN PROFIT AND LOSS ACCOUNT (71,12,474) (76,12,278)" — i.e. the raw figure is **71,12,474 thousand** rupees
(FY25) and 76,12,278 thousand rupees (FY24), in Indian digit-grouping. Stripped of commas this is the plain number
7,112,474 (FY25) / 7,612,278 (FY24), in thousands. Converting to Crore (divide by 10,000, since 1 Crore = 10,000
thousand): **7,112,474 / 10,000 = ₹711.2474 Cr (FY25)**; **7,612,278 / 10,000 = ₹761.2278 Cr (FY24)**.

Pass 1 misread the Indian comma-grouping of "71,12,474" as if the value were ~71.12 (effectively dividing by
100,000, not 10,000) — an isolated misconversion, not a document error.

**Proof by exact reconciliation** (all other Schedule 2 lines re-parsed the same way, PDF p.80-81):
- Statutory Reserve closing: 16,14,984 → 1,614,984 thousand → ₹161.4984 Cr
- Capital Reserves (Revaluation ₹158.6381 Cr + Capital Reserve ₹72.8403 Cr) = ₹231.4784 Cr
- Share Premium: ₹1,156.0538 Cr (Pass 1 had this one right)
- Revenue & Other Reserves (Revenue Reserve ₹138.1351 + IFR ₹27.8512 + IRA ₹0 + Special Reserve ₹5.9857 + AFS Reserve
  ₹(9.1684)) = ₹162.8036 Cr
- Balance in P&L Account: ₹(711.2474) Cr

Sum: 161.4984 + 231.4784 + 1156.0538 + 162.8036 − 711.2474 = **1,000.5868 Cr**, which matches the Bank's own disclosed
Grand Total reserves of "1,00,05,867" thousand = ₹1,000.5867 Cr (PDF p.81) to the fourth decimal. The FY24 column
reconciles identically: 144.8374 + 232.8479 + 1005.4482 + 154.8444 − 761.2278 = ₹776.7501 Cr, matching the disclosed
PY Grand Total "77,67,501" thousand = ₹776.7501 Cr exactly. This is an exact tie-out, not an approximation — it
confirms the ₹711.25 Cr / ₹761.23 Cr conversion is the correct one and the Bank's Schedule 2 has no internal error.

**Cross-tie to Pillar III DF-11** (PDF p.149, not p.150 as Pass 1 cited — the "accumulated loss" line sits in the
table content immediately before the "===== PDF PAGE 150 =====" marker, so it is on marker-page 149; p.150, contrary
to Pass 1's note, is NOT image-only in the text cache — it contains fully extracted text continuing the same table,
verified by direct read): item 9 "Intangibles other than mortgage-servicing rights ... (accumulated loss- ₹7112.47
mio, and other intangible assets-Nil) 7112.47" — stated in the table's own header unit "₹ in Million". 7,112.47
Million ÷ 10 = **₹711.247 Cr**, which matches the correctly-converted Schedule 2 figure (₹711.2474 Cr) to three
decimal places. Further internal Pillar III cross-checks confirm the Million-unit convention: RWA "81554.46"
(million) = ₹8,155.446 Cr matches Note 1.2's disclosed RWA of ₹8,155.45 Cr exactly; the Pillar III "Composition of
Capital" summary table (PDF p.138) independently states "Paid-up Share Capital 3946.99" (million) = ₹394.699 Cr,
matching Schedule 1, and shows the SAME total deduction figure "7534.87" (million) used in DF-11's "Total regulatory
adjustments to CET1" (item 28) row — internally self-consistent.

**Conclusion**: the Bank's negative accumulated Profit & Loss balance is **₹(711.25) Cr at 31.3.2025, improved from
₹(761.23) Cr at 31.3.2024** — roughly 10x larger than Pass 1's headline number. This is a materially more significant
finding than Pass 1 reported: the legacy loss carry-forward is more than half of total paid-up capital + reserves
(₹394.70 Cr + ₹1,000.59 Cr net of the P&L debit = ₹1,395.29 Cr total net worth), not the ~5% figure implied by Pass
1's erroneous ₹71.12 Cr. It still directly explains the nil-CSR mechanic (Note 16i) and the negative retained-earnings
backdrop for the ₹28.68 Cr DTA carry-forward-loss recognition (Note 15g) that Pass 1 flagged — those flags stand, and
are now understood to rest on a legacy loss roughly 10x larger than previously stated. 🔴 Red Flag (materiality
correction, supersedes Pass 1 Top-10 items #4 and #7).

---

## SECOND UNIT-CONVERSION ERROR FOUND ON RE-READ — SCHEDULE 4 BORROWINGS (PDF p.80-81)

Re-parsing Schedule 4's raw "₹ in '000" table the same way surfaces a second, smaller instance of the identical
error pattern, and an internal self-contradiction inside Pass 1's own paragraph:

- PY "Other Institutions and Agencies" borrowing: raw "14,90,350" thousand → 1,490,350 thousand → **₹149.04 Cr**
  (Pass 1 stated ₹1,490.35 Cr — 10x too high).
- PY Lower Tier II bonds: raw "15,00,000" thousand → 1,500,000 thousand → **₹150.00 Cr** (Pass 1's narrative text
  correctly said "₹150 Cr Lower Tier II bonds" here, even though the same paragraph misstated the other two figures).
- PY Total borrowings: raw "29,90,350" thousand → 2,990,350 thousand → **₹299.04 Cr** (149.04 + 150.00 = 299.04,
  exact tie-out). Pass 1 stated ₹2,990.35 Cr — 10x too high, and this also fails a plausibility check: a single Lower
  Tier II bond issuance of ₹1,500 Cr would be larger than the Bank's entire net worth (~₹1,395 Cr), which is not
  realistic for a bank this size.
- FY25 replacement borrowing: Pass 1's own paragraph states "Total borrowings collapsed to ₹200.00 Cr" in its first
  sentence, then two sentences later says this was "replaced with ₹2,000.00 Cr fresh RBI repo borrowing" — a direct
  internal 10x contradiction, since RBI repo is the Bank's only FY25 borrowing category and must equal the stated
  Total. The correct figure is **₹200.00 Cr fresh RBI repo borrowing** (raw "20,00,000" thousand = 2,000,000 thousand
  = ₹200.00 Cr), consistent with Pass 1's own Total line.

Directionally this does not change Pass 1's qualitative read (funding mix shifted from term/capital-instrument
borrowing to short-tenor RBI repo) but the absolute scale of PY borrowings was overstated 10x. 🟡 Watch (correction,
not a new risk).

---

## SCHEDULE 8 vs NOTE 3(b) PROVISION RECONCILIATION — RESOLVED CLEAN (PASS 1's OWN OPEN QUESTION)

Pass 1 flagged Schedule 8's "Depreciation/Provision for Investments" PY figure for cross-note reconciliation against
Note 3(b), and second-guessed its own correct initial read (₹152.67 Cr) down to an incorrect "₹15.27 Cr." Re-parsing
resolves this cleanly: Schedule 8's raw PY figure "15,26,731" thousand → 1,526,731 thousand → **₹152.67 Cr is
correct**. Note 3(b) (already stated in ₹ Crore, PDF p.108-109) shows two separate provision pools as at FY24
close/FY25 opening: Provision for Depreciation on Investments ₹36.71 Cr + Provision for Non-Performing Investments
₹115.97 Cr = **₹152.68 Cr**, which ties to Schedule 8's ₹152.67 Cr to the rupee (rounding). Both pools are written
back to nil during FY25 (₹36.71 Cr and ₹117.30 Cr respectively — Note 3(b), PDF p.109-110), consistent with Schedule
8's FY25 nil closing figure. No discrepancy exists; Pass 1's flagged cross-note question is closed. 🟢 Clean
(resolution, not a new risk).

---

## NEW FINDING — NPA MOVEMENT SCHEDULE SHOWS FLAT FRESH SLIPPAGE, NOT DECELERATING STRESS (Note 4a-i, PDF p.113-114)

Pass 1 extracted only opening/closing GNPA ratios (4.05%→2.98%). The full movement table (not previously extracted)
shows:
- Fresh Gross NPA additions (slippages): **₹152.26 Cr in FY25 vs ₹152.24 Cr in FY24 — essentially flat, not
  improving.**
- Reductions in Gross NPA were actually *lower* in FY25 (₹209.36 Cr: Upgradation ₹44.72 Cr + Recoveries ₹96.85 Cr +
  Technical/Prudential write-off ₹52.42 Cr + Other write-off ₹15.37 Cr) than in FY24 (₹242.18 Cr: ₹65.55 Cr + ₹86.10
  Cr + ₹52.10 Cr + ₹38.43 Cr).
- The headline GNPA ratio improvement (4.05% → 2.98%) is therefore driven mainly by the 18.4% growth in the gross
  advances denominator (Schedule 9), not by a genuine deceleration in fresh slippage or an acceleration in recovery
  activity. 🟡 Watch — new finding, tempers the "clear asset-quality improvement" read Pass 1 gave this note; the
  underlying slippage rate is not actually improving.

---

## NEW FINDING — CUMULATIVE TECHNICAL WRITE-OFF POOL IS GROWING AND NEARLY DOUBLE THE HEADLINE GROSS NPA (Note 4a-i, PDF p.113)

A separate reconciliation within the same note, not previously extracted: "Technical Write off and the recoveries
made thereon" — Opening balance ₹661.47 Cr (FY25) / ₹651.20 Cr (FY24) → + Technical/Prudential write-offs during the
year ₹52.42 Cr (FY25) / ₹52.10 Cr (FY24) → − Recoveries from previously written-off accounts ₹21.42 Cr (FY25) /
₹41.83 Cr (FY24) → **Closing balance ₹692.47 Cr (FY25), up from ₹661.47 Cr, and up again from ₹651.20 Cr at FY23
close.**

- This cumulative written-off pool (₹692.47 Cr) is **nearly double the Bank's headline Gross NPA of ₹364.11 Cr** — a
  large stock of bad debt sitting entirely outside the NPA schedule and its ratios (GNPA 2.98%, NPR 0.99%) because it
  has already been technically/prudentially written off the books.
- The annual recovery rate against this pool has roughly halved: ₹21.42 Cr recovered against a ₹661.47 Cr opening
  pool in FY25 (3.2%) versus ₹41.83 Cr against ₹651.20 Cr in FY24 (6.4%). Gross write-offs added to the pool
  (₹52.42 Cr) are outpacing recoveries from it (₹21.42 Cr) in both years, so the pool is structurally growing, not
  shrinking.
- This quantifies (with a harder, balance-sheet-anchored number) the Other Income item Pass 1 already flagged at
  Note 16a — "Recovery from technical write-off accounts ₹16.70 Cr (PY ₹30.18 Cr, −45%)." 🔴 Red Flag — new finding;
  a growing, low-recovery-rate shadow NPA pool nearly 2x the reported Gross NPA is a materially understated
  asset-quality signal when reading only the headline GNPA/NNPA ratios.

---

## NEW FINDING — CROSS-NOTE MISMATCH ON "RECOVERY FROM TECHNICAL WRITE-OFF" FIGURES BETWEEN NOTE 4 AND NOTE 16a

The recovery amount from technically written-off accounts is disclosed twice with two different figures:
- Note 4a-i (Asset Quality, PDF p.113): "Recoveries made from previously technical/prudential written off accounts
  during the year" = **₹21.42 Cr (FY25)** / ₹41.83 Cr (FY24).
- Note 16a (Additional Disclosures — Miscellaneous Income, PDF p.134): "Recovery from Technical written off
  accounts" = **₹16.70 Cr (FY25)** / ₹30.18 Cr (FY24).

The two years show consistent gaps (₹4.72 Cr FY25, ₹11.65 Cr FY24) between the asset-quality-note recovery figure and
the P&L-income-note recovery figure for what is nominally the same underlying event. A plausible explanation is that
Note 4's figure includes recoveries applied to reduce the carrying provision/reserve rather than routed through the
P&L "Other Income" line, but the AR does not explain the gap. 🟡 Watch — new finding, a fair question for management
(added to Section D candidates for Pass 3).

---

## NEW FINDING — DIVIDEND GAP FROM PASS 1 NOW CONFIRMED, NOT JUST INFERRED (Auditor's Report, CARO Rule 11(e)(v), PDF p.74)

Pass 1 flagged "no explicit dividend declaration/appropriation line found... inferred nil... not confirmed" as an
input gap. The Auditor's Report contains a direct statement resolving this: **"The bank has not declared or paid any
dividend during the year and hence the compliance of Section 123 of the Act is not applicable."** (PDF p.74). This
is textual confirmation, not an inference — nil dividend for FY25 is now a grounded finding rather than a gap.
🟢 Clean (gap closed).

---

## NEW FINDING — LEVEL 3 (UNOBSERVABLE-INPUT) FAIR VALUE INSTRUMENTS FEED INTO THE CET1 DEDUCTION, QUANTUM NOT ISOLATED (Pillar III "Composition of Capital" summary, PDF p.138)

Not previously extracted: the Pillar III "Composition of Capital as on 31.03.2025" summary table states the CET1
deduction of ₹7,534.87 Million covers "Accumulated losses, DTA, Intangible Assets, AFS reserves, **Unrealized Gain on
Level 3 Instruments included in Reserves and Valuation Adjustments on Illiquid securities**." This confirms the Bank
carries Level 3 (unobservable-input) fair-valued instruments with an embedded unrealized gain that regulators require
to be prudentially filtered out of capital — a fair-value-hierarchy risk item. The individual Level 3 quantum is not
separately broken out in the AR (it is bundled with the "Prudential valuation adjustments" line, DF-11 item 7 =
₹135.56 Million / ₹13.56 Cr, which is itself immaterial in size). 🟡 Watch — new finding, disclosure-transparency gap
(quantum of Level 3 exposure and its unrealized gain not isolable from the AR), though the bundled figure is small.

---

## MINOR NEW ITEM — SPECIAL RESERVE U/S 36(1)(VIII) NOT PREVIOUSLY EXTRACTED (Schedule 2, PDF p.81)

Schedule 2 carries a static "Special Reserve U/s 36(1)(viii) of Income Tax Act, 1961" of ₹5.9857 Cr, unchanged both
years (no additions either year) — a routine income-tax-driven statutory reserve, not previously itemized in Pass 1's
Schedule 2 walk. 🟢 Clean, immaterial, noted for completeness only.

---

## PASS 2 NEW FINDINGS SUMMARY

1. **Resolved the Pass-1-flagged 10x "discrepancy"**: it does not exist. Pass 1 misconverted the Indian-digit-grouped
   Schedule 2 figure. Correct accumulated P&L deficit is **₹(711.25) Cr at 31.3.2025** (improved from ₹(761.23) Cr),
   which ties exactly to Pillar III DF-11's ₹7,112.47 Million deduction. Proven by an exact reserves-total tie-out
   (both years, to four decimal places) and by independent Pillar III cross-checks (RWA, Composition of Capital
   summary). This materially upgrades the significance of the legacy-loss overhang already flagged at Pass 1 Top-10
   #4 and #7 — the true scale is ~10x Pass 1's stated number. (Schedule 2, PDF p.80-81; Pillar III DF-11, PDF p.149)
   🔴 Red Flag.
2. Schedule 4 (Borrowings) PY sub-line figures were also overstated 10x by Pass 1, with an internal self-contradiction
   in Pass 1's own paragraph (₹200 Cr Total vs ₹2,000 Cr "replacement" borrowing in the same sentence set). Corrected:
   PY Other Institutions borrowing ₹149.04 Cr, PY Lower Tier II bonds ₹150.00 Cr, PY Total ₹299.04 Cr; FY25 RBI repo
   correctly ₹200.00 Cr. (Schedule 4, PDF p.81) 🟡 Watch (correction).
3. Schedule 8 vs Note 3(b) provision reconciliation, which Pass 1 flagged as an open cross-note question, is now
   resolved clean: ₹152.67 Cr PY provision = ₹36.71 Cr (depreciation) + ₹115.97 Cr (NPI), exact tie-out. (Schedule 8,
   PDF p.82-83; Note 3(b), PDF p.108-109) 🟢 Clean (resolution).
4. NPA movement schedule (previously only opening/closing ratios extracted) shows fresh Gross NPA slippage was flat
   YoY (₹152.26 Cr vs ₹152.24 Cr) and reductions were actually lower in FY25 — the GNPA ratio improvement is a
   denominator (advances growth) effect, not a genuine deceleration in stress. (Note 4a-i, PDF p.113-114) 🟡 Watch.
5. Cumulative technical write-off pool grew to ₹692.47 Cr (from ₹661.47 Cr), nearly double the headline Gross NPA of
   ₹364.11 Cr, with the annual recovery rate against this pool roughly halving YoY (6.4%→3.2%). A large, growing,
   low-recovery shadow bad-debt pool sits entirely outside the reported NPA ratios. (Note 4a-i, PDF p.113) 🔴 Red
   Flag.
6. Cross-note mismatch: "recovery from technical write-off accounts" is stated differently in Note 4a-i (₹21.42 Cr
   FY25/₹41.83 Cr FY24) versus Note 16a (₹16.70 Cr FY25/₹30.18 Cr FY24), unexplained in the AR. (Note 4a-i, PDF p.113;
   Note 16a, PDF p.134) 🟡 Watch.
7. Dividend gap flagged by Pass 1 is now confirmed textually, not inferred: Auditor's Report states no dividend was
   declared or paid in FY25 (Section 123 not applicable). (CARO Rule 11(e)(v), PDF p.74) 🟢 Clean (gap closed).
8. Pillar III "Composition of Capital" summary discloses Level 3 (unobservable-input) fair-valued instruments with an
   embedded unrealized gain feeding into the CET1 deduction, quantum not separately isolated in the AR. (PDF p.138)
   🟡 Watch.
9. Minor completeness item: Special Reserve u/s 36(1)(viii), ₹5.99 Cr static both years, not previously itemized.
   (Schedule 2, PDF p.81) 🟢 Clean.

---

```yaml
stage: B02-notes-pass2
company: "DHANBANK"
run_date: "2026-07-27"
model: claude-sonnet-5
status: complete
pass_2_empty: false
open_item_resolution:
  item: "Apparent 10x discrepancy, Schedule 2 Balance in P&L Account (Rs71.12 Cr) vs Pillar III DF-11 accumulated-loss CET1 deduction (Rs7,112.47 Million/Rs711.25 Cr)"
  method: "PDF page render unavailable (pdftoppm/poppler-utils not installed in this environment); resolved instead via digit-level re-parse of Schedule 2 raw '000 table plus exact tie-out against the Bank's own disclosed Grand Total reserves (both FY25 and FY24, matched to 4 decimal places) and independent Pillar III cross-checks (RWA, Composition of Capital table)"
  finding: "No real discrepancy. Pass 1 misconverted the Indian-digit-grouped Schedule 2 figure. Correct value: Balance in Profit and Loss Account = Rs(711.25) Cr at 31.3.2025, improved from Rs(761.23) Cr at 31.3.2024 -- ties exactly to Pillar III DF-11's Rs7,112.47 Million (= Rs711.25 Cr) deduction. Schedule 2 page anchor p.80-81; DF-11 accumulated-loss line is on PDF p.149 (not p.150 as Pass 1 cited), and p.150 is not image-only in the text cache -- it contains extracted text continuing the same table."
  materiality_note: "Legacy accumulated loss is ~10x larger than Pass 1 reported (Rs711 Cr not Rs71 Cr), more than half of total paid-up capital plus reserves (~Rs1,395 Cr); upgrades materiality of Pass 1 Top-10 items 4 and 7"
new_findings:
  - {finding: "Schedule 4 PY borrowings sub-lines also overstated 10x by Pass 1, with an internal self-contradiction (Rs200 Cr Total vs Rs2,000 Cr stated replacement borrowing); corrected: PY Other Institutions Rs149.04 Cr, PY Lower Tier II bonds Rs150.00 Cr, PY Total Rs299.04 Cr, FY25 RBI repo Rs200.00 Cr", note_ref: "Schedule 4, PDF p.81", rating: "Watch"}
  - {finding: "Schedule 8 vs Note 3(b) investment-provision reconciliation, an open question in Pass 1, resolved clean: Rs152.67 Cr PY provision = Rs36.71 Cr depreciation + Rs115.97 Cr NPI provision, exact tie-out", note_ref: "Schedule 8, PDF p.82-83; Note 3(b), PDF p.108-109", rating: "Clean"}
  - {finding: "NPA movement schedule shows fresh Gross NPA slippage flat YoY (Rs152.26 Cr vs Rs152.24 Cr) and lower reductions in FY25 than FY24; GNPA ratio improvement is a denominator (advances growth) effect, not decelerating stress", note_ref: "Note 4a-i, PDF p.113-114", rating: "Watch"}
  - {finding: "Cumulative technical write-off pool grew to Rs692.47 Cr (from Rs661.47 Cr), nearly double headline Gross NPA of Rs364.11 Cr, with annual recovery rate against the pool roughly halving YoY (6.4% to 3.2%)", note_ref: "Note 4a-i, PDF p.113", rating: "Red Flag"}
  - {finding: "Recovery from technical write-off accounts is stated inconsistently between Note 4a-i (Rs21.42 Cr FY25/Rs41.83 Cr FY24) and Note 16a (Rs16.70 Cr FY25/Rs30.18 Cr FY24), unexplained in the AR", note_ref: "Note 4a-i, PDF p.113; Note 16a, PDF p.134", rating: "Watch"}
  - {finding: "Dividend gap flagged by Pass 1 confirmed textually (not inferred): Auditor's Report states no dividend declared or paid in FY25", note_ref: "CARO Rule 11(e)(v), Auditor's Report, PDF p.74", rating: "Clean"}
  - {finding: "Pillar III Composition of Capital summary discloses Level 3 (unobservable-input) fair-valued instruments with an embedded unrealized gain feeding the CET1 deduction, quantum not separately isolated", note_ref: "Pillar III Composition of Capital table, PDF p.138", rating: "Watch"}
  - {finding: "Special Reserve u/s 36(1)(viii), Rs5.99 Cr static both years, not previously itemized in Pass 1", note_ref: "Schedule 2, PDF p.81", rating: "Clean"}
tool_limitation_noted: "Read tool pages parameter on source PDF failed: pdftoppm/poppler-utils not installed in this environment; visual page render was not possible, verification proceeded via text-cache digit re-parse and exact arithmetic reconciliation instead"
ready_for_pass3: true
```
