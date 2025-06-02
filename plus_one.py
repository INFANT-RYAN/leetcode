lst = [1,9]
res =[]
string = ""
for i in lst:
    string+=str(i)
num = int(string)+1
resstr=str(num)
for i in resstr:
    res.append(int(i))
print(res)
