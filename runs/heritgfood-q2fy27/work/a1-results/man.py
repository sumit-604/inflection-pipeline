import json
rows=json.load(open('work/a1-results/numrows.json'))
n=len(rows)
out=list(rows)
cnt={'NUMBER':0,'ENTITY':0,'FORWARD':0,'DATE':0,'QUALIFIER':0}
def add(pg,ln,typ,val,ctx,flag=''):
    global n; n+=1
    out.append((typ,'R%03d | page %d | line %d | %s | %s | %s%s'%(n,pg,ln,typ,val,ctx,(' | '+flag) if flag else '')))
N='NUMBER';E='ENTITY';D='DATE';Q='QUALIFIER'
for r in [
(1,19,N,'99-26','letter reference number SECT: STOC: 99-26'),
(1,28,N,'519552','BSE scrip code'),
(1,44,N,'11:30 am (IST)','board meeting commencement time'),
(1,45,N,'02:50 pm (IST)','board meeting conclusion time'),
(1,60,N,'FCS-6317','company secretary membership number'),
(6,348,N,'69.33 million','exceptional items FY26 incl GST refund (note 4a, standalone)'),
(6,348,N,'61.54 million','of which for quarter and six months ended 30 Sep 2025'),
(6,349,N,'32.02 million','interest accrual reversed, quarter ended 30 Sep 2025 (standalone)'),
(6,351,N,'5.37 million','impairment provision on investment in Heritage Novandie Foods (note 4b)'),
(6,364,N,'00003741','DIN of N. Bhuvaneswari'),
(7,439,N,'001076N/N500013','auditor firm registration number'),
(8,449,N,'26206931BEPWMN9300','UDIN standalone review report'),
(8,448,N,'206931','auditor partner membership number'),
(13,773,N,'69.33 million','exceptional items FY26 incl GST refund (note 4, consolidated)'),
(13,773,N,'61.54 million','of which for quarter and six months ended 30 Sep 2025 (consolidated)'),
(13,775,N,'32.02 million','interest accrual reversed, quarter ended 30 Sep 2025 (consolidated)'),
(15,863,N,'156.48 million','unreviewed subsidiary total assets at 30 Sep 2026'),
(15,864,N,'142.62 million','unreviewed subsidiary total revenues, quarter ended 30 Sep 2026'),
(15,864,N,'338.35 million','unreviewed subsidiary total revenues, six months ended 30 Sep 2026'),
(15,864,N,'10.82 million','unreviewed subsidiary net loss after tax, quarter'),
(15,865,N,'11.76 million','unreviewed subsidiary net loss after tax, six months'),
(15,865,N,'10.82 million','unreviewed subsidiary total comprehensive loss, quarter'),
(15,865,N,'11.76 million','unreviewed subsidiary total comprehensive loss, six months'),
(15,866,N,'3.95 million','unreviewed subsidiary net cash outflows, period ended 30 Sep 2026'),
(15,889,N,'26206931TTBWQF2267','UDIN consolidated review report'),
(2,112,N,'face value of Rs 5 each (text reads s each)','equity share face value, standalone P&L row 10','OCR_NOISE'),
(9,518,N,'face value of Rs 5 each (text reads f5 each)','equity share face value, consolidated P&L row 14','OCR_NOISE'),
]:
    add(r[0],r[1],r[2],r[3],r[4],r[5] if len(r)>5 else '')
for pg,ln,v,c in [
(1,23,'BSE Limited','stock exchange addressee'),(1,24,'National Stock Exchange of India Limited','stock exchange addressee'),
(1,28,'HERITGFOOD','NSE scrip code'),(1,50,'Heritage Foods Limited','issuer / registrant'),
(1,58,'Umakanta Barik','company secretary and compliance officer'),
(1,38,'Audit Committee','reviewed and recommended results'),
(1,40,'Statutory Auditors','limited review of results'),
(2,67,'CIN L15209TG1992PLC014332 (text garbled)','company CIN'),
(3,128,'Dairy segment','reportable segment standalone'),(3,137,'Renewable energy segment','reportable segment'),
(6,344,'CODM (Chief Operating Decision Maker)','segment evaluator, note 3'),
(6,345,'Dairy','reportable segment, note 3'),(6,345,'Renewable energy','reportable segment, note 3'),
(6,351,'Heritage Novandie Foods Limited (HNFL)','investee, impairment provision (formerly Heritage Novandie Foods Private Limited)'),
(6,348,'Flavoured milk (GST classification matter)','product in GST refund'),
(6,362,'N. Bhuvaneswari','Vice Chairperson and Managing Director'),
(7,375,'Walker Chandiok & Co LLP','statutory auditor'),
(8,446,'Sumesh E S','audit partner'),
(10,549,'Feed segment','reportable segment consolidated'),
(13,770,'Feed','reportable segment, note 3 consolidated'),
(13,777,'Heritage Novandie Foods Limited','controlling interest acquired, previously a joint venture'),
(14,820,'Heritage Foods Limited (Holding Company)','consolidating parent'),
(16,908,'Heritage Nutrivet Limited','subsidiary'),(16,909,'Heritage Novandie Foods Limited','subsidiary'),
(16,910,'Peanut Butter and Jelly Limited','subsidiary'),(16,913,'SKIL Raigam Power (India) Limited','associate'),
(15,862,'one unreviewed subsidiary (unnamed)','subsidiary results not reviewed by its auditors'),
(2,123,'ISO 22000 certified company; FSMS 002','certification line in page footer (repeats pages 3-6, 9-13)'),
]:
    add(pg,ln,E,v,c)
for pg,ln,v,c in [
(1,19,'October 15, 2026','letter / board meeting date'),(1,34,'October 7, 2026','earlier continuation letter date'),
(1,37,'quarter and six months ended September 30, 2026','results period'),
(2,73,'30.09.2026, 30.06.2026, 30.09.2025, 31.03.2026','standalone P&L column period ends'),
(4,179,'30 September 2026; 31 March 2026','standalone balance sheet dates'),
(5,254,'six months ended 30 Sep 2026 / 30 Sep 2025; year ended 31 Mar 2026','cash flow periods'),
(6,336,'15 October 2026','board approval date'),
(6,348,'year ended 31 March 2026','note 4 period'),
(6,348,'quarter and six months ended 30 September 2025','note 4 period'),
(6,350,'quarter ended 30 September 2025','interest reversal quarter'),
(6,351,'quarter and year ended 31 March 2026','impairment provision period'),
(6,363,'15 October 2026','signing date'),(7,396,'1 April 2026 to 30 September 2026','year to date review period'),
(8,451,'15 October 2026','auditor report date'),(8,443,'2026.10.15 13:04:00 +05:30','auditor digital signature timestamp'),
(1,54,'2026.10.15 14:59:25 +05:30','CS digital signature timestamp'),
(10,543,'30.09.2026, 30.06.2026, 30.09.2025, 31.03.2026','consolidated segment column period ends'),
(11,596,'30 September 2026; 31 March 2026','consolidated balance sheet dates'),
(13,777,'16 June 2025','effective date of control of Heritage Novandie Foods Limited'),
(13,762,'15 October 2026','board approval date, consolidated'),
(14,821,'1 April 2026 to 30 September 2026','consolidated YTD review period'),
(15,883,'2026.10.15 13:05:27 +05:30','auditor digital signature timestamp'),
(15,892,'15 October 2026','consolidated auditor report date'),
]:
    add(pg,ln,D,v,c)
for pg,ln,v,c,*f in [
(1,37,'Un-Audited Financial Results (Standalone & Consolidated) as per Ind-AS','results are unaudited'),
(2,70,'(Amount in millions of Rs unless otherwise stated) - text garbled','standalone P&L unit statement','OCR_NOISE'),
(2,75,'(Unaudited)/(Audited) column status labels - text garbled','FY 31.03.2026 column Audited, others Unaudited','OCR_NOISE'),
(2,116,'*EPES is not annualised for the quarter (text garbled)','EPS qualifier, standalone; asterisk on EPS row 115','OCR_NOISE'),
(2,115,'asterisk marker on Basic and Diluted EPES row','EPS marker paired to line 116'),
(2,95,'Exceptional items [refer note 4]','exceptional items pointer to note 4'),
(3,129,'(Amount in millions of Rs unless otherwise stated) - text garbled','standalone segment unit statement','OCR_NOISE'),
(3,134,'(Unaudited)/(Audited) column status labels','standalone segment column status'),
(4,177,'(Amount in millions of Rs unless otherwise stated) - text garbled','standalone balance sheet unit statement','OCR_NOISE'),
(4,180,'(Unaudited) 30 Sep 2026 / (Audited) 31 March 2026 - garbled','balance sheet column status','OCR_NOISE'),
(5,253,'(All amounts in Rs millions, except share data and where otherwise stated)','cash flow unit statement'),
(5,256,'(Unaudited)/(Audited) column status labels - garbled','cash flow column status','OCR_NOISE'),
(5,315,'Note 1: Cash and cash equivalents include: cash on hand; balances with banks in current accounts','cash flow note 1'),
(6,336,'Note 1: results reviewed by Audit Committee and approved by Board on 15 October 2026','standalone note 1'),
(6,339,'Note 2: prepared under Ind AS 34 and Regulation 33 SEBI LODR (as amended)','standalone note 2'),
(6,344,'Note 3: segments per Ind AS 108; CODM identified Dairy and renewable energy as reportable segments','standalone note 3'),
(6,348,'Note 4a: exceptional items FY26 include Rs 69.33 million (incl Rs 61.54 million for quarter/6M ended 30 Sep 2025) GST refund on flavoured milk classification; Rs 32.02 million reversed from accrued interest liability','standalone note 4a'),
(6,351,'Note 4b: exceptional item for quarter and year ended 31 March 2026 includes Rs 5.37 million impairment provision on investment in Heritage Novandie Foods Limited','standalone note 4b'),
(7,411,'Review (SRE 2410) is substantially less in scope than an audit; no audit opinion expressed','auditor review scope limitation, standalone'),
(8,427,'Nothing has come to attention that statement contains material misstatement (unmodified conclusion)','standalone review conclusion'),
(9,466,'(Amount in millions of Rs unless otherwise stated) - text garbled','consolidated P&L unit statement','OCR_NOISE'),
(9,471,'(Unaudited)/(Audited) column status labels - garbled','consolidated P&L column status','OCR_NOISE'),
(9,522,'*EPES is not annualised for the quarter (text garbled)','EPS qualifier, consolidated','OCR_NOISE'),
(9,521,'asterisk marker on Basic and Diluted EPES row','EPS marker paired to line 522'),
(9,493,'Exceptional items (refer note 4)','exceptional items pointer to note 4, consolidated'),
(10,541,'(Amount in millions of Rs unless otherwise stated) - text garbled','consolidated segment unit statement','OCR_NOISE'),
(10,545,'(Unaudited)/(Audited) column status labels - garbled','consolidated segment column status','OCR_NOISE'),
(11,594,'(Amount in millions of Rs unless otherwise stated)','consolidated balance sheet unit statement'),
(11,597,'(Unaudited) 30 Sep 2026 / (Audited) 31 March 2026 - garbled','consolidated BS column status','OCR_NOISE'),
(12,674,'(Amount in millions of Rs unless otherwise stated) - text garbled','consolidated cash flow unit statement','OCR_NOISE'),
(12,677,'(Unaudited)/(Audited) column status labels - garbled','consolidated CF column status','OCR_NOISE'),
(12,736,'Note 1: Cash and cash equivalents includes: cash on hand; balances with banks in current accounts; deposits with original maturity up to 3 months','consolidated CF note 1'),
(13,761,'Note 1: consolidated results reviewed by Audit Committee and approved by Board on 15 October 2026','consolidated note 1'),
(13,764,'Note 2: prepared under Ind AS 34 and Regulation 33 SEBI LODR (as amended)','consolidated note 2'),
(13,769,'Note 3: Ind AS 108 segments; CODM identified Dairy, Renewable energy and Feed as reportable segments','consolidated note 3'),
(13,773,'Note 4: exceptional items FY26 include Rs 69.33 million (incl Rs 61.54 million for quarter/6M ended 30 Sep 2025) GST refund on flavoured milk; Rs 32.02 million interest accrual reversed','consolidated note 4'),
(13,777,'Note 5: effective 16 June 2025 Group acquired controlling interest in Heritage Novandie Foods Limited, previously a joint venture','consolidated note 5'),
(14,836,'Review (SRE 2410) is substantially less in scope than an audit; no audit opinion expressed','auditor review scope limitation, consolidated'),
(14,843,'Procedures also performed per SEBI circular under Regulation 33(8) to the extent applicable','consolidated review extra procedures'),
(15,854,'Nothing has come to attention that statement contains material misstatement (unmodified conclusion)','consolidated review conclusion'),
(15,862,'Statement includes interim results of one subsidiary not reviewed by its auditors; furnished by management','unreviewed subsidiary emphasis'),
(15,870,'Management states unreviewed subsidiary results are not material to the Group','materiality statement'),
(15,873,'Conclusion not modified in respect of this matter','unreviewed subsidiary non-modification'),
(16,905,'List of entities included in the Statement (Annexure 1): subsidiaries and associate','consolidation list scope'),
(2,88,'Depreciation/impairment rows split across lines 87-90 in text layer; column alignment unresolved','layout break in text layer','OCR_NOISE'),
(2,66,'Pages 2-6 and 9-13 carry a low-fidelity OCR text layer; characters in numbers may be misread (flagged OCR_NOISE where detected); undetected misreads possible','extraction-fidelity caveat from A1','OCR_NOISE'),
]:
    add(pg,ln,Q,v,c,f[0] if f else '')
for t,_ in out: cnt[t]+=1
hdr=['# A1 STRUCTURED EXTRACTION: Heritage Foods Limited (HERITGFOOD) results Q2 FY27',
'source fulltext: runs/heritgfood-q2fy27/extracted/heritgfood-results-q2fy27-fulltext.md (line numbers refer to that file)',
'unit: Rs millions; factor to Rs Crores x0.1 (values NOT converted)',
'ROW ID range: R001-R%03d'%n,
'counts: NUMBER %d | ENTITY %d | FORWARD %d | DATE %d | QUALIFIER %d'%(cnt['NUMBER'],cnt['ENTITY'],cnt['FORWARD'],cnt['DATE'],cnt['QUALIFIER']),
'NOTES: Statement-table NUMBER rows were generated mechanically from fulltext table lines, one row per (line item x column period). Flags: OCR_NOISE = value contains non-numeric characters from the OCR text layer; COLUMN_MISMATCH = value count on the line did not match column count, so period is UNMAPPED and downstream must read the fulltext line; ZERO_STANDING = dash value. Label text for noisy lines is verbatim from the text layer.',
'FORWARD table: no forward-looking statements found in this document (filing contains none).','']
body=[]
for t in ['NUMBER','ENTITY','FORWARD','DATE','QUALIFIER']:
    body.append('## %s TABLE (%d rows)'%(t,cnt[t]))
    if t=='FORWARD': body.append('(none)')
    body+= [r for tt,r in out if tt==t]
    body.append('')
open('extracted/heritgfood-results-q2fy27-structured.md','w',encoding='utf-8').write('\n'.join(hdr+body)+'\n')
print(n,cnt)
