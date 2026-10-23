exec(open('gen.py').read())
seen=set()
for r in num:
    k=(r[0],r[1])
    if r[0] in (7,10,11,13) and k not in seen:
        seen.add(k); print(r[1],r[2],'|',r[3][:95])
print(len(num))
