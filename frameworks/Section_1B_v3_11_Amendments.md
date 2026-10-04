# SECTION 1B v3.11 AMENDMENTS — POST-IPO ROCE, EARNED SOTP SLICES, HURDLE BASIS, SEVEN CAP ROWS

*Version 3.11 | issued 16 September 2026. Operator ruling 16-Sep-2026, Keerti Kaushik. Carries one amendment, Amendment 27, in four parts. Layers on top of Section 1B v3.3 + v3.3 Amendments + v3.5.1 + v3.6 + v3.7 + v3.8 + v3.9 (Amendments 20-25) + v3.10 (Amendment 26). This file does not modify any prior file in place, with one exception: the seven rows of 27.4 are also logged in the Master Prompt Section 1B Sector Reality Cap table with this amendment's date and number. Where they overlap on items named here, v3.11 governs, then v3.10, then v3.9, then v3.8, then v3.7, then v3.6, then v3.5.1, then v3.3. Stage 11 reads this through the section-1b skill. Amendment numbering continues from v3.10, whose last amendment is 26.*

*Origin: the 16-Sep-2026 mining pass over LESSONS_ARCHIVE.md. Four failures recurred across runs and were settled ad hoc each time. Post-IPO names had Pillar 1 computed on ROCE diluted by issue cash (EBGNG, AMAGI). SOTP slices carried plucked round-number multiples, or inherited drag from another slice (KCPSUGIND, PERMAGNET). A Hurdle Ratio PASS credited one catalyst twice (INDGN). Seven sectors had no cap row and were ruled ad hoc company by company (SHYAMMETL, MANINDS, KCPSUGIND, ENTERO, BORANA, AIMTRON, FRATELLI, UFBL). Amendment 27 converts each ad hoc ruling into one rule.*

---

## AMENDMENT 27 — GROUP 3 PROMOTIONS

`[v3.11: adds a Pillar 1 basis for names within 24 months of listing (27.1); requires every SOTP slice to earn its multiple (27.2); enforces Amendment 18.1 at the Hurdle Ratio step (27.3); adds seven rows to the sector cap table (27.4) — operator ruling 16-Sep-2026]`

### 27.1 POST-IPO OPERATING ROCE (Pillar 1)

**The distortion.** An IPO puts a large cash balance into capital employed on listing day. Reported ROCE falls, but the operating business has not changed. On AMAGI about 80% of capital employed was idle issue cash: reported ROCE read about 5%, while operating capital earned about 20% to 40%. On EBGNG only about 4 of the 14 points of reported ROCE decline was idle cash; the rest was issue money already deployed into working capital. Pillar 1 on reported ROCE prices the cash pile, not the business.

**The rule.** For any company within 24 months of its listing date at the run date:

1. Pillar 1 uses OPERATING ROCE. Surplus cash is excluded from capital employed.
2. The treasury income the surplus cash earns is excluded from EBIT, so the numerator and the denominator stay on one basis (the consolidated Amendment 9 Route A consistency rule).
3. The surplus cash is added to fair value as a separate line, at face value.

The listing date is `manifest.listed_date`; where that is blank, the listing date in the offer document or the exchange listing notice. From month 25 the company returns to the ordinary Pillar 1 rules.

**Surplus cash.** Cash, bank balances and liquid investments, LESS each of:

- unspent issue proceeds earmarked for the objects of the issue in the offer document, per the latest monitoring agency report where one exists;
- cash the filings tie to operations: margin money, and lien-marked or escrow deposits;
- cash the Section 2 base case spends: capex, acquisitions, or a working-capital build.

Each deduction carries its filing anchor. Earmarked unspent proceeds are not surplus cash: they stay idle raised capital under consolidated Amendment 9 Route A. The Route A selection test runs on the capital employed left after the 27.1 strip, so no rupee is stripped twice.

**Single credit.** Surplus cash is credited once, at face value. It is never also credited as earnings:

- The EPS the destination PE multiplies excludes the after-tax treasury income on the surplus cash.
- Fair value carries two lines: operating fair value, and surplus cash per share at face value, on the same diluted share count the EPS uses. The cash line is never grown, discounted or multiplied.
- The tier hurdle discount applies to the operating line only: entry = operating Year N fair value ÷ (1 + tier hurdle)^N + surplus cash per share. Discounting the cash line would carry the cash below its face. The same holds for every price derived from fair value: the 30% CAGR price and the margin-of-safety price apply their discount to the operating line, then add the cash line.
- Net debt, or net cash, used anywhere in fair value excludes the surplus cash. The cash enters fair value through its own line only.
- The Current PE in the Hurdle Ratio is (CMP − surplus cash per share) ÷ the EPS above (27.3).
- On the Amendment 19 fair-value path the cash line is a constant, added at each year-end row and never compounded. The FV CAGR is computed on the total (operating line plus cash line). The 19.3 decomposition line names the cash line within the static fraction of fair value.

**Worksheet line.** "Post-IPO operating ROCE (A27.1): listed ___ (___ months at run date) | cash and liquid investments ₹___ Cr | less earmarked proceeds ₹___ Cr, encumbered ₹___ Cr, base-case spend ₹___ Cr | surplus cash ₹___ Cr (₹___/share) | treasury income excluded ₹___ Cr | operating ROCE ___% vs reported ___% | Route A test on residual capital employed: ___"

### 27.2 SOTP SLICES EARN THEIR MULTIPLE

**The distortion.** On KCPSUGIND stage 11 carried the Eimco slice at 8x, a round number the devil's advocate and Verifier C both flagged as plucked. The operator re-ruled it to 15x after close, and the whole-company verdict moved two bands on that one number. On PERMAGNET the core slice took Pillar 1 from consolidated ROCE while the loss-making subsidiary sat in its own slice, so the subsidiary's drag was counted twice.

**The rule.** Every slice in a sum-of-parts valuation takes its multiple in one of two ways, and no other:

1. **Its own three-pillar derivation.** Pillar 1 on the slice's own ROCE, Pillar 2 on the slice's own cash conversion, Pillar 3 on the slice's own growth visibility, then the slice's own sector cap row. The slice runs rows A to H of the summary on its own figures.
2. **The Amendment 17 CONVERTER multiple**, where the slice classifies CONVERTER under 17.0. Amendment 17 sets inputs, not a number: the converter multiple is the destination PE the slice earns when its pillars run on the Amendment 17 inputs (through-cycle ROCE under 17.1, volume-denominated working capital under 17.2).

No slice carries a round number. No slice takes a peer multiple, a multiple inherited from another slice, or the core multiple.

**BOO / annuity slices (open ruling OR-10).** Until the operator rules OR-10, a BOO or annuity slice of a hybrid annuity-EPC business keeps the FTTCP hybrid annuity-EPC treatment as written: the InvIT-style EV/EBITDA multiple and the blended cap. The worksheet names OR-10 on that slice. Every other slice follows this part.

- The worksheet states each slice's pillar rows.
- A slice's inputs come from that slice's own disclosed figures. Where the figures are not separately disclosed, the input is NOT FOUND. A slice that cannot run its derivation and does not classify CONVERTER is carried as an unresolved input, named, and takes no multiple. Its slice value is NOT FOUND. The SOTP total is shown without that slice, the gap is named, and the verdict card carries the caveat.
- A slice quarantined with its own losses and debt leaves the core slice's Pillar 1 inputs. The core slice runs on core ROCE, never on consolidated ROCE.
- UA qualifiers are tested once, at company level, and apply to each slice's raw PE.
- A Strategic Premium sits only in the slice that owns the scarce asset (single credit).

**Worksheet line, per slice.** "Slice ___ | basis: [THREE-PILLAR / CONVERTER] | A: ROCE ___% (slice figures, source ___) → ___x | B: cash multiplier ___x | C: ___x | D: +___x | E: +___x (owns the scarce asset: Y/N) | F: ___x | F2: ___x | G: cap row ___ at ___x | G2: override Y/N | G3: ___x | H: ___x | slice PAT ₹___ Cr | slice value ₹___ Cr"

### 27.3 ONE BASIS, BOTH ENDS, AT THE HURDLE RATIO

**The distortion.** On INDGN the entry basis was forward and the destination multiple was also forward. An unproven margin recovery was credited in the forward EPS and again in the forward destination multiple. The Hurdle Ratio read PASS. Rebuilt on the no-recovery bear EPS it read 1.56 against the 1.728 threshold. The PASS existed only because one catalyst was credited twice. Amendment 18.1 already required one earnings basis at both ends of the exit price; nothing enforced it at the Hurdle Ratio step.

**The rule.** This part enforces Amendment 18 at the Hurdle Ratio step. It replaces the v3.8 interaction note that 18.1 does not alter the Hurdle Ratio inputs beyond the exit term: every Hurdle Ratio term now runs on the one basis.

1. **One basis.** The EPS basis used for the entry price is the basis used for the exit price, stated in the worksheet line. EPS CAGR, Destination PE mid and Current PE in the Hurdle Ratio all run on that one basis. A forward basis takes Current PE on forward EPS; a trailing basis takes it on trailing EPS.
2. **One credit.** A catalyst credited in the revenue path (26.1) or in the margin bridge (26.2) is not credited again in the exit multiple. Where the Amendment 26 interaction splits a catalyst between the projection and the exit multiple, the two shares sum to no more than 100% of that catalyst's credit, and the worksheet names both.
3. **Surplus cash.** For a name under 27.1, Current PE runs on price less surplus cash per share.

The basis line and the catalyst credit line are written before the Hurdle Ratio is computed. A Hurdle Ratio shown without both lines is incomplete.

**Worksheet line.** "Hurdle basis (A27.3): [FORWARD / TRAILING], same at entry and exit (A18.1) | Current PE ___x = (CMP ₹___ − surplus cash ₹___/share) ÷ [forward / trailing] EPS ₹___ | EPS CAGR ___% | Destination PE mid ___x | Catalysts: [name: revenue path or margin bridge ___% / exit multiple ___%] × N, each summing to no more than 100%"

### 27.4 SEVEN SECTOR CAP ROWS

Seven rows join the Section 1B Sector Reality Cap table:

| Sector | Maximum exit PE | Closes the ad hoc ruling |
|---|---|---|
| Steel / integrated metals | 15x | SHYAMMETL 19-Jul-2026, ruled 20x; MANINDS 25-Aug-2026, line pipe ruled 20x on that precedent |
| Sugar / agri-commodity | 18x | KCPSUGIND 21-Jul-2026, ruled Agri processing 20x |
| Distribution / trading | 20x | ENTERO 30-Aug-2026, ruled 18-20x |
| Commodity textiles | 18x | BORANA 07-Sep-2026, ruled Recycling / Manufacturing 25x |
| EMS | 30x | AIMTRON 12-Jul-2026, ruled Recycling / Manufacturing 25x |
| Alcoholic beverages | 35x | FRATELLI 07-Sep-2026, ruled Branded apparel / FMCG 35x |
| QSR | 40x | UFBL 05-Aug-2026, ruled Branded apparel / FMCG 35x |

- The rows behave like every other cap row. Each is absolute absent a qualified Category-Break Override; the UA multiplier cannot breach it; Amendment 17 neither raises nor lowers it.
- Stage 0 resolves a company's row against the full table, these rows included.
- A company earlier ruled ad hoc into another row takes its new row from its next run. The ad hoc cap is not carried forward. No company is revalued on adoption.

**Row boundaries.**

- "Sugar / agri-commodity: revenue dominated by one commodity with regulated or exchange-traded pricing. Agri processing: output branded or multi-product."
- "Cybersecurity / VAD: distribution with vendor certifications, bundled services and enterprise contracts. Distribution / trading: pure buy-and-sell with no service layer."

---

## INTERACTION WITH THE REST OF THE FRAMEWORK

- **FTTCP ROCE selection table and Pillar 1 route table.** For a name under 27.1, every reference to current, expected or statutory ROCE reads operating ROCE, and the FTTCP ROCE forward verdict is formed on the operating series. Both ends of any blend stay on one basis (consolidated Amendment 9.1).
- **Consolidated Amendment 9 (Pillar 1 normalization).** 27.1 strips surplus cash first. Route selection then runs on the residual capital employed. Earmarked issue proceeds stay under Route A as idle raised capital, subject to the 9.2 staleness rule.
- **Amendment 4 (single credit).** 27.1 credits surplus cash once, at face value; 27.2 credits each slice's quality in its own slice only; 27.3 credits each catalyst once across the revenue path, the margin bridge and the exit multiple.
- **Amendment 17 (converters).** A CONVERTER slice under 27.2 takes the converter multiple. The seven 27.4 rows price their sectors through the cycle, as every cap row does.
- **Amendment 19.** Under 27.1 the surplus cash line is a constant on the fair-value path, never compounded; the FV CAGR runs on the total.
- **Amendment 18.** 27.2 defines the "slice's OWN destination multiple" that 18.3 applies at a SUCCESS exit. 27.3 enforces 18.1 at the Hurdle Ratio step and replaces the v3.8 note that limited 18.1 to the exit term. The 18.2 Option Resolution Calendar is unchanged.
- **Amendment 20 Step 1C (relative valuation cross-check).** Step 1C cross-checks the earned company-level multiple. It never sources a slice multiple, so 27.2 does not conflict with it.
- **Amendments 20.6 and 20.7 (cap maintenance).** 27.4 adds rows and draws two row boundaries by operator ruling. It changes no existing cap value, so the 20.7 annual review remains the only channel that moves an existing cap. The 27.4 rows are logged in the Master cap table with this amendment's date and number, and from the next annual review they are reviewed against live peer medians, as every row is.
- **Amendments 21 to 24.** The A21 run-rate base and the A22 probability-weighted EPS CAGR run on the 27.3 basis. The Hurdle Ratio stays a feasibility check under Amendment 24 (operator ruling 15-Sep-2026, OR-2).
- **Amendment 26.** 27.3 keeps the 26.1 / A22 split, extends the single-credit rule to the 26.2 margin bridge, and bounds any split at 100% of a catalyst's credit.
- **FTTCP hybrid annuity-EPC rule.** Unchanged by this amendment. Its BOO / annuity slice treatment (InvIT-style EV/EBITDA multiple, blended cap) is carried as written until OR-10 is ruled (27.2).

## VERSION HISTORY

| Version | Date | Changes |
|---|---|---|
| 3.8 | 23-Aug-2026 | (prior) Amendments 18-19, exit-basis symmetry, option resolution, and FV-CAGR classification. See `Section_1B_v3_8_Amendments.md`. |
| 3.9 | 26-Aug-2026 | (prior) Amendment 20, relative valuation cross-check (new step 1C). See `Section_1B_v3_9_Amendments.md`. |
| 3.9 (reissue) | 07-Sep-2026 | (prior) Amendments 21-25, forward-expectation exit framework. See `Section_1B_v3_9_Amendments.md`. |
| 3.10 | 08-Sep-2026 | (prior) Amendment 26, growth symmetry in projections and weighting. See `Section_1B_v3_10_Amendments.md`. |
| 3.11 | 16-Sep-2026 | Amendment 27, operator rulings of 16-Sep-2026. 27.1: Pillar 1 on operating ROCE ex surplus cash for names within 24 months of listing, surplus cash defined, added to fair value at face value once, outside every discount, and held constant on the Amendment 19 path. 27.2: every SOTP slice runs its own three-pillar derivation or takes the Amendment 17 CONVERTER multiple; no round numbers; pillar rows stated per slice; a NOT FOUND slice leaves the SOTP total with a named gap and a verdict-card caveat. 27.3: one EPS basis at entry, exit and every Hurdle Ratio term; a catalyst credited in the revenue path or the margin bridge is not credited again in the exit multiple; a split is capped at 100%. 27.4: seven cap rows added (Steel / integrated metals 15x, Sugar / agri-commodity 18x, Distribution / trading 20x, Commodity textiles 18x, EMS 30x, Alcoholic beverages 35x, QSR 40x), closing eight ad hoc rulings across seven sectors, with two row boundaries (Sugar / agri-commodity vs Agri processing; Cybersecurity / VAD vs Distribution / trading); no company revalued on adoption. |
