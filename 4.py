import requests as r
x=r.get('http://www.xfront.com/us_states/')
for y,_ in sorted([(f[2].strip()[14:-4],f[3].strip()[18:-4]) for f in [f.split('<p>') for f in (x.text.split('<li>'))[3:]]],key=lambda x:float(x[1])): print(y)
