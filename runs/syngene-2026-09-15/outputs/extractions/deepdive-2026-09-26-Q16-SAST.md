# SYNGENE deep-dive extraction, Q16: the four scanned SAST filings (OCR)

Run: runs/syngene-2026-09-15 | Extracted 2026-09-26 by Claude Code
Method: each PDF rendered at 144 dpi and read by RapidOCR. OCR text: work/extracted/announcements/SAST_OCR_4_filings.txt. Page images: work/sast_png/. The 2026-02-17 page 2 figures were checked against the page image.

CORRECTION TO EARLIER CHAT: none of the four filings is by Biocon (the promoter). All four are mutual-fund disclosures. The Biocon stake change from 54.72% (Jun-2024) to 52.59% (Jun-2026) in the screener table is NOT explained by these filings.

## Summary table

| Filing (file, date) | Who | Regulation | Direction | Shares in the transaction | Before | After | Period / date | Mode |
|---|---|---|---|---|---|---|---|---|
| 2026-02-17_SAST-29-1.pdf, 17-Feb-2026 | Nippon India Mutual Fund (through Nippon Life India Trustee Ltd A/c) | 29(1), crossing 5% | Acquisition | 5,74,635 | 1,98,96,140 | 2,04,70,775 (5.0804%) | Purchases 29-Jul-2015 to 13-Feb-2026 | Open market |
| 2026-04-10_SAST-29-1.pdf, 09-Apr-2026 (filed 10-Apr) | DSP Trustee Pvt Ltd for DSP Mutual Fund schemes; PACs DSP AIF and DSP Global Funds ICAV | 29(1), crossing 5% | Acquisition | 9,93,389 (0.24%) | 1,92,92,837 (4.79%) | 2,02,86,226 (5.03%) | 07-Apr-2026 | Open market |
| 2026-04-15_SAST-29-2.pdf, 15-Apr-2026 | Nippon India Mutual Fund | 29(2) | Acquisition | 16,00,307 (0.3972%) | 2,70,76,264 (6.7197%) | 2,86,76,571 (7.1168%) | Purchases 16-Feb-2026 to 10-Apr-2026 | Open market |
| 2026-07-22_SAST-29-2.pdf, 22-Jul-2026 | Mirae Asset Mutual Fund | 29(2) | SALE | 8,61,450 (0.21%) | 41,21,941 (1.02%) | 32,60,491 (0.81%; 0.80% diluted) | 21-Jul-2026 | Open market |

Every acquirer answered "No" to "Whether the acquirer belongs to Promoter/Promoter group".

## Quotes, then comment

1. Nippon, 17-Feb-2026 (2026-02-17_SAST-29-1.pdf p.2-3)
- Quote (p.2): "Before the acquisition under consideration ... a) Shares carrying voting rights 1,98,96,140 2.4689 2.4689" and "a) Shares carrying voting rights acquired 5,74,635 2.6115 2.6115".
- Quote (p.3): "After the acquisition ... 2,04,70,775 5.0804 5.0804"; "Purchase Transactions entered into during the period: From: July 29, 2015 to February 13, 2026"; share capital "40,29,39,420 shares".
- Comment: the share counts add up (1,98,96,140 + 5,74,635 = 2,04,70,775) and 5.0804% matches 2,04,70,775 / 40,29,39,420 (computed). The "before" and "acquired" percentages as printed (2.4689%, 2.6115%) do NOT match their share counts: 1,98,96,140 / 40,29,39,420 = 4.94% (computed), and 5,74,635 is 0.14% (computed). This is a drafting error in the filing, confirmed against the page image, not an OCR error.

2. DSP, 09-Apr-2026 (2026-04-10_SAST-29-1.pdf p.1-3)
- Quote (p.1): "schemes of DSPMF ... have acquired 9,93,389 shares of Syngene International Limited (Company) on April 07, 2026 due to which the shareholding of schemes has increased to 5.03% of the paid-up capital".
- Quote (p.2): before "1,92,92,837 4.79%"; acquired "9,93,389 0.24%"; after "2,02,86,226 5.03%".
- Comment: internally consistent.

3. Nippon, 15-Apr-2026 (2026-04-15_SAST-29-2.pdf p.1-3)
- Quote (p.1): "we have purchased shares of "SYNGENE INTERNATIONAL LIMITED" (on behalf of Nippon India Mutual Fund)".
- Quote (p.2): before "2,70,76,264 6.7197"; acquired "1,600,307 0.3972"; after "2,86,76,571 7.1168".
- Quote (p.3): "Purchase transactions entered into during the period: From February 16, 2026 to April 10, 2026".
- Comment: arithmetic holds within this filing. Across filings it does not: the 17-Feb filing put Nippon at 2,04,70,775 shares after 13-Feb-2026, while this filing's "before" is 2,70,76,264 for purchases starting 16-Feb-2026. The 66,05,489-share gap (computed) is not explained in either filing.

4. Mirae, 22-Jul-2026 (2026-07-22_SAST-29-2.pdf p.1-3)
- Quote (p.1): "disclosure under Regulation 29 (2) ... for the sale made on July 21, 2026".
- Quote (p.2-3): before "4121941 1.02"; sold "-861450 -0.21"; after "3260491 0.81 0.80"; share capital "403669147"; diluted "405250610".
- Comment: this is a sale by a holder at 1.02%, below the usual 2% change trigger for 29(2). The share capital figure of 40,36,69,147 is higher than the 40,29,39,420 in the earlier filings, consistent with ESOP or PSU allotments between April and July 2026 (the 29-Apr-2026 "Allotment" announcement is in the BSE list). The allotment detail is NOT IN CORPUS (filing 2026-04-29 "Allotment" not downloaded).

## What these filings establish

- Institutional buying by domestic mutual funds through Feb to Apr 2026 (Nippon to 7.12%, DSP to 5.03%), consistent with the screener table's DII rise to 28.01% at Jun-2026 (SECONDARY source).
- One small mutual fund sale in Jul-2026 (Mirae, 0.21%) on 21-Jul-2026, eight days before the 29-Jul-2026 Q1FY27 results.
- Nothing about Biocon. No pledge or encumbrance appears in any of the four.

## NOT DISCLOSED / NOT IN CORPUS (Q16)

- Biocon's own stake sales between Jun-2024 and Jun-2026: NOT IN CORPUS. Would be found in Biocon's SAST Reg 29(2) filings on BSE/NSE for Syngene (scrip 539268) in that window, or Biocon's own Reg 30 filings. Earlier chat said the SAST scans likely held these; that was wrong.
- Reason for the Nippon 66,05,489-share gap between the Feb and Apr filings: NOT DISCLOSED. Would need Nippon's scheme-level disclosures or the BSE shareholding pattern (Mar-2026 quarter).
- Allotment on 29-Apr-2026 (share-capital increase): NOT IN CORPUS. BSE announcement 29-Apr-2026 "Allotment" (attachment d935f509-80f7-4032-8599-93b121a5d789.pdf).

## SOURCES QUOTED

- inputs/announcements/2026-02-17_SAST-29-1.pdf (Nippon Life India AMC, 17-Feb-2026)
- inputs/announcements/2026-04-10_SAST-29-1.pdf (DSP Trustee, 09-Apr-2026)
- inputs/announcements/2026-04-15_SAST-29-2.pdf (Nippon Life India AMC, 15-Apr-2026)
- inputs/announcements/2026-07-22_SAST-29-2.pdf (Mirae Asset Investment Managers, 22-Jul-2026)
