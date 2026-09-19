# STAGE 2 — NOTES TO FINANCIAL STATEMENTS, PASS 2 OF 3 (WHAT WAS MISSED)
Company: SHAREINDIA (Share India Securities Limited) | Run date: 2026-09-19
Source: inputs/annual-report/SHAREINDIA-AR-FY26.txt (FY26 AR, page markers cited)
Method: full note-by-note re-read of standalone Notes 1-64 (pp.140-221) and
consolidated Notes 1-68 (pp.251-335), checked line by line against the Pass 1
report (outputs/reports/02-notes-pass1.md) and its block. Only genuinely NEW
findings are reported below; anything Pass 1 already covered is not repeated.
Units as printed: ` in Lakhs. Cr equivalents shown in parentheses (÷100),
arithmetic shown inline, never a silent conversion.

Pass 1 was unusually thorough (all 64 standalone + 68 consol note numbers
individually addressed, LBF1-4 load-bearing facts resolved to the extent the
notes allow). This pass therefore found fewer, but still material, new items,
concentrated in three note families Pass 1 touched only lightly: the
Investments note (10/10A/10B), the fair value hierarchy note (53/54), and the
Schedule III ratio footnotes (58a/63a).

═══════════════════════════════════════════════════════════════════
PASS 2 NEW FINDINGS
═══════════════════════════════════════════════════════════════════

## 1. 🔴 Reported DSCR explicitly EXCLUDES the proposed NCD early redemption
   the Board itself approved (Note 58a standalone p.218; Note 63a consol
   p.328, both identical footnote)

The Schedule III ratio table footnote states, verbatim: "Current maturity
has been considered as per contractual repayment schedule and exclude the
impact of proposed early redemption of Non-convertible debentures (NCDs)."
This is the company's own qualifier on its own headline ratio.

Pass 1 (finding #6) reported the DSCR deterioration (3.25x standalone /
2.74x consol, down from 4.79x / 4.62x) but did not surface that the company
discloses, in the same note, that this ratio is computed on the ORIGINAL
contractual schedule and specifically EXCLUDES the ₹9,990 lakh (~₹99.9 Cr)
early redemption the Board approved on 19-May-2026 (Note 17e/18e, already
in Pass 1 finding #4). If that redemption is added to the current-maturity
denominator — which is the economically relevant test, since the Board has
already resolved to accelerate it — the true near-term debt service
coverage is worse than the 3.25x/2.74x reported. This is a load-bearing,
company-disclosed qualifier on the FLAG-CASH metric, not an outside
inference, and materially sharpens Pass 1 findings #4 and #6 taken together.

## 2. 🟡 Two additional Schedule III ratios deteriorated, not previously cited
   (Note 58a standalone p.218; Note 63a consol p.328)

Beyond DSCR/ISCR (Pass 1 finding #6), the same table shows:
- Long-term debt to working capital ratio: 0.03x → 0.14x standalone (a
  4.7x increase); 0.06x → 0.13x consol (2.2x increase).
- Debtor turnover ratio: 5.87x → 4.12x standalone (-29.8%); 7.13x → 4.69x
  consol (-34.2%).
Both point the same direction as the DSCR/ISCR decline (funding structure
and receivables efficiency both worsened in FY26), reinforcing rather than
contradicting FLAG-CASH, but were not individually named in Pass 1.

## 3. 🟡 FVOCI quoted equity portfolio nearly fully liquidated; gains/losses
   never pass through P&L by design (Note 10/10A standalone pp.159-160,
   consol Note 10/10A pp.258-260)

Pass 1 discussed the FVPL investment book (Note 30, Note 10B) but did not
address the separate FVOCI equity book at all. Note 10(A) shows FVOCI
quoted equity shares fell from ` 5,641.96 lakhs (~₹56.42 Cr, 30 individual
scrips, 55,42,828 shares) to ` 364.09 lakhs (~₹3.64 Cr, 5 scrips,
4,81,602 shares) — a 93.5% reduction, identical at standalone and consol
level (i.e., this is entirely a parent-level book). The single largest
line item, Master Trust Limited, fell from 20,55,441 shares (` 2,592.32
lakhs) to just 1,81,897 shares (` 102.48 lakhs) — the parent divested
roughly 90% of its Master Trust holding.

Under the Company's own accounting policy (2.11(b)(ii), p.145), fair value
movements on FVOCI equity instruments are recognised in OCI, and on
disposal "the realised amount of gain/(loss)... is then finally transferred
from OCI to retained earnings" — i.e. it NEVER passes through the
Statement of Profit and Loss, at acquisition or at exit. A portfolio churn
of this size (~₹52 Cr of holdings exited) is consequently invisible in
reported PAT; the only P&L-adjacent trace is the OCI tax lines in Note
40(b) (₹182.45 lakhs current tax + ₹45.81 lakhs deferred tax on "net
gain/(loss) on fair value of investment," both in OCI). This is a
legitimate, disclosed accounting policy, not a defect, but it is an
earnings-quality/transparency point an investor building a P&L bridge
would otherwise miss entirely.

## 4. 🟡 A subsidiary independently carries a large FVPL position in the SAME
   stock (Master Trust Limited) the parent is exiting, and held it through
   a ~55% mark-to-market decline (Note 10B consol p.260, cross-checked
   against standalone Note 10B which carries no Master Trust FVPL line)

Standalone Note 10(B) (FVPL) has no Master Trust Limited holding at all —
the parent's only Master Trust exposure is the FVOCI stake being wound down
(finding #3 above). Consolidated Note 10(B), however, shows a Master Trust
Limited FVPL position of 21,34,329 shares (` 1,202.48 lakhs) at FY26 versus
21,52,870 shares (` 2,706.16 lakhs) at FY25 — i.e. this FVPL position must
sit entirely at a subsidiary, since it does not appear in the parent's own
schedule. The share count barely moved (down just 18,541 shares, ~0.9%) but
the value fell 55.6% (` 2,706.16 lakhs → ` 1,202.48 lakhs), confirming this
is almost entirely a mark-to-market price decline absorbed while the
position was held, not a disposal. Because this book is FVPL, the ~` 15.04
Cr decline DOES flow through the consolidated P&L (via Note 31 consol "Net
gain on fair value changes"), unlike the parent's FVOCI exit in the same
name. Net effect: the parent is exiting Master Trust Limited exposure while
a subsidiary rode a large loss in the identical stock without trimming the
position — a single-name concentration and risk-discipline question that
sits underneath the group's still-positive aggregate trading gains.

## 5. 🟡 A new Level 3 (illiquid/model-valued) slice appears inside
   "Securities for trade" this year, where none existed in FY25 (Note 53
   standalone p.207-208, fair value hierarchy table)

FY25: Securities for trade ` 17,367.40 lakhs, 100% Level 1 (quoted, liquid).
FY26: Securities for trade ` 24,276.59 lakhs, of which ` 20,973.82 lakhs is
Level 1 but ` 3,302.77 lakhs (13.6%) is now Level 3 (unobservable inputs).
"Securities for trade" is, by definition and by the Company's own stated
trading intent, meant to be the most liquid book on the balance sheet; a
new, meaningful Level 3 slice appearing this year — alongside the
already-known Level 3 investment book (Pass 1's Note 53 finding, unquoted
strategic stakes) — is a distinct and previously unremarked nuance: some of
what is labelled "held for trading" is not, in fact, exchange-quoted.

## 6. 🟡 Two related-party revenue lines collapsed, unexplained (Note 52(iii)
   standalone pp.205-206)

- Brokerage received from Idhyah Futures (an entity under KMP/relative
  control): ` 280.99 lakhs (FY25) → ` 2.26 lakhs (FY26), a 99.2% decline.
  This is the single largest related-party brokerage relationship in the
  disclosed table and its near-total collapse is not explained in the note.
- Consultancy charges paid to Ace Alpha Tech Limited: ` 150.00 lakhs (FY25)
  → nil (FY26); the note explains this entity "ceased to be a related party
  on September 12, 2024," so the FY25 figure reflects a part-year
  relationship that had already ended before FY26 began — a closing item,
  not a new concern, but the ₹150 lakh FY25 consultancy fee to a
  soon-to-exit related party was not previously named.

## 7. 🟢 NBFC segment (Fincap) revenue and profit fell even as its book grew
   and provisioning rose (Note 45 consol pp.286-287, cross-referenced to
   Note 9 consol p.257, already in Pass 1 LBF3/finding set)

NBFC segment revenue: ` 5,552.63 lakhs (FY26) vs ` 5,686.76 lakhs (FY25),
down 2.4%. NBFC segment result (EBIT): ` 2,496.55 lakhs vs ` 2,646.59
lakhs, down 5.7%. NBFC segment liabilities fell sharply, ` 15,134.66 lakhs
→ ` 9,485.55 lakhs (-37.3%), even as the underlying consol gross loan book
(Note 9, largely Fincap-driven beyond parent MTF) grew and impairment
allowance rose 58.9% (already flagged in Pass 1 LBF3). Pass 1 treated the
NBFC book primarily as a credit-risk-concentration point; this pass adds
that the segment's own P&L contribution shrank in FY26, which sharpens Pass
1 finding #2 (parent profit concentration rising to 92.03%): the NBFC arm
is not currently the profit-diversification engine a "subsidiary-led
transition" narrative would need, on this year's numbers.

## 8. 🟢 Minor items closed out cleanly, worth naming for completeness
- Related-party loan to R.A. Maxx Private Limited: ` 185.74 lakhs
  outstanding at FY25, fully repaid, nil at FY26 (Note 9e standalone
  p.158) — a clean closure, not previously named in Pass 1.
- Gratuity financial assumption: salary escalation rate for "other
  employees" (non-trading staff) raised from 10% to 12% (Note 45(iv)
  standalone p.189); the trading-employee rate is unchanged at 10%. A
  modest, disclosed assumption change with a small liability effect,
  not previously noted.

═══════════════════════════════════════════════════════════════════
PASS 2 NEW FINDINGS SUMMARY
═══════════════════════════════════════════════════════════════════
Eight new items found on re-read, none contradicting Pass 1's findings;
all either sharpen an existing Pass 1 concern with a company-disclosed
qualifier (items 1, 2, 7) or add a previously unaddressed note family
(the Investments/fair-value notes, items 3-5) or close out small related
items (items 6, 8). The single most load-bearing new item is #1: the
Company's own footnote that its reported DSCR/consol DSCR excludes the
early NCD redemption it has already resolved to make. This is not a new
risk in substance — Pass 1 already flagged the redemption and the ratio
decline separately — but the footnote is the direct evidentiary link
between the two, and materially strengthens the case that the FY26
reported debt-service coverage is a floor, not a base case, for what the
company will actually face once the redemption executes.
