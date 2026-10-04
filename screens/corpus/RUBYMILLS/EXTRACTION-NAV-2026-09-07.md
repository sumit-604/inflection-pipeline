# RUBYMILLS corpus extraction — NAV / SOTP inputs

- Company: The Ruby Mills Ltd (RUBYMILLS, BSE 503169, CIN L17120MH1917PLC000447).
- Purpose: inputs for a sum-of-the-parts / NAV valuation. Corpus only. Where the
  corpus is silent, "NOT DISCLOSED." No estimate, no inference from outside.
- Extracted 2026-09-07 from `screens/corpus/RUBYMILLS/`. Every number anchors to a
  file and a page or note. Amounts stated as filed. `1 crore = 100 lakh`.
- Convention: FY26 = year ended 31 March 2026 unless a quarter or FY25 is named.

Sources quoted, with dates:
- `annual-report/Annual_Report_2026.txt` — Annual Report FY26 (standalone and
  consolidated), audited, board 28 May 2026.
- `annual-report/Ruby-AR-FY2025.txt` — Annual Report FY25.
- `results/RUBYMILLS-result-20260812-...txt` — unaudited Q1FY27 result, quarter
  ended 30 June 2026, filed 12 August 2026.
- `results/RUBYMILLS-result-20260528-...txt` — Q4FY26 / FY26 audited result.
- `credit-ratings/IndiaRatings-2026-02-16-...txt` — Ind-Ra rationale, 16 Feb 2026.
- `credit-ratings/01-Acuite.txt` and `05-Acuite.txt` — Acuité, 20 Feb 2026, INC.
- `filings/Ruby-33rd-floor-sale-to-Torrent-2026-08-20.txt` — floor sale, 19-20 Aug 2026.
- `filings/Ruby-20260717-Registration-of-Cancellation-Agreement.txt` — DA cancellation.

---

## SECTION 1. ENTITY AND SHARE STRUCTURE

### 1.1 Shares outstanding, face value, dilution
Quote: "Balance as at the end of the year 3,34,40,000 1,672.00" and "The Company
has only one class of shares referred to as equity shares having par value of `5
per share." (AR FY26, note 24, page 122-123.)
Quote: "Weighted average number of shares at 31st March for basic and diluted
earnings per shares (Face Value `5 per share) 334.40 [lakh]." (AR FY26, note 50,
page 147.)
Reading: 3,34,40,000 equity shares of `5 each. No change during the year. Basic
equals diluted, so no warrants, no convertibles, no ESOP dilution is disclosed.
Treat share count as 3.344 crore, fully diluted.

### 1.2 Group structure: which entity holds the tower and the land
Quote: "Name of Subsidiary Ruby Greentech K Private Limited / Ruby Greentech T
Private Limited... The date since when subsidiary was acquired 18th March,2026...
% of shareholding 100.00% / 100.00%... Names of subsidiaries which are yet to
commence operations - Ruby Greentech K Private Limited and Ruby Greentech T
Private Limited." (AR FY26, page 48-49.)
Quote: "(d) Investment property 7 68,084.43" sits in the STANDALONE balance sheet
of the holding company. (AR FY26, page 92.)
Reading: The tower AND the Dadar land sit on the holding company, The Ruby Mills
Ltd, at the standalone level. The two subsidiaries are wholly owned shells,
incorporated 18 March 2026, not yet operating, holding `1 lakh and `83.89 lakh of
total assets. They do not hold the tower or the land. Ruby's ownership in each is
100%.

### 1.3 Non-controlling / minority interest at consolidated level
Quote: both subsidiaries "% of shareholding 100.00%." (AR FY26, page 49.) Auditor:
the two subsidiaries "are not material to the Group." (Q1FY27 result, page 10.)
Reading: both subsidiaries are 100% owned, so there is no minority interest.
NCI = Nil. A separate consolidated-balance-sheet NCI line was not located in the
held text; the 100% ownership makes it Nil by construction.

### 1.4 Standalone vs consolidated Q1FY27 revenue
Operator premise flagged: the question states "standalone Q1FY27 revenue `9.15 Cr
but consolidated `91.5 Cr." The corpus does not support this.
Quote, standalone segment table: "Textiles 5,755.60 / Real Estate and related
3,392.62 / Total 9,148.22." (Q1FY27 result, page 3.)
Quote, consolidated: "Revenue from Operations 9148.22." (Q1FY27 result, page 6.)
Quote, auditor on the subsidiaries: "Group's share of total revenue is Nil."
(Q1FY27 result, page 10.)
Reading: standalone AND consolidated revenue from operations for Q1FY27 are the
same, `9,148.22 lakh = `91.48 crore. The `9.15 Cr figure is a decimal misread of
`91.48 crore (or of "9,148 lakh"). The subsidiaries earn nothing, so consolidated
equals standalone. Both the rent and the textile revenue are earned inside the
holding company. Textiles `57.56 crore, real estate and related `33.93 crore.

---

## SECTION 2. THE RUBY (INVESTMENT PROPERTY)

### 2.1 Built-up / leasable area; retained area after DA cancellation
Quote: "the Company granted the development rights to develop a Tower on 12,204
square meters out of its Freehold Land at Dadar." (AR FY26, KAM, page 91.)
Quote: HDFC LRD is secured on "leased premises of 1,82,348 sq.ft... of the 4th,
7th, 9th, 18th Floors, North East Wing and entire 14th to 16th Floors aggregating
to 1,82,348 sq. ft. area of the building 'The Ruby'." (AR FY26, note 26, page 126.)
Quote, Ind-Ra: "total carpet area of 0.412 million sq ft." (Ind-Ra, 16 Feb 2026.)
Reading: the tower plot is 12,204 sq m of freehold Dadar land. Total carpet area
of The Ruby is 0.412 million sq ft (Ind-Ra). A single figure for Ruby's total
built-up area, and an exact split of retained-versus-transferred area after the
cancellation, is NOT DISCLOSED in the held text. The floors named as loan security
(1,82,348 sq ft plus the 26th-29th floors) are owned by Ruby.

### 2.2 HIGHEST VALUE. Fair value of investment property (Ind AS 40 disclosure)
Quote: "Fair value / Particulars Freehold Land / Buildings / As at 31st March,
2026 7436.25 / 154750.21." (AR FY26, note 7, page 114.)
Quote: "The fair values of the investment property are categorised as level 3 in
the fair valuation hierarchy and has been determined by Ready Reckoner rate as per
local government authority." (Same note.)
Reading: disclosed fair value of the investment property at 31 March 2026 is
`7,436.25 lakh land + `154,750.21 lakh buildings = `162,186.46 lakh = `1,621.86
crore. Prior year fair value was `7,952.48 + `49,364.75 = `57,317.23 lakh (`573.17
crore); the jump is the leased floors coming to Ruby on the settlement. This is a
Ready Reckoner (government circle-rate) value, a conservative floor for Grade A+
Dadar, not a market appraisal. It is the single most important NAV anchor: fair
value `1,621.86 crore against a market value near `1,432 crore (per the card).

### 2.3 Carrying (book) value of the investment property
Quote: "Net Carrying Value / Balance as at 31st March, 2026 553.98 [land]
67,530.45 [buildings] 68,084.43 [total]." (AR FY26, note 7, page 114.)
Quote, movement: "Additions / adjustments - 66,458.06 66,458.06" to buildings
during FY26. (Same note.)
Reading: carrying value `68,084.43 lakh = `680.84 crore (land `5.54 crore,
buildings `675.30 crore). It rose from `30.38 crore a year earlier; `664.58 crore
of building was added in FY26 on the settlement. Fair value `1,621.86 crore sits
`941 crore above carrying value, an unrecognised gain on the cost model.

### 2.4 Rent roll: area, occupancy, tenants, rent per sq ft, lease expiry, FY27 renewal
Quote, Ind-Ra: "the building had 67% occupancy, with total carpet area of 0.412
million sq ft... Long-term contracts with tenants such as Ernst & Young, Cathay
Pacific Airways Limited, DSP Asset Managers Pvt Ltd, which together account for 75%
of total leased carpet area... TRML has a sizable renewal coming up in FY27;
management expects the lease to be rolled over." (Ind-Ra, 16 Feb 2026.)
Quote, Ind-Ra "About the Company": "Key tenants of The Ruby Tower include Cathay
Pacific Airways, IMCD India, DSP Asset Managers, Signet Excipients, and Ernst &
Young." (Same.)
Quote, AR: HDFC LRD escrow is "Rent from M/s. Ernst & Young Services Pvt. Ltd (5th
Floor)." (AR FY26, note 26, page 128.)
Quote, AR contracted rent: "The future minimum lease payments under Non
cancellable lease receivable... Less than one year 9209.50 / Between one to five
years 19017.71." (AR FY26, note 49.B, page 147.)
Reading: occupancy 67%, carpet area 0.412 million sq ft, top three tenants (EY,
Cathay Pacific, DSP) at 75% of leased area, one sizable FY27 renewal, management
expects a roll-over (Ind-Ra). Contracted non-cancellable rent receivable is
`92.10 crore within one year and `190.18 crore across one-to-five years, about
`282 crore contracted. Tenant-by-tenant area, rent per sq ft, and the exact FY27
expiry date and tenant are NOT DISCLOSED in the held text.

### 2.5 Rental income recognised; is Q1FY27 real-estate revenue all recurring
Quote, FY26: "Rental Income derived from Investment Property 5692.02" and "The
amount does not include other amenities charges recovered of `582.68 Lakhs." (AR
FY26, note 7, page 114.)
Quote, Q1FY27 segment: "Real Estate and related 3,392.62" for the quarter versus
"6,632.66" for full FY26. (Q1FY27 result, page 3.)
Quote, note 4: "Due to cancellation of Development Agreement and settlement of
accounts dated 11th December 2025, the figures of Real Estate Segment for the
Quarter ended June 2025 and Year Ended March 2026 are not comparable." (Q1FY27
result, page 2.)
Reading: FY26 rental income from investment property was `56.92 crore, plus `5.83
crore amenities recovered. Q1FY27 real-estate-and-related segment revenue is
`33.93 crore, which annualises far above the `66.33 crore FY26 segment total. The
step-up is the full rent now accruing to Ruby after the December 2025 settlement,
where earlier periods credited part of the rent to the developer. Whether the
`33.93 crore contains a one-time or catch-up item, and its rent-versus-CAM split,
is NOT DISCLOSED in the Q1FY27 filing (no notes accompany the limited review).

### 2.6 History of floor / space sales (realised `/sq ft)
Quote: "the company has sold commercial premises on the 33rd floor of 'The Ruby'
along with the car parking spaces... Consideration received `124.08 Crores...
Buyer: Torrent Pharmaceuticals Limited... Buyer does not belong to the promoter."
(Floor-sale filing, 19-20 Aug 2026.)
Reading: one arm's-length floor sale is documented, the 33rd floor plus parking to
Torrent Pharmaceuticals for `124.08 crore, agreement and completion 19 August 2026.
The floor's carpet area is not stated, so a realised `/sq ft cannot be computed
from the corpus. The earlier Torrent purchase and any Axis Bank floor sale that the
question references are NOT DISCLOSED in the held text.

---

## SECTION 3. DEVELOPMENT-AGREEMENT CANCELLATION

### 3.1 Terms of the cancellation with the developer
Quote: "A Cancellation Agreement has been executed between the Company and the
Developer [Mindset Estates Private Limited] for giving effect to the cessation and
termination of the Development Agreement... The Settlement Agreement constitutes a
full and final settlement between the parties... The Company does not expect any
additional financial impact arising solely on account of the registration...
beyond what has already been appropriately considered in its financial
statements." (DA cancellation filing, 17 July 2026.)
Quote, accounting effect: "Additions / adjustments - 66,458.06" to investment
property buildings, and the FY25 "Other financial assets 13 ... 62,736.81" falling
to "1,710.70" in FY26. (AR FY26, note 7 page 114; balance sheet page 92.)
Reading: the DA with Mindset Estates was cancelled and registered, a full-and-final
settlement via mediation before Justice S. J. Kathawala (Retd.). Ownership of the
leased floors transferred to Ruby at end-December 2025. In the accounts, a `627.37
crore receivable from the developer (FY25 other financial assets) converted into
`664.58 crore of investment-property building. The consideration paid to the
developer, and any residual payable, is not quantified line-by-item in the held
text; the company states no financial impact beyond what is already booked. The
per-item cash consideration is NOT DISCLOSED.

### 3.2 The `250 crore lease-rental-discounting loan (Dec 2024)
Quote: "LRD Loan from Union Bank of India Limited of `25,000.00 lakhs sanctioned
and availed is repayable in 144 monthly instalments to be commenced from January,
2025 [at] 8.25% [outstanding] 24,439.55 [FY26] 14,611.27 [FY25]," secured by "1st
Charge by the way of hypothecation of the future lease rental pertaining to office
premises on 26th floor, to 29th floor at building known as 'The Ruby'... Assignment
of Receivables... Personal guarantee of two promoter directors." (AR FY26, note 26,
page 127.)
Quote, Ind-Ra: "The company availed a lease rental discounting loan of INR2,500
million in December 2024, for making payment towards the development partner and
upgradation of parking, lobby renovation, among others." (Ind-Ra, 16 Feb 2026.)
Reading: the `250 crore (`25,000 lakh) LRD is the Union Bank facility, drawn from
January 2025 at 8.25%, secured on the 26th-29th floor rentals and on two promoter
directors' personal guarantees. Outstanding `244.40 crore at 31 March 2026. Its
purpose was to pay the developer and upgrade the asset (Ind-Ra).

---

## SECTION 4. THE ADJOINING LAND PARCEL (DECISIVE ITEM)

### 4.1 to 4.5 Area, development potential, tenure, book value, separate-or-same plot
Quote: "Beyond the existing commercial development, the Company continues to
actively evaluate the optimal utilisation of its balance land parcel adjoining The
Ruby development... The land parcel carries an estimated development potential of
approximately over a million square feet, providing a rare opportunity to create
large-format Grade A+ commercial real estate... three-road access, proximity to
metro and rail infrastructure." (AR FY26, MD&A, page ~ "Development Potential and
Land Opportunity" section.)
Quote, tower plot: development rights were granted "on 12,204 square meters out of
its Freehold Land at Dadar." (AR FY26, KAM, page 91.)
Quote, carrying value of investment-property land: "Freehold Land ... 553.98" net
carrying; fair value "7436.25." (AR FY26, note 7, page 114.)
Reading, item by item:
- 4.1 Exact area of the adjoining parcel: NOT DISCLOSED. The corpus gives the tower
  plot as 12,204 sq m of Dadar freehold land, not the adjoining parcel's area.
- 4.2 Development potential: "approximately over a million square feet." FSI/TDR
  entitlement figure: NOT DISCLOSED.
- 4.3 Freehold vs leasehold: the Dadar land on which the tower stands is freehold.
  The tenure of the "balance land parcel adjoining" is not separately stated;
  NOT DISCLOSED, though it is described as the company's own balance parcel.
- 4.4 Carrying value of the parcel: NOT DISCLOSED separately. Investment-property
  freehold land carries at `5.54 crore in total (note 7); a separate line for the
  development parcel is not broken out.
- 4.5 Separate parcel or unused FSI on the same plot: the AR language is "balance
  land parcel adjoining The Ruby development," which reads as a distinct adjoining
  parcel rather than unused FSI on the 12,204 sq m tower plot. The corpus does not
  resolve this explicitly, and gives no JDA, approval, or dated monetisation plan.
  Status: "The Company is evaluating the optimal development strategy" (MD&A).
This is the item the NAV upside turns on, and it is the least quantified in the
corpus. A full run must source the parcel area, tenure, FSI, and carrying value
from the land records and the property advisor's note; the held documents do not
carry them.

### 4.6 Textile land at Dhamni / Kharsundi
Quote: "Freehold Land at Dhamni 1 31.80 31.80." (AR FY26, page ~ PP&E schedule.)
Quote: PP&E "Freehold Land ... 491.02" and "Leasehold Land ... 0.93" net carrying.
(AR FY26, note 4, page ~ PP&E, lines for 31 March 2026.)
Quote: "In respect of Freehold Land of Dhamni Unit amounting to `31.80 lacs...the
original title documents deposited with one of the Bank for creation of Mortgage
and later reported by bank as untraceable and informed the Company that FIR and
Newspaper publication have been completed." (AR FY26, note 4.3.)
Reading: the textile land sits in PP&E at `491.02 lakh freehold + `0.93 lakh
leasehold (`4.92 crore total). The Dhamni freehold portion is `31.80 lakh, and its
original title deeds are reported untraceable by the mortgagee bank, a title flag.
The area in acres of the Dhamni and Kharsundi plots is NOT DISCLOSED in the held
text.

---

## SECTION 5. TEXTILE BUSINESS

### 5.1 Textile segment PBIT / EBIT and depreciation
Quote, FY26 audited segment result: "Textiles 3,218.38" profit before tax and
interest; Q1FY27 "Textiles 198.55." (Q1FY27 result, page 3, FY26 and Q1FY27
columns.)
Reading: textile segment PBIT was `32.18 crore in FY26 and `1.99 crore in Q1FY27
(down from `1.82 crore in Q1FY26). Segment depreciation is not split textile-versus
-real-estate in the held results; company-level depreciation was `1,289.47 lakh in
Q1FY27 and `2,488.17 lakh for FY26 (Q1FY27 result page 2). Segment-level
depreciation: NOT DISCLOSED.

### 5.2 Textile segment assets and liabilities
Quote, at 30 June 2026 (standalone): "Segment Assets Textile 29,729.91... Segment
liabilities Textile (5,507.90)... Capital Employed Textile 24,222.02." At 31 March
2026: "Textile 31,519.75 [assets]... (6,901.02) [liabilities]." (Q1FY27 result,
page 3.)
Reading: textile segment assets `297.30 crore, liabilities `55.08 crore, capital
employed `242.22 crore at 30 June 2026 (assets `315.20 crore, capital employed
`246.19 crore at 31 March 2026). Real-estate-and-related segment assets were
`801.34 crore at 30 June 2026, capital employed `267.28 crore.

---

## SECTION 6. NET DEBT AND LIABILITIES

### 6.1 Total borrowings
Quote, 31 March 2026 balance sheet: "Borrowings 26 33,278.84" non-current and
"Borrowings 32 3,992.22" current. (AR FY26, page 92.)
Quote, reconciliation: "Total Borrowings ... 37,271.06." (AR FY26, page 92
movement.)
Reading: total borrowings at 31 March 2026 were `37,271.06 lakh = `372.71 crore
(non-current `332.79 crore, current `39.92 crore). Dominated by two LRD loans on
the tower: Union Bank `244.40 crore (floors 26-29) and HDFC `101.80 crore. At the
latest quarter-end, 30 June 2026, borrowings are NOT DISCLOSED: the Q1FY27 limited
review carries only the profit statement and the segment table, no balance sheet.

### 6.2 Cash, bank balances, current investments
Quote, 31 March 2026: "Cash and cash equivalents 19 871.45 / Bank balances other
than (iii) above 20 511.98 / Investments [current] 17 4,637.19 / Investments
[non-current] 11 6,880.42." (AR FY26, page 92.)
Reading: cash and equivalents `8.71 crore, other bank balances `5.12 crore, current
investments `46.37 crore, together `60.20 crore of near-liquid resources.
Non-current investments `68.80 crore include the two subsidiaries, unlisted FVTPL
shares, mutual funds and government securities. Net debt is therefore roughly
`372.71 crore less about `60 crore, near `313 crore, consistent with Ind-Ra's
net-leverage view. At 30 June 2026 these balances are NOT DISCLOSED.

### 6.3 Lease liabilities (Ind AS 116)
Quote, 31 March 2026: "Lease Liability 27 220.32" non-current and "Lease
Liabilities 33 13.11" current. (AR FY26, page 92.)
Reading: lease liabilities as lessee total `233.43 lakh = `2.33 crore. Small,
immaterial to net debt.

### 6.4 Have the `124.08 crore Torrent proceeds been received and deployed
Quote: "Consideration received from such sale/disposal `124.08 Crores... Expected
date of completion of sale/disposal August 19, 2026." (Floor-sale filing, 19-20 Aug
2026.)
Reading: the sale agreement and completion are dated 19 August 2026, after the
31 March 2026 accounts and after the 30 June 2026 quarter. So the `124.08 crore is
not in any held financial statement. Whether the cash was received and how it was
deployed (debt repayment or cash) is NOT DISCLOSED in the corpus. It is a
post-period event that a full run must confirm from the H1FY27 result.

---

## SECTION 7. CONTINGENCIES AND CLAIMS

### 7.1 Contingent-liabilities note in full (FY26)
Quote: "In respect of Income tax matters 1529.14 / In respect of GST matters 90.65
/ Excise, service tax and customs matters 286.04 / FEMA 14.00 / Claim against
Company in Labour Matters 130.65 / Claim against the Company by ex employees...
Not ascertainable / Bank Guarantees 569.43." Capital commitments net `2,366.16
lakh. (AR FY26, note 56, page 156.)
Reading: contingent liabilities FY26: income tax `15.29 crore, GST `0.91 crore,
excise/service/customs `2.86 crore, FEMA `0.14 crore, labour `1.31 crore, one
ex-employee claim not ascertainable, bank guarantees `5.69 crore. Quantified total
about `26.20 crore. Net capital commitment `23.66 crore. There is also an inter-
corporate deposit of `1,375 lakh (`13.75 crore) to Jambavati Project Realty Two LLP
at 15% (note 57), and a strategic investment partnership with Isprava for Alibaug
luxury second homes (MD&A) worth noting for related-party and diversification.

### 7.2 The Enforcement Directorate attachment
Quote, Ind-Ra: "The ED attached bank balances worth approximately INR26 million of
TRML at end-October 2025, linked to a 2012 transaction with Rajput Retail Ltd.
While the company returned the principal amount, the ED claims interest earned on
related term deposits is proceeds of crime, which TRML is contesting." Positive
rating trigger: "resolution of the outstanding governance issue." (Ind-Ra, 16 Feb
2026.)
Reading: the ED attached about `2.6 crore of bank balances at end-October 2025, on
a 2012 Rajput Retail matter; the interest on related deposits is alleged proceeds
of crime; Ruby is contesting. Ind-Ra makes its resolution the key positive trigger.
Flag: the AR FY26 contingent-liabilities note does NOT disclose this ED matter. It
appears only in the Ind-Ra rationale. A full run should reconcile that gap.

### 7.3 Capital-gains-tax provision on the floor sales
Reading: NOT DISCLOSED. No capital-gains provision or liability tied to a floor
sale is stated in the held text. The Torrent sale is a post-period event (19 Aug
2026) with no accounting entry in the corpus.

### 7.4 Promoter / related-party claim or encumbrance on the real-estate assets
Quote: every LRD and term loan on The Ruby carries "Personal guarantee of two
promoter directors of the Company." (AR FY26, note 26, pages 126-128.)
Reading: the tower's debt is personally guaranteed by two promoter directors, and
each loan is secured by a registered mortgage on named floors plus a rent escrow on
which the lender holds a charge. So the real-estate assets are encumbered to the
lenders, and the promoters carry personal guarantees. No promoter claim of
ownership over the assets is disclosed. The Dhamni freehold-land title deeds are
reported untraceable by the mortgagee bank (note 4.3), a separate title flag.

---

## VERIFICATION

- Section 1: AR FY26 (notes 24 page 122-123, note 50 page 147, subsidiary statement
  page 48-49, balance sheet page 92); Q1FY27 result 12 Aug 2026 (pages 3, 6, 10).
  Figures FY26 and Q1FY27 (quarter ended 30 June 2026).
- Section 2: AR FY26 note 7 (pages 114-115), note 26 page 126, note 49.B page 147,
  MD&A; Ind-Ra 16 Feb 2026; floor-sale filing 19-20 Aug 2026. FY26 and FY25 for the
  fair-value and carrying tables; Q1FY27 for segment revenue.
- Section 3: DA cancellation filing 17 July 2026; AR FY26 note 26 page 127; Ind-Ra
  16 Feb 2026; AR FY26 balance sheet page 92. FY26.
- Section 4: AR FY26 MD&A, KAM page 91, note 7 page 114, note 4 and note 4.3 (PP&E).
  FY26.
- Section 5: Q1FY27 result page 3 (segment, FY26 and Q1FY27 columns). FY26 and
  Q1FY27.
- Section 6: AR FY26 balance sheet page 92, movement schedule; Q1FY27 result (no
  balance sheet). FY26; quarter-end figures NOT DISCLOSED. Floor-sale filing 19-20
  Aug 2026.
- Section 7: AR FY26 note 56 page 156, note 57, note 4.3, note 26 pages 126-128;
  Ind-Ra 16 Feb 2026. FY26, except the ED matter (Ind-Ra, end-October 2025) which
  the AR does not carry.
