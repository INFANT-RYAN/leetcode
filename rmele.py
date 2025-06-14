
nums = [3,2,2,3]
val = 3
res =[]
temp =[]
for i in nums:
    if i != val:
        res.append(i)
    else:
        temp.append("")
print(res)
print(len(res))