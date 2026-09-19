# Stage 2 — Notes to Financial Statements, Triple Pass: PASS 2 (What Was Missed)

Company: Steel Strips Wheels Ltd (SSWL) | Run date: 2026-09-19
Source: inputs/annual-report/SSWL-AR-FY26-Reg34-2026-09-03.txt (page-marked text of the 245-page PDF; "AR p.N" cites the PDF page)
Unit as printed on the face of every note: **Rs in Lakhs**. This report states every figure as "Rs X lakh (Rs Y.YY Cr)".

Scope: re-read standalone notes 1-54 (AR p.144-183) and consolidated notes 1-56 (AR p.196-239), plus AOC-1 (AR p.239-240), against the Pass 1 output (outputs/reports/02-notes-pass1.md). Reported here: NEW findings only, and explicit resolutions of items Pass 1 carried forward. Items Pass 1 already covered fully are not repeated.

Carry-forward list from Pass 1 (checked against, one by one): R&D capex/opex split, leave-encashment 12.4x jump, CSR-through-Hansraj-Trust, missing warranty roll-forward, absent subsequent-events note, AMW AOC-1 "Turnover: 0", and the standalone-vs-consolidated Note 8 security-deposit gap (Rs 269.20 lakh). Disposition of each is stated below.

---

## NEW FINDING 1 (promotes/expands Pass 1 Finding 1): The Rs 364.52 Cr "Transfer to Capital Reserves" is the SECOND large, undisclosed equity reclassification in two years, and consolidated retained earnings never actually lost money by trading

Reading the full consolidated Note 19 Other Equity roll-forward (Note 19, consol AR p.219-220) line by line, not just the closing balances Pass 1 quoted:

| Consolidated Retained Earnings | FY24 close (=FY25 open) | FY25 close (=FY26 open) | FY26 close |
|---|---|---|---|
| Balance | **+Rs 5,763.84 lakh (+Rs 57.64 Cr)** | -Rs 43,823.14 lakh (-Rs 438.23 Cr) | -Rs 82,670.49 lakh (-Rs 826.70 Cr) |

Movements that drove the FY24-close-to-FY26-close swing:
- FY25: Profit for the year +Rs 19,528.48 lakh, dividend -Rs 1,569.29 lakh, **Transfer to General Reserves -Rs 67,468.46 lakh**.
- FY26: Profit for the year +Rs 19,021.84 lakh, dividend -Rs 1,964.76 lakh, **Transfer to Capital Reserves -Rs 36,451.69 lakh**, Transfer to General Reserves -Rs 19,528.48 lakh.

Two things Pass 1 did not surface:

1. **The FY25 "Transfer to General Reserves" of Rs 674.68 Cr is 3.5x that year's own consolidated profit (Rs 195.28 Cr).** A transfer-to-general-reserve line should not exceed the year's profit unless it is also sweeping out a pre-existing balance. The only pre-existing balance available to sweep is the positive Rs 57.64 Cr FY24-close opening balance plus, most plausibly, an FY24 gain that entered retained earnings before this AR's comparative window opens (i.e., before 31-Mar-2025) — which is exactly when the AMW NCLT transaction (LBF4) would have landed per company memory (consideration ~Rs 138 Cr). No note anywhere states this. This means the reserve-reclassification pattern the AR is not explaining is not a one-year, one-line event: **it spans two consecutive years (FY25's oversized general-reserve sweep, then FY26's new Capital Reserve carve-out) and both land in different reserve buckets with zero cross-referencing.**
2. **Consolidated retained earnings turned negative from reserve transfers, not from losses.** Consolidated profit was positive in both FY25 (Rs 195.28 Cr) and FY26 (Rs 190.22 Cr, Note 53 parent-share Rs 202.09 Cr less AMW's -Rs 11.88 Cr and associate's +Rs 0.01 Cr). The -Rs 826.70 Cr closing balance is entirely a function of the two oversized transfer lines, not of trading performance. An investor reading only the balance sheet would misread this as accumulated losses; it is not.
3. **The consolidated "Nature and purpose of Reserves" explanatory note (Note 19, item (i) through (vi), AR p.220) lists Securities premium, Retained earnings, Share Options, General Reserve, Capital revaluation reserve, and Equity instruments through OCI — and omits "Capital Reserve" entirely**, even though Capital Reserve is a Rs 364.52 Cr line in the very same note's movement table, immediately above. Every other reserve the company holds gets a one-paragraph purpose statement; this one, the largest single movement in the filing, gets none. This is a disclosure-template lapse, not merely an absence of explanation — the company's own note structure shows it knows to explain reserves and chose not to for this one. (Note 19, consol AR p.219-220)

Rating: 🔴 Red Flag (elevates Pass 1 Finding 1; this is now a two-year pattern with an internal disclosure inconsistency, not an isolated line item).

## NEW FINDING 2: A second, separate consolidation-only reserve gap — Capital Revaluation Reserve — sits against the company's own "no revaluation" statement

Standalone Note 19 Capital Revaluation Reserve: Rs 5,280.64 lakh, unchanged both years (AR p.164).
Consolidated Note 19 Capital Revaluation Reserve: **Rs 8,764.53 lakh, unchanged both years** (AR p.219).

The consolidation-only excess is **Rs 3,483.89 lakh (Rs 34.84 Cr)**, present at FY25 opening already (i.e., it entered at or before the AMW acquisition on 09-01-2024, per AOC-1 — see New Finding 5) and static since. The reserve's own stated purpose, identical in both standalone and consolidated notes: *"Cumulative gains and losses arising on revaluation of Fixed assets measured at market value"* (Note 19(v), AR p.164/220). But both the standalone and consolidated Note 53(X)/55(X) regulatory-information sections state explicitly: *"The Company/Group has not revalued its property, plant and equipment... or intangible assets... during the current or previous year"* (AR p.182, p.237) — and Pass 1 already confirmed no revaluation either year. A reserve whose defined purpose is PPE revaluation, carrying a Rs 34.84 Cr consolidation-only balance, coexists with an explicit no-revaluation declaration. The most likely explanation — AMW's own pre-acquisition revaluation reserve carried into the group's books at the acquisition date — is never stated. Under Ind AS 103 acquisition accounting, a subsidiary's pre-acquisition equity reserves are not normally meant to survive as identically-labelled lines in the acquirer's consolidated equity; if that is what happened here, it is a technical point the notes should have addressed and did not.

Rating: 🔴 Red Flag (new; ties directly to LBF4 and compounds New Finding 1 — this AR now has TWO unexplained consolidation-only reserve balances tied to the AMW acquisition, not one).

## NEW FINDING 3: The Note 6(II) impairment-assessment cross-reference is a dead end

Pass 1 flagged (🟡) that consolidated Note 6(II) states impairment indicators were identified on the associate investment and an assessment was performed, "Refer Note 52(C)." Pass 2 followed that cross-reference: **Note 52(C) (AR p.236-237) contains only the associate's summarised balance sheet and P&L (current/non-current assets and liabilities, equity, revenue, profit) — no discount rate, no value-in-use methodology, no cash-flow-projection period, no headroom figure, nothing that substantiates an "impairment assessment."** The promised support for the judgment is not present anywhere in the document. This confirms rather than merely suspects a disclosure gap: Ind AS 36 paragraph 134 would ordinarily expect key assumptions and sensitivity for a value-in-use test where indicators were identified; none appear. Upgraded from 🟡 to a firmer 🟡/🔴 boundary call: the assessment itself may be sound, but the AR provides no way to check it.

## NEW FINDING 4: Note 8 standalone-vs-consolidated security-deposit gap — RESOLVED, not a red flag

Pass 1's carry-forward list named an unexplained Rs 269.20 lakh gap: standalone Note 8 Other financial assets (non-current) shows security deposits of Rs 1,471.29 lakh vs consolidated Rs 1,202.09 lakh (FY26). Pass 2 traced this: standalone Note 41 (Related Party Disclosure) shows a **new-this-year Rs 270.00 lakh security deposit paid BY SSWL TO its own wholly-owned subsidiary AMW** (Note 41, AR p.171-172). This is an intercompany balance that eliminates on consolidation: Rs 1,471.29 lakh - Rs 270.00 lakh = Rs 1,201.29 lakh, within Rs 0.80 lakh of the consolidated Rs 1,202.09 lakh figure (residual plausibly AMW's own small deposits or rounding). The FY25 comparative gap is negligible (Rs 1,276.54 lakh standalone vs Rs 1,276.64 lakh consolidated, Rs 0.10 lakh) — consistent with the AMW security deposit not existing yet in FY25. **This carry-forward item is closed: the mechanics are correct, standard consolidation elimination, no irregularity.** (Note 8, standalone AR p.160, consol AR p.216; Note 41, standalone AR p.171-172)

## NEW FINDING 5: AMW's acquisition date is pinned down, and the legal basis for subsidiary status is control-by-agreement, not majority shareholding as the operative clause

Form AOC-1 (AR p.239) states: **"Date since when subsidiary was acquired: 09-01-2024"** and **"Provisions pursuant to which the company has become a subsidiary: Section 2(87)(ii)"** of the Companies Act, 2013 — the "control of composition of the Board of Directors" / agreement-based limb, not Section 2(87)(i) (holds a majority of total voting power). AOC-1 separately confirms 100% shareholding. In substance this changes nothing (100% ownership plus control either way), but the specific clause chosen is consistent with control having been established via the NCLT resolution-plan mechanism (company memory LBF4) potentially ahead of, or alongside, full share transfer — a data point worth carrying into Stage 3/5's verification of the LBF4 gain trail, since it fixes the exact date (09-Jan-2024) against which the FY24 exceptional gain and its P&L/equity treatment should be checked in the FY25 AR (not held in this corpus). 🟢 informational, not a flag on its own.

## NEW FINDING 6: AMW's net-asset figure is not the same number in two places in the same AR

Form AOC-1 (AR p.239): AMW standalone Share capital Rs 500.00 lakh + Reserves & surplus Rs 7,098.32 lakh = **Rs 7,598.32 lakh net assets**.
Consolidated Note 53 (Schedule III additional information, AR p.237): AMW's **Net Assets (consolidated basis) FY26 = Rs 7,061.17 lakh** (3.91% of consolidated net assets).

Gap: Rs 537.15 lakh (Rs 5.37 Cr), unreconciled anywhere. Plausible source is a consolidation/purchase-accounting adjustment (e.g., elimination of the Rs 270 lakh intercompany security deposit from New Finding 4, or a fair-value adjustment carried from the original acquisition accounting), but the AR states neither the adjustment nor its components. Small in absolute terms; noted because it sits inside the same cluster of AMW-related figures (New Findings 1, 2, 5) that already carries the AR's largest disclosure gaps. 🟡 Watch.

## NEW FINDING 7: Authorised, unissued optionally-convertible preference share capital, Rs 17.40 Cr, sits on the balance sheet structure both years with no narrative anywhere

Note 18 (standalone AR p.162, consol AR p.217-218): Authorised capital includes **12,00,000 Preference shares of Rs 145/- each, "Optionally Convertible cumulative or Non Cumulative," Rs 1,740.00 lakh (Rs 17.40 Cr)**, unchanged both years. Issued/Subscribed/Paid-up capital is equity shares only — no preference shares have ever been issued ("the Company has not issued any preference shares until now," Note 18(b)). This is legal shelf capacity, not a live instrument, and is not itself concerning. It is a new data point (Pass 1 did not extract the authorised-capital breakdown) worth carrying forward as background: the company has standing board/shareholder authorisation to issue convertible preference capital at a fixed Rs 145 coupon-reference price without a fresh AGM resolution, which is optionality Stage 8/11 should be aware exists on the cap table even though unused. 🟢 informational.

## NEW FINDING 8: The two-year (not one-year) trend behind the working-capital and leverage findings

Note 48(e) Liquidity risk (standalone AR p.178-179, consol similar) discloses a three-year table Pass 1's Finding 7 did not use in full — it carries an FY24 column Pass 1's payables/borrowings sections did not quote:

| | FY24 | FY25 | FY26 | FY24-25 | FY25-26 |
|---|---|---|---|---|---|
| Trade Payables | Rs 59,990.81 lakh | Rs 75,207.53 lakh | Rs 1,00,177.23 lakh | +25.4% | +33.2% |
| Borrowings | Rs 1,04,793.17 lakh | Rs 82,743.37 lakh | Rs 82,590.12 lakh | -21.0% | -0.2% |

Two things this adds to Pass 1's read:
1. **Trade payables have grown for two consecutive years, accelerating** (+25.4% then +33.2%), not a single-year event — a stronger multi-year corroboration of Pass 1 Finding 7/8 (working-capital strain, MSME overdue-and-unpaid near-doubling) than a one-year snapshot suggests.
2. **The deleveraging Pass 1's Finding 10 credited to FY26 (Net Debt/EBITDA 1.65x to 1.57x) actually happened in FY24-to-FY25** (borrowings fell 21.0%) **and has since stalled** (FY25-to-FY26 borrowings essentially flat, -0.2%). The mild further Net Debt/EBITDA improvement in FY26 is an EBITDA-growth effect (Rs 500.25 Cr to Rs 522.96 Cr, Note 49), not continued balance-sheet deleveraging. Read together with Finding 8's accelerating payables growth, the FY26 leverage-ratio improvement is a thinner result than the headline ratio alone suggests. (Note 48(e), standalone AR p.178-179)

Rating: 🟡 Watch (refines Pass 1 Findings 7 and 10; no new number contradicts Pass 1, but the trend shape changes the read).

## NEW FINDING 9: "Interest Others" opacity is structural, not a sudden FY26 jump

Pass 1 Finding 4 flagged "Interest Others" of Rs 69.85 Cr (Note 35) as 1.4x disclosed bank interest, with no sub-note breakdown. Pass 2 adds the FY25 comparative Pass 1's report text did not carry into its finding: **Rs 65.02 Cr FY25 to Rs 69.85 Cr FY26, +7.4% YoY** — both standalone and consolidated (Note 35, standalone AR p.169, consol AR p.224). The opacity is real and unchanged: no sub-note breaks this line down in either year. But the magnitude of the *unexplained* line is not accelerating; it is a stable, large, structural feature of the finance-cost note across at least two years, which changes the framing from "a growing risk" to "a persistent disclosure gap that should have been closed by now, in either year." 🟡 Watch (refinement, not escalation).

## NEW FINDING 10: RPT table completeness — two immaterial FY25-only lines, and the power-payable outstanding total Pass 1 slightly understated

Two RPT lines exist in the full Note 41 table (standalone AR p.171) that Pass 1's summary table did not carry as separate rows (their net effect was already captured in Pass 1's column totals, so the FY25 total of Rs 5,885.61 lakh is unaffected — this is a completeness note, not a correction to any total):
- "Sale of Machinery & Equipment" to the Subsidiary column: Rs 8.55 lakh FY25, nil FY26.
- "Purchase of Goods," Associate/Others columns: Rs 37.15 lakh FY25, nil FY26.
- "Investment," Subsidiary column FY25: Rs 693.10 lakh — this is the same Rs 693.09 lakh (rounding) further investment in Clean Max Astria that consolidated Note 6 separately discloses as the FY25 equity-method step-up (Note 6, consol AR p.215-216). The two notes tie out exactly; worth stating as a positive cross-check, not previously connected across notes in Pass 1.

One correction: Pass 1 reported "Payables for purchase of power to CMAPL (associate): Rs 135.24 lakh (FY26) vs Rs 79.16 lakh (FY25)" as the full outstanding balance. The AR's outstanding-balances table actually shows a **combined total of Rs 163.67 lakh FY26** (Rs 135.24 lakh to the associate CMAPL plus Rs 28.43 lakh in the "Others" column) **against Rs 79.16 lakh FY25** — Pass 1 omitted the Rs 28.43 lakh "Others" component. Immaterial in absolute terms; noted for completeness. (Note 41, standalone AR p.171-172)

## Carry-forward items checked with no new finding (confirmed closed/empty on re-read)

- **R&D capex/opex split (Note 3(4)/5(5))**: re-read, no new information beyond Pass 1's extraction; the FY25 Mehsana capex spike and FY26 normalisation is fully and consistently disclosed across both notes. No further note connects to it.
- **Leave-encashment 12.4x non-current provision jump (Note 22/28, standalone/consol identical)**: re-read Note 22, Note 28, Note 43 (gratuity), and Note 51 (deferred tax on leave encashment) in full. No note anywhere explains the jump from Rs 30.28 lakh to Rs 374.39 lakh (non-current). The deferred-tax note (Note 51) shows the DTA on leave encashment provision actually *shrank* (Rs 102.21 lakh to Rs 39.31 lakh liability-side), which is consistent with a reclassification between current and non-current buckets rather than a genuine change in the total obligation, but no note states this explicitly. **Remains an open, unexplained item — carry to Stage 3/5.**
- **CSR routed through Hansraj Trust (Note 45D)**: re-read in full (standalone and consolidated, identical). Fully disclosed mechanics, immaterial shortfall (Rs 0.32 lakh). Nothing new; Pass 1's 🟡 (structure, not quantum) stands.
- **Missing warranty provision roll-forward**: confirmed by full-text search of the entire AR for "warranty" — the accounting policy exists twice (standalone Note 2.09(g), AR p.150-151; consolidated equivalent, AR p.205-206, both describing an assurance-type Ind AS 115/Ind AS 37 warranty provision measured on historical claim percentage) but **no provision balance, movement table, or roll-forward appears in Note 22, Note 28, or anywhere else** in either statement. This is a genuine disclosure gap for an auto-component OEM supplier with an explicit warranty accounting policy and no visible warranty liability. 🟡 Watch (confirmed, not new, but now exhaustively verified rather than inferred from absence).
- **Absence of subsequent-events note**: confirmed again by full-text search ("subsequent," "events after," going-concern language). No subsequent-events note format exists anywhere in the document, standalone or consolidated; only boilerplate going-concern language in the Board's/Directors' Responsibility Statement and the auditor's report exists ("they have prepared the annual accounts on a going concern basis"). No material-uncertainty-related-to-going-concern paragraph appears in either auditor's report. 🟡 process observation stands, unchanged from Pass 1.
- **AMW AOC-1 "Turnover: 0"**: re-confirmed verbatim in the source text (Note "Turnover 0," AR p.239). No note anywhere in the standalone or consolidated notes provides AMW's own revenue figure separately, and no note explains why an operating subsidiary shows nil turnover. **Remains unresolved — carry to Stage 3/5** (New Finding 5's acquisition-date/AOC-1 detail is adjacent context, not a resolution).

---

## PASS 2 NEW FINDINGS SUMMARY

| # | Finding | Note anchor | Rating | Relation to Pass 1 |
|---|---|---|---|---|
| 1 | Consolidated retained earnings fell not from losses but from two straight years of oversized, unexplained reserve transfers (Rs 674.68 Cr to General Reserve FY25, Rs 364.52 Cr to Capital Reserve FY26); "Capital Reserve" is omitted from the note's own reserve-purpose list | Note 19, consol AR p.219-220 | 🔴 Red Flag | Expands Finding 1 materially |
| 2 | Second unexplained consolidation-only reserve: Capital Revaluation Reserve Rs 34.84 Cr excess over standalone, static both years, contradicts the AR's own "no revaluation" declaration | Note 19 vs Note 53(X)/55(X), AR p.164/182/219-220/237 | 🔴 Red Flag | New |
| 3 | Note 6(II) impairment-assessment cross-reference (Note 52(C)) contains no impairment methodology, only associate summary financials | Note 6(II)/52(C), consol AR p.215-216/236-237 | 🟡/🔴 | Confirms and sharpens Pass 1's 🟡 |
| 4 | Note 8 standalone-vs-consol security deposit gap (Rs 269.20 lakh) resolved: intercompany deposit to AMW eliminates on consolidation | Note 8/41, AR p.160-161/171-172/216 | 🟢 Resolved | Closes a Pass 1 carry-forward item |
| 5 | AMW acquisition date 09-01-2024, subsidiary status via Section 2(87)(ii) (control-by-agreement clause) | AOC-1, AR p.239 | 🟢 informational | New; strengthens LBF4 evidence base |
| 6 | AMW net assets differ Rs 5.37 Cr between AOC-1 (Rs 75.98 Cr) and consolidated Note 53 (Rs 70.61 Cr), unreconciled | AOC-1 p.239 vs Note 53 p.237 | 🟡 Watch | New |
| 7 | Authorised, unissued optionally-convertible preference capital Rs 17.40 Cr, unused both years | Note 18, AR p.162/217-218 | 🟢 informational | New |
| 8 | Trade payables growth is a two-year accelerating trend (+25.4% then +33.2%); FY26 leverage improvement is an EBITDA effect, not continued deleveraging (borrowings flat FY25-FY26 after a 21% FY24-25 fall) | Note 48(e), AR p.178-179 | 🟡 Watch | Refines Findings 7, 10 |
| 9 | "Interest Others" opacity (Rs 69.85 Cr) is a persistent two-year structural gap (+7.4% YoY), not an accelerating one | Note 35, AR p.169/224 | 🟡 Watch | Refines Finding 4 |
| 10 | RPT table completeness: two immaterial FY25-only lines; power-payable outstanding total corrected to Rs 163.67 Cr (not Rs 135.24 Cr) | Note 41, AR p.171-172 | 🟢 minor correction | Refines Finding 6/RPT section |

**No material new finding on**: R&D capex/opex trend, CSR-trust structure, warranty-provision absence (confirmed, not new), subsequent-events absence (confirmed, not new). **Still unresolved, carried to Stage 3/5**: the 12.4x leave-encashment provision jump; AMW's "Turnover: 0" AOC-1 line.

PASS 2 rating tally (new items only): 🔴 Red Flag = 2 (New Findings 1, 2); 🟡 Watch = 5 (New Findings 3, 6, 8, 9, plus the confirmed warranty gap); 🟢 informational/resolved = 3 (New Findings 4, 5, 7, 10).
