# STAGE 4 REPORT: BUSINESS MODEL DECODER. Onward Technologies Ltd (ONWARDTEC)

Run date 2026-11-12. Sources: Annual_Report_2026.pdf (AR26), Investor_Presentation_1.pdf (Q2 FY27 deck, "Inv. Pres."), Concall_Oct_2026_Transcript.pdf ("Oct call"), screener Data_Sheet CSVs (peer scale and margins), and prior blocks B01 to B03. Company memory (step1-business-brief.md) is used only to choose what to check. Units: AR financial lines in INR lakhs, AR narrative and deck in Rs Cr, stated on each figure. "Derived" means arithmetic on anchored numbers, shown inline.

## Sector cap row finding (read first)

Evidence supports **Consulting / Engineering services (25x)**, not Platform / SaaS / IT services (45x). The operator rules at the /fttcp pillar gate.

| Test | Evidence | Points to |
|---|---|---|
| What is sold | Engineer time. 88% time and material, 12% fixed price (AR26 p.46) | Services |
| Self-description | "software outsourcing company specialising in digital and engineering ER&D" (AR26 p.45) | Services |
| Recurring licence, ARR, per-seat price, product IP | None disclosed. Deck calls the work "managed digital services" billed per contract (Inv. Pres. slide 8) | Not platform |
| Revenue scales with | Headcount and utilisation. 432 net hires in H1 FY27 (Inv. Pres. slide 7); management quotes revenue per head (Oct call, p.10) | Services |
| Software-led work | About 50% of the mix (AR26 p.11), but billed by time, so the billing model is the same | Weakens the 45x reading only on content, not on billing |
| Peers | LTTS, Tata Technologies, Cyient: all ER&D (peer files in inputs/screening) | Engineering services |
| Counter-evidence for 45x | Management says outcome-based and "platform-led" models are industry trends (AR26 p.47), not Onward's revenue | Not evidenced |

Conclusion: nothing in the filed documents shows revenue that scales without adding people. The 45x row needs that. It is not here.

---

## SECTION 1: THE BUSINESS MODEL IN PLAIN ENGLISH

### 1A One line
Onward rents out teams of engineers, mostly in Pune and Hyderabad, to big industrial and vehicle makers in North America and Europe, and bills them by the hour or month (AR26 p.45-46; Inv. Pres. slide 5).

### 1B Money flow chain, for each stream

| Stream | Input | What the company does | What it delivers | Who pays | How they pay |
|---|---|---|---|---|---|
| Time and material (88% FY26; 85% Q2 FY27) (AR26 p.46; Inv. Pres. slide 11) | Hired engineers (lateral hires from shop floors, no campus hiring) (Oct call, p.12), SME leads, training | Places teams on a client's product programme, onsite or at an Indian centre | Design, testing, embedded and software work, billed as hours or a monthly team charge | Global OEMs: 100% overseas clients, 70% North America, 30% Europe (Inv. Pres. slide 5) | Invoice per hour or per month; collected in about 75 to 80 days (AR26 p.46; Inv. Pres. slide 9) |
| Fixed time, fixed price (12% FY26; 15% Q2 FY27) (AR26 p.46; Inv. Pres. slide 11) | Same engineers, plus project management | Takes a scoped job, such as re-engineering a 5 MW cooling unit (Inv. Pres. slide 27) | A finished design package | Same OEM base | Milestone invoices (milestone terms NOT FOUND) |
| Multi-year managed centre (inside the two above; not a separate reported stream) | Dedicated offshore team | Runs an offshore centre or managed digital service for one client. Rs 44.5 Cr over Aug 2026 to Aug 2029, up 72% on the prior term; about Rs 33 Cr new 3-year contract signed Jun 2026 (Inv. Pres. slide 8, 14) | Ongoing service | Global construction and mining equipment maker; a power management leader's data-centre unit (names NOT FOUND) | Contract billing; rate card NOT FOUND |

### 1C Revenue model classification

| Stream | Type (standard taxonomy) | Description | % of revenue (anchor) | Predictability |
|---|---|---|---|---|
| Time and material | Services, resource-based, usage billing | Paid while the team works; stops when the client stops | 88% FY26, 86% FY25 (AR26 p.46); 85% Q2 FY27 (Inv. Pres. slide 11) | M. Repeat clients, but no committed volume floor disclosed (NOT FOUND) |
| Fixed price | Services, project-based | Paid on delivery; Onward carries overrun risk | 12% FY26, 14% FY25 (AR26 p.46); 15% Q2 FY27 (Inv. Pres. slide 11) | L |
| Memo: by industry | IEHM 63%, T&M (transportation and mobility) 34%, HCLS 3% in FY26 (AR26 p.46); IEHM 65%, 32%, 3% in Q2 FY27 (Inv. Pres. slide 11) | Customer end-market, not a stream | | IEHM and mobility are OEM R&D budgets: M |
| Memo: by delivery | Offshore 71%, onsite 29% FY26 (AR26 p.46); offshore 69% Q2 FY27 vs 72% Q2 FY26 (Inv. Pres. slide 11) | Where the work is done | | |
| Memo: by geography | USA 36%, Europe 12%, India 52% FY26 (AR26 p.46); USA 41%, Europe 12%, India 47% Q2 FY27 (Inv. Pres. slide 11). **Conflict:** AR26 p.10 and Inv. Pres. slide 5 say 70% North America and 30% Europe. Note 34 shows India 54.8% (B03). Basis (billing entity or client location) NOT FOUND | | | |

### 1D Simplified business model canvas

| Element | Answer (anchor) |
|---|---|
| What they sell | Engineering design, embedded and software, data and testing work for product makers (AR26 p.45; Inv. Pres. slide 23) |
| Who buys | 72 active clients; top 5 are 48%, top 10 64%, top 25 87% (AR26 p.46); one customer 18.3% (9,965.52 of 54,385.24 lakhs, Note 34 p.93, via B03) |
| Why them | Domain-trained engineers, 5 to 8 year average engagements (Inv. Pres. slide 24), mid-size focus, a claimed 20% saving from "Opex-to-Capex delivery models" (Inv. Pres. slide 25; basis NOT FOUND) |
| How delivered | Pune, Hyderabad centres over 90% utilised (AR26 p.11), onsite staff in the US and Europe; 12 offices in 6 countries (Inv. Pres. slide 5) |
| Cost structure dominance | Employee cost 72.8% of revenue (39,582.25 / 54,385.24 lakhs, derived; AR26 p.46); other expenses 14.0% (7,618.40 / 54,385.24, derived); depreciation 2.9% (1,579.69 / 54,385.24, derived) |
| Scarce resource | Engineers with product and process knowledge. Hired from manufacturing floors then trained; "we have to hire them in hundreds" for one customer (Oct call, p.11) |
| Pricing power source | Not evidenced. Margin gain came from mix, utilisation and cost, not a stated rate rise. Rate per hour NOT FOUND |
| Asset intensity | Light. Depreciation 2.9% of revenue (derived); no inventory (AR26 p.47) |
| WC intensity | Medium. DSO 75 days FY26, 80 at Sep 2026 (AR26 p.46; Inv. Pres. slide 9); unbilled 3,429.35 lakhs, +13.2% vs revenue +10.7% (B02) |
| Regulatory moat or burden | None material. HCLS has regulatory assurance work but is 3% of revenue (AR26 p.46). Burden: US visa and tariff policy affects the onsite share (Oct call, p.10) |

### 1E The chai-stall-uncle version
Think of a firm that lends skilled carpenters to furniture factories abroad. The factory pays for each carpenter by the month. Onward's carpenters are engineers. Most of them sit in India, and some sit in the client's factory. Onward earns the gap between what the client pays per engineer and what the engineer costs. When more of the engineers are busy and more work from India, the gap grows. One factory gives Onward almost a fifth of its income (18.3%), so that client matters far more than the rest.

### Section 1 summary

| Item | Answer |
|---|---|
| Business type | Services (people-based ER&D outsourcing) |
| Revenue nature | Recurring-style relationships, but billed by time with no volume floor disclosed |
| Asset intensity | Light |
| WC intensity | Medium (DSO 75 to 80 days) |
| Pricing power | Weak: no evidenced price lever; margin came from mix and utilisation |

---

## SECTION 2: INDUSTRY DYNAMICS & COMPETITIVE POSITION

### 2A Five forces

| Force | Plain answer (anchor) | Helps / hurts / neutral |
|---|---|---|
| Competition | Large listed peers: LTTS (FY26 sales 10,995.9 Cr), Cyient (7,268.2 Cr), Tata Technologies (5,505.57 Cr) vs Onward 543.85 Cr (screening Data_Sheets, FY26). Count of unlisted rivals NOT FOUND | Hurts |
| Entry barriers | Trained domain talent and years of client trust. No licence or capital barrier. Entry cost is hiring and training time (Oct call, p.11) | Neutral |
| Supplier power | Suppliers are engineers. Attrition 14.85% (AR26 p.11) vs BRSR staff turnover 37.93% (AR26 p.27, B03 conflict). Wage inflation and scarce SMEs push cost | Hurts |
| Customer power and concentration | Top client 18.3%, top 25 87% (AR26 p.46; Note 34). Customers control rate cards, approvals (DSO rose on "delays in customer approvals", Oct call, p.12) | Hurts |
| Substitutes | AI could cut hours billed. Management says no material change in scope, pricing or budgets so far (AR26 p.11) and expects gains. Evidence is one year of management statements | Neutral, unproven |

### 2B Competitive positioning map

| Company | FY26 sales Cr | FY26 EBITDA margin (B01, computed from Data_Sheet) | Employee cost % of sales (derived from Data_Sheet) | Positioning |
|---|---|---|---|---|
| Onward | 543.85 | 13.21% | 72.8% (395.96/543.85) | Mid-size pure-play ER&D, industrial and off-highway lead |
| LTTS | 10,995.9 | 17.60% | 58.7% (6,457.4/10,995.9) | Scale ER&D, transportation and industrial |
| Tata Technologies | 5,505.57 | 15.49% | 49.7% (2,737.42/5,505.57) | Mobility and industrial heavy machinery |
| Cyient | 7,268.2 | 12.37% | 55.6% (4,040.8/7,268.2) | Rail, mining, heavy equipment |

Reading: Onward's margin sits between Cyient and Tata Technologies. Its employee cost share is far higher than peers. Peers may book sub-contracting, onsite and other people costs on other lines, so the gap in cost share is a classification question until the notes are compared line by line (NOT FOUND for peers). Market cap Rs 841.82 Cr is the smallest of the four (B01). Peer concall evidence is for stage 5 and later.

### 2C Moat assessment (eight standard types)

| Moat type | Evidence | Durability |
|---|---|---|
| Switching costs | Average engagement 5 to 8 years, some over 20 (Inv. Pres. slide 24); clients above US$1 mn rose 13 to 16 in FY26, 18 at Sep 2026 (AR26 p.46; Inv. Pres. slide 12) | Moderate. Tenure is not a contract floor. T&M can be cut at short notice (volume floor NOT FOUND) |
| Network effects | None | None |
| Intangible assets (brand, patents, licences) | None disclosed | None |
| Cost advantage | 71% offshore delivery (AR26 p.46); claimed 20% saving (Inv. Pres. slide 25) | Low. Every peer has the same India cost base |
| Scale economies | Smallest of four peers (B01 M5 scored 0); revenue 543.85 Cr vs 5,505.57 Cr for the nearest peer | None |
| Regulatory / licence | None | None |
| Process and domain know-how | SMEs trained per customer; 90+ recruiters in house; lateral hiring only (Oct call, p.11-12) | Low to moderate. Knowledge sits in people |
| Embedded integration (client product programmes) | "Participation in their R&D ecosystems" (AR26 p.48); mining and construction equipment client renewed with 72% higher value (Inv. Pres. slide 8) | Moderate, tied to a few accounts |

Cross-check with B01: B01 confirmed 4 moats on margin and revenue history tests. This stage finds no structural moat above moderate. The two views do not conflict: B01 tests outcomes, this table tests mechanisms.

### 2D Industry lifecycle
Global ER&D outsourcing is in the growth stage: US$81 to 82 bn in CY2024 to US$133 to 135 bn by CY2030, 8.5 to 9.5% growth (AR26 p.45; Inv. Pres. slide 20, sourcing Nasscom-Everest). Onward is a small, late-scaling participant. Its revenue CAGR FY23 to FY26 was 7.2% against 17.5% for the prior three years (B01 M11). The company is catching up on margin (7.0% FY22 to 13.2% FY26, Inv. Pres. slide 14), not yet on growth, until H1 FY27 growth of 16.9% (Inv. Pres. slide 8).

### 2E Key industry drivers

| Driver | Direction | Impact on Onward |
|---|---|---|
| OEM outsourcing of engineering | Up | Volume (AR26 p.45) |
| Data-centre power and cooling equipment demand | Up | Named by management as a growth driver, with a Rs 33 Cr offshore centre win (Inv. Pres. slide 14); revenue share NOT FOUND |
| US visa and onsite restrictions | Pushes work offshore | Faster project start for offshore; lowers blended revenue per head (Oct call, p.10) |
| INR vs USD | INR weaker | Q2 FY27 reported growth 22.4%, constant currency 17.7% (Oct call, p.6; Inv. Pres. slide 9): a 4.7 point currency tailwind |
| Auto cycle and EV programmes | Mixed | Transportation and mobility fell from 38% to 34% of revenue FY25 to FY26 (AR26 p.46) |
| AI productivity | Uncertain | Could cut billed hours or lift value per project; no material impact so far (AR26 p.11) |

---

## SECTION 3: FINANCIAL METRICS THAT MATTER

### 3A Ignore these, track these

| Ratio | Verdict | Why |
|---|---|---|
| Inventory turnover | Irrelevant | No inventory (AR26 p.47) |
| Debt/equity | Irrelevant | No borrowings (AR26 p.47) |
| Current ratio 3.66 | Misleading | Cash and receivables fill it (AR26 p.47); says nothing on delivery risk |
| Interest coverage 1.68 | Misleading | Finance cost is lease interest; B03 could not reproduce it |
| Reported ROCE 25.42% | Misleading | Includes other income; B03 could not reproduce. Standalone 23.48% is 19.17% ex other income (B02) |
| Gross margin | Irrelevant | No cost of goods. Data_Sheet 100% is a cost-classification artifact (B01 M9) |
| Reported debtors turnover 4.74 | Misleading | Leaves unbilled receivables out; use billed plus unbilled DSO |
| Capex to sales, asset turnover | Low value | Depreciation is 2.9% of revenue (derived) |
| Reported EBITDA margin alone | Misleading in Q2 FY27 | Includes a Rs 2.93 Cr (292.60 lakhs) R&D credit (B01); use margin ex credit |
| Headline CFO to PAT | Use with care | 15.3% of CFO is accrued pay and Ind AS 116 adds 22.7 points (B03 FLAG-CASH) |

### 3B Must-track metrics

Healthy ranges use the company's own guidance or history, since no external industry range sits in the corpus (NOT FOUND for external ranges; peer margins from B01).

**Growth**

| Metric | What it tells you | Healthy | Where to find | Red flag |
|---|---|---|---|---|
| Revenue growth, constant currency | Real volume vs FX help | 15 to 18% FY27 guide (Inv. Pres. slide 14); Q2 17.7% cc | Quarterly deck, concall | Constant currency below 10% (FY26 reported 10.7%) |
| Clients above US$1 mn and revenue per client | Account depth | 18 clients; Rs 2.4 Cr per client in the quarter (Inv. Pres. slide 12) | Deck | Below 16 clients |
| Revenue per employee | Productivity, not hiring | Rs 21.9 lakh FY26 (derived) rising 10% or more | Deck, AR | Flat while headcount rises |
| Order wins and renewals | Forward visibility | Rs 44.5 Cr and about Rs 33 Cr (Inv. Pres. slide 14) | Deck, call | No named wins for two quarters |

**Profitability and efficiency**

| Metric | What it tells you | Healthy | Where | Red flag |
|---|---|---|---|---|
| EBITDA margin ex one-offs | Real operating margin | 13.8 to 14.3% (guide); FY26 13.21% (12.96% ex UK credit, B03) | Results, call | Below 13.0% |
| Employee cost % of revenue | Pay leverage | 72.8% FY26; 69.4% Q2 FY27 (118.1/170.2, Inv. Pres. slide 9, derived) | Results | Rising two quarters |
| Incremental EBITDA margin | Operating leverage | FY26 51.7% (derived below); H1 FY27 16.6% | Results | Below 12% for a year |
| Offshore and fixed price share | Margin mix and risk mix | Offshore 70%+, fixed price 12% or below | Deck slide 11 | Offshore below 68%, fixed price above 15% |
| Effective tax rate | PAT quality | 22.3% FY26 vs 25.4% (B02) | Results | PAT growth faster than PBT growth |

**Balance sheet and risk**

| Metric | What it tells you | Healthy | Where | Red flag |
|---|---|---|---|---|
| DSO billed plus unbilled | Cash conversion | 65 to 70 days (target) | Deck | Above 80 two quarters |
| Unbilled growth vs revenue growth | Billing lag | Below revenue growth | Balance sheet note 6 | Faster two quarters |
| Net cash | Buffer | Rs 127.3 Cr FY26 (AR26 p.11); Rs 97.1 Cr at H1 FY27 (Inv. Pres. slide 5; fall of Rs 30.2 Cr in six months coincides with the Rs 18.00 Cr buyback and dividend, not itemised, so cause NOT FOUND) | Deck | Falls with DSO rising |
| Top client share | Concentration | 18.3% | Note 34 | Above 20% |

### 3C Industry-specific KPIs for this company

| KPI | Latest | Where |
|---|---|---|
| Billed utilisation | Pune and Hyderabad "over 90%" (AR26 p.11); company-wide figure NOT FOUND | AR, call |
| Offshore / onsite revenue mix | 69% / 31% Q2 FY27 (Inv. Pres. slide 11) | Deck |
| Net headcount | 2,917 at Sep 2026; 2,485 at Mar 2026; 2,581 at Mar 2025 (Inv. Pres. slide 5; AR26 p.46) | Deck |
| Attrition | 14.85% LTM (AR26 p.11) vs 37.93% BRSR turnover (AR26 p.27): unresolved | AR, BRSR |
| Revenue per client | Rs 7.6 Cr FY26 vs 6.1 FY25 (Inv. Pres. slide 16) | Deck |
| Active clients | 72 (down from 80; 145 in FY22) (AR26 p.46; Inv. Pres. slide 15) | AR |
| Contract type mix | T&M 85% / fixed 15% Q2 FY27 | Deck |

### 3D Unit economics (the physics)

Unit: one billed engineer for one year. All derived from anchored lines; average headcount (2,485 + 2,581) / 2 = 2,533 (AR26 p.46).

| Line | FY26 per average head | Calculation |
|---|---|---|
| Revenue | Rs 21.47 lakh | 54,385.24 lakhs / 2,533 (AR26 p.46) |
| Employee cost | Rs 15.63 lakh | 39,582.25 / 2,533 |
| Other expenses | Rs 3.01 lakh | 7,618.40 / 2,533 |
| EBITDA | Rs 2.84 lakh (13.21%) | 7,184.59 / 2,533 |
| Q2 FY27 revenue per head, annualised | Rs 23.3 lakh | 170.2 x 4 = 680.8 Cr / 2,917 closing heads (Inv. Pres. slide 5, 9) |
| Management aspiration | Rs 30 to 40 lakh (deck slide 13) or 35 to 40 lakh (call p.10); needs 10% onsite, 90% offshore (call p.10-11). Deck and call differ on the low end | |

Drivers:
- **Volume:** heads added and utilisation. Management says the majority of hiring for the revised guide is done (Oct call, p.12).
- **Price:** blended rate per engineer. Not disclosed. The 72% rise in the Rs 44.5 Cr renewal mixes rate and scope; split NOT FOUND.
- **Cost:** wages for lateral hires, SME hiring "in hundreds", training, and the indirect cost of revenue (sales and account teams) (Oct call, p.11). Sub-contracting rose 36.6% to 3,407.42 lakhs against revenue +10.7% (B02).
- **Currency:** revenue in USD and EUR, cost mostly INR. Q2 FY27 reported growth exceeded constant currency by 4.7 points.

Operating leverage (derived):

| Period | Change in revenue | Change in EBITDA | Incremental margin |
|---|---|---|---|
| FY26 vs FY25 (AR26 p.46) | 5,253.63 lakhs (54,385.24 - 49,131.61) | 2,714.98 lakhs (7,184.59 - 4,469.61) | 51.7%. Headcount fell 3.7% (2,581 to 2,485), so this was a one-time productivity gain |
| H1 FY27 vs H1 FY26 (Inv. Pres. slide 10, Rs Cr) | 47.5 (319.6 - 272.1) | 7.9 (44.9 - 37.0) | 16.6%; 10.5% ex Rs 2.93 Cr credit ((7.9 - 2.93) / 47.5) |
| Q2 FY27 vs Q2 FY26 (Inv. Pres. slide 9) | 31.2 (170.2 - 139.0) | 6.7 (26.6 - 19.9) | 21.5%; 12.1% ex credit |

Reading: FY26 leverage came from holding heads flat while revenue grew. FY27 leverage is lower because heads are growing ahead of revenue. A 50% incremental margin is not the physics going forward. A level near 12 to 17% on the filed H1 data is. This is the point the margin debate must answer.

---

## SECTION 4: RISKS, VALUATION APPROACH & MONITORING

### 4A Business-model-specific risks

| Category | Risk | First line item to deteriorate |
|---|---|---|
| Revenue model | Time and material has no volume floor; one client 18.3% (Note 34 p.93); top 25 up from 84% to 87% | Top client share; billable heads on that account |
| Revenue model | Fixed price share rising 11% to 15% (Inv. Pres. slide 11) | Fixed price share; project margin; unbilled revenue |
| Margin | Hiring ahead of revenue: 432 net hires in H1 (Inv. Pres. slide 7); 450-odd per call (Oct call, p.12) | Employee cost % of revenue |
| Margin | One-off credit and FX inside the Q2 print | EBITDA margin ex credit; constant currency gap |
| Margin | Sub-contracting up 36.6% (Note 24 p.86) | Sub-contracting % of revenue (FY26 6.27%) |
| Balance sheet | DSO 80, unbilled unaged and unprovided (Notes 6, 30; B03) | Unbilled growth vs revenue |
| Balance sheet | Gratuity deficit 1,062.86 lakhs; pay accruals 15.3% of CFO (B02) | Employer gratuity contribution; accrued pay |
| Execution | Training SMEs "in hundreds" per account; 90%+ utilisation at two centres (AR26 p.11) leaves little slack for ramps | Utilisation; attrition; revenue per head |
| Execution | Audit trail gap on the billing system, second year (AR26 p.63; B03) | Auditor's report paragraph in FY27 |
| Structural | AI could shrink billed hours; management sees none yet (AR26 p.11) | Revenue per head vs hours billed |
| Structural | US visa and onsite limits cut blended rate (Oct call, p.10) | Onsite share; revenue per head |
| Structural | Cyclical OEM R&D budgets; FY21 revenue -11.5% (B01) | New wins, client budget commentary |

### 4B Valuation method applicability (handoff to Role 1)

| Method | Applies? | Why |
|---|---|---|
| P/E on forward earnings | **PRIMARY** | Cash-backed earnings, no debt, asset-light. Build EPS net of R&D credit, other income (704.23 lakhs, AR26 p.46) and tax rate effects |
| EV/EBITDA vs peers | **SECONDARY** | Removes tax and other-income noise. Remove net cash of Rs 127.3 Cr (AR26 p.11). Peer margins 12.4 to 17.6% (B01) |
| FCF yield after leases and pay-accrual reversal | **TERTIARY** | CFO overstates distributable cash (B03 FLAG-CASH) |
| DCF | Cross-check only, not selected | Margin path is the open question; DCF would restate that assumption |
| P/B, ROE-based | Not applicable | Asset-light |
| EV/Sales | Not applicable | Margin is the debate |
| NAV, SOTP | Not applicable | No separable asset |
| Dividend discount | Not applicable | Payout is policy |
| PEG on trailing growth | Not applicable | Low-base PAT CAGR (B01) |

Cycle stage that matters for valuation: the margin cycle, meaning whether 13.8 to 14.3% is a mid-cycle level or a peak, and the OEM R&D spending cycle behind T&M and IEHM demand. Value on normalised margin. Section 1B governs the exit multiple; this stage names no multiple. The cap row is Consulting / Engineering services (see top).

### 4C Quarterly monitoring checklist

| # | Item | Good | Trouble |
|---|---|---|---|
| 1 | EBITDA margin ex credits | 13.8% or above | Below 13.0% |
| 2 | Constant currency growth | 15% or above | Below 10% |
| 3 | Top client and top 5 share | At or below 18.3% / 48% | Above 20% / 50% |
| 4 | DSO | Heading to 65 to 70 | Above 80 for two quarters |
| 5 | Unbilled vs revenue growth | Slower than revenue | Faster two quarters |
| 6 | Offshore share | 70% or above | Below 68% |
| 7 | Fixed price share | 12% or below | Above 15% |
| 8 | Employee cost % of revenue | Falling | Rising two quarters |
| 9 | Net hires vs revenue added | Revenue per head up | Per head flat or down |
| 10 | Clients above US$1 mn | 18 or more | Below 16 |
| 11 | Sub-contracting % of revenue | Below 7.0% | Above 7.0% |
| 12 | Net cash | Stable after buyback and dividend | Falls while DSO rises |
| 13 | New contract wins named | A named win each half | None |
| 14 | Attrition (single definition) | Reconciled and stable | 14.85% vs 37.93% unresolved |

### 4D Highest-value questions for management

| # | Question | Reassuring answer | Worrying answer |
|---|---|---|---|
| 1 | Offshore share fell 72% to 69% YoY yet margin rose 130 bps. What drove the margin? | Utilisation and rate, quantified | Credit and currency, with offshore share still falling |
| 2 | Share of revenue and receivables from the 18.3% client; renewal date? | Multi-year contract, falling share by growth elsewhere | Share rising, near-term renewal |
| 3 | How much of the 72% uplift in the Rs 44.5 Cr renewal is rate? | Most is rate | All scope: price power absent |
| 4 | Why is fixed price rising to 15%? | Chosen for margin, with track record | Client demand forced it, overruns possible |
| 5 | When do the 432 H1 hires bill, and at what utilisation? | Billing within a quarter, utilisation above 85% | Bench cost carries into H2 |
| 6 | Route from DSO 80 to 65-70? | Named approvals fixed, cash collected after quarter-end | Structural, tied to the large client |
| 7 | Data-centre revenue share and the dependence of the 15-18% guide on it? | Under a third, multiple clients | One client dominates |

---

## SECTION 5: ONE-PAGE SUMMARY CARD

```
+------------------------------------------------------------------+
| ONWARD TECHNOLOGIES (ONWARDTEC)           Run date 2026-11-12    |
+------------------------------------------------------------------+
| Business type     : Services, people-based ER&D outsourcing      |
| Revenue nature    : 88% T&M / 12% fixed (FY26); 85/15 Q2 FY27    |
| Mix               : IEHM 63% / T&M 34% / HCLS 3% (FY26)          |
| Delivery          : Offshore 71% FY26; 69% Q2 FY27 (72% yr ago)  |
| Asset intensity   : Light (depreciation 2.9% of revenue)         |
| WC intensity      : Medium (DSO 75 FY26, 80 Sep 2026)            |
| Pricing power     : Weak (no evidenced rate lever)               |
| Cyclicality       : Cyclical (OEM R&D budgets) over growth trend |
| Moats             : Switching costs (moderate), know-how (low to |
|                     moderate), offshore cost (low)               |
| Sector cap row    : Consulting / Engineering services (25x)      |
| PRIMARY valuation : P/E forward earnings; SECONDARY EV/EBITDA    |
|                     vs peers; TERTIARY FCF yield                 |
| Top 5 metrics     : 1 EBITDA margin ex credits (13.8% / <13.0%)  |
|                     2 Top client share (18.3% / >20%)            |
|                     3 DSO (65-70 / >80)                           |
|                     4 Revenue per head (Rs 21.9 lakh, +10%)      |
|                     5 Offshore and fixed price share             |
| Unit economics    : Rs 21.47 lakh revenue, Rs 2.84 lakh EBITDA   |
|                     per average head FY26 (derived)              |
| Verdict           : Real margin gain, source not yet proven      |
+------------------------------------------------------------------+
```

---

## Margin reading: two readings and the separating observation

| | Reading one | Reading two |
|---|---|---|
| Claim | 15.6% is a new base from offshore leverage and account mining (Oct call, p.6) | Q2 is a peak helped by a credit, currency and a pre-policy offshore shift; the FY27 guide of 13.8 to 14.3% says management expects fallback |
| Filed support | Q2 ex credit 13.87% beats FY26 13.21% and Q1 FY27 12.3% (18.4/149.4, Inv. Pres. slide 9, derived). Incremental margin FY26 51.7% | H1 ex credit 13.1% vs 13.6% a year ago (derived). Offshore share down 72% to 69%. Incremental margin H1 16.6% (10.5% ex credit). Currency added 4.7 points to growth |
| What would confirm | Q3 and Q4 FY27 margin ex credit at or above 14% with offshore share back near 70% | Margin ex credit near 13% with fixed price share and DSO rising |

Separating observation: Q3 and Q4 FY27 EBITDA margin excluding the R&D credit, read with offshore share, fixed price share and DSO. [INFERENCE: the credit is stated as covering the last 12 months of FY26 (Oct call, p.5-6); if so the ex-credit comparison with FY26 is like for like, and the reading rests on the 13.9% Q2 ex-credit margin.]

Guidance cross-check (derived, revenue-from-operations basis assumed because the deck does not state the basis): FY26 revenue 543.9 Cr x 1.15 to 1.18 = 625.5 to 641.8 Cr (Inv. Pres. slide 14 growth, slide 29 base). H1 FY27 is 319.6 Cr. The implied H2 revenue is 305.9 to 322.2 Cr, below twice Q2 revenue of 170.2 Cr (340.4). At guided margins of 13.8 to 14.3% the implied H2 EBITDA margin is 13.5% to 14.6%. The guide is either prudent, as management says (Oct call, p.6), or assumes a fall back. This is a point for the forward basis in Role 1, not a verdict here.

## Items that conflict or are not found

- Geography: three splits (70/30; USA 36 / Europe 12 / India 52; Note 34 India 54.8%). Basis NOT FOUND.
- Aspiration for revenue per head: Rs 30 to 40 lakh (deck slide 13) vs Rs 35 to 40 lakh (call p.10).
- Attrition: 14.85% vs 37.93% (B03).
- Rate per hour, onshore headcount, committed volume floors, client names: NOT FOUND.
- Net cash fell from Rs 127.3 Cr (Mar 2026) to Rs 97.1 Cr (Sep 2026); cause not itemised in the documents read here.

---

```yaml
stage: B04-bizmodel
company: "ONWARDTEC"
run_date: "2026-11-12"
model: claude-sonnet-5-5
status: complete
input_gaps:
  - "Investor presentation present (Q2 FY27, 16 Oct 2026); it is a quarterly deck, so FY26 slides are used only where it restates FY26"
  - "Realised rate per billed hour or per FTE, split of onshore versus offshore headcount, billing split between price and volume in the Rs 44.5 Cr renewal: NOT FOUND, check concall or ask management"
  - "Basis of the India 52% / 47% geography line (billing entity or client location) not stated; AR p.10 (70% North America, 30% Europe) and AR p.46 (USA 36%, Europe 12%, India 52%) conflict"
  - "Name and vertical of the 18.3% customer: NOT FOUND (B03, Note 34 p.93)"
  - "Peer utilisation, revenue per head and client concentration: NOT FOUND in stage 4 inputs; peer concalls are for later stages"
  - "Net working capital definition on Inv. Pres. slide 18 (145, 162, 191 Rs Cr): NOT FOUND"
  - "Sector cap table itself not re-read here; the 25x and 45x figures are carried from B00"
flags:
  - {type: FLAG-MARGIN-READING, reason: "Q2 FY27 margin 15.6% reported; 13.87% ex Rs 2.93 Cr R&D credit; H1 FY27 ex credit 13.1% vs H1 FY26 13.6%; offshore share fell 72% to 69% YoY (Inv. Pres. slide 11), so the offshore mix reading is not what the filed mix shows"}
  - {type: FLAG-FIXED-PRICE-RISING, reason: "fixed price share 11% (Q2 FY26) to 15% (Q2 FY27), T&M 89% to 85% (Inv. Pres. slide 11)"}
  - {type: FLAG-GEOGRAPHY-CONFLICT, reason: "AR p.10 70/30 North America/Europe vs AR p.46 USA 36%, Europe 12%, India 52% vs Inv. Pres. slide 11 USA 41%, Europe 12%, India 47%; basis not stated"}
  - {type: FLAG-LOW-OPERATING-LEVERAGE-H1, reason: "H1 FY27 incremental EBITDA margin 16.6% (10.5% ex credit) vs FY26 51.7%; 432 net hires ahead of revenue (Inv. Pres. slide 7, 10)"}
  - {type: FLAG-SECTOR-ROW, reason: "evidence supports Consulting / Engineering services (25x) over Platform / SaaS / IT services (45x); operator rules at the /fttcp pillar gate"}
  - {type: FLAG-CONCENTRATION, reason: "carried from B03: one customer 18.3%, top 5 48%, top 25 87%; top 25 share up 84% to 87% (AR26 p.46)"}
business_type: services
revenue_streams:
  - {name: "Engineering and digital services billed on time and material", type: "services, time and material (resource-based)", pct_of_revenue: 88, predictability: "M (FY26, AR26 p.46; 85% in Q2 FY27, Inv. Pres. slide 11)"}
  - {name: "Fixed time, fixed price engineering projects", type: "services, fixed price project", pct_of_revenue: 12, predictability: "L (FY26, AR26 p.46; 15% in Q2 FY27, Inv. Pres. slide 11)"}
asset_intensity: light
wc_intensity: medium
pricing_power: weak
cyclicality: cyclical
moats_present:
  - "Switching costs / embedded client relationships: moderate durability (engagement 5 to 8 years, some over 20, Inv. Pres. slide 24; offset by one 18.3% customer)"
  - "Process and domain know-how (SMEs trained from shop floor, no campus hiring): low to moderate durability, leaves with attrition (AR26 p.11 14.85% vs BRSR 37.93%)"
  - "Cost advantage from offshore delivery: low durability, every peer has the same arbitrage"
valuation_methods:
  primary: {method: "P/E on forward earnings (destination multiple from Section 1B, row Consulting / Engineering services)", why: "earnings are cash-backed (CFO 6,507.73 lakhs, AR26 p.66), no debt, asset-light; EPS is the cleanest compounding base; must be built net of R&D credit, other income and tax-rate effects"}
  secondary: {method: "EV/EBITDA against LTTS, TATATECH, CYIENT with net cash (Rs 127.3 Cr FY26, AR26 p.11) removed from EV", why: "strips tax-rate and other-income noise; peer margins 12.4% to 17.6% FY26 (B01) give a margin-adjusted cross-check"}
  tertiary: {method: "FCF yield after lease payments and pay-accrual reversal", why: "Ind AS 116 uplift of 22.7 points and 15.3% of CFO from pay accruals (B03 FLAG-CASH) mean headline CFO overstates distributable cash"}
  not_applicable:
    - "P/B or ROE-based: asset-light, book value is cash and receivables"
    - "EV/Sales: margin spread to peers is the whole debate"
    - "NAV or SOTP: no separable asset"
    - "Dividend discount: payout is a policy choice"
    - "PEG on trailing growth: low-base effects in PAT CAGR (B01 note)"
irrelevant_ratios:
  - "Inventory turnover: no inventory (AR26 p.47 NA)"
  - "Debt/Equity: no borrowings (AR26 p.47 NA)"
  - "Current ratio 3.66: cash and receivables heavy, says nothing about delivery risk"
  - "Interest coverage 1.68: finance cost is lease interest, ratio not reproducible (B03)"
  - "Reported ROCE 25.42%: includes other income, not reproducible (B03); rebuild"
  - "Gross margin: no cost of goods; Data_Sheet 100% is a classification artifact (B01)"
  - "Debtors turnover on reported basis: excludes unbilled receivables"
  - "Asset turnover and capex to sales: asset-light, depreciation 2.9% of revenue"
must_track_metrics:
  - {metric: "EBITDA margin excluding R&D credits and other one-offs", healthy: "13.8% to 14.3% (FY27 guidance, Inv. Pres. slide 14)", red_flag: "below 13.0% (FY26 ex credit 12.96%, B03)"}
  - {metric: "Top client and top 5 share of revenue", healthy: "top client at or below 18.3%; top 5 at or below 48%", red_flag: "top client above 20% or top 5 above 50%"}
  - {metric: "DSO billed plus unbilled", healthy: "65 to 70 days (management target, concall 16 Oct 2026)", red_flag: "above 80 days two quarters running (Sep 2026: 80)"}
  - {metric: "Revenue per employee (annualised, closing headcount)", healthy: "rising 10% or more YoY from Rs 21.9 lakh FY26 (derived)", red_flag: "flat or falling while headcount rises"}
  - {metric: "Offshore share of revenue and fixed price share", healthy: "offshore 70% or more; fixed price at or below 12%", red_flag: "offshore below 68% (Q1 FY27) or fixed price above 15%"}
unit_economics:
  unit: "one billed engineer for one year (average headcount basis)"
  revenue_per_unit: "Rs 21.47 lakh FY26 (54,385.24 lakhs / average 2,533 heads, derived, AR26 p.46-47); Rs 23.3 lakh annualised Q2 FY27 on 2,917 closing heads (derived, Inv. Pres. slide 5, 9)"
  margin_per_unit: "EBITDA Rs 2.84 lakh per head, 13.21% (7,184.59 / 2,533, derived); employee cost Rs 15.63 lakh, other expense Rs 3.01 lakh"
  key_lever: "billed utilisation and offshore leverage on a mostly fixed pay cost; also INR weakness against USD revenue (reported growth 22.4% vs constant currency 17.7% in Q2 FY27)"
first_deterioration_signals:
  - {risk: "customer concentration", first_signal: "top client share of revenue above 20%, then receivable days from that client"}
  - {risk: "margin reversal after hiring ahead of revenue", first_signal: "employee cost as % of revenue (72.8% FY26, Q2 FY27 69.4%) rising two quarters running"}
  - {risk: "collection drift", first_signal: "unbilled revenue growing faster than revenue; DSO above 80"}
  - {risk: "pricing and scope shift to fixed price", first_signal: "fixed price share above 15% with T&M below 85%"}
  - {risk: "offshore story failing", first_signal: "offshore share below 68% while margin is claimed to come from offshore"}
  - {risk: "FX", first_signal: "gap between reported and constant currency growth narrowing; other income FX swing"}
  - {risk: "billing system control", first_signal: "audit trail paragraph repeated in FY27 auditor's report"}
mgmt_questions:
  - "Offshore share fell from 72% to 69% YoY while margin rose 130 bps. What drove the margin: utilisation, rate, currency or the Rs 2.93 Cr credit?"
  - "What share of revenue and receivables sits with the 18.3% customer, and when does its contract renew?"
  - "In the Rs 44.5 Cr renewal, up 72%, how much is higher rate and how much is more scope?"
  - "Fixed price rose from 11% to 15% of revenue. Is this deliberate, and what margin does it carry versus time and material?"
  - "H1 FY27 added 432 heads against Rs 47.5 Cr more revenue. What utilisation and billing lag sit on these hires, and when do they bill?"
  - "What is the DSO path from 80 to 65-70 days, and is the delay customer approval or invoicing?"
  - "What share of revenue is data-centre related, and how much of the 15-18% guide depends on it?"
one_line_verdict: "A people-based engineering services business billed mostly by the hour, whose margin gain is real but not yet shown to come from price or offshore mix; it fits Consulting / Engineering services (25x), not Platform / SaaS."
analyst_note: "Sector row: the business sells engineer time (88% T&M, AR26 p.46), with no licence, ARR, product IP or per-seat price, so Consulting / Engineering services is the row the evidence supports. The alternative reading survives only for the 50% software-led work (AR26 p.11), which is still billed by time. Margin readings: (1) new base from offshore leverage and utilisation; (2) peak helped by a credit that mostly belongs to FY26, FX and a pre-policy offshore shift. Separating observation: Q3 and Q4 FY27 EBITDA margin ex credit, with offshore share, fixed price share and DSO. Filed so far: offshore share down 72% to 69%, H1 ex credit margin 13.1% vs 13.6%, Q2 ex credit 13.9%. Guide of 15 to 18% growth implies H2 revenue of about 306 to 322 Cr (derived, revenue-from-operations basis assumed), below the Q2 run rate of 340 Cr, so the revenue guide looks prudent. Use revenue per head, not reported ROCE."
```
