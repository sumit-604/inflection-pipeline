# ROUTE MOBILE LIMITED (ROUTE): Q2 FY27 MERGED QUARTERLY REVIEW (Role 4; Role 5 NOT RUN)

Quarter and half year ended 30 September 2026. Board meeting 27 October 2026, 9:00 PM to 10:35 PM IST (results R016-R017, L114).
Agent: A4 analyst | Model: claude-opus-5-5 | Run date: 2026-10-29 | Run folder: runs/route-q2fy27/

Documents merged: results filing (Reg 33, limited review), investor presentation (23 slides), press release (3 pages).
Role 5 status: NOT RUN. No concall transcript exists. The call ran 28 October 2026 at 16:30 IST. The company's earnings-call page lists it with no recording, and no ASR transcript appeared before this run started. Every concall-dependent cell below is ND, and every "silence" count is on a filed-document basis only.
Protocol loaded: frameworks/Quarterly_Results_Review_Protocol_v1_4.md (Role 4). Per operator ruling OR-30, Steps 6.5 and 7 are deferred to /fttcp and Role 1; pillar-relevant facts are flagged in place.
Input discipline: A1 structured extractions and fulltexts, A2 ledgers, A3 forensics, the Notion thesis extract, and the prior-quarter merged review only. No source PDF and nothing under inputs/ was opened.

Anchor key: "R###" = A1 structured row ID in the named document; "L###" = A1 fulltext line. Results rows are cited as R### (results); deck rows as dR### (presentation); press-release rows as pR###. Notion rows cite runs/route-q2fy27/work/notion_thesis_context.md line numbers as "N-L###". Derived numbers are arithmetic on two or more filed figures and say so.

---

## LEDGER RECONCILIATION PREAMBLE

Ledger contains 23 notes / 0 turns / 26 slides (23 investor-presentation slides + 3 press-release slide-equivalents). All 23 notes, all 26 slides, and all 1,129 + 368 + 74 = 1,571 structured rows referenced by the three A2 ledgers were reviewed (A2: orphan_ids none in all three; A3: ledger_reconciled_pct 100 in all three). No ledger row is unreviewed.

Findings incorporated (66):
- Results (25): F1-01, F1-02, F1-03, F2-01, F2-02, F2-03, F2-04, F3-01, F4-01, F4-02, F6-01, F6-02, F8-01, F8-02, F9-01, F12-01, F12-02, F12-03, F13-01, F13-02, F13-03, F14-01, F14-02, F14-03, F14-04.
- Presentation (26): A3-01 to A3-26.
- Press release (15): FN01 to FN15.

Cross-document resolutions made in this review (A3 worked one document at a time):
- A3-07 and FN05 (EPS-implied share count fell 5.2%): RESOLVED. Paid-up capital is Rs 63.00 Cr in all six columns (R251-R256, L375), so 6.30 Cr shares. EPS uses PAT attributable to owners: 79.57 / 6.30 = 12.63 (R197, R258); 62.61 / 6.30 = 9.94 (R198, R259). "PAT reported" 82.55 includes NCI 2.98 (R203). No buyback. The residual question moves to the NCI halving (5.94 to 2.98; F2-02).
- A3-08 (dividend wording carried from Q1): RESOLVED. The board letter names a SECOND interim dividend of Rs 4, record date 02 Nov 2026 (R005, R1016, L50-55). FY27 interim to date Rs 8/share.
- FN06 (Reg 30 timing untestable): RESOLVED. Board ended 10:35 PM IST (R017); CS letter signed 23:49 (R1025); press release signed 00:03:52 on 28 Oct (pR036). Sequence clean.
- FN08 (Heltar consideration undisclosed): RESOLVED. Note 6 discloses up to Rs 33.66 Cr; Rs 23.88 Cr paid; Rs 9.78 Cr at 18 months (R585-R587, L851).
- FN12 and A3-18 (thesis-broken test needs Adjusted EBITDA): SOURCED from deck slide 19 (dR266, L745-746). See Step 6C.
- FN01 (unnamed Q2 FY26 exceptional): NAMED by results note 7: 7a Rs 107.96 Cr minimum-guarantee SMS advance write-off; 7b Rs 27.91 Cr vendor advance write-off (R589-R590, L853-857).
- F1-01 (what the Rs 4.90 Cr "provision on other receivables" covers): the H1 cash-flow line 4.90 (R488, L714) equals the deck's Q1 "Loss allowance, Capital advance (one time impact)" 49.0 mn (dR260, L743). [INFERENCE: amount match; the filing does not cross-reference.]

Proceeding to Step 0.

---

# SECTION A: RESULTS REVIEW (ROLE 4)

## STEP 0: PRE-FLIGHT

### 0A. Notion thesis baseline (fetched live by the orchestrator 29-Oct-2026; page content as of 2026-09-03T02:54Z)

| Field | Value on file | Anchor |
|---|---|---|
| Decision Status | HELD | N-L11 property "Decision Status":"HELD" |
| Position | HOLD 4% at average cost Rs 509; RDE trim 4%->3% DEFERRED; cap 5% conditional on revenue YoY >=0% AND GM >=23%; add <=Rs 510; hard floor Rs 450; trim >Rs 820 1%, >Rs 1,330 50% | N-L11 "Position Size", "Avg Cost" |
| One-line thesis | EPS Rs 50 to Rs 88 over 3 years on GM 21% to 25% and 12% revenue CAGR; destination PE 17.6x; thesis breaks if EBITDA margin <10% for 2 consecutive quarters OR Proximus strategic review/sale | N-L21 |
| Destination PE (latest) | ~18.0x (ROCE base 12.0x, cash multiplier 1.10x, growth premium +3.5x, strategic premium +1.25x with Q2 FY27 expiry watch, sector cap 22x); HR 2.53 PASS | N-L583-596 |
| Entry / MoS (latest) | PW FV Rs 1,131; entry Rs 579; MoS Rs 463 (AR review 11-Aug-2026). Properties still show Entry Price Max 628 and Margin of Safety Price 502 (stale) | N-L640-648; N-L11 |
| Base case FY27E | Revenue Rs 4,958 Cr; GM 23.5%; EBITDA margin 12.5%; PAT Rs 394 Cr; EPS Rs 62.6; net cash Rs 1,250 Cr; ROCE ~14% | N-L83-99 |
| Bear / Bull FY27E | Revenue Rs 4,648 / Rs 5,224 Cr; margin, PAT, EPS for FY27 not stated (FY29 bear GM 22%, EBITDA 11%, PAT margin 6.5%; Realistic Bear EBITDA 8.5%) | N-L65-79; N-L126 |
| Thesis-broken conditions | (1) EBITDA margin <10% 2 consecutive Q; (2) Proximus strategic review/sale; (3) loss of 3+ digital-native clients in 12m; (4) ROCE <8% sustained 2Q; (5) arbitration loss >Rs 100 Cr + second similar dispute | N-L202-208 |
| Monitoring checklist | 16 items (12 in Section 8 + #13 Truecaller, #14 Heltar, #15 M&A pace, #16 Salesforce AgentExchange; #6 refined with single customer >18% red) | N-L224-237, N-L277, N-L287-293, N-L656-661 |
| Devil's advocate | Bull 15% / Base 35% / Realistic Bear 30% / Catastrophic Bear 20% (AR re-weight) | N-L642 |
| Management grade | C (Mixed), archetype EVASIVE; 0 of 12 Q1 questions fully addressed | N-L511-517; N-L606 |
| Strategic Premium expiry | Q2 FY27 concall must deliver at least one Proximus revenue-synergy KPI, else +1.25x drops to +1.0x | N-L579; N-L11 Key Notes |

Decision Status verified as HELD before any position framing. Branch 8A applies.

### 0B. Units
- Results filing: Rs crore, x1 (R1082 "(f in crores except earnings per share)").
- Investor presentation: Rs million, x0.1 to Rs crore (slides state "(in mn)", deck L736). Slide 9 (Heltar) alone is in crore (dR079-dR082). A1's header said "Crores"; A3 corrected this, and this review applies x0.1.
- Press release: Rs crore, x1 (pR004).
- Tie-out: deck revenue 11,797 mn = Rs 1,179.7 Cr vs filing 1,179.67 (dR171, R049); deck GP 2,640 mn = 264.0 vs filing-derived 263.95; deck EBITDA 1,150.2 mn = 115.02 vs filing-derived 115.02 (dR250); deck PAT 825.5 mn = 82.55 (dR275, R139). Clean.

### 0C. Share count
- Paid-up equity Rs 63.00 Cr in every column, face value Rs 10, so 6.30 Cr shares (R251-R256, R434-R435, L375, L664).
- Basic = diluted every period (12.63/12.63, 9.94/9.94, (3.37)/(3.37); R258-R269). Dilution spread zero.
- ESOP: 2,860 options lapsed on cessation under Plan 2021 (R011, L80); ESOP charge nil in H1 FY27 (R506, L723; Q1 FY26 1.14).
- No split, bonus, rights, QIP, buyback in the period. Reported EPS = share-adjusted EPS.

### 0D. Notes extraction (all 23 notes: consolidated 1-9 incl. 3a, 7a, 7b; standalone 1-8 incl. 3a; plus 2 cash-flow method lines)

| Note # | Subject | What it says (1 sentence) | Rs Cr impact | Period affected | Comparability impact |
|---|---|---|---|---|---|
| C1 | Basis of preparation | Ind AS 34 / Reg 33; Holding Company and 33 subsidiaries (R562, R1091, L815). | nil | all | None; entity list 33 vs 33, no add or remove (F14-01, F15 PASS). |
| C2 | Review and approval | Audit Committee and Board approved 27 Oct 2026; auditor gives unmodified limited-review conclusion (R1092, L820). | nil | Q2 | First review by MSKA (new auditor; F14-03). |
| C3 | IPO utilisation | Planned 240.00, used 175.00, unutilised 65.00 for Mumbai office (R563-R577, L828-833). | 65.00 unutilised | since IPO | Rs 65 Cr of reported cash is earmarked. |
| C3a | IPO unutilised | Rs 65.00 Cr temporarily in bank deposits (R998, L834). | 65.00 | Q2 | Cash earmark; letter item 4 rescinds the 7 May 2026 variation (F6-01). |
| C4 | QIP | Rs 867.50 Cr QIP "being duly utilised"; unutilised in FDs (R578, R999, L835). | not quantified | prior years | Unchanged vs Q1; utilisation balance ND. |
| C5 | FX presentation | Net FX gain sits in Other income; net FX loss in Other expenses. Net (gain)/loss: Q2 FY27 (1.02), Q1 FY27 (0.61), Q2 FY26 (17.72), H1 FY27 (1.63), H1 FY26 7.01, FY26 (14.76) (R579-R584, L838). | Q2 FY26 OI holds 17.72 gain | Q2 FY26 base | YES. Q2 FY26 Other income 27.16 includes a 17.72 FX gain, so the YoY OI fall (-14.95) is mostly FX. H1 FY26 shows a net loss in other expenses while Q2 FY26 alone shows a gain in OI, so reported EBITDA does not add across periods (A3-03). |
| C6 | Heltar acquisition | Route Connect bought Heltar's AI customer-engagement business on slump sale, 29 Jul 2026 (BTA 13 Jul 2026), up to Rs 33.66 Cr: 23.88 paid, 9.78 at 18 months (R585-R588, L849-851). | 33.66 | Q2 onward | YES. Q2 carries about 2 months of Heltar; no revenue split disclosed, so organic QoQ growth is overstated by an unknown amount (FN08, A3-22). |
| C7 | Exceptional items FY26 | FY26 exceptional items pertain to two write-offs (R1100, L852). | 135.87 | Q2 FY26 / H1 FY26 / FY26 | YES. Q2 FY26 PBT 2.00 is after (135.87); YoY PBT and PAT growth are base effects. |
| C7a | MG SMS advance | Net advance written off Rs 107.96 Cr under a minimum-guaranteed SMS volume agreement; claims withdrawn per settlement 19 Feb 2026 (R589, R1101, L853-855). | 107.96 | FY26 | Closed; watch item 9 GREEN. Bears on thesis-broken condition 5 reading (Step 6C). |
| C7b | Vendor advance | Rs 27.91 Cr advance for messaging services written off on "significant uncertainty regarding its recoverability" (R590, R1102, L856-857). | 27.91 | FY26 | Same asset class as the Q2 Rs 116.83 Cr vendor prepayment (A3-02, F1-01). |
| C8 | Dividend | Interim dividend 40% (Rs 4/share) on 27 Oct 2026 (R591-R593, L858). The note says "recommended"; the letter says the Board declared a "Second Interim Dividend" (L50). | ~25.20 cash in Q3 (A3 derived, F13-03) | Q3 FY27 | Drafting mismatch (F14-04); no comparability impact. |
| C9 | Regrouping | Previous-period figures regrouped; impact not material (R1104, L860). | not quantified | prior | Low. |
| CF note | Cash-flow method | Indirect method, Ind AS 7 (R1089, L702). | nil | H1 | None. |
| S1 | Basis | Standalone Ind AS 34 / Reg 33 (R1117, L1166). | nil | all | None. |
| S2 | Approval | Approved 27 Oct 2026; unmodified conclusion (R1118, L1171). | nil | Q2 | First MSKA review. |
| S3 | IPO (standalone) | Same 240 / 175 / 65 (R884-R898, L1184-1193). | 65.00 | since IPO | Mirrors C3. |
| S3a | IPO unutilised | Rs 65 Cr in bank deposits (R1002, L1195). | 65.00 | Q2 | Mirrors C3a. |
| S4 | QIP (standalone) | Rs 867.50 Cr being utilised (R899, R1122, L1197). | not quantified | prior | Mirrors C4. |
| S5 | Segments | Segment information presented with consolidated results (R1123, L1201). | nil | all | None. |
| S6 | Subsidiary dividends | Standalone Other income includes subsidiary dividends: Q2 FY27 nil, Q1 FY27 4.22, Q2 FY26 nil, H1 FY27 4.22, H1 FY26 2.46, FY26 2.46 (R900-R905, L1206-1209). Q1 column misprinted "30.06.2025" (F14-02). | 4.22 (Q1) | Q1 FY27 | YES for standalone QoQ: Q1 standalone PBT 20.25 held 4.22 of intra-group dividend; Q2 holds none, so the standalone Q2 PBT jump is operating. |
| S7 | Dividend | Interim 40%, Rs 4 (R906-R908, L1211). | as C8 | Q3 | None. |
| S8 | Regrouping | Not material (R1126, L1213). | n/a | prior | Low. |
| SCF note | Cash-flow method | Indirect method (R1115, L1092). | nil | H1 | None. |

Note-level answers:
- YoY comparisons need normalising for C7 (exceptional 135.87) and C5 (Q2 FY26 FX gain 17.72 in OI). QoQ comparisons need C6 (two months of Heltar) and S6 (4.22 subsidiary dividend in Q1 standalone).
- Recurring vs one-off: C7 one-off (closed); C5 recurring presentation with volatile sign; C6 recurring from Q2.
- Thesis-relevant: C7b and the new vendor advance (same asset class); C3a Rs 65 Cr earmark.

Auditor opinion check: Limited review, UNMODIFIED conclusion, consolidated and standalone (R1070, R1073, L224, L248). No Emphasis of Matter and no going-concern paragraph in either review report (F5 PASS; the FY26 AR's two EoMs did not carry into the interim). Other-matter reliance paragraphs: 24 subsidiaries reviewed by other auditors (total assets Rs 1,852.94 Cr, Q2 revenue 565.47, Q2 PAT 65.43, pre-consolidation; R024-R032, L196-203); 11 overseas subs converted from local GAAP by management (R033, L211); 7 subsidiaries not reviewed, management-certified (assets 45.28, Q2 revenue 0.75, Q2 loss (0.21); R034-R042, L227-234); comparatives reviewed or audited by the predecessor auditor (R043, L250-252). Status: AMBER data-reliance flag, not an opinion modification. Auditor change: MSKA & Associates (FRN 105047W/W101187; R044) replaces Walker Chandiok, as approved at the 2 Sep 2026 AGM (N-L11 Key Notes). First quarter of the new auditor.

### 0E. Business type
Standard operating business (CPaaS). Not a lender. Steps 1 and 5 apply. Cost of materials maps to "Purchase of messaging services"; gross profit = revenue less messaging cost.

Checkpoint: Notion fetched incl. Decision Status (HELD), units identified, share count unchanged, all 23 notes extracted, auditor conclusion unmodified with reliance paragraphs, business type standard.

---

## STEP 1: DATA EXTRACTION (Rs Cr)

### 1A. CONSOLIDATED

| Line item (anchor) | Q2 FY26 | Q1 FY27 | Q2 FY27 | H1 FY26 | H1 FY27 | FY26 | FY27 |
|---|---|---|---|---|---|---|---|
| Revenue from operations (R051, R050, R049, R053, R052, R054; L333) | 1,119.42 | 1,151.51 | 1,179.67 | 2,170.25 | 2,331.18 | 4,408.21 | ND |
| Other income (R057, R056, R055, R059, R058, R060; L334) | 27.16 | 11.06 | 12.21 | 20.37 | 23.27 | 54.09 | ND |
| Total income (R063, R062, R061, R065, R064, R066; L335) | 1,146.58 | 1,162.57 | 1,191.88 | 2,190.62 | 2,354.45 | 4,462.30 | ND |
| Cost of materials = Purchase of messaging services (R069, R068, R067, R071, R070, R072; L337) | 872.32 | 911.07 | 915.72 | 1,698.08 | 1,826.79 | 3,400.90 | ND |
| Change in inventories (no such line) | ND | ND | ND | ND | ND | ND | ND |
| Employee benefits expense (R075, R074, R073, R077, R076, R078; L338) | 71.66 | 77.62 | 90.81 | 140.25 | 168.43 | 288.85 | ND |
| Finance costs (R081, R080, R079, R083, R082, R084; L339) | 2.37 | 1.36 | 2.46 | 8.19 | 3.82 | 10.82 | ND |
| Depreciation and amortisation (R087, R086, R085, R089, R088, R090; L340) | 22.87 | 23.71 | 23.84 | 45.35 | 47.55 | 91.61 | ND |
| Other expenses (R093, R092, R091, R095, R094, R096; L341) | 39.49 | 57.34 | 58.12 | 84.31 | 115.46 | 181.21 | ND |
| Total expenses (R099, R098, R097, R101, R100, R102; L342) | 1,008.71 | 1,071.10 | 1,090.95 | 1,976.18 | 2,162.05 | 3,973.39 | ND |
| PBT before exceptional (R105, R104, R103, R107, R106, R108; L343) | 137.87 | 91.47 | 100.93 | 214.44 | 192.40 | 488.91 | ND |
| Exceptional item (R111, R110, R109, R113, R112, R114; L344) | (135.87) | - | - | (135.87) | - | (135.87) | ND |
| Profit before tax (R117, R116, R115, R119, R118, R120; L345) | 2.00 | 91.47 | 100.93 | 78.57 | 192.40 | 353.04 | ND |
| Current tax (R123, R122, R121, R125, R124, R126; L347) | 30.34 | 27.66 | 21.62 | 50.71 | 49.28 | 115.65 | ND |
| Deferred tax (R129, R128, R127, R131, R130, R132; L348) | (9.51) | (4.74) | (3.24) | (12.09) | (7.98) | (19.55) | ND |
| Tax expense (R135, R134, R133, R137, R136, R138; L349) | 20.83 | 22.92 | 18.38 | 38.62 | 41.30 | 96.10 | ND |
| PAT (R141, R140, R139, R143, R142, R144; L350) | (18.83) | 68.55 | 82.55 | 39.95 | 151.10 | 256.94 | ND |
| PAT to owners (R199, R198, R197, R201, R200, R202; L364) | (21.21) | 62.61 | 79.57 | 32.00 | 142.18 | 239.02 | ND |
| NCI share (R205, R204, R203, R207, R206, R208; L365) | 2.38 | 5.94 | 2.98 | 7.95 | 8.92 | 17.92 | ND |
| EPS reported, basic Rs (R260, R259, R258, R262, R261, R263; L380) | (3.37) | 9.94 | 12.63 | 5.08 | 22.57 | 37.94 | ND |
| EPS share-adjusted Rs (no share change; R251-R256) | (3.37) | 9.94 | 12.63 | 5.08 | 22.57 | 37.94 | ND |
| OCI net (R187, R186, R185, R189, R188, R190; L361) | 43.60 | 13.10 | 26.33 | 95.85 | 39.43 | 171.18 | ND |
| of which cash-flow hedge, effective portion (R1128, R164, R163, R166, R165, R167; L357, L1275) | - | (3.80) | 3.83 | - | 0.03 | - | ND |
| of which FCTR (R175, R174, R173, R177, R176, R178; L359) | 43.51 | 16.27 | 22.91 | 96.46 | 39.18 | 171.91 | ND |

FY27 column is ND: the year is not complete. Q2 FY26 hedge cell read by render (R1128, L1275).

Derived metrics, consolidated:

| Derived metric | Formula | Q2 FY26 | Q1 FY27 | Q2 FY27 | H1 FY26 | H1 FY27 | FY26 |
|---|---|---|---|---|---|---|---|
| Gross profit | Rev - messaging | 247.10 | 240.44 | 263.95 | 472.17 | 504.39 | 1,007.31 |
| Gross margin | GP / Rev | 22.07% | 20.88% | 22.38% | 21.76% | 21.64% | 22.85% |
| Operating EBITDA | PBT (pre-exceptional) + D + FC - OI | 135.95 | 105.48 | 115.02 | 247.61 | 220.50 | 537.25 |
| Operating EBITDA margin | Op EBITDA / Rev | 12.14% | 9.16% | 9.75% | 11.41% | 9.46% | 12.19% |
| Reported EBITDA, reported PBT basis | PBT + D + FC | 27.24 | 116.54 | 127.23 | 132.11 | 243.77 | 455.47 |
| Reported EBITDA, pre-exceptional | PBT pre-exc + D + FC | 163.11 | 116.54 | 127.23 | 267.98 | 243.77 | 591.34 |
| Mgmt Adjusted EBITDA (deck, mn x0.1) | dR258, dR267, dR266, dR279, dR278; FY26 prior review | 133.25 | 108.93 | 118.42 | 248.68 | 227.35 | 525.91 |
| Mgmt Adjusted EBITDA margin (deck) | dR261, dR269, dR268, dR283, dR282 | 11.9% | 9.5% | 10.0% (10.04% computed) | 11.5% | 9.8% | 11.9% |
| Adjusted EBITDA ex-Masivian add-back | Adj - Masivian fees (dR263 13.6 mn; dR262 69.0 mn; dR274 82.6 mn) | 133.25 | 107.57 | 111.52 | 248.68 | 219.09 | ND |
| Adjusted ex-Masivian margin | / Rev | 11.90% | 9.34% | 9.45% | 11.46% | 9.40% | ND |
| Core PBT (ex-OI), pre-exceptional | PBT pre-exc - OI | 110.71 | 80.41 | 88.72 | 194.07 | 169.13 | 434.82 |
| Core PBT (ex-OI), reported | PBT - OI | (25.16) | 80.41 | 88.72 | 58.20 | 169.13 | 298.95 |
| Other income / PBT (reported) | OI / PBT | n.m. (1,358%) | 12.09% | 12.10% | 25.93% | 12.09% | 15.32% |
| Other income / PBT (pre-exceptional) | OI / PBT pre-exc | 19.70% | 12.09% | 12.10% | 9.50% | 12.09% | 11.06% |
| Effective tax rate | Tax / PBT | n.m. (1,041.5%) | 25.06% | 18.21% | 49.15% | 21.47% | 27.22% |
| Effective tax rate, normalised Q2 FY26 | (20.83 + 16.69 tax on exceptional, dR273) / 137.87 | 27.21% | n/a | n/a | n/a | n/a | n/a |
| PAT margin | PAT / Rev | (1.68%) | 5.95% | 7.00% | 1.84% | 6.48% | 5.83% |
| Normalised PAT (deck Adjusted PAT) | dR277, dR281, dR280, dR289, dR288 | 100.36 | 68.55 | 82.55 | 159.13 | 151.10 | ND |

Adjusted EBITDA bridge, Q2 FY27 (deck L739-745, mn): EBITDA 1,150.2 less intangible assets under development 35.0, plus Masivian data-breach professional fees 69.0 = 1,184.2. ESOP, FX-loss, capital-advance, exceptional and tax-impact lines are dash (dR290, dR353, dR357, dR362, dR365). Q1 FY27: 1,054.8 - 28.1 + 49.0 + 13.6 = 1,089.3. The IAUD deduction is conservative; the Masivian add-back is the only upward item in Q2.

Segment table, consolidated (segment result before OI, FC, exceptional, tax):

| Segment (anchor) | Q2 FY26 | Q1 FY27 | Q2 FY27 | H1 FY26 | H1 FY27 | FY26 |
|---|---|---|---|---|---|---|
| Revenue India (R272, R271, R270, R274, R273, R275; L522) | 225.68 | 236.21 | 302.22 | 445.15 | 538.43 | 934.39 |
| Revenue Overseas (R278, R277, R276, R280, R279, R281; L523) | 1,069.45 | 1,063.28 | 1,051.89 | 2,062.18 | 2,115.17 | 4,129.31 |
| Inter-segment (R284, R283, R282, R286, R285, R287; L524) | (175.71) | (147.98) | (174.44) | (337.08) | (322.42) | (655.49) |
| Result India (R296, R295, R294, R298, R297, R299; L527) | 32.15 | (4.00) | 27.11 | 51.73 | 23.11 | 69.20 |
| Result Overseas (R302, R301, R300, R304, R303, R305; L528) | 81.08 | 85.67 | 64.40 | 150.75 | 150.07 | 375.96 |
| India result margin (derived) | 14.25% | (1.69%) | 8.97% | 11.62% | 4.29% | 7.41% |
| Overseas result margin (derived) | 7.58% | 8.06% | 6.12% | 7.31% | 7.09% | 9.10% |
| Total segment result (R314, R313, R312, R316, R315, R317; L532) | 113.08 | 81.77 | 91.18 | 202.26 | 172.95 | 445.64 |
| Liabilities Overseas (R380, R379, R378; L545) | 1,480.79 | 1,095.79 | 981.03 | 1,480.79 | 981.03 | 1,103.52 |

Operating KPIs (deck; mn converted to Rs Cr):

| KPI (anchor) | Q2 FY26 | Q1 FY27 | Q2 FY27 | H1 FY26 | H1 FY27 |
|---|---|---|---|---|---|
| Billable transactions, bn (dR166-dR168, dR225, dR224) | 45.2 | 45.8 | 47.6 | 84.4 | 93.4 |
| Revenue per billable transaction, Rs (derived: revenue mn / txn mn) | 0.2477 | 0.2514 | 0.2478 | 0.2571 | 0.2496 |
| Gross profit per billable transaction, Rs (derived; dR179-dR181) | 0.0547 | 0.0525 | 0.0555 | 0.0559 | 0.0540 |
| New products revenue, Rs Cr (dR096-dR098) | 93.9 | 94.5 | 128.4 | ND | ND |
| New products share of revenue (derived) | 8.39% | 8.21% | 10.88% | ND | ND |
| Revenue excluding new products, Rs Cr (derived) | 1,025.52 | 1,057.01 | 1,051.27 | ND | ND |
| Channel mix SMS vs OTT vs voice | ND | ND | ND | ND | ND |
| Proximus-linked revenue | ND | ND | ND | ND | ND |
| Heltar revenue | n/a | n/a | ND | n/a | ND |
| Top 10 client share (dR143-dR146; H1 annualised) | 43% (FY26) | ND (Q1 slide read 43%, prior review) | 42% (H1) | ND | 42% |
| Top 5 client share (dR147, dR150) | 33% (FY26) | ND | 30% (H1) | ND | 30% |
| Clients >$5mn (dR135, dR136) | 21 (FY26) | ND | 19 (H1 annualised) | ND | 19 |
| Clients >$10mn (dR133, dR134) | 8 (FY26) | ND | 9 (H1 annualised) | ND | 9 |
| Net revenue retention (dR158) | ND | ND | 105% (H1 vs H1) | ND | 105% |
| Active billable clients (dR027) | ND | 2,100+ (prior deck, A3-22) | 2,400+ | ND | ND |
| Headcount (dR049, dR344, dR345) | ND | 783 (derived: 786 - 63 + 60) | 786 | ND | ND |
| Single customer (Customer A) share | 15.1% (FY26 AR, N-L11) | ND | ND | ND | ND |

Gross margin per transaction rose 5.7% QoQ (0.0525 to 0.0555) and 1.5% YoY. Revenue per transaction was flat YoY. All QoQ revenue growth came from new products: new products +33.9, the rest -5.74 (derived). [INFERENCE: new products include about two months of Heltar; the organic split is ND.]

### 1B. STANDALONE

| Line item (anchor) | Q2 FY26 | Q1 FY27 | Q2 FY27 | H1 FY26 | H1 FY27 | FY26 | FY27 |
|---|---|---|---|---|---|---|---|
| Revenue from operations (R599, R598, R597, R601, R600, R602; L962) | 180.27 | 197.93 | 256.33 | 362.99 | 454.26 | 769.87 | ND |
| Other income (R605, R604, R603, R607, R606, R608; L963) | 32.64 | 18.97 | 17.87 | 60.13 | 36.84 | 111.52 | ND |
| Total income (R611, R610, R609, R613, R612, R614; L964) | 212.91 | 216.90 | 274.20 | 423.12 | 491.10 | 881.39 | ND |
| Purchase of messaging services (R617, R616, R615, R619, R618, R620; L966) | 127.38 | 151.77 | 176.93 | 259.22 | 328.70 | 541.11 | ND |
| Change in inventories | ND | ND | ND | ND | ND | ND | ND |
| Employee benefits (R623, R622, R621, R625, R624, R626; L967) | 24.36 | 24.30 | 28.99 | 47.31 | 53.29 | 88.97 | ND |
| Finance costs (R629, R628, R627, R631, R630, R632; L968) | 0.40 | 0.39 | 0.49 | 0.77 | 0.88 | 1.44 | ND |
| Depreciation (R635, R634, R633, R637, R636, R638; L969) | 3.56 | 3.90 | 3.63 | 7.11 | 7.53 | 14.24 | ND |
| Other expenses (R641, R640, R639, R643, R642, R644; L970) | 12.92 | 16.29 | 19.60 | 24.71 | 35.89 | 55.85 | ND |
| Total expenses (R647, R646, R645, R649, R648, R650; L971) | 168.62 | 196.65 | 229.64 | 339.12 | 426.29 | 701.61 | ND |
| Profit before tax (R653, R652, R651, R655, R654, R656; L972) | 44.29 | 20.25 | 44.56 | 84.00 | 64.81 | 179.78 | ND |
| Tax expense (R671, R670, R669, R673, R672, R674; L976) | 11.37 | 4.09 | 11.43 | 20.67 | 15.52 | 45.00 | ND |
| PAT (R677, R676, R675, R679, R678, R680; L977) | 32.92 | 16.16 | 33.13 | 63.33 | 49.29 | 134.78 | ND |
| EPS basic = diluted, Rs (R714, R713, R712, R716, R715, R717; L988) | 5.22 | 2.56 | 5.26 | 10.05 | 7.82 | 21.39 | ND |
| EPS share-adjusted, Rs | 5.22 | 2.56 | 5.26 | 10.05 | 7.82 | 21.39 | ND |

Standalone has no exceptional line: the FY26 write-offs sat in subsidiaries.

| Derived (standalone) | Q2 FY26 | Q1 FY27 | Q2 FY27 | H1 FY26 | H1 FY27 | FY26 |
|---|---|---|---|---|---|---|
| Gross margin | 29.34% | 23.32% | 30.98% | 28.59% | 27.64% | 29.71% |
| Operating EBITDA (PBT + D + FC - OI) | 15.61 | 5.57 | 30.81 | 31.75 | 36.38 | 83.94 |
| Operating EBITDA margin | 8.66% | 2.81% | 12.02% | 8.75% | 8.01% | 10.90% |
| Reported EBITDA (PBT + D + FC) | 48.25 | 24.54 | 48.68 | 91.88 | 73.22 | 195.46 |
| Core PBT (ex-OI) | 11.65 | 1.28 | 26.69 | 23.87 | 27.97 | 68.26 |
| Other income / PBT | 73.70% | 93.68% | 40.10% | 71.58% | 56.84% | 62.03% |
| Effective tax rate | 25.67% | 20.20% | 25.65% | 24.61% | 23.95% | 25.03% |
| PAT margin | 18.26% | 8.16% | 12.92% | 17.45% | 10.85% | 17.51% |

### 1C. STANDALONE-VS-CONSOLIDATED GAP (first-class metric; A3 F2)

| Metric | Q2 FY26 | Q1 FY27 | Q2 FY27 | H1 FY26 | H1 FY27 | FY26 |
|---|---|---|---|---|---|---|
| Standalone PAT (R677, R676, R675, R679, R678, R680) | 32.92 | 16.16 | 33.13 | 63.33 | 49.29 | 134.78 |
| Consolidated PAT (R141, R140, R139, R143, R142, R144) | (18.83) | 68.55 | 82.55 | 39.95 | 151.10 | 256.94 |
| Subsidiaries and eliminations (C - S) | (51.75) | 52.39 | 49.42 | (23.38) | 101.81 | 122.16 |
| S-vs-C PAT gap, % of standalone PAT | (157.2%) n.m. (exceptional in subs) | 324.2% | 149.2% | (36.9%) n.m. | 206.6% | 90.6% |
| Standalone share of group PAT | n.m. | 23.6% | 40.1% | n.m. | 32.6% | 52.5% |
| Standalone Op EBITDA | 15.61 | 5.57 | 30.81 | 31.75 | 36.38 | 83.94 |
| Ex-parent Op EBITDA (consol - standalone) | 120.34 | 99.91 | 84.21 | 215.86 | 184.12 | 453.31 |
| Ex-parent revenue (consol - standalone) | 939.15 | 953.58 | 923.34 | 1,807.26 | 1,876.92 | 3,638.34 |
| Ex-parent Op EBITDA margin | 12.81% | 10.48% | 9.12% | 11.94% | 9.81% | 12.46% |

The gap swung from 324.2% to 149.2% of standalone PAT QoQ, far above the 5 pp trigger. The QoQ EBITDA gain of +9.54 came wholly from the parent (5.57 to 30.81, +25.24). Everything outside the parent fell -15.70 and lost 136 bps of margin (F2-01). At PAT level the 24 component-audited subs nearly tripled pre-consolidation PAT (24.19 to 65.43; R028) while the overseas segment result fell 24.8% and the consolidation residual swung from +28.18 to -15.80 (F2-02, F4-02). NCI share halved (5.94 to 2.98). [INFERENCE: intra-group dividends inside the subs, eliminated on consolidation, would explain both the sub PAT jump and the negative residual; profit shifting is the other reading. The filing does not separate them.]

Checkpoint: complete extraction tables; every cell filled or ND.

---

## STEP 2: Q2 YoY COMPARISON (Q2 FY27 vs Q2 FY26), CONSOLIDATED

| Metric | Q2 FY26 | Q2 FY27 | YoY change | Verdict |
|---|---|---|---|---|
| Revenue from operations | 1,119.42 | 1,179.67 | +60.25, +5.38% | GROWTH, modest; H1 +7.41% (2,170.25 to 2,331.18) |
| Gross profit | 247.10 | 263.95 | +16.85, +6.82% | Slightly ahead of revenue |
| Gross margin (pp) | 22.07% | 22.38% | +30 bps | FLAT to slightly up |
| Operating EBITDA | 135.95 | 115.02 | -20.93, -15.40% | NEGATIVE |
| Operating EBITDA margin (pp) | 12.14% | 9.75% | -239 bps | NEGATIVE |
| Mgmt Adjusted EBITDA | 133.25 | 118.42 | -14.83, -11.13% | NEGATIVE |
| Mgmt Adjusted EBITDA margin (pp) | 11.9% | 10.0% (10.04%) | -186 bps (11.90% to 10.04%) | NEGATIVE |
| Depreciation | 22.87 | 23.84 | +0.97, +4.24% | In line with revenue |
| Finance costs | 2.37 | 2.46 | +0.09, +3.80% | Negligible; debt nil both dates |
| EBIT (operating) = segment result | 113.08 | 91.18 | -21.90, -19.37% | NEGATIVE (ties R314, R312) |
| Other income | 27.16 | 12.21 | -14.95, -55.04% | Q2 FY26 held a 17.72 FX gain (note C5) |
| Core operating PBT (PBT pre-exc - OI) | 110.71 | 88.72 | -21.99, -19.86% | NEGATIVE: the cleanest test fails |
| Reported PBT | 2.00 | 100.93 | +98.93, n.m. | Base effect of the 135.87 exceptional |
| PBT before exceptional | 137.87 | 100.93 | -36.94, -26.79% | NEGATIVE |
| PAT | (18.83) | 82.55 | +101.38, n.m. | Base effect |
| Normalised PAT (deck Adjusted PAT) | 100.36 | 82.55 | -17.81, -17.75% | NEGATIVE |
| EPS (share-adjusted), Rs | (3.37) | 12.63 | n.m. | Base effect |

Diagnostic answers:
1. Revenue grew 5.38% YoY (Q2 FY26 1,119.42 to Q2 FY27 1,179.67). Management gave no guidance number in any Q2 document; the release only says "in line with our guidance" (pR040, L94; FN09). The Q1 concall recorded the FY27 5-9% guide as neither reaffirmed nor withdrawn (N-L534). Against the Notion base FY27E Rs 4,958 Cr (+12.5% on FY26 4,408.21), Q2 at +5.38% and H1 at +7.41% run below base.
2. Operating EBITDA margin contracted YoY: Q2 FY27 9.75% vs Q2 FY26 12.14% = -239 bps. Management Adjusted: 10.04% vs 11.90% = -186 bps.
3. Core operating PBT (ex-OI, pre-exceptional) fell 19.86% YoY (110.71 to 88.72). Reported PBT and PAT "grew" only because Q2 FY26 carried the 135.87 exceptional. The headline growth is not real; normalised PAT fell 17.75%.
4. Gap drivers, reported PAT +101.38: operating EBITDA -20.93, D&A -0.97, finance cost -0.09, other income -14.95, exceptional base effect +135.87, tax +2.45 (Step 4). Normalised: the YoY fall in normalised PAT (-17.81) is smaller than the core PBT fall (-21.99) because ETR fell from 27.21% (normalised Q2 FY26) to 18.21%; at 27.21% Q2 FY27 tax would be 27.46, so 9.08 of Q2 FY27 PAT is ETR (derived).
5. D&A (+4.24%) and finance costs (+3.80%) scaled below revenue (+5.38%). No absorption deficit.
6. Other income concentration fell: OI/PBT pre-exceptional 19.70% to 12.10%. No treasury spike masks the quarter. Note C5: Q2 FY26 OI was 65% FX gain (17.72 of 27.16).

Employee cost +26.72% YoY (71.66 to 90.81) and other expenses +47.18% (39.49 to 58.12) outran gross profit (+16.85 vs +37.78 of opex growth). Other expenses include the Masivian professional fees (6.90 in Q2) and "higher legal and professional fees" (dR216).

## STEP 3: SEQUENTIAL QoQ TRAJECTORY

| Quarter | Revenue (Rs Cr) | Op EBITDA margin | Core PBT ex-OI (pre-exc) | One-offs flagged | QoQ run-rate |
|---|---|---|---|---|---|
| Q1 FY26 | 1,050.83 (prior review L64) | 8.94% (prior review L47) | 65.60 (prior L51) | FX loss 24.73 in opex (prior L80); Adj 11.0% | base |
| Q2 FY26 | 1,119.42 (R051) | 12.14% | 110.71 | Exceptional (135.87); FX gain 17.72 in OI (R581) | +6.53% |
| Q3 FY26 | 1,107 (Notion, rounded; N-L59) | 13.86% (derived: Op EBITDA 153.41 = H2 FY26 289.64 - Q4 136.23; on rounded revenue) | 129.33 (derived: H2 240.75 - Q4 111.42) | Meta pricing dilution noted in Notion (N-L163); GM 24.5% (N-L147) | -1.1% |
| Q4 FY26 | 1,131 (derived: H2 FY26 2,237.96 = R054 - R053, less rounded Q3 1,107; +/-0.5) | 12.05% (prior L47) | 111.42 (prior L51) | ETR 17.84%; Adj 11.9% | +2.2% |
| Q1 FY27 | 1,151.51 (R050) | 9.16% | 80.41 | Capital-advance allowance 4.90 (dR260); Masivian 1.36 (dR263); sub dividend 4.22 in standalone | +1.8% |
| Q2 FY27 | 1,179.67 (R049) | 9.75% | 88.72 | Masivian 6.90 (dR262); Heltar ~2 months (C6); ETR 18.21% | +2.45% |

Diagnostics:
- Trajectory: revenue is a slow climb (+1.8%, +2.45% the last two quarters) with QoQ growth wholly from new products. Margin is RECOVERING off the Q1 trough (9.16% to 9.75%), still 239 bps below the year-ago quarter and about 410 bps below Q3 FY26.
- One-off distortions: Q2 FY26 (exceptional, FX gain) and Q1 FY26 (FX loss). Q2 FY27 holds no exceptional; its add-back (Masivian 6.90) is in the Adjusted figure only.
- Q2 vs H1 average: H1 FY27 average revenue 1,165.59 and Op EBITDA 110.25; Q2 sits above both (1,179.67; 115.02). No capex commissioning thesis applies (PPE 32.32, CWIP 6.02; R396, R398).
- Implied Q3 FY27 base to hold trajectory: revenue >=1,179.67 and Op EBITDA margin >=9.75%. To clear 10.0% on the reported basis at flat revenue, Op EBITDA must reach 117.97, +2.95 vs Q2 (derived; F2-01).

## STEP 4: OPERATIONAL DECOMPOSITION (PAT BRIDGE)

### 4A. YoY bridge, Q2 FY26 PAT (18.83) to Q2 FY27 PAT 82.55 (+101.38)

| Component | YoY change (Rs Cr) | Share of reported change | Recurring? |
|---|---|---|---|
| Revenue contribution to gross profit (60.25 x 22.07%) | +13.30 | +13.1% | Recurring |
| Gross margin change contribution (1,179.67 x +0.30 pp) | +3.55 | +3.5% | Recurring |
| Employee cost change (71.66 to 90.81) | -19.15 | -18.9% | Recurring |
| Other expenses change (39.49 to 58.12; incl. Masivian 6.90) | -18.63 | -18.4% | Mostly recurring; 6.90 claimed one-off |
| = Operating EBITDA change | -20.93 | -20.6% | Recurring |
| D&A change | -0.97 | -1.0% | Recurring |
| Finance cost change | -0.09 | -0.1% | Recurring |
| Other income change (incl. Q2 FY26 FX gain 17.72) | -14.95 | -14.7% | NON-RECURRING (FX) |
| Effective tax change (20.83 to 18.38) | +2.45 | +2.4% | Mixed |
| Exceptional items (base effect) | +135.87 | +134.0% | NON-RECURRING |
| Reported PAT YoY change | +101.38 | 100% | |

Ties: 13.30 + 3.55 - 19.15 - 18.63 - 0.97 - 0.09 - 14.95 + 2.45 + 135.87 = 101.38.

### 4B. QoQ bridge, Q1 FY27 PAT 68.55 to Q2 FY27 PAT 82.55 (+14.00)

| Component | QoQ change (Rs Cr) | Share | Recurring? |
|---|---|---|---|
| Revenue contribution to GP (28.16 x 20.88%) | +5.88 | +42.0% | Recurring |
| GM change contribution (1,179.67 x +1.50 pp) | +17.63 | +125.9% | Recurring if routing gains hold (A3-23) |
| Employee cost change (77.62 to 90.81) | -13.19 | -94.2% | Recurring |
| Other expenses change (57.34 to 58.12) | -0.78 | -5.6% | Recurring |
| = Operating EBITDA change | +9.54 | +68.1% | Recurring |
| D&A change | -0.13 | -0.9% | Recurring |
| Finance cost change (1.36 to 2.46) | -1.10 | -7.9% | Recurring (lease, deferred consideration unwind; F1-02) |
| Other income change | +1.15 | +8.2% | Non-recurring |
| Tax change (22.92 to 18.38), of which ETR effect 6.91 | +4.54 | +32.4% | NON-RECURRING until shown otherwise |
| Reported PAT QoQ change | +14.00 | 100% | |

Mandatory answers:
- Recurring vs non-recurring, YoY: the recurring operating line (EBITDA, D&A, FC) fell -21.99. The whole reported increase is the exceptional base effect (+135.87), partly offset by lost FX income (-14.95). Recurring core operations contributed a negative share.
- If other income reverts to the prior-year level: Q2 FY26 OI held a 17.72 FX gain; ex-FX OI was 9.44 vs Q2 FY27 11.19 ex-FX (12.21 - 1.02). On an ex-FX basis Q2 FY27 PAT is about flat YoY: deck ex-forex Adjusted PAT 826.0 mn to 815.3 mn, -1.3% (A3-10). That flat result rests on the ETR drop.
- D&A and finance cost: at steady state. D&A 23.71 to 23.84; finance cost 2.46 is lease interest plus a new amortised-cost unwind (0.14 H1; R490) on the Heltar deferred leg (F1-02, F6-02).
- Tax: deferred-tax credits in every period: (3.24) Q2, (4.74) Q1, (19.55) FY26 (R127-R132). Shield 321 bps in Q2 (F8-01). ETR fell 685 bps QoQ to 18.21% although profit mix moved toward the parent (standalone ETR 25.65%); implied ETR outside the parent fell from 26.44% to 12.33% (F8-02). About 6.91 of the +14.00 QoQ PAT gain (49%) is the lower ETR (FN04). No "earlier years" tax line is printed.

---

## STEP 5: CASH QUALITY AND BALANCE SHEET (H1 FY27 vs H1 FY26; balance sheet 30.09.2026 vs 31.03.2026)

| Metric (anchor) | Prior period | Current period | Change | Verdict |
|---|---|---|---|---|
| CFO, consolidated (R525, R524; L733) | 202.88 (H1 FY26) | 33.34 (H1 FY27) | -169.54, -83.6% | RED direction |
| CFO / PAT, consolidated | 5.08x reported; 1.27x on normalised PAT 159.13 (H1 FY26) | 0.22x (33.34 / 151.10) | down | Below the lowest Pillar 2 band (0.65x) on a single-half reading |
| CFO / Op EBITDA (deck "Reported CFO/EBITDA", dR311) | ND | 15% (on Adj EBITDA) | n/a | Management's FY27 promise was 75-100% (N-L548) |
| Mgmt "Adjusted CFO" (adds back vendor advance 116.83; dR312-dR315) | ND | 150.17; 66% of Adj EBITDA; 0.99x PAT | n/a | Non-GAAP, new this quarter (A3-19) |
| CFO, standalone (R845, R844; L1127) | (209.17) | (126.69) | +82.48 | NEGATIVE both halves |
| Capex, PPE + intangibles incl CWIP/IAUD (R527, R526; L735) | 7.25 | 20.18 | +12.93 | Small |
| FCF (CFO - capex) | 195.63 | 13.16 | -182.47 | Weak |
| FCF after acquisition (less Heltar 23.88, R530) | 187.31 (less 8.32, R531) | (10.72) | -198.03 | Negative |
| Working-capital change (sum of R514, R516, R518 / R515, R517, R519) | +13.17 | (157.34) | -170.51 | RED: other assets +161.33 drives it |
| of which (increase) in financial and other assets (R516-R517; L729) | +231.01 | (161.33) | -392.34 | Vendor advance 116.83 inside (dR312) |
| of which trade receivables (R514-R515) | (44.06) | (45.69) | -1.63 | Neutral |
| of which payables, provisions, other liabilities (R518-R519) | (173.78) | +49.68 | +223.46 | Positive |
| Receivable days, consolidated (R421, R420) | 75.30 (909.40 on FY26 revenue) | 74.13 (946.93 on H1 x2); 73.25 on Q2 x4; deck 72 (dR327) | -1.2 | GREEN (<=115) |
| Receivable days, standalone (R753, R752) | 114.43 (241.36 on FY26) | 139.28 on Q2 x4; 157.19 on H1 x2 | +24.9 to +42.8 | RED direction (F2-03) |
| Inventory days | ND (no inventory) | ND | ND | n/a |
| Payable days, consolidated (R459+R461, R458+R460 on messaging cost) | 53.32 (496.80) | 51.46 (515.12 on H1 x2); deck 64 to 50 (dR326, dR328) | -1.9 (deck -14) | Suppliers paid faster (A3-19) |
| Cash conversion cycle (DSO - DPO) | 21.98 (deck 12) | 22.67 (deck 22) | +0.7 (deck +10) | Lengthening on the deck basis |
| Other current assets, consolidated (R429, R428; L659) | 203.50 | 364.23 | +160.73, +79.0% | RED: standalone only +18.52 (R763, R762), so ~142.21 in subs (F1-01) |
| PPE (R397, R396) | 30.40 | 32.32 | +1.92 | n/a |
| CWIP (R399, R398) | 1.53 | 6.02 | +4.49 | Small |
| Goodwill (R403, R402) | 545.68 | 573.85 | +28.17 | Heltar and FX, not separable (F6-02) |
| Cash + other bank balances (R423+R425, R422+R424) | 1,388.67 | 1,340.08 | -48.59 | GREEN |
| Borrowings (R455, R454) | nil | nil | nil | Debt-free |
| Lease liabilities (R445+R457, R444+R456) | 41.98 | 39.32 | -2.66 | n/a |
| Net debt / (net cash), ex-leases | (1,388.67) | (1,340.08) | +48.59 | GREEN (>=Rs 800 Cr) |
| Net debt / (net cash), after leases | (1,346.69) | (1,300.76) | +45.93 | GREEN |
| of which earmarked: unutilised IPO in deposits (R577) | 65.00 | 65.00 | nil | Not free cash (F6-01) |
| Deck "Cash" (dR021) | ND (Q1 deck "Net Cash" 1,345.2, prior review L100) | 1,355.6 (13,556 mn) | n/a | Label changed from "Net Cash" (A3-16); does not tie to 1,340.08 or 1,357.56 incl. current investments 17.48 |
| Promoter pledge | ND | ND | ND | Not in filing |

Mandatory answers:
- Pillar 2 cash multiplier (on file 1.10x, N-L588): H1 FY27 CFO/PAT 0.22x sits below the 0.65x band. A single half cannot set the band; trailing 4Q CFO/PAT is ND because H2 FY26 CFO is not in the inputs. PILLAR-RELEVANT FLAG; recompute deferred to /fttcp and Role 1 (OR-30).
- Structural or growth-induced: neither proven. Revenue grew only 7.41% in H1, so growth does not explain a 161.33 rise in other assets. The cause is a 116.83 vendor prepayment for "services which will be availed in the subsequent period" (deck L834) plus a standalone receivable build of 149.89 (R834; F2-03). The prepayment is the same asset class as the FY26 write-offs of 107.96 and 27.91 (C7a, C7b) and the Q1 capital-advance allowance 4.90 (dR260). "If the company stopped growing tomorrow" the prepayment would still be there until consumed. Classification: INDETERMINATE-WITH-DIRECTION (negative). Missing evidence named: (1) H2 FY27 consumption of the 116.83 advance; (2) counterparty, security and contract terms of the advance; (3) collection of the standalone receivable build; (4) H2 FY26 CFO to compute trailing-4Q CFO/PAT. Per house rule this caps the cash axis at PROCEED WITH CAVEATS; with the other flags the verdict is PROCEED WITH FLAGS.
- CWIP capitalisation: no major project; CWIP rose 4.49 to 6.02; IAUD 6.24 to 12.90 (R407, R406).
- Net debt within range: yes; net cash 1,340.08 vs Notion base FY27E 1,250 (N-L98). Dividends paid H1 40.63 consolidated (R542). Second interim Rs 4 adds about 25.20 in Q3 (F13-03).

Receivable cash-flow vs balance gap (A3-13): deck receivables moved +37.5 Cr (9,094 to 9,469 mn) while the cash-flow line shows +45.69 Cr; about 8.2 Cr left the balance without collection (write-off 2.81, R480, plus ECL 4.97, R486, explain 7.78 of it; derived). FX translation may explain the rest.

---

## STEP 5.5: DOWNSTREAM SIGNAL RECONCILIATION

### 5.5A. Tracker pull
Tracker rows not supplied. The orchestrator passed no Downstream Signal Tracker rows for ROUTE, so the signal table cannot be filled.

| Signal name | Type | Cadence | Latest observation | Direction | Thesis element | Health |
|---|---|---|---|---|---|---|
| ND (tracker rows not supplied) | ND | ND | ND | ND | ND | ND |

Fewer than three signals are available to this review. The three-signal floor (OR-17) cannot be tested here; flag for the operator and for /fttcp Role 5.5.

### 5.5B. Target vs signals
Target reported: MIXED (revenue +5.38% YoY; core PBT -19.86% YoY; margin recovering QoQ). Signals: ND. No four-outcome cell can be assigned.

### 5.5C. New signals
No new external downstream signal surfaced this quarter. Candidates considered and rejected as tracker signals because they have no external observable: Heltar revenue (company KPI); the unnamed prepaid messaging vendor (no public counterparty); the MOA object expansion (a governance event, tracked as a monitorable). Payload only; nothing written (write gate is operator-approved per the run rules).

### 5.5D. Forward view weighting
With no signal rows, Step 6 relies on the single-quarter print. Weight the Q2 margin reading as one data point; do not extrapolate the +59 bps QoQ recovery.

---

## STEP 6: RECONCILIATION VS THESIS

### 6A. Variance vs Notion projections (FY27E pro-rated to H1 where annual; derived)

| Metric | Bear proj | Base proj | Bull proj | Actual | Lands in |
|---|---|---|---|---|---|
| Revenue, H1 vs half of FY27E (N-L68) | 2,324 (4,648 / 2) | 2,479 (4,958 / 2) | 2,612 (5,224 / 2) | 2,331.18 H1 (R052); Q2 x4 = 4,718.68 | Between Bear and Base (0.3% above bear) |
| EBITDA margin (N-L87; N-L78; N-L126) | FY27 bear ND (FY29 bear 11%; Realistic Bear 8.5%) | 12.5% | FY27 bull ND (FY29 17%) | Adj 9.8% H1 / 10.04% Q2; reported 9.46% H1 / 9.75% Q2 | Below Base; below the FY29 bear path (11%); above Realistic Bear (8.5%) |
| PAT, H1 vs half of FY27E (N-L94) | ND | 197 (394 / 2) | ND | 151.10 (R142) | Below Base (-23.3%); bear ND |
| EPS, H1 vs half of FY27E (N-L95) | ND | 31.3 (62.6 / 2) | ND | 22.57 (R261) | Below Base (-27.9%); bear ND |
| Net debt / (net cash) (N-L98) | ND | (1,250) | ND | (1,340.08) | At or above Base |
| ROCE (N-L99) | ND | ~14% | ND | 13.04% (derived: EBIT H1 196.22 x2 / capital employed 3,010.04 = equity 2,970.72 + leases 39.32); 23.50% ex-cash | Slightly below Base |

Read: revenue sits between bear and base; margin, PAT and EPS sit below base with no FY27 bear figure on file; net cash sits above base. Not "below bear on 2+ key metrics" (bear FY27 margin, PAT and EPS are not stated; on the FY29 bear margin of 11% only margin lands below). Probability re-weighting rule: NOT triggered (needs below bear on 2+ metrics for 2 consecutive quarters). Flag: the Notion page carries no FY27 bear margin, PAT or EPS, so this test is weak; /fttcp should fill them.

### 6B. Watchlist item status (all 16)

| # | Watchlist item | Green | Red | Q2 FY27 reading | Status |
|---|---|---|---|---|---|
| 1 | Gross margin (consol) | >=24% for 2Q | <22% for 2 consecutive Q | 22.38% (Q1 20.88%); deck 22.4% (dR178) | AMBER. Red leg resets (Q2 >=22%). Cap-5% gate (23%) still FAILS. |
| 2 | EBITDA margin (Adjusted) | >=13% sustained | <10% for 2 consecutive Q = THESIS BROKEN | Adj 10.0% printed / 10.04% computed (dR268); reported 9.75%; ex-Masivian 9.45% | AMBER, basis-dependent. See 6C. |
| 3 | CFO/PAT trailing 4Q | >=1.0x | <0.5x for 2Q | H1 FY27 0.22x (R524 / R142); trailing 4Q ND | UNKNOWN on the defined metric; H1 reading in red territory. Lean AMBER-RED. |
| 4 | DSO | <=115 days | >130 days | Consolidated 73-74 days; standalone 139-157 days | GREEN (consolidated). Standalone flag (F2-03). |
| 5 | New products revenue YoY | >=15% | <5% for 2Q | +36.7% YoY, +35.8% QoQ (dR099, dR100); share 10.88% | GREEN. Heltar share not separated (A3-22). |
| 6 | Top 10 concentration; single customer >18% red | <=45% | >55%; single customer >18% | Top 10 42% H1 annualised (dR143); single customer ND | GREEN on Top 10; single-customer UNKNOWN. |
| 7 | Loss of large enterprise clients | zero major losses | 2+ digital natives lost in 12m | >$5mn cohort 21 to 19; top 5 33% to 30%; Q1 large-account recovery not updated (A3-25) | AMBER |
| 8 | Proximus cross-sell revenue | Rs 50+ Cr/qtr by FY28 | COGS-only through FY27 | Not disclosed in any Q2 document (A3-26) | UNKNOWN. Strategic Premium expiry condition triggers (6D, Step 7 flag). |
| 9 | Rs 113 Cr arbitration | settlement / status quo | adverse / impairment >Rs 50 Cr | Settled 19 Feb 2026; note 7a verbatim unchanged (R1101) | GREEN (closed) |
| 10 | Cash position | >=Rs 800 Cr net cash | <Rs 500 Cr without M&A | Net cash 1,340.08 (1,300.76 after leases); Rs 65 Cr earmarked | GREEN |
| 11 | Promoter (Proximus) holding | ~75% | <70% | Not in filing; no delisting or open-offer note in any Q2 document | UNKNOWN |
| 12 | CEO continuity | stable | departures + pivot | CEO Agnihotri and Chairman Arikan quoted (pR046-pR047); MD Gupta signs in Brussels (R1047); Masiv CEO change at subsidiary (dR061) | GREEN |
| 13 | Truecaller BM revenue KPI | disclosed by Q2 FY27, Rs 15+ Cr/qtr | 3 quarters silent | Absent from deck and release (A3-24, FN13); concall content unknown | RED on the Notion counter (AR moved it to 2 of 3; Q2 silence is the 3rd); AMBER on a strict quarter count (Q1, Q2 = 2 of 3). Green deadline missed. Operator to rule the counter. |
| 14 | Heltar integration | consideration at closure; Rs 5+ Cr/qtr by Q2 FY27; founders retained | founders exit / clawback dispute / impairment | Consideration disclosed (33.66; R585); revenue KPI absent; founder status absent | AMBER (definition: consideration disclosed, no revenue KPI) |
| 15 | FY27 M&A pace | <Rs 300 Cr aggregate | >Rs 500 Cr on 3+ deals in 12m | Rs 33.66 Cr, one deal | GREEN |
| 16 | Salesforce AgentExchange revenue | >=Rs 5 Cr/qtr by Q4 FY27 | silent 4 quarters | App launched Aug 2026 (dR065-dR066); no revenue | AMBER; silence 1 of 4 |

### 6C. Thesis-broken trigger check

Basis of condition 1, from the Notion text:
- One-line thesis: "Thesis breaks if EBITDA margin falls below 10% for 2 consecutive quarters" (N-L21). Basis not named.
- Recommendation box: "1. EBITDA margin <10% for 2 consecutive Q" (N-L203). Basis not named.
- Section 8 checklist row 2: "EBITDA Margin (Adjusted) | Quarterly Investor Presentation | ... | <10% for 2 consecutive quarters → THESIS BROKEN" (N-L227). ADJUSTED, deck-sourced.
- RDE pre-defined exit criteria: "EBITDA margin <10% for 2 consecutive quarters | Exit 50% immediately" (N-L264). Basis not named.
- Key Notes, 11-Aug-2026 and 02-Sep-2026: "consolidated Adjusted EBITDA margin (bull >= 10% retires Trigger 1; bear < 10% second consecutive fires Trigger 1 = mandatory 50% exit)" (N-L11). ADJUSTED.
- Early-warning table: "EBITDA margin <10% for any quarter | ... | EXIT 50%; await second quarter" (N-L254). Basis not named.

Finding: every row that names a basis names the management Adjusted figure from the investor presentation. The original thesis line, the recommendation box and the exit criteria name no basis. The text leans Adjusted but does not fully settle it. Both readings are shown. The operator rules.

| Thesis-broken condition | Threshold | Current reading | FIRED? |
|---|---|---|---|
| 1. EBITDA margin <10% for 2 consecutive quarters, ADJUSTED basis (checklist row 2, Key Notes) | Adj <10.0% in Q1 AND Q2 FY27 | Q1 9.5% (dR269); Q2 10.0% printed, 10.04% computed (1,184.2 / 11,796.7 mn; dR266). Headroom Rs 0.45 Cr. | NOT FIRED. Count resets to 0 of 2. Fragile: the 10% clears only because Rs 6.90 Cr of Masivian "data breach" fees is added back a second quarter (15x the headroom; A3-18). |
| 1. Same condition, REPORTED basis (PBT + D + FC - OI; also the deck's own "EBITDA" line, dR250) | Reported <10.0% in Q1 AND Q2 FY27 | Q1 9.16%; Q2 9.75% | FIRED on this basis (2 of 2). |
| 1. Same condition, Adjusted ex-Masivian add-back (bear reading of the add-back) | <10.0% Q1 and Q2 | Q1 9.34%; Q2 9.45% | FIRED on this basis (2 of 2). |
| 2. Proximus announces strategic review or sale | any announcement | None in any Q2 document. Parent-integration signs only: MOA objects expand to AI, digital identity, cloud (F13-01); statements signed in Brussels (F13-02); release adds "a Proximus Global company" (FN15). | NOT FIRED |
| 3. Loss of 3+ digital-native clients in 12 months | 3+ | Not disclosed. Digital native share 12% of H1 revenue (dR109); >$5mn cohort 21 to 19 (dR135-dR136). | NOT FIRED (ND; watch) |
| 4. ROCE <8% sustained for 2 quarters | <8% 2Q | H1 annualised 13.04% on equity + leases (derived); 23.50% ex-cash | NOT FIRED |
| 5. Arbitration loss >Rs 100 Cr + second similar dispute | both legs | FY26 note 7a wrote off Rs 107.96 Cr after "arbitration developments" and settlement (R589, R1101); 7b wrote off Rs 27.91 Cr on recoverability, not a dispute (R1102). Prior reviews closed item 9 GREEN (N-L373). No new dispute in Q2. | NOT FIRED as recorded. Flag: the Q1 6C table listed only 4 conditions; the FY26 write-off sits above the first leg's Rs 100 Cr line. Under the forward-application ruling the closed record stands; the operator may wish to confirm. |

Pre-committed discipline: if the operator rules the REPORTED basis, condition 1 has FIRED and the pre-committed action is "Exit 50% immediately" (N-L264). On the ADJUSTED basis, nothing has fired. This review does not change the Decision Status. You flag; the operator decides.

Related Notion conflict for the operator: the early-warning row "EBITDA margin <10% for any quarter → EXIT 50%; await second quarter" (N-L254) was live at Q1 (Adj 9.5%) and the Q1 record did not apply it. It conflicts with the two-quarter exit rule (N-L264). Operator ruling needed on which governs.

### 6D. Growth trigger status

| Trigger | Original confidence | Confirming evidence | Killing evidence | Updated status |
|---|---|---|---|---|
| 1. Margin expansion via client mix | HIGH (N-L147) | GM 22.38%, +150 bps QoQ; GP per transaction +5.7% QoQ; new-products share 10.88% | GM still below 23% gate and far below the 25% confirm line; management band 21.5-23% (N-L533) sits below the destination; driver now "enhanced routing strategy" (dR182), which can reverse (A3-23); EBITDA 9.75% vs 13% confirm | WEAKENED (FTTCP T2 STALLED stands) |
| 2. Proximus cross-sell synergies | MEDIUM (N-L155) | Proximus Global named as a Heltar sales channel (dR091, dR094) | No Proximus revenue KPI in any Q2 document (A3-26); Europe-HQ customer revenue fell QoQ by about Rs 17.8-64.2 Cr (A3-20); CCGA award re-credited from Route's Konera to Proximus Global (A3-21) | DELAYED, at risk of WEAKENED. Strategic Premium expiry condition met on filed evidence. |
| 3. New products (WhatsApp/RCS/voice/email) | MEDIUM (N-L163) | +36.7% YoY, +35.8% QoQ (dR099-dR100); 2,400+ clients vs 2,100+ | Heltar inorganic share not separated; RCS slide dropped (A3-21); revenue excluding new products fell 0.54% QoQ (derived) | ON TRACK (organic rate unverified) |
| 4. Network APIs / Konera | LOW (N-L171) | none in Q2 | Konera absent from the Q2 deck; award now credited to Proximus Global (A3-21) | WEAKENED |

Checkpoint: 6A-6D presented.

---

## STEP 6.5: EXPECTATION LEDGER REVIEW AND A21 BASE REFRESH
Deferred to /fttcp and Role 1 (operator ruling OR-30). No expectation-ledger rows were passed to this run.
Pillar-relevant facts for the refresh (no base computed here):
- Q2 FY27 PAT 82.55 (R139); owners' PAT 79.57 (R197); EPS 12.63 (R258). Known one-offs in Q2: Masivian 6.90 opex (claimed non-recurring); ETR 18.21% vs statutory 25.17% (shield 7.02 at statutory; FN04); deferred-tax credit 3.24 (R127); about two months of Heltar.
- The seasonal/lumpy test: Q1 FY27 carried a capital-advance allowance and a Q1 FX swing; a trailing-4Q base needs Q3 and Q4 FY26 PAT (Q4 FY26 114.43 per prior review; Q3 FY26 ND in inputs).
- Expectation items with Q2 FY27 confirm-by dates on file: Strategic Premium Proximus KPI (MISSED on filed evidence); Truecaller BM Rs 15+ Cr/qtr (MISSED); Heltar Rs 5+ Cr/qtr (MISSED, no KPI). Ageing (decay, retire) is for /fttcp.

## STEP 7: FOUR-PILLAR DESTINATION PE RE-VALIDATION
Deferred to /fttcp and Role 1 (operator ruling OR-30). Pillar-relevant facts flagged:

| Pillar / input | On file | This quarter's fact | Flag |
|---|---|---|---|
| ROCE base | 12.0x (12% smoothed; N-L587) | H1 annualised ROCE 13.04% (equity + leases) / 23.50% ex-cash (derived); FTTCP verdict governs | PILLAR-RELEVANT |
| Cash multiplier | 1.10x (N-L588) | H1 CFO/PAT 0.22x reported; 0.99x on management's Adjusted CFO; trailing 4Q ND | PILLAR-RELEVANT, adverse direction |
| Growth premium | +3.5x (N-L590) | Revenue +5.38% YoY / H1 +7.41%; GM 22.38%; new products +36.7%; EBITDA margin -239 bps YoY | PILLAR-RELEVANT |
| Strategic premium | +1.25x with Q2 FY27 expiry (N-L591) | No Proximus revenue-synergy KPI in results, deck or release; concall content unknown (no transcript) | PILLAR-RELEVANT: expiry condition says drop to +1.0x. Recompute deferred. Reopen if a transcript later shows a KPI. |
| UA multiplier | not on file in the extract | n/a | n/a |
| Sector cap | 22x (N-L593) | No sector reclassification; MOA object expansion into AI and digital identity is a watch item | Hold |
| Hurdle ratio | 2.53 PASS at 13.9x current PE (N-L596) | Market reference only: trailing PE 7.85 at CMP Rs 435 (screener, 28-Oct-2026); not a valuation input | Recheck at /fttcp |

---

## STEP 8: POSITION DECISION (BRANCH 8A, HELD; flags only, the operator decides)

Decision Status verified: HELD, 4%, average cost Rs 509 (N-L11).

8A logic walk:
1. Thesis-broken condition FIRED? Basis-dependent. Adjusted basis (the only basis the Notion text names): NOT FIRED. Reported basis: FIRED, pre-committed action "Exit 50% immediately". FLAG F-1 to the operator for a ruling before any other step.
2. Momentum bucket? No; value position.
3. Below bear on 2+ key metrics? No (6A).
4. Between bear and base? Yes on revenue; below base on margin, PAT and EPS. Action on this leg: HOLD the existing 4%; tighten add-back triggers; revise Notion projections down (FY27E base revenue 4,958 and margin 12.5% are not supported by H1 at 2,331.18 and 9.8% Adj).

Pre-committed price rules, checked against the market reference (context only):
- Hard floor Rs 450 (Position Size property, N-L11): CMP Rs 435 sits BELOW it. The property does not state the action at the floor. FLAG F-2.
- "Stock breaches ₹420 floor → Exit 50% regardless of narrative" (N-L268): the 52-week low is Rs 407, below Rs 420. The date of that low is not in the inputs, so whether the breach fell inside the holding period is ND. CMP Rs 435 is above Rs 420 today. FLAG F-2.
- CMP Rs 435 sits below the AR-revised MoS price Rs 463 and the entry price Rs 579 (N-L643-645). The Notion properties still show 628 / 502 (stale). FLAG.

Gates:
- Cap-5% gate (revenue YoY >=0% AND consolidated GM >=23%): revenue +5.38% PASS; GM 22.38% FAIL. Gate FAILS. No upsize.
- Add-back rule (add only if price <=Rs 510 AND Q2 Adj EBITDA margin >=10%): price Rs 435 PASS; Adj 10.04% PASS on the stated basis. Both conditions are technically met, but the add is blocked by the failed cap gate, by the open basis question on condition 1, and by the Rs 450 hard-floor reading. No add recommended until the operator rules F-1 and F-2.
- Deferred RDE 4%->3% trim: RE-PUT to the operator a third time. Reasons stack: failed GM gate; condition 1 passes only on an add-back; cash conversion 0.22x; Grade C EVASIVE; price below the hard floor.

### 8B. Add-back / trim trigger refinement
- Original add-back trigger: add only if price <=Rs 510 AND Q2 FY27 Adj EBITDA margin >=10% (N-L398).
- Revised add-back trigger (proposed for operator): add only if (a) consolidated EBITDA margin >=10% on the REPORTED basis (no add-backs) for one quarter, AND (b) the H1 vendor advance of Rs 116.83 Cr shows consumption at FY27 (other current assets falling from Rs 364.23 Cr), AND (c) the cap-5% GM gate (>=23%) passes, AND (d) price <=Rs 510 and above the hard floor as the operator defines it.
- Original trim ladder: CMP >Rs 820 trim 1%; >Rs 1,330 trim 50%; Rs 420 floor exit 50%; Rs 450 hard floor (N-L11, N-L268-271).
- Revised trim ladder: unchanged in levels. Proposed fundamental leg: if Q3 FY27 reported EBITDA margin is <10% a third consecutive quarter AND the Adjusted figure again needs a non-recurring add-back to clear 10%, treat condition 1 as fired regardless of basis. Operator to approve.

### 8C. Single cleanest metric for Q3 FY27
Consolidated EBITDA margin on the REPORTED basis (PBT before exceptional + D&A + finance cost - other income, over revenue; the deck's own "EBITDA" line).
- Bull threshold: >=10.0% (clears the line with no add-back; ends the basis dispute).
- Bear threshold: <10.0% (a third consecutive reported quarter below the line; the Adjusted figure then rests on add-backs for a third quarter).
Q3 results carry no cash flow, so the cash test (vendor-advance unwind) waits for the FY27 filing.

---

## STEP 8.5: QUESTIONS FOR MANAGEMENT

### Prior questions: answer status (filed-document basis only; no Q2 transcript)

Q1 FY27 twelve questions (N-L403-416):

| Prior Q | Status in Q2 filed documents | Note |
|---|---|---|
| 1 Margin restore: actions and quarter for Adj >11%, GM >23% | PARTIALLY ANSWERED (data) | GM 22.38%, Adj 10.04%; no dated commitment |
| 2 Large-account go-live and Rs impact | NOT ADDRESSED | Deck and release silent (A3-25, FN14) |
| 3 India loss structural or one-off | PARTIALLY ANSWERED (data) | India result back to 27.11 (R294); no explanation |
| 4 Truecaller inside New Products; target | NOT ADDRESSED | Truecaller absent (A3-24) |
| 5 Truecaller run-rate; Heltar consideration | PARTIALLY ANSWERED | Heltar 33.66 disclosed (R585); Truecaller not |
| 6 Capital-advance and Masivian one-off; total remediation | NOT ADDRESSED | Masivian fees rose to 6.90; relabelled "data breach" (A3-17) |
| 7 Hedge notional; Adj PAT forex policy | NOT ADDRESSED | Hedge reserve swung (3.80) to 3.83 (F9-01) |
| 8 Deferred-tax shield exhaustion | NOT ADDRESSED | Credit continues (F8-01) |
| 9 Rs 65 Cr IPO object; overseas liabilities | PARTIALLY ANSWERED | Variation rescinded, money re-committed to Mumbai office, no date (F6-01); overseas liabilities unexplained (F12-02) |
| 10 ESOP-lapse seniority; audit scope | PARTIALLY ANSWERED | MSKA widened component disclosure (F4-02); seniority silent |
| 11 RCS direct-operator markets and dates | NOT ADDRESSED | RCS slide dropped (A3-21) |
| 12 Goodwill impairment-testing detail | PARTIALLY ANSWERED (via FY26 AR KAM, N-L11) | No Q2 update |

Tally: 0 answered, 6 partially answered, 6 not addressed. AR-cycle questions (N-L608-614): Customer A decomposition NOT ADDRESSED; Proximus revenue KPI NOT ADDRESSED; India segment structural read PARTIAL (data); Send Clean / Call2Connect strategy NOT ADDRESSED (Call2Connect still excluded from headcount, dR348); Proximus RPT scale NOT ADDRESSED (no RPT note); ECL driver NOT ADDRESSED (ECL 4.97 H1, R486); UK sub loan schedule PARTIAL (loans to subs 281.30 to 247.23; F2-04); vendor prepayment controls NOT ADDRESSED (new 116.83 advance). Repeated non-addressing across Q1, AR and Q2 cycles is a governance signal: log in the Promoter Verdict update. Management grade C / EVASIVE stands; Role 5 cannot re-score it without a transcript.

### Priority questions (Q1 to Q8)

| # | Question | Why it matters | Bull answer | Bear answer | From finding(s) |
|---|---|---|---|---|---|
| 1 (C) | Q2 Adjusted EBITDA margin is 10.0% only after adding back Rs 6.90 Cr of Masivian "data breach" fees; without it the margin is 9.45%, reported 9.75%. What is the total remediation cost to date, the cost still to come, and will any Masivian cost be added back in Q3 FY27? | Decides the thesis-broken basis question | Total capped, last charge in Q3, no customer or regulatory claim | Open-ended cost; claims or fines possible; add-back recurs | A3-18, A3-17, FN12, F2-01 |
| 2 (D) | H1 CFO is Rs 33.34 Cr on PAT Rs 151.10 Cr (0.22x). The deck adds back a Rs 116.83 Cr vendor advance. Name the vendor type, contract tenor, security held, the amount consumed by 31 Oct 2026, and whether this vendor is linked to the Rs 4.90 Cr Q1 capital-advance allowance or the FY26 Rs 135.87 Cr write-offs. | Same asset class as the FY26 write-offs | New, secured, mostly consumed by Q3 | Same counterparty class; unsecured; prepayment demanded by supplier | F1-01, A3-02, A3-04, A3-19 |
| 3 (A) | The overseas segment result fell 24.8% QoQ to Rs 64.40 Cr (margin 6.12% from 8.06%) while overseas revenue fell only 1.1%. What caused it (pricing, an account loss, Masivian), and did the Q1 large account return to its prior run-rate: yes or no? | Overseas is 78% of gross segment revenue | Named one-off; account recovered | Structural repricing or a lost account | F12-01, A3-25, FN14, F2-01 |
| 4 (E) | Give the INR revenue in H1 FY27 from customers introduced by Proximus Global, Telesign or BICS, and state how much of the Q2 fall in Europe-HQ customer revenue relates to Proximus-group accounts. | Strategic Premium expiry condition | A number, rising, Europe drop unrelated | "Not tracked" or COGS-only | A3-26, A3-20, A3-21 |
| 5 (C) | Consolidated ETR fell to 18.21% from 25.06%; implied ETR outside the parent fell to 12.33%; deferred-tax credit Rs 3.24 Cr. What drove it, and what ETR should we use for H2 FY27 and FY28? | About 49% of QoQ PAT gain is tax; the PAT-in-line-with-EBITDA claim fails | Durable jurisdiction mix; ETR guide ~20% | Prior-year true-up or loss offset; ETR back to 25%+ | F8-01, F8-02, FN04, A3-06, A3-10 |
| 6 (D) | Standalone receivables rose Rs 149.89 Cr (+62%) to Rs 391.25 Cr; standalone DSO about 139 days; standalone CFO -Rs 126.69 Cr. How much of India revenue (Rs 302.22 Cr, +28% QoQ) is billed to the top three India accounts and to group entities, and by which date will the build collect? | Parent margin recovery has not turned into cash | Few large accounts, collected in Q3 | Group-entity billing or extended terms | F2-03, F12-03, A3-13 |
| 7 (G) | The board approved new MOA objects (AI, GenAI, ML, digital identity, cloud) and the MD signed the results in Brussels. Does the board plan to acquire or receive any business from the Proximus group in the next 12 months: yes or no? What is the shareholder-vote date? | Related-party transfer or structure change risk | No transfer planned; vote date given | Transfer under study; no date | F13-01, F13-02, FN06 |
| 8 (B) | New products revenue rose to Rs 128.4 Cr (+35.8% QoQ). How much came from Heltar since 29 Jul 2026, how many of the +300 billable clients came with Heltar, are the founders still employed, and is the Rs 9.78 Cr deferred leg an earn-out? | Organic growth rate of the main growth engine | Heltar small; organic >25%; founders stay; fixed deferral | Heltar most of the jump; earn-out; founders gone | F6-02, A3-22, FN03, FN08 |

### Coverage questions (Q9 to Q22; every remaining FORWARD-SIGNAL and AMBIGUOUS finding)

| # | Question | Bull answer | Bear answer | From finding(s) |
|---|---|---|---|---|
| 9 (F) | Why did the board rescind the 7 May 2026 IPO-proceeds variation, and by which date will the Rs 65 Cr Mumbai office purchase complete? | Property identified, date given | No date; money idle a seventh year | F6-01 |
| 10 (A) | The 24 component-audited subs report Q2 PAT Rs 65.43 Cr (Q1 Rs 24.19 Cr) while their revenue fell 14.4%; the consolidation residual swung to -Rs 15.80 Cr and NCI share halved to Rs 2.98 Cr. Did any sub book an intra-group dividend in Q2, and which sub carries the minority? | Intra-group dividend named and sized | Unexplained profit shift | F2-02, F4-02, A3-07, FN05 |
| 11 (F) | Which subsidiaries hold the Rs 247.23 Cr of intercompany loans, why did Rs 62 Cr move from current to non-current, and what is Route Mobile UK's repayment schedule? | Planned refinancing; schedule given | Sub could not repay on time | F2-04 |
| 12 (G) | Name the 7 management-certified subsidiaries and the make-up of their Rs 45.28 Cr assets. | Cash and intercompany balances | Advances or receivables of doubtful quality | F3-01 |
| 13 (D) | Overseas segment liabilities fell Rs 114.76 Cr QoQ and Rs 499.76 Cr YoY, and payable days fell from 64 to 50 (deck). Was this supplier payables paid down or intra-group settlement? | Intra-group settlement | Suppliers demanding faster payment | F12-02, A3-19 |
| 14 (D) | Why did the deck switch LTM EBITDA from adjusted (Q1) to reported (Q2), and "Net Cash" to "Cash"? Give Q2 net cash and gross debt, and what the Rs 1,355.6 Cr includes. | Clerical; net cash given | Basis shopping | A3-15, A3-16 |
| 15 (G) | ESOP charge is nil in FY27 while 60 staff leave per quarter, and employee cost rose 17% QoQ (Rs 77.62 Cr to Rs 90.81 Cr) on flat headcount of 786. What drove the rise, and is a new ESOP scheme planned whose cost would be added back? | Heltar staff and one-time items; no new scheme | Wage inflation; new scheme added back | A3-01 |
| 16 (C) | Gross margin rose 150 bps QoQ to 22.38%. How many bps came from routing (reversible) vs new-product mix, and what is the Q3 FY27 gross-margin band? | Mostly mix; band 22-23% | Mostly routing; band unchanged | A3-23, FN02 |
| 17 (E) | What was Truecaller Business Messaging revenue in Q2 FY27, and is it above Rs 15 Cr per quarter: yes or no? | Yes, with a number | No number again | A3-24, FN13 |
| 18 (B) | The release says Q2 revenue was "in line with our guidance". State the FY27 revenue and EBITDA guidance numbers and their basis. | 5-9% revenue, ~12% EBITDA reaffirmed | No number | FN09 |
| 19 (D) | Is any residual from the FY26 Rs 135.87 Cr exceptional items (recovery, further charge, tax true-up) open in H2 FY27? | None | Further charge possible | FN01 |
| 20 (G) | Did the former Masiv CEO leave because of the data breach, and on what date? | Unrelated, planned | Linked to the breach | A3-09 |
| 21 (F) | FY27 interim dividends total Rs 8/share so far. What is the FY27 total payout target, and is a buyback under consideration? | Payout target stated | No policy | A3-08 |
| 22 (G) | The Chairman, who is also Proximus Global CEO, now stresses "prudent cost management" and a first-half review. Is a cost or restructuring programme planned for H2 FY27, and will its cost go through the exceptional line? | Routine emphasis; no programme | Programme with a one-off charge | FN11 |

Top 3 by likelihood of thesis-changing information:
- Q1 (Masivian total cost and Q3 add-back): a capped, ending cost raises the chance the Adjusted reading is fair; an open cost argues for the reported basis.
- Q2 (vendor advance): a link to the FY26 write-off counterparties or an unsecured prepayment confirms the bear cash case.
- Q4 (Proximus revenue): tests transparency on the one KPI management was asked for two cycles in a row.

Channel recommendation: the concall has already happened (28 Oct 2026) and no transcript exists. Draft an IR email with all 22 questions verbatim now. When a transcript or recording appears, run Role 5 on it and mark each question ANSWERED / PARTIAL / EVADED / NOT ADDRESSED.

---

# SECTION B: CONCALL ANALYSIS (ROLE 5): NOT RUN

No concall transcript exists for Q2 FY27 (call held 28 Oct 2026, 16:30 IST; no recording on the company's earnings-call page; no ASR transcript). Participants, Q&A decomposition, credibility ratio and archetype: ND. Management commentary below comes from the press release only.

Promise-vs-delivery on the Q1 concall commitments (N-L541-550), filed-document basis:

| Q1 commitment | Implied date | Q2 filed evidence | Status |
|---|---|---|---|
| High-margin customer traffic restored | Q2 FY27 | Overseas result -24.8% QoQ; no update (A3-25) | UNVERIFIED, leaning MISSED |
| Bank-customer margin reversal | Q2 FY27 | India result (4.00) to 27.11 (R295, R294) | PARTIALLY DELIVERED (data consistent) |
| Heltar close and consideration | Q2 FY27 | Closed 29 Jul 2026; Rs 33.66 Cr disclosed (R585) | DELIVERED |
| CLO/Clear firewall go-live | Q2 FY27 | Not mentioned; deck shows 12 firewalls deployed (dR052) | UNVERIFIED (slipped once already) |
| Volume growth 10-15% | next couple of quarters | H1 +10.7%; Q2 +5.3% YoY (dR166-dR168, dR224-dR225) | PARTIAL |
| Cash conversion 75-100% of EBITDA | FY27 (H1 test) | H1 reported CFO/EBITDA 15% (dR311) | MISSED on H1 |
| Masivian attestation, business returns | "very soon" | Fees 1.36 to 6.90; relabelled "data breach" | NOT DELIVERED |
| GM in 21.5-23% | Q2 FY27 | 22.38% | DELIVERED |

Narrative vs filing (press release vs filing): "recovery in gross profit margin" (pR040, L94) CONFIRMED (22.38% vs 20.88%). "Revenue performance in line with our guidance" UNVERIFIABLE (no number). Headline leads with PAT against a loss base; pre-exceptional PBT fell 26.79% YoY (FN10, CONFIRMATORY-NEGATIVE). Chairman language moved from demand and traffic to profitability and cost management (FN11).

---

## MONITORABLES AND CATALYST LIST (seeded by A3 F6 commitment registers and F13 board items)

| Item | Implied date | Source ref |
|---|---|---|
| Insider-trading window opens | 30 Oct 2026 | R997, L112 |
| Second interim dividend record date; TDS documents due | 02 Nov 2026 | R1016, R992, L55, L74 |
| Second interim dividend paid (Rs 4/share, ~Rs 25.20 Cr) | by 26 Nov 2026 | R990, L65; F13-03 |
| Q2 FY27 concall transcript or recording appears: run Role 5, re-score grade, test Proximus KPI on the call | when posted (ND) | Role 5 not run |
| MOA alteration shareholder vote (postal ballot or EGM) | date NOT FOUND | R996, L101; F13-01 |
| Q3 FY27 results: reported EBITDA margin (8C), Masivian add-back, India margin at constant volume, ETR, Truecaller and Heltar KPIs | by 14 Feb 2027 (Reg 33, 45 days) | 8C; F12-03; F8-02; A3-24; FN03 |
| Vendor advance Rs 116.83 Cr consumed in H2 FY27 | FY27 results, by 30 May 2027 (Reg 33, 60 days) | dR312, L834; A3-04 |
| Standalone receivable build (Rs 391.25 Cr) collects | FY27 results | R752; F2-03 |
| Rs 65 Cr IPO money spent on Mumbai office | date NOT FOUND | R995, L93; F6-01 |
| QIP Rs 867.50 Cr utilisation | date NOT FOUND | R999, L835 |
| Heltar deferred consideration Rs 9.78 Cr | ~29 Jan 2028 | R587, L851; A3-05 |
| Heltar core-team hires; roadmap (Voice AI, analytics, data layer) | undated | dR088, dR075 |
| Salesforce AgentExchange revenue (item 16) | by Q4 FY27 | dR065-dR066 |
| FY27 AR: hedge designation and notional, Proximus RPT, Customer A share, goodwill test incl. Heltar | ~Jul-Aug 2027 | F9-01; N-L11 |
| Strategic Premium recompute (+1.25x to +1.0x) and pillar refresh | next /fttcp run | Step 7 |
| Operator rulings: condition 1 basis; Rs 450 / Rs 420 floors; early-warning conflict; Truecaller counter; RDE trim | now | Step 6C, Step 8 |
| Q1 carry: large-account traffic recovery | not dated | A3 presentation register |

---

## FLAGS (surfaced for the verdict; the operator decides)

- F-1 THESIS-BROKEN CONDITION 1 IS BASIS-DEPENDENT. Adjusted 10.04% (not fired; headroom Rs 0.45 Cr; rests on a Rs 6.90 Cr add-back). Reported 9.75% after 9.16% (fired; pre-committed exit 50%). The Notion text names Adjusted where it names a basis; the thesis line and exit criteria name none. Operator ruling required.
- F-2 PRICE FLOORS. CMP Rs 435 sits below the Rs 450 hard floor (Position Size property). The 52-week low Rs 407 sits below the Rs 420 "exit 50% regardless of narrative" floor; breach date ND. CMP also sits below the AR-revised MoS Rs 463.
- F-3 Notion internal conflict: early-warning "EBITDA <10% any quarter → EXIT 50%" vs the two-quarter exit rule; the Q1 record did not apply the early-warning row.
- F-4 Strategic Premium expiry condition met on filed evidence (no Proximus revenue KPI); +1.25x to +1.0x pending /fttcp. Concall content unknown.
- F-5 Cash conversion INDETERMINATE-WITH-DIRECTION: H1 CFO/PAT 0.22x; Rs 116.83 Cr vendor prepayment, same asset class as the FY26 Rs 135.87 Cr write-offs; standalone CFO -Rs 126.69 Cr.
- F-6 Cap-5% gate FAILED (GM 22.38% < 23%). Add-back conditions technically met but blocked. RDE 4%->3% trim re-put.
- F-7 PAT quality: 49% of the QoQ PAT gain is a lower ETR; normalised PAT -17.75% YoY; core PBT -19.86% YoY.
- F-8 Mix: overseas result -24.8% QoQ; the parent alone delivered the QoQ EBITDA gain; revenue outside new products fell 0.54% QoQ.
- F-9 Governance: first MSKA review; component-audited subs = 79.3% of consolidated PAT (Q1 35.3%); MOA objects expand into digital identity and AI; Brussels signing; repeated non-addressing of prior questions.
- F-10 Truecaller item 13 RED on the Notion counter; operator to rule the counting basis.
- F-11 Role 5 NOT RUN: no transcript.
- F-12 Notion properties stale: Entry Price Max 628 and MoS 502 vs AR-revised 579 / 463. Notion carries no FY27 bear margin, PAT or EPS.
- F-13 Condition 5 reading: the FY26 write-off of Rs 107.96 Cr sits above the Rs 100 Cr leg; the record treats it as closed; the Q1 6C table omitted condition 5.

Protocol verdict: PROCEED WITH FLAGS. Cash axis capped by INDETERMINATE-WITH-DIRECTION; F-1 and F-2 need operator rulings before any position action.

## STEP 9: NOTION PAYLOAD (not written; Decision Status never written by /run-quarterly)
- Decision Status: no change proposed by A4. If the operator rules the reported basis for condition 1, or applies the Rs 420 / Rs 450 floor, the pre-committed action is EXIT 50% (4% to 2%); the operator sets it.
- Key Notes prepend (proposed): "[29-Oct-26 Q2 FY27 results] Rev Rs 1,179.67 Cr +5.4% YoY; GM 22.38%; Adj EBITDA 10.0% (10.04%) only after Rs 6.90 Cr Masivian add-back; reported 9.75% (2nd quarter <10%). Condition 1 NOT FIRED on Adjusted basis, FIRED on reported basis: OPERATOR RULING. H1 CFO/PAT 0.22x (vendor advance Rs 116.83 Cr). No Proximus KPI: Strategic Premium expiry met. Cap-5% gate FAILED. CMP Rs 435 below Rs 450 hard floor. No concall transcript; Role 5 not run. PROCEED WITH FLAGS; HELD 4% pending rulings."
- Property updates proposed: Entry Price Max 579, Margin of Safety Price 463 (align with AR review); Position Size text to record the Q2 gate result.

---

## PLAIN-LANGUAGE BRIEF

### 1. SUMMARY NARRATIVE
Route Mobile sold Rs 1,179.67 Cr of services in Q2 FY27. That is 5.4% more than a year ago and 2.4% more than last quarter [FILED, this quarter].
Gross margin recovered to 22.4% from 20.9% in Q1 [FILED, this quarter]. It is still below the 23% line our 5% position cap needs [Notion, prior].
Operating profit fell 15.4% from a year ago, to Rs 115.02 Cr [FILED, derived, this quarter].
The key test was the 10% margin line. Management's adjusted margin is 10.0% [MGMT, deck, this quarter]. It clears 10% only because the company adds back Rs 6.90 Cr of data-breach costs at its Colombian unit [MGMT, deck].
Without that add-back, or on plain reported numbers, the margin is below 10% for a second quarter: 9.45% or 9.75% [FILED, derived].
Our notes name the adjusted figure where they name a basis. The exit rule itself names none [Notion, prior]. So the operator must rule which number counts. On the reported number, the rule says sell half.
Cash was weak. The company turned Rs 151 Cr of profit into Rs 33 Cr of operating cash [FILED, this quarter]. Most of the gap is a Rs 117 Cr advance paid to a supplier [MGMT, deck]. Advances of this kind cost Rs 136 Cr in write-offs last year [FILED, FY26 note].
Profit rose 20% from Q1, but half of that rise came from a lower tax rate [FILED, derived].
No figure on Proximus-linked sales appeared, so the strategic premium falls under the rule on file [Notion, prior; FILED silence].
The share price, Rs 435, sits below the Rs 450 floor in our notes [SECONDARY, screener; Notion, prior].
No concall transcript exists, so we could not test what management said on the call.
Decision: still HELD at 4%. Two rulings come first: the margin basis and the price floor.

### 2. SECTOR INTELLIGENCE
The market for business messaging grows about 13% a year [Notion, prior, SECONDARY]. Peer Tanla grew 11.8% [Notion, prior].
Plain SMS is slowing. WhatsApp, RCS and AI chat take the growth [Notion, prior; INFERENCE].
Route's new products grew 36.7% from a year ago and are now 10.9% of sales [MGMT, deck, this quarter]. Its other sales were flat [FILED and MGMT, derived].
Two sector risks stay live. Meta can change WhatsApp prices, as it did in Q3 FY26 [Notion, prior]. Large clients can go direct to telecom operators [Notion, prior].
A data breach brings a new kind of risk: regulators and customer claims can follow [INFERENCE from the deck label change].
The filings do not give the SMS, OTT and voice mix. That metric is not disclosed.

### 3. BUSINESS-MODEL INTELLIGENCE
Route buys message delivery from telecom operators and resells it to businesses. It keeps the difference [Notion, prior].
In Q2 it kept Rs 0.0555 per message, up from Rs 0.0525 in Q1 [MGMT, deck, derived]. Price per message was flat from a year ago [MGMT, deck, derived].
Management credits "enhanced routing" for the better margin [MGMT, deck]. Routing gains can reverse if operators raise prices [INFERENCE].
The model is drifting in two ways. First, the Indian parent now earns the gains, while the overseas units earned 25% less than in Q1 [FILED, this quarter]. Second, cash now goes out early to suppliers, and the parent's unpaid bills rose 62% in six months [FILED, this quarter].
Heltar, an AI chat business bought for up to Rs 33.66 Cr, aims to sell outcomes, not messages [FILED and MGMT, this quarter]. Its revenue is not disclosed.

### 4. COMPETITION INTELLIGENCE
Route wins on reach. It has 280+ direct operator links and serves 2,400+ paying clients [MGMT, deck, this quarter].
It wins on retention too: clients billed every month make up 93% of revenue, and net revenue retention is 105% [MGMT, deck].
It is weaker than Tanla on margin. The thesis bull case needs Tanla-like 17% EBITDA, which Route has never reached [Notion, prior].
Twilio, Sinch and Infobip lead the move to RCS and AI [Notion, prior]. The new Masiv CEO comes from Infobip [Notion, prior].
Sister firm Telesign sells some of the same services, such as verification [Notion, prior]. The board now wants to add digital identity and AI to Route's legal objects [FILED, this quarter]. That gives room to move group businesses into Route. It could also bring overlap.
The risk to watch: the largest clients are thinning. Clients above $5 million fell from 21 to 19 [MGMT, deck].

### 5. FORWARD MAP (next ~10-11 months)
Make-or-break reading: Q3 FY27 reported EBITDA margin, due by 14 Feb 2027. Bull: 10.0% or more with no add-back. Bear: below 10.0% for a third quarter.
- 30 Oct 2026, trading window opens. Bull: no insider selling. Bear: insider selling.
- 2 Nov 2026, dividend record date; payment by 26 Nov 2026. Bull: paid on time. Bear: delay.
- Concall transcript, date unknown. Bull: a Proximus revenue figure appears and the premium question reopens. Bear: no figure, and grade C stays.
- MOA shareholder vote, date not found. Bull: no group transfer follows. Bear: a group business moves in at a related-party price.
- Q3 FY27 results, by 14 Feb 2027. Bull: Masivian costs end and India margin holds at constant volume. Bear: add-backs recur and the tax rate rises back toward 25%.
- FY27 results, by 30 May 2027. Bull: the Rs 116.83 Cr advance is used up and cash recovers. Bear: the advance stays or grows, which points to tighter supplier terms.
- Mumbai office purchase with Rs 65 Cr, date not found. Bull: a date and a property. Bear: the money stays idle.
- FY27 annual report, about Jul-Aug 2027. Bull: Proximus related-party sales are disclosed and growing. Bear: the Customer A share rises above 18%.

---

```yaml
stage: A4-analyst
company: "ROUTE"
quarter: "q2fy27"
model: "claude-opus-5-5"
status: complete
docs_merged: [results, presentation, pressrelease]
ledger_reconciliation:
  notes: 23
  turns: 0
  slides: 26
  all_reviewed: true
  a3_findings_incorporated: [F1-01, F1-02, F1-03, F2-01, F2-02, F2-03, F2-04, F3-01, F4-01, F4-02, F6-01, F6-02, F8-01, F8-02, F9-01, F12-01, F12-02, F12-03, F13-01, F13-02, F13-03, F14-01, F14-02, F14-03, F14-04, A3-01, A3-02, A3-03, A3-04, A3-05, A3-06, A3-07, A3-08, A3-09, A3-10, A3-11, A3-12, A3-13, A3-14, A3-15, A3-16, A3-17, A3-18, A3-19, A3-20, A3-21, A3-22, A3-23, A3-24, A3-25, A3-26, FN01, FN02, FN03, FN04, FN05, FN06, FN07, FN08, FN09, FN10, FN11, FN12, FN13, FN14, FN15]
protocol_verdict: "PROCEED WITH FLAGS"
cash_conversion: "INDETERMINATE-WITH-DIRECTION"
decision_status_verified: "HELD (4%, avg cost Rs 509; Notion fetched 2026-10-29, page as of 2026-09-03)"
position_branch: "8A"
sc_gap_pat_pct:
  - {period: "Q2 FY26", gap_pct: -157.2, note: "n.m., exceptional in subs"}
  - {period: "Q1 FY27", gap_pct: 324.2}
  - {period: "Q2 FY27", gap_pct: 149.2}
  - {period: "H1 FY26", gap_pct: -36.9, note: "n.m., exceptional in subs"}
  - {period: "H1 FY27", gap_pct: 206.6}
  - {period: "FY26", gap_pct: 90.6}
questions_for_management:
  - {q: "Total Masivian breach remediation cost to date and to come; any Q3 FY27 add-back? (Adj 10.0% clears only with Rs 6.90 Cr add-back)", from_finding_id: "A3-18, A3-17, FN12, F2-01"}
  - {q: "Rs 116.83 Cr vendor advance: vendor type, tenor, security, amount consumed by 31 Oct 2026, link to Q1 Rs 4.90 Cr allowance or FY26 Rs 135.87 Cr write-offs", from_finding_id: "F1-01, A3-02, A3-04, A3-19"}
  - {q: "Overseas segment result -24.8% QoQ: cause; did the Q1 large account recover (yes/no)?", from_finding_id: "F12-01, A3-25, FN14, F2-01"}
  - {q: "H1 FY27 INR revenue from Proximus/Telesign/BICS-introduced customers; share of Europe-HQ revenue fall from group accounts", from_finding_id: "A3-26, A3-20, A3-21"}
  - {q: "ETR 18.21% (ex-parent 12.33%), deferred credit Rs 3.24 Cr: driver and H2 FY27/FY28 ETR", from_finding_id: "F8-01, F8-02, FN04, A3-06, A3-10"}
  - {q: "Standalone receivables +Rs 149.89 Cr (+62%), DSO ~139 days: top-3 India and group-entity billing share; collection date", from_finding_id: "F2-03, F12-03, A3-13"}
  - {q: "MOA objects expansion and Brussels signing: any acquisition or transfer from the Proximus group within 12 months (yes/no); vote date", from_finding_id: "F13-01, F13-02, FN06"}
  - {q: "Heltar revenue since 29 Jul 2026; clients added; founders retained; is the Rs 9.78 Cr deferred leg an earn-out", from_finding_id: "F6-02, A3-22, FN03, FN08"}
  - {q: "Why rescind the 7 May 2026 IPO variation; completion date for the Rs 65 Cr Mumbai office", from_finding_id: "F6-01"}
  - {q: "24 component subs PAT Rs 24.19 to 65.43 Cr, residual -15.80, NCI halved: intra-group dividend? which sub carries the minority", from_finding_id: "F2-02, F4-02, A3-07, FN05"}
  - {q: "Which subs hold Rs 247.23 Cr intercompany loans; why Rs 62 Cr moved to non-current; Route Mobile UK schedule", from_finding_id: "F2-04"}
  - {q: "Name the 7 management-certified subs and the make-up of their Rs 45.28 Cr assets", from_finding_id: "F3-01"}
  - {q: "Overseas liabilities -Rs 114.76 Cr QoQ, DPO 64 to 50: supplier paydown or intra-group settlement", from_finding_id: "F12-02, A3-19"}
  - {q: "Why LTM EBITDA basis switched and 'Net Cash' became 'Cash'; Q2 net cash, gross debt, composition of Rs 1,355.6 Cr", from_finding_id: "A3-15, A3-16"}
  - {q: "Employee cost +17% QoQ on flat 786 headcount; nil ESOP charge; any new ESOP scheme to be added back", from_finding_id: "A3-01"}
  - {q: "GM +150 bps QoQ: routing vs mix split in bps; Q3 FY27 GM band", from_finding_id: "A3-23, FN02"}
  - {q: "Truecaller BM revenue Q2 FY27; above Rs 15 Cr/qtr (yes/no)", from_finding_id: "A3-24, FN13"}
  - {q: "State the FY27 revenue and EBITDA guidance numbers behind 'in line with our guidance'", from_finding_id: "FN09"}
  - {q: "Any residual from FY26 Rs 135.87 Cr exceptional items open in H2 FY27", from_finding_id: "FN01"}
  - {q: "Did the former Masiv CEO's exit relate to the breach; date", from_finding_id: "A3-09"}
  - {q: "FY27 total dividend payout target; any buyback under consideration", from_finding_id: "A3-08"}
  - {q: "Is an H2 FY27 cost or restructuring programme planned; would it go through the exceptional line", from_finding_id: "FN11"}
monitorables:
  - {item: "Insider trading window opens", implied_date: "2026-10-30", source_ref: "results R997 L112"}
  - {item: "Second interim dividend record date and TDS documents", implied_date: "2026-11-02", source_ref: "results R1016 R992 L55 L74"}
  - {item: "Second interim dividend paid Rs 4/share (~Rs 25.20 Cr)", implied_date: "by 2026-11-26", source_ref: "results R990 L65; F13-03"}
  - {item: "Q2 FY27 concall transcript/recording: run Role 5; test Proximus KPI on the call", implied_date: "ND (when posted)", source_ref: "Role 5 not run"}
  - {item: "MOA alteration shareholder vote", implied_date: "NOT FOUND", source_ref: "results R996 L101; F13-01"}
  - {item: "Q3 FY27 reported EBITDA margin (single cleanest metric), Masivian add-back, India margin, ETR, Truecaller and Heltar KPIs", implied_date: "by 2027-02-14", source_ref: "Step 8C; F12-03; F8-02; A3-24; FN03"}
  - {item: "Vendor advance Rs 116.83 Cr consumed in H2 FY27", implied_date: "FY27 results, by 2027-05-30", source_ref: "deck dR312 L834; A3-04"}
  - {item: "Standalone receivable build Rs 391.25 Cr collects", implied_date: "FY27 results, by 2027-05-30", source_ref: "results R752; F2-03"}
  - {item: "Rs 65 Cr IPO proceeds spent on Mumbai office", implied_date: "NOT FOUND", source_ref: "results R995 L93; F6-01"}
  - {item: "QIP Rs 867.50 Cr utilisation", implied_date: "NOT FOUND", source_ref: "results R999 L835"}
  - {item: "Heltar deferred consideration Rs 9.78 Cr", implied_date: "~2028-01-29", source_ref: "results R587 L851; A3-05"}
  - {item: "Salesforce AgentExchange revenue (item 16)", implied_date: "by Q4 FY27", source_ref: "deck dR065-dR066"}
  - {item: "FY27 AR: hedge designation, Proximus RPT, Customer A share, goodwill test incl. Heltar", implied_date: "~2027-07 to 2027-08", source_ref: "F9-01; Notion Key Notes"}
  - {item: "Strategic Premium recompute +1.25x to +1.0x and pillar refresh", implied_date: "next /fttcp run", source_ref: "Step 7"}
  - {item: "Operator rulings: condition 1 basis, Rs 450/Rs 420 floors, early-warning conflict, Truecaller counter, RDE trim", implied_date: "now", source_ref: "Steps 6C, 8"}
flags:
  - "F-1 Thesis-broken condition 1 basis-dependent: Adjusted 10.04% NOT FIRED (headroom Rs 0.45 Cr, rests on Rs 6.90 Cr Masivian add-back); reported 9.75% after 9.16% FIRED (pre-committed exit 50%). Notion names Adjusted where it names a basis; thesis line and exit criteria name none. OPERATOR RULING."
  - "F-2 CMP Rs 435 below Rs 450 hard floor (Position Size); 52-week low Rs 407 below Rs 420 'exit 50% regardless' floor, breach date ND; CMP below AR MoS Rs 463."
  - "F-3 Notion conflict: early-warning 'EBITDA <10% any quarter -> EXIT 50%' vs two-quarter rule; not applied at Q1."
  - "F-4 Strategic Premium expiry met on filed evidence (no Proximus revenue KPI); +1.25x to +1.0x deferred to /fttcp; concall content unknown."
  - "F-5 Cash INDETERMINATE-WITH-DIRECTION: H1 CFO/PAT 0.22x; Rs 116.83 Cr vendor prepayment (same asset class as FY26 Rs 135.87 Cr write-offs); standalone CFO -Rs 126.69 Cr."
  - "F-6 Cap-5% gate FAILED (GM 22.38% < 23%); add-back conditions met but blocked; RDE 4%->3% trim re-put."
  - "F-7 PAT quality: 49% of QoQ PAT gain from lower ETR; normalised PAT -17.75% YoY; core PBT -19.86% YoY."
  - "F-8 Overseas result -24.8% QoQ; parent alone delivered the QoQ EBITDA gain; revenue ex-new-products -0.54% QoQ."
  - "F-9 Governance: first MSKA review; component-audited subs 79.3% of consol PAT; MOA expansion into digital identity/AI; Brussels signing; 0 of 12 prior questions answered on filed basis."
  - "F-10 Truecaller item 13 RED on Notion counter (AMBER on strict quarter count)."
  - "F-11 Role 5 NOT RUN: no Q2 concall transcript."
  - "F-12 Notion properties stale (Entry 628 / MoS 502 vs 579 / 463); no FY27 bear margin, PAT or EPS on file."
  - "F-13 Condition 5: FY26 Rs 107.96 Cr write-off above the Rs 100 Cr leg; record treats as closed; Q1 6C omitted condition 5."
plain_language_brief_included: true
analyst_note: "The decisive Q2 test did not resolve cleanly. Management's Adjusted EBITDA margin is 10.04%, Rs 0.45 Cr above the line, but only because Rs 6.90 Cr of Masivian data-breach fees is added back for a second quarter. Reported margin is 9.75% after 9.16%. Notion names the Adjusted basis in the checklist and Key Notes, but the thesis line and RDE exit row name no basis, so A4 shows both and does not rule. Conservative reading of the add-back leans to fired. Separately, CMP Rs 435 sits below the Rs 450 hard floor and the 52-week low Rs 407 sits below the Rs 420 exit floor; breach timing is not in the inputs. Cash is the sharper problem: H1 CFO/PAT 0.22x, driven by a Rs 116.83 Cr supplier prepayment of the same kind that produced FY26's Rs 135.87 Cr write-offs. EPS-share-count findings (A3-07, FN05) resolve: EPS uses owners' PAT; shares unchanged at 6.30 Cr. No concall transcript exists, so Role 5, the Proximus KPI on the call, and the management grade could not be tested."
review_path: "runs/route-q2fy27/work/review_route_q2fy27.md"
```
