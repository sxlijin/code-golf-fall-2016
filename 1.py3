import time as t
p=[]
x=[]
for f in range(2,int(t.strftime('%Y'))):
    if 0 not in (f%n for n in p):
        p.append(f)
        if str(f) == str(f)[::-1]: x.append(f)

print(x)
