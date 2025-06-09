n = int(input("num of ele :"))
pos = int(input("pos(k) :"))

arr = []
res = []

for i in range(1,n+1):
    arr.append(str(i))

arr.sort()

for i in arr:
    res.append(int(i))
        

print(res[pos-1])

