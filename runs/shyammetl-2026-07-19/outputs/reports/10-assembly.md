# STAGE 10: VALUATION INPUT ASSEMBLY
## Shyam Metalics & Energy Limited (SHYAMMETL)
**Run Date:** 2026-07-19 | **Model:** claude-haiku-4-5 | **Status:** complete

---

## COMPANY IDENTITY BLOCK

| Field | Value | Anchor |
|-------|-------|--------|
| Company | Shyam Metalics & Energy Limited | manifest |
| Ticker | SHYAMMETL | manifest |
| Business Model Type | Manufacturing (integrated metals producer, commodity-cyclical) | (B04, one_line_verdict) |
| Sector | Commodity-cyclical integrated steel | fttcp-deliberation p.4 (sector cap override; manifest "Pharma / CDMO" 38x rejected) |
| Sector Cap Row | 20x flat | fttcp-deliberation p.4, operator confirmed |
| CMP | Rs 1,022/share | manifest |
| Market Cap | Rs 28,541 cr | manifest |
| Shares Outstanding (diluted) | 27.92 cr shares | calculated from FY26 EPS 38.70 and PAT 1,070.24cr (results Q4 FY26 p.10) |
| Enterprise Value | Rs 28,520.61 cr | mcap 28,541 + net cash (-20.39) (B12a verified) |
| Net Debt Position | Net cash Rs 20.39 cr | (B12a confirmed, audited balance sheet results Q4 FY26) |

---

## LATEST-PERIOD FINANCIALS (FY26 CONSOLIDATED, YEAR ENDED 31-MAR-2026)

| Field | Value | Anchor |
|-------|-------|--------|
| Revenue from Operations | Rs 18,552.21 cr | Statement of audited consolidated P&L, results Q4 FY26 p.10, line 1 |
| EBITDA | Rs 2,536.65 cr | Audited consolidated P&L, results Q4 FY26 p.10, line 3 (Earnings BIDIT) |
| PAT (Profit after tax, owners) | Rs 1,070.24 cr | Audited consolidated P&L, results Q4 FY26 p.10, line 14 |
| CFO (Operating Cash Flow) | Rs 2,023.56 cr (FY26); Rs 1,713.43 cr (FY25) | Audited consolidated Cash Flow Statement, results Q4 FY26 p.12 |
| Capex (PPE+Intangibles) | Rs 2,637.24 cr (FY26); Rs 2,148.32 cr (FY25) | Audited consolidated Cash Flow Statement, results Q4 FY26 p.12 |
| FCF (Free Cash Flow) | Rs -613.68 cr (CFO - Capex) | Derived: 2,023.56 - 2,637.24 = -613.68 (results Q4 FY26 p.12); negative due to heavy capex |
| Depreciation & Amortization | Rs 248.51 cr | Audited consolidated P&L, results Q4 FY26 p.10, line 8 |
| Diluted EPS | Rs 38.70 | Audited consolidated P&L, results Q4 FY26 p.10, line 17(b) |
| Book Value per Share | Rs 402.56 | Equity 11,244.52cr / 27.92cr shares (from mcap/CMP) |
| Total Equity (excl. NCI) | Rs 11,244.52 cr | Audited consolidated Balance Sheet, results Q4 FY26 p.11 |
| Current Ratio | 0.997x | (B01, audited financials constraint) |
| EBITDA Margin | 13.67% | 2,536.65 / 18,552.21 (results Q4 FY26 p.10) |
| PAT Margin | 5.77% | 1,070.24 / 18,552.21 (results Q4 FY26 p.10) |
| ROCE (Latest, FY26) | 13.21% | (B12a verified) |
| ROCE 2-Year Trend | DECLINING (23.4% FY18 → 13.21% FY26) | (B01, gate0 verdict; fttcp-deliberation confirms TEMPORARILY DEPRESSED with RECOVERING forward at 40-60% probability) |
| ROE | 9.52% | PAT owners 1,070.24 / equity 11,244.52 (audited balance sheet & P&L, results Q4 FY26) |
| Interest Coverage | 8.61x | (B12a verified) |
| CFO/PAT (Latest) | 1.89x | 2,023.56 / 1,070.24 (results Q4 FY26 p.12, p.10) |
| CFO/PAT (Cumulative 9-year) | 1.35x | (B01 block_b_trend, strong cumulative basis) |
| FCF/PAT | -57.36% | -613.68 / 1,070.24 (negative due to capex phase) |
| P/FCF | NOT APPLICABLE | FCF negative (capex-heavy phase) |
| Revenue CAGR (3-year, FY24-26) | 22.12% | (B01 gate0 verdict_card_status, 9-year screener data) |
| PAT CAGR (2-year available, FY25-26) | 17.96% | 1,070.24 / 908.10 = 1.1796, so ~17.96% growth; FY24 data available but 3-year CAGR requires FY23 (unanchored) |
| DPS (Recommended) | Rs 2.70 per share | Board announcement, results Q4 FY26 p.1 (27% of face value Rs 10) |

---

## PREVIOUS PERIOD COMPARATIVES (FY25)

| Field | Value | Anchor |
|-------|-------|--------|
| Revenue from Operations (FY25) | Rs 15,137.50 cr | Audited consolidated P&L comparatives, results Q4 FY26 p.10 |
| EBITDA (FY25) | Rs 2,096.16 cr | Audited consolidated P&L comparatives, results Q4 FY26 p.10 |
| PAT (FY25) | Rs 908.10 cr | Audited consolidated P&L comparatives, results Q4 FY26 p.10 |
| Revenue Growth (YoY FY26/FY25) | 22.59% | (18,552.21 - 15,137.50) / 15,137.50 (results Q4 FY26) |

---

## FORWARD GUIDANCE & MANAGEMENT DELIVERY

| Field | Value | Anchor |
|-------|-------|--------|
| Guided Revenue Growth | 15-20% CAGR over next 2-3 years (escalated to ~30% for FY27 only in Q4 call) | (B05, guidance table; raised unreconciled in Q4 FY26 call vs Q2/Q3 repeated 15-20% guidance) |
| Guided EBITDA Margin Improvement | +200 to +300 bps | (B05, guidance table, Q2 FY26 call) |
| Credibility Grade | B (Good) | (B05, credibility_grade) |
| Credibility Basis | Core capex milestones (Ramsarup blast furnace, CRM Phase II) delivered on exact quarter promised with disciplined tracking every call; PLI stainless and flange beam triggers went silent; 90 MW captive power plant never explicitly confirmed as commissioned in Q4; management deflected substantively on Q4 FY26 ED coal notice; FY27 growth guidance escalation unreconciled | (B05, credibility_basis) |
| Top 2-3 Growth Triggers | (1) Aluminium FRP + foil ramp (Sambalpur/Pakuria), M-H conviction, near-medium term; (2) CRM Phase II Jamuria (color-coated/CR coil), H conviction, near-term; (3) Safeguard duty / pricing discipline, M conviction, near-term | (B05, triggers table) |

---

## EARLIER-STAGE ANALYSIS CARRY-FORWARDS

| Field | Value | Anchor |
|-------|-------|--------|
| EM Score | 30 | (B07, em_score) |
| EM Classification | STRENGTHENING | (B07, combined_assessment categorizes as TURNAROUND due to Gate 0 AVOID paired with EM STRENGTHENING) |
| Evidence Quality Mix | Mixed (19 documented, 10 claim, 6 inference) | (B07, evidence_mix) |
| Primary Catalyst & Proximity Window (12m) | Aluminium FRP plant (60,000 TPA) commercial launch end-Sep-2026; Wagon plant Phase-I at Kharagpur Sep-2026; DRI 0.5 MTPA during FY27 (by Mar-2027) | (B07, catalysts_12m) |
| Strategic Asset / Monopoly Position | YES, with multiple anchors: (1) Cost leadership via backward integration & captive power (durable, ~20yr built); (2) Niche scale in ferro alloys, aluminium foil, sponge iron, pellets; (3) Emerging brand SEL Tiger TMT (weak); (4) Technology partnerships (Danieli stainless mill, Achenbach foil, German Thermex CSP); (5) Distribution moat across 40 countries; (6) Regulatory tailwinds (safeguard duty 12% provisional, PLI stainless benefit already lapsed per B05/B07 dropped triggers). Note: R1 regulatory tailwind at-risk (duty provisional, PLI dropped). | (B04 moats_present, B07 active_categories A1/H2) |
| Gate 0 Classification | AVOID (Core Score 34/100) | (B01, classification: AVOID; deal-breakers Block A<8 and Block B<8 cap max GOOD; Block E scored 0 on shareholding data absence, artificially depressing grand_total) |

---

## TAM / SOM / REVENUE RUNWAY

| Field | Value | Anchor |
|-------|-------|--------|
| TAM (Conservative) | Rs 424,060 cr | (B09, tam_cr conservative) |
| TAM (Realistic) | Rs 484,690 cr | (B09, tam_cr realistic) |
| SAM (Addressable Market) | Rs 381,654 cr (90% of realistic TAM) | (B09, sam_cr) |
| Current SAM Share | 4.86% | (B09, current_sam_share_pct) |
| Revenue Headroom | 20.6x | (B09, revenue_headroom_x; i.e., potential revenue growth multiplier relative to current position within SAM) |
| SOM 3-Year (FY26-29) | Rs 28,090 cr | (B09, som_3yr_cr) |
| SOM 5-Year (FY26-31) | Rs 33,815 cr | (B09, som_5yr_cr) |
| SOM-Implied Revenue CAGR (3-year) | 14.8% | (B09, som_implied_revenue_cagr yr3) |
| SOM-Implied Revenue CAGR (5-year) | 12.7% | (B09, som_implied_revenue_cagr yr5) |
| Management's FY31E Revenue Target | Rs 42,500 cr | (B09, mgmt_claim_cr; represents 18% CAGR FY26-31, above bottom-up 12.7% SOM CAGR) |
| Capacity Gap Alert | Gap of ~Rs 8,500cr between bottom-up 5yr SOM (33,815cr) and mgmt FY31E (42,500cr); management's plan more optimistic, concentrated in stainless steel volume ramp (94,102t FY26 → 699,733t FY31E vs 0.6 MTPA nameplate). Flagged for stage 11 revenue assumption cross-check. | (B09, capacity_check) |
| TAM Growth % | 7% | (B09, tam_growth_pct) |

---

## RATING PDF EXTRACTION

| Field | Value | Anchor |
|-------|-------|--------|
| Rating Agency | CRISIL | ratings.pdf p.1 title |
| Long-Term Rating | AA+ / Stable (upgraded from AA/Positive) | ratings.pdf p.1 rating action table; "Long term rating upgraded to 'Crisil AA+/Stable'" |
| Short-Term Rating | Crisil A1+ (reaffirmed) | ratings.pdf p.1 rating action table |
| Rating Date | November 05, 2025 | ratings.pdf p.1 header |
| Outlook | Stable | ratings.pdf p.1 rating action table |
| Working Capital Commentary (Verbatim) | "Working capital management has been prudent. The group sells mainly on advance/letter of credit basis, leading to low receivables of 15-30 days. Inventory, at 70-90 days, mainly comprises raw materials. While the group does not have captive iron ore mines, its proximity to raw material sources and setting up of railway siding gives it access to iron ore at competitive rates because of lower logistics cost, thereby supporting profitability." | ratings.pdf p.2, Key Rating Drivers - Strengths section: "Healthily operating efficiency driven by integrated operations and prudent working capital management" |

---

## VERIFIER-A SOURCE-FIDELITY CORRECTIONS (NON-OVERRIDABLE)

Applied from (B12a) and per the AUTHORITATIVE DELIBERATION RECORD:

| Item | Correction | Severity | Use-Case | Anchor |
|------|-----------|----------|----------|--------|
| CARO cash-loss entity count | Was 11 of 13; corrected to 10 of 13 (Verifier A per-entity list at AR PDF p.233) | CRITICAL | B02 red_flags, top_findings rank 4 (qualitative conclusion systemic losses unchanged) | (B12a corrections_applied, severity CRITICAL) |
| Standalone related-party trade receivables | Was 729.52cr (78.1%); corrected to 726.53cr (77.77% of 934.39cr) | MAJOR | B02 red_flags rank 6, immaterial 0.33pp (audited Note 42 standalone) | (B12a corrections_applied, severity MAJOR) |
| FY26 raw-material ratio | Was ~72% (Investor Presentation p.57, deck bundling); corrected to 73.68% (13,680.15cr / 18,552.21cr audited P&L) | MAJOR | B04 flags, audited figure authoritative vs deck | (B12a corrections_applied, severity MAJOR source-basis) |
| Promoter cross-holding combined stake | Confirmed 35.18% (Narantak 15.48% + Subham Capital 14.61% + Dorite 5.09%, AR Note 18e) NOT 65% (B03 wrong) | MAJOR | B02 top_findings rank 5, circular related-party structure | (B12a cleared_on_recheck, verdict MATCH, anchor AR Note 18e) |
| SSPL entity share in consolidated profit | FY24 722.34cr → FY25 417.15cr (Note 47 entity-wise table at AR p.298-302; extraction legibility limit, not fabrication) | RENDERING LIMIT | B02 top_findings rank 2 (identifies where consol PAT decline occurred); source-supported but verifier-unconfirmed, re-read phase 3 | (B12a rendering_limited_anchor_not_found) |
| Consolidated equity investment (cross-holding) | Standalone 253.05cr MATCHED; consolidated 352.31cr rendering limit (not fabrication) | RENDERING LIMIT | B02 top_findings rank 5; standalone figure carries | (B12a rendering_limited_anchor_not_found) |

---

## UNRESOLVED FIELDS (NO ANCHOR AVAILABLE)

| Field | Why | Where It Might Be |
|-------|-----|-------------------|
| FY27E EPS (forward earnings basis for exit multiple application) | Management has not quantified FY27E EPS; only FY27 revenue guidance (~30%) and prior guidance (15-20% CAGR) provided. Needed for 20x forward exit PE calculation. | Stage 11 valuation model must derive FY27E EPS from FY26 PAT (1,070.24cr) + growth assumption + margin normalization |
| Peer Financial Comparables (P/E, EV/EBITDA, P/B, Growth, ROCE medians) | Only 4 peers provided (GPIL, JAIBALAJI, SARDAEN, GALLANTT); zero coverage of stainless steel, aluminium, or nickel segments central to Shyam's forward thesis. Correct comparators (Jindal Stainless, Hindalco, NMDC Steel) not in provided set. | B06 flags as unverifiable; requires separate peer pull for Jindal Stainless, Hindalco, NMDC Steel FY26 financials |
| CWIP & Idle Capital as % of Capital Employed | Needed to determine Pillar 1 normalization route (Route A operational ROCE if >20% vs Route B pre-cycle normalized). Deliberation states "exact CWIP figure was NOT anchored this run and must be pulled from balance sheet." | Audited balance sheet Note on CWIP/Construction WIP; balance sheet extracts provided in results Q4 FY26 (blocks section 6c showing Capital work-in-progress 106.47cr at Mar-26 vs 71.62cr at Mar-25) |
| Three-Year PAT CAGR (requires FY23 PAT) | Available: FY25 908.10cr, FY26 1,070.24cr (2-year = 17.96%). FY24 1,034.79cr per B02 available but FY23 data in B12a "data years 9 FY18-26" not extracted for B10. | B01 / screener historical data (9-year series FY18-26 exists but not extracted to B10 for FY23) |
| P/FCF (Price-to-Free-Cash-Flow Multiple) | FCF negative (FY26: -613.68cr) due to capex-heavy phase. P/FCF not computable on negative FCF. | Standard valuation metric inapplicable during capex cycle; relevant only post-commissioning (FY27+) |
| Strategic Asset / Monopoly: Durability and Defensibility Scores | B04/B07 provide qualitative "Strong" / "Moderate" / "Weak" ratings per category (A1, B1, etc.), but no numeric scoring for defensibility duration. | Qualitative assessment sufficient for equity story; quantified only at EM-score level (B07 em_score 30) |
| Peer Medians for Sector P/E Range | No sector-level P/E median provided for commodity-cyclical integrated steel. Operator elected 20x as sector cap ceiling with no computed median context. | Section 1B v3.3 (frameworks/ Master v3.3) may carry sector cap justification; 20x is operator-approved floor, not validated against sector peer set |
| Contingent Liabilities Quantum & Resolution Status | B02 flags two unreconciled cross-note discrepancies (subsidy claim Rs41.83cr vs Rs57.16cr; electricity duty Rs59.17cr vs Rs54.17cr) in the AR. CPCB closure direction at Rengali (Apr 2026) with 3-month remediation window noted but quantum of potential costs unanchored. | AR Note 16 (subsidy), Note 41c (electricity duty), AR CARO table p.255, B08 / B02 flags; phase 3 follow-up needed for remediation cost impact |

---

## FOUR-PILLAR INPUTS (FROM AUTHORITATIVE FTTCP DELIBERATION RECORD)

Per fttcp-deliberation.md, operator-approved and non-negotiable for Phase 3 (stage 11):

| Pillar / Input | Approved Value | Anchor | Notes |
|---|---|---|---|
| **Pillar 1: ROCE Forward Verdict** | RECOVERING at 40-60% probability over 12 months | fttcp-deliberation p.2, line 10; section "Final Rulings" | Sole authority for Pillar 1 ROCE selection per CLAUDE.md ("Never use any exit PE from outside Section 1B v3.3..."). Verdict carries forward. FTTCP v1.2 Pillar 1 table determines blend weighting (current vs FY[Y+2]). |
| **Pillar 1: Normalization Route TBD** | Route A (operational ROCE) if CWIP + idle capital >20% of capital employed; else Route B (pre-cycle normalized ~20% capped at evidenced level, unwind catalyst = commissioning schedule) | fttcp-deliberation p.4, line 67; Section "Operator-Approved Valuation Pillars" | Route A governs if both conditions hold. CWIP exact figure NOT anchored this run — must pull from audited balance sheet. Capital Employed per B12a computed as proxy (Equity+Reserves+Borrowings). |
| **ROCE Recovery Credited Via** | Pillar 1 (single credit rule enforced) | fttcp-deliberation p.4, line 68 | Strategic Premium ROCE re-rating route is BARRED. No double-credit. |
| **Pillar 2: Cash Multiplier** | 1.0x (provisional) | fttcp-deliberation p.4, line 69 | Growth-induced determination: consolidated conversion strong ~1.9x; standalone drain intra-group. Superseded in effect by flat 20x exit PE election below, but recorded for pillar audit trail. |
| **Pillar 3: Growth & Moat Premium** | ~+3x total (+3a +2x on capex-embedded growth & Grade B delivery; +3b +1x on EM 30 STRENGTHENING provisional; +3c 0x duration) | fttcp-deliberation p.4, line 70 | Within +6x cap. EM 30 STRENGTHENING per (B07). Capex-embedded growth 150% per (B07 capex_embedded_growth_pct). |
| **Strategic Premium** | 0x | fttcp-deliberation p.4, line 71 | No additional premium beyond pillars. |
| **Undiscovered Alpha Multiplier** | NOT APPLIED | fttcp-deliberation p.4, line 72 | FII + DII ~16.7% (operator context, non-anchored) exceeds 3% institutional-absence ceiling. UA not available. |
| **Return Hurdle Tier** | Tier A, 25% hurdle | fttcp-deliberation p.4, line 73 | FII+DII >3% would allow Tier B, but promoter CONCERN verdict fails Tier B quality gate (per B08 promoter FLAG-PROMOTER CONCERN due to ED-PMLA attachment on subsidiary + CPCB closure action). |
| **Sector Cap Row** | 20x (operator confirmed) | fttcp-deliberation p.4, line 74 | Commodity-cyclical integrated steel per operator deliberation. Manifest "Pharma / CDMO" 38x OVERRIDDEN. Do not carry manifest sector row. |
| **Approved Destination (Exit) PE Base** | 20x FLAT | fttcp-deliberation p.4, line 75; Override 1 p.32 | Operator elects sector cap ceiling over computed ~17.7x additive / ~15-16x RRM. Single flat exit multiple; both computed tracks superseded. +2.3x uplift from computed 17.7x to 20x sector cap. |
| **Earnings Basis** | FORWARD (one-year-forward, FY27E EPS) | fttcp-deliberation p.4, line 76; Override 2 p.36 | Operator ruling: "use forward earnings" / "yes, forward earnings, write the deliberation record." Fits cyclical business mid-ramp; trailing FY26 EPS understates because commissioned capacity not yet fully earning. |
| **Operator Adjustment to PE** | +2.3x from 17.7x computed to 20x cap, reasoning operator discretion | fttcp-deliberation p.4, line 77; Override 1 reasoning p.34 | Recorded as operator election of sector ceiling; reasoning left to operator discretion. |
| **SHARED CATALYST Flag** | YES | fttcp-deliberation p.4, line 78; p.23 | Capex commissioning drives BOTH Pillar 1 ROCE recovery AND Pillar 3a growth premium. Single point of failure. Role 3 stress test required. |

---

## FTTCP VERDICT SUMMARY (AUTHORITATIVE CARRY-FORWARD)

**Disposition:** CONSTRUCTIVE TRANSITIONS, CAUTIOUS POSITION. Small sizing, strict entry, subject to Phase 3.

**Composite Transition Score:** 5 out of 8 (BUY-candidate band per FTTCP v1.2), unchanged. (fttcp-deliberation p.19, line 11)

**Key Risks to Thesis:**
1. Live ED-PMLA provisional attachment on subsidiary SSPL (Rs 159.51cr, coal-mining investigation, 15-Apr-2026) — unresolved. (B08, fttcp-deliberation honesty consequence p.50)
2. Capex execution risk: 76% of consolidated capex (Rs 10,617cr of Rs 13,902cr) unexecuted with commissioning dates stretching to FY29. (B07 top_moat_risks)
3. ROCE recovery dependent on commissioned capacity converting to earnings; first signal is FY27 return on capital and core subsidiary (SSPL) profit stabilization. (fttcp-deliberation p.48-50)

**Honest Consequence on Record:** Even at 20x on forward earnings, hurdle math is tight. FY26 EPS ~38.5; FY27E at roughly 25-30% growth ~48-50; 20x forward implies fair value ~Rs 960-1,000, around or slightly below CMP Rs 1,022. Phase 3 / Role 1 computes actual entry and MoS. (fttcp-deliberation p.50)

---

## CONFLUENCE & QUALITY OF EVIDENCE

| Dimension | Assessment | Evidence |
|-----------|-----------|----------|
| **Data Completeness** | 77% (24 clean / 31 distinct numbers, per B12a acceptance_rate after rechecks) | B12a reconciliation; initial 64.3% depressed by 8 false ANCHOR-NOT-FOUND on first pass, rechecks cleared 5, corrected 3 |
| **Source Fidelity** | HELD (B12a source_fidelity_gate) | One CRITICAL mismatch (CARO count 11→10) corrected at source, non-verdict-card item. Zero fabrications. All Gate-0 Block A-D verdict-card inputs verified clean. |
| **Accounting Quality** | 5/10 | (B02, accounting_quality score) — Multiple red flags: FY24 PAT inflated by one-off Rs338.57cr tax-recognition item, ~23-36% PBT growth treasury/investment-income driven (not core operating), circular related-party structure, "single business segment" claim contradicted by Note 47 entity-level data, server-backup non-compliance, audit-scope limitation Q4 FY25, audit-trail gaps at multiple entities. |
| **Gate 0 Classification Impact** | AVOID (Core Score 34/100) | (B01) — Deal-breaker blocks (A<8 score 4, B<8 score 5) independently cap max classification at GOOD. Block E (0/20, shareholding & contingent liabilities absent) artificially depressed grand_total. Genuine depressors underneath: ROCE 23.4%→13.2%, EBITDA margin 20.85%→13.67%, FCF -434.89→-613.68cr, current ratio 0.997x. Classification should re-test once shareholding data available per (B01 flags). |
| **Valuation Thesis Alignment** | Transition-alpha play (TURNAROUND) with execution risk | Gate 0 AVOID + EM STRENGTHENING (B07) = transition pattern hunted. 76% capex unexecuted, commissioning dates to FY29, B05-graded B credibility with dropped PLI and unreconciled FY27 guidance. Genuinely evidenced but not yet confirmed. Capex-embedded growth embedded in Pillar 3a (fttcp-deliberation). |

---

## CONFLICT RESOLUTION (IF ANY)

No conflicts between upstream stages at the values selected for this table. B03 promoter cross-holding (65%, WRONG per Verifier A) was not selected; B02 correction (35.18%, CORRECT) carried. Raw-material ratio 72% (deck, WRONG) vs 73.68% (audited, CORRECT) — audited selected. No P/E or exit multiple conflicts; only sourced value is 20x operator-approved (no other submitted). No ROCE conflicts; forward verdict single source (fttcp-deliberation, RECOVERING 40-60%).

---

## MISSING DATA & NEXT STEPS FOR STAGE 11

1. **FY27E EPS**: Mandatory for 20x forward exit PE application. Stage 11 must derive from FY26 PAT + growth assumption + margin guidance normalization.
2. **CWIP Quantum**: Pull exact Capital Work-in-Progress from audited balance sheet to determine Pillar 1 normalization route (Route A vs B threshold 20% of capital employed).
3. **Peer Comparables**: Current peer set inadequate (stainless, aluminium, nickel exposure zero). Stage 11 should validate 20x sector cap vs actual comparable multiples for Jindal Stainless, NMDC Steel, Hindalco segments.
4. **Contingent Liabilities**: AR subsidy claim and electricity duty discrepancies (Rs 15.33cr, Rs 5.00cr gaps per B02) should be reconciled. CPCB Rengali remediation quantum and timing (3-month window from 13-Apr-2026) require follow-up.
5. **Promoter Matter Resolution**: ED-PMLA attachment on SSPL (live, unresolved) and CPCB compliance completion are live gate items. Stage 11 thesis weight depends on resolution confidence.

---

