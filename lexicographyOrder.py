n = int(input("Num "))
lst = []
stlst = []
res = []
for i in range(1,n+1):
    lst.append(i)

for i in lst:
    stlst.append(str(i))
lst = sorted(stlst)

for i in lst:
    res.append(int(i))
    
print(res)