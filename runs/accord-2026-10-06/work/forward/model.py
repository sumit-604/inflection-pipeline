SH=2.0573289+0.05   # diluted Cr shares
TAX=0.7483
yrs=['FY27','FY28','FY29','FY30','FY31']
def run(name,rev,gm,fixed,margin_override,da,intr):
    print('\n==',name)
    out={}
    for i,y in enumerate(yrs):
        r=rev[i]
        if margin_override is not None:
            e=r*margin_override[i]; g=None
        else:
            g=r*gm[i]; e=g-fixed[i]
        ebit=e-da[i]; pbt=ebit-intr[i]; pat=pbt*TAX; eps=pat/SH
        out[y]=dict(rev=r,ebitda=e,m=e/r,ebit=ebit,pbt=pbt,pat=pat,eps=eps,gp=g)
        print(f"{y}: rev {r:7.2f} GP {g if g is None else round(g,2)} EBITDA {e:6.2f} ({e/r*100:5.2f}%) D&A {da[i]:.2f} EBIT {ebit:6.2f} int {intr[i]:.2f} PBT {pbt:6.2f} PAT {pat:6.2f} EPS {eps:6.2f}")
    return out
# BASE
rb=[52.68+53.80]
for g in [0.076]*4: rb.append(rb[-1]*(1+g))
fx=[10.05*1.042]
for _ in range(4): fx.append(fx[-1]*1.08)
da_b=[0.67,0.82,1.29,1.39,1.49]
base=run('BASE',rb,[0.23]*5,fx,None,da_b,[0.55]*5)
print('fixed',[round(x,2) for x in fx])
# BEAR
rr=[52.68+42.35,101.6,101.6,101.6*1.076,101.6*1.076**2]
da_r=[0.67,0.67,0.82,1.29,1.39]
bear=run('BEAR',rr,None,None,[0.0886]*5,da_r,[0.59]*5)
# BULL
ru=[52.68+53.80+20.12, 900.36*0.90*16.69/100]
for _ in range(3): ru.append(ru[-1]*1.30)
fxu=[fx[0],fx[1]]
ratio=fx[1]/ru[1]
for i in range(2,5): fxu.append(ru[i]*ratio)
bull=run('BULL',ru,[0.241]*5,fxu,None,da_b,[0.55]*5)
print('bull fixed',[round(x,2) for x in fxu])
# FY26 core
pbt26=605.75-28.78; print('\nFY26 core PBT lakh',pbt26,'core PAT Cr',pbt26*TAX/100,'core EPS (2.0573)',pbt26*TAX/100/2.0573289)
import json; json.dump(dict(base=base,bear=bear,bull=bull),open('model.json','w'),indent=1)
# CAGRs
for n,s in [('base',rb),('bear',rr),('bull',ru)]:
    print(n,'rev CAGR FY26-28',((s[1]/70.07)**0.5-1)*100,'FY26-29',((s[2]/70.07)**(1/3)-1)*100)
for n,d in [('base',base),('bear',bear),('bull',bull)]:
    print(n,'PAT CAGR FY26-29',((d['FY29']['pat']/4.317)**(1/3)-1)*100, 'EPS FY28->FY31 CAGR',((d['FY31']['eps']/d['FY28']['eps'])**(1/3)-1)*100)
