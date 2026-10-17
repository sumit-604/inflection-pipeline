import sys
rows=[]  # (type,page,line,value,ctx,flag)
def add(t,p,l,v,c,f=""): rows.append((t,p,l,v,c,f))
P=["Q2FY27","Q1FY27","Q2FY26","H1FY27","H1FY26","FY26"]
def pl(p,l,name,vals,flags=None):
    for i,v in enumerate(vals):
        if v is None: continue
        f=""
        if v in("-","0"): f="ZERO_STANDING"
        if flags and i in flags: f=(f+" "+flags[i]).strip()
        add("NUMBER",p,l,v,f"{name}, {P[i]}",f)
pl(2,75,"Revenue from Operations (Inclusive of GST)",["11,506","10,006.00","8,317.00","21,512","15,761","33,890.00"])
pl(2,76,"Other Operating Income",["112","59.00","96,00","171","149","236.00"],{2:"OCR_AS_READ"})
pl(2,77,"TOTAL INCOME",["11,618","10,065","8,413","21,683","15,910","34,126"])
pl(2,80,"Cost of materials consumed",["6,843","4,961","4,167","11,804","8,291","17,351"])
pl(2,81,"Purchases of stock-in-trade",["217","704","215","921","394","1,575"])
pl(2,82,"Change in inventories of FG, WIP, stock-in-trade",["(78)","143","173","65","(78)","(304)"])
pl(2,83,"Employee benefits expense",["888","820","775","1,708","1,499","3,044"])
pl(2,84,"Finance Costs",["24","20","13","37","81"][0:3]+["OCR_UNREADABLE"]+["37","81"][0:0]+[],{})
