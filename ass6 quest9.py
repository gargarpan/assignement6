ip=[1,2,'a','b',2.4,7.8]
print(ip)
q=[]
w=[]
e=[]
for x in ip:
    if type(x)==int:
        q.append(x)
    elif type(x)==float:
        w.append(x)
    elif type(x)==str:
        e.append(x)

print(q)
print(w)
print(e)
