# SOUTHBANK: The South Indian Bank Ltd

Shallow Analysis Framework v1.0. Screened 2026-09-23 by Claude Code.
NSE SOUTHBANK | BSE 532218 | ISIN INE683A01023. Lender variant.
Corpus: `screens/corpus/SOUTHBANK/`. Every number below cites a file and a page.
Corpus deviation: Bull AI chunk reader under operator ruling 2026-09-08; no egress. Pages marked (full page) were read whole with get_document_chunks; all others are search snippets.

---

## Business Understanding Narrative

**What does it do, and how does it make money?** The bank takes deposits and
lends them. FY26 deposits were Rs 1,23,346 crore, up 15%, and gross advances
Rs 1,00,274 crore, up 14.5% (Earnings call Q4 FY26, doc b3dc776b, p2). It earns
net interest income of Rs 3,437 crore plus Rs 2,010 crore of other income
(Investor Presentation FY2026 Q4, doc df63309d, p38, full page).

**What is changing?** The legacy bad book is gone. Over eight quarters GNPA fell
from 4.50% to 1.43% and NNPA from 1.44% to 0.29%. PCR is 94.10% (doc df63309d,
p40, full page). Management wants the corporate book, now 38%, down to "about a
third" (doc b3dc776b, p16).

**Why now?** The clean up is done. CRAR is 19.66% (doc df63309d, p9). Management
says 60 to 65% of deposits reprice this year in its favour (doc b3dc776b, p11).

**What must be true for the thesis to work?** Core earnings must grow. FY26 PAT
rose 12%, but operating profit before treasury fell 4.4% (step 5). NIM must
hold above 3% and cost growth near the guided 5 to 6%.

**What breaks it?** Margin. Q4 FY26 NIM was 2.95% (doc df63309d, p40, full
page). Treasury income was Rs 463 crore in FY26 and zero in Q4 (p38, full page).
Without treasury, RoA stays near 1%.

---

## 1. Corpus ledger

Held: annual report FY26, earnings calls, investor presentations to Q1 FY27.
Key: df63309d, Investor Presentation FY2026 Q4; b6415007, Investor Presentation
FY2027 Q1; b3dc776b, Q4 FY26 call; 7a0c092a, an FY2027 call; 249f4a17, Q4 FY25
call; 8a56949d, a call transcript. Guidance quotes come from the Bull AI
guidance record.

Missing or not read: the shareholding pattern, Q1 FY27 GNPA (pages 8 to 16 of
doc b6415007 returned empty chunks), the annual report note on write-offs and
ARC sales, and any credit rating. Steps 4, 8 and 10 are weak.

## 2. Business model and archetype

One engine: NIM on a deposit base. CASA was 32.12% at 31 March 2026 (doc
df63309d, p8) and 32.98% at 30 June 2026 (doc b6415007, p7).

Standalone, Rs crore (doc df63309d, p38, full page):

| | FY25 | FY26 | Change |
|---|---|---|---|
| Net interest income | 3,486 | 3,437 | -1% |
| Core fee income | 758 | 787 | +4% |
| Treasury and forex | 272 | 463 | +70% |
| Operating expenses | 3,029 | 3,074 | +1.5% |
| Operating profit | 2,270 | 2,373 | +5% |
| Provisions | 513 | 417 | -19% |
| PAT | 1,303 | 1,455 | +12% |

**Archetype: lender.** The binding variables are loan growth, NIM, GNPA and
credit cost, RoA and RoE. The ladder runs on asset quality and RoA.

## 3. Competitive advantages

A lender's moat is cheap, sticky deposits. CASA near a third is ordinary, and
NIM of 2.95% to 3.23% shows no pricing power. Gold loans grew 46% to Rs 24,729
crore (doc b3dc776b, p3) at an LTV of 57.18% (doc 8a56949d, p4). Peers are cut in
shallow. Verdict: **moat not
evidenced.**

## 4. The promoters

Shareholding pattern, promoter status and pledge: **NOT FOUND** in this
corpus.

The substitute is management's record against guidance. For FY26 it
guided RoA "in the neighborhood of 1%" (doc 249f4a17, p13). Q4 FY26 RoA was
1.17% (doc df63309d, p8). It guided asset growth "north of 12%" with hope of
beating it by 3 or 4 points (doc 249f4a17, p5). Gross advances grew 14.5%, or
15.8% excluding technical write-off (doc df63309d, p12). A delivery record,
not a governance finding.

## 5. Financial trajectory

Eight quarters, Q1 FY25 to Q4 FY26 (doc df63309d, p40, full page), then Q1 FY27
(doc b6415007, p7):

| | Start of series | Q4 FY26 | Q1 FY27 |
|---|---|---|---|
| GNPA | 4.50% | 1.43% | NOT FOUND |
| NNPA | 1.44% | 0.29% | NOT FOUND |
| NIM | 3.26% | 2.95% | 3.23% |
| RoA | NOT FOUND | 1.17% | 1.05% |
| RoE | NOT FOUND | 14.49% | 12.84% |

Q1 FY27 PAT was Rs 378 crore, up 17.4% on Rs 322 crore. Gross advances grew
17.0% and deposits 11.4% (doc b6415007, p7). Q4 FY26 PAT was Rs 408 crore
against Rs 342 crore (doc 8a56949d, p4), with treasury income nil (doc df63309d,
p38, full page).

Operating profit before treasury fell from Rs 1,998 crore to Rs 1,910 crore,
down 4.4% (derived: 2,270 less 272; 2,373 less 463). PAT growth of Rs 152 crore
came from treasury (+Rs 191 crore) and lower provisions (Rs 96 crore less).

Leverage: net worth Rs 11,404 crore (derived: capital 262 plus reserves
11,142), borrowings Rs 3,927 crore, deposits Rs 1,23,346 crore (doc df63309d,
p39, full page). CRAR 19.66% (doc df63309d, p9).

**Inflection classification: asset quality led, with a one time assist.**

## 6. The transition and the quality ladder

FROM R1 (lender): legacy corporate NPA, RoA under 0.7%, GNPA 4.5%. TO R2
(lender) claimed: a clean retail, gold and MSME book with RoA of 1.20 to 1.25%.

The mechanism is mix: less corporate, more secured retail, cheaper deposits.

Management's claim, quoted once: "We had said that we'd be in the 100 to 110,
115 range. Over time, that should sort of migrate to 120, 125" (doc 7a0c092a,
p14). The claim has no date. One rung, inside the base rate.

## 7. Growth-trigger register

| Trigger | Date | Source | Status |
|---|---|---|---|
| GNPA 1.43%, NNPA 0.29% | FY26 | doc df63309d, p5 | delivered |
| Gold loans +46% to Rs 24,729 crore | FY26 | doc b3dc776b, p3 | delivered |
| Loan growth 15 to 16% | FY27 | doc b3dc776b, p8 | underway (Q1 +17.0%) |
| Deposit repricing, 60 to 65% of book | FY27 | doc b3dc776b, p11 | underway (Q1 NIM 3.23%) |
| Opex growth 5 to 6% | FY27 | doc 7a0c092a, p6 | stated |
| Slippage Rs 500 to 800 crore; recoveries Rs 800 to 1,000 crore | FY27 | doc 7a0c092a, p10 | stated |
| Corporate book to about a third | not dated | doc b3dc776b, p16 | stated |
| RoA 1.20 to 1.25% | "over time" | doc 7a0c092a, p14 | stated |

## 8. Proof check

**Asset quality: fired.** Q4 FY26 slippage ratio was 0.15. Q4 slippage of Rs
147 crore split Rs 93 crore new book and Rs 54 crore old book. Collection
efficiency was 101.1%. GNPA fell in all four segments: agri Rs 404 to 154
crore, business Rs 1,309 to 647 crore, personal Rs 567 to 378 crore, corporate
Rs 301 to 251 crore (doc df63309d, pp42 and 43).

**Earnings quality: not fired.** Core operating profit fell 4.4% and NII 1%.
Q1 FY27 RoA of 1.05% sits below Q4's 1.17%. Q1 NIM of 3.23% is one quarter.

## 9. Flags from the documents

- **Treasury carried FY26.** Rs 463 crore of income; zero in Q4.
- **Disbursements fell 31%** in Q1 FY27, Rs 52,305 crore to Rs 36,048 crore,
  while gross advances grew 17.0% (doc b6415007, p7). The book includes
  purchased portfolios (doc 8a56949d, p4). [INFERENCE] Part of loan growth may
  be bought, not originated.
- **Gold is 24.7% of gross advances** (derived: 24,729 / 1,00,274).
- **Q4 GNPA deductions of Rs 1,300 crore** (Rs 1,148 crore a year earlier)
  (doc df63309d, p41). Their nature is NOT FOUND (step 11).
- **Market capitalisation of Rs 11,854.96 crore** sits above the small and
  micro cap band.

## 10. Independent check: the credit rating

**NOT FOUND.** No rating rationale is in the corpus read. CRAR of 19.66% is a
regulatory ratio, not a credit opinion.

## 11. Posture: the Transition Decision Matrix

- **Proof gate: FIRED on asset quality, NOT FIRED on earnings.**
- **Ugliness: CONTESTED.** Low RoA and NIM compression from 3.26% to 2.95%,
  then 3.23% in Q1 FY27. ARTIFACT if deposit repricing lifts NIM. STRUCTURAL if
  an old private bank simply earns this much.
- **Recognition gap: OPEN.** Forward PE 7.1x to 7.8x (step 13). Price to book
  about 1.04x (derived: share price about Rs 45.2 = 11,854.96 / 262 crore
  shares; book value per share Rs 43.6, doc df63309d, p40, full page).

**Posture: CONTESTED CELL.** RE-RATING LIVE if the ugliness is artifact.
VALUE-TRAP RISK if it is structural.

Rule I: the pattern is the old private bank that stays cheap for a decade.
Success catalogue pending (0 of 4 names).

Two readings of the Q4 GNPA drop (Amendment 25). Rs 1,300 crore left GNPA while
NPA provisions were only Rs 15 crore, against Rs 249 crore in Q1 FY26 (doc
df63309d, p42).
- **Reading A:** technical write-off of a fully provided legacy book. Cosmetic
  for ratios, neutral for economics. The bank said it intends "to continue to do
  technical write-offs" (doc 249f4a17, p11).
- **Reading B:** an ARC sale or real recovery.
- **The one observation that separates them:** the FY26 annual report note on
  write-offs and ARC sales, read with Q1 FY27 GNPA (NOT FOUND).

## 12. Verdict card

**WATCH.**

Watch trigger: RoA at or above 1.20% for two consecutive quarters, with
treasury gains below 10% of operating profit.

Facts to verify first, the ones the verdict rests on:
1. Q1 FY27 GNPA and NNPA.
2. The FY26 annual report note on write-offs and ARC sales.
3. The shareholding pattern.
4. Operating profit before treasury, Q1 and Q2 FY27.
5. Q2 FY27 NIM against the 3.23% of Q1.

What would change the view. The trigger firing moves this to PROCEED. NIM
under 3.0% with RoA under 1.0% moves it to DEEP WATCH.

Open action 5 status: two years on one page YES (doc df63309d, p38, full page);
PBT build YES (p38); leverage YES (CRAR p40, balance sheet p39, full page);
shareholding NOT FOUND (no pattern in corpus). WATCH rests partly on this
gap.

No price. No position.

## 13. Forward view

| Item | Value |
|---|---|
| FY26A PAT | Rs 1,455 crore (doc df63309d, p38, full page) |
| FY27E PAT | Rs 1,512 crore to Rs 1,659 crore |
| Growth on FY26 | +4% to +14% |
| Market capitalisation | Rs 11,854.96 crore (Bull AI company record, service record, 2026-09-23) |
| **Forward PE** | **7.8x to 7.1x** |
| **Basis tier** | **B (low) and A (high)** |

Derivation. The low case annualises Q1 FY27 PAT: Rs 378 crore x 4 is Rs 1,512
crore (tier B). The high case uses guided loan growth of 15 to 16% (doc
b3dc776b, p8). It assumes the balance sheet grows 14% at flat FY26 RoA: 1,455 x
1.14 is Rs 1,659 crore. The 14% is an assumption, stated. It sits below the
loan guide and near FY26 advance growth of 14.5%.

**The warning this step exists to carry.** FY26 PAT held Rs 463 crore of
treasury income, and Q4 treasury was zero. A 7x multiple on earnings that lean
on treasury is a screen result. For a bank, price to book of
about 1.04x is the better lens. Read this step with steps 5, 8, 9 and 11, never
instead of them.
