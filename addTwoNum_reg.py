l1 = [9]
l2=[1,3]
lst1 = ""
lst2 = ""
res =[]
for i in l1:
    lst1+=str(i)
for i in l2:
    lst2+=str(i)
num1 = int(lst1)
num2 = int(lst2)
tot = num1+num2
temp = str(tot)
for i in temp:
    res.append(int(i))
print(res)