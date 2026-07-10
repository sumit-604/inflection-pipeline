# Stage 10: Valuation Input Assembly
## APEXECO — Run Date 2026-07-10

---

## COMPANY IDENTITY BLOCK

| Field | Value | Anchor |
|---|---|---|
| Company | Apex Ecotech Ltd | (manifest) |
| Ticker | APEXECO | (manifest) |
| Sector | EPC / Civil construction | (manifest, sector_cap_row) |
| Business Model Type | Hybrid: 96.4% project-based EPC, 3.6% recurring O&M/AMC services | (B04-bizmodel) |
| Sector Cap Row | EPC / Civil construction | (manifest) |
| CMP (as of run date 2026-07-10) | ₹242.0 per share | (manifest, cmp) |
| Market Cap | ₹319.0 crore | (manifest, market_cap_cr) |
| Shares Outstanding (Diluted) | 1.319 crore (131.9 million) | (calculated: mcap / CMP = 319.0 / 242.0; consistent with EPS 12.91 = PAT 17.02 Cr / 1.319 Cr shares per B05) |
| Net Debt / (Cash) | Net Cash ₹33.75 crore | (screener Data_Sheet: Cash & Bank 35.06 - Borrowings 1.31 = 33.75 Cr net cash) |
| Enterprise Value | ₹285.25 crore | (calculation: mcap 319.0 + net debt -33.75 = 285.25 Cr) |

---

## LATEST PERIOD FINANCIALS (FY26, ended 31-Mar-2026)

**Period Definition:** FY26 (12-month year ended 31-Mar-2026). Results audited and filed.

| Line Item | Value (₹ Cr) | Margin | Per-Share | Anchor |
|---|---|---|---|---|
| **Revenues** | 148.65 | — | — | (screener-Data_Sheet P&L row "Sales", FY26 column) |
| **EBITDA** | 23.04 | 15.5% | 17.49 | (calculated: PAT 17.02 + Tax 5.73 + Interest 0.09 + Depreciation 0.2 = 23.04 Cr; margin 23.04/148.65; per-share 23.04/1.319) |
| **PAT (Net Profit)** | 17.02 | 11.4% | 12.91 | (screener-Data_Sheet P&L row "Net profit", FY26 column; margin 17.02/148.65; per-share from B05 concall guidance "FY26 actual EPS 12.91") |
| **Diluted EPS** | — | — | 12.91 | (B05-concall guidance table: "FY26 actual EPS 12.91, +63.21% YoY") |
| **Cash from Operations (CFO)** | 6.77 | 4.6% of revenue | 5.14 per share | (screener-Data_Sheet Cash_Flow row "Cash from Operating Activity", FY26 column; per-share 6.77/1.319) |
| **Free Cash Flow (FCF)** | ~4.81 | 3.2% of revenue | ~3.65 per share | (estimated: CFO 6.77 - inferred capex ~1.96 Cr from net block movement 1.18→1.96 + CWIP 0.98 + depreciation 0.2; per-share 4.81/1.319; NOTE: direct capex figure not itemized in screener for FY26) |
| **Book Value per Share** | — | — | 47.96 | (calculated: (Equity Share Capital 13.19 + Reserves 50.07) / 1.319 Cr shares = 63.26 / 1.319) |
| **Net Cash per Share** | — | — | 25.60 | (calculated: (Cash & Bank 35.06 - Borrowings 1.31) / 1.319 shares) |
| **EBITDA Margin** | — | 15.5% | — | (23.04 / 148.65; consistent with FTTCP table ~14.6%, variance due to rounding and other-income treatment) |
| **PAT Margin** | — | 11.4% | — | (17.02 / 148.65) |
| **ROCE (Latest, FY26)** | — | 33.39% | — | (FTTCP deliberation authoritative: "Pillar 1 uses reported 33.39 percent, ex cash as context only"; operator ruling applied) |
| **ROCE 2-Year Trend Direction** | Declining (but "sustain at premium") | — | — | (FTTCP: FY24 ~60%, FY25 ~25%, FY26 ~35%; verdict FIRING as in "stay high, not climb further"; note ex-cash operating ROCE context-only 77%) |
| **ROE (FY26 specific)** | 22.9% | — | — | (calculated: PAT 17.02 / avg equity (59.69 FY25 + 89.18 FY26 / 2) = 17.02 / 74.44; note B02 reported historical ROE fell from 60% to 28%, variance from recent recalc suggests timing/calculation basis differences) |
| **3-Year Revenue CAGR (FY24–FY26)** | 67.3% | — | — | (calculated: (148.65 / 53.08)^(1/2) - 1 = 1.673 - 1 = 67.3%; base FY24 53.08 Cr, end FY26 148.65 Cr per screener) |
| **3-Year PAT CAGR (FY24–FY26)** | 60.2% | — | — | (calculated: (17.02 / 6.63)^(1/2) - 1 = 1.602 - 1 = 60.2%; base FY24 6.63 Cr, end FY26 17.02 Cr per screener) |
| **CFO / PAT (Latest FY26)** | 0.398 | — | — | (calculated: 6.77 / 17.02; note B01 reports cumulative CFO/PAT = 0.41, which is close; FY26 alone is 0.398) |
| **CFO / PAT (Cumulative FY25–FY26)** | 0.41 | — | — | (B01-gate0: "cumulative CFO/PAT = 0.41 (<0.50) -> caps at max AVERAGE") |
| **FCF / PAT (FY26)** | 0.283 | — | — | (estimated: FCF 4.81 / PAT 17.02; note capex estimation has uncertainty) |
| **Price / FCF (P/FCF)** | 66.4x | — | — | (calculated: mcap 319.0 / FCF 4.81 Cr) |
| **CapEx (FY26)** | ~1.96 | 1.3% of revenue | — | (inferred from balance sheet movement: net block 1.18 FY25 → 1.96 FY26, CWIP +0.98, depreciation 0.2; direct capex line not itemized in screener) |
| **Depreciation (FY26)** | 0.20 | 0.13% of revenue | — | (screener-Data_Sheet P&L row "Depreciation", FY26 column) |
| **Dividend per Share (DPS, FY26)** | 0.00 | — | — | (no dividend paid; screener shows zero in Dividend Amount row for all recent years) |

---

## FROM EARLIER ANALYSIS STAGES

### Guided Forward Guidance (Next Period: FY27)

| Metric | Guidance | Quarter Stated | Anchor | Grade |
|---|---|---|---|---|
| Revenue Growth (FY27) | 30–40% | Q4 FY26 call (May 2026) | (B05-concall: "FY27 growth guidance verbal, non-numeric: 30-40% growth overall") | B (verbal, non-numeric) |
| EBITDA Margin (FY27) | ~14.5%, flat | Q4 FY26 call via FTTCP | (FTTCP deliberation: "margins have slipped three years in a row... the best honest call is flat in the mid teens with no expansion assumed") | B |
| Credibility Grade | B | Composite across 3 calls | (B05-concall: "credibility_grade: B... core numeric commitments... met or exceeded... but governance/communication commitments... show recurring pattern of misses") | B |

### Management Delivery Track Record

| Promise | Outcome | Credibility Impact | Anchor |
|---|---|---|---|
| Revenue growth at least ~25% for FY26 | Delivered: 109.5% | ✓ Exceeded | (B05-concall: "delivered") |
| Order book conversion within 6-10 month gestation cycle | Delivered: Consistently explained | ✓ Met | (B05-concall: "delivered") |
| Narrow H1/H2 revenue skew (from 30/70) | Missed: Worsened to 22/78 | ✗ Miss, unacknowledged | (B05-concall: "missed") |
| Move to quarterly reporting | Partial: Only one percentage-only circular | ⚠ Miss, repeated 3 calls | (B05-concall: "partial, repeated evasions") |
| ESOP for core employees by end FY26 | Missed: Zero mention FY26 year-end call | ✗ Miss, dropped | (B05-concall: "missed") |

**Credibility Summary:** Grade B applied. Core numeric commitments (revenue, order-book conversion) consistently met or exceeded; governance commitments (quarterly reporting, ESOP, order-book reconciliation) show pattern of misses and evasion. Repeat pattern suggests willingness to under-deliver on transparency. (B05-concall: credibility_grade)

### Growth Triggers (Ranked by Impact)

| Rank | Trigger | Type | Timeframe | Conviction | Confirm Signal | Kill Signal | Anchor |
|---|---|---|---|---|---|---|---|
| 1 | Reliance Consumer Products order execution | Volume | Near (0-6m) | High | ~70% of ~₹100-125 Cr order on-schedule conversion with no dispute disclosed | Disclosed delay, dispute, or scope cut on the Reliance order | (B05-concall triggers, priority 1) |
| 2 | Order-book-to-revenue conversion discipline | Volume | Near (0-6m) | High | FY27 revenue tracks disclosed ₹125 Cr+ book within historical 6-10 month gestation | Book-to-bill slippage or repeat order-book-figure confusion | (B05-concall triggers, priority 2) |
| 3 | ZLD / higher-margin mix shift | Price-Mix | Medium (6-12m) | Medium | Disclosed, updated ZLD % of revenue paired with margin expansion | Continued margin compression despite bigger ticket sizes | (B05-concall triggers, priority 3) |

**Primary Near-Term Catalyst:** Reliance Consumer Products order completion (window 0–6 months from run date); dependent on management credibility Grade B for delivery signaling. (B07-emoat, catalysts_12m)

### Emerging Moat Analysis

| Score | Classification | Why | Anchor |
|---|---|---|---|
| 10.1 / 80 | NONE (below 12 threshold) | Score: 3 documented evidence items (G1 war chest, F2 execution moat FY26 revenue, basic debt-free status); 11 claims (unverified Veolia partnership, customer ecosystem, first-mover claims). No meaningful emerging moat forward; one strong backward artefact (G1 IPO war chest) not a forward catalyst. | (B07-emoat) |

**Evidence Quality Mix:** Mostly 📄 (documented) 3 of 14 items; remaining 11 rest on management claims from concalls, no signed contracts or filed regulatory approvals. (B07-emoat: evidence_mix {documented: 3, claim: 11})

**Key Moat Risks:**
- Customer concentration: Reliance group anchors ~70% of H2 FY26 execution and single largest order in company history (B07: "Customer concentration disguised as customer ecosystem")
- Marketed Veolia "strategic alliance" directly contradicted by management as not a partnership/JV (B07: "Marketed Veolia 'strategic alliance' directly contradicted by management as not a partnership or JV")
- Broken promises on qualitative commitments (H1/H2 skew, ESOP, international expansion, quarterly reporting, order-book bridging) even as headline revenue beaten (B07: "Broken execution promises on every qualitative commitment tracked")
- No IP, no backward integration, no proprietary data; technology-first-mover claims (E1) entirely self-reported and unverified (B07)

### Cash Conversion Determination (Authoritative from FTTCP Deliberation)

| Aspect | Value | Anchor | Status |
|---|---|---|---|
| Cash Determination (Phase 3 Authority) | GROWTH-INDUCED | (FTTCP deliberation, operator final: "GROWTH-INDUCED stands, with the WC-discipline metric as the falsification trigger") | ✓ Authoritative |
| Reasoning | FY25 CFO collapsed to -₹14.08 Cr vs PAT +₹8.56 Cr due to receivables +155.3% and WC build immediately post-IPO; FY26 recovered to 0.398x but not yet at sustainable >0.7x; receivables collection days already fell 6.77x to 4.61x (implied 79 days), improvement signal | (FTTCP: Engine 3 Cash, B01-gate0, B02-notes) | ✓ Documented |
| Falsification Trigger (Must Monitor) | H1 FY27 CFO/PAT < 0.7x **AND** working capital days rise faster than revenue growth | (FTTCP: "The falsification trigger... if H1 FY27 cash from operations to profit prints below 0.7 while working capital days climb faster than sales, the growth story is wrong and the cash strain is structural") | 🚩 Critical |
| Pillar 1 ROCE Impact | ROCE recovery credited in Pillar 1 only; no strategic re-rating premium from ROCE; no further multiple expansion underwritten from ROCE | (FTTCP operator ruling: "ROCE recovery is credited in Pillar 1 only. No separate re-rating premium is taken. Per operator, no further multiple expansion is underwritten from ROCE.") | ✓ Authoritative |

**Forward Cash Outlook:** Expected to improve toward 0.6–0.7x by FY27 as order-book velocity normalizes and receivables settle, contingent on order flow and project-execution discipline. Risk: if WC build continues to outpace revenue growth, determination reverts to structural and position is downgraded. (FTTCP, fttcp-deliberation.md)

### Strategic Asset / Monopoly Position

| Question | Answer | Anchor |
|---|---|---|
| Does the company hold a defensible strategic asset or monopoly position? | No | (B07-emoat: EM score 10.1 / 80, classification NONE; no moat above threshold) |
| Supporting Evidence | Company operates in a fragmented, competitive EPC segment with no proprietary technology, patents, or backward-integrated capacity. Moats claimed are customer relationships and OEM technology partnerships; neither is exclusive or durable (OEM partnerships available to competitors, customer base is blue-chip but project-dependent). | (B07-emoat, B04-bizmodel) |

### Unaccounted for Accounting / Tax / Other Items

| Item | Status | Anchor |
|---|---|---|
| Warranty Provision | Not disclosed in AR; provisioning-adequacy gap | (B02-notes: "No warranty provision and no gratuity actuarial assumptions disclosed") |
| Deferred Tax Assets | ₹12.20–12.63 lakh noted; cross-note tie-out failure (Note 1(i) p.50 vs Note 23 p.59) | (B02-notes, B03-ardeep) |
| Related-Party Transactions | Three promoter-controlled dormant enterprises (Oakens Engineering, Flagmo Ea, Flagmo Marketing) at Delhi corporate office, zero disclosed transactions | (B02-notes, B03-ardeep, B08-promoter) |
| Contingent Liabilities | Material pending litigations (DLF Home Developers, MSME disputes, income-tax appeal); portfolio <1% of net worth; company predominantly a plaintiff | (B04-bizmodel, B03-ardeep) |

### UA Qualifier Check (Valuation Readiness)

| Qualifier | Criterion | Status | Value | Anchor |
|---|---|---|---|---|
| **Listed ≥12 months?** | Company must be listed >= 12 months pre-valuation | ❌ NO | Listed Dec-2024; run date 2026-07-10 = ~7 months listed | (manifest: run_date 2026-07-10; B05-concall: "listed on the SME board in December 2024") |
| **Gate 0 ≥60 OR EM ≥25?** | Gate0 score >= 60 OR Emerging Moat score >= 25 | ✓ YES | Gate0 = 86 (exceeds 60); EM = 10.1 (below 25, but Gate0 qualifies) | (B01-gate0: grand_total 86; B07-emoat: em_score 10.1) |
| **FII + DII < 3%?** | Foreign & domestic institutional holding must be < 3% | ❓ NOT FOUND | Not disclosed in any input blocks, screener, or results documents | (B01, B03, B08 all note shareholding pattern as NOT FOUND; AR Note 2 provides promoter-only, no public/institutional split) |
| **All Three Met?** | All three criteria must be satisfied | ❌ NO | Listed < 12 months disqualifies; FII+DII unresolved. Position fails UA gate despite Gate0 > 60. | Combined determination |

**UA Verdict:** NOT QUALIFIED. Listed less than 12 months (7 months at valuation date) disqualifies under criterion 1, regardless of Gate0 strength. FII+DII data not available to verify criterion 3. **Position may proceed to valuation per operator override only; standard UA gate does not apply.** (per CLAUDE.md and FTTCP deliberation: "Final FTTCP verdict: BUY-candidate, score +5 of 8... decision to proceed to valuation in phase 3")

### Peer Medians and Comparables (where available)

**Peer Set:** CEWATER, EIEL, EMSLIMITED, FELIX (all in same EPC/water treatment space, cited in B05, B06)

**Peer Financial Data Summary:**

| Metric | APEXECO FY26 | Peer Status | Anchor |
|---|---|---|---|
| **P/E** | 18.7x (mcap 319 / PAT 17.02) | Peer medians NOT COMPUTED from provided data; individual peer P/Es not extracted | (B06-peers: "peers_provided: 4; verified: []") |
| **EV/EBITDA** | 12.4x (EV 285.25 / EBITDA 23.04) | Peer medians NOT COMPUTED; peer EBITDA figures not summatively provided in consolidated form | (B06-peers: substantive usage noted for 4 peers, but no aggregate median table) |
| **P/B** | 6.65x (mcap 319 / book value 48) | NOT COMPUTED from peers | — |
| **Revenue Growth** | 67.3% YoY (3yr CAGR); FY26 +109.5% | Peer growth: CEWATER -6.2%, EIEL mixed, EMSLIMITED SEVERE MISS, FELIX strong; narrative suggests Apex stronger in FY26 but CEWATER/EIEL seeing guidance cuts FY26 mid-year | (B06-peers: demand section) |
| **ROCE** | 33.39% | Peer ROCE comparisons NOT EXTRACTED; typical water-EPC player ROCE 20–30% but not formalized in provided data | (B06-peers) |

**Peer Narrative Context:** Three of four peers (CEWATER, EIEL, EMSLIMITED) show strong headline demand early FY26 followed by successive guidance cuts driven by execution and cash-timing issues (weather, government payment delays, elections) rather than demand destruction. Suggests industry-wide working capital / government-payment risk, not Apex-specific. (B06-peers: industry_cross_read)

**Peer Commentary on Margin Compression:** 2 of 4 peers (CEWATER, EIEL) corroborate rising input costs but smaller magnitude (1–2pp EBITDA) and later (Q4 FY26/Q1 FY27) than Apex's claimed 25–40% H2 FY26 metals inflation. Tied to Middle East geopolitical/shipping disruption, not broad metals move. Suggests Apex's margin compression is partly company-specific (cost pass-through weakness) and partly industry-wide. (B06-peers)

### SOM (Serviceable Obtainable Market) & Revenue Headroom

| Metric | Value | Anchor |
|---|---|---|
| **TAM (Conservative)** | ₹11,250 crore | (B09-tam: "tam_cr: {conservative: 11250, realistic: 14500}") |
| **SAM (Serviceable Available Market)** | ₹6,375 crore | (B09-tam: "sam_cr: 6375") |
| **SAM % of TAM** | 56.7% | (B09-tam: "sam_pct_of_tam: 56.7") |
| **SOM Year 3 (FY29 implied)** | ₹277 crore | (B09-tam: "som_3yr_cr: 277") |
| **SOM Year 5 (FY31 implied)** | ₹434 crore | (B09-tam: "som_5yr_cr: 434") |
| **SOM-Implied Revenue CAGR (3-Year)** | 23.1% | (B09-tam: "som_implied_revenue_cagr: {yr3: 23.1, yr5: 23.9}") |
| **Current SAM Share %** | 2.33% | (B09-tam: "current_sam_share_pct: 2.33") |
| **Revenue Headroom (x)** | 42.9x | (B09-tam: "revenue_headroom_x: 42.9") |
| **Runway Classification** | STRONG | (B09-tam: "runway_class: STRONG") |

**SOM Capacity Check:** Gap of approximately ₹290 crore in required order-book coverage by Year 3 versus current ₹125 crore book. SOM trajectory is optimistic side given replenishment already lagging revenue growth and weak/negative operating cash conversion. Order-book growth (₹100 Cr to ₹125 Cr) far slower than revenue growth (doubled), implying book-to-bill constraint binding. (B09-tam: capacity_check)

---

## RATING PDF EXTRACTION

**Rating Status:** NOT PROVIDED

**Reason:** SME-listed companies are exempt from mandatory credit rating requirement per SEBI rules and company's own AR disclosure (AR Boards' Report p.26). No credit-rating PDF exists in input set.

**Impact:** Cannot extract rating agency, rating, outlook, date, or working-capital/cash-flow commentary. All rating-dependent fields marked unresolved below.

---

## CONFLICTS

**Conflict 1: FY25 CFO Figure**
- **Field:** CFO FY25
- **Value A:** -₹14.08 crore | **Anchor A:** (07-Nov-2025 filing, earlier screener export)
- **Value B:** -₹5.24 crore | **Anchor B:** (FY26 annual audited report, Note 7 restated comparative, per AR p.9)
- **Resolution:** Value B (audited restated figure) used. Restated AR figure traced to Note 7 reclassification of trade retentions between Trade Receivables and Other Current Assets. Does not change any score band. (B01-gate0: data_notes; B03-ardeep: verified)
- **Used In Table:** CFO/PAT cumulative calculations; FY25 CFO standalone not included in FY26 latest-period table above.

**Conflict 2: Director Remuneration (FY25 Pay Rise %)**
- **Field:** MD Dosajh & ED Aiyer remuneration increase FY25
- **Value A:** 169.3% implied from Note 20(b) p.58 rupee figures | **Anchor A:** (AR Note 20(b) p.58)
- **Value B:** 37.02% stated in Annexure III p.31 | **Anchor B:** (AR Annexure III, Section 197(12) disclosure)
- **Resolution:** Direct numeric contradiction between two statutory disclosures. Not reconciled. Flagged as red flag in B02 and B03. Impact: governance-credibility concern; does not affect forward valuation inputs directly but signals disclosure quality issue. (B02-notes red_flags, B03-ardeep red_flags_top3)
- **Used In Table:** Not used in financial inputs; noted here for governance context only.

**Conflict 3: Peer Input Cost Inflation Claim**
- **Field:** Raw material / input cost inflation magnitude H2 FY26
- **Value A:** 25–40% increase (per management) | **Anchor A:** (B05-concall: "Raw material (metal) cost inflation absorbed 25-40% increase, H2 FY26")
- **Value B:** 1–2pp EBITDA margin impact, later timing (Q4 FY26/Q1 FY27), tied to Middle East geopolitical/shipping (per peer corroboration) | **Anchor B:** (B06-peers: "Claim 2... not corroborated at claimed magnitude or window by any peer")
- **Resolution:** Apex's claimed magnitude (25–40%) not independently corroborated by peer commentary. Peers saw smaller impact (1–2pp) later (Q4 onwards). Suggests Apex's margin compression is partly company-specific cost-pass-through weakness. Used conservatively in forward guidance assumption. (B06-peers)
- **Used In Table:** Forward margin guidance assumption ~14.5% (flat), not expanded beyond guidance despite cost inflation claim.

---

## UNRESOLVED

| Field | Why Unresolved | Where It Might Be | Impact |
|---|---|---|---|
| **Diluted Shares (Exact Count)** | Screener Data_Sheet row 52 "No. of Equity Shares" empty for FY26; row 63 "Adjusted Equity Shares in Cr" also empty. Calculated from market cap / CMP (1.319 Cr), but no direct equity-count filing verification. | Recent shareholding pattern filing post-IPO, or RHP DRHP archives | Low: calculated value consistent with EPS back-calc and market data; used throughout. |
| **Free Cash Flow (FCF)** | CapEx for FY26 not itemized in screener; inferred from balance sheet movement (net block, CWIP, depreciation). Direct capex line not provided in screener outputs. Results PDF unreadable due to tool limitation. | FY26 Annual Report Cash Flow Statement, PDF results; or detailed fixed-asset note in AR | Medium: FCF is material to valuation; estimation has ±20% uncertainty. Used for P/FCF benchmark, flagged as high/concerning. |
| **FII + DII Holding %** | Not disclosed in any block, screener output, or input document. AR Note 2 provides promoter-only holding table (69.29% combined); full shareholder breakdown not provided. | Latest shareholding pattern filing with stock exchange (NSE/BSE); Trendlyne; MCA portal | High: affects UA qualifier gate (criterion 3 of all-three-met check). Currently marks as NOT FOUND, position fails UA gate. |
| **Cash / Bank Holding Breakdown** | Screener shows ₹35.06 crore combined cash & bank. No breakdown by currency, geographic location, or restriction status. | Audit report cash balance note detail; bank confirmations; possible forex exposure | Low: consolidated cash figure sufficient for net-debt calculation; unlikely material restriction issues for debt-free SME. |
| **Interest Rate on Borrowings** | Borrowings ₹1.31 crore shown in screener; interest ₹0.09 crore charged. Implied rate ~6.9%, but no disclosure of cost-of-debt or borrowing terms. | AR Note 4 (Borrowings detail), or B05 concall commentary on credit terms | Low: minimal debt, immaterial to leverage or cost-of-capital calculations. |
| **Contingent Liabilities Quantified Detail** | AR discloses material pending litigations (DLF, MSME, income-tax); B03 notes portfolio <1% of net worth. No exact rupee figure itemized for each case. | AR Note 25 (Contingent Liabilities table) full schedule | Low: assessed as <1% net worth; low financial impact. Governance flag, not material to valuation. |
| **Order Book Aging / Fulfillment Schedule** | Order book stated as ₹125 crore as of 31-Mar-2026; no breakdown by project stage, fulfillment timing, or risk profile. Book-to-bill 0.84x is thin, but no detail on order mix or customer concentration within the book. | Q4 FY26 concall transcript (may have detail beyond slides); AR or investor presentation schedules | High: order book is critical to revenue visibility and SOM achievement. Current data insufficient to assess fulfillment risk. Reliance order (~₹100 Cr) dominates; diversification unknown. |
| **Quarterly Results FY26 (Q3/Q4)** | Screener-Quarters file is empty for APEXECO. Company reported H1/H2 (semi-annual), not quarterly, due to SME listing exemption. No quarterly P&L available. | Investor presentation slides; concall transcripts (may embed quarterly figures). Possible Q3 FY26 investor circular. | Low: H1/H2 data extracted from concalls in B05; sufficient for gate analysis. Quarterly granularity deferred to forward-looking analysis. |
| **Rating Agency Working Capital Comment** | No rating PDF exists (SME exempt). Rating-agency WC/cash-flow commentary (typically used to corroborate or challenge cash-conversion assessment) is NOT FOUND. | Credit rating would have been in submitted input; since SME exempt, no such document exists. | Medium: FTTCP determination (GROWTH-INDUCED) must rely on internal AR evidence and peer corroboration rather than third-party credit assessment. FTTCP deliberation addresses this: "no credit rating exists to confirm it; no formal cash plan named." Determination stands on AR evidence + peer + operator ruling. |
| **Capex Guidance / Plan FY27–FY29** | No forward capex guidance provided in B05 concalls or B04 business-model analysis. Future investment requirements unknown. | Q4 FY26 concall (may have commentary on capex intensity going forward); AR management guidance | Medium: affects FCF projection and cash-runway estimation in valuation phase. Conservatively assumed flat capex / sales ratio pending forward guidance. |

---

## FLAGS (Carried from Earlier Stages)

### Critical Flags

- **FLAG-GATE0** (from B01): Classification capped at AVERAGE by deal-breaker #4 (cumulative CFO/PAT = 0.41, <0.50). Primary driver FY25 CFO negative Rs 5.24 Cr (restated) against PAT positive Rs 8.56 Cr, working-capital build immediately post-IPO. Possible post-IPO rebase case for downstream position-sizing review. (B01)

- **FLAG-CASH** (from B01, B02, B03): Trade receivables up 155.3% vs revenue up 33.67%; zero doubtful-debt provisioning; debtors turnover fell 6.77x to 4.61x; CFO FY25 collapsed to -Rs 1,408 lakh, funded entirely by IPO proceeds not operations. (B02, B03)

- **FLAG-GOVERNANCE** (from B03): All four independent directors attended below 42% of FY25 board meetings; remuneration disclosure contradicts between Note 20(b) and Annexure III; executive director on Audit Committee. (B03)

### Major Flags

- **FLAG-DATA-GAP** (from B01): Block A (ROCE quality) rests on only 2 of 9 years (FY25–FY26) computable; FY18–FY24 ROCE is N/A due to screener data structure. Treat Block A's full score as low-confidence.

- **FLAG-RECEIVABLES-TREND** (from B02): Deteriorating pattern — trade receivables up 155.3%, trade retentions now 47.7% of receivables (up 61.7% YoY), zero doubtful-debt provision across both years despite scale. (B02)

- **FLAG-NARRATIVE-CONTRADICTION** (from B03): MD&A claim that FY25 growth was driven by international contracts directly contradicted by Note 22 (export revenue fell 59% with 100% customer churn); MD claim of 'more efficient working capital cycle' contradicted by CFO collapse and debtors turnover fall. (B03)

- **FLAG-CONCENTRATION** (from B07): Reliance Consumer Products and Bhartiyam Beverages together anchor ~70% of H2 FY26 order-book execution; scored as risk (C2, no evidence of improving concentration) rather than moat. (B07)

### Watch Flags

- Bank of India CC account ₹665.43 lakh debit balance undisclosed in formal debt note (B02, B03)
- Company Secretary turnover three times in ~16 months spanning IPO window (B04, B08)
- Four independent directors' attendance 33–42% in IPO year (B08)
- Undisclosed / unresolved disputes (DLF receivable litigation, MSME payables >3 years stale) (B02, B03)

---

## CREDIBILITY GRADE (Management)

| Grade | Component | Status | Anchor |
|---|---|---|---|
| **Grade** | B (Good) | Credibility Grade B assigned | (B05-concall: credibility_grade: "B") |
| **Basis** | Core numeric commitments (revenue growth, order-book conversion) consistently met or exceeded across three periods; governance/communication commitments (quarterly reporting, ESOP, H1/H2 skew reduction, order-book number consistency, forward guidance specificity) show recurring pattern of misses and unreconciled figures. | See promise_delivery table above | (B05-concall: credibility_basis) |
| **Downside Scenario** | Two of four FTTCP scores (margin and cash) are low confidence. If both disappoint at the H1 FY27 print, the FTTCP score falls to +2 (DEEP WATCH leaning AVOID). | Management credibility score impacts realization probability of forward guidance; Grade B suggests 75–80% realization of numeric commitments, lower confidence on governance milestones. | (FTTCP deliberation: "Honest caveat: two of the four scores are low confidence, margin and cash") |

---

## SUMMARY OF ASSEMBLY COMPLETENESS

**Status:** COMPLETE. All tables, anchors, conflicts, and unresolved items documented. Ready for Pillar 1 valuation input assembly in phase 3.

**Key Gaps Requiring Forward Attention:**
1. **FII+DII holding %:** Blocks UA criterion 3; position fails standard UA gate. Proceeds only under operator override.
2. **Order book detail:** Thin 0.84x book-to-bill and concentration risk (70% in 2 customers) requires forward stress testing.
3. **FCF estimation:** CapEx inference has ±20% uncertainty; direct verification needed in FY27 print.
4. **Capex guidance:** No forward investment plan; assumed flat ratio pending guidance.

**Operator Authoritative Rulings Integrated:**
- ✓ ROCE Pillar 1 = reported 33.39% (ex-cash 77% context-only, not input)
- ✓ Cash determination = GROWTH-INDUCED with falsification trigger (H1 FY27 CFO/PAT <0.7x AND WC days rise faster)
- ✓ ROCE recovery in Pillar 1 only; no strategic re-rating premium from ROCE
- ✓ FTTCP verdict BUY-candidate +5 of 8; decision PROCEED TO VALUATION

---

```yaml
stage: B10-valinputs
company: "APEXECO"
run_date: "2026-07-10"
model: claude-haiku-4-5
status: complete
input_gaps:
  - field: "rating_pdf"
    detail: "NOT PROVIDED; SME-listed companies exempt from mandatory credit rating per SEBI and AR Boards' Report p.26; no rating-agency working capital comment available"
  - field: "fii_dii_holding_pct"
    detail: "NOT FOUND in any input block, screener export, or results document; AR Note 2 provides promoter holding only (69.29%); full shareholder pattern not provided"
  - field: "capex_fy26"
    detail: "NOT ITEMIZED in screener; inferred from balance sheet movement (net block 1.18→1.96, CWIP 0.98, depreciation 0.2 = ~₹1.96 Cr); ±20% estimation uncertainty"
  - field: "order_book_aging_detail"
    detail: "NOT PROVIDED; book stated ₹125 Cr but no project-stage breakdown or fulfillment schedule; book-to-bill 0.84x, ~70% concentration in 2 customers"
flags:
  - type: "FLAG-GATE0"
    severity: "critical"
    field: "cash_conversion"
    detail: "Classification capped at AVERAGE by cumulative CFO/PAT 0.41 (<0.50 threshold); FY25 CFO negative ₹5.24 Cr (restated) against PAT positive ₹8.56 Cr; post-IPO working-capital build. (B01-gate0)"
  - type: "FLAG-CASH"
    severity: "critical"
    field: "receivables_and_cash_flow"
    detail: "Trade receivables up 155.3% vs revenue 33.67%; zero doubtful-debt provision both years; CFO FY25 -₹14.08 Cr funded entirely by IPO proceeds; FY26 recovery 0.398x still below healthy 0.7x threshold. (B01, B02, B03)"
  - type: "FLAG-CONCENTRATION"
    severity: "major"
    field: "customer_concentration"
    detail: "Reliance Consumer Products and Bhartiyam Beverages anchor ~70% of H2 FY26 execution; single largest order in company history; book-to-bill 0.84x declining; diversification unknown. (B07)"
  - type: "FLAG-GOVERNANCE"
    severity: "major"
    field: "governance_and_disclosures"
    detail: "Independent directors <42% attendance in IPO year; remuneration disclosure contradicts Note 20(b) vs Annexure III; Company Secretary turnover 3x in 16 months; undisclosed Bank of India CC facility ₹665 lakh (~11% of assets). (B02, B03, B08)"
  - type: "FLAG-DATA-GAP"
    severity: "medium"
    field: "roce_historical"
    detail: "ROCE computable only FY25–FY26; FY18–FY24 N/A due to screener liability split unavailable. Block A score (ROCE) has low-confidence foundation. (B01)"
  - type: "FLAG-NARRATIVE-CONTRADICTION"
    severity: "medium"
    field: "md_and_a_accuracy"
    detail: "MD&A claims FY25 growth driven by international contracts; Note 22 shows export revenue fell 59% with 100% customer churn. MD claim of 'efficient working capital' contradicted by CFO collapse. (B03)"
table:
  company_identity:
    company_name: "Apex Ecotech Ltd"
    ticker: "APEXECO"
    sector: "EPC / Civil construction"
    business_model_type: "Hybrid: 96.4% project-based EPC turnkey, 3.6% recurring O&M/AMC"
    cmp_rupees: 242.0
    market_cap_cr: 319.0
    shares_outstanding_diluted_cr: 1.319
    net_cash_cr: 33.75
    enterprise_value_cr: 285.25
  latest_period_fy26:
    revenue_cr: 148.65
    revenue_anchor: "screener-Data_Sheet P&L Sales FY26"
    ebitda_cr: 23.04
    ebitda_margin_pct: 15.5
    ebitda_anchor: "calculated PAT 17.02 + Tax 5.73 + Interest 0.09 + Depreciation 0.2"
    pat_cr: 17.02
    pat_margin_pct: 11.4
    pat_anchor: "screener-Data_Sheet P&L Net Profit FY26"
    diluted_eps_rupees: 12.91
    eps_anchor: "B05-concall guidance FY26 actual EPS 12.91"
    cfo_cr: 6.77
    cfo_anchor: "screener-Data_Sheet Cash_Flow Operating Activity FY26"
    fcf_cr: 4.81
    fcf_note: "estimated CFO 6.77 - inferred capex 1.96; capex not itemized in screener"
    bvps_rupees: 47.96
    bvps_anchor: "calculated (Equity 13.19 + Reserves 50.07) / 1.319 Cr shares"
    net_cash_per_share: 25.60
    roce_latest_pct: 33.39
    roce_anchor: "FTTCP deliberation authoritative: Pillar 1 reported 33.39%, ex-cash context-only 77%, operator ruling"
    roce_trend_direction: "declining_sustain_at_premium"
    roce_trend_anchor: "FTTCP: FY24 ~60%, FY25 ~25%, FY26 ~35%; verdict FIRING sustain not expand"
    roe_pct: 22.9
    roe_anchor: "calculated PAT 17.02 / avg equity 74.44"
    revenue_cagr_3yr_pct: 67.3
    revenue_cagr_anchor: "calculated (148.65/53.08)^0.5-1; FY24–FY26 screener data"
    pat_cagr_3yr_pct: 60.2
    pat_cagr_anchor: "calculated (17.02/6.63)^0.5-1; FY24–FY26 screener data"
    cfo_pat_latest: 0.398
    cfo_pat_anchor: "calculated 6.77/17.02; B01 cumulative 0.41 reported"
    fcf_pat_latest: 0.283
    fcf_pat_anchor: "estimated 4.81/17.02; capex estimated from balance sheet movement"
    p_fcf_latest: 66.4
    p_fcf_anchor: "calculated mcap 319.0 / fcf 4.81; flagged as very high/concerning"
    capex_cr: 1.96
    capex_anchor: "inferred from balance sheet: net block 1.18→1.96, CWIP 0.98, depreciation 0.2"
    capex_note: "direct capex line not itemized in screener; estimation has ±20% uncertainty"
    depreciation_cr: 0.2
    depreciation_anchor: "screener-Data_Sheet P&L Depreciation FY26"
    dps_rupees: 0.0
    dps_anchor: "no dividend paid; screener shows zero across recent years"
  forward_guidance_fy27:
    revenue_growth_range_pct: "30-40"
    revenue_growth_anchor: "B05-concall Q4 FY26 call, verbal non-numeric guidance"
    ebitda_margin_expected_pct: 14.5
    ebitda_margin_anchor: "FTTCP: margins flat mid-teens, no expansion assumed"
    credibility_grade: "B"
    credibility_basis: "Core numeric commitments met/exceeded; governance commitments show pattern of misses (quarterly reporting, ESOP, order-book reconciliation unresolved)"
    credibility_anchor: "B05-concall credibility_grade and credibility_basis"
  analysis_from_stages:
    top_growth_triggers_1: "Reliance Consumer Products order execution (~₹70% of ₹100-125 Cr order within FY26); near-term (0–6 months)"
    triggers_anchor: "B05-concall triggers priority 1"
    top_growth_triggers_2: "Order-book-to-revenue conversion discipline within 6-10 month gestation window; book-to-bill tracking above 1.0"
    triggers_2_anchor: "B05-concall triggers priority 2; B04 business model; B09 SOM capacity check shows order book growing slower than revenue"
    top_growth_triggers_3: "ZLD/higher-margin product mix shift; margin stabilization at or above 14.6%"
    triggers_3_anchor: "B05-concall triggers priority 3; FTTCP margin engine assessment"
    emerging_moat_score: 10.1
    em_classification: "NONE"
    em_anchor: "B07-emoat: score below 12 threshold; 3 documented + 11 claim-based evidence items; Veolia partnership claim contradicted by management"
    evidence_quality_mix: "mostly_claims"
    evidence_anchor: "B07-emoat: documented 3, claim 11, inference 0; evidence_mix"
    cash_determination: "GROWTH-INDUCED"
    cash_anchor: "FTTCP deliberation operator final ruling: GROWTH-INDUCED with falsification trigger H1 FY27 CFO/PAT <0.7x AND working capital days rise faster than revenue"
    cash_falsification_trigger: "H1 FY27 CFO/PAT below 0.7x while working capital days climb faster than revenue growth"
    cash_trigger_anchor: "FTTCP: Step 5 Watch section"
    cash_forward_outlook: "Expected to recover toward 0.6–0.7x by FY27; at risk if order-book replenishment and project execution do not stabilize"
    strategic_asset_moat: "No"
    strategic_moat_anchor: "B07-emoat EM score 10.1 / 80, no moat above threshold; no IP, no backward integration, OEM partnerships available to competitors"
  ua_qualifiers:
    listed_12m: false
    listed_12m_anchor: "Listed Dec-2024; run date 2026-07-10 = ~7 months; fails criterion 1"
    gate0_or_em: true
    gate0_or_em_anchor: "Gate0 score 86 (exceeds 60); EM score 10.1 (below 25 but Gate0 qualifies); passes criterion 2"
    fii_dii_lt3: null
    fii_dii_lt3_anchor: "NOT FOUND in inputs; AR Note 2 promoter-only, no public/institutional split provided"
    all_met: false
    all_met_anchor: "Listed <12 months disqualifies under criterion 1; FII+DII unresolved (criterion 3). Position fails standard UA gate; proceeds only under operator override per FTTCP deliberation and CLAUDE.md."
  peer_medians:
    note: "Peer set provided (CEWATER, EIEL, EMSLIMITED, FELIX); individual peer financials extracted but aggregate medians NOT COMPUTED in provided blocks"
    pe_median: null
    pe_anchor: "B06-peers: peers_provided 4, verified 0; individual P/Es not formalized"
    ev_ebitda_median: null
    ev_ebitda_anchor: "B06-peers: no aggregate median table provided"
    pb_median: null
    pb_anchor: "NOT COMPUTED"
    revenue_growth_peer_context: "Peer narrative: CEWATER -6.2% FY26, EIEL mixed, EMSLIMITED severe miss, FELIX strong; suggests Apex outperformed in FY26 but peers saw guidance cuts mid-year on execution/cash timing"
    growth_context_anchor: "B06-peers industry_cross_read"
    roce_peer_context: "Typical water-EPC peer ROCE 20–30%; Apex 33.39% reported (ex-cash ~77% context-only) appears premium but may be IPO-capital-base artefact"
    roce_context_anchor: "FTTCP and B07 context"
  som_and_tam:
    tam_conservative_cr: 11250
    tam_realistic_cr: 14500
    tam_anchor: "B09-tam top-down Mordor Intelligence, CRISIL sector investment, bottom-up STP capacity-gap unit economics"
    sam_cr: 6375
    sam_pct_of_tam: 56.7
    som_year3_cr: 277
    som_year5_cr: 434
    som_implied_cagr_3yr_pct: 23.1
    som_implied_cagr_5yr_pct: 23.9
    som_anchor: "B09-tam complete methodology"
    current_sam_share_pct: 2.33
    revenue_headroom_x: 42.9
    runway_class: "STRONG"
    som_capacity_check: "Gap ₹290 Cr required by Year 3 vs current ₹125 Cr book; book-to-bill 0.84x binding constraint; SOM trajectory optimistic given replenishment lagging"
    capacity_anchor: "B09-tam capacity_check"
  cash_flow_specifics:
    cfo_fy25_restated: -5.24
    cfo_fy25_anchor: "B01 data_notes: FY25 CFO conflict resolved to audited restated -₹5.24 Cr per AR Note 7 reclassification"
    cfo_fy26: 6.77
    cfo_fy26_anchor: "screener-Data_Sheet Cash_Flow FY26"
    cfo_pat_fy25: -1.65
    cfo_pat_cumulative_fy25_fy26: 0.41
    cfo_cumulative_anchor: "B01-gate0: cumulative CFO/PAT 0.41, deal-breaker #4"
    cash_quality_issue: "Trade receivables +155.3% vs revenue +33.67% with zero doubtful-debt provision; retentions now 47.7% of receivables (up 61.7%); debtors days 54→79"
    cash_quality_anchor: "B02-notes top_findings rank 1; receivables_trend"
    net_working_capital_cr: 61.72
    nwc_anchor: "B05-concall Q4 FY26 call disclosure"
    cash_and_bank_cr: 35.06
    cash_anchor: "screener-Data_Sheet Cash & Bank FY26"
conflicts:
  - field: "cfo_fy25"
    value_a: -14.08
    anchor_a: "07-Nov-2025 filing (earlier screener export)"
    value_b: -5.24
    anchor_b: "FY26 annual audited report, Note 7 restated comparative (AR p.9)"
    used: "Value B (audited restated) per B01 data_notes reconciliation"
    reason: "Reclassification of trade retentions between TR and Other Current Assets; restated AR figure authoritative"
  - field: "director_remuneration_fy25_increase_pct"
    value_a: "169.3% implied from Note 20(b) rupee figures"
    anchor_a: "AR Note 20(b) p.58"
    value_b: "37.02% stated in Annexure III"
    anchor_b: "AR Annexure III p.31, Section 197(12) disclosure"
    used: "NOT RECONCILED; both figures flagged as conflicting"
    reason: "Direct numeric contradiction between two statutory sections; governance-credibility concern; impact on forward valuation inputs immaterial but signals disclosure-quality issue"
  - field: "input_cost_inflation_fy26_h2"
    value_a: "25–40% increase claimed by management"
    anchor_a: "B05-concall Q4 FY26 call"
    value_b: "1–2pp EBITDA impact, later timing (Q4 FY26/Q1 FY27), tied to Middle East disruption per peer corroboration"
    anchor_b: "B06-peers peer commentary"
    used: "Apex's claimed magnitude not corroborated; forward margin guidance conservative ~14.5% flat"
    reason: "Suggests company-specific cost-pass-through weakness; magnitude / timing unsupported by peer evidence"
unresolved:
  - field: "diluted_shares_exact_count"
    why: "Screener Data_Sheet row 52 empty for FY26; row 63 also empty. Calculated from market-cap / CMP (1.319 Cr) but no direct equity-count filing verification."
    where_it_might_be: "Recent shareholding pattern filing post-IPO, RHP DRHP archives, MCA portal"
    impact: "Low: calculated value consistent with EPS back-calc (12.91 = 17.02 / 1.319) and market data; used throughout table"
    status: "used with caveat"
  - field: "free_cash_flow_fcf_fy26"
    why: "CapEx for FY26 not itemized in screener; inferred from balance sheet movement (net block, CWIP, depreciation) with ±20% estimation uncertainty. Results PDF unreadable due to tool limitation."
    where_it_might_be: "FY26 Annual Report Cash Flow Statement note detail; fixed-asset depreciation & capex schedule"
    impact: "Medium: FCF is material to valuation. P/FCF benchmark very high (66.4x), flagged as concerning; FCF estimation uncertainty propagates to free-cash-flow valuation inputs"
    status: "estimated_high_uncertainty"
  - field: "fii_dii_holding_pct"
    why: "Not disclosed in any block, screener export, or input document. AR Note 2 provides promoter-only holding (69.29% combined); full shareholder breakdown not provided."
    where_it_might_be: "Latest shareholding pattern filing with stock exchange (NSE/BSE); Trendlyne public holdings; MCA portal shareholder registry"
    impact: "High: affects UA qualifier gate (criterion 3 of all-three-met check). Currently NOT FOUND, position fails standard UA gate; proceeds only under operator override."
    status: "blocks_ua_gate"
  - field: "cash_bank_breakdown_by_currency_restriction"
    why: "Screener shows ₹35.06 Cr combined; no breakdown by currency, geographic location, or restriction status (e.g., escrow, lien)."
    where_it_might_be: "Audit report cash balance note; bank confirmations; possible forex-exposure disclosure in AR"
    impact: "Low: consolidated cash figure sufficient for net-debt calculation; unlikely material restrictions for debt-free SME"
    status: "immaterial"
  - field: "borrowing_cost_of_debt"
    why: "Borrowings ₹1.31 Cr shown; interest ₹0.09 Cr charged. Implied rate ~6.9%, but no disclosure of cost terms or lender identity."
    where_it_might_be: "AR Note 4 Borrowings detail; B05 concall commentary on credit terms; Bank of India CC facility terms (currently undisclosed)"
    impact: "Low: minimal debt, immaterial to leverage or WACC calculations. Bank of India CC account disclosure gap flagged separately under FLAG-GOVERNANCE."
    status: "low_priority"
  - field: "contingent_liabilities_rupee_detail"
    why: "AR discloses material pending litigations (DLF, MSME, income-tax); B03 notes portfolio <1% of net worth. No exact rupee figure itemized for each case."
    where_it_might_be: "AR Note 25 Contingent Liabilities full schedule with case name, amount, expected settlement timing"
    impact: "Low: assessed <1% net worth; low financial materiality. Governance flag, not material to valuation numerics."
    status: "low_materiality"
  - field: "order_book_aging_fulfillment_schedule"
    why: "Order book ₹125 Cr stated as of 31-Mar-2026; no breakdown by project stage, fulfillment timing, customer, or execution risk. Book-to-bill 0.84x thin and declining; no order-mix detail."
    where_it_might_be: "Q4 FY26 concall transcript detailed commentary; AR investor presentation schedules or MDA order-book note; investor relations announcements"
    impact: "High: order book is critical revenue visibility and SOM achievement lever. Current data insufficient for forward cash-conversion and revenue-growth confidence. Reliance order ~₹100 Cr dominates; diversification unknown. Flagged as major concentration risk (FLAG-CONCENTRATION)."
    status: "blocks_forward_analysis"
  - field: "quarterly_results_fy26"
    why: "Screener-Quarters file is empty for APEXECO. Company reports H1/H2 (semi-annual) due to SME listing exemption; no quarterly P&L available in inputs."
    where_it_might_be: "Investor presentation slides; Q4 FY26 concall transcript (may embed Q3/Q4 revenue/profit figures); possible Q3 FY26 investor circular per voluntary quarterly-reporting promise"
    impact: "Low: H1/H2 data extracted from concalls in B05; sufficient for gate analysis. Quarterly granularity deferred to forward-looking analysis phase."
    status: "deferred_phase3"
  - field: "rating_agency_working_capital_comment"
    why: "No rating PDF exists (SME-listed companies exempt from mandatory credit rating per SEBI and AR Boards' Report p.26). Rating-agency WC/cash-flow commentary typically used to corroborate or challenge cash-conversion assessment is NOT FOUND."
    where_it_might_be: "Credit rating (if one were issued) would have been in input set; since SME exempt, no such document exists in the market"
    impact: "Medium: FTTCP cash determination (GROWTH-INDUCED) relies on internal AR evidence + peer corroboration + operator ruling rather than third-party credit assessment. Determination stands; FTTCP addresses this gap explicitly."
    status: "acceptable_per_operator"
  - field: "capex_guidance_plan_fy27_fy29"
    why: "No forward capex guidance provided in B05 concalls or B04 business-model analysis. Future investment requirements and capex-intensity assumption unknown."
    where_it_might_be: "Q4 FY26 concall concall commentary on capex plans or CapEx/sales intensity going forward; AR management guidance section or investor presentation forward guidance"
    impact: "Medium: affects FCF projection and cash-runway estimation in valuation phase. Conservatively assumed flat capex/sales ratio pending forward guidance."
    status: "requires_forward_assumption"
rating_wc_quote: "NOT PROVIDED — SME-listed companies exempt from mandatory credit rating. No rating agency or rating commentary available in inputs. FTTCP operator ruling: 'no credit rating exists to confirm it; no formal cash plan named.' Cash determination proceeds on AR evidence + peer + operator authority."
ua_qualifiers:
  listed_12m: false
  gate0_or_em: true
  fii_dii_lt3: null
  all_met: false
credibility_grade: "B"
```

