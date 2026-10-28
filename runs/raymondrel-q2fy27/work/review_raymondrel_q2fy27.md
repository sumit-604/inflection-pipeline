# QUARTERLY REVIEW: RAYMOND REALTY LIMITED (RAYMONDREL), Q2 FY27 (quarter and H1 ended 30-Sep-2026)

Agent A4 ANALYST | model claude-opus-5-5 | run date 28-Oct-2026 | Role 4 (Quarterly Results Review Protocol v1.4) then Role 5 (Quarterly Concall Analysis Protocol v1.1), presentation findings feeding both. Revision: correction loop 1 (A5 audit); change log after the closing block.

**Evidence caveats (read first).**
- CONCALL IS ASR. The transcript is a machine transcript (faster-whisper small.en). Speakers are unlabelled. Numbers may be misheard (CC L19). Every concall figure below is tagged `MGMT, unverified, ASR`. Where the concall and a filed document conflict, the filed document wins.
- Deck figures are management-compiled and "not subjected to review by Auditors or the Board" (PRE l742). Deck P&L/BS tie to the consolidated Reg 33 statements (equity 1,622 = RES L531; debt 1,220 = RES L535+L541), so the deck is read as consolidated.
- The ICICI Pru corporate-action filing has an A1 extraction only (no A2/A3 chain, orchestrator decision). It is carried as a capital event in Role 4.
- Anchor key: `RES L###` = results fulltext line (statements Rs Lakhs, converted ÷100 to Rs Cr; press release Rs Cr). `PRE l###` = presentation fulltext line. `CC L###` = concall fulltext line. `CA L###` = corporate-action fulltext line. `NOT L###` = Notion snapshot line. `[DER]` = A4 arithmetic on anchored figures. `ND` = not disclosed.
- Decision Status verified BEFORE framing: **WATCHLIST / AVOID** (NOT L8; digest line 6). Not held. Branch 8A-W. This is a THESIS CHECK.

---

## LEDGER RECONCILIATION PREAMBLE (contract item 1)

Ledger contains **13 notes / 16 turns / 46 slides. All 13 / 16 / 46 reviewed.**
- Results ledger: 13 notes (N01-N13), 184 line items, 23 zero-standing items (48 cells), 3 agenda items, 13 auditor paragraph rows, 874 of 874 structured IDs, 0 orphans; MISSING_FROM_STRUCTURED M1-M4 read by A3 at fulltext (UDINs, firm reg nos, place lines; non-numeric). All reviewed.
- Presentation ledger: 46 slides (43 with rows; dividers p18, p21, p25; image-only p13), 1,082 of 1,082 IDs, 0 orphans; M1 (phone number) immaterial. All reviewed.
- Concall ledger: 16 turns (R305-R320), 10 questions, 145 management numbers, 59 forward rows, 320 of 320 IDs, 0 orphans. All reviewed.
- Corporate action (no A2 ledger by orchestrator decision): 63 A1 rows (R001-R063) read directly by A4. All reviewed.
- A1 header inconsistency carried: presentation fulltext says `rendered_pages: [none]` while the structured header says p4-p44 were render-checked (PRE-A3 section 0). Internal arithmetic ties support the mapping.

**Findings incorporated:**
- Results A3: RES-A3-01 to RES-A3-23 (23).
- Presentation A3: PRE-A3-01 to PRE-A3-35 (35).
- Concall A3: FND-01 to FND-23 (23).
Total 81 findings. FORWARD-SIGNAL + AMBIGUOUS = 70; each maps to a Questions-for-Management row (Step 8.5 coverage map).

---

# SECTION A: RESULTS REVIEW (ROLE 4)

## STEP 0: PRE-FLIGHT

### 0A. Notion baseline (verified)
| Item | On file | Anchor |
|---|---|---|
| Decision Status | WATCHLIST / AVOID (framework-strict AVOID via Promoter CONCERN 3 Red; ring-fencing override permits WATCHLIST) | NOT L8, L404-408 (checklist file L3-8) |
| One-line thesis | Not buying at Rs 641 despite Rs 1,343 base FV Y3; WATCHLIST at MoS Rs 550 only if margin >=18% and CFO turns; breaks if net debt > Rs 1,500 Cr with -CFO or new Singhania event | NOT L363 |
| Entry / MoS / post-DA entry | Rs 550-611 / Rs 550 / Rs 500-550 (post-Devil's Advocate) | NOT L355, L1529 |
| Base FV Y3 (diluted) | Rs 1,343 (about Rs 1,277 if warrants convert) | NOT L339; digest L7 |
| Destination PE | 20x (sector cap binds); scenarios 15/20/25x | NOT L303, L309-311 |
| Projections (Role 1) | Bear rev CAGR 12% / EBITDA 14% / Y3 PAT Rs 280 Cr; Base 18% / 17% / Rs 478 Cr; Bull 25% / 20% / Rs 660 Cr | NOT L315-319 |
| FY27E / FY28E (11-Aug addendum) | Revenue ~Rs 3,600 Cr / Rs 4,150-4,300 Cr; PAT FY27 bear ~300, base 340-370, bull ~430; FY28 bear 280, base 410-430, bull 540 | NOT L979-993 |
| CFO path / net debt peak | FY27 -600, FY28 -200, FY29 +300; peak ~Rs 1,300 Cr FY28 | NOT L321 |
| Stop-loss / thesis broken | Rs 520 hard OR net debt > Rs 1,500 Cr OR new Singhania governance event OR 2 consecutive Q EBITDA <14% OR Q1 FY27 pre-sales YoY decline | checklist L13-15 (NOT L404-414) |
| Position size | Small (2-3%) max, ring-fencing only | NOT L8 |
| Promoter Verdict | CONCERN (3 Red) | NOT L8 |
| Pending rulings | (1) margin stop 14/15/18%; (2) net-debt test before/after warrant and AIF money | checklist L60-64 |

### 0B. Units
Statements in **Rs Lakhs** (RES L162, L203, L258, L461, L502, L557). Converted to **Rs Crores at ÷100**. Press release and deck in Rs Cr (RES L652; PRE l344). Concall in Rs Cr (spoken).

### 0C. Share count and capital events
| Item | Reading | Anchor |
|---|---|---|
| Paid-up capital | Rs 66.57 Cr (6,657 lakhs) in every period; 6,65,73,731 shares of Rs 10 | RES L194, L493 |
| Basic = diluted EPS | Yes, all 12 cells, despite share-based payment Rs 1.60 Cr H1 | RES L197-198, L496-497, L269 |
| Warrants | 66,57,373 at Rs 614 (Rs 408.76 Cr) approved at EGM 8-Oct-2026 (after period end); in-principle approvals 23-Oct; 25% upfront (~Rs 102 Cr) not received in H1 | NOT L8, L1158-1174; RES-A3-13 |
| Fully diluted count (per Notion) | 7,36,92,319 (incl. 4,61,215 ESOPs + warrants) | NOT L8 (14-Oct entry) |
| Equity roll-forward (consolidated) | 1,500.85 + PAT 66.49 - dividend 13.31 + SBP 1.60 = 1,555.63 vs reported 1,555.61 (diff Rs 0.02 Cr). No warrant money, no NCI in H1 | RES L494, L484, L585, L566, L530 [DER] |
| Dividend | Final Rs 2/share FY26 paid 14-Jul-2026 (Rs 13.31 Cr) | RES L324-325, L292 |
| No split, bonus, QIP or buyback | none disclosed | RES notes L309-327 |

**Capital event: ICICI Pru AIF investment agreement (Reg 30, 26-Oct-2026), post period.**

| Term | Filed reading | Concall reading (MGMT, unverified, ASR) | Status |
|---|---|---|---|
| Amount | Letter: investor "has agreed to invest an aggregate amount of Rs.210,00,00,000" (CA L49-50, R009). Annexure (d): "Up to Rs.210 Crores" (CA L130, R021, R060) | "up to 210 crores of rupees" as ICICI's 60% share (CC L197-198); "has raised 210 crores" (CC L145-146) | Wording conflict inside the filing: aggregate vs ceiling. Annexure is the itemised term; read Rs 210 Cr as a ceiling [INFERENCE] |
| Instrument | NOT DISCLOSED (CA R063 absence note) | OCPRS (CC L194, L490) | NOT DISCLOSED in filing |
| Issuer / entity | Ten X Realty West Limited (TXRWL), "material wholly owned subsidiary" (CA L42-43, R030, R059) | "10X realty best" (CC L378) | Filed: TXRWL. Notion Q1 linked the "10X Mahalakshmi SPV" to a pending deal (NOT L955, L1011); the filed vehicle is TXRWL, not Ten X Mahalaxmi Limited (RES L450 lists both as separate subsidiaries) |
| Parties | Three parties: TXRWL as issuer, the ICICI Pru fund as investor, and RRL itself as counterparty 3 (CA L44, L95-123) | n/a | FILED: the listed parent is a signatory. Why the parent signed, and what it undertakes, is NOT DISCLOSED |
| Project | "redevelopment for one of its projects in the MMR region" (CA L130-136); project name NOT DISCLOSED | Mahim project (CC L380) | Name NOT DISCLOSED in filing |
| Use of funds | facilitating redevelopment of that project (CA L132-136) | "joint equity investment will directly fund a high value redevelopment project" (CC L154-155) | consistent |
| Related-party status | Not an RPT; investor independent of promoter group (CA L148-157, R053-R054) | n/a | FILED: not RPT |
| Change in subsidiary shareholding / control | NOT DISCLOSED for TXRWL. Item (e) speaks only to the listed holding company: "No Impact on the management or control of the Listed Holding Company" (CA L138-142) | ICICI contributes 60% of capital, RR 40%; profit after a 5% execution fee split 60:40 (CC L196-201) | NOT DISCLOSED in filing. Concall implies TXRWL stops being wholly owned (FND-12) |
| Dilution at listed level | None described: the securities are to be issued by TXRWL as "Issuer" (CA L99-101); the filing describes no RRL securities | n/a | none at RRL; economic dilution at project level per concall |
| Price / economics | Price / TXRWL PAT: NOT COMPUTABLE. TXRWL earnings, debt and cash are NOT DISCLOSED (R063); the project is pre-launch (PRE l460-461), so trailing earnings are nil | 60% residual profit to ICICI at a "virtually zero" coupon (CC L197-201, L584-587); project IRR "around 25%" vs debt "under 10%"; "equity anyway is available at a higher rate" (CC L468-470) | The money is priced at the project equity return (IRR 20-25%), not at a debt rate (9.6%, RES L716) [DER on MGMT figures]. Positive for net debt if classified as equity; not cheaper capital. No premium for RRL's JDA rights or brand is visible beyond the 5% fee |
| Liability on listed company | "No restriction or liability imposed" (CA L144, R052) | n/a | FILED. Guarantees, puts, support: NOT DISCLOSED (R063) |
| Tranches / timing | NOT DISCLOSED | first part "in the next 30 days", entire sum "by March" (CC L376-377) | NOT DISCLOSED in filing |
| Coupon / return | NOT DISCLOSED | "coupon is virtually zero"; "no dividend payout, it is effectively zero" (CC L584-587) | NOT DISCLOSED |
| Tenure, conversion ratio, redemption, put | NOT DISCLOSED (R063) | "only for ease of movement of cash flow they have structured it as OCPRS" (CC L489-490) | NOT DISCLOSED |
| Conditions precedent | NOT DISCLOSED (R063) | n/a | NOT DISCLOSED |
| Securities issued | "only a signing ... no Securities has been issued yet"; issue to be intimated separately (CA L170-180, R055, R047) | "has raised" (CC L145) | Concall tense overstates: at 28-Oct the money was committed, not received (FND-14) |
| Accounting classification | NOT DISCLOSED | "it will not reflect as debt" (CC L486) | management assertion; Ind AS 32 terms decide (FND-13) |
| RR's own share | NOT DISCLOSED | RR contributes 40% (CC L198); analyst's "our 140 crore" unanswered (CC L480) | 210 / 0.60 x 0.40 = Rs 140 Cr [DER, candidate] |
| Execution date | 26-Oct-2026 (CA L188, R029) | n/a | FILED |

Feed to the pending net-debt ruling: see Step 5, "Pending ruling 2". A4 does not rule.

### 0D. Notes extraction (all 13 ledger notes)
| Note # | Subject | What it says | Rs Cr impact | Period | Comparability impact |
|---|---|---|---|---|---|
| N01 (S1) | Basis of preparation | Ind AS 34, s.133, Reg 33 (RES L309-314) | ND | all | none |
| N02 (S2) | Review and approval | Audit Committee reviewed; Board approved 27-Oct-2026; limited review done (RES L316-318) | ND | Q2/H1 | none |
| N03 (S3) | Segment | Single segment "Real Estate" (RES L320-322) | ND | all | whole balance sheet is the segment |
| N04 (S4) | Dividend | Final Rs 2/share FY26, AGM 14-Jul, paid 14-Jul (RES L324-325) | 13.31 cash (RES L292) | Q2 FY27 | financing outflow only |
| N05 (S5) | Regrouping | "Previous periods' figures have been regrouped" (RES L327) | ND | prior periods | Unquantified regrouping; no demerger or perimeter note (RES-A3-21) |
| N06 (C1) | Basis (consolidated) | same as N01 (RES L601-607) | ND | all | none |
| N07 (C2) | Review and approval (consolidated) | same as N02 (RES L609-611) | ND | Q2/H1 | none |
| N08 (C3) | Segment (consolidated) | single segment (RES L613-615) | ND | all | none |
| N09 (C4) | Dividend (consolidated) | same as N04 (RES L617-618) | 13.31 (RES L585) | Q2 FY27 | none |
| N10 (C5) | Regrouping (consolidated) | same as N05 (RES L620) | ND | prior | same as N05 |
| N11 | Standalone CF method | indirect method, Ind AS 7 (RES L305) | ND | H1 | none |
| N12 | Consolidated CF method | indirect method (RES L597) | ND | H1 | none |
| N13 | CF asterisk footnote | loss on PPE disposal below rounding (RES L268, L303) | <0.01 | H1 | none |

Absent notes: no exceptional item, no demerger/comparability note, no contingent liability, no RPT note, no EPS-adjustment note, no subsidiary-change note (RES-A3-21; ledger L37). Former name "Raymond Lifestyle Limited" sits only on the cover letter (RES L77).

Answers to the four note questions: (1) N05/N10 leave the Q2 FY26 and H1 FY26 perimeter unstated, so YoY comparisons carry a basis risk (A3-21; PRE-A3-12). (2) No note forces normalisation. (3) No recurring/one-off flag in notes; one-off-like items sit in the press release and deck (authority interest, BKC revenue). (4) N03 single segment means no entity or project split is filed.

**Auditor opinion check:** Limited review, conclusion **unmodified** on both standalone (RES L130-136) and consolidated (RES L385-392). No Emphasis of Matter, no Going Concern paragraph. Consolidated report carries reliance paragraphs: 5 subsidiaries reviewed by other auditors (Q2 PAT Rs 11.07 Cr, H1 loss Rs 8.10 Cr, assets Rs 3,871.04 Cr) (RES L394-407) and 2 subsidiaries reviewed by one joint auditor alone (assets Rs 1,881.04 Cr, H1 PAT Rs 6.64 Cr) (RES L409-420); "Our conclusion is not modified" (RES L422). Not a modification. AMBER for coverage: all 7 subsidiaries (63.0% of Q2 revenue, 72.7% of gross assets) sit outside joint review (RES-A3-06). The OCR value "(81 O)" resolves to (810) (RES-A3-07).

### 0E. Business type
Standard operating business (residential real estate developer, percentage-of-completion revenue per CC L233-234, MGMT ASR). Not a lender. Steps 1 and 5 apply.

▶ Checkpoint: Notion fetched with Decision Status, units Lakhs to Cr ÷100, share count flat, 13 notes tabled, auditor unmodified with reliance AMBER, business type standard.

---

## STEP 1: DATA EXTRACTION (Rs Cr; Lakhs ÷100)

Q2FY26 = quarter to 30-Sep-2025; Q1FY27 = to 30-Jun-2026; Q2FY27 = to 30-Sep-2026. FY27 full-year column is ND (H1 columns added because Q2 is a half-year filing).

### 1A. CONSOLIDATED (source: RES L466-497)
| Line item | Q2 FY26 | Q1 FY27 | Q2 FY27 | H1 FY26 | H1 FY27 | FY26 (audited) | FY27 | Line |
|---|---|---|---|---|---|---|---|---|
| Revenue from operations | 697.15 | 526.67 | 748.52 | 1,076.50 | 1,275.19 | 2,990.79 | ND | RES L466 |
| Other income | 8.64 | 9.04 | 8.97 | 21.15 | 18.01 | 48.63 | ND | RES L467 |
| Total income | 705.79 | 535.71 | 757.49 | 1,097.65 | 1,293.20 | 3,039.42 | ND | RES L468 |
| Cost of land, development, construction | 1,373.91 | 413.86 | 1,260.82 | 1,628.95 | 1,674.68 | 4,864.99 | ND | RES L471 |
| Change in inventories | (870.39) | (47.68) | (739.44) | (864.26) | (787.12) | (2,722.79) | ND | RES L473 |
| Employee benefits | 33.98 | 39.62 | 47.71 | 63.18 | 87.33 | 138.39 | ND | RES L474 |
| Finance costs | 25.61 | 47.17 | 43.53 | 40.19 | 90.70 | 97.69 | ND | RES L475 |
| Depreciation | 5.33 | 7.87 | 5.39 | 10.49 | 13.26 | 23.13 | ND | RES L476 |
| Other expenses | 67.23 | 59.70 | 73.16 | 127.53 | 132.86 | 263.37 | ND | RES L477 |
| Total expenses | 635.67 | 520.54 | 691.17 | 1,006.08 | 1,211.71 | 2,664.78 | ND | RES L478 |
| PBT | 70.12 | 15.17 | 66.32 | 91.57 | 81.49 | 374.64 | ND | RES L479 |
| Tax (current + deferred) | 9.94 | 1.74 | 13.26 | 14.89 | 15.00 | 70.05 | ND | RES L481-483 |
| PAT | 60.18 | 13.43 | 53.06 | 76.68 | 66.49 | 304.59 | ND | RES L484 |
| EPS reported (Rs) | 9.04 | 2.02 | 7.97 | 11.52 | 9.99 | 45.52 | ND | RES L496 |
| EPS share-adjusted (Rs) | 9.04 | 2.02 | 7.97 | 11.52 | 9.99 | 45.52 | ND | no share change (RES L493) |

### 1B. STANDALONE (source: RES L167-198)
| Line item | Q2 FY26 | Q1 FY27 | Q2 FY27 | H1 FY26 | H1 FY27 | FY26 | FY27 | Line |
|---|---|---|---|---|---|---|---|---|
| Revenue from operations | 391.76 | 239.89 | 279.95 | 703.67 | 519.84 | 1,615.74 | ND | RES L167 |
| Other income | 23.00 | 27.64 | 30.27 | 45.43 | 57.91 | 109.94 | ND | RES L168 |
| Total income | 414.76 | 267.53 | 310.22 | 749.10 | 577.75 | 1,725.68 | ND | RES L169 |
| Cost of land, development, construction | 288.64 | 276.37 | 173.31 | 503.79 | 449.68 | 1,286.77 | ND | RES L172 |
| Change in inventories | (46.89) | (136.08) | (28.64) | (51.63) | (164.72) | (296.38) | ND | RES L174 |
| Employee benefits | 31.54 | 34.34 | 41.61 | 59.18 | 75.95 | 127.83 | ND | RES L175 |
| Finance costs | 11.46 | 21.71 | 19.01 | 19.84 | 40.72 | 59.88 | ND | RES L176 |
| Depreciation | 5.02 | 3.59 | 4.10 | 9.90 | 7.69 | 20.22 | ND | RES L177 |
| Other expenses | 53.61 | 35.04 | 50.06 | 103.29 | 85.10 | 201.91 | ND | RES L178 |
| Total expenses | 343.38 | 234.97 | 259.45 | 644.37 | 494.42 | 1,400.23 | ND | RES L179 |
| PBT | 71.38 | 32.56 | 50.77 | 104.73 | 83.33 | 325.45 | ND | RES L180 |
| Tax | 12.97 | 6.18 | 9.22 | 19.39 | 15.40 | 62.73 | ND | RES L184 |
| PAT | 58.41 | 26.38 | 41.55 | 85.34 | 67.93 | 262.72 | ND | RES L185 |
| EPS reported (Rs) | 8.77 | 3.96 | 6.24 | 12.82 | 10.20 | 39.23 | ND | RES L197 |
| EPS share-adjusted (Rs) | 8.77 | 3.96 | 6.24 | 12.82 | 10.20 | 39.23 | ND | no share change |

### 1C. Derived metrics [DER on rows above]
Consolidated:
| Metric | Formula | Q2 FY26 | Q1 FY27 | Q2 FY27 | H1 FY26 | H1 FY27 | FY26 | FY27 |
|---|---|---|---|---|---|---|---|---|
| Operating EBITDA | PBT + D + Fin - OI | 92.42 | 61.17 | 106.27 | 121.10 | 167.44 | 446.83 | ND |
| Operating EBITDA margin | Op EBITDA / Revenue | 13.26% | 11.61% | 14.20% | 11.25% | 13.13% | 14.94% | ND |
| Reported EBITDA | PBT + D + Fin | 101.06 | 70.21 | 115.24 | 142.25 | 185.45 | 495.46 | ND |
| Reported EBITDA / total income (press-release basis) | as named | 14.32% | 13.11% | 15.21% | 12.96% | 14.34% | 16.30% | ND |
| Core PBT (ex-OI) | PBT - OI | 61.48 | 6.13 | 57.35 | 70.42 | 63.48 | 326.01 | ND |
| OI / PBT | OI / PBT | 12.3% | 59.6% | 13.5% | 23.1% | 22.1% | 13.0% | ND |
| Effective tax rate | Tax / PBT | 14.2% | 11.5% | 20.0% | 16.3% | 18.4% | 18.7% | ND |
| PAT margin (on revenue) | PAT / Revenue | 8.63% | 2.55% | 7.09% | 7.12% | 5.21% | 10.18% | ND |

Press release reconciles: EBITDA 115 = 115.24; margin "15%" = 15.21%; PBT 66 = 66.32 (RES L653-656; RES-A3-14). Deck EBITDA includes other income (PRE-A3-35).

Standalone:
| Metric | Q2 FY26 | Q1 FY27 | Q2 FY27 | H1 FY26 | H1 FY27 | FY26 | FY27 |
|---|---|---|---|---|---|---|---|
| Operating EBITDA | 64.86 | 30.22 | 43.61 | 89.04 | 73.83 | 295.61 | ND |
| Operating EBITDA margin | 16.56% | 12.60% | 15.58% | 12.65% | 14.20% | 18.30% | ND |
| Reported EBITDA | 87.86 | 57.86 | 73.88 | 134.47 | 131.74 | 405.55 | ND |
| Core PBT (ex-OI) | 48.38 | 4.92 | 20.50 | 59.30 | 25.42 | 215.51 | ND |
| OI / PBT | 32.2% | 84.9% | 59.6% | 43.4% | 69.5% | 33.8% | ND |
| ETR | 18.2% | 19.0% | 18.2% | 18.5% | 18.5% | 19.3% | ND |
| PAT margin | 14.9% | 11.0% | 14.8% | 12.1% | 13.1% | 16.3% | ND |

Standalone other income is mostly interest on loans to subsidiaries (interest income Rs 51.18 Cr H1, RES L265). Standalone core PBT is thin: Rs 20.50 Cr in Q2.

### 1D. STANDALONE vs CONSOLIDATED GAP (first-class metric, from RES-A3-04)
| Period | Standalone PAT | Consolidated PAT | C - S | (C - S) / S | Anchor |
|---|---|---|---|---|---|
| Q2 FY27 | 41.55 | 53.06 | +11.51 | +27.7% | RES L185, L484 |
| Q1 FY27 | 26.38 | 13.43 | -12.95 | -49.1% | same |
| Q2 FY26 | 58.41 | 60.18 | +1.77 | +3.0% | same |
| H1 FY27 | 67.93 | 66.49 | -1.44 | -2.1% | same |
| H1 FY26 | 85.34 | 76.68 | -8.66 | -10.1% | same |
| FY26 | 262.72 | 304.59 | +41.87 | +15.9% | same |

Swing +24.7 pp YoY and +76.8 pp QoQ. Standalone share of consolidated revenue: Q2 FY27 37.4% (279.95/748.52), Q1 FY27 45.5%, Q2 FY26 56.2% [DER]. Subsidiary Q2 PAT Rs 11.07 + 0.02 = Rs 11.09 Cr (RES L397-398, L411-412). Read: the consolidated print now depends on lumpy recognition inside JDA subsidiaries that sit outside joint review (RES-A3-04, -06).

▶ Checkpoint: every cell filled or ND.

---

## STEP 2: Q2 YoY COMPARISON (Q2 FY27 vs Q2 FY26)

Consolidated:
| Metric | Q2 FY26 | Q2 FY27 | YoY | Verdict |
|---|---|---|---|---|
| Revenue from operations | 697.15 | 748.52 | +7.4% | Weak vs ~20% guide reading |
| Operating EBITDA | 92.42 | 106.27 | +15.0% | Positive |
| Operating EBITDA margin | 13.26% | 14.20% | +94 bps | Up, still below 17-19% guide |
| Operating EBITDA, authority-adjusted (authority interest Q2 FY26 Rs 10 Cr, Q2 FY27 Rs 17 Cr treated as approval cost; PRE l365, R316, R315) [DER] | 82.42 | 89.27 | +8.3% | Modest |
| Operating EBITDA margin, authority-adjusted [DER] | 11.82% | 11.93% | +10 bps | Flat |
| Depreciation | 5.33 | 5.39 | +1.1% | Flat |
| Finance costs | 25.61 | 43.53 | +70.0% | Adverse |
| EBIT (operating) = Op EBITDA - D | 87.09 | 100.88 | +15.8% | Positive |
| Other income | 8.64 | 8.97 | +3.8% | Flat, immaterial |
| Core operating PBT (PBT - OI) | 61.48 | 57.35 | -6.7% | Adverse |
| Reported PBT | 70.12 | 66.32 | -5.4% | Adverse |
| PAT | 60.18 | 53.06 | -11.8% | Adverse |
| EPS (share-adjusted) | 9.04 | 7.97 | -11.8% | Adverse |

Standalone: revenue 391.76 to 279.95 (-28.5%); op EBITDA 64.86 to 43.61 (-32.8%); PBT 71.38 to 50.77 (-28.9%); PAT 58.41 to 41.55 (-28.9%) (RES L167-185).

Diagnostic answers:
1. Revenue grew 7.4% YoY (Q2 FY27 vs Q2 FY26). Management withdrew the revenue guide (CC L230; FND-03); the Notion addendum base is +20% (NOT L982). Q2 sits well below that reading. Caveat: the Q2 FY26 base carries Rs 175 Cr of BKC revenue booked before BKC's Q3 FY26 launch with zero bookings (PRE l707; PRE-A3-25, render-mapped, verifier to confirm). Ex-BKC, revenue would be 522 to 695, +33% [DER, conditional on that mapping].
2. Operating EBITDA margin: Q2 FY27 14.20% vs Q2 FY26 13.26% = +94 bps YoY. Reported (with OI, on total income): 15.21% vs 14.32% = +89 bps. Sequential Q1 to Q2: 11.61% to 14.20% (operating). **Authority-adjusted** (interest to BMC/TMC/MHADA on approval dues treated as approval cost, PRE l365): Q2 op EBITDA Rs 82.42 Cr to Rs 89.27 Cr, +8.3% YoY; margin 11.82% to 11.93%, +10 bps [DER]. H1 on the same basis (authority interest 16 to 36, R318, R317): 105.10 to 131.44, +25.1%, margin 9.76% to 10.31%, +54 bps, vs +38.3% and +188 bps unadjusted [DER]. Deck authority figures are rounded to whole crores, so the Q2 growth range is about 7.6-9.0%. Most of the reported +94 bps comes from where approval-linked interest is classified. Separating observation: the answer on principal owed to authorities and its balance-sheet line (Q4).
3. Core operating PBT fell 6.7% YoY (61.48 to 57.35). Reported PAT fell 11.8%. Operating EBITDA rose 15.0%. **The operating gain did not reach the bottom line**: finance costs absorbed it.
4. Gap drivers (PBT change -3.80): op EBITDA +13.85, D&A -0.06, finance -17.92, OI +0.33. PAT change -7.12 adds tax -3.32 (ETR 14.2% to 20.0%). No exceptional items.
5. Finance costs +70.0% vs revenue +7.4%: capital-absorption gap. Split: bank interest 16 to 27; authority interest 10 to 17 (PRE l364-365, R311-R318; RES L717-719). D&A flat.
6. Other income is flat at 8.6-9.0 per quarter (1.2% of revenue). No treasury masking at consolidated level. At standalone, OI is 59.6% of Q2 PBT (intra-group interest).

▶ Checkpoint shown.

---

## STEP 3: SEQUENTIAL TRAJECTORY (consolidated)

Q3 FY26 and Q4 FY26 are not separately filed; H2 FY26 is FY26 minus H1 FY26 [DER].

| Quarter | Revenue | Op EBITDA margin | Reported EBITDA / TI | Core PBT (ex-OI) | One-offs flagged | Run-rate note |
|---|---|---|---|---|---|---|
| Q1 FY26 [DER H1-Q2] | 379.35 | 7.56% | 10.51% | 8.94 | none filed | trough |
| Q2 FY26 | 697.15 | 13.26% | 14.32% | 61.48 | BKC Rs 175 Cr pre-launch revenue (PRE-A3-25) | step-up |
| Q3 FY26 | ND | ND | ND | ND | ND | ND |
| Q4 FY26 | ND | ND | ND | ND | ND | ND |
| H2 FY26 [DER FY-H1], per half | 1,914.29 | 17.02% | 18.19% | 255.59 | Q4 launch-mix outlier per Notion risk #4 (checklist L26) | peak half |
| Q1 FY27 | 526.67 | 11.61% | 13.11% | 6.13 | none filed | dip; authority interest Rs 19 Cr [DER 36-17, PRE l365] is recurring (Q2 17, H1 36), not a one-off |
| Q2 FY27 | 748.52 | 14.20% | 15.21% | 57.35 | Tower B OC (Thane) in quarter (RES L687) | recovering |

Diagnostics:
- Trajectory: RECOVERING within H1 (Q1 to Q2 revenue +42.1%, op margin +259 bps). H1 FY27 sits below H2 FY26 on every line. The business is H2-weighted: H1 FY26 was 36.0% of FY26 revenue and 25.2% of FY26 PAT [DER].
- Distortions: Q2 FY26 base (BKC pre-launch revenue); Q2 FY27 OC trigger at Thane Tower B (RES-A3-05). Neither is quantified in the filing.
- Latest quarter vs H1 average: Q2 revenue 748.52 vs H1 average 637.60, above. Q2 op margin 14.20% vs H1 13.13%, above.
- Implied Q3 base: to reach the 17% low end of the FY27 EBITDA guide on total income equal to FY26 (3,039.42), H2 must run 19.0% (Rs 331.3 Cr on Rs 1,746.2 Cr); at FY26 x 1.20 total income (3,647.30), H2 must run 18.5% [DER]. Q3 needs a reported EBITDA margin near 18-19% to keep the guide alive.

---

## STEP 4: OPERATIONAL DECOMPOSITION (consolidated PAT bridge)

### 4A. Q2 FY27 vs Q2 FY26 (PAT 60.18 to 53.06)
| Component | YoY change (Rs Cr) | % of base PAT 60.18 | Recurring? |
|---|---|---|---|
| Revenue contribution (Δrevenue 51.37 x prior op margin 13.26%) | +6.81 | +11.3% | Recurring |
| Margin change contribution (residual of op EBITDA +13.85) | +7.04 | +11.7% | Recurring (mix-dependent) |
| D&A change | -0.06 | -0.1% | Recurring |
| Finance cost change (bank +11, authority +7, PRE l364-365) | -17.92 | -29.8% | Recurring (post-debt) |
| Other income change | +0.33 | +0.5% | Non-recurring typically |
| Effective tax rate change (14.2% to 20.0%; volume effect +0.54, rate effect -3.86) | -3.32 | -5.5% | Mixed |
| Exceptional items | 0.00 | 0.0% | n/a (none filed) |
| **Reported PAT YoY change** | **-7.12** | **-11.8%** | |

### 4B. H1 FY27 vs H1 FY26 (PAT 76.68 to 66.49)
| Component | Change | Recurring? |
|---|---|---|
| Revenue contribution (198.69 x 11.25%) | +22.35 | Recurring |
| Margin change | +23.99 | Recurring |
| D&A | -2.77 | Recurring |
| Finance cost | -50.51 | Recurring |
| Other income | -3.14 | Non-recurring |
| Tax | -0.11 | Mixed |
| Exceptional | 0.00 | n/a |
| **PAT change** | **-10.19 (-13.3%)** | |

Answers:
- All of the YoY PAT decline is recurring: higher finance cost (-17.92 Q2; -50.51 H1) outweighs recurring operating gains (+13.85 Q2; +46.34 H1). Other income is immaterial.
- If OI reverted to the prior-year level, Q2 PAT would move by about -0.27 after tax [DER]. Run-rate is unchanged.
- Finance cost is not at steady state. Management guides H2 at the H1 run rate (CC L266-267, MGMT ASR), about Rs 181 Cr for FY27 [DER 90.70 x 2] vs Rs 97.69 Cr in FY26. Debt will not fall for 1-2 years (CC L471-472).
- Tax: ETR stays below 25.17% statutory in every period (consolidated 11.5-20.0%); deferred tax moved from credit (-4.10 Q1) to charge (+4.69 Q2) (RES L482). The shield source is not disclosed (RES-A3-12; PRE-A3-14). Taxes paid 29.46 exceed current tax 14.41 in H1 (RES L573, L481). Step-up risk flagged.

---

## STEP 5: CASH QUALITY AND BALANCE SHEET (H1 statements; Rs Cr)

| Metric | Consolidated H1 FY26 / Mar-26 | Consolidated H1 FY27 / Sep-26 | Change | Standalone prior | Standalone current | Verdict |
|---|---|---|---|---|---|---|
| CFO | -319.08 (RES L574) | -147.02 (RES L574) | +172.06 | 33.19 (RES L277) | 142.38 (RES L277) | Consolidated negative, improving |
| CFO / PAT | -4.16x | -2.21x | improved | 0.39x | 2.10x | Below every Pillar 2 band |
| Capex (PPE incl. CWIP) | 18.10 (RES L576) | 20.69 | +2.59 | 24.70 (RES L279) | 10.09 | Small |
| FCF (CFO - capex) | -337.18 | -167.71 | +169.47 | 8.49 | 132.29 | Negative at group |
| Working-capital change (receivables + inventories + payables) | -407.01 (RES L569-571) | -291.20 | +115.81 | -24.81 (RES L272-274) | +85.22 | Inventory build funded by advances [INFERENCE] |
| Receivable days [DER, annualised H1 revenue] | 27.5 (Mar-26, FY26 rev) | 32.0 | +4.5 | 36.2 | 66.6 | Rising |
| Inventory days [DER, on cost of revenue] | 729 | 1,028 | +299 | 352 | 673 | Structural for POCM developer; direction adverse |
| Payable days [DER, on cost of land/dev] | 124 | 175 | +51 | 255 | 349 | Rising |
| Cash conversion cycle [DER] | 633 | 885 | +252 | 134 | 391 | Lengthening |
| PPE | 88.59 (RES L506) | 85.66 | -2.93 | 61.19 (RES L207) | 59.42 | n/a |
| CWIP | 5.28 (RES L507) | 13.61 | +8.33 | 0.49 | 2.62 | n/a |
| Gross debt | 1,013.75 (RES L535+L541) | 1,219.73 | +205.98 | 660.75 (RES L238+L243) | 626.71 | Rising at group, flat at holding |
| Liquid funds (cash + other bank + current investments) | 356.00 (RES L519-522) | 303.58 | -52.42 | 208.61 (RES L221-224) | 179.27 | |
| Net debt / (net cash) | 657.75 | 916.15 (PR 912, RES L646) | +258.40 | 452.14 | 447.44 | Rising; first-signal lines lit |
| Gross D/E | 0.647 | 0.752 (PR "0.8x") | +0.105 | 0.425 | 0.389 | Above 0.75 first signal |
| Net D/E | 0.420 | 0.565 (CC "closer to 0.5") | +0.145 | 0.291 | 0.278 | |
| Promoter pledge | ND | ND | ND | ND | ND | Not disclosed |

Balance-sheet movements behind CFO (consolidated): inventories +717.60 (+16.8%) to 4,998.47 (RES L517); other current liabilities +479.59 (+47.2%) to 1,495.95 (RES L546; the line's composition is not disclosed; reading it as mainly customer advances is [INFERENCE]); other financial liabilities +148.00 to 1,908.20 (RES L545), outside borrowings and outside PR net debt (RES-A3-17). Standalone loans to subsidiaries 1,191.64 vs 1,068.30 (RES L212+L225), funded through a new ICD caption of Rs 127.60 Cr (RES L285; RES-A3-01). Standalone CFO rests on a Rs 217.39 Cr fall in other current assets (RES L227) that the group does not mirror (RES-A3-20), so standalone CFO is not evidence of collections.

Interest cash check (partly answers PRE-A3-16): finance costs paid Rs 85.75 Cr (RES L586) vs P&L finance cost Rs 90.70 Cr (RES L475), 94.5% paid in cash. Gross debt rose 205.98 vs net borrowing inflow 200.58 (RES L582-584), gap Rs 5.40 Cr [DER]. At the statutory level interest is not accruing into debt. The deck's management cash format has no interest line: it shows a bank-loan inflow of Rs 155 Cr (R366) and a "Finance, Legal & IT Cost" line of Rs 26 Cr (PRE l401, R363), which is a corporate-cost line, not interest. PRE-A3-16's comparison of that Rs 26 Cr line with Rs 55 Cr of bank interest therefore rests on a label misread. The open item is where the Rs 85.75 Cr of interest paid sits in the deck format, and how the Rs 155 Cr bank-loan line reconciles to Rs 200.58 Cr of net borrowing (Q5).

Mandatory answers:
- **Pillar 2 band.** H1 CFO/PAT is -2.21x (consolidated). On file: CFO/PAT -2.98x, base multiplier 0.80x, growth offset +0.10, effective 0.90x (NOT L289). H1 is negative and outside every band (0.65-1.30x). The recompute is deferred to /fttcp and Role 1 (OR-30); flagged as pillar-relevant.
- **Structural vs growth-induced.** Evidence for growth-induced: the mature cohort generated +Rs 364 Cr project OCF while newly launched (-135) and pre-launch (-184) cohorts consumed cash (PRE l398, R357-R359; MGMT, unreviewed); the other-current-liabilities line, if mainly customer advances [INFERENCE], funded 67% of the inventory build [DER 479.59/717.60]. Evidence against: JDA revenue recognised to date Rs 2,549 Cr on the project rows (Bandra 1,345, BKC 577, Sion 242, Wadala 385; R446, R454, R464, R472) vs JDA collections Rs 857 Cr (PRE-A3-27); BKC revenue 577 exceeds bookings 521 and Sion 242 exceeds 229 (PRE-A3-24, -26). Collections to date include GST and other possession charges (PRE l149, l444); revenue excludes GST; the GST amount is NOT DISCLOSED, so the revenue-to-cash gap is wider than shown. **The deck contradicts itself on JDA revenue:** p5 states revenue recognised of Rs 9,500 Cr in total, of which owned land Rs 7,570 Cr and JDAs Rs 1,930 Cr (R037-R039), while the project rows total Rs 10,078 Cr (R478). Owned land agrees within Rs 41 Cr (7,570 vs 7,529 from the p26 owned rows). The whole Rs 619 Cr gap sits in JDAs (2,549 - 1,930). p5 ties JDA revenue to sold units (sold 3,430 = recognised 1,930 + balance 1,500; R036, R039, R042). [INFERENCE] The Rs 619 Cr may be the revenue not tied to unit sales (for example a landowner share) behind Q1. This also revises PRE-A3-21's reading: the gap is Rs 619 Cr within JDAs, not the BKC Rs 577 Cr. No rating-agency WC assessment was passed this run. Classification: **INDETERMINATE-WITH-DIRECTION** (direction: growth-induced, improving YoY). Missing evidence: statutory project or entity cash split; the Ind AS 115 basis for JDA revenue above bookings and the p5 vs p26 reconciliation; Q3/Q4 CFO.
- **CWIP.** No major capex commissioning in this model; CWIP Rs 13.61 Cr is immaterial.
- **Net debt vs projection.** Rs 916 Cr computed (PR 912) vs Rs 658 Cr at Mar-26; +Rs 258 Cr in H1, about Rs 129 Cr per quarter vs the tracker's +Rs 90 Cr (RES-A3-16). Model peak ~Rs 1,300 Cr FY28 (NOT L321). At the H1 pace, the Rs 1,000 Cr line is crossed in Q3 FY27 before any third-party money [INFERENCE, conditional].

### Pending ruling 2: net-debt lines before or after warrant and AIF money (evidence only; A4 does not rule)
| Reading | Q2 FY27 net debt (actual) | Pro forma after inflows | Rs 1,000 Cr checklist red | Rs 1,500 Cr thesis stop | Risk #2 first signal > Rs 900 Cr |
|---|---|---|---|---|---|
| R1: before both inflows (tests underlying burn) | 916 (PR 912) | 916 (inflows excluded by definition) | Not fired at Q2; crosses in Q3 at H1 pace [INFERENCE] | Not fired | LIT |
| R2: after warrant Rs 102 Cr; AIF as equity (NCI) | 916 | 916 - 102 - 210 = 604 [DER, once both land and before spend] | Not fired | Not fired | Not lit |
| R3: after warrant; AIF debt-like (OCPRS with a put, redemption or fixed return) | 916 | 916 - 102 = 814 (AIF cash offsets the AIF liability) | Not fired | Not fired | Not lit |
| R4: AIF debt-like and fully spent; warrant excluded (Notion Key Notes framing) | 916 | 916 + 210 = 1,126 (Notion ~1,124, NOT L8) | Would fire | Not fired | LIT |

Facts for the ruling:
- No warrant or AIF money arrived by 30-Sep. The equity roll closes on PAT, dividend and SBP only (RES-A3-13). CA L170-172 says no securities were issued at 26-Oct. **At Q2 all four readings score the same: Rs 912-916 Cr, no stop fired.** The ruling binds from Q3.
- The AIF instrument is filed as NOT DISCLOSED (CA R063). Management calls it OCPRS, "virtually zero" coupon, "will not reflect as debt" (CC L486, L584-587; MGMT ASR). RRL is itself a party to the agreement (CA L121-123); any undertaking it gives is NOT DISCLOSED beyond item (f) "No restriction or liability imposed" (CA L144).
- Rs 1,908.20 Cr of other financial liabilities sits outside PR net debt (RES L545). Its composition is not disclosed (RES-A3-17). Authority dues (interest Rs 17 Cr in Q2, PRE l365) are a debt-like leg outside the Rs 1,220 Cr gross debt (FND-08; PRE-A3-28).
- **The one observation that separates the readings:** the securities-issue intimation promised under CA item (i) (CA L174-180), and the Q3 FY27 consolidated balance sheet. An NCI line with no borrowing or OFL increase supports R2. A borrowing or OFL increase of about Rs 210 Cr supports R3/R4.

---

## STEP 5.5: DOWNSTREAM SIGNAL RECONCILIATION

### 5.5A. Tracker pull
**Tracker rows not supplied (titles only).** Five linked titles (checklist L67-73). Readings below come from this quarter's documents, not from tracker observations.
| Signal (title only) | Type | Cadence | Latest observation (this quarter, own docs) | Direction | Thesis element | Health |
|---|---|---|---|---|---|---|
| Q2 FY27 EBITDA margin vs two-quarter stop-loss (Q1 13%) | Company KPI | Quarterly | Q2 15.21% reported / 14.20% operating (RES L479, L475-476) | Rising | Margin stop | Neutral (basis-dependent) |
| Net debt vs Rs 1,000 Cr line (Rs 914 Cr at Q2, +Rs 90 Cr/qtr) | Company KPI | Quarterly | Rs 916 computed / 912 PR; H1 pace +Rs 129/qtr | Rising | I-3, stop | Threatens |
| H1 FY27 CFO vs model FY27 -Rs 600 Cr | Company KPI | Half-yearly | -Rs 147.02 Cr (RES L574) | Improving | Pillar 2, I-7 | Confirms base path |
| Warrant money received (Rs 102 Cr upfront) vs net debt ex-warrants | Capital event | Event | Not received in H1 (RES-A3-13); concall says "has infused" (CC L208, contradicted) | n/a | Net-debt ruling | Neutral |
| Thane Jekegram launch (RERA) in FY27 vs warrant objects Rs 247 Cr | Launch | Event | Deck: Thane owned parcel launch Q2 FY28 (PRE l464; PRE-A3-08) | Delayed | Warrant objects, NAV | Threatens |

Fewer than three external signals are available: all five rows are company-derived. Flag: Role 5.5 should reopen for external signals (MMR registrations, housing-loan rates, cement and steel prices).

### 5.5B. Reconciliation
Target reported: MIXED (bookings strong; PAT down; cash negative). Signals: tracker values not supplied. Outcome: **not assessable on the four-outcome matrix this run**. The company's own leading indicators (pre-sales +98%, collections +67%; RES L634-640) point to "strong", while the P&L lags under POCM.

### 5.5C. New signals (payload only; written only through the operator-approval gate)
- Proposed new signal: "TXRWL OCPRS terms and classification (securities-issue intimation; Q3 BS NCI vs borrowing)", Case B, because the instrument decides the net-debt reading.
- Proposed new signal: "BKC aviation height approval and RERA for upper floors", Case B, because H2 Invictus BKC pre-sales depend on it (FND-16).
- Proposed new signal: "JDA revenue recognised vs JDA collections (deck p7/p26)", Case B, because it tests I-2 and revenue quality (PRE-A3-27).
- Proposed new signal: "Interest to government authorities (quarterly) and principal outstanding", Case A (attach to the net-debt row), because it is a debt-like leg outside gross debt.

### 5.5D. Forward view weighting
No multi-month external signal is available to outweigh the single print. Step 6 proceeds on filed numbers alone.

---

## STEP 6: RECONCILIATION VS THESIS

### 6A. Variance vs Notion projections (FY27; H1 actual extrapolated only where stated)
| Metric | Bear | Base | Bull | Actual (H1 FY27) | Lands in |
|---|---|---|---|---|---|
| Revenue FY27 | 3,350 [DER 2,990.79 x 1.12] | ~3,600 (NOT L982) | 3,739 [DER x 1.25] | H1 1,275.19 (RES L466); H1-seasonality FY run-rate 3,543 [DER 1,275.19/0.3599] | Between bear and base (near base) |
| EBITDA margin | 14% | 17% | 20% (NOT L317-319) | H1 14.34% on total income; 14.54% on revenue | At bear |
| PAT FY27 | ~300 | 340-370 | ~430 (NOT L991) | H1 66.49 (RES L484); seasonality run-rate 264 [DER 66.49/0.2517]; H2-bridge method 276-309 on Reading B revenue (Forward Estimate Inputs) | Below bear on seasonality; straddles bear on the bridge |
| EPS FY27 | 45 | 51-56 | 65 (NOT L991) | H1 9.99; seasonality run-rate 39.7 [DER 264/6.6574]; bridge 41.5-46.4 | Below bear to at bear |
| Net debt | path to ~1,300 peak FY28 | same | n/a (NOT L321) | 916 at Sep-26 | On or above path (faster than tracker pace) |
| ROCE | 22-24% mid-cycle (NOT L321) | same | n/a | Not disclosed. H1 annualised EBIT / average (equity + gross debt) = 12.7% [DER, seasonal: 344.38 / avg of 2,581.17 and 2,841.91]. FY26 on the same basis 23.4% [DER: EBIT 472.33 / avg of FY25 capital 1,459 (deck, PRE l180 R127) and Mar-26 2,581.17]; 18.3% on closing capital only. Notion 30.5% uses a different basis | UNKNOWN on a like-for-like basis; H1 seasonal reading is below all cases |

Probability re-weighting rule: below bear on 2+ key metrics for 2 consecutive quarters. This quarter: the PAT seasonality run-rate sits below bear, while the bridge method straddles bear (264-309 vs 300); EPS is PAT divided by an unchanged count, so effectively the same metric. EBITDA margin sits at bear. Q1 FY27 had no Reg 33 data in the prior review (NOT L878). **Rule not triggered.** Flag: if Q3 also prints below bear on PAT and margin, the rule fires at the next valuation refresh.

### 6B. Watchlist item status (Notion checklist L32-43; inflection block L48-56)
| # | Item | Green | Red | This quarter | Status |
|---|---|---|---|---|---|
| 1 | EBITDA margin | >=18% sustained | <15% for 2 consecutive Q | Q1 13.11% / Q2 15.21% reported; Q1 11.61% / Q2 14.20% operating (RES L466-479) | AMBER on reported basis; RED on operating basis (ruling pending) |
| 2 | Booking value | >= Rs 500 Cr | < Rs 350 Cr | Q2 Rs 902 Cr; Q1 Rs 700 Cr (RES L634-636) | GREEN |
| 3 | Net debt | stable/declining from Rs 656 Cr | > Rs 1,000 Cr by Q2; Rs 1,500 Cr exit | Rs 916 Cr (PR 912), +258 in H1 | AMBER |
| 4 | Mahim 1 & 2 launch | Q3 FY27 launch as guided | delay to Q4 FY27+ | Mahim-2 Q3 FY27, Mahim-1 Q4 FY27 (PRE l460-461); PR "next two quarters" (RES L702-704); no RERA yet | AMBER (Mahim-1 in red window) |
| 5 | New JDA signings vs Rs 8,000 Cr | >= Rs 5,000 Cr by Q3 | < Rs 3,000 Cr full year | ~Rs 8,500 Cr added in H1 on gross GDV (CC L72-74, MGMT ASR); GDV 42,000 to 52,000 (PRE l178). The addition equals Parel's listed GDV of Rs 8,500 Cr (R493) at 55% economic interest (R491): about Rs 4,675 Cr at RRL's share if the addition is Parel [DER; INFERENCE that it is Parel] | GREEN on gross GDV; AMBER at economic interest (below the Rs 5,000 Cr green line) (I-5 caution) |
| 6 | Related-party loans to subs | stable Rs 1,000-1,200 Cr | > Rs 1,500 Cr | Standalone loans Rs 1,191.64 Cr, +123 in H1 (RES L212, L225) | GREEN at upper edge; trend adverse |
| 7 | Promoter governance event | silence | new RPT or SEBI action | No event in any document; deck "Board Independence : 100% i.e. All the Board Committees are chaired by Independent Director" (PRE l218-220) while 5 of 8 directors are independent (PRE-A3-19) | GREEN (drafting point logged) |
| 8 | Cost of debt | 9.5-9.75% | > 10.5% | 9.60% headline (RES L716); authority leg outside | GREEN headline; effective higher |
| 9 | Thane commercial optionality | formal announcement | 12-month silence = expires | No mention in filing, deck or call; Thane parcel launch Q2 FY28, use class NOT FOUND | AMBER (silent 2 quarters) |
| 10 | Quarterly CFO | positive by Q4 FY27 | -CFO through FY28 | H1 -Rs 147.02 Cr (RES L574) | AMBER (negative, improving) |
| I-1 | Delivery / OC pace | MMR JDA handovers | only Thane delivering | Only Thane OCs (RES L687; PRE-A3-09) | RED |
| I-2 | Collections vs WIP | collections outrun spend; ratio rising | spend outruns collections | Collections Rs 1,233 Cr vs cost of land/dev Rs 1,674.68 Cr (RES L640, L471); collections/pre-sales 77.0% vs 103.0% H1 FY26 [DER]. Deck collections include GST and possession charges (PRE l149, l444); the press-release collections basis is not stated | RED |
| I-3 | Net debt | peaks then declines | > Rs 1,000 Cr Q2 | Rs 916 Cr rising | AMBER |
| I-4 | Launch-to-delivery mix | toward harvesting | early-stage weighted | Newly + pre-launch cohorts 595 of 1,212 outflow (49%) (PRE l393) | RED |
| I-5 | Signing vs delivery pace | signings moderate | signings keep pace | LRP adds Rs 8-10k Cr GDV every year (CC L413) | RED-leaning |
| I-6 | PAT/OCF guidance | management guides | refusal | PAT margin 9-10% guided (RES L724); OCF only as "~10,000 Cr over 4-5 years ... pretty tight" (CC L357-365) | PARTIAL GREEN |
| I-7 | CFO print | turns positive | negative through FY28 | -147.02 H1 | AMBER |

### 6C. Thesis-broken trigger check (scored under each pending reading)
| Condition | Threshold | Current reading | FIRED? |
|---|---|---|---|
| Hard price stop | Rs 520 | CMP Rs 548 (screener 28-Oct, task input) | NO (Rs 28 headroom; name not held) |
| Net debt | > Rs 1,500 Cr | Rs 912-916 Cr (R1-R3); R4 pro forma 1,126 | NO under all four net-debt readings |
| New Singhania governance event | any | None in results, deck, call or CA filing; CA investor independent, not RPT (CA L148-157) | NO |
| 2 consecutive Q EBITDA below threshold | 14% (stop on file) | See matrix below | Basis-dependent |
| Q1 FY27 pre-sales YoY decline | any decline | Q1 Rs 700 Cr vs ~Rs 305 Cr (PRE l336-338 [DER 760-455]) | NO |

**Margin-stop matrix (consolidated; pending ruling 1; evidence only, A4 does not rule)**
| Basis | Q1 FY27 | Q2 FY27 | <14% x2 | <15% x2 | <18% x2 |
|---|---|---|---|---|---|
| A. Reported EBITDA / total income (press-release basis) | 13.11% | 15.21% | NOT FIRED | NOT FIRED | FIRED |
| B. Operating EBITDA (ex-OI) / revenue (protocol anchor basis) | 11.61% | 14.20% | NOT FIRED | **FIRED** | FIRED |
| C. Reported, authority interest treated as project cost (Q1 Rs 19 Cr, Q2 Rs 17 Cr; PRE l365) | 9.56% | 12.97% | **FIRED** | FIRED | FIRED |
| D. Operating, authority-adjusted | 8.01% | 11.93% | FIRED | FIRED | FIRED |
| Standalone, basis A (reference only) | 21.63% | 23.82% | NOT FIRED | NOT FIRED | NOT FIRED |

Evidence for each threshold reading:
- 14%: the Recommendation stop-loss on file (checklist L13). Fires only if authority interest counts as cost (basis C or D).
- 15%: checklist #1 red and risk #4 "Two consecutive Q <15% = margin case broken" (checklist L26, L34). Fires on the protocol's operating basis (B) but not on the press-release basis (A); Q2 basis A clears by 21 bps.
- 18%: the Devil's Advocate reading (NOT L1066). Fires on every basis.
- The observation that separates them: the operator's ruling on threshold AND basis. For the 15% reading, the basis decides the outcome: Q2 basis A is 15.21% and basis B is 14.20%. The press-release basis includes Rs 8.97 Cr of other income; the protocol requires the operating basis as the analytical anchor.
- Consequence under 8A-W if a stop is ruled fired: propose reclassification to AVOID (dropping the ring-fencing WATCHLIST override). Flag only. Decision Status is not changed by A4.

### 6D. Growth trigger status (NOT L369-375)
| Trigger | Original confidence | Confirming | Killing | Updated status |
|---|---|---|---|---|
| 1 Bandra JDA collections maturing FY27-28 | #1 | JDA sales Rs 3,430 Cr, collections Rs 857 Cr to date (RES L699-700; collections include GST and possession charges, PRE l149, l444); Bandra Rs 1,345 Cr revenue recognised (PRE l432) | Bandra at 4th-8th slab (PRE-A3-09); JDAs collected 25% of bookings [DER 857/3,432, GST-inclusive] | ON TRACK (unproven) |
| 2 Kandivali JDA launch FY28 | #2 | Deck: Q2 FY28, economic interest 70.2%, Rs 3,000 Cr (PRE l462) | none | ON TRACK |
| 3 Mahim 1 & 2 launches Q3 FY27 | #3 | Two FY27 launches, GDV Rs 4,100 Cr (RES L702-709); funded via TXRWL AIF (CC L380) | Mahim-1 at Q4 FY27 (PRE l461); no RERA date; Q1 log had Mahim-1 in Q3 (NOT L924) | DELAYED (Mahim-1) |
| 4 Thane commercial optionality | #4 | none | Silent; Thane parcel Q2 FY28 with use class NOT FOUND (PRE l464) | WEAKENED |
| 5 FY27 BD Rs 8,000 Cr new GDV | #5 | ~Rs 8,500 Cr added H1 on gross GDV (CC L72-74); GDV 52,000 (RES L641) | If the addition is Parel at 55% economic interest (R491, R493), RRL's share is about Rs 4,675 Cr [DER; INFERENCE] | FIRED on gross GDV; not fired at economic interest if the H1 addition is Parel (separating observation: Q14) |

---

## STEP 6.5: EXPECTATION LEDGER AND A21 BASE REFRESH
**Deferred to /fttcp and Role 1 (operator ruling OR-30).** Pillar-relevant facts flagged for that work:
- A21 base: H1 FY27 is seasonal (H1 FY26 = 36.0% of FY26 revenue, 25.2% of PAT [DER]). A trailing-4-quarter base is indicated. TTM PAT = 304.59 - 76.68 + 66.49 = Rs 294.40 Cr; TTM EPS Rs 44.22 [DER]. This matches the screener trailing PE of 12.4x at Rs 548 (548/44.22 = 12.4x).
- Expectation rows that this quarter tests: Mahim timing (Mahim-1 slipped a quarter vs the Q1 log); PAT margin 9-10% (new guide, below FY26 10.2% of revenue); FY27 revenue +20% (guide withdrawn); interest Rs 100-120 Cr (trajectory about Rs 181 Cr).

## STEP 7: FOUR-PILLAR DESTINATION PE RE-VALIDATION
**Deferred to /fttcp and Role 1 (OR-30). No Section 1B exit multiple, no valuation.** Pillar-relevant facts:
| Pillar / input | On file | This quarter's fact | Flag |
|---|---|---|---|
| ROCE base | FY26 30.51%, base 24x; FTTCP FIRING (NOT L287) | FY27 ROCE guide ~20% (RES L724); filing gives no ROCE; H1 annualised 12.7% [DER, seasonal]; FY26 same basis 23.4% [DER] | ROCE step-down guided; FTTCP verdict governs |
| Cash multiplier | 0.80x + 0.10 growth offset = 0.90x (NOT L289) | H1 CFO/PAT -2.21x; growth-induced direction; JDA revenue-ahead-of-cash evidence | Band evidence mixed |
| Growth visibility premium | +3x (EM 38, catalysts Q1 FY27 and Mahim Q3) (NOT L293) | Mahim-1 Q4; BKC approval pending; LRP 20% pre-sales CAGR (CC L407, MGMT ASR) | Catalyst proximity slipping one quarter |
| Strategic premium | +0x (NOT L295) | ICICI AIF partnership at project level (CA L42-50) | Single-credit rule: validation is not scarcity |
| UA multiplier | not applicable (NOT L301) | no change | Hold |
| Sector cap | 20x (NOT L299) | no reclassification | Hold |
| Hurdle recheck | HR on EPS CAGR | FY27 PAT run-rate at or below bear; diluted share count 7.369 Cr if warrants convert | Recompute needed |
| Stale Notion fields | net D/E ~0.13x (NOT L999) | filed net D/E 0.565x [DER RES L531, L535, L541] | Correct the page |
| Economic interest | Mahim on file at 100%/82.4% (PRE l460-461) | ICICI holds 60% of project capital per concall (CC L197-198) | Attributable PAT falls once Mahim recognises (NCI) |

---

## STEP 8: POSITION DECISION

Decision Status verified: **WATCHLIST / AVOID, not held. Branch 8A-W.**

8A-W logic applied:
- Thesis-broken condition FIRED? On the reported basis, no. On the operating basis with a 15% threshold, or an authority-adjusted basis with a 14% threshold, yes. Ruling pending. **If the operator rules a fired reading: reclassify to AVOID.** Re-entry would then need two consecutive quarters back above the ruled threshold on the ruled basis.
- Otherwise (no stop ruled fired): actuals land BETWEEN BEAR AND BASE (revenue near base; margin at bear; PAT run-rate at or below bear, 264-309 vs 300). Action: revise projections down; the entry zone likely shifts down. Recompute deferred to Role 1 (OR-30).
- No pre-committed BUY gate is met. The entry gate needs Q1 FY27 margin >=18% and a CFO turn (NOT L363); neither is met. Promoter CONCERN still caps the name.
- CMP Rs 548 (task input) sits Rs 2 below the undiluted band floor and MoS of Rs 550 (NOT L355), inside the post-DA band Rs 500-550 (NOT L1529), and inside the diluted band ~Rs 523-581 (NOT L1525). It is Rs 28 above the Rs 520 hard stop. In band is not buyable under Promoter CONCERN (NOT L1529).
- Proposed Decision Status: unchanged (WATCHLIST / AVOID) unless the margin ruling fires a stop, in which case the proposal is AVOID. **The operator sets it.**

### 8B. Add-back / trigger refinement
- Original entry trigger: enter only at <= Rs 611 AND after Q1 FY27 clears the binary gates (checklist L16). Post-DA: Rs 500-550.
- Proposed refinement (operator decides): any entry also needs (1) Q3 FY27 operating EBITDA margin >= the ruled threshold on the ruled basis, (2) the TXRWL instrument filed as equity with no put or support on RRL, and (3) Q3 net debt under Rs 1,000 Cr on the ruled reading.
- Trim ladder: not applicable (not held).

### 8C. Single cleanest metric for Q3 FY27
**Q3 FY27 consolidated EBITDA margin, reported on both bases (operating ex-OI on revenue, and press-release basis on total income).**
- Bull threshold: >= 18% on the press-release basis (keeps the 17-19% guide arithmetically alive; H2 needs 18.5-19.0% [DER]) and >= 15% on the operating basis.
- Bear threshold: < 15% on the operating basis (a third consecutive sub-15% quarter; the FY27 guide becomes unreachable without an extreme Q4).

▶ Stop: position decision, refinements and cleanest metric presented.

---

## STEP 8.5: QUESTIONS FOR MANAGEMENT (Role 4, merged with Role 5 Step 8F)

Ordered by thesis materiality. Every A3 FORWARD-SIGNAL and AMBIGUOUS finding maps to at least one row (coverage map below).

| # | Cat | Question | Why it matters | Bull answer | Bear answer | Finding IDs |
|---|---|---|---|---|---|---|
| Q1 | A | The deck states JDA revenue recognised to date of Rs 1,930 Cr on p5 (total Rs 9,500 Cr) but the project rows sum to Rs 2,549 Cr (total Rs 10,078 Cr); reconcile the Rs 619 Cr gap. Within it, Invictus BKC shows revenue Rs 577 Cr against bookings of Rs 521 Cr and collections of Rs 64 Cr at shore-piling stage; Sion shows Rs 242 Cr vs Rs 229 Cr; BKC booked Rs 175 Cr in Q2 FY26 before its Q3 FY26 launch. What component of JDA revenue is not unit-sale revenue (landowner-share or barter, sale of rights), in Rs Cr, and what Ind AS 115 method and threshold applies? State collections ex-GST and possession charges. | Revenue quality and EBITDA cash content | The Rs 619 Cr identified, with a stated policy and a filed note | No reconciliation; "accounting standard" answer | PRE-A3-24, PRE-A3-25, PRE-A3-26, PRE-A3-27, PRE-A3-21, RES-A3-05, FND-03 |
| Q2 | F | Give the TXRWL OCPRS terms: conversion date and ratio, any redemption, put or support on RRL (a party to the agreement), coupon, the post-issue shareholding of TXRWL, tranche dates and amounts, the project (Mahim-1, Mahim-2 or both), and whether RRL's 40% (about Rs 140 Cr) is already deployed. | Decides the net-debt reading and the attributable share of Mahim | Equity, no put, no coupon; filed shareholding; RRL share already in | Any put or fixed return; terms withheld | FND-12, FND-13, FND-14, RES-A3-17 |
| Q3 | C | H1 FY27 reported EBITDA margin was 14.3% against a 17-19% FY27 guide. Give the Q3 and Q4 margin path, state whether the guide includes other income, and state whether the Rs 17 Cr quarterly interest to authorities is excluded from EBITDA in the guide. | Margin stop ruling and guide credibility | Q3 >= 18% with named projects crossing thresholds; basis stated | "Normalise progressively" with no path | RES-A3-08, RES-A3-11, RES-A3-15, PRE-A3-05, PRE-A3-11, PRE-A3-35, PRE-A3-28, FND-01, FND-02 |
| Q4 | D | State the net-debt definition. What principal is outstanding to BMC/TMC/MHADA on deferred approvals, which balance-sheet line holds it, and what is the composition of Rs 1,908 Cr of other financial liabilities? What is the blended cost of all borrowings including the authority leg? | Debt-like liabilities outside the Rs 1,220 Cr gross debt | Principal disclosed; OFL is landowner deposits with no cost | Large interest-bearing dues outside debt | RES-A3-16, RES-A3-17, PRE-A3-15, PRE-A3-28, FND-07, FND-08 |
| Q5 | F | Group current borrowings are Rs 452 Cr against a Rs 308 Cr liquidity buffer. What is the refinancing plan for current maturities? Where does the Rs 85.75 Cr of interest paid (RES L586) sit in the deck's cash format, and how does the Rs 155 Cr bank-loan line (R366) reconcile to Rs 200.58 Cr of net borrowing (RES L582-584)? What is FY27 total finance cost in Rs Cr? | Liquidity and interest trajectory | Sanctioned lines named; deck reconciled; FY figure given | "Same run rate" again | RES-A3-03, PRE-A3-16, FND-06, FND-10, FND-21 |
| Q6 | A | The Q1 deck guided revenue growth of 20%; the Q2 deck dropped it and the call said no revenue guide was given. Give the FY27 revenue growth number, and reconcile EBITDA growth of 20% with a 17-19% margin and pre-sales growth of 20%. | Guidance withdrawal; internal consistency | A number near 20% with a bridge | Low-double-digit revenue confirmed | FND-03, FND-23, PRE-A3-06 |
| Q7 | B | Give RERA registration dates for Mahim-2 (Q3 FY27) and Mahim-1 (Q4 FY27). Why did Mahim-1 move from Q3 (Q1 call) to Q4? Is either launch contingent on the ICICI tranche? | Checklist #4; H2 pre-sales | Mahim-2 registered by December; launch not tied to the tranche | No date; launch tied to funding | RES-A3-09, PRE-A3-07, PRE-A3-01, FND-15 |
| Q8 | F | The promoter "has infused approximately 410 crores" (call) while the H1 equity roll shows no warrant money. On what date was the Rs 102 Cr upfront received, is it in Q3 liquidity, and when will the Rs 247 Cr Jekegram object be spent given the Thane parcel launch is Q2 FY28? | Contradiction; warrant objects | Received on a stated date; Jekegram approvals spend dated | Not yet received; objects drift | RES-A3-13, PRE-A3-17, FND-11, PRE-A3-08, RES-A3-19 |
| Q9 | E | When is the BKC aviation height approval expected (date), and what booking value is waiting for upper-floor RERA registration? Explain the Q1 FY27 net cancellation at BKC. | H2 pre-sales contingency | Approval dated within Q3; queue quantified | "Next few weeks" again; no number | FND-16, PRE-A3-03 |
| Q10 | E | Invictus Tower B (Thane) bookings fell 5, 2, 0 over three quarters. Will the unsold inventory be repriced, held or converted to another product? | Thane luxury velocity | Plan with a date | Silence | PRE-A3-02 |
| Q11 | D | Was the 9-10% PAT margin guided before Q2, and on what base (revenue or total income; consolidated or attributable)? Give the basis and first positive year of the Rs 10,000 Cr operating cash flow figure. | I-6 turn; record conflict | Basis and year stated | "Pretty tight" without a year | RES-A3-10, PRE-A3-10, FND-04, FND-05, PRE-A3-13 |
| Q12 | G | All 7 subsidiaries (72.7% of gross assets) sit outside joint review. Which entity booked the Tower B OC revenue, and why did subsidiary revenue rise 63% QoQ while standalone revenue fell 29% YoY? | Review coverage; entity dependence | Entity named; one-off quantified | No split | RES-A3-04, RES-A3-06, RES-A3-05 |
| Q13 | D | Name the counterparty of the Rs 127.60 Cr ICD and explain the Rs 217 Cr fall in standalone other current assets. | Intra-group flows; standalone CFO quality | Counterparty and nature stated | Intra-group release behind standalone CFO | RES-A3-01, RES-A3-20 |
| Q14 | E | What does the Rs 2 lakh group investment fund (new SPV?), when was Chembur Realty renamed Ten X Realty North, and which JDAs make up the GDV rise from Rs 42,000 Cr (FY26) to Rs 52,000 Cr? Give the addition at RRL's economic interest. | Signing pace (I-5); BD trigger at economic interest | Parel only; dates given | New vehicles and signings undisclosed | RES-A3-02, RES-A3-23, PRE-A3-20, FND-17 |
| Q15 | D | What drives the 18.5% ETR against 25.17% statutory, and is it durable? Why do taxes paid exceed current tax in H1? | PAT guide depends on ETR | Durable deduction named | Temporary; step-up ahead | RES-A3-12, PRE-A3-14 |
| Q16 | G | On what basis are the Q2 FY26 and H1 FY26 comparatives and the FY20-FY26 track record prepared (carve-out, audited or not)? | Demerger comparability | Basis stated and audited | Unaudited carve-out | RES-A3-21, PRE-A3-12 |
| Q17 | F | The LRP needs Rs 400-600 Cr more equity. When, in what form, and how does that square with the earlier no-fundraise stance? | Dilution | Project-level partner money, not RRL equity | RRL equity issue inside 2 years | FND-11, FND-10 |
| Q18 | A | Report pre-sales at RRL's economic interest (Wadala 62%, Parel 55%), state whether booking value includes GST, and define "launched units sold". | Headline overstatement | Economic-share series published | Gross-only series continues | PRE-A3-32, PRE-A3-31, PRE-A3-30 |
| Q19 | G | Supply the missing footnote text (12 markers), Park Street collections, and identify pipeline serial no. 4 and launched serial no. 7. | Disclosure hygiene; dropped project | Footnotes filed; Sr. 4 named | A pipeline project removed | PRE-A3-22, PRE-A3-29 |
| Q20 | G | The deck states "Board Independence : 100% i.e. All the Board Committees are chaired by Independent Director" (PRE l218-220), while 5 of 8 directors are independent. Will the headline be restated to the committee claim it actually makes? | Governance claim under CONCERN | Corrected | Repeated | PRE-A3-19 |
| Q21 | A | The release attributes growth "entirely" to Address by GS sales velocity; Address projects gave 53% of Q2 revenue and BKC launched retail units. Quantify revenue by brand. | Attribution accuracy | Brand split filed | Narrative unchanged | PRE-A3-34, RES-A3-05 |
| Q22 | C | What contingency (% of cost) sits in the Mahim budgets, and what margin is underwritten for H2 launches given cost inflation? | Margin path FY28+ | Contingency % and underwriting margin given | Hedge only | FND-20 |
| Q23 | D | Which projects make up the Rs 185 Cr pre-launch outflow (Rs 178 Cr approvals)? | I-4 cohort mix | Named projects with launch dates | Unnamed | PRE-A3-18, RES-A3-18 |
| Q24 | D | Collections were 77% of H1 pre-sales vs 103% a year ago. What collection ratio is targeted for FY27, and on what basis (with or without GST)? | I-2 | Target with a date | None | RES-A3-18, FND-23 |
| Q25 | F | With rates expected to harden, what share of the Rs 1,220 Cr debt is floating, and at what cost does the AIF money sit? | Checklist #8 | Mostly fixed; AIF near zero cost | Floating; AIF expensive | FND-21 |

**Top 3 by likelihood of thesis-changing information:**
- Q1 (JDA revenue: p5 Rs 1,930 Cr vs project rows Rs 2,549 Cr, and BKC/Sion above bookings): a quantified non-sale component would cut the bull case's EBITDA quality; a clean answer lifts it.
- Q2 (OCPRS terms): a put or fixed return confirms the bear net-debt reading (R3/R4).
- Q6 (revenue guide withdrawal): tests transparency; the call already denied the guide existed.

**Channel:** the concall was held 28-Oct-2026 and these were not answered. Send all 25 by **IR email** (Head of IR, CC L319). Re-ask Q1, Q2, Q3 live on the Q3 call.

**Coverage map (A3 FORWARD-SIGNAL + AMBIGUOUS):**
- Results (20): A3-01 Q13; 02 Q14; 03 Q5; 04 Q12; 05 Q1/Q12/Q21; 06 Q12; 08 Q3; 09 Q7; 10 Q11; 11 Q3; 12 Q15; 13 Q8; 15 Q3; 16 Q4; 17 Q2/Q4; 18 Q23/Q24; 19 Q8; 20 Q13; 21 Q16; 23 Q14.
- Presentation (31): A3-01 Q7; 02 Q10; 03 Q9; 05 Q3; 06 Q6; 07 Q7; 08 Q8; 10 Q11; 11 Q3; 12 Q16; 13 Q11; 14 Q15; 15 Q4; 16 Q5; 17 Q8; 18 Q23; 19 Q20; 20 Q14; 21 Q1; 22 Q19; 24 Q1; 25 Q1; 26 Q1; 27 Q1; 28 Q3/Q4; 29 Q19; 30 Q18; 31 Q18; 32 Q18; 34 Q21; 35 Q3.
- Concall (19): FND-01 Q3; 02 Q3; 03 Q1/Q6; 04 Q11; 05 Q11; 06 Q5; 07 Q4; 08 Q4; 10 Q5/Q17; 11 Q8/Q17; 12 Q2; 13 Q2; 14 Q2; 15 Q7; 16 Q9; 17 Q14; 20 Q22; 21 Q5/Q25; 23 Q6/Q24.
- Confirmatory-negative and neutral findings carried to the verdict: FND-09, FND-18, FND-19, FND-22, PRE-A3-09, PRE-A3-33, PRE-A3-04, PRE-A3-23, RES-A3-07, RES-A3-14, RES-A3-22.

### Prior-quarter questions (Q1 FY27 QM-1 to QM-13, NOT L924-936): answer status
| Q1 question | Status | What was said | Verdict |
|---|---|---|---|
| QM-1 Mahim dates | PARTIALLY ANSWERED | "Q3 one project and in Q4 one project" (CC L368); deck swaps order: Mahim-2 Q3, Mahim-1 Q4 (PRE l460-461) | No dates; Mahim-1 one quarter later |
| QM-2 Parel route to market | PARTIALLY (deck only) | Parel launch Q2 FY28 (PRE l463); not on call | |
| QM-3 6 of 8 JDAs by FY27-end; Kandivali | PARTIALLY | 4 launched + 2 Mahim (RES L694, L704); Kandivali Q2 FY28 (PRE l462) | |
| QM-4 Quarterly margin path | NOT ADDRESSED | "normalize progressively" (CC L50-52) | First repeat |
| QM-5 10X Mahalakshmi ownership | PARTIALLY (filing) | Ten X Mahalaxmi Limited is a consolidated subsidiary (RES L450); ownership % not stated; the AIF deal sits in TXRWL (CA L42) | |
| QM-6 ROCE step-down | NOT ADDRESSED | 20% reaffirmed (CC L175) | First repeat |
| QM-7 Exact FY27 interest | PARTIALLY | Quarterly split filed (RES L717-719); FY figure "same run rate" (CC L266-267) | |
| QM-8 D/E reconciliation | ANSWERED (by filing) | Gross 0.752x stated as 0.8x; net 0.565x stated as "closer to 0.5" [DER RES L531-541] | Rounding in two directions |
| QM-9 Runway 6-7 vs 7-8 years | NOT ADDRESSED | none | First repeat |
| QM-10 Governance disclosure steps | PARTIALLY | IR head hired; coverage to 4 firms (CC L316-320) | No governance specifics |
| QM-11 CFO presence | INDETERMINATE | Two people introduced as CFO (CC L31-32); speakers unlabelled (ASR) | Operator to confirm |
| QM-12 Blended cost incl. govt leg | NOT ADDRESSED | Leg disclosed again at Rs 17 Cr (CC L104-109) | First repeat |
| QM-13 Actual Q1 OCF | PARTIALLY (filing) | H1 statutory CFO -147.02 (RES L574); Q1 alone ND | |
Four questions (QM-4, QM-6, QM-9, QM-12) were not addressed for a first repeat. A third consecutive non-answer becomes a Promoter Verdict input (Role 5 rule).

## STEP 9: NOTION UPDATE
Not executed by A4. The orchestrator writes through the run's operator-approval gate. **Decision Status is never written.** Proposed Key Notes prefix: "28-Oct-2026 | Q2 FY27: op EBITDA +15% (+8% authority-adjusted) but PAT -12% on finance cost +70%; net debt Rs 916 Cr; margin stop basis-dependent (ruling pending); revenue guide dropped; deck JDA revenue 1,930 vs 2,549 unreconciled; ICICI terms undisclosed. Status unchanged (operator-only)."

---

# SECTION B: CONCALL ANALYSIS (ROLE 5)

**ASR caveat applies to every figure in this section: MGMT, unverified, ASR.**

## STEP 0: PRE-FLIGHT
- 0A. Notion fetched (Section A, Step 0A). Prior concall log: Q1 FY27 review (NOT L876-969) passed. Two-quarters-ago log (Q4 FY26): not passed; columns marked "ND (prior log not passed)".
- 0B. Participants:
| Role | Name (ASR) | Notes |
|---|---|---|
| Hosting broker / IR | Antique (Akil Rajendani, ASR spelling) (CC L26-29; R265-R267) | Host did not ask questions |
| CMD / Chairman (promoter) | Gautam Hari Singhania: **not on the call** | Yellow flag: promoter absent on a call announcing a promoter preferential issue |
| Managing Director & CEO | Harmohan Sahni ("Harmon Fani") (CC L32) | Fielded the answers that can be attributed |
| CFO | "Rakesh Tewari, CFO" (CC L31); "Anko Jindal, CFO" (CC L32) | Two CFOs introduced (Group CFO and CFO per Notion 22-Oct entry); speakers unlabelled, so CFO participation cannot be confirmed (QM-11) |
| Other | "Salih Baha, Group Head of IR"; Amit Sabharwal, Head of IR (CC L32-33, L319) | New IR head introduced |
- 0C. Structure: call 28-Oct-2026 11:30 IST (concall fulltext header, line 14; CC L19 is the transcript production time), one day after the 27-Oct board (RES L54). Duration ~60 min (3,607 s). Opening 00:00:38-00:18:07 (~17.5 min); Q&A 00:18:15-00:59:23 (~41 min, ~69%). 10 analysts asked questions (R289-R298).
- 0D. Safe harbour: no forward-looking disclaimer in the ASR opening (CC L21-34). Disclaimers sit in the press release (RES L754-761) and deck (PRE l742-744). No new caveats can be compared (no prior disclaimer log).
- 0E. Standard operating business (not lender).

## STEP 1: OPENING REMARKS CLAIMS INVENTORY (CC L35-180)
| # | Claim | Type | Quantified? | Line |
|---|---|---|---|---|
| 1 | Nearly doubled quarterly pre-sales without new launches | Backward | YES | CC L43-45 |
| 2 | Total income +7% YoY to Rs 757 Cr | Backward | YES | CC L46 |
| 3 | EBITDA rose 14%, margin 15% vs 14% (rupee figure garbled) | Backward | YES | CC L47-48 |
| 4 | Margins normalise progressively, this year into next | Forward Soft | NO | CC L50-52 |
| 5 | On track for FY27 EBITDA margin 17-19% | Forward Guidance | YES | CC L53-54 |
| 6 | Non-Thane 57% / Thane 43% of bookings; mix keeps skewing outside Thane | Backward / Strategic | YES | CC L56-59 |
| 7 | Collections +67% to Rs 682 Cr | Backward | YES | CC L60 |
| 8 | H1 collections Rs 1,233 Cr; bookings +111% to Rs 1,602 Cr | Backward | YES | CC L62-63 |
| 9 | OC for Address by GS Season 1 Tower B, 270 units, ahead of RERA | Operational | YES | CC L64-69 |
| 10 | GDV ~Rs 52,000 Cr incl. ~Rs 8,500 Cr added in H1 | Customer/Order | YES | CC L72-74 |
| 11 | Thane: 100 acres, Rs 25,000 Cr potential; 65 acres, 6.7 mn sq ft, Rs 16,500 Cr; sold Rs 9,770 Cr; collected Rs 7,977 Cr | Backward | YES | CC L77-82 |
| 12 | JDAs 52% of GDV, Rs 27,000 Cr; 4 launched; sales Rs 3,432 Cr; collections Rs 857 Cr | Backward | YES | CC L83-90 |
| 13 | Net debt Rs 912 Cr, gross ~Rs 1,200 Cr, D/E 0.8x, net ~0.5 | Backward | YES | CC L98-101 |
| 14 | ~Rs 300 Cr liquidity, cost of debt 9.6%, funded for construction this year | Operational | YES | CC L102-103 |
| 15 | Interest Rs 44 Cr = Rs 27 Cr bank + Rs 17 Cr authorities | Backward | YES | CC L104-109 |
| 16 | New JDA cash-negative 2 years, positive from year 3 | Strategic | YES | CC L117-119 |
| 17 | Steady state (8-10 projects outside Thane) within two years (MD estimate) | Forward Soft | YES | CC L121-126 |
| 18 | Debt stabilises at Rs 1,200-1,400 Cr | Forward Guidance | YES | CC L138-140 |
| 19 | Subsidiary "has raised" Rs 210 Cr from an ICICI-promoted AIF | Customer/Order (capital) | YES | CC L145-146 |
| 20 | Promoter committed ~Rs 400 Cr; first tranche "shortly" | Forward Guidance | YES | CC L148-151 |
| 21 | Rs 210 Cr is ~60% of the project's peak investment | Strategic | YES | CC L152-153 |
| 22 | Two H2 launches, both Mahim, GDV ~Rs 4,100 Cr | Forward Guidance | YES | CC L166-167 |
| 23 | More JDAs in the pipeline to sign | Forward Soft | NO | CC L168-169 |
| 24 | All projects on time or ahead | Operational | NO | CC L170-173 |
| 25 | FY27: pre-sales >=20%, ROCE 20%, EBITDA 17-19%, PAT 9-10% | Forward Guidance | YES | CC L174-177 |
| 26 | "This has been a earlier guidance we are maintaining" | Strategic | NO | CC L178 |

Diagnostics:
- Quantified: 22 of 26 (84.6%) [DER].
- New vs reaffirmed. New: ICICI Rs 210 Cr; promoter Rs ~400 Cr; PAT margin 9-10% (vs Q1 refusal, NOT L905); debt range Rs 1,200-1,400 Cr; steady state within two years. Reaffirmed: pre-sales 20%, EBITDA 17-19%, ROCE 20%, JDA cash-negative two years.
- Quietly dropped: revenue growth >=20% (Q1 HIGH, NOT L902); FY27 interest Rs 100-120 Cr (NOT L908); Parel and Kandivali timing absent from the opening.
- Contradictions: claim 19 "has raised" vs CA L170-172 "no Securities has been issued yet"; claim 26 "earlier guidance" vs Q1 PAT refusal; "profitable growth" (CC L128-129) vs consolidated PAT -11.8% YoY (RES L484).

## STEP 2: FORWARD GUIDANCE EXTRACTION
| Metric | This quarter (Q2 FY27) | Last quarter (Q1 FY27, NOT L897-909) | Two quarters ago | Trajectory | Confidence |
|---|---|---|---|---|---|
| Revenue growth FY27 | "not given"; "similar range"; "not very different from a twenty percent growth" (CC L230, L246, L545-547) | minimum 20% (HIGH) | ND (prior log not passed) | Withdrawn (soft verbal replacement) | LOW |
| Revenue growth FY28 | LRP pre-sales CAGR ~20% for 5 years (CC L407); no revenue figure | ND | ND | New (pre-sales only) | LOW |
| EBITDA margin band | 17-19% FY27 (CC L176; RES L724; PRE l172); EBITDA growth 20% (CC L237) | 17-19% (MEDIUM) | ND | Maintained (EBITDA growth new) | MEDIUM |
| PAT margin | 9-10% (CC L176-177; RES L724) | REFUSED | ND | New | MEDIUM |
| Order book / pipeline | Mahim GDV ~Rs 4,100 Cr; GDV Rs 8-10k Cr added per year (CC L167, L413) | Parel Rs 8,500 Cr; 6 of 8 launched by FY27-end | ND | Maintained | MEDIUM |
| Capex envelope | not applicable (asset-light JDA); equity need Rs 400-600 Cr under LRP (CC L409, L475) | ND | ND | New | LOW |
| Utilisation / launch timeline | Mahim: Q3 one, Q4 one (CC L368); BKC aviation approval "next few weeks" (CC L518) | Mahim-1 Q3 (Nov-Dec), Mahim-2 Q4 (NOT L924) | ND | Maintained in aggregate; order swapped in deck | MEDIUM |
| Working capital / CCC | JDA cash-negative 2 years then positive (CC L117-119); ~Rs 10,000 Cr OCF over 4-5 years (CC L362) | OCF REFUSED | ND | New (partial) | LOW ("pretty tight", CC L365) |
| Net debt trajectory | Gross debt stays ~Rs 1,200(-1,400) Cr; will not come down for 1-2 years (CC L140, L471-472) | no moderation 1-2 years | ND | Maintained | HIGH (adverse) |
| Interest cost | H2 at H1 run rate (CC L266-267) | Rs 100-120 Cr (LOW) | ND | Withdrawn / widened | LOW |
| ROCE | ~20% (CC L175; RES L724) | 20% or upward | ND | Maintained | MEDIUM |
| Dividend / payout | none stated | none | ND | n/a | n/a |
| Pre-sales growth FY27 | >=20% (CC L175, L238; RES L723) | >=20% | ND | Maintained (not raised after H1 +111%) | HIGH |

Diagnostics:
- Widened or tightened: revenue and interest guides were withdrawn or widened; margin and pre-sales maintained; PAT added. Net: guidance became less specific on the two items the P&L tests (revenue, interest).
- Dropped without acknowledgment: revenue guide removed from the deck; on challenge management said "This year we have not given a guidance on revenue growth" (CC L230), contradicting the Aug-19 deck (CC L242-244) and the Q1 log. **Major credibility flag.**
- Internal consistency: EBITDA +20% on FY26 Rs 495.46 Cr gives ~Rs 594.6 Cr [DER]. At 17-19% margin that implies FY27 total income of Rs 3,129-3,497 Cr, i.e. +3% to +15% growth. Revenue growth of 20% with EBITDA +20% implies a margin of 16.3%, below the band. The three statements cannot all hold [DER]. The analyst's back-calculation of high-single or low-double-digit revenue growth (CC L541-543) was not disputed.
- vs Four-Pillar projections: the pre-sales guide implies H2 pre-sales of ~Rs 2,026 Cr vs Rs 2,263 Cr in H2 FY26, about -10.5% (PRE-A3-06; NOT L1052). PAT 9-10% on ~Rs 3,589 Cr gives Rs 323-359 Cr, the lower half of the Notion base (NOT L991).
- Refused: exact FY27 interest cost; Mahim inventory release (CC L382); project-wise unsold break-up "communicate separately" (CC L346); annual OCF.

## STEP 3: PROMISE vs DELIVERY AUDIT

### 3A. Q1 FY27 commitments
| Commitment (Q1 FY27 concall, NOT L897-936) | This quarter's actual | Status | Points |
|---|---|---|---|
| Pre-sales growth >=20% FY27 | H1 +111% (RES L634-636) | UNCLEAR (FY not closed) | excl. |
| Revenue growth >=20% FY27 | Guide removed from deck; denied on call (CC L230) | DROPPED (+ governance flag) | 0 |
| EBITDA margin 17-19% FY27 | H1 14.34% (RES L479 [DER]) | UNCLEAR | excl. |
| ROCE >=20% FY27 | not disclosed | UNCLEAR | excl. |
| Net debt no moderation 1-2 years | Net debt 658 to 916 (RES L535-541 [DER]) | DELIVERED (accurate adverse guide) | 1.0 |
| FY27 interest ~Rs 100-120 Cr | H1 already Rs 90.70 Cr (RES L475); H2 "same run rate" | MISSED (trajectory; FY not closed) | 0 |
| Mahim-1 Q3, Mahim-2 Q4 | Q3 one, Q4 one (CC L368); deck Mahim-2 Q3, Mahim-1 Q4 | UNCLEAR (not due) | excl. |
| 6 of 8 JDAs launched by FY27-end | 4 + 2 Mahim planned | UNCLEAR | excl. |
| FY27 BD >= Rs 8,000 Cr new GDV | ~Rs 8,500 Cr added H1 on gross GDV (CC L72-74); about Rs 4,675 Cr at economic interest if Parel (Section A 6D) | DELIVERED (scored on the gross basis the commitment used) | 1.0 |
| Separate disclosure of interest detail | Bank vs authority split filed (RES L717-719); FY figure not given | PARTIALLY DELIVERED | 0.5 |

### 3B. Cumulative record (trailing window available: 1 scored concall)
| Concall | Total | Delivered | Partially | Missed | Delayed | Dropped | Unclear | Points |
|---|---|---|---|---|---|---|---|---|
| Q1 FY27 (11-Aug-2026), scored at Q2 | 10 | 2 | 1 | 1 | 0 | 1 | 5 | 2.5 |
| Q4 FY26 and earlier | ND (prior log not passed) | | | | | | | |

**Credibility ratio = 2.5 / (10 - 5) = 50%** → Grade **C (Mixed)**, provisional on one of four quarters.
- Sensitivity: if the interest item is scored UNCLEAR (FY not closed), the ratio is 2.5/4 = 62.5% (B). If the revenue item is scored DELAYED (0.25) not DROPPED, it is 2.75/5 = 55% (C). The grade turns on one scoring call; the separating observation is the FY27 finance cost at Q4 and whether the Rs 100-120 Cr guide was bank-only (bank interest H1 Rs 55 Cr, PRE l364).
- DROPPED count: 1 in the window. The automatic downgrade needs 2.

### 3C. Pattern recognition
- Management meets operating guides (bookings, BD signings) and misses or withdraws financial guides (revenue, interest). Pattern on one quarter only.
- Capital stance reversed: the analyst recalls a no-fundraise stance "two or three concall" ago (CC L205-207), uncontested; now promoter warrants, AIF money and Rs 400-600 Cr more equity.

### 3D. Management grade
On file: Sahni Grade A (NOT L367). This run: provisional C (Mixed). Protocol forbids grading on one quarter alone; **flag the gap, no Notion change proposed until a second scored quarter.**

### 3E. Prior questions answered
See Step 8.5 table "Prior-quarter questions": 1 answered (by filing), 7 partially, 4 not addressed, 1 indeterminate.

## STEP 4: Q&A DECOMPOSITION

### 4A. Inventory
| # | Analyst (ASR) | Question | Category | Response grade | Substance |
|---|---|---|---|---|---|
| 1a | Ritul Shah, Anubhoti Advisors | ICICI stake for Rs 210 Cr | Financial | B | OCPRS; 60/40 capital; 5% fee on turnover (CC L194-201) |
| 1b | same | Why a promoter preferential when no fundraise was planned | Governance | C | "capital is needed"; market concern on debt; equity is the other option (CC L208-214) |
| 2 | Avantika Jhaver, Mani Tree LLP | Revenue guidance of 20% missing from slides | Forward Guidance | D | Denied a revenue guide was given; "similar range" (CC L230-247) |
| 3 | "Mr. Zabs", auto research | Interest Rs 91 Cr in H1 vs Rs 100-120 Cr guide | Financial | C | "same run rate"; no number (CC L266-267) |
| 4a | Rishabh Kothari | Rate rise impact on demand | Macro | B | Portfolio Rs 1.5 Cr+ ticket; rates must harden (CC L273-292) |
| 4b | same | Valuation 50% below listing | Governance | B | IR strategy; coverage to 4 firms (CC L302-328) |
| 5a | "Tenantche" Mishra | Unsold Rs 14,800 Cr: launched vs unlaunched | Clarification | D | "We will communicate separately" (CC L346) |
| 5b | same | Net OCF over 4-5 years | Forward Guidance | B | ~Rs 10,000 Cr; "pretty tight" (CC L357-365) |
| 5c | same | Mahim phasing | Forward Guidance | A | Q3 one, Q4 one (CC L368) |
| 6a | Heta Lhuna | ICICI timing | Financial | A | 30 days; full by March (CC L376-377) |
| 6b | same | Mahim inventory at launch | Forward Guidance | D | "We haven't taken that call yet" (CC L382) |
| 6c | same | H2 sustenance | Forward Guidance | B | Better than H1 (festive) (CC L385-387) |
| 6d | same | IRR accretive; more such deals | Strategic | B | Yes; for the right project (CC L389-391) |
| 7a | Janam Shah | 5-year pre-sales CAGR; capital | Forward Guidance | A | ~20% CAGR; Rs 400-600 Cr equity; Rs 8-10k Cr GDV per year (CC L407-413) |
| 7b | same | Land strategy | Strategic | B | JDAs; no land banking (CC L422-425) |
| 7c | same | Market share; Thane | Strategic | A | Thane stabilises at Rs 1,500-1,600 Cr (CC L439) |
| 8a | Bhavat Modi | Is Rs 1,200 Cr peak debt? | Financial | A | Will not come down for 1-2 years (CC L471-472) |
| 8b | same | RRL's Rs 140 Cr; OCPRS as debt | Financial | C | 140 unanswered; "it will not reflect as debt" (CC L486-490) |
| 8c | same | H2 pre-sales arithmetic | Forward Guidance | B | Existing stock "much more" than Rs 1,000 Cr (CC L497-498) |
| 8d | same | Mahim product | Customer/Order | A | One Invictus, one Address (CC L503) |
| 8e | same | Luxury flatness; Invictus Thane zero sales | Strategic | C | "Thane is a lab"; BKC approval (CC L510-524) |
| 9 | Deepak Poda, fire capital | Revenue growth back-calc | Forward Guidance | C | Joke; "in that range" (CC L543-547) |
| 10a | Ihas Paramesh | OCPRS dividend | Financial | B | "virtually zero" (CC L584-587) |
| 10b | same | Construction cost inflation | Operational | B | Fixed-price on ongoing; part pass-through on new (CC L590-608) |

### 4B. Pattern analysis
- Most repeated: revenue/20% growth (Q2, Q7, Q8, Q9; four analysts) and debt/interest (Q1b, Q3, Q8). Repetition signals the market does not trust the first answer (A2 REPEAT_QUESTION flags R310, R311, R315-R317).
- Consistently graded C-E: revenue guidance (D, C), interest cost (C), the RRL Rs 140 Cr share and OCPRS classification (C), unsold break-up and Mahim inventory (D). These are the topics management does not want to quantify.
- Buy-side vs sell-side: names are ASR-garbled; firms read as advisory and PMS houses (Anubhoti Advisors, Mani Tree LLP, Clattarian Management). Split ND. No identifiable large sell-side.
- Host broker: Antique did not open with a question. No house-broker softball.
- Pushback: Avantika Jhaver cited the Aug-19 deck slide 9 (CC L242-244) after management said no revenue guide existed. The topic is contested.

### 4C. Three most important exchanges

**Exchange 1: revenue guidance (Q2, CC L227-247; Q9, CC L535-547).**
- Question: "there hasn't been a guidance on revenue mentioned of 20% unlike last time where the revenue guidance was also pulled out of 20%" (CC L227-229).
- Response: "This year we have not given a guidance on revenue growth ... we follow percentage completion there are many moving parts" (CC L230-234); later "you've got the same calculator as me my friend" (CC L543).
- Said: no number; "similar range".
- Not said: why a guide on file was removed; the revenue number for FY27.
- Thesis implication: FY27 revenue of ~Rs 3,600 Cr (Notion base) loses its anchor; Reading B (Rs 3,260-3,543 Cr) gains weight.
- Follow-up we would ask: Q6.

**Exchange 2: ICICI money and debt classification (Q1, CC L192-202; Q8, CC L478-490).**
- Question: "our 140 crore have you already infused ... if the instrument is OCPRS ... some portion which will come in as a debt" (CC L480-485).
- Response: "No, it will not reflect as debt ... this is equity that we have got from ICICI and only for ease of movement of cash flow they have structured it as OCPRX" (CC L486-490).
- Said: equity treatment; 60/40 capital; 5% fee.
- Not said: the Rs 140 Cr status; conversion, redemption or put terms; the TXRWL shareholding.
- Implication: the net-debt ruling cannot be scored from the call; the filing is silent too (CA R063).
- Follow-up: Q2.

**Exchange 3: debt trajectory (Q8, CC L457-478).**
- Question: is Rs 1,200 Cr peak debt, and is promoter money for debt repayment?
- Response: "we are at 1200, it will not come down at least for the next one or two years for sure ... our requirement as per the LRP is in the range of maybe 4 to 600 crores" (CC L471-475).
- Said: debt flat-to-up into FY28-FY29; more equity.
- Not said: whether promoter money repays debt; the net-debt path after inflows.
- Implication: I-3 stays red-leaning; net debt falls in Q3 only for financing reasons (FND-10).
- Follow-up: Q5, Q17.

## STEP 5: NEW INFORMATION AUDIT

### 5A. New disclosures
| Disclosure | Type | Material? | Thesis impact |
|---|---|---|---|
| ICICI Pru AIF Rs 210 Cr into TXRWL (OCPRS; 60/40; 5% fee) (CC L145-201; CA L42-50) | New partnership | YES | First project-level partner; net-debt reading; NCI on Mahim |
| PAT margin 9-10% guide (CC L176-177) | Forward guidance | YES | I-6 partial turn |
| Revenue guide withdrawn (CC L230) | Negative surprise | YES | Credibility; revenue base |
| LRP: 20% pre-sales CAGR 5 years; Rs 8-10k Cr GDV per year; Rs 400-600 Cr equity (CC L407-413) | Forward catalyst / capital | YES | I-5 red case; dilution |
| Thane stabilises at Rs 1,500-1,600 Cr per year (CC L439-440) | Negative surprise | YES | Cash engine ex-growth (FND-19) |
| ~Rs 10,000 Cr OCF over 4-5 years (CC L357-362) | Forward catalyst | YES | First OCF figure; basis unclear |
| BKC aviation approval pending (CC L517-524) | Regulatory | YES | H2 Invictus BKC pre-sales |
| Steady state within two years (CC L124-126) | Forward catalyst | MEDIUM | Inflection timing ~FY29 |
| New Head of IR Amit Sabharwal (CC L319) | New senior management | NO | IR outreach |
| Fixed-price EPC contracts on ongoing projects (CC L590-592) | Operational | MEDIUM | Margin protection limited to ongoing projects |

### 5B. What was NOT discussed
| Expected topic | Why | Significance |
|---|---|---|
| Consolidated PAT -11.8% YoY, -13.3% H1 (RES L484) | Headline earnings fell | AMBER: highlights and call led with EBITDA (PRE-A3-33) |
| H1 statutory CFO -Rs 147 Cr | Notion monitor #10; QM-13 | AMBER (sent to deck slide 23, CC L110-112), 2nd quarter silent |
| Related-party loans to subsidiaries (Rs 1,191.64 Cr) | Monitor #6 | AMBER, 2nd quarter silent |
| Promoter governance | Monitor #7 | Neutral by checklist definition; promoter absent from call |
| Thane commercial optionality | Monitor #9 | AMBER, 2nd quarter silent; 12-month expiry window advancing |
| Warrant money receipt status | Tracker row; contradicts "has infused" | AMBER |
| Thane Jekegram launch vs warrant objects | Tracker row | AMBER (deck: Q2 FY28) |
| Parel route to market | QM-2 | AMBER (not named on call) |
| Revenue recognition at BKC/Sion above bookings; deck p5 vs p26 JDA revenue | Deck data | RED-candidate: undisclosed driver of reported revenue |
| Other financial liabilities Rs 1,908 Cr | Debt-like leg | AMBER |
| Margin basis (with or without other income) | Margin stop ruling | AMBER (only the analyst's "16 and a half percent including your other income", CC L539) |
| No peer development discussed | Peer cross-check | Neutral (no peer concalls passed) |

## STEP 6: TONE AND SPECIFICITY

### 6A. Tone vs Q1 FY27 (NOT L897-965)
| Topic | Q1 phrase | Q2 phrase | Direction |
|---|---|---|---|
| Revenue growth | "minimum 20%" | "we have not given a guidance on revenue" (CC L230) | DROPPED |
| PAT guidance | "not a policy of giving that out" | "pet margin will be 9 to 10 percent ... earlier guidance" (CC L176-178) | UPGRADED (record conflict) |
| Net debt | "no moderation ~1-2 years" | "will not come down at least for the next one or two years for sure" (CC L471-472) | MAINTAINED |
| Interest cost | "~Rs 100-120 cr ... don't hold me to it" | "same run rate" (CC L266-267) | DOWNGRADED |
| Capital raising | no-fundraise stance (CC L205-207, analyst recall) | "May be in the range of 5-600 crores of equity" (CC L409) | DOWNGRADED |
| MMR demand | "quite strong" | "no major impact ... unless interest rates really run away"; rates "have to harden" (CC L287-291) | DOWNGRADED (hedged) |
| Margin normalisation | 17-19% back-ended | "normalize progressively ... into next year also" (CC L50-52) | DOWNGRADED (window widened) |
| Thane | cash engine | "I do not see any significant growth coming beyond this number from Tana" (CC L439-440) | DOWNGRADED |
| Mahim timing | Mahim-1 Q3, Mahim-2 Q4 | "Q3 one project and in Q4 one project" (CC L368) | MAINTAINED (less precise) |

### 6B. Specificity score (59 forward rows R206-R264)
Quantified 30, unquantified 29 [A4 count on A1 rows]. **Specificity ratio 0.51** (just above the 0.5 line).

### 6C. Defensive language count
"We will communicate separately" (CC L346); "we have not given a guidance" (CC L230); "I don't have an exact number" (CC L547); "We haven't taken that call yet" (CC L382); "my estimate is" (CC L124); "my belief is" (CC L287); "I guess" (CC L290, L326); "I think" (CC L292, L477, L608); "expected" (CC L50, L376, L518); "maybe/may be" (CC L409, L475). **Total 16. Hedge-heavy (>5).** Prior-call count ND (Q1 log notes "hedged ~5x" on interest alone, NOT L908).

### 6D. Confidence indicators
Named counterparty and amount (ICICI Rs 210 Cr); dated tranche (30 days; March); OC 18 months early (RES L732); specific LRP numbers. Against: promoter absent; finance-officer attribution unconfirmable.

### 6E. Archetype (provisional)
Specificity 0.51 (>0.5) x credibility 50% (<60%) = **OVERPROMISER (provisional, borderline on both axes)**. One scoring call flips it: credibility 62.5% gives COMMITTED & CREDIBLE. Treatment while provisional: anchor to filing numbers; require pre-committed thresholds for any position action. Archetype shift vs workup (Grade A, NOT L367) flagged.

## STEP 7: CROSS-REFERENCE

### 7A. Concall narrative vs filing
| Concall claim | Filing evidence | Reconciliation |
|---|---|---|
| EBITDA +14%, Rs 115 Cr, margin 15% (CC L47-48) | 115.24 / 757.49 = 15.21%; Q2 FY26 101.06 (RES L475-479 [DER]) | CONFIRMED (includes other income) |
| Net debt 912; gross ~1,200; D/E 0.8x; net ~0.5 (CC L98-100) | Net 916.15; gross 1,219.73; gross D/E 0.752; net D/E 0.565 [DER RES L519-541] | PARTIALLY CONFIRMED (rounded up and down in opposite directions) |
| Liquidity ~Rs 300 Cr (CC L102) | 303.58 computed; PR 308 (RES L715) | CONFIRMED |
| Interest Rs 44 Cr = 27 + 17 (CC L104-105) | Finance costs 43.53 (RES L475); PR split (RES L717-719) | CONFIRMED |
| "a promoter has infused equity of approximately 410 crores" (CC L208) | Equity roll has no warrant money; no financing inflow (RES L494, L530, L582-587) | CONTRADICTED (committed, not received in H1) |
| Subsidiary "has raised 210 crores" (CC L145-146) | "only a signing ... no Securities has been issued yet" (CA L170-172) | CONTRADICTED (committed, not received) |
| Collections +67% to Rs 682 Cr (CC L60) | PR/deck only (RES L638; PRE l315); other current liabilities +479.59 H1 (RES L546) | UNVERIFIABLE vs statements; directionally consistent |
| "Tana is already net cash positive" (CC L123) | No entity or project statutory split; deck mature cohort +364 (PRE l398) | UNVERIFIABLE |
| "we have done this growth profitably" (CC L128-129) | Consolidated PAT -11.8% Q2, -13.3% H1 (RES L484) | PARTIALLY CONFIRMED (profitable, not growing) |
| Margin up on "optimized product mix" (CC L46-47) | Operating margin +94 bps YoY, +10 bps authority-adjusted (RES [DER]; PRE l365); JDA revenue above bookings at BKC/Sion (PRE-A3-24/26) | PARTIALLY CONFIRMED |
| Net D/E "closer to 0.5" | 0.565 | PARTIALLY CONFIRMED |

### 7B. Peer concall cross-check
**UNVERIFIABLE this run** (peer concalls not passed). Notion peer context (Sunteck D/E 0.21x, cleaner governance) is prior work, not a same-window concall (NOT L965).

### 7C. External channel checks
| Claim | Source | External says | Alignment |
|---|---|---|---|
| Balance sheet comfort | CARE (via company PR, RES L720-722) | A+ Stable reaffirmed | Aligned (company-reported; agency text not passed) |
| Demand holds at higher rates | none passed | ND | UNVERIFIABLE |

## STEP 8: THESIS AND POSITION (concall view)

### 8A. Growth triggers post-concall
| Trigger | Pre-concall | Concall evidence | Post-concall |
|---|---|---|---|
| Bandra JDA collections | ON TRACK (unproven) | JDA cash-negative 2 years from late-Q4 FY26 launches (CC L117-119, L136) | ON TRACK (later: FY28+) |
| Kandivali FY28 | ON TRACK | not named on call | ON TRACK (deck) |
| Mahim Q3 FY27 | DELAYED (Mahim-1) | "Q3 one, Q4 one"; funded by ICICI tranche (CC L368, L380) | DELAYED (Mahim-1) |
| Thane commercial | WEAKENED | silence; Thane ex-growth (CC L439) | WEAKENED |
| BD Rs 8,000 Cr | FIRED (gross GDV) | H1 ~Rs 8,500 Cr gross (CC L72-74); ~Rs 4,675 Cr at economic interest if Parel | FIRED on gross GDV; not fired at economic interest if Parel |
| NEW: project-level PE partners | n/a | ICICI deal; "will continue" (CC L217-218, L389-391) | NEW |

### 8B. Watchlist items (concall-specific)
| # | Item | Concall reading | Status |
|---|---|---|---|
| 1 | EBITDA margin | "margins now at 15%" (CC L48) | AMBER/RED by basis (Section A 6C) |
| 4 | Mahim | Q3 and Q4, no dates (CC L368) | AMBER |
| 5 | JDA signings | ~Rs 8,500 Cr H1 gross (CC L73) | GREEN gross; AMBER at economic interest |
| 8 | Cost of debt | 9.6% (CC L102); authority leg outside | GREEN headline |
| 9 | Thane commercial | silent | AMBER |
| 10 | CFO | sent to slide 23 (CC L110-112) | AMBER |

### 8C. Thesis-broken triggers (concall-relevant)
| Condition | Threshold | Concall evidence | FIRED? |
|---|---|---|---|
| Net debt | > Rs 1,500 Cr | "1200, 1400 crore level" gross; within 1:1 (CC L140, L476-478) | NO |
| Governance event | any | none raised | NO |
| Margin 2Q below stop | 14% | "15%" (CC L48), rupee figure garbled | Score on filing only (Section A 6C) |
| Q1 pre-sales YoY | decline | H1 +111% (CC L63) | NO |

### 8D. Four-pillar inputs (concall)
**Deferred to /fttcp and Role 1 (OR-30).** Pillar-relevant concall facts flagged:
| Pillar | Concall evidence | Flag |
|---|---|---|
| Pillar 1 ROCE | ROCE ~20% FY27 (CC L175); projects IRR 20-25% vs debt under 10% (CC L468-469) | FTTCP ROCE verdict governs |
| Pillar 2 cash | JDA cash-negative 2 years; steady state within 2 years (CC L117-126); ~Rs 10,000 Cr OCF over 4-5 years "pretty tight" (CC L357-365) | Growth-induced framing, management tier |
| Pillar 3 / GVP | LRP 20% pre-sales CAGR; Rs 8-10k Cr GDV per year (CC L407, L413) | I-5 red case resets the cash clock |
| Strategic premium | ICICI partnership; 5% fee "margin profile improves" (CC L220-221) | Fee eliminates on consolidation (FND-12); single-credit rule |

### 8E. Position decision (concall overrides)
- Credibility ratio below 60% (50%, provisional): discount management commentary 30-50%; tighten add-back triggers (Section A 8B); Promoter Verdict downgrade not proposed on one quarter.
- Two DROPPEDs: no (one).
- Undisclosed material risk: revenue recognition at BKC/Sion and the deck's own p5 vs p26 JDA revenue gap (Rs 619 Cr) are surfaced by the deck, not explained on the call. Name not held, so the trim rule does not apply.
- Undisclosed material positive: ICICI partnership. Hold pending terms. RRL is itself a party to the agreement (CA L121-123). Price / TXRWL PAT is not computable (earnings NOT DISCLOSED; pre-launch). ICICI's 60% residual-profit share at a near-zero coupon prices the money at the project equity return management cites (IRR 20-25%, CC L468-469), against 9.6% debt (RES L716). Positive for net debt if classified as equity; not cheaper capital.
- Narrative contradicts filing: "has infused" and "has raised" vs filed records. **Trust the filing.** Logged as a credibility issue.
- Position: unchanged posture under 8A-W (Section A Step 8).

### 8F. Updated questions (forward)
Merged into Section A Step 8.5 (Q1-Q25). What to watch in the Q3 call: Q2 (OCPRS terms), Q3 (margin path), Q6 (revenue number), Q7 (Mahim RERA dates), Q9 (BKC approval date).

**Concall verdict:**
- Management credibility (this quarter): C (provisional).
- Trailing credibility ratio: 50% (2.5 / 5), one scored concall of four.
- Archetype: OVERPROMISER (provisional, borderline).
- Role 1 track-record input: Mixed (provisional; window 1 of 4).
- Net concall impact on thesis: WEAKENED (capital and guidance), with one funding positive (leverage only, not cost of capital).
- Position: entry-zone review deferred to Role 1; Decision Status unchanged (operator-only).

---

# SECTION C: COMBINED VERDICT

| Signal | Filing-derived | Concall/deck-derived | Reconciliation |
|---|---|---|---|
| Demand | n/a in statements | Pre-sales Q2 Rs 902 Cr +98%; collections +67% (PR/deck) | Strong on gross bookings (management-compiled). Qualified: at RRL's economic interest Q2 pre-sales rose about 81% (about Rs 794 Cr vs Rs 438 Cr; Bandra 91%, Wadala 62%, R441, R467, R758-R829) [DER]; the unchanged >=20% guide implies H2 pre-sales about Rs 2,026 Cr vs Rs 2,263 Cr, about -10.5%; H1 BD ~Rs 8,500 Cr gross is about Rs 4,675 Cr at economic interest if it is Parel [INFERENCE] |
| Operations | Op EBITDA +15.0% YoY; op margin 14.20% (+94 bps) | "optimized product mix" | Partly confirmed. Authority-adjusted: +8.3%, +10 bps (Step 2). JDA revenue quality open (deck p5 vs p26 gap Rs 619 Cr) |
| Earnings | PAT -11.8% Q2, -13.3% H1; finance cost +70% | not discussed | Filing wins: earnings fell |
| Cash | H1 CFO -147.02 (improved from -319.08) | NOCF -205 (deck format) | Statutory governs; still negative |
| Leverage | Net debt 916; gross D/E 0.752 | "won't come down 1-2 years"; more equity | Risk #2 first signals lit |
| Capital | No warrant or AIF money in H1 | "has infused", "has raised"; ICICI 60/40 at "virtually zero" coupon | Concall overstates; filing wins. RRL is a party to the ICICI agreement; the money is equity-priced (project IRR 20-25% vs 9.6% debt): positive for net debt if equity, not cheaper capital |
| Guidance | PR: pre-sales 20%, ROCE 20%, EBITDA 17-19%, PAT 9-10% | Revenue guide withdrawn; interest guide widened | Credibility flag |

**Protocol verdict: PROCEED WITH FLAGS.** Cash conversion INDETERMINATE-WITH-DIRECTION (growth-induced direction, improving YoY); missing evidence named in Step 5. Net thesis impact: WEAKENED on earnings, leverage and guidance; demand leg confirmed on gross bookings, qualified at economic interest (about +81% in Q2) and by a guide that implies H2 pre-sales about 10.5% lower than H2 FY26. Watchpoints for Q3: margin on both bases; net debt on each ruled reading; OCPRS terms; Mahim-2 RERA; BKC approval.

## MONITORABLES / CATALYST LIST (from A3 commitment registers and board-outcome forward items)
| # | Item | Implied date | Source |
|---|---|---|---|
| M1 | ICICI AIF first tranche into TXRWL | by ~27-Nov-2026 ("next 30 days" from 28-Oct) | CC L376 (C-12) |
| M2 | Securities-issue intimation (instrument terms) | on issue, ~Nov-2026 | CA L174-180 (R047) |
| M3 | Warrant allotment and Rs 102 Cr upfront | Q3 FY27 (~Nov-2026) | NOT L8 (24-Oct entry); CC L149-150 |
| M4 | BKC aviation approval, then RERA for upper floors | ~Nov-Dec 2026 ("next few weeks") | CC L517-522 (C-16) |
| M5 | Mahim-2 launch and RERA registration | Q3 FY27, by 31-Dec-2026 | PRE l460; CC L368 |
| M6 | Q3 FY27 results: margin (both bases), net debt (each reading), NCI line | by 14-Feb-2027 | Reg 33 cadence; Section A 8C |
| M7 | Mahim-1 launch | Q4 FY27, by 31-Mar-2027 | PRE l461 |
| M8 | ICICI full sum received | by 31-Mar-2027 | CC L377 |
| M9 | Research coverage to at least 4 firms | by end of "this year" (Dec-2026 or Mar-2027) | CC L316-317 (C-23) |
| M10 | FY27 guidance test: pre-sales +20%, ROCE 20%, EBITDA 17-19%, PAT 9-10% | 31-Mar-2027 (Q4 results ~May-2027) | RES L723-724 |
| M11 | Kandivali, Parel, Thane owned-parcel launches | Q2 FY28 (Jul-Sep 2027) | PRE l462-464 |
| M12 | "Fully funded for the next year of construction" (Rs 308 Cr buffer) | through ~Sep-2027 | RES L715 |
| M13 | Gross debt holds Rs 1,200-1,400 Cr; no fall for 1-2 years | FY28-FY29 | CC L140, L471-472 |
| M14 | Warrant balance Rs ~307 Cr (18-month window) | by ~Apr-2028 | NOT L8 (12-Sep entry) |
| M15 | Steady state 8-10 projects outside Thane | ~FY29 (MD estimate) | CC L121-126 |
| M16 | LRP equity Rs 400-600 Cr decision | FY28-FY32 | CC L409-410, L475 |
| M17 | Project-wise launch break-up sent to analyst | unspecified | CC L346 |
| M18 | Margin stop ruling and net-debt ruling (operator) | before Q3 print | checklist L60-64 |

---

## FORWARD ESTIMATE INPUTS (for the operator brief; indicative, not Role 1)

Basis rules: consolidated, Rs Cr. No Section 1B multiple, no fair value. Each figure carries its basis and tier. Share counts: basic 6,65,73,731 (RES L194); fully diluted 7,36,92,319 if warrants and ESOPs convert (NOT L8). CMP Rs 548 (screener.in 28-Oct 08:48 IST; market cap Rs 3,644 Cr; trailing PE 12.4; book Rs 244; ROCE 29.6%; 52-week Rs 742 / 349; task input). Check: TTM EPS Rs 44.22 [DER] gives 12.4x; book Rs 1,622.18 Cr / 6.6574 Cr = Rs 243.7 [DER]. The inputs tie.

| Item | Reading A | Basis A | Tier A | Reading B | Basis B | Tier B | Separating observation |
|---|---|---|---|---|---|---|---|
| FY27E revenue | 3,589-3,600 | FY26 2,990.79 x 1.20; Notion base ~3,600 (NOT L982); verbal "not very different from a twenty percent growth" (CC L545-547) | MGMT (ASR) + Notion model | 3,260-3,543 | H1 seasonality 1,275.19 / 0.3599 = 3,543; analyst back-calc 9-12% uncontested (CC L541-543) | DERIVED from FILED; MGMT (ASR) | Q3 FY27 revenue: Reading A needs H2 Rs 2,314 Cr vs H2 FY26 Rs 1,914 Cr (+20.9%) [DER] |
| FY27E PAT | 323-370 | PAT margin 9-10% on ~3,589 (RES L724); Notion base 340-370 (NOT L991) | MGMT (FILED PR guide) + Notion model | 264-309 | Low end: H1 seasonality 66.49 / 0.2517 = 264. Bridge: H1 PAT 66.49 + H2 revenue (Reading B less H1: 1,984.81-2,267.81) x H2 FY26 PAT margin on revenue 11.9% (227.91 / 1,914.29) less ~Rs 27.1 Cr extra after-tax interest (H2 finance at the H1 run rate 90.70 vs 57.50, taxed at 18.4%) = 276-309 [DER] | DERIVED from FILED | Q3 FY27 reported EBITDA margin: >= 18% supports A; <= 15% supports B |
| FY28E revenue | 4,150-4,300 | Notion addendum (NOT L983) | Notion model (INFERENCE) | 3,651-3,968 | Reading B FY27 x 1.12 (Notion bear CAGR) | INFERENCE on DERIVED base | Mahim-2/Mahim-1 RERA in FY27 and Kandivali/Parel/Thane launches holding Q2 FY28 (PRE l460-464) |
| FY28E PAT | 410-430 | Notion base (NOT L992) | Notion model | 280 | Notion bear "declining" (NOT L992) | Notion model | FY28 H1 margin >= 17% with finance cost flat at ~Rs 181 Cr run-rate; NCI share of TXRWL profit (CC L197-201) |

Reading B for FY27 PAT straddles the Notion bear of Rs 300 Cr: the seasonality end sits below it and the bridge top sits above it.

EPS and forward PE at CMP Rs 548 [DER]:
| Year / reading | PAT | EPS basic (6.6574 Cr sh) | PE basic | EPS diluted (7.3692 Cr sh) | PE diluted |
|---|---|---|---|---|---|
| FY27E A | 323-370 | 48.5-55.6 | 9.9-11.3x | 43.8-50.2 | 10.9-12.5x |
| FY27E B | 264-309 | 39.7-46.4 | 11.8-13.8x | 35.8-41.9 | 13.1-15.3x |
| FY28E A | 410-430 | 61.6-64.6 | 8.5-8.9x | 55.6-58.4 | 9.4-9.9x |
| FY28E B | 280 | 42.1 | 13.0x | 38.0 | 14.4x |

Notes: diluted figures assume conversion without crediting the Rs 307 Cr balance cash or its interest saving (NOT FOUND in model). Attributable PAT will fall once TXRWL's Mahim project recognises revenue, because ICICI holds 60% of project capital (CC L197-198, MGMT ASR); timing NOT FOUND. FY27 ROCE NOT FOUND in filings.

---

## PLAIN-LANGUAGE BRIEF

Provenance tags: FILED (Reg 33 statements or press release), AGENCY, MGMT (company claim; concall figures are ASR and unverified), SECONDARY, INFERENCE. "Prior Notion" marks earlier work. All else is this quarter.

### 1. SUMMARY NARRATIVE
Raymond Realty sold more homes but earned less this quarter. Q2 bookings were Rs 902 Cr, up 98% (FILED press release). At the company's own share of each project, bookings rose about 81% (MGMT deck, A4 arithmetic). Collections were Rs 682 Cr, up 67% (FILED press release). Revenue rose only 7.4% to Rs 748.52 Cr (FILED). Operating EBITDA rose 15.0% to Rs 106.27 Cr (FILED, A4 arithmetic). Interest owed to approval authorities sits below EBITDA. Counted as a project cost, EBITDA rose only 8.3% and the margin barely moved (A4 arithmetic). Finance cost rose 70% to Rs 43.53 Cr (FILED). Net profit fell 11.8% to Rs 53.06 Cr (FILED). H1 operating cash flow was minus Rs 147 Cr (FILED). That is better than minus Rs 319 Cr a year ago. Net debt rose to about Rs 916 Cr from Rs 658 Cr in March (FILED, A4 arithmetic). Two risk first signals are now lit: net debt above Rs 900 Cr, gross debt-to-equity above 0.75. Management kept its 20% bookings guide after H1 grew 111% (FILED press release). That guide implies H2 bookings about 10% below last year's H2 (A4 arithmetic). Management dropped its revenue growth guide (MGMT, ASR). It says debt will not fall for one to two years (MGMT, ASR). It may need Rs 400-600 Cr more equity (MGMT, ASR). The margin stop depends on a pending ruling. The press-release basis gives 15.2%, so no stop fires. The operating basis gives 14.2% after 11.6% in Q1. So a 15% stop fires on that basis. The share price of Rs 548 sits just below the Rs 550 margin-of-safety price. The Decision Status stays WATCHLIST / AVOID. The operator decides after the two rulings.

### 2. SECTOR INTELLIGENCE
Mumbai demand looks firm for tickets above Rs 1.5 Cr (MGMT, ASR). Management expects interest rates to rise (MGMT, ASR). It says buyers at its price points will not react much (MGMT, ASR). Prior Notion work records Mumbai registrations at a 14-year high in CY2025 (prior Notion). Construction labour and material costs are rising (analyst statement on call). Fixed-price contracts protect only ongoing projects (MGMT, ASR). New launches carry the cost risk. Real-estate AIF money is a growing funding route (FILED: ICICI Pru agreement). Peer concalls were not supplied, so no peer check exists this run.

### 3. BUSINESS-MODEL INTELLIGENCE
The company has two engines. Thane owned land is mature and generates cash (MGMT deck, unreviewed). Mumbai JDAs are early and consume cash (MGMT deck, unreviewed). Management now says Thane will plateau at Rs 1,500-1,600 Cr a year (MGMT, ASR). All growth must now come from JDAs. The deck gives two figures for JDA revenue to date. One slide says Rs 1,930 Cr (MGMT deck). The project slides add up to Rs 2,549 Cr (MGMT deck, A4 arithmetic). The Rs 619 Cr gap is not explained. JDA collections to date are Rs 857 Cr (MGMT deck). Those collections include GST and possession charges, so the real cash gap is wider (MGMT deck). At BKC and Sion, revenue exceeds total bookings (MGMT deck). A possible cause is a non-cash landowner share (INFERENCE). Project money from ICICI funds one Mumbai project (FILED). ICICI takes 60% of that project's capital and profit (MGMT, ASR). That lowers the company's share of future Mahim profit. The model is drifting toward more partners, more equity and slower cash.

### 4. COMPETITION INTELLIGENCE
The company wins on brand and fast JDA launches (prior Notion; MGMT). It delivered a Thane tower about 18 months early (FILED press release). Prior Notion work names Sunteck as the cleaner peer (prior Notion). Sunteck carries lower debt and cleaner governance (prior Notion). Raymond Realty is weaker on debt, cash and governance (prior Notion). The ICICI deal answers an earlier gap: a project-level partner (FILED). The partner takes an equity-sized share of project profit (MGMT, ASR). So the deal eases debt but does not make capital cheaper (INFERENCE). Watch whether rivals sign larger partners on better terms. The filings do not disclose market share by micro-market.

### 5. FORWARD MAP (next ~10-11 months)
Make-or-break reading: Q3 FY27 EBITDA margin on both bases, due by 14-Feb-2027 (Section A 8C).
- ICICI first tranche, by about 27-Nov-2026. Bull: equity terms, no put on the parent. Bear: a put or fixed return makes it debt.
- Securities-issue filing, about Nov-2026. Bull: TXRWL terms disclosed in full. Bear: terms withheld again.
- Warrant upfront Rs 102 Cr, Q3 FY27. Bull: received and dated. Bear: still not received.
- BKC aviation approval, Nov-Dec 2026. Bull: approval, then upper floors sell. Bear: further delay hits H2 bookings.
- Mahim-2 launch, by 31-Dec-2026. Bull: RERA registration and a strong launch. Bear: slips into Q4.
- Q3 FY27 results, by 14-Feb-2027. Bull: margin at 18% or above, net debt under Rs 1,000 Cr. Bear: margin under 15%, net debt above Rs 1,000 Cr.
- Mahim-1 launch, by 31-Mar-2027. Bull: launch on time. Bear: slips into FY28.
- FY27 guide test, 31-Mar-2027. Bull: pre-sales up 20% with EBITDA margin 17% or above. Bear: margin and PAT miss.
- Kandivali, Parel and Thane launches, Jul-Sep 2027. Bull: all three launch on time. Bear: launches slip again.

---

```yaml
stage: A4-analyst
company: "RAYMONDREL"
quarter: "q2fy27"
model: "claude-opus-5-5"
status: complete
docs_merged: [results, concall, presentation, corpaction]
ledger_reconciliation:
  notes: 13
  turns: 16
  slides: 46
  all_reviewed: true
  a3_findings_incorporated: [RES-A3-01, RES-A3-02, RES-A3-03, RES-A3-04, RES-A3-05, RES-A3-06, RES-A3-07, RES-A3-08, RES-A3-09, RES-A3-10, RES-A3-11, RES-A3-12, RES-A3-13, RES-A3-14, RES-A3-15, RES-A3-16, RES-A3-17, RES-A3-18, RES-A3-19, RES-A3-20, RES-A3-21, RES-A3-22, RES-A3-23, PRE-A3-01, PRE-A3-02, PRE-A3-03, PRE-A3-04, PRE-A3-05, PRE-A3-06, PRE-A3-07, PRE-A3-08, PRE-A3-09, PRE-A3-10, PRE-A3-11, PRE-A3-12, PRE-A3-13, PRE-A3-14, PRE-A3-15, PRE-A3-16, PRE-A3-17, PRE-A3-18, PRE-A3-19, PRE-A3-20, PRE-A3-21, PRE-A3-22, PRE-A3-23, PRE-A3-24, PRE-A3-25, PRE-A3-26, PRE-A3-27, PRE-A3-28, PRE-A3-29, PRE-A3-30, PRE-A3-31, PRE-A3-32, PRE-A3-33, PRE-A3-34, PRE-A3-35, FND-01, FND-02, FND-03, FND-04, FND-05, FND-06, FND-07, FND-08, FND-09, FND-10, FND-11, FND-12, FND-13, FND-14, FND-15, FND-16, FND-17, FND-18, FND-19, FND-20, FND-21, FND-22, FND-23]
protocol_verdict: "PROCEED WITH FLAGS"
cash_conversion: "INDETERMINATE-WITH-DIRECTION"
decision_status_verified: "WATCHLIST / AVOID"
position_branch: "8A-W"
sc_gap_pat_pct:
  - {period: "Q2 FY27", gap_pct: 27.7}
  - {period: "Q1 FY27", gap_pct: -49.1}
  - {period: "Q2 FY26", gap_pct: 3.0}
  - {period: "H1 FY27", gap_pct: -2.1}
  - {period: "H1 FY26", gap_pct: -10.1}
  - {period: "FY26", gap_pct: 15.9}
questions_for_management:
  - {q: "Reconcile deck p5 JDA revenue recognised Rs 1,930 Cr with project rows Rs 2,549 Cr (gap Rs 619 Cr); quantify non-unit-sale JDA revenue (BKC 577 vs bookings 521; Sion 242 vs 229; BKC Rs 175 Cr pre-launch in Q2 FY26); state the Ind AS 115 method and collections ex-GST", from_finding_id: "PRE-A3-24, PRE-A3-25, PRE-A3-26, PRE-A3-27, PRE-A3-21, RES-A3-05, FND-03"}
  - {q: "Give TXRWL OCPRS terms: conversion, redemption/put/support on RRL (a party to the agreement), coupon, post-issue shareholding, tranches, project, RRL Rs 140 Cr share status", from_finding_id: "FND-12, FND-13, FND-14, RES-A3-17"}
  - {q: "Give the Q3/Q4 EBITDA margin path to 17-19% from H1 14.3%; state whether the guide includes other income and excludes Rs 17 Cr authority interest", from_finding_id: "RES-A3-08, RES-A3-11, RES-A3-15, PRE-A3-05, PRE-A3-11, PRE-A3-35, PRE-A3-28, FND-01, FND-02"}
  - {q: "Define net debt; disclose authority-dues principal and its line; break down Rs 1,908 Cr other financial liabilities; give blended cost of all borrowings", from_finding_id: "RES-A3-16, RES-A3-17, PRE-A3-15, PRE-A3-28, FND-07, FND-08"}
  - {q: "Refinancing plan for Rs 452 Cr current borrowings vs Rs 308 Cr buffer; where does Rs 85.75 Cr interest paid sit in the deck cash format, and how does the Rs 155 Cr bank-loan line reconcile to Rs 200.58 Cr net borrowing; FY27 finance cost in Rs Cr", from_finding_id: "RES-A3-03, PRE-A3-16, FND-06, FND-10, FND-21"}
  - {q: "Give the FY27 revenue growth number dropped from the deck; reconcile EBITDA +20%, margin 17-19% and pre-sales +20%", from_finding_id: "FND-03, FND-23, PRE-A3-06"}
  - {q: "Give RERA dates for Mahim-2 (Q3) and Mahim-1 (Q4); why Mahim-1 moved from Q3; is launch contingent on the ICICI tranche", from_finding_id: "RES-A3-09, PRE-A3-07, PRE-A3-01, FND-15"}
  - {q: "Date of receipt of the Rs 102 Cr warrant upfront vs 'has infused 410 crores'; timing of the Rs 247 Cr Jekegram object given Thane parcel launch Q2 FY28", from_finding_id: "RES-A3-13, PRE-A3-17, FND-11, PRE-A3-08, RES-A3-19"}
  - {q: "Date of BKC aviation approval and booking value awaiting upper-floor RERA; explain Q1 BKC net cancellation", from_finding_id: "FND-16, PRE-A3-03"}
  - {q: "Plan for Invictus Tower B Thane after bookings fell 5, 2, 0", from_finding_id: "PRE-A3-02"}
  - {q: "Was PAT margin 9-10% guided before Q2, on what base; basis and first positive year of the Rs 10,000 Cr OCF figure", from_finding_id: "RES-A3-10, PRE-A3-10, FND-04, FND-05, PRE-A3-13"}
  - {q: "Which entity booked Tower B OC revenue; why subsidiary revenue +63% QoQ while standalone -29% YoY; subsidiaries outside joint review", from_finding_id: "RES-A3-04, RES-A3-06, RES-A3-05"}
  - {q: "Counterparty of the Rs 127.60 Cr ICD and nature of the Rs 217 Cr fall in standalone other current assets", from_finding_id: "RES-A3-01, RES-A3-20"}
  - {q: "Purpose of the Rs 2 lakh group investment; date of Chembur to Ten X Realty North rename; JDAs behind GDV 42,000 to 52,000 and the addition at economic interest", from_finding_id: "RES-A3-02, RES-A3-23, PRE-A3-20, FND-17"}
  - {q: "Source and durability of the 18.5% ETR vs 25.17%; why taxes paid exceed current tax", from_finding_id: "RES-A3-12, PRE-A3-14"}
  - {q: "Basis of Q2 FY26/H1 FY26 comparatives and the FY20-FY26 track record (carve-out, audited or not)", from_finding_id: "RES-A3-21, PRE-A3-12"}
  - {q: "Timing and form of the Rs 400-600 Cr LRP equity vs the prior no-fundraise stance", from_finding_id: "FND-11, FND-10"}
  - {q: "Report pre-sales at economic interest; state GST treatment of bookings; define launched units sold", from_finding_id: "PRE-A3-32, PRE-A3-31, PRE-A3-30"}
  - {q: "Supply missing footnotes, Park Street collections, and identify pipeline Sr. 4 and launched Sr. 7", from_finding_id: "PRE-A3-22, PRE-A3-29"}
  - {q: "Restate 'Board Independence : 100% i.e. All the Board Committees are chaired by Independent Director' when 5 of 8 directors are independent", from_finding_id: "PRE-A3-19"}
  - {q: "Quantify revenue by brand vs the claim that growth came 'entirely' from Address by GS", from_finding_id: "PRE-A3-34, RES-A3-05"}
  - {q: "Contingency % in Mahim budgets and underwriting margin for H2 launches under cost inflation", from_finding_id: "FND-20"}
  - {q: "Projects behind the Rs 185 Cr pre-launch outflow (Rs 178 Cr approvals)", from_finding_id: "PRE-A3-18, RES-A3-18"}
  - {q: "Target FY27 collections-to-pre-sales ratio after 77% in H1 vs 103% a year ago, with or without GST", from_finding_id: "RES-A3-18, FND-23"}
  - {q: "Share of Rs 1,220 Cr debt that is floating, and cost of the AIF money", from_finding_id: "FND-21"}
monitorables:
  - {item: "ICICI AIF first tranche into TXRWL", implied_date: "2026-11-27", source_ref: "CC L376; C-12"}
  - {item: "Securities-issue intimation with instrument terms", implied_date: "2026-11", source_ref: "CA L174-180; R047"}
  - {item: "Warrant allotment and Rs 102 Cr upfront", implied_date: "Q3 FY27 (2026-11)", source_ref: "NOT L8; CC L149-150"}
  - {item: "BKC aviation approval then upper-floor RERA", implied_date: "2026-11 to 2026-12", source_ref: "CC L517-522; C-16"}
  - {item: "Mahim-2 launch and RERA registration", implied_date: "2026-12-31", source_ref: "PRE l460; CC L368"}
  - {item: "Q3 FY27 results: margin both bases, net debt per ruling, NCI line", implied_date: "2027-02-14", source_ref: "Reg 33; Step 8C"}
  - {item: "Mahim-1 launch", implied_date: "2027-03-31", source_ref: "PRE l461"}
  - {item: "ICICI full Rs 210 Cr received", implied_date: "2027-03-31", source_ref: "CC L377"}
  - {item: "Research coverage at least 4 firms", implied_date: "2026-12-31 to 2027-03-31", source_ref: "CC L316-317"}
  - {item: "FY27 guide test: pre-sales +20%, ROCE 20%, EBITDA 17-19%, PAT 9-10%", implied_date: "2027-03-31", source_ref: "RES L723-724"}
  - {item: "Kandivali, Parel, Thane owned-parcel launches", implied_date: "Q2 FY28 (2027-09-30)", source_ref: "PRE l462-464"}
  - {item: "Fully funded for next year of construction (Rs 308 Cr buffer)", implied_date: "2027-09", source_ref: "RES L715"}
  - {item: "Gross debt holds Rs 1,200-1,400 Cr; no fall for 1-2 years", implied_date: "FY28-FY29", source_ref: "CC L140, L471-472"}
  - {item: "Warrant balance Rs ~307 Cr", implied_date: "2028-04", source_ref: "NOT L8"}
  - {item: "Steady state 8-10 projects outside Thane", implied_date: "FY29", source_ref: "CC L121-126"}
  - {item: "LRP equity Rs 400-600 Cr decision", implied_date: "FY28-FY32", source_ref: "CC L409-410, L475"}
  - {item: "Operator rulings: margin stop and net-debt basis", implied_date: "before Q3 FY27 print", source_ref: "checklist L60-64"}
flags:
  - "Margin stop basis-dependent: operating (ex-OI) Q1 11.61% / Q2 14.20% fires a 15% stop; press-release basis 13.11% / 15.21% does not; authority-interest-adjusted fires 14%; 18% fires on all bases. Ruling pending; if fired, 8A-W proposes AVOID (operator sets)."
  - "Operations claim qualified: op EBITDA +15.0% / +94 bps YoY shrinks to +8.3% / +10 bps with authority interest (10 to 17) treated as approval cost."
  - "Risk #2 first signals lit: net debt Rs 916 Cr (> 900) and gross D/E 0.752 (> 0.75); H1 pace +Rs 129 Cr/qtr crosses Rs 1,000 Cr in Q3 before inflows [INFERENCE]."
  - "Net-debt ruling moot at Q2 (no warrant or AIF money by 30-Sep); binds from Q3; R4 framing gives Rs 1,126 Cr."
  - "Consolidated PAT -11.8% YoY Q2 and -13.3% H1 on finance cost +70%; FY27 PAT Reading B Rs 264-309 Cr straddles the Notion bear Rs 300 Cr (seasonality end below it)."
  - "Revenue guide DROPPED: removed from deck and denied on call; guidance trio internally inconsistent."
  - "JDA revenue quality: deck p5 states JDA revenue recognised Rs 1,930 Cr vs Rs 2,549 Cr on project rows (Rs 619 Cr gap, all in JDAs); BKC and Sion revenue exceed bookings; JDA collections Rs 857 Cr include GST and possession charges; BKC Rs 175 Cr pre-launch revenue in Q2 FY26 base."
  - "Demand qualified: Q2 pre-sales +98% gross but about +81% at economic interest; unchanged guide implies H2 pre-sales about -10.5% YoY; H1 BD ~Rs 8,500 Cr gross is ~Rs 4,675 Cr at economic interest if Parel [INFERENCE]."
  - "Concall 'promoter has infused ~410 Cr' and 'subsidiary has raised 210 Cr' contradicted by filings (no money in H1; no securities issued at 26-Oct)."
  - "ICICI AIF terms NOT DISCLOSED in filing (instrument, coupon, put, TXRWL shareholding, tranches); RRL is a party; money is equity-priced (60% residual profit, project IRR 20-25% vs 9.6% debt); price / TXRWL PAT not computable; NCI ahead."
  - "Mahim-1 now Q4 FY27 (checklist #4 red window); Thane owned-parcel launch Q2 FY28 vs warrant objects."
  - "All 7 subsidiaries (63.0% Q2 revenue, 72.7% gross assets) outside joint review; standalone revenue -28.5% YoY."
  - "Credibility provisional 50% (Grade C) on 1 of 4 quarters; archetype OVERPROMISER provisional and borderline; workup grade A not replaced."
  - "Promoter absent from call; capital stance reversed (Rs 400-600 Cr more equity under LRP)."
  - "CMP Rs 548 is Rs 2 below the Rs 550 MoS; inside post-DA Rs 500-550 and diluted ~Rs 523-581 bands; Promoter CONCERN caps; no BUY gate met."
  - "Stale Notion fields: net D/E 0.13x (filed 0.565x); I-6 state; 10X Mahalakshmi vs TXRWL as deal vehicle."
  - "Tracker rows not supplied (titles only); fewer than three external signals."
plain_language_brief_included: true
analyst_note: "Q2 splits along a basis line. Operating EBITDA rose 15% and margin 94 bps, but with authority interest counted as approval cost the gains are +8.3% and +10 bps; finance cost +70% took the rest, so PAT fell 11.8%. The margin stop depends on basis more than threshold: at 15%, the press-release basis clears by 21 bps and the operating basis fails. The net-debt ruling cannot change Q2 because no warrant or AIF money arrived by 30-Sep; OCPRS terms decide R2 versus R3/R4 from Q3. ICICI money is equity-priced: it lowers net debt only if classified as equity, and it does not cheapen capital. The biggest open risk is JDA revenue quality: deck p5 states JDA revenue recognised of Rs 1,930 Cr while the project slides sum to Rs 2,549 Cr; the Rs 619 Cr gap may be non-sale revenue. Demand is strong gross but about +81% at economic interest, and the unchanged guide implies H2 pre-sales about 10.5% lower. Credibility C and OVERPROMISER are provisional and turn on one scoring call. Loop 1 also corrected FY26 ROCE, the FY27E PAT B range (264-309) and the hedge count."
review_path: "runs/raymondrel-q2fy27/work/review_raymondrel_q2fy27.md"
```

---

## Loop 1 change log (A5 audit, correction loop 1 of 1)

Placed after the closing block on the coordinator's instruction; the block above is unchanged in schema and is the copy written to `work/blocks/a4-review.yaml`.

| Item | Type | Change | Where |
|---|---|---|---|
| F1 | FACTUAL | Deck R363 relabelled "Finance, Legal & IT Cost (26)", a corporate-cost line, not interest; deck format has no interest line; PRE-A3-16 premise noted as a label misread; Q5 re-posed (interest paid Rs 85.75 Cr location; bank loan Rs 155 Cr vs net borrowing Rs 200.58 Cr) | Step 5 interest cash check; Q5; YAML q5 |
| F2 | FACTUAL | FY27E PAT Reading B widened from 264-290 to 264-309 with the H2 input stated (H2 revenue 1,984.81-2,267.81; PAT margin on revenue 11.9%; -27.1 after-tax interest); bridge gives 276-309. PE row B: basic 11.8-13.8x, diluted 13.1-15.3x; EPS 39.7-46.4 / 35.8-41.9. Dependent lines aligned: 6A PAT/EPS rows and re-weighting note ("straddles bear"), Step 7 hurdle row, Step 8 8A-W bullet, flags, analyst_note. Verdict and stop scores unchanged | Forward Estimate Inputs; 6A; Step 7; Step 8; YAML |
| F3 | FACTUAL | FY26 ROCE same basis corrected from 18.4% to 23.4% (EBIT 472.33 / avg of FY25 deck capital 1,459, PRE l180 R127, and Mar-26 2,581.17); 18.3% on closing capital | 6A ROCE row; Step 7 ROCE row |
| F4 | FACTUAL | Defensive-language total corrected from 15 to 16 (A4's own list); conclusion unchanged | Role 5 Step 6C |
| M1 | MISSING | Authority-adjusted YoY added: Q2 op EBITDA 82.42 to 89.27 (+8.3%), margin 11.82% to 11.93% (+10 bps); H1 +25.1%, +54 bps | Step 2 table and diagnostic 2; Role 5 7A margin row; Section C Operations; Step 9 Key Notes; brief summary; flags; analyst_note |
| M2 | MISSING | Collections include GST and other possession charges (PRE l149, l444); GST amount NOT DISCLOSED; gap wider than shown | Step 5 structural answer; 6B I-2; 6D trigger 1; Q1; Q24; brief business-model; flags |
| M3 | MISSING | Demand qualified: economic-interest Q2 pre-sales about +81% (794 vs 438); guide implies H2 -10.5%; BD ~Rs 4,675 Cr at economic interest if Parel [INFERENCE] | Section C Demand row and verdict line; 6B #5; 6D trigger 5; Role 5 Step 2 diagnostic, 3A BD row, 8A, 8B #5; Q14; brief summary; flags |
| M4 | MISSING | ICICI: RRL is a party (CA L44, L95-123); price / TXRWL PAT not computable; money equity-priced (IRR 20-25% vs 9.6% debt) | 0C term table (new Parties and Price/economics rows); Step 5 ruling facts; Role 5 8E; concall verdict; Section C Capital row; Q2; brief competition; flags; analyst_note |
| C1 | CONTRADICTION | Deck p5 JDA revenue Rs 1,930 Cr (R037-R039) vs project rows Rs 2,549 Cr (R446, R454, R464, R472; total R478); Rs 619 Cr gap all in JDAs; PRE-A3-21's BKC-577 reading revised | Step 5 structural answer; Role 5 5B and 8E; Section C Operations; Q1 and Top-3; Step 9 Key Notes; brief business-model; flags; analyst_note; YAML q1 |
| S1 | STYLE | Deck board-independence gloss quoted | 6B #7; Q20; YAML q20 |
| S2 | STYLE | Call time cited to the concall fulltext header (line 14), not CC L19 | Role 5 Step 0C |
| S3 | STYLE | "Customer-advance" reading of Other current liabilities tagged [INFERENCE] | Step 5 table and text; Role 5 7A collections row |
| S4 | STYLE | Q1 FY27 authority interest moved from one-offs to the run-rate note (recurring) | Step 3 table |
| S5 | STYLE | Dilution row cites the issuer line (TXRWL "Issuer", CA L99-101) | 0C term table |

Unchanged: protocol verdict (PROCEED WITH FLAGS), cash conversion (INDETERMINATE-WITH-DIRECTION), every stop-loss score, the margin-stop and net-debt matrices, FY27E Reading A, FY28E rows, credibility and archetype, monitorables. C2 (concall ledger line/turn columns) is addressed to A2; no A4 number uses that column.
