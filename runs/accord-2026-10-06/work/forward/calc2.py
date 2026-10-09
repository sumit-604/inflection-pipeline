import json
m=json.load(open('model.json'))
CMP=85.2; MC=175.0; D=8.83; CASH=22.33; IPO=20.40; SH=2.1073289
EVa=MC+D-CASH; EVb=MC+D-(CASH-IPO)
print('EVa',EVa,'EVb',EVb)
for sc in ['bear','base','bull']:
    for y in ['FY27','FY28']:
        r=m[sc][y]
        print(f"{sc} {y}: EPS {r['eps']:.2f} PE {CMP/r['eps']:.1f} Mcap/EBIT {MC/r['ebit']:.1f} EVa/EBIT {EVa/r['ebit']:.1f} EVb/EBIT {EVb/r['ebit']:.1f}")
# trailing FY26
ebit26=(694.61-62.60)/100; print('FY26 core EBIT',ebit26,'EVa/EBIT',EVa/ebit26,'EVb',EVb/ebit26,'Mcap/EBIT',MC/ebit26,'PE core',CMP/(4.3175/SH))
# Section B H1 decomposition
rev=52.68
for gm in [0.206,0.22,0.23,0.241,0.258]:
    for fx in [5.03,5.24,5.53]:
        e=rev*gm-fx; pbt=e-0.335-0.226; print(f"GM {gm*100:.1f} fixed {fx}: EBITDA {e:.2f} ({e/rev*100:.1f}%) corePBT {pbt:.2f} corePAT {pbt*0.7483:.2f}")
# valuation
base=m['base']; bear=m['bear']; bull=m['bull']
for H in [12.95,14.80,14.95,16.65,16.80,18.65,13.91]:
    ex=H*base['FY31']['eps']; print(f"H {H}: exitFV {ex:.1f} entry25 {ex/1.953125:.1f} entry30 {ex/2.197:.1f} FVtoday {H*base['FY28']['eps']:.1f} exitFY30 {H*base['FY30']['eps']:.1f}->{H*base['FY30']['eps']/1.953125:.1f} bearExit {H*bear['FY31']['eps']:.1f} bullExit {H*bull['FY31']['eps']:.1f}")
H=16.80
b,e,u=H*bear['FY31']['eps'],H*base['FY31']['eps'],H*bull['FY31']['eps']
for n,v in [('bear',b),('base',e),('bull',u)]: print(n,'CAGR from CMP',((v/CMP)**(1/3)-1)*100)
for w in [(0.35,0.45,0.20),(0.45,0.40,0.15)]:
    wf=w[0]*b+w[1]*e+w[2]*u; wc=sum(wi*((v/CMP)**(1/3)-1) for wi,v in zip(w,[b,e,u]))
    print('weights',w,'wFV',wf,'CAGR on wFV',((wf/CMP)**(1/3)-1)*100,'weighted CAGR',wc*100)
print('disp',(u-b)/e, 'FV CAGR',((base['FY31']['eps']/base['FY28']['eps'])**(1/3)-1)*100)
pe=CMP/base['FY28']['eps']; g=(base['FY31']['eps']/base['FY28']['eps'])**(1/3)-1
print('HR base',(1+g)**3*(H/pe),'HR bull(C/D)',(1+g+0.05)**3*(H/pe), 'curPE',pe)
print('upside/downside',(e-CMP)/(CMP-b))
# T1/T2
t1=H*(4.3175/SH); t2=H*(base['FY28']['eps']-4.3175/SH); print('T1',t1,t1/CMP,'T2',t2,t2/CMP,'resid',1-(t1+t2)/CMP)
print('lot value',3000*CMP/1e5,'lakh; portfolio for 2%:',3000*CMP/0.02/1e7,'Cr')
print('ESOP intrinsic Cr',(CMP-10)*5e5/1e7, 'per yr over3', (CMP-10)*5e5/1e7/3, 'EPS hit FY28', (CMP-10)*5e5/1e7/3*0.7483/SH)
